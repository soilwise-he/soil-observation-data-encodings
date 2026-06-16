# ro-crate - ISA/ARC profile

ndfiplant endorses a ro-crate profile adopting aspects of the ISA/ARC community.

ro-crate is an approach to package a data file with metadata, so it becomes machine actionable.
ro-crate focusses on the context in which a data file is procuded. It links the data file to its project, 
experiment setup and workflows.

the ro-crate can be deposited in Zenodo or in dedicated ro-crate hubs

The ISA/ARC profile adds labprocesses from the life sciences, using bioschemas.org. Basic principles such as data-referencing are explained in [this webpage](https://arc-rdm.org/details/documentation-principle/)

A nice visualisation of labprocess is available at <https://bioschemas.org/useCases/LabProcess>

This repository contains some ongoing examples to study different ro-crate implementations, their validation and transformation.

For basic ro-crate creation, use the LDACA [crate-o editor](https://language-research-technology.github.io/crate-o/#/), which allows to select a local folder and start annotating the files present


```mermaid
graph TD

    ARC[ARC RO-Crate]

    ARC --> INV[Investigation]

    INV --> ST1[Study]
    INV --> ST2[Study]
    INV --> WF[Computational Workflow]

    ST1 --> AS1[Assay]
    ST2 --> AS2[Assay]

    AS1 --> LP1[LabProcess]
    AS2 --> LP2[LabProcess]

    LP1 --> S1[Samples]
    LP1 --> D1[Data Files]

    LP2 --> S2[Samples]
    LP2 --> D2[Data Files]

    WF --> PROTO[LabProtocol]
    PROTO --> RUN[Workflow Run / LabProcess]

    RUN --> IN[Input Data]
    RUN --> OUT[Output Data]

    D1 -. used by .-> RUN
    D2 -. used by .-> RUN

    classDef isa fill:#e1f5fe,stroke:#0277bd;
    classDef process fill:#fff3e0,stroke:#ef6c00;
    classDef data fill:#e8f5e9,stroke:#2e7d32;

    class INV,ST1,ST2,AS1,AS2 isa;
    class LP1,LP2,PROTO,RUN process;
    class S1,S2,D1,D2,IN,OUT data;
```

Crate file structure

```mermaid
graph TD

    ARC["ARC Root"]

    ARC --> INV["isa.investigation.xlsx"]
    ARC --> STUDIES["studies/"]
    ARC --> ASSAYS["assays/"]
    ARC --> WFS["workflows/"]
    ARC --> RUNS["runs/"]

    INV --> I["Investigation"]

    STUDIES --> S["Study entities"]
    ASSAYS --> A["Assay entities"]

    WFS --> WP["LabProtocol / Workflow"]
    RUNS --> RP["LabProcess / Workflow Run"]

    S --> LP1["Experimental LabProcess"]
    A --> LP1

    WP --> RP

    RP --> OUT["Derived datasets"]

    LP1 --> RAW["Assay datasets"]
```
