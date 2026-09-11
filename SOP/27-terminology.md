# 27. Terminology

Terms as used in this document and in Trimble's software. Where TBC uses a word differently from
ordinary survey usage, that is noted.

## 27.1 The trajectory and navigation

| Term | Meaning |
|---|---|
| **Trajectory** | The computed position and attitude of the sensor head over time. Everything the system collects is referenced to it (§2.1) |
| **SBET** | **Smoothed Best Estimate of Trajectory** — the post-processed trajectory, computed forward and backward through time and merged. The normal input for survey work |
| **NAV** | The real-time trajectory computed in the vehicle. A fallback, not an option (§11.2) |
| **POSPac MMS** | Applanix software that computes the SBET. **A licence is required** for both the external route and TBC's in-application command (§4.4) |
| **IN-Fusion+ Single Base** | POSPac computation mode using corrections from a local base station |
| **IN-Fusion+ PP-RTX** | POSPac computation mode using Trimble RTX corrections, with no local base |
| **GNSS/INS integration** | Combining satellite positioning with inertial sensing so each covers the other's failure mode (§2.2) |
| **IMU** | Inertial Measurement Unit. Precise instant to instant, **drifts without limit** over time |
| **GAMS** | GNSS Azimuth Measurement System — a second antenna giving a direct heading measurement. Speeds initialization *(TBC 25943)* |
| **DMI** | Distance Measuring Indicator — a wheel sensor giving independent along-track distance. Scale factor sign depends on the mounting side *(TBC 25943)* |
| **Initialization** | The static period, straight run and dynamic manoeuvres that let the filter resolve attitude and sensor bias (§8.2) |
| **`smrmsg_xxx.out`** | POSPac file describing position, orientation and velocity RMS after smoothing. **The source of the trajectory's RMS colouring** *(TBC 27248)* |
| **ITRF00 path** | Where POSPac does not recognise the project datum and epoch, the SBET is computed in ITRF00 and then transformed — indicated by the filename `sbet_[mission]_[frame].out` *(TBC 25943; §5.3)* |

## 27.2 Missions, runs and data objects

| Term | Meaning |
|---|---|
| **Mission** | One deployment. The `.mxdb` and everything beneath it |
| **Run** | One continuous stretch of collection within a mission. A mission has many |
| **Station** | One instant of imagery capture along a run |
| **`.mxdb`** | The mission database written in the field. **The file you import** |
| **TMX** | Polar scan data — ranges and angles, sensor-relative. Not georeferenced |
| **RWCX** | The point cloud — XYZ, intensity, colour, normals. Produced by applying the trajectory to TMX |
| **MTA** | Multiple Times Around — range-ambiguity correction. **Not part of the MX60 workflow** *(TBC 22503; §13.1)* |
| **`Extcal.json`** | The calibration file written with the raw mission data |
| **Capture Devices** | The TBC node listing the sensors: for the MX60, **Camera 3 Back Down**, **Camera 4 360°**, and the two lasers |

## 27.3 Processing commands

| Term | Meaning |
|---|---|
| **Process Raw Trajectory Data** | Computes an SBET inside TBC. **Requires POSPac 8.6+ and a licence** *(TBC 25943)* |
| **Generate Scans** | Applies the trajectory to raw scanner data, producing the point cloud (§13) |
| **Update Scans** | **Recomputes scans against a different trajectory.** How a registration reaches the point cloud. No Filters pane *(TBC 22638; §13.6)* |
| **Recover Mobile Mapping Scans** | Recovery for failed or interrupted scan generation *(TBC 28155)* |
| **LiDAR QC** | Uses scan data as an aiding sensor, SLAM-like, to refine the trajectory. Runs inside trajectory processing *(TBC 28972; §12.7)* |
| **PFIX** · **Generate POSPac Position Fixes** | Projects GCP-to-target offsets back into the navigation solution for a **second POSPac pass** *(TBC 24460; §20.5)* |
| **Cleanup Mobile Mapping Mission** | Keeps the most recent registration and removes the rest. **Destructive and not undoable** *(TBC 26466; §21)* |

## 27.4 Calibration

| Term | Meaning |
|---|---|
| **Boresight** | The fixed **angular** offset between a sensor and the inertial reference frame. **This is what a calibration estimates** |
| **Lever arm** | The fixed **distance** offset between two sensors. **Known from manufacture and measurement — not estimated** *(TBC 24886; §14.2)* |
| **Installation Matrix** | Parameters **before** calibration — the as-built values *(TBC 22920)* |
| **Refinement Matrix** | Parameters **after** calibration *(TBC 22920)* |
| **Boresight installation / Boresight refinement** | The same distinction as it appears in TBC's sensor properties *(TBC 24868)* |
| **Vehicle frame** | **+X forward, +Y right, +Z downward.** Governs lever arms and boresight angles *(TBC 25943; §7.3)* |

## 27.5 Registration

