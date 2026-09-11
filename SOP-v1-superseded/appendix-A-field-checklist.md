# APPENDIX A — MX60 FIELD CHECKLIST

Quick reference. Print double-sided and keep it in the vehicle.
Full detail is in the section noted against each block.

---

## A1. Before leaving the office — §5, §6

| ☐ | Item |
|---|---|
| ☐ | Route, pass count and direction planned per pass |
| ☐ | **Satellite almanac checked** — `gnssplanning.com/#/charts` |
| ☐ | Two initialization locations identified — open sky, both ends of the job |
| ☐ | GNSS-hostile stretches mapped; strategy for each |
| ☐ | Weather checked; stand-down criteria understood |
| ☐ | Vehicle height clearances checked on route |
| ☐ | Mechanical check — mounting, screws, torques |
| ☐ | System settings checked — lever arms, sensor settings |
| ☐ | **SSDs prepared** and field protocol printed |
| ☐ | Cleaning kit aboard |
| ☐ | Wi-Fi password sticker accessible |
| ☐ | If air-freighted: **24 h acclimatisation complete** |
| ☐ | If idle > 2 months: run 30–60 min beforehand |

---

## A2. Safety check — before AND after every mission — §6

**Rules:** replace damaged parts immediately · tighten loose screws to correct torque ·
clean or dry anything dirty or wet · **do not start a mission with an unresolved issue**

| ☐ | Check |
|---|---|
| ☐ | Roof rack installed correctly; all screws tight |
| ☐ | Roof rack shows no cracks or deformation |
| ☐ | Sensor Unit damage-free — no scratches or deformation |
| ☐ | **All camera lenses clean and undamaged** |
| ☐ | Sensor in operation position and **properly locked** |
| ☐ | Control Unit undamaged, installed correctly, secured |
| ☐ | Power Unit undamaged, secured, **vents clear** |
| ☐ | All connectors plugged in and fixed |
| ☐ | Cables fixed to roof rack before entering the cabin |
| ☐ | No cable damaged or liable to be damaged |
| ☐ | Operator device working |

---

## A3. Power up — §7

**Order matters — 25 A startup surge**

1. ☐ Engine **auto start/stop OFF**
2. ☐ Both SSDs inserted and **locked**
3. ☐ **Start the vehicle**
4. ☐ Hold Control Unit power button **≥ 15 seconds**
5. ☐ Power Unit LED **constant green**
6. ☐ SU + CU LEDs blink ~10 s → **solid green**

| LED | Meaning |
|---|---|
| Blinking green | Starting / updating / shutting down |
| **Solid green** | Ready |
| **Blinking red** | **Failed — do not start a mission** |

7. ☐ Connect tablet → Chrome → `http://tmi.mx-scan.net`
8. ☐ Wi-Fi country set (first use / new country)

---

## A4. System health before initializing — §7

| ☐ | Check |
|---|---|
| ☐ | Disk check complete — **no Warning or Error icon** |
| ☐ | Correct **Vehicle Preset** — install height matches this vehicle today |
| ☐ | **DMI / GAMS checkboxes ACTIVATED** if fitted |
| ☐ | Correct **Capture Preset** selected |
| ☐ | Camera and Laser buttons **green** |
| ☐ | UTC time showing |
| ☐ | Vehicle parked in open sky |

> **An unactivated DMI or GAMS logs nothing.** Fitted, measured and connected is not
> enough — the checkbox must be ticked.

---

## A5. Initialization — §8

1. ☐ Parked **open sky**, good PDOP, clear of buildings
2. ☐ Mission started — name, area, presets confirmed
3. ☐ **STILL for 2–3 minutes**
4. ☐ Blue arrow visible; UTC time showing
5. ☐ **Drive straight ~20 m** → NAV **red → orange**
6. ☐ **Vary speed + 2–3 dynamic turns** → NAV **orange → green**
   Example: `0 → 50 → 20 → 50 → 20 km/h`
7. ☐ All parameters green in Nav View
8. ☐ **Wait — up to 10 more minutes** before logging
9. ☐ Initialization time and location recorded

