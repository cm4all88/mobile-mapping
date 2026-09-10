# 6. EQUIPMENT PREPARATION AND VEHICLE INSTALLATION

Everything from "the system is in its case" to "ready to switch on."

## 6.1 How often each task happens

Read this table first. It is the reason this section is organised the way it is.

| Frequency | Tasks | Who |
|---|---|---|
| **Once, or when the vehicle changes** | Power supply installation, roof bar fitting, Power Unit mounting, rack positioning | **Trained personnel** + professional automotive electrician |
| **When the setup changes** | Lever-arm measurement (GAMS/DMI only), Vehicle Preset creation, Wi-Fi country setting | **Trained personnel** |
| **Every project** | Confirm installation height, confirm correct Vehicle Preset | Operator |
| **Every day / every mission** | Safety check, components checklist, optics cleaning, cable inspection | Operator |

> **CAUTION**
>
> Trimble requires that anyone installing or removing the system be familiar with the
> installation chapter of the Trimble manual **and have received prior training**.
> Operation and service may only be performed by properly trained personnel.
> *(MX60 UG Rev B, pp.7, 9, 10)*

## 6.2 One-time installation

Performed once per vehicle. Not an operator task.

### Power supply

> **CAUTION**
>
> Any installation and integration of a power supply in a vehicle **must be done by a
> professional car electrician service** and is under the customer's responsibility and
> control. All components — cable type, gauge, fuses, relay — must comply with the MX60
> input power requirements and with local law and vehicle regulations.
> *(MX60 UG Rev B, p.61)*

| Requirement | Value |
|---|---|
| Input voltage | 12–16 V DC |
| Current at startup | **25 A at 12.8 V** (320 W) |
| Current in operation | 12 A (160 W) |
| Supply rating needed | **30 A or more** |
| Battery capacity | **60 Ah minimum** |
| Auxiliary/buffer battery | **Recommended** |
| Direct-connection fuse | 35 A, close to the battery |

*(MX60 UG Rev B, pp.52, 61–62; QSG Rev B, p.4)*

Trimble documents two setups — direct connection (car battery only) and buffer battery
(recommended). Both use a relay that supplies power only when the alternator is running,
preventing the car battery from going flat *(MX60 UG Rev B, p.62)*.

> **CAUTION**
>
> On vehicles using electric propulsion, install the product so it is **fully separate
> from the car battery charging system**. *(MX60 UG Rev B, p.8)*

### Vehicle requirements

| Requirement | Detail |
|---|---|
| Wheels and use | Rubber wheels, paved roads only |
| Body | Hatchback with upright rear door |
| **Roof height** | **Minimum 1.60 m** — required by the down-looking camera's minimum distance |
| Colour | **Not bright** — avoids exposure artefacts in imagery |
| Start/stop | **Must be switched off** |
| Alternator | Sufficient power, or an additional battery pack |
| Roof rails | Withstand the load; ideally covering the entire roof so rack position can be adjusted |
| Interior room | Space for the Sensor Unit case (806 × 716 × 634 mm) and Control Unit case (453 × 255 × 408 mm) during transfer |

*(MX60 UG Rev B, p.59)*

### Mounting the Power Unit and Control Unit

Both live inside the vehicle and **neither is waterproof** (IP30).

**Power Unit** — three mounting points, 6 mm screws:

- Dry location
- Securely fastened
- **Always keep clear space around the vents on the back and bottom**
- Never cover it
- Consider cable routing: 3 m to the Control Unit

*(MX60 UG Rev B, p.28)*

**Control Unit** — position it where the operator can:

- Reach the **data disks**
- **See the status LEDs**

The only hard constraint is the 5 m cable to the Sensor Unit. It can be secured with
screws or through its two belt guides *(MX60 UG Rev B, p.23)*.

> **CAUTION**
>
> Ensure the vent holes in each unit are always uncovered.
> *(QSG Rev B, p.6)*

### Roof bars and rack

1. Park the vehicle in a **level location** *(QSG Rev B, p.4)*
2. Install two roof bars so the rack sits **as far to the rear as possible**
3. Remove the screw bridge; place the rack on the bars
4. Adjust bracket position so the rack is **as horizontal as possible**
5. Attach the screw bridge and tighten all screws

**Positioning limits:**

