# APPENDIX C — GLOSSARY

Plain English first, technical detail second where it helps.

---

**Attitude**
Which way the sensor is pointing — roll, pitch and heading together.
*Attitude error rotates the point cloud, and the resulting position error grows with
range. This is why accuracy degrades away from the vehicle.*

**Boresight / boresight calibration**
The small angular misalignment between the scanner and the inertial system, and the
process of measuring it.
*Determined by office processing and saved to a JSON file, which must be imported back
into the system via USB1 before it takes effect (TMI UG Rev L, pp.18, 20). TMR requires
calibration before and after every project (§6, p.7).*

**Capture Preset**
A saved set of sensor settings — laser mode, camera triggers, dust filter, user
accuracies. Can be changed mid-mission.

**Check point**
A surveyed point used to **verify** the data. Held out of the adjustment entirely.
*A point used to register the cloud cannot verify it — it will fit because you made it
fit.*

**Clearly Defined Point**
A feature identifiable with confidence in both the point cloud and by conventional survey
— concrete corners, pole centres, line-marking ends, guardrail posts *(TMR App F)*.

**Colorization**
Assigning RGB values to points from the imagery, so the cloud looks photographic.
*Alternative to intensity colouring, which is more common for engineering use.*

**Control point**
A surveyed point used to **improve** the solution, by registering or adjusting the cloud
to it.

**DMI — Distance Measuring Indicator**
A wheel odometer. Improves accuracy in poor GNSS and stop-and-go traffic.
*Supplies ZUPT information for post-processing. Must be on a non-steering wheel; lever arm
measured to the centre of the tread (MX60 UG Rev B, p.46).*

**Dust filter**
A TMI setting that discards points inside a box around the vehicle, to avoid recording
dust clouds.
*For unpaved roads and open pit mines only — not paved roads or urban canyons. Depends
entirely on installation height being correct (Dust Filter Bulletin, pp.1–2).*

**Exchangeable Data Disk / SSD**
The two removable 4 TB drives in the Control Unit.
*SSD 1: navigation, both lasers, panoramic camera, mission database, logs. SSD 2:
back-down camera. Both are needed for a complete mission.*

**External Reference Point (ERP)**
The physical origin for all mounting measurements — right side, at the back of the rack.
*Installation height and every lever arm are measured from here (MX60 UG Rev B, p.45).*

**GAMS — GNSS Azimuth Measurement System**
A second GNSS antenna that lets the system derive heading from the baseline between
antennas.
*Speeds initialization and eliminates the need for special driving manoeuvres (MX60 UG
Rev B, p.67). Post-processing requires millimetre-level offsets and a ≥2.0 m baseline.*

**GNSS outage**
Any period where satellite signals are unusable — tunnel, underpass, canyon, canopy.
*The IMU bridges the gap. Trimble publishes performance at 60 seconds and nothing beyond.*

**Heading**
Which compass direction the vehicle is pointing.
*The hardest attitude component. Roll and pitch are observable at rest because gravity
gives an absolute reference; heading has none and must be inferred from motion — or
measured directly by GAMS.*

**IMU — Inertial Measurement Unit**
Senses rotation and acceleration hundreds of times a second.
*Fast and immune to sky blockage, but drifts. Complementary to GNSS, which is stable but
slow and easily blocked.*

**Initialization**
The manoeuvres at the start of a mission that let the navigation solution converge.
*Static period, straight run, then speed changes and turns. The dynamics make attitude and
sensor-bias errors observable — see §8.4.*

**Install Height**
Vertical distance from the External Reference Point to the road surface.
*The one measurement required for a standard system. Must be accurate to ~1 cm. Wrong
values produce faulty navigation solutions and break the dust filter.*

**Intensity**
The strength of the returned laser pulse, recorded per point.
*Gives the greyscale "photographic" look of an uncoloured cloud. TMR requires delivery
normalised to 16-bit, 0–65535 (§9.2.2, p.11).*

**Lateral Range Limit**
A TMI setting that discards points beyond a set distance perpendicular to travel, 5–50 m.
*A data-volume tool. Discarded points are gone permanently.*

**Lever arm**
The three-dimensional offset from the External Reference Point to another sensor.
*Measured in the Vehicle Frame: +X forward, +Y right, **+Z down**. Required only for GAMS
and DMI — standard system lever arms are set by default (QSG Rev B, p.7).*

**Mission**
One continuous session from start to Complete Mission. Contains one or more runs.
*Navigation logs continuously for the whole mission. Minimum 30 minutes.*

