# MX60 Office How To

**Trimble Business Center 2026.10 · Trimble MX60**

---

## Document control

> **Provisional.** Parametrix's document-control convention is not established (**D-1**). The
> values below are placeholders.

| Field | Value |
|---|---|
| Document | **MX60 Office How To** |
| Identifier | *`MX60 Office How To — Draft A`* — provisional |
| Revision | *Draft A* |
| Date | 2026-09-11 |
| Status | **Draft. Not issued.** |
| Issued in support of | **MX60 Mobile Mapping SOP**, Draft A |

## What this guide is

**It shows you what to do in Trimble Business Center, in the order you do it.**

| Question | Document |
|---|---|
| Why does it work this way? | Technical Manual |
| Must I? | SOP |
| **How do I do it in the office?** | **This guide** |
| How do I do it in the field? | Field How To |

**This guide cannot create a requirement.** If it tells you to do something the SOP does not
require, one of the two is wrong — and the SOP is the one that governs.

## Abbreviations used here

Everything else is in **Technical Manual §6**, the authoritative glossary for all four documents.

| | |
|---|---|
| **TBC** | Trimble Business Center |
| **SBET** | The post-processed trajectory. The normal input for survey work |
| **NAV** | The real-time trajectory computed in the vehicle. A fallback |
| **GCP** | Ground control point — the surveyed coordinate |
| **Target** | In TBC's registration commands, **a point picked in the point cloud**. Not a physical panel |
| **RMS** | Root mean square — here, a residual statistic |

## Visual identity

Parametrix Brand Guide v6, November 2023, through the shared style system in
`deliverables/_control/style/`. Document accent: **Optimistic Yellow**.

---

# 1. How to Use This Guide

## 1.1 The four questions

Every section answers the same four questions, in the same order. If you read nothing else in a
section, read **Stop if**.

| | |
|---|---|
| **Do** | The clicks, in order |
| **Look at** | What to inspect once you have done it — not "check it worked", but where to point your eyes |
| **Expect** | What normal looks like, so you can tell when it isn't |
| **Stop if** | What means you do not proceed. **These are not suggestions.** Stopping costs an hour; not stopping has cost a remobilisation |

## 1.2 The order

The guide follows the processing sequence. §2 to §12 get you from a disk to a point cloud you can
look at. §13 to §21 register it. §22 to §26 check it and fix what is fixable. §27 to §34 identify,
export, record and archive it. §35 is what to check when something is wrong.

**You will not use every section on every job.** Calibration (§13) is periodic. LiDAR QC (§24),
degraded-GNSS remedies (§25) and PFIX (§26) apply only when the trajectory needs them.

## 1.3 Three things to know before you start

These are the mistakes that cost the most, and all three are silent. The explanation for each is in
the Technical Manual at the reference given.

| | | |
|---|---|---|
| 1 | **Registration does not change the point cloud.** Until you run **Update Scans**, the cloud is the unregistered one — and it exports perfectly happily | §19 |
| 2 | **A good RMS does not prove the work succeeded.** A bad one proves it failed. Trimble says this in identical words in two places | §23 |
| 3 | **Cleanup cannot be undone** | §28 |

## 1.4 When a section says a decision is open

A **PARAMETRIX DECISION REQUIRED** marker means the SOP identifies a requirement whose answer is
not set. You still have to do something today. Where this guide suggests what, it is marked as a
suggestion and it is not a Parametrix standard.

## 1.5 Record as you go

Several sections end with **Record**. Those entries are the SOP's required records (SOP Appendix
B), and five of them have **no software artefact behind them** — if you do not write them down at
the time, nothing else will.

Templates are in **Appendix F**.

---

# 2. Data Intake

**Before anything else happens.** Nothing in this section involves TBC.

### Do

1. **Copy, do not move.** The source disk stays the source until a verified copy exists in two
   places
2. **Verify the copy** — file count and total size at minimum; a checksum comparison if your
   tooling allows
3. **Confirm `POS_1/raw/` is present and non-empty**
4. **Confirm base station data** is in `Base/`, if a local base was occupied
5. **Take the raw-data backup now**, before any processing
6. Only then is the source disk available for reuse

### Look at

The mission folder, which should look like this:

```
TMX<serial>-<mission id>/
  ├── Base/                 .YYo .YYn .YYg      base RINEX, if collected
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── POS_1/raw/            posl_*.000, .001 …  ← the irreplaceable one
  ├── Extcal.json           the calibration file
  ├── <mission>.mxdb        the file you import
  └── <mission>_*.log
```

### Expect

Tens to hundreds of gigabytes. `POS_1/raw/` holds a numbered series of `posl_*` files, not one
file. `Extcal.json` is small and is there.

### Stop if

- **`POS_1/raw/` is missing or empty.** There is no post-processed trajectory without it and the
  mission is NAV-only. Raise it now, while re-collection is still a small decision
- The copy does not verify
- The mission folder has arrived without the field record

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

> **Take the backup before processing, not after.** Processing writes into the project and, with
> **Backup SBET Next to MXDB** enabled (§8), into the raw data folder beside the `.mxdb`. A backup
> taken afterwards is a backup of a partly processed state *(SOP §11.3)*.

### Record

Offload performed, verified how, by whom, when. Where the backup is.

---

# 3. Checking Mission Information

Do this immediately after import (§7), before any processing. Seven checks, none taking a minute.

### Do

Open the mission properties and the **Mobile Mapping** node in Project Explorer and check:

| # | Check | Against |
|---|---|---|
| 1 | **Project coordinate system** | The control network and the client requirement |
| 2 | **Covered distance** | The field record |
| 3 | **Run count** | The field record |
| 4 | **Active trajectory** — is it SBET, not NAV? | Intent |
| 5 | **Capture Devices** — the sensors listed | The configuration: **Camera 3 Back Down**, **Camera 4 360°**, and the two lasers |
| 6 | **Base station data** present in the project | Whether you will process the trajectory in house |
| 7 | **Calibration state recorded** | §4 |

### Look at

The **Capture Devices** node, and the **Sbet** node under each run.

### Expect

The tree looks like this — **note that scans will hang off the trajectory, not off the run**:

```
Mobile Mapping
  └── <mission id>
        ├── Capture Devices     Camera 3 Back Down, Camera 4 360°, Laser Left, Laser Right
        └── Run 0, Run 1, Run 2 …
              └── Sbet          the imported trajectory
```

### Stop if

- **Run count is lower than the field record.** Data was lost in transfer. Do not process it —
  go back to the copy
- **A sensor is missing from Capture Devices.** It was disabled or it failed in the field. That is
  a field-record and re-collection question, not a processing one
- **Covered distance is materially short** of what the crew logged
- **The trajectory is NAV, not SBET,** and you have no recorded reason

> **Intake does not fix anything.** If a check fails, record it and raise it *(SOP §12.4)*. A
> processor who quietly corrects a coordinate system mismatch at intake has removed the evidence
> that field and office disagreed.

### Record

Each check, with its result. Anything that failed, and what was done.

---

# 4. Calibration-State Intake

**Do this at intake, not later.** A later project cleanup (§29) removes the objects that would
produce the report.

### Do

1. **Copy `Extcal.json` out of the raw mission folder** into the project record, named with the
   system serial number and the mission date
2. Run the **Mission Report** — *(TBC 23991_1)*
3. Archive the report into the project record

### Look at

The report's **Capture devices** table. It carries per-sensor **boresight installation** and
**boresight refinement**, and a **date of calibration**.

### Expect

A date of calibration you can point at, for each sensor.

### Stop if

- **The calibration date cannot be established.** Which calibration a mission was processed
  against is a question somebody will ask later, and the answer has to exist now
- The calibration date is older than whatever interval Parametrix has set

> **PARAMETRIX DECISION REQUIRED · D-26**
>
> The recalibration interval and its triggers — including whether daily removal of the Sensor Unit
> counts as disturbing the calibration *(SOP §14.2)*.

> **That dated record is the only one found anywhere in the workflow** *(Technical Manual §30)*.
> There is no other place the software tells you when the system was last calibrated.

### Record

`Extcal.json` and the Mission Report, both in the project record. Which calibration this mission
was processed against.

---

# 5. Project Setup

### Do

1. Create the VCE project
2. **Set the coordinate system, datum, epoch and geoid model — before importing anything**
3. Record what you set, and who set it

### Look at

The project's coordinate system properties, against the control network and the written client
requirement (SOP §6.1).

### Expect

A coordinate system that matches the control you are going to register against. TBC 2026.10 ships
**Coordinate System Database v115**; selecting a predefined geoid model now enters the vertical
datum name automatically *(TBC RN 2026.10)*.

### Stop if

- The project's accuracy requirement is not stated in writing
- The CRS, datum or epoch has not been decided *(SOP §6.2, D-21)*
- Grid or ground has not been agreed with the client *(SOP §6.3, D-38)*

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

> Practically: if you discover the CRS is wrong after processing, the cheapest honest route is a
> new project and a re-import, not a change in place.

### Record

CRS, datum, epoch, geoid, and who set them.

---

# 6. Coordinate Systems — What to Set and What to Check

This is not a lesson in datums. It is the four places mobile mapping treats them differently
*(Technical Manual §12)*.

### Do

| # | | |
|---|---|---|
| 1 | Set the CRS **before** import | §5 |
| 2 | Set the epoch deliberately if the datum is time-dependent | TBC 2026.10 allows a non-default epoch and warns it "is intended for experienced users" *(TBC RN 2026.10)* |
| 3 | After trajectory processing, **read the SBET filename** | §10 |
| 4 | At export, know whether you are producing grid or ground | §30 |

### Look at

The SBET filename once the trajectory exists:

| Filename | What POSPac did |
|---|---|
| `sbet_[mission].out` | Computed directly in the project's datum and epoch |
| `sbet_[mission]_[frame].out` | **Computed first in ITRF00, then transformed** into the project datum and epoch |

*(TBC 25943)*

### Expect

Either form. Neither is an error.

### Stop if

Nothing here stops you on its own. But **record which form you got**, because the second means an
additional transformation happened that nobody chose.

> **The filename is an indicator, not a verdict.** It tells you a transformation occurred. It does
> not tell you the parameters were right or that the result is accurate — and the plain form is
> equally not proof of correctness *(Technical Manual §12.3)*.

> **TESTING REQUIRED · T10**
>
> Which of Parametrix's normal coordinate systems POSPac recognises directly, and which trigger the
> ITRF00 path. Answerable once, then known.

### Record

The SBET filename, in full, in the delivery record (§28).

---

# 7. Importing the Mission

### Do

