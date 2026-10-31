---
title: suggestion for an alignment of sosa with schema.org 
description: an extension of chapter 7 in https://w3c.github.io/sdw-sosa-ssn/ssn/, similar to the DOLCE-alignment
---

### 7.2.4 Schema.org Alignment Module

This section introduces the alignment of SOSA with Schema.org.

Schema.org is a vocabulary for structured data on the Web, widely used to describe entities and their properties in web pages and other data sources. 
Schema.org provides the class `schema:Observation` for describing observations about an entity at a particular time. Its properties include `schema:observationAbout`, 
`schema:measuredProperty`, `schema:observationDate`, `schema:value`, and `schema:measurementTechnique`.

The Schema.org Observation class provides a useful correspondence with SOSA for publishing observation data on the Web. In particular, Schema.org properties 
can be used to describe the feature of interest, observed property, time, and result associated with a SOSA observation.

There is, however, a distinction between the two models. SOSA models an observation as an execution, whereas Schema.org primarily provides a 
description of an observation and its associated information. Consequently, the alignment should be understood as an application-level correspondence, 
rather than an assertion that the two classes have identical semantics.

The Schema.org alignment may be used to integrate observation data published using Schema.org with data structured using SOSA.

The ontology IRI of the Schema.org Alignment module is `http://www.w3.org/ns/sosa/schema`

The version IRI of the Schema.org Alignment module 2026 edition is `http://www.w3.org/ns/sosa/2026/schema`

#### 7.2.4.1 Namespaces

The following namespace prefixes are used in the alignment of SOSA with Schema.org.

sosa:  
&nbsp;&nbsp;&nbsp;&nbsp;`http://www.w3.org/ns/sosa/`

schema:  
&nbsp;&nbsp;&nbsp;&nbsp;`https://schema.org/`

#### 7.2.4.2 Class Alignments

The principal class from Schema.org is `schema:Observation`. It describes an observation about an entity at a particular time, potentially including a measured 
property and its value.

A Schema.org observation can be interpreted as corresponding to a `sosa:Observation`, provided that it describes an actual observation event rather than merely 
a statistical statement or an aggregate description.

The correspondence is therefore:

* `schema:Observation` ↔ `sosa:Observation` (application-level correspondence; not an OWL equivalence assertion).

#### 7.2.4.3 Property Alignments

The following properties from Schema.org have correspondences with SOSA properties.

* `schema:observationAbout` ↔ `sosa:hasFeatureOfInterest`
* `schema:measuredProperty` ↔ `sosa:observedProperty`
* `schema:observationDate` ↔ `sosa:phenomenonTime` (where the date denotes the time of the observed phenomenon)
* `schema:measurementTechnique` ↔ `sosa:usedProcedure` (where the technique identifies a procedure)
* `schema:measurementMethod` ↔ `sosa:usedProcedure` (where the method identifies a procedure)
* `schema:value` ↔ `sosa:hasSimpleResult` (for literal values)

The properties `schema:unitCode` and `schema:unitText` can be used to describe the unit associated with a quantitative result. SOSA does not prescribe 
a particular unit-of-measurement vocabulary, so these properties may be retained alongside the SOSA result.

The Schema.org property `schema:variableMeasured` can also provide information about the observed property, although it is broader in scope and may 
describe variables measured across a dataset rather than an individual observation.

#### 7.2.4.4 Explanations

The alignment of `schema:observationAbout` with `sosa:hasFeatureOfInterest` reflects the fact that both properties identify the entity or feature to 
which an observation relates.

Similarly, `schema:measuredProperty` identifies the property being measured and thus corresponds closely to `sosa:observedProperty`.

The distinction between `schema:observationDate` and the SOSA temporal properties deserves particular attention. Schema.org uses `observationDate` 
to indicate the date of an observation. SOSA distinguishes the time of the observed phenomenon (`sosa:phenomenonTime`) from the time at which the 
result was generated (`sosa:resultTime`). Accordingly, `schema:observationDate` should only be mapped to `sosa:phenomenonTime` when it actually 
denotes the phenomenon time. If it instead denotes the time at which the observation result was generated, `sosa:resultTime` is the more appropriate correspondence.

The Schema.org property `schema:value` can represent a Boolean, number, text, qualitative value, or structured value. SOSA distinguishes between 
`sosa:hasSimpleResult`, for literal results, and `sosa:hasResult`, for results represented by resources. Therefore, the correspondence with `sosa:hasSimpleResult` 
applies only to literal values. Structured results should be represented using `sosa:hasResult` where appropriate.

Finally, `schema:measurementTechnique` and `schema:measurementMethod` describe techniques and methods used in making measurements. They can correspond to 
`sosa:usedProcedure` when their values identify an actual procedure. Where these properties contain only textual descriptions of a technique, the correspondence 
is informational rather than a direct property mapping.

#### 7.2.4.5 Example

An example of an observation expressed in schema.org:

```json
{
  "@context": {
    "schema": "https://schema.org/"
  },
  "@type": "schema:Observation",
  "schema:observationAbout": {
    "@type": "schema:Place",
    "schema:name": "Wageningen"
  },
  "schema:measuredProperty": {
    "@id": "https://schema.org/temperature"
  },
  "schema:observationDate": "2026-10-31",
  "schema:value": 15.2,
  "schema:unitCode": "CEL"
}
```

#### 7.2.4.6 Dataset and PropertyValue Alignments

In addition to representing individual observations, Schema.org provides a mechanism for describing the variables measured in a dataset. The property `schema:variableMeasured` can be used on a `schema:Dataset` to indicate the variables measured in that dataset. Its values can be represented using `schema:PropertyValue`, which allows a variable to be described as a property–value pair, or using `schema:StatisticalVariable`.

This provides an additional correspondence with SOSA/SSN. Whereas `schema:Observation` describes an individual observation, `schema:PropertyValue` can be used to describe measured variables at the dataset level, without requiring each measurement to be represented as an individual observation.

The following correspondences are relevant:

* `schema:Dataset` ↔ `sosa:ObservationCollection` (application-level correspondence, where the dataset groups observations).
* `schema:variableMeasured` ↔ `sosa:observedProperty` (at the level of the variables represented in a dataset).
* `schema:PropertyValue` ↔ a description of an observed property and its associated metadata, rather than an observation itself.

It should be noted that `schema:variableMeasured` is also available on `schema:Observation`. In this context, Schema.org additionally provides `schema:measuredProperty`, which identifies the particular property measured, typically through a `schema:StatisticalVariable`.

Consequently, `schema:PropertyValue` should not be considered equivalent to `sosa:Observation` or `sosa:Result`. Rather, it provides a complementary means of describing the variables and their associated metadata in Schema.org dataset descriptions.