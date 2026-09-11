# Source Inventory — Batch 7: the export surface closes

**Prepared:** 2026-09-11
**Status:** Ingestion and classification. **No rewrite performed.**
**Captures:** `../sources/tbc-help-captures-batch7/` — 7 topics
**Continues:** [`SOURCE-INVENTORY-TBC-BATCH-6.md`](SOURCE-INVENTORY-TBC-BATCH-6.md)

---

## 0. Headline

**Every export path available to an MX60 has now been read.** The provenance question is no
longer open for want of documentation — it is answered, and the answer is a considered
negative rather than a gap.

Three of the seven topics turned out not to apply to the MX60 at all, which is itself a useful
result: it removes the three sources batch 6 nominated as *most likely* to settle the question.

---

## 1. Three topics eliminated — they are MX7 exporters

**Trimble documented fact** ✅ in all three cases. Read the exporter name, not the topic title:

| Topic | Exporter selected in the UI | Verdict |
|---|---|---|
| Export Mobile Mapping **Station Positions and Panorama Orientations (.xml)** *(20926)* | **"MX7 Export to XML Horus"** — "converting PGR files captured with a **Trimble MX7 360° camera**" | ❌ Not an MX60 path |
| Export Mobile Mapping **Panoramic Images and Trajectory Files (.csv)** *(20927_1)* | **"MX7 Export to TMX"** — starts from a **Trident project file (.tridb)**, panoramic image size **8000 × 4000 px** | ❌ Not an MX60 path |
| Export Mobile Mapping **Cubical Images and Trajectory Files (.csv)** *(21713_1)* | **"MX7 Export to Mapillary"** — same 8000 × 4000 px panorama | ❌ Not an MX60 path |

> **Batch 6 §5 nominated exactly these three as the most likely to name a trajectory**, on the
> reasoning that they export trajectory or station data as their primary product. That
> reasoning was sound and the answer is simply that they are a different system's exporters.
> **The nomination is withdrawn.**
>
> Note the tell: the MX7 panorama is **8000 × 4000**, where the MX60 is **8192 × 4096** (Core)
> or **12288 × 6144** (Premium/Pro) *(batch 6 §3)*. The pixel counts are a reliable way to
> tell which system a TBC topic is describing when the title does not say.

One incidental find worth keeping *(TBC 21713_1)* ✅ — an exported Mapillary panorama's Windows
file properties show **`Program name: Trimble Business Center`**. Software provenance does
reach at least one exported artefact, in image EXIF. It names the software, not the trajectory.

---

## 2. Export Point Cloud Files *(TBC 11769)* — the generic exporter

This is the path most likely to be used for an ordinary LAS or E57 deliverable, and it is now
fully documented. **Trimble documented fact** ✅ throughout.

**Formats:** `.e57` (with a separate **structured** e57 exporter), `.las`, `.laz`, `.pod`
(Bentley Pointools), `.pts`, `.ptx`, `.rcp` (Autodesk ReCap), `.tdx` (TBC/RealWorks exchange).

**Reached at** *Home ▸ Data Exchange ▸ Export ▸ **Point Cloud** tab* — note, a different tab
from the Mobile Mapping exporters.

### 2.1 The finding that matters

> **Selection is by point cloud region or graphical selection — not by run and not by
> trajectory.**
>
> Trimble's step 4: select "one or more entire point cloud regions… in the Project Explorer or
> graphic view", or draw a **Rectangle Select** or **Polygon Select** in a graphic view.

⚠ **Assessment, flagged not asserted:** nothing in the command ties the export to a trajectory,
and a rectangle drawn across a graphic view could span scans generated from different
trajectories. Whether TBC prevents or warns about that is **not stated**. **Testing required.**

### 2.2 Settings

