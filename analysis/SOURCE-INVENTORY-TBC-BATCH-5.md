# Source Inventory — Batch 5: the export provenance pass

**Prepared:** 2026-09-11
**Status:** Evidence pass. **No rewrite performed.**
**Continues:** [`SOURCE-INVENTORY-TBC-BATCH-4.md`](SOURCE-INVENTORY-TBC-BATCH-4.md)

---

## 0. The blocker, stated first

**I could not capture *Export Mobile Mapping Data*.** No archive was uploaded with this
instruction, and **outbound access to `help.fieldsystems.trimble.com` is blocked by this
environment's network egress proxy** — confirmed again this session, both through the fetch
tool (`EGRESS_BLOCKED`) and directly (`CONNECT tunnel failed, response 403`).

So the primary question — *does an exported deliverable identify the trajectory that produced
it?* — **cannot be answered from captured evidence in this pass.** It is recorded below as
**Not documented in captured material**, which is not the same as "no".

What this pass *did* produce:

1. **An exact capture list** — the Export branch enumerated with topic IDs and URLs, §1
2. **The reconciliation you asked for**, done against what is already captured, §3
3. **A classification of how far traceability survives**, §4 — **Partly confirmed**
4. **The Cleanup finding, preserved and sharpened**, §5
5. **The POSPac dependency table**, §6 — confirmation, not new research
6. **Unverified leads**, quarantined in §8 and used only to build the capture list

> **§8 is quarantined deliberately.** Web search reached Trimble's domain even though direct
> fetch did not, and returned several statements that bear directly on your question — one of
> them says a registration report with signed residuals exists. **Search-engine summaries of
> pages I could not open are not evidence.** They are in §8, they are not classified
> Confirmed, and none of them has been written into the reference dataset.

---

## 1. The capture list — Export Mobile Mapping Data

The Export branch is **collapsed** in every page captured so far, so the sub-topic list below
is assembled from topic titles and IDs rather than from the expanded navigation. Expand the
branch before capturing, in case it holds topics this list misses.

**Parent branch:** *Mobile Mapping ▸ Export Mobile Mapping Data*
Confirmed present in the navigation tree of every batch 2 and batch 4 capture. ✅

### Priority 1 — bears directly on the provenance question

| Topic | ID | URL |
|---|---|---|
| **Export Mobile Mapping Data** *(the parent — capture it expanded)* | — | navigate from any Mobile Mapping page |
| **Export Point Cloud Files (.e57, .las, .laz, .pod, .pts, .ptx, .rcp, .tdx)** | 11769 | `help.fieldsystems.trimble.com/tbc/11769.htm` |
| **Export Mobile Mapping Classified Point Cloud Regions to LAS (.las)** | 27279 | `…/27279.htm` |
| **Export Mobile Mapping Station Positions and Panorama Orientations files (.xml)** | 20926 | `…/20926.htm` |
| **Export Mobile Mapping Panoramic Images and Trajectory Files (.csv)** | 20927 | `…/20927.htm` |
| **Exportable and Uploadable Data Formats** | 1590 | `…/1590.htm` |

> **11769 and 20926 are the two most likely to settle the question.** A point-cloud export
> dialog is where a trajectory reference would appear if one is written at all, and a station
> positions / panorama orientations XML is the one export whose *purpose* is to carry
> positional provenance.

### Priority 2 — format-specific exports, capture if cheap

| Topic | ID |
|---|---|
| Export Mobile Mapping Images, Point Cloud and Trajectory (.csv) to Trimble TMX | 22501 |
| Export Mobile Mapping Cubical Images and Trajectory Files (.csv) | 21713_1 |
| Export Mobile Mapping Images and Point Cloud to TopoDot | 23339 |
| Export Mobile Mapping Panoramic Images and Point Cloud to Solv3D | 23888 |
| Export TopoDOT Files (.iprj, .lst, .cal, .jpg) | 23871 |
| Export and Share Point Cloud Data | 25726 |

### Priority 3 — settles the version question, which is now blocking several procedures

| Topic | ID |
|---|---|
| TBC Release Notes index | `release-notes.htm` |
| 2025.21 readme | `release-notes/2025.21-readme.htm` |
| 2026.10 | `release-notes/2026.10.htm` |

> **Capture a release note and the version question closes.** Batch 4 left three procedures
> depending on "which TBC version is installed" (5.21 for calibration, 5.80 for the RMS file).
> The release-notes tree is public and enumerable, and it also dates the help portal.

