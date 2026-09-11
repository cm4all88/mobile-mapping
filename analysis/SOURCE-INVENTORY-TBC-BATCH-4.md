# Source Inventory — Batch 4: the registration and calibration branches

**Prepared:** 2026-09-11
**Status:** Ingestion and classification. **No rewrite performed.**

**Captures:** `../sources/tbc-help-captures-batch4/` — 15 TBC help topics
**Supersedes the gap list in** [`SOURCE-INVENTORY-TBC-BATCH-3.md`](SOURCE-INVENTORY-TBC-BATCH-3.md) §1

---

## 0. What arrived, and what it closes

Batch 3 identified three missing branches as the reason the eight registration questions
could not be answered. Batch 4 contains **two of the three in full, and the third entire**:

| Batch 3 priority | Status now |
|---|---|
| 1. **Register Mobile Mapping Trajectories** | ✅ **Complete** — all five sub-topics |
| 2. **Cleanup Mobile Mapping Mission** | ✅ **Complete** — the topic is four sentences long |
| 3. **Perform Mobile Mapping Calibrations** | ✅ **Complete** — all nine sub-topics |
| 4. Export Mobile Mapping Data | ❌ still missing — now the **only** material gap |

**Six of the eight questions are now answered from Trimble's own text.** One is partly
answered. One — the proof-of-trajectory question — is *better* answered than batch 3
expected, and the remainder of it depends entirely on the Export topic.

> Two caveats carried forward unchanged: the help portal states no version and no date, and
> **nothing in this batch is Parametrix procedure.** Everything below is Trimble behaviour
> (marked ✅), inference (⚠), or an explicit proposal for testing.

---

## 1. Classification

Categories as established in batch 2: **CORE WORKFLOW · ADVANCED PROCESSING ·
QC-DOCUMENTATION · TROUBLESHOOTING-RECOVERY · REFERENCE-SYSTEM CONFIGURATION.**

| # | Topic | TBC ID | Category | Training level |
|---|---|---|---|---|
| 1 | **Register a Run** | 22905 | **CORE WORKFLOW** | Intermediate |
| 2 | **Register a Mission** | 26473 | **CORE WORKFLOW** | Intermediate |
| 3 | Edit a Run | 25362 | CORE WORKFLOW | Intermediate |
| 4 | Edit a Mission | 26578 | CORE WORKFLOW | Intermediate |
| 5 | **Register Multiple Pairs of Runs** | 25096 | ADVANCED PROCESSING | Advanced |
| 6 | **Cleanup Mobile Mapping Mission** | 26466 | CORE WORKFLOW *(destructive)* | Intermediate |
| 7 | **Process Raw Trajectory Data** | 25943 | ADVANCED PROCESSING | Advanced |
| 8 | **LiDAR QC Processing** | 28972 | ADVANCED PROCESSING | Advanced |
| 9 | Generate POSPac Position Fixes | 24460 | ADVANCED PROCESSING | Advanced |
| 10 | Calibrate Mobile Mapping Laser Scanners | 24886 | ADVANCED PROCESSING | Advanced |
| 11 | Calibrate Mobile Mapping Cameras | 24868 | ADVANCED PROCESSING | Advanced |
| 12 | Perform a Manual Camera Calibration | 20728 | ADVANCED PROCESSING | Advanced |
| 13 | Import / Export Calibration File (.json) | 22920 | REFERENCE-SYSTEM CONFIGURATION | Intermediate |
| 14 | Trajectory Color Settings | 27248 | **QC-DOCUMENTATION** | Basic |
| 15 | View Trajectory Plots | 27415 | QC-DOCUMENTATION | Basic |

---

## 2. The four topics that change the guide

### 2.1 Register a Run *(TBC 22905)* — CORE WORKFLOW

**What it does.** Adjusts one run's trajectory by matching **ground control points (GCPs)
imported into the project** against **targets the operator picks in the point cloud**. ✅

**Trimble's own definitions, verbatim in substance:** ✅
- A **GCP** is "an accurately surveyed coordinate location for a physical feature that can
  be identified on the ground, e.g., a corner on the pavement markings"
- A **target** is "a point extracted from the acquired scan data"

> **This settles the batch 3 ambiguity.** Registration observations are **GCP-to-cloud
> pairs**, not cloud-to-cloud ties. Cloud-to-cloud matching exists, but it is a *different
> command* — Register Run to Run (§2.3).

**Inputs** ✅
| Input | Requirement |
|---|---|
| Scan data | At least one generated scan, or the command is dimmed |
| GCP file | Shape, ASCII or CSV, imported into the project; lands under the **Points** node |
| Picked targets | One GCP/target pair is the minimum to compute |

