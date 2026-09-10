# Stage 1 — Source Analysis for the Parametrix MX60 Mobile Mapping SOP

**Prepared:** 2026-09-10
**Revision 2** — updated after receipt of the MX60 User Guide, spec sheet, and mounting rack guide.
**Status:** For review. No SOP drafting has begun.

---

## Headline

The collection now totals **723 pages across 12 PDFs (9 distinct documents)**, of which
**82 pages are authoritative Trimble MX60 documentation**.

This is a decisive change from Revision 1. Sections 3 (System Components), 6 (Equipment
Preparation), and 7 (Vehicle Installation) are now **fully sourced** and can be written
to a high standard. Safety, specifications, mounting, lever arms, power, cabling, and
maintenance are all covered directly by Trimble.

**Two documents remain outstanding**, and they hold the operational heart of the SOP:

1. **Trimble TMI Software for Trimble Mobile Mapping Systems User Guide**
2. **Trimble MX60 Quick Start Guide**

The MX60 User Guide names both explicitly and defers to them. Between them they contain
the initialization procedure, the mission workflow, the TMI interface, and — in the Quick
Start Guide's own words as cited by the User Guide — the *"standard operation workflow"*
and the *"In-the-field operation checklist."* Sections 8, 9, 10, 12, and 13 cannot be
written without them.

---

## 1. Source inventory

### Tier 1 — Authoritative Trimble MX60 documentation (82 pages)

#### 1.1 Trimble MX60 User Guide, Revision B

| Field | Value |
|---|---|
| Date / version | **May 2025, Revision B**, P/N T001983 |
| Publisher | Trimble Inc. |
| Pages | 68 printed (supplied as two PDFs: 36 + 32 pages) |
| Appears current | **Yes — the authoritative MX60 hardware document** |

**Document history** (p.2): Rev A May 2024 first release; **Rev B May 2025** updated the
support email address and the *AP+ Positioning System Performance* and *External-Signal
Connector* sections. Applies to "Trimble MX60 and all of its variants."

**Completeness.** The two PDFs are sequential and complete — part 1 covers printed pages
1–36, part 2 covers 37–68, ending at the final appendix. No gaps.

**Structure.** Safety Instructions (pp.7–11) · 1 System Overview and Installation
(pp.12–43) · 2 Operation (pp.44–48) · 3 Maintenance and Support (pp.49–51) · Appendix
(pp.52–68).

**Note the shape of this document: it is a hardware guide.** "Operation" is five pages,
and it covers the safety check, the External Reference Point, lever-arm measurement, and
prerequisites — then hands off to TMI and the Quick Start Guide for everything else.

**What it unblocks — Section 3 (System Components).** Three main devices: MX60 Sensor
Unit, MX SCAN Control Unit 2, MX SCAN Power Unit, plus the MX SCAN Roof Rack (p.12).
Three configurations — **Core, Pro, Premium** — differing in the 360° camera and/or
GNSS/IMU system (p.12). Sensor Unit contains two laser scanners, a 360° panoramic
camera, a down-looking camera, and the GNSS/IMU position-and-orientation system (p.13).
Control Unit front panel is documented element by element, including LED semantics and
both circuit breakers (pp.20–21). Power Unit properties including Battery Protect
behaviour (p.27). Data Carrier Docking Station procedure (p.24).

**What it unblocks — Section 6 (Equipment Preparation).** A Trimble-authored
**Components Checklist** (p.44) — roof rack screws and cracks, sensor damage and lens
cleanliness, lock state, control unit security, power unit ventilation, every cable
connection, and the user interface device. Plus the safety-check rules: complete a check
before *and* after each mission, exchange broken parts immediately, and **do not start a
mission before resolving any prior system issue** (p.44).

**What it unblocks — Section 7 (Vehicle Installation).** This is the richest yield:

- **External Reference Point** location: right side, at the back of the MX SCAN Roof Rack (p.45)
- **Installation Height**: measured from the ERP down to the road surface, in metres,
  absolute value; roof rack must be horizontally aligned during measurement (pp.46–47)
