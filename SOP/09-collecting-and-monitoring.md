# 9. COLLECTING DATA AND MONITORING

## 9.1 Recording runs

**To start a run:** press **Record**. The button turns **green → red**.
**To stop a run:** press **Record** again. **Red → green**.

*(QSG Rev B, pp.12–13; TMI UG Rev L, p.9)*

> **IMPORTANT**
>
> Record only project-specific areas *(QSG Rev B, p.13)*. The Record button controls
> **laser and imagery only** — GNSS and IMU logging continues for the whole mission
> regardless *(TMI UG Rev L, pp.36, 40)*.

**Minimum mission time: 30 minutes** *(QSG Rev B, pp.13–14)*.

> **FIELD TIP**
>
> A short corridor does not excuse a short mission. If the work itself is 12 minutes, keep
> the mission open — drive, sit, extend the initialization at both ends — until you clear
> 30 minutes. Closing early gives the office less to work with.

## 9.2 Driving

### Speed

| | |
|---|---|
| **Recommended maximum, system operating** | **80 km/h (50 mph)** |
| Absolute maximum, operating or not | 110 km/h (68 mph) |

*(MX60 UG Rev B, pp.9, 53)*

> **WHY THIS MATTERS**
>
> Speed sets point density. The scanner fires at a fixed rate, so the faster you drive the
> further apart the profiles land. Vehicle speed is "a major factor affecting the final
> point density" *(TMR MLS Guideline §9.4.1, p.12)*.
>
> Slower is denser. It is also more time in traffic. Match speed to what the deliverable
> needs, not to what the road allows.

> **PARAMETRIX DECISION REQUIRED**
>
> Set a standard collection speed and the conditions for reducing it.
>
> *Recommended practice:* collect at or near prevailing traffic speed up to 80 km/h.
> Reduce for high-detail extraction, dusty conditions, or where the deliverable needs
> density. Never exceed 80 km/h with the system operating.

### Smoothness

Drive smoothly. Avoid harsh acceleration, hard braking, and abrupt steering.

The dust filter bulletin says it directly: "avoid harsh vehicle maneuvers as much as
possible" and "reduce driving speed as much as possible" in dusty environments
*(Dust Filter Bulletin, p.3)*.

> **WHY THIS MATTERS**
>
> This is the opposite of initialization, and the contrast is instructive. During
> initialization you *want* dynamics, because they make errors observable. During
> collection you want the vehicle behaving predictably, because every unmodelled jolt is
> a demand on the IMU and a source of noise in the cloud.
>
> Dynamics before you record. Smoothness while you record.

### Lane selection and passes

- Drive the lane closest to what you are collecting
- Follow the pass plan from Section 5 — minimum three passes for survey-grade work
- Drive each direction; two-way coverage fills shadows
- On dual carriageways, include at least one run in the **left-hand through lane** of each
  carriageway *(TMR §8.1.3, p.10)*

### Traffic and obstructions

You cannot control traffic, but you can respond to it:

| Situation | Response |
|---|---|
| Truck blocking the curb for a stretch | Note it; that stretch needs another pass |
| Stopped at a light | Not a problem. Trajectory continues; the scanner keeps collecting from a stationary position |
| Heavy stop-and-go | This is what the DMI is for |
| Parked cars occluding the curb line | Additional passes, or consider night collection (Section 5) |

> **CAUTION — heat**
>
> The operating temperature range is qualified: **not exposed to direct sun and without
> driving less than 10 km/h** *(MX60 UG Rev B, p.53)*. Extended idling in direct sun is
> outside the rated envelope. If you are held up for a long period in heat, keep air
> moving through the vehicle.

### Reversing and U-turns

Nothing in the Trimble documentation prohibits either. Both are legitimate — you will need
U-turns to run a corridor both ways.

> **FIELD TIP**
>
> Stop recording for the turnaround and start again on the new pass. It keeps the runs
> clean and makes the office's job easier, and it costs nothing — navigation logging
> continues either way.

## 9.3 What to watch while driving

This is the operator's real job. Check these in a loop.

| Watch | Good | Act if |
|---|---|---|
| **NAV button** | **Green** | Turns orange — note location. Turns **red** — recording stops being possible |
| **Camera buttons** | Green | Orange (not synced) or **red (error)** |
| **Laser buttons** | Green | Orange or **red** |
| **Record button** | **Red while on a run** | Green when you think you're recording |
| **Trajectory on map** | Thin blue line following the road | Line missing, jumping, or offset from the road |
| **Recorded coverage** | **Thick blue line** over collected areas | Thick line missing where you have driven a run |
| **SSD fill status** | Space remaining | Approaching full |
| **UTC time** | Displayed | Missing — GNSS initialization lost |
| **Disk icons** | No icon | Warning or Error icon appears |
| **Audible alarm** | Silent | **Battery Protect — 78 seconds to restore charge** |

*(TMI UG Rev L, pp.8–9, 33–34; MX60 UG Rev B, p.27)*

