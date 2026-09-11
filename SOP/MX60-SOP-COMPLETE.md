# PARAMETRIX
# TRIMBLE MX60 MOBILE MAPPING
## STANDARD OPERATING PROCEDURE

---

**Document status:** DRAFT — not yet approved for use
**Revision:** 0.1
**Date:** 2026-09-10

---

## Document control

> **PARAMETRIX DECISION REQUIRED**
>
> Establish document control for this SOP: owning group, document number, approval
> authority, review cycle, and the location of the controlled copy.
>
> *Recommended practice:* assign an owner in the survey technology group, require
> approval by a licensed professional surveyor, and review annually or whenever
> Trimble issues a new revision of the MX60 User Guide or TMI software. Keep one
> controlled electronic copy and treat printed copies as uncontrolled and
> date-stamped.

## Revision history

| Rev | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-09-10 | — | Initial draft. Sections 1–2. |

## Callouts used in this document

| Callout | Meaning |
|---|---|
| **CAUTION** | Could damage equipment, compromise safety, or cause serious data loss. |
| **IMPORTANT** | Failure to follow this could compromise the mobile mapping dataset. |
| **FIELD TIP** | Practical advice that helps the operator. |
| **WHY THIS MATTERS** | Plain-language explanation of the reason behind a procedure. |
| **PARAMETRIX DECISION REQUIRED** | An internal Parametrix standard still needs to be established. This is *not* existing Parametrix policy. |
| **ADVANCED** | Material a new operator does not need immediately. |

> **IMPORTANT**
>
> Anything marked **PARAMETRIX DECISION REQUIRED** is an open question, not a
> procedure. Do not treat the recommended practice shown beneath it as an approved
> Parametrix standard until it has been formally adopted.


---

# 1. PURPOSE AND SCOPE

## 1.1 What this SOP is for

This document explains how to operate the Trimble MX60 mobile mapping system and how
the data it collects becomes usable survey information.

It is written for people who already know how to survey but have never done mobile
mapping. If you are comfortable with control, coordinate systems, GNSS, and field
procedure, you have everything you need to start here. Mobile mapping does not replace
what you already know — it adds a different way of collecting, with a different set of
things that can go wrong.

The goal is that after reading the first several sections you can:

- Recognise every part of the system and say what it does
- Prepare a vehicle and mount the system correctly
- Understand what a normal mobile mapping job looks like from start to finish
- Know what you are watching for while the vehicle is moving
- Know what ruins a collection, and what to do about it

The later sections then go considerably deeper, into trajectory behaviour, data
quality, processing, calibration, and troubleshooting.

## 1.2 Who this is for

| Role | What you need from this document |
|---|---|
| **System operator** | Sections 1–14 and 22–23. This is your working document. |
| **Survey technician** | All of the above, plus 15–20 for processing and QC. |
| **Project surveyor** | Sections 1–5 and 16–21 especially. You are deciding whether mobile mapping suits the project and what supplemental work it needs. |
| **Project manager** | Sections 1–5, 20–21. Enough to scope the work, understand the limits, and know what could force a return trip. |
| **Anyone new to mobile mapping** | Start at Section 2 and read forward. Stop when it gets too technical — you can come back. |

## 1.3 How to read this document

The SOP is layered deliberately. You do not need to read it all before you can be
useful.

**Layer 1 — Sections 1 to 4.** What the system is, what it does, and what a job looks
like. Plain language. No settings, no theory.

**Layer 2 — Sections 5 to 14.** How to actually do it. Planning, preparation, mounting,
startup, collection, shutdown, and protecting the data.

**Layer 3 — Sections 15 to 21.** Why it behaves the way it does. Processing, trajectory,
point cloud and imagery quality, control, QC, and the situations where mobile mapping
is the wrong tool.

**Layer 4 — Sections 22 to 28.** Troubleshooting, checklists, training, advanced
technical material, and reference appendices.

Throughout, the pattern is **how first, why second**. You will be told exactly what to
do, and then — once the procedure makes sense — what it accomplishes.

## 1.4 Equipment covered

This SOP addresses the **Trimble MX60 Mobile Laser Mapping System**.

Trimble supplies the MX60 in three configurations. They share the same body, the same
two laser scanners, the same down-looking camera, and the same operating procedure. They
differ in the 360° camera and the GNSS/IMU positioning system.

| Configuration | Spherical camera | Positioning performance (no GNSS outage) |
|---|---|---|
| **Core** | 30 MP | Roll/pitch 0.005°, heading 0.015° |
| **Pro** | 72 MP | Roll/pitch 0.005°, heading 0.015° |
| **Premium** | 72 MP | Roll/pitch **0.0025°**, heading 0.015° |

*(MX60 User Guide Rev B, pp.12, 53, 56)*

All three are covered here. Where a procedure or a specification differs between
configurations, this SOP says so.

> **PARAMETRIX DECISION REQUIRED**
>
> Record which MX60 configuration Parametrix owns — Core, Pro, or Premium — and note
> the system serial number and any optional accessories fitted.
>
> This is not a formality. The configuration determines the imagery resolution and the
> attitude accuracy of the trajectory, and therefore the accuracy statements this SOP
> can make. It also determines which row of every specification table applies.
>
> *Recommended practice:* record it here in Section 1, and repeat it on the field
> checklist so the operator always knows which system they have.

### Accessories

Two optional accessories materially change the field procedure:

| Accessory | What it does | Effect on procedure |
|---|---|---|
| **GAMS** (GNSS Azimuth Measurement System) | Adds a second GNSS antenna | Speeds up initialization **and eliminates the special driving manoeuvres otherwise needed to initialize** |
| **DMI** (Distance Measuring Indicator) | Wheel odometer | Improves accuracy in poor GNSS conditions and heavy stop-and-go traffic; supplies ZUPT information for post-processing |

*(MX60 User Guide Rev B, pp.42–43, 67; MX60 Spec Sheet p.4)*

> **PARAMETRIX DECISION REQUIRED**
>
> Confirm whether GAMS and DMI are owned and whether they are fitted as standard.
>
> Whether GAMS is fitted changes Section 10 (Initialization) substantially — with it,
> no special driving manoeuvre is needed; without it, one is required before every
> mission. Whether a DMI is fitted changes what the system can do in urban canyon and
> tunnel work.
>
> *Recommended practice:* fit both as standard. GAMS removes a step the operator can
> get wrong, and DMI protects the trajectory exactly where mobile mapping is most
> fragile.

### Mounting hardware

Trimble supplies more than one rack, and they are not interchangeable in procedure.

| Rack | Weight | Mounting | Intended use |
|---|---|---|---|
| **MX SCAN Roof Rack** | 18 kg | Clamps to square-cut universal roof bars, up to 85 × 30 mm | Standard road vehicles |
| **MX Shock Absorbing Mounting Rack** | 28 kg | Bolts to a prepared level platform or aluminium T-slot profile, M6 or M8 | Vehicles "mostly driving in harsher environments than a standard road" |

*(MX60 User Guide Rev B, pp.29, 31; MX Shock Absorbing Mounting Rack User Guide Rev B, pp.6–7, 9)*

> **CAUTION**
>
> Both racks carry the system's External Reference Point, but they are physically
> different. The GAMS corner offsets published in the MX60 User Guide (X = +1.006 m,
> Y = −0.469 m, Z = +0.025 m) are stated for the **standard Roof Rack** and must not
> be assumed to apply to the Shock Absorbing Mounting Rack.
>
> Confirm which rack is on the vehicle before doing any lever-arm work.
> *(MX60 User Guide Rev B, p.68)*

> **PARAMETRIX DECISION REQUIRED**
>
> Record which rack is installed on the Parametrix vehicle, and whether it is
> considered permanently mounted.
>
> *Recommended practice:* treat the rack as permanently installed on a dedicated
> vehicle, as Trimble assumes (MX60 User Guide Rev B, p.41). Re-mounting a rack means
> re-measuring lever arms.

## 1.5 Software covered

| Software | Where it runs | What it does |
|---|---|---|
| **TMI** (Trimble Mobile Imaging) | In a web browser on a tablet or laptop, in the vehicle | Controls the system, configures missions, and shows live camera, LiDAR, and trajectory information |
| **Trimble Business Center (TBC)**, mobile mapping module | Office | Trajectory processing, point cloud registration and colorization, classification, feature extraction, export |
| **POSPac MMS** | Office | Post-processes the navigation data to produce the final trajectory |
| **Trimble MX Publisher** | Office / web | Organises and shares mobile mapping deliverables, with GIS and CAD plug-ins |

*(MX60 Spec Sheet p.4; MX60 User Guide Rev B, pp.47–48)*

> **IMPORTANT**
>
> TMI runs in **Google Chrome**. No other browser is specified by Trimble, and no
> additional software is installed on the operator's device.
> *(MX60 User Guide Rev B, pp.13, 36)*

## 1.6 What is outside the scope of this SOP

This document does **not** teach:

- Basic land surveying — control networks, datums, coordinate systems, GNSS
  fundamentals, traverse, least squares, or boundary practice. These are covered only
  where mobile mapping treats them differently.
- Boundary determination or any judgment reserved to a licensed professional surveyor.
- Airborne, UAS, static terrestrial, or handheld scanning.
- Detailed TBC operation beyond the mobile mapping workflow.
- Vehicle maintenance, or the electrical installation of the power supply — Trimble
  requires that this be done by a professional automotive electrician
  *(MX60 User Guide Rev B, p.61)*.
- Repair of the MX60. Maintenance by the operator is limited to cleaning and inspecting
  external surfaces, lens glass, and controls *(MX60 User Guide Rev B, p.49)*.

> **CAUTION**
>
> Do not open, modify, or attempt to repair any part of the MX60. Trimble states that
> dismantling or having the system repaired by unauthorised personnel can be hazardous
> and costly, and that unauthorised changes — including software changes made by any
> means — can cause personal injury or damage and void all guarantees.
> *(MX60 User Guide Rev B, pp.7, 49)*

## 1.7 Sections not yet written

This SOP is being built in stages, and some sections are deliberately incomplete.

**Sections 8 through 13** — starting the system, the TMI interface, initialization,
in-mission monitoring, and ending a collection — depend on two Trimble documents that
are not yet available to Parametrix:

1. **Trimble TMI Software for Trimble Mobile Mapping Systems User Guide**
   (`geospatial.trimble.com/en/links?dcs=Collection-129953`)
2. **Trimble MX60 Quick Start Guide**, which the MX60 User Guide states contains the
   standard operation workflow and the in-the-field operation checklist
   *(MX60 User Guide Rev B, p.48)*

> **IMPORTANT**
>
> Until those sections are written from the Trimble sources, **do not improvise a
> startup or initialization procedure.** An incorrect initialization does not announce
> itself in the field — it produces a trajectory that looks plausible and is wrong, and
> the whole collection inherits the error.
>
> If you need to operate before those sections exist, work from the Trimble Quick Start
> Guide directly and with an experienced operator present.

## 1.8 Requirement for trained personnel

Trimble is explicit and repeated on this point:

- The system "must be used only by well-trained persons"
- "Operation and service of the system may only be performed by properly trained
  personnel"
- Anyone installing or removing the system must be familiar with the installation
  chapter of the Trimble manual and must have received prior training

*(MX60 User Guide Rev B, pp.7, 9, 10)*

> **PARAMETRIX DECISION REQUIRED**
>
> Define what "trained" means at Parametrix: what training an operator must complete,
> who signs it off, and what supervised experience is required before running a
> production collection alone.
>
> *Recommended practice:* require completion of the Section 24 training exercise,
> supervised participation in at least one production collection, and sign-off by an
> experienced operator before working unsupervised. Maintain a list of qualified
> operators.

---

## Trimble References — Section 1

| Source | Pages used |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7, 9, 10, 12, 13, 29, 31, 36, 41, 42–43, 47–48, 49, 53, 56, 61, 67, 68 |
| Trimble MX60 Spec Sheet, PN 022516-737C (04/25) | 2, 4 |
| Trimble MX Shock Absorbing Mounting Rack User Guide, Rev B, May 2025 (P/N 37000001) | 6–7, 9 |


---

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


---

# 3. SYSTEM COMPONENTS

Reference section. Skim it once, come back to it when something isn't working.

Full specifications for every item here live in `reference/mx60-reference-data.csv`,
each row carrying its Trimble source and page.

## 3.1 The system at a glance

| # | Component | Where it lives | Weight |
|---|---|---|---|
| 1 | **MX60 Sensor Unit** | Vehicle roof, on the rack | 24 / 26 / 28 kg (Core / Pro / Premium) |
| 2 | **MX SCAN Control Unit 2** | Inside vehicle | 13 kg |
| 3 | **MX SCAN Power Unit** | Inside vehicle | 9 kg |
| 4 | **MX SCAN Roof Rack** | Vehicle roof | 18 kg |
| 5 | **Operator device** (tablet or laptop) | Inside vehicle | — |
| — | Cables (3), Data Carrier Docks (2), SSDs (2) | — | — |

*(MX60 UG Rev B, pp.12, 52; QSG Rev B, p.3)*

Optional: **GAMS** second GNSS antenna, **DMI** wheel odometer.

## 3.2 Sensor Unit

**What it is.** The sealed pod on the roof. Everything that measures lives here.

**What's inside:**

| Sensor | Detail |
|---|---|
| **2 laser scanners** | Time-of-flight, rotating mirror. ~346° deflection each. 2 mm accuracy, 2.5 mm precision @ 30 m. Range 0.6 m min; 150 m @ 500 kHz or 120 m @ 1000 kHz |
| **360° spherical camera** | Six cameras. 30 MP (Core) or 72 MP (Pro/Premium). Global shutter. ~90% of full sphere. Max 10 fps |
| **Down-looking camera** | 12 MP, on all configurations. Focal 8.0 mm, sharp from 2.0–9.0 m. Max 9 fps |
| **GNSS/IMU** | Applanix IN-Fusion+ / ProPoint. 2 × 336 tracking channels. IMU logs at 200 Hz, GNSS at 5 Hz |

*(MX60 UG Rev B, pp.13, 53–57)*

**Connectors** — one on the left, three on the right:

| Connector | Use |
|---|---|
| **Main** | Control Unit ← 5 m cable |
| **Ant.** | GAMS Antenna Kit |
| **DMI** | DMI Kit |
| **Ext.** | External devices — PPS, trigger, event, RS-232 |

*(MX60 UG Rev B, p.13)*

**Why you should care.** This is the expensive part and the accurate part. Its optics
must be clean, its mounting must be rigid, and it must have a clear view.

> **CAUTION**
>
> Two people are required to mount or dismount the Sensor Unit. Prepare the mount
> mechanism *before* lifting, and lift only by the dedicated handles.
> *(MX60 UG Rev B, pp.9, 10, 16; QSG Rev B, p.5)*

**Common problems:**

| Symptom | Usually means |
|---|---|
| Dirty or hazy imagery | Lens glass needs cleaning — see §6 for the correct method |
| Missing data low on one side | Sensor obstructed by the vehicle, or rack too far forward |
| Noisy cloud in dust | Consider the dust filter, but only on unpaved roads or mine sites |
| Sensor LED blinking red | Component failed — do not start a mission |

## 3.3 Control Unit (MX SCAN Control Unit 2)

**What it is.** The computer that runs the system and records the data.

> **CAUTION**
>
> The MX60 works **only** with Control Unit 2. Do not attempt to operate it with an
> older MX SCAN Control Unit — Trimble states this may damage the system.
> *(MX60 UG Rev B, p.20; QSG Rev B, p.6)*

**Front panel:**

| Item | Notes |
|---|---|
| Power In connector | From Power Unit |
| Sensor Unit connector | 5 m cable |
| **On/Off button** | **Hold ≥15 seconds** to start |
| **Status LEDs** ×3 | Control Unit, Sensor Unit, Wi-Fi |
| **2 × Exchangeable Data Disks** | 4 TB SSDs — see §3.7 |
| Wi-Fi USB stick 1 | System's own access point (operator device connects here) |
| Wi-Fi USB stick 2 | Connects the system *to* a network/hotspot |
| LAN | Operator device via Ethernet |
| WAN | Internet / remote support |
| USB 1 | Software load, licence update |
| USB 2 | **Trimble Support use only** |
| Fuses | Circuit breaker 1 = Control Unit, 2 = Sensor Unit, under the cover |

*(MX60 UG Rev B, pp.20–21)*

**LED meanings — learn these:**

| LED state | Meaning |
|---|---|
| Blinking green | Starting, updating, or shutting down |
| **Solid green** | **Ready** |
| **Blinking red** | **Component failed** |

*(MX60 UG Rev B, p.21)*

**Where to mount it.** Where the operator can reach the data disks *and* see the status
LEDs. The only hard constraint is the 5 m cable to the Sensor Unit.
*(MX60 UG Rev B, p.23)*

> **CAUTION**
>
> IP30 — not waterproof. Keep vent holes clear at all times.
> *(MX60 UG Rev B, p.53; QSG Rev B, p.6)*

**If a circuit breaker trips:** reactivate it, but check every cable before turning the
system back on — the trip may have been caused by a damaged cable *(MX60 UG Rev B, p.21)*.

## 3.4 Power Unit

**What it is.** The interface between the vehicle battery and the system. It converts
power, filters out alternator spikes, and protects the vehicle battery.

**Battery Protect** — the behaviour to recognise in the field:

| Condition | Response |
|---|---|
| Below 10.5 V for >12 s | **Audible warning** |
| Below 10.5 V for >90 s | **Power cut off** |
| Rises above 12.0 V within those 90 s | Normal status recovered |

*(MX60 UG Rev B, p.27)*

> **WHY THIS MATTERS**
>
> That audible warning is a 78-second countdown to losing the mission. If you hear it,
> get the engine running and the alternator charging — don't finish the run first.

**Power requirements:** 12–16 V DC. 9 A standby, 12 A operating, **25 A at startup**.
Trimble's Quick Start Guide asks for a **30 A or greater supply** and recommends an
auxiliary battery. Minimum vehicle battery 60 Ah.
*(MX60 UG Rev B, pp.52, 61; QSG Rev B, p.4)*

> **CAUTION**
>
> Never cover the Power Unit — it has vents on the back and bottom and will overheat.
> Install it in a dry place, secured through its three mounting points.
> *(MX60 UG Rev B, pp.25, 28)*

If the system is used daily, the Power Unit can stay connected to the vehicle. If it
will sit unused for a long period, disconnect it to save the vehicle battery
*(MX60 UG Rev B, pp.25–26)*.

## 3.5 Roof rack

**Two different racks exist.** Confirm which one you have before any lever-arm work.

| | **MX SCAN Roof Rack** | **MX Shock Absorbing Mounting Rack** |
|---|---|---|
| Weight | 18 kg | 28 kg |
| Mounts to | Square-cut universal roof bars, ≤85 × 30 mm | Prepared level platform / aluminium T-slot profile |
| Fixings | Bracket screws | M6 (20 × 6.6 mm holes) or M8 (16 × 9.0 mm holes) — all holes of one type must be used |
| Intended for | Standard road vehicles | "Harsher environments than a standard road" |
| Limits | Overhang ≤330 mm; bracket spacing ≥650 mm | Platform must be level; screws min A2-70 or class 8.8 |

*(MX60 UG Rev B, pp.29–33, 52; Rack UG Rev B, pp.6–7, 9)*

> **CAUTION**
>
> Both racks carry the **External Reference Point**, but the GAMS corner offsets
> published in the MX60 User Guide (X = +1.006 m, Y = −0.469 m, Z = +0.025 m) apply to
> the **standard Roof Rack only**. Do not use them with the shock absorbing rack.
> *(MX60 UG Rev B, p.68)*

**Positioning:** as far to the rear of the vehicle as possible, so the laser and the
backward/downward camera have a clear line of sight to the road surface, unobstructed by
the vehicle *(QSG Rev B, p.4)*.

**Maintenance:** clean and re-lubricate the lock bars and fast-lock mechanism frequently;
spray oil after cleaning *(MX60 UG Rev B, p.49)*.

## 3.6 Operator device

Not supplied by Trimble — bring your own.

| Requirement | Detail |
|---|---|
| Display | 10" or larger, touch preferred |
| Browser | **Google Chrome** — other browsers untested |
| Connection | Ethernet (DHCP: obtain IP and DNS automatically) or Wi-Fi |
| Software | **None.** TMI runs entirely in the browser at `http://tmi.mx-scan.net` |

*(MX60 UG Rev B, pp.13, 36; QSG Rev B, pp.3, 8)*

**Wi-Fi:** SSID is `Trimble MX60 (<serial number>)`. The password is on stickers inside
the Control Unit top case — **unique per system and not changeable**
*(MX60 UG Rev B, p.37)*.

> **FIELD TIP**
>
> Photograph the Wi-Fi sticker and keep it somewhere you can find it. It cannot be reset,
> and it lives in a case that may not be in the vehicle.

## 3.7 Storage media

**2 × 4 TB removable SSDs**, and they are not interchangeable in content:

| Disk | Records |
|---|---|
| **SSD 1** | Laser 1 and 2, navigation (GNSS + IMU), panoramic camera |
| **SSD 2** | Down-facing camera |

*(MX60 Spec Sheet p.3; QSG Rev B, p.8)*

> **IMPORTANT**
>
> Both disks are needed for a complete mission. SSD 1 holds the navigation data — without
> it there is no trajectory, and without a trajectory the imagery on SSD 2 is worthless.
> Treat them as one dataset.

> **CAUTION**
>
> **Never connect the USB cable while an exchangeable data disk is inside the Control
> Unit.** Remove the disk first. *(MX60 UG Rev B, p.10)*

Data comes off via the **MX SCAN Data Carrier Dock** (two supplied) over USB 3 — see §11.

## 3.8 Optional accessories

### GAMS (GNSS Azimuth Measurement System)

A second GNSS antenna. Because the system can then see the *orientation* of the baseline
between two antennas, it works out heading far faster than a single antenna can.

**Effect on the field procedure:** GAMS "not only is the initialization time reduced but
also **no special driving maneuvers are necessary** to complete initialization"
*(MX60 UG Rev B, p.67)*.

| Use case | Offset accuracy needed | Baseline |
|---|---|---|
| Collection only | 10 cm or better | — |
| **Post-processing the navigation data** | **A few millimetres** | **≥2.0 m** |

Both antennas **must be the same type** *(MX60 UG Rev B, p.68)*.

> **IMPORTANT**
>
> GAMS offsets must be re-measured **every time** the antenna is re-installed for a new
> mission. *(MX60 UG Rev B, p.67)*

### DMI (Distance Measuring Indicator)

A mechanical wheel odometer. Improves accuracy in challenging GNSS conditions and in
heavy stop-and-go traffic, and supplies **ZUPT** (zero velocity update) information for
navigation post-processing.
*(MX60 UG Rev B, p.42; MX60 Spec Sheet p.4)*

> **CAUTION**
>
> The DMI must be fitted to a **non-steering wheel**, and its lever arm is measured to
> the centre of the tread where that wheel contacts the road. A DMI on the **left** wheel
> has a **negative Y** lever arm. *(MX60 UG Rev B, p.46)*

> **PARAMETRIX DECISION REQUIRED**
>
> Confirm whether GAMS and DMI are owned, and whether they are fitted as standard.
>
> *Recommended practice:* fit both. GAMS removes an initialization step the operator can
> get wrong; DMI protects the trajectory exactly where mobile mapping is weakest.

## 3.9 Delivered items

