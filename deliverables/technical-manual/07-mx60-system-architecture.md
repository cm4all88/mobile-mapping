# 7. MX60 System Architecture

## 7.1 The units

The MX60 is a vehicle-roof-mounted mobile mapping system. Its components, as they appear in
this document and in TMI:

| Component | Function |
|---|---|
| **Sensor Unit** | The roof-mounted head: scanners, cameras, GNSS antenna, IMU. **24–28 kg** depending on configuration *(MX60 UG Rev B)* — a two-person lift |
| **Control Unit** | In-vehicle computer, data storage, power management. **IP30 — not waterproof**, and lives inside the vehicle *(MX60 UG Rev B, p.53)* |
| **Exchangeable data disk** | Removable storage inside the Control Unit |
| **Mounting rack** | Attaches the Sensor Unit to the vehicle |
| **GAMS antenna** *(optional)* | Second GNSS antenna for direct heading |
| **DMI** *(optional)* | Wheel-mounted distance measuring indicator |

## 7.2 The sensors

| Sensor | Count | Notes |
|---|---|---|
| Laser scanner | **2** | One per side, mounted at opposing oblique angles |
| Spherical camera | 1 | 360° panoramic |
| Rear-downward camera | 1 | Pavement-facing |

> **The two-scanner arrangement is the reason Register Run to Run can work on a single run**, and
> the reason most exports produce a pair of files — *Laser Left* and *Laser Right* — rather than
> one *(TBC 22501, 23339)*.

## 7.3 The three configurations

Three: **Core**, **Pro**, **Premium** *(MX60 UG Rev B, p.12)*. They differ in the 360° camera
and in the GNSS/IMU grade.

| | Core | Pro | **Premium — ours** |
|---|---|---|---|
| Panoramic image size | **8192 × 4096 px** | **12288 × 6144 px** | **12288 × 6144 px** |
| Side / planar image size | 4096 × 3008 px | 4096 × 3008 px | 4096 × 3008 px |

*(TBC 22501, 23888 — the panorama figures; these are the sizes TBC writes at export)*

> **The Parametrix system is the MX60 Premium.** Read the Premium column throughout this manual,
> and the larger of any two figures a Trimble topic gives. Recorded in the master register under
> **D-2**; confirmation against the serial number is still outstanding under **V-4**.

## 7.4 Specification discrepancies to be aware of

Two unresolved conflicts sit in the source documents. Neither blocks work, but neither should be
quoted to a client without checking.

| | Source A | Source B | Status |
|---|---|---|---|
| Scanner field of view | ~346° beam deflection *(MX60 UG Rev B, p.54)* | Full 360° *(Spec sheet, p.2)* | **VENDOR CLARIFICATION REQUIRED · V-15** — matters for occlusion geometry |
| Mounting rack | MX SCAN Roof Rack, 18 kg | MX Shock Absorbing Mounting Rack, 28 kg | **PARAMETRIX DECISION REQUIRED** — which is fitted. The published GAMS corner offsets apply to the standard rack **only** *(MX60 UG Rev B, p.68)* |

*(Recorded as `CONFLICT-002` and `CONFLICT-003` in `reference/mx60-reference-data.csv`.)*

> **On the rack, one piece of circumstantial evidence.** The manual held for this system is the
> **MX Shock Absorbing Mounting Rack User Guide**, Rev B May 2025, P/N 37000001 — the 28 kg rack.
> The spec sheet lists a single rack at **18 kg**, which is the standard one. Holding a manual is
> not proof of what is bolted to the vehicle, and Trimble may supply both, but it is the strongest
> indication in the source set and it points away from the standard rack. **If the Shock Absorbing
> rack is fitted, the published GAMS corner offsets do not apply**, which is the whole reason the
> question matters. Settle it by looking at the vehicle *(D-2)*.
## 7.5 The vehicle frame

Every offset and every angle in this system is expressed in one convention, and it is worth
fixing in mind once because it is not the convention most surveyors carry around.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943, 24886)*
>
> - **Positive X = forward driving direction**
> - **Positive Y = right side of the vehicle**
> - **Positive Z = downward**

> **WHY THIS MATTERS — Z is down**
>
> A sensor mounted **above** the reference point has a **negative Z** in this convention. Getting
> the sign wrong puts twice the offset into the solution, in the wrong direction — and it will not
> present as a sign error downstream. It will present as a height problem, which people
> reasonably attribute to the geoid, the antenna model or the base station.

The same convention governs every boresight angle in §20: **roll about X, pitch about Y, heading
about Z**, with Z pointing down.

## 7.6 Lever arms and boresight angles — the two kinds of offset

The system has to know where each sensor is relative to the inertial reference point, and how
each sensor is oriented relative to it. These are two different quantities, determined in two
different ways, and conflating them is the most common conceptual error in this subject.

| | **Lever arm** | **Boresight** |
|---|---|---|
| What it is | The **distance** offset between two sensor frames — a three-dimensional vector | The **angular** offset between a sensor and the inertial reference frame |
| How it is determined | **Measured.** Known from manufacture and from installation measurement | **Estimated.** This is what a calibration solves (§20) |
| Changes when | The hardware is remounted or the rack changes | Thermal cycling, vibration, remounting — it drifts |
| Error behaviour | A constant offset, the same at every range | **Multiplies with range** (§3.1) |

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
>
> "**Lever Arm** refers to the displacement between two body coordinate frames… expressed as a
> three-dimensional vector."