| NAV | Meaning | Record? |
|---|---|---|
| **Red** | No valid solution | **Blocked** |
| **Orange** | Solution exists | Permitted — but not for survey grade |
| **Green** | Meets accuracy figures | **Yes** |

---

## A6. During collection — §9

**Press Record** — green → red. **Stop** — red → green.
Record button controls **laser and imagery only**; navigation logs continuously.

**Speed: 80 km/h (50 mph) recommended max · 110 km/h absolute max**
Drive smoothly — no harsh acceleration, braking or steering.

### Monitor in a loop

| Watch | Good | Act if |
|---|---|---|
| **NAV** | Green | Orange — note it · **Red — recording blocked** |
| **Camera / Laser** | Green | Orange or **red** |
| **Record** | **Red on a run** | Green when you think you're recording |
| **Thick blue line** | Over every collected stretch | Missing where you drove a run |
| **SSD fill** | Space remaining | Approaching full |
| **UTC time** | Displayed | Missing |
| **Disk icons** | None | Warning / Error appears |
| **Audible alarm** | Silent | **Battery Protect — 78 s to restore charge** |

☐ Use **Comments** to time-tag events into the mission database
☐ **Minimum mission time: 30 minutes**

**Need different capture settings?** Use **mission re-configuration** — do NOT close the
mission. No re-initialization needed.

---

## A7. Ending the mission — §10

1. ☐ Stop recording the final run
2. ☐ Drive to an initialization point, dynamic manoeuvres on the way
3. ☐ **FINALIZE SEQUENCE — mirror of the start:**
   a. ☐ Dynamic steering manoeuvres
   b. ☐ Vary speed — accelerate / decelerate
   c. ☐ Drive straight
   d. ☐ **STILL for 2–3 minutes**
4. ☐ **Review the map — thick blue line over every intended stretch**
5. ☐ Close mission → **Complete Mission**
6. ☐ Shut down → **Shutdown**
7. ☐ Wait for power button light **OUT** — up to 90 s
8. ☐ Field protocol complete — runs, directions, date, mission, system S/N
9. ☐ Post-mission safety check (A2)

> **Never power off by removing power.** Use Complete Mission AND Shutdown, or risk
> corrupted data.

> **Do the map review before closing.** If a run is missing and you're still on site and
> initialized, you can re-drive it. Ten minutes later you cannot.

---

## A8. Data handling — §11

| ☐ | Step |
|---|---|
| ☐ | System fully shut down before removing disks |
| ☐ | **Unlock and remove BOTH SSDs** — they are one dataset |
| ☐ | Offload via Data Carrier Docks, USB 3 (use both — halves the wait) |
| ☐ | **Verify:** navigation data · both lasers · panoramic · back-down camera · Mission Report · logs |
| ☐ | File count and size match source |
| ☐ | **Back up before any processing** |
| ☐ | **Only then** prepare SSDs for the next mission |

> **Never connect USB while a disk is in the Control Unit.** Remove it first.

> **Never delete raw mission data** because processing succeeded or the deliverable shipped.

---

## A9. Stop-work triggers

| Situation | Action |
|---|---|
| **Blinking red LED** | Do not start / stop the mission |
| **Disk Error icon** | Do not run a production mission |
| **Battery Protect alarm** | Restore charge within 78 s or power cuts |
| **NAV red across a material extent** | Nothing is recording — fix before continuing |
| **Rain or mist** | Trimble says avoid operating |
| **Unresolved fault from a previous mission** | Do not start |

---

## A10. Support — §14

**`mx_support@trimble.com`** · Americas **+1-289-695-4416**

Provide: problem description · workflow to reproduce · mission location and conditions ·
**system log file** · serial number · total operating hours · photos or video

Log file: auto-saved to **removable Disk 1 during shutdown**, or TMI.AI → Log Download.

> Granting remote access makes **all data on the system visible to Trimble Support**.
> Remove confidential data first.

---

*Sources: MX60 User Guide Rev B (May 2025) · MX60 Quick Start Guide Rev B (March 2025) ·
TMI Software User Guide Rev L (April 2026) · Dust Filter Bulletin (January 2025).
Page-level citations are in the numbered sections.*
