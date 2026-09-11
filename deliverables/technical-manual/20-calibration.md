# 20. Calibration

## 20.1 Why this section sits here

Calibration is **periodic, not per-project.** It belongs to the system, not to the job, and most
missions will not involve it at all.

It appears here, between scan generation and registration, for two reasons: TBC's calibration
procedures **consume generated scans** as their input, so it cannot be explained before §18; and
a reader meeting registration in §21 needs to already know what a boresight angle is.

> **Calibration and registration are different things and are easy to confuse.** Calibration
> determines the fixed angular relationship **between sensors on the vehicle**, and is valid for
> months. Registration ties a **particular mission's trajectory** to surveyed control, and is
> valid for that mission only. A current calibration does not reduce the control requirement, and
> a good registration does not indicate the calibration is sound.

## 20.2 What is calibrated, and what is not

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886, 24868)*
>
> "A system calibration describes the estimation of the exact translation and orientation of each
> sensor referring to an internal virtual reference point of the sensor head. For a Trimble MX
> series mobile mapping system, each sensor has its individual set of:
>
> - **Lever arms** (offsets in translation — X, Y and Z): X-axis in the driving direction to the
>   front, Y-axis in the driving direction to the right, Z-axis in the down direction
> - **Boresight angles** (offsets in orientation around the X, Y and Z axes, respectively Roll,
>   Pitch and Heading)"
>
> And the key sentence:
>
> **"In a calibration process, the offsets in translation are known for all sensors and do not
> need to be estimated while the offsets in rotation need to be."**

> **Calibration estimates angles only.** Lever arms are fixed by manufacture and are known. That
> is why a calibration can be computed from scan agreement without any surveyed control — the
> unknowns are three rotations per sensor, and they show up as systematic disagreement between
> overlapping scans.

### Why boresight error is the error that grows with range

An error in the boresight angle of a scanner is an error in **which direction it thinks it is
pointing**, and it displaces points **in proportion to range** — exactly as described in §3.

> That proportionality is geometry, not a system specification. Multiplying any small angular
> error by any distance gives the lateral displacement at that distance, and the arithmetic is
> the reader's to do for the ranges and tolerances of a particular job. **No Trimble source in the
> set states a boresight error budget for the MX60**, and none is asserted here.

> **WHY THIS MATTERS**
>
> Boresight error is systematic, not random. It does not average out with more data — collecting
> twice as much produces twice as much consistently displaced cloud. And because it scales with
> range, it appears as a dataset that is excellent near the vehicle and progressively wrong
> further out, which reads as "the scanner is noisy at range" rather than as a calibration
> problem.

## 20.3 Calibrating the laser scanners

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886; also documented at TBC 20716)*

### Where it runs

"In TBC, up to the 5.21 version, laser scanners are calibrated out of the application and the
calibration values are imported into TBC from a JSON format file. The **Calibrate Laser
Scanners** feature allows you to calibrate the laser scanners of the MX series mobile mapping
systems in TBC."

> Version 5.21 predates 5.70, the oldest release Trimble still publishes notes for (§10.2). **Any
> recent TBC calibrates in the application.** The JSON import path (§20.5) remains available and
> is how a calibration moves between projects.

### The acquisition geometry

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886 / 20716)*
>
> The mission must contain **four runs: two in one direction (forward and backward), and two
> orthogonal (forward and backward as well)** — in practice, two roads crossing.
>
> | Run | Direction |
> |---|---|
> | Run_0 / Run_1 | Along the first road, forward and backward |
> | Run_2 / Run_3 | Along the crossing road, forward and backward |
>
> **Site requirements:**
>
> | Requirement | Value |
> |---|---|
> | **Crossing angle** | As close to **90°** as possible, tolerance **± 30°** |
> | **Minimum run length** | **At least 20 m from each side** of the crossing |
> | **Ideal run length** | **80 m long — 40 m from each side** of the crossing, "for an efficient calibration" |
> | **Overlap** | Enough overlap between runs |
> | **Façades** | Present **in each direction**, in sufficient quantity |
> | **Vegetation** | A few or none, ideally |

> **WHY THIS MATTERS**
>
> **Façades are the measurement.** A boresight error shows up as the same flat vertical surface
> appearing in two places when scanned from opposing directions. No façades, no signal.
> **Vegetation is the opposite** — soft, non-repeating returns that add noise to exactly the
> run-to-run comparison the calibration depends on.

