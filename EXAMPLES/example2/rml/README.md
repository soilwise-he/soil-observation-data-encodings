# R2RML with Morph_kgc

[R2RML](https://www.w3.org/TR/r2rml/) is yet another standardised approach to convert RDB (like postgres, CSV) into triples

[Morph-kgc](https://morph-kgc.readthedocs.io/) is a rml tool from the python ecosystem

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
