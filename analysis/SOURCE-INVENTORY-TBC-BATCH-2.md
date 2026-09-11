# Source Inventory — TBC Mobile Mapping Help, Batch 2

**Ingested:** 2026-09-11
**Status:** Source ingestion and classification only. **No rewrite performed.** More
Trimble material expected.

**Source:** 16 full-page captures of the Trimble Business Center help portal,
`https://help.fieldsystems.trimble.com/tbc/<id>.htm`, captured 2026-09-11.

**Provenance note:** supplied as page screenshots. The live pages could not be fetched
from this environment — egress to `help.fieldsystems.trimble.com` is blocked — so content
is read from the captures and cited by topic ID. The help portal carries no revision
number or date, and TBC version is not stated on any page. **Confirm the TBC version
before treating any UI detail as current.**

---

## A. The data-object chain — read this first

Everything in this batch operates on one of seven distinct objects. Conflating them is
the single largest source of confusion in the office workflow, so the eventual guide
should establish this chain before any procedure.

| # | Object | Format | Created by | Notes |
|---|---|---|---|---|
| 1 | **Raw mission data** | `.mxdb` + `.tmx` (+ `.pgr`, `.mxips`) | TMI, in the field | The mission database links everything |
| 2 | **Trajectory — imported** | SBET (`.out`) or NAV | POSPac / field | Set at import; shown in *Refine trajectory* |
| 3 | **Trajectory — adjusted** | "Reg. Trajectory" node | TBC registration | A *second* trajectory, not a replacement |
| 4 | **Generated scans** | `.rwcx` | Generate Scans | Point cloud with intensity, colour, normal |
| 5 | **Updated scans** | `.rwcx` | Update Scans | Re-derived against a *different* trajectory |
| 6 | **Panoramic imagery** | `.pgr` | 360° camera | Viewed at a **Station** |
| 7 | **Rectified imagery** | derived | TBC, on demand | Panorama unstitched into six flat images |

**The format conversion differs by system, and MX60 is the simple case:**

| System | Conversion path |
|---|---|
| MX9 / MX90 | RXP → TMX → RWCX (**two steps**) |
| **MX50 / MX60** | **TMX → RWCX (one step)** |

- **TMX** = scan raw data: polar scan coordinates, intensity, timestamp
- **RWCX** = point cloud: intensity, colour, normal

*(TBC 22499)*

> **This matters for MX60 specifically:** because the MX60 has no RXP stage, **MTA
> processing does not appear in the MX60 workflow at all.** See §F.

---

## B. Classification summary

| Topic | ID | Classification | Training level |
|---|---|---|---|
| Understanding Mobile Mapping | 20717 | CORE WORKFLOW | Basic |
| Mobile Mapping System Data Structure | 22503 | CORE WORKFLOW | Basic |
| Import the Mobile Mapping Data | 20736-1 | CORE WORKFLOW | Basic |
| View Data in the Project Explorer | 22554 | CORE WORKFLOW | Basic |
| Hide, Display and Center on a Trajectory | 22567 | CORE WORKFLOW | Basic |
| Navigate a long Mobile Mapping Run | 20727 | CORE WORKFLOW | Basic |
| **Generate Mobile Mapping Scans** | **22499** | **CORE WORKFLOW** | **Basic → Advanced** |
| **Update Mobile Mapping Scans** | **22638** | **CORE WORKFLOW** | **Intermediate** |
| Go to a Mobile Mapping Station Position | 22863 | QC / DOCUMENTATION | Basic |
| Display Rectified Camera Views | 28912 | ADVANCED PROCESSING | Intermediate |
| Define a Region of Interest | 26947 | ADVANCED PROCESSING | Intermediate |
| Split a Mobile Mapping Run | 24024 | ADVANCED PROCESSING | Intermediate |
| **Run a Mission Report** | **23991** | **QC / DOCUMENTATION** | **Basic** |
| **Recover Mobile Mapping Scans** | **28155** | **TROUBLESHOOTING / RECOVERY** | **Intermediate** |
| Mobile Mapping Options | 21243-1 | REFERENCE / SYSTEM CONFIG | Intermediate |
| Configure Graphic Card Driver for MTA | 23856 | REFERENCE / SYSTEM CONFIG | **Not MX60** |

---

## C. CORE WORKFLOW

### C1. Generate Mobile Mapping Scans — *(TBC 22499)*

**The major processing topic in this batch.** Treated at length below.

