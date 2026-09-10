# 7. STARTING THE SYSTEM AND TMI

From "the system is mounted" to "ready to initialize."

## 7.1 Power-up sequence

Order matters. Startup draws **25 A**, and the system asks for a 30 A supply
*(MX60 UG Rev B, p.61; QSG Rev B, p.4)*.

1. **Turn off the engine auto start/stop function**
2. Confirm both SSDs are **inserted and locked** in the Control Unit
3. **Start the vehicle**
4. **Then** press and hold the Control Unit power button for **at least 15 seconds**
5. Power Unit LED goes **constant green** once the vehicle is delivering 12 V
6. Sensor Unit and Control Unit LEDs **blink for about 10 seconds**
7. Both LEDs turn **solid green** — the system is ready

*(QSG Rev B, p.8; MX60 UG Rev B, p.21)*

> **CAUTION**
>
> Before starting, make sure all connections are secure and the recording SSDs are
> inserted and locked. *(MX60 UG Rev B, p.48; TMI UG Rev L, p.4)*

> **WHY THIS MATTERS — start the vehicle first**
>
> A 25 A startup surge on a battery with no alternator behind it is how you meet Battery
> Protect the hard way: audible warning below 10.5 V, power cut 90 seconds later
> *(MX60 UG Rev B, p.27)*.

**LED reference:**

| State | Meaning |
|---|---|
| Blinking green | Starting, updating, or shutting down |
| **Solid green** | **Ready** |
| **Blinking red** | **Component failed — do not start a mission** |

*(MX60 UG Rev B, p.21)*

## 7.2 Connecting to TMI

TMI is web-based. Nothing is installed on your device.

| | |
|---|---|
| **Browser** | Google Chrome — other browsers untested |
| **TMI.Capture** | `http://tmi.mx-scan.net` |
| **TMI.AI** (admin) | `http://admin.mx-scan.net` |

*(TMI UG Rev L, pp.7, 46)*

**Wi-Fi:** SSID `TrimbleMX60 (<serial number>)`. Password is on stickers shipped inside
the system — **unique per system, cannot be changed**. If lost, contact Trimble Imaging
Support with the serial number *(TMI UG Rev L, pp.5, 51)*.

**Ethernet:** patch cable to the Control Unit LAN port. Your device gets an IP by DHCP
*(TMI UG Rev L, p.5)*.

> **CAUTION — mandatory before first use**
>
> The **Wi-Fi country** must be set the first time the system is turned on, and again
> every time you start a collection campaign **in a different country**. This is a legal
> compliance requirement.
>
> `Settings → System Administration → WiFi → MX60 WiFi Access Point → <country>`
> *(TMI UG Rev L, pp.5, 51; MX60 UG Rev B, p.48)*

> **FIELD TIP**
>
> An Internet connection is optional but useful — it's what puts the OSM background map
> behind your trajectory *(TMI UG Rev L, pp.8, 32)*. Note you **cannot** use a hotspot
> that requires logging in through a web page *(TMI UG Rev L, p.51)*.

## 7.3 The TMI screen

| Button | What it does |
|---|---|
| ☰ | Main menu |
| ⏻ | Shut down the system |
| ⊗ | Close the mission in progress |
| ? | Help |
| Layers | Map layers |
| +/− | Zoom |
| ↻ | Map orientation — north vs. vehicle |
| ⊙ | Auto-centre on vehicle |
| Dashboard | System overview |
| **Camera** | Camera view — **colour-coded** |
| **Nav** | Navigation view — **colour-coded** |
| **Laser** | Laser view — **colour-coded** |
| 💬 | Comments — time-tagged to the mission timeline |
| ⚙ | Change capture settings mid-mission |
| **● Record** | **Red = logging, green = not logging** |

*(TMI UG Rev L, pp.8–9)*

### Status colours — learn these before you drive

**Camera and Laser buttons:**

