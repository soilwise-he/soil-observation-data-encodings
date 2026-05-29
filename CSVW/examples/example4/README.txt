SOIL BULK DENSITY DATASET – LAO PDR

Version: 1.0
Dataset status: Final and frozen

DATASET OVERVIEW -------------------------------------
This dataset contains soil bulk density measurements collected across different land-use types in Lao People’s Democratic Republic (Lao PDR). Data were collected in two provinces, Attapeu and Khammouane, under contrasting seasonal conditions. The dataset documents variations in soil bulk density across common agricultural and non-cultivated land uses.

The dataset is intended for descriptive analysis, comparison across land uses, and contextual soil health assessments. No further data processing is expected.

STUDY AREA -------------------------------------
Country: Lao People’s Democratic Republic (Lao PDR)

Provinces: Attapeu and Khammouane

Study sites are located in lowland agricultural landscapes.

TEMPORAL COVERAGE -------------------------------------

Attapeu Province: January–February 2024 (dry season)

Khammouane Province: November 2025 (end of the rainy season)

LAND-USE DEFINITIONS -------------------------------------

Rice
Paddy rice fields cultivated in lowland plains and flooded by rainfall during the rainy season. This represents the traditional lowland rice cultivation system in Lao PDR.

Cassava
Cassava fields managed under conventional agricultural practices commonly used in Lao PDR.

Gardens
Household vegetable gardens located around houses. Soil samples were collected under various vegetable crops within each garden. Crop types were not systematically recorded.

Non-cultivated
Areas adjacent to agricultural fields with no active cultivation, used as reference or control sites.

DATA DESCRIPTION --------------------------------------------
The dataset consists of soil bulk density and associated soil property measurements collected at the field level.

For each field, three to four replicate sampling points were collected. At each replicate, soil samples were taken at two depth intervals: 0–5 cm and 15–20 cm.

Each record in the dataset is associated with a unique sample name and corresponds to one soil sample from one replicate at one depth, associated with a specific land use, location. Each sample is associated with a unique sample name where F indicates the field number, P indicates the within-field replicate, the letter A or B indicate the depth (A for 0-5 cm and B for 15-20 cm) and the three capital letters indicate location (ATP for Attapeu and KHA for Khamouan). 

File format: CSV
Each row represents one soil sample

VARIABLE DEFINITIONS AND ONTOLOGY REFERENCES  -------------------------------------

1. MEASURED VARIABLES

wet_mass
Description: Mass of the soil sample immediately after collection, before drying, including water content.
Ontology reference: ENVO – soil sample mass
Unit: g 

dry_mass
Description: Mass of the soil sample after oven-drying at 105 °C for 48 hours until constant weight, representing the dry mass of soil.
Ontology reference: ENVO – soil sample mass
Unit: g

bulk_density
Description: Dry mass of soil per unit volume, including pore space, measured using a 100 cm³ soil sampling cylinder and oven-drying at 105 °C until constant mass.
Ontology reference: ENVO – soil bulk density (ENVO:09200004)
Unit: g/cm3

water_content
Description: Mass of water in the soil per unit dry mass of soil, determined by oven-drying the soil at 105 °C until constant mass.
Ontology reference: ENVO – soil gravimetric water content
Unit: % (w/w)

volume_cylinder
Description: Volume of the soil sampling cylinder used to collect an undisturbed soil sample for determining bulk density.
Ontology reference: ENVO – soil sampling device (ENVO:00002792)
Unit: cm³ 

2. EXPERIMENTAL DESIGN VARIABLES

sample_name
Description: Unique identifier assigned to each soil sample. The sample_name ensures that each sample can be uniquely traced and is constructed by combining three elements:
	F = field number
	P = within-field replicate number
	A or B = depth interval, where A corresponds to 0–5 cm and B corresponds to 15–20 cm
	ATP or KHA = administrative location, where ATP corresponds to Attapeu and KHA corresponds to Khammouan

Format: ID_field_ID_profile_ID_depth_ID_location (e.g., F1_P2_A_ATP)
Ontology reference: ENVO – soil sample (ENVO:00002792)

depth
Description: Soil depth interval from the soil surface over which the soil sample was collected.
Ontology reference: ENVO – soil depth
Unit: cm 

land_use
Description: Land-use category under which the soil sample was collected, measured from the soil surface.
Ontology reference: ENVO – land use (ENVO:01000267)

Land-use categories:

rice
Description: Paddy rice field
Ontology reference: ENVO – paddy field (ENVO:00000155); AGROVOC – rice

cassava
Description: Cassava cropland
Ontology reference: AGROVOC – cassava

gardens
Description: Household vegetable garden
Ontology reference: ENVO – home garden (ENVO:01000451)

non_cultivated
Description: Uncultivated land adjacent to agricultural fields
Ontology reference: ENVO – uncultivated land (ENVO:01000438)

3. GEOGRAPHICAL AND TEMPORAL VARIABLES

collection_date
Description: Date of soil sampling.
Ontology reference: OBOE – sampling event
Format: YYYY-MM

latitude
Description: Latitude of the geographic location where the soil sample was collected, expressed in decimal degrees (WGS84).
Ontology reference: WGS84 – latitude
Unit: degree (UCUM: deg)

longitude
Description: Longitude of the geographic location where the soil sample was collected, expressed in decimal degrees (WGS84).
Ontology reference: WGS84 – longitude
Unit: degree (UCUM: deg)

elevation
Description: Elevation of the location where the soil sample was collected, measured relative to sea level.
Ontology reference: ENVO – elevation (ENVO:01000322)
Unit: meter (UCUM: m)

location
Description: Administrative province where the sample was collected.
Ontology reference: ENVO – administrative region (ENVO:00000005)

country
Description: Country in which the soil sample was collected.
Ontology reference: ENVO – country (ENVO:00002009) (or ISO 3166-1 alpha-2/alpha-3 codes for interoperability)
Unit / Format: Text / ISO country code LA for Laos

FUNDING AND PROJECTS ----------------------------------------------------

Attapeu data: Agroecology Initiative (CIAT, IWMI)
Khammouane data: SOLAO Project (French Embassy in Laos)


LIMITATIONS AND NOTES ------------------------------------------------

Sampling was conducted during different seasons across provinces, which may influence bulk density values.

Crop types in garden plots were not recorded.

Non-cultivated sites represent nearby uncultivated areas and should not be interpreted as undisturbed natural soils.

Bulk density values reflect conditions at the time of sampling only.

Measurements represent point samples within each field and depth interval; spatial variability within fields may not be fully captured despite replication.

DATA USE AND CITATION ------------------------------------------------------

Data collected by: Ms Sunee Peecha, Ms Nampheung Sayalath, Ms Florine Degrune
Affiliation: CIRAD, UMR Eco&Sols, France / IRD, UMR XX, France

Suggested citation:
[Author(s)] ([Year]). Soil bulk density dataset across land uses in Lao PDR. [Repository name]. DOI: [to be assigned]

License: [e.g. CC-BY 4.0]

CONTACT
For questions related to this dataset, please contact:
florine.degrune@cirad.fr