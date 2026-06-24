
# An experiment on using existing bonares (meta)data for soilwise interoperability (Signal database Bonares)

Harmonize a Bonares dataset with 4 tables using Soilwise harmonization guidance/tooling.

The [BonaRes SIGNAL](https://doi.org/10.20387/bonares-4984-ZWYR) dataset has been downloaded from bonares platform under a CC-BY license (attribution: [Marcus Schmidt](https://orcid.org/0000-0002-5546-5521) University of Goettingen, PTS)
 
- the metadata with table schema is available as *.bonares.json
- the cswv as -metadata.json

We selected 4 tables from the [signal database](https://doi.org/10.20387/bonares-4984-ZWYR) for this experiment

## bonares.py

[bonares.py](../../bonares.py) is a script which generates a csvw context or metadata file for a set of related csv's in a folder.

Run bonares.py as:

```python
python bonares.py examples/bonares1
```

The script will write a [csvw context file](./csv-metadata.json) in examples/bonares1. Use [csvwlib](https://pypi.org/project/csvwlib/) to serialise the csvw as rdf.