| Case | Contents |
|---|---|
| **Box 1** — Sensor Unit transport case (806 × 716 × 634 mm) | Sensor Unit; Control-Unit-to-Sensor-Unit cable 5 m; hex wrenches 5 and 6 |
| **Box 2** — 75 kg, 1170 × 770 × 500 mm | Roof Rack; Power Unit; Control Unit 2 (with Wi-Fi sticker labels, SSD keys, 2 × Wi-Fi sticks, Quick Start Guide, SSD installed); 2 × Data Carrier Dock; Source-to-Power-Unit cable 5 m; Power-Unit-to-Control-Unit cable 3 m |

*(MX60 UG Rev B, pp.38–40; QSG Rev B, p.3)*

**Trimble's use assumptions** — worth knowing, because they shape the procedures:

- Roof Rack: **permanently** installed on the vehicle
- Power Unit and its source cable: **permanently** installed inside
- Control Unit: **temporarily** installed, for operation
- Sensor Unit: **temporarily** installed, removed for transfer and stored in its case
- GAMS and DMI: removed for transfer and storage

*(MX60 UG Rev B, p.41)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether Parametrix follows Trimble's assumptions — particularly whether the
> Sensor Unit is removed and cased at the end of each day.
>
> *Recommended practice:* follow them. Removing the Sensor Unit protects a very
> expensive item from weather, theft, and low-clearance accidents, and Trimble's storage
> instructions assume it. Note that removing the Sensor Unit means removing GAMS too,
> which means re-measuring its lever arm next time.

---

## References — Section 3

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 10, 12–13, 16, 20–21, 23, 25–29, 31–33, 36–42, 46, 49, 52–57, 61, 67–68 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 3–6, 8 |
| Trimble MX60 Spec Sheet, PN 022516-737C (04/25) | 2–4 |
| Trimble MX Shock Absorbing Mounting Rack User Guide, Rev B, May 2025 (P/N 37000001) | 6–7, 9 |


---

# 4. WORKFLOW AT A GLANCE

The whole job, start to finish. Each step points at the section that covers it properly.

## 4.1 The short form

```
OFFICE          Plan route ─── Check almanac ─── Prepare SSDs & field protocol
                                      │
VEHICLE         Mount ─── Measure ─── Power up ─── Connect TMI ─── Configure
                                      │
FIELD           Park open sky ─── INITIALIZE ─── Record runs ─── FINALIZE
                                      │
OFFICE          Offload ─── Back up ─── Trajectory ─── Point cloud ─── QC ─── Extract
```

**The two ends matter most.** Initialization at the start and finalization at the end are
mirror images of each other, and both are non-negotiable. Everything between them is
driving.

## 4.2 Step by step

### Before you leave the office

| # | Step | Section |
|---|---|---|
| 1 | Plan the route, passes, and direction of travel | 5 |
| 2 | **Check the satellite almanac** — `gnssplanning.com/#/charts` | 5 |
| 3 | Identify initialization locations — open sky, at both ends | 5, 8 |
| 4 | Mechanical check: mounting, screws, torques | 6 |
| 5 | Check system settings — lever arms, sensor settings | 6 |
| 6 | Prepare SSDs and the field protocol form | 6, 11 |

*(QSG Rev B, p.14)*

### At the vehicle

| # | Step | Section |
|---|---|---|
| 7 | Safety check — Trimble's components checklist | 6 |
| 8 | Clean all optics | 6 |
| 9 | Confirm the Vehicle Preset matches this vehicle and setup | 6, 7 |
| 10 | Turn off engine auto start/stop | 7 |
| 11 | **Start the vehicle**, then power on the system (hold ≥15 s) | 7 |
| 12 | Wait for solid green LEDs — about 10 seconds of blinking first | 7 |
| 13 | Connect the tablet, open `http://tmi.mx-scan.net` in Chrome | 7 |
| 14 | Select or create Vehicle and Capture presets | 7 |

*(QSG Rev B, pp.8–10)*

### Starting the mission

| # | Step | Section |
|---|---|---|
| 15 | Park in **open sky**, good GNSS visibility and PDOP | 8 |
| 16 | Start the mission, enter mission and area name | 8 |
| 17 | **Stay still 2–3 minutes** logging static data | 8 |
| 18 | Drive straight ~20 m — NAV status goes red → orange | 8 |
| 19 | Vary speed and make 2–3 dynamic turns — orange → **green** | 8 |
| 20 | Allow up to 10 more minutes before logging | 8 |

*(QSG Rev B, pp.11–12, 14)*

> **IMPORTANT**
>
> Navigation alignment must complete before data logging is allowed. Do not try to work
> around this — it is the system protecting you. *(QSG Rev B, p.11)*

### Collecting

| # | Step | Section |
|---|---|---|
| 21 | Press **Record** — button turns green → red | 9 |
| 22 | Drive the route: smooth, ≤80 km/h recommended, correct lanes | 9 |
| 23 | **Watch status while driving** — NAV, laser, cameras, storage, power | 9 |
| 24 | Press Record again to stop a run — red → green | 9 |
| 25 | Repeat for each run. **Minimum mission time 30 minutes** | 9 |

*(QSG Rev B, pp.12–14)*

> **FIELD TIP**
>
> Record only project-specific areas *(QSG Rev B, p.13)*. GNSS and IMU logging continues
> for the whole mission regardless — stopping the recording stops laser and imagery, not
> the trajectory.

### Ending the mission

| # | Step | Section |
|---|---|---|
| 26 | Drive to an initialization point (open sky), making dynamic manoeuvres on the way | 10 |
| 27 | **Dynamic steering → vary speed → drive straight → 2–3 min static** | 10 |
| 28 | Close the mission | 10 |
| 29 | Shut down the system | 10 |
| 30 | Wait for the power button light to go out — **up to 90 seconds** | 10 |
| 31 | Check the field protocol: order of runs, direction, date, mission, system S/N | 10, 11 |

*(QSG Rev B, pp.13–14)*

### Back at the office

| # | Step | Section |
|---|---|---|
| 32 | Unlock and remove both SSDs | 11 |
| 33 | Offload via the Data Carrier Docks over USB 3 | 11 |
| 34 | **Verify the transfer, then back up before doing anything else** | 11 |
| 35 | Prepare SSDs for the next mission | 11 |
| 36 | Process the trajectory (POSPac / TBC) | 12 |
| 37 | Generate and register the point cloud, colorize | 12 |
| 38 | QC against independent check points | 13 |
| 39 | Extract features and deliver | 12 |
| 40 | Archive source data | 11 |

*(QSG Rev B, pp.13, 15)*

## 4.3 The symmetry rule

The start and end sequences are deliberate mirror images:

| Start | End |
|---|---|
| 2–3 min static | dynamic steering |
| drive straight | vary speed |
| vary speed | drive straight |
| dynamic steering | 2–3 min static |

*(QSG Rev B, p.13)*

> **WHY THIS MATTERS**
>
> Trimble states that symmetrical collection at both ends "supports forward and reverse
> processing modes in the office software (TBC or POSPac), obtaining a good
> initialization" *(QSG Rev B, p.13)*.
>
> Office software processes the trajectory in both directions and blends the results. A
> good initialization at *both* ends means both passes start well, and the weakest part
> of the trajectory — the middle — gets solved from two strong ends instead of one.
>
> Skipping the end sequence does not ruin the mission, but it removes half the strength
> from the solution, and you cannot add it back later.

## 4.4 What a normal day looks like

A realistic sequence for a corridor project:

1. **Office, morning.** Route planned, almanac checked, SSDs formatted, protocol printed.
2. **Mobilise.** Sensor Unit out of its case, mounted, cabled. Optics cleaned. 20 minutes.
3. **Drive to site.** System off. Sensor Unit may stay mounted for a short transfer.
4. **Initialization point.** Open sky, away from buildings. Power up, connect, configure.
5. **Initialize.** Static, straight, manoeuvres, wait for green. **10–20 minutes.**
6. **Collect.** Runs recorded pass by pass, with the operator watching status.
7. **Return to an initialization point.** Finalize sequence, close mission, shut down.
8. **Demobilise.** Sensor Unit off the roof and into its case.
9. **Office.** Offload, verify, back up.

> **FIELD TIP**
>
> Budget the initialization honestly. Between the static period, the manoeuvres, and the
> advised settling time, **the first 20 minutes of a mission produce no data**. Crews new
> to mobile mapping consistently underestimate this and start recording too early.

## 4.5 Things that end a collection early

| Situation | What happens |
|---|---|
| NAV status never reaches green | Cannot log. Re-initialize; consider a better location |
| Battery Protect audible warning | 78 seconds to restore charge before power is cut |
| Blinking red LED | Component failed — do not continue |
| SSD full | Recording stops |
| Mission under 30 minutes | Below Trimble's stated minimum |
| Heavy rain | Trimble says avoid operating in rainy or misty weather |

Section 14 covers troubleshooting properly.

---

## References — Section 4

| Source | Pages |
|---|---|
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 8–15 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 27, 49, 53 |


---

# 5. PRE-FIELD PLANNING

This section covers only what is different about planning a *mobile mapping* job. It
assumes you already know how to plan a survey.

The short version: **you are planning a drive, not a set of setups.** Almost every
decision here is about where the vehicle goes, when, and how many times.

## 5.1 Route and passes

### How many passes

Trimble's documents do not specify a pass count. Queensland TMR's guideline does, and it
is the most defensible standard available:

> A minimum of **three passes** shall be run on the pavement.
> *(TMR MLS Guideline §8, p.8)*

The reasoning matters more than the number:

- **Redundancy** — three observations of the same surface let you detect a bad one
- **Changing constellation** — passes separated in time see a different GNSS geometry,
  which reduces the effect of multipath
- **Shadowing** — a truck blocking the curb on pass 1 is somewhere else on pass 3

> **IMPORTANT**
>
> TMR is explicit that a **multi-scanner system does not escape this**. Two scanners
> capturing simultaneously share one GNSS constellation and one trajectory, so they
> provide coverage redundancy but **not positional redundancy**:
>
> > "On MLS vehicles using multiple scanners to give the multiple aspect coverage in one
> > pass by capturing two or more scans at the one time, these scans do not use
> > independent GNSS constellations. In this case, a minimum of three independent passes
> > are still generally required."
> > *(TMR MLS Guideline §8, p.8)*
>
> The MX60 has two scanners. Plan passes as though it had one.

> **PARAMETRIX DECISION REQUIRED**
>
> Set the Parametrix minimum pass standard, and who may authorise fewer.
>
> *Recommended practice:* adopt three passes as standard for survey-grade work. TMR
> permits fewer only by prior agreement and warns that "extreme caution should be
> exercised and is NOT a recommended practice" *(§8, p.8)*. Allow reduction only with
> written approval from the project surveyor, recorded in the survey report.

### Pass patterns by roadway type

| Roadway | Minimum pattern |
|---|---|
| **Single carriageway, multiple lanes** | One pass each direction, plus a third in either direction |
| **Single carriageway, divided lanes** | If scans from each direction don't fully overlap, three passes per direction |
| **Dual carriageway** | If carriageways don't fully overlap, three passes each; at least one run in the left-hand through lane of each carriageway |
| **Any lane not fully overlapped by the adjacent lane's scan** | Three passes of that lane |

*(TMR MLS Guideline §8.1, pp.9–10)*

### Direction of travel

Plan it, and record it. The field protocol requires the **order and direction of runs**
*(QSG Rev B, p.14)*.

Direction matters because the sensor's view is asymmetric in practice — a curb, a sign
face, or a barrier is seen well from one direction and poorly from the other. Two-way
coverage is what fills those shadows.

> **FIELD TIP**
>
> Drive the lane closest to what you care about. If the deliverable is curb-and-gutter,
> the outside lane gives you a much better look at it than the inside lane does.

## 5.2 GNSS planning

This is the one piece of conventional survey planning that changes materially.

### Check the almanac

Trimble builds this into their own office checklist:

> Check satellite almanac (`www.gnssplanning.com/#/charts`)
> *(QSG Rev B, p.14)*

You are looking for windows of good satellite count and low PDOP over your corridor,
and — just as importantly — **avoiding** windows where the constellation is weak.

> **WHY THIS MATTERS**
>
> In static GNSS work a poor window costs you time. In mobile mapping it costs you the
> whole run, because you cannot go back and reoccupy — the vehicle has already driven
> the corridor and everything it collected inherited that geometry.

### Identify initialization locations

You need **open sky at both ends of the mission** — one to initialize, one to finalize.

Requirements *(QSG Rev B, pp.11, 14)*:

- Good GNSS visibility and PDOP
- Away from high buildings and obstructions that reduce reception and increase multipath
- Somewhere you can **safely sit still for 2–3 minutes**
- Room to drive straight ~20 m and perform 2–3 dynamic turns

Good candidates: large parking lots, wide intersections in open areas, rural road ends,
highway rest areas.

> **FIELD TIP**
>
> Scout initialization points on aerial imagery before you mobilise, and pick two —
> primary and backup. Discovering that your chosen lot is fenced, occupied, or under a
> canopy of trees costs 20 minutes at the worst moment of the day.

### Map the GNSS-hostile stretches

Walk the route on imagery and mark:

- Tunnels and long underpasses
- Urban canyon — tall buildings both sides
- Heavy tree canopy
- Deep cuts and overhead structures

For each, estimate **how long the vehicle will be under it at collection speed.** That
duration is the number that matters, not the length.

| Outage duration | Expectation |
|---|---|
| Brief (seconds) | IMU bridges it comfortably |
| **60 seconds** | Trimble publishes degraded but specified performance: X,Y 0.10–0.12 m, Z 0.07–0.10 m *(MX60 UG Rev B, p.56)* |
| Well beyond 60 s | Outside published specification — treat as a planning problem, not a driving problem |

> **IMPORTANT**
>
> Trimble specifies positioning performance at no outage and at a **60-second** outage.
> They publish nothing beyond that. A two-minute tunnel is not "twice as bad as one
> minute" — IMU drift is not linear, and you are extrapolating past the manufacturer's
> stated envelope.
>
> Plan long outages deliberately: a DMI, extra passes from both directions, or
> conventional survey supplementation. Section 13 covers the consequences.

TMR places responsibility squarely on the operator here:

> "It is the responsibility of the MLS contractor to increase the number of passes or
> implement other strategies in poor GNSS environments. These areas shall be reported to
> the project manager and noted in the survey report."
> *(TMR MLS Guideline §8.2, p.10)*

## 5.3 Timing

Three separate clocks constrain when you collect.

| Constraint | Window | Source |
|---|---|---|
| **Satellite geometry** | Whenever PDOP is good | QSG p.14 |
| **Imagery lighting** | Avoid early morning and late afternoon — **8am–4pm usually ideal** | TMR §10, p.15 |
| **Traffic** | Whenever the road is least occluded | — |

These frequently conflict. A good GNSS window at 7am is useless if the imagery is a
deliverable.

> **FIELD TIP**
>
> If imagery is not a deliverable and shadowing is the main problem, **night collection**
> is a legitimate tool. TMR explicitly permits it for parked-vehicle occlusion:
>
> > "If there is a problem with parked vehicles in urban areas, then consideration should
> > be given to scanning at night when parked vehicles may be absent."
> > *(TMR MLS Guideline §9.3, p.12)*
>
> LiDAR does not need daylight. Cameras do.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the Parametrix position on night collection: when it is permitted, what
> additional safety measures apply, and how the loss of usable imagery is handled with
> the client.
>
> *Recommended practice:* permit night collection where imagery is not a deliverable and
> parked-vehicle occlusion would otherwise force recollection. Require it to be agreed
> with the client in advance, because the imagery *will* be unusable for interpretation.

## 5.4 Weather

Weather is a go/no-go decision, not a driving adjustment.

| Condition | Guidance | Source |
|---|---|---|
| **Rain or mist** | **Avoid operating the system** | MX60 UG Rev B, p.49 |
| Wet pavement | Degrades laser returns; standing water may give no return at all | TMR §9.1, p.11 |
| Heavy dew | Affects point cloud quality | TMR §9.1, p.11 |
| Wet conditions for imagery | Make a considered effort not to capture; water on the lens is grounds for rejection | TMR §10, p.15 |
| Extreme dust | Dust filter available — unpaved roads and mine sites only | Dust Filter Bulletin, p.1 |
| Direct sun, stationary or <10 km/h | Outside the rated operating envelope | MX60 UG Rev B, p.53 |

> **CAUTION**
>
> The Control Unit and Power Unit are **IP30** — not waterproof. They live inside the
> vehicle for a reason. *(MX60 UG Rev B, p.53)*

> **PARAMETRIX DECISION REQUIRED**
>
> Write one clear wet-weather rule. Trimble says avoid operating in rain or mist; TMR
> says don't capture imagery in wet conditions; neither defines "wet."
>
> *Recommended practice:* no collection during active precipitation. After rain, wait
> until the pavement is visibly dry before collecting, and note conditions in the field
> protocol. Give the operator explicit authority to stand down without seeking approval.

## 5.5 Access, traffic and safety

Mobile mapping removes the crew from the roadway, but it does not remove the vehicle.

**Plan for:**

- **Legal and physical access** to every part of the corridor — gated roads, private
  drives, restricted areas
- **Turnarounds** — cul-de-sacs, medians, where a U-turn is legal
- **Traffic control**, if any pass requires an unusual manoeuvre or speed
- **Total vehicle height.** The system adds height, and the driver must know the new
  clearance *(MX60 UG Rev B, p.9)*
- **Safe stopping locations**, for initialization and for problems

> **CAUTION**
>
> The system adds significant height to the vehicle. Check clearances on the planned
> route — low bridges, parking structures, drive-throughs, and the shop door at the
> office. *(MX60 UG Rev B, p.9)*

> **PARAMETRIX DECISION REQUIRED**
>
> Define traffic control requirements by roadway class, and the go/no-go criteria for
> collecting without it.
>
> *Recommended practice:* no traffic control needed where the vehicle travels at or near
> the prevailing speed in a normal lane. Require a traffic control plan wherever the
> collection speed would be materially below prevailing traffic, or where a pass requires
> stopping, reversing, or occupying a shoulder.

## 5.6 Control planning

Detail is in Section 13. At the planning stage you need to decide two things.

**1. What service level is this?**

TMR distinguishes two, and conflating them is expensive:

| Service level | Control approach |
|---|---|
| **Survey-grade** | Full project reference frame, base stations, ground control points, check points |
| **Asset-grade** | A "GNSS only solution" — appropriate "where asset information is the primary objective," minimising initial control cost while keeping enough rigour to post-control later if needed *(TMR §11, p.17)* |

**2. Where does control go?**

TMR requires, at minimum:

- A ground control point **adjacent to the start and end** of the project
- A ground control point at **all intersections of state-controlled roads** within the
  project area, so future collections match

*(TMR MLS Guideline, Appendix E, p.31)*

Short baselines between base station and vehicle give the best positional outcome
*(TMR §5.2, p.6; §7.2, p.8)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the Parametrix control standard for mobile mapping: base station strategy
> (own base, VRS, RTX, or CORS post-processing), maximum baseline length, control point
> spacing, and independent check point density.
>
> *Recommended practice:* own base stations on project control, with baselines kept
> short. Control at both project ends and at every significant intersection. Independent
> check points at a spacing set per project, placed in **both good and poor GNSS
> environments** — TMR's stated intent is "to gather an understanding of the accuracies
> achieved in areas of both good and poor GNSS coverage" *(Appendix F, p.32)*, which is
> exactly what you need to know.

## 5.7 The calibration site

Boresight calibration needs a **specific drive**, not a normal collection, and the site
has to meet real geometric requirements. Plan it once and reuse it.

**What the crew must collect** — four runs over one crossroad:

| Run | Direction |
|---|---|
| Run_0 / Run_1 | Along the first road, forward and backward |
| Run_2 / Run_3 | Along the crossing road, forward and backward |

**Site requirements** *(TBC Help: Calibrate Mobile Mapping Laser Scanners)*:

| Requirement | Value |
|---|---|
| Crossing angle | As near **90°** as possible, within **±30°** |
| Run length | ≥ **20 m each side** of the crossing; ideally **80 m total, 40 m each side** |
| Overlap | Sufficient between runs |
| **Façades** | Present **in each direction**, in sufficient quantity |
| Vegetation | **Few or none** |

> **WHY THIS MATTERS**
>
> Boresight angles are solved by comparing the same surfaces seen from opposing
> directions. Flat façades make an angular error show up as a visible gap between two
> point clouds; pavement viewed at a grazing angle barely constrains it. The orthogonal
> pair supplies the axes a single road cannot. Vegetation is excluded because soft,
> non-repeating returns add noise to exactly that comparison.

> **FIELD TIP**
>
> A quiet crossroad with buildings on all four approaches, few trees, and room for 40 m of
> clean run each way is not common. Find one, record it, and use it every time.

Section 12.3 covers what happens to the data afterwards.

> **PARAMETRIX DECISION REQUIRED**
>
> Identify and record a standard Parametrix calibration site meeting the requirements
> above.
>
> *Recommended practice:* scout one near the office, document it with an aerial image and
> the four run lines, and note it in the field protocol whenever a calibration mission is
> driven.

## 5.8 Identify what mobile mapping will not get

Do this at planning, not at delivery.

Walk the corridor on imagery and mark anything that will need conventional survey:

- Features behind barriers, walls, or dense vegetation
- Drainage structures — invert elevations, pipe sizes, anything inside a structure
- Deep ditches and steep side slopes below the sensor's line of sight
- Anything under permanently parked vehicles
- Monuments and boundary evidence
- Areas the vehicle cannot reach

> **WHY THIS MATTERS**
>
> This list is not a shortcoming to be hidden. It is a scope item to be priced. A project
> that discovers it needs conventional supplementation *after* the mobile mapping crew has
> demobilised pays for two mobilisations.

Section 13 covers the full picture of what the system can and cannot see.

## 5.9 Planning checklist

| ☐ | Item |
|---|---|
| ☐ | Project limits defined and mapped |
| ☐ | Route, pass count, and direction of travel planned per pass |
| ☐ | Satellite almanac checked for the collection window |
| ☐ | Two initialization locations identified — primary and backup, both ends |
| ☐ | GNSS-hostile stretches mapped, with estimated outage duration |
| ☐ | Strategy for each long outage — passes, DMI, or supplementation |
| ☐ | Collection window reconciled against lighting and traffic |
| ☐ | Weather forecast checked; stand-down criteria understood |
| ☐ | Access confirmed; turnarounds identified |
| ☐ | Vehicle height clearances checked on route |
| ☐ | Traffic control decided |
| ☐ | Service level agreed — survey-grade or asset-grade |
| ☐ | Control and check point plan set |
| ☐ | Conventional supplementation identified and scoped |
| ☐ | Calibration site identified, if a calibration mission is due |

---

## References — Section 5

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 49, 53, 56 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 11, 14 |
| Trimble Business Center Help: *Calibrate Mobile Mapping Laser Scanners* | help.fieldsystems.trimble.com/tbc/20716.htm |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 1 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §5.2 p.6; §7.2 p.8; §8 p.8; §8.1 pp.9–10; §8.2 p.10; §9.1 p.11; §9.3 p.12; §10 p.15; §11 p.17; App E p.31; App F p.32 |


---

# 6. EQUIPMENT PREPARATION AND VEHICLE INSTALLATION

Everything from "the system is in its case" to "ready to switch on."

## 6.1 How often each task happens

Read this table first. It is the reason this section is organised the way it is.

| Frequency | Tasks | Who |
|---|---|---|
| **Once, or when the vehicle changes** | Power supply installation, roof bar fitting, Power Unit mounting, rack positioning | **Trained personnel** + professional automotive electrician |
| **When the setup changes** | Lever-arm measurement (GAMS/DMI only), Vehicle Preset creation, Wi-Fi country setting | **Trained personnel** |
| **Every project** | Confirm installation height, confirm correct Vehicle Preset | Operator |
| **Every day / every mission** | Safety check, components checklist, optics cleaning, cable inspection | Operator |