**The registration methods** ✅ — Trimble's descriptions, not paraphrase:

| Method | What it does | When Trimble says to use it |
|---|---|---|
| **Global** | A shift of the whole trajectory, **without rotation**. No local adjustment near control | "consistent differences between the laser data and the ground control points… data can be corrected with a simple shift" |
| **Local** | Local adjustment with **interpolation between** control points | "suitable for a local adjustment of a run, **not for systematic error along the run or for adjusting outside the ground control points set**" |
| **Global, and then Local** | Global first, then Local | *(no separate guidance given)* |

> **IMPORTANT for the guide.** Trimble states plainly that **Local does not extrapolate**.
> Beyond the first and last control point the trajectory is not adjusted. That is a
> corridor-geometry consequence a surveyor will recognise immediately, and it belongs in
> the plain-English layer.

**Control vs check** ✅ — this is the answer to a question the SOP could not previously ask:

| Column | Meaning |
|---|---|
| **Use XY** | Optimise the horizontal coordinates of this GCP |
| **Use Z** | Optimise the vertical coordinate |
| **As Check** | **Validation point (VP)** — "used only for measuring the quality of the registration… The resulting XYZ residual values **will not be taken into account in the registration**" |

- A validation point **still has to be paired with a picked target** ✅
- **At least one GCP must not be a check point**, or TBC errors ✅

> This is the conventional control/check split, implemented per-point and per-component.
> The SOP can therefore describe check points in TBC without inventing anything.

**Target picking — the Point Cloud Smart Picking tool** ✅

| Picking type | Use |
|---|---|
| **Default** | Snap to a cloud point near the GCP. Not for road marks or plane intersections |
| **Intersected Plane** | Fits a plane near the rough pick and projects onto it. Target sub-types: **Single Pick, Checkerboard (0.5 m), Diamond (0.4 m edge), Rectangular (0.5 × 0.5 m), GV Target (L-shape, 0.08 m bolt)** |
| **Road Mark** | Picks a point on a **pavement marking edge line** |

Each pick opens **Validate Picking**, showing an overhead view, a side view perpendicular to
the trajectory, the 3D coordinates, **the RMS of the fitted plane**, and — in the current
version — **direct residuals to the GCP, updated live as the template is nudged**. ✅

> **This is the single most useful fact in the batch for training.** The operator sees the
> residual *before* committing the pick. The workflow is "pick, read the residual, adjust,
> then validate" — not "pick everything, compute, then discover the problem."

**Numeric constraints Trimble states** ✅

| Constraint | Value |
|---|---|
| Maximum GCP-to-target distance in a pair | **30 m (100 ft)** — exceeded pairs are rejected |
| Target-bundle adjustment **checked** | Bundle adjustment at **250 m** acquisition intervals — "few GCPs… accuracy of the GCPs is moderate… precision in target picking is less stringent" |
| Target-bundle adjustment **unchecked** | Bundle adjustment at **70 m** intervals — "more GCPs available… accuracy of the GCPs is high and precise target picking is necessary" |
| Keyboard nudge (camera calibration) | ±0.001° arrow, ±0.01° Ctrl+arrow / PgUp / PgDn |

> **Note the inversion.** *Checking* the box makes the adjustment **coarser** (250 m), not
> finer. The option name reads the other way round to most people. Flagged as **T9**.

**Two warning icons Trimble defines** ✅
- Picked point is **not a 3D point** (no Z) and/or does not belong to the scan of the run
  being registered
- Picked point **does not belong to the most recent scan** of that run

In both cases: pick again. ✅

**Outputs** ✅
- An **adjusted trajectory node** nested beneath the run, named *RunName* **Trajectory**
- A **new SBET/NAV file on disk**, `sbet_<date>_reg_####.out`, rooted in the project folder
  and **incrementing** (`_reg_0001`, `_0002`, …)
- Picked targets renamed *RunName TrajectoryGCPName*; updated targets get a trailing `*`
- Trajectory properties carry **Origin: Registration result**, **Input trajectory: Imported
  trajectory**, **Registration type: GlobalThenLocal**

**What can go wrong** ⚠ *(assessment, flagged)*
- Picking a target on a *superseded* scan (the second warning icon)
- Setting every GCP As Check — blocked, but the near-miss is invisible
- Using **Local** and expecting adjustment beyond the outermost control point
- **Closing the command without applying** — "TBC will prompt you to discard collected
  points." If Registration Auto-Saving is off, the picks are gone