- **Vehicle Frame convention**: +X forward, +Y right of vehicle, **+Z downward** (p.46)
- **Sign caution**: a DMI on the left wheel has a **negative Y** lever arm (p.46)
- DMI lever arm measured to the centre of the tread; the **DMI wheel must be non-steering** (p.46)
- GAMS lever arm measured to the **L1 antenna phase centre** (pp.46, 67)
- Values are stored as a **Vehicle Preset in TMI**; **CAUTION — incorrect values produce
  faulty navigation solutions; enter to the order of 1 cm** (p.47)
- **POSPac note**: the MX60 System Reference Frame origin differs from the ERP; TMI adds
  internal vectors, so POSPac shows corrected lever arms that differ from the mechanical
  measurements. Operators who don't know this will think something is wrong (p.47)
- GAMS accuracy tiers: **10 cm is enough for collection only; a few millimetres and a
  ≥2.0 m baseline are required if the navigation data will be post-processed**; both
  antennas must be the same type (p.68)
- GAMS known offsets from the standard Roof Rack's top-left front corner to the ERP:
  **X = +1.006 m, Y = −0.469 m, Z = +0.025 m** (p.68)
- **GAMS must be re-measured every time it is re-installed** (p.67)
- Sensor Unit install/uninstall procedures, step by step, **two people required** (pp.16–19)
- Roof rack limits: **max overhang 330 mm, min bracket spacing 650 mm** (marked by a red
  stripe on the mainframe), screws No.5 to **8 Nm** (pp.31–33)
- **Screw tightening discipline**: clusters tightened crosswise in three steps at
  33% / 66% / 100% of final torque, and **a second person must verify the torque** (pp.10–11)
- Cable lengths that constrain the layout: Power Unit→Control Unit **3 m**,
  Control Unit→Sensor Unit **5 m** (p.59)
- Vehicle requirements (p.59): rubber wheels, paved roads, **no bright colour** (exposure
  artefacts), hatchback with upright rear door, **minimum 1.60 m roof height** to satisfy
  the down camera's minimum distance, **start/stop must be switched off**, sufficient
  alternator or an added battery pack, **60 Ah minimum**
- Power supply installation, both direct and buffer-battery setups, with fuse ratings
  (pp.61–62), and the instruction that installation **must be done by a professional
  automotive electrician**

**Operating limits that belong in the SOP as hard rules:**

- **Maximum vehicle speed 110 km/h (68 mph)** — operating or not (pp.9, 53)
- **Recommended maximum speed with the system operating: 80 km/h (50 mph)** (p.53) —
  this is the single most important driving number in the collection
- Operating temperature −10 °C to +50 °C, with the footnote *"not exposed to direct sun
  and without driving less than 10 km/h (6 mph)"* — i.e. **prolonged slow or stationary
  operation in direct sun is outside the rated envelope** (p.53)
- **IP64 Sensor Unit; IP30 Power Unit and Control Unit** — the units inside the cabin are
  not waterproof (p.53)
- **24 hours acclimatisation after air freight** before switching on, or condensation can
  short the electronics (p.7)
- **The driver is not allowed to operate the system while driving**; a dedicated second
  person is recommended (p.9)
- **On/Off button must be held a minimum of 15 seconds** to start (p.21)
- LED semantics: blinking green = starting/updating/shutting down · solid green = ready ·
  **blinking red = component failed** (p.21)
- Battery Protect: audible warning below **10.5 V for >12 s**; **power cut after 90 s**
  below 10.5 V; recovery if voltage rises above **12.0 V** within that window (p.27)
- **Never connect the USB cable while the exchangeable data disk is inside the Control
  Unit** — remove the disk first for backup (p.10)
- Clean all sensor optics before each mission; cleaning during a mission may be necessary
  depending on weather and road surface (p.10)
- **Avoid operating in rainy or misty weather** (p.49)
- If unused, run the system **30–60 minutes every two months** (p.9)
- Trimble's own recommended data-quality check: scan ~8 flat retro-reflecting targets at
  varied distances over >180° horizontally, previously surveyed by total station; **pass
  if residuals are within the instrument's specified accuracy** (p.7). This is a
  ready-made basis for a Parametrix periodic verification procedure.