1. Confirm the project CRS is already set (§5)
2. Import the **`<mission>.mxdb`**
3. If you will process the trajectory in house, **import the base station observation file** from
   `Base/` — the **`.YYo`**

### Look at

Project Explorer, under **Mobile Mapping**. Then go straight to §3 and do the seven checks.

### Expect

A mission node, a **Capture Devices** node, and one node per run with an **Sbet** trajectory
beneath it.

### Stop if

- The `.mxdb` will not open. Go back to the copy (§2) — this is the definitive test that the
  transfer worked
- The run count or covered distance disagrees with the field record (§3)

> **CAUTION**
>
> **Import the observation file only.** The `Base/` folder also holds `.YYn` and `.YYg` ephemeris
> files. Trimble states: **"Do not import the ephemeris files into TBC."** *(TBC 25943)*

> **Scans are children of a trajectory, not of a run.** That is why a run can end up with two sets
> of scans that look identical in plan, and it is the structural fact the whole of §27 rests on
> *(Technical Manual §5.3)*.

### Record

Import date, and that the seven intake checks were done.

---

# 8. Trajectory Processing

Computes the SBET inside TBC, without going out to POSPac. **Requires a POSPac MMS 8.6+ licence**
— see §9 if you do not have one.

### Do

1. Import the base station `.YYo` first (§7)
2. Right-click the **Mission** node ▸ **Process Raw Trajectory Data**
3. TBC loads the raw POS data automatically and fills the settings from what the vehicle logged.
   **Check them — do not accept them unread.** Trimble's own instruction: *"Double check the
   settings values and if needed modify them"* *(TBC 25943)*
4. Set **Computation Mode** — **IN-Fusion+ Single Base** or **IN-Fusion+ PP-RTX**
5. **Verify the antenna model** — see below
6. Enable **Backup SBET Next to MXDB**
7. Consider **Generate QC Report**
8. **Compute**

### Look at — the settings, with Trimble's defaults

| Setting | Values | Default |
|---|---|---|
| **Computation Mode** | Single Base · PP-RTX | *none stated* |
| **Initialization Mode** | VNAV · **Gyro-compassing** · GAMS · GAMS and Gyro-compassing | Gyro-compassing |
| **Multipath** | Low · **Medium** · High | Medium |
| **Antenna Manufacturer / Type** | Read from the RINEX | — |
| **GAMS** | lever arm and standard deviation | *dimmed if GAMS was disabled at acquisition* |
| **DMI** | lever arm, SD, scale factor, scale factor SD | *dimmed if DMI was disabled at acquisition* |
| **LiDAR QC (Refine with scans)** | on/off | Off — see §24 |

*(TBC 25943)*

### The one field to check every time

> **CAUTION**
>
> **The antenna model must read `Trimble 112735`** for an MX60. `Tallysman/33-3970` is the MX9 and
> MX50 antenna *(TBC 25943)*.
>
> It is read automatically from the RINEX, **which means it can be read wrongly.** An incorrect
> antenna model puts a **systematic antenna-height and reference error** into the trajectory, and
> nothing downstream will attribute the symptom to its real cause.

### Expect

A trajectory that computes without error, and an SBET file in the project folder.

### Stop if

- **The antenna model is not `Trimble 112735`**
- **A GAMS or DMI pane is dimmed and you expected the sensor to be fitted.** Dimmed means the
  sensor was disabled during acquisition and logged nothing (§35). That is a field problem
- The DMI scale factor came from a manual rather than a measured wheel, and the standard deviation
  is still at the 5 % default. Trimble's escape hatch is to **set it to 100 % if the value is not
  known at all** *(TBC 25943)*

> **TESTING REQUIRED · T11, T12**
>
> Whether **Multipath = Medium** is right for open-sky Parametrix corridors, and whether the DMI
> 5 % default is an accuracy claim anybody verified *(SOP §13.1)*.

### Record

The settings used, the computation mode, and the frame-and-epoch log that **Backup SBET Next to
MXDB** writes. That log is the only artefact anywhere in the workflow that records the frame and
epoch a trajectory was computed in, and it lives beside the raw data rather than inside a project
that may later be cleaned up *(SOP §13.2)*.

---

# 9. POSPac Requirements — and What to Do Without It

### What the licence gates

| Route | Needs POSPac? |
|---|---|
| **Process Raw Trajectory Data** inside TBC | **Yes** — POSPac MMS **8.6 or later**, licensed *(TBC 25943)* |
| **Generate POSPac Position Fixes (PFIX)** — §26 | **Yes** |
| Processing in POSPac externally and importing the SBET | Yes, obviously |
| Using the SBET the vehicle or a bureau produced | No |
| **LiDAR QC** — §24 | Not stated by Trimble. See below |

### Do — if you have the licence

Confirm the version is 8.6 or later and that TBC can see it. **Support ▸ License Manager**.

### Do — if you do not

1. Obtain a post-processed SBET from whoever holds a licence, and import it
2. Or, if no post-processed trajectory is available at all, **stop and raise it** — see below
3. Record which route was used, on every job

### Stop if

- **The only trajectory available is the NAV solution** and the deliverable is survey-grade. NAV is
  the real-time solution computed in the vehicle. It is a fallback, not an option
  *(Technical Manual §17.2)*

> **PARAMETRIX DECISION REQUIRED · D-10 · blocks operation**
>
> **Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?**
>
> Without it, two of the three degraded-GNSS remedies disappear: reprocessing with different
> settings, and PFIX *(SOP §13.1)*.

> **VENDOR CLARIFICATION REQUIRED · V-9**
>
> Whether **LiDAR QC** has its own POSPac dependency. Trimble does not state one, but it is an
> Applanix technology and the topic directs configuration questions to the Applanix Support Team
> *(TBC 28972)*.

---

# 10. Reading the Trajectory

**Do this before you generate a single scan.** It is the highest-value, lowest-effort check in the
whole workflow, it takes seconds, and it tells you where everything else is going to be difficult.

### Do

1. **Mobile Mapping ▸ Trajectory Settings ▸ Rendering Settings ▸ RMS values**
2. Set the ranges and colours you want. **The settings persist between projects** *(TBC 27248)*
3. Look at the trajectory in **Plan View**
4. For detail: **Mobile Mapping ▸ Reports ▸ Trajectory Plots**

### Look at

Three things, in this order:

| | |
|---|---|
| **Where the solution degraded** | That is where control is worth most (§14), and where registration will struggle |
| **How long each degraded stretch is** | A short gap bracketed by good data is bridged well. A long one is not |
| **Whether the degradation is at the ends of the mission** | The ends are where the smoother had data on one side only. If the last stretch is a different colour from the rest, that is the closing sequence talking *(Technical Manual §14.4)* |

### Expect

Mostly one colour, with the degraded stretches where the mission plan predicted them — under the
overpass, through the tree cover — and short.

### Stop if

- A degraded stretch is long and you have **no control bracketing it** and **no overlapping pass**.
  You have no remedy for it, and that is a conversation to have now rather than after registration
  (§25)
- The whole trajectory is degraded. Something is wrong upstream — check §8 and §35

> **Segments that have been registered render as "Undefined RMS"** *(TBC 27248)*. A registered
> trajectory no longer matches its `smrmsg` file, so the colouring drops out. That is a side
> effect, and §27 turns it into a useful one: it makes the extent of a registration visible in
> plan, including where a **Local** adjustment stopped.

### Record

A screen capture of the RMS-coloured trajectory. It is a required QC record (SOP §15.8) and it is
one click.

---

# 11. Generate Scans

This is where the trajectory meets the measurements. Before it, the scanner data is ranges and
angles from a moving sensor; after it, every return has a coordinate.

### Do

1. Select a **run** in Project Explorer — **one run first**, not the mission
2. **Generate Scans** from the context menu
3. Set the **Filters**
4. Set **Colorization**
5. Run it, inspect the result (§12), and only then repeat at **mission** level

### Look at — the filters

| Filter | Removes |
|---|---|
| **Range Min / Max** | Returns outside a distance window |
| **Isolated Points** | Points with too few neighbours |
| **Fog** | Returns caused by fog |
| **Sun** | Returns caused by direct sunlight on the sensor |
| **Reflective Panels** | "the noise before and after a target" |
| **Dust** | Airborne dust returns *(Product Bulletin, January 2025)* |

Then the **Results of Scan Generation** dialog, which records per run the filters applied, the
range, and the counts.

### Expect

Scans appearing **beneath the trajectory node**, not beneath the run. Generating at mission level
processes all runs; at run level, one.

### Stop if

- **The deliverable is sign or retroreflectivity work and Reflective Panels is on.** Those returns
  may be the deliverable
- The filter set is not the one you intended. Regenerating is cheap in effort and expensive in
  time; getting it right on one run first is why step 1 says one run

> **TESTING REQUIRED · T1, T3**
>
> Filter defaults are untested against Parametrix work. **T3:** whether **Reflective Panels**
> removes legitimate retro-reflective returns from signs and line marking *(SOP §13.3)*.

> **The MX60 has no MTA stage.** If you find TBC documentation about configuring a GPU driver for
> MTA range-ambiguity correction *(TBC 23856)*, it does not apply to this system — that is the MX9
> and MX90 path *(Technical Manual §5.1)*.

### Record

**Capture the Results of Scan Generation into the project record.** It is the only artefact that
states which filters produced a given cloud *(SOP §13.3)*.

---

# 12. Checking the Scans

A first look, on one run, before you commit to the mission.

### Do

1. Open the run's scans in **3D View**
2. Set rendering to **Scan Color** — one colour per scan
3. Look along the corridor, and then at a cross-section

### Look at

| | |
|---|---|
| **Coverage** | Does the cloud run the full length you expected? |
| **Both lasers** | Left and right should both be present |
| **Density at range** | Thinning with distance is normal and expected |
| **Obvious voids** | Occlusion by a vehicle, or a filter that removed more than you meant |
| **The filters' effect** | Compare against an unfiltered generation if you are unsure |

### Expect

A clean, dense cloud. **It will look clean even when the trajectory was poor** — that is the whole
problem with mobile mapping data *(Technical Manual §3.2)*. This check is for coverage and filter
sanity, not for accuracy.

### Stop if

- A laser is missing
- Coverage is materially shorter than the run
- A filter has visibly removed something you need

> **This is not the QC pass.** The QC pass needs control, registration and a cutting plane, and it
> is §22. This is a five-minute sanity check before you spend an hour generating a whole mission.

---

# 13. Calibration

**Periodic, not per-job.** Run it when the interval or a trigger says so (SOP §14.2), not because
a dataset looks wrong.

## 13.1 The laser scanners

### Do

1. Collect the calibration mission: **four runs — two along one road forward and backward, two
   along a crossing road forward and backward** *(TBC 24886)*
