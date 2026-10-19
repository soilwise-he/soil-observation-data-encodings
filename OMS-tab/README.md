# OMS-tab

An dedicated format to capture metadata of columns in a dataset of (soil) observations, measurement and samples.

The format describes columns of one or more related tables, assuming that some columns contain obervation data, either field observations or laboratory measurements on samples.

For each column the following properties can be capured

| Name | Description | Required | Default | Example |
| --- | --- | --- | --- | --- |
| table_name | (File)name of the table | true | - | Field_obs |
| column_label | Name of the column, if empty assumes table has no column names, and uses columns in numeric order | false | - | Speed (m/s) | 
| column_type | Value type of the column | - | string  |numeric | 
| column_format | The format of a date or numeric field, it can also be used to split a string in two or more fields, in that case the column is included multiple times in the metadata, 1 row for each string part | false | - | %Y-%m-%d | 
| concept_type | The class for which this is a property | false | Sample | Observation, Site, Plot, Profile, Layer, Sample | 
| concept | The nature of the property | false | - | Calcium content | 
| concept_uri | A URI describing the concept | true | - | https://w3id.org/eusoilvoc/calcium-content |
| unit_symbol | the unit in which the value is written | false | - | m/s |
| unit_uri | the uri of the unit | true | - | http://qudt.org/vocab/unit/CentiM3 |
| quantity_kind_uri | The quantity kind of the unit | false | - | Weight | 
| method | the observation method used | false | - | The mass of the soil sample after oven-drying at 105 °C until constant weight, representing the dry mass of soil, measured in grams. |
| method_uri | A uri of the method | false | - | https://w3id.org/eusoilvoc/proc-calcium-extr |
| description | A description of the column | false | | This column contains the measured length of the sample |
| primary_key | Indicates if this column is a primary key | false | false | true |


## Serialisations

The file can be serialised as CSV or as json-ld.

### CSV

In a CSV encoding, each row describes a single column of a table.

Example:

|table_name|column_label|column_type|column_format|concept_type|concept|concept_uri|unit_symbol|unit_uri|quantity_kind_uri|method|description|
|---|---|---|---|---|---|---|---|---|---|---|---|
|laos_data.csv|sample_ID|string||Feature of Interest|||||||A unique identifier assigned to each soil sample, constructed to ensure traceability.|
|laos_data.csv|sample_name|string||Feature of Interest|||||||A unique identifier for each soil sample, combining field number, replicate number, depth interval, and location.|
|laos_data.csv|ID_field|string||Attribute|||||||Identifier representing the specific field from which the soil sample was collected.|
|laos_data.csv|ID_profile|string||Attribute|||||||Identifier indicating the within-field replicate number for the soil sample.|
|laos_data.csv|ID_depth|string||Attribute|||||||Identifier denoting the depth interval from which the soil sample was taken, with A for 0–5 cm and B for 15–20 cm.|
|laos_data.csv|ID_location|string||Attribute|||||||Identifier representing the administrative location where the soil sample was collected, with ATP for Attapeu and KHA for Khammouane.|
|laos_data.csv|depth|string||Depth Upper|soil depth|http://w3id.org/glosis/model/common/soilDepthProperty|||||The soil depth interval from the surface over which the soil sample was collected, measured in centimeters.|
|laos_data.csv|landuse|codelist||Attribute|land use type|Tab-LandCoverTypes|||||The category of land use under which the soil sample was collected, such as rice, cassava, gardens, or non-cultivated.|
|laos_data.csv|volum_cylinder_cm3|integer||Observed Property|sample volume|https://data.geoscience.earth/ncl/ISO11074v2025/3.409|cm³|http://qudt.org/vocab/unit/CentiM3|http://qudt.org/vocab/quantitykind/Volume|ENVO – soil sampling device (ENVO:00002792)|The volume of the soil sampling cylinder used to collect an undisturbed soil sample, measured in cubic centimeters.|
|laos_data.csv|wet_mass_soil_g|float||Observed Property|soil water content|http://aims.fao.org/aos/agrovoc/c_7208|g|http://qudt.org/vocab/unit/GM|http://qudt.org/vocab/quantitykind/Mass||The mass of the soil sample immediately after collection, including water content, measured in grams.|
|laos_data.csv|dry_mass_soil_g|float||Observed Property|soil sample|http://opendata.inrae.fr/thesaurusINRAE/c_17874|g|http://qudt.org/vocab/unit/GM|http://qudt.org/vocab/quantitykind/Mass||The mass of the soil sample after oven-drying at 105 °C until constant weight, representing the dry mass of soil, measured in grams.|
|laos_data.csv|bulk_density|float||Observed Property|bulk density|https://data.geoscience.earth/ncl/ISO11074v2025/3.62|g/cm³|http://qudt.org/vocab/unit/GM-PER-CentiM3|http://qudt.org/vocab/quantitykind/MassDensity|ENVO – soil bulk density (ENVO:09200004)|The dry mass of soil per unit volume, including pore space, measured using a soil sampling cylinder and expressed in grams per cubic centimeter.|
|laos_data.csv|water_content|integer||Observed Property|soil water content|http://aims.fao.org/aos/agrovoc/c_7208|g/g|http://qudt.org/vocab/unit/GM-PER-GM|http://qudt.org/vocab/quantitykind/MassRatio|ENVO – soil gravimetric water content|The mass of water in the soil per unit dry mass of soil, expressed as a percentage by weight.|
|laos_data.csv|collection_date|date|%Y-%m|Phenomenon Time|||||||The date on which the soil sampling occurred, formatted as YYYY-MM.|
|laos_data.csv|latitude|float||Latitude (Y)|||||||The latitude of the geographic location where the soil sample was collected, expressed in decimal degrees (WGS84).|
|laos_data.csv|longitude|float||Longitude (X)|||||||The longitude of the geographic location where the soil sample was collected, expressed in decimal degrees (WGS84).|
|laos_data.csv|elevation|integer||Elevation (Z)|||||||The elevation of the location where the soil sample was collected, measured relative to sea level in meters.|
|laos_data.csv|location|string||Attribute|location|schema:location|||||The administrative province where the soil sample was collected.|
|laos_data.csv|country|string||Attribute|Country|schema:Country|||||The country in which the soil sample was collected, represented by the ISO country code LA for Laos.|

### JSON-ld

The json-ld encoding contains an array of table and column objects which are described using a flavour of CSV-W, extended to support observation metadata. Ambition for this implementation of CSV-W is not to enable full CSW-W interoperability, but to describe the columns in full detail. In a second automated step the OMS-tab metadata will be converted to RML to provide full SSN/SOSA interoperability. 

Example:

```
{
  "@context": "http://www.w3.org/ns/csvw",
  "tables": [{
    "url": "signal.ID_7036_SIGNAL_SITE_POINTS.csv",
    "tableSchema": {
      "columns": [{
          "name": "OBJECTID",
          "titles": "OBJECTID",
          "datatype": "decimal",
          "propertyUrl": "http://schema.org/identifier"
          "@type": "sosa:FeatureOfInterest"
          "@id": "https://example.com#{OBJECTID}"
        },
        {
          "titles": "Latitude",
          "datatype": "decimal",
          "propertyUrl": "https://schema.org/latitude",
          "about": "https://example.com#{OBJECTID}"
        },
        {
          "titles": "Longitude",
          "datatype": "decimal",
          "propertyUrl": "https://schema.org/longitude",
          "about": "https://example.com#{OBJECTID}"
        },
        {
          "titles": "ECEC (DC/m)",
          "name": "ecec",
          "datatype": "decimal",
          "propertyUrl": "http://w3id.org/glosis/model/codelists/properties/electricalConductivity",
          "schema:measurementTechnique": "https://w3id.org/eusoilvoc",
          "schema:unitCode": "http://qudt.org/schema/qudt/DeciS-PER-M",
          "@type": "sosa:Observation",
          "@id": "https://example.com#{OBJECTID}/ecec"
        }
      ]
    }
  }]
}
```


