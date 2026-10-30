## Conversion tools between SoilWise formats

Within SoilWise, we support different formats, as well as conversion tools between these formats.
<img width="1437" height="811" alt="grafik" src="https://github.com/user-attachments/assets/7bdd8890-689a-4cab-a74d-37710e351202" />

A [conversion API](https://github.com/soilwise-he/data-download/blob/main/README.md) is provided to transform between these formats.

### GPkg -> INSPIRE GML

#### SoilWise GPkg -> INSPIRE GML
<https://github.com/soilwise-he/soil-observation-data-encodings/tree/main/GPKG/gpkg-to-inspire-soil-transformation>

#### EJP-Soil GPkg -> INSPIRE GML
Somewhere in EJP Soil ancient history

#### RANDOM GPkg -> INSPIRE GML

Another implementation is at:
- api: https://api.soilwise-he.eu/csvw/docs
  - MISSING Breadcrumbs on what API aspect to use
  - https://api.soilwise-he.eu/csvw/docs#/default/return_converted_convert_post
- source: https://github.com/soilwise-he/data-download

- Not formally INSPIRE compliant, as not using INSPIRE Model

### INSPIRE GML -> GPkg

https://github.com/soilwise-he/data-download/issues/19

### SoilWise GPkg -> STA

https://github.com/soilwise-he/soil-observation-data-encodings/tree/main/GPKG/gpkg-to-sta-transformation/schemas

### STA -> SoilWise GPkg

Frost server?

### STA -> OMS-Metadata-Table (CSV)

Frost server?
Need some work as STA Native only supports long format, not wide

### STA -> SOSA RDF ?
Bespoke script?

### SOSA RDF -> STA ?
Bespoke script?

### Excel -> OMS-Metadata-Table

Really just storing the OMS-Metadata-Table as a CSV file. May need checks to assure no offending characters in the content, e.g. no newlines, quotes.

- ??? api: https://api.soilwise-he.eu/csvw/docs
- ??? source: https://github.com/soilwise-he/data-download

### OMS-Metadata-Table -> CSVW JSON
Trivial - store tab as CSV (don't forget to first clean offending symbols, e.g. newlines, quotes, ;)

### OMS-Metadata-Table -> R2RML TTL
Trivial - store tab as CSV (don't forget to first clean offending symbols, e.g. newlines, quotes, ;)

### CSVW JSON + Data-Table -> SOSA RDF
- api: https://api.soilwise-he.eu/csvw/docs
- source: https://github.com/soilwise-he/data-download

### R2RML TTL + Data-Table -> SOSA RDF

### ~~SOSA RDF -> OMS-Metadata-Table~~
Not sure we need this, can also transform SOSA -> GPkg -> OMS-Metadata-Table
https://github.com/soilwise-he/data-download/issues/15

### GPKG -> OMS-Metadata-Table



### SOSA-RDF -> GPKG

- api: https://api.soilwise-he.eu/csvw/docs
- source: https://github.com/soilwise-he/data-download

### GPKG -> SOSA-rdf

https://github.com/soilwise-he/data-download/issues/18
