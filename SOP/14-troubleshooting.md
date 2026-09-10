# 14. TROUBLESHOOTING

Look up the symptom. Everything here traces to a Trimble source.

> **CAUTION — the overriding rule**
>
> "Do not start a mission before solving any issue you may have had previously with the
> system. **Not doing this may damage the system permanently.**"
> *(MX60 UG Rev B, p.44)*

## 14.1 Power and startup

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Nothing happens on power button press | Held < 15 s | Hold **at least 15 seconds** | Yes | — | No | UG p.21 |
| Power Unit LED not green | Vehicle not supplying 12 V; engine off | Start the vehicle; check source cable and fuses | Not until resolved | Check 35 A fuse, relay, battery | No | UG pp.25, 62; QSG p.8 |
| **Audible alarm during mission** | **Battery Protect — below 10.5 V for >12 s** | **Restore charge immediately. Power cuts after 90 s.** Recovers if voltage rises above 12.0 V within that window | Only if voltage recovers | Check alternator, battery, buffer battery | If power was cut mid-run | UG p.27 |
| System cut out with no warning | Battery Protect cutoff, or a tripped breaker | Check circuit breakers under the Control Unit fuse cover | After resolving | **Check all cables before restarting — the trip may have been a damaged cable** | Yes, for the affected run | UG pp.21, 27 |
| Blinking red LED | Component failed | **Do not start a mission** | No | Contact Trimble Support with log file and serial number | — | UG pp.21, 51 |
| LEDs blink far longer than ~10 s | Startup or update in progress | Wait | — | — | No | UG p.21; QSG p.8 |
| System does not power up after air freight | Possibly powered on before acclimatisation | **Do not retry.** Allow 24 h at constant temperature and pressure | No | Contact Trimble Support | — | UG p.7 |

## 14.2 Connection and TMI

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| System Wi-Fi not visible | System not fully booted; Wi-Fi stick issue | Wait for solid green LEDs; check Wi-Fi USB stick 1 seated | Yes once visible | — | No | UG pp.21, 37 |
| Wi-Fi password rejected / lost | Password is unique and unchangeable | Use the sticker in the Control Unit top case | — | **Contact Trimble Imaging Support with the serial number** | No | TMI p.51; UG p.37 |
| TMI page will not load | Wrong browser; wrong address; no connection | Use **Google Chrome**; `http://tmi.mx-scan.net`; check LAN/Wi-Fi | Yes | — | No | TMI p.7 |
| Ethernet connected but no access | Static IP set on the device | Set to obtain IP **and DNS** automatically (DHCP) | Yes | — | No | UG p.36; TMI p.5 |
| No background map | No Internet connection | Optional — the map is cosmetic. Check WAN or Wi-Fi stick 2 | **Yes** | — | No | TMI pp.8, 32 |
| Cannot connect system to a hotspot | Hotspot requires web-page login | Use a different network — this is not supported | Yes | — | No | TMI p.51 |
| Wi-Fi behaving oddly in a new country | **Country code not set** | `System Administration → WiFi → MX60 WiFi Access Point → country` | Not until set — legal requirement | — | No | TMI pp.5, 51; UG p.48 |

## 14.3 Disks and storage

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| **Start Mission button greyed out** | **Disk check still running** (Initializing/Analyzing) | **Wait for it to finish** | Yes, once complete | — | No | TMI p.38 |
| Disk **Warning** icon | Disk degraded | Mission can run, but **data loss may occur under high system load** | Risk decision | Replace or reformat the disk | No | TMI pp.33–34 |
| Disk **Error** icon | Disk performance compromised | **Do not start a production mission.** Requires confirmation to proceed | No | Replace the disk | If a mission was run on it | TMI pp.33–34 |
| SSD filling during mission | Long mission, high capture rates | Monitor fill status top-right of the map window | Until full | Consider lateral range limit or lower rates next time | If the disk filled mid-run | TMI p.33 |
| Disk not recognised in Data Carrier Dock | Not locked in | Insert, **lock with key, turn 90° clockwise**, then power on | — | — | No | UG p.24 |

> **CAUTION**
>
> **Never connect the USB cable while a data disk is inside the Control Unit.** Remove the
> disk first. *(MX60 UG Rev B, p.10)*

