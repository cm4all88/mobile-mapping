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
