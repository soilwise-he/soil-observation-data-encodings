# Simple CSV
As a very simple approach to providing soil data, we describe an approach where all data is stored within a set of CSV files:
- General: general metadata applicable to the entire dataset. Includes concepts like CRS for spatial data
- Spatial Objects: description of the spatial objects on which data is provided, alternatively the samples/specimens
- Observable Properties: list of all column headers describing an observed property. Includes methodology, Unit of Measurement, sample preparation. If the same property is provided using 2 methodologies, one entry must be provided per methodology
- Data: the values, columns describe Observable Properties, rows describe Spatial Objects