**Registration Auto-Saving, resolved** ✅ — batch 3 flagged this as **T7**; Trimble now
states the mechanism:
> Picked targets are saved to a **`Targets.csv`** in the project, even if the project has
> not been saved, and even if Register a Run was closed without applying. Reopening the
> command prompts to reload them. **Choosing "No" empties Targets.csv permanently.**

> **T7 partially closes.** The mechanism is documented; the **default state** still is not.

---

### 2.2 Register a Mission *(TBC 26473)* — CORE WORKFLOW

Same command family, different scope. The differences that matter:

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs at once, not sequentially |
| GCP reuse | Once per registration | **Every GCP can be used more than once** — with different run clouds or different passes of the same run ✅ |
| Control list | One row per GCP | **One row per GCP *instance*** — TBC creates an instance per **250 m scan section** whose bounding box contains the GCP ✅ |
| Side | — | An instance binds to the **left, right, or both** sides of the scan section ✅ |
| Default name | *RunName* Trajectory | **Reg** |
| Naming | *RunName TrajectoryGCPName* | ***RegistrationName*_*GCPName*_*RunName*** |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** ✅ |
| Unused instances | — | "All unused instances are removed from the Control Points list" ✅ |

> **Why this matters, and it is not obvious.** On a corridor driven in both directions, or
> on overlapping passes, the same painted mark is a *separate observation* in each pass.
> Mission registration is what lets one surveyed GCP constrain all of them simultaneously —
> which is the normal survey situation, not the exception. **Register a Mission is likely
> the default Parametrix workflow, not Register a Run.** That is a proposal, not a decision.

---

### 2.3 Register Multiple Pairs of Runs *(TBC 25096)* — ADVANCED PROCESSING

**Command name in the UI: Register Run to Run.** This is the cloud-to-cloud path, and it is
a genuinely different thing from GCP registration.

**What it does** ✅ — registers runs **two by two in batch**, from the same or different
missions. In each pair one run is the **Reference Run** (its trajectory does not change) and
one is the **Run to Adjust** (optimised to the reference). A new trajectory is created for
the Run to Adjust and its scan data is updated so the two clouds match.

**Prerequisites** ✅ — both runs need at least one scan (left or right, either), and
**enough overlapping scan data along the trajectories**.

**A useful exception** ✅ — "Missing TMX files" in the Status column does **not** block the
command: *"you do not need to generate the scans first, TMX files will be generated on the
fly."* This contradicts the pattern of every other registration command, which requires a
generated scan.

**Quality output — this is the registration report batch 3 could not find** ✅

> TBC computes statistics into a **Results** tab. **Timestamps are computed every twenty
> metres depending on vehicle speed. For each timestamp, three RMS values are computed in
> three directions: Tangential, Orthogonal and Vertical.**

Cells read `No overlap` where there is none, and a metric value (e.g. `0.014 / 0.011 /
0.016`) where there is. The same three-axis convention appears in laser scanner calibration
*(TBC 24886)*, so it is TBC's standard mobile-mapping agreement metric.

**Visual validation** ✅ — checking **Open Cutting Plane View** creates a plane named
*MissionID Last Two Digits - Run to Adjust* per pair, renders a profile of the two clouds,
and the operator drags a slider along the run to inspect the gap. Trimble's guidance on
reading it (from the calibration topic, identical wording): **good RMS does not prove
success; bad RMS does prove failure.**

**Update Scans is an option inside this command** ✅ — checking it regenerates the Run to
Adjust's scans on the new trajectory immediately and enables the Cutting Plane View. This is
the one place where Update Scans is not a separate step.

---

### 2.4 Cleanup Mobile Mapping Mission *(TBC 26466)* — CORE WORKFLOW, destructive

The whole topic, and every word of it matters:

> "Keeping the most recent registration (and related scans), and trajectory consistent with
> the latest version of navigation and trajectory information file (**SBET** or **NAV**).
> This feature can be run at the end of the data preparation process (registration,
> colorization, etc.), it allows you to share a light project, before moving on to a feature
> extraction phase. **Please, have a backup copy of your project prior performing the
> operation, it cannot be undone.**" ✅

Run from the **Mission** node's context menu. ✅

> **This is the tool that resolves the proof gap — and it is also the tool most likely to
> destroy evidence.** It deletes every superseded registration and its scans, so afterwards
> the project contains exactly one answer to "which trajectory did the delivered scans use."
> It also deletes the audit trail that would have shown the earlier attempts.
>
> **PROPOSED PARAMETRIX PRACTICE — not Trimble behaviour, not adopted.** Run the Mission
> Report *before* Cleanup, archive it with the project, then back up, then Cleanup. The
> order is the whole point. **Requires testing and a decision.**