**What it does.** Extracts mobile mapping scans from the raw data files. For MX60,
converts TMX → RWCX in one step, computing XYZ coordinates for every point.

**Input.** A mission, run(s) or trajectory, plus the navigation/trajectory file (SBET or
NAV) set when the `.mxdb` was imported.

**Output.**
- RWCX point cloud files
- A **Point Cloud Region** node, auto-created as **Default**
- **Two Scan nodes** per run (Scan Right / Scan Left), nested under the imported trajectory
- A set of **Stations** under the Scans node, each containing a Scan node
  (e.g. `Run 1_Laser Left (S2)`)
- Optionally, six **PGM mask files** if colorization is used

*Single-scanner configurations produce only one side's station and scan nodes.*

**When a Parametrix processor uses it.** Immediately after import, once the trajectory is
correct. This is the step that turns a mission into a point cloud.

#### Dialog structure — MX60 differs from MX9/MX90

| Pane | MX9 / MX90 | **MX50 / MX60** |
|---|---|---|
| 1 | Runs | **Runs** |
| 2 | **MTA and Filters** | **Filters** *(no MTA)* |
| 3 | Scan Configuration | **Scan Configuration** |

**Constraint:** where a project holds several missions, only runs belonging to **the same
mission** can be selected and processed together.

#### Pane 1 — Runs

Check the **Mission** to select all runs, or check individual **Run** options. Selecting a
run lists its devices and raw data files. For MX60: Camera Back Down, 360° Camera, Laser
Right, Laser Left — all TMX.

#### Pane 2 — Filters (MX60)

Choose between **Default** and **High Quality**:

| Preset | Contents |
|---|---|
| **Default** | Isolated Points filter |
| **High Quality** | **Fog**, **Sun**, and **Reflective Panels** (Reflective Panels is MX60-only) |

| Filter | What it removes |
|---|---|
| **Fog** | On foggy days, a thick tunnel of very dark points at short distances around the vehicle trajectory |
| **Sun** | On sunny days, a burst of points from the scanner toward a single direction in the sky |
| **Reflective Panels** | Noise before and after a target |
| **Isolated Points** | Stray points |

**Restore Default Values** *(as stated by Trimble)*:

| Preset | Values |
|---|---|
| Default | Isolated Points **Off**, Range Min 0.50 m, Range Max **150 m (MX60)** / 80 m (MX50) |
| High Quality | Fog On, Sun On, Reflective Panels On (MX60), Range Min 0.50 m, Range Max **150 m (MX60)** |

> **Source inconsistency to resolve.** The prose says *"Default contains the Isolated
> Points filter, set to **On**"* while the Restore Default Values list says *"Default:
> Isolated Points **Off**"*. These contradict. Verify in the software before writing
> either into the guide.

*Note the 150 m MX60 Range Max aligns with the 150 m maximum range at the lower laser
rate from the MX60 User Guide (p.54) — a useful cross-check for the guide.*

#### Pane 3 — Scan Configuration

- **Trajectory** dropdown — selects which trajectory the scans are computed against
- **Colorize Points with panoramic view** checkbox — enables the **Mask** pane
- **Mask** pane: Vehicle mask **Generate**, Folder, Mask files, **Colouriser settings**
- **Colouriser settings**: No Preference · Prefer Backward Looking Sensors · Prefer
  Forward Looking Sensors

**Changing the trajectory before generation:** to use an SBET/NAV other than the one set
at import, open the **mission properties**, click the **[…]** on *Active trajectory file*,
and choose another in the **Select Trajectory** dialog. Mission properties also expose
Start/Stop time, UTC start/end, Duration, **Covered distance** and Import file.

#### Colorization and the mask

The principle: build a **Mask** covering undesirable areas, objects and obstructions
visible in the images, so their colour is not used for colorization — in practice, masking
out the vehicle itself.

Workflow:
1. **Save the VCE project first.** If not saved, TBC cannot resolve the mask folder path
   and errors out.
2. Click **Generate** → six **PGM** files are written, one per camera of the 360° camera,
   into the VCE project folder
3. Open each PGM in a third-party editor (**Irfanview** or **GIMP**) and fill the problem
   area with **RGB 0,0,0**
4. **Do not rotate the PGM files clockwise while editing** — Trimble states this may
   compromise the colorization result

A mask from another project may be reused **only if the capture system settings are
exactly the same**.

#### Result

**Results of Scan Generation** dialog — MX60 example content:

```
Finished processing of 1 run(s) at 9/10/2024 1:55:58 PM.
Mission "calib Ehmen", Run "Run 1_1": Colorization off.
Range - min: 0.500 m, max: 150.000 m.
Fog filter on.
Sun filter on.
Filter for reflective panels on.
```

**This is a per-run record of exactly which filters produced the cloud.** See §E1 — strong
QC/defensibility candidate.

**What could go wrong**
- Wrong trajectory selected → the entire cloud is computed against the wrong path
- Project not saved → colorization fails with a path error
- Mask rotated during editing → colorization compromised
- Mask reused from a system with different settings → wrong areas masked
- Runs from different missions selected → rejected
- Processing interrupted before save → see §F1 Recover Scans
- Filter preset mismatched to conditions → over- or under-filtered cloud

**How the result should be checked**
- Confirm the **Results of Scan Generation** text matches intended settings, and capture it
- Confirm Point Cloud Region point count is plausible for the corridor length
- Confirm two Scan nodes exist per run (or one, for single-scanner)
- Inspect in Plan View and 3D View for coverage gaps
- If colorized, inspect for vehicle self-colorization — the failure mode a bad mask causes

**Training level.** Basic for a default run; **Advanced** for filter selection,
colorization and masking.

---

### C2. Update Mobile Mapping Scans — *(TBC 22638)*

**Deliberately separate from Generate. The distinction is the point.**

| | **Generate Scans** | **Update Scans** |
|---|---|---|
| Starts from | Raw data, **from scratch** | Runs for which **an initial extraction already exists** |
| Path | TMX → RWCX (MX60) | **Straight TMX → RWCX** |
| Dialog lists | All runs | **Only already-extracted runs** |
| Panes | Runs / Filters / Scan Configuration | **Runs / Scan Configuration** — *no Filters pane* |
| Primary purpose | Produce the first cloud | **Switch between imported and adjusted trajectory** |

**What it does.** Re-derives the point cloud from the same raw data against a *different
trajectory* — specifically, it lets you switch between the **imported trajectory file**
and the **adjusted trajectory file**.

**Why it matters.** This is the step that makes trajectory adjustment meaningful. Register
or adjust the trajectory, then Update Scans re-computes every point against the improved
path. Without it, the registration exists only as a trajectory and never reaches the cloud.

**Input.** A mission, run or trajectory that has already been extracted, plus the target
trajectory.

**Output.**
- New RWCX files — **two per run** — under the **SdeDatabase** folder in the VCE project
- New **Stations** with a `_reg_####` suffix (e.g. `Run_14_Laser Right_reg_0001 (S3)`)
- **Two Scan nodes nested under the Registration Trajectory** of the run — so the original
  and adjusted clouds coexist in the tree

> **Both versions persist.** The original Scan Right/Left under `Sbet` and the new ones
> under `Reg. Trajectory` are both present. The guide must be explicit about which is
> being measured, exported and delivered.

**What could go wrong**
- Updating against the wrong trajectory — the failure is silent and looks like a valid cloud
- Confusing original and updated scans downstream
- Expecting filter changes — **Update Scans has no Filters pane**; changing filtering
  requires Generate, not Update
- MX9/MX90 only: the MTA option is hidden and defaults to unchecked when updating

**How the result should be checked**
- Confirm the new scans sit under the **Reg. Trajectory** node, not `Sbet`
- Compare the updated cloud against control — this is the whole reason for the step
- Confirm two RWCX files per run appear under `SdeDatabase`
- If nothing appears in Plan/3D View, check **Show scans after generation** in Options
  before assuming the update failed

**Training level.** Intermediate. A processor must understand trajectories before this
step makes sense.

---

### C3. Import the Mobile Mapping Data — *(TBC 20736-1)*

**What it does.** Imports a mission into a VCE project. For MX9/MX50/MX60/MX90, import the
mission database file (`.mxdb`); TBC creates an `.RWI` folder, an `.sdb` database and the
MXDB file inside the VCE project folder.

**Path.** `Home > Data Exchange > Import`, or drag-and-drop the file.

**Key behaviour.** If an **SBET** file is present in the data set it is **used by default**,
and its path shows in the **Refine trajectory** list. Settings also expose *Panoramic views
→ Automatically generate cache on import*.

**What could go wrong.** The default SBET is silently adopted — if it is the wrong or an
older trajectory, every downstream product inherits it. Verify the path at import.