| Colour | Meaning |
|---|---|
| Red | Device error |
| Orange | Device not yet time-synchronized |
| **Green** | **Time synchronization complete** |

**Navigation button** — different, and more important:

| Colour | Meaning | Can you record? |
|---|---|---|
| **Red** | No valid navigation solution, or navigation system failure | **No** |
| **Orange** | Navigation solution available | **Yes — but see below** |
| **Green** | Solution **meets your user accuracy requirements** | Yes |

*(TMI UG Rev L, pp.8–9, 25, 40)*

> **IMPORTANT — orange is not good enough**
>
> TMI *permits* recording at orange. Trimble's Quick Start Guide tells you to wait for
> **green** *(QSG Rev B, pp.12, 14)*.
>
> Orange means only that a solution exists. **Green means the solution meets the accuracy
> figures you set.** For survey-grade work, wait for green.

> **PARAMETRIX DECISION REQUIRED**
>
> State whether recording at orange NAV status is ever permitted.
>
> *Recommended practice:* prohibit it for survey-grade work. Permit it only for
> asset-grade collection, with the project surveyor's approval recorded in the field
> protocol.

## 7.4 What "green" actually means

The orange→green threshold is set in **Capture Settings → User Accuracies for
Navigation**, and Trimble ships different defaults per configuration:

| Parameter | MX60 **Premium** | MX60 **Core / Pro** |
|---|---|---|
| Attitude RMS (roll/pitch) | 0.060° | 0.075° |
| Heading RMS | 0.045° | 0.045° |
| Position RMS | 10.000 m | 10.000 m |
| Velocity RMS | 0.025 m/s | 0.030 m/s |

*(TMI UG Rev L, p.26)*

> **ADVANCED — read the position threshold again**
>
> Position RMS defaults to **10 metres**. That is deliberately loose. The green light is
> effectively driven by **attitude, heading and velocity** — the things initialization
> manoeuvres actually improve — not by absolute position.
>
> So green tells you the *orientation* solution has converged. It does not tell you the
> corridor will meet a centimetre-level positional spec. That is decided later, by
> post-processing, control and geometry. Section 13.

> **CAUTION**
>
> Changing these defaults "can ONLY be done by advanced users," and values must stay
> compliant with the navigation system in use. *(TMI UG Rev L, p.25)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether Parametrix uses Trimble's factory user-accuracy defaults or its own, and
> who may change them.
>
> *Recommended practice:* use factory defaults. Restrict changes to a named
> trained-personnel list, and record any change in the field protocol — a mission run
> against altered thresholds is not comparable to one run against the defaults.

## 7.5 Configuring the mission

### Vehicle settings

Describes how the sensor is mounted. Set once per vehicle setup and saved as a preset.

| Field | Notes |
|---|---|
| **Name** | Required — appears in the preset pull-down |
| Description | Optional |
| **Install Height** | From the External Reference Point on the rack to the road surface, in metres |
| **Use DMI** | Checkbox + lever arm XYZ, mounting position (left/right, driving direction as reference), **wheel diameter** |
| **Use GAMS** | Checkbox + lever arm XYZ |
| Use External Connector | Checkbox + trigger/event/COM configuration |

*(TMI UG Rev L, pp.20–24)*

> **CAUTION — the aiding-sensor trap**
>
> "If you do not activate an aiding navigation sensor here, the data from this sensor will
> **NOT be logged** during the mission, even though the required connections to the sensor
> unit may have all been made properly."
> *(TMI UG Rev L, p.21)*
>
> A DMI can be perfectly fitted, correctly measured, physically connected — and silently
> contribute nothing, because the checkbox is off. Nothing in the field will tell you.

> **FIELD TIP**
>
> Measure the DMI **wheel diameter** carefully *(TMI UG Rev L, p.21)*. It scales every
> distance the DMI reports. Tyre wear and pressure change it.

### Capture settings

What the sensors do. Can be changed mid-mission; vehicle settings cannot.

