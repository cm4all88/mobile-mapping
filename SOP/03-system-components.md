# 3. SYSTEM COMPONENTS

Reference section. Skim it once, come back to it when something isn't working.

Full specifications for every item here live in `reference/mx60-reference-data.csv`,
each row carrying its Trimble source and page.

## 3.1 The system at a glance

| # | Component | Where it lives | Weight |
|---|---|---|---|
| 1 | **MX60 Sensor Unit** | Vehicle roof, on the rack | 24 / 26 / 28 kg (Core / Pro / Premium) |
| 2 | **MX SCAN Control Unit 2** | Inside vehicle | 13 kg |
| 3 | **MX SCAN Power Unit** | Inside vehicle | 9 kg |
| 4 | **MX SCAN Roof Rack** | Vehicle roof | 18 kg |
| 5 | **Operator device** (tablet or laptop) | Inside vehicle | — |
| — | Cables (3), Data Carrier Docks (2), SSDs (2) | — | — |

*(MX60 UG Rev B, pp.12, 52; QSG Rev B, p.3)*

Optional: **GAMS** second GNSS antenna, **DMI** wheel odometer.

## 3.2 Sensor Unit

**What it is.** The sealed pod on the roof. Everything that measures lives here.

**What's inside:**

| Sensor | Detail |
|---|---|
| **2 laser scanners** | Time-of-flight, rotating mirror. ~346° deflection each. 2 mm accuracy, 2.5 mm precision @ 30 m. Range 0.6 m min; 150 m @ 500 kHz or 120 m @ 1000 kHz |
| **360° spherical camera** | Six cameras. 30 MP (Core) or 72 MP (Pro/Premium). Global shutter. ~90% of full sphere. Max 10 fps |
| **Down-looking camera** | 12 MP, on all configurations. Focal 8.0 mm, sharp from 2.0–9.0 m. Max 9 fps |
| **GNSS/IMU** | Applanix IN-Fusion+ / ProPoint. 2 × 336 tracking channels. IMU logs at 200 Hz, GNSS at 5 Hz |

*(MX60 UG Rev B, pp.13, 53–57)*

**Connectors** — one on the left, three on the right:

| Connector | Use |
|---|---|
| **Main** | Control Unit ← 5 m cable |
| **Ant.** | GAMS Antenna Kit |
| **DMI** | DMI Kit |
| **Ext.** | External devices — PPS, trigger, event, RS-232 |

*(MX60 UG Rev B, p.13)*

**Why you should care.** This is the expensive part and the accurate part. Its optics
must be clean, its mounting must be rigid, and it must have a clear view.

> **CAUTION**
>
> Two people are required to mount or dismount the Sensor Unit. Prepare the mount
> mechanism *before* lifting, and lift only by the dedicated handles.
> *(MX60 UG Rev B, pp.9, 10, 16; QSG Rev B, p.5)*

**Common problems:**

| Symptom | Usually means |
|---|---|
| Dirty or hazy imagery | Lens glass needs cleaning — see §6 for the correct method |
| Missing data low on one side | Sensor obstructed by the vehicle, or rack too far forward |
| Noisy cloud in dust | Consider the dust filter, but only on unpaved roads or mine sites |
| Sensor LED blinking red | Component failed — do not start a mission |

## 3.3 Control Unit (MX SCAN Control Unit 2)

**What it is.** The computer that runs the system and records the data.

> **CAUTION**
>
> The MX60 works **only** with Control Unit 2. Do not attempt to operate it with an
> older MX SCAN Control Unit — Trimble states this may damage the system.
> *(MX60 UG Rev B, p.20; QSG Rev B, p.6)*

**Front panel:**

| Item | Notes |
|---|---|
| Power In connector | From Power Unit |
| Sensor Unit connector | 5 m cable |
| **On/Off button** | **Hold ≥15 seconds** to start |
| **Status LEDs** ×3 | Control Unit, Sensor Unit, Wi-Fi |
| **2 × Exchangeable Data Disks** | 4 TB SSDs — see §3.7 |
| Wi-Fi USB stick 1 | System's own access point (operator device connects here) |
| Wi-Fi USB stick 2 | Connects the system *to* a network/hotspot |
| LAN | Operator device via Ethernet |
| WAN | Internet / remote support |
| USB 1 | Software load, licence update |
| USB 2 | **Trimble Support use only** |
| Fuses | Circuit breaker 1 = Control Unit, 2 = Sensor Unit, under the cover |

*(MX60 UG Rev B, pp.20–21)*

**LED meanings — learn these:**

