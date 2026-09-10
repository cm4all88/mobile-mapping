# Parametrix MX60 Mobile Mapping SOP

**Status:** Draft in progress. Revision 0.4, 2026-09-10.

## Contents

| § | Section | Status |
|---|---|---|
| — | [Front matter](00-front-matter.md) | Draft |
| 1 | [Purpose and Scope](01-purpose-and-scope.md) | Draft |
| 2 | [Mobile Mapping in Plain Language](02-mobile-mapping-in-plain-language.md) | Draft |
| 3 | [System Components](03-system-components.md) | Draft |
| 4 | [Workflow at a Glance](04-workflow-at-a-glance.md) | Draft |
| 5 | [Pre-Field Planning](05-pre-field-planning.md) | Draft |
| 6 | [Equipment Preparation and Vehicle Installation](06-equipment-preparation-and-installation.md) | Draft |
| 7 | [Starting the System and TMI](07-starting-the-system-and-tmi.md) | Draft |
| 8 | [Initialization](08-initialization.md) | Draft |
| 9 | [Collecting Data and Monitoring](09-collecting-and-monitoring.md) | Draft |
| 10 | [Ending a Collection](10-ending-a-collection.md) | Draft |
| 11 | Data Handling | Not started |
| 12 | Office Workflow (TBC) | Overview only — TBC Technical Notes (2022) predates MX60 support |
| 13 | Quality, Control and Limits | Not started |
| 14 | Troubleshooting | Not started |
| A–E | Appendices: checklists, glossary, training exercise | Not started |

This is the trimmed structure — 14 sections plus appendices, consolidated from the
original 28-section outline. Trajectory, point cloud quality, imagery quality, control
and QC are told once in Section 13 rather than five times across five sections.

## Reference data

`../reference/mx60-reference-data.csv` — 272 structured records of every specification,
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
| Trimble Mobile Imaging Software User Guide | **Rev L, April 2026** (P/N T001242) | 56 |
| Trimble MX60 User Guide | Rev B, May 2025 (P/N T001983) | 68 |
| Trimble MX60 Quick Start Guide | Rev B, March 2025 | 16 |
| Trimble MX60 Spec Sheet | PN 022516-737C (04/25) | 4 |
| Trimble MX Shock Absorbing Mounting Rack User Guide | Rev B, May 2025 (P/N 37000001) | 10 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60 | January 2025 | 3 |
| Trimble Business Center Technical Notes: For Mobile Mapping | October 2022 | 8 |
| Queensland TMR, Mobile Laser Scanning Technical Guideline | March 2023 (CC BY 4.0) | 65 |
| NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data | 2024 | 211 |

Full assessment: [`../analysis/STAGE-1-SOURCE-ANALYSIS.md`](../analysis/STAGE-1-SOURCE-ANALYSIS.md)

## Still needed

- **Current TBC mobile mapping documentation.** The supplied TBC Technical Notes is dated
  October 2022 and lists raw import from MX7/MX50/MX9 only — MX60 support reached TMI in
  December 2024. Section 12 can describe the workflow shape but not current procedure.
- **Trimble GAMS Antenna Kit** and **DMI Installation & Operation** manuals, if those
  accessories are fitted.
- **Parametrix logo in vector form.** Raster PNGs are in `../brand/`; vector (SVG/EPS)
  and a reversed version for dark backgrounds should be requested before print issue.