| Limit | Value |
|---|---|
| Distance between front and back brackets | **> 650 mm** (marked by a red stripe on the mainframe) |
| Back bracket to end of rack (overhang) | **≤ 330 mm** |
| Roof bar dimensions | Square cut, ≤ 85 mm wide × 30 mm high |
| Torque, screws No.5 | **8 Nm** |

*(MX60 UG Rev B, pp.29, 31–33; QSG Rev B, pp.4–5)*

> **IMPORTANT**
>
> The laser and the backward/downward camera must have a **clear line of sight to the
> road surface**, unobstructed by the vehicle. This is why the rack goes to the rear.
> *(QSG Rev B, p.4)*

### Tightening screws — the correct method

Trimble is specific about this, and it applies everywhere in the system.

**Standalone screws:** slow, continuous movement. No jerking. Comply strictly with the
stated torque value.

**Clusters:** tighten **crosswise in three steps**:

| Step | Torque |
|---|---|
| 1 | ~33% of final |
| 2 | ~66% of final |
| 3 | 100% of final |

Always tighten the screw opposite the last one. After the first pair, move to the next
adjacent pair.

> **IMPORTANT**
>
> After all screws reach final torque, **a second person must check the torque values.**
> *(MX60 UG Rev B, pp.10–11)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide how the second-person torque verification is recorded.
>
> *Recommended practice:* a dated sign-off on the installation record, naming both people.
> Repeat after any disassembly.

## 6.3 Lever arms and the Vehicle Preset

**Good news, and it simplifies this considerably:**

> The lever arms of the standard system are set by default in the MX60 system. Only the
> vehicle height needs to be saved once as a preset.
> *(QSG Rev B, p.7)*

So for a standard system with no accessories, there is **one measurement**: installation
height.

You measure lever arms **only** when GAMS or DMI are fitted.

### Installation height

**How to measure:**

1. Ensure the roof rack is **horizontally aligned** *(MX60 UG Rev B, p.47)*
2. Locate the **External Reference Point** — right side, at the back of the rack
   *(MX60 UG Rev B, p.45)*
3. Measure **strictly vertically** from that point down to the road surface
4. Record in metres, as an absolute value
5. Enter in TMI under **Settings → Vehicle settings → Install Height**

**Accuracy required: on the order of 1 cm** *(MX60 UG Rev B, p.47)*.

> **CAUTION**
>
> Using incorrect or poor measurement values in the Vehicle Preset **may result in faulty
> navigation solutions.** Make sure all values are entered correctly, and make sure you
> select the correct Vehicle Preset before starting a mission.
> *(MX60 UG Rev B, p.47)*

> **FIELD TIP**
>
> Vehicle loading changes this measurement. The dust filter bulletin warns that a heavily
> loaded vehicle, or one with soft suspension, needs this considered when measuring
> installation height *(Dust Filter Bulletin, p.2)*. Measure the vehicle in the condition
> it will be driven in — fuel, gear, and people aboard.

### GAMS lever arm — only if fitted

Measured to the **L1 antenna phase centre** of the secondary antenna.

| Intended use | Accuracy | Baseline |
|---|---|---|
| Collection only | 10 cm or better | — |
| **Post-processing navigation data** | **A few millimetres** | **≥ 2.0 m** |

Both antennas must be the **same type** *(MX60 UG Rev B, p.68)*.

**The practical method** *(MX60 UG Rev B, p.68)*: measuring from the GAMS antenna all the
way to the External Reference Point is awkward. Instead, measure the short distance to the
**top-left front corner** of the rack, then add the known fixed offsets:

| Axis | Known offset, corner → ERP | Your measurement |
|---|---|---|
| X | +1.006 m | + your value |
| Y | −0.469 m | + your value |
| Z | +0.025 m | − your value |

> **CAUTION**
>
> Those known offsets are published for the **Trimble standard Roof Rack**. Do not apply
> them to the MX Shock Absorbing Mounting Rack. *(MX60 UG Rev B, p.68)*

> **IMPORTANT**
>
> GAMS offsets must be re-measured **every time** the antenna is re-installed for a new
> mission. If the Sensor Unit comes off the roof at the end of each day, so does GAMS —
> and its lever arm is measured again the next morning. *(MX60 UG Rev B, p.67)*

### DMI lever arm — only if fitted

Measured to the **centre of the tread**, where the DMI-equipped wheel contacts the road.

