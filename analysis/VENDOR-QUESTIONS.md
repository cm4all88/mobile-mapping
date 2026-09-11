# Questions for the Trimble vendor / dealer

Every open item in the MX60 SOP that a vendor conversation could close. Ordered by how
much each unblocks.

Contact: `mx_support@trimble.com` · Americas +1-289-695-4416
*(MX60 UG Rev B, p.51)*

---

## 1. Boresight calibration — ANSWERED, see note

> **Resolved 2026-09-11.** The procedure is documented at
> <https://help.fieldsystems.trimble.com/tbc/20716.htm> and written up in SOP §12.3.
> It is office work in TBC, not a shop job. Two questions remain, both narrower:
>
> - **Which TBC version does Parametrix run?** After 5.21 calibrates in TBC; 5.21 and
>   earlier require calibrating outside TBC and importing a JSON.
> - **Does daily removal of the Sensor Unit count as "disturbed"** for the purposes of
>   recalibration frequency?

### Original question, retained for context

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

## 2. Current TBC documentation for the MX60 — LARGELY ANSWERED

> **Resolved 2026-09-11.** The TBC help portal at
> <https://help.fieldsystems.trimble.com/tbc/> documents the mobile mapping workflow in
> full, and 31 of its topics have now been captured and classified (see
> `SOURCE-INVENTORY-TBC-BATCH-2.md` through `-BATCH-4.md`). Import, scan generation,
> registration, calibration, trajectory processing and cleanup are all covered.
>
> **One topic still matters and has not been captured: Export Mobile Mapping Data.** It is
> the only place that can answer whether an export carries the identity of the trajectory
> the scans were built on.
>
> The help portal carries **no version number and no date**, which is why question 2b below
> exists.

### Original question, retained for context

> **Is there TBC mobile mapping documentation that covers the MX60?**

The only TBC document we have is *Technical Notes: For Mobile Mapping*, **October 2022**.
It lists raw import from "MX7, MX50, or MX9" — **the MX60 is not mentioned**, because
MX60 support did not reach TMI until **December 2024** *(TMI UG Rev L, p.2)*.

We need step-by-step procedure for: importing the `mxdb`, trajectory processing,
registration to control, colorization, classification, and export.

**Blocks:** SOP §12 entirely

---

## 2a. POSPac MMS licence — added 2026-09-11

> **Do we hold a POSPac MMS 8.6 or later licence, and is it installed on the processing
> workstation alongside TBC?**

This turns out to gate more than expected. TBC's **Process Raw Trajectory Data** command
computes the SBET inside TBC, but *"the requirement to run the feature is to have the
Applanix's POSPac MMS application (from version 8.6 and a valid license) installed alongside
TBC"* *(TBC Help 25943)*. **Generate POSPac Position Fixes** — the documented remedy for
corridors with no usable GNSS — also requires POSPac, and a second processing pass in it
*(TBC Help 24460)*.

Without the licence, neither is available, and trajectory production has to happen wherever
POSPac lives.

**Blocks:** the whole shape of the office workflow

---

## 2b. TBC version — added 2026-09-11

> **Which TBC version is installed?**

Already asked under item 1 for the calibration behaviour at 5.21. Two more version
boundaries have since appeared:

- **5.21** — after it, laser scanners *and* cameras calibrate in TBC; at or before it, both
  calibrate externally and import as JSON *(TBC Help 24886, 24868)*
- **5.80** — projects saved before it may carry a registration with no RMS file set, and TBC
  prompts for one *(TBC Help 27248)*

**Blocks:** SOP §12.3 and the registration QC procedure

---

## 2c. LiDAR QC capability — added 2026-09-11

> **Is LiDAR QC processing something we intend to be able to do?**

It is the only documented way to improve a trajectory in poor-GNSS corridors *without*
placing additional ground control, and it needs a workstation well beyond a normal one:
**128 GB RAM minimum, 256 GB recommended**, a dedicated 1–2 TB SSD for TEMP on the PCI bus,
a further 1–2 TB for virtual memory, a paging file at 6× installed RAM, and the **MATLAB
Runtime R2024b** installed after TBC *(TBC Help 28972)*.

Worth confirming with the vendor whether Trimble considers this optional or expected for
survey-grade MX60 work, and whether the requirements differ for the MX60's two-scanner
configuration.

**Relates to:** a capability decision, not a software setting

---

## 2d. Export provenance — added 2026-09-11

Three narrow, answerable questions. All five MX60 export paths and Publish to TRCPS have been
read; none of the help topics answers these, and no further documentation will.

> **1. Does any TBC export write the source trajectory into a LAS header, a VLR, or a sidecar
> file?**

Trimble's help topics describe dialogs, options and output folder structures. They do not
enumerate LAS header fields. Something may be written that the documentation does not mention.

> **2. When a run carries both an imported `Sbet` and a registered trajectory, which one does
> the TMX export write, and which one does Publish to TRCPS send?**

Both paths carry a trajectory — the TMX export writes "the trajectory file… once for all
devices" *(TBC 22501)*, and Publish to TRCPS states that "mobile mapping point cloud and
trajectories will be automatically exported" by default *(TBC 29527)*. **Neither says which.**

> **3. Which report contains the signed GCP residuals added in TBC 2025.21?**

The 2025.21 release note says the Easting, Northing and Elevation residuals "are now signed and
included in the report." The only mobile mapping report topic — *Run a Mission Report*
*(TBC 23991_1)* — does not mention residuals at all.

**Blocks:** delivery provenance, and the records-at-delivery decision

---

## 2e. Export timestamps — added 2026-09-11, and this one is urgent

> **When "Export timestamps" is set to Yes and TBC reprocesses the scans from the raw data,
> which trajectory does it use?**

Trimble states, identically in two export topics *(TBC 23339, 22501)*:

> "If the TIMESTAMP option has been set to No, the exported scans are the ones processed with
> the Generate Scans feature… If the TIMESTAMP option has been set to Yes, the exported scans
> are **reprocessed from the raw data** and directly written to the LAS format files."

Every quality step — registration, Update Scans, filtering, colorization — acts on the
generated scans. If the reprocessing does not pick up the registered trajectory, then **turning
this option on silently delivers unregistered data after the registration has been checked and
signed off.**

Both readings are consistent with Trimble's wording. This is a direct yes/no question and it
is the single most consequential unknown in the workflow.

**Blocks:** the export procedure, and any QC sign-off that precedes export

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