### Priority 4 — previously listed, still outstanding, still not material to provenance

Blur Exported Images · Create Orthomosaics from a Back-Camera System · Display Mobile Mapping
Run Views · Run a Batch Command (27618) · Create CAD Entities · Import Ortho Lane Images ·
Inspect Pavement Condition · AgileAssets · BBI Report

---

## 2. One new fact from re-reading the existing captures

**Trimble documented fact** ✅ — the help portal footer reads **"© 2025, Trimble Inc. All
rights reserved."** on every captured page.

That is the **first date evidence of any kind** for the help portal, which batch 2 recorded as
carrying "no revision number and no date." It is a copyright year, not a revision — it bounds
the material at 2025 or later and no more than that. Combined with the topics' own references
to behaviour "up to the 5.21 version" and "prior to version 5.80", the captured set is
**later than 5.80 and stamped 2025**.

> Still **Vendor clarification required**: which version Parametrix actually runs. A copyright
> year on a help portal says nothing about the installed software.

---

## 3. Reconciling the provenance chain — what is actually established

Every row below is from a **captured page**. Nothing here is inferred.

### 3.1 Provenance that exists inside the TBC project

| Evidence | What it identifies | Source | Class |
|---|---|---|---|
| Trajectory node property **`Origin: Registration result`** | That this trajectory came from a registration, not an import | TBC 22905, 26473 | Trimble documented fact ✅ |
| Trajectory node property **`Input trajectory: Imported trajectory`** | Which trajectory the registration was computed *from* | TBC 22905, 26473 | Trimble documented fact ✅ |
| Trajectory node property **`Registration type: GlobalThenLocal`** | Which adjustment method was used | TBC 22905, 26473 | Trimble documented fact ✅ |
| Trajectory node property **`Trajectory file: …\sbet_2017080301_reg_0014.out`** | The exact SBET on disk | TBC 22905, 26473 | Trimble documented fact ✅ |
| On-disk **`sbet_<date>_reg_####.out`**, incrementing | How many registrations exist and in what order | TBC 22905, 26473 | Trimble documented fact ✅ |
| Scan nodes **nested beneath their trajectory node** | Which trajectory a scan set was computed against | TBC 22638 | Trimble documented fact ✅ |
| Scan station suffix **`_reg_####`** | Same, at station level | TBC 22638 | Trimble documented fact ✅ |
| Registered segments render in the **"Undefined RMS" colour** | *Visually*, which parts of a trajectory were adjusted | TBC 27248 | Trimble documented fact ✅ |
| **`Targets.csv`** in the project | The registration observations themselves | TBC 22905 | Trimble documented fact ✅ |
| **Mission Report** — capture devices, runs, trajectories, generated scans; per-sensor boresight and lever-arm calibration **with date of calibration** | The mission's configuration and calibration state | TBC 23991, 24868 | Trimble documented fact ✅ |

### 3.2 Where that provenance stops

| Question | Answer | Class |
|---|---|---|
| Does the **Mission Report** state which trajectory each scan set used, or only list trajectories present? | The captured text says it "displays the properties of a mission, including capture devices, runs, trajectories and generated scans." **It does not say the scans are attributed to a trajectory.** | Not documented in captured material ❌ |
| Does the **adjusted trajectory carry a registration report** with residuals? | Not in any captured page. Per-pick residuals are shown live in the dialog; per-pair RMS appears in the Results tab of Run-to-Run only. | Not documented in captured material ❌ *(but see §8, lead L1)* |
| Does **any export** carry trajectory identity? | **No export topic has been captured.** | Not documented in captured material ❌ |
| Do **imagery and station positions** inherit a registration? | Unchanged from batch 4. | Not documented in captured material ❌ |

### 3.3 The one export-adjacent fact that *is* captured

**Trimble documented fact** ✅ *(TBC 25943)* — the **SBET itself** is written to
`NAVPROC/Export/` with the report in `NAVPROC/Report/`, and `Backup SBET Next to MXDB` copies
the SBET **and a log containing the frame and epoch information used to create it** into the
raw data folder beside the `.mxdb`.

> That log is a genuine provenance artefact and it survives outside the TBC project. But it
> documents **the imported trajectory's** production, not a registration — the registered
> SBETs are written to the project folder root, not to `NAVPROC`. It does not answer the
> question; it is the nearest thing captured that resembles an answer.

