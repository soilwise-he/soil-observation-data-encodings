# ASAJA CASE STUDY

| Metadata | |
| --- | --- |
| source |            https://doi.org/10.5281/zenodo.17423881 |
| Project |        Novasoil - Horizon Europe Soil Mission |
| Partner |        ASAJA (Spain) |
| Date |       2026-04-30 |
| License |     CC-BY 4.0 |
| Keywords:       Novasoil, Soil Mission, Horizon Europe, soil organic carbon, soil texture, olive, integrated production, FAIR data, EPSG:4326, Spain, ASAJA |

DESCRIPTION
-----------
Harmonized soil observation dataset from the ASAJA case study on olive
integrated production systems in Spain. Data has been standardized for
interoperability according to FAIR data principles for the SoilWise
European catalogue.

SITE INFORMATION
----------------
Country         : Spain
Region          : Andalusia
Site name       : ASAJA - Olive Integrated Production
Approximate lat : 37.342208
Approximate lon : -4.636731
Land use        : Olive grove - integrated production
Sampling period : (insert years)

GEOSPATIAL BOUNDING BOX (for Zenodo)
-------------------------------------

  CRS   : EPSG:4326 (WGS84)

================================================================================
FILES INCLUDED
================================================================================

1. ASAJA_Case_Study_Olive_Integrated_Production_fixed6.csv
   Description : Soil chemical and physical data from olive integrated
                 production plots managed by ASAJA
   Delimiter   : comma (,)
   Encoding    : UTF-8

================================================================================
DATA DICTIONARY - COLUMN DEFINITIONS
================================================================================

Sample_ID
  Type        : Text
  Description : Unique identifier for each soil sample.

Soil_Sampling_Date
  Type        : Date (ISO 8601: YYYY-MM-DD)
  Description : Date of soil sampling.

Upper_Depth_cm
  Type        : Integer
  Unit        : cm
  Description : Upper boundary of the sampled soil layer. Always >= 0.

Lower_Depth_cm
  Type        : Integer
  Unit        : cm
  Description : Lower boundary of the sampled soil layer.

Latitude_EPSG4326
  Type        : Float
  Unit        : Decimal degrees (WGS84 / EPSG:4326). Positive = North.
  Description : Geographic latitude of the sampling point.

Longitude_EPSG4326
  Type        : Float
  Unit        : Decimal degrees (WGS84 / EPSG:4326). Positive = East.
  Description : Geographic longitude of the sampling point.

Clay_pct
  Type        : Float
  Unit        : % (g per 100 g soil)
  Method      : Hydrometer or pipette method (ISO 11277)
  Description : Clay fraction (< 2 µm) as percentage of fine earth.

Silt_pct
  Type        : Float
  Unit        : % (g per 100 g soil)
  Method      : ISO 11277
  Description : Silt fraction (2-50 µm) as percentage of fine earth.

Sand_pct
  Type        : Float
  Unit        : % (g per 100 g soil)
  Method      : ISO 11277
  Description : Sand fraction (50-2000 µm) as percentage of fine earth.

USDA_Classification
  Type        : Text (categorical)
  Description : USDA soil texture class (e.g., Sandy loam, Silt loam, Loam).

pH
  Type        : Float
  Unit        : pH units (dimensionless)
  Method      : Potentiometry in water suspension (1:2.5), ISO 10390
  Description : Soil reaction. Range: 3.5-9.5.

Organic_Matter_pct
  Type        : Float
  Unit        : % (g per 100 g soil)
  Method      : Loss on ignition or calculated as SOC × 1.724
  Description : Soil Organic Matter content as percentage.

Total_N_g_kg
  Type        : Float
  Unit        : g kg⁻¹
  Method      : Kjeldahl (ISO 11261) or dry combustion (ISO 13878)
  Description : Total nitrogen content.

CN_ratio
  Type        : Float
  Unit        : dimensionless
  Description : Carbon-to-Nitrogen ratio.

Phosphorus_Olsen_mg_kg
  Type        : Float
  Unit        : mg kg⁻¹ (ppm)
  Method      : Olsen extraction (NaHCO₃ 0.5M, pH 8.5) — ISO 11263
  Description : Plant-available phosphorus.

================================================================================
STANDARDIZATION NOTES
================================================================================
- All coordinates in EPSG:4326 (WGS84 decimal degrees)
- Date format: ISO 8601 (YYYY-MM-DD)
- Decimal separator: period (.)
- Missing values: empty cell (no NA, no N/A text)
- Encoding: UTF-8
- Delimiter: comma (,)

================================================================================
ZENODO UPLOAD CHECKLIST
================================================================================
[ ] Title: "Harmonized soil observations for ASAJA Olive Integrated Production
            - SoilWise Project"
[ ] Creators: all authors with ORCID
[ ] Description: olive integrated production, sampling methodology, time period
[ ] Keywords: SoilWise, Soil Mission, Horizon Europe, Spain, olive, integrated
              production, soil organic carbon, FAIR data
[ ] License: CC-BY 4.0
[ ] Funding: Horizon Europe Grant Agreement No. (insert number)
[ ] Geographic location (Bounding Box): (insert coordinates)
[ ] Upload this README alongside the CSV files
[ ] After publication: verify DOI via SoilWise portal

================================================================================
END OF README
================================================================================
