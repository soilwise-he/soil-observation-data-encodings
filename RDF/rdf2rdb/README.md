# soil-rdf2rdb

Goal of this module is to provide a conversion from soil observations rdf to a relational database. 

This code uses [SOSA observations](https://www.w3.org/TR/vocab-ssn/) and later also [schema.org](https:/schema.org/Observation) as input and writes to [SQLite](https://github.com/ejpsoil/inspire_soil_gpkg_template) as output.

The code uses as output format a simplified version of inspire geopackage, available at https://github.com/soil-on-web/iso28258-as-rdbs

As input some flavours of RDF are considered:

- [ ] schema.org
- [x] [SOSA](https://www.w3.org/TR/vocab-ssn/)
- [ ] [Glosis Web Ontology (based on SOSA)](https://glosis-ld.github.io/glosis)

In a python virtual environment, run:

```bash
pip3 install -r requirements.txt 
python soil-rdf2rdb.py ../CSVW-Excel-Template/example3/data.ttl
```


