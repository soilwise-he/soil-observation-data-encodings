# RML

[R2RML](#) is a w3c standard for annotation of relational (RDB) data to RDF. 
RML is a subset of R2RML for basic tabular formats, such as CSV.
The approach uses a mapping file which defines the mapping from tabular to CSV.
Various tools exist which can apply an RML mapping. In the python ecosystem 
[morph-kgc](#) is the most common tool. 

## The why

This approach is an alternative to the [CSVW](../CSVW) approach. The CSVW approach seems less optimal for 
observation data. The hierarchical structure of observation data, requires many additional triples on top of the 1-to-1 mapping of column to result. We've shown it is possible with csvw virtual columns, but the required configuration is a bit challenging to read, and not all csvw tools support it.

We identified that a minimal data dictionary (column, property, method, unit) for observation data is easy to configure, and this format can then be translated to CSVW before changing to RDF. However if this is already an automated step, the RML approach could be a better alternative.

## The how

Typically soil scientists would create a data dictionary file. This dictionary file plus the data file are used to produce a SSN/SOSA knowledge graph. An intermediate step can be the CSVW or RML mapping file. Users register at minimum the CSV, data-dictionary and RML mapping file. And if relevant, also the produced RDF.

column | entity | property | method | unit
--- | --- | --- | --- | ---
ID  | site | identifier | | 
X   | site | longitude | | epsg:4326
Y   | site | latitude  | | epsg:4325
LID | layer | identifier | | 
Upper | layer | upperDepth | | cm
Lower | layer | lowerDepth | | cm
TX | observation | Texture | TextureClasses
BD | observation | BulkDensity | kg/l
PH | observation | PH | %
CA | observation | Calcium | mg/kg
MG | observation | Magnesium | mg/kg

Advanced users could define a RML mapping file themselves, potentially supported by one of the common LLM's. And upload it with their CSV data to a repository. This is also relevant for cases which do not follow the templates we support.

Alternatively a soil observation data dictionary file is converted by a python script to an RML mapping file.



## The mapping file

A typical mapping file defines a triplemap for each table column, in the case of an observation, the various aspects of an observation are collected from the CSV or provided to complete the graph.

```ttl
<#PhysicalObservationMapping>
    a rml:TriplesMap ;

    rml:logicalSource [
        rml:source "../soveur.csv" ;
        rml:referenceFormulation rml:CSV
    ] ;

    rml:subjectMap [
        rml:template
            "http://data.soilwise-he.eu/soveur/observation/{PRID}/{HONU}/SDTO" ;
        rml:class sosa:Observation
    ] ;

    rml:predicateObjectMap [
        rml:predicate sosa:hasFeatureOfInterest ;
        rml:objectMap [
            rml:template
                "http://data.soilwise-he.eu/soveur/horizon/{PRID}/{HONU}"
        ]
    ] ;

    rml:predicateObjectMap [
        rml:predicate sosa:observedProperty ;
        rml:objectMap [
            rml:constant props:SandProperty
        ]
    ] ;

    rml:predicateObjectMap [
        rml:predicate sosa:hasSimpleResult ;
        rml:objectMap [
            rml:reference "SDTO" ;
            rml:datatype xsd:decimal
        ]
    ] ;

    rml:predicateObjectMap [
        rml:predicate qudt:unit ;
        rml:objectMap [
            rml:constant unit:PERCENT
        ]
    ] .
```

## Morph-KGC

The python tool Morph-KGC requires a .ini file 