Compare with the LiDAR QC pattern *(TBC 28972; §11)*:

| | Laser scanner calibration *(TBC 24886)* | LiDAR QC *(TBC 28972)* |
|---|---|---|
| Runs | Four — two orthogonal pairs, both directions | Four — two perpendicular strips, both directions |
| Crossing angle | **90°, ± 30°** | Perpendicular |
| Length | **≥ 20 m each side; ideally 80 m total** | **250–300 m per strip** |
| Scene | **Façades in each direction; little or no vegetation** | Structured — "a residential area with detached houses and objects within the LiDAR sensor's maximum range" |
| Sky | Not stated | **Open sky for good GNSS satellite visibility** |

> **The two are compatible, and LiDAR QC is the stricter on length.** A site of two roads crossing
> near 90°, with 125–150 m of façade-lined street available on each arm, satisfies both.
>
> ⚠ **One assumption is being made and should be stated.** Trimble specifies the laser scanner
> pattern as two roads **crossing**, and specifies the LiDAR QC pattern as two **perpendicular
> strips** without saying the strips intersect. Treating a LiDAR QC strip as centred on the
> crossing — and therefore needing half its length on each arm — is this document's reading, not
> Trimble's statement. It is the conservative reading: a site meeting it also meets any
> non-intersecting arrangement of the same total length.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §15** (D-24); it is not decided here.

### The result, and how to read it

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886)*
>
> The calibration reports:
>
> - **Overall Overlap** — the percentage of points used against those generated
> - **Overall RMS** — the average of the RMS between the scans used
> - **Per-pair RMS**, in **Tangential, Orthogonal and Vertical**

The same three-axis convention as run-to-run registration (§21.15), and it diagnoses the same way:
a large tangential component points at along-track scale or timing, a large orthogonal component
at heading, a large vertical component at pitch or height.

### The rule that governs acceptance

> **TRIMBLE DOCUMENTED METHOD**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886)*

> **This is the origin of the principle that governs §21, §23 and §25**, and of the QC
> requirements in the **SOP §16**. Trimble states it here and repeats it verbatim in the
> run-to-run registration topic. It is not a hedge — it
> follows from what a residual measures. **A number can prove failure. A number cannot prove
> success.**

### The visual check

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886)*
>
> Check **Cutting Plane View**. A plane named **Mobile Mapping Cutting Plane** is created, visible
> as a yellow plane in 3D View at the beginning of the first run pair (`Run_0 <-> Run_1`).
>
> - Change rendering to **Scan Color** — one colour per scan
> - Increase **Point Size**
> - Adjust **cutting plane thickness**
> - Drag the slider along the run pair, looking at the gap between the two clouds
> - Then **choose `Run_2 <-> Run_3` in the Calibrate Laser Scanners dialog and check that pair
>   too**
>
> Only then **Apply**.

> **IMPORTANT**
>
> **Both run pairs must be checked.** The dialog presents one pair at a time and the second is
> easy to skip. The orthogonal pair is the one that constrains heading — the component a single
> direction of travel cannot resolve.

> **FIELD TESTING REQUIRED · T16**
>
> Cutting plane thickness: Trimble's screenshots show `0.030` in the calibration topic and `5.000`
> in the run-to-run topic, with no stated basis. Too thin shows nothing; too thick buries a real
> offset in a band of points. *(Appendix E)*

## 20.4 Calibrating the cameras

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24868, 20728)*

The camera frames on an MX-series vehicle are the **360° camera frame**, the **vehicle frame**,
the **oblique camera frame (1/2)** and the **down-looking camera frame**.

As with the scanners, "up to the 5.21 version, cameras are calibrated out of the application and
the calibration values are imported into TBC from a JSON format file. The **Manual Camera
Calibration** feature allows you to calibrate the cameras of the MX series mobile mapping systems
in TBC **by entering the calibration values directly**."

### The procedure

1. Create a VCE project, import the `.mxdb`, apply the SBET
2. **Generate scans from at least one run**
3. In Project Explorer select a camera under **Capture Devices**
4. **Manual Camera Calibration** from the context menu
5. Pick a position on a run's trajectory in Plan View. The camera view displays at that location
6. Enter a value in **Heading**, **Pitch** or **Roll** and press Enter — **the camera view updates
   immediately**

| Input | Step |
|---|---|
| Arrow up / down | ± 0.001° |
| Ctrl + arrow, Page Up / Page Down | ± 0.01° |
| Mouse wheel | ± 0.001° |
| Ctrl + mouse wheel | ± 0.01° |

