# 8. Mission Planning Requirements

## 8.1 What planning must produce

A mission plan, in the project record, before mobilisation. It states the route, the passes, the
GNSS assessment, the initialization locations, and — explicitly — **what mobile mapping will not
get**.

## 8.2 Passes and overlap

> **PARAMETRIX DECISION REQUIRED · D-41 · P1 · blocks operation**
>
> **How many passes, in what pattern, by roadway type?**
>
> No Trimble source specifies a pass pattern. The v1 Parametrix draft stated a minimum of three
> passes on the pavement; **that figure is not traceable to any source in the evidence set** and is
> recorded here so it is not lost, not because it is established.

Two facts constrain the answer, and both are in the Technical Manual:

- **A second pass in the opposite direction improves a dataset more than any setting change**,
  because it converts grazing incidence into direct incidence and long range into short range for
  the far side of the corridor *(Technical Manual §16.3)*
- **Overlap is what makes the office remedies possible.** LiDAR QC and run-to-run registration both
  require overlapping runs *(Technical Manual §11.5, §21.11)*

> **CAUTION · W-10**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

## 8.3 GNSS assessment

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> The plan **should** identify GNSS-hostile stretches **before mobilising**, and for each state the
> expected duration at realistic collection speed.

> **Duration, not length.** Inertial drift is a function of time. A 300 m tunnel at 80 km/h is 13
> seconds; the same tunnel at 20 km/h in traffic is nearly a minute *(Technical Manual §15.1)*.
> The time of day is part of the assessment.

> **IMPORTANT**
>
> Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
> nothing beyond *(MX60 UG Rev B, p.56; Technical Manual §15.2)*.
>
> **Outages materially longer than 60 seconds are a planning problem, not a driving problem.**
> Beyond the published figure, any expectation is an extrapolation past the manufacturer's stated
> envelope.

For each hostile stretch the plan states the mitigation: additional control, planned overlap for
LiDAR QC, or a different acquisition method — **because two of the three have to be arranged
before the crew leaves.**

> **TESTING REQUIRED · T31**
>
> Whether predicted GNSS conditions correlate with achieved trajectory RMS on this system. Until
> that is established, the assessment is judgement rather than estimate.

## 8.4 Initialization locations

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> The plan identifies a **primary and a backup** initialization location, each of which is:
>
> - open sky, away from buildings and canopy
> - somewhere the vehicle can safely sit still for two to three minutes
> - with room afterwards to drive straight and perform dynamic manoeuvres
>
> Scout them on imagery before mobilising. A lot that turns out to be fenced, occupied or under
> trees costs twenty minutes at the worst moment of the day. *(Technical Manual §13)*

## 8.5 Base station strategy

> **PARAMETRIX DECISION REQUIRED · D-42 · P1 · blocks operation**
>
> **Own base on project control, VRS, RTX, or CORS post-processing — and what maximum baseline?**
>
> It interacts with **D-19** (§6.2): Single Base requires a local base station on every mission,
> PP-RTX does not. The decision determines field logistics on every job.

## 8.6 What mobile mapping will not get

> **PARAMETRIX PROCEDURE (PROPOSED) · D-34**
>
> Record in the project file **before mobilising**: the segments where mobile mapping is expected
> to be marginal, the mitigation chosen for each, and the segments where another method is
> proposed.

> **This is the clause people avoid**, and the reason it is a requirement rather than a
> recommendation. What it costs to discover the same thing in the office instead is set out in
> **Technical Manual §15.5**.

> **PARAMETRIX DECISION REQUIRED · D-34**
>
> The decision rule when a corridor produces an unacceptable trajectory: who decides, against what,
> and what the client is told.

## 8.7 Records this section requires

| Record | State |
|---|---|
| The mission plan — route, passes, direction, overlap | **D-41** |
| GNSS assessment, with duration estimates and mitigations | **D-41, D-42** |
| Initialization locations, primary and backup | **PROPOSED** |
| Segments mobile mapping will not serve, and what is proposed instead | **D-34** |