---

## 4. Classification — does trajectory identity survive export?

> ### **PARTLY CONFIRMED**
>
> **Confirmed:** inside an intact TBC project, an adjusted trajectory is uniquely and
> durably identified — by name, by `Origin`, by `Input trajectory`, by `Registration type`,
> and by a named, numbered SBET file on disk. Scans are attributed to it by tree position and
> by a `_reg_####` station suffix. **This part is not in doubt.**
>
> **Not confirmed:** that any of it crosses the export boundary. **No captured Trimble page
> describes an export that writes a trajectory name, an SBET filename, a registration type, a
> `_reg_####` number, or a registration identity into an exported file, header, sidecar,
> metadata block or log.**
>
> **Explicitly not claimed:** that exports *lack* provenance. Six export topics exist and
> none has been read. Absence of evidence here is exactly that.

### The operational answer to the question you posed

> *If Parametrix later receives or reviews an exported point cloud, can we determine which
> adjusted trajectory produced it without relying solely on the original operator's memory or
> project state?*

**On captured evidence: no — and the dependency is on project state specifically, not
memory.** Every confirmed identifier in §3.1 lives *inside the TBC project*. An exported
point cloud arriving without its project has, on what is captured, nothing in it that names a
trajectory.

Two qualifications, both material:

1. **This may change entirely once the export topics are read.** It is a gap in the evidence,
   not a finding about the software.
2. **Timestamps are a partial exception.** Point records in LAS carry GPS Time, and the
   registration statistics are themselves timestamped every 20 m *(TBC 25096)*. A timestamp
   does not name a trajectory, but it does let an exported point be matched back to an epoch
   in a specific SBET **if that SBET is retained**. That is a *reconstruction* path, not a
   provenance record, and it depends on Parametrix keeping the SBETs.

**Testing required**, and this one Parametrix can answer without Trimble: export the same run
twice, once on the imported trajectory and once on a registered trajectory, and diff the two
outputs — filenames, headers, sidecars, and any log written alongside. That test is decisive
and takes an afternoon.

---

## 5. Cleanup — the batch 4 finding, preserved and checked

**Unchanged and not weakened.** Cleanup Mobile Mapping Mission is **destructive and not
undoable**, and it removes intermediate registration history.

Trimble's complete text, re-verified against the capture *(TBC 26466)*:

> "The feature enables you to cleanup your project by keeping the most recent registration
> (and related scans), and trajectory consistent with the latest version of navigation and
> trajectory information file (SBET or NAV). This feature can be run at the end of the data
> preparation process (registration, colorization, etc.), it allows you to share a light
> project, before moving on to a feature extraction phase. **Please, have a backup copy of
> your project prior performing the operation, it cannot be undone.**"

### Does Trimble prescribe preserving registration information before Cleanup?

**One recommendation exists, and it is narrower than a preservation step.**

| | |
|---|---|
| **What Trimble does say** | Take a **backup copy of the project** before running Cleanup. That is an explicit, stated recommendation. ✅ |
| **What Trimble does not say** | Nothing in any captured page recommends **exporting, reporting, archiving or otherwise recording registration information** before Cleanup. No captured page links Cleanup to the Mission Report, to `Targets.csv`, to the registered SBET files, or to any export. |

> **No vendor-prescribed preservation step was found** beyond "back up the project."
>
> Note what that omission means in practice: a project backup preserves everything, so it is
> a sufficient remedy *if it is actually taken and actually kept*. Trimble's recommendation is
> adequate on its own terms. It is simply not a records requirement, and it does not survive
> being skipped.

**Parametrix decision required** — whether a backup is sufficient, or whether a durable record
(Mission Report, `Targets.csv`, the `_reg_####` SBET set) must be archived independently of
the project. **Not decided, not drafted, and deliberately not written as a procedure here.**

---

## 6. POSPac dependency — confirmation, not new research

Already established in batch 4 §3. Restated as the clean decision point you asked for, with
nothing added:

