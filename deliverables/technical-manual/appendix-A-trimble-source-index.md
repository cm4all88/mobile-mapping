# Appendix A — Trimble Source Index

Every Trimble source cited in this SOP. **`reference/mx60-reference-data.csv` (402 records) is the
authority for numbers**; this document explains what they mean.

## A1 · Manuals and bulletins

| Document | Revision | Cited for |
|---|---|---|
| **Trimble MX60 User Guide** | Rev B, May 2025 (P/N T001983), 68 pp | Hardware, installation, power, safety, specifications, periodic verification |
| **Trimble MX60 Quick Start Guide** | Rev B, March 2025, 16 pp | Field sequence, initialization, capture settings |
| **Trimble Mobile Imaging (TMI) Software User Guide** | **Rev L, April 2026** (P/N T001242), 56 pp | Field software, status, capture settings, calibration import |
| **Trimble MX60 Spec Sheet** | PN 022516-737C (04/25), 4 pp | Specifications |
| **Trimble MX Shock Absorbing Mounting Rack User Guide** | Rev B, May 2025 (P/N 37000001), 10 pp | Vehicle installation |
| **Product Bulletin: Enabling the Dust Filter in TMI for MX60** | January 2025, 3 pp | Dust filter |
| **TBC Technical Notes: For Mobile Mapping** | October 2022, 8 pp | **Predates MX60 support — used with caution** |

## A2 · TBC help portal — **TBC 2026.10**

The captured help documents **TBC 2026.10**, confirmed by cross-reference: a registration feature
listed as new in the 2026.10 release notes is present in the captured topic *(TBC RN 2026.10;
TBC 22905)*. URLs follow `https://help.fieldsystems.trimble.com/tbc/<id>.htm`.

### Understanding and structure

| ID | Topic | Cited in |
|---|---|---|
| 20717 | Understanding Mobile Mapping | 2 |
| 22503 | Mobile Mapping System Data Structure | 2.5, 13.1 |
| 21243-1 | Mobile Mapping Options | 15.3 |
| 22554 | View the Mobile Mapping Data in the Project Explorer | 11.3 |

### Import, view and process

| ID | Topic | Cited in |
|---|---|---|
| 20736-1 | Import the Mobile Mapping Data | 11.3 |
| **22499** | **Generate Mobile Mapping Scans** | 11.4, 13.2–13.5 |
| **22638** | **Update Mobile Mapping Scans** | 13.6, 22.2, 23.3 |
| 22567 | Hide, Display and Center on a Mobile Mapping Trajectory | — |
| 22863 | Go to a Mobile Mapping Station Position | — |
| 20727 | Navigate a long Mobile Mapping Run | — |
| 24024 | Split a Mobile Mapping Run | — |
| 26947 | Define a Region of Interest | — |
| **28155** | **Recover Mobile Mapping Scans** | 13.7, 26.3 |
| 28912 | Display Mobile Mapping Rectified Camera Views | 19 |
| 23856 | Configure your Graphic Card Driver When Using the MTA Correction | **13.1 — does not apply to MX60** |
| **23991_1** | **Run a Mission Report** | 14.6, 17.6, 23.3, 25.2 |

### Register Mobile Mapping Trajectories

| ID | Topic | Cited in |
|---|---|---|
| **22905** | **Register a Run** | 15.2–15.9, 17.2, 22.2, 23.3 |
| **26473** | **Register a Mission** | 15.4, 17.2, 22.2, 23.3 |
| **25096** | **Register Multiple Pairs of Runs** (Register Run to Run) | 16, 18.2–18.3 |
| 25362 | Edit a Run | 15.8, 16.8, 24 L4 |
| 26578 | Edit a Mission | 15.8, 24 L4 |

### Perform Mobile Mapping Calibrations

| ID | Topic | Cited in |
|---|---|---|
| **24886** *(also 20716)* | **Calibrate Mobile Mapping Laser Scanners** | 14.2–14.3, 18.1 |
| 24868 | Calibrate Mobile Mapping Cameras | 14.4, 14.6 |
| 20728 | Perform a Manual Camera Calibration | 14.4 |
| 22920 | Import and Export Mobile Mapping Calibration File (.json) | 14.5 |
| **25943** | **Process Raw Trajectory Data** | 5.3, 10.1, 12.2–12.4, 23.3 |
| **28972** | **LiDAR QC Processing** | 4.5, 12.7, 20.6 |
| 24460 | Generate POSPac Position Fixes | 11.2, 20.5 |
| 27248 | Change the Real-time or Post-processed Trajectory Color Settings | 12.4, 18.4, 22.2 |
| 27415 | View Trajectory Plots | 12.5, 24 L2 |

### Cleanup

| ID | Topic | Cited in |
|---|---|---|
| **26466** | **Cleanup Mobile Mapping Mission** | 21, 23.5, 25.4 |

### Export and publish

