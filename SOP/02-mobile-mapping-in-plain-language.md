# 2. MOBILE MAPPING IN PLAIN LANGUAGE

No settings or tolerances here — this section exists so the rest of the document makes
sense.

## 2.1 The short version

**Mobile mapping is surveying from a moving vehicle.**

You drive a road at close to normal traffic speed. The equipment on the roof measures
everything it can see and photographs it. In the office, that becomes a 3D point cloud
and georeferenced imagery covering the whole corridor. You then take your measurements
from that dataset instead of from the roadway.

The trade: you collect enormous amounts of data fast, without a crew in traffic. In
exchange you give up choosing individual shots — you get what the vehicle could see.

> **WHY THIS MATTERS**
>
> That trade explains nearly every limitation in this document. You are choosing routes
> and driving, not shots. What the vehicle cannot see, you do not get.

## 2.2 What the MX60 is

A sealed sensor pod on the vehicle roof, plus a control unit and power unit inside.

Inside the pod:

| Component | Job |
|---|---|
| **Two laser scanners** | Measure the shape of the world |
| **360° panoramic camera** | Six cameras covering ~90% of the sphere |
| **Down-looking camera** | Pavement detail |
| **GNSS/IMU system** | Where the pod is, and which way it points, continuously |

*(MX60 User Guide Rev B, pp.12–13)*

Everything else — control unit, power unit, rack, cables, tablet — powers that pod,
records what it produces, and lets you control it.

## 2.3 How the pieces fit together

**This is the core concept.** If you take one thing from this section, take this.

| Piece | What it contributes | Its weakness |
|---|---|---|
| **LiDAR** | Distance and direction from itself — a *shape*, not a location | Knows nothing about where it is |
| **Cameras** | Visual record; can colour the point cloud | Needs light; sees only what's exposed |
| **GNSS** | Position in the real world | Slow-updating; fails where sky is blocked |
| **IMU** | Rotation and acceleration, hundreds of times a second | Drifts — errors grow over time |
| **Time sync** | Stamps every measurement to the exact GPS second | — |
| **Processing** | Combines it all into a georeferenced dataset | Cannot fix what wasn't collected well |

**How it comes together:** GNSS and IMU are processed into a **trajectory** — where the
sensor was and how it was oriented at every instant. Each laser measurement is then
matched to the trajectory by timestamp. The scanner says *"something 14.2 m away, that
direction, at 10:43:07.184."* The trajectory says *"at 10:43:07.184 you were here,
pointing this way."* Combine them → a real-world coordinate. Do it a billion times → a
point cloud.

> **WHY THIS MATTERS — GNSS and IMU are deliberately complementary**
>
> GNSS is stable over time but coarse and easily blocked. The IMU is fast and immune to
> blockage but drifts. Blended, you get both stable and continuous.
>
> This is why a *short* GNSS outage is survivable and a *long* one is dangerous. The IMU
> carries you across the gap — but only so far before drift takes over. See Section 16.

> **WHY THIS MATTERS — timing is accuracy, not admin**
>
> At 80 km/h the vehicle moves ~22 mm per millisecond. A 1 ms timing error puts a point
> 2 cm from where it belongs. The MX60 times everything to the GPS second using a
> one-pulse-per-second signal *(MX60 UG Rev B, pp.65–66)*.

## 2.4 The single most important idea

**Everything is positioned relative to the trajectory.**

The scanner is accurate to about 2 mm at 30 m *(MX60 UG Rev B, p.54)*. That number is
nearly irrelevant to your final accuracy. Every point inherits the *trajectory's* error at
the moment it was measured.

> **IMPORTANT**
>
> A perfect scanner on a poor trajectory produces a poor point cloud, and no processing
> step recovers it later. Protecting the trajectory is the operator's most important job.

Initialization, driving behaviour, route planning, avoiding long GNSS outages — these are
all trajectory protection. Section 16 explains the mechanism.

## 2.5 What gets delivered

| Deliverable | Notes |
|---|---|
| Georeferenced point cloud | With intensity; optionally coloured from imagery |
| Georeferenced imagery | Panoramic and pavement, indexed to coordinates |
| Trajectory | Path and orientation, with quality information |
| **Extracted features** | Surfaces, breaklines, edge of pavement, signs, poles, assets — *usually what the client actually wants* |
| Survey report | What was collected, how, with what control, how it checked |

Point cloud and imagery are the **source**. Extracted features are the **product**. Most
office effort goes into extraction.

> **FIELD TIP**
>
> The point cloud is permanent in a way conventional survey is not. Someone can measure
> something three years later that nobody thought to record — as long as the vehicle saw
> it and the raw data still exists. That's why Section 14 is firm about never deleting
> source data.

## 2.6 What the operator does

1. Check equipment, mount the sensor
2. Confirm mounting measurements are correct in the software
3. Power up, connect the tablet
4. Wait for system ready and a good GNSS solution
5. Initialize
6. Start the mission
7. **Drive the planned route** — smoothly, sensible speed, correct lanes
8. **Watch the status while driving**
9. End the mission correctly
10. Shut down correctly
11. Get the data off safely

Steps 7 and 8 are where the operator earns their keep. The rest can be checklisted.

> **CAUTION**
>
> The driver may not operate the system while driving. Trimble recommends a second person
> be dedicated to operating it. *(MX60 UG Rev B, pp.9, 36)*

## 2.7 Three ways this differs from what you know

**You cannot re-shoot a point.** Occluded by a truck means occluded. The remedy is another
pass, not another shot — which is why multiple passes are standard, not a luxury.

**Accuracy varies along the route.** Better in open sky, worse under that bridge, and the
transition is gradual. There is no single accuracy number for a corridor.

**Accuracy varies with distance from the vehicle.** The cloud may reach far beyond the
roadway, but the part meeting project accuracy is much narrower. Queensland's guideline
requires contractors to state this "useful range" explicitly, noting that although a
cloud may extend to 200 m, "in most cases the part of the point cloud that meets the
accuracy specified by the project will be considerably less than that distance"
*(TMR MLS Guideline §11.7, p.18)*.

> **WHY THIS MATTERS**
>
> This causes more trouble than any other misunderstanding. A client sees the cloud
> reaching a building 60 m away and assumes it's surveyed to the same standard as the
> curb line. It isn't. State useful range early and you avoid the argument later.

## 2.8 Where mobile mapping fits

| Good at | Poor at / cannot do |
|---|---|
| Long roadway corridors | Anything the vehicle can't see — behind barriers, under parked cars |
| Pavement surfaces and cross-sections | Anything needing physical contact — invert elevations, buried utilities |
| Roadside assets — signs, poles, barriers | Monument recovery, boundary evidence |
| Capture without road closure or crew exposure | Areas the vehicle can't legally or safely reach |
| Permanent visual and dimensional record | |

It is normal for a mobile mapping project to include conventional survey filling these
gaps. That's not a failure of the method — it's how it's used properly. See Section 21.

---

## References — Section 2

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 12–13, 36, 54, 65–66 |
| Trimble MX60 Spec Sheet, PN 022516-737C (04/25) | 2 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §11.7, p.18 |
