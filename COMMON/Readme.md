## Common Elements across encodings for observation data

While SoilWise supports an array of different encodings for observation data, each tailored for different usage areas, these models are united through the underlying conceptual [OGC/ISO Observations, Measurements and Samples Standard](https://www.ogc.org/standards/om/), 
semantically formalized under [W3C SSN/SOSA](https://w3c.github.io/sdw-sosa-ssn/ssn/). This model entails the use of the Observation concept, that unites:
- Feature of Interest: target of the Observation, what exactly is being Observed
- Result: the actual value being conveyed by the Observation, e.g. a value representing Bulk Density, Organic Carbon, pH at the Feature of Interest
- Observational Metainformation:
  - Observed Property: what exactly was being Observed, e.g. Bulk Density, Organic Carbon, pH
  - Observing Procedure: how was this property ascertained, what methodology was used
  - Unit of Measurement: in what unit is the result being conveyed
  - Additional concepts, e.g. Sensor used in measurement, Host at which this Sensor was deployed... Currently not being utilized in SoilWise

## Observed Property++

### Special Relationship between Observed Property, Observing Procedure and UoM

In previous versions of OMS and SOSA, the only relation between Observed Property, Observing Procedure and UoM was provided through actual Observations utilizing these concepts.
This deficit was recognized in recent updates of both OMS and SOSA, new properties proposed. This enables direct links between Observed Property, Observing Procedure, and via QUDT we can add information on the QuantityKind to determine applicable UoM.

_We still need to discuss which exact properties and inverses we use_

<img width="1275" height="519" alt="ObsPropProcModel" src="https://github.com/user-attachments/assets/400b7d8f-d046-4be4-aa89-0e145a0e2b1b" />

### Conversion between UoM

Different organizations traditionally survey data with different units of measurement. A simple example pertains to length, some report this in meters, some in centimeters.
As lossless conversion between SI units is trivial, there is no reason to mandate the exact UoM to be used, only the category, thus the decision to utilize QUDT QuantityKind. When using  QUDT QuantityKind, one must take care not to select dimensionless, but instead provide the correct fraction or ration type (e.g. [MassRatio](https://qudt.org/vocab/quantitykind/MassRatio) for mg/g or [VolumeFraction](https://qudt.org/vocab/quantitykind/VolumeFraction) for ml/l).

### Common Repo for Observed Property, Observing Procedure and UoM

In order to keep all data encoding models open for the future, they must be very flexible in the use of Observed Property, Observing Procedure and UoM, as these lists will never be finalized, will continue to grow and evolve.
In online environments, systems can rely on interactive codelists referenced by URIs for these concepts, but with standalone systems (e.g. GPkg for Field Survey), 
the system must be pre-filled with the relevant concepts, required Observed Property, Observing Procedure and UoM imported to the system before data entry commences.

In order to enable this, we propose the definition of unique IDs (unclear if GUIDs, W3IDs or ...?) for each Observed Property, Observing Procedure and UoM, their maintanance within a central registry or repository.
Through the unique IDs, partial updates of existing systems with new concepts becomes quite simple.

In addition, as we have links between Observed Property, Observing Procedure and UoM, data entry systems can take this into account. 
Once a user has selected an Observed Property, the Observing Procedure and UoM options provided are limited to those aligned with the selected Observed Property.

## Feature-of-Interest types
Under O&M (ISO 19156:2011), there was only the basic Feature-of-Interest (FoI) association between an Observation and it's object of measurement. Over time it became clear that more detail is required here, especially in the case of Specimens that have a different location than the real-world object they are representative of. While it has always been possible to traverse from the actual object of measurement via the sampledFeature association to the real-world object the FoI is representative of, this has often caused issues in correctly identifying Observations and their context. In the update from O&M to OMS leading to ISO 19156:2023 (as well as under the ongoing SOSA/SSN update), the FoI concept was split into two concepts:
- Proximate FoI: the actual object on which the observation or measurement is performed, e.g. often a sample or specimen
- Ultimate FoI: the real-world object that the Proximate FoI is representative of

### Implication for existing soil standards (e.g. INSPIRE, ISO 28258, GloSIS)
The existing soil data models have all been crafted based on O&M, thus missing the benefits of this extended functionality. 

#### Timeseries for Soil Data
One use case where this can be of help is in creating true time-series for soil data, to date difficult as soil observation tends to be destructive. The result is that one has a set of sort-of co-located profile descriptions with one set of Observations for each individual Profile; the only way of bringing the data on these individual related Profiles to a timeseries is to follow the Feature associations from Profile to Plot to Site and then back down again to find the next Profile. Through utilization of the Ultimate FoI concept and introduction of a SiteTypicalProfile, the Observations can be linked both to the specific Profile (or relevant Layer or Horizon) being measured on as Proximate FoI, as well as to the corresponding element of the SiteTypicalProfile

<img width="1849" height="1079" alt="grafik" src="https://github.com/user-attachments/assets/7690eb8e-a82e-47d8-b6d2-4d777960eeb5" />

#### Keeping Specimens in Context
ISO 28258 includes the concept of Specimen, but no guidance on how to link this to the spatial object from which this specimen was sampled. O&M only provides the sampledFeature association to link a Specimen to its source, but this is not directly clear from the Observation perspective. Utilization of Proximate and Ultimate FoI could help to clarify this, allowing the Observation to indicate both the Specimen (as Proximate FoI) as well as it's source(s) (e.g. both the Layer from which the specimen was taken as well as the Site as Ultimate FoI) 
