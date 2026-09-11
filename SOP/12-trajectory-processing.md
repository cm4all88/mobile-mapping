# 12. Trajectory Processing

This is where the accuracy of the whole dataset is decided. Everything after it either applies
the trajectory or improves it — nothing else creates it.

## 12.1 The three routes, and the licence that chooses between them

| Route | Where it runs | Requires |
|---|---|---|
| **POSPac MMS, externally** | A workstation with POSPac | A POSPac licence |
| **Process Raw Trajectory Data, inside TBC** | TBC | **POSPac MMS 8.6+ installed alongside TBC, with a valid licence** *(TBC 25943)* |
| **Real-time NAV** | Already computed in the vehicle | Nothing — but see §11.2 |

> **Both post-processing routes require POSPac.** TBC's in-application command is a convenience
> wrapper, not an alternative to owning the software. There is no route to a survey-grade
> trajectory that does not involve a POSPac licence somewhere.

> **PARAMETRIX DECISION REQUIRED**
>
> **Where does trajectory processing happen, and who does it?** See §4.4. Without a licence the
> answer is "somewhere else," and the project schedule has a dependency in it that should be
> visible at quoting time rather than at processing time. *(Register item 10)*

## 12.2 What Process Raw Trajectory Data does

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> "The feature enables you to compute a Smoothed Best Estimate of Trajectory (SBET) within TBC
> using the raw inertial, GNSS satellites, and base station data, without having to use the
> Applanix's POSPac MMS application and to import the trajectory into TBC."

Run from the **Mission** node context menu. TBC loads the raw POS data automatically.

### Inputs

| Input | Where it comes from | Notes |
|---|---|---|
| **Raw POS data** | `POS_1/raw/` — `posl_*.000`, `.001`, `.002` … | Selected automatically. "TBC will sequentially process the entire series of valid POS logged data files starting from the first file selected" |
| **Base station RINEX** | `Base/` — the `.YYo` observation file | **Must be imported into TBC before running the command** |

> **CAUTION**
>
> **Import the observation file only.** The `Base/` folder also contains `.YYn` and `.YYg`
> ephemeris files. Trimble states: **"Do not import the ephemeris files into TBC."**
> *(TBC 25943)*

## 12.3 Settings — with Trimble's stated defaults

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> "TBC automatically fills the below fields with the information found in the POS logged files,
> like GNSS/Inertial/DMI Sensors Lever Arms and GAMS Baselines settings which are set in the
> vehicle before the data collection. **Double check the settings values and if needed modify
> them.**"

### Computation Mode

| Mode | What it uses |
|---|---|
| **IN-Fusion+ Single Base** | "high-accuracy GNSS positioning using corrections from a nearby local base station" |
| **IN-Fusion+ PP-RTX** | "high-accuracy GNSS positioning globally using Trimble's satellite or internet-based RTX corrections, **without the need for a local base station**" |

No default is stated.

> **PARAMETRIX DECISION REQUIRED**
>
> **Single Base or PP-RTX, and on what basis?** This is a survey decision with real consequences
> — it determines whether a base station must be occupied for every mission, and it determines
> the reference frame the solution is computed in.
>
> It interacts with §12.6: a PP-RTX solution is computed in Trimble's RTX frame and epoch, which
> is not necessarily the project's. *(Register item 19)*

### The rest

| Setting | Values | Default |
|---|---|---|
| **Time Start / Time End** | GPS seconds of the start week | — |
| **Initialization Mode** | VNAV · **Gyro-compassing** · GAMS · GAMS and Gyro-Compassing | **Gyro-compassing** |
| **Multipath** | Low (good coverage) · **Medium** · High (urban canyon, narrow streets, dense foliage) | **Medium** |
| **Antenna Manufacturer / Type** | Read from the RINEX automatically | — |
| **GAMS** | On/off, with a lever arm and a standard deviation | Dimmed if GAMS was disabled during acquisition |
| **DMI** | Lever arm, standard deviation, scale factor, scale factor SD | Dimmed if DMI was disabled during acquisition |
| **LiDAR QC (Refine with scans)** | On/off | Off — see §12.7 |
| **Generate QC Report** | On/off | — |