- Wi-Fi: SSID is `Trimble MX60 (<serial>)`; the password is on stickers in the Control
  Unit top case, is **unique per system and cannot be changed** (p.37)
- **Mandatory**: set the Wi-Fi access point country on first use and **every time you
  collect in a different country** — TMI menu *System Administration / WiFi / MX60 WiFi
  Access Point* (p.48)
- User interface device: 10"+ display, touch preferred, **Google Chrome** required to run
  the TMI interface; Ethernet set to obtain IP and DNS automatically (pp.36, 48)
- **GAMS eliminates the need for special initialization driving manoeuvres** (p.67) —
  which necessarily implies that **without GAMS, such manoeuvres are required**. The
  manoeuvres themselves are not described in this guide.

---

#### 1.2 Trimble MX60 Spec Sheet

| Field | Value |
|---|---|
| Date / version | **PN 022516-737C (04/25)** — April 2025 |
| Publisher | Trimble Inc. |
| Pages | 4 |
| Appears current | Yes, but **conflicts with the User Guide** — see §4 |

Gives the three configurations side by side, system component dimensions and weights,
environmental and electrical data, camera capture modes (**spherical 10 fps max, down
camera 9 fps max, by distance or by time**), **data storage of 2 × 4 TB removable SSD**,
and one-line descriptions of Trimble Mobile Imaging, the TBC mobile mapping module, and
Trimble MX Publisher.

**Marketing-adjacent but specification-bearing.** Treat the numbers as authoritative only
where they agree with the User Guide; where they differ, see §4.

---

#### 1.3 Trimble MX Shock Absorbing Mounting Rack User Guide, Revision B

| Field | Value |
|---|---|
| Date / version | **May 2025, Revision B**, P/N 37000001 |
| Pages | 10 |
| Appears current | Yes |

**IMPORTANT — this is a different rack from the one in the MX60 User Guide.** The MX60
User Guide describes the **MX SCAN Roof Rack** (18 kg, clamps to square-cut universal roof
bars up to 85 × 30 mm). This document describes the **MX Shock Absorbing Mounting Rack**
(28 kg, bolts to a prepared level mounting platform or aluminium T-slot profiles with
M6/M8 screws, for vehicles "mostly driving in harsher environments than a standard road").

The two racks have different weights, different mounting methods, and different mounting
requirements. Both carry the External Reference Point, but **the GAMS corner offsets
published in the MX60 User Guide (X = +1.006, Y = −0.469, Z = +0.025) are specified for
the standard Roof Rack and cannot be assumed to apply to the shock absorbing rack.**

Parametrix must confirm which rack is on the vehicle before any lever-arm work.

Also notable: this rack is rated for a sensor unit of **up to 37 kg** — well above the
MX60 Premium's 28 kg — so it is shared across the MX product line.

---

#### 1.4 Product Bulletin: Enabling the Dust Filter in TMI for MX60

| Field | Value |
|---|---|
| Date / version | January 2025, PUBLIC |
| Pages | 3 |
| Appears current | Yes |

As assessed in Revision 1, and now better anchored. The bulletin's installation-height
instruction (**strictly vertical, 2–3 cm, to the external reference cross on the right
side of the mounting rack**) is consistent with the User Guide's External Reference Point
(p.45) — the two describe the same physical point, and the User Guide's 1 cm figure is
the tighter requirement.

Contributes: TMI paths (**Mission Presets → Capture settings**), the **laser waterfall
view**, **reconfigure mission**, laser rate selection, and one documented failure mode
(height too high → mask touches ground → data loss).

---

### Tier 2 — Vendor-neutral practice guidance

#### 1.5 Mobile Laser Scanning Technical Guideline — Queensland TMR, March 2023, 65 pp, CC BY 4.0

Unchanged from Revision 1, and still the strongest operational source for **how to run a
project** as opposed to **how to run the machine**. Minimum three passes; boresight before
and after every project; survey vs relative uncertainty in 200 m sliding windows; useful
range statement; point scale factor caution (40 mm/100 m); imagery 8am–4pm and not in wet
conditions; reclassify rather than delete; a complete QA deliverable list; a ready-made
glossary.

