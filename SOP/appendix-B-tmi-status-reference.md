# Appendix B — TMI Status and Warning Reference

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> This appendix is carried forward from the v1 draft and is sourced to the **TMI Software User
> Guide Rev L** and the **MX60 Quick Start Guide Rev B**. **The TMI version installed on the
> Parametrix system has not been confirmed** *(V-2)*, and TMI's interface has changed between
> versions. Verify against the system before issue.

## B1 · Reaching TMI

| | |
|---|---|
| Browser | **Chrome** |
| Capture interface | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |
| Modules | TMI.Capture · TMI.AI |

*(TMI UG Rev L)*

TMI is served by the Control Unit. It requires no internet access, and the addresses resolve only
on the Control Unit's network.

## B2 · Status colours

Learn these before driving. The operator's only view of system health is this interface.

| Colour | Meaning |
|---|---|
| **Green** | The parameter meets its accuracy threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Red** | Not meeting threshold |

> **CAUTION**
>
> **Orange permits recording. Survey-grade work does not.**
>
> TMI will let a mission be recorded on an orange navigation status. Whether Parametrix work may
> be collected on anything other than green is **D-3 / D-49** — an operator decision rule that has
> not been made. Until it is, treat orange as a stop-and-assess condition and record it.

> **Green means the solution met its accuracy figures — not that it has finished converging**
> (§8.3). Trimble asks for **up to ten more minutes** of settling before recording data that
> matters *(MX60 QSG Rev B)*.

## B3 · The navigation status

What to do when it will not reach its ready state:

| Holding parameter | Likely cause | Action |
|---|---|---|
| **Heading** | Insufficient dynamic manoeuvres, or GAMS unavailable | More turns and speed changes. Heading is the hardest component to resolve (§8.3) |
| **Position** | Poor sky view | Move to a genuinely open location |
| **Attitude** | Insufficient motion variety | Complete the full manoeuvre profile |

> **FIELD TIP**
>
> Ask TMI **which** parameter is holding the solution rather than waiting. Heading means drive
> more; position means move the vehicle. The two remedies are different and waiting helps neither.

## B4 · Alarms and protective behaviour

| Indication | Meaning | Response |
|---|---|---|
| **Audible alarm** | **Battery Protect** — supply below **10.5 V** | Power is cut in **78–90 seconds**. Restore charge immediately; do not continue *(MX60 UG Rev B)* |
| Sensor absent from the device list | Cable, power or sensor fault | Stop. A run with a sensor down is incomplete (§9.4) |
| Storage warning | Disk filling | Reassess before it fills mid-run — an interrupted run loses the closing sequence (§8.7) |

## B5 · Capture settings

> **VENDOR CLARIFICATION REQUIRED · V-2 · unresolved presentation conflict**
>
> | Source | Presentation |
> |---|---|
> | **MX60 Quick Start Guide Rev B, p.10** | Two controls — *Measurement Prog* `[500 kHz, 1000 kHz]` and *Line Speed* `[120 Hz, 200 Hz]` |
> | **TMI User Guide Rev L, p.29** | A single combined **Laser Mode** for the MX60 |
>
> **Which the operator sees depends on the TMI version installed.** Expect either; record which
> was used. *(`CONFLICT-005`)*

Also:

- Trimble states the **measurements-per-second values shown in the interface are rounded**
  *(TMI UG Rev L, pp.28–29)*
- **Lateral Range Limit** is settable **5–50 m** *(TMI UG Rev L, p.29)*. Whether it affects
  accuracy or is purely a data-volume control is **V-7**
- A **dust filter** is available and is intended for **unpaved roads and mine sites**
  *(Product Bulletin, January 2025)*

### Resolved specification conflict, recorded for reference

> The spec sheet quotes **1000 / 2000 kHz** and **240 / 400 Hz** where the User Guide quotes
> **500 / 1000 kHz** and **120 / 200 Hz** — a factor of exactly two, being system totals against
> per-scanner figures. **The Quick Start Guide confirms TMI uses the User Guide's per-scanner
> numbering**, so the values the operator selects in TMI are the User Guide values.
> *(`RESOLVED-001` in `reference/mx60-reference-data.csv`)*

## B6 · Calibration import

TMI accepts a boresight calibration JSON via **USB1** *(TMI UG Rev L, p.18)*. Relevant where a
calibration is computed in TBC (§14) and applied to the system rather than to a project.

## B7 · Comments

> **FIELD TIP**
>
> **Use the Comments feature during collection.** A note made at the moment — *"heavy canopy from
> the bridge"*, *"stopped 4 min, traffic control"*, *"parked truck occluding the north side"* — is
> worth an hour of office guesswork three weeks later (§8.6, §9.5).

---

> **The full TMI procedure is §7 and §8.** This appendix is a reference for the indications, not a
> substitute for the procedure.
