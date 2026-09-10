# GeoPackage → SensorThings API (STA 2.0) transformation

Converts the [SoilWise GeoPackage](https://github.com/soilwise-he/Geopackage-so) into a
[SensorThings API](https://www.ogc.org/standards/sensorthings/) 2.0 batch request, ready
to POST to a [FROST server's](https://github.com/FraunhoferIOSB/FROST-Server)
[`$batch`](https://fraunhoferiosb.github.io/FROST-Server/extensions/JsonBatchRequest.html)
endpoint. [FROST Server docs](https://fraunhoferiosb.github.io/FROST-Server/) if you need
a server to test against or want the full API reference.

The transformation is built as a [hale Studio](https://github.com/halestudio/hale) project. Two
small Python scripts handle the parts hale's stock JSON writer cannot do on its own (see
[Known limitations](#known-limitations)).

## Pipeline

```
GeoPackage --[hale transform]--> flat JSON array --[assemble_batch.py]--> FROST $batch file --[upload_batch.py]--> FROST server
```

1. **hale transform**: runs the alignment (`SoilWise-gpkg-to-STA.halex`) against a source
   GeoPackage, producing one flat, ordered JSON array of STA request envelopes (one per
   entity to create).
2. **`assemble_batch.py`**: post-processes that array. It reprojects each Feature's geometry
   from the GeoPackage's native CRS (EPSG:3035) to WGS84 (EPSG:4326) as required by
   GeoJSON, and wraps the array in the `{"requests": [...]}` envelope FROST's `$batch`
   endpoint expects.
3. **`upload_batch.py`** *(optional)*: uploads the assembled batch to a live FROST server
   via its [JSON Batch Request](https://fraunhoferiosb.github.io/FROST-Server/extensions/JsonBatchRequest.html)
   extension, in dependency order and in manageable chunks, rewriting the batch-internal
   `"$<id>"` placeholder references into the real server-assigned `@iot.id`s as it goes.

## Prerequisites

- [hale Studio](https://github.com/halestudio/hale) / [hale CLI](https://github.com/halestudio/hale-cli) 6.2.1 or later (the CLI is
  sufficient; no GUI needed to run the pipeline)
- Python 3 with `shapely` and `pyproj` installed (`pip install shapely pyproj`), only
  needed for `assemble_batch.py`'s geometry reprojection step
- A populated GeoPackage to actually transform. The alignment was authored and tested
  against the schema published in
  [soilwise-he/Geopackage-so](https://github.com/soilwise-he/Geopackage-so)
  (`geopackage/SoilWise_with_data/SoilWise.gpkg` for real content,
  `geopackage/SoilWise_empty/SoilWise.gpkg` for structure only); a mismatched schema
  version may need re-mapping.

## Usage

```bash
# 1. Transform the GeoPackage to a flat JSON array
hale transform -project SoilWise-gpkg-to-STA.halex \
  -source path/to/your/SoilWise.gpkg \
  -target out.json -providerId eu.esdihumboldt.hale.io.json.writer -trustGroovy

# 2. Assemble the FROST batch file
python assemble_batch.py out.json batch.json

# 3. (optional) Upload to a FROST server
#    Set FROST_USER / FROST_PASS as environment variables first if the server requires auth.
python upload_batch.py batch.json https://your-frost-server/v2.0
```

`upload_batch.py` also accepts an optional `max-per-type` argument to cap how many
requests per entity type are uploaded, useful for a smaller test/demo load instead of the
full dataset.

## What's mapped

All INSPIRE Soil feature types present in the GeoPackage are mapped to STA `Feature` +
shared `FeatureType` entities (SoilSite, SoilProfile, ProfileElement, SoilDerivedObject,
SoilBody), each carrying its full geometry (including SoilBody's multi-part geometries,
combined into one `MultiPolygon` per body). The observational side
(ObservedProperty, Sensor, ObservingProcedure, Thing, Datastream, Observation) is mapped
in full, including SWE Common's per-type `resultType` handling (Quantity/Category/etc.)
and unit-of-measure resolution.

Non-observational/qualitative content nested under SoilProfile and ProfileElement (WRB
qualifiers, FAO horizon notation, and the `isderivedfrom` provenance relation) is carried
through as structured nested arrays/objects in `properties`, in the
`{source_table, related_source_table, records:[...]}` shape.

## Provisional modelling decisions

The following are working decisions made to unblock the transformation, **not final,
agreed answers**. They're built and functioning, but each has open alternatives that
were considered and not resolved.

- **`Thing` = one synthetic Thing per SoilSite** (`thing-<soilsite.guid>`). Two other
  options are on the table and unresolved: modelling `Thing` as the laboratory instead
  (the GeoPackage's own original convention), or a dual model where the site and each
  laboratory are separate, cross-linked Things.
- **Proximate FoI = ProfileElement, Ultimate FoI = SoilSite.** At least three different
  proposals for this mapping have been discussed (involving specimens/samples, the
  profile-as-integrity-sample vs. profile-element-as-subsample framing, and a proposed
  "representative profile" concept to bind repeated yearly digs at one site into a
  pseudo time series) without landing on one. What's built is the simplest option that
  works with the data as it exists today (no sample/specimen data yet).
- **Sensor.encodingType / metadata are left null.** STA 2.0 marks both mandatory; FROST
  itself accepts the nulls.
- **Broken-chain rows are silently skipped, not explicitly handled.** See the first
  point under Known limitations below. No decision has been made yet on the "right" way
  to handle them (fix at source, skip with an explicit flag, placeholder, inherit from a
  parent feature, or isolate them in their own atomicity group).

## Known limitations

- **Rows with a broken plot-chain link** (a soilprofile/profileelement with no resolvable
  path back to a plot geometry) still produce a Feature, just without a `feature`
  geometry. The Datastreams that depend on those rows for their `Thing`/FoI currently get
  silently skipped by `upload_batch.py` (not sent to FROST at all) rather than erroring.
- **`Sensors[]` on ObservingProcedure and `other_horizons` on ProfileElement** are not
  built. The source GeoPackage tables backing them (`obsprocedure_sensor`,
  `otherhorizon_profileelement`) are currently empty in available test data.
- **`othersoilnametype`** is not mapped. No foreign key back to `soilprofile` currently
  exists in the GeoPackage schema for this table.
- hale's stock JSON writer cannot emit a `{"requests": [...]}` root wrapper, nor write a
  nested geometry property already reprojected. `assemble_batch.py`'s two responsibilities
  above are a stand-in for these until (if) hale ships writer extensions for them.