> **CAUTION**
>
> Trimble requires that anyone installing or removing the system be familiar with the
> installation chapter of the Trimble manual **and have received prior training**.
> Operation and service may only be performed by properly trained personnel.
> *(MX60 UG Rev B, pp.7, 9, 10)*

## 6.2 One-time installation

Performed once per vehicle. Not an operator task.

### Power supply

> **CAUTION**
>
> Any installation and integration of a power supply in a vehicle **must be done by a
> professional car electrician service** and is under the customer's responsibility and
> control. All components — cable type, gauge, fuses, relay — must comply with the MX60
> input power requirements and with local law and vehicle regulations.
> *(MX60 UG Rev B, p.61)*

| Requirement | Value |
|---|---|
| Input voltage | 12–16 V DC |
| Current at startup | **25 A at 12.8 V** (320 W) |
| Current in operation | 12 A (160 W) |
| Supply rating needed | **30 A or more** |
| Battery capacity | **60 Ah minimum** |
| Auxiliary/buffer battery | **Recommended** |
| Direct-connection fuse | 35 A, close to the battery |

*(MX60 UG Rev B, pp.52, 61–62; QSG Rev B, p.4)*

Trimble documents two setups — direct connection (car battery only) and buffer battery
(recommended). Both use a relay that supplies power only when the alternator is running,
preventing the car battery from going flat *(MX60 UG Rev B, p.62)*.

> **CAUTION**
>
> On vehicles using electric propulsion, install the product so it is **fully separate
> from the car battery charging system**. *(MX60 UG Rev B, p.8)*

### Vehicle requirements

| Requirement | Detail |
|---|---|
| Wheels and use | Rubber wheels, paved roads only |
| Body | Hatchback with upright rear door |
| **Roof height** | **Minimum 1.60 m** — required by the down-looking camera's minimum distance |
| Colour | **Not bright** — avoids exposure artefacts in imagery |
| Start/stop | **Must be switched off** |
| Alternator | Sufficient power, or an additional battery pack |
| Roof rails | Withstand the load; ideally covering the entire roof so rack position can be adjusted |
| Interior room | Space for the Sensor Unit case (806 × 716 × 634 mm) and Control Unit case (453 × 255 × 408 mm) during transfer |

*(MX60 UG Rev B, p.59)*

### Mounting the Power Unit and Control Unit

Both live inside the vehicle and **neither is waterproof** (IP30).

**Power Unit** — three mounting points, 6 mm screws:

- Dry location
- Securely fastened
- **Always keep clear space around the vents on the back and bottom**
- Never cover it
- Consider cable routing: 3 m to the Control Unit

*(MX60 UG Rev B, p.28)*

**Control Unit** — position it where the operator can:

- Reach the **data disks**
- **See the status LEDs**

The only hard constraint is the 5 m cable to the Sensor Unit. It can be secured with
screws or through its two belt guides *(MX60 UG Rev B, p.23)*.

> **CAUTION**
>
> Ensure the vent holes in each unit are always uncovered.
> *(QSG Rev B, p.6)*

### Roof bars and rack

1. Park the vehicle in a **level location** *(QSG Rev B, p.4)*
2. Install two roof bars so the rack sits **as far to the rear as possible**
3. Remove the screw bridge; place the rack on the bars
4. Adjust bracket position so the rack is **as horizontal as possible**
5. Attach the screw bridge and tighten all screws

**Positioning limits:**

| Limit | Value |
|---|---|
| Distance between front and back brackets | **> 650 mm** (marked by a red stripe on the mainframe) |
| Back bracket to end of rack (overhang) | **≤ 330 mm** |
| Roof bar dimensions | Square cut, ≤ 85 mm wide × 30 mm high |
| Torque, screws No.5 | **8 Nm** |

*(MX60 UG Rev B, pp.29, 31–33; QSG Rev B, pp.4–5)*

> **IMPORTANT**
>
> The laser and the backward/downward camera must have a **clear line of sight to the
> road surface**, unobstructed by the vehicle. This is why the rack goes to the rear.
> *(QSG Rev B, p.4)*

### Tightening screws — the correct method

Trimble is specific about this, and it applies everywhere in the system.

**Standalone screws:** slow, continuous movement. No jerking. Comply strictly with the
stated torque value.

**Clusters:** tighten **crosswise in three steps**:

| Step | Torque |
|---|---|
| 1 | ~33% of final |
| 2 | ~66% of final |
| 3 | 100% of final |

Always tighten the screw opposite the last one. After the first pair, move to the next
adjacent pair.

> **IMPORTANT**
>
> After all screws reach final torque, **a second person must check the torque values.**
> *(MX60 UG Rev B, pp.10–11)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide how the second-person torque verification is recorded.
>
> *Recommended practice:* a dated sign-off on the installation record, naming both people.
> Repeat after any disassembly.

## 6.3 Lever arms and the Vehicle Preset

**Good news, and it simplifies this considerably:**

> The lever arms of the standard system are set by default in the MX60 system. Only the
> vehicle height needs to be saved once as a preset.
> *(QSG Rev B, p.7)*

So for a standard system with no accessories, there is **one measurement**: installation
height.

You measure lever arms **only** when GAMS or DMI are fitted.

### Installation height

**How to measure:**

1. Ensure the roof rack is **horizontally aligned** *(MX60 UG Rev B, p.47)*
2. Locate the **External Reference Point** — right side, at the back of the rack
   *(MX60 UG Rev B, p.45)*
3. Measure **strictly vertically** from that point down to the road surface
4. Record in metres, as an absolute value
5. Enter in TMI under **Settings → Vehicle settings → Install Height**

**Accuracy required: on the order of 1 cm** *(MX60 UG Rev B, p.47)*.

> **CAUTION**
>
> Using incorrect or poor measurement values in the Vehicle Preset **may result in faulty
> navigation solutions.** Make sure all values are entered correctly, and make sure you
> select the correct Vehicle Preset before starting a mission.
> *(MX60 UG Rev B, p.47)*

> **FIELD TIP**
>
> Vehicle loading changes this measurement. The dust filter bulletin warns that a heavily
> loaded vehicle, or one with soft suspension, needs this considered when measuring
> installation height *(Dust Filter Bulletin, p.2)*. Measure the vehicle in the condition
> it will be driven in — fuel, gear, and people aboard.

### GAMS lever arm — only if fitted

Measured to the **L1 antenna phase centre** of the secondary antenna.

| Intended use | Accuracy | Baseline |
|---|---|---|
| Collection only | 10 cm or better | — |
| **Post-processing navigation data** | **A few millimetres** | **≥ 2.0 m** |

Both antennas must be the **same type** *(MX60 UG Rev B, p.68)*.

**The practical method** *(MX60 UG Rev B, p.68)*: measuring from the GAMS antenna all the
way to the External Reference Point is awkward. Instead, measure the short distance to the
**top-left front corner** of the rack, then add the known fixed offsets:

| Axis | Known offset, corner → ERP | Your measurement |
|---|---|---|
| X | +1.006 m | + your value |
| Y | −0.469 m | + your value |
| Z | +0.025 m | − your value |

> **CAUTION**
>
> Those known offsets are published for the **Trimble standard Roof Rack**. Do not apply
> them to the MX Shock Absorbing Mounting Rack. *(MX60 UG Rev B, p.68)*

> **IMPORTANT**
>
> GAMS offsets must be re-measured **every time** the antenna is re-installed for a new
> mission. If the Sensor Unit comes off the roof at the end of each day, so does GAMS —
> and its lever arm is measured again the next morning. *(MX60 UG Rev B, p.67)*

### DMI lever arm — only if fitted

Measured to the **centre of the tread**, where the DMI-equipped wheel contacts the road.

> **CAUTION**
>
> - The DMI wheel **must be a non-steering wheel**
> - Use the correct **sign**. A DMI mounted on the **left** wheel has a **negative Y**
>   lever arm
>
> *(MX60 UG Rev B, p.46)*

### The Vehicle Frame

All lever arms are measured in the Vehicle Frame:

| Axis | Positive direction |
|---|---|
| **X** | Forward, in the driving direction |
| **Y** | **Right** side of the vehicle |
| **Z** | **Downward** |

*(MX60 UG Rev B, p.46)*

> **WHY THIS MATTERS — Z is down**
>
> Surveyors expect Z up. This frame has Z **down**. Get this wrong and the sign of every
> vertical lever arm inverts.

> **ADVANCED — why POSPac shows different numbers than you measured**
>
> The origin of the MX60 System Reference Frame is **not** the External Reference Point.
> TMI adds internal vectors to the lever arms you enter. In POSPac processing you will see
> corrected lever arm values that differ from your mechanical measurements.
>
> **This is correct behaviour, not an error.** *(MX60 UG Rev B, p.47)*

> **PARAMETRIX DECISION REQUIRED**
>
> Establish who measures lever arms, by what method, where the record is kept, and when
> re-verification is required.
>
> *Recommended practice:* lever-arm measurement is a trained-personnel task with a written
> record — date, who measured, method, values, and vehicle condition. Re-verify whenever
> the Sensor Unit, GAMS, DMI, or rack is disturbed. Keep the record with the project data,
> because a trajectory problem months later is often a lever-arm problem.

## 6.4 Mounting the Sensor Unit

> **CAUTION**
>
> **Two people are required.** The Sensor Unit weighs 24–28 kg depending on
> configuration. Prepare the mount mechanism *before* lifting, to prevent injury or damage.
> Lift only by the dedicated handles.
> *(MX60 UG Rev B, pp.9, 10, 16; QSG Rev B, p.5)*

**To install:**

1. Confirm the rack's **safety locks are open**. Use the tool stored in the Control Unit
   case.
2. Two people, one on each side, lift the Sensor Unit by its handles.
3. Let the **lower mounting bolts slide into** the lower mounting facilities of the rack.
4. As the lower bolts reach their final position, **tilt the Sensor Unit forward** until
   the upper mounting bolts **click** into place and the fast lock engages.
5. Once the upper bolts have clicked, the unit is stable and cannot turn over or fall.
6. **Tighten the safety locks** to close the lock bars.
7. The unit is now safe to cable.

*(MX60 UG Rev B, pp.16–18)*

**To remove:**

1. Remove cables
2. Open the safety locks
3. Release the fast locks by pressing the fast-lock button downwards
4. Turn the Sensor Unit while pressing the button, and free the upper mounting bolts
5. Lift out of the lower mounting facilities and place directly into its transport case

*(MX60 UG Rev B, p.19)*

## 6.5 Cabling

Three cables. Each has a defined route.

| # | Cable | Length | Connects |
|---|---|---|---|
| 1 | Source-to-Power-Unit | 5 m | Vehicle power → Power Unit |
| 2 | Power-Unit-to-Control-Unit | 3 m | Power Unit → Control Unit (power **and** signal) |
| 3 | Control-Unit-to-Sensor-Unit | 5 m | Control Unit → Sensor Unit |

*(MX60 UG Rev B, pp.34–35)*

**Connecting cable 3 — the one that needs care:**

1. Check you are holding the **correct end** — each end uses a specific connector type
2. Check the pins are in good state — **not bent or broken**
3. Connect the "Sensor Unit" end to the Sensor Unit
4. Slide in and secure by **turning the black lock screw** on top of the connector to the
   right
5. Install and secure the cable safely relative to the vehicle
6. Connect the "Control Unit" end and secure its lock screw the same way

*(MX60 UG Rev B, p.35)*

**Grounding:** connect the ground terminal of the **Power Unit** and the **Sensor Unit**
to the vehicle chassis. All ground connections are the owner's responsibility and depend
on the vehicle *(MX60 UG Rev B, p.34; QSG Rev B, p.7)*.

> **CAUTION**
>
> Cables must be **fixed to the vehicle roof rack before being led inside the cabin**, and
> secured with straps or binders so nothing can move during operation.
> *(MX60 UG Rev B, pp.9, 44)*

> **WHY THIS MATTERS**
>
> An unsecured cable at 80 km/h chafes, and the connector pins are rated for 1500 mating
> cycles but nothing at all for being yanked *(MX60 UG Rev B, p.35)*. A cable failure
> mid-mission ends the mission.

## 6.6 Daily safety check

Trimble requires a safety check **before and after each mission**
*(MX60 UG Rev B, p.44)*.

### Rules

- All broken or damaged components **exchanged immediately**
- All loose screws tightened, to the correct torque, by the correct method
- Any dirty or wet part cleaned or dried
- **Do not start a mission before solving any issue you had previously with the system.
  Not doing this may damage the system permanently.**

*(MX60 UG Rev B, p.44)*

### Components checklist

Trimble's own list, verbatim in substance *(MX60 UG Rev B, p.44)*:

| ☐ | Check |
|---|---|
| ☐ | Roof rack installed correctly |
| ☐ | All roof rack screws tightened |
| ☐ | Roof rack shows no cracks or deformation |
| ☐ | Sensor Unit damage-free — no scratches or deformation |
| ☐ | **All camera lenses clean and undamaged** |
| ☐ | Sensor in operation position and **properly locked** |
| ☐ | Control Unit free of damage or broken parts |
| ☐ | Control Unit installed correctly and secured |
| ☐ | Power Unit damage-free, no broken parts |
| ☐ | Power Unit secured, **air inlet and outlet free** |
| ☐ | All connectors plugged in and fixed |
| ☐ | Cables fixed to the roof rack before entering the cabin |
| ☐ | No cable damaged or liable to be damaged during operation |
| ☐ | User interface device operational |

### Cleaning the optics

Clean all sensor optics **before starting a mission**. Depending on weather and road
surface, cleaning **during** the mission may be necessary *(MX60 UG Rev B, p.10)*.

**Correct method** *(MX60 UG Rev B, p.50)*:

1. Work in a clean environment
2. First try to **blow debris off with an air compressor**
3. If that fails, apply a small amount of optics cleaner or ethyl alcohol to a clean lens
   cloth — **moist, not dripping**
4. Wipe along the length of the glass in smooth movements
5. **Do not press hard, and do not rub repeatedly on one spot**
6. If pooling or streaks appear, there is too much solution — wait for it to dry, repeat
7. Examine the surface in good light; repeat with a clean cloth if dust spots remain

> **FIELD TIP**
>
> Carry the cleaning kit in the vehicle, not the office. Road spray and insects are a
> mid-mission problem, and imagery with a dirty lens is grounds for rejection
> *(TMR MLS Guideline §10, p.15)*.

## 6.7 Before you leave the office

From Trimble's own checklist *(QSG Rev B, p.14)*:

| ☐ | Item |
|---|---|
| ☐ | System checked — mechanical, mounting, screws, torques |
| ☐ | System settings checked — lever arms, sensor settings |
| ☐ | Field protocol prepared |
| ☐ | SSDs prepared and available |
| ☐ | Satellite almanac checked |

Plus, from elsewhere in the Trimble documentation:

| ☐ | Item | Source |
|---|---|---|
| ☐ | **24 hours acclimatisation** completed, if the system has been air freighted | UG p.7 |
| ☐ | Wi-Fi country code set — **mandatory** before first use and in any new country | UG p.48; QSG p.2 |
| ☐ | Wi-Fi password sticker accessible | UG p.37 |
| ☐ | Cleaning kit aboard | UG p.10 |
| ☐ | System exercised recently — if idle >2 months, run 30–60 min | UG p.9 |

> **CAUTION — acclimatisation**
>
> After air freight transportation, allow **24 hours** in a place with constant
> temperature and air pressure before switching the system on. Condensation inside the
> housings can cause short circuits and damage the instrument when switched on.
> *(MX60 UG Rev B, p.7; QSG Rev B, p.2)*

> **PARAMETRIX DECISION REQUIRED**
>
> Create a standard Parametrix field protocol form. Trimble requires that it record the
> **order of runs, direction of runs, date, mission, and system serial number**
> *(QSG Rev B, p.14)*.
>
> *Recommended practice:* build a single-page form capturing Trimble's required fields
> plus operator name, vehicle, weather, installation height used, Vehicle Preset name,
> initialization location and time, and any events during collection. Store it with the
> project data.

---

## References — Section 6

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7–11, 16–19, 23, 28–29, 31–35, 37, 44–48, 50, 52, 59, 61–62, 67–68 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 2, 4–7, 14 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 2 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §10, p.15 |


---

# 7. STARTING THE SYSTEM AND TMI

From "the system is mounted" to "ready to initialize."

## 7.1 Power-up sequence

Order matters. Startup draws **25 A**, and the system asks for a 30 A supply
*(MX60 UG Rev B, p.61; QSG Rev B, p.4)*.

1. **Turn off the engine auto start/stop function**
2. Confirm both SSDs are **inserted and locked** in the Control Unit
3. **Start the vehicle**
4. **Then** press and hold the Control Unit power button for **at least 15 seconds**
5. Power Unit LED goes **constant green** once the vehicle is delivering 12 V
6. Sensor Unit and Control Unit LEDs **blink for about 10 seconds**
7. Both LEDs turn **solid green** — the system is ready

*(QSG Rev B, p.8; MX60 UG Rev B, p.21)*

> **CAUTION**
>
> Before starting, make sure all connections are secure and the recording SSDs are
> inserted and locked. *(MX60 UG Rev B, p.48; TMI UG Rev L, p.4)*

> **WHY THIS MATTERS — start the vehicle first**
>
> A 25 A startup surge on a battery with no alternator behind it is how you meet Battery
> Protect the hard way: audible warning below 10.5 V, power cut 90 seconds later
> *(MX60 UG Rev B, p.27)*.

**LED reference:**

| State | Meaning |
|---|---|
| Blinking green | Starting, updating, or shutting down |
| **Solid green** | **Ready** |
| **Blinking red** | **Component failed — do not start a mission** |

*(MX60 UG Rev B, p.21)*

## 7.2 Connecting to TMI

TMI is web-based. Nothing is installed on your device.

| | |
|---|---|
| **Browser** | Google Chrome — other browsers untested |
| **TMI.Capture** | `http://tmi.mx-scan.net` |
| **TMI.AI** (admin) | `http://admin.mx-scan.net` |

*(TMI UG Rev L, pp.7, 46)*

**Wi-Fi:** SSID `TrimbleMX60 (<serial number>)`. Password is on stickers shipped inside
the system — **unique per system, cannot be changed**. If lost, contact Trimble Imaging
Support with the serial number *(TMI UG Rev L, pp.5, 51)*.

**Ethernet:** patch cable to the Control Unit LAN port. Your device gets an IP by DHCP
*(TMI UG Rev L, p.5)*.

> **CAUTION — mandatory before first use**
>
> The **Wi-Fi country** must be set the first time the system is turned on, and again
> every time you start a collection campaign **in a different country**. This is a legal
> compliance requirement.
>
> `Settings → System Administration → WiFi → MX60 WiFi Access Point → <country>`
> *(TMI UG Rev L, pp.5, 51; MX60 UG Rev B, p.48)*

> **FIELD TIP**
>
> An Internet connection is optional but useful — it's what puts the OSM background map
> behind your trajectory *(TMI UG Rev L, pp.8, 32)*. Note you **cannot** use a hotspot
> that requires logging in through a web page *(TMI UG Rev L, p.51)*.

## 7.3 The TMI screen

| Button | What it does |
|---|---|
| ☰ | Main menu |
| ⏻ | Shut down the system |
| ⊗ | Close the mission in progress |
| ? | Help |
| Layers | Map layers |
| +/− | Zoom |
| ↻ | Map orientation — north vs. vehicle |
| ⊙ | Auto-centre on vehicle |
| Dashboard | System overview |
| **Camera** | Camera view — **colour-coded** |
| **Nav** | Navigation view — **colour-coded** |
| **Laser** | Laser view — **colour-coded** |
| 💬 | Comments — time-tagged to the mission timeline |
| ⚙ | Change capture settings mid-mission |
| **● Record** | **Red = logging, green = not logging** |

*(TMI UG Rev L, pp.8–9)*

### Status colours — learn these before you drive

**Camera and Laser buttons:**

| Colour | Meaning |
|---|---|
| Red | Device error |
| Orange | Device not yet time-synchronized |
| **Green** | **Time synchronization complete** |

**Navigation button** — different, and more important:

| Colour | Meaning | Can you record? |
|---|---|---|
| **Red** | No valid navigation solution, or navigation system failure | **No** |
| **Orange** | Navigation solution available | **Yes — but see below** |
| **Green** | Solution **meets your user accuracy requirements** | Yes |

*(TMI UG Rev L, pp.8–9, 25, 40)*

> **IMPORTANT — orange is not good enough**
>
> TMI *permits* recording at orange. Trimble's Quick Start Guide tells you to wait for
> **green** *(QSG Rev B, pp.12, 14)*.
>
> Orange means only that a solution exists. **Green means the solution meets the accuracy
> figures you set.** For survey-grade work, wait for green.

> **PARAMETRIX DECISION REQUIRED**
>
> State whether recording at orange NAV status is ever permitted.
>
> *Recommended practice:* prohibit it for survey-grade work. Permit it only for
> asset-grade collection, with the project surveyor's approval recorded in the field
> protocol.

## 7.4 What "green" actually means

The orange→green threshold is set in **Capture Settings → User Accuracies for
Navigation**, and Trimble ships different defaults per configuration:

| Parameter | MX60 **Premium** | MX60 **Core / Pro** |
|---|---|---|
| Attitude RMS (roll/pitch) | 0.060° | 0.075° |
| Heading RMS | 0.045° | 0.045° |
| Position RMS | 10.000 m | 10.000 m |
| Velocity RMS | 0.025 m/s | 0.030 m/s |

*(TMI UG Rev L, p.26)*

> **ADVANCED — read the position threshold again**
>
> Position RMS defaults to **10 metres**. That is deliberately loose. The green light is
> effectively driven by **attitude, heading and velocity** — the things initialization
> manoeuvres actually improve — not by absolute position.
>
> So green tells you the *orientation* solution has converged. It does not tell you the
> corridor will meet a centimetre-level positional spec. That is decided later, by
> post-processing, control and geometry. Section 13.

> **CAUTION**
>
> Changing these defaults "can ONLY be done by advanced users," and values must stay
> compliant with the navigation system in use. *(TMI UG Rev L, p.25)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether Parametrix uses Trimble's factory user-accuracy defaults or its own, and
> who may change them.
>
> *Recommended practice:* use factory defaults. Restrict changes to a named
> trained-personnel list, and record any change in the field protocol — a mission run
> against altered thresholds is not comparable to one run against the defaults.

## 7.5 Configuring the mission

### Vehicle settings

Describes how the sensor is mounted. Set once per vehicle setup and saved as a preset.

| Field | Notes |
|---|---|
| **Name** | Required — appears in the preset pull-down |
| Description | Optional |
| **Install Height** | From the External Reference Point on the rack to the road surface, in metres |
| **Use DMI** | Checkbox + lever arm XYZ, mounting position (left/right, driving direction as reference), **wheel diameter** |
| **Use GAMS** | Checkbox + lever arm XYZ |
| Use External Connector | Checkbox + trigger/event/COM configuration |

*(TMI UG Rev L, pp.20–24)*

> **CAUTION — the aiding-sensor trap**
>
> "If you do not activate an aiding navigation sensor here, the data from this sensor will
> **NOT be logged** during the mission, even though the required connections to the sensor
> unit may have all been made properly."
> *(TMI UG Rev L, p.21)*
>
> A DMI can be perfectly fitted, correctly measured, physically connected — and silently
> contribute nothing, because the checkbox is off. Nothing in the field will tell you.

