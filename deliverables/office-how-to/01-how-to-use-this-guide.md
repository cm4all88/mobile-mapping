# 1. How to Use This Guide

## 1.1 The four questions

Every section answers the same four questions, in the same order. If you read nothing else in a
section, read **Stop if**.

| | |
|---|---|
| **Do** | The clicks, in order |
| **Look at** | What to inspect once you have done it — not "check it worked", but where to point your eyes |
| **Expect** | What normal looks like, so you can tell when it isn't |
| **Stop if** | What means you do not proceed. **These are not suggestions.** Stopping costs an hour; not stopping has cost a remobilisation |

## 1.2 The order

The guide follows the processing sequence. §2 to §12 get you from a disk to a point cloud you can
look at. §13 to §21 register it. §22 to §26 check it and fix what is fixable. §27 to §34 identify,
export, record and archive it. §35 is what to check when something is wrong.

**You will not use every section on every job.** Calibration (§13) is periodic. LiDAR QC (§24),
degraded-GNSS remedies (§25) and PFIX (§26) apply only when the trajectory needs them.

## 1.3 Three things to know before you start

These are the mistakes that cost the most, and all three are silent. The explanation for each is in
the Technical Manual at the reference given.

| | | |
|---|---|---|
| 1 | **Registration does not change the point cloud.** Until you run **Update Scans**, the cloud is the unregistered one — and it exports perfectly happily | §19 |
| 2 | **A good RMS does not prove the work succeeded.** A bad one proves it failed. Trimble says this in identical words in two places | §23 |
| 3 | **Cleanup cannot be undone** | §28 |

## 1.4 When a section says a decision is open

A **PARAMETRIX DECISION REQUIRED** marker means the SOP identifies a requirement whose answer is
not set. You still have to do something today. Where this guide suggests what, it is marked as a
suggestion and it is not a Parametrix standard.

## 1.5 Record as you go

Several sections end with **Record**. Those entries are the SOP's required records (SOP Appendix
B), and five of them have **no software artefact behind them** — if you do not write them down at
the time, nothing else will.

Templates are in **Appendix F**.
