# Soil Data Standards
When discussing soil data models confusion often arises as there are three different models to choose from (INSPIRE, ISO 28258, GloSIS). However, upon closer examination, it becomes clear that these models are very closely related. All three models utilize the Observations and Measurements standard for provision of soil data values. The minor differences between these three models pertain to the spatial features defined for representing parts of soils.
## INSPIRE
The first of these data models is the INSPIRE Soil model, defined under the European INSPIRE Initiative. The main spatial features defined in this model are:
- Soil site: area within a larger survey, study or monitored area, where a specific soil investigation is carried out.
- Soil plot: spot where a specific soil investigation is carried out.
- Soil profile: description of the soil that is characterized by a vertical succession of profile elements. Specialized into
  - Observed soil profile: a representation of a soil profile found on a specific location which is described on the basis of observations in a trial pit or with a borehole.
  - Derived soil profile: non-point-located soil profile that serves as a reference profile for a specific soil type in a certain geographical area.
- Profile element: An abstract spatial object type grouping soil layers and / or horizons for functional/operational aims. Specialized into
  - Soil horizon: Domain of a soil with a certain vertical extension, more or less parallel to the surface and homogeneous for most morphological and analytical characteristics, developed in a parent material layer through pedogenic processes or made up of in-situ sedimented organic residues of up-growing plants (peat).
  - Soil layer: domain of a soil with a certain vertical extension developed through non-pedogenic processes, displaying a change in structure and/or composition to possibly over- or underlying adjacent domains, or a grouping of soil horizons or other sub-domains with a special purpose.
- Soil derived object: A spatial object type for representing spatial objects with soil-related property derived from one or more soil and possibly other non soil properties.
- Soil body: Part of the soil cover that is delineated and that is homogeneous with regard to certain soil properties and/or spatial patterns.

While the INSPIRE model formally specifies Observations only on the spatial features SoilSite, SoilProfile, ProfileElement and SoilDerivedObject, nothing hinders applying Observations to any feature type, so not only limited to the 4 types listed.

<img width="649" height="597" alt="INSPIRE Soil" src="https://github.com/user-attachments/assets/d2e1a67b-9794-458c-a9c0-bcd9294d7b17" />
INSPIRE Soil Spatial Feature Types

## ISO 28258
ISO 28258:2013 - Digital exchange of soil-related data describes how to digitally exchange soil-related data. This model is a refinement of the INSPIRE model described above, also utilizing the Observations and Measurements standard for provision of soil data values. While relying on the same cascade of the spatial features Site, Plot, Profile and Profile Elements (Layers and Horizons) defined under INSPIRE, there are some subtle refinements. The derived types have been removed, replaced by soil mapping. Divergences from INSPIRE as follows:
- Project: The project holds the background information for soil studies. A project does not describe the soil as such. It is of importance to exchange project data along with other soil quality data in order to know the aim and circumstances of data collection. The project provides the context of the data collection as a prerequisite for the proper use or reuse of these data.
The project information also may be the starting point to retrieve further information that cannot be exchanged using soil quality. For example, the name of an author or the project number may be the key for finding a report or decision document.
- Soil Plot is further specialized as follows:
  - Surface: Surface is a subtype of a plot with surface shape. Surfaces may be located within other surfaces.
  - Trial pit (test pit, trench): excavation prepared to carry out profile descriptions, sampling, and/or field tests. Trial pit is a subtype of a plot with point shape. A trial pits may have an associated soil profile. TrialPit represents the location of a dug soil opening made to observe the soil.
  - Borehole: penetration into the  subsurface with removal of soil/rock material by using e. g. a hollow tube-shaped tool. Synonyms : Boring and bore. Borehole is a subtype of a plot with point shape. A boreholes may have an associated profile.
- Soil specimen: Soil specimen is a subtype of SF_Specimen. Soil specimen may be taken in the Site, Plot, Profile, or ProfileElement including their subtypes.
- Analysis requeset: AnalysisRequest is a description of an analysis which should be carried out on soil specimens.
- Soil Mapping consists of the following types, linked to typical profiles (see diagram below for relations):
  - SoilMap: SoilMap is a soil map or soil map series with unified classification of soil mapping units and soil typological units.
  - SoilMappingUnitCategory: Soil mapping unit category is a map legend category used for grouping soil mapping units or another categories. Each category is either root category of a map or subcategory of another category. Concerning this, each category is related exactly to one map through root category of the tree structure (see subcategory).
  - SoilMappingUnit (SMU): Soil mapping unit is a map legend category with unique map symbol within the soil map. Each mapping unit is related exactly to one map (through category tree). Mapping unit may represent one or more soil typological units, whereas soil typological unit may occur within one or more mapping units.
  - SoilTypologicalUnit (STU): Soil typological unit is a non-spatial unit of systematically similar soils. Each typological is related exactly to one map (see constraint).

<img width="945" height="522" alt="grafik" src="https://github.com/user-attachments/assets/2e19aa58-b376-47e7-9efc-ce5eafa1f7c6" />
ISO 28258 Soil Mapping

## GloSIS (FAO Global Soil Information System)
GloSIS is a further refinement of ISO 28258 implemented by the FAO under the Global Soil Partnership. Leaving the spatial features untouched, GloSIS focuses on defining Observable Properties for which soil data is to be provided, together with applicable Observing Procedures, detailing how these Observable Properties have been ascertained.
It is often difficult to understand which Observable Properties apply to which spatial object when utilizing Observations and Measurements, as theoretically, any type of Observation can be applied to any spatial object. Under GloSIS, this was constrained through the use of helper classes that clearly tie Observable Properties to specific spatial features, as shown in the example of the Surface feature type in the diagram below.

<img width="945" height="704" alt="grafik" src="https://github.com/user-attachments/assets/dcdcc7c3-3222-4024-a70b-eb41afc19495" />
GloSIS Surface Helper Classes illustrating applicable Observations.

Under the SIEU-Soil Project, [GloSIS was refined to an Ontology](https://glosis-ld.github.io/glosis/), retaining all relations defined under the UML version.