> **FIELD TIP**
>
> Measure the DMI **wheel diameter** carefully *(TMI UG Rev L, p.21)*. It scales every
> distance the DMI reports. Tyre wear and pressure change it.

### Capture settings

What the sensors do. Can be changed mid-mission; vehicle settings cannot.

| Setting | Options |
|---|---|
| **Sensor selection** | Each laser and camera active or idle. **The navigation sensor is always active** |
| **User Accuracies for Navigation** | The orange→green thresholds above |
| **Camera trigger** | Distance Based (constant metres) or Fixed Frame Rate (constant fps). **Max 10 fps** |
| **Laser Mode** | Combination of measurements/second and rotations/second |
| **Enable Dust Filter** | Eliminates dust above the road surface |
| **Lateral Range Limit** | 5–50 m. Discards points beyond that distance perpendicular to travel. **Applies to both scanners** |

*(TMI UG Rev L, pp.25–29; QSG Rev B, p.10)*

> **CAUTION**
>
> Both the dust filter and the lateral range limit depend on **installation height being
> set correctly** in Vehicle Settings. Get it wrong and you lose data.
> *(TMI UG Rev L, p.29; Dust Filter Bulletin, p.2)*

> **IMPORTANT — check how your TMI version presents the laser setting**
>
> The Quick Start Guide (March 2025) describes two separate controls — *Measurement Prog*
> `[500 kHz, 1000 kHz]` and *Line Speed* `[120 Hz, 200 Hz]`. The TMI User Guide Rev L
> (April 2026) describes a single combined **Laser Mode** for the MX60.
>
> Rev L is the newer document. Confirm against your installed TMI version before relying
> on either. Note also that Trimble states the measurements/second values shown in the
> interface are **rounded** *(TMI UG Rev L, pp.28–29)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish standard capture presets and a naming convention — for example a default
> corridor preset, a dust preset, and an urban preset.
>
> *Recommended practice:* build named presets in advance and export them to file. TMI can
> export all presets to a single file and re-import them with Overwrite or Append
> *(TMI UG Rev L, pp.17–18)*, which gives you a backup and a way to put an identical
> configuration on a second system.

## 7.6 Disk check

At startup and after every mission, TMI checks the data disks. The result appears in the
**upper-right corner of the map window**, alongside UTC time and SSD fill status.

| Result | Meaning |
|---|---|
| **No icon** | Everything is fine |
| **Warning** | Mission can still run, but **data loss may occur under high system load** |
| **Error** | Disk performance is compromised; **proceeding may lead to data loss**. You must confirm to start |

*(TMI UG Rev L, pp.33–34)*

> **IMPORTANT**
>
> The **Start Mission button is disabled while a disk check is running** (Initializing /
> Analyzing). Wait for it. *(TMI UG Rev L, p.38)*

> **PARAMETRIX DECISION REQUIRED**
>
> Set the rule for proceeding past a disk Warning or Error.
>
> *Recommended practice:* never start a production mission on a disk reporting Error, and
> treat a Warning as grounds for swapping the disk before a long collection. A disk that
> fails under load fails in the middle of the corridor, not at the start.

## 7.7 Ready-to-initialize check

| ☐ | Item |
|---|---|
| ☐ | Both SSDs inserted and locked; disk check clean |
| ☐ | Control Unit, Sensor Unit LEDs **solid green** |
| ☐ | Power Unit LED constant green |
| ☐ | TMI open in Chrome, connected |
| ☐ | Wi-Fi country set (first use / new country) |
| ☐ | Correct **Vehicle Preset** selected — installation height matches this vehicle today |
| ☐ | DMI and/or GAMS **checkboxes activated** if fitted |
| ☐ | Correct **Capture Preset** selected |
| ☐ | Camera and Laser buttons green (time-synchronized) |
| ☐ | UTC time showing — GNSS initialization complete |
| ☐ | Vehicle parked in open sky for initialization |

---

## References — Section 7

| Source | Pages |
|---|---|
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 4–5, 7–9, 17–18, 20–29, 32–34, 38, 40, 46, 51 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 4, 8, 10, 12, 14 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 21, 27, 48, 61 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 2 |


---

# 8. INITIALIZATION

The most important twenty minutes of the day.

## 8.1 In plain language

Before the system can produce an accurate trajectory, the navigation solution has to
*converge* — it has to work out not just where the vehicle is, but exactly how it is
oriented, and how much its inertial sensors are drifting.

It cannot do that sitting still, and it cannot do it from GNSS alone. It needs to feel the
vehicle move in ways that reveal those unknowns.

**So you park in the open, sit still for a few minutes, drive straight, then deliberately
speed up, slow down and turn.** That's initialization. Do it at the start of every
mission, and again — in reverse — at the end.

## 8.2 The procedure

> **IMPORTANT**
>
> Navigation alignment must complete **before data logging is allowed**. This is the
> system protecting you, not an obstacle. *(QSG Rev B, p.11)*

### Step by step

1. **Park in an open-sky area** with good GNSS visibility and PDOP. Avoid high buildings
   and obstructions that reduce reception and increase multipath.
2. **Start the mission** — enter mission name and area name, select the Vehicle and
   Capture presets, press Next, then Start.
3. **Remain still for 2–3 minutes**, logging static data.
4. **Drive straight ahead for approximately 20 m**, with no large steering inputs.
   → NAV status switches **red → orange**.
5. **Vary speed and perform dynamic steering manoeuvres.** Typically **2–3 turns** are
   sufficient. Trimble's example speed profile:
   **0 → 50 → 20 → 50 → 20 km/h**
   → NAV status switches **orange → green**.
6. **Repeat until all navigation parameters are green.**
7. **Allow additional settling time — up to 10 minutes** — before logging data.

*(QSG Rev B, pp.11–12, 14)*

> **FIELD TIP — where to do it**
>
> You need room to sit still safely, drive straight ~20 m, and make 2–3 turns with speed
> changes. A large empty parking lot is ideal. Scout two locations before you mobilise;
> Section 5 covers this.

> **IMPORTANT — the settling time is not optional padding**
>
> "Depending on your working environment, the time period can vary for the system to
> resolve its ambiguities, so it is advised to add some time (up to 10 minutes) before
> logging data **to avoid poor results at the start of recording runs**."
> *(QSG Rev B, p.12)*
>
> Data logged immediately after the light turns green is the weakest data of the mission.
> If the first thing you record is the most important part of the corridor, you have put
> your worst solution on your most important asset.

### With GAMS fitted

GAMS changes this materially. With a second GNSS antenna the system can derive heading
directly from the baseline between antennas, so:

> "Using a GAMS, not only is the initialization time reduced but also **no special driving
> maneuvers are necessary** to complete initialization."
> *(MX60 UG Rev B, p.67)*

The Quick Start Guide is more measured: driving straight is "more important if a GAMS
antenna is not used," and the relevance of straight driving versus dynamic steering
"depends on the hardware used" *(QSG Rev B, p.12)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether the full manoeuvre sequence is performed even when GAMS is fitted.
>
> *Recommended practice:* perform it anyway. It costs a few minutes, it is what the Quick
> Start Guide's checklist describes, and it gives the office a strong initialization at
> both ends regardless of GAMS status. Skipping it saves little and removes redundancy you
> cannot recover later.

## 8.3 Reading the status

| NAV colour | Meaning | Recording |
|---|---|---|
| **Red** | No valid solution, or navigation system failure | **Blocked** |
| **Orange** | A solution exists | Permitted by TMI |
| **Green** | Solution **meets your user accuracy figures** | Yes — this is the target |

*(TMI UG Rev L, pp.9, 25, 40)*

**Other things that tell you initialization is progressing:**

| Sign | Meaning |
|---|---|
| **Blue arrow** appears on the map | A valid position is available — navigation logging has already started |
| **UTC time** appears top-right | GNSS initialization complete *(TMI UG Rev L, p.33)* |
| **Thin blue line** on the map | Trajectory is being recorded |
| Camera / Laser buttons turn green | Those devices are time-synchronized |

> **IMPORTANT — navigation logging is not the same as recording**
>
> Three facts from the TMI guide *(pp.36, 40)* that operators consistently confuse:
>
> - Navigation logging **starts automatically** as soon as a valid position exists and the
>   blue arrow appears — **even if the NAV button is still red**
> - Navigation logging is **not affected** by the colour changing orange↔green
> - Navigation logging **stops immediately when the mission is closed**
>
> So the trajectory is being recorded long before you press Record, and it keeps recording
> between runs. Pressing Record starts and stops **laser and imagery only**.

### The Navigation View

Press the Nav button for detail: a **logarithmic-scale** display of each accuracy
parameter, plus status information and a **satellite skyplot**. The point at which each
bar turns from orange to green is the User Accuracy figure from Capture Settings
*(TMI UG Rev L, pp.35–36)*.

> **FIELD TIP**
>
> Watch which parameter is holding you at orange. If it is heading, you need more dynamic
> manoeuvres. If it is position, you likely have a sky-visibility problem and should move
> to a better location rather than driving more circles.

## 8.4 What the system is actually doing

> **ADVANCED — a new operator can skip this**

The MX60 blends GNSS and inertial data using Applanix IN-Fusion+ / ProPoint GNSS-Inertial
integration on a dedicated Inertial Engine board *(MX60 UG Rev B, p.56)*. Initialization
is the process of that blended filter resolving several unknowns at once.

**The static period (2–3 minutes)** does two things. It lets the GNSS receiver collect a
clean stretch of data for the post-processor to resolve carrier-phase ambiguities against
— Trimble says explicitly this "aids post-processing software in resolving ambiguities"
*(QSG Rev B, p.11)*. And with the vehicle known to be stationary, the IMU's output *is*
its own bias: anything it reports while parked is error, which the filter can measure and
remove.

**Driving straight** gives the filter a clean velocity vector. GNSS knows the direction of
travel; the IMU knows the vehicle's orientation. Comparing them starts to pin down heading
— the hardest of the three attitude angles.

**Why heading is hardest.** Roll and pitch are observable even at rest, because gravity
gives an absolute vertical reference the accelerometers can feel. There is no equivalent
absolute reference for heading. It has to be *inferred* from motion — which is why a
system without GAMS needs manoeuvres, and one with GAMS does not.

**Varying speed and turning** is what makes the remaining errors observable. Under
constant velocity, an accelerometer bias and a small attitude error look identical to the
filter — both produce the same steady signal, and it cannot tell which is which. Change
the speed and direction, and the two decouple: they affect the measurements differently,
so the filter can separate and estimate them. This is what "dynamic manoeuvres" are
buying — not motion for its own sake, but **observability**.

**The 10-minute settling advice** reflects that convergence is gradual. The light turns
green the moment thresholds are crossed; the solution continues improving after that.

**Why symmetry at the end matters.** Office software processes the trajectory forwards
*and* backwards and blends the two. A good initialization at both ends means both
directions start from strength, and the weakest part of the run — the middle — is solved
from two strong ends instead of one *(QSG Rev B, p.13)*. Section 10.

## 8.5 When initialization goes wrong

| Symptom | Likely cause | Action |
|---|---|---|
| NAV stays **red** | No valid solution — poor sky, obstruction, multipath | Move to a genuinely open location. Check the skyplot |
| NAV reaches orange, won't go green | Attitude/heading not converged | More dynamic manoeuvres — speed changes and turns |
| Green, then drops back to orange | Passing through obstruction, or a marginal solution | Return to open sky; repeat manoeuvres; consider a better site |
| Takes far longer than usual | Poor constellation, or a location worse than it looks | Check the almanac. Consider waiting or relocating |
| NAV never leaves red, sky is clearly open | Possible system fault | Check LEDs and Message Log. Section 14 |

### When to re-initialize

Trimble does not publish a re-initialization trigger list. Based on what the documents
*do* say, re-initialize when:

- The NAV solution degrades and does not recover in open sky
- You have completed a long GNSS outage and are about to collect critical data
- The mission has been closed — **closing a mission stops navigation logging**, so a new
  mission requires a new initialization *(TMI UG Rev L, pp.31, 42)*

> **FIELD TIP — the exception worth knowing**
>
> If you only need **different capture settings** — a dust preset, a different laser mode —
> use **mission re-configuration** rather than closing the mission. Navigation logging
> keeps running throughout, so **no new GNSS/IMU initialization is needed**
> *(TMI UG Rev L, p.41)*.
>
> Closing the mission to change a setting costs you a full re-initialization. Section 9.

> **PARAMETRIX DECISION REQUIRED**
>
> Define the Parametrix re-initialization triggers and record them on the field checklist.
>
> *Recommended practice:* re-initialize after any NAV degradation not recovered within a
> few minutes of open sky, after any GNSS outage materially longer than 60 seconds if
> critical data follows, and whenever a mission has been closed. Record every
> initialization — time and location — in the field protocol.

## 8.6 Initialization checklist

| ☐ | Step |
|---|---|
| ☐ | Parked in open sky, good PDOP, away from buildings |
| ☐ | Mission started; correct Vehicle and Capture presets confirmed |
| ☐ | **Still for 2–3 minutes** |
| ☐ | Blue arrow visible; UTC time showing |
| ☐ | Straight ~20 m → NAV **orange** |
| ☐ | Speed variation + 2–3 dynamic turns → NAV **green** |
| ☐ | All navigation parameters green in Nav View |
| ☐ | **Settling time allowed — up to 10 minutes** |
| ☐ | Camera and Laser buttons green |
| ☐ | Initialization time and location recorded in the field protocol |

---

## References — Section 8

| Source | Pages |
|---|---|
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 11–14 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 9, 25, 31, 33, 35–36, 40–42 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 56, 67 |


---

# 9. COLLECTING DATA AND MONITORING

## 9.1 Recording runs

**To start a run:** press **Record**. The button turns **green → red**.
**To stop a run:** press **Record** again. **Red → green**.

*(QSG Rev B, pp.12–13; TMI UG Rev L, p.9)*

> **IMPORTANT**
>
> Record only project-specific areas *(QSG Rev B, p.13)*. The Record button controls
> **laser and imagery only** — GNSS and IMU logging continues for the whole mission
> regardless *(TMI UG Rev L, pp.36, 40)*.

**Minimum mission time: 30 minutes** *(QSG Rev B, pp.13–14)*.

> **FIELD TIP**
>
> A short corridor does not excuse a short mission. If the work itself is 12 minutes, keep
> the mission open — drive, sit, extend the initialization at both ends — until you clear
> 30 minutes. Closing early gives the office less to work with.

## 9.2 Driving

### Speed

| | |
|---|---|
| **Recommended maximum, system operating** | **80 km/h (50 mph)** |
| Absolute maximum, operating or not | 110 km/h (68 mph) |

*(MX60 UG Rev B, pp.9, 53)*

> **WHY THIS MATTERS**
>
> Speed sets point density. The scanner fires at a fixed rate, so the faster you drive the
> further apart the profiles land. Vehicle speed is "a major factor affecting the final
> point density" *(TMR MLS Guideline §9.4.1, p.12)*.
>
> Slower is denser. It is also more time in traffic. Match speed to what the deliverable
> needs, not to what the road allows.

> **PARAMETRIX DECISION REQUIRED**
>
> Set a standard collection speed and the conditions for reducing it.
>
> *Recommended practice:* collect at or near prevailing traffic speed up to 80 km/h.
> Reduce for high-detail extraction, dusty conditions, or where the deliverable needs
> density. Never exceed 80 km/h with the system operating.

### Smoothness

Drive smoothly. Avoid harsh acceleration, hard braking, and abrupt steering.

The dust filter bulletin says it directly: "avoid harsh vehicle maneuvers as much as
possible" and "reduce driving speed as much as possible" in dusty environments
*(Dust Filter Bulletin, p.3)*.

> **WHY THIS MATTERS**
>
> This is the opposite of initialization, and the contrast is instructive. During
> initialization you *want* dynamics, because they make errors observable. During
> collection you want the vehicle behaving predictably, because every unmodelled jolt is
> a demand on the IMU and a source of noise in the cloud.
>
> Dynamics before you record. Smoothness while you record.

### Lane selection and passes

- Drive the lane closest to what you are collecting
- Follow the pass plan from Section 5 — minimum three passes for survey-grade work
- Drive each direction; two-way coverage fills shadows
- On dual carriageways, include at least one run in the **left-hand through lane** of each
  carriageway *(TMR §8.1.3, p.10)*

### Traffic and obstructions

You cannot control traffic, but you can respond to it:

| Situation | Response |
|---|---|
| Truck blocking the curb for a stretch | Note it; that stretch needs another pass |
| Stopped at a light | Not a problem. Trajectory continues; the scanner keeps collecting from a stationary position |
| Heavy stop-and-go | This is what the DMI is for |
| Parked cars occluding the curb line | Additional passes, or consider night collection (Section 5) |

> **CAUTION — heat**
>
> The operating temperature range is qualified: **not exposed to direct sun and without
> driving less than 10 km/h** *(MX60 UG Rev B, p.53)*. Extended idling in direct sun is
> outside the rated envelope. If you are held up for a long period in heat, keep air
> moving through the vehicle.

### Reversing and U-turns

Nothing in the Trimble documentation prohibits either. Both are legitimate — you will need
U-turns to run a corridor both ways.

> **FIELD TIP**
>
> Stop recording for the turnaround and start again on the new pass. It keeps the runs
> clean and makes the office's job easier, and it costs nothing — navigation logging
> continues either way.

## 9.3 What to watch while driving

This is the operator's real job. Check these in a loop.

| Watch | Good | Act if |
|---|---|---|
| **NAV button** | **Green** | Turns orange — note location. Turns **red** — recording stops being possible |
| **Camera buttons** | Green | Orange (not synced) or **red (error)** |
| **Laser buttons** | Green | Orange or **red** |
| **Record button** | **Red while on a run** | Green when you think you're recording |
| **Trajectory on map** | Thin blue line following the road | Line missing, jumping, or offset from the road |
| **Recorded coverage** | **Thick blue line** over collected areas | Thick line missing where you have driven a run |
| **SSD fill status** | Space remaining | Approaching full |
| **UTC time** | Displayed | Missing — GNSS initialization lost |
| **Disk icons** | No icon | Warning or Error icon appears |
| **Audible alarm** | Silent | **Battery Protect — 78 seconds to restore charge** |

*(TMI UG Rev L, pp.8–9, 33–34; MX60 UG Rev B, p.27)*

> **FIELD TIP — the thick blue line is your best QC tool**
>
> TMI draws the trajectory as a thin blue line and **areas where data was recorded as a
> thick blue line** *(TMI UG Rev L, p.33)*.
>
> At the end of a corridor, look at the map. Every stretch you meant to collect should be
> thick. A thin stretch where you believed you were recording means a run that did not
> start — and finding that in the vehicle costs minutes, while finding it in the office
> costs a mobilisation.

### Views worth opening

| View | Shows |
|---|---|
| **Dashboard** | Navigation status and camera thumbnails |
| **Camera** | Real-time preview per camera, with exposure control |
| **Nav** | Per-parameter accuracy on a log scale, plus satellite skyplot |
| **Laser** | Reduced real-time data stream — the **waterfall view** |

*(TMI UG Rev L, pp.34–37)*

**Camera exposure** can be adjusted live: the panoramic camera has an **Auto** button and
a slider mixing exposure time and gain; the back-down camera has an exposure compensation
slider. Left = darker, right = brighter *(TMI UG Rev L, pp.34–35)*.

**The waterfall view** is where you confirm the laser is producing sensible data — and
it is specifically where a wrong installation height shows up as immediate data gaps when
the dust filter is enabled *(Dust Filter Bulletin, p.3)*.

### Use the Comments feature

TMI lets you enter comments during a mission. They are **time-tagged and saved to the
database against the mission timeline** *(TMI UG Rev L, p.9)*.

> **FIELD TIP**
>
> Use it. "Truck blocking curb, north end" or "NAV dropped to orange under the overpass"
> written at the moment it happens is worth far more than a memory three days later — and
> it lands in the data, not on a piece of paper.

## 9.4 Changing settings mid-mission

You can change **capture settings** between data collection sequences without closing the
mission.

**To do it:** press the capture settings button, select a different Capture preset from the
drop-down, press Next. All sensors shut down and restart with the new configuration.

| Can change | Cannot change |
|---|---|
| Capture settings — laser mode, dust filter, camera triggers, sensor selection | **Vehicle settings** — you are still in the same vehicle |

*(TMI UG Rev L, p.41)*

> **IMPORTANT**
>
> Navigation data logging **keeps running** throughout the reconfiguration. This is the
> whole point: "you will save time as no additional GNSS/IMU initialization procedure will
> be needed." *(TMI UG Rev L, p.41)*

**Prepare presets in advance.** The dust filter bulletin makes the same point — capture
settings for enabling and disabling the filter "would need to be prepared in advance"
*(Dust Filter Bulletin, p.3)*.

## 9.5 Special conditions

### Dust

The dust filter is for **extremely dusty environments** — unpaved roads and open pit mines.
It is explicitly **not** intended for paved roads, urban canyons, or intercity
infrastructure *(Dust Filter Bulletin, p.1)*.

When using it:

| ☐ | Requirement |
|---|---|
| ☐ | **Installation height correct** — this is critical; too high means the mask touches the ground and you lose data |
| ☐ | Use the **higher** laser measurement rate |
| ☐ | Reduce speed as much as possible |
| ☐ | Avoid harsh manoeuvres |
| ☐ | Watch the **waterfall view** — gaps appear immediately if the height is wrong |

*(Dust Filter Bulletin, pp.2–3; TMI UG Rev L, p.29)*

### Lateral range limit

TMI can discard laser points beyond a set distance perpendicular to travel — **5 m to
50 m**, applied to both scanners *(TMI UG Rev L, p.29)*.

> **FIELD TIP**
>
> This is a data-volume tool, not a quality tool. It reduces file size by throwing away
> the far field before it is written. Useful on a long corridor where only the roadway
> matters — but discarded points are gone permanently. If in doubt, collect and filter in
> the office.

### GNSS-denied stretches

When you know you are entering a tunnel, underpass, or urban canyon:

- **Keep driving smoothly.** The IMU is bridging the gap and abrupt inputs make its job
  harder
- **Do not stop inside** unless you must
- **Note it** — use the Comments feature
- **Expect NAV to degrade**, and expect it to take time to recover afterwards
- Trimble specifies performance at a **60-second** outage; beyond that you are outside
  published figures *(MX60 UG Rev B, p.56)*

Section 13 covers the consequences.

## 9.6 Recognising a bad collection before you waste the day

| Sign | Meaning |
|---|---|
| NAV red for an extended period | No recording was possible during that stretch |
| Thick blue line missing where you drove a run | The run was not recording |
| Waterfall view showing gaps or nothing | Laser problem, or dust filter height wrong |
| Camera or laser button red | Device error — data from it is suspect or absent |
| Disk Error icon | Proceeding risks data loss |
| Battery Protect alarm | Power about to be cut |
| UTC time disappeared | GNSS initialization lost |

> **IMPORTANT**
>
> Trimble's rule is worth repeating here: **do not start a mission before solving any
> issue you had previously with the system** *(MX60 UG Rev B, p.44)*. The same judgement
> applies mid-mission. A system that is misbehaving will not fix itself over the next
> 30 km.

---

## References — Section 9

| Source | Pages |
|---|---|
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 8–9, 29, 33–37, 40–41 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 12–14 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 27, 44, 53, 56 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 1–3 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §8.1.3 p.10; §9.4.1 p.12 |


---

# 10. ENDING A COLLECTION

Short section. Get it wrong and you damage a mission that went perfectly.