| ID | Topic | Cited in |
|---|---|---|
| **11769** | **Export Point Cloud Files** (.e57, .las, .laz, .pod, .pts, .ptx, .rcp, .tdx) | 22.4–22.6.5 |
| **27279** | **Export Mobile Mapping Classified Point Cloud Regions to LAS** | 22.5, 22.6.1 |
| **22501** | **Export to Trimble TMX** | 19.2, 22.3, 22.6.2 |
| **23339** | **Export to TopoDot** | 19.2, 22.3, 22.6.3 |
| **23888** | **Export to Solv3D** | 19.2, 22.6.4 |
| **29527** | **Publish Mobile Mapping Point Cloud Data, Trajectories, and Images to Trimble Connect** | 4.6, 22.6.6 |
| 28963 | Workflow: Publish Point Cloud Data and Panoramic Images to Trimble Connect | **Publish Scan Data — a static-scanner path** |

### Analysis — **not yet ingested**

The TBC Mobile Mapping navigation tree carries a group of analysis and product-making commands that
this document set does not cover. They are listed here so the gap is visible rather than silent,
and they are tracked as **T32** and **T33**.

| ID | Topic | Status |
|---|---|---|
| **29599** | **Run a Boeing Bump Index (BBI) Report** | Cited for the capability. **The workflow has not been run here** — T32 |
| — | Inspect Pavement Condition | Not ingested — T33 |
| — | Create CAD Entities on Mobile Mapping Data | Not ingested — T33 |
| — | Create Orthomosaics from a Trimble Back-Camera Mobile Mapping System | Not ingested — T33 |
| — | Import Ortho Lane Images | Not ingested — T33 |
| — | Import and Export Road Segments in AgileAssets | Not ingested — T33 |
| — | Run a Batch Command | Not ingested — T33 |

> **This is the downstream half of the module** — the part that turns a registered point cloud into
> a deliverable. The set explains how to produce the cloud and stops there. Source for the list:
> `sources/tbc-help-captures/_nav-tree-mobile-mapping.png`.

### MX7-only exporters — **do not apply to the MX60**

| ID | Topic | Why excluded |
|---|---|---|
| 20926 | Station Positions and Panorama Orientations (.xml) | **"MX7 Export to XML Horus"** — converts PGR files from an MX7 360° camera |
| 20927_1 | Panoramic Images and Trajectory Files (.csv) | **"MX7 Export to TMX"** — starts from a Trident `.tridb`; 8000 × 4000 px panorama |
| 21713_1 | Cubical Images and Trajectory Files (.csv) | **"MX7 Export to Mapillary"** — same panorama size |

> **The MX7 panorama is 8000 × 4000 px; the MX60 is 8192 × 4096 (Core) or 12288 × 6144
> (Pro/Premium).** Pixel counts are a reliable way to tell which system a TBC topic describes when
> the title does not say.

### Release notes

| Release | Cited for |
|---|---|
| **2025.21** | Signed GCP residuals "in the report"; Publish to TRCPS; Smart Picking window instability; licence eligibility |
| **2026.10** | Direct residuals to GCP **(the version cross-reference)**; dynamic datum epoch; two-step verification; dark theme; Rectified Camera Views naming |

## A3 · Not held, and needed

| Document | Needed for | Item |
|---|---|---|
| **Trimble GAMS Antenna Kit Installation & Operation Manual** | Lever-arm procedure if GAMS is fitted | V-5 |
| **Trimble DMI Installation & Operation Manual** | DMI scale factor for the measured wheel diameter | V-5 |
| **TBC Help: Blur Exported Images** | Imagery privacy procedure | §26.6 — capture when privacy is drafted |

## A4 · Non-Trimble sources — reference only

> **These are cited as examples of how others have answered questions Parametrix has not. They are
> not Parametrix standards and not Trimble requirements.**

| Source | Used for |
|---|---|
| **Queensland TMR, Mobile Laser Scanning Technical Guideline**, March 2023, CC BY 4.0 | An example of a published agency specification for control layout, accuracy tiers, and wet-weather practice — §22.6, the **Field How To** |
| **NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data**, 2024 | Background |

### Held but not cited

Present in the repository and **used for nothing in this document set**. Listed so that the holdings
and the citations agree, and so nobody assumes a statement rests on them:

| Source | Status |
|---|---|
| *3D Reconstruction and Mobile Mapping in Urban Environments Using Remote Sensing*, 4 parts, ~120 MB | Background reading. No statement in any of the four documents derives from it |
| Trimble article, *Informed Infrastructure* Smart Engineering special issue, 2025, 2 pp | Vendor marketing. **Not evidence**, and not to be cited as any |

## A5 · Analysis record

The source ingestion and classification behind this document set. These are **build records in the
repository, not part of the issued documents**:

| Document | Content |
|---|---|
| `analysis/STAGE-1-SOURCE-ANALYSIS.md` | Initial manual assessment |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-2.md` | 16 TBC topics classified |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-3.md` | Chain model tested; the registration gap identified |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-4.md` | Registration and calibration branches; six of eight questions answered |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-5.md` | Export provenance pass; release notes |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-6.md` | Four export topics; **version confirmed as TBC 2026.10** |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-7.md` | Export surface closed; ingestion declared sufficient |
| `analysis/GUIDE-REQUIREMENTS.md` | Branding and comprehension-layer requirements |
| `analysis/VENDOR-QUESTIONS.md` | Vendor question record — mirrored in Appendix I Table 3 |

> Unresolved conflicts between these sources are listed separately in **Appendix G**.