2. Import it, and **generate scans** from all four runs
3. **Calibrate Laser Scanners**
4. Work **both run pairs**. The dialog presents one pair at a time and the second is easy to miss
5. Read the results, then **do the visual check**

### Look at

| | Requirement |
|---|---|
| Crossing angle | As close to **90°** as possible, tolerance **± 30°** |
| Minimum run length | **At least 20 m each side** of the crossing |
| Ideal run length | **80 m — 40 m each side** |
| Façades | Present **in each direction**, in quantity |
| Vegetation | A few or none |

*(TBC 24886 / 20716)*

Then, in the results: **Overall Overlap %**, **Overall RMS**, and per-pair RMS in **tangential,
orthogonal and vertical**.

### Expect

Three similar-sized components. **One much larger than the other two points at a specific part of
the solution**: tangential at timing or along-track scale, orthogonal at heading, vertical at pitch
or the height component *(Technical Manual §23.3)*.

### Stop if

> **CAUTION**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> **Do not accept a calibration on RMS alone.** Bad numbers end it; good numbers do not finish it.

Also stop if the site has no façades in one direction, or heavy vegetation. **Façades are the
measurement** — a boresight error shows as the same flat surface appearing twice when scanned from
opposing directions. Vegetation is noise in exactly that comparison.

## 13.2 The cameras

### Do

1. Generate scans from at least one run
2. Select a camera under **Capture Devices** ▸ **Manual Camera Calibration**
3. Pick a position on the trajectory in Plan View; the camera view displays there
4. Enter **Heading**, **Pitch** or **Roll** and press Enter — **the view updates immediately**

| Input | Step |
|---|---|
| Arrow up / down · mouse wheel | ± 0.001° |
| Ctrl + arrow · Page Up/Down · Ctrl + wheel | ± 0.01° |

*(TBC 24868)*

### Expect

**A visual, iterative alignment, not a computed adjustment.** You nudge until the imagery lines up
with the cloud. There is no residual, and the quality is whatever care you took.

### Stop if

You cannot get the imagery to sit on the cloud at more than one location. That is not a boresight
you can nudge out.

## 13.3 Afterwards

### Do

1. **Export the calibration JSON and archive it outside the TBC project**, named with the system
   serial number and the calibration date *(SOP §14.5)*
2. Record the calibration: date, site, who, and the result **including the visual check**

> The JSON is the complete calibration state in one small file. It imports into any later project
> and is the only portable record of what the system's angles were on a given date. A cleanup
> (§29) or a lost workstation should not take it with them.

---

# 14. Importing Control

### Do

1. Obtain the control file — **Shape, ASCII or CSV** *(TBC 22905)*
2. Confirm it is in the project's coordinate system (§5)
3. Import it
4. Confirm the points appear in **Plan View** and under the **Points** node

### Look at

The points, in plan, against the trajectory and the scans. Do they fall where the field record says
they should?

### Expect

Every point you surveyed, in the right place, in the right frame.

### Stop if

- The points plot in the wrong place — that is a coordinate system or units problem, and it is much
  cheaper to fix now than after a registration
- **The control does not bracket the extent you intend to deliver.** A **Local** registration does
  not adjust beyond the outermost control point (§15, §16)
- **Nobody has designated which points are control and which are independent checks.** That
  designation is made **before** registration, by someone other than the person registering
  *(SOP §7.3)*

> **A mobile mapping control point has to be findable in the point cloud** at the density and
> incidence angle the vehicle produced — which is a different requirement from occupiable with a
> prism. A painted stop-bar corner is excellent horizontally and poor vertically; a survey nail in
> asphalt is below cloud resolution *(Technical Manual §22.5)*.

### Record

The control file used, and the control-versus-check designation with the name of whoever made it.

---

# 15. GCP and Check Point Configuration

**Three independent choices per point.** This is the most consequential configuration in the
office workflow and it is three checkboxes.

### Do

For each point, in the **Control Points** list of a registration command:

| Setting | Meaning |
|---|---|
| **Use XY** | The point constrains the adjustment horizontally |
| **Use Z** | The point constrains the adjustment vertically |
| **As Check** | The point is paired and measured, **but excluded from the adjustment** |

They are per-point and per-component. A point can be **Use XY** and **As Check** in Z — used
horizontally, held out vertically.

### Look at

The designation you were given (§14), and set it. **Do not decide it here.**

### Expect

A mixture. A painted road-surface mark is usually Use XY and not Use Z. A point held out entirely
is a validation point.

### Stop if

- **Every point is set As Check.** TBC will not compute — the adjustment has nothing to fit
- **No point is set As Check.** Then nothing measures the result, and the residuals you are about
  to read measure only how well the adjustment fitted observations it was given *(§20)*
- **You are about to change an As Check setting during processing.** Stop. That designation was
  fixed before registration began, and changing it is a Project Surveyor decision that gets
  recorded and requires the registration to be recomputed from the imported trajectory using
  **Edit** (§19) — not layered on top *(SOP §7.3)*

> **The failure this prevents.** A conscientious processor registers a mission, finds one check
> point with a larger residual than expected, and adds it to the adjustment to bring it in. Every
> step is well intentioned. The result is an adjustment with **no independent check at all**, and a
> set of residuals that now measure nothing *(Technical Manual §22.4)*.

### Record

Point ID, Use XY, Use Z, As Check — for every point, **outside TBC**. The software does not
appear to report it (§20, §28).

---

# 16. Register a Run

One run, against surveyed control.

### Do

1. In **Project Explorer**, select a run
2. Generate its scans if not already done (§11) — **the command is dimmed without at least one
   generated scan**
3. Import the GCP file (§14)
4. **Mobile Mapping ▸ Processing ▸ Register a Run**
5. Accept the default **Registration Name** (*RunName* Trajectory) or enter one. **This name goes
   to the computed trajectory — it is what you will be identifying months later** (§27)
6. Choose a **Registration Type** — see below
7. Select a GCP under the **Points** node ▸ **Add Selection to Control Points**
8. Set **Use XY**, **Use Z**, **As Check** for that point (§15)
9. Optionally **Activate Limit Box** — hides everything outside a box, "to remove potential
   parasitic points over the target"
10. Optionally **Activate Target-Bundle Adjustment** — see below
11. Select the point in the **Control Points** list. It centres in Plan View and **Point Cloud
    Smart Picking** opens
12. Pick the target, read the residuals, **Validate**
13. Repeat for further points
14. **Compute.** The adjusted trajectory draws **blue**; the original stays **green**
15. **Apply**

*(TBC 22905)*

### Look at — Registration Type

| Type | What it does |
|---|---|
| **Global** | A shift of the whole trajectory, **without rotation** |
| **Local** | Interpolates **between** control points |
| **Global, and then Local** | Global first, then Local |

> **CAUTION · W-08**
>
> **Local does not extrapolate.** Trimble states it is *"not for systematic error along the run or
> for adjusting outside the ground control points set"* *(TBC 22905)*.
>
> Beyond the first and last control point the trajectory is not adjusted, **and nothing indicates
> where the adjustment stopped.** Control must bracket the extent you intend to deliver.

> **TESTING REQUIRED · T15**
>
> Which type, when. No selection rule is published, and **Global-then-Local** appears in every
> Trimble screenshot with no guidance attached *(SOP §13.4)*.

### Look at — Target-Bundle Adjustment

**The name reads backwards.** Checked = **250 m** intervals, which is **coarser**. Unchecked =
**70 m** *(TBC 22905)*.

> **TESTING REQUIRED · T9** — test both states against independent checks.

### Expect, after Apply

*(TBC 22905)*

- An **adjusted trajectory node** beneath the run, beside `Sbet`
- A new SBET on disk: **`sbet_<date>_reg_####.out`**, incrementing with each registration
- Picked targets renamed *RunName TrajectoryGCPName*, updated ones carrying a trailing `*`
- Trajectory properties reading **`Origin: Registration result`**, **`Input trajectory: Imported
  trajectory`**, and **`Registration type:`**

**Those four properties and the numbered SBET file are your provenance record** (§27).

### Stop if

- The command is dimmed — you have no generated scan on the run
- You are registering a run that has already been registered. **That stacks adjustments.** Use
  **Edit** (§19)
- The residuals on your check points are not what you expected. Read §20 before doing anything
  about it

### Record

Registration name, type, the trajectory node produced, and the SBET filename **with its `_reg_####`
number**.

---

# 17. Register a Mission

A set of runs at once, **with every GCP reusable**. For ordinary corridor work this is probably the
command you want.

### Do

The sequence is that of §16, run from the mission rather than a run. What differs:

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs |
| GCP reuse | Once | **Every GCP, as many times as it appears** |
| Control list | One row per GCP | **One row per GCP `instance`** |
| Instances | — | One per **250 m scan section** whose bounding box contains the GCP |
| Side | — | An instance binds to the **left**, **right**, or **both** sides of the scan section |
| Default name | *RunName* Trajectory | **Reg** |
| Target naming | `RunName TrajectoryGCPName` | `RegistrationName_GCPName_RunName` |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** |

*(TBC 26473)*

### Look at

The **Control Points** list. One painted mark visible in four passes produces **four instances**,
and each is picked separately. Unused instances are removed from the list when you compute.

### Expect

Four runs adjusted against the same observation, and therefore mutually consistent — which is the
point of the command. A corridor driven in both directions twice is the ordinary case.

### Stop if

- You expected instances and got none. The GCP is outside every 250 m scan section's bounding box
- You are about to re-register a mission that has already been registered (§19)

> **PARAMETRIX DECISION REQUIRED · D-12**
>
> Is Register a Mission the corridor default, with Register a Run reserved for single-run cases and
> for repairing one run in an otherwise accepted mission? And what happens to a mission
> registration when one run is later re-collected? *(SOP §13.4)*

### Record

As §16, plus which runs were included.

---

# 18. Register Run to Run

**Cloud-to-cloud, against a fixed Reference Run. It uses no surveyed control.**

That is the whole point and the whole limitation: it makes two runs agree with each other. It
cannot make them agree with the ground.

### Do

1. Import the missions
2. **Mobile Mapping ▸ Processing ▸ Register Run to Run**
3. Enter a **Registration Name** — "This name will be given to all computed trajectories"
4. Select a pair: one **Run to Adjust**, one **Reference Run**. They may come from the same
   mission or from different missions. Runs list as `<mission ID last two digits> - Run <n>`
5. **Swap Runs** inverts the two
6. **+** adds the pair to the batch
7. In Plan View the **Run to Adjust draws green**, the **Reference Run draws red**
8. Repeat for further pairs. **−** removes; the arrows reorder — **TBC registers the pairs in the
   order given**
