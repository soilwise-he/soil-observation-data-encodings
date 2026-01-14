# GeoPackage

This work builds on the work of EJP Soil project, which crafted a [geopackage for soil data based on the INSPIRE model](https://github.com/ejpsoil/inspire_soil_gpkg_template).

While testing the geopackage in real world scenario's, some observations were made

## Convert geopackage to GML using Hale Studio

Any INSPIRE GeoPackage is combined with a Hale Studio transformation project to transform the data to the INSPIRe Soil GML model. How is this transformation project stored along side the geopackage?


## Visualize STA in QGIS

Sensor Things API recently arrived in QGIS. It brings a whole new type of vizualisations to QGIS (combination of data streams in maps and diagrams). We aim to find out if (and how) similar patterns can also be used on the INSPIRE GeoPackage for Soil data in QGIS.



## Populate GeoPackage from QGIS

Bit off topic, but still interesting.

A need arose to populate a Soil Geopackage from QGIS. 
- When running sql queries from the data manager, we ran into [this issue](https://github.com/OSGeo/gdal/pull/13345) which is now resolved in upcoming GDAL versions
- Alternative is described below

## Import data into GeoPackage from RDF

Soil Data in an RDF format would benefit from loading into a GeoPackage, so it can be used by users more comfortable with the geopackage format.

The [rdf to rdb library](../RDF/rdf2rdb/) aims to fullfill this scenario

### Import using SQL in dbmanager

### Import using copy-paste

A procedure commonly used to import geometries into existing layers within a GeoPackage using QGIS.

The import of geometries into an existing table of a GeoPackage with QGIS is structured in three main steps:

- Importing geometries as a layer in QGIS
- Copying the imported geometries
- Pasting the geometries into the GeoPackage layer

Let’s look at each step in detail.

#### Importing geometries

QGIS allows the import of geometries from various formats, such as CSV, Shapefile, or other GeoPackages. In this example, we will import data from a CSV file.

- Click on the “Open Data Source Manager” button (1) in the QGIS toolbar.
- In the window that opens, you can choose from various data sources to import.
- In our example, we select CSV (2) as the source format and proceed with importing the desired (3) file.
- Check the geometry type (e.g., WKT or coordinates separated into latitude/longitude). (4)
- Set the correct Coordinate Reference System (CRS). (5)
- Click on Add (6) to create the layer (in this case, a point layer) in the project.

WARNING: For the copy-paste operation to work correctly, the source layer (from which geometries are copied) must have the same fields (name and data type) as the destination layer, or at least match the required fields.
This check can be done during the import phase, later using QGIS tools, or by using an RDBMS to modify or remove unnecessary fields.

- In this case, since I did not perform the check during import, I processed the layer by creating a temporary support layer named “copy”.


#### Copying geometries

- Import the newly created layer (if it is not already present in the project).
- Right-click on the layer name (7) and, from the context menu, select “Open Attribute Table” (8) to view its data.
- Select all geometries. (9)
- Copy the geometries. (10)

#### Pasting geometries

- Enable editing mode on the destination GeoPackage layer using the Toggle Editing button. (11)
- Paste the geometries. (12)
- Save the changes.

To support this procedure, there is also a QGIS plugin that simplifies and extends the described steps.

It is called AppendFeaturesToLayer and is available at:
https://github.com/gacarrillor/AppendFeaturesToLayer

The plugin includes two geoprocessing tools:

- ETL_LOAD, which allows easy matching of the source table with the destination geometry table
- Append Feature To Layer, which handles the copy-paste operation with additional advanced options

