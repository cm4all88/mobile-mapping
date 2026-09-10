# APPENDIX B — TMI STATUS AND WARNING REFERENCE

Every indicator TMI shows, what it means, and whether it needs action now.

---

## B1. Status buttons

### Camera and Laser

| Colour | Meaning | Action |
|---|---|---|
| **Red** | Device error | **Stop.** Do not collect quality data |
| **Orange** | Not yet time-synchronized | Wait for green |
| **Green** | Time synchronization complete | Proceed |

*(TMI UG Rev L, pp.8–9)*

### Navigation — different rules

| Colour | Meaning | Recording | Action |
|---|---|---|---|
| **Red** | No valid solution, or navigation system failure | **Blocked by the system** | Improve sky visibility; complete initialization |
| **Orange** | A navigation solution is available | **Permitted by TMI** | Continue initializing to reach green |
| **Green** | Solution meets your **user accuracy figures** | Yes | Proceed |

*(TMI UG Rev L, pp.9, 25, 40)*

> **IMPORTANT**
>
> TMI *permits* recording at orange. The Quick Start Guide directs you to wait for
> **green** *(QSG Rev B, pp.12, 14)*. Orange means only that a solution exists.

### Record button

| Colour | Meaning |
|---|---|
| **Red** | Data logging **active** |
| **Green** | **No** data logging |

*(TMI UG Rev L, p.9)*

> Counter-intuitive: **red means recording**. Green means you are not.

---

## B2. What "green" means numerically

The orange→green threshold is set in **Capture Settings → User Accuracies for Navigation**.

| Parameter | MX60 **Premium** | MX60 **Core / Pro** |
|---|---|---|
| Attitude RMS (roll/pitch) | 0.060° | 0.075° |
| Heading RMS | 0.045° | 0.045° |
| Position RMS | 10.000 m | 10.000 m |
| Velocity RMS | 0.025 m/s | 0.030 m/s |

*(TMI UG Rev L, p.26)*

> Position RMS defaults to **10 m**. Green is driven by attitude, heading and velocity —
> not absolute position. See §7.4.

> **CAUTION** — changing these "can ONLY be done by advanced users"
> *(TMI UG Rev L, p.25)*.

---

## B3. Navigation logging — three rules that surprise people

| Rule | Source |
|---|---|
| Navigation logging **starts automatically** when a valid position exists and the blue arrow appears — **even if NAV is still red** | TMI p.40 |
| Navigation logging is **not affected** by orange↔green transitions | TMI pp.36, 40 |
| Navigation logging **stops immediately** when the mission is closed | TMI pp.31, 42 |

**Consequence:** the trajectory records long before you press Record and continues between
runs. The Record button starts and stops **laser and imagery only**.

---

## B4. Map window indicators

| Indicator | Meaning |
|---|---|
| **Blue arrow** | Valid position available — navigation logging has begun |
| **Thin blue line** | Trajectory |
| **Thick blue line** | **Areas where data was recorded** |
| **UTC time** (top right) | Appears when GNSS initialization is complete |
| **SSD fill status** (top right) | Remaining capacity |
| No OSM background | System has no Internet connection — cosmetic only |

*(TMI UG Rev L, pp.32–33, 40)*

> **FIELD TIP**
>
> The **thick blue line** is the single best in-vehicle QC check. Every stretch you meant
> to collect should be thick. Thin where you believed you were recording = a run that
> never started.

---

## B5. Disk check states

Checked at system startup and after each mission.

| Icon | Meaning | Can you continue? |
|---|---|---|
| **None** | Everything is fine | Yes |
| **Warning** | Mission can run, but **data loss may occur under high system load** | Risk decision — not for production |
| **Error** | **Disk performance compromised; proceeding may lead to data loss** | Requires explicit confirmation — recommend no |

*(TMI UG Rev L, pp.33–34)*

Click an icon for detail. The **Start Mission button is disabled while a disk check is
running** *(TMI UG Rev L, p.38)*.

---

## B6. Message Log

`Menu → Message Log`. Filters *(TMI UG Rev L, p.16)*:

| Filter | Shows |
|---|---|
| **All** | Every logged event |
| **Alarm** | Alarm events only |
| **Warning** | Warning events only |

Sortable by user name.

> **FIELD TIP**
>
> Check the Alarm filter before closing a long mission. Something may have been logged
> hours ago that nobody saw at the time.

---

## B7. Views

| View | Contents |
|---|---|
| **Dashboard** | Navigation status; camera thumbnails |
| **Camera** | Real-time preview per camera + exposure control |
| **Nav** | Per-parameter accuracy on a **logarithmic** scale, status, **satellite skyplot** |
| **Laser** | Reduced real-time data stream — the **waterfall view** |

*(TMI UG Rev L, pp.34–37)*

**Camera exposure, adjustable live** *(TMI UG Rev L, pp.34–35)*:

| Camera | Control |
|---|---|
| Panoramic | **Auto** button, or slider mixing exposure time and gain |
| Back-down | Exposure compensation slider |

Slider **left = darker**, **right = brighter**.

---

## B8. Actions that need care

| Action | Effect | Reference |
|---|---|---|
| **Complete Mission** | Stops the mission **and navigation logging** immediately | TMI pp.31, 42 |
| **Shutdown** | Powers off all sensors and the control unit | TMI p.31 |
| **Mission re-configuration** | Changes capture settings; sensors restart; **navigation logging continues — no re-initialization** | TMI p.41 |
| **Removing power directly** | **Risk of corrupted data — never do this** | TMI p.31 |
| **Calibration Import** | Loads a new boresight JSON from USB1 | TMI p.18 |
| **Firmware update** | Full shutdown; power-on may take **up to 6 minutes** | TMI p.49 |
| **Remote access** | **All data on the system becomes visible to Trimble Support** | TMI p.54 |

---

## B9. Settings that silently lose data

The four ways to collect nothing while everything looks normal.

| Setting | Failure |
|---|---|
| **DMI / GAMS checkbox not activated** in Vehicle Settings | That sensor logs **nothing**, even though it is fitted, measured and connected *(TMI p.21)* |
| **Sensor deactivated** in Capture Settings | That laser or camera records nothing |
| **Lateral Range Limit** enabled (5–50 m) | Points beyond the limit are **discarded permanently** *(TMI p.29)* |
| **Dust filter with wrong install height** | Mask reaches the ground — data loss, visible as gaps in the waterfall view *(TMI p.29; Dust Filter Bulletin pp.2–3)* |

> **IMPORTANT**
>
> None of these produce an error. All four are prevented by the same habit: confirm the
> Vehicle Preset and Capture Preset at the start of every mission, out loud, against the
> field protocol.

---

*Sources: TMI Software User Guide Rev L, April 2026 (P/N T001242) · MX60 Quick Start
Guide Rev B, March 2025 · Product Bulletin: Enabling the Dust Filter in TMI for MX60,
January 2025.*
