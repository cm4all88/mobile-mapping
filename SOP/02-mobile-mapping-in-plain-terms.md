# 2. Mobile Mapping in Plain Terms

This section is for the reader who knows surveying and has never operated a mobile mapping
system. Everything else in this document depends on the ideas here.

## 2.1 The one difference that explains all the others

A total station or a static scanner measures from a **known, stationary point**. You occupy,
you orient, you shoot. The instrument's position is fixed and separately determined, so the
quality of any measurement is a question about that measurement.

The MX60 never stops. It measures continuously from a vehicle moving at highway speed, and it
has no occupied point at all. Instead it computes, for every instant, **where the sensor head
was and which way it was pointing** — a continuous record called the **trajectory**.

> Every point in a mobile mapping cloud is the sum of two things: a range and angle measured by
> the scanner, and the position and attitude of the scanner at the instant of that measurement.
> The scanner part is excellent and nearly constant. **The trajectory part is where the error
> lives.**

This single fact drives the rest of the document:

- Why initialization matters, and why it is not a formality (§8)
- Why GNSS conditions dominate the accuracy conversation (§6, §20)
- Why everything downstream of the trajectory has to be recomputed when it changes (§13, §15)
- Why the office work is largely about improving the trajectory, not the points (§12, §15, §16)
- Why proving *which trajectory* produced a deliverable turns out to be hard (§23)

## 2.2 What the trajectory is, and how it is computed

The trajectory is a time series: position (X, Y, Z) and attitude (roll, pitch, heading) at a
high rate, for the whole mission. It is produced by combining two sensor types that fail in
opposite ways.

| | **GNSS** | **Inertial (IMU)** |
|---|---|---|
| Measures | Absolute position | Change in orientation and velocity |
| Error behaviour | Bounded but noisy — it does not drift, but it jumps and can be lost entirely | Smooth and precise instant to instant, but **drifts without limit over time** |
| Fails when | Sky is obstructed — trees, buildings, bridges, tunnels | Always, gradually, by its nature |

Neither alone is adequate. Combined, each covers the other's weakness: GNSS anchors the
inertial solution and stops the drift; the IMU carries the solution smoothly through the gaps
when GNSS is degraded or absent.

The combination is done by a filter, and for surveying work it is done **twice** — once
forward through time and once backward — then merged. The merged result is called a **Smoothed
Best Estimate of Trajectory**, universally abbreviated **SBET**.

> **The backward pass is why the end of a mission matters as much as the beginning.** A gap in
> the middle of the drive is bracketed by good data on both sides, and the smoother can bridge
> it from both directions. A gap at the *end* has good data on one side only. This is the
> practical reason the field procedure requires a proper closing sequence (§8.7), and it is the
> single most commonly skipped step in mobile mapping.

Two supporting sensors appear throughout this document:

- **GAMS** — a second GNSS antenna. Two antennas a known distance apart give a direct heading
  measurement, which is otherwise the hardest attitude component to determine. It speeds up
  initialization considerably *(TBC 25943)*
- **DMI** — a distance measuring indicator on a wheel. It provides an independent along-track
  distance, which constrains the inertial solution when GNSS is poor *(TBC 25943)*

## 2.3 How mobile mapping error behaves

This is where a surveyor's intuition needs adjusting, and it is worth being precise.

**Error is not uniform across the dataset.** It varies along the corridor with GNSS quality, and
it varies within a single scan line with range.

### Attitude error multiplies with range

An error in the *position* of the sensor head displaces every point by the same amount. An
error in the *attitude* — which way it was pointing — displaces points by an amount
proportional to how far away they are.

The relationship is simple geometry: lateral displacement is range multiplied by the angular
error in radians. A given attitude error therefore costs five times as much at 50 m as at 10 m.

> This is arithmetic, not a specification. **No Trimble source in the set publishes an attitude
> error budget for the MX60**, so the useful range for a given tolerance has to be established
> from the manufacturer's accuracy statement for the configuration Parametrix owns (§4.1), or by
> test.

> **WHY THIS MATTERS**
>
> This is why *useful range* is a shorter distance than *maximum range*. The scanner can return
> a point at its maximum range; whether that point is good enough to measure from is a
> different question, and the answer depends on the attitude accuracy of the trajectory at that
> instant. Two clouds collected on the same day with the same instrument can have quite
> different useful ranges if one was collected under open sky and the other in an urban canyon.

### Error is correlated in time, not scattered

Conventional survey errors tend to be independent — one shot's error tells you little about the
next. Mobile mapping error is **strongly correlated over seconds and minutes**, because it is
dominated by the state of a filter that evolves smoothly.

The practical consequence: a bad stretch of trajectory produces a whole *region* of cloud that
is consistently displaced, not a scatter of bad points. It will look internally consistent and
perfectly clean. **It will simply be in the wrong place**, and only comparison against
independent control will reveal it.

> That is the most important thing in this section. **Mobile mapping data does not look wrong
> when it is wrong.**

## 2.4 What the MX60 actually collects

| Sensor | What it produces |
|---|---|
| **Two laser scanners** | Range and angle, continuously, to both sides of the vehicle |
| **360° spherical camera** | Panoramic imagery along the corridor |
| **Rear-downward camera** | Pavement-facing imagery, used for pavement condition and orthomosaics |
| **GNSS receiver and IMU** | The raw observations from which the trajectory is computed |

