# 7. Field Preparation and Preflight

## 7.1 How often each task happens

| Task | Frequency |
|---|---|
| Power supply installation, Control Unit and Power Unit mounting | **Once per vehicle** |
| Roof bars, rack, lever arm measurement, Vehicle Preset | **Once per vehicle**, and after any change to the fitting |
| Sensor Unit mounting and cabling | **Every deployment** |
| Preflight checks | **Every mission** |

> **CAUTION**
>
> The one-time tasks are one-time **for a given installation**. Changing the rack, the roof bars,
> the vehicle, or the Sensor Unit's position on the rack **invalidates the lever arms and may
> invalidate the calibration** (§14.7). Treat any change to the fitting as a return to §7.2.

## 7.2 One-time installation

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> This subsection carries figures from the MX60 User Guide and the Roof Rack User Guide. The
> **figures are sourced**; the procedural framing around them is v1 draft material and should be
> confirmed against the installation as actually performed on the Parametrix vehicle.

### Power

| Parameter | Value | Source |
|---|---|---|
| Input voltage | 12–16 V DC | *(MX60 UG Rev B)* |
| Current at startup | **25 A at 12.8 V** (320 W) | *(MX60 UG Rev B)* |
| Current in operation | 12 A (160 W) | *(MX60 UG Rev B)* |
| **Supply rating needed** | **30 A or more** | *(MX60 QSG Rev B, p.4)* |
| Direct-connection fuse | 35 A, close to the battery | *(MX60 UG Rev B)* |

> **CAUTION**
>
> **An auxiliary battery as a backup power source is recommended** *(MX60 QSG Rev B, p.4)*. A
> supply interruption mid-mission does not merely stop collection — it ends the run, and with it
> the continuity the reverse-processing pass depends on (§8.7).

### Cabling and mounting

The Sensor Unit cable is **5 m**; the Control Unit run is about **3 m**. Route and secure cables
so they cannot chafe, catch, or be closed in a door. The Control Unit and Power Unit are **IP30 —
not waterproof** and live inside the vehicle *(MX60 UG Rev B, p.53)*.

### Roof bars, rack, and screw tightening

> **IMPORTANT**
>
> Follow the tightening method and sequence in the **MX Shock Absorbing Mounting Rack User Guide**
> or the **MX SCAN Roof Rack** documentation, as applicable. **Which rack is fitted is an open
> question** (§4.1) and matters: the published GAMS corner offsets apply to the standard rack
> **only** *(MX60 UG Rev B, p.68)*.

## 7.3 Lever arms and the Vehicle Preset

Lever arms are the fixed distance offsets between sensors. **They are measured, not estimated**
(§14.2) — TBC's calibration solves angles only.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> The vehicle frame convention *(TBC 25943, 24886)*:
>
> - **Positive X = forward driving direction**
> - **Positive Y = right side of the vehicle**
> - **Positive Z = downward**

> **WHY THIS MATTERS — Z is down**
>
> This trips people every time. A sensor mounted **above** the reference point has a **negative Z**
> in this convention. Getting the sign wrong puts twice the offset into the solution, in the wrong
> direction, and it will not look like a sign error downstream — it will look like a height
> problem.

### GAMS lever arm — only if fitted

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Where navigation data will be **post-processed** — which is all survey-grade work — the MX60
> User Guide requires GAMS offsets to **a few millimetres** and a baseline of **≥ 2.0 m**
> *(MX60 UG Rev B, p.68)*.

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* is
> not held. It is needed to complete this procedure if GAMS is fitted. *(Appendix I)*

### DMI lever arm — only if fitted

Measured in the vehicle frame from the reference point to **the centre of the tread where the
DMI-equipped wheel contacts the road** *(TBC 25943)*.

> **CAUTION**
>
> **The DMI scale factor carries a sign that depends on which side it is mounted:** positive on
> the **left**, negative on the **right** *(TBC 25943)*. It is entered in the office (§12.3) but
> determined by the installation, so **record which side it is on at installation** — the
> processor will not be able to see the vehicle.

> **VENDOR CLARIFICATION REQUIRED · V-6**
>
> The **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)* is not held. It
> contains the scale-factor value for the measured wheel diameter, which §12.3 needs.
> *(Appendix I)*

> **PARAMETRIX DECISION REQUIRED · D-46**
>
> **Where are the lever arms, the Vehicle Preset, and the installation configuration recorded, and
> who verifies them?** These values are entered once and used on every mission thereafter. An
> error in them is systematic, invisible, and persists until someone re-measures.

## 7.4 Mounting the Sensor Unit

> **CAUTION**
>
> **Two people are required.** The Sensor Unit weighs **24–28 kg** depending on configuration
> *(MX60 UG Rev B)*. It is awkward, it is expensive, and it is mounted above head height.

Mount, secure, connect, and confirm the unit is seated as it was when the lever arms were
measured. Any doubt about seating is a doubt about the lever arms.