## 10.1 The sequence

1. **Stop recording** the final run — Record button red → green
2. **Drive to an initialization point** (open sky, good PDOP), making dynamic manoeuvres —
   changing direction and speed — on the way
3. At the point, perform the **finalize sequence**:
   a. **Dynamic steering manoeuvres**
   b. **Vary speed** — accelerate, decelerate, accelerate, decelerate
   c. **Drive straight ahead**
   d. **Remain stationary 2–3 minutes**, logging static data
4. **Close the mission** — press the close button, confirm **Complete Mission**
5. **Shut down the system** — press shutdown, confirm **Shutdown**
6. **Wait for the Control Unit power button light to go out** — up to **90 seconds**
7. **Check the field protocol** — order of runs, direction of runs, date, mission, system
   serial number

*(QSG Rev B, pp.13–14; TMI UG Rev L, pp.42–43)*

## 10.2 Why the ending mirrors the beginning

| Start | End |
|---|---|
| 2–3 min static | dynamic steering |
| drive straight | vary speed |
| vary speed | drive straight |
| dynamic steering | 2–3 min static |

> **WHY THIS MATTERS**
>
> Trimble states that symmetrical collection at both ends "supports forward and reverse
> processing modes in the office software (TBC or POSPac), obtaining a good
> initialization" *(QSG Rev B, p.13)*.
>
> Office software solves the trajectory **forwards from the start and backwards from the
> end**, then blends the two. A strong initialization at only one end means one of those
> two passes begins weak.
>
> The middle of a mission is always the weakest part of the trajectory — it is furthest
> from both anchors. A good finalize sequence is what gives the reverse pass a strong
> anchor to work back from. Skip it and you halve the support under your weakest data.
>
> **You cannot add this later.** No processing step recovers an initialization that was
> never collected.

> **IMPORTANT**
>
> The finalize sequence takes about five minutes. It is the cheapest quality improvement
> available in mobile mapping, and it is the step most often skipped at the end of a long
> day.

## 10.3 Closing and shutting down correctly

> **CAUTION**
>
> "To avoid the possibility of corrupted data, **do not power off the Trimble Mobile
> Mapping system by simply removing power.** Always power off the system using the
> **Complete Mission AND Shutdown** buttons."
> *(TMI UG Rev L, p.31)*

**What each does:**

| Action | Effect |
|---|---|
| **Complete Mission** | Immediately stops the mission in progress. **Navigation data logging stops immediately.** |
| **Shutdown** | Powers off all sensors **and** the control unit |

*(TMI UG Rev L, pp.31, 42)*

> **IMPORTANT — closing a mission ends navigation logging**
>
> Navigation data logs continuously from the moment a valid position exists until the
> mission is closed *(TMI UG Rev L, pp.36, 40, 42)*.
>
> So do not close the mission until the finalize sequence is **complete**. Closing it
> before the static period discards exactly the data the reverse-processing pass needs.

**During shutdown**, a system log file is automatically saved to removable **Disk 1**.
Keep it — Trimble Support asks for it when troubleshooting *(TMI UG Rev L, p.43)*.

After a successful shutdown you need to reload the web client before reconnecting
*(TMI UG Rev L, p.43)*.

## 10.4 Confirming the data is written

Before the vehicle moves off site:

| ☐ | Check |
|---|---|
| ☐ | Mission closed via **Complete Mission** — not by pulling power |
| ☐ | Shutdown completed via the **Shutdown** button |
| ☐ | Control Unit power button light **out** (up to 90 s) |
| ☐ | No disk **Error** icon was showing at the end of the mission |
| ☐ | Map showed a **thick blue line** over every stretch you intended to collect |
| ☐ | Field protocol complete — runs, directions, date, mission name, system S/N |
| ☐ | Any events noted during the mission are recorded (Comments and/or protocol) |

> **FIELD TIP**
>
> Do the map review *before* you close the mission, while the coverage layer is still on
> screen. If a run is missing and you are still on site with an initialized system, you
> can drive it. Ten minutes later, you cannot.

## 10.5 After shutdown

**Sensor Unit removal** — if following Trimble's use assumptions, the Sensor Unit comes
off the roof and into its transport case at the end of the day *(MX60 UG Rev B, p.41)*:

1. Remove cables
2. Open the safety locks
3. Release the fast locks by pressing the fast-lock button downwards
4. Turn the Sensor Unit while pressing the button; free the upper mounting bolts
5. Lift out — **two people** — and place directly into the transport case

*(MX60 UG Rev B, p.19)*

> **IMPORTANT**
>
> If GAMS is fitted, removing it means its lever arm must be **re-measured** before the
> next mission *(MX60 UG Rev B, p.67)*.

**Post-mission safety check.** Trimble requires a safety check **after** each mission, not
just before *(MX60 UG Rev B, p.44)*. Same components checklist as Section 6. Anything
found now is something you can fix before tomorrow morning.

**Power Unit.** If the system is used daily it can stay connected to the vehicle. If it
will sit for a long period, disconnect it to protect the vehicle battery
*(MX60 UG Rev B, pp.25–26)*.

---

## References — Section 10

| Source | Pages |
|---|---|
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 13–14 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 31, 36, 40, 42–43 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 19, 25–26, 41, 44, 67 |


---

# 11. DATA HANDLING

The data on those two SSDs cost a day of crew time and cannot be re-collected without
another mobilisation. Treat it accordingly.

## 11.1 What is on the disks

| Disk | Contents |
|---|---|
| **SSD 1** (upper) | Mission database files · mission log file · **Mission Report** · **navigation data** · laser 1 and 2 data · panoramic camera data |
| **SSD 2** (lower) | Oblique camera data — on the MX60, the back-down camera |

*(TMI UG Rev L, p.44; QSG Rev B, p.8)*

> **IMPORTANT**
>
> **Both disks are one dataset.** SSD 1 holds the navigation data — without it there is no
> trajectory, and without a trajectory everything on SSD 2 is a folder of ungeoreferenced
> photographs. Never separate them.

**Mission directory naming** is automatic:

```
TMX60<serial number>-<mission ID> - <MissionName>
```

The mission ID comes from an increasing counter. Mission name and area name are also saved
as attributes inside the mission database file *(TMI UG Rev L, p.44)*.

A **system log file** is written automatically to removable Disk 1 during shutdown
*(TMI UG Rev L, p.43)*.

## 11.2 Removing the disks

> **CAUTION**
>
> **Never connect the USB cable while an exchangeable data disk is inside the Control
> Unit.** Remove the disk first. *(MX60 UG Rev B, p.10)*

1. Confirm the system is fully shut down — power button light out
2. **Unlock both SSDs** with the provided key
3. Remove both
4. Keep them together, labelled with the mission

## 11.3 Offloading

Use the **MX SCAN Data Carrier Dock** — two are supplied.

1. Connect the Dock's AC adapter to power, and the other end to the rear of the Dock
2. Connect the **USB 3** cable from the rear of the Dock to a USB 3 port on the office
   computer
3. Insert the Exchangeable Data Disk into the Dock
4. **Lock the disk with the key and turn 90° clockwise** to secure it
5. Power on the Dock
6. Download the mission

*(MX60 UG Rev B, p.24; QSG Rev B, p.13)*

> **FIELD TIP**
>
> Two Docks are supplied for a reason — you can offload both disks at once, which roughly
> halves the wait on a full day's data. With 2 × 4 TB of capacity, this is not a quick copy.

## 11.4 Verify before you do anything else

> **IMPORTANT**
>
> A copy that ran without an error message is not a verified copy. Confirm the data is
> genuinely readable **before** the disks go back in the vehicle for tomorrow.

| ☐ | Check |
|---|---|
| ☐ | Mission folder present, correctly named |
| ☐ | **Navigation data present on the SSD 1 copy** |
| ☐ | Laser data present for both scanners |
| ☐ | Panoramic imagery present |
| ☐ | Back-down camera imagery present from the SSD 2 copy |
| ☐ | Mission Report and mission log copied |
| ☐ | System log file copied |
| ☐ | File count and total size match the source |
| ☐ | Project opens in TBC from the `mxdb` database file |

> **CAUTION**
>
> **Do not format or reuse the SSDs until the transfer is verified and backed up.** The
> Quick Start Guide's office procedure is "back up the data" and *then* "prepare SSDs for
> the next mission" *(QSG Rev B, p.15)* — in that order. Reversing it has ended projects.

## 11.5 Back up before you work

Once verified, back up **before** any processing begins.

**The principle:** the raw mission data is the only irreplaceable thing you have. Every
derived product — trajectory, point cloud, colorized cloud, extracted features — can be
regenerated from it. It cannot be regenerated from them.

**Work from a copy.** Never process against the only instance of the raw data.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the Parametrix backup standard for mobile mapping data: how many copies, on
> what media, in which locations, and how long they are retained.
>
> *Recommended practice:* three copies on two media types with one off-site or in cloud
> storage. Raw mission data retained for the life of the project plus the firm's records
> retention period — the point cloud's long-term value depends on the raw data still
> existing. NCHRP's synthesis documents state DOTs treating lidar data as a long-term
> asset with governance attached, not as project scratch *(NCHRP 2024, Ch.3)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Determine the standard MX60 raw data storage location and project folder structure.
>
> *Recommended practice:* one project folder per job, containing `01-raw` (untouched
> mission directories exactly as offloaded), `02-trajectory`, `03-pointcloud`,
> `04-imagery`, `05-control`, `06-qc`, `07-deliverables`, and `08-field-records` (field
> protocol, photos, notes). Make `01-raw` read-only as soon as it is verified.

> **PARAMETRIX DECISION REQUIRED**
>
> Set the project and mission naming convention.
>
> *Recommended practice:* let TMI's automatic directory naming stand — it encodes system
> serial and mission ID, which is exactly what you want for traceability — and carry the
> Parametrix project number in the **mission name** field you type at mission start. That
> puts the project number inside the mission database as an attribute, where it travels
> with the data.

## 11.6 Never delete source data prematurely

> **CAUTION**
>
> Do not delete raw mission data because processing succeeded, because the deliverable
> shipped, or because storage is short.

Reasons this rule exists:

- Processing parameters change. A trajectory reprocessed with better base station data,
  or a cloud re-registered against new control, can be materially better
- Deliverables get revised. The client asks for something nobody extracted the first time
- Boresight calibration improves. A new JSON file can be imported and prior missions
  reprocessed *(TMI UG Rev L, p.18)*
- **The point cloud's long-term value is the whole argument for mobile mapping.** Someone
  measuring something in three years that nobody thought to record is only possible while
  the source exists

> **PARAMETRIX DECISION REQUIRED**
>
> Define the retention and archive policy, including who may authorise deletion of raw
> mission data and after what period.
>
> *Recommended practice:* raw mission data is never deleted by the project team.
> Deletion requires sign-off by the survey technology group owner, and only after the
> retention period has elapsed.

## 11.7 Field records

Trimble requires a field protocol recording, at minimum:

- **Order of runs**
- **Direction of runs**
- **Date**
- **Mission**
- **System serial number**

*(QSG Rev B, p.14)*

Add to that everything from the mission that a processor or reviewer would want:

| Field | Why |
|---|---|
| Operator and driver names | Accountability, and who to ask |
| Vehicle | Ties to the Vehicle Preset |
| **Installation height used** | Affects dust filter, lateral range limit, imagery |
| **Vehicle Preset and Capture Preset names** | Reproducibility |
| Initialization location and time, both ends | Trajectory quality investigation |
| Weather and surface conditions | Explains point cloud and imagery anomalies |
| Events during collection | Occlusions, NAV degradation, traffic incidents |
| Control occupied / base station used | Processing input |

> **FIELD TIP**
>
> TMI's **Comments** feature time-tags notes into the mission database
> *(TMI UG Rev L, p.9)*. Use it *and* the paper protocol. The comments travel with the
> data; the protocol survives if the data does not.

**Also worth exporting:** TMI can download **Mission Coverage as a `.kmz`** containing the
trajectory *(TMI UG Rev L, p.14)*. That is a lightweight, universally readable record of
exactly where you drove — useful in the project file and useful to send a client.

## 11.8 Chain of custody

For most survey work this is informal. It stops being informal when the data supports
litigation, a claim, or a boundary determination.

> **PARAMETRIX DECISION REQUIRED**
>
> Determine whether mobile mapping data requires formal chain of custody, and under what
> circumstances.
>
> *Recommended practice:* standard projects need no formal chain of custody beyond the
> field protocol and dated backups. For any project identified as litigation-related or
> forensic, apply a documented chain of custody from the moment the disks leave the
> vehicle, and preserve the raw data unaltered with checksums.

## 11.9 Preparing for the next mission

Only after verification and backup:

1. Return both SSDs to the Control Unit
2. Insert and **lock** them
3. On next startup, watch the **disk check** result — no icon is what you want; a Warning
   or Error means investigate before committing to a mission *(TMI UG Rev L, pp.33–34)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide how many SSD sets are in circulation.
>
> *Recommended practice:* hold at least one spare set. A single set means the crew cannot
> mobilise until the previous day's offload finishes and verifies — which is precisely the
> pressure that causes someone to skip verification.

---

## References — Section 11

| Source | Pages |
|---|---|
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 9, 14, 18, 33–34, 43–44 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 8, 13–15 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 10, 24 |

## Other References — Section 11

| Source | Chapter |
|---|---|
| NCHRP, *Practices for Collecting, Managing, and Using Lidar Data*, 2024 | Ch.3, Lidar Data Life Cycle |


---

# 12. OFFICE WORKFLOW

> **IMPORTANT — read this before relying on the section**
>
> The only TBC mobile mapping document available to Parametrix is *TBC Technical Notes:
> For Mobile Mapping*, **October 2022**. It is a capability brochure, not a procedure
> manual, and it predates the MX60 — it lists raw import from "MX7, MX50, or MX9" only
> *(TBC Technical Notes, p.3)*. MX60 support reached TMI in **December 2024**
> *(TMI UG Rev L, p.2)*.
>
> This section therefore describes the **shape** of the workflow and Trimble's own
> terminology for it. It is not a step-by-step procedure, and the specific commands,
> dialogs, and settings must come from current TBC documentation before this section is
> used to train anyone.

## 12.1 The workflow in one line

```
Import mxdb → Process trajectory → Generate scans → Register to control
   → Colorize → Classify → Extract → QC → Deliver → Archive
```

## 12.2 The stages

### 1. Import

Import raw mobile mapping data by **pointing at the project database file (`mxdb`)**
created by TMI in the field.

The `mxdb` "maintains your data integrity between trajectory, LiDAR data, and panoramic
images," and "full synchronization between original sensor data is maintained for data
runs as collected in the field" *(TBC Technical Notes, p.3)*.

> **WHY THIS MATTERS**
>
> You import a *mission*, not a pile of files. The database is what preserves the timing
> relationship between the trajectory and every laser and camera observation — which, per
> Section 2, is the thing that makes the data georeferenced at all. This is why Section 11
> insists the two SSDs stay together and the mission folder stays intact.

### 2. Vehicle trajectory processing

Two routes:

| Route | Notes |
|---|---|
| **In TBC** | Requires the TBC Mobile Mapping subscription licence. Load raw trajectory and base station data directly; process without leaving TBC; run trajectory reports and QA/QC in TBC |
| **Standalone Applanix POSPac MMS** | Still supported |

*(TBC Technical Notes, pp.2–3)*

This is where the GNSS and IMU data become the trajectory that everything else depends on.
Section 13 covers what to look for in the result.

> **ADVANCED — forward and reverse processing**
>
> This is the step that consumes the symmetry you built in the field. The processor runs
> the solution forward from the start and backward from the end and blends them — which is
> exactly why Trimble asks for a good initialization at **both** ends *(QSG Rev B, p.13)*.
> A mission with a strong start and a skipped finalize sequence produces a visibly weaker
> reverse pass.

> **ADVANCED — lever arms will not match what you measured**
>
> The MX60 System Reference Frame origin differs from the External Reference Point. TMI
> adds internal vectors, so POSPac displays corrected lever arms that differ from your
> mechanical measurements. **This is correct.** *(MX60 UG Rev B, p.47)*

### 3. Generate scans

Use the finished trajectory to generate scans, for individual runs or all runs in the
project.

Available at this stage *(TBC Technical Notes, p.3)*:

- **Filters for sun and fog**
- A **masking template** for point cloud colorization

### 4. Register point clouds

Register mobile mapping runs to fixed control points — Trimble's stated purpose is to
"reduce, or eliminate, **IMU drift**" *(TBC Technical Notes, p.4)*.

| Capability | Detail |
|---|---|
| Registration to control | TBC **smart picking tool** plus the integrated **POSPac PFix engine** |
| **Batch registration** | Register several runs together "to minimize anomalies between common runs in the same geographical location from one mission or from multiple ones" |
| Scan update | Update scans based on registration constraints |

*(TBC Technical Notes, p.4)*

> **IMPORTANT**
>
> Batch registration across runs is how run-to-run disagreement gets resolved. Section 13
> explains why that disagreement is also your best free QC measure — and why you should
> **look at it before you remove it**.

### 5. Colorize

Colorize point clouds using **RGB from the 360° imagery**
*(TBC Technical Notes, p.3)*.

Intensity colouring is the alternative and is the more common delivery for engineering
use. TMR requires delivered intensity data to be normalised to a **16-bit range, 0
(black) to 65535 (white)** *(TMR MLS Guideline §9.2.2, p.11)*.

### 6. Classify and extract

TBC's automated classification creates extraction regions
*(TBC Technical Notes, p.4)*:

| Region | Typical use |
|---|---|
| **Ground** | Surface and corridor deliverables, digital surface models |
| **Buildings** | Context, clearance |
| **High Vegetation** | Vegetation clearance, landscape management |
| **Poles** and **Signs** | Asset inventory |
| **Power Lines** | Power line and pole extraction |

From there: CAD and drafting, surfaces and volumes, alignments and corridors, utility
modelling *(TBC Technical Notes, pp.5–6)*.

### 7. Review imagery

360° panoramic images can be navigated **synchronised with the point cloud 3D view**, with
point clouds overlaid on images for feature verification and object inspection
*(TBC Technical Notes, p.4)*.

> **FIELD TIP**
>
> This is the office's equivalent of walking the site. When a point cloud feature is
> ambiguous — is that a sign or a mailbox, is that curb or a shadow — the synchronised
> panorama resolves it in seconds.

### 8. QC, deliver, archive

Section 13 covers quality control. Delivery formats and archive policy are Parametrix
decisions recorded in Section 11.

## 12.3 Boresight calibration

### What is actually being calibrated

A system calibration estimates where each sensor sits and how it is oriented relative to
an internal virtual reference point inside the sensor head. Each sensor has two sets of
offsets:

| Offset | What it is | Estimated? |
|---|---|---|
| **Lever arms** | Translation — X forward, Y right, **Z down** | **No — known for all sensors** |
| **Boresight angles** | Rotation about those axes — roll, pitch, heading | **Yes — this is what calibration solves** |

*(TBC Help: Calibrate Mobile Mapping Laser Scanners)*

> **WHY THIS MATTERS**
>
> This is the point that makes the whole subject tractable. **You never measure the
> scanners' positions** — Trimble knows where they are inside the head. What drifts, and
> what calibration recovers, is the tiny **angular** misalignment between each scanner and
> the inertial system.
>
> And per Section 13, angular error is the one that multiplies with range. A boresight
> error of a few hundredths of a degree is invisible at the curb line and significant at
> 50 m.

Do not confuse these with the **vehicle** lever arms in Section 6. Those describe where
GAMS and the DMI sit relative to the External Reference Point, and you do measure them.
The sensor lever arms discussed here are internal to the head.

### Where it happens

**In TBC.** Trimble states that "up to the 5.21 version, laser scanners are calibrated out
of the application and the calibration values are imported into TBC from a JSON format
file," and that the *Calibrate Laser Scanners* feature now allows calibration inside TBC
*(TBC Help: Calibrate Mobile Mapping Laser Scanners)*. The feature therefore arrived after
5.21; the exact release is not stated.

> **IMPORTANT**
>
> Both routes still exist, and which one applies depends on your TBC version:
>
> - **TBC after 5.21** — calibrate in TBC using *Calibrate Laser Scanners*, then **Apply**
> - **TBC 5.21 and earlier** — calibrate outside TBC, then import the JSON via
>   `Settings → Calibration Import` in TMI, from a USB stick in the **USB1** socket
>   *(TMI UG Rev L, p.18)*
>
> Confirm which TBC version Parametrix runs before writing this into procedure.

**This is office work.** Nothing is returned to Trimble and nothing is dismantled.

### The calibration mission — what the field crew must collect

This is the part that lands on the field crew, and it is a specific drive, not a normal
collection.

**Four runs over one crossroad:**

| Run | Direction |
|---|---|
| Run_0 | Along the first road, forward |
| Run_1 | Along the first road, backward |
| Run_2 | Along the crossing road, forward |
| Run_3 | Along the crossing road, backward |

**Site requirements** *(TBC Help: Calibrate Mobile Mapping Laser Scanners)*:

| Requirement | Detail |
|---|---|
| **Crossing angle** | As close to **90°** as possible, within **±30°** |
| **Run length** | At least **20 m each side** of the crossing. **Ideally 80 m long — 40 m each side** |
| **Overlap** | Enough overlap between runs |
| **Façades** | **Present in each direction, in sufficient quantity** |
| **Vegetation** | **Few or none, ideally** |

> **WHY THIS MATTERS — why façades and why a crossing**
>
> Boresight angles are solved by comparing the same surfaces seen from different
> directions. Flat vertical surfaces seen from two opposing passes make an angular error
> show up as a visible gap between the two point clouds; pavement alone, viewed at a
> grazing angle, barely constrains it.
>
> The orthogonal pair matters for the same reason in the other axis. A single road only
> constrains the rotations that road's geometry is sensitive to — the crossing supplies
> the rest.
>
> And vegetation is excluded because it gives soft, inconsistent returns that do not
> repeat between passes, so it adds noise to exactly the comparison the solver depends on.

> **FIELD TIP**
>
> Scout the calibration site once and reuse it. A quiet crossroad with buildings on all
> four approaches, minimal trees, and room for 40 m of clean run each way is not common —
> having a known good one saves an hour every time.

### The TBC procedure

1. Create a VCE project; set the coordinate system to match the mobile mapping data
2. Import the `.mxdb`
3. In **Project Explorer**, select a laser scanner under **Capture Devices**
4. From the pop-up menu, choose **Calibrate Laser Scanners**
5. Select the **four runs** (Run_0 – Run_3) of the same crossroad
   — *fewer than four raises an error*
6. Optionally **Toggle Active Trajectory** to see which runs intersect
7. Optionally check **Open Cutting Plane View**
8. Press **Compute** — this may take a while
9. Review the results (below), and **perform the visual check**
10. In the dialog, switch to **Run_2 <-> Run_3** and check that pair too
11. Press **Apply**

*(TBC Help: Calibrate Mobile Mapping Laser Scanners)*

### Reading the result

The dialog reports:

| Output | Meaning |
|---|---|
| **Computed calibration values** | Heading, pitch and roll per laser scanner |
| **Overall Overlap** | Percentage of points used against total points generated |
| **Overall RMS** | Average of the RMS values between used scans |
| **Per-pair Timestamps + 3 RMS values** | For each set of two parallel runs, over a 20 m section around the crossing |

The three RMS directions are **Tangential**, **Orthogonal** and **Vertical** — how closely
the parallel runs agree in each.