**Training level.** Basic.

---

### C4. Mobile Mapping System Data Structure — *(TBC 22503)*

Useful corroboration: *"A Trimble MX60 mobile laser mapping system consists in its standard
configuration of two high-end laser scanners, a 360° camera and one rear downwards looking
camera, and GNSS/IMU system."* — independently confirms the MX60 User Guide configuration.

Mission directory naming: **system name + serial number + Mission ID** (from an increasing
counter), e.g. `TMX90123032001-000068`. The mission *name* is stored as an attribute inside
the mission database and appears once imported.

**Training level.** Basic — pairs naturally with SOP §11 Data Handling.

---

## D. ADVANCED PROCESSING

### D1. Display Mobile Mapping Rectified Camera Views — *(TBC 28912)*

**What it does.** Unstitches a 360° panorama into **six separate flat rectified images**,
each viewable in its own viewer, individually or simultaneously.

**When used.** Feature identification and extraction, where the distortion of a spherical
panorama makes an object hard to judge — reading sign faces, confirming asset condition.

**Input.** A Run with panoramic imagery. **Output.** Rectified views, camera markers
colour-coded by run, and a field-of-view indicator in Plan/3D View.

**Navigation.** Click a camera position in a rectified view to move all views to it; jump
next/previous/first/last; customise keyboard increments via Options; centre a camera in
Plan and 3D View.

**Gotcha.** The chosen view is **removed from the drop-down after selection** — which looks
like a fault but is not.

**Training level.** Intermediate — a productivity and extraction tool, not part of the
core sequence.

---

### D2. Define a Region of Interest — *(TBC 26947)*

**What it does.** Displays a customisable planar box (Plan View) or 3D box (3D View) around
a position on a trajectory, **hides scan points outside the box**, and lets you step the box
along the trajectory.

**When used.** Working a dense corridor cloud section by section — extraction, inspection,
or isolating a defect without loading everything.

**Parameters.** From beginning (A) · From end (B) · Width (C) · Length (D) · **Height (E —
disabled in Planar View, enabled in 3D View)** · **Step (F)** · Colour.

**Gotcha.** The command **only works on the graphic view it was opened for.** Opening it
for Plan View and expecting 3D View behaviour is a common confusion.

**Training level.** Intermediate. Productivity tool.

---

### D3. Split a Mobile Mapping Run — *(TBC 24024)*

**What it does.** Splits a long run into smaller chunks that can be selected individually
for processing.

**When used.** Long corridor runs where processing everything at once is impractical, or
where only part of a run is needed. Also useful for isolating a problem segment.

**Input.** An **unprocessed** run. **Output.** The run becomes two runs (`Unnamed Run 0_1`,
`Unnamed Run 0_2`), each with its own Sbet node.

**Procedure.** `Mobile Mapping > Processing > Split Run`, pick a position on the displayed
trajectory. The dialog reports **Timestamp** and **Distance From Beginning** for the split.

**What could go wrong.** The run must be **unprocessed** — splitting is not available after
extraction. Splitting also multiplies the runs to track downstream.

**Training level.** Intermediate.

---

## E. QC / DOCUMENTATION

### E1. Run a Mission Report — *(TBC 23991)*

**What it does.** Reports the properties of a mission — **capture devices, runs,
trajectories and generated scans**.

**Access.** `Mobile Mapping > Reports > Mobile Mapping Report`, or Quick Access Toolbar →
Reports → More Reports… → Mission Report. **Report Options** sets header, footer and other
settings.

**Why it matters.** This is the only single artifact in the batch that captures what was
collected and what was produced, in one place. Combined with the **Results of Scan
Generation** text (§C1) it forms a defensible record of how a deliverable was made.

> **FLAGGED — candidate Parametrix QC/project documentation requirement.**
> Not proposed as policy. If adopted, the natural rule would be: run a Mission Report per
> mission, retain it with the project record alongside the field protocol, and capture the
> Results of Scan Generation text for each run. **This needs a Parametrix decision and is
> not company policy unless and until that decision is made.**

**Training level.** Basic.

---

### E2. Go to a Mobile Mapping Station Position — *(TBC 22863)*

**What it does.** Displays the panoramic imagery from the **Station closest to a point
picked on a run**.

**When used.** Constantly, during QC and extraction — "what is actually here?" It is the
office equivalent of walking the site.