| Setting | Behaviour |
|---|---|
| **Scaling: Grid** | Points in the current projected coordinate system with the combined scale factor. **An associated `.txt` file is created specifying the coordinate system and scale factor.** Trimble warns re-importing may cause "inconsistencies due to a double-scaling effect" |
| **Scaling: Ground** | Ground coordinates scaled from the 0,0 origin by the average combined scale factor. **"The scale factor is not exposed during export"** — recoverable only by exporting to grid and reading the `.txt` |
| Scaling applicability | Selectable for e57, LAS, LAZ, POD, PTS, RCP. **TDX and PTX are always ground-based** |
| **ECEF export** | LAS or LAZ in ground-based scaling "that includes the project's global coordinate system information" |
| **Split** | *By station* — one LAS per scan station; *None* — a single LAS from all stations in the setup |
| **Use inspection colors** | Exports heat-map colours from a Scan Inspection instead of true colour, in E57/LAS/LAZ |

The grid/ground/`.txt`/ECEF wording is **identical** to the classified-regions exporter
*(TBC 27279, batch 6)*. It is TBC's standard point-cloud export behaviour, not a mobile
mapping special case.

---

## 3. Publish to TRCPS *(TBC 29527)* — the second branch, now read

**Trimble documented fact** ✅.

The **Publish to TRCPS** command uploads point cloud data, trajectories and images from a TBC
project to a **Trimble Connect** project, via the **Trimble Desktop Utility (TDU)**, installed
alongside TBC. Requires a **Trimble ID**. Uploaded data consumes the account's Trimble Connect
storage quota.

**Reached at** *Home ▸ Data Exchange ▸ Publish to TRCPS*, then the **Mobile Mapping** tab.

### 3.1 The key sentence

> **"NOTE: By default, mobile mapping point cloud and trajectories will be automatically
> exported."** ✅

**The trajectory is not optional.** The publishing options — Publish panoramic Images, Publish
side Images, Publish back-facing images, Blur people, Blur vehicles — govern *imagery only*.
Point cloud and trajectory go regardless.

### 3.2 Selection, and the gap that survives

Selection is **by run, by multiple runs (Shift/Ctrl+Click), or by the entire mission
(Ctrl+A)** ✅ — genuinely run-aware, unlike the generic point cloud exporter. The selected
mission or run must include scan data; if not, Trimble says to run **Generate Scans** first.

❌ **But which trajectory is published is still not stated.** A run carrying both `Sbet` and a
`Reg. Trajectory` has two candidates, and topic 29527 does not say which travels — or whether
both do.

> This is now the **last unanswered documentation question on provenance**, and it is narrow
> enough to test in an hour: publish a registered run and look at what arrives in Trimble
> Connect.

### 3.3 Other recorded facts ✅

- **Blur people** and **Blur vehicles** are greyed out until an images option is selected
- Blurring prompts to use **GPU (if compatible) or CPU**
- Progress shows on the **Process View** tab and can be cancelled
- **View in Connect** opens Trimble Connect Web (`web.connect.trimble.com`) with the **Reality
  Capture** tab active; the TRCPS extension may need enabling at *Settings ▸ Extensions*
- The **3D+ View** offers **3D**, **Map**, **Image** and **Panorama** modes, and in 3D and
  Panorama **"trajectories and camera markers can be included or hidden as needed"** — so the
  trajectory is a first-class, viewable object in the delivered dataset
- Large publications show "Not ready for viewing" while processing

**Related but not the same command** *(TBC 28963)* ⚠ — *Workflow: Publish Point Cloud Data and
Panoramic Images to Trimble Connect* uses **Publish Scan Data**, a different command on a
static-scanner path. It is not the mobile mapping route. Recorded so the two are not confused.

---

## 4. Run a Mission Report *(TBC 23991_1)* — a definitive negative

The current version of the topic was captured. **It is substantively identical to the batch 2
capture of `23991.htm`.** ✅

> "Run a **Mission Report** to see the properties of a mission, including capture devices, runs,
> trajectories and generated scans."

Reached at *Mobile Mapping ▸ Reports ▸ Mobile Mapping Report*, or via *More Reports…* ▸
*Mission Report*. **Report Options** sets header, footer and other settings.

### What this settles

| Question | Answer |
|---|---|
| Does the Mission Report hold the **signed registration residuals** added in 2025.21? | ❌ **The topic does not say so.** It lists capture devices, runs, trajectories and generated scans — residuals are not mentioned |
| Does the Mission Report **attribute scans to a trajectory**? | ❌ **Not stated.** It lists trajectories and lists generated scans; no relationship between them is described |

