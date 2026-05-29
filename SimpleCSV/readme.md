# Simple CSV
As a very simple approach to providing soil data, we describe an approach where all data is stored within a set of CSV files or a single excel sheets with tabs:
- Metadata: general metadata applicable to the entire dataset. Includes concepts like CRS for spatial data
- Observable Properties: list of all column headers describing an observed property. Includes methodology, Unit of Measurement, sample preparation. If the same property is provided using 2 methodologies, one entry must be provided per methodology
- Samples: description of the samples on which observations are made, samples refer to the features of interest (site, plot, profile, layer/horizon, sample)
- Data: the values, columns describe Observable Properties, rows describe Samples or Sites where observations are made on

## Diagram

```mermaid
erDiagram 
    Metadata ||--|{ Data : describes
    ObservableProperties ||--|{ Data : defines
    Samples ||--|{ Data : locates
    Data
    Metadata {
        string property
        string value
    }
    ObservableProperties {
        string Column-name
        string Variable
        string Variable-URI
        string Unit
        string Unit-URI
        string Methodology
        string Methodology-URI
    }
    Samples {
        string Identification	
        number X	
        number Y	
        number Upper-Depth	
        number Lower-Depth	
        string Feature-of-Interest
    }
    Data {
        string Sample-ID
        string Column1
        string Column2
    }
```
