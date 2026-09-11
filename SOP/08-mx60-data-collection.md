# 8. MX60 Data Collection

## 8.1 The shape of a mission

| Stage | What it is | §
|---|---|---|
| **Initialization** | Static period, straight run, dynamic manoeuvres | 8.2 |
| **Settling** | Additional time before recording anything that matters | 8.3 |
| **Collection** | The runs | 8.4–8.6 |
| **Closing sequence** | The mirror of initialization | 8.7 |
| **Shutdown** | Controlled, and confirmed | 8.8 |

> **The first and last five minutes of a mission determine the quality of the middle.** Everything
> in §2.2 about forward and backward filter passes comes down to this: the solution needs good
> observations at **both** ends, because the smoother works inward from both.

## 8.2 Initialization

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** — sourced to
> *(MX60 QSG Rev B, pp.13–14; MX60 UG Rev B)*

1. Position the vehicle at the initialization location — **open sky**, clear of buildings and
   canopy (§6.3)
2. Start the mission in TMI
3. **Remain stationary for 2–3 minutes**, logging static data
4. Drive **straight** for a short distance
5. Perform **dynamic manoeuvres** — a speed profile such as
   **0 → 50 → 20 → 50 → 20 km/h**, with turns
6. Watch for the navigation status to reach its ready indication
7. **Allow additional settling time — up to 10 minutes — before logging data that matters**

### With GAMS fitted

GAMS provides a direct heading measurement from two antennas and shortens initialization
considerably *(TBC 25943)*.

> **FIELD TIP**
>
> **Perform the full sequence anyway.** It costs a few minutes, it is what the Quick Start Guide
> describes, and the static period is doing more than heading determination (§8.3).

## 8.3 What the system is actually doing — and why green is not finished

**The static period** lets the GNSS receiver collect a clean, continuous set of observations and
resolve its ambiguities, and it gives the inertial filter a condition it can exploit: **the
vehicle's true velocity is zero.** Anything the motion sensors report while parked is therefore
pure error, measurable and removable.

**The dynamic manoeuvres** separate quantities that look identical at constant velocity. While
driving straight at a steady speed, a small attitude error and a sensor bias produce the same
signature. Change speed and direction and they stop looking alike, so the filter can tell them
apart. **Heading is the hardest component** and is what the turns are for.

> **IMPORTANT**
>
> **Green means the solution met the accuracy thresholds — not that it has finished converging.**
> That is why Trimble asks for up to ten more minutes before recording anything that matters
> *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day.** Do not spend it
> on the most important part of the corridor.

## 8.4 Recording runs

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **Minimum mission time: 30 minutes** *(MX60 QSG Rev B, pp.13–14)*.

> **A short corridor does not excuse a short mission.** If the collection itself is twelve
> minutes, keep the system running and logging navigation data to reach thirty. The trajectory
> solution improves with observation time, and closing early gives the office less to work with.

Runs are started and stopped within a mission. Each becomes a **Run** node in TBC (§11.3).

## 8.5 Driving

### Speed

| | Value | Source |
|---|---|---|
| **Recommended maximum, system operating** | **80 km/h (50 mph)** | *(MX60 UG Rev B)* |
| Absolute maximum, operating or not | 110 km/h (68 mph) | *(MX60 UG Rev B)* |

> **PARAMETRIX DECISION REQUIRED · D-48**
>
> **What collection speed, by deliverable type?** Speed determines point density along the
> corridor and the number of images per unit length. Trimble publishes a recommended maximum and
> an absolute maximum and **no guidance relating speed to deliverable quality**.
>
> *For consideration, not adopted:* collect at or near prevailing traffic speed up to 80 km/h,
> reducing where point density requires it. **Never exceed 80 km/h with the system operating.**

### Smoothness, lane selection and traffic

Drive smoothly. Sudden braking and sharp manoeuvres stress the inertial solution unnecessarily.
Choose the lane that gives the best line of sight to the features being collected, and remember
that the far side of a truck is not collected at all.

> **CAUTION**
>
> **Direct sun with the vehicle stationary or driving below 10 km/h is outside the rated operating
> envelope** *(MX60 UG Rev B, p.53)*. Extended idling in direct sun — at a signal, in a queue, or
> waiting for traffic control — is a real risk on a hot day.

### Reversing and U-turns

Plan turnarounds at locations where the vehicle can complete them without reversing under the
sensor's collection. Where a turn must happen inside the corridor, note it in the field record so
the office knows why the trajectory does what it does there.