Queensland-specific throughout (GDA94/GDA2020, AHD71, MGA, ICSM SP1, `.12daz`, Form 6/PSM),
and **most numeric tolerances are left as per-project variables** in a checklist that is
not in the collection.

#### 1.6 NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data — 2024, 211 pp

Unchanged from Revision 1. Descriptive, not prescriptive. Valuable for data life cycle,
governance, QA expectations, and DOT case examples. No MX60 content. Its accuracy figures
are survey responses about intent, not achievable tolerances. Non-commercial licence terms
flagged at decision item 28.

### Tier 3 — Background

#### 1.7 3D Reconstruction and Mobile Mapping in Urban Environments — MDPI reprint, 2024, 360 pp across 4 PDFs

Unchanged from Revision 1. Verified complete and continuous (printed pp.2–95, 96–171,
172–265, 266–345). Academic research; contributes at most a few citations to Section 25.

#### 1.8 "Mobile Mapping, AI and Digital Data Optimize Road Infrastructure Management" — 2025, 2 pp

Sponsored content. Context only. **Not to be cited as technical authority.**

---

## 2. What is still missing

| Missing document | Named where | Blocks |
|---|---|---|
| **Trimble TMI Software User Guide** | MX60 UG p.48, p.37 | **8, 9, 10, 12, 13**, 14, 22 |
| **Trimble MX60 Quick Start Guide** | MX60 UG p.48 | **8, 10, 13, 23, 28** |
| Trimble DMI Installation & Operation Manual | MX60 UG p.42 | 3, 7, 25 |
| Trimble GAMS Antenna Kit Installation & Operation Manual | MX60 UG p.43 | 7, 10, 25 |
| POSPac MMS documentation | MX60 UG p.47 | 15, 16, 25 |
| TBC mobile mapping module documentation | Spec sheet p.4 | 15, 16, 19, 25 |

**Sources named in the documents themselves:**

- TMI User Guide: `geospatial.trimble.com/en/links?dcs=Collection-129953` (MX60 UG p.48)
- MX60 documentation generally: `geospatial.trimble.com/en/products/hardware/trimble-mx60` (p.51)
- Trimble Land Mobile Download Center at `geospatial.trimble.com` (Rack UG p.10)
- Support: `mx_support@trimble.com`; Americas +1-289-695-4416 (p.51)

---

## 3. Section-by-section feasibility

| Section | Status |
|---|---|
| 1 Purpose and scope | **Ready** — can now state Core/Pro/Premium precisely |
| 2 Mobile mapping in plain language | **Ready** |
| 3 System components | **Ready** — fully sourced |
| 4 Workflow at a glance | **Partial** — field sequence depends on Quick Start Guide |
| 5 Pre-field planning | **Ready** |
| 6 Equipment preparation | **Ready** — Trimble checklist p.44 |
| 7 Vehicle installation and setup | **Ready** — richest new material |
| 8 Starting the MX60 | **Blocked** — power-on is known; everything after is in TMI |
| 9 TMI field interface | **Blocked** — four UI elements known |
| 10 Initialization | **Blocked** — we know GAMS removes the manoeuvres, not what they are |
| 11 Collecting data | **Partial** — speeds and limits ready; TMI operation is not |
| 12 What to watch while driving | **Blocked** — LEDs and waterfall only |
| 13 Ending a collection | **Blocked** |
| 14 Data handling | **Partial** — media, docking station, and the USB/disk rule are ready |
| 15 TBC workflow | **Blocked** |
| 16 Understanding trajectory | **Ready** — positioning performance table is a strong anchor |
| 17 Point cloud quality | **Ready** — range/rate/reflectivity trade-offs now documented |
| 18 Imagery quality | **Ready** |
| 19 Control and mobile mapping | **Ready** |
| 20 Quality control | **Ready** — including Trimble's own target-check method (p.7) |
| 21 When mobile mapping does not work well | **Ready** |
| 22 Troubleshooting | **Partial** — LEDs, breakers, Battery Protect, dust filter now sourced |
| 23 Field checklist | **Partial** — pre/post-mission ready; in-mission blocked |
| 24 First day training exercise | **Partial** |
| 25 Advanced | **Partial** — lever arms, GAMS, POSPac frame offset ready; boresight is not |
| 26 Lessons learned | **Ready** |
| 27 Glossary | **Ready** — MX60 UG p.58 plus TMR §2 |
| 28 Appendices | **Partial** |

