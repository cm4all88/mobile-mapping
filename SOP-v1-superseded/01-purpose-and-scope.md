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