9. Set the **Update Scans** option — see below
10. Check **Open Cutting Plane View**
11. **Compute**

*(TBC 25096)*

### Look at — the Results tab

RMS in **tangential, orthogonal and vertical**, every **20 m**, plus `No overlap` where the two
runs do not overlap.

`No overlap` rows are information, not noise. They tell you where the comparison had nothing to
compare.

### Update Scans is inside this command

**This is the only place the two steps merge.** The **Update Scans** checkbox regenerates the Run
to Adjust's scans inline *(TBC 25096)*. Everywhere else, Update Scans is a separate command (§21).

### Expect

- A trajectory beneath the **Run to Adjust**, named `GivenName: Runname_X To Runname_X+1`
- RMS statistics in the Results tab
- A cutting plane per pair, named `MissionID Last Two Digits - Run to Adjust`

### Stop if

- **You have not registered to surveyed control first.** Run-to-run improves *relative* agreement.
  It cannot establish absolute position, and if the Reference Run is itself displaced, run-to-run
  will faithfully propagate that displacement into the run you adjusted
- **You have not re-checked against independent check points afterwards.** The Run to Adjust has
  moved; its residuals against control have changed

> **The order that matters** *(SOP §13.4)*:
>
> 1. Register the mission to surveyed control (§17)
> 2. Assess against independent check points (§20) and visually (§22)
> 3. **Only then** use run-to-run, choosing as Reference Run the pass with the better GNSS
>    conditions and the better residuals
> 4. **Re-check against the independent check points**
>
> Step 4 is the one that gets skipped.

> **CAUTION**
>
> The same principle as §13 applies here, in Trimble's identical wording: **good RMS does not mean
> the registration succeeded; bad RMS means it failed; a visual check is needed** *(TBC 25096)*.

> **TESTING REQUIRED · T24** — how much run overlap is enough.

### Record

Registration name, the pairs and their order, the RMS statistics, and the check-point residuals
**after** the adjustment.

---

# 19. Editing a Registration — and Why Not to Register Twice

### The problem

> **CAUTION · W-07**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.

Running a registration command a second time on a run that has already been registered adjusts the
**adjusted** trajectory, not the imported one — and no number in the result shows it.

### Do

1. Select the **registered trajectory node**
2. **Edit** from the context menu *(TBC 25362, 26578)*
3. The command reopens with the control points, their Use XY / Use Z / As Check states and the
   picked targets reloaded
4. Change what needs changing
5. **Compute**, then **Apply**

### Look at

That the reloaded state is the one you expect — particularly the **As Check** settings. Edit is
also how you confirm what a previous registration actually used, since no report of it has been
found (§20).

### Expect

The registration recomputed **from the imported trajectory**, not from the adjusted one.

### Stop if

- **A reload prompt appears and you are about to answer "No".** See below
- You cannot find the Edit command. Do not fall back to running the registration again

> **CAUTION · W-06**
>
> If Registration Auto-Saving is on, picked targets are written to **`Targets.csv`**. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

> **TESTING REQUIRED · T7** — whether Registration Auto-Saving is on by default. One glance at the
> dialog answers it.

### Record

That the registration was edited rather than repeated, and what changed.

---

# 20. Residual Review

### Do

1. Read the residuals in the **Targets** pane and in the **Validate Picking** window
2. Separate them: **residuals on points used in the adjustment** and **residuals on points held As
   Check**
3. Write both into the control-and-check table (Appendix F)
4. Read the three-axis breakdown where you have one

### Look at — what TBC gives you, at four levels

| Level | Indicator | Where |
|---|---|---|
| **Per pick, live** | Easting, Northing, Elevation residual to the GCP, **signed**; RMS of the fitted plane | Validate Picking, Targets pane *(TBC 22905)* |
| **Per run pair, every 20 m** | RMS in tangential / orthogonal / vertical; `No overlap` | Results tab, Register Run to Run *(TBC 25096)* |
| **Whole calibration** | Overall Overlap %, Overall RMS, per-pair three-axis | Calibrate Laser Scanners *(TBC 24886)* |
| **Trajectory-wide** | Position, orientation, velocity RMS after smoothing | Plan View colouring (§10) |

### Look at — the three axes, when you have them

| Dominant component | Points at |
|---|---|
| **Tangential** — along travel | Timing, or along-track scale. Check the DMI scale factor and time synchronisation |
| **Orthogonal** — across travel | **Heading.** The hardest component, and the one a single direction of travel cannot resolve |
| **Vertical** | Pitch, or the height component. Check the antenna model (§8) and the geoid |

Three similar-sized components mean random disagreement, which is what good data looks like. **One
much larger than the other two is the solution telling you which part of itself is struggling**
*(Technical Manual §23.3)*.

### Expect

Residuals on the **used** points to be small. That is not evidence of anything — an adjustment with
few observations fits them exactly, and one whose observations share a systematic error fits them
beautifully and carries the error straight through.

### Stop if

> **CAUTION**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> **A number can prove failure. A number cannot prove success.**

Stop if:

- **There are no As Check residuals.** Nothing is measuring the result
- A check-point residual is much larger than the used-point residuals, and you are about to promote
  it into the adjustment. **Do not.** Read §15 again
- One three-axis component dominates. Diagnose it before accepting

> **What TBC does not report.** No captured topic produces a statement of **which points were used
> as control and which as checks** in a registration already applied. The state is visible while
> the command is open and reloads on **Edit** *(TBC 25362, 26578)* — but no report of it has been
> found.
>
> **TESTING REQUIRED · T21, V-11.** TBC 2025.21 says signed residuals are "included in the report"
> without naming it, and the only mobile mapping report topic does not mention residuals. Ten
> minutes with the software answers it.

### Record

The control-and-check table: point ID, Use XY, Use Z, As Check, and the residual on each. **Six
columns, written once.** It is the single most important record in the workflow and the software
does not produce it (§28, SOP §19).

---

# 21. Update Scans — and Confirming It Worked

**The step that is easiest to skip and most expensive to skip.**

### Do

1. Select the run or mission
2. **Update Scans**
3. Choose the **registered** trajectory
4. Confirm the result in Project Explorer — see **Look at**

### Look at

The scan stations. Updated ones carry a **`_reg_####`** suffix:

```
Run_14_Laser Right_reg_0001 (S3)
```

And their position in the tree: they hang beneath the **registered trajectory**, not beneath
`Sbet`.

### Expect

A **second** set of scans, beneath the adjusted trajectory. The original set is still there,
beneath `Sbet`, and both look identical in plan. That is not a duplicate to tidy away — they are
the same raw data computed against two different trajectories *(Technical Manual §5.3)*.

### Stop if

- The stations do not carry `_reg_####`
- The scans still sit beneath `Sbet`

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

> **Update Scans works both ways.** It switches between the imported and the adjusted trajectory,
> so it is also how you revert.

> **One exception:** **Register Run to Run** has an **Update Scans** checkbox inside the command
> (§18). That is the only place the two steps merge.

### Record

That Update Scans was run, against which trajectory. The pre-export check in §31 confirms it again
before anything leaves.

---

# 22. Visual QC

**This is the layer that catches what numbers cannot.** It has no software artefact, so if you do
not record it, there is no evidence it happened.

### Do

1. **Point Clouds ▸ View ▸ Cutting Plane View**
2. **Set rendering to Scan Color** — see below
3. Drag the plane along the corridor, full length
4. Work the checklist under **Look at**
5. Record what you covered, and by whom

### The setting that makes or breaks this

> **IMPORTANT**
>
> **Set rendering to Scan Color** — one colour per scan. Without it, two offset surfaces read as
> one thick surface and the exact defect this check exists to find is invisible
> *(Technical Manual §25)*.
>
> It is part of the method, not a display preference.

### Look at

| Check | Looking for |
|---|---|
| **Overlapping passes in the cutting plane, full length** | Doubled surfaces |
| **Flat surfaces at range** — a wall, a building face | Thickening with distance: attitude error or a calibration issue |
| **The ends of the corridor** | Where a **Local** adjustment stopped; where the smoother was weakest |
| **The degraded stretches you found in §10** | Whether the registration actually fixed them |
| **Vertical surfaces against horizontal** | Systematic tilt |
| **Features near control versus far from control** | Residual growth with distance from constraint |

*(SOP §15.5)*

### Expect

Overlapping passes landing on each other. Flat surfaces that stay flat as range increases.

### Stop if

- Two passes are visibly offset from each other anywhere
- A wall thickens with range
- The cloud is good near control and degrades between — that is the shape of an adjustment that
  fitted its constraints and nothing else

> **TESTING REQUIRED · T16** — the working cutting-plane thickness for these checks.

> **PARAMETRIX DECISION REQUIRED · D-39** — how much of a corridor is inspected, and how that is
> decided *(SOP §15.5)*.

### Record

**That the visual check was performed, by whom, and over what extent.** No software artefact
exists. This is the record.

---

# 23. Imagery QC

### Do

1. Step through the imagery along the corridor
2. Work the checklist
3. Check alignment against the point cloud at a feature edge

### Look at

| Check | Looking for |
|---|---|
| **Coverage** | Gaps where a camera stopped, or a run was not colorized |
| **Exposure** | Blown highlights; blocked shadows under canopy and in underpasses. **Both unrecoverable** |
| **Motion blur** | Speed too high for the light available |
| **Obstruction** | Aerials, a following vehicle, a smear on the dome |
| **Focus and contamination** | Rain, dust, insects on the optical surface |
| **Corrupted images** | **Silent** — see below |
| **Alignment with the cloud** | Colour in the wrong place at feature edges: a camera boresight issue (§13.2) |

*(SOP §15.6)*

### Expect

Resolution by configuration *(TBC 22501, 23888)*:

| | Core | Pro | Premium |
|---|---|---|---|
| Panoramic | **8192 × 4096** | **12288 × 6144** | **12288 × 6144** |
| Side / planar | 4096 × 3008 | 4096 × 3008 | 4096 × 3008 |

> **PARAMETRIX DECISION REQUIRED · D-2** — which configuration this system is. Every number above
> depends on it *(SOP §6.4)*.

### Stop if

- **A corrupted side camera image exports as black.** It is silent: nothing warns you, and the
  export succeeds. If you find one, assume there are others
- Coverage has a gap you cannot account for
- The imagery does not sit on the cloud

> **PARAMETRIX DECISION REQUIRED · D-31**
>
> Whether the proposed **file-size scan** for finding silently corrupted imagery is adopted. It is a
> screening method proposed by this project and **not validated** *(Technical Manual §26)*.

> **TESTING REQUIRED · T26, T27** — whether exported imagery reflects a registration at all, and
> which imagery streams the MX60 actually has and TBC exposes.

