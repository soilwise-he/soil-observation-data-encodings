# Semantic Web

The Semantic Web vocabularies [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/) (SSN) and Sensor, Observation, Sample, and Actuator Ontology (SOSA) provide a standardized framework for representing observation data in RDF.
They enable interoperable descriptions of sensors, sampling activities, observations, observed properties, procedures, and results across environmental and agricultural domains.
In soil science, SOSA/SSN can model field observations, laboratory analyses, and sensor measurements related to soil horizons, texture, moisture, pH, carbon content, and nutrient status.
Each soil observation can be linked to a sampling feature, geographic location, timestamp, responsible agent, and measurement method using RDF triples.
This semantic approach improves data integration between soil databases, monitoring networks, and decision-support systems.
Controlled vocabularies expressed with Simple Knowledge Organization System (SKOS) are commonly used to harmonize soil property definitions and classifications.
SKOS concept schemes can define standardized terms for soil properties such as bulk density, cation exchange capacity, and organic carbon.
They also support consistent representation of units of measure, often aligned with established unit ontologies and measurement standards.
In addition, SKOS vocabularies can describe soil observation procedures, including sampling protocols, laboratory methods, and sensor calibration techniques.
Together, SOSA/SSN and SKOS provide a robust semantic infrastructure for interoperable, machine-readable soil observation data within linked data ecosystems.

Alternatively [schema.org/Observation](https://schema.org/Observation) offers similar capabilities in the schema.org cmmuni.

## SoilWise efforts

- Semantic web formats can be created using the [CSV-W](../CSVW/) approach.
- the [soil vocabulary](https://w3id.eusoilvoc) lists soil properties and procedures and their relations.

## Related works

### GLOSIS-LD
In the project [Sino-EU Soil Observatory for intelligent Land Use Management (SIEUSOIL)](https://cordis.europa.eu/project/id/818346) the group developed a Semantic Web Ontology based on ISO28258, [GLOSIS-LD](https://github.com/glosis-ld/glosis), using existing ontologies, such as [SSN/SOSA](https://www.w3.org/TR/vocab-ssn/). This work extends on previous work of the [GLOSIS working group](https://github.com/FAO-SID/GloSIS) of FAO/GSP. The GLOSIS-LD initiative provides mechanisms to encode soil observation data in RDF. The ontology is quite rich in listing Observable properties and observation procedures. These Codelists are also used outside the semantic web context.

### iMash
[iMash](https://archive.researchdata.leeds.ac.uk/42/) is an archived repository which describes observations on soil

### Miappe
The [Minimal Information About Plant Phenotyping Experiment](https://github.com/MIAPPE/MIAPPE) (MIAPPE) is an open, community driven project to harmonize data from plant phenotyping experiments 