> **Lead L1 stays at Partly confirmed and stops improving from documentation.** The 2025.21
> release note says signed residuals are "included in the report"; the only mobile-mapping
> report topic does not mention them. Either the release note means a *different* report — one
> with no help topic — or the topic is simply not exhaustive.
>
> **This is now a question only a test or the vendor can answer.** Run a registration, run a
> Mission Report, and look. Recorded as **testing required** and added to the vendor list.

---

## 5. The MX60 export surface — complete

Five paths, all now read:

| # | Path | Trajectory travels? | Trajectory identified? |
|---|---|---|---|
| 1 | **Export to LAS (Trajectory Split)** — classified regions *(27279)* | ❌ No | ❌ No |
| 2 | **Export to TMX** *(22501)* | ✅ **Yes** — "the trajectory file is created once for all devices" | ❌ **Not stated which** |
| 3 | **Export to TopoDot** *(23339)* | ❌ No | ❌ No |
| 4 | **Export to Solv3D** *(23888)* | ❌ No | ❌ No |
| 5 | **Export Point Cloud Files** — Point Cloud tab *(11769)* | ❌ No | ❌ No |
| — | **Publish to TRCPS** *(29527)* | ✅ **Yes, mandatorily** | ❌ **Not stated which** |

### What *is* carried out of TBC, across all paths ✅

| Carried | By which path |
|---|---|
| **Coordinate system and scale factor**, in a `.txt` sidecar | Any grid-scaled point cloud export |
| **Project global coordinate system**, embedded | ECEF option, LAS/LAZ |
| **GPS Time per point**, per ASPRS LAS 1.4 | Any LAS export with timestamps on |
| **Software name** — "Trimble Business Center" | Image EXIF |
| **The trajectory geometry itself** | TMX export; Publish to TRCPS |
| **Latitude, longitude, altitude, acquisition time** | Images, where GPS attributes are enabled |

### What is not carried, by any path

❌ Trajectory name or ID · adjusted trajectory name or ID · SBET filename · registration result ·
registration type · `_reg_####` sequence · source run or mission identifier in the data itself ·
calibration identity · processing date/time of the *trajectory* (as distinct from the imagery)

---

## 6. Classification — final, on documentation

> ### **PARTLY CONFIRMED** — and now a closed finding, not a gap
>
> The distinction matters. Batch 5 and batch 6 returned Partly confirmed **because topics were
> uncaptured**. That is no longer the reason.
>
> **Every export and publish path available to an MX60 has been read.** Not one is documented
> as writing trajectory identity into an exported artefact. Two paths carry the trajectory
> *geometry*; neither is documented as labelling it.
>
> **The honest limit of this finding:** Trimble's help topics describe dialogs, options and
> output structures. **They do not exhaustively enumerate LAS header fields, VLRs, or sidecar
> contents.** Something may be written that the documentation does not mention. That is a
> question about software behaviour, not about documentation — and **no further documentation
> collection will answer it.**

### The operational answer

> *If Parametrix later receives or reviews an exported point cloud, can we determine which
> adjusted trajectory produced it?*

**Not from anything Trimble documents.** Two mitigations exist and both are real:

1. **TMX and TRCPS deliveries include the trajectory.** An unlabelled trajectory can still be
   compared against a retained `sbet_<date>_reg_####.out`. That is a reconstruction path, and
   it depends on Parametrix retaining the SBETs.
2. **Coordinate system provenance is solid.** The `.txt` sidecar and the ECEF option mean the
   *frame* is never in doubt, even when the trajectory is.

**Both remain proposals for testing. Neither is written as procedure.**

---

## 7. Testing required — the consolidated list

Unchanged in status. **None of these is a recommendation, a default to adopt, or a procedure.**