| LED state | Meaning |
|---|---|
| Blinking green | Starting, updating, or shutting down |
| **Solid green** | **Ready** |
| **Blinking red** | **Component failed** |

*(MX60 UG Rev B, p.21)*

**Where to mount it.** Where the operator can reach the data disks *and* see the status
LEDs. The only hard constraint is the 5 m cable to the Sensor Unit.
*(MX60 UG Rev B, p.23)*

> **CAUTION**
>
> IP30 — not waterproof. Keep vent holes clear at all times.
> *(MX60 UG Rev B, p.53; QSG Rev B, p.6)*

**If a circuit breaker trips:** reactivate it, but check every cable before turning the
system back on — the trip may have been caused by a damaged cable *(MX60 UG Rev B, p.21)*.

## 3.4 Power Unit

**What it is.** The interface between the vehicle battery and the system. It converts
power, filters out alternator spikes, and protects the vehicle battery.

**Battery Protect** — the behaviour to recognise in the field:

| Condition | Response |
|---|---|
| Below 10.5 V for >12 s | **Audible warning** |
| Below 10.5 V for >90 s | **Power cut off** |
| Rises above 12.0 V within those 90 s | Normal status recovered |

*(MX60 UG Rev B, p.27)*

> **WHY THIS MATTERS**
>
> That audible warning is a 78-second countdown to losing the mission. If you hear it,
> get the engine running and the alternator charging — don't finish the run first.

**Power requirements:** 12–16 V DC. 9 A standby, 12 A operating, **25 A at startup**.
Trimble's Quick Start Guide asks for a **30 A or greater supply** and recommends an
auxiliary battery. Minimum vehicle battery 60 Ah.
*(MX60 UG Rev B, pp.52, 61; QSG Rev B, p.4)*

> **CAUTION**
>
> Never cover the Power Unit — it has vents on the back and bottom and will overheat.
> Install it in a dry place, secured through its three mounting points.
> *(MX60 UG Rev B, pp.25, 28)*

If the system is used daily, the Power Unit can stay connected to the vehicle. If it
will sit unused for a long period, disconnect it to save the vehicle battery
*(MX60 UG Rev B, pp.25–26)*.

## 3.5 Roof rack

**Two different racks exist.** Confirm which one you have before any lever-arm work.

| | **MX SCAN Roof Rack** | **MX Shock Absorbing Mounting Rack** |
|---|---|---|
| Weight | 18 kg | 28 kg |
| Mounts to | Square-cut universal roof bars, ≤85 × 30 mm | Prepared level platform / aluminium T-slot profile |
| Fixings | Bracket screws | M6 (20 × 6.6 mm holes) or M8 (16 × 9.0 mm holes) — all holes of one type must be used |
| Intended for | Standard road vehicles | "Harsher environments than a standard road" |
| Limits | Overhang ≤330 mm; bracket spacing ≥650 mm | Platform must be level; screws min A2-70 or class 8.8 |

*(MX60 UG Rev B, pp.29–33, 52; Rack UG Rev B, pp.6–7, 9)*

> **CAUTION**
>
> Both racks carry the **External Reference Point**, but the GAMS corner offsets
> published in the MX60 User Guide (X = +1.006 m, Y = −0.469 m, Z = +0.025 m) apply to
> the **standard Roof Rack only**. Do not use them with the shock absorbing rack.
> *(MX60 UG Rev B, p.68)*

**Positioning:** as far to the rear of the vehicle as possible, so the laser and the
backward/downward camera have a clear line of sight to the road surface, unobstructed by
the vehicle *(QSG Rev B, p.4)*.

**Maintenance:** clean and re-lubricate the lock bars and fast-lock mechanism frequently;
spray oil after cleaning *(MX60 UG Rev B, p.49)*.

## 3.6 Operator device

Not supplied by Trimble — bring your own.

| Requirement | Detail |
|---|---|
| Display | 10" or larger, touch preferred |
| Browser | **Google Chrome** — other browsers untested |
| Connection | Ethernet (DHCP: obtain IP and DNS automatically) or Wi-Fi |
| Software | **None.** TMI runs entirely in the browser at `http://tmi.mx-scan.net` |

*(MX60 UG Rev B, pp.13, 36; QSG Rev B, pp.3, 8)*

**Wi-Fi:** SSID is `Trimble MX60 (<serial number>)`. The password is on stickers inside
the Control Unit top case — **unique per system and not changeable**
*(MX60 UG Rev B, p.37)*.

> **FIELD TIP**
>
> Photograph the Wi-Fi sticker and keep it somewhere you can find it. It cannot be reset,
> and it lives in a case that may not be in the vehicle.

## 3.7 Storage media

