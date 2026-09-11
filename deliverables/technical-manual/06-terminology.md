# 6. Terminology

**This section is the authoritative glossary for all four Parametrix MX60 deliverables.** The
SOP, the Field How To and the Office How To carry at most a short list of essential abbreviations
and point here. Where a term appears to be defined twice, this section governs.

Terms are grouped by where you meet them rather than alphabetically, because most of the
confusion in this subject is between two terms that sit next to each other in the workflow —
boresight and lever arm, Register a Run and Register a Mission, Global and Local.

## 6.1 Five words that do not mean what they usually mean

Ordinary survey usage and TBC usage diverge on a small number of words. Every one of them has
caused a real mistake, and they are collected here so that the divergence is seen once rather
than discovered five sections apart.

| Word | Ordinary survey usage | What it means here |
|---|---|---|
| **Target** | A physical panel or prism you place and observe | **A point picked in the point cloud** by the operator, which is then paired with a surveyed GCP *(TBC 22905; §21)* |
| **Registration** | Bringing scans into a common frame by moving them | **Adjusting a trajectory.** It does not move points, and does not touch the cloud at all until **Update Scans** runs (§19) |
| **Calibration** | A broad word covering any instrument check | In TBC, specifically **boresight estimation** — the angular offset between sensor and inertial frame. Lever arms are *not* estimated (§20) |
| **Local** | Nearby, or a local coordinate system | An adjustment method that interpolates **between** control points and **does not extrapolate beyond the outermost one** *(TBC 22905; §21)* |
| **Station** | An occupied instrument setup | **One instant of imagery capture** along a run. A mobile mapping system occupies nothing |

> **"Target" is the trap that catches people first.** A checkerboard panel is one kind of feature
> you might pick, but so is the corner of a painted road marking, or a manhole rim. The physical
> thing in the field is the **GCP**. The thing in TBC's Targets pane is a *pick*.

## 6.2 The trajectory and navigation

| Term | Meaning |
|---|---|
| **Trajectory** | The computed position and attitude of the sensor head over time. Everything the system collects is referenced to it (§2.1) |
| **SBET** | **Smoothed Best Estimate of Trajectory** — the post-processed trajectory, computed forward and backward through time and merged. The normal input for survey work |
| **NAV** | The real-time trajectory computed in the vehicle. A fallback, not an option (§17.1) |
| **POSPac MMS** | Applanix software that computes the SBET. **A licence is required** for both the external route and TBC's in-application command (§10.3) |
| **IN-Fusion+ Single Base** | POSPac computation mode using corrections from a local base station |
| **IN-Fusion+ PP-RTX** | POSPac computation mode using Trimble RTX corrections, with no local base |
| **GNSS/INS integration** | Combining satellite positioning with inertial sensing so each covers the other's failure mode (§8) |
| **IMU** | Inertial Measurement Unit. Precise instant to instant, **drifts without limit** over time |
| **GAMS** | GNSS Azimuth Measurement System — a second antenna giving a direct heading measurement. Speeds initialization *(TBC 25943)* |
| **DMI** | Distance Measuring Indicator — a wheel sensor giving independent along-track distance. Scale factor sign depends on the mounting side *(TBC 25943)* |
| **Initialization** | The static period, straight run and dynamic manoeuvres that let the filter resolve attitude and sensor bias (§13) |
| **`smrmsg_xxx.out`** | POSPac file describing position, orientation and velocity RMS after smoothing. **The source of the trajectory's RMS colouring** *(TBC 27248)* |
| **ITRF00 path** | Where POSPac does not recognise the project datum and epoch, the SBET is computed in ITRF00 and then transformed — indicated by the filename `sbet_[mission]_[frame].out` *(TBC 25943; §12.3)* |

## 6.3 Missions, runs and data objects

| Term | Meaning |
|---|---|
| **Mission** | One deployment. The `.mxdb` and everything beneath it |
| **Run** | One continuous stretch of collection within a mission. A mission has many |
| **Station** | One instant of imagery capture along a run |
| **`.mxdb`** | The mission database written in the field. **The file you import** |
| **TMX** | Polar scan data — ranges and angles, sensor-relative. Not georeferenced |
| **RWCX** | The point cloud — XYZ, intensity, colour, normals. Produced by applying the trajectory to TMX |
| **MTA** | Multiple Times Around — range-ambiguity correction. **Not part of the MX60 workflow** *(TBC 22503; §18.1)* |
| **`Extcal.json`** | The calibration file written with the raw mission data |
| **Capture Devices** | The TBC node listing the sensors: for the MX60, **Camera 3 Back Down**, **Camera 4 360°**, and the two lasers |

