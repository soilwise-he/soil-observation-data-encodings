# Conceptual and Real world data examples in soil research


## 10 examples

| nr | title | license |scenario | hasGeometry | hasTime | Spatial | Sample | Observations | ObsProp | Time | Sampling Time | Example # |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 1. | [Soveur](example1) | CC-BY | location, depth and observations in a single table | Y | N |  |  |  |  |  |  |  | 
| 2. | [Leafy Tree](example2) | CC-BY | locations (trees) and observations (leafs) in separate tables | Y | N |  |  |  |  |  |  |  | 
| 3. | [NPK](example3) | CC-BY | location and observations in a single table | Y | Y |  |  |  |  |  |  |  | 
| 4. | [Laos](example4) | CC-BY | location and observations in a single table | Y | Y |  |  |  |  |  |  |  | 
| 5. | [Curieuzeneuzen; citizen science](example5) | CC-BY | Citizen science project measuring temperature and humidity in gardens | Y | Y |  |  |  |  |  |  |  | 
| 6. | [Soil of Côte d'Ivoire](example6) | CC-BY |Two tables with location and observations in a single table | Y | N |  |  |  |  |  |  |  | 
| 7. | ~~[Waste4soil](example7)~~ | CC-BY | Seems to describe outputs of a biogas plant. While the digestates may later be applied to soils, not described here KS: Not sure relevant | N | N |  |  |  |  |  |  |  | 
| 8. | [Novasoil](example8) | CC-BY | 1 location in metadata, observations in table | Y | N |  |  |  |  |  |  |  | 
| 9. | [AFSIS](example9) | CC-BY | locations (profiles) and observations (smples) in separate tables | Y | Y |  |  |  |  |  |  |  | 
| 10. | [Bonares](example10) | CC-BY | locations and samples and observations in 3 separate tables | Y | Y |  |  |  |  |  |  |  | 

## Potential permutations of files
Based on the files above, we analysed the different permutations of files with which observational data is provided. In the table below, we assume 1 - 3 individual CSV files, with an additional readme file. The CSV files are numbered sequentially for this analysis, in some cases one CSV file covers all concepts, in others spatial and sampling information may be factored out into additional CSV files.

### CSV

In the table below, one can see these individual permutations for the various constellations of CSV files. In order to indicate which CSV file provides which concepts, the number of the CSV file is provided in the table. When the required information is provided by a semi-structured readme, an X is provided in the table.

| Spatial | Sample | Observations | ObsProp | Time | Sampling Time | Example # |
| --- | --- | --- | --- | --- | --- | --- | 
| 1 | | 1 | X | X	|  |  | 
| X |  | 1 | X | X |  |  | 
|1 |  | 2 | X | X |  |  | 
|1 | 2 | 3 | X | X | X |  | 
|1 |  | 1 | X | 1 |  |  | 
|X |  | 1 | X | 1 |  |  | 
|1 |  | 2 | X | 1 |  |  | 
|1 | 2 | 3 | X | 2 | 2 |  | 
|1 |  | 2 | X | 2 |  |  | 
|1 | 2 | 3 | X | 3 |  |  | 
|1 | 2 | 3 | X | 3 | 2 |  | 

### Grids
In the table below, we perform the same analysis for grid files, focusing on well known formats.

| Format | Spatial | Sample | Observations | ObsProp | Time | Sampling Time | Example # |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| CovJSON | 1 |  | 1 | 1 | 1 |  |  | 
| GeoTIFF | 1 |  | 1 | X | X |  |  | 
| CIS | 1 |  | 1 | 1 | 1 |  |  | 