| # | Test | Priority |
|---|---|---|
| **T18** | **Export timestamps = Yes reprocesses from raw** *(batch 6 §1)*. Export a registered run twice, timestamps off and on, and compare geometry. Determines whether a documented option silently undoes a registration | **1 — highest in the project** |
| **T19** | **Which trajectory does Publish to TRCPS send?** Publish a registered run; inspect what arrives in Trimble Connect | **2** |
| **T20** | **Which trajectory does the TMX export write?** Same test, TMX path | **2** |
| **T21** | **Does the Mission Report contain the signed registration residuals?** Register, run the report, look *(§4)* | **3** |
| **T22** | **Does a LAS/E57 export carry any undocumented provenance** — header fields, VLRs, sidecar contents? Export and inspect the file directly | **3** |
| **T23** | **Can the generic Point Cloud exporter span trajectories?** Draw a selection across scans from two trajectories and see whether TBC warns *(§2.1)* | **4** |
| T7, T9–T17 | Unchanged from batches 3, 4 and 6 — filter and registration defaults, target-bundle adjustment, sampling, cutting plane thickness | As recorded |

**No acceptance tolerance is proposed.** No numerical tolerance for registration or calibration
appears in any export topic. The Trimble position is unchanged: **good RMS cannot prove
success; bad RMS indicates failure; a visual check is necessary.**

---

## 8. Vendor questions — three additions

| Question | Why |
|---|---|
| **Does any TBC export write the source trajectory into a LAS header, VLR or sidecar?** | The one question documentation cannot answer |
| **Which trajectory do the TMX export and Publish to TRCPS send when a run has both an imported and a registered trajectory?** | §3.2, §5 |
| **Which report holds the signed GCP residuals added in 2025.21?** | §4 |

Added to `VENDOR-QUESTIONS.md`.

---

## 9. Figure recommendations

Continuing from **F35**.

| # | Figure | Source |
|---|---|---|
| F36 | The **Publish to TRCPS** note — "By default, mobile mapping point cloud and trajectories will be automatically exported" | 29527 |
| F37 | The **3D+ View** published result — colorized point cloud with trajectory and camera markers beside the georeferenced map | 29527 |
| F38 | **Export Point Cloud Files** Settings — Scaling, ECEF, Split | 11769 |

F17–F35 stand. **F32–F35 still cannot be cropped** — the batch 6 pages arrived inline and are
not archived.

---

## 10. Stop condition — **MET**

> ## The TBC source collection is sufficiently complete to begin SOP architecture and drafting.

Stated deliberately, against the earlier refusals to say it.

**Why it is met now.** The provenance question was the one material gap, and it is closed as a
documentation question. Every export and publish path an MX60 can use has been read. What
remains unknown is **software behaviour that Trimble does not document** — six specific,
bounded tests in §7 — and those cannot be resolved by collecting more help topics.

**What remains uncaptured is not material:** Blur Exported Images, Create Orthomosaics from a
Back-Camera System, Display Mobile Mapping Run Views, Run a Batch Command, Create CAD Entities,
Import Ortho Lane Images, Inspect Pavement Condition, AgileAssets, BBI Report. None bears on
collection, trajectory, registration, QC or delivery provenance. **Blur Exported Images is the
only one worth picking up later**, and only when imagery privacy is drafted.

**One archival gap stands:** the four batch 6 export pages (27279, 22501, 23339, 23888) arrived
inline and are not held as files, so F32–F35 cannot be cropped. That blocks figure production,
not drafting.

### What drafting is now blocked on

Not evidence. **Parametrix decisions and field testing** — which is the right place to be:

| Blocker | Owner |
|---|---|
| Registration acceptance criteria | Parametrix decision |
| Records retained at delivery | Parametrix decision |
| Whether a project backup suffices before Cleanup | Parametrix decision |
| Whether to provision for LiDAR QC | Parametrix decision |
| Which system configuration — Core, Pro, Premium | Vendor clarification |
| POSPac MMS licence and TBC version | Vendor clarification |
| T18–T23 and the earlier T-items | Field testing |

> **The guide can be architected and drafted around these**, with each marked **PARAMETRIX
> DECISION REQUIRED** where it belongs, exactly as the original instruction requires. What it
> cannot do is resolve them — and nothing in a Trimble document ever would.

---

*Source ingestion is complete for the purposes of drafting. No rewrite has been performed.*
