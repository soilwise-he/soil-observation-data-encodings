# Soil observation encodings

Observation data on soil samples is typically captured accoring to Observations, Measurements and Samples (OMS) principles. Various encoding conventions exist to store or exchange such observation data. In this repository we explore a number of these conventions. Including sample code, data and tools.

Soil data models such as [ISO28258:2013](https://www.iso.org/standard/44595.html) and [INSPIRE Soil](https://github.com/INSPIRE-MIF/technical-guidelines/tree/main/data/so) are based on the OMS datamodel.

The encodings explored are: 

- [OMS as GML](#oms-as-gml)
- [SensorThings API](#sensor-things-api-sta)
- [Relational databases](#relational-databases)
- [Semantic web](#semantic-web)
- [Annotated tabular data (CSVW)](#annotated-tabular-data)

## Background

The [Observations Measurements and Samples](https://www.ogc.org/standards/om/) (previously `observations & measurements`) working group of the Open Geospatial Consortium has a long history of interoperability of (sensor) observation data. Over time the group has prepared various editions of the OMS UML model. A model to exchange interoperable observation data. Soil data models such as [ISO28258:2013](https://www.iso.org/standard/44595.html) and [INSPIRE Soil](https://github.com/INSPIRE-MIF/technical-guidelines/tree/main/data/so) are based on the OMS datamodel.

Adopting one of the models for your (research) data has three benefits.

- The models assist in identifying what aspects are typically captured on an observation: which `property` is observed, how can you reference the `feature of interest`, which `unit of measure` is used, which `procedure` is used, when and by who has the observation been made. (For some soil properties the selected procedure effects the result or uncertainty substantially).
- When you encode the above information in standardised ways, other users (humans and machines) can easily locate and understand the information
- Various software tools are available which support workflows on standardised observation data, such as conversion tools, validation tools, visualisation tools. So you don't need to write custom software or data models.


## Which data models

In the SoilWise project we're exploring the following data encodings to capture soil observation data.

### OMS as GML

Traditionally data following the UML based models are exchanged via a GML/XML encoding. The OGC [Web Feature Service (WFS)](https://www.ogc.org/standards/wfs) protocol is typically used to exchange such GML documents. Because the Soil data model builds on OMS, also the Senser Observation Service (SOS) protocol can be used to exchange soil observation data.

On the web various datasets are available in this encoding. For example via the [INSPIRE Geoportal](https://inspire-geoportal.ec.europa.eu/).

The [Hale Desktop](https://github.com/halestudio/hale) software is an interesting utility to create or consume these GML documents.

Over the years challenges have been identified with this encoding, such as complexity of the GML syntax, large file sizes, limited support in common software tools. Newer encodings are explored below to address these challenges.


### Sensor Things API (STA)

The [SensorThings API](https://www.ogc.org/standards/sensorthings/) provides a modern mechanism to interact with observation data (advanced select and filter options). STA builds on [ODATA protocol](https://odata.org) and REST principles. An efficient implementation of the API is provided by the [Frost Server](https://github.com/FraunhoferIOSB/FROST-Server) software. Recent version of QGIS include a [STA interface](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_ogc/ogc_client_support.html#sensorthings) to visualise observation data from STA services. 

Beyond the API definition, STA has introduced some conventions on top of OMS, which could be interesting to explore in the scope of using STA model in a file format.

[Read more](./STA/)


### Relational databases

Over time various groups have worked on initiatives to encode observation data following the OMS UML model in a relational database such as SQLite (GeoPackage), MS Access or PostGreSQL.

Based on the [INSPIRE good practice for geopackage encoding](https://github.com/INSPIRE-MIF/gp-geopackage-encodings) CREA, in the scope of the EJP Soil project, explored [options to encode INSPIRE soil data in a GeoPackage format](https://github.com/ejpsoil/inspire_soil_gpkg_template). GeoPackage is a spatial extension to the common SQLite database format. In the SoilWise project the work is further [extended and tested](https://github.com/soilwise-he/Geopackage-so). The SQLite format is focussed on data exchange.

At ISRIC - World Soil Information, a [relational database model for soil data](https://github.com/ISRICWorldSoil/iso-28258) based on ISO28258:2013 has been developed. This model is targetting the PostGreSQL database. The model is optimised for use in an operational multi user Soil Information System.  

[Read more](./GPKG/)


### Semantic web

In the project [Sino-EU Soil Observatory for intelligent Land Use Management (SIEUSOIL)](https://cordis.europa.eu/project/id/818346) the group developed a Semantic Web Ontology based on ISO28258, [GLOSIS-LD](https://github.com/glosis-ld/glosis), using existing ontologies, such as [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/). This work extends on previous work of the [GLOSIS working group](https://github.com/FAO-SID/GloSIS) of FAO/GSP. The GLOSIS-LD initiative provides mechanisms to encode soil observation data in RDF. The ontology is quite rich in listing Observable properties and observation procedures. These Codelists are also used outside the semantic web context.

These days the [Schema.org](https://schema.org) ontology provides options to capture various aspects of observation data via its [Observation](https://schema.org/Observation) class and [variableMeasured](https://schema.org/variableMeasured) property.

Other relevant ontologies in this domain are [iMash](https://archive.researchdata.leeds.ac.uk/42/), [Sweet](https://earthportal.eu/ontologies/SWEET), [iAdopt](https://i-adopt.github.io/ontology/) and [ISO11074](https://www.iso.org/standard/83168.html).

[Read more](./RDF/)


### Annotated tabular data

In the soil science domain it is quite common to share soil observation data in a tabular format (Excel, CSV, DBF). Where samples are listed as rows and observed properties as columns. Column contents are further explained in a readme file or report. Various initiatives exist to standardise the syntax of these readme documents, so also machines can parse this information. We are aware of the following initiatives:

- [CSV-W](./CSVW/) a json-ld alike initiative to annotate CSV files (as rdf)
- [TableSchema](./CSVW/README.md#okfn-datapackage) of the DataPackage inititative (OKFN Frictionless data).
- [ISO19110:2016](./CSVW/README.md#iso19110--iso19115) which can be embedded in a ISO19115 document

In [CSVW](./CSVW/) we're exploring a [CSV-W approach](https://csvw.org/) to annotate tabular data, to make it  interoperable. 

[Read more](./CSVW/)