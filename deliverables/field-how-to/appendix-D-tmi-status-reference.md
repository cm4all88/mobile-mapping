# Appendix D — TMI Status and Warning Reference

> **VENDOR CLARIFICATION REQUIRED · V-2**
>
> **The TMI version installed on the Parametrix system has not been confirmed**, and TMI's
> interface has changed between versions. This appendix is sourced to **TMI User Guide Rev L** and
> **MX60 Quick Start Guide Rev B**. **Verify against the system before issue.**

## D1 · Reaching TMI

| | |
|---|---|
| Browser | **Chrome** |
| Capture | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |
| Modules | TMI.Capture · TMI.AI |

*(TMI UG Rev L)*

Served by the Control Unit. No internet access required; the addresses resolve only on the Control
Unit's network.

## D2 · Status colours

| Colour | Meaning |
|---|---|
| **Green** | The parameter meets its accuracy threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Red** | Not meeting threshold |

> **CAUTION**
>
> **Orange permits recording. Survey-grade work does not.** Until **D-3 / D-49** is decided, treat
> orange as a stop-and-assess condition and record it.

> **Green means the solution met its accuracy figures — not that it has finished converging.**
> Trimble asks for **up to ten more minutes** of settling before recording data that matters
> *(MX60 QSG Rev B)*.

## D3 · When the navigation status will not reach its ready state

| Holding parameter | Likely cause | Action |
|---|---|---|
| **Heading** | Insufficient dynamic manoeuvres, or GAMS unavailable | **More turns and speed changes.** Heading is the hardest component to resolve |
| **Position** | Poor sky view | **Move to a genuinely open location** |
| **Attitude** | Insufficient motion variety | Complete the full manoeuvre profile |

> **Ask TMI which parameter is holding the solution rather than waiting.** Heading means drive
> more; position means move the vehicle. **Waiting helps neither.**

## D4 · Alarms and protective behaviour

| Indication | Meaning | Response |
|---|---|---|
| **Audible alarm** | **Battery Protect** — supply below **10.5 V for more than 12 s** | Power cuts at **90 s**, leaving roughly **78 s**. Recovery needs the voltage above **12.0 V** within that window. **Restore charge immediately; do not continue** *(MX60 UG Rev B, p.27)* |
| **Sensor absent from the device list** | Cable, power or sensor fault | **Stop.** A run with a sensor down is incomplete (§24) |
| **Storage warning** | Disk filling | Reassess before it fills mid-run — an interrupted run loses the closing sequence (§21) |

## D5 · Capture settings

> **Two presentations exist, depending on the TMI version** *(`CONFLICT-005`, **V-2**)*:
>
> | Source | Presentation |
> |---|---|
> | MX60 QSG Rev B, p.10 | **Measurement Prog** `[500 kHz, 1000 kHz]` and **Line Speed** `[120 Hz, 200 Hz]` |
> | TMI UG Rev L, p.29 | A single combined **Laser Mode** |
>
> **Expect either. Record which you saw.**

- The measurements-per-second values shown in the interface are **rounded** *(TMI UG Rev L,
  pp.28–29)*
- **Lateral Range Limit** is settable **5–50 m** *(TMI UG Rev L, p.29)*. Whether it affects accuracy
  or is purely a data-volume control is **V-7**
- A **dust filter** is available, intended for **unpaved roads and mine sites** *(Product Bulletin,
  January 2025)*

> **A resolved conflict, recorded so it is not re-opened.** The specification sheet quotes
> **1000 / 2000 kHz** and **240 / 400 Hz** where the User Guide quotes **500 / 1000 kHz** and
> **120 / 200 Hz** — a factor of exactly two, being system totals against per-scanner figures. **TMI
> uses the per-scanner numbering.** `RESOLVED-001`.

## D6 · Comments

Recorded during collection, against the moment. §19.

## D7 · Calibration import

TMI accepts a boresight calibration JSON via **USB1** *(TMI UG Rev L, p.18)*. Relevant where a
calibration is computed in the office and applied to the system rather than to a project.

## D8 · Administration

| | |
|---|---|
| Firmware update | Copy the `.tmx.install` file to a USB stick, connect to **USB1**, **Refresh** then **Install**. The system shuts down; wait until all Control Unit LEDs are off, then power back on. **Powering on may take up to six minutes** *(TMI UG Rev L, p.49)* |
| Licence update | Copy the licence file to a USB stick, connect to USB1, **Import** *(TMI UG Rev L, p.53)* |
| **Remote access** | **When remote control is given to Trimble Support, all data on the system is visible to them.** Remove confidential data before granting it *(TMI UG Rev L, p.54)* |
| Wi-Fi country | Must be set on first use **and every time you collect in a different country** *(MX60 UG Rev B, p.48)* |
| Wi-Fi limitation | Cannot connect to a hotspot that requires logging in on a web page *(TMI UG Rev L, p.51)* |

---

> **This appendix is a reference for the indications, not a substitute for the procedure.** The
> procedure is §8 to §22.
