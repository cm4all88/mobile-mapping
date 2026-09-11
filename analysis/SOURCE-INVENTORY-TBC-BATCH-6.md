# Source Inventory — Batch 6: the export topics

**Prepared:** 2026-09-11
**Status:** Ingestion and classification. **No rewrite performed.**
**Continues:** [`SOURCE-INVENTORY-TBC-BATCH-5.md`](SOURCE-INVENTORY-TBC-BATCH-5.md)

---

## 0. What arrived, and one housekeeping problem

Four export topics, all legible and all treated as evidence:

| Topic | ID | Category |
|---|---|---|
| **Export Mobile Mapping Classified Point Cloud Regions to LAS (.las)** | 27279 | CORE WORKFLOW — delivery |
| **Export Mobile Mapping Images, Point Cloud and Trajectory (.csv) to Trimble TMX** | 22501 | CORE WORKFLOW — delivery |
| **Export Mobile Mapping Images and Point Cloud to TopoDot** | 23339 | CORE WORKFLOW — delivery |
| **Export Mobile Mapping Panoramic Images and Point Cloud to Solv3D** | 23888 | ADVANCED — delivery |

A fifth capture, the **2026.10 release note**, again rendered too small to read — but its
**text was then supplied directly** and is treated as evidence in §10. It resolves the
version question outright.

> **Housekeeping:** these five arrived **inline in the conversation, not as an uploaded
> archive**, so unlike batches 2 and 4 the PNGs could not be written to
> `../sources/`. The findings below are recorded and cited; **the page images themselves are
> not archived in the repository.** If the guide is to keep its evidence base complete —
> and the branding requirement says Trimble screenshots are preserved as source material —
> **these four pages need to be re-sent as a zip.**

---

## 1. The single most important finding in this batch

It is not about provenance. It is a silent data-substitution hazard, and it appears in
**identical wording in two separate export topics** *(TBC 23339, 22501)*:

> **"If the TIMESTAMP option has been set to No, the exported scans are the ones processed
> with the Generate Scans feature**, and the color information will be exported if the
> generated scans have been processed with the color option set to on.
>
> **If the TIMESTAMP option has been set to Yes, the exported scans are reprocessed from the
> raw data** and directly written to the LAS format files, the color information will be
> exported in the LAS format files."

**Trimble documented fact** ✅.

### Why this matters more than anything else in the batch

Every quality step in the workflow — registration, Update Scans, filters, colorization, the
Cutting Plane check — acts on the **generated scans**. Setting **Export timestamps = Yes**
causes TBC to **discard those and re-derive the point cloud from the raw data at export
time**.

> **The QC was performed on one point cloud. The deliverable can be a different one.**
>
> Nothing in the dialog says so. The option is called *Export timestamps* — it reads as a
> per-point attribute toggle, not as a reprocessing switch. A processor turning it on to get
> GPS Time into the LAS has, on Trimble's own description, **replaced the data**.

### What is NOT stated, and must not be assumed

❌ **Which trajectory the reprocessing uses.** Trimble does not say whether "reprocessed from
the raw data" uses the mission's currently-applied trajectory — which would pick up a
registration — or the originally imported one. **Both readings are consistent with the text.**

> **Testing required, and this is now the highest-priority test in the project.** Export the
> same registered run twice, once with timestamps off and once on, and compare the point
> geometry. It is a one-afternoon test and it determines whether a documented Trimble option
> can silently undo a registration.
>
> **Vendor clarification required** in parallel — this is a direct, answerable question.

---

## 2. Does trajectory identity survive export?

### 2.1 What the export topics actually show