| Function | Needs POSPac MMS 8.6+ installed | Needs a valid POSPac licence | Native in TBC | Source |
|---|---|---|---|---|
| **Import `.mxdb`, apply SBET or NAV** | No | No | ✅ Yes | TBC 20736-1 |
| **Generate Mobile Mapping Scans** | No | No | ✅ Yes | TBC 22499 |
| **Update Mobile Mapping Scans** | No | No | ✅ Yes | TBC 22638 |
| **Register a Run / Mission / Run-to-Run** | No | No | ✅ Yes | TBC 22905, 26473, 25096 |
| **Calibrate laser scanners / cameras** | No | No | ✅ Yes *(TBC after 5.21)* | TBC 24886, 24868 |
| **Cleanup Mobile Mapping Mission** | No | No | ✅ Yes | TBC 26466 |
| **Mission Report, Trajectory Plots** | No | No | ✅ Yes | TBC 23991, 27415 |
| **Process Raw Trajectory Data** *(SBET inside TBC)* | **Yes — 8.6 or later** | **Yes, explicitly** | ❌ No | TBC 25943 ✅ |
| **Generate POSPac Position Fixes** *(PFIX)* | **Yes** | **Yes — "valid license for the typical IN-Fusion processing methods"** | ❌ No | TBC 24460 ✅ |
| **LiDAR QC Processing** | Not stated | Not stated | Runs in TBC, but **requires MATLAB Runtime R2024b** and a 128–256 GB workstation | TBC 28972 ⚠ |

### The degraded-GNSS consequence, which is the point of the table

There are **three** documented remedies for poor GNSS, and the licence cuts across them:

| Remedy | Needs POSPac | Needs extra field control | Needs a big workstation |
|---|---|---|---|
| **Register a Run / Mission** to GCPs | No | **Yes** | No |
| **Generate POSPac Position Fixes** | **Yes** | **Yes** | No |
| **LiDAR QC Processing** | Not stated | **No** | **Yes** |

> **Without a POSPac licence, Parametrix has exactly two remedies: place more control, or buy
> a much larger workstation.** That is the office-workflow decision point, and it is a
> procurement question, not a software setting.
>
> **Vendor clarification required:** whether LiDAR QC has its own POSPac dependency. Trimble
> does not state one, but it is described as an Applanix technology and the topic directs
> configuration questions to the **Applanix Support Team**. ⚠

---

## 7. Categories carried forward untouched

### T9–T16 remain flagged for testing. None has become a procedure.

Restated so this document stands alone, with **no change of status**:

| # | Item | Status |
|---|---|---|
| **T9** | **Activate Target-Bundle Adjustment** — checking it makes the adjustment **coarser** (250 m vs 70 m); the name reads the other way round | **Testing required.** Not a recommendation, not a default to adopt |
| T10 | `sbet_[mission]_[frame].out` naming silently indicates an extra datum transformation | Testing required |
| T11 | Multipath default **Medium**, described as being for *degraded* coverage | Testing required |
| T12 | DMI scale factor SD default **5 %** | Testing required |
| T13 | LiDAR QC range default **3–100 m** | Testing required |
| T14 | LiDAR QC lasers default **All**, against Trimble's own guidance beside it | Testing required |
| T15 | **Registration type** — no selection rule given for Global / Local / Global-then-Local | Testing required |
| T16 | **Cutting plane thickness** — 5.000 and 0.030 both shown, no stated basis | Testing required |
| T7 | Registration auto-saving **default state** still unstated | Testing required |

### The acceptance position is unchanged, and no threshold has been proposed

**Trimble documented fact** ✅, stated in identical wording in two separate topics *(TBC 24886,
25096)*:

> Good RMS values do not by themselves prove a successful calibration or registration. Bad RMS
> values do indicate failure. **A visual check is necessary.**

**No Parametrix RMS threshold is proposed in this document, and none exists anywhere in the
repository.** No numerical tolerance for registration or calibration appears in any Trimble
source captured to date. If one is found later it will be recorded **with its exact scope and
context and will not be generalised** beyond it.

---

## 8. Quarantined — unverified leads

**These are web-search summaries of pages that could not be opened from this environment.**
They are **not evidence**, they are **not classified**, and **none has been written into
`reference/mx60-reference-data.csv`.** They exist to direct the next capture.

