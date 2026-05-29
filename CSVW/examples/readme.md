# Examples for CSVW Encoding

## Underlying CSV Structure

Based on analysis of CSV files providing soil data, common patterns have been identified. 
While there is always a central data table, in some cases additional tables are provided. 
These tables fall into the following 4 categories, reflecting the structure of the [SimpleCSV approach](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/SimpleCSV/readme.md):

**1. General (G):** a table containing general information applicable to the entire file.
In addition to administrative information, global concepts such as the coordinate reference system (CRS) are often provided at this level.

**2. Spatial or Specimen Information (S):** a table containing further information on each object being observed or measured (Feature-of-Interest). 
In some cases, this will be spatial information, e.g. describing a soil plot or profile while in other cases, this may be a specimen in a lab.
An identifier must be used to link the information from this table to the data table.

**3. Observable Property Information (O):** a table containing the properties for which data is being conveyed. These are usually column headers in the data table.
In addition to the property, additional information such as the utilized methodology or the unit-of-measurement can be provided

**4. Data (D):** the core CSV table containing the soil data values.

In the table below, we analyse the available information for each example, indicating what type of information is provided in which files (letters from the list above). 
Information types are:
- **FoI ID**: Identifier of the Feature-of-Interest, e.g., the spatial object or specimen on which data is being provided
- **Spatial**: Spatial information indicating where the measurements took place, e.g. coordinates of the spatial object for which we have the FoI ID
- **FoI Attributes**: Attributes on the Feature-of-Interest, e.g., the spatial object or specimen on which data is being provided.
- **ObsProp**: Observable Property Information
- **Date**: Temporal information on when the data was observed or measured


| Example    | FoI ID | Spatial | FoI Attributes | ObsProp | Date | 
|------------|--------|---------|----------------|---------|------| 
|	Example  1 | D      | D	      |                |         |      | 		
|	Example  2 | D      | S	      |                |         |      | 		
|	Example  3 | D      |         |                |         | D    |

