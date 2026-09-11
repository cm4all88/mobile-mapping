# 26. What Must Accompany the Data

## 26.1 The field record

**[PROPOSED · SOP §9.6 · D-49]** — what the record contains is not yet decided.

**No software produces it.** That part is a fact, not a proposal: it is the only record of
everything the software cannot see, and the office depends on it.

Recorded **at the time**, per mission:

| | |
|---|---|
| Date, operator, vehicle, mission ID | |
| **Capture settings used** — and which presentation you saw (§10.2) | |
| Initialization location and time | |
| **Time green was reached, and time significant recording began** | The settling time (§14.5) |
| Each run — start, end, any incident | |
| **GNSS conditions observed**, per hostile stretch | Entry/exit times, whether overlap was driven |
| Weather | |
| Traffic and occlusion events | |
| **Anything not collected, and why** | |
| **Closing sequence performed** — and the time | |
| Disk and free space at end | |
| Any re-drive decision, and its reason | §24 |

Template: **Appendix C**.

## 26.2 Why each of the hard ones matters

| | |
|---|---|
| **Conditions and occlusion** | Nothing in the software knows a truck was there |
| **What was not collected, and why** | Otherwise the office cannot tell a gap from a decision |
| **The settling time** | It is the only evidence §14.2 was respected |
| **Closing sequence performed** | The office looks for it, and cannot tell from the data alone |

## 26.3 With the data

| ☐ | |
|---|---|
| ☐ | The complete mission folder (§25.2) |
| ☐ | The field record |
| ☐ | Base station data, if a local base was occupied |
| ☐ | Deviations from the mission plan, with reasons |

## 26.4 The test

**Could somebody who was not there work out what happened on this corridor, three weeks from now,
from what you are handing over?**

If not, the missing piece is in the field record.
