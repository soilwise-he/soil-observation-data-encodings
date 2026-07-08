
# Curieuzeneuzen in de tuin (DOV) - Soil time-series example

| Metadata | |
| --- | --- |
| source | Databank Ondergrond Vlaanderen (DOV): https://www.dov.vlaanderen.be |
| dataset export date | 2026-06-30 |
| language | Dutch |

This example demonstrates a compact but realistic setup with one location table and high-frequency time-series observations split over monthly files.

It contains:

- **Location metadata** - `Curieuzeneuzen_in_de_tuin.csv` with one monitoring point (`CN_223031_2021`), start/end dates, summary min/max values, links to DOV pages, and coordinates (`X`, `Y`, `Z`) in Lambert72; `Z` is height in mTAW
- **Two observed properties** - separate folders for time-series exports:
	- `meetpunten_bodemlocatie_2021-032627_1911_CN_T1`: temperature series (`Parameter: Temperatuur`)
	- `meetpunten_bodemlocatie_2021-032627_1912_CN_SWC`: volumetric soil moisture series (`Parameter: Volumetrisch vochtgehalte`)
- **Phenomenon time** - timestamps in ISO 8601 with timezone offset (e.g. `2021-04-06T02:00:00.000+02:00`)
- **Sampling interval** - 15-minute observations in monthly CSV files (`202104.csv` to `202110.csv`)
- **Sensor/instrument metadata** - per file header lines include sensor identification and instrument validity window
- **Data quality indicator** - third value column appears to be a quality/status flag (typically `1`)

Notes for encoding:

- Coordinate reference system is Lambert72; elevation is expressed as mTAW.

