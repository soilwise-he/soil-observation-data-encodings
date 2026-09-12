## Simple CSV following [Example 4 Laos Dataset](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/EXAMPLES/example4/README.md)

### ReadMe
General information about the dataset
| Concept | Information |
|---|---|
| Project | Soil bulk density dataset across land uses in Lao PDR. |
| Publication | --- |
| Funding | Attapeu data: Agroecology Initiative (CIAT, IWMI)<br>Khammouane data: SOLAO Project (French Embassy in Laos) |
| Citation | Ms Sunee Peecha, Ms Nampheung Sayalath, Ms Florine Degrune: Soil bulk density dataset across land uses in Lao PDR. CIRAD, UMR Eco&Sols, France / IRD, UMR XX, France |
| Contact | florine.degrune@cirad.fr |
| Experiment | --- |
| Site | Attapeu and Khammouane |
| Country | LAO PDR |
| Sampling | Sampling was conducted during different seasons across provinces, which may influence bulk density values.<br>Crop types in garden plots were not recorded.<br>Non-cultivated sites represent nearby uncultivated areas and should not be interpreted as undisturbed natural soils.<br>Bulk density values reflect conditions at the time of sampling only.<br>Measurements represent point samples within each field and depth interval; spatial variability within fields may not be fully captured despite replication. |
| Date | Attapeu Province: January–February 2024 (dry season)<br>Khammouane Province: November 2025 (end of the rainy season) |
| CRS | EPSG:4326 |

## Properties
Description of all properties of the data csv

|name|column_type|column_format|concept|element|element_uri|unit_symbol|unit_uri|quantity_kind_uri|method|description___________________________________________|
|---|---|---|---|---|---|---|---|---|---|---|
|sample_ID|string||Feature of Interest|||||||A unique identifier assigned to each soil sample, constructed to ensure traceability.|
|sample_name|string||Feature of Interest|||||||A unique identifier for each soil sample, combining field number, replicate number, depth interval, and location.|
|ID_field|string||Attribute|||||||Identifier representing the specific field from which the soil sample was collected.|
|ID_profile|string||Attribute|||||||Identifier indicating the within-field replicate number for the soil sample.|
|ID_depth|string||Attribute|||||||Identifier denoting the depth interval from which the soil sample was taken, with A for 0–5 cm and B for 15–20 cm.|
|ID_location|string||Attribute|||||||Identifier representing the administrative location where the soil sample was collected, with ATP for Attapeu and KHA for Khammouane.|
|depth|string||Depth Upper|soil depth|http://w3id.org/glosis/model/common/soilDepthProperty|||||The soil depth interval from the surface over which the soil sample was collected, measured in centimeters.|
|landuse|codelist||Attribute|land use type|Tab-LandCoverTypes|||||The category of land use under which the soil sample was collected, such as rice, cassava, gardens, or non-cultivated.|
|volum_cylinder_cm3|integer||Observed Property|sample volume|https://data.geoscience.earth/ncl/ISO11074v2025/3.409|cm³|http://qudt.org/vocab/unit/CentiM3|http://qudt.org/vocab/quantitykind/Volume|ENVO – soil sampling device (ENVO:00002792)|The volume of the soil sampling cylinder used to collect an undisturbed soil sample, measured in cubic centimeters.|
|wet_mass_soil_g|float||Observed Property|soil water content|http://aims.fao.org/aos/agrovoc/c_7208|g|http://qudt.org/vocab/unit/GM|http://qudt.org/vocab/quantitykind/Mass||The mass of the soil sample immediately after collection, including water content, measured in grams.|
|dry_mass_soil_g|float||Observed Property|soil sample|http://opendata.inrae.fr/thesaurusINRAE/c_17874|g|http://qudt.org/vocab/unit/GM|http://qudt.org/vocab/quantitykind/Mass||The mass of the soil sample after oven-drying at 105 °C until constant weight, representing the dry mass of soil, measured in grams.|
|bulk_density|float||Observed Property|bulk density|https://data.geoscience.earth/ncl/ISO11074v2025/3.62|g/cm³|http://qudt.org/vocab/unit/GM-PER-CentiM3|http://qudt.org/vocab/quantitykind/MassDensity|ENVO – soil bulk density (ENVO:09200004)|The dry mass of soil per unit volume, including pore space, measured using a soil sampling cylinder and expressed in grams per cubic centimeter.|
|water_content|integer||Observed Property|soil water content|http://aims.fao.org/aos/agrovoc/c_7208|g/g|http://qudt.org/vocab/unit/GM-PER-GM|http://qudt.org/vocab/quantitykind/MassRatio|ENVO – soil gravimetric water content|The mass of water in the soil per unit dry mass of soil, expressed as a percentage by weight.|
|collection_date|date|%Y-%m|Phenomenon Time|||||||The date on which the soil sampling occurred, formatted as YYYY-MM.|
|latitude|float||Latitude (Y)|||||||The latitude of the geographic location where the soil sample was collected, expressed in decimal degrees (WGS84).|
|longitude|float||Longitude (X)|||||||The longitude of the geographic location where the soil sample was collected, expressed in decimal degrees (WGS84).|
|elevation|integer||Elevation (Z)|||||||The elevation of the location where the soil sample was collected, measured relative to sea level in meters.|
|location|string||Attribute|location|schema:location|||||The administrative province where the soil sample was collected.|
|country|string||Attribute|Country|schema:Country|||||The country in which the soil sample was collected, represented by the ISO country code LA for Laos.|