---

## 3. Trajectory production — what batch 4 adds upstream of registration

### 3.1 Process Raw Trajectory Data *(TBC 25943)*

TBC can compute the SBET itself, **without opening POSPac** — but it still requires
**POSPac MMS 8.6+ installed alongside TBC with a valid licence.** ✅

Inputs: raw POS logged files (`POS_1/raw`, processed sequentially from the first selected),
plus **base station RINEX observation** imported into TBC *first*. Ephemeris files (`.YYg`,
`.YYn`) must **not** be imported. ✅

**MX60-specific fact, and the first one found in any TBC source:** ✅
> Rover antenna model: **Tallysman/33-3970 GNSS** for MX9/MX50; **Trimble 112735 GNSS for
> MX90 or MX60.**

**Settings, with Trimble's stated defaults:** ✅

| Setting | Values | Default |
|---|---|---|
| Computation Mode | IN-Fusion+ **Single Base** (local base) · IN-Fusion+ **PP-RTX** (no local base) | not stated |
| Initialization Mode | VNAV · **Gyro-compassing** · GAMS · GAMS and Gyro-Compassing | **Gyro-compassing** |
| Multipath | Low (good coverage) · **Medium** · High (urban canyon, narrow streets, dense foliage) | **Medium** |
| DMI scale factor SD | percentage | **5 %** — "set it to 100 % if it is not known at all" |
| DMI scale factor sign | **positive** = DMI on left of vehicle, **negative** = right | — |
| LiDAR QC (Refine with scans) | on/off | off (requires MATLAB Runtime R2024b) |
| Generate QC Report | on/off | — |

Vehicle-frame axis convention, stated for lever arms: **+X forward, +Y right, +Z down.** ✅
(The same convention appears in both calibration topics.)

**Outputs** ✅ — `sbet_[mission].out` if POSPac knows the project datum and epoch;
`sbet_[mission]_[frame].out` computed first in ITRF00 then transformed, if it does not. SBET
and report land under `NAVPROC/Export` and `NAVPROC/Report`. **The created SBET is coloured
by the computed RMS.**

> **Flag for testing (T10).** "Unknown by POSPac" silently introduces an extra datum
> transformation. A processor should know which of the two filenames they are looking at,
> because the second one means POSPac did not recognise the project's coordinate system.

### 3.2 LiDAR QC Processing *(TBC 28972)*

"An advanced trajectory processing technology that, similar to **LiDAR SLAM**, uses scan data
as an **aiding sensor** to improve georeferencing accuracies in areas of poor GNSS coverage or
where overlapping scans are not perfectly matching… generates 3D Voxels matched in overlap
scan regions… solving the constant IMU boresight angles and making corrections to the
post-processed trajectory (position and orientation)." ✅

**Trimble's calibration-pattern prescription** ✅ — the first field procedure in any source
for a calibration drive:

| Element | Requirement |
|---|---|
| Area | Structured scene — residential, detached houses, objects **within the LiDAR's maximum range**; **open sky** for good GNSS |
| Strips | **Two perpendicular strips**, each driven **in both directions** (four runs) |
| Strip length | **250–300 m** |

