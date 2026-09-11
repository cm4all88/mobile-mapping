# Questions for the Trimble vendor / dealer

Every open item in the MX60 SOP that a vendor conversation could close. Ordered by how
much each unblocks.

Contact: `mx_support@trimble.com` · Americas +1-289-695-4416
*(MX60 UG Rev B, p.51)*

---

## 1. Boresight calibration — the actual blocker

> **Does the MX60 require user boresight calibration? If so, what is the procedure?**

**Why we're asking.** TMI has a **Calibration Import** function that takes a boresight
JSON via USB1 *(TMI UG Rev L, p.18)*. But the description of how that JSON is *produced*
appears in TMI's **Sensor Settings** section, which is marked **MX90/MX9 only**
*(p.20)*. The MX60 has no user-adjustable sensor orientation in TMI, and the Quick Start
Guide says MX60 lever arms are *"set by default in the MX60 system"* (p.7).

That reads like the MX60 is factory-calibrated — but nothing states it.

**Follow-ups if the answer is "yes, it's a user task":**
- What does a calibration mission look like — route, duration, manoeuvres, targets?
- Which software computes it — TBC, POSPac, or a Trimble service?
- Recommended frequency, and what triggers an unscheduled calibration?
- Does removing and re-mounting the Sensor Unit daily count as "disturbing" it?

**Follow-up if the answer is "it's factory-set":**
- What is the recommended interval for returning the unit for factory recalibration?
- What symptoms indicate calibration has drifted?

**Blocks:** SOP §12.3 · Decision register item 20

---

## 2. Current TBC documentation for the MX60

> **Is there TBC mobile mapping documentation that covers the MX60?**

The only TBC document we have is *Technical Notes: For Mobile Mapping*, **October 2022**.
It lists raw import from "MX7, MX50, or MX9" — **the MX60 is not mentioned**, because
MX60 support did not reach TMI until **December 2024** *(TMI UG Rev L, p.2)*.

We need step-by-step procedure for: importing the `mxdb`, trajectory processing,
registration to control, colorization, classification, and export.

**Blocks:** SOP §12 entirely

---

## 3. Periodic data-quality verification

> **Is the retro-reflective target check the recommended periodic verification for the
> MX60, and at what interval?**

The User Guide recommends scanning ~8 flat retro-reflecting targets at varied distances
over >180° horizontally, previously surveyed by total station, passing if residuals fall
within specified accuracy *(MX60 UG Rev B, p.7)*. It says to do this "regularly" and
"especially before starting an extensive data acquisition campaign" — but gives no
interval.

- Is this the right check for an MX60 specifically?
- Recommended interval?
- Any Trimble-specified target type or geometry?

**Relates to:** Decision register item 33

---

## 4. Two documented specification discrepancies

Worth confirming so the SOP quotes the right numbers.

**a. Laser setting presentation.** The Quick Start Guide (March 2025) describes two
separate MX60 controls — *Measurement Prog* `[500 kHz, 1000 kHz]` and *Line Speed*
`[120 Hz, 200 Hz]` (p.10). The TMI User Guide Rev L (April 2026) describes a single
combined **Laser Mode** for the MX60 (p.29).

> Which is current for the TMI version shipping now?

**b. Field of view.** The User Guide states each scanner provides ~**346°** beam
deflection (p.54). The spec sheet states **Full 360°** (p.2).

> Which figure should be used when reasoning about occlusion geometry?

Also worth noting: Trimble states the measurements/second values shown in the TMI
interface are **rounded** *(TMI UG Rev L, pp.28–29)*.

**Relates to:** `CONFLICT-002`, `CONFLICT-005` in the reference dataset

---

## 5. Accessory manuals — only if fitted

If GAMS and/or DMI are on the vehicle:

- **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)*
- **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)*

Both are needed to complete the lever-arm procedure in SOP §6. Note the MX60 User Guide
requires millimetre-level GAMS offsets and a **≥2.0 m baseline** if the navigation data
will be post-processed (p.68) — worth confirming that applies to our setup.

---

## 6. Configuration confirmation

> **Which configuration is our system — Core, Pro, or Premium?**

The vendor can confirm from the serial number. This determines imagery resolution and
attitude accuracy, and therefore every accuracy statement in the SOP.

Also confirm:
- Which mounting rack we have — **MX SCAN Roof Rack** (18 kg) or **MX Shock Absorbing
  Mounting Rack** (28 kg). The GAMS corner offsets published in the User Guide apply to
  the standard rack **only** *(p.68)*
- Are GAMS and DMI included?

**Relates to:** Decision register items 1, 2, 3

---

## 7. Worth asking while you have their attention

- **Current TMI version** on our system, and how firmware updates are distributed
- Whether there is an **MX60-specific** training course, and what it covers
- Whether Trimble publishes **recommended collection speeds** by deliverable type — the
  documentation gives only 80 km/h recommended / 110 km/h maximum
- Whether the **Lateral Range Limit** (5–50 m, TMI Rev L p.29) has any documented effect
  on accuracy, or is purely a data-volume tool

---

*Prepared from the MX60 documentation set. Full source assessment in
`STAGE-1-SOURCE-ANALYSIS.md`; all open Parametrix decisions in
`../SOP/appendix-D-decision-register.md`.*
