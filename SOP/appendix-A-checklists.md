# Appendix A — Working Checklists

Thirteen standalone checklists, written to be used at the bench or in the vehicle rather than read
as summaries. Each names its section for the detail.

> **Items marked ⚠ depend on an open Parametrix decision** (Appendix I). Perform them using
> project-specific direction until the decision is made.

---

## A1 · Project Planning

*§5, §6*

| ☐ | Item |
|---|---|
| ☐ | Client accuracy requirement stated **in writing, per component** |
| ☐ | Deliverable formats agreed ⚠ *D-38* |
| ☐ | **Grid or ground** agreed, and what accompanies it ⚠ *D-40* |
| ☐ | Project CRS, vertical datum and geoid fixed |
| ☐ | **Epoch** confirmed where a time-dependent datum is in use ⚠ *D-21* |
| ☐ | Corridor extent defined, including extent beyond the deliverable needed to bracket control |
| ☐ | Pass pattern and directions decided ⚠ *D-41* |
| ☐ | **Overlap planned** where a degraded-GNSS remedy may be needed — §20.3 |
| ☐ | Control network designed, **bracketing both ends** of the delivered extent — §5.6 |
| ☐ | Control points chosen for **findability in a point cloud**, not just occupiability — §5.5 |
| ☐ | **Independent check points designated in writing by the Project Surveyor** — §17.4 ⚠ *D-15* |
| ☐ | Check points distributed across GNSS environments, including near each end |
| ☐ | Base station strategy fixed ⚠ *D-42* |
| ☐ | GNSS almanac checked for the planned window |
| ☐ | **GNSS-hostile stretches mapped, with outage duration estimated** — not length |
| ☐ | Mitigation chosen for each hostile stretch — control, overlap, or another method |
| ☐ | **Segments unsuitable for mobile mapping identified and communicated** — §6.8 |
| ☐ | Initialization locations identified — primary and backup, scouted on imagery |
| ☐ | Collection window agreed against GNSS, imagery and traffic |
| ☐ | Weather go/no-go understood by the operator ⚠ *D-44* |
| ☐ | **Calibration currency confirmed** — §14.7 ⚠ *D-26* |
| ☐ | Road occupancy, permits, access and notifications arranged |

---

## A2 · Field Preflight

*§7 · every mission*

| ☐ | Item |
|---|---|
| ☐ | Sensor Unit mounted and secured — **two people**, 24–28 kg |
| ☐ | Unit seated as it was when lever arms were measured |
| ☐ | All cables connected, routed, secured, and not able to be shut in a door |
| ☐ | Power supply live — **30 A or more**; 35 A fuse close to the battery |
| ☐ | Battery healthy; **no Battery Protect warning** (audible below 10.5 V) |
| ☐ | Control Unit powered up — hold **≥ 15 s**; LEDs through the startup sequence |
| ☐ | TMI reachable in **Chrome** at `http://tmi.mx-scan.net` |
| ☐ | **All sensors reporting present** — two lasers, 360° camera, back-down camera |
| ☐ | **Vehicle Preset / lever arms correct for this vehicle and this installation** ⚠ *D-46* |
| ☐ | **Z sign checked** — positive is **downward** |
| ☐ | DMI mounting side recorded, if fitted — determines the scale factor sign |
| ☐ | Capture settings configured **and written down** |
| ☐ | Dust filter set appropriately — unpaved or mine sites only |
| ☐ | Data disk installed, correct disk, **sufficient free space with margin** ⚠ *D-47* |
| ☐ | Scanner windows and camera dome clean |
| ☐ | Initialization location confirmed available |
| ☐ | Weather within the go/no-go rule |
| ☐ | **Field record started** |

---

## A3 · End-of-Mission Field QC

*§8.7, §9 · before the vehicle leaves*

**Closing sequence**

| ☐ | Item |
|---|---|
| ☐ | Last run finished |
| ☐ | Driven to an **open-sky** location |
| ☐ | **Dynamic manoeuvres performed** — the mirror of initialization |
| ☐ | **Stationary 2–3 minutes**, logging static data |
| ☐ | Mission closed in TMI |
| ☐ | **Power button light out** — up to 90 s — before power or disk is disturbed |

**Verification**