> This is materially the same geometry the laser scanner calibration requires ("four runs,
> two in a direction and two orthogonal"), so **one site can serve both.** SOP §5.7 already
> anticipates a calibration site; this gives it dimensions from Trimble rather than from us.

**MX60-specific default** ✅ — LiDAR QC **Noise**: "the default value is **5 mm for an
MX 50/60** and 10 mm for an MX 9/90." Range default **3 m to 100 m**. Lasers default **All**,
though Trimble notes using both "can increase computation time without significantly
improving the accuracy."

**Workstation requirements — conditional guidance, not a purchase order** ✅

| | Minimal | Recommended |
|---|---|---|
| CPU | Intel Core i7/i9 | Intel XEON |
| RAM | 128 GB | 256 GB |
| TEMP storage | 1 TB SSD on PCI bus | 2 TB SSD M.2 on PCI bus |
| Virtual memory | +1 TB SSD always available | +2 TB SSD M.2 (or 4 TB combined) |
| Paging file | — | initial = installed RAM, **maximum = 6 × installed RAM** |
| Other | **MATLAB Runtime R2024b (24.2)**, installed after TBC | |

> **PARAMETRIX DECISION REQUIRED — candidate.** LiDAR QC is the only documented remedy for
> poor-GNSS corridors that does not require additional field control, and it is out of reach
> of an ordinary workstation. Whether Parametrix provisions for it is a capability decision,
> not a software setting. **Not adopted; added to the register at the rewrite.**

### 3.3 Generate POSPac Position Fixes *(TBC 24460)*

The other poor-GNSS remedy, and the opposite trade: it needs **control**, not hardware.

Measures the offset between GCPs and picked targets, **projects those offsets back onto the
trajectory**, writes a **`custom_events.txt`** into a `PFIX` folder, and POSPac MMS consumes
it as position fixes on a **second processing pass**. ✅ The corrected SBET then replaces the
mission's trajectory in TBC and **Update Scans** is run. ✅

Same picking tool, same 30 m pair rule, same one-pair minimum. Updated targets are named
*Mission_Name*-PFIX-*GCP_Name*. ✅

> **The distinction the guide must draw, because Trimble never states it side by side:**
>
> | | **Register a Run / Mission** | **Generate POSPac Position Fixes** |
> |---|---|---|
> | Where the correction is applied | On the trajectory **after** the navigation solution | **Inside** the navigation solution, as an observation |
> | Software needed | TBC only | TBC **and** POSPac MMS |
> | Passes | One | Two |
> | Result | A registered trajectory in TBC | A better SBET, from which everything re-derives |
>
> Registration corrects the answer; PFIX corrects the computation. ⚠ **That framing is ours,
> inferred from the two topics, and should be checked with the vendor before it is taught.**

---

## 4. Calibration — what changed

`../sources/TBC-Calibrate-Mobile-Mapping-Laser-Scanners.md` (topic 20716) is confirmed by
the batch 4 capture of **24886**, which is the same content under a slightly different
title. **SOP §12.3 does not need rewriting** — but three things are now additionally known:

1. **Cameras have their own calibration path** *(TBC 24868, 20728)*. Up to TBC 5.21 cameras
   were calibrated outside the application and imported as JSON; **Manual Camera
   Calibration** lets an operator enter Heading/Pitch/Roll directly against a live camera
   view at a picked trajectory position, nudging in 0.001° steps and watching the image
   update. Frames: 360° camera, vehicle, oblique (1/2), down-looking. ✅
2. **The JSON carries both matrices** *(TBC 22920)* — the **Installation Matrix** (before
   calibration) and the **Refinement Matrix** (after), for **each sensor**. Import and Export
   Calibration both sit on the **mission node** context menu. ✅
3. **The calibration record is in the Mission Report** *(TBC 24868)* — the *Capture devices*
   table carries, per sensor: Boresight installation · **Boresight calibration** · Lever arm
   installation · Lever arm calibration · **Date of calibration**. ✅

> **That last one closes a real gap.** Batch 3 could find no record proving *when* the system
> was last calibrated. The Mission Report carries it per sensor, per mission.

---

## 5. The eight questions — answered

Verified Trimble behaviour ✅ · inference ⚠ · unknown ❌

### Q1 — How is an adjusted / Registration Trajectory created? ✅ **ANSWERED**

Three commands produce one, and they are not interchangeable:

| Command | Constraint used | Scope |
|---|---|---|
| **Register a Run** | Surveyed GCPs ↔ picked targets | One run |
| **Register a Mission** | Same, with GCP instances per 250 m section, reusable across runs | A set of runs |
| **Register Run to Run** | Cloud-to-cloud overlap against a fixed Reference Run | Pairs, batched |

Each writes a new trajectory node under the run and an incrementing
`sbet_<date>_reg_####.out` in the project folder. **Batch 3's inference that registrations
are numbered and repeatable is confirmed.** ✅

### Q2 — What observations or control can constrain it? ✅ **ANSWERED**

Surveyed **GCPs** paired with operator-**picked targets** in the cloud, one pair minimum,
30 m maximum separation within a pair, each GCP usable for **XY**, **Z**, or **both**, or as
a **validation point**. Picked targets persist in `Targets.csv` when auto-saving is on.
Cloud-to-cloud overlap is a separate command, not an option within GCP registration.

### Q3 — What quality indicators does TBC provide? ✅ **ANSWERED**

| Level | Indicator | Where |
|---|---|---|
| Per pick, live | Easting / Northing / Elevation residual to the GCP, signed | Targets pane and Validate Picking |
| Per pick | **RMS of the fitted plane** | Validate Picking |
| Per run pair, every 20 m | **RMS in Tangential, Orthogonal, Vertical** | Results tab *(Run to Run)* |
| Whole calibration | Overall Overlap %, Overall RMS, per-pair RMS in three axes | Calibrate Laser Scanners |
| Trajectory-wide | SBET coloured by **position/orientation/velocity RMS** from `smrmsg_xxx.out` | Plan View |
| Visual | **Cutting Plane View** profile of two clouds | Point Clouds ▸ View |

### Q4 — Acceptable versus unacceptable result? ⚠ **PARTLY — and Trimble states a rule, not a number**

Trimble publishes **no acceptance threshold** for registration. It publishes a rule about
the logic of the test, twice, in identical wording in two different topics:

> "Good RMS values do not mean that the calibration succeeded. A visual check is needed. On
> the other side, bad RMS values mean that the calibration failed."

Batch 3 proposed carrying this asymmetry forward as a hypothesis. **It is now confirmed
Trimble's own position across the calibration and run-to-run registration topics.**

> **Consequence for Parametrix, stated as a proposal only:** any acceptance rule must pair a
> numeric threshold with a **mandatory visual check in Cutting Plane View**, because Trimble
> explicitly says the number alone cannot demonstrate success. **The threshold itself remains
> undefined and unproposed** — it is a project-accuracy decision, not a software fact.

### Q5 — Does registration change the trajectory only? ✅ **ANSWERED — trajectory only, until you act**

Confirmed and strengthened. Registration writes a new trajectory node and a new SBET file.
Existing scans are untouched. Two exceptions found in batch 4:

- **Register Run to Run** has an **Update Scans checkbox** that regenerates scans in the same
  operation ✅
- **Generate POSPac Position Fixes** does not touch scans at all — the operator manually
  replaces the mission trajectory afterwards, then runs Update Scans ✅

❌ Still unknown: whether imagery / station positions inherit the adjustment. The batch 3
empirical test (compare a station's panoramic position before and after) stands.

### Q6 — When is Update Scans required? ✅ **ANSWERED**

Whenever a registered trajectory must be reflected in the point cloud — and in **both**
directions, since the dialog switches between imported and adjusted. Not required when
Register Run to Run did it inline. Required after replacing an SBET following a PFIX pass.

### Q7 — How can a processor prove the final scans use the intended trajectory? ✅⚠ **MUCH BETTER — and one gap left**

Batch 3 called this "the weakest point in the entire documented workflow." It is no longer.
Five independent pieces of evidence exist **inside TBC**:

| Evidence | Source |
|---|---|
| Scans sit beneath their trajectory node in Project Explorer | TBC 22638 |
| Updated scan stations carry the `_reg_####` suffix | TBC 22638 |
| **Trajectory properties state `Origin: Registration result`, `Input trajectory: Imported trajectory`, `Registration type: GlobalThenLocal`** | **TBC 22905, 26473** |
| **A numbered `sbet_<date>_reg_####.out` on disk, one per registration, incrementing** | **TBC 22905, 26473** |
| **Registered segments render in the "Undefined RMS" colour** — because they no longer match the `smrmsg` RMS file | **TBC 27248** |
| **Cleanup Mobile Mapping Mission leaves exactly one registration in the project** | **TBC 26466** |

> ❌ **The gap that remains is exactly one question: does any export carry trajectory
> identity with it?** The Export Mobile Mapping Data topic is the only uncaptured material
> topic and the only place that can answer it.

> **PROPOSED PARAMETRIX PRACTICE — not Trimble behaviour, not adopted.** Unchanged from batch
> 3 in intent, sharpened by what is now known: record the trajectory node, the `_reg_####`
> number, and the SBET filename; run the Mission Report **before** Cleanup; back up before
> Cleanup. **Still requires testing, and still requires the Export topic.**

### Q8 — What reports or records should be retained? ✅ **ANSWERED, with additions**

| Record | Source | Captures |
|---|---|---|
| **Mission Report** | TBC 23991, 24868 | Capture devices, runs, trajectories, generated scans, **and per-sensor boresight/lever-arm calibration with date** |
| **Results of Scan Generation** | TBC 22499 | Per run: filters, range, colorization |
| **Run-to-run Results tab** | TBC 25096 | Per-pair RMS every 20 m, three axes |
| **Calibration results** | TBC 24886 | Computed angles, Overall Overlap, Overall RMS, per-pair RMS |
| **Trajectory QC Report + Trajectory Plots** | TBC 25943, 27415 | Plots from the SBET computation, re-openable without recomputing |
| **`smrmsg_xxx.out`** | TBC 27248 | Position, orientation and velocity RMS after smoothing |
| **Calibration JSON** | TBC 22920 | Installation and Refinement matrices, per sensor |
| **`Targets.csv`** | TBC 22905 | The picked registration observations themselves |

> **FLAGGED, not adopted.** The natural retention package is now visible and it is larger
> than batch 3 assumed. **`Targets.csv` in particular is the registration's field book** —
> it is the only artefact holding the observations, and TBC will empty it on a wrong answer
> to a dialog. That is a candidate P1 decision.

---

## 6. Defaults and ambiguities flagged for testing

Continuing the batch 3 numbering. **None of these is a recommendation.**

| # | Item | Why it needs testing rather than adopting |
|---|---|---|
| **T9** | **Activate Target-Bundle Adjustment** | Checking it makes the adjustment **coarser** (250 m vs 70 m). The name implies the opposite. Trimble ties the choice to GCP density *and* GCP accuracy *and* picking precision — three conditions that will rarely all point the same way |
| **T10** | `sbet_[mission]_[frame].out` naming | The second filename silently means POSPac did not know the project datum and an extra transformation occurred. Nothing warns the processor |
| **T11** | **Multipath = Medium** default | Medium is Trimble's default but is described as being *for degraded coverage*. Using it on open-sky corridors is a defensible default or an unnecessary de-weighting — untested |
| **T12** | **DMI scale factor SD = 5 %** | Only correct if the wheel diameter was actually measured. If the value came from the manual, 5 % is an assertion of accuracy nobody verified |
| **T13** | **LiDAR QC range 3–100 m** | The MX60's useful range and the LiDAR QC window are different questions. 100 m may include geometry too noisy to aid the solution |
| **T14** | **Lasers = All** in LiDAR QC | Trimble itself says both lasers "can increase computation time without significantly improving the accuracy" — the default contradicts the guidance beside it |
| **T15** | **Registration type** — which of Global / Local / Global-then-Local | Trimble describes each mechanism but gives **no selection rule** beyond "consistent differences." Global-then-Local gets no guidance at all, and it is the one shown in every screenshot |
| **T16** | **Cutting plane thickness** | 5.000 in one screenshot, 0.030 in another, with no stated basis. Thickness determines what the visual check can actually see |
| **T7** *(carried)* | Registration auto-saving default state | Mechanism now documented; **default still unstated.** Given `Targets.csv` is the observation record, the default matters |

---

## 7. The chain model, tested again

Batch 3 corrected the model five times. Batch 4 requires **three further corrections and one
addition**:

```
Raw MX60 data (.mxdb + POS raw + base RINEX)
   │
   ├─[A]─ Trajectory production — one of:
   │        · POSPac MMS externally  →  SBET
   │        · TBC "Process Raw Trajectory Data"  →  SBET   (needs POSPac 8.6+ licensed)
   │        · real-time NAV, if no post-processing possible
   │        (optionally: LiDAR QC refinement during this step)
   │
   ├─ Import .mxdb into TBC, apply SBET or NAV
   │
   ├─ Generate Mobile Mapping Scans          TMX → RWCX, one step on MX50/MX60
   │
   ├─[B]─ Adjustment — one or more of:
   │        · Register a Run / Register a Mission   (GCP ↔ picked target)
   │        · Register Run to Run                   (cloud ↔ cloud, batched)
   │        · Generate POSPac Position Fixes        (→ second POSPac pass → new SBET)
   │        · Edit a Run / Edit a Mission           (re-registers the SAME imported
   │                                                 trajectory, no increment)
   │
   ├─ Update Scans                            unless Run-to-Run did it inline
   │
   ├─[C]─ QC — residuals · per-20 m RMS · validation points · Cutting Plane View
   │              · Mission Report · Trajectory Plots
   │
   ├─[D]─ Cleanup Mobile Mapping Mission      DESTRUCTIVE, NOT UNDOABLE
   │                                          back up first; report first
   │
   └─ Extraction / delivery                   ← Export topic still uncaptured
```

**Correction 6.** Trajectory production is **not necessarily external to TBC.** The model
assumed POSPac. TBC can do it, licence permitting.

**Correction 7.** "Adjustment" is **not one step.** It is three distinct mechanisms with
different inputs, and one of them (PFIX) loops back to step [A] rather than forward.

**Correction 8.** **Edit a Run / Edit a Mission are not repeats of registration.** They
re-register the *same imported trajectory* with modified pairs — "not by incrementing each
time the adjusted trajectory but by editing the same (imported) trajectory." ✅ The output is
`RunName_Trajectory2`, and **Reset restores the original pairs**, which registration itself
cannot do. Getting this wrong means stacking adjustments on adjustments.

**Addition.** **[D] Cleanup is a step, and it is the last safe moment for anything.** It was
not in the model at all.

---

## 8. New open questions

| # | Question | Blocks |
|---|---|---|
| 1 | Does **Export** carry trajectory identity? | Q7, the last piece |
| 2 | Does Parametrix hold a **POSPac MMS 8.6+ licence**? Without it, Process Raw Trajectory Data and PFIX are both unavailable | Which workflow is even possible |
| 3 | What is the **default state of Registration Auto-Saving**, and can it be enforced? | T7, and the `Targets.csv` retention decision |
| 4 | Do **imagery and station positions** inherit a registration? | Q5 |
| 5 | Is **Register a Mission** the intended normal workflow, with Register a Run the exception? | Structure of the office chapter |
| 6 | Does the **Mission Report** name which trajectory each scan set used, or only list trajectories? | Q7, Q8 |
| 7 | Which **TBC version** is installed? Behaviour differs at 5.21 (calibration) and 5.80 (RMS file) | Several procedures |
| 8 | Can **one site** serve both the laser calibration (4 runs, 2 orthogonal) and LiDAR QC (2 perpendicular strips, 250–300 m, both directions)? | SOP §5.7 |

Questions 2 and 7 are **vendor questions** and have been added to `VENDOR-QUESTIONS.md`.

---

## 9. Figure recommendations

Crop these from `../sources/tbc-help-captures-batch4/`. **Crops, not whole pages.**

| # | Figure | Source | Where it goes |
|---|---|---|---|
| F17 | Control Points grid showing **Use XY / Use Z / As Check / Target** columns with a picked pair | 22905 | Registration — control vs check |
| F18 | Targets pane with **Easting / Northing / Elevation residual** populated (0.062 / 0.106 / 0.018 m) | 22905 | Registration — reading residuals |
| F19 | **Validate Picking** window, checkerboard, showing overhead + perpendicular side view + RMS of plane | 22905 | Target picking |
| F20 | Project Explorer: `Unnamed Run 0 › Sbet` / `Reg. Trajectory` | 22905 | Where the adjusted trajectory lives |
| F21 | **Trajectory properties**: Trajectory file, `Origin: Registration result`, Input trajectory, Registration type | 22905 or 26473 | **Proving which trajectory was used** |
| F22 | Project folder listing `sbet_…_reg_0001…0004.out` | 22905 | Same |
| F23 | Mission control list showing **one GCP, five instances, one per run** | 26473 | Register a Mission — GCP instances |
| F24 | Project Explorer: `Run 10 › Sbet / RegTrajectory`, `Run 11 › Sbet / RegTrajectory` | 26473 | Mission registration output |
| F25 | **Tangential / Orthogonal / Vertical** axis diagram on a curved trajectory | 25096 | What the three RMS numbers mean |
| F26 | **Results tab** — Run Pairs + RMS Statistics grid with `No overlap` rows | 25096 | Reading the registration result |
| F27 | **Cutting Plane View** profile of a building across two runs | 25096 | The mandatory visual check |
| F28 | Plan View: Run to Adjust green, Reference Run red | 25096 | Run-to-run geometry |
| F29 | Raw data folder tree — `POS_1/raw`, `Base`, `Camera_1..4`, `Laser_1/2`, `Extcal.json`, `.mxdb` | 25943 | What is actually on the drive |
| F30 | **Mission Report "Capture devices" table** with Boresight calibration and **Date of calibration** | 24868 | Calibration record / QC package |
| F31 | Camera properties showing **Boresight installation vs Boresight refinement** | 24868 | What a calibration changes |

---

## 10. What this does **not** change

Stated explicitly, because the batch is large and the temptation is to start rewriting.

- **No Parametrix tolerance has been created.** Trimble states none for registration.
- **No Parametrix procedure has been created.** Everything in §2–§4 is Trimble behaviour.
- **SOP §12.3 (calibration) stands** — 24886 confirms it.
- **SOP §13 (QC) gains evidence but no numbers.** The indicators are now known; the
  thresholds are still a Parametrix decision.
- **The decision register is unchanged at 35 items.** Batch 4 generates candidates
  (LiDAR QC provisioning, `Targets.csv` retention, Cleanup sequencing, run-vs-mission
  registration as the default) but they are **candidates**, and they are added at the
  rewrite, not now.

---

*Ingestion continues. Export Mobile Mapping Data is the one remaining material gap. No
rewrite has been performed.*