> **This is a visual, iterative alignment, not a computed adjustment.** The operator nudges the
> orientation until the imagery lines up with the point cloud, watching it move. It is closer to
> collimating an instrument than to running a least-squares solution — and like collimation, the
> quality depends on the care taken and is not captured by any residual.

### Where the values end up

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24868)*
>
> In the camera properties, as **Boresight refinement** — distinct from **Boresight
> installation**, which is the as-built value. Lever arm installation and lever arm refinement
> appear alongside, and are equal, because lever arms are not estimated (§20.2).

## 20.5 The calibration file

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22920)*
>
> "In TBC, a **JSON** format file contains the parameters **before** calibration (**Installation
> Matrix**) and the parameters **after** calibration (**Refinement Matrix**), of **each sensor** of
> the mobile mapping system."
>
> - **Import Calibration** — mission node context menu. Applies refined parameters to the project
> - **Export Calibration** — mission node context menu. Writes the refined parameters computed in
>   TBC

The MX60 also accepts a boresight JSON in the field through TMI's **Calibration Import**, via USB1
*(TMI UG Rev L, p.18)*.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §15** (D-55); it is not decided here.

## 20.6 The calibration record — and the date

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24868)*
>
> The **Mission Report** contains a **Capture devices** table carrying, per sensor:
>
> | Column |
> |---|
> | Boresight installation |
> | **Boresight calibration** |
> | Lever arm installation |
> | Lever arm calibration |
> | **Date of calibration** |

> **This is the only record found anywhere in the workflow that states when the system was last
> calibrated, and it is attached to the mission rather than to the system.** Every mission carries
> a statement of the calibration state it was processed under. That is a genuinely useful audit
> property and it costs one report to capture (§30).

## 20.7 When to recalibrate

> **Open Parametrix decision — D-26, D-3.** *On what interval, and after what events, is the MX60 recalibrated?* Stated and tracked in the **SOP §15**; see also the master register.

> **VENDOR CLARIFICATION REQUIRED · V-13**
>
> **Does removing and refitting the Sensor Unit disturb the calibration?** And what symptoms
> indicate a calibration has drifted? *(Appendix E)*

## 20.8 Calibration is not validated by control

A warning against a natural but wrong inference.

TBC's laser scanner calibration derives boresight angles from **scan-to-scan agreement**. No
surveyed control participates. A calibration can therefore be internally excellent and carry a
systematic error common to all four runs.

The independent check on calibration is the periodic target verification in §31 — retro-
reflective targets previously surveyed by total station — which is a different activity with a
different geometry, and one Parametrix has not yet scheduled.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We worked out the exact angles at which each sensor is bolted to the
> vehicle relative to the inertial unit. Not where they are — those distances are known from
> manufacture — but which way they point, to a hundredth of a degree. For the scanners TBC solves
> it by driving a specific four-run pattern and making the overlapping clouds agree. For the
> cameras the operator nudges the orientation by hand and watches the image line up with the
> points.
>
> **Why it matters.** A boresight error is an aiming error, and aiming errors get worse with
> distance. A hundredth of a degree is nothing at the kerb beside the vehicle and over a
> centimetre at a building face 60 m away — on every point, always in the same direction. It does
> not look like noise and it does not average out. It looks like a dataset that is crisp up close
> and untrustworthy further out.
>
> **What can go wrong.** The big one is believing the numbers. TBC reports an overall RMS and
> per-pair residuals, and Trimble says plainly — twice, in two different topics — that good
> numbers do not prove the calibration worked, though bad numbers prove it failed. You have to
> look. And you have to look at **both** run pairs: the dialog shows one at a time, and the
> orthogonal pair is the one that pins down heading, which driving in a single direction cannot
> resolve at all.
>
> The other failure is confusing this with registration. A current calibration does not reduce
> your control requirement by one point. It is the difference between an instrument that is
> properly collimated and an instrument that is properly oriented on a known station — you need
> both, and one does not substitute for the other.
>
> **What good looks like.** Drag the cutting plane along the run pair and see one wall, not two —
> on both pairs. Residuals of similar size in all three directions, rather than one much larger
> than the others, which would be telling you something specific about which axis is off. And the
> whole thing recorded: export the JSON, keep it with the serial number and the date, and know
> that every mission report afterwards will say which calibration it was processed under.