## 6.4 Processing commands

| Term | Meaning |
|---|---|
| **Process Raw Trajectory Data** | Computes an SBET inside TBC. **Requires POSPac 8.6+ and a licence** *(TBC 25943)* |
| **Generate Scans** | Applies the trajectory to raw scanner data, producing the point cloud (§18) |
| **Update Scans** | **Recomputes scans against a different trajectory.** How a registration reaches the point cloud. No Filters pane *(TBC 22638; §19)* |
| **Recover Mobile Mapping Scans** | Recovery for failed or interrupted scan generation *(TBC 28155)* |
| **LiDAR QC** | Uses scan data as an aiding sensor, SLAM-like, to refine the trajectory. Runs inside trajectory processing *(TBC 28972; §11)* |
| **PFIX** · **Generate POSPac Position Fixes** | Projects GCP-to-target offsets back into the navigation solution for a **second POSPac pass** *(TBC 24460; §27.5)* |
| **Cleanup Mobile Mapping Mission** | Keeps the most recent registration and removes the rest. **Destructive and not undoable** *(TBC 26466; §28)* |

## 6.5 Calibration

| Term | Meaning |
|---|---|
| **Boresight** | The fixed **angular** offset between a sensor and the inertial reference frame. **This is what a calibration estimates** |
| **Lever arm** | The fixed **distance** offset between two sensors. **Known from manufacture and measurement — not estimated** *(TBC 24886; §20.2)* |
| **Installation Matrix** | Parameters **before** calibration — the as-built values *(TBC 22920)* |
| **Refinement Matrix** | Parameters **after** calibration *(TBC 22920)* |
| **Boresight installation / Boresight refinement** | The same distinction as it appears in TBC's sensor properties *(TBC 24868)* |
| **Vehicle frame** | **+X forward, +Y right, +Z downward.** Governs lever arms and boresight angles *(TBC 25943; §7.6)* |

## 6.6 Registration

| Term | Meaning |
|---|---|
| **Registration** | Adjusting a **trajectory** to fit surveyed control, or to fit another run. **It does not move points** (§21.1) |
| **Register a Run** | GCPs matched to picked targets, one run *(TBC 22905)* |
| **Register a Mission** | The same, across a set of runs, with each GCP reusable *(TBC 26473)* |
| **Register Run to Run** | **Cloud-to-cloud** against a fixed Reference Run. **Uses no surveyed control** *(TBC 25096; §21.10)* |
| **Reference Run** | In run-to-run, the run whose trajectory does not change |
| **Run to Adjust** | The run optimised to the Reference Run |
| **GCP** | Ground control point — "an accurately surveyed coordinate location for a physical feature that can be identified on the ground" *(TBC 22905)* |
| **Target** | **In TBC's registration sense: a point picked in the point cloud.** Not a physical panel (§21.2) |
| **Validation point (VP)** | A GCP set **As Check** — paired and measured, but **excluded from the adjustment** *(TBC 22905; §22.2)* |
| **Use XY · Use Z · As Check** | The three independent per-point choices in the Control Points list (§22.2) |
| **Global** | A shift of the whole trajectory, without rotation *(TBC 22905)* |
| **Local** | Local adjustment interpolating **between** control points. **Does not extrapolate beyond them** *(TBC 22905; §21.5)* |
| **Global, and then Local** | Global first, then Local. No separate selection guidance published |
| **Target-Bundle Adjustment** | Checked = **250 m** intervals (coarser); unchecked = **70 m** *(TBC 22905; §21.7)* |
| **Point Cloud Smart Picking** | The picking tool. Types: Default, Intersected Plane, Road Mark *(TBC 22905)* |
| **`Targets.csv`** | Where picked targets are saved when Registration Auto-Saving is on. **Emptied permanently by answering "No" to the reload prompt** *(TBC 22905)* |
| **`sbet_<date>_reg_####.out`** | The registered SBET on disk, incrementing per registration *(TBC 22905)* |
| **`_reg_####` suffix** | Carried by scan stations updated against a registered trajectory *(TBC 22638)* |
| **Reg. Trajectory · RegTrajectory** | The adjusted trajectory node, from Register a Run and Register a Mission respectively |