> **TBC's laser scanner calibration solves angles only** *(TBC 24886; §20.2)*. If a lever arm is
> wrong, no amount of calibration will find it — the adjustment has no parameter for it. It will
> be absorbed partly into the boresight estimate, which then compensates for a translation with a
> rotation, and the compensation is only correct at the range where it was determined.

> **CAUTION**
>
> **Changing the rack, the roof bars, the vehicle, or the Sensor Unit's position on the rack
> invalidates the lever arms and may invalidate the calibration.** None of those changes announces
> itself in the data, and the resulting error is systematic rather than noisy.

### Where the values live

`Extcal.json`, written alongside the raw mission data, carries the calibration state that
produced that mission (§5.2). TBC distinguishes the values **before** calibration from the values
**after**:

| Term | Meaning |
|---|---|
| **Installation Matrix** | Parameters **before** calibration — the as-built values *(TBC 22920)* |
| **Refinement Matrix** | Parameters **after** calibration *(TBC 22920)* |
| **Boresight installation / Boresight refinement** | The same distinction as it appears in TBC's sensor properties *(TBC 24868)* |

## 7.7 The optional sensors, and why fitment is a live question

GAMS and DMI are both optional. Whether this system has them changes the field procedure, the
office procedure, and what the data is capable of — which is why their fitment sits in the master
register as a blocking item rather than a detail.

| | Fitted | Not fitted |
|---|---|---|
| **GAMS** | Direct heading from a two-antenna baseline. Initialization is faster and heading is better determined throughout (§9.1) | Heading must be solved from motion. **Straight driving during initialization matters more, not less** *(TBC 25943; §13)* |
| **DMI** | Independent along-track distance, constraining the solution through GNSS gaps (§9.2) | The inertial sensor carries the gaps alone |

> **Open Parametrix decision — D-2 / V-4.** *Are GAMS and DMI fitted, and which rack is on the
> vehicle?* The configuration itself is answered — **Premium** — but these three are not, and each
> changes procedure: GAMS changes how the first two minutes of every mission are driven, DMI
> changes what the published no-outage accuracy assumes, and the rack decides whether the
> published GAMS corner offsets apply at all. One call to the dealer answers all three.

## 7.8 Power

The Control Unit manages vehicle power. The specifications below are what the installation has to
satisfy; the installation procedure itself is the **Field How To §6**.

> **TRIMBLE DOCUMENTED METHOD**
>
> | | Value | Source |
> |---|---|---|
> | Input voltage | **12–16 V DC** | MX60 UG Rev B |
> | Current at startup | **25 A at 12.8 V** (320 W) | MX60 UG Rev B |
> | Current in operation | 12 A (160 W) | MX60 UG Rev B |
> | **Supply rating required** | **30 A or more** | MX60 QSG Rev B, p.4 |
> | Direct-connection fuse | **35 A**, close to the battery | MX60 UG Rev B |
> | Data storage | 2 × 4 TB removable SSD | MX60 Spec Sheet, p.3 |
>
> An **auxiliary battery as a backup power source is recommended** *(MX60 QSG Rev B, p.4)*.

> **WHY THIS MATTERS**
>
> The startup draw is twice the operating draw. A supply sized for the operating figure will brown
> out at every power-on, and the symptom — a system that starts unreliably — does not look like a
> supply problem.

## 7.9 The protection that ends a run

The Control Unit manages vehicle power, and it protects the vehicle's battery rather than the
mission. That priority is correct and worth knowing about in advance.

> **CAUTION · W-11**
>
> **Battery Protect** *(MX60 UG Rev B, p.27)*:
>
> | Event | Trigger |
> |---|---|
> | Audible warning | Supply below **10.5 V for longer than 12 seconds** |
> | Power cut | Supply below **10.5 V for more than 90 seconds** |
> | Recovery | Voltage rises above **12.0 V within that 90 seconds** |
>
> The alarm leaves roughly **78 seconds** to restore charge — that figure is the arithmetic of the
> two sourced timings, not a separately published one.
>
> An interrupted run loses the closing sequence with it.

> **WHY THIS MATTERS**
>
> The consequence is not "the system switched off." It is that the mission ended without a closing
> sequence, so the backward filter pass has no anchor at the end of the data (§14). The cost is
> paid at the end of the trajectory, which is often the most recent and most important part of the
> day's work.
>
> The practical response is to keep the engine running while the system is operating, and to treat
> the audible warning as an instruction to restore charge immediately rather than as information.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We took the system apart on paper: two laser scanners, two cameras, a
> GNSS/inertial unit, and optionally a second antenna and a wheel sensor — plus the conventions
> that describe where each of them sits.
>
> **Why it matters.** Almost every number in the rest of this manual depends on two things about
> this particular vehicle: which configuration it is, and what is fitted to it. The first is
> settled — **Premium**, so the panoramas are the full 12288 × 6144 px and the navigation grade is
> the best of the three. The second is not. Without GAMS, the heading has to be solved out of the
> vehicle's motion, which changes how you drive the first two minutes of every mission. That is
> not a detail to look up later — it changes the procedure.
>
> **What can go wrong.** The offset signs. Z is **down** in this convention, so a sensor on the
> roof has a negative Z. And a lever arm is measured while a boresight is estimated, so a wrong
> lever arm cannot be calibrated out — the calibration has no parameter for it, and will quietly
> absorb part of the error into an angle instead, which then only works at one range.
>
> **What good looks like.** The configuration, the fitment and the measured offsets are written
> down somewhere a processor can find them, and somebody has checked them against the vehicle
> rather than against the last project's paperwork. These values are entered once and used on
> every mission afterwards, so an error in them is systematic, invisible, and permanent until
> someone re-measures.