### The MX60 antenna model — check this one

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "the rover antenna model should be **Tallysman/33-3970 GNSS** for an MX9 (or MX50) system and
> **Trimble 112735 GNSS for a MX90 (or MX60) system**." *(TBC 25943)*

> **IMPORTANT**
>
> This is retrieved automatically from the RINEX file, which means it can be retrieved *wrongly*
> if the RINEX carries a different antenna descriptor. **Verify it reads Trimble 112735 before
> computing.** An incorrect antenna model puts a systematic vertical bias into the trajectory that
> nothing downstream will reveal — registration will absorb part of it, and the rest will appear
> as a height offset that looks like a geoid problem.

### DMI settings, if fitted

| Setting | Trimble's statement |
|---|---|
| **Scale factor sign** | "DMI installed on the **left** side of the vehicle: scale factor is **positive**… **right** side: scale factor is **negative**" |
| **Scale factor value** | From "the Trimble MX Distance Measuring Indicator Installation & Operation Manual, in the DMI Scale Factor section" — **a manual Parametrix does not hold** (§4.7) |
| **Scale factor SD** | **Default 5 %.** "Increase the setting if the scale factor is not known with 5% accuracy, and **set it to 100% if it is not known at all**" |

> **FIELD TESTING REQUIRED · T12**
>
> **The 5 % default is only correct if the wheel diameter was actually measured.** If the value
> came out of a manual for a nominal tyre, 5 % is an assertion of accuracy nobody verified, and
> the solution is weighting the DMI accordingly.
>
> Trimble provides the honest escape hatch — set it to 100 % if unknown. Determine which case
> applies before trusting the default. *(Appendix E)*

### Multipath

> **FIELD TESTING REQUIRED · T11**
>
> **Medium is the default and is described as being for degraded coverage.** Trimble's own
> descriptions place Low with "good GNSS coverage" and Medium/High with "a degraded GNSS
> coverage, such as in urban canyon, narrow streets, dense foliage."
>
> Running Medium on an open-sky rural corridor may be a harmless conservatism or an unnecessary
> de-weighting of good observations. Untested. *(Appendix E)*

### Lever arms and the vehicle frame

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "**Lever Arm** refers to the displacement between two body coordinate frames… expressed as a
> three-dimensional vector."
>
> Measured in the vehicle frame, from the external reference point to the DMI wheel contact patch
> or the GAMS antenna phase centre, in metres along three axes:
>
> - **Positive X = forward driving direction**
> - **Positive Y = right side of the vehicle**
> - **Positive Z = downward**
>
> *(TBC 25943)*

> **The same convention governs every boresight angle in §14.** Roll about X, pitch about Y,
> heading about Z, with Z pointing down. It is worth fixing in mind once.

## 12.4 Outputs, and a filename that means something

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> | Condition | Output filename |
> |---|---|
> | Datum and epoch **known** by POSPac | `sbet_[mission name].out` |
> | Datum and epoch **unknown** by POSPac | `sbet_[mission name]_[frame].out` — "created, **first in ITRF00 and then in the datum and epoch of the project**" |

> **IMPORTANT · this is the trap in this section**
>
> **The second filename is a warning, and nothing else flags it.**
>
> It means POSPac did not recognise the project's coordinate system, computed the solution in
> ITRF00, and then transformed it. That transformation is an extra step with its own assumptions
> about the frame and the epoch — and the only indication you will ever get is a longer filename.
>
> **Look at the SBET filename after every computation.**

