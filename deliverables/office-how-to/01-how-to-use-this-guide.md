# 1. How to Use This Guide

This is the operating path for a survey employee who understands survey office work but may have
little MX60 specific processing experience. The goal is not to teach survey theory. The goal is to
let the processor follow the MX60 workflow, recognize when the result is not normal, troubleshoot
the common causes, and stop before a bad state is carried into the next step.

## 1.1 The four questions

Every section answers the same four questions, in the same order. If you read nothing else in a
section, read **Stop if**.

| | |
|---|---|
| **Do** | The clicks, in order |
| **Look at** | What to inspect once you have done it — not "check it worked", but where to point your eyes |
| **Expect** | What normal looks like, so you can tell when it isn't |
| **Stop if** | What means you do not proceed. **These are not suggestions.** Stopping costs an hour; not stopping has cost a remobilisation |

**Each of the four is numbered** — §16.1 *Do*, §16.5 *Stop if* — because "Stop if" appears in
every section and is not an address on its own. Cite the number when you report a problem with
this guide: **Office How To §16.5**, not "the stop-if in registration".

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

## 1.4 Who is telling you — the authority key

**This guide cannot require anything.** Everything in it is somebody else's instruction, and the
marker says whose. That matters because the two are not the same: a Parametrix practice is a
recommendation, while **a Trimble instruction and an equipment limit bind regardless.**

| Marker | Who says so | Force today |
|---|---|---|
| **[TRIMBLE]** | Trimble states it as a requirement, in the cited topic or manual page | **Binding.** Does not wait on a Parametrix decision |
| **[TRIMBLE METHOD]** | Trimble documents the method, but does not state it as a requirement | **Strong advice.** The method is Trimble's; the obligation is not |
| **[EQUIPMENT]** | A hardware limit or an irreversible software operation | **Binding.** It is a fact about the tool |
| **[SOP §n]** | A Parametrix requirement, at that clause | As strong as that clause — check its state |
| **[PROPOSED]** | Recommended by this project | **Not company policy.** Do it unless told otherwise, and record it if you do not |
| **[TESTING · Tn]** | Depends on a result nobody has yet | An interim posture, not a rule |
| **[DECISION · D-n]** | Parametrix has not decided | **Raise it.** Do not improvise a standing rule |

> **[TRIMBLE] and [TRIMBLE METHOD] are not the same thing.** Where Trimble states a rule —
> *"A visual check is needed"* — the marker is **[TRIMBLE]**. Where it documents a way of working
> without making it mandatory, the marker is **[TRIMBLE METHOD]**. This guide does not promote the
> second into the first.

> **This is why §1.1 says "Stop if" is not a suggestion.** A *Stop if* whose authority is
> **[TRIMBLE]** or **[EQUIPMENT]** is not negotiable today. A *Stop if* marked **[PROPOSED]** is
> this project's recommendation — you may proceed past it, and if you do, **record that you did
> and why.** Either way the instruction stays direct, because a hedged instruction gets ignored.

## 1.5 When a section says a decision is open

A **PARAMETRIX DECISION REQUIRED** marker means the SOP identifies a requirement whose answer is
not set. You still have to do something today. Where this guide suggests what, it is marked as a
suggestion and it is not a Parametrix standard.

## 1.6 Record as you go

Several sections end with **Record**. Those entries are the SOP's required records (SOP Appendix
B), and five of them have **no software artefact behind them** — if you do not write them down at
the time, nothing else will.

Templates are in **Appendix F**.

## 1.7 First supervised processing job

For a processor with minimal MX60 experience, use the guide in workflow order:

1. Intake and identify the mission with §§2–4.
2. Set the project and coordinate system with §§5–7.
3. Process the trajectory and generate scans with §§8–12.
4. Follow the registration path in §§13–21. Do not skip **Update Scans**.
5. Perform QC and any justified remedies with §§22–26.
6. Identify the final state, export, document and archive with §§27–34.
7. If anything does not match the expected state in a section, go to §35 before experimenting.

**Do not troubleshoot by stacking adjustments or changing several settings together.** Establish
the symptom, check the last known good stage, make one controlled change, and record what happened.