| Evidence | Source | Class |
|---|---|---|
| **The TMX export writes a trajectory file.** "The trajectory file is created once for all devices. It resides in a folder under the Mission folder." A `trajectory` sub-folder appears in the MX9/MX90, MX50 **and MX60** folder-structure examples | TBC 22501 | Trimble documented fact ✅ |
| The exporter for classified regions is named **"Export to LAS (Trajectory Split)"**, and splits files by a **Splitting distance in multiples of 250 m** | TBC 27279 | Trimble documented fact ✅ |
| With **Scaling: Grid**, "an associated **.txt file is also created to specify the coordinate system and scale factor used**" | TBC 27279 | Trimble documented fact ✅ |
| With **Scaling: Ground**, points are exported as ground coordinates and "the scale factor is **not exposed** during export" | TBC 27279 | Trimble documented fact ✅ |
| An **ECEF** export option produces a ground-scaled LAS "that includes the project's global coordinate system information" | TBC 27279 | Trimble documented fact ✅ |
| Point records carry **GPS Time** per ASPRS LAS 1.4 — "standard GPS Time (satellite GPS Time) minus 1 billion of seconds", origin midnight 6 January 1980 | TBC 23339, 22501 | Trimble documented fact ✅ — *lead L3 confirmed* |
| The **Point Cloud tab LAS Exporter** exports Generate-Scans output as LAS 1.2 or 1.4, **"one file for all processed runs"** | TBC 23339, 22501 | Trimble documented fact ✅ — *lead L2 confirmed* |
| Exports are reached at **Home ▸ Data Exchange ▸ Export ▸ Mobile Mapping tab**, which lists the available exporters | TBC 23339, 23888, 22501 | Trimble documented fact ✅ — *lead L4 confirmed* |
| Solv3D and TopoDot exports produce **LAS 1.4**, one couple of files per run (left and right laser on a two-scanner system) | TBC 23888, 23339 | Trimble documented fact ✅ |

### 2.2 What no export topic states

❌ None of the four captured export topics mentions a **trajectory name**, an **SBET
filename**, a **registration result**, a **registration type**, a **`_reg_####` sequence**, a
**processing date or time**, a **calibration identity**, or **software or version
information** in any exported file, header, sidecar, log or folder name.

❌ For the TMX trajectory file: **its format, its contents, and — critically — *which*
trajectory it contains are not stated.** A run with an imported `Sbet` and a
`Reg. Trajectory` beneath it has two candidates and the topic does not say which is written.

### 2.3 Classification — unchanged, and now for a better-understood reason

> ### **PARTLY CONFIRMED**
>
> **What improved.** One documented export path — TMX — **ships a trajectory file alongside
> the point cloud and imagery**. That is a materially different situation from a bare LAS: the
> receiving party holds the artefact that defines the geometry, not a reference to it. And
> **coordinate-system provenance is now confirmed** — the grid-scaled LAS carries a `.txt`
> sidecar naming the coordinate system and scale factor, and the ECEF option embeds the
> project's global coordinate system.
>
> **What did not improve.** The exported trajectory is **not identified**. Nothing in the
> captured text distinguishes a registered trajectory from an imported one in any export.
> Your original question — *which adjusted trajectory produced this?* — is not answered by a
> file called `trajectory` in a folder called `Mission`.
>
> **What got worse.** §1. On Trimble's own description, an export option can **substitute a
> reprocessed point cloud for the one that was registered and checked**. Provenance is not
> only unrecorded; under one documented setting the deliverable may not be the QC'd data at
> all.

### 2.4 The operational answer, restated

> *If Parametrix later receives or reviews an exported point cloud, can we determine which
> adjusted trajectory produced it?*

**On captured evidence: still no — but the gap has moved.** It is no longer "nothing
accompanies the data." For a TMX export it is **"the trajectory accompanies the data but is
not labelled,"** which is a smaller and more tractable problem: a retained
`sbet_<date>_reg_####.out` could be compared against an exported trajectory file to establish
identity after the fact, if the formats permit.

**Testing required:** whether an exported TMX trajectory file can be matched to a specific
registered SBET. **Not proposed as procedure.**

---

## 3. New MX60-specific facts

The MX60 appears **by name** in the export folder-structure examples — the first time any TBC
topic has illustrated MX60 output.

