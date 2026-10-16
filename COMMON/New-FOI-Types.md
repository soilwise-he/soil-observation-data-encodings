## New Feature-of-Interest types
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
