# Parametrix MX60 Mobile Mapping SOP

**Status:** Draft in progress. Revision 0.2, 2026-09-10.

## Contents

| § | Section | Status |
|---|---|---|
| — | [Front matter](00-front-matter.md) | Draft |
| 1 | [Purpose and Scope](01-purpose-and-scope.md) | Draft |
| 2 | [Mobile Mapping in Plain Language](02-mobile-mapping-in-plain-language.md) | Draft |
| 3 | [System Components](03-system-components.md) | Draft |
| 4 | [Workflow at a Glance](04-workflow-at-a-glance.md) | Draft |
| 5 | Pre-Field Planning | Not started |
| 6 | Equipment Preparation and Vehicle Installation | Not started |
| 7 | Starting the System and TMI | Not started |
| 8 | Initialization | Not started |
| 9 | Collecting Data and Monitoring | Not started |
| 10 | Ending a Collection | Not started |
| 11 | Data Handling | Not started |
| 12 | Office Workflow (TBC) | **Blocked** — needs TBC mobile mapping documentation |
| 13 | Quality, Control and Limits | Not started |
| 14 | Troubleshooting | Not started |
| A–E | Appendices: checklists, glossary, training exercise | Not started |

This is the trimmed structure — 14 sections plus appendices, consolidated from the
original 28-section outline. Trajectory, point cloud quality, imagery quality, control
and QC are told once in Section 13 rather than five times across five sections.

## Reference data

`../reference/mx60-reference-data.csv` — 212 structured records of every specification,
limit, requirement, warning, procedure and setting drawn from the Trimble sources.

Each row carries: `id`, `category`, `topic`, `item`, `value`, `notes`, `source`, `page`,
`sop_section`.

The CSV is the **authority for numbers**; the SOP prose explains what they mean. When a
Trimble revision changes a value, update the CSV row.

Categories: `spec` · `limit` · `requirement` · `warning` · `procedure` · `setting` ·
`indicator` · `note` · `conflict` · `resolved` · `contact` · `reference`

## Source documents

| Document | Rev / date | Pages |
|---|---|---|
| Trimble MX60 User Guide | Rev B, May 2025 (P/N T001983) | 68 |
| Trimble MX60 Quick Start Guide | Rev B, March 2025 | 16 |
| Trimble MX60 Spec Sheet | PN 022516-737C (04/25) | 4 |
| Trimble MX Shock Absorbing Mounting Rack User Guide | Rev B, May 2025 (P/N 37000001) | 10 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60 | January 2025 | 3 |
| Queensland TMR, Mobile Laser Scanning Technical Guideline | March 2023 (CC BY 4.0) | 65 |
| NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data | 2024 | 211 |

Full assessment: [`../analysis/STAGE-1-SOURCE-ANALYSIS.md`](../analysis/STAGE-1-SOURCE-ANALYSIS.md)

## Still needed

- **Trimble TMI Software User Guide** — `geospatial.trimble.com/en/links?dcs=Collection-129953`.
  Needed to complete Section 7 (TMI interface detail) and Section 14 (warning reference).
- **TBC mobile mapping module documentation** — blocks Section 12 entirely.
- **Parametrix logo** in vector form, for `../brand/`.