| Fact | Value | Source |
|---|---|---|
| **Panoramic image size, MX60 Core** | 8192 × 4096 px | TBC 22501, 23888 ✅ |
| **Panoramic image size, MX60 Premium and Pro** | 12288 × 6144 px | TBC 22501, 23888 ✅ |
| Side / planar image size, MX60 | 4096 × 3008 px *(shared with MX90)* | TBC 22501 ✅ |
| MX60 export tree names the cameras | **Camera 3 Back Down** and **Camera 4 360°**, with per-face `.cal` files for the 360° camera (Front, Rear, Left, Right, Top, Bottom) | TBC 23339, 22501 ✅ |

> **This settles a configuration question the SOP has carried since §3.** Imagery resolution
> is **not** a single MX60 specification — **Core delivers a quarter of the pixels of Premium
> and Pro** on the panoramic camera. Every statement about imagery deliverable quality depends
> on which configuration Parametrix owns, which remains **vendor clarification required**
> (`VENDOR-QUESTIONS.md` item 6) and is now materially more consequential than when it was
> written.
>
> Note also: the MX60 tree shows **one 360° camera and one back-down camera**, consistent with
> the MX60 User Guide. It does **not** show the Planar 1 / Planar 2 side cameras that the MX9
> and MX50 trees carry — so the "Export side images" option may have nothing to export on an
> MX60. **Not stated by Trimble. Testing required.**

---

## 4. Export settings worth recording — none of which is a Parametrix procedure

### 4.1 Export to LAS (Trajectory Split) — classified regions *(TBC 27279)*

Prerequisite: run **Extract Classified Point Cloud** in *Point Clouds ▸ Regions* first. ✅

| Setting | Trimble's description |
|---|---|
| **Splitting distance** | "a value in meter multiple of 250" |
| **Export both lasers in the same file** | Yes merges left and right into one LAS. "You need to select at least one laser to export" |
| **Export laser left / right** | Independent Yes/No per laser |
| **Split into files** | Yes splits the LAS per the Splitting Distance |
| **Sample points** | Yes performs **random sampling**; *Number of points* sets the sample size |
| **Format** | LAS **1.2 or 1.4** |
| **Export unit** | Unit of distance in the exported file |

> **Flag — T17, testing required.** *Sample points* performs **random** sampling to a fixed
> point count. On a survey deliverable that is a destructive thinning with no documented
> spatial rule. Its default state is not stated.

### 4.2 Scaling — and a warning Trimble gives about its own output ✅

> "**When Scaling: Grid is selected**, the exported points are expressed in the current
> projected coordinate system (that is, with the current combined scale factor). An associated
> .txt file is also created to specify the coordinate system and scale factor used. **(Note
> that re-importing this file into TBC may cause some inconsistencies due to a double-scaling
> effect.)**"

> "**When Scaling: Ground is selected**, the exported points are exported as ground
> coordinates (that is, as they were measured in the field, independent of the coordinate
> system used). The ground coordinates are scaled from the 0.0 origin by the average combined
> scale factor. **The scale factor is not exposed during export** when this option is selected
> but can be determined by first exporting to grid and then viewing the associated .txt file."

> This is a grid-vs-ground question and a competent surveyor needs no explanation of it. What
> is **not** obvious, and belongs in the guide, is that **the ground-scaled export does not
> tell you the scale factor it used**, and that **re-importing a grid-scaled LAS into TBC can
> double-scale it.** Both are Trimble's own warnings about its own output.

### 4.3 Per-exporter options ✅

| Option | Where | Trimble's guidance |
|---|---|---|
| **Export timestamps** | TopoDot, Solv3D, TMX | **Solv3D: "Solv3D does not need the Timestamps information. Trimble recommends turning this option to No."** See §1 for why the setting is not cosmetic |
| **Fill image files with GPS attributes** | TopoDot, Solv3D, TMX | Writes latitude, longitude, altitude and timestamp into the image files |
| **Blur the images** | TopoDot, Solv3D, TMX | Cross-references *Blur Exported Images* — still uncaptured |
| **Close Command after export** | TopoDot | Closes the Export pane when done |
| **Use inspection colors** | Classified LAS | Exports heat-map colours instead of true colour where a scan inspection has been applied |