| Term | Meaning |
|---|---|
| **Registration** | Adjusting a **trajectory** to fit surveyed control, or to fit another run. **It does not move points** (§15.1) |
| **Register a Run** | GCPs matched to picked targets, one run *(TBC 22905)* |
| **Register a Mission** | The same, across a set of runs, with each GCP reusable *(TBC 26473)* |
| **Register Run to Run** | **Cloud-to-cloud** against a fixed Reference Run. **Uses no surveyed control** *(TBC 25096; §16)* |
| **Reference Run** | In run-to-run, the run whose trajectory does not change |
| **Run to Adjust** | The run optimised to the Reference Run |
| **GCP** | Ground control point — "an accurately surveyed coordinate location for a physical feature that can be identified on the ground" *(TBC 22905)* |
| **Target** | **In TBC's registration sense: a point picked in the point cloud.** Not a physical panel (§15.2) |
| **Validation point (VP)** | A GCP set **As Check** — paired and measured, but **excluded from the adjustment** *(TBC 22905; §17.2)* |
| **Use XY · Use Z · As Check** | The three independent per-point choices in the Control Points list (§17.2) |
| **Global** | A shift of the whole trajectory, without rotation *(TBC 22905)* |
| **Local** | Local adjustment interpolating **between** control points. **Does not extrapolate beyond them** *(TBC 22905; §15.5)* |
| **Global, and then Local** | Global first, then Local. No separate selection guidance published |
| **Target-Bundle Adjustment** | Checked = **250 m** intervals (coarser); unchecked = **70 m** *(TBC 22905; §15.7)* |
| **Point Cloud Smart Picking** | The picking tool. Types: Default, Intersected Plane, Road Mark *(TBC 22905)* |
| **`Targets.csv`** | Where picked targets are saved when Registration Auto-Saving is on. **Emptied permanently by answering "No" to the reload prompt** *(TBC 22905)* |
| **`sbet_<date>_reg_####.out`** | The registered SBET on disk, incrementing per registration *(TBC 22905)* |
| **`_reg_####` suffix** | Carried by scan stations updated against a registered trajectory *(TBC 22638)* |
| **Reg. Trajectory · RegTrajectory** | The adjusted trajectory node, from Register a Run and Register a Mission respectively |

## 27.6 Quality

| Term | Meaning |
|---|---|
| **Tangential / Orthogonal / Vertical** | TBC's three-axis agreement convention: along travel, across travel, and up. Diagnostic, not just descriptive (§18.3) |
| **Overall Overlap** | Percentage of points used against those generated, in calibration *(TBC 24886)* |
| **The RMS asymmetry** | **Good RMS does not prove success; bad RMS proves failure; a visual check is necessary** *(TBC 24886, 25096)* |
| **Cutting Plane View** | Profile view across a plane, used to check agreement between overlapping data. **Set rendering to Scan Color** or two offset surfaces read as one thick one (§18.5) |
| **Scan Color** | Rendering mode giving one colour per scan. **Part of the QC method, not a display preference** |
| **`No overlap`** | In run-to-run Results, a timestamp where the two runs do not overlap. Informative, not noise (§16.6) |
| **Undefined RMS colour** | How registered trajectory segments render, having lost their match to the `smrmsg` file *(TBC 27248)* |
| **Mission Report** | Capture devices, runs, trajectories, generated scans, and **per-sensor calibration with date** *(TBC 23991_1, 24868)* |

## 27.7 Export and delivery

| Term | Meaning |
|---|---|
| **Mobile Mapping tab** | Export pane tab holding the **run-aware** exporters |
| **Point Cloud tab** | Export pane tab holding the generic exporters. **Selects by region or drawn rectangle — not by run** *(TBC 11769; §22.4)* |
| **Export to LAS (Trajectory Split)** | The classified-regions exporter. Splits by distance; **carries no trajectory** *(TBC 27279)* |
| **Scaling: Grid** | Projected coordinates with the combined scale factor. **Writes a `.txt` sidecar naming the CRS and scale factor** *(TBC 11769)* |
| **Scaling: Ground** | Ground coordinates. **Does not expose the scale factor used** *(TBC 11769)* |
| **ECEF export** | Ground-scaled LAS/LAZ including the project's global CRS *(TBC 11769)* |
| **Export timestamps** | **Not merely an attribute toggle.** Set to Yes, "the exported scans are reprocessed from the raw data" *(TBC 23339, 22501; §22.3)* |
| **Publish to TRCPS** | Upload to Trimble Connect. **Point cloud and trajectories are exported by default** *(TBC 29527)* |
| **TRCPS** | Trimble Reality Capture Platform Service — an extension of Trimble Connect |
| **TDU** | Trimble Desktop Utility, installed with TBC, which performs the upload |

## 27.8 Evidence tags used in this document

| Tag | Meaning |
|---|---|
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble states this, in the cited topic or page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software; not stated by Trimble as procedure |
| **PARAMETRIX PROCEDURE (PROPOSED)** | Recommended by this document. **Not company policy** |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Decided by Parametrix, with a date and owner in Appendix H |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make |
| **FIELD TESTING REQUIRED** | Answerable by testing, not reading |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble |
| **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** | Carried from the v1 draft; not yet re-sourced |
| **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED** | A screening method proposed here and not yet validated |
