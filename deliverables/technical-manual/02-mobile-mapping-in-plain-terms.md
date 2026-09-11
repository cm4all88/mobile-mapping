# 2. Mobile Mapping in Plain Terms

This section is for the reader who knows surveying and has never operated a mobile mapping
system. Everything else in this manual depends on the ideas here.

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

- Why initialization matters, and why it is not a formality (§13)
- Why GNSS conditions dominate the accuracy conversation (§15, §27)
- Why everything downstream of the trajectory has to be recomputed when it changes (§18, §21)
- Why the office work is largely about improving the trajectory, not the points (§17, §21)
- Why proving *which trajectory* produced a deliverable turns out to be hard (§30)

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
> practical reason the field procedure requires a proper closing sequence (§14), and it is the
> single most commonly skipped step in mobile mapping.

Two supporting sensors appear throughout this document:

- **GAMS** — a second GNSS antenna. Two antennas a known distance apart give a direct heading
  measurement, which is otherwise the hardest attitude component to determine. It speeds up
  initialization considerably *(TBC 25943)*
- **DMI** — a distance measuring indicator on a wheel. It provides an independent along-track
  distance, which constrains the inertial solution when GNSS is poor *(TBC 25943)*

## 2.3 What the office actually does

A surveyor coming from static scanning expects office work to mean registration of scans to
each other and to control. Mobile mapping is different in an instructive way.

| Stage | What is being improved |
|---|---|
| **Trajectory processing** (§17) | The trajectory itself, from raw observations and base station data |
| **Scan generation** (§18) | Nothing — this applies the trajectory to produce the cloud |
| **Calibration** (§20) | The fixed angular offsets between sensors. Periodic, not per-job |
| **Registration** (§21) | **The trajectory again**, now using surveyed control or overlapping cloud |
| **Update Scans** (§19) | Nothing — this reapplies the improved trajectory to produce a new cloud |

> **Three of the five stages improve the trajectory. Two of them just recompute points.**
>
> This is the shape of mobile mapping office work, and it is why the phrase "registering the
> point cloud" is misleading. You are not moving points. You are improving the path the sensor
> took, and then recomputing where the points must therefore have been.


---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We established the one idea the rest of this manual rests on: a mobile
> mapping system has no occupied point. It computes where it was, continuously, and every point it
> collects is hung off that computed path. The path is called the trajectory, and it is the job.
>
> **Why it matters.** Think of it as a very long, very fast resection that never stops — except
> that instead of resecting from known points, the system is dead-reckoning with an inertial sensor
> and correcting itself with satellites whenever the sky allows. When the sky does not allow, it
> keeps going on inertial alone and quietly gets worse. Almost everything the office does later is
> an attempt to improve that path, not to move the points around.
>
> **What can go wrong.** The thing that catches people is that the office work does not look like
> registration in the static scanning sense. Three of the five office stages improve the
> trajectory; two of them just recompute points from it. A processor who thinks they are moving a
> point cloud will eventually be surprised by something — most often by discovering that a
> registration they performed never reached the data (§19).
>
> **What good looks like.** You can say, for any point in a delivered cloud, which trajectory put
> it there and what the quality of that trajectory was at that instant. §30 is about how far that
> is currently possible.