### Record

That the imagery check was performed and by whom. **No software artefact exists.**

> **PARAMETRIX DECISION REQUIRED · D-32** — imagery privacy. Whether unblurred originals are
> retained, and for how long. Decided before collection, not on request *(SOP §18.6)*.

---

# 24. LiDAR QC

Uses the **scan data itself** as an aiding sensor to improve the trajectory — SLAM-like, run
inside trajectory processing. The only degraded-GNSS remedy that needs **neither POSPac nor
additional ground control**.

### Before you start — can this machine run it?

| | Minimum | Recommended |
|---|---|---|
| CPU | Intel Core i7 or i9 | Intel XEON |
| **RAM** | **128 GB** | **256 GB** |
| TEMP storage | 1 TB SSD on the PCI bus | 2 TB SSD M.2 |
| Virtual memory | +1 TB SSD always available | +2 TB M.2, or 4 TB combined |
| Paging file | — | initial = installed RAM, **maximum = 6 × installed RAM** |
| Also required | **MATLAB Runtime R2024b (24.2)**, installed **after** TBC | |

*(TBC 28972)*

### Do

1. Check **LiDAR QC (Refine with scans)** in **Process Raw Trajectory Data** (§8). A LiDAR QC tab
   appears
2. Select the runs from the Project Tree **with overlap** — parallel runs, or crossing runs
3. **Add**
4. Set the parameters
5. **Compute**

### Look at — the settings

| Setting | Values | Default |
|---|---|---|
| **Range** | Minimum and maximum LiDAR measurement distance used | **3 m to 100 m** |
| **Noise** | 5, 10, 50, 80, 100, 200 mm | **5 mm for MX50/MX60** |
| **Lasers** | Left · Right · All | **All** |

### Expect

A long computation. It solves the constant IMU boresight angles and corrects the post-processed
trajectory, position and orientation, from voxels matched in overlapping scan regions
*(TBC 28972)*.

### Stop if

- **The runs do not overlap.** It has nothing to match
- The machine does not meet the requirement above. It is not a setting you can push through

> **TESTING REQUIRED · T13**
>
> Two defaults are untested, and one of them contradicts Trimble's own guidance printed beside it:
> **Lasers = All**, where the note says using both "can increase computation time without
> significantly improving the accuracy, as it compares the left versus right laser of isolated
> runs." Also the **3–100 m** range: the MX60's useful range and the range over which scan geometry
> usefully aids a trajectory are different questions *(Technical Manual §11.3)*.

### The acquisition geometry it wants

| Element | Requirement |
|---|---|
| Area | A structured scene — detached houses, objects within sensor range; open sky |
| Strips | **Two perpendicular strips**, each consisting of **two runs, one in each direction** |
| Strip length | **250–300 m** |

*(TBC 28972)*

**That is materially the same geometry the laser scanner calibration wants (§13).** One site can
serve both, which matters because establishing one is real work *(SOP §14.3)*.

### Record

That LiDAR QC was run, on which runs, with which settings.

---

# 25. Degraded GNSS — Choosing and Applying a Remedy

You are here because §10 showed a degraded stretch. **Four remedies, and they are not
interchangeable.**

### Look at — what each costs and what it needs

| Remedy | Acts on | Needs | Section |
|---|---|---|---|
| **Reprocess with better base data or settings** | The GNSS side of the solution | Raw data intact; better corrections available | §8 |
| **LiDAR QC** | Adds scan data as a third aiding sensor | **Overlapping runs**, and a very large workstation | §24 |
| **PFIX** | Injects surveyed control into a **second POSPac pass** | **POSPac licence**, surveyed control, picked targets | §26 |
| **Registration to control** | Bends the finished trajectory to fit control | Surveyed control | §16, §17 |

> **The first three improve the *solution*. Registration improves the *fit*.** That distinction
> matters: a registered trajectory has been adjusted to agree with the control it was given, so its
> agreement with that control is no longer evidence of anything *(Technical Manual §8.5)*.

### Do

1. Establish how long the degraded stretch is **in time**, not in metres
2. Check what you actually have: overlap? control bracketing it? a POSPac licence?
3. Choose. Prefer a remedy that improves the solution over one that improves the fit
4. Apply it, then **re-check against independent check points** (§20)

### Expect

Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
nothing beyond *(MX60 UG Rev B, p.56)*:

| | Core / Pro | Premium |
|---|---|---|
| No outage | X,Y < 0.01 m · Z 0.01 m | X,Y < 0.01 m · Z 0.01 m |
| **After 60 s outage** | X,Y **0.12 m** · Z **0.1 m** | X,Y **0.1 m** · Z **0.07 m** |

### Stop if

- **The outage is materially longer than 60 seconds.** Beyond the published figure you are
  extrapolating past the manufacturer's stated envelope. Inertial drift is not linear
- **No remedy applies** — no overlap, no bracketing control, no licence. Then the honest finding is
  that **mobile mapping may not be the appropriate acquisition method for that segment**, and that
  goes up, not into the deliverable

> **PARAMETRIX DECISION REQUIRED · D-34** — the decision rule when a corridor produces an
> unacceptable trajectory: who decides, against what, and what the client is told *(SOP §21.5)*.

> **The remedies that need something from the field cannot be arranged now.** Overlap for LiDAR QC
> and control bracketing a hostile stretch are mission-planning decisions *(SOP §8)*. If they were
> not made, the option does not exist today.

### Record

Which remedy, why, and the check-point residuals before and after.

---

# 26. PFIX — The Two-Pass Procedure

**Generate POSPac Position Fixes.** Where registration corrects the answer, PFIX corrects the
computation: the control observations go back into the navigation solver as position fixes and the
filter re-solves with them available.

### Prerequisites

*(TBC 24460)*

- **POSPac MMS installed with a valid licence** for the IN-Fusion processing methods
- An SBET processed in POSPac — or the NAV trajectory, "in case of POSPac processing not possible"
- A VCE project whose coordinate system matches the data
- The `.mxdb` imported with that trajectory applied
- **Scan data generated from at least one run**
- A GCP file imported in the project coordinate system

### Do — part one, in TBC

1. Right-click the **Mission** node ▸ **Generate Pospac Position Fixes**. *The command does not
   open if the mission has no generated scan*
2. Select a GCP under **Points** ▸ **Add Selection to Control Points**
3. Pick the target — **the same Point Cloud Smart Picking tool as registration** (§16), with the
   same live residuals and the same **30 m maximum pair separation**
4. **Validate.** Easting, Northing and Elevation residuals display
5. Add further pairs
6. **Compute.** Updated targets are named `Mission_Name-PFIX-GCP_Name`, and
   **a `custom_events.txt` is written into a `PFIX` folder under the TBC project folder**
7. Close the dialog

### Do — part two, in POSPac

1. Start POSPac MMS, create and save a project
2. Import the POS logged files from `POS_1/raw`
3. **Copy `custom_events.txt` from TBC into the `Extract` folder of the POSPac project**
4. Open the **GNSS-Inertial Processor**
5. Optionally open **Position Fixes and Satellite Events** to inspect the fixes
6. Select the IN-Fusion processing mode
7. **All Processings.** A new SBET appears in the `Proc` folder

### Do — part three, back in TBC

1. Select the mission ▸ properties
2. **Replace the initial trajectory file with the new SBET**
3. **Update Scans** (§21)

### Expect

A better trajectory through the stretch that had no GNSS, with the correction propagated by the
filter's own model of how the system behaves rather than by interpolation between control points.

### Stop if

- **You stop after step 7 of part one.** The `custom_events.txt` does nothing by itself
- **You skip part three's Update Scans.** A better trajectory that never reaches the point cloud
  has cost a day and changed nothing in the deliverable

> **VENDOR CLARIFICATION REQUIRED · V-16**
>
> When should PFIX be preferred over registration? Trimble describes both commands and never
> contrasts them. The framing at the top of this section is this project's reading, not Trimble's
> statement *(Technical Manual §27.5)*.

### Record

That PFIX was used, on which stretch, and the check-point residuals before and after.

---

# 27. Identifying Registration Results

**Which trajectory is this cloud built on?** You will be asked. This section is how you answer.

### Do

Work the four layers, in this order.

| # | Layer | Where |
|---|---|---|
| 1 | **Tree position** | Scans hang beneath the trajectory that produced them |
| 2 | **Station suffix** | Updated stations carry **`_reg_####`** |
| 3 | **Trajectory properties** | **`Origin: Registration result`** · **`Input trajectory:`** · **`Registration type:`** *(TBC 22905, 26473)* |
| 4 | **SBET filename on disk** | `sbet_<date>_reg_####.out`, incrementing per registration, in the project folder |

### Look at

Project Explorer, expanded. A run that has been registered has **two trajectories and two sets of
scans**:

```
Run 14
  ├── Sbet                        the imported trajectory
  │     └── Run_14_Laser Right (S1)          ← unregistered scans
  └── Reg. Trajectory             Origin: Registration result
        └── Run_14_Laser Right_reg_0001 (S3) ← registered scans
```

**They look identical in plan.** Tree position and the suffix are the difference.

### A fifth, incidental indicator

Registered trajectory segments render as **"Undefined RMS"** in the RMS colouring (§10), because a
registered trajectory no longer matches its `smrmsg` file *(TBC 27248)*.

That makes the **extent** of a registration visible in plan — including where a **Local**
adjustment stopped adjusting, which nothing else shows you.

### Expect

All four layers agreeing.

### Stop if

- **They disagree.** A cloud beneath `Sbet` whose stations carry `_reg_####` is telling you
  something you need to resolve before exporting
- **You cannot tell which trajectory a cloud was built on.** Do not export it (§31)

> **Nothing in this is conclusive once the data leaves the project.** That is what §28 is about.

### Record

The trajectory node name and the SBET filename **with its `_reg_####` number**, in the delivery
record.

---

# 28. Trajectory Provenance — What to Record Before You Go Further

### The limitation, stated plainly

> **IMPORTANT**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**

Inside the project, §27 gives you four layers of evidence. **Outside it, you have what you wrote
down.**

### Do

Record these, now, before Cleanup (§29) and before export (§30):

| # | Artefact | Where it comes from |
|---|---|---|
| 1 | **The delivery record** — mission ID, trajectory node name, SBET filename including `_reg_####`, registration type, export path and date, exported by whom | Written by you. Appendix F |
| 2 | **The control-and-check table** — point ID, Use XY, Use Z, As Check, residual on each | Written by you (§20). Appendix F |
| 3 | **The Mission Report**, run **before** Cleanup | *(TBC 23991_1)* |
| 4 | **The calibration JSON** in force | §13.3 |
| 5 | **`Targets.csv`** | The project folder |
| 6 | **The field record** | It came with the data (§2) |
| 7 | **The QC record** — including the visual and imagery checks | Written by you (§22, §23) |