> **CAUTION**
>
> - The DMI wheel **must be a non-steering wheel**
> - Use the correct **sign**. A DMI mounted on the **left** wheel has a **negative Y**
>   lever arm
>
> *(MX60 UG Rev B, p.46)*

### The Vehicle Frame

All lever arms are measured in the Vehicle Frame:

| Axis | Positive direction |
|---|---|
| **X** | Forward, in the driving direction |
| **Y** | **Right** side of the vehicle |
| **Z** | **Downward** |

*(MX60 UG Rev B, p.46)*

> **WHY THIS MATTERS — Z is down**
>
> Surveyors expect Z up. This frame has Z **down**. Get this wrong and the sign of every
> vertical lever arm inverts.

> **ADVANCED — why POSPac shows different numbers than you measured**
>
> The origin of the MX60 System Reference Frame is **not** the External Reference Point.
> TMI adds internal vectors to the lever arms you enter. In POSPac processing you will see
> corrected lever arm values that differ from your mechanical measurements.
>
> **This is correct behaviour, not an error.** *(MX60 UG Rev B, p.47)*

> **PARAMETRIX DECISION REQUIRED**
>
> Establish who measures lever arms, by what method, where the record is kept, and when
> re-verification is required.
>
> *Recommended practice:* lever-arm measurement is a trained-personnel task with a written
> record — date, who measured, method, values, and vehicle condition. Re-verify whenever
> the Sensor Unit, GAMS, DMI, or rack is disturbed. Keep the record with the project data,
> because a trajectory problem months later is often a lever-arm problem.

## 6.4 Mounting the Sensor Unit

> **CAUTION**
>
> **Two people are required.** The Sensor Unit weighs 24–28 kg depending on
> configuration. Prepare the mount mechanism *before* lifting, to prevent injury or damage.
> Lift only by the dedicated handles.
> *(MX60 UG Rev B, pp.9, 10, 16; QSG Rev B, p.5)*

**To install:**

1. Confirm the rack's **safety locks are open**. Use the tool stored in the Control Unit
   case.
2. Two people, one on each side, lift the Sensor Unit by its handles.
3. Let the **lower mounting bolts slide into** the lower mounting facilities of the rack.
4. As the lower bolts reach their final position, **tilt the Sensor Unit forward** until
   the upper mounting bolts **click** into place and the fast lock engages.
5. Once the upper bolts have clicked, the unit is stable and cannot turn over or fall.
6. **Tighten the safety locks** to close the lock bars.
7. The unit is now safe to cable.

*(MX60 UG Rev B, pp.16–18)*

**To remove:**

1. Remove cables
2. Open the safety locks
3. Release the fast locks by pressing the fast-lock button downwards
4. Turn the Sensor Unit while pressing the button, and free the upper mounting bolts
5. Lift out of the lower mounting facilities and place directly into its transport case

*(MX60 UG Rev B, p.19)*

## 6.5 Cabling

Three cables. Each has a defined route.

| # | Cable | Length | Connects |
|---|---|---|---|
| 1 | Source-to-Power-Unit | 5 m | Vehicle power → Power Unit |
| 2 | Power-Unit-to-Control-Unit | 3 m | Power Unit → Control Unit (power **and** signal) |
| 3 | Control-Unit-to-Sensor-Unit | 5 m | Control Unit → Sensor Unit |

*(MX60 UG Rev B, pp.34–35)*

**Connecting cable 3 — the one that needs care:**

1. Check you are holding the **correct end** — each end uses a specific connector type
2. Check the pins are in good state — **not bent or broken**
3. Connect the "Sensor Unit" end to the Sensor Unit
4. Slide in and secure by **turning the black lock screw** on top of the connector to the
   right
5. Install and secure the cable safely relative to the vehicle
6. Connect the "Control Unit" end and secure its lock screw the same way

*(MX60 UG Rev B, p.35)*

**Grounding:** connect the ground terminal of the **Power Unit** and the **Sensor Unit**
to the vehicle chassis. All ground connections are the owner's responsibility and depend
on the vehicle *(MX60 UG Rev B, p.34; QSG Rev B, p.7)*.

> **CAUTION**
>
> Cables must be **fixed to the vehicle roof rack before being led inside the cabin**, and
> secured with straps or binders so nothing can move during operation.
> *(MX60 UG Rev B, pp.9, 44)*

> **WHY THIS MATTERS**
>
> An unsecured cable at 80 km/h chafes, and the connector pins are rated for 1500 mating
> cycles but nothing at all for being yanked *(MX60 UG Rev B, p.35)*. A cable failure
> mid-mission ends the mission.

