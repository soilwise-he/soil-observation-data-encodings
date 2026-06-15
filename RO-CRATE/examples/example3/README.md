# a ARC style ro-crate

ro-crate according to [ARC profile](https://github.com/nfdi4plants/arc-ro-crate-profile)

Validation in roc-validator fails with:

- [Violation]: The 1 occurrence of the JSON-LD key "executesLabProtocol" is not allowed in the compacted format because it is not present
in the @context of the document [ ro-crate-1.1_2.3 ] File Descriptor JSON-LD must be flattened: Check if the file descriptor is flattened
Detected issues
- [Violation]: RO-Crate file descriptor "ro-crate-metadata.json" is not fully flattened at entity
"studies/study_01.csv#sample_root_N_low_01"
- [Violation]: entity "{'@type': 'PropertyValue', 'name': 'Sampling Location Source', 'value': "Gedefinieerd in study_01.csv onder kolom
'Characteristics[Location]'", 'valueReference': {'@id': 'studies/study_01.csv'}}" is not a valid node object reference: it MUST have only @id, but no other properties.