## Data
The original CSV data (first 9 rows)

|sample_ID | sample_name | ID_field | ID_profile | ID_depth | ID_location | depth | landuse | volum_cylinder_cm3 | wet_mass_soil_g | dry_mass_soil_g | bulk_density | water_content | collection_date | latitude | longitude | elevation | location | country| 
|--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---|
 | s001 | F1-P1-A-ATP | F1 | P1 | A | ATP | 0-5 | cassava | 100 | 149 |  | 1.41 | 5 | 2024-01 | 14.736163 | 106.63576 | 93 | Attapeu | LA | 
 | s002 | F5-P3-A-ATP | F5 | P3 | A | ATP | 0-5 | paddy_rice | 100 | 157 |  | 1.31 | 21 | 2024-01 | 14.711535 | 106.63576 | 93 | Attapeu | LA | 
 | s003 | F1-P2-A-ATP | F1 | P2 | A | ATP | 0-5 | cassava | 100 | 133 |  | 1.3 | 1 | 2024-01 | 14.736163 | 106.63576 | 93 | Attapeu | LA| 
 | s004 | F5-P3-B-ATP | F5 | P3 | B | ATP | 15-20 | paddy_rice | 100 | 152 |  | 1.35 | 21 | 2024-01 | 14.711535 | 106.63576 | 93 | Attapeu | LA| 
 | s005 | F1-P3-A-ATP | F1 | P3 | A | ATP | 0-5 | cassava | 100 | 157 |  | 1.48 | 5 | 2024-01 | 14.736163 | 106.63576 | 93 | Attapeu | LA| 
 | s006 | F6-P1-A-ATP | F6 | P1 | A | ATP | 0-5 | non_cultivated | 100 | 151 |  | 1.42 | 7 | 2024-01 | 14.71234 | 106.63576 | 93 | Attapeu | LA| 
 | s007 | F2-P1-A-ATP | F2 | P1 | A | ATP | 0-5 | non_cultivated | 100 | 166 |  | 1.64 | 0 | 2024-01 | 14.730497 | 106.63576 | 93 | Attapeu | LA| 
 | s008 | F6-P1-B-ATP | F6 | P1 | B | ATP | 15-20 | non_cultivated | 100 | 156 |  | 1.28 | 12 | 2024-01 | 14.71234 | 106.63576 | 93 | Attapeu | LA| 
 | s009 | F6-P2-A-ATP | F6 | P2 | A | ATP | 0-5 | non_cultivated | 100 | 156 |  | 1.45 | 8 | 2024-01 | 14.71234 | 106.63576 | 93 | Attapeu | LA| 