## 6.7 Quality

| Term | Meaning |
|---|---|
| **Tangential / Orthogonal / Vertical** | TBC's three-axis agreement convention: along travel, across travel, and up. Diagnostic, not just descriptive (§23.3) |
| **Overall Overlap** | Percentage of points used against those generated, in calibration *(TBC 24886)* |
| **The RMS asymmetry** | **Good RMS does not prove success; bad RMS proves failure; a visual check is necessary** *(TBC 24886, 25096)* |
| **Cutting Plane View** | Profile view across a plane, used to check agreement between overlapping data. **Set rendering to Scan Color** or two offset surfaces read as one thick one (§25.1) |
| **Scan Color** | Rendering mode giving one colour per scan. **Part of the QC method, not a display preference** |
| **`No overlap`** | In run-to-run Results, a timestamp where the two runs do not overlap. Informative, not noise (§21.15) |
| **Undefined RMS colour** | How registered trajectory segments render, having lost their match to the `smrmsg` file *(TBC 27248)* |
| **Mission Report** | Capture devices, runs, trajectories, generated scans, and **per-sensor calibration with date** *(TBC 23991_1, 24868)* |

## 6.8 Export and delivery

| Term | Meaning |
|---|---|
| **Mobile Mapping tab** | Export pane tab holding the **run-aware** exporters |
| **Point Cloud tab** | Export pane tab holding the generic exporters. **Selects by region or drawn rectangle — not by run** *(TBC 11769; §29.4)* |
| **Export to LAS (Trajectory Split)** | The classified-regions exporter. Splits by distance; **carries no trajectory** *(TBC 27279)* |
| **Scaling: Grid** | Projected coordinates with the combined scale factor. **Writes a `.txt` sidecar naming the CRS and scale factor** *(TBC 11769)* |
| **Scaling: Ground** | Ground coordinates. **Does not expose the scale factor used** *(TBC 11769)* |
| **ECEF export** | Ground-scaled LAS/LAZ including the project's global CRS *(TBC 11769)* |
| **Export timestamps** | **Not merely an attribute toggle.** Set to Yes, "the exported scans are reprocessed from the raw data" *(TBC 23339, 22501; §29.3)* |
| **Publish to TRCPS** | Upload to Trimble Connect. **Point cloud and trajectories are exported by default** *(TBC 29527)* |
| **TRCPS** | Trimble Reality Capture Platform Service — an extension of Trimble Connect |
| **TDU** | Trimble Desktop Utility, installed with TBC, which performs the upload |

## 6.9 Evidence tags

These tags appear throughout all four deliverables. They are the mechanism that keeps verified
Trimble behaviour separate from proposed Parametrix practice, and they are load-bearing: a
statement's tag is part of its meaning.

| Tag | Meaning |
|---|---|
| **TRIMBLE DOCUMENTED METHOD** | Trimble states this, in the cited topic or page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software; not stated by Trimble as procedure |
| **PARAMETRIX PROCEDURE (PROPOSED)** | Recommended by this document. **Not company policy** |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Decided by Parametrix, with a date and owner in Appendix H |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make |
| **FIELD TESTING REQUIRED** | Answerable by testing, not reading |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble |
| **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** | Carried from the v1 draft; not yet re-sourced |
| **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED** | A screening method proposed here and not yet validated |

> **The tag is a state, not a style.** A clause tagged **PARAMETRIX PROCEDURE (PROPOSED)** is a
> recommendation made by this project. It becomes **(ADOPTED)** only when Parametrix records a
> decision against it, with a date and an owner, in the SOP's adoption record. At the revision on
> the front matter of this manual, **no entry has been adopted.**

## 6.10 Terms deliberately not defined here

| Term | Why not |
|---|---|
| Parametrix document-control vocabulary — *controlled copy*, *document owner*, *effective date*, revision scheme | Parametrix's actual convention has not been established. This project uses temporary descriptive identifiers rather than inventing one (§1.5) |
| Accuracy classes, tolerance bands, pass/fail thresholds | No numerical acceptance criterion is defined in this manual. Trimble publishes no MX60 acceptance tolerance, and inventing one would be worse than leaving it open (§23, master register **D-13**) |
| Ordinary survey terms — *resection*, *least squares*, *geoid*, *combined scale factor* | Assumed knowledge. This manual teaches mobile mapping to surveyors, not surveying (§1.2) |