## 14.4 Navigation and initialization

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| **NAV stays red** | No valid solution — poor sky, obstruction, multipath | Move to genuinely open sky. Check the skyplot in Nav View | **No — recording is blocked at red** | — | No | TMI pp.9, 40 |
| NAV reaches orange, will not go green | Attitude/heading not converged | More dynamic manoeuvres — vary speed, 2–3 turns | Recording is permitted, but see §7.3 | Review trajectory quality | Possibly | QSG p.12; TMI p.25 |
| Takes far longer than usual to initialize | Poor constellation; site worse than it looks | Check almanac; relocate; allow the full settling period | Yes | — | No | QSG pp.12, 14 |
| NAV drops green → orange mid-run | Passing obstruction, degraded geometry | Note location using **Comments**. Return to open sky if it persists | Yes, but flag the stretch | Check trajectory over that stretch against check points | Possibly | TMI pp.9, 36 |
| NAV green but position looks wrong on map | Background map offset, or genuine position error | Compare trajectory to the road on the map | Investigate | Verify against control | Possibly | TMI p.33 |
| No blue arrow on the map | No valid position yet | Wait; check sky visibility | No | — | No | TMI p.40 |
| UTC time not displayed | GNSS initialization not complete | Wait; improve sky visibility | No | — | No | TMI p.33 |
| Trajectory recorded but **DMI/GAMS data missing** | **Aiding sensor not activated in Vehicle Settings** | Cannot be fixed retrospectively | — | Verify the checkbox before every mission | Depends on reliance on that sensor | TMI p.21 |

> **IMPORTANT**
>
> The last row is a silent failure. The sensor can be fitted, measured, and connected
> correctly and still log nothing because a checkbox is off. Nothing in the field indicates
> it. Make the checkbox part of the pre-mission check.

## 14.5 Laser

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Laser button **red** | Device error | Check connections; restart if necessary | No | Log file to Trimble Support | Yes, for affected extent | TMI p.9 |
| Laser button **orange** persistently | Not time-synchronized | Wait; if it persists, restart the mission | Not for quality work | — | Possibly | TMI p.9 |
| **Waterfall view shows gaps near the ground** | **Dust filter enabled with wrong installation height** — the mask reaches the ground | Correct install height in Vehicle Settings; reconfigure mission | After correction | — | Yes, for affected extent | Dust Filter Bulletin pp.2–3; TMI p.29 |
| Cloud missing beyond a set distance | **Lateral range limit** enabled | Check Capture Settings — 5–50 m limit discards points beyond it **permanently** | Yes | Cannot be recovered | Yes, if far-field data was required | TMI p.29 |
| Sparse cloud | Speed too high, or low measurement rate | Reduce speed; select a higher laser mode | Yes | — | If density is insufficient | UG p.53; TMR §9.4.1 |
| Excessive noise | Rain, mist, dust, spray | **Avoid operating in rainy or misty weather.** Consider the dust filter *only* on unpaved roads | Judgement call | Cleansing — reclassify, do not delete | Likely | UG p.49; TMR §11.8.1 |
| No returns from wet pavement | Water absorbs / reflects away | Do not collect wet surfaces | No | — | Yes | TMR §9.1 |

## 14.6 Cameras

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Camera button **red** | Device error | Check connections; restart | No | Log file to Trimble Support | Yes, if imagery is a deliverable | TMI p.9 |
| Camera button **orange** | Not time-synchronized | Wait for green before recording | Not for quality work | — | Possibly | TMI p.9 |
| Images too dark or too bright | Exposure | Adjust in Camera View — **Auto** or the slider | Yes | — | If unusable | TMI pp.34–35 |
| Hazy or spotted images | Dirty lens | Clean per the correct method — air first, then optics cleaner on a moist cloth | Yes after cleaning | — | For the affected extent | UG p.50 |
| Water droplets on images | Wet conditions | Stand down — **water on the lens is grounds for rejection** | No | — | Yes | TMR §10 |
| Blown highlights, deep shadow | Low sun angle | Collect between **8am and 4pm** | Judgement call | — | If unusable | TMR §10 |
| Pavement imagery out of focus | Vehicle roof height below 1.60 m | Back-down camera is sharp only from **2.0 to 9.0 m** | — | Vehicle does not meet requirements | Yes | UG pp.54, 59 |

## 14.7 Mission and shutdown

