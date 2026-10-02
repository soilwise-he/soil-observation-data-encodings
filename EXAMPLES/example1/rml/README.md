# RML mapping for SOTER-Eastern Europa database

The startingpoint is a dataset [soveur.csv](./soveur.csv), which has been exported from the [SOTER Eastern Europe dataset](https://data.isric.org/geonetwork/srv/metadata/b1fa4988-b511-48e3-9548-3c48f0a908fa). This database is made available by ISRIC - World Soil Information under a CC-BY-3.0 license.

Initial mapping by chatgpt, based on report https://files.isric.org/public/documents/isric_report_2013_04.pdf
further improved by authors

The structure of the graph:

``` 
Profile
   │
   ├── latitude
   ├── longitude
   ├── elevation
   │
   └── Horizon
          │
          ├── upperDepth (HBUP)
          ├── lowerDepth (HBDE)
          ├── designation (HODE)
          │
          └── Observation
                 ├── PHAQ
                 ├── PHKC
                 ├── TOTC
                 └── ...
```