**Roughly 16 of 28 sections can now be written to a high standard**, against 11 in
Revision 1, and the newly-ready ones include the three heaviest reference chapters.

---

## 4. Contradictions and unclear points

### 4.1 Laser rate and scan speed differ by exactly 2× between the spec sheet and the User Guide — **significant**

| Parameter | User Guide p.54 | Spec Sheet p.2 |
|---|---|---|
| Rate | Laser Pulse Repetition Rate **500 kHz / 1000 kHz** | Effective measurement rate **1000 kHz / 2000 kHz selectable** |
| Scan speed | **120 Hz / 200 Hz** selectable (profiles per second) | **240 / 400** selectable |
| Max range | 150 m / 120 m | 150 m @ 1000 kHz, 120 m @ 2000 kHz |

Both pairs differ by exactly a factor of two, and the ranges line up. The consistent
explanation is that **the MX60 has two scanners**: the User Guide quotes **per-scanner**
figures (PRR, profiles per second) and the spec sheet quotes **system-total** figures
("effective measurement rate"). Under that reading the two documents describe the same
hardware in different units.

**The operational problem is the dust filter bulletin.** It says to use *"1000 kHz
**effective measurement rate** instead of 500 kHz"* — spec-sheet terminology with
User-Guide numbers. An operator who reads the bulletin, then looks at a TMI dropdown
labelled in system-total units, would select **1000 kHz — the lower setting — and get the
opposite of what the bulletin intends**.

**Until TMI's actual labelling is confirmed, the SOP should instruct by intent rather than
by number: in dusty conditions select the higher of the two available measurement rates,
accepting the reduced maximum range.** This needs verification against TMI and is worth a
question to Trimble support.

### 4.2 Field of view

Spec sheet p.2 states "Full 360°". User Guide p.54 states each scanner provides a beam
deflection of **~346°**. The system may achieve effectively full coverage from two
overlapping 346° scanners, but the spec sheet's figure is the rounder claim. Use 346° per
scanner when discussing occlusion geometry.

### 4.3 Range specification conditions differ

The User Guide (p.55) qualifies maximum range as flat targets larger than the beam
diameter, perpendicular incidence, **23 km atmospheric visibility**, and notes range is
shorter in bright sunlight than under overcast. The spec sheet (p.4) says only "matte
surface with normal angle of incidence" and ">80% target reflectivity". **The User Guide's
conditions are the ones to quote** — they are the ones an operator can actually reason
about.

### 4.4 Minor numeric disagreements

| Item | User Guide | Spec Sheet |
|---|---|---|
| Control Unit weight | 13 kg (p.52) | 12.4 kg / 10.2 kg without cover (p.3) |
| Core spherical focal length | 4.40 mm (p.53) | 4.44 mm (p.2) |
| Down camera horizontal FOV | 82.9° (p.54) | 82.0° (p.2) |

Immaterial operationally. **Prefer the User Guide** as the controlled, revision-tracked
document.

### 4.5 Two different mounting racks

Covered at §1.3. The SOP must not present rack instructions generically. Confirm which
rack Parametrix owns; the GAMS corner offsets are rack-specific.

### 4.6 Resolved since Revision 1

- **Laser rate trade-off** — now documented: the higher rate costs maximum range
  (150 m → 120 m). Revision 1 listed this as unexplained.
- **Installation height reference point** — the bulletin's "external reference cross" and
  the User Guide's "External Reference Point" are the same feature. The User Guide's 1 cm
  tolerance supersedes the bulletin's 2–3 cm.

### 4.7 Carried forward from Revision 1, still open