*(SOP §19.2)*

### Expect

**Five of the seven already exist as files.** Two are written by a person. The whole package is a
few hundred kilobytes beside a project of tens of gigabytes.

### Stop if

- You are about to run Cleanup and any of items 3 to 5 is not archived
- You are about to export and item 1 does not exist

> **PARAMETRIX DECISION REQUIRED · D-29** — what provenance record accompanies a deliverable, where
> it lives, and who produces it *(SOP §19.2)*.

> **TESTING REQUIRED · T19, T22, T30** — which trajectory travels with a publish or an export; what
> a LAS file actually carries in its header, VLRs and sidecar; and whether a delivered dataset can
> be matched back to its trajectory after the fact.

---

# 29. Cleanup Mobile Mapping Mission

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*

### Do — the archive-first sequence

**In this order.** Steps 2 to 6 are small files; the whole set is a few megabytes.

| # | Step | Why here |
|---|---|---|
| 1 | **Complete and accept QC** (§22, §32) | Cleanup is an end-of-preparation step. Before acceptance it removes the alternatives you might need |
| 2 | **Run the Mission Report and archive it** | It records capture devices, runs, trajectories, generated scans, and **per-sensor calibration with date**. **Run it before Cleanup** — afterwards it can only report what survives |
| 3 | **Record the registration evidence** (§20, §28) | Control/check designation and residuals. TBC does not report these |
| 4 | **Archive `Targets.csv`** | The picked registration observations — not recoverable |
| 5 | **Archive the numbered SBET files** `sbet_<date>_reg_####.out` | Pending **T28**, assume Cleanup removes them |
| 6 | **Archive the calibration JSON** (§13.3) | The system state the mission was processed under |
| 7 | **Take the project backup Trimble asks for** — into the project archive, not a local copy | A backup nobody can find is not a backup |
| 8 | **Obtain the written authorisation** | SOP §17.2 |
| 9 | **Run Cleanup** | |
| 10 | **Record that it was run** — by whom, on what date, what was archived first | Otherwise the absence of history is itself unexplained |

*(SOP §17.3)*

### Look at

Before running it: the project tree, so you know what you are about to lose. Registered
trajectories, their scans, and the numbered SBET files.

### Expect

Only the most recent registration surviving.

### Stop if

- **You do not have written authorisation** (SOP §17.2, **D-35**)
- Any of steps 2 to 6 is not done
- The backup went to your own machine rather than into the project archive

> **TESTING REQUIRED · T28**
>
> **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?**
> Until it is known, assume the worse case and archive them.

> **PARAMETRIX DECISION REQUIRED · D-35 · blocks operation** — when Cleanup may be performed, by
> whom, and what must be archived first.

### Record

Authorisation; what was archived and where; that Cleanup was run, by whom, on what date.

---

# 30. Export — by Path

**Six documented MX60 paths.** No preference between them is expressed here; format choice is a
project and client matter Parametrix has not decided *(SOP §18.4, **D-38**)*.

**Do §31 first.** Every path below assumes the pre-export check has passed.

### The paths

| Path | Where | Carries the trajectory? |
|---|---|---|
| **Export to LAS (Trajectory Split)** | Mobile Mapping tab | **No**, despite the name |
| **Export to TMX** | Mobile Mapping tab | **Yes** — one trajectory file for all devices, in a folder under the Mission folder |
| **Export to TopoDot** | Mobile Mapping tab | The `.lst` carries image position and orientation |
| **Export to Solv3D** | Mobile Mapping tab | Sidecar `reference.csv` |
| **Generic Point Cloud Export** | **Point Cloud tab** | **No** |
| **Publish to TRCPS** | Home ▸ Data Exchange ▸ Publish to TRCPS | **Yes** — point cloud and trajectories are exported by default |

### Do — Export to LAS (Trajectory Split)

1. **Run Extract Classified Point Cloud first** — *Point Clouds ▸ Regions*. Without it there is
   nothing to export
2. **Home ▸ Data Exchange ▸ Export ▸ Mobile Mapping tab**
3. Set **Splitting distance** — "a value in meter multiple of 250"
4. Choose lasers: merged into one file, or left and right independently. **At least one must be
   selected**
5. Set **Format** — LAS 1.2 or 1.4 — and **Export unit**

*(TBC 27279)*

> **TESTING REQUIRED · T17**
>
> **Sample points performs *random* sampling to a fixed point count.** On a survey deliverable that
> is destructive thinning with no documented spatial rule — no minimum spacing, no preservation of
> edges or breaklines. Its default state is not stated. **Check it before exporting.**

### Do — Export to TMX

1. **Mobile Mapping tab ▸ Export to TMX**
2. Decide the **Export timestamps** setting — **read §31 first**
3. Export

Produces panoramic images, side camera images, laser point clouds **and the trajectory**, plus a
`reference.csv` *(TBC 22501)*.

### Do — Export to TopoDot

1. **Generate scans first.** "Otherwise, nothing will be exported"
2. **Close all run views.** "Otherwise, a warning message will pop up"
3. Export

Produces LAS 1.4, one couple per run *(TBC 23339)*.

### Do — Export to Solv3D

1. **Mobile Mapping tab ▸ Export to Solv3D**
2. Trimble recommends **disabling timestamps** on this path

Produces a mission-named folder with `Lasers` and `Panorama` sub-folders, LAS 1.4 *(TBC 23888)*.

> On this path the recommended setting is also the safe one: timestamps off means the **generated**
> scans are exported rather than reprocessed ones (§31).

### Do — Generic Point Cloud Export

1. **Home ▸ Data Exchange ▸ Export ▸ Point Cloud tab**
2. **This tab selects by region or a drawn rectangle — not by run** *(TBC 11769)*
3. Set **Scaling**: **Grid** or **Ground**, or **ECEF**

| Option | Behaviour |
|---|---|
| **Grid** | Current projected CRS with the combined scale factor. **Writes a `.txt` sidecar naming the coordinate system and scale factor.** Trimble warns re-importing it "may cause some inconsistencies due to a double-scaling effect" |
| **Ground** | Ground coordinates scaled from the 0,0 origin. **"The scale factor is not exposed during export"** |
| **ECEF** | LAS or LAZ in ground-based scaling, "that includes the project's global coordinate system information" |

> **IMPORTANT**
>
> **A ground-scaled export does not record the scale factor it used.** The recipient cannot recover
> it from the file. Agree grid or ground in writing, and make sure the delivery can say which
> *(SOP §6.3)*.

> **This is the path most likely to be used for an ordinary LAS deliverable, and it is the one with
> the least documented provenance and no run awareness.**
>
> **TESTING REQUIRED · T23** — what happens when a Point Cloud tab selection is drawn across scans
> belonging to two different trajectories. Not documented.

### Do — Publish to TRCPS

1. **Home ▸ Data Exchange ▸ Publish to TRCPS ▸ Mobile Mapping tab**
2. Requires a **Trimble ID**; uploads via the **Trimble Desktop Utility**, installed with TBC
3. **Point cloud and trajectories are exported by default** — the publishing options govern
   imagery only *(TBC 29527)*

> **VENDOR CLARIFICATION REQUIRED · V-10 · TESTING REQUIRED · T19**
>
> **Which trajectory is published when several exist under a run is not documented.**

> **From TBC 2026.10, Trimble ID sign-in requires two-step verification** — a code by email each
> time. Worth knowing before it stops a session.

### Record

Export path, date, by whom, format, scaling — into the delivery record (§28, Appendix F).

---

# 31. The Pre-export Check

**One minute. It prevents the most expensive failure in the workflow.**

### Do

1. In **Project Explorer**, find the scan nodes you are about to export
2. Confirm they sit **beneath the intended registered trajectory**
3. Confirm their stations carry the **`_reg_####`** suffix
4. Screen-capture the tree
5. Decide the **Export timestamps** setting — see below
6. Only then export

*(SOP §18.2)*

### Look at

```
Run 14
  ├── Sbet                             ← NOT this one
  │     └── Run_14_Laser Right (S1)
  └── Reg. Trajectory                  ← this one
        └── Run_14_Laser Right_reg_0001 (S3)
```

### Stop if

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

Stop if the scans sit beneath `Sbet`, or the stations have no `_reg_####`. Go back to §21.

### Export timestamps

> **CAUTION · W-03**
>
> With **Export timestamps** set to **Yes**, Trimble states that *"the exported scans are
> **reprocessed from the raw data**"* rather than being the scans processed with Generate Scans
> *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated.** Until this is established, the
> exported data may not be the data that was registered and checked.

**Until T18 is answered, treat an export with timestamps enabled as unverified against the checked
dataset, and do not enable it on a delivered dataset without a recorded reason** *(SOP §18.3)*.

> **TESTING REQUIRED · T18 — the highest-priority test in the register.** Export the same
> registered run twice, timestamps off and on, and compare point geometry.

> **TESTING REQUIRED · T29** — the reliable export-state verification method for each path. How an
> export dialog resolves its selection is not documented.

### Record

The screen capture, and the timestamps setting used.

---

# 32. Final QA/QC — Working the Layers

**Each layer catches something the others cannot.** None is optional because another was performed.

### Do

Work them in order and record each.

| # | Layer | Catches | Where | Artefact |
|---|---|---|---|---|
| 1 | **Field coverage verification** | Missing passes, missing overlap | Field record | Field record |
| 2 | **Intake checks** | Transfer loss, wrong CRS, missing sensors | §3 | Intake record |
| 3 | **Trajectory RMS review** | Where the solution was weak — **before any cloud exists** | §10 | Screen capture |
| 4 | **Residuals on control** | A broken adjustment | §20 | Targets pane |
| 5 | **Residuals on independent checks** | An adjustment that fits its own observations and is still wrong | §20 | **Written by you** |
| 6 | **Visual inspection of the cloud** | Doubled surfaces, thickening at range, tilt | §22 | **No software artefact** |
| 7 | **Imagery inspection** | Coverage, exposure, blur, corruption | §23 | **No software artefact** |
| 8 | **Export-state confirmation** | Delivering the unregistered cloud | §31 | Screen capture |

*(SOP §15.2)*

### Look at

Layer 5 especially. **Residuals on points that took no part in the adjustment are the only
numerical evidence that means anything**, and they exist only if somebody designated check points
before registration began (§15).

### Expect

Layers 6 and 7 to produce nothing you can file unless you write it. **Two of the eight layers have
no software artefact at all.** If a reviewer asks whether the visual check was performed and over
what extent, the only possible answer is a record somebody wrote.

### Stop if