### 4.4 Prerequisites and failure modes stated by Trimble ✅

- **"You need to first generate scans from the raw data before exporting them to the TopoDot
  software. Otherwise, nothing will be exported."**
- **"You must close all run views prior to export. Otherwise, a warning message will pop up."**
- **"Corrupted side camera images are exported as black images."** — a silent-ish failure: the
  export succeeds and the defect is only visible by looking
- For Solv3D, "the selected run must have their scans being processed first"
- **"For the MX9 Export to TMX, the user must use a coordinate system without Geoid."** Stated
  for MX9 only; **whether it applies to the MX60 is not stated. Vendor clarification required**

---

## 5. The complete mobile mapping export list

Read from the left navigation of the captured pages — the *Exportable and Uploadable Data
Formats* tree. ✅

| Export topic | Captured? |
|---|---|
| Export Mobile Mapping Classified Point Cloud Regions to LAS (.las) | ✅ this batch |
| Export Mobile Mapping Images, Point Cloud and Trajectory (.csv) to Trimble TMX | ✅ this batch |
| Export Mobile Mapping Images and Point Cloud to TopoDot | ✅ this batch |
| Export Mobile Mapping Panoramic Images and Point Cloud to Solv3D | ✅ this batch |
| **Export Mobile Mapping Cubical Images and Trajectory Files (.csv)** | ❌ `21713_1` |
| **Export Mobile Mapping Panoramic Images and Trajectory Files (.csv)** | ❌ `20927` |
| **Export Mobile Mapping Station Positions and Panorama Orientations files (.xml)** | ❌ `20926` |
| **Export Point Cloud Files (.e57, .las, .laz, .pod, .pts, .ptx, .rcp, .tdx)** *(the generic Point Cloud tab exporter)* | ❌ `11769` |

> **The three uncaptured `.csv` / `.xml` topics are now the most likely to settle the identity
> question**, because all three export **trajectory or station position data as their primary
> product** rather than as a side file. If a trajectory is ever labelled, it is labelled there.

---

## 6. Leads from batch 5 — status

| # | Lead | Status now |
|---|---|---|
| L1 | Signed residuals "in the report" | **Partly confirmed** *(batch 5 §13.2)* — which report still unnamed |
| L2 | LAS exporter on the Point Cloud tab, LAS 1.2/1.4, one file for all runs | ✅ **Confirmed** *(TBC 23339, 22501)* |
| L3 | LAS point records carry GPS Time per ASPRS LAS 1.4 | ✅ **Confirmed** *(TBC 23339, 22501)* |
| L4 | A Mobile Mapping tab lists the exporters | ✅ **Confirmed** *(TBC 23339, 23888, 22501)* |
| L5 | Publish to TRCPS carries point clouds, trajectories and images | ✅ **Confirmed** *(batch 5 §13.3)* — topics still uncaptured |
| L6 | A 2026.10 release exists | ✅ **Confirmed** *(batch 5 §13.1)* — page still illegible |

**All six leads are resolved or promoted. §8 of batch 5 is closed.**

---

## 7. Defaults flagged for testing — one addition

T7 and T9–T16 are **unchanged in status**. Two additions:

| # | Item | Class |
|---|---|---|
| **T17** | **Sample points** in the classified-LAS exporter performs **random** sampling to a fixed point count. Default state not stated. A destructive thinning with no documented spatial rule | **Testing required** |
| **T18** | **Export timestamps** — see §1. Not a flag about a default but about what the option *does*. **This is the highest-priority test in the project** | **Testing required** + **Vendor clarification required** |

**No acceptance tolerance is proposed.** No numerical tolerance for registration or
calibration appears in any export topic. The Trimble position recorded in batch 4 — good RMS
cannot prove success, bad RMS indicates failure, a visual check is necessary — is unchanged.

---

## 8. Figure recommendations

Continuing from **F31**. Crops, not whole pages — **and these require the pages to be re-sent
as files before any crop can be made.**

