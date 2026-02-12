## Common Elements across encodings

While SoilWise supports an array of different encodings, each tailored for different usage areas, these models are united through the underlying conceptual [OGC/ISO Observations, Measurements and Samples Standard](https://www.ogc.org/standards/om/), 
semantically formalized under [W3C SSN/SOSA](https://w3c.github.io/sdw-sosa-ssn/ssn/). This model entails the use of the Observation concept, that unites:
- Feature of Interest: target of the Observation, what exactly is being Observed
- Result: the actual value being conveyed by the Observation, e.g. a value representing Bulk Density, Organic Carbon, pH at the Feature of Interest
- Observational Metainformation:
  - Observed Property: what exactly was being Observed, e.g. Bulk Density, Organic Carbon, pH
  - Observing Procedure: how was this property ascertained, what methodology was used
  - Unit of Measurement: in what unit is the result being conveyed
  - Additional concepts, e.g. Sensor used in measurement, Host at which this Sensor was deployed... Currently not being utilized in SoilWise

### Special Relationship between Observed Property, Observing Procedure and UoM

In previous versions of OMS and SOSA, the only relation between Observed Property, Observing Procedure and UoM was provided through actual Observations utilizing these concepts.
This deficit was recognized in recent updates of both OMS and SOSA, new properties proposed. This enables direct links between Observed Property, Observing Procedure, and via QUDT we can add information on the UoM.

_We still need to discuss which exact properties and inverses we use_

<img width="659" height="413" alt="grafik" src="https://github.com/user-attachments/assets/7141ec42-e538-419a-b7dd-45d514fdd225" />



### Conversion between UoM

Different organizations traditionally survey data with different units of measurement. A simple example pertains to length, some report this in meters, some in centimeters.
As lossless conversion between SI units is trivial, there is no reason to mandate the exact UoM to be used, only the category. Initial attempt at utilizing QUDT Dimensions failed, as too many units become dimensionless (e.g. mg/g or ml/l).
We thus agreed to use the QUDT unit utilizing SI base units as far as possible, provide conversion factors from the unit provided to this base unit, enabling conversion between all units referencing the same base unit.

Details on this work are currently available via the [GPkg Repo UoM Conversion Table](https://github.com/soilwise-he/Geopackage-so/blob/main/geopackage/UoM/readme.md).

### Common Repo for Observed Property, Observing Procedure and UoM

In order to keep all data encoding models open for the future, they must be very flexible in the use of Observed Property, Observing Procedure and UoM, as these lists will never be finalized, will continue to grow and evolve.
In online environments, systems can rely on interactive codelists referenced by URIs for these concepts, but with standalone systems (e.g. GPkg for Field Survey), 
the system must be pre-filled with the relevant concepts, required Observed Property, Observing Procedure and UoM imported to the system before data entry commences.

In order to enable this, we propose the definition of unique IDs (unclear if GUIDs, W3IDs or ...?) for each Observed Property, Observing Procedure and UoM, their maintanance within a central registry or repository.
Through the unique IDs, partial updates of existing systems with new concepts becomes quite simple.

In addition, as we have links between Observed Property, Observing Procedure and UoM, data entry systems can take this into account. 
Once a user has selected an Observed Property, the Observing Procedure and UoM options provided are limited to those aligned with the selected Observed Property.
