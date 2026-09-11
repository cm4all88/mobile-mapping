# Mobile Mapping Standard Operating Procedure
## Trimble MX60 · Trimble Business Center 2026.10

**Revision 1.0 — first complete draft, 2026-09-11**

> ## This document contains no adopted Parametrix policy.
>
> Every Parametrix procedure is marked **PROPOSED**. Every acceptance threshold is marked
> **PARAMETRIX DECISION REQUIRED**. [Appendix H](appendix-H-decision-adoption-record.md) is empty,
> and that is correct on first issue. **Nothing here may be quoted to a client as an existing
> Parametrix standard.**
>
> [**Appendix I**](appendix-I-open-items.md) is the backlog — **74 open items**, 30 at P1, **9 that
> genuinely block operation**, with a six-round sequence for working through them.

## Read

| | |
|---|---|
| **[Assembled document](MX60-SOP-COMPLETE.md)** | Everything in one file — **~69,000 words** |
| [Front matter](00-front-matter.md) | Status, reading paths, contents |
| [Architecture](00-ARCHITECTURE.md) | Build specification — **read before editing any section** |

## Contents

### Part I — Orientation

| § | Section |
|---|---|
| 1 | [Purpose and Scope](01-purpose-and-scope.md) |
| 2 | [Mobile Mapping in Plain Terms](02-mobile-mapping-in-plain-terms.md) |
| 3 | [Roles and Responsibilities](03-roles-and-responsibilities.md) |
| 4 | [Equipment and Software](04-equipment-and-software.md) |

### Part II — Before the field

| § | Section |
|---|---|
| 5 | [Coordinate Systems, Control, and Project Setup](05-coordinate-systems-control-and-project-setup.md) |
| 6 | [Mission Planning](06-mission-planning.md) |
| 7 | [Field Preparation and Preflight](07-field-preparation-and-preflight.md) |

### Part III — Acquisition

| § | Section |
|---|---|
| 8 | [MX60 Data Collection](08-mx60-data-collection.md) |
| 9 | [Field Quality Checks](09-field-quality-checks.md) |
| 10 | [Data Transfer and Project Organization](10-data-transfer-and-project-organization.md) |

### Part IV — Office processing

| § | Section |
|---|---|
| 11 | [Import into TBC](11-import-into-tbc.md) |
| 12 | [Trajectory Processing](12-trajectory-processing.md) |
| 13 | [Generate Scans](13-generate-scans.md) |
| 14 | [Calibration](14-calibration.md) |
| 15 | [**Registration**](15-registration.md) |
| 16 | [Run to Run Registration](16-run-to-run-registration.md) |
| 17 | [Control and Independent Check Points](17-control-and-independent-check-points.md) |
| 18 | [Point Cloud QC](18-point-cloud-qc.md) |
| 19 | [Imagery QC](19-imagery-qc.md) |
| 20 | [Degraded GNSS Conditions](20-degraded-gnss-conditions.md) |
| 21 | [Cleanup Mobile Mapping Mission](21-cleanup-mobile-mapping-mission.md) |

### Part V — Delivery and closeout

| § | Section |
|---|---|
| 22 | [Export and Deliverables](22-export-and-deliverables.md) |
| 23 | [Data Provenance and Audit Trail](23-data-provenance-and-audit-trail.md) |
| 24 | [Final QA/QC](24-final-qa-qc.md) |
| 25 | [Archiving and Records](25-archiving-and-records.md) |
| 26 | [Troubleshooting](26-troubleshooting.md) |
| 27 | [Terminology](27-terminology.md) |

### Appendices

| | Appendix |
|---|---|
| A | [**Working Checklists**](appendix-A-checklists.md) — 13 standalone checklists |
| B | [TMI Status and Warning Reference](appendix-B-tmi-status-reference.md) |
| C | [Trimble Source Index](appendix-C-trimble-source-index.md) |
| D | [First-Week Training Exercise](appendix-D-training-exercise.md) |
| G | [Figure List and Placeholders](appendix-G-figures.md) |
| H | [Decision Adoption Record](appendix-H-decision-adoption-record.md) — **empty by design** |
| I | [**Open Decisions, Field Tests, and Vendor Questions**](appendix-I-open-items.md) — the backlog |

## The findings this document is built on

| Finding | § |
|---|---|
| The trajectory is the job; every point inherits its error | 2.1 |
| Bad mobile mapping data looks fine — error is correlated in stretches, not scattered | 2.3 |
| Import creates an index, not data; covered distance is the cheapest completeness check | 11.1, 11.4 |
| **MX60 antenna model must read `Trimble 112735`** | 12.3 |
| SBET filename is a processing-path **indicator**, not a verdict | 12.4 |
| Trajectory RMS colouring — the highest-value, lowest-effort QC view | 12.4, 18.4 |
| **Registration does not modify the point cloud until Update Scans is run** | 13.6, 22.2 |
| Calibration is periodic, not per-project; boresight error scales with range | 14 |
| **Good RMS does not prove success; bad RMS proves failure; look at the data** | 14.3, 18.1 |
| The three registration commands are not interchangeable | 15.1 |
| **Local registration does not extrapolate** beyond the outermost control | 15.5 |
| Target-Bundle Adjustment reads backwards — checked is coarser | 15.7 |
| Use XY / Use Z / As Check, and why not everything can be a check | 17.2 |
| Sparse spot-checking misses localised degradation | 18.5, 24 L7 |
| **Scan Color rendering** — two surfaces 4 cm apart look like one 4 cm thick | 18.5 |
| Corrupted imagery exports as **black**, silently | 19.4 |
| Two of three degraded-GNSS remedies must be arranged before driving | 20.3 |
| **Cleanup is destructive and not undoable** | 21 |
| **Export provenance limitation — partly confirmed** | 22.7, 23.4 |
| POSPac licence gates trajectory processing and PFIX | 4.4, 12.1 |

## Evidence base

- `../reference/mx60-reference-data.csv` — **402 records. The authority for numbers.**
- `../analysis/` — source inventories, batches 1–7
- `../sources/` — 39 Trimble help captures
- `../SOP-v1-superseded/` — the first draft, retained as a text source. **Do not issue.**
