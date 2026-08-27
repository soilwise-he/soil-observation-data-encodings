# Soil observation encodings

Authors: Kathi Schleidt, Max Vercruyssen, Paul van Genuchten

Observation data from the field or on soil samples in laboratories is typically captured according to the Observations, Measurements and Samples (OMS) principles. Various encoding conventions exist to store or exchange such observation data. In this effort we explore a number of these conventions. Including sample code, data and tools.

## Background

The [Observations Measurements and Samples](https://www.ogc.org/standards/om/) (previously `observations & measurements`) working group of the Open Geospatial Consortium has a long history of interoperability of (sensor) observation data. Over time the group has prepared various editions of the OMS UML model. A model to exchange interoperable observation data. 

Adopting one of the models for your (research) data has three benefits.

- The models assist in identifying what aspects are typically captured on an observation: which `property` is observed, how can you reference the `feature of interest`, which `unit of measure` is used, which `procedure` is used, when and by who has the observation been made. (For some soil properties the selected procedure effects the result or uncertainty substantially).
- When you encode the above information in standardised ways, other users (humans and machines) can easily locate and understand the information
- Various software tools are available which support workflows on standardised observation data, such as conversion tools, validation tools, visualisation tools. So you don't need to write custom software or data models.

[Read more about OMS principles](./COMMON)


### Differences between INSPIRE Soil, ISO 28258 and GloSIS data models

The main difference between the INSPIRE and ISO 28258 models pertains to the spatial features defined to represent aspects of soil investigations. While there is clear consensus on the core FeatureTypes required, specifically Site, Plot, Profile and ProfileElements (Layers and Horizons), the 2 models then diverge on various aspects:
- Specimen: only provided under ISO 28258
- Derived Types: DerivedSoilProfile, SoilDerivedObject, SoilBody only available under INSPIRE
- Soil Mapping: SoilMap with the associated classes SoilMappingUnitCategory, SoilTypologicalUnit and SoilMappingUnit are only provided under ISO 28258
- Projects and related Analysis Requests are only provided under ISO 28258

[Read more about the differences in common encodings](./COMMON/SoilDataModels.md)

## Soil observation data encodings

We explore some of the commonly used encodings and how to traverse between them.
The encodings explored are: 

- [Simple CSV](#simple-csv)
- [Annotated tabular data (CSVW)](#annotated-tabular-data)
- [RO-Crate](#ro-crate---isa-profile)
- [OMS as GML](#oms-as-gml)
- [SensorThings API](#sensor-things-api-sta)
- [Relational databases](#relational-databases)
- [Semantic web](#semantic-web)


### Simple CSV

Simple CSV is the most basic approach, where providers are suggested to populate a pre configured Excel template with their data, provide relevant metadata and 
run the excel sheet through a validation and conversion utility. The results of this effort can be published in any of SOSA RDF, INSPIRE GPKG, INSPIRE GML or SensorThingsAPI. 

The Simple CSV approach is an interesting starting point to understand the OMS conventions. The template illustrates the aspects involved in capturing data about an observation 
on a soil profile or measurement on a prepared soil sample.

[Read more](./SimpleCSV/)

### Annotated tabular data

In the soil science domain it is quite common to share soil observation data in a tabular format (Excel, CSV, DBF). Where samples are listed as rows and observed properties as columns. Column contents are further explained in a readme file or report. Various initiatives exist to standardise the syntax of these readme documents, so also machines can parse this information. We are aware of the following initiatives:

- [CSV-W](./CSVW/) a json-ld alike initiative to annotate CSV files (as rdf)
- [TableSchema](./CSVW#okfn-datapackage) of the DataPackage inititative (OKFN Frictionless data).
- [ISO19110:2016](./CSVW#iso19110--iso19115) which can be embedded in a ISO19115 document

In [CSVW](./CSVW/) we're exploring a [CSV-W approach](https://csvw.org/) to annotate tabular data, to make it  interoperable. The above Simple CSV approach internally uses this technology.

[Read more](./CSVW/)

### RO-Crate - ISA profile

RO-Crate (Research Object Crate) is a lightweight, machine-readable packaging standard for research data, metadata, workflows, and related digital objects.
It builds on web standards such as JSON-LD and schema.org to create FAIR (Findable, Accessible, Interoperable, Reusable) research assets.
An RO-Crate bundles data files together with rich metadata describing their contents, provenance, creators, and relationships.
The approach is domain-agnostic and has been adopted across multiple scientific disciplines.
By using linked data principles, RO-Crate enables both human and machine interpretation of research outputs.
Community-developed profiles extend the core specification for particular research domains and use cases.

The ISA RO-Crate Profile combines RO-Crate with the ISA (Investigation–Study–Assay) metadata framework widely used in life and environmental sciences.
It provides a structured way to describe research projects, studies, samples, observations, and analytical processes.
The profile captures experimental design, sampling activities, measured variables, protocols, and data provenance in a standardized format.
For soil sciences, the ISA profile can represent field campaigns, soil sampling schemes, laboratory analyses, and environmental measurements.
Individual soil observations can be linked to sampling locations, depths, horizons, dates, instruments, and analytical methods.
The model supports integration of physical, chemical, biological, and spectroscopic soil measurements within a common metadata framework.
Relationships between soil samples, derived datasets, workflows, and publications can be explicitly recorded and traced.
Using the ISA RO-Crate Profile can improve interoperability between soil databases, observatories, and data repositories while supporting FAIR data stewardship.
This makes it a promising approach for describing, exchanging, and reusing soil observational data across research infrastructures and international soil monitoring initiatives.

[Read more](./RO-CRATE/)

### OMS as GML

Traditionally data following the UML based models are exchanged via a GML/XML encoding. The OGC [Web Feature Service (WFS)](https://www.ogc.org/standards/wfs) protocol is typically used to exchange such GML documents. 

On the web various datasets are available in this encoding. For example via the [EU data portal](https://data.europa.eu/).

The [Hale Desktop](https://github.com/halestudio/hale) software is an interesting utility to create or consume these GML documents.

Over the years challenges have been identified with this encoding, such as complexity of the GML syntax, large file sizes, limited support in common software tools. Newer encodings are explored below to address these challenges.

[Read more about the GML encoding]()


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

## Alternative models not (yet) explored in this effort

Some alternative/complemetary models used to describe observation data in our domains, but not further explored here, are:
- The [ISA (Investigation, Study, Assay)](https://isa-tools.org) framework is a platform designed for managing experimental metadata in life sciences, environmental, and biomedical research.
- The Observation class in [schema.org](https://schema.org/Observation) aims to capture observation data, including unit and measurement method
- [GBIF/EML](https://doi.org/10.35035/doc-ynvs-eh84) aims to collect information about biological organisms observed in a specific area at a given time
- [MIAPPE (Minimum Information About Plant Phenotyping Experiments)](https://www.miappe.org/) is a data standard designed to harmonize data from plant phenotyping experiments