| ☐ | Item |
|---|---|
| ☐ | Mission folder present on the disk, plausible size |
| ☐ | **Run count matches what was driven** |
| ☐ | **`POS_1/raw` present and non-empty** — without it there is no post-processed trajectory |
| ☐ | Base station data captured, if a local base was used |
| ☐ | **Every planned pass driven, in the planned direction** |
| ☐ | **Planned overlap actually collected** — §9.3 |
| ☐ | Sections not collected recorded, with the reason |
| ☐ | Field record complete — conditions, incidents, occlusions, comments |
| ☐ | **Any re-drive decided and performed now** ⚠ *D-51* |

> **The overlap check is the one worth being pedantic about.** Missed overlap removes two of the
> three office remedies for degraded GNSS, with no software warning.

---

## A4 · Office Intake

*§10, §11*

| ☐ | Item |
|---|---|
| ☐ | **Copy, do not move** — source disk remains the source |
| ☐ | Copy verified — file count, total size, checksum where tooling allows |
| ☐ | **Verified copy exists in two locations** |
| ☐ | **`.mxdb` confirmed to open** — import into a scratch project. The only definitive test |
| ☐ | `POS_1/raw` present and non-empty |
| ☐ | Base station data present if a local base was used |
| ☐ | **Raw-data backup taken before any processing begins** |
| ☐ | Field record filed with the data |
| ☐ | **Only then** may the source disk be cleared |
| ☐ | Project CRS set **before import** — §11.2 |
| ☐ | **Covered distance checked against the field record** — §11.4 |
| ☐ | Run count matches the field record |
| ☐ | Active trajectory is the intended one, and is **SBET not NAV** unless recorded otherwise |
| ☐ | Capture Devices lists the expected sensors |

---

## A5 · Trajectory Processing

*§12*

| ☐ | Item |
|---|---|
| ☐ | **Base station `.YYo` imported into TBC first** |
| ☐ | **`.YYn` and `.YYg` ephemeris NOT imported** |
| ☐ | Raw POS files located — `POS_1/raw`, processed from the first selected |
| ☐ | **Antenna model reads `Trimble 112735`** — verify before computing |
| ☐ | Computation mode set ⚠ *D-19* |
| ☐ | Initialization mode reviewed — default Gyro-compassing |
| ☐ | Multipath reviewed — default Medium ⚠ *T11* |
| ☐ | GAMS settings reviewed, if fitted |
| ☐ | DMI lever arm, **scale factor and sign**, and SD reviewed, if fitted ⚠ *T12* |
| ☐ | Vehicle-frame convention confirmed — **+X forward, +Y right, +Z down** |
| ☐ | **Backup SBET Next to MXDB enabled** ⚠ *D-20* |
| ☐ | LiDAR QC considered where GNSS was degraded and overlap exists — §12.7 |
| ☐ | Generate QC Report enabled |
| ☐ | **SBET filename read** — `sbet_<mission>.out` or `sbet_<mission>_<frame>.out` |
| ☐ | If `_<frame>`: CRS and epoch setup reviewed. **The filename is an indicator, not a verdict** |
| ☐ | **Trajectory switched to RMS colouring and inspected in plan** |
| ☐ | **Degraded stretches listed** — this list drives QC layers 5, 6 and 7 |
| ☐ | Trajectory Plots reviewed |

---

## A6 · Generate Scans

*§13*

| ☐ | Item |
|---|---|
| ☐ | Correct trajectory active on the mission |
| ☐ | Filter settings chosen deliberately, not accepted ⚠ *T1–T5* |
| ☐ | **Reflective Panels considered** if signs or line marking are in the deliverable ⚠ *T3* |
| ☐ | Range max considered against useful range in the day's conditions ⚠ *T4* |
| ☐ | Colorization decision made ⚠ *D-22* |
| ☐ | **One representative run generated and inspected before committing the mission** |
| ☐ | Expected features still present — signs, line marking, a wall at range |
| ☐ | Mission generated |
| ☐ | **Results of Scan Generation captured into the project record** ⚠ *D-23* |
| ☐ | Scans visible beneath the expected trajectory node |

---

## A7 · Calibration

*§14 · periodic, not per project*