> **FIELD TESTING REQUIRED · T10**
>
> Establish which of Parametrix's normal coordinate systems POSPac recognises directly, and which
> trigger the ITRF00 path. This is answerable once and then known. *(Appendix E; §5)*

### Where the outputs go

| Output | Location |
|---|---|
| SBET | `NAVPROC/Export/` under the project folder |
| Processing report | `NAVPROC/Report/` |
| **Backup SBET Next to MXDB** *(option)* | Copies the SBET **and a log containing the frame and epoch information used to create it** into the raw data folder beside the `.mxdb` |

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Enable Backup SBET Next to MXDB.** That log is the only artefact found anywhere in the
> workflow that records the frame and epoch a trajectory was computed in, and it lives with the
> raw data rather than inside a TBC project that may later be cleaned up (§21) or lost.
>
> **Not adopted.** *(Register item 20; §23, §25)*

### The SBET is coloured by its own quality

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "The created SBET trajectory file will be **colored according to the values of the computed
> RMS**." *(TBC 25943)*
>
> The RMS comes from `smrmsg_xxx.out`, a file POSPac produces that "describes the accuracy of the
> post-processed solution and contains the position, orientation and velocity RMS after
> smoothing" *(TBC 27248)*.

Colour settings are at **Mobile Mapping ▸ Trajectory Settings**, where **Rendering Settings** can
be set to **Default** (a flat colour — red for real-time, green for processed) or to **RMS
values**, with user-defined ranges and colours. Settings are persistent.

> **This is the single most useful QC view in the entire workflow and it costs nothing.**
>
> Switch the trajectory to RMS colouring and look at the corridor. The stretches where the
> solution struggled are drawn in a different colour, in plan, before any point cloud exists.
> That tells you where to concentrate control (§17), where to expect trouble at registration, and
> whether a degraded-GNSS remedy (§20) is going to be needed — while there is still time to do
> something about it.

> **OBSERVED SOFTWARE BEHAVIOR**
>
> "If the mission contains some registrations then the **modified segments will be colorized with
> the 'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
> `smrmsg` file, so the adjusted stretches lose their RMS colouring. Incidentally, this makes the
> extent of a registration's effect visible in plan — which is one way to see where a **Local**
> adjustment stopped adjusting (§15.5).

## 12.5 Trajectory Plots

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 27415)*
>
> "After computing a SBET with the Process Raw Trajectory Data command, the resulting plots open
> **only once**. The **Trajectory Plots** feature lets you open the plots without running again
> the command."

At **Mobile Mapping ▸ Reports ▸ Trajectory Plots**, or the command `MissionTrajectoryPlots`. It
is greyed out until an SBET has been computed, and opens plots per mission where several exist.

> **FIELD TIP**
>
> The plots open once and then vanish, which is why people think they are gone. They are not —
> but a processor who does not know this command exists will re-run a multi-hour computation to
> get them back.

## 12.6 Datum and epoch

§5 covers the coordinate system decisions. Two things belong here because they are specific to
trajectory processing.

**The ITRF00 path (§12.4)** is the practical expression of an epoch mismatch, and the filename is
its only symptom.

**Dynamic datum epoch selection**, added in TBC 2026.10:

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "When working with a time-dependent datum, you can now work at a specific epoch that is not the
> default reference epoch for the selected datum… **Note that this feature is intended for
> experienced users, as incorrect settings may lead to inaccurate results.**" *(TBC RN 2026.10)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Which datum and epoch does Parametrix work in for mobile mapping, and who sets it?**
>
> Trimble itself flags the epoch control as capable of producing inaccurate results if set wrongly.
> Combined with the ITRF00 path above, epoch handling is not an abstract datum concern in this
> workflow — it is a live setting with a silent failure mode. *(Register item 21; §5)*