## 8.6 Monitoring while driving

| Watch | For |
|---|---|
| **Navigation status** | Any degradation from the ready state |
| **Storage** | Remaining capacity against remaining corridor |
| **Sensor status** | A camera or laser that has stopped |
| **Audible alarm** | **Battery Protect — 78 seconds to restore charge** *(MX60 UG Rev B)* |

> **FIELD TIP**
>
> **Use TMI's Comments feature.** A note recorded at the moment — *"heavy canopy from here",
> *"stopped 4 min for traffic control"*, *"parked truck occluding the north side"* — is worth an
> hour of the office inferring it from residuals three weeks later.

### Recognising a bad collection before the day is wasted

Stop and reassess if: navigation status will not hold, a sensor has stopped reporting, storage
will not last the corridor, the battery is cycling into protection, or the conditions have moved
outside the go/no-go rule (§6.5).

> **The operator has authority to stand down.** A mission abandoned after twenty minutes costs
> twenty minutes. A mission completed on a degraded solution costs the office days and may cost a
> return visit.

## 8.7 The closing sequence

> **CAUTION · this is the most commonly skipped step in mobile mapping**
>
> The ending mirrors the beginning, and for the same reason. The post-processed trajectory is
> computed **forward and backward** and merged (§2.2). A degraded stretch in the middle of a
> mission is bracketed by good data on both sides and is bridged well. **A degraded stretch at the
> end has good data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** — sourced to
> *(MX60 QSG Rev B; MX60 UG Rev B)*

1. Finish the last run
2. Drive to an open-sky location
3. Perform **dynamic manoeuvres** — the mirror of initialization
4. **Remain stationary for 2–3 minutes**, logging static data
5. Close the mission in TMI
6. **Wait for the Control Unit power button light to go out — up to 90 seconds**

> **The whole sequence takes about five minutes and is the cheapest quality improvement available
> in the entire workflow.**

> **IMPORTANT**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and *then*
> driving to open sky achieves nothing.

## 8.8 Shutdown and confirming the data is written

Follow the documented shutdown. **Wait for the power button light to go out** before removing
power or the data disk *(MX60 UG Rev B)*.

> **CAUTION**
>
> Confirm the mission is written and closed before leaving the site. **While you are still at the
> site you can re-drive a run. Ten minutes down the road, you cannot.**

## 8.9 Mission record

The field record is a Parametrix artefact — **no software produces it**, and §9 and §11 both
depend on it.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Record per mission: date, operator, vehicle, mission ID; capture settings used; initialization
> location and time; each run with start/end and any incident; **GNSS conditions observed**;
> weather; traffic and occlusion events; anything not collected and why; the closing sequence
> performed; disk and free space at end.
> *(D-49)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We parked in the open and sat still for a few minutes, drove straight, then
> deliberately sped up, slowed down and turned — all so the system could work out three things it
> cannot see directly: how its inertial sensors are drifting, and exactly how the vehicle is tilted
> and pointed. Then we drove the corridor, and finished by repeating the whole start sequence
> backwards.
>
> **Why it matters.** It is like resection. The instrument has to know where it is and which way it
> is facing before any shot means anything. The difference is that here the answer degrades over
> time and distance, so you establish it at the start, let it settle, and re-establish it at the
> end.
>
> Sitting still is the part people skip and it is doing real work: parked, the system knows its
> true speed is zero, so anything its motion sensors report is pure error it can measure and
> remove. The manoeuvres do the same job for orientation — at a steady speed in a straight line, a
> small tilt error and a sensor bias look identical to the software; change speed and direction and
> they stop looking identical.
>
> **What can go wrong.** Green is a threshold, not a finish line. It means the solution met the
> accuracy figures, not that it has converged, which is why Trimble asks for up to ten more minutes
> before you record anything that matters. The first data of the day is the weakest data of the
> day.
>
> And the closing sequence gets skipped, because the job is done and everyone wants to leave. The
> office computes the trajectory forwards and backwards and merges them — so the end of the mission
> is an anchor for the whole reverse pass. Five minutes. You cannot add it afterwards.
>
> **What good looks like.** A proper static period in genuinely open sky. Manoeuvres that actually
> change speed and direction rather than a gentle curve. Settling time taken, with the important
> part of the corridor driven after it rather than before. Steady driving at a sensible speed.
> Comments recorded as things happen. A full closing sequence. And confirmation the data is written
> before the vehicle leaves — because on site a re-drive is twenty minutes, and from the office it
> is a day.
