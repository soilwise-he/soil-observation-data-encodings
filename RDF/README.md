# Semantic Web

## SoilWise efforts

- [Soil Health Knowledge Graph](https://github.com/soilwise-he/soil-health-knowledge-graph)
- [CSV-W](../CSVW/) to convert tabular soil observation data to RDF
- [rdf 2 rdb](./rdf2rdb/) is a library to convert SOSA RDF to SQLite
- a [virtuoso](https://repository.soilwise-he.eu/sparql/) instance hosting some soil data to explore query options

## Ontology to describe soil data

OGC and W3c developed the [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/) ontology to facilitate sharing of observation data over the web. These days Schema.org also provides option to describe measuredValues of a dataset in quite some detail. 


## Existing works

### GLOSIS-LD

In the project [Sino-EU Soil Observatory for intelligent Land Use Management (SIEUSOIL)](https://cordis.europa.eu/project/id/818346) the group developed a Semantic Web Ontology based on ISO28258, [GLOSIS-LD](https://github.com/glosis-ld/glosis), using existing ontologies, such as [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/). This work extends on previous work of the [GLOSIS working group](https://github.com/FAO-SID/GloSIS) of FAO/GSP. The GLOSIS-LD initiative provides mechanisms to encode soil observation data in RDF. The ontology is quite rich in listing Observable properties and observation procedures. These Codelists are also used outside the semantic web context.

### Schema.org

These days the [Schema.org](https://schema.org) ontology provides options to capture various aspects of observation data via its [Observation](https://schema.org/Observation) class and [variableMeasured](https://schema.org/variableMeasured) property.

### Other

Other relevant ontologies in this domain 

- [iMash](https://archive.researchdata.leeds.ac.uk/42/), 
- [Sweet](https://earthportal.eu/ontologies/SWEET), 
- [iAdopt](https://i-adopt.github.io/ontology/) 
- [ISO11074](https://www.iso.org/standard/83168.html).