> **CAUTION — the asymmetry that matters**
>
> **Good RMS values do not mean the calibration succeeded. A visual check is needed.**
> Bad RMS values do mean it failed, and a visual check will confirm that.
> *(TBC Help: Calibrate Mobile Mapping Laser Scanners)*
>
> So the numbers can only tell you when you have failed. They cannot tell you that you
> have passed. **Never press Apply on RMS alone.**

### The visual check

With **Open Cutting Plane View** checked, a plane named *Mobile Mapping Cutting Plane*
appears as a yellow plane in the 3D View at the start of the first run pair, and points
intersecting it show as a profile in the Cutting Plane View tab.

To use it well:

- Set **rendering to Scan Color** so each scan draws in its own colour — this is what
  makes a gap between passes obvious
- Increase **Point Size** so thin surfaces read clearly
- Adjust **cutting plane thickness** to control which points appear
- **Drag the slider** along the run pair and watch the gap between the two scans at
  several positions, not just one

Then repeat for **Run_2 <-> Run_3**.

> **FIELD TIP**
>
> You are looking for the two colours to sit on top of each other on flat surfaces —
> especially building façades, which is why the site needs them. A consistent offset that
> grows with distance from the vehicle is the signature of a residual angular error.

### How often

No Trimble document in our set states a frequency for the MX60. Queensland TMR, writing
for any MLS system, requires calibration immediately before **and** again at the end of
every project, plus any time the system is disturbed or reassembled
*(TMR MLS Guideline §6, p.7)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Set the boresight calibration policy: frequency, who performs it, what triggers an
> unscheduled calibration, and how the calibration in force is recorded against each
> mission.
>
> *Recommended practice:* calibrate on a defined interval and after any event that could
> have disturbed the sensor head or rack. Record the calibration date and values in the
> field protocol so any mission can be traced to the calibration it was collected under.
> Establish one standard calibration site meeting the crossing requirements above.
>
> Two questions this needs answered first:
>
> - **Which TBC version** does Parametrix run? Versions after 5.21 calibrate in TBC;
>   5.21 and earlier require the external-then-import route.
> - **Does daily removal of the Sensor Unit count as "disturbed"?** If Parametrix follows
>   Trimble's assumption and cases the head each night (Section 3), a literal reading of
>   TMR would require calibration every day, which is not practical. A sensible position
>   is that the fast-lock mount is repeatable and only rack disturbance or a suspected
>   problem triggers recalibration — but that position should be tested against a
>   calibration check, not assumed.

## 12.4 What this section still needs

| Needed | To write |
|---|---|
| Current TBC mobile mapping documentation covering MX60 | Step-by-step import, trajectory processing, registration, export |
| TBC trajectory report interpretation | Section 13 acceptance criteria |
| MX60 boresight calibration procedure | §12.3 policy and the procedure itself |
| POSPac MMS documentation | Trajectory processing detail, forward/reverse settings |

---

## References — Section 12

| Source | Pages |
|---|---|
| Trimble Business Center Technical Notes: For Mobile Mapping, October 2022 | 2–6 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 2, 18, 20 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 47 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 13 |

## Other References — Section 12

| Source | Section |
|---|---|
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §6 p.7; §9.2.2 p.11 |


---

# 13. QUALITY, CONTROL AND LIMITS

The longest section, because it answers the question that matters: **is this data good
enough, and where isn't it?**

It is told once, in one place, because trajectory quality, point cloud quality, control
and QC are not four subjects — they are one subject seen from four angles.

---

## 13.1 Understanding the trajectory

### Why everything depends on it

From Section 2: every point inherits the trajectory's error at the instant it was
measured. The scanner's own accuracy — 2 mm, precision 2.5 mm at 30 m
*(MX60 UG Rev B, p.54)* — is a small contributor to your final number.

The trajectory has six components at every instant:

| Component | Comes from |
|---|---|
| **X, Y, Z position** | GNSS, bridged and smoothed by the IMU |
| **Roll, pitch** | IMU, referenced to gravity |
| **Heading** | IMU, inferred from motion — or directly from GAMS |

### How trajectory error becomes point error

**Position error** shifts points. A 10 cm position error moves every point collected at
that instant by 10 cm, in the same direction. This is the easy case: it is a translation,
and control can partly correct it.

**Attitude error rotates points, and the effect grows with range.** This is the case people
underestimate.

A small angular error at the sensor becomes a large positional error at distance. The
approximate lever is:

```
position error ≈ range × angular error (in radians)
```

Worked from Trimble's published figures *(MX60 UG Rev B, p.56)*:

| Angular error | At 10 m | At 30 m | At 100 m |
|---|---|---|---|
| 0.005° (Core/Pro roll-pitch) | 0.9 mm | 2.6 mm | 8.7 mm |
| 0.0025° (Premium roll-pitch) | 0.4 mm | 1.3 mm | 4.4 mm |
| 0.015° (heading, with GAMS) | 2.6 mm | 7.9 mm | 26 mm |

> **WHY THIS MATTERS**
>
> This table is the mathematical reason for the "useful range" concept in Section 2. The
> cloud is most accurate near the vehicle and degrades with distance — not because the
> laser gets worse, but because attitude error is multiplied by range.
>
> It is also why **attitude accuracy is the headline difference between Premium and
> Core/Pro**. At the roadway it barely matters. At 100 m it is a factor of two.

### GNSS outages and IMU bridging

When GNSS is lost, the IMU carries the solution alone. It does this well briefly and
badly eventually, because inertial errors accumulate — small biases integrate into
velocity error, which integrates into position error.

Trimble publishes two points on this curve *(MX60 UG Rev B, p.56)*:

| Condition | Core / Pro | Premium |
|---|---|---|
| **No outage** | X,Y <0.01 m · Z 0.01 m | X,Y <0.01 m · Z 0.01 m |
| **60-second outage** | X,Y 0.12 m · Z 0.10 m | X,Y 0.10 m · Z 0.07 m |

Note both are post-processed with POSPac and assume the **DMI option** and best
conditions.

> **IMPORTANT**
>
> Trimble publishes nothing beyond 60 seconds. Do not extrapolate — inertial drift is not
> linear, and a two-minute outage is not twice a one-minute outage. Beyond 60 seconds you
> are outside the manufacturer's stated envelope and into territory that must be verified
> by check points, not predicted.

**What helps during an outage:**

| Aid | Effect |
|---|---|
| **DMI** | Constrains distance travelled; supplies ZUPT information. This is what it is for *(MX60 UG Rev B, p.42)* |
| Smooth driving | Fewer unmodelled dynamics for the IMU to absorb |
| Short exposure | The only real fix — plan the route so outages are brief |
| Passes from both directions | The outage falls at a different point in each solution |

**What does not help:** driving faster to get through it sooner. You reduce the outage
duration but add dynamics at exactly the wrong moment.

### Reading the trajectory afterwards

TMR requires a trajectory string "attributed with RMSE values on each vertex... during
capture," plus an explicit statement of "how the IMU (and wheel encoder if fitted)
observations are applied during times of degraded, lost, or obstructed GNSS signal
reception" *(TMR MLS Guideline §14, p.25)*.

> **FIELD TIP**
>
> Plot the trajectory's reported accuracy against the route before you look at anything
> else. The spikes tell you where to concentrate your QC — and they will line up with the
> overpasses, canyons and canopy you mapped in Section 5.

---

## 13.2 Point cloud quality

### What degrades it, and how

The most useful distinction is **missing data vs. noisy data vs. wrong data**, because
they have different causes and different remedies.

| Cause | Effect | Remedy |
|---|---|---|
| **Occlusion** — traffic, parked cars, vegetation, barriers | **Missing** | More passes, other direction, night collection, conventional survey |
| **Beyond useful range** | **Wrong** (degraded accuracy, looks fine) | Understand and state useful range |
| **Wet surfaces, standing water** | **Missing** — no return | Do not collect wet |
| **Rain, mist, spray, snow** | **Noisy** — returns off airborne particles | Do not operate in rain or mist *(MX60 UG Rev B, p.49)* |
| **Dust** | **Noisy** | Dust filter, but only on unpaved roads and mine sites |
| **Glass, water, polished metal** | **Missing or wrong** — specular reflection | Expect gaps; verify by imagery |
| **Retro-reflective signs** | Blooming, saturated returns | Normal; usually still usable |
| **Grazing incidence** — far pavement, steep slopes | **Noisy and sparse** | Passes from both directions |
| **Excessive speed** | **Sparse** — lower point density | Reduce speed |
| **Moving vehicles** | **Wrong** — a car in the cloud that is not there | Cleansing, in the office |
| **Vehicle vibration, harsh manoeuvres** | **Noisy** | Drive smoothly |

### Range and reflectivity

Maximum range is **150 m at the lower measurement rate, 120 m at the higher**
*(MX60 UG Rev B, p.54)*. Those figures assume *(p.55)*:

- Flat targets larger than the beam diameter
- **Perpendicular** angle of incidence
- Atmospheric visibility of **23 km**
- And explicitly: **range is shorter in bright sunlight than under an overcast sky**

> **WHY THIS MATTERS**
>
> Every one of those conditions is optimistic relative to a real roadside. A dark, wet,
> obliquely-angled surface at 100 m in bright sun is nothing like the specification case.
> Treat published range as a ceiling, not an expectation.

### Density

Point density is set by measurement rate, line speed, range, and **vehicle speed**. TMR
notes speed is "a major factor affecting the final point density" *(§9.4.1, p.12)*.

TMR's approach is worth adopting: rather than specifying a density number, require a
**statement** of the density and pattern achieved at a stated speed, on defined surfaces
at defined distances *(§9.4.3, pp.12–13)*.

### Multiple passes and what they buy

Three things, per Section 5: redundancy, changed GNSS constellation, and shadow reduction.

But there is a subtlety worth knowing *(TMR Note 1, §9.4.3, p.14)*:

> "Multiple scans can achieve a higher overall density of points, but if there are any
> issues with aligning multiple Pointcloud scans together, the definition of features can
> become a problem if the point density is not high enough in each individual scan."

> **IMPORTANT**
>
> Passes are not a substitute for a good single pass. If each individual pass is sparse or
> poorly registered, stacking three of them produces a thicker, blurrier cloud — not a
> better one.

### Useful range — state it

TMR requires the contractor to state the width over which the cloud actually meets project
accuracy, noting a cloud may reach 200 m while the compliant portion is "considerably
less" *(§11.7, p.18)*.

Their worked example of an acceptable statement:

> "The MCPPC supplied meets or exceeds the accuracy requirements for this project between
> the edges of pavement."

> **IMPORTANT — the point scale factor trap**
>
> Laser scanners measure **plane** distances. Deliverables are usually **grid**
> coordinates. TMR warns of errors "of up to 40 mm / 100 m due entirely to Point Scale
> Factor," and says this must be considered in any useful range statement
> *(§11.7, p.19)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether Parametrix issues a useful range statement with every mobile mapping
> deliverable.
>
> *Recommended practice:* yes, on every project. It is a few lines in the survey report, it
> is defensible, and it prevents the most common and most expensive client
> misunderstanding — that everything visible in the cloud is surveyed to the same standard.

### Cleansing

Moving vehicles and other transient objects appear as real points.

> **IMPORTANT**
>
> TMR's rule is the right one: **reclassify, do not delete.**
>
> "It is recommended that data is not deleted but pushed to other files or classified in
> such a way so that it can be separated from the clean data. Care should be taken as
> removal of non-erroneous data during a cleansing process may result in the MLS
> contractor having to re-supply datasets."
> *(TMR §11.8.1, p.19)*

---

## 13.3 Imagery quality

Imagery fails differently from LiDAR, and it fails for reasons LiDAR does not care about.

| Factor | Effect |
|---|---|
| **Low sun angle** | Under- and over-exposure. TMR: avoid early morning and late afternoon; **8am–4pm usually ideal** *(§10, p.15)* |
| **Direct sun into lens** | Flare, blown highlights |
| **Deep shadow** | Unusable detail in shadowed areas |
| **Rain, water on lens** | **Grounds for rejection** *(TMR §10, p.15)* |
| **Dirty lens** | Haze across every frame from that camera |
| **Motion** | Blur — mitigated by the global shutter *(MX60 UG Rev B, p.53)* |
| **Traffic, pedestrians** | Occlusion, and privacy exposure |
| **Wrong exposure setting** | Correctable live in TMI — see below |

**Live exposure control** is available while driving *(TMI UG Rev L, pp.34–35)*: the
panoramic camera has an **Auto** button plus a slider mixing exposure time and gain; the
back-down camera has an exposure compensation slider. Left darker, right brighter.

> **FIELD TIP**
>
> Check the Camera view when lighting changes materially — entering a tree tunnel, turning
> into the sun, coming out of a cutting. An exposure set for open highway is wrong under
> canopy, and unlike LiDAR you cannot fix it afterwards.

**Focus is fixed, and the ranges matter** *(MX60 UG Rev B, pp.53–54)*:

| Camera | Sharp from |
|---|---|
| Spherical, Core | 0.7 m to infinity |
| Spherical, Pro/Premium | Calibrated 2.0 m to infinity |
| **Back-down camera** | **2.0 m to 9.0 m** |

That back-down range is why the vehicle needs a **minimum roof height of 1.60 m**
*(MX60 UG Rev B, p.59)*.

**Capture triggering** is by distance or by time, max 10 fps spherical, 9 fps back-down
*(MX60 Spec Sheet p.2)*. Distance-based gives even spatial coverage regardless of speed —
usually what you want.

> **IMPORTANT**
>
> Imagery must be captured **at the same time as the point cloud** to be a valid record of
> site conditions. TMR is explicit: capture at a different time does not meet the
> requirement, because conditions change *(§10, pp.14–15)*.

### Privacy

Mobile mapping imagery captures faces, licence plates, and private property incidentally.
No Trimble document addresses this.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the imagery privacy policy: whether faces and plates are blurred, who may
> access raw imagery, what is delivered to clients, retention period, and how requests for
> removal are handled.
>
> *Recommended practice:* treat raw imagery as internal and restricted. Where imagery is
> delivered or published, apply face and plate blurring. Set this before the first project
> that publishes imagery, not after.

---

## 13.4 Control and mobile mapping

This is not a section on control surveying. It covers only how control interacts with
mobile mapping.

### Two different jobs — do not confuse them

| | **Control points** | **Check points** |
|---|---|---|
| Purpose | **Improve** the solution | **Verify** the solution |
| Used in | Registration / adjustment | Independent testing only |
| If used for both | The test is meaningless | — |

> **IMPORTANT**
>
> A point used to register the cloud cannot then be used to verify it. It will fit,
> because you made it fit. Independent check points must be held out of the adjustment
> entirely.

### How control is used

TBC registers mobile mapping runs to fixed control points explicitly to "reduce, or
eliminate, IMU drift," using the smart picking tool and the POSPac PFix engine
*(TBC Technical Notes, p.4)*.

Control points must be **identifiable in the point cloud**. TMR calls these "Clearly
Defined Points" and gives examples *(App F, pp.32–33)*:

- Corners of concrete — bridge abutments, culverts
- Centres of light poles or posts
- Ends of line marking strings
- Guardrail posts
- Targets specifically placed for the purpose

### Where control goes

TMR's minimum *(App E, p.31)*:

- A ground control point **adjacent to the start and end** of the project
- A ground control point at **all intersections of state-controlled roads**, so future
  collections match

And for check sites, the stated intent is what makes them useful *(App F, p.32)*:

> "The intention of all the check sites is to gather an understanding of the accuracies
> achieved in areas of **both good and poor GNSS coverage** as well as close to and half
> way between [control marks]."

> **IMPORTANT**
>
> Check points only in open sky tell you the best case. Deliberately place them where you
> expect trouble — that is where you need to know.

### Base stations

Short baselines between base station and vehicle give the best positional outcome
*(TMR §5.2, p.6; §7.2, p.8)*. TMR requires 1-second epochs or better and dual-frequency
receivers *(§7.2, p.8)*.

> **ADVANCED — redundancy at the base is not redundancy at the vehicle**
>
> TMR makes a point worth absorbing:
>
> "If [base stations] are occupied simultaneously, there is only a redundancy in the GNSS
> observation at the [base marks], but generally **NO redundancy at the vehicle**.
> Therefore, concurrent base station observations only constitute a **partially
> independent** GNSS reading."
> *(§7.1, p.8)*
>
> Two base stations do not give you two independent measurements of where the vehicle was.
> Real redundancy at the vehicle comes from repeat passes at different times.

### Identifying systematic problems

| Symptom | Likely cause |
|---|---|
| Constant offset over a whole run | Base station coordinate error, or datum/epoch mismatch |
| Offset growing with distance from control | Trajectory drift between constraints |
| Vertical bias only | Geoid model, antenna height, or lever-arm Z error |
| Run-to-run disagreement, one direction consistently off | Boresight error |
| Disagreement worsening with range from vehicle | Attitude error — see §13.1 |
| Step at a run boundary | Registration issue; TMR: steps are "unacceptable" *(§8.3, p.10)* |

> **FIELD TIP**
>
> **Run-to-run disagreement is your best free QC measure.** Before you register the runs
> together, look at how far apart they are. That difference is a direct, independent
> measure of the system's internal consistency — and once you batch-register them, it is
> gone. Record it first.

---

## 13.5 The QC process

### Field QC — before leaving site

| ☐ | Check | Fail action |
|---|---|---|
| ☐ | NAV green throughout collection | Note stretches at orange or red |
| ☐ | **Thick blue line over every intended stretch** | Re-drive the missing run — now |
| ☐ | Camera and laser buttons green all mission | Investigate; the data may be incomplete |
| ☐ | Waterfall view showed sensible data | Investigate before leaving |
| ☐ | No disk Warning or Error | Do not reuse the disk |
| ☐ | Finalize sequence completed | Cannot be added later |
| ☐ | Field protocol complete | Complete it now |

### Office QC — after processing

| # | Question | How to answer |
|---|---|---|
| 1 | Did the system operate correctly? | System log, TMI Message Log (Alarm/Warning filter), field protocol |
| 2 | Is the trajectory acceptable? | Trajectory report; plot reported accuracy along the route; check both initializations |
| 3 | Is the point cloud complete? | Compare coverage against the project limits; look for gaps |
| 4 | Do the runs agree with each other? | **Run-to-run comparison, before registration** |
| 5 | Does independent control agree? | Check points held out of the adjustment |
| 6 | Are there areas of excessive noise? | Visual review; cross-sections through suspect areas |
| 7 | Are important features occluded? | Review against the deliverable list |
| 8 | Is imagery usable? | Review exposure, blur, lens cleanliness, coverage |
| 9 | Does anything need recollection? | See the decision table below |
| 10 | Does anything need conventional supplementation? | Compare against the Section 5 list |

### Acceptance categories

| Category | Meaning | Action |
|---|---|---|
| **ACCEPT** | Meets project requirements throughout the stated useful range | Proceed to delivery |
| **REVIEW** | Localised issues that may be acceptable depending on the deliverable | Project surveyor decides; document the decision |
| **SUPPLEMENT** | Data is sound but incomplete for the deliverable | Conventional survey fills the gaps |
| **RECOLLECT** | Trajectory or coverage failure over a material extent | Re-mobilise |

> **PARAMETRIX DECISION REQUIRED**
>
> Set the numerical tolerances that separate these categories.
>
> **No tolerances are proposed here**, because none of the Trimble documents provide them
> and TMR deliberately leaves its values as per-project variables — its uncertainty
> formulas appear as `(x) mm`, `(y) mm + (yy) ppm`, and so on, filled in by a project
> checklist that is not in our source set *(TMR App A–D, pp.27–30)*.
>
> *Recommended practice:* adopt a recognised US framework — ASPRS *Positional Accuracy
> Standards for Digital Geospatial Data* (2014) or NSSDA — and set default project
> tolerances against it, allowing per-project override. Adopt TMR's **structure** even if
> not its numbers, because the structure is sound:
>
> - **Horizontal survey uncertainty** — vector between a clearly defined point in the cloud
>   and the same point by independent means, at 95% *(App A, p.27)*
> - **Horizontal relative uncertainty** — distances within a sliding window of up to 200 m
>   agree to `(y) mm + (yy) ppm` *(App B, p.28)*
> - **Vertical survey uncertainty** — height difference on hard surfaces at 95%
>   *(App C, p.29)*
> - **Vertical relative uncertainty** — height differences within a 200 m sliding window
>   *(App D, p.30)*
>
> Absolute *and* relative matter. A cloud can be biased 5 cm and internally excellent —
> fine for volumes, wrong for tying to existing control. The reverse is also possible.

### Periodic system verification

Trimble's own recommended check, worth adopting as a scheduled procedure
*(MX60 UG Rev B, p.7)*:

> Register a scan position by scanning a number (e.g. 8) of flat retro-reflecting targets
> at different distances and at angles covering more than 180° horizontally, which have
> also been surveyed by a highly accurate total station. **The check is passed if the
> residual error is less than the instrument's specified accuracy.**

Trimble "strongly recommends" checking data quality regularly, "especially before starting
an extensive data acquisition campaign."

> **PARAMETRIX DECISION REQUIRED**
>
> Adopt this as a scheduled Parametrix verification, and set the interval.
>
> *Recommended practice:* establish a permanent target array at a Parametrix facility,
> surveyed conventionally. Run the check quarterly, before any major campaign, and after
> any event that could have disturbed the system. Retain results as a performance history —
> a trend is far more informative than a single pass/fail.

### QC deliverables

TMR's reporting list is a good starting template *(§14, p.25)*:

| ☐ | Item |
|---|---|
| ☐ | System reports — component calibration, alignment, self-tests |
| ☐ | Trajectory with accuracy values attributed along it |
| ☐ | Statement of how IMU (and DMI) observations are applied during degraded or lost GNSS |
| ☐ | Evidence of how scans from each scanner join |
| ☐ | Compliance report — cloud against control, horizontal and vertical |
| ☐ | **Useful range statement** |
| ☐ | Survey report, signed, including any areas where accuracy was not achieved |

> **IMPORTANT**
>
> TMR requires that "if there are areas where the contractor has not achieved the accuracy
> specified, the MLS contractor shall identify these areas in the Survey Report"
> *(§14, p.26)*.
>
> Disclose shortfalls. A documented limitation is a professional judgement. An undisclosed
> one discovered by the client is something else.

---

## 13.6 When mobile mapping does not work well

### What the system can and cannot see

**Can see:** anything with line of sight from a sensor about 2 m above the road, within
useful range, that reflects enough light, during the pass.

**Cannot see:**

| Cannot see | Why |
|---|---|
| Behind barriers, walls, dense vegetation | No line of sight |
| Under parked vehicles | Occluded |
| Inside structures — invert elevations, pipe conditions | No line of sight |
| Deep ditches, steep back slopes | Below the sensor's line of sight |
| Beneath water | No return |
| Through glass | Specular / transparent |
| Anything requiring physical contact or interpretation | Not a measurement problem |
| Monuments, boundary evidence | Requires professional judgement and recovery |
| Areas the vehicle cannot reach | Not driven |

### Environments that degrade or defeat it

| Environment | Problem | Mitigation |
|---|---|---|
| **Tunnel** | Total GNSS loss, potentially far beyond 60 s | DMI; short transit; control at both ends; verify with check points |
| **Underground parking** | Total loss, plus no initialization possible | Usually the wrong tool |
| **Urban canyon** | Multipath and partial loss — often worse than a clean outage | Multiple passes at different times; DMI; more check points |
| **Heavy canopy** | Intermittent loss, plus occlusion of everything above | Passes both directions; seasonal timing; supplementation |
| **Dense traffic** | Occlusion of curb and roadside | More passes; off-peak or night |
| **Standing water** | No return; hides the surface | Do not collect; return when dry |
| **Long GNSS outage** | Trajectory drift beyond published spec | See §13.1 |