- Dust filter on paved roads: consequence of misuse unstated
- Installation height entered too **low**: consequence unstated
- Mid-mission reconfiguration: mechanism unexplained
- TMR's rule that simultaneous multi-scanner passes are not independent — directly
  relevant to a two-scanner MX60, and unaddressed by any Trimble document
- Boresight calibration: TMR requires it before and after every project; **no Trimble
  boresight procedure exists in the collection**
- NCHRP accuracy percentages are aspirations, not tolerances

---

## 5. PARAMETRIX DECISION REQUIRED

Items 1–28 from Revision 1 stand. The new sources add these:

| # | Decision | Section |
|---|---|---|
| 29 | **Which MX60 configuration** does Parametrix own — Core, Pro, or Premium? This changes camera resolution and positioning performance, and the SOP's accuracy statements depend on it | 1, 3, 16 |
| 30 | **Which mounting rack** — MX SCAN Roof Rack or MX Shock Absorbing Mounting Rack? Determines install procedure and GAMS offsets | 7 |
| 31 | **Are GAMS and DMI owned and fitted?** GAMS removes initialization manoeuvres; DMI provides ZUPT for GNSS-challenged work. Both change the field procedure materially | 3, 7, 10, 11 |
| 32 | **Standard collection speed policy.** Trimble recommends 80 km/h max operating, 110 km/h absolute. Parametrix should set a normal working speed and the conditions for reducing it | 11 |
| 33 | **Two-person crew requirement.** Trimble states the driver may not operate the system. Is a two-person crew mandatory for all MX60 work? | 4, 11 |
| 34 | **Dedicated vehicle specification** — hatchback, upright rear door, ≥1.60 m roof, non-bright colour, start/stop disabled, ≥60 Ah, professional electrical install | 7 |
| 35 | **Lever-arm measurement procedure and record.** Who measures, to what method, recorded where, re-verified when? Trimble requires ~1 cm and warns of faulty navigation solutions | 7, 25 |
| 36 | **Vehicle Preset management in TMI** — naming, who may create or edit, and how the correct preset is confirmed before each mission | 7, 8 |
| 37 | **Periodic data-quality verification.** Adopt Trimble's retro-reflective target check (UG p.7) as a scheduled Parametrix procedure? At what interval? | 20 |
| 38 | **Wet weather stand-down.** Trimble says avoid operating in rain or mist; TMR says do not capture imagery in wet conditions. Parametrix needs one clear rule | 5, 11, 18 |
| 39 | **Hot weather / stationary operation limits**, given the temperature footnote excluding direct sun below 10 km/h | 11, 12 |
| 40 | **SSD handling and rotation** — 2 × 4 TB removable; who removes, how transported, how many sets in circulation | 14 |
| 41 | **Air freight acclimatisation rule** — 24 hours before power-on after air transport | 6 |
| 42 | **Torque verification sign-off** — Trimble requires a second person to check torque values | 7 |
| 43 | **Wi-Fi country setting** — mandatory on first use and per country; add to mobilisation checklist for any out-of-country work | 8 |
| 44 | **Laser rate selection standard**, pending resolution of the labelling ambiguity at §4.1 | 11, 17 |

---

## 6. Recommendation

**Drafting can now begin productively**, and I recommend starting rather than waiting.

Proposed order, front-loading what is fully sourced and following your Layer philosophy:

1. Section 1 — Purpose and Scope
2. Section 2 — Mobile Mapping in Plain Language
3. Section 3 — System Components
4. Section 6 — Equipment Preparation
5. Section 7 — Vehicle Installation and System Setup

That is five substantial, well-sourced sections covering everything from "what is this?"
through "the system is mounted, measured, and ready to switch on."

**Sections 8–13 should be held** until the TMI User Guide and Quick Start Guide arrive.
Writing them now would mean inventing a startup sequence, an initialization manoeuvre, and
a shutdown procedure — precisely the material where a plausible-sounding guess is most
dangerous, because an operator would follow it.

Both documents are obtainable: the TMI guide from
`geospatial.trimble.com/en/links?dcs=Collection-129953`, and both via the Trimble Land
Mobile Download Center or `mx_support@trimble.com`.