| # | Lead | Why it matters | Verify by capturing |
|---|---|---|---|
| **L1** | TBC **2025.21** release notes are reported to say GCP registration "now provide signed residuals (Easting, Northing, and Elevation) **in the report**" | If true, **a registration report exists** — which is Q8's remaining unknown, and it would be the single most useful QC artefact in the workflow | `release-notes/2025.21-readme.htm` |
| **L2** | The **LAS exporter** is reported to live on the **Point Cloud** tab, exporting scans generated by Generate Scans as **LAS 1.2 or 1.4, one file for all processed runs** | "One file for all runs" would mean run identity is lost at export even before trajectory identity is considered | 11769, 27279 |
| **L3** | LAS point records are reported to carry **GPS Time** per ASPRS LAS 1.4 | The timestamp reconstruction path in §4 depends on this | 11769 |
| **L4** | A **Mobile Mapping tab** in the Export pane is reported to list exporters: TMX, Mapillary, TopoDOT, Solv3D, Horus | Tells us the export surface is format-specific, not one generic exporter | the Export parent topic |
| **L5** | TBC **2025.21** is reported to add publishing to the Trimble Reality Capture Platform Service "for sharing point clouds, trajectories, and images" | A path that ships the **trajectory alongside the cloud** would change the provenance answer materially | `release-notes/2025.21-readme.htm` |
| **L6** | A **2026.10** release exists | Bears on which version Parametrix should be running | `release-notes/2026.10.htm` |

> **L1 and L5 are the two that could change the §4 classification from Partly confirmed.**
> Both are release notes, both are small pages, and both are worth capturing before the
> export topics themselves.

> **UPDATE, later the same day.** The 2025.21 release note was captured. **L1 is now partly
> confirmed, L5 is confirmed, L6 is confirmed** — see §13. L2, L3 and L4 remain unverified and
> remain out of the reference dataset. The §4 classification is **unchanged at Partly
> confirmed**; see §13.3 for why confirming L5 did not move it.

---

## 9. Evidence inventory — additions

Continuing the existing numbering. Batch 4 ended at figure **F31**; reference IDs continue in
their existing prefixes.

### 9.1 New reference records

| ID | Item | Source | Class |
|---|---|---|---|
| `TBC-010` | Help portal footer reads "© 2025, Trimble Inc." on every captured page | all batch 2 / 4 captures | Trimble documented fact ✅ |
| `TBC-011` | Export Mobile Mapping Data branch confirmed present in the navigation tree; **not captured** | all batch 2 / 4 captures | Gap, recorded as a gap |

### 9.2 Figures — none added

No new figure recommendations. **F17–F31 from batch 4 stand unchanged**, and no figure can be
recommended from the export topics until they are captured.

### 9.3 Topics catalogued but not captured

Recorded in §1 with IDs and URLs so the next pass is a capture task, not a search task.

---

## 10. Stop condition — not met

**The TBC source collection is NOT yet sufficiently complete to begin SOP architecture and
drafting.**

One material gap remains, and it is the one this pass was sent to close:

> **Does an exported mobile mapping deliverable identify the trajectory that produced it?**

This is not a marginal topic and it is not being collected to increase a source count. It
determines whether a delivered point cloud is self-describing or whether it is only
interpretable alongside its project — which in turn determines what Parametrix has to record
at delivery, and whether the Cleanup decision is reversible in practice.

**Everything else is ready.** §11 sets out what can be drafted now.

> **What would close it:** the six Priority 1 captures in §1, plus the two release notes in
> §8. That is eight pages. Egress from this environment is blocked, so they have to arrive as
> an upload the same way batches 2 and 4 did.

---

## 11. What is now safe to draft — and what is not

Recorded now so the rewrite does not have to re-derive it. **Still no rewrite performed.**

### Evidence-backed — can be drafted as instruction

| SOP area | Backed by |
|---|---|
| Mission import and the data-object chain | TBC 20736-1, 22503 |
| Scan generation, filters and their contents | TBC 22499 |
| Update Scans — what it does, when it is required, both directions | TBC 22638 |
| Scan recovery | TBC 28155 |
| **Registration — all three mechanisms, inputs, options, outputs, naming** | TBC 22905, 26473, 25096, 25362, 26578 |
| **Control vs check points in TBC** | TBC 22905, 26473 |
| **Target picking and reading residuals before validating** | TBC 22905 |
| **Registration QC indicators at all four levels** | TBC 22905, 25096, 24886, 27248 |
| **The visual check, and why the numbers alone cannot pass a job** | TBC 24886, 25096 |
| Laser scanner and camera calibration, and the calibration JSON | TBC 24886, 24868, 20728, 22920 |
| Trajectory production in TBC, its settings and its licence dependency | TBC 25943 |
| LiDAR QC — what it is, its field pattern, its requirements | TBC 28972 |
| PFIX — what it is and when it applies | TBC 24460 |
| **Cleanup — what it destroys and Trimble's backup recommendation** | TBC 26466 |
| Mission Report and Trajectory Plots as retained records | TBC 23991, 24868, 27415 |