> **FIELD TIP — the thick blue line is your best QC tool**
>
> TMI draws the trajectory as a thin blue line and **areas where data was recorded as a
> thick blue line** *(TMI UG Rev L, p.33)*.
>
> At the end of a corridor, look at the map. Every stretch you meant to collect should be
> thick. A thin stretch where you believed you were recording means a run that did not
> start — and finding that in the vehicle costs minutes, while finding it in the office
> costs a mobilisation.

### Views worth opening

| View | Shows |
|---|---|
| **Dashboard** | Navigation status and camera thumbnails |
| **Camera** | Real-time preview per camera, with exposure control |
| **Nav** | Per-parameter accuracy on a log scale, plus satellite skyplot |
| **Laser** | Reduced real-time data stream — the **waterfall view** |

*(TMI UG Rev L, pp.34–37)*

**Camera exposure** can be adjusted live: the panoramic camera has an **Auto** button and
a slider mixing exposure time and gain; the back-down camera has an exposure compensation
slider. Left = darker, right = brighter *(TMI UG Rev L, pp.34–35)*.

**The waterfall view** is where you confirm the laser is producing sensible data — and
it is specifically where a wrong installation height shows up as immediate data gaps when
the dust filter is enabled *(Dust Filter Bulletin, p.3)*.

### Use the Comments feature

TMI lets you enter comments during a mission. They are **time-tagged and saved to the
database against the mission timeline** *(TMI UG Rev L, p.9)*.

> **FIELD TIP**
>
> Use it. "Truck blocking curb, north end" or "NAV dropped to orange under the overpass"
> written at the moment it happens is worth far more than a memory three days later — and
> it lands in the data, not on a piece of paper.

## 9.4 Changing settings mid-mission

You can change **capture settings** between data collection sequences without closing the
mission.

**To do it:** press the capture settings button, select a different Capture preset from the
drop-down, press Next. All sensors shut down and restart with the new configuration.

| Can change | Cannot change |
|---|---|
| Capture settings — laser mode, dust filter, camera triggers, sensor selection | **Vehicle settings** — you are still in the same vehicle |

*(TMI UG Rev L, p.41)*

> **IMPORTANT**
>
> Navigation data logging **keeps running** throughout the reconfiguration. This is the
> whole point: "you will save time as no additional GNSS/IMU initialization procedure will
> be needed." *(TMI UG Rev L, p.41)*

**Prepare presets in advance.** The dust filter bulletin makes the same point — capture
settings for enabling and disabling the filter "would need to be prepared in advance"
*(Dust Filter Bulletin, p.3)*.

## 9.5 Special conditions

### Dust

The dust filter is for **extremely dusty environments** — unpaved roads and open pit mines.
It is explicitly **not** intended for paved roads, urban canyons, or intercity
infrastructure *(Dust Filter Bulletin, p.1)*.

When using it:

| ☐ | Requirement |
|---|---|
| ☐ | **Installation height correct** — this is critical; too high means the mask touches the ground and you lose data |
| ☐ | Use the **higher** laser measurement rate |
| ☐ | Reduce speed as much as possible |
| ☐ | Avoid harsh manoeuvres |
| ☐ | Watch the **waterfall view** — gaps appear immediately if the height is wrong |

*(Dust Filter Bulletin, pp.2–3; TMI UG Rev L, p.29)*

### Lateral range limit

TMI can discard laser points beyond a set distance perpendicular to travel — **5 m to
50 m**, applied to both scanners *(TMI UG Rev L, p.29)*.

> **FIELD TIP**
>
> This is a data-volume tool, not a quality tool. It reduces file size by throwing away
> the far field before it is written. Useful on a long corridor where only the roadway
> matters — but discarded points are gone permanently. If in doubt, collect and filter in
> the office.

### GNSS-denied stretches

When you know you are entering a tunnel, underpass, or urban canyon:

- **Keep driving smoothly.** The IMU is bridging the gap and abrupt inputs make its job
  harder
- **Do not stop inside** unless you must
- **Note it** — use the Comments feature
- **Expect NAV to degrade**, and expect it to take time to recover afterwards
- Trimble specifies performance at a **60-second** outage; beyond that you are outside
  published figures *(MX60 UG Rev B, p.56)*

Section 13 covers the consequences.

## 9.6 Recognising a bad collection before you waste the day

| Sign | Meaning |
|---|---|
| NAV red for an extended period | No recording was possible during that stretch |
| Thick blue line missing where you drove a run | The run was not recording |
| Waterfall view showing gaps or nothing | Laser problem, or dust filter height wrong |
| Camera or laser button red | Device error — data from it is suspect or absent |
| Disk Error icon | Proceeding risks data loss |
| Battery Protect alarm | Power about to be cut |
| UTC time disappeared | GNSS initialization lost |

> **IMPORTANT**
>
> Trimble's rule is worth repeating here: **do not start a mission before solving any
> issue you had previously with the system** *(MX60 UG Rev B, p.44)*. The same judgement
> applies mid-mission. A system that is misbehaving will not fix itself over the next
> 30 km.

---

## References — Section 9

| Source | Pages |
|---|---|
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 8–9, 29, 33–37, 40–41 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 12–14 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 27, 44, 53, 56 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 1–3 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §8.1.3 p.10; §9.4.1 p.12 |