## 7.5 Power-up

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** — sourced to
> *(MX60 UG Rev B; MX60 QSG Rev B)*

1. Vehicle ignition on
2. Confirm the power supply is live
3. Press and hold the **Control Unit** power button for **at least 15 seconds**
4. Sensor Unit and Control Unit LEDs **blink for about 10 seconds**
5. Wait for the system to reach a ready state before connecting to TMI

> **CAUTION**
>
> **Battery Protect** gives an audible warning below **10.5 V** and cuts power **90 seconds**
> later *(MX60 UG Rev B)*. If the alarm sounds during preflight, restore charge before doing
> anything else — a mission that starts on a marginal battery will end unexpectedly.

## 7.6 Connecting to TMI

TMI is served by the Control Unit and runs in **Chrome**:

| | |
|---|---|
| Capture | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |

*(TMI UG Rev L)*

Status reference — the colour meanings, warnings and indicators — is **Appendix B**.

## 7.7 Mission configuration in TMI

### Capture settings

> **VENDOR CLARIFICATION REQUIRED · V-2 · unresolved presentation conflict**
>
> The **Quick Start Guide** describes two separate MX60 controls — *Measurement Prog*
> `[500 kHz, 1000 kHz]` and *Line Speed* `[120 Hz, 200 Hz]` *(MX60 QSG Rev B, p.10)*.
>
> The **TMI User Guide Rev L** describes a single combined **Laser Mode** for the MX60
> *(TMI UG Rev L, p.29)*.
>
> **Which is current depends on the TMI version installed.** The operator should expect either and
> should record which was used. *(`CONFLICT-005`; Appendix I)*

> **Note also:** Trimble states the measurements-per-second values shown in the TMI interface are
> **rounded** *(TMI UG Rev L, pp.28–29)*.

### The dust filter

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A dust filter is available for the MX60 and is intended for **unpaved roads and mine sites**
> *(Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025)*.

### Lateral Range Limit

Settable 5–50 m *(TMI UG Rev L, p.29)*.

> **VENDOR CLARIFICATION REQUIRED · V-7**
>
> **Does the Lateral Range Limit have any documented effect on accuracy, or is it purely a
> data-volume tool?** *(Appendix I)*

## 7.8 Disk check

Confirm the exchangeable data disk is installed, has sufficient free space for the planned
mission, and is the intended disk.

> **CAUTION**
>
> **Never connect the USB cable while the exchangeable data disk is inside the Control Unit.**
> Remove the disk first *(MX60 UG Rev B, p.10)*.

> **PARAMETRIX DECISION REQUIRED · D-47**
>
> **What free-space margin is required before a mission is permitted to start?** A mission that
> fills the disk mid-corridor ends the run and takes the closing sequence with it (§8.7).

## 7.9 Preflight check

Full version in **Appendix C**.

| ☐ | Item |
|---|---|
| ☐ | Sensor Unit mounted, secured, seated as when lever arms were measured |
| ☐ | All cables connected, routed and secured |
| ☐ | Power supply live; battery healthy; no Battery Protect warning |
| ☐ | System powered up; LEDs through their startup sequence |
| ☐ | TMI reachable in Chrome; all sensors reporting present |
| ☐ | Vehicle Preset / lever arms correct for **this** vehicle and installation |
| ☐ | Capture settings configured and **recorded** |
| ☐ | Data disk installed, correct, with sufficient free space |
| ☐ | **Calibration currency confirmed** (§14.7) |
| ☐ | Optics clean — scanner windows and camera dome |
| ☐ | Initialization location confirmed available (§6.3) |
| ☐ | Weather within the go/no-go rule (§6.5) |
| ☐ | Field record started |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We got the vehicle ready: the sensor head mounted and secured, the offsets
> between sensors measured and entered, power confirmed, the software reachable, the disk in, and
> the optics clean.
>
> **Why it matters.** The lever arms are the part that deserves respect. They are measured once
> and then used on every mission for months. An error in them is systematic — it does not average
> out, it does not look like noise, and nothing downstream will point at it. The office will see a
> height that is slightly wrong everywhere and will probably blame the geoid.
>
> **What can go wrong.** The classic is the sign on Z. The convention has **Z positive downward**,
> so a sensor above the reference point takes a negative value. Get it backwards and you have put
> twice the offset in, the wrong way, into every mission from now until somebody re-measures.
>
> The other is treating a re-fit as routine. If the rack changed, the bars moved, the head was
> re-seated differently, or the unit went on a different vehicle, the lever arms are no longer
> the ones in the software — and the calibration may not be either.
>
> **What good looks like.** Two people on the head. Cables that cannot chafe or get shut in a
> door. A battery that is not marginal. Lever arms that were measured by somebody who knew Z was
> down, written down, and verified by somebody else. Clean optics. Enough disk for the whole
> mission with margin. And a note of exactly which capture settings were used, because in three
> weeks nobody will remember.