**Mission re-configuration**
Changing capture settings mid-mission without closing it.
*Navigation logging continues, so no new initialization is needed (TMI UG Rev L, p.41).*

**Multipath**
GNSS signals arriving after bouncing off buildings, implying a wrong position.
*More dangerous than a clean outage, because the system may treat the bad observation as
good. The reason for multiple passes at different times in urban canyons.*

**mxdb**
The project database file TMI creates in the field; the entry point for TBC import.
*Maintains the timing relationship between trajectory, LiDAR and imagery — which is what
makes the data georeferenced at all.*

**PDOP — Position Dilution of Precision**
A measure of how well-spread the satellites are. Lower is better.
*Poor PDOP means poor geometry regardless of satellite count.*

**Point cloud**
The set of measured 3D points.
*Every point inherits the trajectory's error at the instant it was measured.*

**POSPac MMS**
Applanix software that post-processes GNSS and IMU data into the final trajectory.
*Can run standalone or inside TBC. Displays lever arms corrected by internal vectors, so
they differ from your mechanical measurements — this is correct.*

**PPS — Pulse Per Second**
A once-per-second timing signal from the GNSS receiver whose edge coincides with the exact
GPS second.
*The MX60's internal timing reference, available on the external connector for
synchronising other equipment.*

**Precision vs. accuracy**
*Accuracy* = closeness to the true value. *Precision* = repeatability.
*The MX60 scanner: 2 mm accuracy, 2.5 mm precision at 30 m.*

**Registration**
Aligning point cloud runs to each other and to control.
*TBC uses it to "reduce, or eliminate, IMU drift." Look at run-to-run disagreement before
registering — it is your best free QC measure, and registration removes it.*

**Run**
One recorded pass, from pressing Record to pressing it again.
*A mission contains several runs. The Record button controls laser and imagery only.*

**Shadowing / occlusion**
Where the laser was blocked, leaving a void.
*Caused by traffic, parked cars, vegetation, barriers, terrain. The remedy is another
pass — or conventional survey, if nothing can see it.*

**Time synchronization**
Stamping every measurement to the exact GPS second.
*At 80 km/h a 1 ms timing error displaces a point by 2 cm. This is accuracy, not
bookkeeping.*

**Trajectory**
The continuous record of where the sensor was and how it was oriented, at every instant.
*Everything in the dataset is positioned relative to it. A perfect scanner on a poor
trajectory produces a poor cloud, and no processing step recovers it.*

**Useful range**
The distance from the vehicle over which the cloud actually meets project accuracy.
*Always less than the cloud's visible extent. TMR requires contractors to state it
explicitly (§11.7, p.18) — the single best defence against client misunderstanding.*

**Vehicle Frame**
The coordinate frame for lever arms: **+X forward, +Y right, +Z down**.
*Note Z is **down**, not up.*

**Vehicle Preset**
A saved set of mounting parameters — install height, DMI and GAMS lever arms and their
activation checkboxes.
*Cannot be changed mid-mission. An unactivated aiding sensor logs nothing.*

**Waterfall view**
The live laser data display in TMI.
*Where you confirm the laser is producing sensible data, and where a wrong dust-filter
install height shows up immediately as gaps.*

**ZUPT — Zero Velocity Update**
Telling the navigation filter the vehicle is stationary, so anything the IMU reports is
error.
*How the filter measures and removes inertial bias. Supplied by the DMI, and the reason
for the static period at both ends of a mission.*

---

## Abbreviations

| | |
|---|---|
| **APC** | Antenna Phase Centre |
| **CU** | Control Unit |
| **DMI** | Distance Measuring Indicator |
| **ERP** | External Reference Point |
| **GAMS** | GNSS Azimuth Measurement System |
| **GNSS** | Global Navigation Satellite System |
| **IMU** | Inertial Measurement Unit |
| **PDOP** | Position Dilution of Precision |
| **PPS** | Pulse Per Second |
| **PRR** | Pulse Repetition Rate |
| **PU** | Power Unit |
| **RMS** | Root Mean Square |
| **RR** | Roof Rack |
| **SSD** | Solid State Disk |
| **SU** | Sensor Unit |
| **TBC** | Trimble Business Center |
| **TMI** | Trimble Mobile Imaging |
| **UTC** | Coordinated Universal Time |
| **ZUPT** | Zero Velocity Update |

*(MX60 UG Rev B, p.58; TMR MLS Guideline §2, pp.1–4)*
