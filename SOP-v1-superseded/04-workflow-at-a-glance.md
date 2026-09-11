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