**2 × 4 TB removable SSDs**, and they are not interchangeable in content:

| Disk | Records |
|---|---|
| **SSD 1** | Laser 1 and 2, navigation (GNSS + IMU), panoramic camera |
| **SSD 2** | Down-facing camera |

*(MX60 Spec Sheet p.3; QSG Rev B, p.8)*

> **IMPORTANT**
>
> Both disks are needed for a complete mission. SSD 1 holds the navigation data — without
> it there is no trajectory, and without a trajectory the imagery on SSD 2 is worthless.
> Treat them as one dataset.

> **CAUTION**
>
> **Never connect the USB cable while an exchangeable data disk is inside the Control
> Unit.** Remove the disk first. *(MX60 UG Rev B, p.10)*

Data comes off via the **MX SCAN Data Carrier Dock** (two supplied) over USB 3 — see §11.

## 3.8 Optional accessories

### GAMS (GNSS Azimuth Measurement System)

A second GNSS antenna. Because the system can then see the *orientation* of the baseline
between two antennas, it works out heading far faster than a single antenna can.

**Effect on the field procedure:** GAMS "not only is the initialization time reduced but
also **no special driving maneuvers are necessary** to complete initialization"
*(MX60 UG Rev B, p.67)*.

| Use case | Offset accuracy needed | Baseline |
|---|---|---|
| Collection only | 10 cm or better | — |
| **Post-processing the navigation data** | **A few millimetres** | **≥2.0 m** |

Both antennas **must be the same type** *(MX60 UG Rev B, p.68)*.

> **IMPORTANT**
>
> GAMS offsets must be re-measured **every time** the antenna is re-installed for a new
> mission. *(MX60 UG Rev B, p.67)*

### DMI (Distance Measuring Indicator)

A mechanical wheel odometer. Improves accuracy in challenging GNSS conditions and in
heavy stop-and-go traffic, and supplies **ZUPT** (zero velocity update) information for
navigation post-processing.
*(MX60 UG Rev B, p.42; MX60 Spec Sheet p.4)*

> **CAUTION**
>
> The DMI must be fitted to a **non-steering wheel**, and its lever arm is measured to
> the centre of the tread where that wheel contacts the road. A DMI on the **left** wheel
> has a **negative Y** lever arm. *(MX60 UG Rev B, p.46)*

> **PARAMETRIX DECISION REQUIRED**
>
> Confirm whether GAMS and DMI are owned, and whether they are fitted as standard.
>
> *Recommended practice:* fit both. GAMS removes an initialization step the operator can
> get wrong; DMI protects the trajectory exactly where mobile mapping is weakest.

## 3.9 Delivered items

| Case | Contents |
|---|---|
| **Box 1** — Sensor Unit transport case (806 × 716 × 634 mm) | Sensor Unit; Control-Unit-to-Sensor-Unit cable 5 m; hex wrenches 5 and 6 |
| **Box 2** — 75 kg, 1170 × 770 × 500 mm | Roof Rack; Power Unit; Control Unit 2 (with Wi-Fi sticker labels, SSD keys, 2 × Wi-Fi sticks, Quick Start Guide, SSD installed); 2 × Data Carrier Dock; Source-to-Power-Unit cable 5 m; Power-Unit-to-Control-Unit cable 3 m |

*(MX60 UG Rev B, pp.38–40; QSG Rev B, p.3)*

**Trimble's use assumptions** — worth knowing, because they shape the procedures:

- Roof Rack: **permanently** installed on the vehicle
- Power Unit and its source cable: **permanently** installed inside
- Control Unit: **temporarily** installed, for operation
- Sensor Unit: **temporarily** installed, removed for transfer and stored in its case
- GAMS and DMI: removed for transfer and storage

*(MX60 UG Rev B, p.41)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether Parametrix follows Trimble's assumptions — particularly whether the
> Sensor Unit is removed and cased at the end of each day.
>
> *Recommended practice:* follow them. Removing the Sensor Unit protects a very
> expensive item from weather, theft, and low-clearance accidents, and Trimble's storage
> instructions assume it. Note that removing the Sensor Unit means removing GAMS too,
> which means re-measuring its lever arm next time.

---

## References — Section 3

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 10, 12–13, 16, 20–21, 23, 25–29, 31–33, 36–42, 46, 49, 52–57, 61, 67–68 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 3–6, 8 |
| Trimble MX60 Spec Sheet, PN 022516-737C (04/25) | 2–4 |
| Trimble MX Shock Absorbing Mounting Rack User Guide, Rev B, May 2025 (P/N 37000001) | 6–7, 9 |