| # | Figure | Source | Where it goes |
|---|---|---|---|
| F32 | The **MX60** export folder tree — Camera 3 Back Down, Camera 4 360° with six `.cal` faces, Laser Left / Laser Right `.las` | 23339 | Export — what an MX60 deliverable contains |
| F33 | The **TMX** MX60 tree showing the `trajectory` sub-folder beside `laser` and `panorama` | 22501 | **The trajectory travels with the data** |
| F34 | The classified-LAS **Settings** pane — splitting distance, per-laser options, Format, Export unit | 27279 | Export settings |
| F35 | The Solv3D output tree — `lasers` / `panorama`, with `reference.csv` | 23888 | What a reference file is |

---

## 9. Stop condition — not yet, but close

**The TBC source collection is not yet sufficient to begin SOP architecture and drafting** —
but the remaining gap is now narrow and specific, and it is no longer "the export branch."

| Outstanding | Why it is material |
|---|---|
| **20926 · 20927 · 21713_1** — the trajectory and station-position exports | The three most likely to state which trajectory is exported and whether it is identified |
| **11769** — the generic Point Cloud export | The exporter most likely used for a plain LAS/E57 deliverable |
| **The two Publish to Trimble Connect topics** | The second provenance branch, confirmed to carry trajectories |
| **23991_1** — Run a Mission Report, current version | Would likely identify "the report" holding the signed residuals |
| **The four pages in this batch, as files** | So the evidence base is archived, not only cited |

> Everything else needed to draft is in hand. The batch 5 §11 list of what is safe to write
> now gains **export procedures and settings** — with the explicit exception of **what a
> deliverable proves about its own trajectory**, which stays open.


---

## 10. TBC 2026.10 — and the version question closes

The 2026.10 release notes were supplied as text. **Trimble documented fact** ✅ throughout
this section.

### 10.1 The captured help portal documents TBC 2026.10

This is a derived conclusion, and the derivation is short enough to check.

The 2026.10 release notes list, under **Mobile Mapping**, as a **new** feature:

> "In the **Register a Run** (or **Register a Mission**, or **Generate POSPac Position Fixes**)
> tool, the Point Cloud Smart Picking tool now includes **direct residuals to GCP** helping you
> choose the optimal target center, regardless of the target type. These residuals are updated
> whenever you modify the template, such as: changing the center of the target by selecting a
> new center or moving it with the keyboard arrows (including fine adjustments using the Shift
> key); adjusting the bolt size when selecting a GV Target."

**That paragraph is present, almost verbatim, in the captured page for topic 22905** *(batch 4,
Register a Run — the NOTES block following the Road Mark picking type)*.

> **Therefore the captured help material documents TBC 2026.10** — the current release. It is
> not stale, and the behaviour recorded across batches 2, 4 and 6 is current behaviour.
>
> This also explains the "© 2025, Trimble Inc." footer noted in batch 5 §2: it is a portal-wide
> copyright line, not a content date. **The footer was weak evidence and the cross-reference
> is strong evidence. The cross-reference wins.**

**What this closes:**

| Previously open | Now |
|---|---|
| Which TBC version does the captured help describe? | **2026.10.** Closed |
| Does "calibrate outside TBC up to 5.21" apply to us? | **No** — 5.21 predates 5.70, the oldest published release note. Legacy handling only |
| Does the "Select RMS File" prompt (pre-5.80) apply? | **Only to inherited legacy projects** |
| **Which TBC version does Parametrix run?** | **Still vendor clarification required** — unchanged. The documentation being current says nothing about the installation |

**Licensing** ✅ — 2026.10 requires a warranty or subscription valid to **1 June 2026** or
later. (2025.21 required 1 November 2025.)

### 10.2 Mobile mapping changes in 2026.10

Five items, and **none of them touches export or the registration report**:

| Change | Bearing on this project |
|---|---|
| **Direct residuals to GCP in Smart Picking** | §10.1. Already captured and written up in batch 4 |
| **Rectified Camera Views** now names the direction each camera faces — "Rear", "Right-left" — instead of index numbers | Small but real for training: a processor reads *Back Down*, not *Camera 3*. Batch 2's capture of topic 28912 predates this |
| Import Ortholane Images | Pavement work. Not in scope |
| Pavement inspection now supports **jointed concrete** (rigid pavement) | Pavement work. Not in scope |
| Inspect Pavement Condition workflow enhancements | Pavement work. Not in scope |

