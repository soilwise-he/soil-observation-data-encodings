# A real-world soil observation dataset with geodata, IDs, attributes and observed properties

This example is based on a real-world dataset of soil bulk density measurements collected across land-use types in Lao PDR (Attapeu and Khammouane provinces, 2024–2025).

It demonstrates a more complete and realistic case with:

- **Geodata** — latitude, longitude and elevation per sample point (WGS84, decimal degrees / metres)
- **Multiple IDs** — a composite `sample_name` plus separate component identifiers (`ID_field`, `ID_profile`, `ID_depth`, `ID_location`) 
- **Categorical attributes** — `landuse`, `location`, `country`
- **Observed properties with Units of Measure (UoM)** — `depth`, `volum_cylinder_cm3`, `wet_mass_soil_g`, `dry_mass_soil_g`, `bulk_density`, `water_content` each linked to a QUDT unit URI and a quantity kind
- **Procedures** — observed properties reference named laboratory methods
- **Phenomenon time** — `collection_date` 

## Column metadata

Column-level metadata is provided in [laos_soil_bulk_density_attapeu_khammouane_2024-2025_v1.csv_metadata.csv](laos_soil_bulk_density_attapeu_khammouane_2024-2025_v1.csv_metadata.csv), 


## MCF YAML

The result of annotating this dataset is a [OGC API Records / pygeometa MCF](https://geopython.github.io/pygeometa/) YAML file:

[laos_soil_bulk_density_attapeu_khammouane_2024-2025_v1.csv.mcf.yml](laos_soil_bulk_density_attapeu_khammouane_2024-2025_v1.csv.mcf.yml)