## 12.7 LiDAR QC — refining the trajectory with the scan data

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 28972)*
>
> "LiDAR QC is an advanced trajectory processing technology that, **similar to LiDAR SLAM**, is
> using scan data as an aiding sensor to improve georeferencing accuracies in areas of poor GNSS
> coverage or in areas where overlapping scans are not perfectly matching. Based on a robust and
> iterative least square adjustment, LiDAR QC generates 3D Voxels that are matched in overlap
> scan regions. The result of this iterative process is solving the constant IMU boresight angles
> and making corrections to the post-processed trajectory (position and orientation)."

Enabled by the **LiDAR QC (Refine with scans)** checkbox in Process Raw Trajectory Data, which
adds a LiDAR QC tab. Requires **MATLAB Runtime R2024b (24.2)** and a substantial workstation
(§4.5).

### Settings

| Setting | Values | Default |
|---|---|---|
| **Range** | Minimum and maximum LiDAR measurement distance used | **3 m to 100 m** |
| **Noise** | 5, 10, 50, 80, 100, 200 mm | **5 mm for MX50/MX60**; 10 mm for MX9/MX90 |
| **Lasers** | Left · Right · All | **All** |

> **FIELD TESTING REQUIRED · T13, T14**
>
> **T13 — the 3–100 m range.** The MX60's useful range and the range over which scan geometry
> usefully aids a trajectory solution are different questions. 100 m may include returns too noisy
> to help.
>
> **T14 — Lasers = All.** Trimble's own text beside the setting says using both "can increase
> computation time without significantly improving the accuracy, as it compares the left versus
> right laser of isolated runs." **The default contradicts the guidance printed next to it.**
> *(Appendix E)*

### Running it

Select runs from the Project Tree **with overlap — parallel runs, or crossing runs** — click
**Add**, set the parameters, **Compute** *(TBC 28972)*.

### The calibration pattern

Trimble prescribes a specific acquisition geometry for LiDAR QC:

| Element | Requirement |
|---|---|
| **Area** | "a structured scene such as a residential area with detached houses and objects within the LiDAR sensor's maximum range"; "open sky terrain for good GNSS satellite visibility" |
| **Strips** | "two perpendicular strips. **Each strip will consist of two runs (one in each direction)**" |
| **Strip length** | **250–300 m** |

*(TBC 28972)*

> This is materially the same geometry the laser scanner calibration requires (§14.3) — four runs,
> two orthogonal pairs, both directions. **One site can serve both**, which matters because
> establishing a calibration site is a real piece of work (§6).

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We took the raw GNSS and inertial observations the vehicle recorded,
> combined them with base station data, and computed the path the sensor head actually followed —
> forward through time, backward through time, and merged. That path is the SBET, and every point
> in the finished cloud will be hung off it.
>
> **Why it matters.** This is the step that sets the accuracy ceiling for the job. Nothing later
> improves the raw measurements; registration bends the path to fit control, but it cannot invent
> information that was never collected. A trajectory computed from good observations, with the
> right antenna model and a sensible base station, is a dataset you can work with. One computed
> from a weak solution is a dataset you will fight for the rest of the project.
>
> **What can go wrong.** Three things, and all three are silent. The antenna model is read
> automatically from the RINEX and can be read wrongly — the MX60 wants **Trimble 112735**, and a
> wrong entry puts a height bias into everything that no later check will attribute to its real
> cause. The output filename quietly tells you whether POSPac understood your coordinate system:
> `sbet_mission.out` means yes, `sbet_mission_frame.out` means it worked in ITRF00 and then
> transformed, and nothing else will mention it. And the DMI's 5 % default accuracy is only true
> if somebody actually measured the wheel.
>
> **What good looks like.** After the computation, switch the trajectory to RMS colouring and look
> at it in plan. A good job is mostly one colour, with the degraded stretches where you expected
> them — under the overpass, through the tree cover — and short. That picture, available before
> any point cloud exists, tells you where to put control, where registration will struggle, and
> whether you are going to need one of the remedies in §20. It is five seconds of work and it is
> the best early warning the software gives you.