### Blocked on evidence

| SOP area | Blocked by |
|---|---|
| **Export procedures and formats** | No export topic captured |
| **Delivery provenance — what accompanies a deliverable** | §4, Partly confirmed |
| Imagery privacy / blurring | Blur Exported Images not captured |

### Blocked on a Parametrix decision or on field testing

| SOP area | Blocked by |
|---|---|
| **Registration acceptance criteria** | No Trimble threshold exists. Parametrix decision required |
| **Which registration type to use when** | T15, testing required |
| **Target-bundle adjustment setting** | T9, testing required |
| **Filter and LiDAR QC defaults** | T11–T14, testing required |
| **Records retained at delivery** | Parametrix decision required |
| **Whether a project backup is sufficient before Cleanup** | Parametrix decision required, §5 |
| **Whether to provision for LiDAR QC** | Parametrix decision required, §6 |
| Which TBC version, and whether a POSPac licence exists | Vendor clarification required |

---

## 12. Design requirement — plain-language layer

**Recorded, already in force.** This requirement was established on 2026-09-11 and is set out
in full, with worked examples and acceptance criteria, in
[`GUIDE-REQUIREMENTS.md`](GUIDE-REQUIREMENTS.md) §2. It is **not** re-specified here; this
section exists so that batch 5 does not read as though the requirement lapsed.

Restating only the obligation:

> **Every major technical section in the final Parametrix guide must end with a short
> plain-language explanation for a reader who is new to mobile mapping.** Heading: **IN PLAIN
> ENGLISH**. The technical material remains complete and authoritative; the box is additive.

Each box must answer: **what we just did · why it matters · what could go wrong · what "good"
looks like in practical terms.**

> **One amendment to `GUIDE-REQUIREMENTS.md` §2 arises from this instruction.** The
> requirement as recorded asks three questions — *what just happened, why does it matter,
> what do I need to remember.* The instruction adds a fourth: **what could go wrong.** That
> is a real addition, not a rephrasing, and several of the most important facts in the source
> set are failure modes rather than procedures — a picked target on a superseded scan, Local
> registration not extrapolating beyond the outermost control point, `Targets.csv` emptied by
> the wrong answer to a dialog, Cleanup without a backup. **`GUIDE-REQUIREMENTS.md` has been
> amended to four questions.**

The guide cannot assume the reader already understands trajectory processing, SBETs, GNSS/INS
integration, boresight calibration, registration, residuals, or point-cloud QC. It can assume
they are a competent surveyor.

---

## 13. Addendum — release notes captured, 2026-09-11

Two release-notes pages arrived after §0 was written. **2025.21 is legible and is treated as
evidence below. 2026.10 rendered too small to read and is not evidence** — it is re-requested.

### 13.1 Version numbering — an open question closes

**Trimble documented fact** ✅ — the Release Notes navigation lists, newest first:

> **2026.10** · 2025.21 · 2025.20.1 · 2025.20 · 2025.10 · 2024.13 · 2024.10 · 2024.00 ·
> 2024.02 · 2024.01 · 2023.12 · 2023.11 · 2023.10 · 5.90.1 · 5.90 · 5.81 · 5.80 · 5.70.1 ·
> 5.70

TBC moved from `5.x` numbering to `YYYY.MM` at **5.90.1 → 2023.10**. The current release is
**2026.10**.

> **This substantially de-risks the version question from batch 4.** Two procedures were
> flagged as version-dependent:
>
> | Flagged behaviour | Boundary | Where that sits now |
> |---|---|---|
> | Laser scanners and cameras calibrate **outside** TBC and import as JSON | "up to the 5.21 version" *(TBC 24886, 24868)* | **5.21 predates 5.70 — the oldest release note published.** Any TBC a working office is plausibly running calibrates **in** TBC |
> | Registration with no RMS file set, prompting **Select RMS File** | "typically a project saved in TBC prior to version 5.80" *(TBC 27248)* | Also well before the 2023.10 renumbering. Relevant only to **inherited legacy projects**, not new work |
>
> **Vendor clarification still required** — which version Parametrix runs — but the question
> has shrunk from "does this procedure apply to us" to "confirm we are not on something from
> before 2023." Both flagged behaviours now read as **legacy-project handling**, not as a
> fork in current procedure.

