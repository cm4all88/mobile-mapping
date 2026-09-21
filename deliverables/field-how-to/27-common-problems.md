# 27. Common Problems — What to Check First

## 27.1 Troubleshooting pattern

When something is wrong, do not start changing settings at random.

1. **Name what you actually see.** A color, missing device, alarm, status or screen message is more
   useful than "the MX60 is not working."
2. **Return to the last known good state.** Check power, connections, TMI connection, Vehicle
   Settings and the current mission before changing anything else.
3. **Change one thing at a time.** If three things are changed together, you do not know what fixed
   the problem or what new problem was introduced.
4. **Record the abnormal condition.** Use a TMI comment where appropriate and put the event in the
   field record.
5. **Stop when data integrity is uncertain.** A run that looks complete but was collected with a
   missing sensor, failed initialization or interrupted closing sequence is not made safer by
   continuing to drive.

## 27.2 Symptom table

| What you see | Check first | If that is not it | Stop, re-drive or raise when |
|---|---|---|---|
| **TMI will not load** | Confirm the Control Unit is fully started and the field device is on its network | Enter **`http://tmi.mx-scan.net`** exactly, use Chrome, then repeat §9 from the beginning | You cannot establish a stable TMI connection; do not invent an IP/SSID or change system networking from memory |
| **System will not start** | Power button held **15 s**? Supply live? Battery healthy? | §6, then §8 | Power or Control Unit status is uncertain |
| **LEDs blink and do not settle** | Allow for a firmware update, which can take **up to 6 minutes** | Compare the LED condition with §8.2 | The condition persists beyond the documented startup behavior |
| **A sensor is missing from the device list** | Compare the list with the confirmed system configuration, then check cable and power to that sensor | Restart only by the documented sequence in §8 and re-check §9.3 | **Stop. Do not collect with a required sensor missing** |
| **A fitted DMI or GAMS logs nothing** | Is it activated in Vehicle Settings? | Verify the installed configuration against §10.1 | The sensor is expected for the mission and still does not log |
| **Navigation will not reach green** | Ask TMI which parameter is holding it | Heading: drive more dynamic manoeuvres. Position: move to better sky view | Initialization does not converge before meaningful collection |
| **Status is stuck on heading** | Dynamic manoeuvres and whether GAMS is available | More turns and speed changes per §14.3 | Heading quality does not recover |
| **Status is stuck on position** | Sky view | Move the vehicle. Waiting in the same blocked location will not help | Position quality does not recover |
| **Status goes orange mid-corridor** | Identify the location and likely obstruction | Record it, maintain planned overlap and use §17 | The degraded section cannot be covered defensibly or the guide calls for re-drive |
| **Audible alarm** | **Battery Protect** | Restore charge immediately, then follow §7 | Power stability is not restored |
| **Power cut mid-run** | Treat the run as ended | Record the event and use §24 | The run has no valid closing sequence. Make the re-drive decision now |
| **Storage is filling faster than expected** | Remaining free space and expected run duration | End the run cleanly before the disk fills if needed | Continuing risks an interrupted run or missing closing sequence |
| **Capture settings look different from the guide** | Confirm TMI version and which presentation is shown | Record what you see and compare §10.2 | A required setting cannot be positively identified |
| **Cannot find 2000 kHz on screen** | Remember 2000 kHz is the system total | TMI uses per-scanner 500/1000 kHz values; see §10.2 | The actual configured rate still cannot be verified |
| **Imagery looks wrong on screen** | Rain, dust, insects or smear on optics | Clean the optics and inspect again | The affected stretch was collected with unusable imagery and imagery is required |
| **A planned pass was skipped** | Record exactly which pass and why | Use §24 before leaving | Missing overlap or coverage removes an office remedy |
| **A run was stopped accidentally but the mission is still open** | Confirm the mission itself remains open | Record the interruption, leave the mission open, and start a new run when ready (§20) | Coverage or overlap was lost; use §24 before leaving |
| **Mission was closed before the closing sequence** | A closed mission cannot be appended to | Record it; any new mission needs its own initialization and closing sequence (§20.4) | Use §24 — a missing mission closing sequence is not repaired by starting another mission |
| **Transfer copy looks incomplete** | Compare file count and total size with the source | Confirm the `.mxdb` opens and `POS_1/raw/` is present and non-empty; use SOP §11.2 | **Do not clear the field disk** until verification is complete |
| **Unsure whether to re-drive** | Use the actual missing or abnormal condition, not the schedule | §24 | If you cannot explain why the existing data is adequate, raise it before leaving site |

## 27.3 When the answer is "ask"

**Stop and ask rather than improvising on the vehicle.** You may always stand down, record a
comment, or re-drive while you are still on site (§1.4).

Escalation is the correct result when the guide reaches the end of its troubleshooting path. The
guide is supposed to help a minimally experienced MX60 operator recognize that point; it is not
supposed to make them invent a new field procedure.