> **WHY THIS MATTERS — multipath is worse than a clean outage**
>
> A total outage is honest: the system knows it has no GNSS and relies on the IMU, which
> is well characterised for about a minute.
>
> An urban canyon is not honest. The receiver still gets signals — reflected off buildings,
> arriving late, implying a position that is wrong. The filter may weight that bad
> observation as though it were good.
>
> This is why TMR requires extra passes at different times in poor GNSS environments
> *(§8.2, p.10)*: a different constellation gives a different, uncorrelated multipath
> pattern.

### Recollection decision

| Situation | Decision |
|---|---|
| A run was not recording | **Recollect** that run |
| NAV red across a material extent | **Recollect** |
| Trajectory failed check points over a material extent | **Recollect**, or supplement |
| Localised occlusion of a required feature | **Supplement** conventionally |
| Imagery unusable, LiDAR sound | Recollect **imagery** only, if imagery is a deliverable |
| Point density insufficient for the deliverable | **Recollect** at lower speed |
| Feature is fundamentally not visible from the road | **Supplement** — recollection will not help |

> **IMPORTANT**
>
> The last row is the one that gets missed. If a feature cannot be seen from the roadway,
> driving it again changes nothing. Recognise this at planning (Section 5), not after a
> second mobilisation.

> **PARAMETRIX DECISION REQUIRED**
>
> Define who authorises recollection and how remobilisation cost is handled — whether it
> falls to the project, to overhead, or is recoverable from the client depending on cause.
>
> *Recommended practice:* the project surveyor decides, with the project manager informed
> before mobilisation. Record the cause in the survey report — a pattern of recollections
> from the same cause is a training or equipment signal, not bad luck.

---

## References — Section 13

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7, 42, 49, 53–56, 59 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 34–35 |
| Trimble MX60 Spec Sheet, PN 022516-737C (04/25) | 2 |
| Trimble Business Center Technical Notes: For Mobile Mapping, October 2022 | 4 |

## Other References — Section 13

| Source | Sections |
|---|---|
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §5.2 p.6; §7.1–7.2 p.8; §8.2–8.3 p.10; §9.2.2 p.11; §9.4.1 p.12; §9.4.3 pp.12–14; §10 pp.14–15; §11.7 pp.18–19; §11.8.1 p.19; §14 pp.25–26; App A–D pp.27–30; App E p.31; App F pp.32–33 |
| NCHRP, *Practices for Collecting, Managing, and Using Lidar Data*, 2024 | Ch.5, Quality Assurance, pp.80–82 |


---

# 14. TROUBLESHOOTING

Look up the symptom. Everything here traces to a Trimble source.

> **CAUTION — the overriding rule**
>
> "Do not start a mission before solving any issue you may have had previously with the
> system. **Not doing this may damage the system permanently.**"
> *(MX60 UG Rev B, p.44)*

## 14.1 Power and startup

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Nothing happens on power button press | Held < 15 s | Hold **at least 15 seconds** | Yes | — | No | UG p.21 |
| Power Unit LED not green | Vehicle not supplying 12 V; engine off | Start the vehicle; check source cable and fuses | Not until resolved | Check 35 A fuse, relay, battery | No | UG pp.25, 62; QSG p.8 |
| **Audible alarm during mission** | **Battery Protect — below 10.5 V for >12 s** | **Restore charge immediately. Power cuts after 90 s.** Recovers if voltage rises above 12.0 V within that window | Only if voltage recovers | Check alternator, battery, buffer battery | If power was cut mid-run | UG p.27 |
| System cut out with no warning | Battery Protect cutoff, or a tripped breaker | Check circuit breakers under the Control Unit fuse cover | After resolving | **Check all cables before restarting — the trip may have been a damaged cable** | Yes, for the affected run | UG pp.21, 27 |
| Blinking red LED | Component failed | **Do not start a mission** | No | Contact Trimble Support with log file and serial number | — | UG pp.21, 51 |
| LEDs blink far longer than ~10 s | Startup or update in progress | Wait | — | — | No | UG p.21; QSG p.8 |
| System does not power up after air freight | Possibly powered on before acclimatisation | **Do not retry.** Allow 24 h at constant temperature and pressure | No | Contact Trimble Support | — | UG p.7 |

## 14.2 Connection and TMI

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| System Wi-Fi not visible | System not fully booted; Wi-Fi stick issue | Wait for solid green LEDs; check Wi-Fi USB stick 1 seated | Yes once visible | — | No | UG pp.21, 37 |
| Wi-Fi password rejected / lost | Password is unique and unchangeable | Use the sticker in the Control Unit top case | — | **Contact Trimble Imaging Support with the serial number** | No | TMI p.51; UG p.37 |
| TMI page will not load | Wrong browser; wrong address; no connection | Use **Google Chrome**; `http://tmi.mx-scan.net`; check LAN/Wi-Fi | Yes | — | No | TMI p.7 |
| Ethernet connected but no access | Static IP set on the device | Set to obtain IP **and DNS** automatically (DHCP) | Yes | — | No | UG p.36; TMI p.5 |
| No background map | No Internet connection | Optional — the map is cosmetic. Check WAN or Wi-Fi stick 2 | **Yes** | — | No | TMI pp.8, 32 |
| Cannot connect system to a hotspot | Hotspot requires web-page login | Use a different network — this is not supported | Yes | — | No | TMI p.51 |
| Wi-Fi behaving oddly in a new country | **Country code not set** | `System Administration → WiFi → MX60 WiFi Access Point → country` | Not until set — legal requirement | — | No | TMI pp.5, 51; UG p.48 |

## 14.3 Disks and storage

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| **Start Mission button greyed out** | **Disk check still running** (Initializing/Analyzing) | **Wait for it to finish** | Yes, once complete | — | No | TMI p.38 |
| Disk **Warning** icon | Disk degraded | Mission can run, but **data loss may occur under high system load** | Risk decision | Replace or reformat the disk | No | TMI pp.33–34 |
| Disk **Error** icon | Disk performance compromised | **Do not start a production mission.** Requires confirmation to proceed | No | Replace the disk | If a mission was run on it | TMI pp.33–34 |
| SSD filling during mission | Long mission, high capture rates | Monitor fill status top-right of the map window | Until full | Consider lateral range limit or lower rates next time | If the disk filled mid-run | TMI p.33 |
| Disk not recognised in Data Carrier Dock | Not locked in | Insert, **lock with key, turn 90° clockwise**, then power on | — | — | No | UG p.24 |

> **CAUTION**
>
> **Never connect the USB cable while a data disk is inside the Control Unit.** Remove the
> disk first. *(MX60 UG Rev B, p.10)*

## 14.4 Navigation and initialization

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| **NAV stays red** | No valid solution — poor sky, obstruction, multipath | Move to genuinely open sky. Check the skyplot in Nav View | **No — recording is blocked at red** | — | No | TMI pp.9, 40 |
| NAV reaches orange, will not go green | Attitude/heading not converged | More dynamic manoeuvres — vary speed, 2–3 turns | Recording is permitted, but see §7.3 | Review trajectory quality | Possibly | QSG p.12; TMI p.25 |
| Takes far longer than usual to initialize | Poor constellation; site worse than it looks | Check almanac; relocate; allow the full settling period | Yes | — | No | QSG pp.12, 14 |
| NAV drops green → orange mid-run | Passing obstruction, degraded geometry | Note location using **Comments**. Return to open sky if it persists | Yes, but flag the stretch | Check trajectory over that stretch against check points | Possibly | TMI pp.9, 36 |
| NAV green but position looks wrong on map | Background map offset, or genuine position error | Compare trajectory to the road on the map | Investigate | Verify against control | Possibly | TMI p.33 |
| No blue arrow on the map | No valid position yet | Wait; check sky visibility | No | — | No | TMI p.40 |
| UTC time not displayed | GNSS initialization not complete | Wait; improve sky visibility | No | — | No | TMI p.33 |
| Trajectory recorded but **DMI/GAMS data missing** | **Aiding sensor not activated in Vehicle Settings** | Cannot be fixed retrospectively | — | Verify the checkbox before every mission | Depends on reliance on that sensor | TMI p.21 |

> **IMPORTANT**
>
> The last row is a silent failure. The sensor can be fitted, measured, and connected
> correctly and still log nothing because a checkbox is off. Nothing in the field indicates
> it. Make the checkbox part of the pre-mission check.

## 14.5 Laser

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Laser button **red** | Device error | Check connections; restart if necessary | No | Log file to Trimble Support | Yes, for affected extent | TMI p.9 |
| Laser button **orange** persistently | Not time-synchronized | Wait; if it persists, restart the mission | Not for quality work | — | Possibly | TMI p.9 |
| **Waterfall view shows gaps near the ground** | **Dust filter enabled with wrong installation height** — the mask reaches the ground | Correct install height in Vehicle Settings; reconfigure mission | After correction | — | Yes, for affected extent | Dust Filter Bulletin pp.2–3; TMI p.29 |
| Cloud missing beyond a set distance | **Lateral range limit** enabled | Check Capture Settings — 5–50 m limit discards points beyond it **permanently** | Yes | Cannot be recovered | Yes, if far-field data was required | TMI p.29 |
| Sparse cloud | Speed too high, or low measurement rate | Reduce speed; select a higher laser mode | Yes | — | If density is insufficient | UG p.53; TMR §9.4.1 |
| Excessive noise | Rain, mist, dust, spray | **Avoid operating in rainy or misty weather.** Consider the dust filter *only* on unpaved roads | Judgement call | Cleansing — reclassify, do not delete | Likely | UG p.49; TMR §11.8.1 |
| No returns from wet pavement | Water absorbs / reflects away | Do not collect wet surfaces | No | — | Yes | TMR §9.1 |

## 14.6 Cameras

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Camera button **red** | Device error | Check connections; restart | No | Log file to Trimble Support | Yes, if imagery is a deliverable | TMI p.9 |
| Camera button **orange** | Not time-synchronized | Wait for green before recording | Not for quality work | — | Possibly | TMI p.9 |
| Images too dark or too bright | Exposure | Adjust in Camera View — **Auto** or the slider | Yes | — | If unusable | TMI pp.34–35 |
| Hazy or spotted images | Dirty lens | Clean per the correct method — air first, then optics cleaner on a moist cloth | Yes after cleaning | — | For the affected extent | UG p.50 |
| Water droplets on images | Wet conditions | Stand down — **water on the lens is grounds for rejection** | No | — | Yes | TMR §10 |
| Blown highlights, deep shadow | Low sun angle | Collect between **8am and 4pm** | Judgement call | — | If unusable | TMR §10 |
| Pavement imagery out of focus | Vehicle roof height below 1.60 m | Back-down camera is sharp only from **2.0 to 9.0 m** | — | Vehicle does not meet requirements | Yes | UG pp.54, 59 |

## 14.7 Mission and shutdown

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Record button will not turn red | **NAV is red** — recording blocked | Complete initialization | No | — | No | TMI p.40 |
| Thick blue line missing where a run was driven | The run was not recording | **Re-drive it now, while still on site and initialized** | Yes | — | Yes if not caught on site | TMI p.33 |
| Need different capture settings mid-corridor | — | Use **mission re-configuration** — do **not** close the mission | Yes | — | No | TMI p.41 |
| Closed the mission by mistake | Navigation logging stops immediately on close | Start a new mission — **full re-initialization required** | Yes after re-init | Two missions to process | No | TMI pp.31, 42 |
| Mission shorter than 30 minutes | Below Trimble's stated minimum | Extend the mission before closing | — | Flag in the survey report | Possibly | QSG pp.13–14 |
| Power removed without shutdown | Improper shutdown | — | — | **Verify data integrity carefully — corruption is possible** | If data is corrupt | TMI p.31 |
| Control Unit light still on after shutdown | Shutdown in progress | **Wait up to 90 seconds** | — | — | No | QSG p.13 |
| Web client unresponsive after shutdown | Expected | Reload the web client | Yes | — | No | TMI p.43 |

## 14.8 Escalating to Trimble

**Support contacts** *(MX60 UG Rev B, p.51; TMI UG Rev L, p.55)*:

| | |
|---|---|
| Email | `mx_support@trimble.com` |
| Americas | +1-289-695-4416 |
| APAC | +86-105-603-4179 |
| Europe & Rest of World | +49-7351-474-0237 |

**Provide** *(MX60 UG Rev B, p.51)*:

| ☐ | Item |
|---|---|
| ☐ | Short description of the problem |
| ☐ | The workflow used, and how to reproduce it |
| ☐ | Mission location and environmental conditions, if it occurred during a mission |
| ☐ | **System log file** |
| ☐ | Serial number |
| ☐ | Total operating hours since purchase |
| ☐ | Photos or video |

**Where to get the log file:**

- A system log is written automatically to **removable Disk 1 during shutdown**
  *(TMI UG Rev L, p.43)*
- Or download from **TMI.AI → Log Download** *(TMI UG Rev L, p.50)*
- **System Information Export** generates a further file Support may request
  *(TMI UG Rev L, p.54)*

**Remote support:**

> **CAUTION**
>
> "When remote control of the system is given to Trimble Support, be aware **all data on
> the system are visible** to Trimble Support. If there are confidential data on the
> internal disk, please remove them from the system before granting remote access."
> *(TMI UG Rev L, p.54)*

Remote access requires the system to be connected to a wireless network with Internet
access *(TMI UG Rev L, p.53)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Define the escalation path when an operator hits a problem in the field, and who may
> authorise granting Trimble remote access to the system.
>
> *Recommended practice:* the operator contacts the survey technology group owner first,
> who decides whether to contact Trimble. Remote access requires that owner's approval,
> after confirming no client-confidential data is on the system.

## 14.9 Firmware and licence

| Task | Procedure | Reference |
|---|---|---|
| **Firmware update** | Copy the `.tmx.install` file to a USB stick → USB1 on the Control Unit → TMI.AI → Firmware Update → Refresh → Install. System shuts down; **wait until all Control Unit LEDs are off**, then power back on. **Powering on may take up to 6 minutes** while the update completes | TMI p.49 |
| **Licence update** | Copy the licence file to a USB stick → USB1 → TMI.AI → License → Import | TMI p.53 |
| **Calibration import** | Copy the boresight JSON to a USB stick → USB1 → Settings → Calibration Import | TMI p.18 |

> **CAUTION**
>
> Do not attempt a firmware update immediately before a collection. The process requires a
> full shutdown and a power-on that may take six minutes, and a failed update leaves you
> with no system.

---

## References — Section 14

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7, 10, 21, 24–25, 27, 36–37, 44, 48–51, 53–54, 59, 62 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 5, 7–9, 18, 21, 25, 29, 31–38, 40–43, 49–55 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 8, 12–14 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 2–3 |

## Other References — Section 14

| Source | Sections |
|---|---|
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §9.1 p.11; §9.4.1 p.12; §10 p.15; §11.8.1 p.19 |


---

# APPENDIX A — MX60 FIELD CHECKLIST

Quick reference. Print double-sided and keep it in the vehicle.
Full detail is in the section noted against each block.

---

## A1. Before leaving the office — §5, §6

| ☐ | Item |
|---|---|
| ☐ | Route, pass count and direction planned per pass |
| ☐ | **Satellite almanac checked** — `gnssplanning.com/#/charts` |
| ☐ | Two initialization locations identified — open sky, both ends of the job |
| ☐ | GNSS-hostile stretches mapped; strategy for each |
| ☐ | Weather checked; stand-down criteria understood |
| ☐ | Vehicle height clearances checked on route |
| ☐ | Mechanical check — mounting, screws, torques |
| ☐ | System settings checked — lever arms, sensor settings |
| ☐ | **SSDs prepared** and field protocol printed |
| ☐ | Cleaning kit aboard |
| ☐ | Wi-Fi password sticker accessible |
| ☐ | If air-freighted: **24 h acclimatisation complete** |
| ☐ | If idle > 2 months: run 30–60 min beforehand |

---

## A2. Safety check — before AND after every mission — §6

**Rules:** replace damaged parts immediately · tighten loose screws to correct torque ·
clean or dry anything dirty or wet · **do not start a mission with an unresolved issue**

| ☐ | Check |
|---|---|
| ☐ | Roof rack installed correctly; all screws tight |
| ☐ | Roof rack shows no cracks or deformation |
| ☐ | Sensor Unit damage-free — no scratches or deformation |
| ☐ | **All camera lenses clean and undamaged** |
| ☐ | Sensor in operation position and **properly locked** |
| ☐ | Control Unit undamaged, installed correctly, secured |
| ☐ | Power Unit undamaged, secured, **vents clear** |
| ☐ | All connectors plugged in and fixed |
| ☐ | Cables fixed to roof rack before entering the cabin |
| ☐ | No cable damaged or liable to be damaged |
| ☐ | Operator device working |

---

## A3. Power up — §7

**Order matters — 25 A startup surge**

1. ☐ Engine **auto start/stop OFF**
2. ☐ Both SSDs inserted and **locked**
3. ☐ **Start the vehicle**
4. ☐ Hold Control Unit power button **≥ 15 seconds**
5. ☐ Power Unit LED **constant green**
6. ☐ SU + CU LEDs blink ~10 s → **solid green**

| LED | Meaning |
|---|---|
| Blinking green | Starting / updating / shutting down |
| **Solid green** | Ready |
| **Blinking red** | **Failed — do not start a mission** |

7. ☐ Connect tablet → Chrome → `http://tmi.mx-scan.net`
8. ☐ Wi-Fi country set (first use / new country)

---

## A4. System health before initializing — §7

| ☐ | Check |
|---|---|
| ☐ | Disk check complete — **no Warning or Error icon** |
| ☐ | Correct **Vehicle Preset** — install height matches this vehicle today |
| ☐ | **DMI / GAMS checkboxes ACTIVATED** if fitted |
| ☐ | Correct **Capture Preset** selected |
| ☐ | Camera and Laser buttons **green** |
| ☐ | UTC time showing |
| ☐ | Vehicle parked in open sky |

> **An unactivated DMI or GAMS logs nothing.** Fitted, measured and connected is not
> enough — the checkbox must be ticked.

---

## A5. Initialization — §8

1. ☐ Parked **open sky**, good PDOP, clear of buildings
2. ☐ Mission started — name, area, presets confirmed
3. ☐ **STILL for 2–3 minutes**
4. ☐ Blue arrow visible; UTC time showing
5. ☐ **Drive straight ~20 m** → NAV **red → orange**
6. ☐ **Vary speed + 2–3 dynamic turns** → NAV **orange → green**
   Example: `0 → 50 → 20 → 50 → 20 km/h`
7. ☐ All parameters green in Nav View
8. ☐ **Wait — up to 10 more minutes** before logging
9. ☐ Initialization time and location recorded

| NAV | Meaning | Record? |
|---|---|---|
| **Red** | No valid solution | **Blocked** |
| **Orange** | Solution exists | Permitted — but not for survey grade |
| **Green** | Meets accuracy figures | **Yes** |

---

## A6. During collection — §9

**Press Record** — green → red. **Stop** — red → green.
Record button controls **laser and imagery only**; navigation logs continuously.

**Speed: 80 km/h (50 mph) recommended max · 110 km/h absolute max**
Drive smoothly — no harsh acceleration, braking or steering.

### Monitor in a loop

| Watch | Good | Act if |
|---|---|---|
| **NAV** | Green | Orange — note it · **Red — recording blocked** |
| **Camera / Laser** | Green | Orange or **red** |
| **Record** | **Red on a run** | Green when you think you're recording |
| **Thick blue line** | Over every collected stretch | Missing where you drove a run |
| **SSD fill** | Space remaining | Approaching full |
| **UTC time** | Displayed | Missing |
| **Disk icons** | None | Warning / Error appears |
| **Audible alarm** | Silent | **Battery Protect — 78 s to restore charge** |

☐ Use **Comments** to time-tag events into the mission database
☐ **Minimum mission time: 30 minutes**

**Need different capture settings?** Use **mission re-configuration** — do NOT close the
mission. No re-initialization needed.

---

## A7. Ending the mission — §10

1. ☐ Stop recording the final run
2. ☐ Drive to an initialization point, dynamic manoeuvres on the way
3. ☐ **FINALIZE SEQUENCE — mirror of the start:**
   a. ☐ Dynamic steering manoeuvres
   b. ☐ Vary speed — accelerate / decelerate
   c. ☐ Drive straight
   d. ☐ **STILL for 2–3 minutes**
4. ☐ **Review the map — thick blue line over every intended stretch**
5. ☐ Close mission → **Complete Mission**
6. ☐ Shut down → **Shutdown**
7. ☐ Wait for power button light **OUT** — up to 90 s
8. ☐ Field protocol complete — runs, directions, date, mission, system S/N
9. ☐ Post-mission safety check (A2)

> **Never power off by removing power.** Use Complete Mission AND Shutdown, or risk
> corrupted data.

> **Do the map review before closing.** If a run is missing and you're still on site and
> initialized, you can re-drive it. Ten minutes later you cannot.

---

## A8. Data handling — §11

| ☐ | Step |
|---|---|
| ☐ | System fully shut down before removing disks |
| ☐ | **Unlock and remove BOTH SSDs** — they are one dataset |
| ☐ | Offload via Data Carrier Docks, USB 3 (use both — halves the wait) |
| ☐ | **Verify:** navigation data · both lasers · panoramic · back-down camera · Mission Report · logs |
| ☐ | File count and size match source |
| ☐ | **Back up before any processing** |
| ☐ | **Only then** prepare SSDs for the next mission |

> **Never connect USB while a disk is in the Control Unit.** Remove it first.

> **Never delete raw mission data** because processing succeeded or the deliverable shipped.

---

## A9. Stop-work triggers

| Situation | Action |
|---|---|
| **Blinking red LED** | Do not start / stop the mission |
| **Disk Error icon** | Do not run a production mission |
| **Battery Protect alarm** | Restore charge within 78 s or power cuts |
| **NAV red across a material extent** | Nothing is recording — fix before continuing |
| **Rain or mist** | Trimble says avoid operating |
| **Unresolved fault from a previous mission** | Do not start |

---

## A10. Support — §14

**`mx_support@trimble.com`** · Americas **+1-289-695-4416**

Provide: problem description · workflow to reproduce · mission location and conditions ·
**system log file** · serial number · total operating hours · photos or video

Log file: auto-saved to **removable Disk 1 during shutdown**, or TMI.AI → Log Download.

> Granting remote access makes **all data on the system visible to Trimble Support**.
> Remove confidential data first.

---

*Sources: MX60 User Guide Rev B (May 2025) · MX60 Quick Start Guide Rev B (March 2025) ·
TMI Software User Guide Rev L (April 2026) · Dust Filter Bulletin (January 2025).
Page-level citations are in the numbered sections.*


---

# APPENDIX B — TMI STATUS AND WARNING REFERENCE

Every indicator TMI shows, what it means, and whether it needs action now.

---

## B1. Status buttons

### Camera and Laser

| Colour | Meaning | Action |
|---|---|---|
| **Red** | Device error | **Stop.** Do not collect quality data |
| **Orange** | Not yet time-synchronized | Wait for green |
| **Green** | Time synchronization complete | Proceed |

*(TMI UG Rev L, pp.8–9)*

### Navigation — different rules

| Colour | Meaning | Recording | Action |
|---|---|---|---|
| **Red** | No valid solution, or navigation system failure | **Blocked by the system** | Improve sky visibility; complete initialization |
| **Orange** | A navigation solution is available | **Permitted by TMI** | Continue initializing to reach green |
| **Green** | Solution meets your **user accuracy figures** | Yes | Proceed |