**Licensing**, stated in the same page ✅: 2025.21 is available to perpetual licence users
whose **warranty expiration date is 1 November 2025 or later**, and to subscription users
with an active subscription. Warranty or subscription expiry is visible at
**Support ▸ License Manager**.

### 13.2 Lead L1 — PARTLY CONFIRMED

Trimble's 2025.21 text, under **Mission and Run Registration** ✅:

> "The distance gaps between the selected Ground Control Point (GCP) and the picked target -
> known as the Easting, Northing, and Elevation residuals - **are now signed and included in
> the report.**"

| | |
|---|---|
| **Confirmed** | Registration residuals **are written to a report**, signed, in all three components, as of 2025.21 |
| **Not confirmed** | **Which report.** Trimble says "the report" without naming it. The Mission Report is the only mobile-mapping report captured, but nothing states the residuals land there |

> This is the strongest evidence yet that a durable registration record exists — and it is
> still not enough to say where it lives. **Not converted to a conclusion.** Capturing the
> current *Run a Mission Report* topic (23991_1) would likely settle it.

### 13.3 Lead L5 — CONFIRMED, and it matters more than expected

Trimble's 2025.21 text ✅:

> "**Publish to TRCPS** - Send mobile mapping data to the Trimble Reality Capture Platform
> Service for sharing and collaboration on **point clouds, trajectories, and images** (with or
> without the blurring option)."

Two help topics are named in the same sentence, **neither previously known to exist**:

- **Publish Point Cloud Data and Panoramic Images to Trimble Connect**
- **Publish Mobile Mapping Point Cloud Data, Trajectories, and Images to Trimble Connect**

> **A delivery path that ships the trajectory alongside the cloud is a different answer to the
> provenance question than any export format.** If the trajectory travels with the data, the
> receiving party holds the thing that defines the geometry — not a reference to it, the
> artefact itself.
>
> **This does not change the §4 classification.** Publishing to a platform service is not the
> same as exporting a file, the topics are uncaptured, and nothing states *which* trajectory
> is published when several exist under a run. But it means the provenance question has **two
> branches**, and only one of them was being investigated:
>
> | Branch | Question |
> |---|---|
> | **Export** to a file | Does the file identify its trajectory? *Still open* |
> | **Publish** to TRCPS / Trimble Connect | The trajectory is sent too — but **which one**, and is it identified? *Newly open* |

### 13.4 An operational warning worth carrying into the guide

**Trimble documented fact** ✅, 2025.21, listed as a known issue rather than a fix:

> "Resizing the Smart Picking window during registration causes instability. **Enlarging it
> forces a square aspect ratio to eliminate whitespace, while shrinking it can cause TBC to
> lag or freeze.**"

Smart Picking is where every registration observation is made, and a freeze mid-session risks
the picked targets. Combined with the `Targets.csv` behaviour *(TBC 22905)*, this is a
concrete argument for confirming **Registration Auto-Saving** is on before starting — which
remains **T7, testing required**, not a procedure.

### 13.5 Minor, recorded for completeness

**Export Orthoimage options** ✅ — the Orthoimage exporter gained a **Create world file**
option producing a `.tfw`, and a **Compression** option. Topic named: *Export Orthoimage Files
(.tiff, .txt)*. Bears on back-camera orthomosaic deliverables, not on trajectory provenance.

### 13.6 Capture list — revised

**Still needed, highest value first:**

| # | Page | Why |
|---|---|---|
| 1 | **2026.10 release notes** — *re-requested, legibly* | Same reasons as before, plus: it is the current release and may carry further registration or export changes |
| 2 | **Publish Mobile Mapping Point Cloud Data, Trajectories, and Images to Trimble Connect** | §13.3 — the trajectory-carrying delivery path |
| 3 | **Publish Point Cloud Data and Panoramic Images to Trimble Connect** | §13.3 |
| 4 | **Run a Mission Report** (`23991_1.htm` — the current version) | §13.2 — would likely identify "the report" |
| 5–10 | The six Export topics from §1 | Unchanged |

Batch 2 captured Mission Report at `23991.htm`; the current topic is `23991_1.htm`. **Recapture
it** — the `_1` suffix marks a revised topic, and 2025.21 changed what the report contains.


---

*No rewrite has been performed. One material gap remains: Export Mobile Mapping Data — now with a second branch, Publish to TRCPS.*
