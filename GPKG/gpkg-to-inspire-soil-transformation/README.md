# GeoPackage → INSPIRE Soil (so 4.0) transformation

A [hale Studio](https://github.com/halestudio/hale) project that converts the
[SoilWise GeoPackage](https://github.com/soilwise-he/Geopackage-so) into an
[INSPIRE Soil](https://inspire-mif.github.io/technical-guidelines/data/so/) GML dataset
(`so` 4.0.2, [schema](https://inspire.ec.europa.eu/schemas/so/4.0/Soil.xsd)).

## Usage

Requires [hale Studio](https://github.com/halestudio/hale) or the
[hale CLI](https://github.com/halestudio/hale-cli) 6.4.1+, and network access on first
open to fetch the INSPIRE schemas.

```bash
cd transformation
hale transform -project SoilWise-GeoPackage-to-INSPIRE-Soil.halex \
  -source path/to/SoilWise.gpkg -target SoilWise-INSPIRE-Soil.gml \
  -preset INSPIRE-Soil-GML -reportsOut reports.xml
```

The `INSPIRE-Soil-GML` preset holds the writer settings; set the same in the GUI export
wizard:

- `crs.epsg.prefix` = `http://www.opengis.net/def/crs/EPSG/0/`
- `geometry.unifyWindingOrder` = `clockwise` (correct: the alignment swaps the axes into
  EPSG:3035 northing/easting order, which reverses ring orientation)
- `xml.notNil.omitNilReason` = `true`
- `xml.pretty` = `true` (indented output)

**Check the hale report after each run.** Data the transformation changes or leaves out
is reported as a *warning*. A mandatory INSPIRE element with no value in the source, or
an unexpected `isderived` / `profileelementtype` value, is reported as an *error*: the
feature is still written, but is not INSPIRE-conformant until the source is fixed. For
the SoilWise GeoPackage (`SoilWise_with_data`, 2026-10-07), expect 0 errors and 47 warnings (47
`derivedProfilePercentageRange` values above 100 %).

Project variables (in the `.halex`, editable in hale Studio):

- `INSPIRE_NAMESPACE` (default `https://soilwise-he.eu/`) is used only for rows without an
  `inspireid_namespace`.
- `INSPIRE_PARAMETER_NAMES` (default `false`): see *observed properties* below.

## What's mapped

| INSPIRE type | from |
|---|---|
| `SoilSite` | `soilsite` |
| `SoilPlot` | `soilplot` |
| `ObservedSoilProfile` / `DerivedSoilProfile` | `soilprofile`, by `isderived` (0 / 1) |
| `SoilHorizon` / `SoilLayer` | `profileelement`, by `profileelementtype` (0 / 1) |
| `SoilBody` | `soilbody` + `soilbody_geom` (one `MultiSurface` per body) |
| `SoilDerivedObject` | `soilderivedobject` |

- Associations are written in both directions, and nested types (WRB name and qualifiers,
  FAO notation, other soil names / horizon notations, depth ranges, derived profile
  presence) are built in full.
- Observations become inline `om:OM_Observation` on the site, profile, profile element or
  derived object they belong to. Units are the UCUM codes from the GeoPackage (e.g.
  `[pH]`); `Count` results get `uom="1"`.
- **Observed properties** keep the URI of the external vocabulary as stored in the
  GeoPackage (GLOSIS / SOILVOC), also where an INSPIRE equivalent exists. Total vs.
  extractable contents are distinguished by the observation's procedure. The INSPIRE
  Soil model expects values from its own `…ParameterNameValue` code lists (a manual check
  in the INSPIRE validator); if a reviewer requires them, set `INSPIRE_PARAMETER_NAMES`
  to `true`, which maps `pH`, `Carorg` and `Nittot` to `pHValue`, `organicCarbonContent`
  and `nitrogenContent`.
- **Transitional horizons:** `FAOHorizonMaster` allows one symbol, so it carries
  `faohorizonmaster_1`; the full notation with both master symbols goes into
  `gml:description`, e.g. *"Transitional horizon AC (FAO master symbols A and C)"*.
- **Texture** (sand, silt, clay) becomes `particleSizeFraction`: content in %, size range
  in µm from the GLOSIS code descriptions. A fraction measured more than once on the same
  element stays an observation, as `particleSizeFraction` has no date or method.
- Properties with no source data are voided (`xsi:nil` + `nilReason`).
