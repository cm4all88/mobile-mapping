# 13. Calibration

**Periodic, not per-job.** Run it when the interval or a trigger says so (SOP §15.2), not because
a dataset looks wrong.

## 13.1 The laser scanners

### 13.1 Do

1. Collect the calibration mission: **four runs — two along one road forward and backward, two
   along a crossing road forward and backward** *(TBC 24886)*
2. Import it, and **generate scans** from all four runs
3. **Calibrate Laser Scanners**
4. Work **both run pairs**. The dialog presents one pair at a time and the second is easy to miss
5. Read the results, then **do the visual check**

### 13.2 Look at

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

### 13.3 Expect

Three similar-sized components. **One much larger than the other two points at a specific part of
the solution**: tangential at timing or along-track scale, orthogonal at heading, vertical at pitch
or the height component *(Technical Manual §23.3)*.

### 13.4 Stop if

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

### 13.5 Do

1. Generate scans from at least one run
2. Select a camera under **Capture Devices** ▸ **Manual Camera Calibration**
3. Pick a position on the trajectory in Plan View; the camera view displays there
4. Enter **Heading**, **Pitch** or **Roll** and press Enter — **the view updates immediately**

| Input | Step |
|---|---|
| Arrow up / down · mouse wheel | ± 0.001° |
| Ctrl + arrow · Page Up/Down · Ctrl + wheel | ± 0.01° |

*(TBC 24868)*

### 13.6 Expect

**A visual, iterative alignment, not a computed adjustment.** You nudge until the imagery lines up
with the cloud. There is no residual, and the quality is whatever care you took.

### 13.7 Stop if

You cannot get the imagery to sit on the cloud at more than one location. That is not a boresight
you can nudge out.

> **PARAMETRIX DECISION REQUIRED · D-24**
>
> **Where is the calibration site, and who maintains it?** *(SOP §15.3)*

## 13.3 Afterwards

### 13.8 Do

1. **Export the calibration JSON and archive it outside the TBC project**, named with the system
   serial number and the calibration date *(SOP §15.5)*
2. Record the calibration: date, site, who, and the result **including the visual check**

> The JSON is the complete calibration state in one small file. It imports into any later project
> and is the only portable record of what the system's angles were on a given date. A cleanup
> (§29) or a lost workstation should not take it with them.