**Procedure.** Select run → **Toggle Trajectory** (Plan View draws each run's trajectory in
its own colour) → `Mobile Mapping > View > Go to Run Position` → pick a position. The **Run
View** tab opens on the nearest Station.

**Training level.** Basic. Should be taught early — it is how a processor checks anything
ambiguous.

---

## F. TROUBLESHOOTING / RECOVERY

### F1. Recover Mobile Mapping Scans — *(TBC 28155)*

**The most operationally important item in this batch after Generate/Update.**

**The underlying hazard, in Trimble's own terms:** when TBC generates or updates scans, the
resulting RWCX files **are not saved in between or at the end of processing**. If TBC is
interrupted before the VCE project is saved, **the link with the generated scans is lost**.

**Recovery.** Re-open the interrupted VCE project. A prompt offers to repair the database:

| Choice | Effect |
|---|---|
| **Yes** | Recovers scans generated before the interruption and continues processing the remaining run(s). Scans reappear in 3D View and Project Explorer. **Save the project immediately after recovery.** |
| **No** | Does not recover; cleans up the database |

**The preventive rule this implies:** **save the VCE project immediately after scan
generation or update completes.** Scan generation on a full mission is long; an unsaved
crash costs the whole run.

**Training level.** Intermediate — but the *preventive* rule belongs in basic training.

**Related:** Mobile Mapping Options includes **Registration auto-saving**, which
automatically saves targets picked during run or mission registration so they are not lost
(§G1). Same family of hazard.

---

## G. REFERENCE / SYSTEM CONFIGURATION

### G1. Mobile Mapping Options — *(TBC 21243-1)*

`Options` in the Quick Access Toolbar → Mobile Mapping. Also reachable from any camera view.

| Option | Effect | Note |
|---|---|---|
| Number of observations per point | More observations → more accurate created point | MX7-oriented |
| Spatial Picker step | Stations the view jumps when an observation is made; may be negative | MX7-oriented |
| **Automatic enhancement of side views** | Enhances side and down-looking camera images in dark areas | Relevant to MX60 back-down camera |
| **Show scans after generation** | Shows/hides scans after generating or updating | **Explains "my scans didn't appear"** |
| Page Up/Down station increment | Camera markers to move per keypress | Navigation comfort |
| **Registration auto-saving** | Auto-saves targets picked during run or mission registration | Data-loss prevention |

**Training level.** Intermediate. Set once; two entries prevent support calls.

---

### G2. Configure your Graphic Card Driver When Using the MTA Correction — *(TBC 23856)*

> **Likely NOT applicable to MX60.** MTA is part of the **RXP → TMX** conversion, which
> exists only for MX9/MX90. The MX60 Filters pane contains **no MTA option**, and the MX60
> path is TMX → RWCX in one step. **Confirm with Trimble before including this in an MX60
> guide**; if confirmed, it should appear only as a note explaining why MX60 processors
> will not encounter MTA.

**What it says.** On laptops with both integrated and dedicated graphics, using the
integrated card while applying MTA correction **increases noise in the scan result and
increases processing time**. Trimble recommends **CUDA-enabled Nvidia** cards, updating to
the latest driver, and configuring TBC to use the high-performance card — set it in both
NVIDIA Control Panel → Manage 3D Settings → **Global Settings** and **Program Settings**
(selecting `TrimbleBusinessCenter.exe`).

**Classification.** Conditional workstation guidance. **Outside the normal processing
sequence.**

---

### G3. MTA — the concept, for reference only

**MTA = Multiple Times Round.** Arises at high measurement rates, where range ambiguity
causes points to be recorded at the wrong distance. The MTA correction module detects and
corrects the false distance by applying the correct MTA zone.

In the MX9/MX90 dialog it also controls the conversion path: **checked** → RXP → SDCX →
TMX; **unchecked** → RXP → TMX directly.

Filter presets referencing MTA — **Default** (MTA On, Auto), **Rail** (MTA On, Auto,
enhanced filtering near railheads), **Power Lines** (**MTA Off**, for work where cables are
the point of interest) — belong to the **MX9/MX90** filter set, alongside Amplitude,
Reflectance, Deviation and Range parameters.

> Retained here for completeness and because the terms appear in shared dialogs. **Do not
> teach as MX60 procedure without confirming applicability.**

Definitions worth keeping if any of this proves relevant:
- **Amplitude** — ratio of detected optical amplitude of the echo to the scanner's
  detection threshold, in dB. Falls with distance.