- **There are no As Check residuals**
- Any layer was skipped because another one looked fine
- You are about to accept on RMS alone

> **CAUTION**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

### Acceptance is not yours

**Acceptance is a decision by the person with the authority under SOP §4**, recorded, against the
project's stated accuracy requirement. Your job is to produce the evidence, not to conclude.

> **PARAMETRIX DECISION REQUIRED · D-13 · blocks operation**
>
> **What constitutes an acceptable registration and an acceptable point cloud is not established.**
> Trimble publishes no acceptance tolerance for the MX60 and none has been set by test. **Do not
> invent one, and do not quote one** *(SOP §16.2)*.

### Record

The QA/QC record: every layer, who performed it, when, and over what extent. Appendix C and
Appendix F.

---

# 33. Archiving

### Do

1. Assemble the **record package** (§28) — seven artefacts, a few hundred kilobytes
2. Decide and apply the **retention tier** for everything else
3. Write the **archive record** — one page
4. Put it where somebody who was not involved can find it

### Look at — the three tiers

**Tier 1 — small, irreplaceable, keep indefinitely**

Field record · control-and-check table with residuals · Mission Report run **before** Cleanup ·
calibration JSON · Results of Scan Generation · delivery record · QA/QC record · the accuracy
statement issued.

> **The whole of Tier 1 is a few hundred kilobytes.** There is no storage argument against keeping
> it.

**Tier 2 — a defined period**

SBET and its processing report and the frame-and-epoch log · numbered registered SBETs ·
`Targets.csv` · base station data · the delivered files.

**Tier 3 — per the decision**

| | Size | Note |
|---|---|---|
| **Raw mission folder** | Tens to hundreds of GB | **The only thing that permits reprocessing.** Once gone, the deliverable cannot be improved, only re-collected |
| TBC project | Tens to hundreds of GB | The provenance record |

*(SOP §20.2)*

### Stop if

- **You are about to delete `POS_1/raw/` or `Targets.csv` on your own judgement.** Neither is
  recoverable: one cannot be recomputed, the other was picked by a person and would be different if
  picked again *(SOP §20.3)*
- The archive record does not exist

> **PARAMETRIX DECISION REQUIRED · D-55** — what is retained, where, for how long, by whom
> *(SOP §20.1)*.

> **PARAMETRIX DECISION REQUIRED · D-53** — folder structure, naming and storage location.

### The archive record

One page per project: what was archived, where, when, by whom; the retention tier applied; whether
Cleanup was run and what was archived first; and where the raw mission data is, if it is held
elsewhere.

**Without it, the archive is a folder somebody has to reverse-engineer.**

### Record

The archive record itself. Appendix F.

---

# 34. Documentation Required for QC and Delivery

**One list, so nothing is discovered missing at the end.** Everything here is required by the SOP;
its full index is SOP Appendix B.

### The package

| # | Artefact | From | Exists as a file? |
|---|---|---|---|
| 1 | Intake check record | §3 | **No — you write it** |
| 2 | `Extcal.json` and the Mission Report | §4 | Yes |
| 3 | Trajectory settings and the frame-and-epoch log | §8 | Yes |
| 4 | Trajectory RMS screen capture | §10 | Yes, once you capture it |
| 5 | Results of Scan Generation | §11 | Yes |
| 6 | Calibration record and JSON | §13 | Yes |
| 7 | **Control-and-check table with residuals** | §20 | **No — you write it** |
| 8 | **Visual QC record** | §22 | **No — you write it** |
| 9 | **Imagery QC record** | §23 | **No — you write it** |
| 10 | Update Scans confirmation | §21 | Screen capture |
| 11 | Pre-export check capture and the timestamps setting | §31 | Screen capture |
| 12 | Delivery record | §28 | **No — you write it** |
| 13 | QA/QC record | §32 | **No — you write it** |
| 14 | Cleanup authorisation and what was archived | §29 | **No — you write it** |
| 15 | Archive record | §33 | **No — you write it** |

### Look at

**Eight of the fifteen do not exist unless a person writes them.** That is not an oversight in the
software; several of these facts have no representation in it at all.

### Expect

To spend perhaps thirty minutes across a project producing all of them, most of it copying files
out before Cleanup.

### Stop if

You are at delivery and items 7, 8 or 12 do not exist. Those are the three a reviewer asks for
first, and none can be reconstructed afterwards.

> Templates for the writing-required items are in **Appendix F**.

---

# 35. Common Problems — What to Check First

| Symptom | First check | Then |
|---|---|---|
| **A registration command is dimmed** | Does the run have at least one **generated scan**? | §11 |
| **GAMS or DMI settings are dimmed** in Process Raw Trajectory Data | The sensor was **disabled during acquisition** and logged nothing. Not a software problem | §9 of the Field How To; field record |
| **The trajectory is NAV, not SBET** | Is `POS_1/raw/` present? Is a POSPac licence available? | §2, §9 |
| **Picked targets have vanished** | Was a reload prompt answered **"No"**? `Targets.csv` is emptied permanently | §19, W-06 |
| **Residuals got worse after a second registration** | You registered twice. Adjustments stack — use **Edit** | §19 |
| **The exported cloud is not the registered one** | Was **Update Scans** run? Do the stations carry `_reg_####`? | §21, §31 |
| **Two passes are offset in the cutting plane** | Is rendering set to **Scan Color**? Without it, two surfaces read as one | §22 |
| **A surface looks thick and the numbers were fine** | Attitude error or calibration. Check whether thickening grows with range | §13, §22 |
| **Side camera images export black** | Corrupted imagery. It is **silent** — assume there are others | §23 |
| **Imagery colour sits beside feature edges** | Camera boresight | §13.2 |
| **Nothing exported to TopoDot** | Scans not generated; or run views not closed | §30 |
| **`Extract Classified Point Cloud` produced nothing** | Run it before **Export to LAS (Trajectory Split)**, not after | §30 |
| **The whole trajectory is degraded** | Antenna model — must read **`Trimble 112735`** | §8 |
| **A height bias across the whole job** | Antenna model, geoid, or base station coordinate | §8, §5 |
| **The RMS colouring has gaps** | Registered segments render as **"Undefined RMS"**. Not a fault | §10, §27 |
| **`No overlap` rows in run-to-run results** | Information, not noise. The two runs do not overlap there | §18 |
| **LiDAR QC will not produce a useful result** | Do the runs actually overlap? Does the machine have 128 GB of RAM? | §24 |
| **MTA / GPU driver documentation** | **Not applicable to the MX60.** That is the MX9 and MX90 path | §11 |
| **TBC sign-in asks for an emailed code** | From TBC 2026.10, Trimble ID requires two-step verification | §30 |

### When the answer is "re-collect"

Some of these are not office problems. Missing coverage, missing overlap, a mission with no closing
sequence and a sensor that logged nothing are all field problems, and the only remedy is a
mobilisation *(SOP §21.3)*.

**Raise it. Do not absorb it.** A non-conformance fixed quietly leaves no trace that the workflow
failed, which means it happens again to somebody else on a job where it costs more.

---


---

# Appendices — 

---


---

# Appendix A — Office Processing Checklist

**Intake to delivery.** Tick as you go; the § column is where the detail is.

## A1 · Intake

| ☐ | | § |
|---|---|---|
| ☐ | Copy verified — file count and size, checksum if available | 2 |
| ☐ | `POS_1/raw/` present and non-empty | 2 |
| ☐ | Base station data present, if a local base was occupied | 2 |
| ☐ | Raw-data backup taken **before** any processing | 2 |
| ☐ | Field record received | 2 |
| ☐ | `Extcal.json` copied into the project record | 4 |
| ☐ | Mission Report run and archived; **calibration date established** | 4 |

## A2 · Project and import

| ☐ | | § |
|---|---|---|
| ☐ | Accuracy requirement stated in writing | 5 |
| ☐ | **CRS, datum, epoch, geoid set — before import** | 5 |
| ☐ | Grid or ground agreed in writing | 5 |
| ☐ | `.mxdb` imported; base `.YYo` imported (**not** `.YYn`/`.YYg`) | 7 |
| ☐ | Coordinate system matches the control network | 3 |
| ☐ | Covered distance consistent with the field record | 3 |
| ☐ | **Run count matches the field record** | 3 |
| ☐ | Active trajectory is SBET, not NAV | 3 |
| ☐ | Capture Devices lists the expected sensors | 3 |

## A3 · Trajectory

| ☐ | | § |
|---|---|---|
| ☐ | **Antenna model reads `Trimble 112735`** | 8 |
| ☐ | Computation mode set deliberately | 8 |
| ☐ | GAMS / DMI panes checked — dimmed means the sensor logged nothing | 8 |
| ☐ | **Backup SBET Next to MXDB enabled** | 8 |
| ☐ | Trajectory computed | 8 |
| ☐ | **RMS colouring reviewed and captured** | 10 |
| ☐ | SBET filename recorded — plain or `_frame` | 6 |

## A4 · Scans

| ☐ | | § |
|---|---|---|
| ☐ | One run generated first, filters checked | 11 |
| ☐ | Filters appropriate to the deliverable | 11 |
| ☐ | **Results of Scan Generation captured** | 11 |
| ☐ | Mission generated | 11 |
| ☐ | First look done — coverage, both lasers, voids | 12 |

## A5 · Registration

See **Appendix B**.

## A6 · QC and delivery

See **Appendix C** and **Appendix D**.

## A7 · Close-out

| ☐ | | § |
|---|---|---|
| ☐ | Record package complete — seven artefacts | 28 |
| ☐ | Cleanup, if run, followed the archive-first sequence | 29 |
| ☐ | Archive record written | 33 |

---

# Appendix B — Registration Checklist

## B1 · Before you open the command

| ☐ | | § |
|---|---|---|
| ☐ | Scans generated on the run(s) — **the command is dimmed otherwise** | 11 |
| ☐ | Control imported, in the project coordinate system | 14 |
| ☐ | Control plots where the field record says it should | 14 |
| ☐ | **Control brackets the extent you intend to deliver** | 14 |
| ☐ | **Control-versus-check designation received, in writing, from the Project Surveyor** | 15 |
| ☐ | You are not the person who made that designation | SOP §4.3 |

## B2 · Setting it up

| ☐ | | § |
|---|---|---|
| ☐ | Registration name chosen — **this is what you will identify months later** | 16 |
| ☐ | Registration type chosen deliberately | 16 |
| ☐ | **Use XY / Use Z / As Check set per the designation — not per your judgement** | 15 |
| ☐ | At least one point held **As Check** | 15 |
| ☐ | Not every point held As Check | 15 |
| ☐ | Target-Bundle Adjustment state decided — **checked = 250 m, coarser** | 16 |

