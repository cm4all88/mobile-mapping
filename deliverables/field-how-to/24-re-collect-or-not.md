# 24. Re-collect or Not

## 24.1 The rule of thumb

**On site, a re-drive costs twenty minutes. From the office, it costs a mobilisation.**

So the bar for re-driving **while you are still here** is much lower than it feels.

## 24.2 Re-drive now

| | |
|---|---|
| A run ended unexpectedly — power cut, disk, sensor fault | It has no closing sequence, and may be incomplete |
| A sensor was down for part of a run | You will not know what is missing until the office opens it |
| A planned pass was not driven | |
| **Planned overlap was not collected** | Removes LiDAR QC and run-to-run for that stretch |
| Navigation status was orange or red for a significant stretch | §14.4 |
| Occlusion spoiled a stretch you cannot re-drive later | |

## 24.3 Cannot be fixed by re-driving

| | |
|---|---|
| A mission with no closing sequence | **A new mission is a new trajectory.** Re-drive the whole mission, or accept it |
| Weak initialization | The same — it is per-mission |
| A GNSS outage longer than the published envelope | Not a driving problem. Record it and raise it (§17.4) |

## 24.4 If you decide not to re-drive

**Record the decision and the reason.** The office needs to know it was a decision and not an
oversight.

## 24.5 If the segment cannot be served at all

Where no amount of re-driving will produce an acceptable result, the honest finding is that
**mobile mapping may not be the appropriate acquisition method for that segment**. Record it and
raise it — that is a project decision, not yours to absorb.

> **PARAMETRIX DECISION REQUIRED · D-34** — who decides, against what, and what the client is told
> *(SOP §21.5)*.
