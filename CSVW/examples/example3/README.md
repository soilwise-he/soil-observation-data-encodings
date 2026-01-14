# A basic observations-on-samples csv

A basic case of multiple observed properties on a featureOfInterest

I had difficulty modelling this in csvw, due to a bug in csvwlib related to valueUrl, [bug is fixed](https://github.com/DerwenAI/csvwlib/pull/4) in latest csvwlib (not on pypi yet). Some more optimisations are available in the [latest branch of this fork](https://github.com/pvgenuchten/csvwlib/tree/latest).

Notice that a lot of virtual columns are added, which define relations between the various entities in sosa

**SOSA/SSN**

[SOSA/SSN](https://www.w3.org/TR/vocab-ssn/) is a set of ontologies to describe observation data, based on the [OMS conventions](https://www.ogc.org/standards/om/). 

```
pip install csvwlib
csvwlib --meta http://localhost:8080/obs.csv-metadata.json -f ttl --out data.ttl
```
Test the ttl using [SOSA SHACL](https://github.com/KnowWhereGraph/KWG-SHACL/raw/refs/heads/main/shacl_sosa.ttl) and [pySHACL](https://pypi.org/project/pyshacl/)
```
pyshacl -s https://github.com/KnowWhereGraph/KWG-SHACL/raw/refs/heads/main/shacl_sosa.ttl -m -i rdfs -a -j -f human data.ttl
```

**Schema.org**
```
pip install csvwlib
csvwlib --meta http://localhost:8080/obs.csv-schema-org-metadata.json --out data.jsonld
```
Test the json in [schema.org validator](https://validator.schema.org)

---

Run a webserver at the current folder (npx httpserver) to be able to call the files as url's.