## 6.6 Daily safety check

Trimble requires a safety check **before and after each mission**
*(MX60 UG Rev B, p.44)*.

### Rules

- All broken or damaged components **exchanged immediately**
- All loose screws tightened, to the correct torque, by the correct method
- Any dirty or wet part cleaned or dried
- **Do not start a mission before solving any issue you had previously with the system.
  Not doing this may damage the system permanently.**

*(MX60 UG Rev B, p.44)*

### Components checklist

Trimble's own list, verbatim in substance *(MX60 UG Rev B, p.44)*:

| ☐ | Check |
|---|---|
| ☐ | Roof rack installed correctly |
| ☐ | All roof rack screws tightened |
| ☐ | Roof rack shows no cracks or deformation |
| ☐ | Sensor Unit damage-free — no scratches or deformation |
| ☐ | **All camera lenses clean and undamaged** |
| ☐ | Sensor in operation position and **properly locked** |
| ☐ | Control Unit free of damage or broken parts |
| ☐ | Control Unit installed correctly and secured |
| ☐ | Power Unit damage-free, no broken parts |
| ☐ | Power Unit secured, **air inlet and outlet free** |
| ☐ | All connectors plugged in and fixed |
| ☐ | Cables fixed to the roof rack before entering the cabin |
| ☐ | No cable damaged or liable to be damaged during operation |
| ☐ | User interface device operational |

### Cleaning the optics

Clean all sensor optics **before starting a mission**. Depending on weather and road
surface, cleaning **during** the mission may be necessary *(MX60 UG Rev B, p.10)*.

**Correct method** *(MX60 UG Rev B, p.50)*:

1. Work in a clean environment
2. First try to **blow debris off with an air compressor**
3. If that fails, apply a small amount of optics cleaner or ethyl alcohol to a clean lens
   cloth — **moist, not dripping**
4. Wipe along the length of the glass in smooth movements
5. **Do not press hard, and do not rub repeatedly on one spot**
6. If pooling or streaks appear, there is too much solution — wait for it to dry, repeat
7. Examine the surface in good light; repeat with a clean cloth if dust spots remain

> **FIELD TIP**
>
> Carry the cleaning kit in the vehicle, not the office. Road spray and insects are a
> mid-mission problem, and imagery with a dirty lens is grounds for rejection
> *(TMR MLS Guideline §10, p.15)*.

## 6.7 Before you leave the office

From Trimble's own checklist *(QSG Rev B, p.14)*:

| ☐ | Item |
|---|---|
| ☐ | System checked — mechanical, mounting, screws, torques |
| ☐ | System settings checked — lever arms, sensor settings |
| ☐ | Field protocol prepared |
| ☐ | SSDs prepared and available |
| ☐ | Satellite almanac checked |

Plus, from elsewhere in the Trimble documentation:

| ☐ | Item | Source |
|---|---|---|
| ☐ | **24 hours acclimatisation** completed, if the system has been air freighted | UG p.7 |
| ☐ | Wi-Fi country code set — **mandatory** before first use and in any new country | UG p.48; QSG p.2 |
| ☐ | Wi-Fi password sticker accessible | UG p.37 |
| ☐ | Cleaning kit aboard | UG p.10 |
| ☐ | System exercised recently — if idle >2 months, run 30–60 min | UG p.9 |

> **CAUTION — acclimatisation**
>
> After air freight transportation, allow **24 hours** in a place with constant
> temperature and air pressure before switching the system on. Condensation inside the
> housings can cause short circuits and damage the instrument when switched on.
> *(MX60 UG Rev B, p.7; QSG Rev B, p.2)*

> **PARAMETRIX DECISION REQUIRED**
>
> Create a standard Parametrix field protocol form. Trimble requires that it record the
> **order of runs, direction of runs, date, mission, and system serial number**
> *(QSG Rev B, p.14)*.
>
> *Recommended practice:* build a single-page form capturing Trimble's required fields
> plus operator name, vehicle, weather, installation height used, Vehicle Preset name,
> initialization location and time, and any events during collection. Store it with the
> project data.

---

## References — Section 6

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7–11, 16–19, 23, 28–29, 31–35, 37, 44–48, 50, 52, 59, 61–62, 67–68 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 2, 4–7, 14 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 2 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §10, p.15 |
