# RML with Morph_kgc

RML is yet another approach to convert CSV into triples

Morph-kgc is a rml tool from the python ecosystem

morph-kgc requires a .ini file with basic parameters and a .ttl mapping file

then call the serialization with:

``` 
pip install morph-kgc
python -m morph_kgc config.ini
``` 

morph-kgc produces n-quads or n-triples, if you need to convert to ttl, use:

``` 
python -c "from rdflib import Graph; g=Graph(); g.parse('output.nt', format='nt'); g.serialize('output.ttl', format='turtle')"
```