## B3 · Picking

| ☐ | | § |
|---|---|---|
| ☐ | Each pick validated, residuals read at the time | 16, 20 |
| ☐ | GCP-to-target separation within **30 m** | 26 |
| ☐ | Reload prompt — **never answered "No"** | 19 |

## B4 · After Compute

| ☐ | | § |
|---|---|---|
| ☐ | Adjusted trajectory node present | 16 |
| ☐ | `sbet_<date>_reg_####.out` on disk, number recorded | 16, 27 |
| ☐ | Trajectory properties read: `Origin: Registration result`, input trajectory, registration type | 27 |
| ☐ | **Residuals on As Check points recorded, by component** | 20 |
| ☐ | Three-axis breakdown read where available | 20 |
| ☐ | **Update Scans run** | 21 |
| ☐ | Stations carry `_reg_####` | 21, 27 |

## B5 · If something needs changing

| ☐ | | § |
|---|---|---|
| ☐ | **Edit** used — **never a second registration** | 19 |
| ☐ | Any change to an As Check designation went back to the Project Surveyor and was recorded | 15 |

## B6 · Run-to-run, if used

| ☐ | | § |
|---|---|---|
| ☐ | Registered to surveyed control **first** | 18 |
| ☐ | Reference Run is the pass with better GNSS and better residuals | 18 |
| ☐ | Pair order set deliberately — **TBC registers in the order given** | 18 |
| ☐ | **Check points re-checked afterwards** | 18 |

---

# Appendix C — QC Checklist

**Eight layers. Each catches something the others cannot.** None is optional because another one
looked fine.

| ☐ | # | Layer | Evidence produced | § |
|---|---|---|---|---|
| ☐ | 1 | Field coverage verification | Field record | 2 |
| ☐ | 2 | Intake checks — seven | Intake record | 3 |
| ☐ | 3 | **Trajectory RMS review** | Screen capture | 10 |
| ☐ | 4 | Residuals on control points used | Targets pane | 20 |
| ☐ | 5 | **Residuals on independent check points** | **Written by you** | 20 |
| ☐ | 6 | **Visual inspection — Cutting Plane View, Scan Color** | **Written by you** | 22 |
| ☐ | 7 | **Imagery inspection** | **Written by you** | 23 |
| ☐ | 8 | Export-state confirmation | Screen capture | 31 |

## C1 · Layer 6 in detail

| ☐ | Check | Looking for |
|---|---|---|
| ☐ | Rendering set to **Scan Color** | Without it the check does not work |
| ☐ | Overlapping passes, plane dragged full length | Doubled surfaces |
| ☐ | Flat surfaces at range | Thickening with distance |
| ☐ | The ends of the corridor | Where a Local adjustment stopped |
| ☐ | The degraded stretches from layer 3 | Whether registration fixed them |
| ☐ | Vertical against horizontal | Systematic tilt |
| ☐ | Near control versus far from control | Residual growth with distance |

## C2 · Layer 7 in detail

| ☐ | Check |
|---|---|
| ☐ | Coverage — gaps where a camera stopped or a run was not colorized |
| ☐ | Exposure — blown highlights, blocked shadows. Both unrecoverable |
| ☐ | Motion blur |
| ☐ | Obstruction — aerials, following vehicle, smear on the dome |
| ☐ | Focus and contamination |
| ☐ | **Corrupted images — silent, export as black** |
| ☐ | Alignment with the point cloud at feature edges |

## C3 · Before you call it done

| ☐ | |
|---|---|
| ☐ | **As Check residuals exist and are recorded** |
| ☐ | No layer was skipped |
| ☐ | Layers 6 and 7 were written down — **nothing else records them** |
| ☐ | Nothing is being accepted on RMS alone |
| ☐ | **No acceptance tolerance has been invented or quoted** — D-13 is open |

---

# Appendix D — Export and Delivery Checklist

## D1 · The gate

| ☐ | | § |
|---|---|---|
| ☐ | QC complete, all eight layers | 32 |
| ☐ | Accepted by the person with the authority — **not by you** | 32 |
| ☐ | **Scan nodes sit beneath the intended registered trajectory** | 31 |
| ☐ | **Stations carry `_reg_####`** | 31 |
| ☐ | Tree screen-captured | 31 |
| ☐ | **Export timestamps setting decided and recorded** | 31 |

## D2 · The export

| ☐ | | § |
|---|---|---|
| ☐ | Path chosen, and it carries what the client needs | 30 |
| ☐ | Grid or ground per the written agreement | 30 |
| ☐ | If ground: **the scale factor is communicated separately** — the file does not carry it | 30 |
| ☐ | If Trajectory Split: **Extract Classified Point Cloud run first** | 30 |
| ☐ | If Trajectory Split: **Sample points checked** — it randomly thins | 30 |
| ☐ | If TopoDot: scans generated, **all run views closed** | 30 |
| ☐ | If Point Cloud tab: the selection does not cross two trajectories | 30 |

## D3 · What goes with it

| ☐ | | § |
|---|---|---|
| ☐ | **Delivery record** — mission ID, trajectory node, SBET filename with `_reg_####`, registration type, export path, date, by whom | 28 |
| ☐ | Coordinate system, datum and epoch stated in the delivery, not only in the file | 30 |
| ☐ | Accuracy statement, where accuracy is relied on | 32 |
| ☐ | Control-and-check table, where the client receives the evidence | 20 |

## D4 · After

| ☐ | |
|---|---|
| ☐ | What was delivered, to whom, when, in what format and scaling — recorded |
| ☐ | The delivered files retained per the retention tier |

---

# Appendix E — Archive and Cleanup Checklist

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*

## E1 · The archive-first sequence

**In this order.** Do not reorder it.

| ☐ | # | Step | § |
|---|---|---|---|
| ☐ | 1 | QC complete and **accepted** | 32 |
| ☐ | 2 | **Mission Report run and archived** — before Cleanup, or it can only report survivors | 29 |
| ☐ | 3 | Registration evidence recorded — designation and residuals | 20 |
| ☐ | 4 | **`Targets.csv` archived** | 29 |
| ☐ | 5 | **Numbered SBET files archived** — `sbet_<date>_reg_####.out` | 29 |
| ☐ | 6 | Calibration JSON archived | 13 |
| ☐ | 7 | **Project backup taken into the project archive** — not a local copy | 29 |
| ☐ | 8 | **Written authorisation obtained** | 29 |
| ☐ | 9 | Cleanup run | 29 |
| ☐ | 10 | Recorded — by whom, on what date, what was archived first | 29 |

## E2 · Archive

| ☐ | | § |
|---|---|---|
| ☐ | **Tier 1** complete — a few hundred kB, keep indefinitely | 33 |
| ☐ | **Tier 2** stored with the retention period noted | 33 |
| ☐ | **Tier 3** decision applied and recorded — raw mission folder and TBC project | 33 |
| ☐ | **`POS_1/raw/` and `Targets.csv` not deleted by an individual acting alone** | 33 |
| ☐ | **Archive record written** — one page | 33 |

## E3 · Tier 1, itemised

| ☐ | |
|---|---|
| ☐ | Field record |
| ☐ | Control-and-check table with residuals |
| ☐ | Mission Report, run before Cleanup |
| ☐ | Calibration JSON in force |
| ☐ | Results of Scan Generation |
| ☐ | Delivery record |
| ☐ | QA/QC record |
| ☐ | Accuracy statement issued |

---

# Appendix F — Record Templates

Five templates for the records that **have no software artefact**. Each is small. Each is
unrecoverable if it is not written at the time.

---

## F1 · Control and check table

**The single most important record in the workflow**, and TBC does not produce it (§20).

| Project | | Mission | | Registration name | |
|---|---|---|---|---|---|
| Designated by | | Date designated | | Registered by | |

| Point ID | Use XY | Use Z | As Check | Residual E | Residual N | Residual Elev | Notes |
|---|---|---|---|---|---|---|---|
| | ☐ | ☐ | ☐ | | | | |
| | ☐ | ☐ | ☐ | | | | |
| | ☐ | ☐ | ☐ | | | | |

> **Designation is fixed before registration and is not changed during it** (§15, SOP §7.3). If it
> changes, the Project Surveyor decides, it is recorded here with a date, and the registration is
> recomputed using **Edit** — not layered on top.

---

## F2 · Delivery record

One page per delivered dataset.

| | |
|---|---|
| Project | |
| Mission ID | |
| **Trajectory node name** | |
| **SBET filename, including `_reg_####`** | |
| Registration type | Global · Local · Global then Local · Run to Run |
| Update Scans confirmed | ☐ stations carry `_reg_####` |
| Export path | |
| **Export timestamps** | ☐ No ☐ Yes — *if Yes, state the recorded reason* |
| Scaling | ☐ Grid ☐ Ground ☐ ECEF · scale factor communicated: ☐ |
| Coordinate system, datum, epoch | |
| Export date | | 
| Exported by | |
| Delivered to | |

---

## F3 · QA/QC record

| Layer | Performed by | Date | Extent covered | Result |
|---|---|---|---|---|
| 1 Field coverage verification | | | | |
| 2 Intake checks | | | | |
| 3 Trajectory RMS review | | | | |
| 4 Residuals on control | | | | |
| 5 **Residuals on independent checks** | | | | |
| 6 **Visual inspection** | | | | |
| 7 **Imagery inspection** | | | | |
| 8 Export-state confirmation | | | | |

| | |
|---|---|
| Accuracy requirement assessed against | |
| Accepted by | |
| Acceptance date | |

> **Acceptance is not the processor's.** It is a decision by the person with the authority under
> SOP §4, against the requirement stated at project setup.

---

## F4 · Cleanup authorisation and archive-first record

| | |
|---|---|
| Project · Mission | |
| **Authorised by** | |
| Authorisation date | |
| Mission Report archived | ☐ · location: |
| Registration evidence recorded | ☐ |
| `Targets.csv` archived | ☐ · location: |
| Numbered SBET files archived | ☐ · location: |
| Calibration JSON archived | ☐ · location: |
| Project backup taken | ☐ · location: |
| **Cleanup run by** | |
| **Date run** | |

---

## F5 · Archive record

One page per project.

| | |
|---|---|
| Project | |
| Archived by · date | |
| What was archived | |
| Where it is | |
| **Retention tier applied** | ☐ Tier 1 ☐ Tier 2 ☐ Tier 3 |
| Retention period runs from | |
| Cleanup run? | ☐ No ☐ Yes — see F4 |
| **Where the raw mission data is**, if held elsewhere | |
| Disposal, if any — what, when, authorised by | |

> **Without this, the archive is a folder somebody has to reverse-engineer.**