| ☐ | Item |
|---|---|
| ☐ | Calibration currency checked — is one actually due? ⚠ *D-26* |
| ☐ | Calibration site available ⚠ *D-24* |
| ☐ | **Four runs collected** — two roads crossing, each driven both ways |
| ☐ | Crossing angle **90° ± 30°** |
| ☐ | Run length **≥ 20 m each side; ideally 80 m total** |
| ☐ | **Façades present in each direction**; little or no vegetation |
| ☐ | Project created, CRS set, `.mxdb` imported with SBET applied |
| ☐ | **Scans generated** — the calibration consumes them |
| ☐ | Calibrate Laser Scanners run |
| ☐ | Overall Overlap, Overall RMS and per-pair three-axis RMS reviewed |
| ☐ | **Visual check performed in Cutting Plane View, rendering set to Scan Color** |
| ☐ | **BOTH run pairs checked** — `Run_0 ↔ Run_1` **and** `Run_2 ↔ Run_3` |
| ☐ | Applied only after both visual checks |
| ☐ | Camera calibration performed if required — §14.4 |
| ☐ | **Calibration JSON exported and archived** with serial number and date ⚠ *D-25* |
| ☐ | Mission Report run — it carries the **date of calibration** per sensor |

> **Good RMS does not prove the calibration succeeded. Bad RMS proves it failed. Look at the
> data.**

---

## A8 · Registration

*§15, §16, §17*

**Before**

| ☐ | Item |
|---|---|
| ☐ | Scans generated on every run to be registered |
| ☐ | GCP file imported in the project CRS |
| ☐ | **Control / check designation received in writing from the Project Surveyor** ⚠ *D-15* |
| ☐ | **Registration Auto-Saving state confirmed** ⚠ *T7* |
| ☐ | Command chosen deliberately — Run, Mission, or Run-to-Run. **They are not interchangeable** |

**During**

| ☐ | Item |
|---|---|
| ☐ | Registration Name set — **this is what you will identify months later** |
| ☐ | Registration Type chosen ⚠ *T15* |
| ☐ | If **Local**: control **brackets** the delivered extent — it does not extrapolate |
| ☐ | Target-Bundle Adjustment state chosen knowingly — **checked = coarser (250 m)** ⚠ *T9* |
| ☐ | **Use XY / Use Z / As Check set per the written designation** |
| ☐ | Each target picked with the residual read **before** validating |
| ☐ | Pick warnings resolved — not a 3D point; not the most recent scan |
| ☐ | No pair exceeding **30 m** separation |
| ☐ | Redundancy sufficient that removing any one pair would not change the answer much |
| ☐ | Computed; adjusted trajectory (blue) compared against original (green) |
| ☐ | **To improve: use Edit, not Register again** — avoids stacking adjustments |
| ☐ | Applied |

**After**

| ☐ | Item |
|---|---|
| ☐ | Adjusted trajectory node present, with `Origin: Registration result` |
| ☐ | Numbered `sbet_<date>_reg_####.out` present in the project folder |
| ☐ | **Residuals on control and on independent checks recorded outside TBC** ⚠ *D-17* |
| ☐ | **Update Scans run** — §13.6 |
| ☐ | Scan stations carry the **`_reg_####`** suffix |
| ☐ | `Targets.csv` archived |

---

## A9 · Point Cloud QC

*§18*

| ☐ | Item |
|---|---|
| ☐ | Residuals on control reviewed, by component |
| ☐ | **Residuals on independent check points reviewed** — the only numerical evidence of accuracy |
| ☐ | Run-to-run three-axis RMS reviewed where used; **`No overlap` rows read** |
| ☐ | One axis much larger than the other two investigated — it names the problem |
| ☐ | **Rendering set to Scan Color before looking for misalignment** |
| ☐ | Point size increased; cutting plane thickness set ⚠ *T16* |
| ☐ | **Cutting plane dragged the full length of every overlap** — not sampled |
| ☐ | Flat surfaces checked at range for thickening |
| ☐ | **Ends of the corridor checked** — where Local stops and the smoother was weakest |
| ☐ | Degraded stretches from A5 revisited — did the registration fix them? |
| ☐ | Features near control compared with features far from control |
| ☐ | **Visual QC recorded — who, when, what extent.** No software artefact exists |

> **Two surfaces 4 cm apart look exactly like one surface 4 cm thick in a single colour.**

---

## A10 · Imagery QC

*§19*

| ☐ | Item |
|---|---|
| ☐ | Coverage continuous for the full corridor |
| ☐ | Exposure holds through shaded stretches and underpasses |
| ☐ | No motion blur at the speed collected |
| ☐ | No obstruction — aerials, following vehicles, dome contamination |
| ☐ | **Systematic sample opened and looked at**, not counted |
| ☐ | **Black images screened** — corrupted side camera images export as black, silently ⚠ *D-31* |
| ☐ | Colour fringing at feature edges checked on colorized clouds — indicates camera boresight |
| ☐ | Exposure consistency between passes |
| ☐ | Blur applied where required ⚠ *D-32* |
| ☐ | Resolution matches the configuration commitment — §19.2 ⚠ *D-2* |