> **Note what is absent.** 2026.10 makes no change to export, to the registration report, or to
> trajectory handling. The signed-residuals-in-the-report item is from **2025.21** and nothing
> since has revisited it. So §2's classification is not about to be overtaken by a newer
> release — **the Partly confirmed finding reflects current software.**

### 10.3 Coordinate system and datum changes that do bear on mobile mapping

Three, and the first is genuinely important for an MX60 workflow:

**Work in a dynamic datum at a specific epoch** ✅
> "When working with a time-dependent datum, you can now work at a specific epoch that is not
> the default reference epoch for the selected datum. This provides the flexibility necessary
> to select an epoch that meets special needs (for example, in areas with recent earthquakes or
> distorted datums). **Note that this feature is intended for experienced users, as incorrect
> settings may lead to inaccurate results.**"

> **Why this matters here specifically.** Batch 4 established that when POSPac does not
> recognise the project datum and epoch, the SBET is computed **first in ITRF00 and then
> transformed**, and is named `sbet_[mission]_[frame].out` to say so *(TBC 25943)*. Epoch
> handling is therefore already part of the mobile mapping trajectory path, not an abstract
> datum concern — and TBC now exposes a control over it that Trimble itself flags as capable of
> producing inaccurate results if set wrongly.
>
> **This raises T10 in priority.** It is no longer only "a filename that silently indicates an
> extra transformation" — there is now a user-settable epoch that interacts with it. Still
> **testing required**, and emphatically not a procedure.

**Exchange a coordinate system with Trimble Connect** ✅ — push or pull a coordinate system
between TBC and Trimble Connect, comparing projection, datum and geoid first, "reduc[ing] the
chances of mismatched coordinate systems between office and field data." Requires Administrator
rights on the Trimble Connect project to push.

**Coordinate System Database v115** ✅ — of the twenty-odd entries, two are relevant to US work:
a grid transformation from **CSRN2025 (NAD83 2011) to CA SRS Epoch 2017.50** for California
zones 1–6, and a **beta** Canadian **NATRF2022(CSRS)** modernised reference frame with
SGEOID2022-beta2. Also: selecting a predefined geoid model now fills the vertical datum name
automatically.

> **Recorded, not acted on.** Which coordinate system and epoch Parametrix works in is a
> **Parametrix decision** that long predates this guide and is not one to be made here.

### 10.4 Two operational notes worth carrying

**Trimble ID now requires two-step verification** ✅ — "you will receive a verification code via
email each time you sign in." Anyone signing in to TBC or Trimble Connect needs access to the
account's email at sign-in time. A small thing that stops a field or office session dead if
unanticipated.

**Trimble Connect UK region is unavailable** ✅ — affects Dataset Workspace, **Trimble Mobile
Mapping data**, Trimble Access data and **Publish to TRCPS**. Not applicable to Parametrix, but
it confirms that **Publish to TRCPS is a Connected Workspace function** — which is where to look
for it when the two Publish topics are eventually captured.

**Dark theme (beta)** ✅ — TBC now has a dark theme, switched at *Options ▸ General ▸ Display*.

> Relevant only to the branding requirement: if Trimble screenshots are preserved as source
> material — and `GUIDE-REQUIREMENTS.md` says they are — **all captures should be taken in one
> theme.** Mixed light and dark TBC screenshots in a Parametrix manual would look like an
> error. Light is the safer default, being what every existing capture uses.

### 10.5 Point cloud changes

**Advanced Point Cloud Filtering** ✅ — a median elevation filter can now use "actual measured
points rather than averaged points." **Boeing Bump Index Report** and an **ADA Ramp Compliance
Report** are now generally available. None bears on trajectory, registration or provenance.


---

*No rewrite has been performed.*