*(TMI UG Rev L, pp.9, 25, 40)*

> **IMPORTANT**
>
> TMI *permits* recording at orange. The Quick Start Guide directs you to wait for
> **green** *(QSG Rev B, pp.12, 14)*. Orange means only that a solution exists.

### Record button

| Colour | Meaning |
|---|---|
| **Red** | Data logging **active** |
| **Green** | **No** data logging |

*(TMI UG Rev L, p.9)*

> Counter-intuitive: **red means recording**. Green means you are not.

---

## B2. What "green" means numerically

The orange→green threshold is set in **Capture Settings → User Accuracies for Navigation**.

| Parameter | MX60 **Premium** | MX60 **Core / Pro** |
|---|---|---|
| Attitude RMS (roll/pitch) | 0.060° | 0.075° |
| Heading RMS | 0.045° | 0.045° |
| Position RMS | 10.000 m | 10.000 m |
| Velocity RMS | 0.025 m/s | 0.030 m/s |

*(TMI UG Rev L, p.26)*

> Position RMS defaults to **10 m**. Green is driven by attitude, heading and velocity —
> not absolute position. See §7.4.

> **CAUTION** — changing these "can ONLY be done by advanced users"
> *(TMI UG Rev L, p.25)*.

---

## B3. Navigation logging — three rules that surprise people

| Rule | Source |
|---|---|
| Navigation logging **starts automatically** when a valid position exists and the blue arrow appears — **even if NAV is still red** | TMI p.40 |
| Navigation logging is **not affected** by orange↔green transitions | TMI pp.36, 40 |
| Navigation logging **stops immediately** when the mission is closed | TMI pp.31, 42 |

**Consequence:** the trajectory records long before you press Record and continues between
runs. The Record button starts and stops **laser and imagery only**.

---

## B4. Map window indicators

| Indicator | Meaning |
|---|---|
| **Blue arrow** | Valid position available — navigation logging has begun |
| **Thin blue line** | Trajectory |
| **Thick blue line** | **Areas where data was recorded** |
| **UTC time** (top right) | Appears when GNSS initialization is complete |
| **SSD fill status** (top right) | Remaining capacity |
| No OSM background | System has no Internet connection — cosmetic only |

*(TMI UG Rev L, pp.32–33, 40)*

> **FIELD TIP**
>
> The **thick blue line** is the single best in-vehicle QC check. Every stretch you meant
> to collect should be thick. Thin where you believed you were recording = a run that
> never started.

---

## B5. Disk check states

Checked at system startup and after each mission.

| Icon | Meaning | Can you continue? |
|---|---|---|
| **None** | Everything is fine | Yes |
| **Warning** | Mission can run, but **data loss may occur under high system load** | Risk decision — not for production |
| **Error** | **Disk performance compromised; proceeding may lead to data loss** | Requires explicit confirmation — recommend no |

*(TMI UG Rev L, pp.33–34)*

Click an icon for detail. The **Start Mission button is disabled while a disk check is
running** *(TMI UG Rev L, p.38)*.

---

## B6. Message Log

`Menu → Message Log`. Filters *(TMI UG Rev L, p.16)*:

| Filter | Shows |
|---|---|
| **All** | Every logged event |
| **Alarm** | Alarm events only |
| **Warning** | Warning events only |

Sortable by user name.

> **FIELD TIP**
>
> Check the Alarm filter before closing a long mission. Something may have been logged
> hours ago that nobody saw at the time.

---

## B7. Views

| View | Contents |
|---|---|
| **Dashboard** | Navigation status; camera thumbnails |
| **Camera** | Real-time preview per camera + exposure control |
| **Nav** | Per-parameter accuracy on a **logarithmic** scale, status, **satellite skyplot** |
| **Laser** | Reduced real-time data stream — the **waterfall view** |

*(TMI UG Rev L, pp.34–37)*

**Camera exposure, adjustable live** *(TMI UG Rev L, pp.34–35)*:

| Camera | Control |
|---|---|
| Panoramic | **Auto** button, or slider mixing exposure time and gain |
| Back-down | Exposure compensation slider |

Slider **left = darker**, **right = brighter**.

---

## B8. Actions that need care

| Action | Effect | Reference |
|---|---|---|
| **Complete Mission** | Stops the mission **and navigation logging** immediately | TMI pp.31, 42 |
| **Shutdown** | Powers off all sensors and the control unit | TMI p.31 |
| **Mission re-configuration** | Changes capture settings; sensors restart; **navigation logging continues — no re-initialization** | TMI p.41 |
| **Removing power directly** | **Risk of corrupted data — never do this** | TMI p.31 |
| **Calibration Import** | Loads a new boresight JSON from USB1 | TMI p.18 |
| **Firmware update** | Full shutdown; power-on may take **up to 6 minutes** | TMI p.49 |
| **Remote access** | **All data on the system becomes visible to Trimble Support** | TMI p.54 |

---

## B9. Settings that silently lose data

The four ways to collect nothing while everything looks normal.

| Setting | Failure |
|---|---|
| **DMI / GAMS checkbox not activated** in Vehicle Settings | That sensor logs **nothing**, even though it is fitted, measured and connected *(TMI p.21)* |
| **Sensor deactivated** in Capture Settings | That laser or camera records nothing |
| **Lateral Range Limit** enabled (5–50 m) | Points beyond the limit are **discarded permanently** *(TMI p.29)* |
| **Dust filter with wrong install height** | Mask reaches the ground — data loss, visible as gaps in the waterfall view *(TMI p.29; Dust Filter Bulletin pp.2–3)* |

> **IMPORTANT**
>
> None of these produce an error. All four are prevented by the same habit: confirm the
> Vehicle Preset and Capture Preset at the start of every mission, out loud, against the
> field protocol.

---

*Sources: TMI Software User Guide Rev L, April 2026 (P/N T001242) · MX60 Quick Start
Guide Rev B, March 2025 · Product Bulletin: Enabling the Dust Filter in TMI for MX60,
January 2025.*


---

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


---

# APPENDIX D — PARAMETRIX DECISION REGISTER

Every **PARAMETRIX DECISION REQUIRED** item in this SOP, consolidated.

> **IMPORTANT**
>
> Nothing in this register is current Parametrix policy. Each row is an open question with
> a recommended answer. The recommendations are drawn from Trimble documentation, the
> Queensland TMR guideline, and NCHRP practice — they are **not** Parametrix standards
> until formally adopted.

**35 items.** Priority reflects what blocks first use of the system, not importance in the
abstract.

| Priority | Meaning |
|---|---|
| **P1** | Blocks first production collection |
| **P2** | Needed before delivering to a client |
| **P3** | Needed for a mature, repeatable programme |

---

## P1 — Blocks first production use

| # | § | Decision | Recommended |
|---|---|---|---|
| 1 | 1 | **Which MX60 configuration** — Core, Pro or Premium? Record serial number and accessories | Record in §1 and repeat on the field checklist. It sets imagery resolution, attitude accuracy and every spec table row |
| 2 | 1, 3 | **Are GAMS and DMI owned and fitted?** | Fit both. GAMS removes an initialization step the operator can get wrong; DMI protects the trajectory where mobile mapping is weakest |
| 3 | 1 | **Which mounting rack** — MX SCAN Roof Rack or MX Shock Absorbing? | Record it. Determines install procedure, and the published GAMS corner offsets apply to the standard rack **only** |
| 4 | 1 | **What does "trained" mean?** Required training, sign-off, supervised experience | Complete the Appendix E exercise, participate in one supervised production collection, sign-off by an experienced operator. Maintain a qualified-operator list |
| 5 | 6 | **Who measures lever arms**, by what method, recorded where, re-verified when | Trained-personnel task with a written record: date, who, method, values, vehicle condition. Re-verify after any disturbance to Sensor Unit, GAMS, DMI or rack |
| 6 | 6 | **Field protocol form** — Trimble requires order of runs, direction, date, mission, system S/N | One page capturing Trimble's fields plus operator, vehicle, weather, install height, preset names, initialization times and locations, and events |
| 7 | 7 | **Is recording at orange NAV ever permitted?** | Prohibit for survey-grade. Permit for asset-grade only with the project surveyor's approval, recorded in the field protocol |
| 8 | 9 | **Standard collection speed** and conditions for reducing it | At or near prevailing traffic up to 80 km/h. Reduce for high-detail extraction, dust, or density needs. Never exceed 80 km/h operating |
| 9 | 11 | **Backup standard** — copies, media, locations, retention | Three copies, two media types, one off-site. Raw data retained for project life plus records retention |
| 10 | 11 | **Raw data storage location and folder structure** | One project folder: `01-raw` (read-only once verified), `02-trajectory`, `03-pointcloud`, `04-imagery`, `05-control`, `06-qc`, `07-deliverables`, `08-field-records` |
| 11 | 11 | **Project and mission naming convention** | Keep TMI's automatic directory naming; carry the Parametrix project number in the mission name field, so it lands inside the mission database |

---

## P2 — Before client delivery

| # | § | Decision | Recommended |
|---|---|---|---|
| 12 | 5 | **Minimum pass count**, and who may authorise fewer | Three passes for survey-grade. TMR permits fewer only by agreement and warns against it. Written approval from the project surveyor, recorded in the survey report |
| 13 | 5 | **Control standard** — base strategy, max baseline, control spacing, check point density | Own base on project control, short baselines. Control at both project ends and at significant intersections. Check points in **both good and poor GNSS environments** |
| 14 | 5 | **Wet-weather rule.** Trimble says avoid rain and mist; TMR says no imagery in wet; neither defines "wet" | No collection during active precipitation. After rain, wait until pavement is visibly dry. Operator has explicit authority to stand down without approval |
| 15 | 5 | **Traffic control** by roadway class, and go/no-go without it | None needed where the vehicle travels at or near prevailing speed in a normal lane. Required where collection speed is materially below traffic, or where a pass requires stopping, reversing or occupying a shoulder |
| 16 | 13 | **Numerical tolerances** for accept / review / recollect | **None are proposed** — the sources contain none. Adopt ASPRS 2014 or NSSDA, and TMR's four-way structure: horizontal and vertical, absolute and relative, relative within a 200 m sliding window |
| 17 | 13 | **Useful range statement** with every deliverable? | Yes, every project. A few lines in the survey report; prevents the most common and expensive client misunderstanding |
| 18 | 13 | **Imagery privacy** — blurring, access, delivery, retention, removal requests | Raw imagery internal and restricted. Blur faces and plates on anything delivered or published. Decide before the first project that publishes imagery |
| 19 | 13 | **Who authorises recollection**, and how remobilisation cost is handled | Project surveyor decides, project manager informed before mobilising. Record the cause — a pattern is a training or equipment signal |
| 20 | 5, 12 | **Boresight calibration policy** — frequency, who performs it, what triggers an unscheduled one, and how the calibration in force is recorded | Defined interval plus after any event that could disturb the sensor head or rack. Record calibration date and values in the field protocol. Establish a standard calibration site (§5.7). **Two answers needed first: which TBC version Parametrix runs, and whether daily Sensor Unit removal counts as "disturbed"** |
| 21 | — | **Document control** — owner, number, approval authority, review cycle, controlled copy | Owner in the survey technology group; approval by a licensed professional surveyor; annual review or on any new Trimble revision |

---

## P3 — Programme maturity

| # | § | Decision | Recommended |
|---|---|---|---|
| 22 | 3 | **Is the Sensor Unit removed and cased daily?** | Yes — follow Trimble's assumption. Protects an expensive item from weather, theft and clearance accidents. Note this means GAMS comes off too, so its lever arm is re-measured each morning |
| 23 | 5 | **Standard calibration site** — identify and record one meeting the §12.3 crossing requirements | Scout one near the office; document with an aerial image and the four run lines; note it in the field protocol whenever a calibration mission is driven |
| 24 | 5 | **Night collection** — when permitted, safety measures, client handling | Permit where imagery is not a deliverable and parked-vehicle occlusion would otherwise force recollection. Agree with the client in advance — imagery **will** be unusable |
| 25 | 6 | **How second-person torque verification is recorded** | Dated sign-off on the installation record naming both people. Repeat after any disassembly |
| 26 | 7 | **Factory user-accuracy defaults, or Parametrix values?** Who may change them | Use factory defaults. Restrict changes to named trained personnel; record any change in the field protocol — a mission on altered thresholds is not comparable to one on defaults |
| 27 | 7 | **Standard capture presets and naming** | Build named presets in advance — corridor, dust, urban — and export to file as a backup and for replication to a second system |
| 28 | 7 | **Rule for proceeding past a disk Warning or Error** | Never start a production mission on Error. Treat Warning as grounds for swapping the disk before a long collection |
| 29 | 8 | **Full manoeuvre sequence even with GAMS fitted?** | Perform it anyway. Costs minutes, matches the Quick Start checklist, and gives the office strong initialization at both ends regardless |
| 30 | 8 | **Re-initialization triggers** | After NAV degradation not recovered in a few minutes of open sky; after any outage materially longer than 60 s if critical data follows; whenever a mission has been closed. Record every initialization |
| 31 | 11 | **Retention and archive policy** — who may authorise deletion of raw data | Never deleted by the project team. Deletion requires survey technology group owner sign-off after the retention period |
| 32 | 11 | **Chain of custody** — when formal handling applies | Standard projects: field protocol and dated backups suffice. Litigation or forensic work: documented chain from the moment disks leave the vehicle, with checksums |
| 33 | 11 | **How many SSD sets in circulation** | At least one spare. A single set means the crew cannot mobilise until the previous offload verifies — which is exactly the pressure that causes someone to skip verification |
| 34 | 13 | **Periodic system verification** using Trimble's retro-reflective target check | Permanent target array at a Parametrix facility, surveyed conventionally. Quarterly, before major campaigns, and after any disturbance. Retain results as a trend |
| 35 | 14 | **Field escalation path**, and who may grant Trimble remote access | Operator contacts the survey technology group owner, who decides on Trimble contact. Remote access needs that owner's approval after confirming no client-confidential data is on the system |

---

## Blocked pending Trimble documentation

One item remains blocked. **Boresight calibration is no longer among them** — the procedure
is documented at §12.3, sourced from TBC Help.

| Blocker | Needed |
|---|---|
| Section 12 office procedure | Current TBC mobile mapping documentation covering import, trajectory processing, registration and export for the MX60. The supplied Technical Notes is October 2022 and predates MX60 support |


---

## How to use this register

1. Work P1 first — those eleven items block the first production collection
2. Assign an owner and a date to each
3. When adopted, replace the **PARAMETRIX DECISION REQUIRED** callout in the relevant
   section with the decided standard, and note the decision date
4. Keep this register as the record of what was decided and when

> **PARAMETRIX DECISION REQUIRED**
>
> Nominate an owner for this register and a target date for closing the P1 items.
>
> *Recommended practice:* the survey technology group owner named under item 21, with P1
> closed before the first production collection and P2 before the first client delivery.


---

# APPENDIX E — FIRST DAY TRAINING EXERCISE

For someone who has never operated a mobile mapping system. **Not a production project** —
nothing collected here should be delivered to a client.

**Time:** one field day plus one office half-day.
**Crew:** trainee, an experienced operator, and a driver.

---

## E1. What the trainee should be able to do afterwards

- Set the system up and take it down safely, unsupervised
- Run a mission start to finish, including both initializations
- Read every TMI status indicator and say what it means
- Recognise a bad collection **while still on site**
- Explain why the trajectory determines everything
- Point at real occlusions in their own data and say why they happened

---

## E2. Route

Pick a route with these five features. It does not need to be long — 5 to 10 km is plenty.

| Feature | Why |
|---|---|
| **Open-sky area** for initialization, both ends | The exercise cannot start without it |
| **A straight segment**, ~500 m, driveable both ways | Repeat-pass comparison |
| **An intersection** | Coverage geometry and turn behaviour |
| **A GNSS-challenged stretch** — underpass, tree canopy, or buildings both sides | Watching NAV degrade is the lesson |
| **Something the vehicle cannot see** — behind a barrier, a ditch, a structure | Teaches limits better than any explanation |

> **FIELD TIP**
>
> Choose the GNSS-challenged stretch so the vehicle is under it for **15–45 seconds** at
> collection speed. Long enough to see degradation, short enough to recover.

---

## E3. Field exercise

### Part 1 — Setup (trainee leads, operator supervises)

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Walk the components checklist (Appendix A2) | What "before and after every mission" actually covers |
| ☐ | Mount the Sensor Unit — **two people** | Weight, lock mechanism, why one person cannot do it |
| ☐ | Cable the system, secure everything | Which end is which; why cables are fixed before entering the cabin |
| ☐ | Clean the optics using the correct method | Air first, then a moist — not dripping — cloth |
| ☐ | Measure installation height from the ERP | Where the External Reference Point is, and why ~1 cm matters |
| ☐ | Create a Vehicle Preset | Where the measurement goes and what depends on it |

**Talking point:** ask the trainee what happens if the install height is entered 10 cm too
high and the dust filter is on. *(Answer: the mask reaches the ground and data is lost —
visible immediately in the waterfall view.)*

### Part 2 — Startup

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Power up in the correct order | Why the vehicle starts **first** — 25 A surge |
| ☐ | Watch the LED sequence | Blink ≈ 10 s, then solid green |
| ☐ | Connect the tablet, open TMI | Chrome, `tmi.mx-scan.net`, no software installed |
| ☐ | Find every status button and name its colours | The vocabulary for the rest of the day |
| ☐ | Open Capture Settings; find User Accuracies | What "green" actually means numerically |

**Talking point:** Position RMS defaults to 10 m. Ask why green is not a promise of a
centimetre corridor.

### Part 3 — Initialization (the core lesson)

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Park in open sky; start the mission | Site selection matters |
| ☐ | **Sit still 2–3 minutes** — watch the clock | It feels long. It is not optional |
| ☐ | Note when the blue arrow and UTC time appear | Navigation logging has **already started** |
| ☐ | Drive straight ~20 m — **watch NAV go red → orange** | Seeing the transition is the point |
| ☐ | Vary speed, 2–3 turns — **watch orange → green** | Dynamics create observability |
| ☐ | Open Nav View; identify which parameter converged last | Usually heading. Ask why |
| ☐ | Wait the settling period | Green is the start of convergence, not the end |

**Talking point:** why can roll and pitch be solved sitting still, but not heading?
*(Gravity gives an absolute vertical reference. Nothing gives an absolute heading
reference — it must be inferred from motion, or measured by GAMS.)*

### Part 4 — Collection

| ☐ | Run | Purpose |
|---|---|---|
| ☐ | **Run 1** — straight segment, direction A | Baseline |
| ☐ | **Run 2** — straight segment, direction B | Repeat-pass comparison |
| ☐ | **Run 3** — straight segment, direction A again | Three-pass redundancy |
| ☐ | **Run 4** — through the intersection, both approaches | Coverage geometry |
| ☐ | **Run 5** — the GNSS-challenged stretch, **watching NAV throughout** | The key observation of the day |
| ☐ | **Run 6** — past the feature the vehicle cannot see | Limits |

During every run the trainee monitors and calls out: NAV colour · camera and laser status ·
**thick blue line appearing** · SSD fill.

| ☐ | Extra exercises |
|---|---|
| ☐ | Enter a **Comment** when NAV degrades — see it time-tag |
| ☐ | Open the **waterfall view** while driving |
| ☐ | Adjust panoramic exposure entering and leaving shade |
| ☐ | Perform a **mission re-configuration** to a different capture preset — note no re-initialization is required |

**Talking point:** during Run 5, ask the trainee to predict what the point cloud will look
like there. Check the prediction in the office.

### Part 5 — Ending

| ☐ | Task | Learning |
|---|---|---|
| ☐ | **Review the map before closing** — thick blue line over every run | The last moment a missing run is cheap |
| ☐ | Perform the **full finalize sequence** | Mirror of the start, and why |
| ☐ | Complete Mission, then Shutdown | Never by removing power |
| ☐ | Wait for the light to go out — up to 90 s | Patience is part of the procedure |
| ☐ | Complete the field protocol | What the office will need |
| ☐ | Post-mission safety check | It happens after, not just before |

**Talking point:** what would have been lost by skipping the finalize sequence?
*(The reverse-processing pass loses its anchor. The middle of the mission — already the
weakest part — is then solved from one strong end instead of two.)*

---

## E4. Office exercise

### Part 6 — Data handling

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Remove both SSDs; offload via both Docks | Why USB is never connected with a disk in the Control Unit |
| ☐ | Find navigation data on the SSD 1 copy | Why the two disks are one dataset |
| ☐ | Locate the Mission Report and system log | What exists for troubleshooting |
| ☐ | Verify, **then** back up, **then** clear the disks | The order matters |

### Part 7 — Inspect the results

| ☐ | Inspection | Look for |
|---|---|---|
| ☐ | **Trajectory** — plot reported accuracy along the route | Spikes at the GNSS-challenged stretch. Compare to what was seen live |
| ☐ | **Point cloud, overall** | Coverage against the route driven |
| ☐ | **Repeat passes 1 vs 2 vs 3** — before any registration | How far apart are they? This is the system's internal consistency |
| ☐ | **Cross-section** through the straight segment | Thickness of the road surface across passes |
| ☐ | **The GNSS-challenged stretch** | Is the cloud displaced? Does it recover? |
| ☐ | **Near vs. far from the vehicle** | Density and noise as range increases |
| ☐ | **The intersection** | Coverage gaps at corners |
| ☐ | **Occlusions** — list every one found | Traffic, parked cars, barriers, vegetation |
| ☐ | **The feature that could not be seen** | Confirm it is genuinely absent |
| ☐ | **Imagery** | Exposure, blur, lens cleanliness, coverage |

### Part 8 — Write it up

The trainee writes one page:

1. What was collected, and how
2. Repeat-pass agreement — the actual number
3. Where trajectory quality degraded, and by how much
4. Every occlusion found, and its cause
5. What could not be captured at all, and what would be needed instead
6. What they would do differently

> **IMPORTANT**
>
> Item 5 is the one that matters. A trainee who can look at their own data and say
> "this ditch invert needs conventional survey, and no amount of re-driving will fix it"
> has understood mobile mapping.

---

## E5. Assessment

| ☐ | Competency |
|---|---|
| ☐ | Mounted and dismounted the Sensor Unit safely, two-person |
| ☐ | Measured installation height correctly and entered it |
| ☐ | Powered up in the correct order |
| ☐ | Completed initialization unprompted |
| ☐ | Named every status indicator and its colours |
| ☐ | Monitored correctly during runs, and noticed at least one real event |
| ☐ | Performed the finalize sequence unprompted |
| ☐ | Shut down and offloaded correctly |
| ☐ | Identified occlusions in their own data |
| ☐ | Explained why the trajectory determines everything |
| ☐ | Identified where conventional survey is required |

> **PARAMETRIX DECISION REQUIRED**
>
> Confirm whether this exercise, plus supervised participation in a production collection,
> is sufficient for an operator to work unsupervised — and who signs it off.
>
> *Recommended practice:* both required, signed off by an experienced operator, recorded
> on a qualified-operator list. See Appendix D item 4.

---

## E6. Things to deliberately show, not explain

Five demonstrations worth more than a paragraph each:

1. **Sit through the full static period in silence.** Two to three minutes is longer than
   anyone expects, and that is the lesson.
2. **Watch NAV go red → orange → green in real time.** Nobody forgets seeing it.
3. **Point at the thick blue line** and say "that is your proof you were recording."
4. **Open the repeat passes side by side** and let the trainee see they do not perfectly
   coincide — before registration hides it.
5. **Stand at the feature the vehicle could not see**, then show its absence in the cloud.