| Setting | Options |
|---|---|
| **Sensor selection** | Each laser and camera active or idle. **The navigation sensor is always active** |
| **User Accuracies for Navigation** | The orange→green thresholds above |
| **Camera trigger** | Distance Based (constant metres) or Fixed Frame Rate (constant fps). **Max 10 fps** |
| **Laser Mode** | Combination of measurements/second and rotations/second |
| **Enable Dust Filter** | Eliminates dust above the road surface |
| **Lateral Range Limit** | 5–50 m. Discards points beyond that distance perpendicular to travel. **Applies to both scanners** |

*(TMI UG Rev L, pp.25–29; QSG Rev B, p.10)*

> **CAUTION**
>
> Both the dust filter and the lateral range limit depend on **installation height being
> set correctly** in Vehicle Settings. Get it wrong and you lose data.
> *(TMI UG Rev L, p.29; Dust Filter Bulletin, p.2)*

> **IMPORTANT — check how your TMI version presents the laser setting**
>
> The Quick Start Guide (March 2025) describes two separate controls — *Measurement Prog*
> `[500 kHz, 1000 kHz]` and *Line Speed* `[120 Hz, 200 Hz]`. The TMI User Guide Rev L
> (April 2026) describes a single combined **Laser Mode** for the MX60.
>
> Rev L is the newer document. Confirm against your installed TMI version before relying
> on either. Note also that Trimble states the measurements/second values shown in the
> interface are **rounded** *(TMI UG Rev L, pp.28–29)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish standard capture presets and a naming convention — for example a default
> corridor preset, a dust preset, and an urban preset.
>
> *Recommended practice:* build named presets in advance and export them to file. TMI can
> export all presets to a single file and re-import them with Overwrite or Append
> *(TMI UG Rev L, pp.17–18)*, which gives you a backup and a way to put an identical
> configuration on a second system.

## 7.6 Disk check

At startup and after every mission, TMI checks the data disks. The result appears in the
**upper-right corner of the map window**, alongside UTC time and SSD fill status.

| Result | Meaning |
|---|---|
| **No icon** | Everything is fine |
| **Warning** | Mission can still run, but **data loss may occur under high system load** |
| **Error** | Disk performance is compromised; **proceeding may lead to data loss**. You must confirm to start |

*(TMI UG Rev L, pp.33–34)*

> **IMPORTANT**
>
> The **Start Mission button is disabled while a disk check is running** (Initializing /
> Analyzing). Wait for it. *(TMI UG Rev L, p.38)*

> **PARAMETRIX DECISION REQUIRED**
>
> Set the rule for proceeding past a disk Warning or Error.
>
> *Recommended practice:* never start a production mission on a disk reporting Error, and
> treat a Warning as grounds for swapping the disk before a long collection. A disk that
> fails under load fails in the middle of the corridor, not at the start.

## 7.7 Ready-to-initialize check

| ☐ | Item |
|---|---|
| ☐ | Both SSDs inserted and locked; disk check clean |
| ☐ | Control Unit, Sensor Unit LEDs **solid green** |
| ☐ | Power Unit LED constant green |
| ☐ | TMI open in Chrome, connected |
| ☐ | Wi-Fi country set (first use / new country) |
| ☐ | Correct **Vehicle Preset** selected — installation height matches this vehicle today |
| ☐ | DMI and/or GAMS **checkboxes activated** if fitted |
| ☐ | Correct **Capture Preset** selected |
| ☐ | Camera and Laser buttons green (time-synchronized) |
| ☐ | UTC time showing — GNSS initialization complete |
| ☐ | Vehicle parked in open sky for initialization |

---

## References — Section 7

| Source | Pages |
|---|---|
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 4–5, 7–9, 17–18, 20–29, 32–34, 38, 40, 46, 51 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 4, 8, 10, 12, 14 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 21, 27, 48, 61 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 2 |
