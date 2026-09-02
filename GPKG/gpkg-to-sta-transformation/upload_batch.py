#!/usr/bin/env python3
"""Upload an assembled FROST batch ({"requests":[...]}) to a FROST endpoint, robustly.

The batch is a linked graph with within-batch references ({"@id":"$<ref>"}). FROST
can resolve those only inside a single $batch, and a 100k-request batch is too big for
one POST. So we upload in DEPENDENCY ORDER, in chunks, WITHOUT atomicityGroup (partial
success), rewriting each "$<ref>" into a real {"@iot.id": N} using the ids captured from
earlier phases.

Order: ObservedProperties, Sensors, ObservingProcedures, Things, FeatureTypes (deduped),
Features, Datastreams, Observations.

Usage:
    python upload_batch.py <assembled-batch.json> <FROST-base-url> [max-per-type]

  max-per-type (optional): cap requests uploaded per entity type (for a smaller demo
  load). Omit to upload everything.
"""
import json, sys, os, base64, urllib.request, collections

if len(sys.argv) < 3:
    print(__doc__); sys.exit(1)
BATCH = sys.argv[1]
B = sys.argv[2].rstrip("/")
MAXPER = int(sys.argv[3]) if len(sys.argv) > 3 else None
CHUNK = 1000

# Optional HTTP Basic auth from env (FROST_USER / FROST_PASS) — keeps creds out of the repo.
_AUTH = None
if os.environ.get("FROST_USER"):
    tok = base64.b64encode(f"{os.environ['FROST_USER']}:{os.environ.get('FROST_PASS','')}".encode()).decode()
    _AUTH = "Basic " + tok

reqs = json.load(open(BATCH, encoding="utf-8"))["requests"]
realid = {}   # request id (guid / thing-<guid> / ft-<x>) -> numeric @iot.id

# reference fields per entity type (only these are rewritten; geometry is left alone)
REF_FIELDS = {
    "Features": ["FeatureTypes"],
    "ObservingProcedures": ["ObservedProperties", "Sensors"],
    "Datastreams": ["Thing", "Sensor", "ObservedProperties", "ObservingProcedure",
                    "ProximateFeatureOfInterest", "UltimateFeaturesOfInterest"],
    "Observations": ["Datastream"],
}
# refs that must resolve or the request is skipped
MANDATORY = {
    "Datastreams": ["Thing", "Sensor", "ObservedProperties"],
    "Observations": ["Datastream"],
}


def post_batch(rs):
    body = json.dumps({"requests": rs}).encode("utf-8")
    hdr = {"Content-Type": "application/json"}
    if _AUTH:
        hdr["Authorization"] = _AUTH
    r = urllib.request.Request(B + "/$batch", data=body, headers=hdr, method="POST")
    with urllib.request.urlopen(r, timeout=600) as resp:
        return json.loads(resp.read().decode("utf-8")).get("responses", [])


def num_from(loc):
    loc = str(loc or "")
    return int(loc.split("(")[-1].rstrip(")")) if "(" in loc else None


def capture(responses, sent):
    ok = 0
    for x, src in zip(responses, sent):
        if x.get("status", 0) >= 300:
            continue
        ok += 1
        b = x.get("body")
        rid = None
        if isinstance(b, dict):
            if "@iot.id" in b:
                rid = b["@iot.id"]
            else:
                rid = num_from(b.get("@id") or b.get("@iot.selfLink"))
        if rid is None:
            hdrs = x.get("headers") or {}
            rid = num_from(x.get("location") or hdrs.get("Location") or hdrs.get("location"))
        if rid is not None:
            realid[str(src["id"])] = int(rid)
    return ok


def resolve_ref(v, missing):
    """Replace {"@id":"$X"} with {"@iot.id": realid[X]}; drop if X unresolved."""
    if isinstance(v, dict) and isinstance(v.get("@id"), str) and v["@id"].startswith("$"):
        k = v["@id"][1:]
        if k in realid:
            return {"@iot.id": realid[k]}
        missing.append(k)
        return None
    if isinstance(v, list):
        out = [resolve_ref(e, missing) for e in v]
        return [e for e in out if e is not None]
    return v


def upload(url, dedup=False):
    items = [r for r in reqs if r.get("url") == url]
    if dedup:
        seen, uni = set(), []
        for r in items:
            if r["id"] in seen:
                continue
            seen.add(r["id"]); uni.append(r)
        items = uni
    if MAXPER:
        items = items[:MAXPER]

    prepared, skipped = [], 0
    for r in items:
        body = dict(r.get("body") or {})
        missing = []
        for f in REF_FIELDS.get(url, []):
            if f in body:
                rv = resolve_ref(body[f], missing)
                if rv is None or (isinstance(rv, list) and not rv):
                    body.pop(f, None)
                else:
                    body[f] = rv
        # resultType.definition references the ObservedProperty; FROST needs a real
        # selflink (EntityType(id)), not the within-batch "$<guid>" placeholder.
        if url == "Datastreams":
            rt = body.get("resultType")
            if isinstance(rt, dict) and isinstance(rt.get("definition"), str) and rt["definition"].startswith("$"):
                k = rt["definition"][1:]
                if k in realid:
                    rt["definition"] = f"{B}/ObservedProperties({realid[k]})"
                else:
                    rt.pop("definition", None)
        if any(m not in body for m in MANDATORY.get(url, [])):
            skipped += 1
            continue
        r2 = {k: v for k, v in r.items() if k not in ("if", "atomicityGroup")}
        r2["body"] = body
        prepared.append(r2)

    created = 0
    for i in range(0, len(prepared), CHUNK):
        chunk = prepared[i:i + CHUNK]
        resp = post_batch(chunk)
        created += capture(resp, chunk)
        bad = [x for x in resp if x.get("status", 0) >= 400]
        if bad:
            m = bad[0].get("body")
            msg = m.get("message") if isinstance(m, dict) else m
            print(f"  {url} chunk {i//CHUNK+1}: first error {bad[0].get('status')}: {str(msg)[:100]}")
    print(f"{url}: created {created}, skipped {skipped} (unresolved mandatory refs), of {len(items)}")


for u in ["ObservedProperties", "Sensors", "ObservingProcedures"]:
    upload(u)
upload("Things", dedup=True)
upload("FeatureTypes", dedup=True)
upload("Features")
upload("Datastreams")
upload("Observations")
print(f"\nDONE. Endpoint: {B}")
