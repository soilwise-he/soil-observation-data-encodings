#!/usr/bin/env python3
"""Post-process hale's JSON output into a FROST JSON batch request.

hale (per-type target architecture) already emits a FLAT, reference-safe-ordered
array of STA request envelopes. This script:

  1. (interim) injects the `body.feature` geometry as a GeoJSON object, reprojected
     to EPSG:4326, from the `body.properties.geometry_3035` WKT that hale DOES emit.
     hale cannot currently write a nested geometry property as GeoJSON itself
     (see hale-dev-extension-proposals.md, Extension A) — remove this step once
     that writer extension lands.
  2. strips the doc-only `comment` field.
  3. wraps everything as {"requests": [...]}  (FROST $batch envelope; hale cannot
     add a root wrapper — Extension B).

Back-compat: also accepts the older single-`StaTarget`-wrapper form (one wrapper
object per source row) and flattens it in reference-safe order.

Usage: python assemble_batch.py <hale-export.json> <out-batch.json>
Requires: pyproj, shapely (only for the geometry injection).
"""
import json
import sys

ORDER = [
    "FeatureType", "ObservedProperty", "Sensor", "ObservingProcedure",
    "Thing", "Location", "Feature", "Datastream", "Observation",
]

# --- geometry reprojection (interim, until hale Extension A) ---
_transformers = {}


def _reproject_wkt_to_geojson(wkt_text, src_srs):
    """WKT in src_srs -> GeoJSON geometry dict in EPSG:4326 (lon/lat). None on failure."""
    try:
        from shapely import wkt as shapely_wkt
        from shapely.geometry import mapping
        from shapely.ops import transform as shapely_transform
        from pyproj import Transformer
    except ImportError as e:
        print(f"WARNING: geometry injection skipped, missing lib: {e}", file=sys.stderr)
        return None
    src = (src_srs or "EPSG:3035").replace("urn:ogc:def:crs:", "").strip()
    if ":" not in src:
        src = "EPSG:" + src
    try:
        tr = _transformers.get(src)
        if tr is None:
            tr = Transformer.from_crs(src, "EPSG:4326", always_xy=True)
            _transformers[src] = tr
        geom = shapely_wkt.loads(wkt_text)
        geom4326 = shapely_transform(tr.transform, geom)
        gj = mapping(geom4326)
        # mapping() yields tuples; json handles them, but normalise to lists
        return json.loads(json.dumps(gj))
    except Exception as e:  # noqa: BLE001 - provenance is best-effort
        print(f"WARNING: could not reproject geometry ({e})", file=sys.stderr)
        return None


def _reproject_geojson(gj, src_srs):
    """Reproject a GeoJSON geometry dict from src_srs to EPSG:4326 (lon/lat), in place."""
    try:
        from shapely.geometry import shape, mapping
        from shapely.ops import transform as shapely_transform
        from pyproj import Transformer
    except ImportError as e:
        print(f"WARNING: geometry reprojection skipped, missing lib: {e}", file=sys.stderr)
        return gj
    src = (src_srs or "EPSG:3035").replace("urn:ogc:def:crs:", "").strip()
    if ":" not in src:
        src = "EPSG:" + src
    if src.upper() in ("EPSG:4326", "4326"):
        return gj
    try:
        tr = _transformers.get(src)
        if tr is None:
            tr = Transformer.from_crs(src, "EPSG:4326", always_xy=True)
            _transformers[src] = tr
        geom = shape(gj)
        return json.loads(json.dumps(mapping(shapely_transform(tr.transform, geom))))
    except Exception as e:  # noqa: BLE001
        print(f"WARNING: could not reproject feature geometry ({e})", file=sys.stderr)
        return gj


def _inject_feature_geometry(req):
    """hale emits `feature` as full GeoJSON in NATIVE CRS (via rename); reproject it
    to EPSG:4326 here. Falls back to building from geometry_3035 WKT if `feature`
    is absent (e.g. a geometry-less row)."""
    if req.get("url") != "Features":
        return
    body = req.get("body") or {}
    props = body.get("properties") or {}
    feat = body.get("feature")
    if isinstance(feat, dict) and feat.get("coordinates") is not None:
        body["feature"] = _reproject_geojson(feat, props.get("srs"))
        return
    wkt_text = props.get("geometry_3035")
    if wkt_text:
        gj = _reproject_wkt_to_geojson(wkt_text, props.get("srs"))
        if gj is not None:
            body["feature"] = gj


def _clean(req):
    req = {k: v for k, v in req.items() if k != "comment"}
    _inject_feature_geometry(req)
    return req


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    data = json.load(open(sys.argv[1], encoding="utf-8"))

    if isinstance(data, list) and data and isinstance(data[0], dict) and "url" in data[0]:
        # current form: flat, already-ordered array of request envelopes
        requests = [_clean(r) for r in data]
    else:
        # legacy form: one/more StaTarget wrappers with 9 entity arrays -> flatten + order
        wrappers = data if isinstance(data, list) else [data]
        buckets = {k: [] for k in ORDER}
        for w in wrappers:
            if not isinstance(w, dict):
                continue
            for key, envs in w.items():
                if key in buckets:
                    buckets[key].extend(_clean(e) for e in (envs or []))
        requests = [r for key in ORDER for r in buckets[key]]

    json.dump({"requests": requests}, open(sys.argv[2], "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    feats = sum(1 for r in requests if r.get("url") == "Features")
    withgeom = sum(1 for r in requests
                   if r.get("url") == "Features"
                   and isinstance((r.get("body") or {}).get("feature"), dict))
    print(f"{len(requests)} requests written to {sys.argv[2]} "
          f"({withgeom}/{feats} Features have GeoJSON geometry)")


if __name__ == "__main__":
    main()