The system is sold in three configurations — **Core**, **Pro** and **Premium** — which differ
in imagery resolution and in the grade of the GNSS/IMU system *(MX60 UG Rev B, p.12)*.

> **PARAMETRIX DECISION REQUIRED**
>
> **Which configuration is the Parametrix system?** This is not a detail. Panoramic imagery is
> **8192 × 4096 px on Core and 12288 × 6144 px on Premium and Pro** *(TBC 22501, 23888)* — four
> times the pixels. The attitude accuracy of the navigation system also differs by
> configuration, which changes every accuracy statement in this document.
>
> The vendor can confirm from the serial number. *(Register item 2; Appendix F)*

## 2.5 The data chain, once

The names matter because TBC's commands are named after them, and a processor who does not know
which object a command acts on will eventually act on the wrong one.

```
  .mxdb          The mission database written in the field. The index to everything
     │
     ├── raw GNSS + IMU observations  ──►  SBET (or NAV)      the trajectory
     │
     └── raw scanner + camera data
              │
              ▼
            TMX          polar scan data — ranges and angles, sensor-relative
              │
              │   Generate Scans  ◄── applies the trajectory
              ▼
           RWCX          the point cloud — XYZ, intensity, colour, normals
```

Two things are worth noting now and will be returned to in §13.

**The MX60 converts TMX to RWCX in one step.** Older MX9 and MX90 systems go through an
intermediate stage requiring a range-ambiguity correction called MTA. **The MX60 workflow has
no MTA stage**, which removes a whole category of setup and a whole category of failure
*(TBC 22503)*.

**The trajectory is applied at scan generation, not at collection.** The raw scan data is
sensor-relative. It becomes a georeferenced point cloud only when combined with a trajectory —
which is why improving the trajectory later means regenerating the cloud (§15, §13).

## 2.6 What the office actually does

A surveyor coming from static scanning expects office work to mean registration of scans to
each other and to control. Mobile mapping is different in an instructive way.

| Stage | What is being improved |
|---|---|
| **Trajectory processing** (§12) | The trajectory itself, from raw observations and base station data |
| **Scan generation** (§13) | Nothing — this applies the trajectory to produce the cloud |
| **Calibration** (§14) | The fixed angular offsets between sensors. Periodic, not per-job |
| **Registration** (§15, §16) | **The trajectory again**, now using surveyed control or overlapping cloud |
| **Update Scans** (§13.6) | Nothing — this reapplies the improved trajectory to produce a new cloud |

> **Three of the five stages improve the trajectory. Two of them just recompute points.**
>
> This is the shape of mobile mapping office work, and it is why the phrase "registering the
> point cloud" is misleading. You are not moving points. You are improving the path the sensor
> took, and then recomputing where the points must therefore have been.

## 2.7 Vocabulary

Enough to read the next several sections. The full glossary is §27.

| Term | Meaning |
|---|---|
| **Trajectory** | The computed position and attitude of the sensor head over time |
| **SBET** | Smoothed Best Estimate of Trajectory — the post-processed trajectory |
| **NAV** | The real-time trajectory computed in the field. Lower quality; a fallback |
| **Mission** | One deployment: a `.mxdb` and everything under it |
| **Run** | One continuous stretch of collection within a mission. A mission has many |
| **Station** | One instant of imagery capture along a run |
| **Boresight** | The fixed angular offset between a sensor and the inertial reference frame |
| **Lever arm** | The fixed distance offset between two sensors. **Known, not estimated** |
| **Registration** | Adjusting a trajectory to fit surveyed control, or to fit another run |
| **Target** | In TBC's registration sense: a point **picked in the point cloud** |
| **GCP** | Ground control point — an accurately surveyed coordinate on an identifiable feature |
| **Validation point** | A GCP held out of the adjustment, used only to measure its quality |

> **"Target" is a trap.** In TBC's registration commands a *target* is not a physical panel you
> placed in the field. It is a point the operator picks in the point cloud, which is then paired
> with a surveyed GCP *(TBC 22905)*. The physical thing in the field is the GCP. A checkerboard
> panel is one kind of feature you might pick, but so is a corner of a painted road marking.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We established the one idea the rest of this document rests on: a mobile
> mapping system has no occupied point. It computes where it was, continuously, and every point
> it collects is hung off that computed path. The path is called the trajectory, and it is the
> job.
>
> **Why it matters.** Think of it as a very long, very fast resection that never stops — except
> that instead of resecting from known points, the system is dead-reckoning with an inertial
> sensor and correcting itself with GNSS whenever the sky allows. When the sky does not allow,
> it keeps going on inertial alone and quietly gets worse. Everything the office does later is
> an attempt to improve that path, not to move the points around.
>
> **What can go wrong.** The thing that catches people is that bad mobile mapping data looks
> fine. If the trajectory was drifting through a tree-lined stretch, the cloud from that stretch
> is still crisp, still dense, still internally consistent — and sitting 8 cm from where it
> should be. There is no noise, no scatter, no visual tell. You find it by checking against
> control you surveyed independently, or you do not find it at all. This is different from a
> total station, where a bad shot usually looks like a bad shot.
>
> **What good looks like.** A dataset you can trust is one where the trajectory had continuous
> good GNSS or short, well-bracketed gaps; where independent check points that took no part in
> any adjustment fall where they should; and where two passes down the same corridor land on top
> of each other. Not one where the cloud looks clean — it always looks clean.