| Symptom | Likely cause | Field action | Continue? | Office follow-up | Recollect? | Reference |
|---|---|---|---|---|---|---|
| Record button will not turn red | **NAV is red** — recording blocked | Complete initialization | No | — | No | TMI p.40 |
| Thick blue line missing where a run was driven | The run was not recording | **Re-drive it now, while still on site and initialized** | Yes | — | Yes if not caught on site | TMI p.33 |
| Need different capture settings mid-corridor | — | Use **mission re-configuration** — do **not** close the mission | Yes | — | No | TMI p.41 |
| Closed the mission by mistake | Navigation logging stops immediately on close | Start a new mission — **full re-initialization required** | Yes after re-init | Two missions to process | No | TMI pp.31, 42 |
| Mission shorter than 30 minutes | Below Trimble's stated minimum | Extend the mission before closing | — | Flag in the survey report | Possibly | QSG pp.13–14 |
| Power removed without shutdown | Improper shutdown | — | — | **Verify data integrity carefully — corruption is possible** | If data is corrupt | TMI p.31 |
| Control Unit light still on after shutdown | Shutdown in progress | **Wait up to 90 seconds** | — | — | No | QSG p.13 |
| Web client unresponsive after shutdown | Expected | Reload the web client | Yes | — | No | TMI p.43 |

## 14.8 Escalating to Trimble

**Support contacts** *(MX60 UG Rev B, p.51; TMI UG Rev L, p.55)*:

| | |
|---|---|
| Email | `mx_support@trimble.com` |
| Americas | +1-289-695-4416 |
| APAC | +86-105-603-4179 |
| Europe & Rest of World | +49-7351-474-0237 |

**Provide** *(MX60 UG Rev B, p.51)*:

| ☐ | Item |
|---|---|
| ☐ | Short description of the problem |
| ☐ | The workflow used, and how to reproduce it |
| ☐ | Mission location and environmental conditions, if it occurred during a mission |
| ☐ | **System log file** |
| ☐ | Serial number |
| ☐ | Total operating hours since purchase |
| ☐ | Photos or video |

**Where to get the log file:**

- A system log is written automatically to **removable Disk 1 during shutdown**
  *(TMI UG Rev L, p.43)*
- Or download from **TMI.AI → Log Download** *(TMI UG Rev L, p.50)*
- **System Information Export** generates a further file Support may request
  *(TMI UG Rev L, p.54)*

**Remote support:**

> **CAUTION**
>
> "When remote control of the system is given to Trimble Support, be aware **all data on
> the system are visible** to Trimble Support. If there are confidential data on the
> internal disk, please remove them from the system before granting remote access."
> *(TMI UG Rev L, p.54)*

Remote access requires the system to be connected to a wireless network with Internet
access *(TMI UG Rev L, p.53)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Define the escalation path when an operator hits a problem in the field, and who may
> authorise granting Trimble remote access to the system.
>
> *Recommended practice:* the operator contacts the survey technology group owner first,
> who decides whether to contact Trimble. Remote access requires that owner's approval,
> after confirming no client-confidential data is on the system.

## 14.9 Firmware and licence

| Task | Procedure | Reference |
|---|---|---|
| **Firmware update** | Copy the `.tmx.install` file to a USB stick → USB1 on the Control Unit → TMI.AI → Firmware Update → Refresh → Install. System shuts down; **wait until all Control Unit LEDs are off**, then power back on. **Powering on may take up to 6 minutes** while the update completes | TMI p.49 |
| **Licence update** | Copy the licence file to a USB stick → USB1 → TMI.AI → License → Import | TMI p.53 |
| **Calibration import** | Copy the boresight JSON to a USB stick → USB1 → Settings → Calibration Import | TMI p.18 |

> **CAUTION**
>
> Do not attempt a firmware update immediately before a collection. The process requires a
> full shutdown and a power-on that may take six minutes, and a failed update leaves you
> with no system.

---

## References — Section 14

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7, 10, 21, 24–25, 27, 36–37, 44, 48–51, 53–54, 59, 62 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 5, 7–9, 18, 21, 25, 29, 31–38, 40–43, 49–55 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 8, 12–14 |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 2–3 |

## Other References — Section 14

| Source | Sections |
|---|---|
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §9.1 p.11; §9.4.1 p.12; §10 p.15; §11.8.1 p.19 |