- **Reflectance** — ratio of the target's optical amplitude to that of a diffuse white flat
  target at the same range, in dB. Negative = diffuse, positive = retro-reflective.
- **Deviation Gate** (Deviation Min→Max) — filters **mixed pixels**, the noise echoes
  between two objects struck by the same pulse. **Lower Deviation Max deletes more mixed
  pixels.**
- **Range Gate** (Range Min→Max) — the range window the scanner measures within.

---

## H. Recommended figures for the eventual guide

Cropped figures only. **No full-page captures** — every source page is 1,400–17,800 px tall
and unusable as a figure.

| # | Source | Crop | What it must demonstrate |
|---|---|---|---|
| F1 | 22499 | MX60 *Runs* pane, dialog only | The three-pane structure **Runs / Filters / Scan Configuration** — and that MX60 has no MTA pane |
| F2 | 22499 | MX60 *Filters* pane, dialog only | Default vs High Quality, and the Range min/max fields |
| F3 | 22499 | MX50/MX60 *Scan Configuration* pane | Trajectory dropdown + Colorize checkbox + Mask pane together |
| F4 | 22499 | Mission Properties panel | Where **Active trajectory file** lives and the **[…]** button |
| F5 | 22499 | Before/after PGM mask pair | The masking concept — unmasked vs filled black. Crop tight to the vehicle area |
| F6 | 22499 | **MX60 Results of Scan Generation dialog** | The per-run filter record. **Highest-value single figure in the batch** |
| F7 | 22499 | Project Explorer after generation | Point Cloud Region + two Scan nodes under the trajectory |
| F8 | 22499 | Scan Stations tree | Station naming `Run 1_Laser Left (S2)` |
| F9 | **22638** | Update dialog **Trajectory dropdown expanded** | Both `Sbet` and `Reg. Trajectory` listed — **the single most important figure for the Generate vs Update distinction** |
| F10 | **22638** | Project Explorer with both trajectories expanded | Scans under `Sbet` *and* under `Reg. Trajectory` coexisting |
| F11 | 22638 | SdeDatabase folder listing | Two RWCX per run, and where they live |
| F12 | 26947 | The labelled A–F box diagram | Region of Interest parameters against the trajectory |
| F13 | 24024 | Plan View with **Run Split Point** | What a split looks like before committing |
| F14 | 21243-1 | Options table rows only | **Show scans after generation** and **Registration auto-saving** |
| F15 | 22503 | Mission directory name with A/B/C callouts | System + serial + Mission ID naming |
| F16 | 22863 | Plan View with coloured trajectories + Run View | How station imagery is reached from a picked point |

**Redraw rather than screenshot:** the data-object chain in §A. A clean diagram of
raw → trajectory (imported / adjusted) → generated scans → updated scans, with imagery
branching to panoramic and rectified, would carry more than any screenshot here.

---

## I. Open questions raised by this batch

| # | Question | Why it matters |
|---|---|---|
| 1 | **Which TBC version** does Parametrix run? | Determines whether §12.3 calibration happens in TBC, and whether these UI details are current |
| 2 | **Isolated Points filter — On or Off by default?** Trimble's prose and its Restore Default Values list contradict each other | Affects the default cloud |
| 3 | Does **MTA** appear anywhere in MX60 processing? | Decides whether G2/G3 belong in the guide at all |
| 4 | When is **High Quality** preferred over **Default** for MX60? Trimble states what each contains but not when to choose | A processor needs a rule, not a list |
| 5 | Does the **Reflective Panels** filter risk removing legitimate retro-reflective returns — signs, line marking? | Directly relevant to asset extraction and retroreflectivity work |
| 6 | Is **Mission Report** adopted as a Parametrix QC requirement? | Flagged, not decided — §E1 |
| 7 | What is the practical guidance on **Colouriser settings** (forward vs backward preference)? | Trimble defines the options but gives no selection rule |

---

## J. What this batch does *not* cover

Still absent from the office workflow, and still needed before Section 12 can be a
procedure rather than an overview:

- **Trajectory processing itself** — running the GNSS/IMU solution in TBC or POSPac
- **Registration to control** — the smart picking tool and PFix engine in practice
- **Point cloud classification and feature extraction** procedures
- **Export** formats and settings
- **Trajectory report interpretation** — what good looks like numerically

---

*No SOP section has been rewritten. Section 12 still reflects the earlier source set;
this inventory is input for the eventual restructure, pending further material.*
