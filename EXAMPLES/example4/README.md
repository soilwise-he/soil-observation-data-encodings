# A real-world soil observation dataset with geodata, IDs, attributes and observed properties

| Metadata | |
| --- | --- |
| authors | |
| source  | |
| license | | 

This example is based on a real-world dataset of soil bulk density measurements collected across land-use types in Lao PDR (Attapeu and Khammouane provinces, 2024–2025).

It demonstrates a more complete and realistic case with:

- **Geodata** — `latitude`, `longitude` and `elevation` per sample point (WGS84, decimal degrees / metres)
- **Multiple IDs** — a composite `sample_name` plus separate component identifiers (`ID_field`, `ID_profile`, `ID_depth`, `ID_location`) 
- **Categorical attributes** — `landuse`, `location`, `country`
- **Observed properties with Units of Measure (UoM)** — `depth`, `volum_cylinder_cm3`, `wet_mass_soil_g`, `dry_mass_soil_g`, `bulk_density`, `water_content` each linked to a QUDT unit URI and a quantity kind
- **Procedures** — observed properties reference named laboratory methods
- **Phenomenon time** — `collection_date` 