---

## A11 · Export

*§22*

| ☐ | Item |
|---|---|
| ☐ | **Scan nodes selected sit beneath the intended registered trajectory** |
| ☐ | **Stations carry the `_reg_####` suffix** |
| ☐ | Trajectory properties read `Origin: Registration result`, with expected input and type |
| ☐ | Correct export tab chosen — **Mobile Mapping (run-aware)** or **Point Cloud (region-based)** |
| ☐ | Export path chosen ⚠ *D-38* |
| ☐ | **Export timestamps setting decided and recorded** ⚠ *D-37 · T18 · V-1* |
| ☐ | Scaling decided — **grid writes a `.txt` sidecar; ground does not expose its scale factor** |
| ☐ | ECEF considered where the global CRS must travel |
| ☐ | Path-specific prerequisites met — scans generated; run views closed for TopoDot |
| ☐ | Blur applied where required |
| ☐ | **Delivery record written** — mission, trajectory node, SBET filename and `_reg_` number, registration type, export path, date, by whom ⚠ *D-29* |

> **Registration does not modify the point cloud until Update Scans is performed.** An export can
> succeed, open correctly, and contain pre-registration data.

---

## A12 · Final QA/QC

*§24 · the ten layers*

| ☐ | Layer |
|---|---|
| ☐ | **1 Mission completeness** — covered distance, run count, coverage in plan vs the field record |
| ☐ | **2 Trajectory quality** — RMS colouring reviewed; **suspect stretches listed, not averaged** |
| ☐ | **3 Coordinate system** — CRS, vertical datum, geoid, epoch; SBET filename read as an indicator |
| ☐ | **4 Control usage** — Use XY / Use Z / As Check confirmed against the written designation; checks did not drive the adjustment |
| ☐ | **5 Registration results** — residuals on control and checks; run-to-run RMS; registration type suited the error; Local bracketed the extent |
| ☐ | **6 Visual QC** — Scan Color, cutting plane, overlaps, range, corridor ends |
| ☐ | **7 Corridor continuity** — traversed, not sampled ⚠ *D-39* |
| ☐ | **8 Imagery QC** — A10 |
| ☐ | **9 Export state** — scans under the registered trajectory; `_reg_` suffix; settings recorded ⚠ *T29* |
| ☐ | **10 Deliverable review** — files exist, extents present, CRS and units correct, each file opens in other software, point count and size plausible, imagery present and sampled, sidecars present, no corrupt output, project requirements met |
| ☐ | **Acceptance against the project accuracy requirement** ⚠ *D-13* |
| ☐ | **QA/QC record written** — who performed each layer, and when |

> **Bad RMS can demonstrate failure. Good RMS does not by itself demonstrate success.**

---

## A13 · Archive and Cleanup

*§21, §25*

**Archive first — in this order**

| ☐ | Item |
|---|---|
| ☐ | QC complete and **accepted** |
| ☐ | **Mission Report run and archived** — it can only report what still exists |
| ☐ | Control / check designation and residuals recorded |
| ☐ | `Targets.csv` archived |
| ☐ | **Numbered `sbet_*_reg_####.out` files archived** ⚠ *T28 — assume Cleanup removes them* |
| ☐ | Calibration JSON archived |
| ☐ | Results of Scan Generation archived |
| ☐ | Delivery record and QA/QC record filed |
| ☐ | **Project backup taken to a location that is part of the project archive** — not a local copy |

**Cleanup**

| ☐ | Item |
|---|---|
| ☐ | **Authorisation obtained** ⚠ *D-6 · D-35* |
| ☐ | Cleanup Mobile Mapping Mission run |
| ☐ | **Recorded** — by whom, on what date, and what was archived first |

**Close out**

| ☐ | Item |
|---|---|
| ☐ | Retention tier applied ⚠ *D-55* |
| ☐ | Raw mission data disposition recorded |
| ☐ | Archive record page completed — what, where, when, by whom |

> **Cleanup is destructive and cannot be undone.** Trimble recommends a project backup and nothing
> else; no vendor-prescribed preservation step exists.
