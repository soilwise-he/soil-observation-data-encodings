# Example 1; a ro-crate with csvw

A basic ro-crate delegating the semantics to the csvw context file,

This setup validates in [roc-validator](https://pypi.org/project/roc-validator/)

no single tooling seems to exist to parse a ro-crate including embedded csvw, however it can be managed in a 2 step process. practical examples of this include: Language Data Commons of Australia (LDaCA): They use RO-Crates to make massive linguistic datasets accessible. In their Jupyter Notebook analysis environments, a script first scans the RO-Crate and then automatically extracts the correct [columns](https://www.ldaca.edu.au/resources/user-guides/crate-o/convert-spreadsheet/#columns) and data types via the CSVW standard to feed text analytics workflows. The Helmholtz Metadata Collaboration (HMC): In their Zeitgeist project (within the energy research domain), the backend supplies data as an RO-Crate, where the internal time series and measured values ​​are semantically described and loaded specifically via the CSVW standard.
