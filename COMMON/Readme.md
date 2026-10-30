## Common Elements across encodings for observation data

While SoilWise supports an array of different encodings for observation data, each tailored for different usage areas, these models are united through the underlying conceptual [OGC/ISO Observations, Measurements and Samples Standard](https://www.ogc.org/standards/om/), 
semantically formalized under [W3C SSN/SOSA](https://w3c.github.io/sdw-sosa-ssn/ssn/). This model entails the use of the Observation concept, that unites:
- Feature of Interest: target of the Observation, what exactly is being Observed
- Result: the actual value being conveyed by the Observation, e.g. a value representing Bulk Density, Organic Carbon, pH at the Feature of Interest
- Observational Metainformation:
  - Observed Property: what exactly was being Observed, e.g. Bulk Density, Organic Carbon, pH
  - Observing Procedure: how was this property ascertained, what methodology was used
  - Unit of Measurement: in what unit is the result being conveyed
  - Additional concepts, e.g. Sensor used in measurement, Host at which this Sensor was deployed... Currently not being utilized in SoilWise

## Soil Data Models
At present, there are three closely related soil data models to chose from:
- INSPIRE Soil: defined under the European INSPIRE Initiative, this model provides a set of spatial features for which soil data can be provided using the Observations and Measurements model-
- ISO 28258:2013 - Digital exchange of soil-related data describes how to digitally exchange soil-related data. This model is a refinement of the INSPIRE model, whereby feature type definitions have been modified.
- GloSIS (FAO Global Soil Information System) extends the ISO 28258 model with Observable Properties and Observing Procedures suitable for the spatial feature types defined.

For a more detailed description of these soil data models, please see the section on [Soil Data Standards](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/COMMON/SoilDataModels.md).

## Encodings

Based on the soil data models described above, the following explicit encodings for soil data storage and provision have been created:
- [CSVW](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/CSVW/README.md)
- [CSV Template](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/SimpleCSV/readme.md)
- SOSA RDF
- [SoilWise GeoPackage](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/GPKG/README.md)
- [OGC SensorThings API](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/STA/README.md)
- [INSPIRE GML](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/GML/README.md)

### Converters

In order to transform data between the different SoilWise data encodings, a suite of [Converters](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/COMMON/Converters/README.md) has been implemented.

## Observed Property++

In order to work with O&M based data models, one needs a registry (codelist, vocabulary...) of Observable Properties together with applicable Observing Procedures as well as Unit of Measurement types. We provide details on the requirements to an [Observable Property registry](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/COMMON/Observed%20Property.md).

### SoilVoc Links
SoilVoc provides access to the necessary Observable Properties together with applicable Observing Procedures. At present, SoilVoc is being hosted by various portals. Here a list of [SoilVoc Viewers](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/COMMON/SoilVoc-Viewers.md).

## New Feature-of-Interest types

Due to the update of O&M to OMS, new possibilities of data structuring become possible. We provide information on potential [new Feature-of-Interest types](https://github.com/soilwise-he/soil-observation-data-encodings/blob/main/COMMON/New-FOI-Types.md).
