# Mobile Mapping Standard Operating Procedure
## Trimble MX60 and Trimble Business Center

**Parametrix**

---

| | |
|---|---|
| **Revision** | 1.0 — first complete draft |
| **Date** | 2026-09-11 |
| **Status** | **DRAFT — not issued. Not approved. Not binding.** |
| **Software documented** | Trimble Business Center **2026.10** · Trimble Mobile Imaging **Rev L** |
| **Owner** | **Not assigned** — *D-1* |
| **Approved by** | — |
| **Next review** | **Not set** — *D-1* |

---

> ## CAUTION — READ BEFORE USING THIS DOCUMENT
>
> **This SOP contains no adopted Parametrix policy.**
>
> Every Parametrix procedure in it is marked **PARAMETRIX PROCEDURE (PROPOSED)**. Every acceptance
> threshold is marked **PARAMETRIX DECISION REQUIRED**. **Appendix H — the Decision Adoption
> Record — is empty**, and that is the correct state on first issue.
>
> **Nothing in this document may be quoted to a client as an existing Parametrix standard.**
>
> The technical content is complete and evidenced against Trimble documentation. The company
> decisions that would make it binding have not been made. **Appendix I lists all 100 of them**,
> in priority order; **ten genuinely block operation** and should be settled before the first
> production job.

---

## Purpose

A standard operating procedure for mobile mapping production at Parametrix using the **Trimble
MX60** and **Trimble Business Center**, written so that a competent survey professional who has
never operated an MX60 can understand the workflow, the terminology, the risks, the checks and who
is responsible for each.

It does not teach land surveying. It teaches mobile mapping.

## How this document is built

Every instruction carries a tag saying where its authority comes from — Trimble, observation,
Parametrix, or an open question. §1.5 explains the system; §27.8 lists the tags.

Every major technical section ends with an **In Plain English** box answering four questions: what
we just did, why it matters, what can go wrong, and what a good result looks like in practical
terms. **Read end to end, those boxes are a complete description of the workflow in ordinary
language** — a project manager or reviewer can get a true picture from them alone.

## Evidence base

Thirty-eight Trimble Business Center help topics, two release notes, six MX60 and TMI manuals and
bulletins, captured and classified before drafting began. **402 structured records** in
`reference/mx60-reference-data.csv`, which is the authority for numbers. Full index in
**Appendix C**.

## Reading paths

| If you are… | Start at |
|---|---|
| A surveyor new to mobile mapping | §2, then the In Plain English boxes in order |
| A field technician | §4, then §6–§10, then checklists A1–A3 |
| An office technician | §11, then §11–§22 in order, then checklists A4–A11 |
| A project surveyor | §17, then §5, §15, §18, §23, §24 |
| A project manager | §1, §3, §23, §24, §25 — and the In Plain English boxes alone |
| Training someone | **Appendix D** |

## Contents

**Part I — Orientation**
1. Purpose and Scope · 2. Mobile Mapping in Plain Terms · 3. Roles and Responsibilities ·
4. Equipment and Software

**Part II — Before the field**
5. Coordinate Systems, Control, and Project Setup · 6. Mission Planning ·
7. Field Preparation and Preflight

**Part III — Acquisition**
8. MX60 Data Collection · 9. Field Quality Checks · 10. Data Transfer and Project Organization

**Part IV — Office processing**
11. Import into TBC · 12. Trajectory Processing · 13. Generate Scans · 14. Calibration ·
15. Registration · 16. Run to Run Registration · 17. Control and Independent Check Points ·
18. Point Cloud QC · 19. Imagery QC · 20. Degraded GNSS Conditions ·
21. Cleanup Mobile Mapping Mission

**Part V — Delivery and closeout**
22. Export and Deliverables · 23. Data Provenance and Audit Trail · 24. Final QA/QC ·
25. Archiving and Records · 26. Troubleshooting · 27. Terminology

**Appendices**
A. Working Checklists · B. TMI Status and Warning Reference · C. Trimble Source Index ·
D. First-Week Training Exercise · G. Figure List and Placeholders ·
H. Decision Adoption Record · **I. Open Parametrix Decisions, Field Tests, and Vendor Questions**

---

> **PARAMETRIX BRANDING — PLACEHOLDER**
>
> This document is unstyled. Branding is applied once, at the end, when content and structure are
> stable. See **Appendix G §G4**.

---

# 1. Purpose and Scope

## 1.1 Purpose

This standard operating procedure covers mobile mapping production at Parametrix using the
**Trimble MX60** vehicle-mounted laser scanning and imaging system, and **Trimble Business
Center (TBC)** for office processing.

It exists to make three things possible:

1. **Repeatable acquisition.** Two crews on two days should collect data the same way, and a
   third person should be able to tell from the record that they did.
2. **Defensible processing.** Every adjustment applied to the data should be traceable to a
   decision someone made deliberately, with evidence of why it was acceptable.
3. **Transferable competence.** A surveyor who has never operated an MX60 should be able to
   read this document and understand what the crew did, what the office did, and where the
   result could have gone wrong.

## 1.2 What this document assumes, and what it does not

**It assumes** the reader is a competent survey professional. Control networks, datums,
geoids, residuals, least squares adjustment, check points and accuracy statements are taken as
known. This document does not teach them and does not restate them.

**It does not assume** any prior mobile mapping experience. Trajectories, SBETs, GNSS/INS
integration, boresight calibration, scan generation, registration and mobile LiDAR quality
control are explained from the beginning.

Where conventional survey practice and mobile mapping differ, the difference is explained **at
the point where it matters** rather than in a preamble. Most of those differences come down to
one thing, and §2 is about it: in mobile mapping, the instrument is never stationary, so
everything the system measures is referenced to a computed path through space rather than to an
occupied point.

## 1.3 Scope

**In scope**

- MX60 field acquisition: planning, installation, initialization, collection, field checks
- Data transfer and project organisation
- TBC office processing: import, trajectory processing, scan generation, calibration,
  registration, QC, cleanup and export
- Quality control at every stage, and the records that demonstrate it
- The decisions Parametrix must make before this becomes binding procedure

**Out of scope**

- Basic land surveying practice
- Establishing the control network the mobile mapping data will be registered to — that is
  conventional survey work and is governed by Parametrix's existing survey procedures
- Feature extraction, CAD production and deliverable drafting downstream of the point cloud
- Static terrestrial scanning, UAS and aerial workflows, except where TBC behaviour is shared
- Vehicle operation, traffic control and site safety, which are governed by Parametrix's health
  and safety procedures and by the client's requirements

## 1.4 How to read this

The document is sequential — it follows the production workflow from planning to archive — but
almost nobody needs all of it.

| If you are… | Start here | Then read |
|---|---|---|
| **A surveyor new to mobile mapping** | §2, *Mobile Mapping in Plain Terms* | §5, §12, §15, §17, §18 — and every **In Plain English** box, in order |
| **A field technician** | §4, *Equipment and Software* | §6–§10, then Appendices A–C |
| **An office technician** | §11, *Import into TBC* | §11–§22 in order, then Appendix C |
| **A project surveyor** | §17, *Control and Independent Check Points* | §5, §15, §18, §23, §24 |
| **A project manager** | §1 and §3 | §23, §24, §25 — and the **In Plain English** boxes on their own |

> **The In Plain English boxes are a complete document in themselves.** Read end to end, with
> nothing else, they describe the whole workflow in ordinary language. That is deliberate: a PM
> or a reviewer should be able to get a true picture without working through the technical
> detail.

## 1.5 How to read the evidence tags

Every instruction in this document carries a tag saying where its authority comes from. This
matters more here than in most procedures, because the MX60 workflow is new to Parametrix and
much of what looks like established practice is in fact a software default that nobody has yet
examined.

| Tag | What it means |
|---|---|
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble states this, in the cited topic or manual page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software, but Trimble does not state it as procedure |
| **PARAMETRIX PROCEDURE (PROPOSED)** | This document recommends it. **It is not company policy** |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Decided by Parametrix, with a date and an owner in Appendix D |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make. The question is stated; the answer is not |
| **FIELD TESTING REQUIRED** | Answerable by testing, not by reading. See Appendix E |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble. See Appendix F |

### The state of this document on first issue

> **CAUTION**
>
> **On first issue, this SOP contains no PARAMETRIX PROCEDURE (ADOPTED) entries at all.**
>
> Every Parametrix procedure in it is marked **PROPOSED**. Every acceptance threshold is marked
> **PARAMETRIX DECISION REQUIRED**. Nothing in this document is yet binding company policy, and
> nothing in it should be quoted to a client as an existing Parametrix standard.
>
> That is the correct state, not an oversight. The technical content is complete and evidenced;
> the company decisions on top of it have not been made. **Appendix D lists all of them, in
> priority order, and eleven of them should be settled before the first production job.**

## 1.6 What this document is built from

| Source | Revision | Used for |
|---|---|---|
| Trimble MX60 User Guide | Rev B, May 2025 | Hardware, installation, specifications, safety |
| Trimble MX60 Quick Start Guide | Rev B, March 2025 | Field sequence |
| Trimble Mobile Imaging (TMI) Software User Guide | Rev L, April 2026 | Field software |
| Trimble MX60 Spec Sheet | PN 022516-737C | Specifications |
| Trimble MX Shock Absorbing Mounting Rack User Guide | Rev B, May 2025 | Vehicle installation |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60 | January 2025 | Laser settings |
| **Trimble Business Center help portal** | **TBC 2026.10** | **All office processing** |
| TBC Release Notes 2025.21 and 2026.10 | — | Version-dependent behaviour |

Thirty-eight TBC help topics were captured, read and classified before this document was
drafted. The full assessment is in `analysis/`, the structured data in
`reference/mx60-reference-data.csv` (402 records), and the cited topic index in **Appendix G**.

> **The CSV is the authority for numbers.** This document explains what they mean. When a
> Trimble revision changes a value, the CSV row is updated and the prose usually is not.

### A note on version

The captured TBC help documents **TBC 2026.10**, confirmed by cross-reference: a registration
feature listed as new in the 2026.10 release notes is present in the captured help topic
*(TBC RN 2026.10; TBC 22905)*.

> **VENDOR CLARIFICATION REQUIRED**
>
> **Which TBC version is installed on the Parametrix processing workstation?** Two behaviours
> in this document depend on it, and both are legacy: calibrating outside TBC (versions up to
> 5.21) and a prompt for a missing RMS file (projects saved before 5.80). Both boundaries
> predate 5.70, the oldest release Trimble still publishes notes for, so any recent
> installation is unaffected — but this should be confirmed rather than assumed. *(Appendix F)*

## 1.7 Revision and ownership

> **PARAMETRIX DECISION REQUIRED**
>
> **Who owns this document, who approves revisions, and on what cycle is it reviewed?**
>
> Nothing in this SOP establishes an owner, an approver or a review interval, because no such
> assignment has been made. A procedure with no owner decays quietly — the software changes
> underneath it and nobody is responsible for noticing.
>
> Two things make this more pressing than usual. TBC is now on an annual release cycle
> (2023.10 through 2026.10), and each release has changed mobile mapping behaviour. And the
> MX60 itself is recent — TMI support arrived in December 2024 *(TMI UG Rev L, p.2)* — so the
> documentation underneath this SOP is still moving.
>
> *Register item 1. See Appendix D.*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We set out what this document covers, who it is for, and — most
> importantly — how to tell the difference between something Trimble says, something the
> software does, and something Parametrix has decided. Right now that last category is empty.
>
> **Why it matters.** Mobile mapping produces enormous, convincing-looking datasets very
> quickly. A point cloud with a hundred million points looks authoritative whether or not the
> trajectory underneath it was ever checked. The only thing standing between "looks right" and
> "is right" is a procedure that says what was done and what was verified — and a reader who
> can tell which parts of that procedure someone actually thought about.
>
> **What can go wrong.** The most likely failure with a new SOP is not that somebody ignores
> it. It is that somebody reads a software default in it, assumes it was chosen deliberately,
> and defends it to a client. That is why the tags exist and why nothing in this document is
> yet marked as adopted. If you find yourself citing this SOP as a Parametrix standard, check
> the tag first.
>
> **What good looks like.** You should be able to open any page of this document, point at any
> instruction, and answer in one sentence: *who says so?* If you cannot, the tag is missing and
> the document has a defect worth reporting.

---

# 2. Mobile Mapping in Plain Terms

This section is for the reader who knows surveying and has never operated a mobile mapping
system. Everything else in this document depends on the ideas here.

## 2.1 The one difference that explains all the others

A total station or a static scanner measures from a **known, stationary point**. You occupy,
you orient, you shoot. The instrument's position is fixed and separately determined, so the
quality of any measurement is a question about that measurement.

The MX60 never stops. It measures continuously from a vehicle moving at highway speed, and it
has no occupied point at all. Instead it computes, for every instant, **where the sensor head
was and which way it was pointing** — a continuous record called the **trajectory**.

> Every point in a mobile mapping cloud is the sum of two things: a range and angle measured by
> the scanner, and the position and attitude of the scanner at the instant of that measurement.
> The scanner part is excellent and nearly constant. **The trajectory part is where the error
> lives.**

This single fact drives the rest of the document:

- Why initialization matters, and why it is not a formality (§8)
- Why GNSS conditions dominate the accuracy conversation (§6, §20)
- Why everything downstream of the trajectory has to be recomputed when it changes (§13, §15)
- Why the office work is largely about improving the trajectory, not the points (§12, §15, §16)
- Why proving *which trajectory* produced a deliverable turns out to be hard (§23)

## 2.2 What the trajectory is, and how it is computed

The trajectory is a time series: position (X, Y, Z) and attitude (roll, pitch, heading) at a
high rate, for the whole mission. It is produced by combining two sensor types that fail in
opposite ways.

| | **GNSS** | **Inertial (IMU)** |
|---|---|---|
| Measures | Absolute position | Change in orientation and velocity |
| Error behaviour | Bounded but noisy — it does not drift, but it jumps and can be lost entirely | Smooth and precise instant to instant, but **drifts without limit over time** |
| Fails when | Sky is obstructed — trees, buildings, bridges, tunnels | Always, gradually, by its nature |

Neither alone is adequate. Combined, each covers the other's weakness: GNSS anchors the
inertial solution and stops the drift; the IMU carries the solution smoothly through the gaps
when GNSS is degraded or absent.

The combination is done by a filter, and for surveying work it is done **twice** — once
forward through time and once backward — then merged. The merged result is called a **Smoothed
Best Estimate of Trajectory**, universally abbreviated **SBET**.

> **The backward pass is why the end of a mission matters as much as the beginning.** A gap in
> the middle of the drive is bracketed by good data on both sides, and the smoother can bridge
> it from both directions. A gap at the *end* has good data on one side only. This is the
> practical reason the field procedure requires a proper closing sequence (§8.7), and it is the
> single most commonly skipped step in mobile mapping.

Two supporting sensors appear throughout this document:

- **GAMS** — a second GNSS antenna. Two antennas a known distance apart give a direct heading
  measurement, which is otherwise the hardest attitude component to determine. It speeds up
  initialization considerably *(TBC 25943)*
- **DMI** — a distance measuring indicator on a wheel. It provides an independent along-track
  distance, which constrains the inertial solution when GNSS is poor *(TBC 25943)*

## 2.3 How mobile mapping error behaves

This is where a surveyor's intuition needs adjusting, and it is worth being precise.

**Error is not uniform across the dataset.** It varies along the corridor with GNSS quality, and
it varies within a single scan line with range.

### Attitude error multiplies with range

An error in the *position* of the sensor head displaces every point by the same amount. An
error in the *attitude* — which way it was pointing — displaces points by an amount
proportional to how far away they are.

The relationship is simple geometry: lateral displacement is range multiplied by the angular
error in radians. A given attitude error therefore costs five times as much at 50 m as at 10 m.

> This is arithmetic, not a specification. **No Trimble source in the set publishes an attitude
> error budget for the MX60**, so the useful range for a given tolerance has to be established
> from the manufacturer's accuracy statement for the configuration Parametrix owns (§4.1), or by
> test.

> **WHY THIS MATTERS**
>
> This is why *useful range* is a shorter distance than *maximum range*. The scanner can return
> a point at its maximum range; whether that point is good enough to measure from is a
> different question, and the answer depends on the attitude accuracy of the trajectory at that
> instant. Two clouds collected on the same day with the same instrument can have quite
> different useful ranges if one was collected under open sky and the other in an urban canyon.

### Error is correlated in time, not scattered

Conventional survey errors tend to be independent — one shot's error tells you little about the
next. Mobile mapping error is **strongly correlated over seconds and minutes**, because it is
dominated by the state of a filter that evolves smoothly.

The practical consequence: a bad stretch of trajectory produces a whole *region* of cloud that
is consistently displaced, not a scatter of bad points. It will look internally consistent and
perfectly clean. **It will simply be in the wrong place**, and only comparison against
independent control will reveal it.

> That is the most important thing in this section. **Mobile mapping data does not look wrong
> when it is wrong.**

## 2.4 What the MX60 actually collects

| Sensor | What it produces |
|---|---|
| **Two laser scanners** | Range and angle, continuously, to both sides of the vehicle |
| **360° spherical camera** | Panoramic imagery along the corridor |
| **Rear-downward camera** | Pavement-facing imagery, used for pavement condition and orthomosaics |
| **GNSS receiver and IMU** | The raw observations from which the trajectory is computed |

The system is sold in three configurations — **Core**, **Pro** and **Premium** — which differ
in imagery resolution and in the grade of the GNSS/IMU system *(MX60 UG Rev B, p.12)*.

> **PARAMETRIX DECISION REQUIRED**
>
> **Which configuration is the Parametrix system?** This is not a detail. Panoramic imagery is
> **8192 × 4096 px on Core and 12288 × 6144 px on Premium and Pro** *(TBC 22501, 23888)* — four
> times the pixels. The attitude accuracy of the navigation system also differs by
> configuration, which changes every accuracy statement in this document.
>
> The vendor can confirm from the serial number. *(Register item 2; Appendix F)*

## 2.5 The data chain, once

The names matter because TBC's commands are named after them, and a processor who does not know
which object a command acts on will eventually act on the wrong one.

```
  .mxdb          The mission database written in the field. The index to everything
     │
     ├── raw GNSS + IMU observations  ──►  SBET (or NAV)      the trajectory
     │
     └── raw scanner + camera data
              │
              ▼
            TMX          polar scan data — ranges and angles, sensor-relative
              │
              │   Generate Scans  ◄── applies the trajectory
              ▼
           RWCX          the point cloud — XYZ, intensity, colour, normals
```

Two things are worth noting now and will be returned to in §13.

**The MX60 converts TMX to RWCX in one step.** Older MX9 and MX90 systems go through an
intermediate stage requiring a range-ambiguity correction called MTA. **The MX60 workflow has
no MTA stage**, which removes a whole category of setup and a whole category of failure
*(TBC 22503)*.

**The trajectory is applied at scan generation, not at collection.** The raw scan data is
sensor-relative. It becomes a georeferenced point cloud only when combined with a trajectory —
which is why improving the trajectory later means regenerating the cloud (§15, §13).

## 2.6 What the office actually does

A surveyor coming from static scanning expects office work to mean registration of scans to
each other and to control. Mobile mapping is different in an instructive way.

| Stage | What is being improved |
|---|---|
| **Trajectory processing** (§12) | The trajectory itself, from raw observations and base station data |
| **Scan generation** (§13) | Nothing — this applies the trajectory to produce the cloud |
| **Calibration** (§14) | The fixed angular offsets between sensors. Periodic, not per-job |
| **Registration** (§15, §16) | **The trajectory again**, now using surveyed control or overlapping cloud |
| **Update Scans** (§13.6) | Nothing — this reapplies the improved trajectory to produce a new cloud |

> **Three of the five stages improve the trajectory. Two of them just recompute points.**
>
> This is the shape of mobile mapping office work, and it is why the phrase "registering the
> point cloud" is misleading. You are not moving points. You are improving the path the sensor
> took, and then recomputing where the points must therefore have been.

## 2.7 Vocabulary

Enough to read the next several sections. The full glossary is §27.

| Term | Meaning |
|---|---|
| **Trajectory** | The computed position and attitude of the sensor head over time |
| **SBET** | Smoothed Best Estimate of Trajectory — the post-processed trajectory |
| **NAV** | The real-time trajectory computed in the field. Lower quality; a fallback |
| **Mission** | One deployment: a `.mxdb` and everything under it |
| **Run** | One continuous stretch of collection within a mission. A mission has many |
| **Station** | One instant of imagery capture along a run |
| **Boresight** | The fixed angular offset between a sensor and the inertial reference frame |
| **Lever arm** | The fixed distance offset between two sensors. **Known, not estimated** |
| **Registration** | Adjusting a trajectory to fit surveyed control, or to fit another run |
| **Target** | In TBC's registration sense: a point **picked in the point cloud** |
| **GCP** | Ground control point — an accurately surveyed coordinate on an identifiable feature |
| **Validation point** | A GCP held out of the adjustment, used only to measure its quality |

> **"Target" is a trap.** In TBC's registration commands a *target* is not a physical panel you
> placed in the field. It is a point the operator picks in the point cloud, which is then paired
> with a surveyed GCP *(TBC 22905)*. The physical thing in the field is the GCP. A checkerboard
> panel is one kind of feature you might pick, but so is a corner of a painted road marking.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We established the one idea the rest of this document rests on: a mobile
> mapping system has no occupied point. It computes where it was, continuously, and every point
> it collects is hung off that computed path. The path is called the trajectory, and it is the
> job.
>
> **Why it matters.** Think of it as a very long, very fast resection that never stops — except
> that instead of resecting from known points, the system is dead-reckoning with an inertial
> sensor and correcting itself with GNSS whenever the sky allows. When the sky does not allow,
> it keeps going on inertial alone and quietly gets worse. Everything the office does later is
> an attempt to improve that path, not to move the points around.
>
> **What can go wrong.** The thing that catches people is that bad mobile mapping data looks
> fine. If the trajectory was drifting through a tree-lined stretch, the cloud from that stretch
> is still crisp, still dense, still internally consistent — and sitting 8 cm from where it
> should be. There is no noise, no scatter, no visual tell. You find it by checking against
> control you surveyed independently, or you do not find it at all. This is different from a
> total station, where a bad shot usually looks like a bad shot.
>
> **What good looks like.** A dataset you can trust is one where the trajectory had continuous
> good GNSS or short, well-bracketed gaps; where independent check points that took no part in
> any adjustment fall where they should; and where two passes down the same corridor land on top
> of each other. Not one where the cloud looks clean — it always looks clean.

---

# 3. Roles and Responsibilities

> **This entire section is PARAMETRIX DECISION REQUIRED.**
>
> No role assignment, approval authority, qualification requirement or sign-off has been made
> for mobile mapping at Parametrix. Everything below is a **structure for the decision**, not a
> record of one. Nothing in this section may be quoted as an existing Parametrix requirement.

## 3.1 Why this section is not optional

Most of the failure modes in this document are not technical. They are questions of who noticed
and who decided.

A registration that used the wrong trajectory, a Cleanup that destroyed the only record of an
earlier attempt, a deliverable exported with a setting nobody examined — none of these is a
software fault. Each is a place where a person made a choice, and the difference between a
defensible project and an indefensible one is whether the right person made it and whether
anyone can tell afterwards.

> **WHY THIS MATTERS**
>
> Mobile mapping compresses a great deal of judgement into a small number of dialog boxes. A
> processor clicking **Apply** in the Register a Run dialog is making an adjustment decision
> that, in conventional survey work, would have been a least-squares run reviewed by a licensed
> surveyor. The software does not care who clicks. The SOP has to.

## 3.2 The roles this document assumes

These are **functions, not job titles**. One person may hold several. On a small job the same
person may hold all of them — which is workable, provided it is recorded and provided the
independent checks in §17 and §24 are genuinely independent of the adjustment.

### Field Technician / Operator

Runs the system. Owns everything from vehicle preparation through to verified data transfer.

- Vehicle installation, sensor mounting, cabling, power (§7)
- Preflight checks and TMI configuration (§7, §8)
- Initialization, collection, monitoring, closing sequence (§8)
- Field quality checks before leaving site (§9)
- Data offload and integrity verification (§10)
- The field record: what was collected, in what conditions, what went wrong

> **The operator is the only person who will ever see the collection conditions.** GNSS quality,
> weather, traffic, obstructions, a manoeuvre that had to be abandoned — none of this survives
> into the data in a readable form. If the operator does not record it, it is gone, and the
> office will be inferring it from residuals three weeks later.

### Mobile Mapping Processor

Takes the raw mission to a QC'd, registered point cloud.

- Import and project setup (§11)
- Trajectory processing, or coordination with whoever holds the POSPac licence (§12)
- Scan generation and filter selection (§13)
- Registration to control (§15, §16)
- Point cloud and imagery QC (§18, §19)
- Export and delivery preparation (§22)
- The processing record (§23)

### Project Surveyor

Owns the accuracy statement. This is the role that must be independent of the adjustment.

- Control network design and adequacy for the corridor (§5, §6)
- **Designating which points are control and which are held as independent checks** (§17)
- Reviewing registration results against the project accuracy requirement (§15, §18)
- Accepting or rejecting the dataset (§24)
- Signing the accuracy statement that goes to the client

> **IMPORTANT**
>
> The person who performs a registration should not be the only person who judges whether it
> passed. This is ordinary survey practice and it applies here unchanged — but it is easier to
> lose in mobile mapping, because the adjustment and the assessment happen in the same
> software, in the same session, by the same person, minutes apart.

### Project Manager

Does not need to operate anything. Needs to be able to answer a client.

- Scope, schedule and the accuracy requirement agreed with the client (§5)
- Knowing what was collected and what was not
- Knowing whether the deliverable is defensible, and on what evidence (§23, §24)
- Records retention and archive (§25)

### System Owner

The role with no obvious home, and the one most likely to go unassigned.

- Calibration currency — when the system was last calibrated and whether it is still valid (§14)
- Firmware and software versions, and what changed in them (§4)
- Vendor relationship, support, open questions (Appendix F)
- **Maintaining this SOP** as TBC and TMI change

## 3.3 The decisions

> **PARAMETRIX DECISION REQUIRED**
>
> **D-3.1 · Who may operate the MX60?** Is there a qualification, a training requirement, a
> supervised-run count, or a sign-off before someone collects production data alone?
>
> **D-3.2 · Who may perform a registration?** Registration is an adjustment. Is it restricted,
> and if so to whom?
>
> **D-3.3 · Who accepts a registration?** Must the accepting person be someone other than the
> person who performed it? *(§17, §24)*
>
> **D-3.4 · Who may run Cleanup Mobile Mapping Mission?** It is destructive and not undoable.
> *(§21 — this is the sharpest single instance of the problem)*
>
> **D-3.5 · Who signs the accuracy statement?** Under what licensure, and against what evidence?
>
> **D-3.6 · Who owns calibration currency?** *(§14)*
>
> **D-3.7 · Who owns this SOP?** *(§1.7)*
>
> *Register items 3–9. See Appendix D.*

## 3.4 A proposed structure, offered for decision

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted. Offered so the decisions in §3.3 have something concrete to react to.**
>
> | Activity | Performed by | Reviewed or approved by |
> |---|---|---|
> | Mission planning | Processor or Project Surveyor | Project Surveyor |
> | Control network design | Project Surveyor | — |
> | Field acquisition | Field Technician | — |
> | Field quality checks | Field Technician | — |
> | Trajectory processing | Processor | — |
> | Calibration | Processor | System Owner |
> | **Registration** | **Processor** | **Project Surveyor** |
> | **Designating control vs. check** | **Project Surveyor** | — |
> | Point cloud and imagery QC | Processor | Project Surveyor |
> | **Cleanup Mobile Mapping Mission** | **Processor** | **Project Surveyor, in writing** |
> | Export and delivery | Processor | Project Surveyor |
> | Accuracy statement | Project Surveyor | — |
> | Archive | Processor | Project Manager |
>
> The three rows in bold are the ones where the reviewer genuinely matters. The rest could
> reasonably collapse onto fewer people on a small job.
>
> **The rationale for control-versus-check sitting with the Project Surveyor and nobody else:**
> if the person performing the adjustment also chooses which points the adjustment is measured
> against, the check is not independent. That is true in conventional survey work and it is true
> here. TBC makes the choice a checkbox *(§17)*, which makes it easy to change quietly.

## 3.5 What must be recorded regardless of who does it

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> Whatever Parametrix decides about roles, the project record should be able to answer, for any
> dataset, years later:
>
> - Who collected it, when, and in what conditions
> - Which trajectory the delivered data was built on *(§23 — this one is genuinely hard)*
> - Which points were used as control and which were held as independent checks
> - What the registration residuals were, on both
> - Who accepted it, on what date, against what accuracy requirement
> - Whether Cleanup was run, by whom, and what was archived first
>
> Six facts. None is onerous to record at the time and all are effectively unrecoverable later.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We listed the jobs that have to be done and the decisions about who does
> them — and were honest that Parametrix has not made those decisions yet. What is here is a
> proposal to argue with, not a rule to follow.
>
> **Why it matters.** In conventional survey work, the boundaries between roles are established
> by decades of practice and by licensure. Mobile mapping has none of that yet at Parametrix, and
> the software actively blurs the lines: the same person, in the same hour, in the same
> application, can adjust the data, decide what to measure the adjustment against, judge whether
> it passed, and export the result. Nothing stops them. Nothing records that they did.
>
> **What can go wrong.** The specific failure to worry about is not carelessness — it is a
> conscientious processor who adjusts, checks, finds a residual they do not like, adds a point to
> the adjustment to improve it, and re-checks. Every step is well intentioned. The result is an
> adjustment measured against itself, and a residual figure that means nothing. This is exactly
> the failure that separating "who adjusts" from "who decides what is a check" prevents.
>
> **What good looks like.** On a well-run job, the person who signs the accuracy statement can
> point to check points they designated before the adjustment ran, that took no part in it, and
> say what the residuals on those points were. If that sentence cannot be said, the accuracy
> statement is an opinion.

---

# 4. Equipment and Software

## 4.1 The MX60 system

The MX60 is a vehicle-roof-mounted mobile mapping system. Its components, as they appear in
this document and in TMI:

| Component | Function |
|---|---|
| **Sensor Unit** | The roof-mounted head: scanners, cameras, GNSS antenna, IMU |
| **Control Unit** | In-vehicle computer, data storage, power management |
| **Exchangeable data disk** | Removable storage inside the Control Unit |
| **Mounting rack** | Attaches the Sensor Unit to the vehicle |
| **GAMS antenna** *(optional)* | Second GNSS antenna for direct heading |
| **DMI** *(optional)* | Wheel-mounted distance measuring indicator |

### Sensors

| Sensor | Count | Notes |
|---|---|---|
| Laser scanner | **2** | One per side, mounted at opposing oblique angles |
| Spherical camera | 1 | 360° panoramic |
| Rear-downward camera | 1 | Pavement-facing |

> **The two-scanner arrangement is the reason Register Run to Run can work on a single run**, and
> the reason most exports produce a pair of files — *Laser Left* and *Laser Right* — rather than
> one *(TBC 22501, 23339)*.

### Configurations

Three: **Core**, **Pro**, **Premium** *(MX60 UG Rev B, p.12)*. They differ in the 360° camera
and in the GNSS/IMU grade.

| | Core | Pro | Premium |
|---|---|---|---|
| Panoramic image size | **8192 × 4096 px** | **12288 × 6144 px** | **12288 × 6144 px** |
| Side / planar image size | 4096 × 3008 px | 4096 × 3008 px | 4096 × 3008 px |

*(TBC 22501, 23888 — the panorama figures; these are the sizes TBC writes at export)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Which configuration is the Parametrix system, and is it fitted with GAMS and DMI?**
>
> This changes: every imagery accuracy and resolution statement in §19; the attitude accuracy
> that underlies every point cloud accuracy statement; whether GAMS-assisted initialization is
> available (§8); and whether DMI settings appear in trajectory processing (§12).
>
> The vendor can confirm from the serial number. *(Register item 2; Appendix F)*

### Specification discrepancies to be aware of

Two unresolved conflicts sit in the source documents. Neither blocks work, but neither should be
quoted to a client without checking.

| | Source A | Source B | Status |
|---|---|---|---|
| Scanner field of view | ~346° beam deflection *(MX60 UG Rev B, p.54)* | Full 360° *(Spec sheet, p.2)* | **VENDOR CLARIFICATION REQUIRED** — matters for occlusion geometry |
| Mounting rack | MX SCAN Roof Rack, 18 kg | MX Shock Absorbing Mounting Rack, 28 kg | **PARAMETRIX DECISION REQUIRED** — which is fitted. The published GAMS corner offsets apply to the standard rack **only** *(MX60 UG Rev B, p.68)* |

*(Recorded as `CONFLICT-002` and `CONFLICT-003` in `reference/mx60-reference-data.csv`.)*

## 4.2 Trimble Mobile Imaging — the field software

**TMI** is the browser-based field software. It runs in **Chrome** against the Control Unit.

| | |
|---|---|
| Capture interface | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |
| Modules | TMI.Capture, TMI.AI |

*(TMI UG Rev L)*

> **TMI is a web application served by the vehicle, not a cloud service.** It does not need
> internet access, and the addresses above resolve only on the Control Unit's network.

MX60 support arrived in TMI in **December 2024** *(TMI UG Rev L, p.2)*, which is why documents
older than that — including the TBC Technical Notes of October 2022 — do not mention the MX60 at
all.

> **VENDOR CLARIFICATION REQUIRED**
>
> **Which TMI version is on the Parametrix system, and how are firmware updates distributed?**
> One documented behaviour differs between versions: the Quick Start Guide describes two separate
> MX60 laser controls (*Measurement Prog* and *Line Speed*), where TMI Rev L describes a single
> combined **Laser Mode** *(MX60 QSG p.10; TMI UG Rev L p.29)*. *(Appendix F; `CONFLICT-005`)*

## 4.3 Trimble Business Center — the office software

TBC with the **mobile mapping module**. The captured documentation is **TBC 2026.10** (§1.6).

### Where the mobile mapping commands live

| Ribbon location | Commands |
|---|---|
| **Mobile Mapping ▸ Processing** | Register a Run, Register a Mission, Register Run to Run |
| **Mobile Mapping ▸ Reports** | Mobile Mapping Report, Trajectory Plots |
| **Mission node context menu** | Generate Scans, Update Scans, Process Raw Trajectory Data, Generate POSPac Position Fixes, Import/Export Calibration, **Cleanup Mobile Mapping Mission** |
| **Capture Devices node context menu** | Manual Camera Calibration |
| **Point Clouds ▸ Regions** | Extract Classified Point Cloud |
| **Point Clouds ▸ View** | Cutting Plane View |
| **Home ▸ Data Exchange ▸ Export** | **Mobile Mapping** tab and **Point Cloud** tab — different exporters |
| **Home ▸ Data Exchange** | Publish to TRCPS |

*(TBC 22905, 26473, 25096, 23991_1, 27415, 26466, 25943, 24460, 22920, 20728, 27279, 11769, 29527)*

> **IMPORTANT**
>
> **The Export dialog has two tabs that both export point clouds, and they behave differently.**
> The **Mobile Mapping** tab holds the run-aware exporters; the **Point Cloud** tab holds the
> generic ones, which select by region or by a rectangle drawn in a view rather than by run
> *(TBC 11769)*. §22 covers the distinction. Choosing the wrong tab is an easy and consequential
> mistake.

### Version-dependent behaviour

Two behaviours in this document depend on TBC version. Both are legacy.

| Behaviour | Boundary | Relevance |
|---|---|---|
| Laser scanners and cameras calibrated **outside** TBC and imported as JSON | "up to the 5.21 version" *(TBC 24886, 24868)* | 5.21 predates 5.70, the oldest release Trimble publishes notes for. **Any recent installation calibrates in TBC** |
| **Select RMS File** prompt on a registration with no RMS file | "typically a project saved in TBC prior to version 5.80" *(TBC 27248)* | Affects **inherited legacy projects** only |

TBC renumbered from `5.x` to `YYYY.MM` after 5.90.1; releases run 2023.10 through 2026.10
*(TBC RN 2025.21)*.

### Licensing

| Release | Requires warranty or subscription valid to |
|---|---|
| 2025.21 | 1 November 2025 or later |
| 2026.10 | **1 June 2026 or later** |

*(TBC RN 2025.21, 2026.10)*. Visible at **Support ▸ License Manager**.

> **OBSERVED SOFTWARE BEHAVIOR**
>
> From TBC 2026.10, **Trimble ID sign-in requires two-step verification** — a code by email each
> time *(TBC RN 2026.10)*. Anyone signing in to TBC or Trimble Connect needs access to the
> account's email at that moment. Worth knowing before it stops a session.

## 4.4 POSPac MMS — and the licence gate that shapes the whole workflow

**Applanix POSPac MMS** computes the SBET from raw GNSS and inertial observations. Whether
Parametrix holds a licence determines which office workflow is even available.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> TBC's **Process Raw Trajectory Data** command computes an SBET inside TBC — but "the
> requirement to run the feature is to have the Applanix's POSPac MMS application (**from version
> 8.6 and a valid license**) installed alongside TBC" *(TBC 25943)*.
>
> **Generate POSPac Position Fixes** — the documented remedy for corridors with no usable GNSS —
> also requires POSPac, and a second processing pass in it *(TBC 24460)*.

| Function | Needs POSPac 8.6+ and a licence? |
|---|---|
| Import `.mxdb`, apply SBET or NAV | No |
| Generate Scans · Update Scans | No |
| Register a Run / Mission / Run-to-Run | No |
| Calibrate laser scanners and cameras | No |
| Cleanup, Mission Report, Trajectory Plots | No |
| Export and Publish | No |
| **Process Raw Trajectory Data** | **Yes** |
| **Generate POSPac Position Fixes (PFIX)** | **Yes** |
| **LiDAR QC Processing** | Not stated — see below |

> **PARAMETRIX DECISION REQUIRED**
>
> **Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?**
>
> Without it, the trajectory must be produced wherever POSPac lives — a subcontractor, a partner
> office, or not at all — and **one of the three documented remedies for degraded GNSS becomes
> unavailable** (§20).
>
> This is the single decision that most changes the shape of the office workflow.
> *(Register item 10; Appendix F)*

## 4.5 LiDAR QC — a capability decision, not a setting

**LiDAR QC Processing** uses the scan data itself as an aiding sensor to improve the trajectory
where GNSS is poor — similar in principle to SLAM *(TBC 28972)*. It is the only documented remedy
for degraded GNSS that needs **neither POSPac nor additional ground control** (§20).

It needs a workstation well beyond an ordinary one.

| | Minimum | Recommended |
|---|---|---|
| CPU | Intel Core i7 or i9 | Intel XEON |
| RAM | **128 GB** | **256 GB** |
| TEMP storage | 1 TB SSD on the PCI bus | 2 TB SSD M.2 on the PCI bus |
| Virtual memory | +1 TB SSD always available | +2 TB SSD M.2, or 4 TB combined |
| Paging file | — | initial = installed RAM, **maximum = 6 × installed RAM** |
| Also required | **MATLAB Runtime R2024b (24.2)**, installed after TBC | |

*(TBC 28972)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Is LiDAR QC a capability Parametrix intends to have?** It is a procurement question, not a
> software setting, and it only becomes urgent on a job with a genuinely bad GNSS corridor — at
> which point it is too late to buy a workstation. *(Register item 11)*

> **VENDOR CLARIFICATION REQUIRED**
>
> **Does LiDAR QC have its own POSPac dependency?** Trimble does not state one, but it is an
> Applanix technology and the topic directs configuration questions to the **Applanix Support
> Team** *(TBC 28972)*. *(Appendix F)*

## 4.6 Trimble Connect and TRCPS

**Publish to TRCPS** uploads point cloud data, trajectories and images from TBC to a **Trimble
Connect** project, through the **Trimble Desktop Utility (TDU)** installed alongside TBC. It
requires a Trimble ID, and uploads consume the account's Trimble Connect storage quota
*(TBC 29527)*.

It matters to this document for a reason beyond delivery convenience: **it is one of only two
paths that carries the trajectory out of TBC with the data** (§22, §23).

## 4.7 Reference documents

The full list is §1.6. Two gaps:

> **VENDOR CLARIFICATION REQUIRED**
>
> **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* and
> **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)* are both needed to
> complete the lever-arm procedure in §7, **if those accessories are fitted**. Neither is held.
>
> Note that the MX60 User Guide requires millimetre-level GAMS offsets and a **≥ 2.0 m baseline**
> where navigation data will be post-processed *(p.68)* — which is all survey-grade work.
> *(Appendix F)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We inventoried the hardware and the three pieces of software, and
> identified the two questions that decide what the office workflow can even look like: which
> configuration of MX60 this is, and whether Parametrix has a POSPac licence.
>
> **Why it matters.** Most equipment sections are reference material you never read twice. This
> one contains a fork in the road. If there is no POSPac licence, the trajectory has to be
> computed somewhere else and one of the three fixes for bad GNSS is simply unavailable — and
> you want to know that before you quote a job through a tree-lined corridor, not during it. The
> configuration question is similar: Core and Premium differ by a factor of four in image
> resolution, so a promise about imagery deliverables made without knowing which one is on the
> roof is a promise made blind.
>
> **What can go wrong.** The quiet failure here is the Export dialog having two tabs that both
> produce point clouds. The Mobile Mapping tab knows about runs; the Point Cloud tab does not,
> and lets you export a rectangle drawn across a view. Both produce a plausible LAS file. Only
> one of them was selected with any awareness of which data it was taking. §22 comes back to
> this.
>
> **What good looks like.** Before the first production job, someone should be able to state, on
> one page: the configuration and serial number, whether GAMS and DMI are fitted, which rack is
> on the vehicle, the TMI version, the TBC version, and whether a POSPac licence exists and where
> it lives. None of that is known today. All of it is a phone call to the dealer.

---

# 5. Coordinate Systems, Control, and Project Setup

## 5.1 What this section does and does not cover

The reader is a survey professional. Projections, datums, geoids, epochs, grid and ground
coordinates, and the design of a control network are taken as known.

**This section covers only what mobile mapping does differently** — and there are five things:

1. The trajectory is computed in a frame that may not be the project's (§5.3)
2. Epoch handling has a silent failure mode and a new user-settable control (§5.4)
3. Control must be **findable in a point cloud**, which is a different requirement from
   occupiable (§5.5)
4. Control must **bracket** the delivered extent, because one adjustment method does not
   extrapolate (§5.6)
5. Grid and ground are decided at export, and one of the two options withholds its scale factor
   (§5.7)

## 5.2 Set the project coordinate system before importing

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "Create a VCE project and if necessary, change the coordinate system so that it matches the
> coordinate system for the mobile mapping data to import." *(TBC 24886, 24460)*

> **IMPORTANT**
>
> Changing the CRS after import is possible in TBC generally, but by then every derived product —
> scans, registrations, exports — was computed in the previous frame. **Treat it as irreversible
> in practice** (§11.2).

### The database

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> The **Coordinate System Database v115** ships with TBC 2026.10. Selecting a predefined geoid
> model now enters the vertical datum name automatically *(TBC RN 2026.10)*.
>
> Two v115 entries relevant to US work: a grid transformation from **CSRN2025 (NAD83 2011) to
> CA SRS Epoch 2017.50** for California zones 1–6, and a **beta** Canadian **NATRF2022(CSRS)**
> with SGEOID2022-beta2.

## 5.3 The frame the trajectory is computed in

The trajectory is produced by POSPac, not by TBC (§12), and POSPac has its own view of the
project's coordinate system.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> | Condition | SBET filename |
> |---|---|
> | Datum and epoch **known** by POSPac | `sbet_[mission name].out` |
> | Datum and epoch **unknown** by POSPac | `sbet_[mission name]_[frame].out` — computed "first in ITRF00 and then in the datum and epoch of the project" |

> **The filename is a processing-path indicator and nothing more** (§12.4, §24 Layer 3). It tells
> you an additional transformation occurred. It does not tell you the parameters were right, that
> the project CRS is set up correctly, or that the result is accurate. The plain form is equally
> not proof of correctness.

> **FIELD TESTING REQUIRED · T10**
>
> **Establish which of Parametrix's normal coordinate systems POSPac recognises directly, and
> which trigger the ITRF00 path.** Answerable once, then known — and it determines whether an
> extra transformation is routine on Parametrix work or exceptional. *(Appendix I)*

### Computation mode and the reference frame

> **PARAMETRIX DECISION REQUIRED · D-19**
>
> **IN-Fusion+ Single Base or IN-Fusion+ PP-RTX?** *(TBC 25943; §12.3)*
>
> Single Base uses a local base station; PP-RTX uses Trimble's RTX corrections and needs no local
> base. The choice determines whether a base station must be occupied for every mission **and**
> the reference frame the solution is computed in — which feeds directly into §5.3.

## 5.4 Epoch

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> From TBC 2026.10: "When working with a time-dependent datum, you can now work at a specific
> epoch that is not the default reference epoch for the selected datum… **Note that this feature
> is intended for experienced users, as incorrect settings may lead to inaccurate results.**"
> *(TBC RN 2026.10)*

> **PARAMETRIX DECISION REQUIRED · D-21**
>
> **Which datum and epoch does Parametrix work in for mobile mapping, who sets it, and who checks
> it?**
>
> Epoch handling is not abstract in this workflow. It has a silent failure mode (§5.3) and now a
> user-settable control that Trimble itself flags as capable of producing inaccurate results.

## 5.5 Control that works for mobile mapping

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A **GCP** is "an accurately surveyed coordinate location for a physical feature that can be
> identified on the ground, e.g., **a corner on the pavement markings**." A **target** is "a point
> extracted from the acquired scan data." *(TBC 22905)*

> **IMPORTANT · this changes control design**
>
> A mobile mapping GCP must be **findable in a point cloud** at the density and incidence angle
> the vehicle produced. That is a different requirement from occupiable with a prism.
>
> | Works well | Works poorly |
> |---|---|
> | Painted stop-bar and lane-line corners — crisp intensity edges | A survey nail in asphalt — a few millimetres across, below cloud resolution |
> | Checkerboard, diamond, rectangular and L-shape (GV) target panels, for which TBC has templates *(TBC 22905)* | Small features at grazing incidence |
> | Painted arrow and legend corners | Anything that moves, is repainted, or is worn |

### Horizontal and vertical are separable

TBC lets a point participate as **Use XY**, **Use Z**, or both — independently (§17.2).

> A painted stop-bar corner is an excellent horizontal target and a poor vertical one: it lies in
> the road surface, the scan hits it at a grazing angle, and the picked height depends on which
> return the operator snapped to. **Use it for what it is good at.**

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** Answerable on a test site with features surveyed conventionally,
> and the answer will shape control design more than any software setting. *(Appendix I)*

## 5.6 Control layout

### The constraint that drives it

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A **Local** registration is "suitable for a local adjustment of a run, **not for systematic
> error along the run or for adjusting outside the ground control points set**." *(TBC 22905)*

> **CAUTION**
>
> **Local does not extrapolate.** Beyond the outermost control point the trajectory is not
> adjusted, and nothing indicates where the adjustment stopped. **Control must bracket the extent
> you intend to deliver, not merely fall within it.**

### The other scale indication Trimble gives

**Target-Bundle Adjustment** operates at **250 m** intervals when checked and **70 m** when
unchecked *(TBC 22905; §15.7)*. That is Trimble's own indication of the scale at which control
density matters.

### A structure for the decision

> **PARAMETRIX DECISION REQUIRED · D-16**
>
> **How many control points, at what spacing, and how many held as independent checks?**
>
> **No Trimble source states a minimum, a spacing, or a ratio.** TBC's software minimum is one
> control pair — a mathematical floor with no bearing on survey adequacy (§15.6).

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> - Control **bracketing** each end of the delivered extent, outside it where the corridor allows
> - Control along the corridor at an interval set from the project accuracy requirement, and
>   **tightened where GNSS is predicted to be degraded** (§6.3)
> - **Independent check points distributed, not clustered**, including at least one in each
>   distinct GNSS environment — open sky, tree cover, urban canyon
> - **A check point near each end**, where a Local adjustment stops working and where the smoother
>   had data on one side only (§2.2)
>
> No counts, spacings or ratios appear here deliberately. Those are the content of D-16.

### Reference practice, for information only

> **EXTERNAL REFERENCE — NOT PARAMETRIX PROCEDURE**
>
> The Queensland TMR *Mobile Laser Scanning Technical Guideline* (March 2023, CC BY 4.0) is a
> published transport-agency specification in the source set. It defines survey-grade,
> engineering-grade and asset-grade tiers, and for its higher tiers specifies control adjacent to
> the start and end of the project and at intersections of controlled roads *(TMR §11)*.
>
> **It is cited as an example of how another agency has answered D-16, not as a Parametrix
> standard and not as a Trimble requirement.** Parametrix's own accuracy tiers, if it adopts any,
> are D-16.

## 5.7 Grid, ground, and what the deliverable carries

Decided at export (§22.5), but it belongs in project setup because the client agreement depends
on it.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 11769, 27279)*
>
> | Option | Behaviour |
> |---|---|
> | **Scaling: Grid** | Points in the current projected CRS with the combined scale factor. **An associated `.txt` file specifies the coordinate system and scale factor used.** Trimble warns that re-importing it "may cause some inconsistencies due to a **double-scaling effect**" |
> | **Scaling: Ground** | Ground coordinates scaled from the 0,0 origin by the average combined scale factor. **"The scale factor is not exposed during export"** |
> | **ECEF export** | LAS or LAZ in ground-based scaling "that includes the project's global coordinate system information" |

> **IMPORTANT**
>
> **A ground-scaled export does not record the scale factor it used.** The recipient cannot
> convert without being told. Grid writes a sidecar; ECEF embeds the global CRS. Agree with the
> client which they are receiving, and make sure the file can say so.

> **PARAMETRIX DECISION REQUIRED · D-40**
>
> **What is Parametrix's default deliverable scaling, and what accompanies it?** *(§22)*

## 5.8 Project setup checklist

Full version in **Appendix C**.

| ☐ | Item |
|---|---|
| ☐ | Project CRS, vertical datum and geoid set and confirmed against the client requirement |
| ☐ | Epoch confirmed where a time-dependent datum is in use |
| ☐ | Control network computed and adjusted in the project CRS |
| ☐ | Control points selected for **findability in a point cloud**, not just occupiability |
| ☐ | Control **brackets** the delivered extent at both ends |
| ☐ | **Independent check points designated in writing, by the Project Surveyor, before processing** (§17.4) |
| ☐ | Grid or ground deliverable agreed with the client |
| ☐ | Accuracy requirement stated, in writing, per component |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We set up the project frame and planned the control — with two twists that
> do not arise in conventional work. The control has to be *visible in a point cloud*, not just
> occupiable, and it has to sit at both ends of the job rather than merely inside it.
>
> **Why it matters.** Control is what ties a mobile mapping dataset to the ground. Without it you
> have an internally consistent shape floating on whatever the satellites managed that day. And
> unlike a traverse, you cannot add a point later by going back and occupying it — the target has
> to be visible in data that was already collected.
>
> **What can go wrong.** Two things specific to this workflow. A survey nail is an excellent
> control point and a useless mobile mapping target: it is millimetres across and the cloud simply
> does not resolve it. Pick painted markings, panel targets, things with an edge. And if you set
> control inside the corridor rather than bracketing it, one of TBC's adjustment methods will
> quietly leave the ends unadjusted — the cloud there looks exactly like the rest and is on the
> original trajectory.
>
> **What good looks like.** Control at both ends, outside the delivered extent where you can
> manage it. Features you can actually point at in a cloud. Points held back as independent checks
> — chosen and written down before anyone processes anything, spread along the corridor and
> including the difficult stretches. And a clear agreement about grid or ground, because one of
> the export options does not tell the recipient which scale factor it used.

---

# 6. Mission Planning

## 6.1 The question this section answers

**What must be decided before anyone drives, so that the office has a defensible dataset to
process?**

Most of what goes wrong in the office cannot be fixed in the office. A GNSS-hostile stretch
driven once cannot be run-to-run registered. A corridor whose control sits inside the delivered
extent cannot be adjusted at the ends. Overlap that was not collected is not available.

## 6.2 Route and passes

### How many passes

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> The v1 draft stated a minimum of three passes on the pavement. **That figure is not traceable
> to a Trimble source in the current evidence set** and is carried here only so it is not lost.
> It must be confirmed, sourced or replaced before issue.

> **PARAMETRIX DECISION REQUIRED · D-41**
>
> **How many passes, and in what pattern, by roadway type?** The inputs are:
>
> - **Coverage and occlusion** — a single pass leaves the far side of parked vehicles, medians and
>   structures unmeasured
> - **Redundancy for run-to-run registration** (§16) — which needs "enough overlapping scan data
>   along the trajectories" *(TBC 25096)*
> - **LiDAR QC** (§12.7) — which needs runs "with overlap (parallel runs, or crossing runs)"
>   *(TBC 28972)*. **Without overlap, this remedy is unavailable in the office no matter what the
>   workstation can do**
> - Cost and road occupancy

> **IMPORTANT**
>
> **Two of the three degraded-GNSS remedies have to be arranged before you drive** (§20.3):
> control has to be surveyed, and overlap has to be collected. Discovering at QC that a corridor
> needed overlap you did not collect means going back.

### Direction of travel

Drive each pass in both directions where the corridor allows. It improves occlusion coverage, and
it is the geometry both the laser scanner calibration and LiDAR QC require (§14.3, §12.7).

## 6.3 GNSS planning

### Before mobilising

| Task | Why |
|---|---|
| **Check the almanac** for the planned window | Satellite geometry is knowable in advance; a poor window is avoidable |
| **Identify initialization locations** — a primary and a backup | §8.2 |
| **Map the GNSS-hostile stretches** | Below |

### Initialization locations need specific properties

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> - Open sky, away from buildings and canopy
> - Somewhere the vehicle can **safely sit still for 2–3 minutes**
> - Room to drive straight and perform dynamic manoeuvres afterwards (§8.2)

> **FIELD TIP**
>
> Scout them on aerial imagery before mobilising and pick two. Discovering that the chosen lot is
> fenced, occupied or under trees costs twenty minutes at the worst moment of the day.

### Map the hostile stretches, and estimate duration not length

Walk the route on imagery and mark tunnels, long underpasses, urban canyon, heavy canopy, deep
cuts and overhead structures.

> **For each, estimate how long the vehicle will be under it at collection speed.** That duration
> is the number that matters — a 300 m tunnel at 80 km/h is 13 seconds; the same tunnel at 20 km/h
> in traffic is nearly a minute.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Trimble publishes positioning performance at **no outage** and at a **60-second outage**
> *(MX60 UG Rev B, p.56)*.

> **IMPORTANT**
>
> **Trimble publishes nothing beyond 60 seconds.** A two-minute outage is not "twice as bad as one
> minute" — inertial drift is not linear, and beyond the published figure you are extrapolating
> past the manufacturer's stated envelope.
>
> Treat outages materially longer than 60 seconds as a **planning** problem, not a driving
> problem: additional control, planned overlap for LiDAR QC, DMI, or a different method for that
> segment (§20.7).

### Base station strategy

> **PARAMETRIX DECISION REQUIRED · D-42**
>
> **Own base on project control, VRS, RTX, or CORS post-processing — and what maximum baseline?**
>
> This interacts with D-19 (§5.3): **IN-Fusion+ Single Base** requires a local base station;
> **IN-Fusion+ PP-RTX** does not *(TBC 25943)*. The decision determines field logistics on every
> mission.

## 6.4 Timing

Three constraints that routinely conflict:

| Constraint | Wants |
|---|---|
| **GNSS geometry** | The best satellite window |
| **Imagery** | High sun, even light, no long shadows, dry surfaces |
| **Traffic** | Light traffic, so the corridor is not occluded by vehicles |

> **FIELD TIP**
>
> A good GNSS window at 07:00 is useless if the imagery is a wall of low-sun shadow, and an empty
> corridor at 05:00 is useless if it is dark. Where the three cannot be reconciled, decide which
> the deliverable actually depends on and say so in the project record.

> **PARAMETRIX DECISION REQUIRED · D-43**
>
> **Is night collection permitted, and under what conditions?** It solves the traffic-occlusion
> problem completely and makes the imagery unusable for interpretation. If it is permitted, the
> client must agree in advance and in writing.

## 6.5 Weather

Weather is a go/no-go decision, not a driving adjustment.

| Condition | Guidance | Source |
|---|---|---|
| **Rain or mist** | **Avoid operating the system** | *(MX60 UG Rev B, p.49)* |
| Wet pavement | Degrades laser returns; standing water may give no return at all | *(TMR §9.1)* |
| Heavy dew | Affects point cloud quality | *(TMR §9.1)* |
| Wet conditions, imagery | Water on the lens is grounds for rejection | *(TMR §10)* |
| Extreme dust | A dust filter is available — unpaved roads and mine sites *(Dust Filter Bulletin)* | |
| **Direct sun, stationary or < 10 km/h** | **Outside the rated operating envelope** | *(MX60 UG Rev B, p.53)* |

> **CAUTION**
>
> The Control Unit and Power Unit are **IP30 — not waterproof.** They live inside the vehicle for
> a reason. *(MX60 UG Rev B, p.53)*

> **PARAMETRIX DECISION REQUIRED · D-44**
>
> **One clear wet-weather rule.** Trimble says avoid operating in rain or mist; TMR says do not
> capture imagery in wet conditions; **neither defines "wet."**
>
> The rule should give the operator **explicit authority to stand down without seeking approval**.
> An operator who has to phone for permission will drive.

## 6.6 Access, traffic and safety

Mobile mapping removes the crew from the roadway. It does not remove the vehicle.

Plan for: road occupancy permits where required, the vehicle's behaviour in traffic at collection
speed (§8.5), locations where the vehicle must stop or turn, restricted or private access, and
any client or jurisdictional notification.

> **Vehicle operation, traffic control and site safety are governed by Parametrix's health and
> safety procedures and by the client's requirements. This SOP does not restate them and does not
> override them** (§1.3).

## 6.7 The calibration site

Plan it once and reuse it. Requirements are in **§14.3** and repeated here because they are a
planning task, not a processing one.

| Requirement | Value | Source |
|---|---|---|
| Four runs — two roads crossing, each driven both ways | | *(TBC 24886)* |
| **Crossing angle** | 90°, tolerance **± 30°** | *(TBC 24886)* |
| **Minimum run length** | ≥ **20 m each side** of the crossing | *(TBC 24886)* |
| **Ideal run length** | **80 m — 40 m each side** | *(TBC 24886)* |
| **Façades** present in each direction | | *(TBC 24886)* |
| **Vegetation** — few or none | | *(TBC 24886)* |
| For LiDAR QC as well: **250–300 m per strip**, structured scene, **open sky** | | *(TBC 28972)* |

> **FIELD TIP**
>
> A quiet crossroad with buildings on all four approaches, few trees, room for 125–150 m on each
> arm, and no traffic-control complications. Finding one is a morning's work. Finding one under
> schedule pressure, the week a calibration is overdue, is not.

> **PARAMETRIX DECISION REQUIRED · D-24**
>
> **Where is the Parametrix calibration site, and who maintains it?** *(§14.7)*

## 6.8 Identify what mobile mapping will not get

> **IMPORTANT · a professional judgement point**
>
> Part of planning is deciding what this method cannot deliver on this corridor:
>
> - Surfaces occluded from the roadway — behind walls, inside structures, beyond a crest
> - Detail finer than the point density at the achievable standoff
> - Features under a long GNSS outage where none of the §20 remedies is available
> - Anything requiring an accuracy the trajectory cannot support in that environment
>
> **Mobile mapping may not be the appropriate acquisition method for a particular segment.**
> Conventional survey, static scanning or total station work may produce a more defensible result
> there. Identifying that at planning is a professional judgement, and it is cheaper and more
> honest than delivering a weak segment mixed in with a good corridor.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Record, in the project file before mobilising: the segments where mobile mapping is expected to
> be marginal, the mitigation chosen for each, and the segments where another method is proposed.
> *(Register item 45)*

## 6.9 The planning record

Full checklist in **Appendix B**.

| ☐ | Item |
|---|---|
| ☐ | Corridor extent and pass pattern defined |
| ☐ | Control plan complete and bracketing the extent (§5.6) |
| ☐ | Independent check points designated in writing (§17.4) |
| ☐ | GNSS-hostile stretches mapped, with **outage duration** estimated |
| ☐ | Mitigation chosen for each — control, overlap, or another method |
| ☐ | Initialization locations identified, primary and backup |
| ☐ | Base station strategy fixed |
| ☐ | Collection window agreed against GNSS, imagery and traffic |
| ☐ | Weather go/no-go understood by the operator |
| ☐ | Calibration currency confirmed (§14.7) |
| ☐ | Segments unsuitable for mobile mapping identified and communicated |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We planned the drive: how many passes and in which directions, where to
> initialize, which stretches will lose satellites and for how long, when to collect, and what to
> do about the parts of the job this method will not handle well.
>
> **Why it matters.** Almost nothing here can be fixed later. If a tree-lined kilometre is driven
> once, the office cannot register it run-to-run, cannot refine it with LiDAR QC, and has only
> whatever control you happened to set. The decisions that determine whether the office has
> options are all made before anyone turns a key.
>
> **What can go wrong.** The one that costs a return visit is estimating obstruction by length
> instead of by time. A tunnel is not a distance problem; it is a duration problem, and the same
> tunnel in traffic can be four times the outage it is at speed. Trimble publishes performance at
> a sixty-second outage and nothing beyond, so anything longer is off the edge of the specification
> and needs a plan, not optimism.
>
> The other is quieter: planning a single pass because coverage looks adequate, and removing two of
> the three ways the office could have rescued a bad stretch.
>
> **What good looks like.** A route marked up with the hostile stretches and an estimated outage
> duration on each. A mitigation chosen for every one of them, before mobilisation. Two
> initialization spots, both scouted. Control that brackets the job. And an explicit note saying
> which parts of the corridor mobile mapping is not the right tool for — written down and sent to
> the client while there is still time to do something about it.

---

# 7. Field Preparation and Preflight

## 7.1 How often each task happens

| Task | Frequency |
|---|---|
| Power supply installation, Control Unit and Power Unit mounting | **Once per vehicle** |
| Roof bars, rack, lever arm measurement, Vehicle Preset | **Once per vehicle**, and after any change to the fitting |
| Sensor Unit mounting and cabling | **Every deployment** |
| Preflight checks | **Every mission** |

> **CAUTION**
>
> The one-time tasks are one-time **for a given installation**. Changing the rack, the roof bars,
> the vehicle, or the Sensor Unit's position on the rack **invalidates the lever arms and may
> invalidate the calibration** (§14.7). Treat any change to the fitting as a return to §7.2.

## 7.2 One-time installation

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> This subsection carries figures from the MX60 User Guide and the Roof Rack User Guide. The
> **figures are sourced**; the procedural framing around them is v1 draft material and should be
> confirmed against the installation as actually performed on the Parametrix vehicle.

### Power

| Parameter | Value | Source |
|---|---|---|
| Input voltage | 12–16 V DC | *(MX60 UG Rev B)* |
| Current at startup | **25 A at 12.8 V** (320 W) | *(MX60 UG Rev B)* |
| Current in operation | 12 A (160 W) | *(MX60 UG Rev B)* |
| **Supply rating needed** | **30 A or more** | *(MX60 QSG Rev B, p.4)* |
| Direct-connection fuse | 35 A, close to the battery | *(MX60 UG Rev B)* |

> **CAUTION**
>
> **An auxiliary battery as a backup power source is recommended** *(MX60 QSG Rev B, p.4)*. A
> supply interruption mid-mission does not merely stop collection — it ends the run, and with it
> the continuity the reverse-processing pass depends on (§8.7).

### Cabling and mounting

The Sensor Unit cable is **5 m**; the Control Unit run is about **3 m**. Route and secure cables
so they cannot chafe, catch, or be closed in a door. The Control Unit and Power Unit are **IP30 —
not waterproof** and live inside the vehicle *(MX60 UG Rev B, p.53)*.

### Roof bars, rack, and screw tightening

> **IMPORTANT**
>
> Follow the tightening method and sequence in the **MX Shock Absorbing Mounting Rack User Guide**
> or the **MX SCAN Roof Rack** documentation, as applicable. **Which rack is fitted is an open
> question** (§4.1) and matters: the published GAMS corner offsets apply to the standard rack
> **only** *(MX60 UG Rev B, p.68)*.

## 7.3 Lever arms and the Vehicle Preset

Lever arms are the fixed distance offsets between sensors. **They are measured, not estimated**
(§14.2) — TBC's calibration solves angles only.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> The vehicle frame convention *(TBC 25943, 24886)*:
>
> - **Positive X = forward driving direction**
> - **Positive Y = right side of the vehicle**
> - **Positive Z = downward**

> **WHY THIS MATTERS — Z is down**
>
> This trips people every time. A sensor mounted **above** the reference point has a **negative Z**
> in this convention. Getting the sign wrong puts twice the offset into the solution, in the wrong
> direction, and it will not look like a sign error downstream — it will look like a height
> problem.

### GAMS lever arm — only if fitted

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Where navigation data will be **post-processed** — which is all survey-grade work — the MX60
> User Guide requires GAMS offsets to **a few millimetres** and a baseline of **≥ 2.0 m**
> *(MX60 UG Rev B, p.68)*.

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* is
> not held. It is needed to complete this procedure if GAMS is fitted. *(Appendix I)*

### DMI lever arm — only if fitted

Measured in the vehicle frame from the reference point to **the centre of the tread where the
DMI-equipped wheel contacts the road** *(TBC 25943)*.

> **CAUTION**
>
> **The DMI scale factor carries a sign that depends on which side it is mounted:** positive on
> the **left**, negative on the **right** *(TBC 25943)*. It is entered in the office (§12.3) but
> determined by the installation, so **record which side it is on at installation** — the
> processor will not be able to see the vehicle.

> **VENDOR CLARIFICATION REQUIRED · V-6**
>
> The **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)* is not held. It
> contains the scale-factor value for the measured wheel diameter, which §12.3 needs.
> *(Appendix I)*

> **PARAMETRIX DECISION REQUIRED · D-46**
>
> **Where are the lever arms, the Vehicle Preset, and the installation configuration recorded, and
> who verifies them?** These values are entered once and used on every mission thereafter. An
> error in them is systematic, invisible, and persists until someone re-measures.

## 7.4 Mounting the Sensor Unit

> **CAUTION**
>
> **Two people are required.** The Sensor Unit weighs **24–28 kg** depending on configuration
> *(MX60 UG Rev B)*. It is awkward, it is expensive, and it is mounted above head height.

Mount, secure, connect, and confirm the unit is seated as it was when the lever arms were
measured. Any doubt about seating is a doubt about the lever arms.

## 7.5 Power-up

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** — sourced to
> *(MX60 UG Rev B; MX60 QSG Rev B)*

1. Vehicle ignition on
2. Confirm the power supply is live
3. Press and hold the **Control Unit** power button for **at least 15 seconds**
4. Sensor Unit and Control Unit LEDs **blink for about 10 seconds**
5. Wait for the system to reach a ready state before connecting to TMI

> **CAUTION**
>
> **Battery Protect** gives an audible warning below **10.5 V** and cuts power **90 seconds**
> later *(MX60 UG Rev B)*. If the alarm sounds during preflight, restore charge before doing
> anything else — a mission that starts on a marginal battery will end unexpectedly.

## 7.6 Connecting to TMI

TMI is served by the Control Unit and runs in **Chrome**:

| | |
|---|---|
| Capture | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |

*(TMI UG Rev L)*

Status reference — the colour meanings, warnings and indicators — is **Appendix E**.

## 7.7 Mission configuration in TMI

### Capture settings

> **VENDOR CLARIFICATION REQUIRED · V-2 · unresolved presentation conflict**
>
> The **Quick Start Guide** describes two separate MX60 controls — *Measurement Prog*
> `[500 kHz, 1000 kHz]` and *Line Speed* `[120 Hz, 200 Hz]` *(MX60 QSG Rev B, p.10)*.
>
> The **TMI User Guide Rev L** describes a single combined **Laser Mode** for the MX60
> *(TMI UG Rev L, p.29)*.
>
> **Which is current depends on the TMI version installed.** The operator should expect either and
> should record which was used. *(`CONFLICT-005`; Appendix I)*

> **Note also:** Trimble states the measurements-per-second values shown in the TMI interface are
> **rounded** *(TMI UG Rev L, pp.28–29)*.

### The dust filter

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A dust filter is available for the MX60 and is intended for **unpaved roads and mine sites**
> *(Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025)*.

### Lateral Range Limit

Settable 5–50 m *(TMI UG Rev L, p.29)*.

> **VENDOR CLARIFICATION REQUIRED · V-7**
>
> **Does the Lateral Range Limit have any documented effect on accuracy, or is it purely a
> data-volume tool?** *(Appendix I)*

## 7.8 Disk check

Confirm the exchangeable data disk is installed, has sufficient free space for the planned
mission, and is the intended disk.

> **CAUTION**
>
> **Never connect the USB cable while the exchangeable data disk is inside the Control Unit.**
> Remove the disk first *(MX60 UG Rev B, p.10)*.

> **PARAMETRIX DECISION REQUIRED · D-47**
>
> **What free-space margin is required before a mission is permitted to start?** A mission that
> fills the disk mid-corridor ends the run and takes the closing sequence with it (§8.7).

## 7.9 Preflight check

Full version in **Appendix C**.

| ☐ | Item |
|---|---|
| ☐ | Sensor Unit mounted, secured, seated as when lever arms were measured |
| ☐ | All cables connected, routed and secured |
| ☐ | Power supply live; battery healthy; no Battery Protect warning |
| ☐ | System powered up; LEDs through their startup sequence |
| ☐ | TMI reachable in Chrome; all sensors reporting present |
| ☐ | Vehicle Preset / lever arms correct for **this** vehicle and installation |
| ☐ | Capture settings configured and **recorded** |
| ☐ | Data disk installed, correct, with sufficient free space |
| ☐ | **Calibration currency confirmed** (§14.7) |
| ☐ | Optics clean — scanner windows and camera dome |
| ☐ | Initialization location confirmed available (§6.3) |
| ☐ | Weather within the go/no-go rule (§6.5) |
| ☐ | Field record started |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We got the vehicle ready: the sensor head mounted and secured, the offsets
> between sensors measured and entered, power confirmed, the software reachable, the disk in, and
> the optics clean.
>
> **Why it matters.** The lever arms are the part that deserves respect. They are measured once
> and then used on every mission for months. An error in them is systematic — it does not average
> out, it does not look like noise, and nothing downstream will point at it. The office will see a
> height that is slightly wrong everywhere and will probably blame the geoid.
>
> **What can go wrong.** The classic is the sign on Z. The convention has **Z positive downward**,
> so a sensor above the reference point takes a negative value. Get it backwards and you have put
> twice the offset in, the wrong way, into every mission from now until somebody re-measures.
>
> The other is treating a re-fit as routine. If the rack changed, the bars moved, the head was
> re-seated differently, or the unit went on a different vehicle, the lever arms are no longer
> the ones in the software — and the calibration may not be either.
>
> **What good looks like.** Two people on the head. Cables that cannot chafe or get shut in a
> door. A battery that is not marginal. Lever arms that were measured by somebody who knew Z was
> down, written down, and verified by somebody else. Clean optics. Enough disk for the whole
> mission with margin. And a note of exactly which capture settings were used, because in three
> weeks nobody will remember.

---

# 8. MX60 Data Collection

## 8.1 The shape of a mission

| Stage | What it is | §
|---|---|---|
| **Initialization** | Static period, straight run, dynamic manoeuvres | 8.2 |
| **Settling** | Additional time before recording anything that matters | 8.3 |
| **Collection** | The runs | 8.4–8.6 |
| **Closing sequence** | The mirror of initialization | 8.7 |
| **Shutdown** | Controlled, and confirmed | 8.8 |

> **The first and last five minutes of a mission determine the quality of the middle.** Everything
> in §2.2 about forward and backward filter passes comes down to this: the solution needs good
> observations at **both** ends, because the smoother works inward from both.

## 8.2 Initialization

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** — sourced to
> *(MX60 QSG Rev B, pp.13–14; MX60 UG Rev B)*

1. Position the vehicle at the initialization location — **open sky**, clear of buildings and
   canopy (§6.3)
2. Start the mission in TMI
3. **Remain stationary for 2–3 minutes**, logging static data
4. Drive **straight** for a short distance
5. Perform **dynamic manoeuvres** — a speed profile such as
   **0 → 50 → 20 → 50 → 20 km/h**, with turns
6. Watch for the navigation status to reach its ready indication
7. **Allow additional settling time — up to 10 minutes — before logging data that matters**

### With GAMS fitted

GAMS provides a direct heading measurement from two antennas and shortens initialization
considerably *(TBC 25943)*.

> **FIELD TIP**
>
> **Perform the full sequence anyway.** It costs a few minutes, it is what the Quick Start Guide
> describes, and the static period is doing more than heading determination (§8.3).

## 8.3 What the system is actually doing — and why green is not finished

**The static period** lets the GNSS receiver collect a clean, continuous set of observations and
resolve its ambiguities, and it gives the inertial filter a condition it can exploit: **the
vehicle's true velocity is zero.** Anything the motion sensors report while parked is therefore
pure error, measurable and removable.

**The dynamic manoeuvres** separate quantities that look identical at constant velocity. While
driving straight at a steady speed, a small attitude error and a sensor bias produce the same
signature. Change speed and direction and they stop looking alike, so the filter can tell them
apart. **Heading is the hardest component** and is what the turns are for.

> **IMPORTANT**
>
> **Green means the solution met the accuracy thresholds — not that it has finished converging.**
> That is why Trimble asks for up to ten more minutes before recording anything that matters
> *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day.** Do not spend it
> on the most important part of the corridor.

## 8.4 Recording runs

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **Minimum mission time: 30 minutes** *(MX60 QSG Rev B, pp.13–14)*.

> **A short corridor does not excuse a short mission.** If the collection itself is twelve
> minutes, keep the system running and logging navigation data to reach thirty. The trajectory
> solution improves with observation time, and closing early gives the office less to work with.

Runs are started and stopped within a mission. Each becomes a **Run** node in TBC (§11.3).

## 8.5 Driving

### Speed

| | Value | Source |
|---|---|---|
| **Recommended maximum, system operating** | **80 km/h (50 mph)** | *(MX60 UG Rev B)* |
| Absolute maximum, operating or not | 110 km/h (68 mph) | *(MX60 UG Rev B)* |

> **PARAMETRIX DECISION REQUIRED · D-48**
>
> **What collection speed, by deliverable type?** Speed determines point density along the
> corridor and the number of images per unit length. Trimble publishes a recommended maximum and
> an absolute maximum and **no guidance relating speed to deliverable quality**.
>
> *For consideration, not adopted:* collect at or near prevailing traffic speed up to 80 km/h,
> reducing where point density requires it. **Never exceed 80 km/h with the system operating.**

### Smoothness, lane selection and traffic

Drive smoothly. Sudden braking and sharp manoeuvres stress the inertial solution unnecessarily.
Choose the lane that gives the best line of sight to the features being collected, and remember
that the far side of a truck is not collected at all.

> **CAUTION**
>
> **Direct sun with the vehicle stationary or driving below 10 km/h is outside the rated operating
> envelope** *(MX60 UG Rev B, p.53)*. Extended idling in direct sun — at a signal, in a queue, or
> waiting for traffic control — is a real risk on a hot day.

### Reversing and U-turns

Plan turnarounds at locations where the vehicle can complete them without reversing under the
sensor's collection. Where a turn must happen inside the corridor, note it in the field record so
the office knows why the trajectory does what it does there.

## 8.6 Monitoring while driving

| Watch | For |
|---|---|
| **Navigation status** | Any degradation from the ready state |
| **Storage** | Remaining capacity against remaining corridor |
| **Sensor status** | A camera or laser that has stopped |
| **Audible alarm** | **Battery Protect — 78 seconds to restore charge** *(MX60 UG Rev B)* |

> **FIELD TIP**
>
> **Use TMI's Comments feature.** A note recorded at the moment — *"heavy canopy from here",
> *"stopped 4 min for traffic control"*, *"parked truck occluding the north side"* — is worth an
> hour of the office inferring it from residuals three weeks later.

### Recognising a bad collection before the day is wasted

Stop and reassess if: navigation status will not hold, a sensor has stopped reporting, storage
will not last the corridor, the battery is cycling into protection, or the conditions have moved
outside the go/no-go rule (§6.5).

> **The operator has authority to stand down.** A mission abandoned after twenty minutes costs
> twenty minutes. A mission completed on a degraded solution costs the office days and may cost a
> return visit.

## 8.7 The closing sequence

> **CAUTION · this is the most commonly skipped step in mobile mapping**
>
> The ending mirrors the beginning, and for the same reason. The post-processed trajectory is
> computed **forward and backward** and merged (§2.2). A degraded stretch in the middle of a
> mission is bracketed by good data on both sides and is bridged well. **A degraded stretch at the
> end has good data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** — sourced to
> *(MX60 QSG Rev B; MX60 UG Rev B)*

1. Finish the last run
2. Drive to an open-sky location
3. Perform **dynamic manoeuvres** — the mirror of initialization
4. **Remain stationary for 2–3 minutes**, logging static data
5. Close the mission in TMI
6. **Wait for the Control Unit power button light to go out — up to 90 seconds**

> **The whole sequence takes about five minutes and is the cheapest quality improvement available
> in the entire workflow.**

> **IMPORTANT**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and *then*
> driving to open sky achieves nothing.

## 8.8 Shutdown and confirming the data is written

Follow the documented shutdown. **Wait for the power button light to go out** before removing
power or the data disk *(MX60 UG Rev B)*.

> **CAUTION**
>
> Confirm the mission is written and closed before leaving the site. **While you are still at the
> site you can re-drive a run. Ten minutes down the road, you cannot.**

## 8.9 Mission record

The field record is a Parametrix artefact — **no software produces it**, and §9 and §11 both
depend on it.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Record per mission: date, operator, vehicle, mission ID; capture settings used; initialization
> location and time; each run with start/end and any incident; **GNSS conditions observed**;
> weather; traffic and occlusion events; anything not collected and why; the closing sequence
> performed; disk and free space at end.
> *(Register item 49)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We parked in the open and sat still for a few minutes, drove straight, then
> deliberately sped up, slowed down and turned — all so the system could work out three things it
> cannot see directly: how its inertial sensors are drifting, and exactly how the vehicle is tilted
> and pointed. Then we drove the corridor, and finished by repeating the whole start sequence
> backwards.
>
> **Why it matters.** It is like resection. The instrument has to know where it is and which way it
> is facing before any shot means anything. The difference is that here the answer degrades over
> time and distance, so you establish it at the start, let it settle, and re-establish it at the
> end.
>
> Sitting still is the part people skip and it is doing real work: parked, the system knows its
> true speed is zero, so anything its motion sensors report is pure error it can measure and
> remove. The manoeuvres do the same job for orientation — at a steady speed in a straight line, a
> small tilt error and a sensor bias look identical to the software; change speed and direction and
> they stop looking identical.
>
> **What can go wrong.** Green is a threshold, not a finish line. It means the solution met the
> accuracy figures, not that it has converged, which is why Trimble asks for up to ten more minutes
> before you record anything that matters. The first data of the day is the weakest data of the
> day.
>
> And the closing sequence gets skipped, because the job is done and everyone wants to leave. The
> office computes the trajectory forwards and backwards and merges them — so the end of the mission
> is an anchor for the whole reverse pass. Five minutes. You cannot add it afterwards.
>
> **What good looks like.** A proper static period in genuinely open sky. Manoeuvres that actually
> change speed and direction rather than a gentle curve. Settling time taken, with the important
> part of the corridor driven after it rather than before. Steady driving at a sensible speed.
> Comments recorded as things happen. A full closing sequence. And confirmation the data is written
> before the vehicle leaves — because on site a re-drive is twenty minutes, and from the office it
> is a day.

---

# 9. Field Quality Checks

## 9.1 What can and cannot be checked in the field

> **The distinction matters more than the checks themselves.** A great deal of what determines
> dataset quality cannot be assessed until the trajectory is post-processed in the office — which
> may be days later, and always after the vehicle has left.

| Can be checked in the field | Cannot be checked until the office |
|---|---|
| The mission recorded and closed | **Post-processed trajectory quality** (§12.4) |
| All planned runs exist | **Point cloud accuracy against control** (§15, §17) |
| Data written to disk and readable | **Whether GNSS degradation was bridged adequately** |
| Coverage — was the corridor driven | **Point density at the achieved standoff** |
| Sensors reported present throughout | **Imagery detail sufficiency** |
| Gross imagery problems — obstruction, contamination | **Colour fringing, boresight symptoms** (§19.5) |
| Free space and disk health | **Anything requiring the SBET** |

> **IMPORTANT**
>
> **Nothing available in the field confirms that the data is of survey quality.** The field checks
> confirm that the data **exists, is complete, and is readable**. That is a genuinely valuable
> thing to confirm before leaving — and it is not the same as confirming it is good.

## 9.2 The checks, in order

### Before leaving the initialization location

| ☐ | Check |
|---|---|
| ☐ | Navigation status reached its ready indication |
| ☐ | **Settling time allowed** (§8.3) |
| ☐ | All sensors reporting present in TMI |
| ☐ | Storage sufficient for the planned mission |

### During collection

| ☐ | Check |
|---|---|
| ☐ | Navigation status held |
| ☐ | No sensor dropped out |
| ☐ | No Battery Protect event |
| ☐ | Storage tracking against remaining corridor |
| ☐ | Comments recorded as events occurred (§8.6) |

### Immediately after closing the mission — before the vehicle moves

| ☐ | Check |
|---|---|
| ☐ | **Closing sequence performed in full** (§8.7) |
| ☐ | Mission closed in TMI |
| ☐ | **Power button light out** before power or disk is disturbed (§8.8) |

### Before leaving site

| ☐ | Check |
|---|---|
| ☐ | **Mission folder present on the disk, with a plausible size** |
| ☐ | **Run count matches what was driven** |
| ☐ | Raw POS data present in `POS_1/raw` (§11.3) |
| ☐ | Base station data captured, if a local base was used |
| ☐ | Field record complete (§8.9) |
| ☐ | **Any re-drive decided and performed now** (§9.4) |

> **CAUTION**
>
> **Do these before the vehicle leaves the corridor.** Every item above is recoverable on site in
> minutes and costs a mobilisation from the office.

## 9.3 Coverage verification

The one substantive quality check available in the field.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Before leaving, confirm against the plan (§6.9):
>
> - Every planned pass was driven, in the planned direction
> - The corridor was driven end to end, including any extent beyond the deliverable required to
>   bracket control (§5.6)
> - **Planned overlap was actually collected** — this is the one that removes office options if
>   missed (§20.3)
> - Sections not collected, and why, are recorded
>
> *(Register item 50)*

> **IMPORTANT**
>
> **Overlap is the check worth being pedantic about.** If a GNSS-hostile stretch was planned for
> two passes and got one, **both LiDAR QC and run-to-run registration become unavailable** in the
> office (§20). There is no software warning and no way to tell later except by looking at what is
> there.

## 9.4 The re-collection decision

> **IMPORTANT · this is a field decision with office consequences**
>
> Re-driving a run while the vehicle is on site costs minutes. Re-driving from the office costs a
> mobilisation and, on a corridor requiring traffic control, considerably more.

> **PARAMETRIX DECISION REQUIRED · D-51**
>
> **What triggers a re-drive, and who decides?**
>
> Candidate triggers, offered for decision, not adopted:
>
> - Navigation status degraded through a section that matters
> - A sensor dropped out mid-run
> - A run interrupted by a power or storage event
> - Significant occlusion by traffic through a section that matters
> - The closing sequence not completed
> - Conditions moved outside the weather rule mid-mission (§6.5)
>
> The decision needs to state **whether the operator may re-drive on their own judgement**, or
> must seek approval. An operator who must phone will usually drive on.

## 9.5 What the field record must carry into the office

Field notes are not administrative. **Three later sections depend on them**, and no software
produces any of it:

| Field record item | Where the office needs it |
|---|---|
| Planned versus driven extent | §11.4 — covered distance check; §24 Layer 1 |
| Run count and which runs are which | §11.5; §16 pair selection |
| **GNSS conditions observed** | §12.4 — corroborates the RMS picture; §18.4 |
| Occlusion and traffic events | §18.5 — explains a gap that is not a defect |
| Sections not collected, and why | §24 Layer 1; the client conversation |
| Capture settings used | §13; §24 Layer 3 |
| Incidents, stoppages, re-drives | §26 — troubleshooting a dataset after the fact |

> **FIELD TIP**
>
> The most useful single thing an operator can write is **why the corridor looks the way it does**
> at any point where it is unusual. Three weeks later, the office is looking at a stretch with
> poor residuals and cannot tell whether it was tree canopy, a stopped truck, or a system problem.
> One sentence at the time settles it.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** Before the vehicle left, we confirmed the data exists, is complete, is
> readable, and covers what it was supposed to cover — and we wrote down what the conditions were
> like.
>
> **Why it matters.** Almost nothing about *quality* can be judged in the field. You cannot tell
> whether the trajectory is good until it has been post-processed in the office, days later. What
> you can tell is whether the data is there. Those are different questions, and confusing them is
> how people talk themselves into leaving.
>
> **What can go wrong.** The expensive miss is overlap. If a difficult stretch was meant to get two
> passes and got one, two of the three office remedies for bad GNSS have just become unavailable —
> and nothing warns anyone. It looks like a complete dataset. It is a complete dataset with fewer
> options.
>
> The other is the field record. Three weeks on, the office is staring at a stretch with poor
> residuals and no way to know whether it was tree cover, a parked truck, or a fault. One sentence
> written at the time — "heavy canopy from the bridge to the school" — saves a day of guessing and
> sometimes a return visit.
>
> **What good looks like.** Every planned pass driven, in the planned direction, including the
> overlap. The mission closed properly and confirmed written. A run count that matches what was
> actually driven. A short honest note of conditions, incidents, and anything not collected. And
> any re-drive done *now*, while the vehicle is still here and it costs twenty minutes.

---

# 10. Data Transfer and Project Organization

## 10.1 What is on the disk

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*

```
TMX<serial>-<mission id>/
  ├── Backup/
  ├── Base/                 base station RINEX — .YYo observation, .YYn .YYg ephemeris
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── NavProc_01/           navigation processing outputs
  ├── POS_1/
  │     ├── raw/            raw IMU + GNSS — posl_*.000, .001, .002 …
  │     └── realtime/
  ├── Extcal.json           the calibration file
  ├── readme_*.txt
  ├── <mission>.mxdb        the mission database
  ├── <mission>.tridb
  └── <mission>_*.log
```

> **Everything the office can ever do derives from this folder.** The `.mxdb` is the index; the
> `POS_1/raw` files are the raw observations from which the trajectory is computed; `Extcal.json`
> is the calibration state the mission was collected under.

## 10.2 Removing the disk

> **CAUTION**
>
> - **Wait for the Control Unit power button light to go out** before removing the disk (§8.8)
> - **Never connect the USB cable while the exchangeable data disk is inside the Control Unit** —
>   remove the disk first *(MX60 UG Rev B, p.10)*

## 10.3 Offload and verify — before anything else happens

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> 1. **Copy, do not move.** The source disk remains the source until a verified copy exists in two
>    places
> 2. **Verify the copy** — file count and total size at minimum; a checksum comparison where the
>    tooling allows
> 3. **Confirm the `.mxdb` opens** — importing into a scratch TBC project is the definitive test
>    (§11)
> 4. **Confirm `POS_1/raw` is present and non-empty.** Without it there is no post-processed
>    trajectory and the mission is NAV-only (§11.2)
> 5. **Confirm base station data** is present if a local base was used
> 6. **Only then** consider the source disk available for reuse
>
> *(Register item 52)*

> **CAUTION**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.** A disk cleared for the next mission is not recoverable,
> and the mission is not re-drivable without a mobilisation.

## 10.4 Backup before processing

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> **Take the raw-data backup before any processing begins**, not after. Processing writes into the
> project and, with **Backup SBET Next to MXDB** enabled (§12.4), into the raw data folder
> alongside the `.mxdb`.
>
> A backup taken after processing has begun is a backup of a partly-processed state — which is
> usually fine and is occasionally exactly the wrong thing to have. *(Register item 52)*

## 10.5 Project organisation

> **PARAMETRIX DECISION REQUIRED · D-53**
>
> **What is the Parametrix folder structure, naming convention and storage location for mobile
> mapping projects?**
>
> **No structure, path, server location or naming convention is proposed in this document**, and
> none should be inferred from the examples above — those are Trimble's own folder names as
> written by the system.
>
> The decision must cover at least:
>
> | Element | Why it matters here specifically |
> |---|---|
> | Where raw mission data lives, and for how long | Re-processing requires it; §25 |
> | Where the TBC project lives | It is large, and it is the provenance record (§23) |
> | Where **`NAVPROC/`** outputs live | The SBET, its report, and the frame/epoch log (§12.4) |
> | Where the **numbered `sbet_*_reg_####.out`** files live | The registration lineage (§23.3) |
> | Where **Parametrix records** live — control/check designation, residuals, delivery record | **None of these have a software home** (§23.6) |
> | Naming that survives a person leaving | — |
>
> *(Register item 53)*

> **The structure matters more in mobile mapping than in most survey work**, because several of
> the provenance artefacts identified in §23 are small files sitting loose in a project folder.
> A convention that keeps them together is the difference between an auditable job and a
> reconstruction exercise.

## 10.6 Chain of custody

> **PARAMETRIX DECISION REQUIRED · D-54**
>
> **Is a chain-of-custody record required for mobile mapping data, and in what form?**
>
> Relevant where data may be used in a dispute, where a client requires it, or where the
> deliverable supports a design decision with legal consequence. The provenance findings in §23
> mean that **the project and the Parametrix record are the evidence** — the deliverable may not
> be able to speak for itself.

## 10.7 Preparing for the next mission

| ☐ | Item |
|---|---|
| ☐ | Verified copy exists in two locations |
| ☐ | `.mxdb` confirmed to open |
| ☐ | Field record filed with the data |
| ☐ | Disk cleared **only after** the above |
| ☐ | Disk health checked; free space sufficient for the next mission |
| ☐ | System powered down correctly |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We got the data off the vehicle, proved the copy is good, and put it
> somewhere it can be found again.
>
> **Why it matters.** This is the only irreversible step in the whole workflow. Everything in the
> office can be redone — you can regenerate scans, redo a registration, re-export. You cannot
> un-erase a disk. And a mobile mapping mission is not re-drivable at reasonable cost: it means a
> vehicle, a crew, traffic control on some corridors, and the same GNSS and lighting conditions
> you had the first time.
>
> **What can go wrong.** The disk gets cleared for the next job before anyone has actually opened
> the mission. A file count looks right, the copy seems fine, and the `.mxdb` turns out to be
> truncated. Importing it into a scratch TBC project takes five minutes and is the only test that
> genuinely proves the data is there.
>
> The other one is `POS_1/raw`. Without those files there is no post-processed trajectory — the
> mission is stuck on the real-time solution, which is not survey grade. It is a folder nobody
> looks at because nothing opens it directly.
>
> **What good looks like.** Two verified copies before the source disk is touched. The mission
> opened once, in TBC, to prove it. The field record filed alongside the data rather than in
> somebody's notebook. And a folder structure someone else can navigate in three years, which
> matters here more than usual because several of the things that prove how the data was processed
> are small files sitting loose in a project folder.

---

# 11. Import into TBC

## 11.1 What import does, and what it does not

Importing a mission brings the **mission database** into a TBC project and makes its contents
visible in Project Explorer. It does **not** produce a point cloud, and it does not compute
anything.

> **The most common misunderstanding at this stage:** after import you can see runs,
> trajectories and capture devices, and the Plan View draws a line along the corridor. It looks
> like data. It is an index. The point cloud does not exist until Generate Scans is run (§13).

## 11.2 Before you import — the project must be right first

> **IMPORTANT**
>
> **Set the project coordinate system before importing the mission.** Trimble states the
> prerequisite as "Create a VCE project and if necessary, change the coordinate system so that it
> matches the coordinate system for the mobile mapping data to import" *(TBC 24886, 24460)*.
>
> Changing it afterwards is possible in TBC generally, but on a mobile mapping project it means
> every derived product — scans, registrations, exports — was computed in the previous frame.
> §5 covers the coordinate system decisions; this is simply the point at which they become
> irreversible in practice.

The trajectory must also be decided before or during import (§12). A mission can be imported
with either:

- the **post-processed SBET** — the normal case for survey work, or
- the **real-time NAV** trajectory, "in case POSPac processing not possible" *(TBC 24460)*

> **CAUTION**
>
> **NAV is a fallback, not an option.** It is the trajectory the system computed in the vehicle,
> in real time, without the benefit of a reverse pass or base station corrections. It is
> appropriate for a quick look and for checking coverage. It is not appropriate for a survey
> deliverable, and a project that reaches export still on NAV has skipped the single largest
> quality step in the workflow.

## 11.3 The data objects, and where they appear

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 20736-1, 22503, 22554)*

The mission on disk, as written in the field:

```
TMX<serial>-<mission id>/
  ├── Backup/
  ├── Base/                 base station RINEX, if collected      .YYo .YYn .YYg
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── NavProc_01/           navigation processing outputs
  ├── POS_1/
  │     ├── raw/            raw IMU + GNSS — posl_*.000, .001, .002 …
  │     └── realtime/
  ├── Extcal.json           the calibration file
  ├── readme_*.txt
  ├── <mission>.mxdb        the mission database — this is what you import
  ├── <mission>.tridb
  └── <mission>_*.log
```

*(TBC 25943)*

In Project Explorer after import:

```
Mobile Mapping
  └── <mission id>
        ├── Capture Devices          Camera 3 Back Down, Camera 4 360°, Laser Left, Laser Right
        └── Run 0, Run 1, Run 2 …
              └── Sbet                the imported trajectory
                    └── (scans appear here after Generate Scans)
```

> Note the shape. **Scans are children of a trajectory, not of a run.** That is the structural
> fact that makes tree position meaningful evidence of which trajectory a cloud was built on
> (§23) — and it is why a run with two trajectories has two independent sets of scans beneath it.

## 11.4 Mission properties worth reading at import

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*

Selecting the mission node shows properties including start and stop times, duration, **covered
distance**, and the **active trajectory file**.

> **FIELD TIP**
>
> **Read the covered distance against what the crew said they collected.** It is the fastest
> available check that the mission is complete — a corridor the crew reported as 14 km that
> imports as 9 km means a run is missing, a file did not transfer, or a collection stopped
> without anyone noticing. Catching that at import costs a minute. Catching it at QC costs a
> return visit.

## 11.5 What to verify before going further

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> At import, before any processing:
>
> 1. **Project coordinate system** matches the control network and the client's requirement
> 2. **Covered distance** is consistent with the field record (§11.4)
> 3. **Run count** matches the field record — a mission with fewer runs than the crew logged has
>    lost data in transfer
> 4. **The active trajectory** is the intended one, and is SBET rather than NAV unless there is a
>    recorded reason
> 5. **Capture Devices** lists the sensors expected for the configuration (§4.1) — a missing
>    camera or laser here means a sensor was disabled or failed in the field
> 6. **Base station data** is present in `Base/` if the trajectory will be processed in-house
>    (§12)
>
> **Not adopted.** Six checks, none taking more than a minute, all cheaper now than later.
> *(Register item 18)*

## 11.6 Multiple missions in one project

A TBC project can hold several missions, and both **Register Run to Run** *(TBC 25096)* and
**LiDAR QC** *(TBC 28972)* can work across them. Runs are identified in those commands as
`<last two digits of mission ID> - Run <n>`.

> **FIELD TIP**
>
> Those last two digits come from the `.mxdb` filename — `TMX50320120101-000033.mxdb` is mission
> `33` *(TBC 25096)*. On a project with several days of collection, write the mapping down. The
> pair selectors in Register Run to Run show only the two digits, and choosing the wrong run
> because two missions ended in similar numbers is an easy and expensive mistake.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We pointed TBC at the mission database the vehicle wrote, and it read the
> index: which runs exist, which sensors were on, how far the vehicle travelled, and which
> trajectory is currently attached. It drew the route on the map.
>
> **Why it matters.** This is the moment the project's coordinate system gets locked in for
> practical purposes, and it is the cheapest moment in the entire workflow to notice that
> something is missing. Everything downstream is built on what came in here.
>
> **What can go wrong.** The thing to watch for is that it all looks fine. A mission missing two
> runs imports without complaint and draws a perfectly convincing line on the map — just a
> shorter one than it should be. Nobody notices until the deliverable is short a section of
> corridor, by which time the crew and the vehicle are three jobs away. The other one is
> importing with the real-time NAV trajectory attached because the post-processed SBET was not
> ready, and then simply never going back. NAV works. It produces a cloud. It is just not
> survey-grade, and nothing in the software will remind you.
>
> **What good looks like.** The covered distance matches what the crew wrote down. The run count
> matches. The sensors listed are the ones that were supposed to be running. The trajectory
> attached is the post-processed one. Five minutes of looking, before any processing starts.

---

# 12. Trajectory Processing

This is where the accuracy of the whole dataset is decided. Everything after it either applies
the trajectory or improves it — nothing else creates it.

## 12.1 The three routes, and the licence that chooses between them

| Route | Where it runs | Requires |
|---|---|---|
| **POSPac MMS, externally** | A workstation with POSPac | A POSPac licence |
| **Process Raw Trajectory Data, inside TBC** | TBC | **POSPac MMS 8.6+ installed alongside TBC, with a valid licence** *(TBC 25943)* |
| **Real-time NAV** | Already computed in the vehicle | Nothing — but see §11.2 |

> **Both post-processing routes require POSPac.** TBC's in-application command is a convenience
> wrapper, not an alternative to owning the software. There is no route to a survey-grade
> trajectory that does not involve a POSPac licence somewhere.

> **PARAMETRIX DECISION REQUIRED**
>
> **Where does trajectory processing happen, and who does it?** See §4.4. Without a licence the
> answer is "somewhere else," and the project schedule has a dependency in it that should be
> visible at quoting time rather than at processing time. *(Register item 10)*

## 12.2 What Process Raw Trajectory Data does

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> "The feature enables you to compute a Smoothed Best Estimate of Trajectory (SBET) within TBC
> using the raw inertial, GNSS satellites, and base station data, without having to use the
> Applanix's POSPac MMS application and to import the trajectory into TBC."

Run from the **Mission** node context menu. TBC loads the raw POS data automatically.

### Inputs

| Input | Where it comes from | Notes |
|---|---|---|
| **Raw POS data** | `POS_1/raw/` — `posl_*.000`, `.001`, `.002` … | Selected automatically. "TBC will sequentially process the entire series of valid POS logged data files starting from the first file selected" |
| **Base station RINEX** | `Base/` — the `.YYo` observation file | **Must be imported into TBC before running the command** |

> **CAUTION**
>
> **Import the observation file only.** The `Base/` folder also contains `.YYn` and `.YYg`
> ephemeris files. Trimble states: **"Do not import the ephemeris files into TBC."**
> *(TBC 25943)*

## 12.3 Settings — with Trimble's stated defaults

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> "TBC automatically fills the below fields with the information found in the POS logged files,
> like GNSS/Inertial/DMI Sensors Lever Arms and GAMS Baselines settings which are set in the
> vehicle before the data collection. **Double check the settings values and if needed modify
> them.**"

### Computation Mode

| Mode | What it uses |
|---|---|
| **IN-Fusion+ Single Base** | "high-accuracy GNSS positioning using corrections from a nearby local base station" |
| **IN-Fusion+ PP-RTX** | "high-accuracy GNSS positioning globally using Trimble's satellite or internet-based RTX corrections, **without the need for a local base station**" |

No default is stated.

> **PARAMETRIX DECISION REQUIRED**
>
> **Single Base or PP-RTX, and on what basis?** This is a survey decision with real consequences
> — it determines whether a base station must be occupied for every mission, and it determines
> the reference frame the solution is computed in.
>
> It interacts with §12.6: a PP-RTX solution is computed in Trimble's RTX frame and epoch, which
> is not necessarily the project's. *(Register item 19)*

### The rest

| Setting | Values | Default |
|---|---|---|
| **Time Start / Time End** | GPS seconds of the start week | — |
| **Initialization Mode** | VNAV · **Gyro-compassing** · GAMS · GAMS and Gyro-Compassing | **Gyro-compassing** |
| **Multipath** | Low (good coverage) · **Medium** · High (urban canyon, narrow streets, dense foliage) | **Medium** |
| **Antenna Manufacturer / Type** | Read from the RINEX automatically | — |
| **GAMS** | On/off, with a lever arm and a standard deviation | Dimmed if GAMS was disabled during acquisition |
| **DMI** | Lever arm, standard deviation, scale factor, scale factor SD | Dimmed if DMI was disabled during acquisition |
| **LiDAR QC (Refine with scans)** | On/off | Off — see §12.7 |
| **Generate QC Report** | On/off | — |

### The MX60 antenna model — check this one

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "the rover antenna model should be **Tallysman/33-3970 GNSS** for an MX9 (or MX50) system and
> **Trimble 112735 GNSS for a MX90 (or MX60) system**." *(TBC 25943)*

> **IMPORTANT**
>
> This is retrieved automatically from the RINEX file, which means it can be retrieved *wrongly*
> if the RINEX carries a different antenna descriptor. **Verify it reads Trimble 112735 before
> computing.**
>
> An antenna model defines the phase-centre offsets and variations the solver applies. An
> incorrect model can therefore **introduce a systematic antenna-height and reference error into
> the trajectory solution.** The evidence supports that statement and no more precise
> characterisation of the resulting bias.
>
> The practical point is enough: **the mistake occurs upstream, it is a single field nobody looks
> at, and it can contaminate everything derived from that trajectory** — the point cloud, the
> registration that partially absorbs it, and the deliverable.

### DMI settings, if fitted

| Setting | Trimble's statement |
|---|---|
| **Scale factor sign** | "DMI installed on the **left** side of the vehicle: scale factor is **positive**… **right** side: scale factor is **negative**" |
| **Scale factor value** | From "the Trimble MX Distance Measuring Indicator Installation & Operation Manual, in the DMI Scale Factor section" — **a manual Parametrix does not hold** (§4.7) |
| **Scale factor SD** | **Default 5 %.** "Increase the setting if the scale factor is not known with 5% accuracy, and **set it to 100% if it is not known at all**" |

> **FIELD TESTING REQUIRED · T12**
>
> **The 5 % default is only correct if the wheel diameter was actually measured.** If the value
> came out of a manual for a nominal tyre, 5 % is an assertion of accuracy nobody verified, and
> the solution is weighting the DMI accordingly.
>
> Trimble provides the honest escape hatch — set it to 100 % if unknown. Determine which case
> applies before trusting the default. *(Appendix E)*

### Multipath

> **FIELD TESTING REQUIRED · T11**
>
> **Medium is the default and is described as being for degraded coverage.** Trimble's own
> descriptions place Low with "good GNSS coverage" and Medium/High with "a degraded GNSS
> coverage, such as in urban canyon, narrow streets, dense foliage."
>
> Running Medium on an open-sky rural corridor may be a harmless conservatism or an unnecessary
> de-weighting of good observations. Untested. *(Appendix E)*

### Lever arms and the vehicle frame

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "**Lever Arm** refers to the displacement between two body coordinate frames… expressed as a
> three-dimensional vector."
>
> Measured in the vehicle frame, from the external reference point to the DMI wheel contact patch
> or the GAMS antenna phase centre, in metres along three axes:
>
> - **Positive X = forward driving direction**
> - **Positive Y = right side of the vehicle**
> - **Positive Z = downward**
>
> *(TBC 25943)*

> **The same convention governs every boresight angle in §14.** Roll about X, pitch about Y,
> heading about Z, with Z pointing down. It is worth fixing in mind once.

## 12.4 Outputs, and a filename that means something

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> | Condition | Output filename |
> |---|---|
> | Datum and epoch **known** by POSPac | `sbet_[mission name].out` |
> | Datum and epoch **unknown** by POSPac | `sbet_[mission name]_[frame].out` — "created, **first in ITRF00 and then in the datum and epoch of the project**" |

> **IMPORTANT · this is the trap in this section**
>
> **The second filename is an indicator, and nothing else surfaces it.**
>
> It tells you POSPac did not recognise the project's datum and epoch, computed the solution in
> ITRF00, and then transformed it into the project frame. That is a **processing-path indicator**,
> and it is the only one the software gives.
>
> **Be precise about what it does and does not tell you:**
>
> | It tells you | It does **not** tell you |
> |---|---|
> | That POSPac used the frame-transformation workflow | That the transformation parameters were right |
> | That an additional transformation step occurred | That the project CRS is set up correctly |
> | Where to direct scrutiny | That the final point cloud is accurate |
>
> A plain `sbet_[mission].out` is equally not proof of correctness — it means only that POSPac
> recognised the datum and epoch it was given, which may still be the wrong ones.
>
> **Look at the SBET filename after every computation, and treat it as a flag for review rather
> than as a verdict.**

> **FIELD TESTING REQUIRED · T10**
>
> Establish which of Parametrix's normal coordinate systems POSPac recognises directly, and which
> trigger the ITRF00 path. This is answerable once and then known. *(Appendix E; §5)*

### Where the outputs go

| Output | Location |
|---|---|
| SBET | `NAVPROC/Export/` under the project folder |
| Processing report | `NAVPROC/Report/` |
| **Backup SBET Next to MXDB** *(option)* | Copies the SBET **and a log containing the frame and epoch information used to create it** into the raw data folder beside the `.mxdb` |

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Enable Backup SBET Next to MXDB.** That log is the only artefact found anywhere in the
> workflow that records the frame and epoch a trajectory was computed in, and it lives with the
> raw data rather than inside a TBC project that may later be cleaned up (§21) or lost.
>
> **Not adopted.** *(Register item 20; §23, §25)*

### The SBET is coloured by its own quality

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "The created SBET trajectory file will be **colored according to the values of the computed
> RMS**." *(TBC 25943)*
>
> The RMS comes from `smrmsg_xxx.out`, a file POSPac produces that "describes the accuracy of the
> post-processed solution and contains the position, orientation and velocity RMS after
> smoothing" *(TBC 27248)*.

Colour settings are at **Mobile Mapping ▸ Trajectory Settings**, where **Rendering Settings** can
be set to **Default** (a flat colour — red for real-time, green for processed) or to **RMS
values**, with user-defined ranges and colours. Settings are persistent.

> **This is the single most useful QC view in the entire workflow and it costs nothing.**
>
> Switch the trajectory to RMS colouring and look at the corridor. The stretches where the
> solution struggled are drawn in a different colour, in plan, before any point cloud exists.
> That tells you where to concentrate control (§17), where to expect trouble at registration, and
> whether a degraded-GNSS remedy (§20) is going to be needed — while there is still time to do
> something about it.

> **OBSERVED SOFTWARE BEHAVIOR**
>
> "If the mission contains some registrations then the **modified segments will be colorized with
> the 'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
> `smrmsg` file, so the adjusted stretches lose their RMS colouring. Incidentally, this makes the
> extent of a registration's effect visible in plan — which is one way to see where a **Local**
> adjustment stopped adjusting (§15.5).

## 12.5 Trajectory Plots

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 27415)*
>
> "After computing a SBET with the Process Raw Trajectory Data command, the resulting plots open
> **only once**. The **Trajectory Plots** feature lets you open the plots without running again
> the command."

At **Mobile Mapping ▸ Reports ▸ Trajectory Plots**, or the command `MissionTrajectoryPlots`. It
is greyed out until an SBET has been computed, and opens plots per mission where several exist.

> **FIELD TIP**
>
> The plots open once and then vanish, which is why people think they are gone. They are not —
> but a processor who does not know this command exists will re-run a multi-hour computation to
> get them back.

## 12.6 Datum and epoch

§5 covers the coordinate system decisions. Two things belong here because they are specific to
trajectory processing.

**The ITRF00 path (§12.4)** is the practical expression of an epoch mismatch, and the filename is
its only symptom.

**Dynamic datum epoch selection**, added in TBC 2026.10:

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "When working with a time-dependent datum, you can now work at a specific epoch that is not the
> default reference epoch for the selected datum… **Note that this feature is intended for
> experienced users, as incorrect settings may lead to inaccurate results.**" *(TBC RN 2026.10)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Which datum and epoch does Parametrix work in for mobile mapping, and who sets it?**
>
> Trimble itself flags the epoch control as capable of producing inaccurate results if set wrongly.
> Combined with the ITRF00 path above, epoch handling is not an abstract datum concern in this
> workflow — it is a live setting with a silent failure mode. *(Register item 21; §5)*

## 12.7 LiDAR QC — refining the trajectory with the scan data

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 28972)*
>
> "LiDAR QC is an advanced trajectory processing technology that, **similar to LiDAR SLAM**, is
> using scan data as an aiding sensor to improve georeferencing accuracies in areas of poor GNSS
> coverage or in areas where overlapping scans are not perfectly matching. Based on a robust and
> iterative least square adjustment, LiDAR QC generates 3D Voxels that are matched in overlap
> scan regions. The result of this iterative process is solving the constant IMU boresight angles
> and making corrections to the post-processed trajectory (position and orientation)."

Enabled by the **LiDAR QC (Refine with scans)** checkbox in Process Raw Trajectory Data, which
adds a LiDAR QC tab. Requires **MATLAB Runtime R2024b (24.2)** and a substantial workstation
(§4.5).

### Settings

| Setting | Values | Default |
|---|---|---|
| **Range** | Minimum and maximum LiDAR measurement distance used | **3 m to 100 m** |
| **Noise** | 5, 10, 50, 80, 100, 200 mm | **5 mm for MX50/MX60**; 10 mm for MX9/MX90 |
| **Lasers** | Left · Right · All | **All** |

> **FIELD TESTING REQUIRED · T13, T14**
>
> **T13 — the 3–100 m range.** The MX60's useful range and the range over which scan geometry
> usefully aids a trajectory solution are different questions. 100 m may include returns too noisy
> to help.
>
> **T14 — Lasers = All.** Trimble's own text beside the setting says using both "can increase
> computation time without significantly improving the accuracy, as it compares the left versus
> right laser of isolated runs." **The default contradicts the guidance printed next to it.**
> *(Appendix E)*

### Running it

Select runs from the Project Tree **with overlap — parallel runs, or crossing runs** — click
**Add**, set the parameters, **Compute** *(TBC 28972)*.

### The calibration pattern

Trimble prescribes a specific acquisition geometry for LiDAR QC:

| Element | Requirement |
|---|---|
| **Area** | "a structured scene such as a residential area with detached houses and objects within the LiDAR sensor's maximum range"; "open sky terrain for good GNSS satellite visibility" |
| **Strips** | "two perpendicular strips. **Each strip will consist of two runs (one in each direction)**" |
| **Strip length** | **250–300 m** |

*(TBC 28972)*

> This is materially the same geometry the laser scanner calibration requires (§14.3) — four runs,
> two orthogonal pairs, both directions. **One site can serve both**, which matters because
> establishing a calibration site is a real piece of work (§6).

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We took the raw GNSS and inertial observations the vehicle recorded,
> combined them with base station data, and computed the path the sensor head actually followed —
> forward through time, backward through time, and merged. That path is the SBET, and every point
> in the finished cloud will be hung off it.
>
> **Why it matters.** This is the step that sets the accuracy ceiling for the job. Nothing later
> improves the raw measurements; registration bends the path to fit control, but it cannot invent
> information that was never collected. A trajectory computed from good observations, with the
> right antenna model and a sensible base station, is a dataset you can work with. One computed
> from a weak solution is a dataset you will fight for the rest of the project.
>
> **What can go wrong.** Three things, and all three are silent. The antenna model is read
> automatically from the RINEX and can be read wrongly — the MX60 wants **Trimble 112735**, and a
> wrong entry puts a height bias into everything that no later check will attribute to its real
> cause. The output filename quietly tells you whether POSPac understood your coordinate system:
> `sbet_mission.out` means yes, `sbet_mission_frame.out` means it worked in ITRF00 and then
> transformed, and nothing else will mention it. And the DMI's 5 % default accuracy is only true
> if somebody actually measured the wheel.
>
> **What good looks like.** After the computation, switch the trajectory to RMS colouring and look
> at it in plan. A good job is mostly one colour, with the degraded stretches where you expected
> them — under the overpass, through the tree cover — and short. That picture, available before
> any point cloud exists, tells you where to put control, where registration will struggle, and
> whether you are going to need one of the remedies in §20. It is five seconds of work and it is
> the best early warning the software gives you.

---

# 13. Generate Scans

## 13.1 What it does

**Generate Scans** applies the trajectory to the raw scanner data and produces the point cloud.

```
   TMX                 Generate Scans                RWCX
   polar scan data  ──────────────────────────►   point cloud
   ranges + angles      + the trajectory           XYZ, intensity, colour, normals
   sensor-relative                                 georeferenced
```

> **This is where the trajectory meets the measurements.** Before it, the scanner data is a set
> of ranges and angles relative to a sensor that was moving. After it, every return has a
> coordinate. Change the trajectory and the same raw data produces a different cloud — which is
> the whole basis of registration (§15) and of Update Scans (§13.6).

### The MX60 has no MTA stage

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22503)*
>
> MX50 and MX60 convert **TMX → RWCX in one step**. MX9 and MX90 go RXP → TMX → RWCX in two, and
> the intermediate stage requires **MTA** (Multiple Times Around) range-ambiguity correction.

> **The MX60 workflow has no MTA configuration and no MTA failures.** If you encounter TBC
> documentation about configuring a GPU driver for MTA correction *(TBC 23856)*, it does not
> apply to this system. Mentioned because it is prominent in the TBC help and causes confusion.

## 13.2 Running it

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*

Select a run or a mission in **Project Explorer** and choose **Generate Scans** from the context
menu. Scans appear beneath the trajectory node they were computed from.

Generating at mission level processes all runs. Generating at run level processes one — useful
when a single run has been re-collected or when testing filter settings before committing to a
full mission.

## 13.3 Filters

The Filters pane is where most of the judgement in this command lives, and where most of the
untested defaults are.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*

| Filter | What Trimble says it does |
|---|---|
| **Range Min / Max** | Discards returns outside the distance window |
| **Isolated Points** | Removes points with too few neighbours |
| **Fog** | Removes returns caused by fog |
| **Sun** | Removes returns caused by direct sunlight on the sensor |
| **Reflective Panels** | "Removes the noise before and after a target" |
| **Dust** | Removes airborne dust returns *(Product Bulletin, January 2025)* |

Two presets are offered — **Default** and **High Quality** — where High Quality enables Fog, Sun
and Reflective Panels.

> **FIELD TESTING REQUIRED · T1–T5**
>
> **The filter defaults are the largest block of untested settings in the workflow.** Each removes
> real returns under conditions that may or may not have occurred.
>
> **T1 — Default vs High Quality.** Trimble states what each preset contains and gives no
> selection criteria. High Quality enables three filters unconditionally, including on data
> collected in conditions where none of them applies.
>
> **T2 — Isolated Points.** Trimble's own text contradicts itself: the prose says the filter is
> on, the Restore Default Values behaviour says off.
>
> **T3 — Reflective Panels.** "Removes the noise before and after a target." **Does it also
> remove legitimate retro-reflective returns from signs and line marking?** This bears directly on
> sign inventory and retroreflectivity work, where those returns are the deliverable.
>
> **T4 — Range Max.** The MX60 default matches the scanner's maximum range at the lower pulse
> rate. The User Guide separately warns that real-world range is shorter in bright sunlight and at
> oblique incidence *(MX60 UG Rev B)*, so points may be retained well beyond useful range.
>
> **T5 — Fog and Sun.** Both remove real returns under defined conditions. Applying them when
> those conditions did not occur removes valid data.
>
> *(Appendix E)*

> **CAUTION**
>
> **Filtering is not reversible within a scan set.** A filtered return is not flagged, it is
> absent. Recovering it means regenerating the scans with different settings — which is cheap in
> effort and expensive in time on a large mission, and impossible once the raw data has been
> archived and the project cleaned up (§21).
>
> **Generate one representative run with the intended settings and look at the result before
> committing a whole mission.**

## 13.4 Colorization

Scans can be generated with colour from the imagery, or without.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Colour is exported "if the scans have been generated with the color option set to on"
> *(TBC 23339, 22501)* — so the decision made here propagates all the way to the deliverable.

> **FIELD TESTING REQUIRED · T6**
>
> The colouriser offers a forward versus backward camera preference with no stated selection rule.
> *(Appendix E)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Are scans generated coloured by default?** Colorization costs processing time and disk, and
> is not needed for every deliverable — but generating without it and discovering later that the
> client wanted coloured points means regenerating the mission. *(Register item 22)*

## 13.5 The Results record

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*
>
> A **Results of Scan Generation** dialog records, per run: the **filters applied**, the **range**,
> and whether **colorization** was on.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Capture the Results of Scan Generation into the project record.** It is the only artefact that
> states which filters produced a given cloud, and filter choice is a defensible-or-not decision
> that a reviewer may need to see years later.
>
> **Not adopted.** *(Register item 23; §23, §25)*

## 13.6 Update Scans — switching a cloud onto a different trajectory

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22638)*

**Update Scans** regenerates scans against a different trajectory. It is how a registration (§15)
reaches the point cloud.

| | **Generate Scans** | **Update Scans** |
|---|---|---|
| Purpose | Create scans from raw data | **Switch existing scans to a different trajectory** |
| Filters pane | Yes | **No** |
| Trajectory choice | The run's current trajectory | **Switches between the imported trajectory and an adjusted one** |

Updated scan stations carry a **`_reg_####`** suffix — for example
`Run_14_Laser Right_reg_0001 (S3)`.

> **IMPORTANT**
>
> **Registration alone changes nothing about the point cloud.**
>
> A registration produces a new trajectory node. The scans sitting under the old trajectory are
> still the old scans, in the old positions. Until Update Scans is run, **the cloud you would
> export is the unregistered one.**
>
> This is the most consequential sequencing fact in the office workflow, and the mistake it
> guards against is invisible: the project contains a registration, the residuals were good, the
> processor moved on — and the delivered cloud never received the adjustment.

Update Scans works in **both directions**: it switches between imported and adjusted, so it is
also the mechanism for reverting.

> **The exception.** **Register Run to Run** has an **Update Scans** checkbox inside the command,
> which regenerates the Run to Adjust's scans inline *(TBC 25096; §16.5)*. That is the only place
> where the two steps merge.

## 13.7 Recovering failed scans

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 28155)*
>
> **Recover Mobile Mapping Scans** exists for scan generation that failed or was interrupted.
> Treated as a recovery procedure in §26.

## 13.8 A hazard that lives in §22 but starts here

> **CAUTION · cross-reference to §22.3**
>
> Some TBC export paths do **not** export the scans this command produced.
>
> Trimble states, identically in two export topics: with **Export timestamps = No**, "the exported
> scans are the ones processed with the Generate Scans feature"; with **Export timestamps = Yes**,
> "the exported scans are **reprocessed from the raw data** and directly written to the LAS format
> files" *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated by Trimble.** Both readings are
> consistent with the text.
>
> The consequence for this section: the filters you chose here, the colorization decision you
> made, and — critically — the registration you applied through Update Scans may or may not be
> present in an export made with timestamps enabled.
>
> **FIELD TESTING REQUIRED · T18 — the highest-priority test in this document.** See §22.3 and
> Appendix E.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We combined the vehicle's computed path with the raw scanner measurements
> to produce an actual point cloud — the first time in the workflow that the data has coordinates.
> We also chose which returns to keep and whether to colour them from the imagery.
>
> **Why it matters.** Up to now the project has been an index and a line on a map. This is the
> data. It is also the first point at which the job becomes expensive to redo: regenerating a
> large mission with different filters is hours of processing, and on a corridor job it can be
> overnight.
>
> **What can go wrong.** The filters are the quiet problem. Several of them remove genuine
> returns under conditions that may not have applied on the day — a fog filter on a clear morning
> is throwing away data to solve a problem you did not have. And there is a specific worry for
> anyone doing sign or line-marking work: the Reflective Panels filter is described as removing
> noise around a target, and nobody has established whether it also removes the retro-reflective
> returns that *are* the deliverable. Nothing warns you; the points are simply not there.
>
> The bigger trap is sequencing, and it comes later in the job. Registering a mission does not
> change the point cloud. It produces a better path and leaves the cloud where it was. If nobody
> runs Update Scans, the project contains a perfectly good registration with good residuals, and
> the data you export is the unregistered version. It looks identical. It is centimetres out.
>
> **What good looks like.** Generate one run first, look at it, and only then commit the mission.
> A good result has the noise you expected removed and the features you care about still present —
> check the signs, check the line marking, check a wall at range. And when a registration is
> applied later, the scans sitting under the registered trajectory carry a `_reg_` suffix. If you
> cannot see that suffix, the adjustment has not reached the data.

---

# 14. Calibration

## 14.1 Why this section sits here

Calibration is **periodic, not per-project.** It belongs to the system, not to the job, and most
missions will not involve it at all.

It appears here, between scan generation and registration, for two reasons: TBC's calibration
procedures **consume generated scans** as their input, so it cannot be explained before §13; and
a reader meeting registration in §15 needs to already know what a boresight angle is.

> **Calibration and registration are different things and are easy to confuse.** Calibration
> determines the fixed angular relationship **between sensors on the vehicle**, and is valid for
> months. Registration ties a **particular mission's trajectory** to surveyed control, and is
> valid for that mission only. A current calibration does not reduce the control requirement, and
> a good registration does not indicate the calibration is sound.

## 14.2 What is calibrated, and what is not

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24886, 24868)*
>
> "A system calibration describes the estimation of the exact translation and orientation of each
> sensor referring to an internal virtual reference point of the sensor head. For a Trimble MX
> series mobile mapping system, each sensor has its individual set of:
>
> - **Lever arms** (offsets in translation — X, Y and Z): X-axis in the driving direction to the
>   front, Y-axis in the driving direction to the right, Z-axis in the down direction
> - **Boresight angles** (offsets in orientation around the X, Y and Z axes, respectively Roll,
>   Pitch and Heading)"
>
> And the key sentence:
>
> **"In a calibration process, the offsets in translation are known for all sensors and do not
> need to be estimated while the offsets in rotation need to be."**

> **Calibration estimates angles only.** Lever arms are fixed by manufacture and are known. That
> is why a calibration can be computed from scan agreement without any surveyed control — the
> unknowns are three rotations per sensor, and they show up as systematic disagreement between
> overlapping scans.

### Why boresight error is the error that grows with range

An error in the boresight angle of a scanner is an error in **which direction it thinks it is
pointing**, and it displaces points **in proportion to range** — exactly as described in §2.3.

> That proportionality is geometry, not a system specification. Multiplying any small angular
> error by any distance gives the lateral displacement at that distance, and the arithmetic is
> the reader's to do for the ranges and tolerances of a particular job. **No Trimble source in the
> set states a boresight error budget for the MX60**, and none is asserted here.

> **WHY THIS MATTERS**
>
> Boresight error is systematic, not random. It does not average out with more data — collecting
> twice as much produces twice as much consistently displaced cloud. And because it scales with
> range, it appears as a dataset that is excellent near the vehicle and progressively wrong
> further out, which reads as "the scanner is noisy at range" rather than as a calibration
> problem.

## 14.3 Calibrating the laser scanners

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24886; also documented at TBC 20716)*

### Where it runs

"In TBC, up to the 5.21 version, laser scanners are calibrated out of the application and the
calibration values are imported into TBC from a JSON format file. The **Calibrate Laser
Scanners** feature allows you to calibrate the laser scanners of the MX series mobile mapping
systems in TBC."

> Version 5.21 predates 5.70, the oldest release Trimble still publishes notes for (§4.3). **Any
> recent TBC calibrates in the application.** The JSON import path (§14.5) remains available and
> is how a calibration moves between projects.

### The acquisition geometry

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24886 / 20716)*
>
> The mission must contain **four runs: two in one direction (forward and backward), and two
> orthogonal (forward and backward as well)** — in practice, two roads crossing.
>
> | Run | Direction |
> |---|---|
> | Run_0 / Run_1 | Along the first road, forward and backward |
> | Run_2 / Run_3 | Along the crossing road, forward and backward |
>
> **Site requirements:**
>
> | Requirement | Value |
> |---|---|
> | **Crossing angle** | As close to **90°** as possible, tolerance **± 30°** |
> | **Minimum run length** | **At least 20 m from each side** of the crossing |
> | **Ideal run length** | **80 m long — 40 m from each side** of the crossing, "for an efficient calibration" |
> | **Overlap** | Enough overlap between runs |
> | **Façades** | Present **in each direction**, in sufficient quantity |
> | **Vegetation** | A few or none, ideally |

> **WHY THIS MATTERS**
>
> **Façades are the measurement.** A boresight error shows up as the same flat vertical surface
> appearing in two places when scanned from opposing directions. No façades, no signal.
> **Vegetation is the opposite** — soft, non-repeating returns that add noise to exactly the
> run-to-run comparison the calibration depends on.

Compare with the LiDAR QC pattern *(TBC 28972; §12.7)*:

| | Laser scanner calibration *(TBC 24886)* | LiDAR QC *(TBC 28972)* |
|---|---|---|
| Runs | Four — two orthogonal pairs, both directions | Four — two perpendicular strips, both directions |
| Crossing angle | **90°, ± 30°** | Perpendicular |
| Length | **≥ 20 m each side; ideally 80 m total** | **250–300 m per strip** |
| Scene | **Façades in each direction; little or no vegetation** | Structured — "a residential area with detached houses and objects within the LiDAR sensor's maximum range" |
| Sky | Not stated | **Open sky for good GNSS satellite visibility** |

> **The two are compatible, and LiDAR QC is the stricter on length.** A site of two roads crossing
> near 90°, with 125–150 m of façade-lined street available on each arm, satisfies both.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Establish one calibration site that satisfies both patterns** — two streets crossing near 90°,
> façades on all four approaches, little vegetation, **125–150 m of usable street on each arm**
> (satisfying LiDAR QC's 250–300 m strip), open sky, drivable in both directions without
> traffic-control complications.
>
> The two requirements are compatible and the stricter one (LiDAR QC) should govern. Establishing
> such a site is real work — reconnaissance, a traffic plan, possibly permission — and doing it
> once, well, before it is needed under schedule pressure is worth more than the procedure it
> supports.
>
> **Not adopted.** *(Register item 24; §6)*

### The result, and how to read it

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24886)*
>
> The calibration reports:
>
> - **Overall Overlap** — the percentage of points used against those generated
> - **Overall RMS** — the average of the RMS between the scans used
> - **Per-pair RMS**, in **Tangential, Orthogonal and Vertical**

The same three-axis convention as run-to-run registration (§16.6), and it diagnoses the same way:
a large tangential component points at along-track scale or timing, a large orthogonal component
at heading, a large vertical component at pitch or height.

### The rule that governs acceptance

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886)*

> **This is the origin of the principle that governs §15, §16, §18 and §24.** Trimble states it
> here and repeats it verbatim in the run-to-run registration topic. It is not a hedge — it
> follows from what a residual measures. **A number can prove failure. A number cannot prove
> success.**

### The visual check

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24886)*
>
> Check **Cutting Plane View**. A plane named **Mobile Mapping Cutting Plane** is created, visible
> as a yellow plane in 3D View at the beginning of the first run pair (`Run_0 <-> Run_1`).
>
> - Change rendering to **Scan Color** — one colour per scan
> - Increase **Point Size**
> - Adjust **cutting plane thickness**
> - Drag the slider along the run pair, looking at the gap between the two clouds
> - Then **choose `Run_2 <-> Run_3` in the Calibrate Laser Scanners dialog and check that pair
>   too**
>
> Only then **Apply**.

> **IMPORTANT**
>
> **Both run pairs must be checked.** The dialog presents one pair at a time and the second is
> easy to skip. The orthogonal pair is the one that constrains heading — the component a single
> direction of travel cannot resolve.

> **FIELD TESTING REQUIRED · T16**
>
> Cutting plane thickness: Trimble's screenshots show `0.030` in the calibration topic and `5.000`
> in the run-to-run topic, with no stated basis. Too thin shows nothing; too thick buries a real
> offset in a band of points. *(Appendix E)*

## 14.4 Calibrating the cameras

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24868, 20728)*

The camera frames on an MX-series vehicle are the **360° camera frame**, the **vehicle frame**,
the **oblique camera frame (1/2)** and the **down-looking camera frame**.

As with the scanners, "up to the 5.21 version, cameras are calibrated out of the application and
the calibration values are imported into TBC from a JSON format file. The **Manual Camera
Calibration** feature allows you to calibrate the cameras of the MX series mobile mapping systems
in TBC **by entering the calibration values directly**."

### The procedure

1. Create a VCE project, import the `.mxdb`, apply the SBET
2. **Generate scans from at least one run**
3. In Project Explorer select a camera under **Capture Devices**
4. **Manual Camera Calibration** from the context menu
5. Pick a position on a run's trajectory in Plan View. The camera view displays at that location
6. Enter a value in **Heading**, **Pitch** or **Roll** and press Enter — **the camera view updates
   immediately**

| Input | Step |
|---|---|
| Arrow up / down | ± 0.001° |
| Ctrl + arrow, Page Up / Page Down | ± 0.01° |
| Mouse wheel | ± 0.001° |
| Ctrl + mouse wheel | ± 0.01° |

> **This is a visual, iterative alignment, not a computed adjustment.** The operator nudges the
> orientation until the imagery lines up with the point cloud, watching it move. It is closer to
> collimating an instrument than to running a least-squares solution — and like collimation, the
> quality depends on the care taken and is not captured by any residual.

### Where the values end up

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24868)*
>
> In the camera properties, as **Boresight refinement** — distinct from **Boresight
> installation**, which is the as-built value. Lever arm installation and lever arm refinement
> appear alongside, and are equal, because lever arms are not estimated (§14.2).

## 14.5 The calibration file

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22920)*
>
> "In TBC, a **JSON** format file contains the parameters **before** calibration (**Installation
> Matrix**) and the parameters **after** calibration (**Refinement Matrix**), of **each sensor** of
> the mobile mapping system."
>
> - **Import Calibration** — mission node context menu. Applies refined parameters to the project
> - **Export Calibration** — mission node context menu. Writes the refined parameters computed in
>   TBC

The MX60 also accepts a boresight JSON in the field through TMI's **Calibration Import**, via USB1
*(TMI UG Rev L, p.18)*.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Export the calibration JSON after every calibration and archive it outside the TBC project**,
> named with the system serial number and the calibration date.
>
> It is the complete calibration state of the system in one small file, it can be imported into
> any subsequent project, and it is the only portable record of what the system's angles were on
> a given date. A project cleanup (§21) or a lost workstation should not take it with them.
>
> **Not adopted.** *(Register item 25; §25)*

## 14.6 The calibration record — and the date

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24868)*
>
> The **Mission Report** contains a **Capture devices** table carrying, per sensor:
>
> | Column |
> |---|
> | Boresight installation |
> | **Boresight calibration** |
> | Lever arm installation |
> | Lever arm calibration |
> | **Date of calibration** |

> **This is the only record found anywhere in the workflow that states when the system was last
> calibrated, and it is attached to the mission rather than to the system.** Every mission carries
> a statement of the calibration state it was processed under. That is a genuinely useful audit
> property and it costs one report to capture (§23).

## 14.7 When to recalibrate

> **PARAMETRIX DECISION REQUIRED**
>
> **On what interval, and after what events, is the MX60 recalibrated?**
>
> No Trimble source in the set gives an interval. The available guidance is general and comes from
> the User Guide's periodic verification recommendation (§18.7), which says to check "regularly"
> and "especially before starting an extensive data acquisition campaign" *(MX60 UG Rev B, p.7)*
> without defining either.
>
> The decision needs to cover:
>
> - A **routine interval**
> - **Triggering events** — a knock, a rack change, a vehicle change, removal and refitting
> - **Whether daily removal of the Sensor Unit counts as disturbing the calibration.** This is the
>   live question for Parametrix: if the head comes off the vehicle every night, the answer
>   determines whether calibration is a periodic activity or a routine one
> - **Who owns currency** (§3.3 D-3.6)
>
> *(Register item 26; Appendix F)*

> **VENDOR CLARIFICATION REQUIRED**
>
> **Does removing and refitting the Sensor Unit disturb the calibration?** And what symptoms
> indicate a calibration has drifted? *(Appendix F)*

## 14.8 Calibration is not validated by control

A warning against a natural but wrong inference.

TBC's laser scanner calibration derives boresight angles from **scan-to-scan agreement**. No
surveyed control participates. A calibration can therefore be internally excellent and carry a
systematic error common to all four runs.

The independent check on calibration is the periodic target verification in §18.7 — retro-
reflective targets previously surveyed by total station — which is a different activity with a
different geometry, and one Parametrix has not yet scheduled.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We worked out the exact angles at which each sensor is bolted to the
> vehicle relative to the inertial unit. Not where they are — those distances are known from
> manufacture — but which way they point, to a hundredth of a degree. For the scanners TBC solves
> it by driving a specific four-run pattern and making the overlapping clouds agree. For the
> cameras the operator nudges the orientation by hand and watches the image line up with the
> points.
>
> **Why it matters.** A boresight error is an aiming error, and aiming errors get worse with
> distance. A hundredth of a degree is nothing at the kerb beside the vehicle and over a
> centimetre at a building face 60 m away — on every point, always in the same direction. It does
> not look like noise and it does not average out. It looks like a dataset that is crisp up close
> and untrustworthy further out.
>
> **What can go wrong.** The big one is believing the numbers. TBC reports an overall RMS and
> per-pair residuals, and Trimble says plainly — twice, in two different topics — that good
> numbers do not prove the calibration worked, though bad numbers prove it failed. You have to
> look. And you have to look at **both** run pairs: the dialog shows one at a time, and the
> orthogonal pair is the one that pins down heading, which driving in a single direction cannot
> resolve at all.
>
> The other failure is confusing this with registration. A current calibration does not reduce
> your control requirement by one point. It is the difference between an instrument that is
> properly collimated and an instrument that is properly oriented on a known station — you need
> both, and one does not substitute for the other.
>
> **What good looks like.** Drag the cutting plane along the run pair and see one wall, not two —
> on both pairs. Residuals of similar size in all three directions, rather than one much larger
> than the others, which would be telling you something specific about which axis is off. And the
> whole thing recorded: export the JSON, keep it with the serial number and the date, and know
> that every mission report afterwards will say which calibration it was processed under.

---

# 15. Registration

This is the section the rest of the office workflow exists to support. Read §2 and §13 first.

## 15.1 What registration is, in this system

**Registration adjusts the trajectory.** It does not move points.

TBC takes surveyed ground control points, pairs each with a point the operator picks in the
point cloud, and computes a correction to the trajectory that reduces the difference between
the pairs. The output is a **new trajectory**, stored beside the imported one. The existing
point cloud is untouched until you deliberately recompute it (§13.6).

> **This is the single most important structural fact about TBC registration, and it surprises
> people from a static scanning background.** In static work, registration moves scans. Here it
> produces a better path, and the points follow only when you ask them to.

### The three commands

They are **not interchangeable**. Each solves a different problem with a different kind of
observation.

| Command | What constrains it | Scope | Section |
|---|---|---|---|
| **Register a Run** | Surveyed GCPs ↔ targets picked in the cloud | One run | §15.3 |
| **Register a Mission** | The same, with each GCP reusable across runs and passes | A set of runs at once | §15.4 |
| **Register Run to Run** | **Cloud-to-cloud overlap** against a fixed reference run | Pairs, batched | **§16** |

> **IMPORTANT**
>
> Register Run to Run uses **no surveyed control at all**. It makes two runs agree with each
> other. Two runs can agree perfectly and both be in the wrong place. It is a relative tool, and
> §16 explains where it belongs in a controlled workflow.

## 15.2 What TBC means by "target"

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A **ground control point (GCP)** is "an accurately surveyed coordinate location for a physical
> feature that can be identified on the ground, e.g., a corner on the pavement markings."
>
> A **target** is "a point extracted from the acquired scan data." *(TBC 22905)*

The target is **not** a physical panel. It is a point the operator picks in the point cloud,
which TBC then pairs with a surveyed GCP. A painted road-marking corner is as legitimate a GCP
as a checkerboard panel — and in corridor work, far more common.

> **FIELD TIP**
>
> This shapes control design (§6). A GCP for mobile mapping registration has to be something you
> can *find in a point cloud* at the density and incidence angle the vehicle produced — which is
> a different requirement from something you can occupy with a prism. A painted stop-bar corner
> is excellent. A survey nail in asphalt is nearly useless: it is a few millimetres across, and
> the cloud will not resolve it.

## 15.3 Register a Run

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*

### Prerequisites

- **At least one generated scan on the run.** The command is dimmed otherwise
- **A GCP file imported into the project** — Shape, ASCII or CSV. Imported points appear in Plan
  View and under the **Points** node

### The sequence

1. In **Project Explorer**, select a run
2. Generate its scans if not already done (§13)
3. Import the GCP file
4. **Mobile Mapping ▸ Processing ▸ Register a Run**
5. Accept the default **Registration Name** (*RunName* Trajectory) or enter one. **This name is
   given to the computed trajectory** — it is what you will be identifying months later (§23)
6. Choose a **Registration Type** (§15.5)
7. Select a GCP under the **Points** node and click **Add Selection to Control Points**
8. Set **Use XY**, **Use Z**, **As Check** for that point (§17)
9. Optionally enable **Activate Limit Box** — a flat box in Plan View or a 3D box in 3D View that
   hides everything outside it, "to remove potential parasitic points over the target"
10. Optionally set **Activate Target-Bundle Adjustment** (§15.7)
11. Select the point in the **Control Points** list. It centres in Plan View and **Point Cloud
    Smart Picking** opens
12. Pick the target, read the residuals, and **Validate** (§15.6)
13. Repeat for further points, or adjust an existing pick
14. **Compute**. The adjusted trajectory draws in **blue**; the original stays **green**
15. Add or modify pairs and recompute as needed
16. **Apply**

### What Apply produces

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*
>
> - An **adjusted trajectory node** nested beneath the run, beside `Sbet`
> - A new **SBET file on disk**: `sbet_<date>_reg_####.out`, in the project folder,
>   **incrementing** with each registration — `_reg_0001`, `_reg_0002`, and so on
> - Picked targets renamed *RunName TrajectoryGCPName*; the updated targets carry a trailing `*`
> - Trajectory properties carrying **`Origin: Registration result`**, **`Input trajectory:
>   Imported trajectory`**, and **`Registration type:`** the method used

> **Those four properties and the numbered SBET file are your provenance record.** They are the
> strongest evidence available that a given point cloud was built on a given adjustment. §23 is
> about how far that evidence travels — and it does not travel as far as you would like.

### A note for single-scanner acquisition

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "In case of a single head configuration (one high-end laser scanner acquisition), it does not
> matter which scan is used (left or right) for the registration." *(TBC 22905)*

## 15.4 Register a Mission

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 26473)*

Register a Mission registers "a set of runs at the same time" rather than sequentially, and —
this is the point of it — **lets every GCP be used more than once**, with different run point
clouds or different passes of the same run.

### How it differs from Register a Run

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs |
| GCP reuse | Once | **Every GCP, as many times as it appears** |
| Control list | One row per GCP | **One row per GCP *instance*** |
| Instances | — | TBC creates one per **250 m scan section** whose bounding box contains the GCP |
| Side | — | An instance binds to the **left, right, or both** sides of the scan section |
| Default name | *RunName* Trajectory | **Reg** |
| Target naming | *RunName TrajectoryGCPName* | ***RegistrationName*_*GCPName*_*RunName*** |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** |
| Unused instances | — | "All unused instances are removed from the Control Points list" |

### Why this is probably the normal case

Consider an ordinary corridor: driven in both directions, perhaps twice, with control set along
it. A single painted mark is visible in four passes. Under Register a Run it constrains one of
them. Under Register a Mission it constrains all four **simultaneously**, and the four runs come
out mutually consistent because they were adjusted against the same observation.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Register a Mission should be the default for corridor work, with Register a Run reserved for
> single-run situations and for repairing one run within an otherwise accepted mission.**
>
> **Not adopted.** The reasoning is above and follows from Trimble's description, but it is a
> production convention and Parametrix should decide it deliberately — including whether a
> mission registration should be redone from scratch when one run is later re-collected.
> *(Register item 12)*

## 15.5 Registration Type — and the one that does not extrapolate

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905, 26473)*

| Method | What it does | Trimble's stated use |
|---|---|---|
| **Global** | A shift of the whole trajectory, **without rotation**. No local adjustment near control | "situations where there are consistent differences between the laser data and the ground control points. A situation in which the data can be corrected with a simple shift" |
| **Local** | Local adjustment **with interpolation between** control points | "suitable for a local adjustment of a run, **not for systematic error along the run or for adjusting outside the ground control points set**" |
| **Global, and then Local** | Global first, then Local | *No separate guidance given* |

> **CAUTION**
>
> **Local does not extrapolate.** Trimble says so directly: it is not for "adjusting outside the
> ground control points set."
>
> Beyond the first and last control point along a run, a Local adjustment does not correct the
> trajectory. The cloud at the ends of the corridor is left on the imported trajectory while the
> middle is adjusted — and there is no visual indication of where the adjustment stopped.
>
> **The practical consequence for control design:** control must bracket the extent you intend
> to deliver, not merely fall within it. A GCP 200 m inside each end of a 3 km corridor leaves
> 400 m unadjusted at the tails. §6 and §17 return to this.

> **FIELD TESTING REQUIRED · T15**
>
> **Which registration type, when?** Trimble describes the mechanism of each and gives no
> selection rule beyond "consistent differences." **Global, and then Local** receives no guidance
> at all, and is the method shown in every screenshot Trimble publishes.
>
> Do not adopt a default from the screenshots. Test the three methods on a representative
> corridor with independent check points and compare. *(Appendix E)*

## 15.6 Target picking, and reading residuals before you commit

This is where the operator's judgement enters the adjustment, and TBC gives real help.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*

### Picking types

| Type | Use |
|---|---|
| **Default** | Snap to a cloud point near the GCP. Not for road marks or plane intersections |
| **Intersected Plane** | Fits a plane near the rough pick and projects the pick onto it |
| **Road Mark** | Picks a point on a **pavement marking edge line** |

Within **Intersected Plane**, a target template may be applied:

| Template | Predefined dimension |
|---|---|
| Single Pick | — |
| Checkerboard | 0.500 m middle line |
| Diamond | 0.400 m edge length |
| Rectangular | 0.500 × 0.500 m |
| GV Target (L-shape) | 0.080 m bolt |

### The Validate Picking window

Each pick opens **Validate Picking**, which shows:

- An overhead view of the projected point
- A **side view perpendicular to the trajectory**
- The 3D coordinates of the pick
- The **RMS of the fitted plane**
- **Direct residuals to the GCP**, updating live as the template is adjusted

> **IMPORTANT**
>
> **The residuals are shown before you commit the pick, and they update as you nudge it.**
>
> That changes the working method. This is not "pick everything, compute, then discover the
> problem." It is *pick, read the residual, adjust, then validate* — and the operator should be
> forming a judgement about each observation as they make it, exactly as they would reject a bad
> total station shot at the instrument rather than in the office.
>
> Live residuals update when the target centre moves (by picking a new centre, or with the
> keyboard arrows, including fine adjustment with **Shift**) or when the GV Target bolt size
> changes *(TBC 22905; TBC RN 2026.10)*.

Rendering can be changed to **Gray-Scale Intensity**, **Color-Coded Intensity** or **Color By
Distance to Plane**, and for Intersected Plane an **Intensity** slider reduces contrast on
targets with reflective parts.

### Two warnings TBC raises

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> One icon means "the picked point is not a 3D point (no Z coordinate) and/or does not belong to
> the scan of the run to register."
>
> The other means "the picked point **does not belong to the most recent scan** of the run to
> register."
>
> "In both cases, pick again a new target." *(TBC 22905)*

> **The second warning deserves attention.** It means the pick landed on a superseded scan — an
> earlier generation, or one built on a different trajectory. Registering against it would be
> adjusting a trajectory to fit a cloud produced by a different trajectory. TBC catches it. It is
> a good illustration of why superseded scan sets are a hazard worth managing (§21, §23).

### The 30 m rule

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "The distance in a pair of points cannot exceed the allowed maximum distance of **30 meters (or
> 100 feet)**." *(TBC 22905, 26473)*

A pair exceeding it is rejected. In practice this is a sanity limit, not a working tolerance — a
GCP and its picked target should be a few centimetres apart, not tens of metres. Hitting this
limit means the wrong feature was picked.

### Minimum observations

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "A pair of a ground control point (GCP) and a picked target is **enough to perform the
> registration**." *(TBC 22905)*

> **CAUTION**
>
> **One pair is enough for TBC. It is nowhere near enough for survey work.**
>
> A single pair gives a shift with no redundancy, no residual to inspect and nothing to check it
> against. TBC will compute it, apply it, and report residuals of zero — because with one
> observation and three unknowns the fit is exact and meaningless.
>
> **How many pairs are required, at what spacing, is PARAMETRIX DECISION REQUIRED** and is
> treated in §17. Do not infer a Parametrix minimum from Trimble's software minimum.

## 15.7 Target-Bundle Adjustment — the option whose name reads backwards

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905, 26473)*

| State | Bundle adjustment interval | Trimble's stated fit |
|---|---|---|
| **Checked** | **250 m** acquisition intervals | "few GCPs… accuracy of the GCPs is moderate… precision in target picking is less stringent" |
| **Unchecked** | **70 m** acquisition intervals | "more GCPs available… accuracy of the GCPs is high and precise target picking is necessary" |

> **IMPORTANT**
>
> **Checking the box makes the adjustment coarser, not finer.** The name implies you are turning
> something on that will improve the result. What you are turning on is a longer averaging
> interval, appropriate when you have few or moderate-quality control points.
>
> For survey-grade work with dense, well-surveyed control and careful picking, **unchecked** is
> what Trimble's own description points to. This document does not adopt that as a rule.

> **FIELD TESTING REQUIRED · T9**
>
> Trimble ties the choice to three conditions at once — GCP density, GCP accuracy, and picking
> precision — which will rarely all point the same way. The default state is not stated.
>
> Test both states on a representative dataset with independent check points. *(Appendix E)*

## 15.8 Editing a registration — not the same as registering again

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25362, 26578)*

**Edit a Run** and **Edit a Mission** reopen an existing registration and improve it "not by
incrementing each time the adjusted trajectory but by **editing the same (imported)
trajectory**."

Re-running Register on an already-registered run stacks a new adjustment and creates a new
numbered trajectory. **Edit** reloads the original registration's parameters — registration type,
each GCP's Use XY / Use Z / As Check choices, and the paired targets — and lets you add, remove
or re-pick pairs, then recompute **from the imported trajectory**.

| | Register (again) | **Edit** |
|---|---|---|
| Starts from | The current trajectory | **The imported trajectory** |
| Output | A further incremented trajectory | *RunName*_Trajectory2 |
| **Reset available?** | **No** — "There is no restoration when you register the trajectory of a run but only when you edit it" | **Yes** — restores modified targets to their initial picked position, restores deleted pairs, removes added pairs, and restores the original Use XY / Use Z / As Check choices |

> **CAUTION**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.

## 15.9 Judging the result

Covered fully in §18, but the governing principle belongs here because it is where the temptation
to shortcut is greatest.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Trimble's position, in identical wording in two separate topics:
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

> **The asymmetry is the whole point. A number can prove failure. A number cannot prove
> success.**
>
> That is not a quirk of Trimble's software — it follows from what a residual is. A residual
> measures the fit between the adjustment and the observations that shaped it. An adjustment with
> few observations, or with a systematic error common to all of them, will fit beautifully and be
> wrong. Only observations that took no part in the adjustment (§17) and a direct look at the
> data (§18) can distinguish the two.

> **PARAMETRIX DECISION REQUIRED**
>
> **What constitutes an acceptable registration at Parametrix?**
>
> **No numerical threshold appears anywhere in this document, because none exists in any Trimble
> source and inventing one would be indefensible.**
>
> The acceptance framework should combine four things, and a rule built on any one alone will
> fail:
>
> 1. **Numerical residuals** on the control used in the adjustment
> 2. **Independent check information** — residuals on points held out of it (§17)
> 3. **Visual inspection** — Cutting Plane View across overlapping runs (§18)
> 4. **The project accuracy requirement**, which is set per job and is the only thing that makes
>    any threshold meaningful
>
> **Under no circumstances should this SOP acquire a statement of the form "RMS below X equals
> pass."** *(Register item 13; §18, §24)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We took surveyed control points, found each one in the point cloud by
> eye, and told TBC to bend the vehicle's computed path so the cloud lands where the control says
> it should. The output is a new path — a new trajectory — sitting next to the original one. The
> point cloud has not moved yet.
>
> **Why it matters.** This is the step that ties a mobile mapping dataset to the ground. Before
> it, the cloud is an internally consistent shape floating on whatever the GNSS and inertial
> solution managed on the day. After it, the shape has been fitted to points a surveyor actually
> occupied. Everything a client relies on — that a curb is where you say it is, that a clearance
> is what you measured — rests on this and on the control network underneath it.
>
> **What can go wrong.** Three things, in order of how often they bite.
>
> First, **too little control and too much confidence**. TBC computes a registration from one
> pair and reports a residual of zero. That zero means the arithmetic worked, not that the data
> is good. Second, **registering twice instead of editing** — the residuals improve each time
> while the trajectory gets bent further against the same handful of points. Third, and least
> visible: **choosing Local and expecting it to fix the ends of the corridor.** It does not
> extrapolate. The last 400 m sit on the unadjusted trajectory and look identical to the rest.
>
> **What good looks like.** Control distributed along the whole extent you intend to deliver,
> bracketing both ends rather than sitting inside them. Enough pairs that removing any one would
> not change the answer much. Residuals that do not grow systematically as you move away from
> control. Some points deliberately held out of the adjustment, with residuals on them in the
> same range as the ones that were used. And a cutting plane through two overlapping passes
> showing the same wall in the same place. A small RMS on its own is not a result — it is one of
> four things you need, and it is the only one the software hands you for free.

---

# 16. Run to Run Registration

## 16.1 What it is, and what it is not

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
>
> **Register Run to Run** "provides a way to register a set of runs, two by two in batch mode,
> from the same mission or from different missions. In a pair of runs, one has to be defined as
> a **Reference Run**, meaning that its trajectory will not change, and the other as a **Run to
> Adjust**, its trajectory will be optimized with regards to the Reference Run's trajectory. As a
> result, a new trajectory will be created and the scan data of the Run to Adjust will be updated
> with this new trajectory so that the scan data of both runs will match well together."

The help topic is titled *Register Multiple Pairs of Runs*; the command in the ribbon is
**Register Run to Run**.

> **CAUTION**
>
> **This command uses no surveyed control.** It makes two clouds agree with each other.
>
> Two runs can agree perfectly and both be in the wrong place. Run-to-run registration improves
> **relative** accuracy — the internal consistency of the dataset — and does nothing whatever for
> **absolute** accuracy. It cannot replace registration to control (§15), and a dataset that has
> only been run-to-run registered has not been tied to the ground at all.

## 16.2 Where it belongs

Run-to-run registration solves a specific problem: two passes down the same corridor that are
each individually acceptable against control, but that do not sit on top of each other.

That mismatch is real and visible — a doubled curb line, a wall with two faces 4 cm apart — and
it is the thing a client notices first in a delivered cloud. It arises because the two passes
were collected at different times with different GNSS conditions, and each carries its own
trajectory error.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Where run-to-run registration fits in a controlled workflow:**
>
> 1. Register the mission to surveyed control first (§15). This establishes absolute position
> 2. Assess the result against independent check points (§17) and visually (§18)
> 3. **Only then**, if overlapping passes still disagree, use run-to-run to reconcile them —
>    choosing as **Reference Run** the pass with the better GNSS conditions and the better
>    residuals against control
> 4. Re-check against the independent check points afterwards, because the Run to Adjust has
>    moved
>
> **Not adopted.** Step 4 is the part most likely to be skipped and is the reason this sequence
> matters: adjusting a run to match another run will change its residuals against control, and
> if the reference run was itself slightly off, run-to-run will faithfully propagate that error
> into the run you adjusted. *(Register item 14)*

> **The choice of which run is the Reference is a survey decision, not a processing convenience.**
> Whatever the Reference Run's absolute error is, the Run to Adjust inherits it.

## 16.3 Prerequisites

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
>
> In a pair, the two runs need to have:
>
> - **At least one scan**, whatever the scan (left or right)
> - **Enough overlapping scan data** along the trajectories

### A useful exception

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> *"Missing TMX Files for 'Runname_X and Runname_X+1'" in the Status column means that no scan
> data has been generated… "Missing TMX files" does not prevent you from launching the Register
> Run to Run directly, and you do not need to generate the scans first, **TMX files will be
> generated on the fly**.* *(TBC 25096)*

This is the only registration command that does not require pre-generated scans. Every other one
is dimmed without them.

## 16.4 The sequence

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*

1. Import the missions into the TBC project
2. **Mobile Mapping ▸ Processing ▸ Register Run to Run**
3. Enter a **Registration Name**. "This name will be given to all computed trajectories"
4. Select a pair — one as **Run to Adjust**, one as **Reference Run**. They may come from the
   same mission or from different missions. In the pair selectors, runs are listed as
   `<mission ID last two digits> - Run <n>`
5. Optionally **Swap Runs** to invert the two
6. Click **+** to add the pair to the batch
7. In Plan View the **Run to Adjust draws green** and the **Reference Run draws red**
8. Repeat for further pairs. Pairs can be removed with **−**, or reordered with the up and down
   buttons — **TBC registers the pairs in the order given**
9. Set the **Update Scans** option (§16.5)
10. Check **Open Cutting Plane View** to inspect visually
11. **Compute**

### What Compute produces

- A new trajectory nested beneath the **Run to Adjust**, named
  `GivenName: Runname_X To Runname_X+1`
- **RMS statistics in the Results tab** (§16.6)
- If **Update Scans** was checked, new Scan nodes beneath the created trajectory
- A cutting plane named `MissionID Last Two Digits - Run to Adjust`, one per pair

## 16.5 Update Scans is an option inside this command

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
>
> - **Unchecked** — do not generate the scan data after the registration
> - **Checked** — generate the scan data for the **Run to Adjust** on the adjusted trajectory,
>   and enable the **Open Cutting Plane View** option

> **This is the one place in TBC where Update Scans is not a separate step.** Everywhere else,
> registration produces a trajectory and the cloud is recomputed later and deliberately (§13.6).
> Here it can happen inline.
>
> The consequence for provenance is worth noting: a run-to-run registration with Update Scans
> checked produces a new scan set immediately, and the previous scan set remains in the project.
> Which one is delivered becomes a question of which node is selected at export (§22, §23).

## 16.6 The result — and TBC's most informative QC output

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
>
> "TBC also computes some statistics and displays them in the **Results** tab. **Timestamps are
> computed every twenty meters depending on the speed of the vehicle.** For each Timestamp,
> **three RMS values are computed along three directions (Tangential, Orthogonal and
> Vertical)**."

| Direction | Meaning |
|---|---|
| **Tangential** | Along the direction of travel |
| **Orthogonal** | Across the direction of travel, horizontally |
| **Vertical** | Up and down |

Cells read **`No overlap`** where the two runs do not overlap at that timestamp, and a metric
value where they do.

> **This is the most detailed quality output anywhere in the mobile mapping workflow, and it is
> worth understanding why the three axes are separated.**
>
> An error that is large **tangentially** but small orthogonally and vertically is a *timing* or
> along-track scale problem. One that is large **orthogonally** is a heading or lateral position
> problem. One that is large **vertically** is a height or pitch problem. The three-axis
> breakdown tells you which part of the trajectory solution is struggling — information a single
> combined RMS would hide.
>
> The same three-axis convention appears in laser scanner calibration *(TBC 24886)*, so it is
> TBC's standard agreement metric for mobile mapping.

### The `No overlap` rows are information, not noise

A run pair with many `No overlap` timestamps did not have "enough overlapping scan data along the
trajectories" — the prerequisite in §16.3. The registration may still compute, on the few
timestamps that did overlap. **A pair that overlaps for 200 m of a 2 km run has been registered
on 10 % of its length and extrapolated across the rest.**

> **FIELD TESTING REQUIRED · T24**
>
> **How much overlap is enough?** Trimble states the requirement qualitatively — "enough
> overlapping scan data" — and gives no proportion, no minimum length and no distribution rule.
> The Results tab makes the actual overlap visible after the fact but offers no guidance on
> reading it.
>
> Test on a representative pair, varying overlap, and observe where the adjustment stops being
> trustworthy. *(Appendix E)*

## 16.7 The visual check

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*

Checking **Open Cutting Plane View** creates, per pair, a plane named *MissionID Last Two Digits
- Run to Adjust*, appearing as:

- A plane node beneath the parent **Plane** node in Project Explorer
- A **yellow cutting plane** at the beginning of the Run to Adjust, visible in 3D View
- A profile in the **Cutting Plane View** tab, showing the points that intersect the plane

To read it:

- Change rendering to **Scan Color** — one colour per scan, so the two runs are distinguishable
- Increase **Point Size**
- Adjust **Cutting plane thickness** — "a wider thickness will typically result in additional
  points being displayed"
- Keep only the pair's Scan nodes checked in Project Explorer
- **Drag the slider at the bottom of the tab to move the plane along the Run to Adjust**, looking
  at the gap between the two clouds

> **This is the check Trimble says you cannot skip.** Good RMS values do not prove success
> *(TBC 24886, 25096)*. What you are looking for in the profile is one wall, one curb, one pole —
> not two of each, offset.

> **FIELD TESTING REQUIRED · T16**
>
> **Cutting plane thickness.** Trimble's screenshots show `5.000` in one topic and `0.030` in
> another, with no stated basis. Thickness determines what the visual check can actually see: too
> thin and there is nothing in the profile; too thick and a real offset is buried in a band of
> points from either side of the plane. *(Appendix E)*

## 16.8 Improving a run-to-run result

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "You can use the **Register a Run** command to improve the trajectory resulting from
> registering two runs together. The improvement can be done by editing the same (run_to_run)
> trajectory." *(TBC 25362)*

So a run-to-run result can subsequently be adjusted against surveyed control through Edit — which
supports the sequencing in §16.2, in reverse order, for situations where the relative fit was
addressed first.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We took two passes down the same stretch of road that did not quite line
> up, held one of them fixed, and bent the other until the two clouds sat on top of each other.
> No survey control was involved at all. TBC then told us how well they now agree, every 20 m,
> broken into along-track, across-track and vertical.
>
> **Why it matters.** A doubled curb line is the most visible defect in a delivered mobile mapping
> dataset. A client who cannot evaluate absolute accuracy can see two of something that should be
> one, immediately. Reconciling overlapping passes is what makes a dataset look — and be —
> internally coherent.
>
> **What can go wrong.** The trap is mistaking this for registration. It is not. Making two runs
> agree tells you nothing about whether either is in the right place, and it is entirely possible
> to take a well-controlled run and drag it off position by registering it to a poorly controlled
> reference. Whatever error the reference run carries, the adjusted run inherits. The second trap
> is overlap: the software will happily register a pair that only overlaps for a short stretch,
> and quietly extrapolate that correction along the whole run. The `No overlap` rows in the
> Results tab are how you catch it, and they are easy to scroll past.
>
> **What good looks like.** You choose as reference the pass with the better GNSS and the better
> residuals against control — deliberately, not by whichever was listed first. The Results tab
> shows real numbers across most of the run's length rather than a column of `No overlap`. The
> three axes are of similar size; one axis much larger than the other two is telling you
> something specific about which part of the solution is struggling. And when you drag the cutting
> plane along the corridor, you see one building face rather than two. Then you go back and
> re-check the run you moved against your independent control points, because you just moved it.

---

# 17. Control and Independent Check Points

## 17.1 Why this section is separate

Every accuracy claim Parametrix makes about a mobile mapping deliverable rests on this section.

Registration (§15) is the mechanism. This section is about the **survey decision** underneath it:
which surveyed points participate in the adjustment, which are held back to measure it, and who
decides. TBC reduces that decision to three checkboxes, which makes it easy to make
inadvertently.

> A surveyor needs no explanation of why check points matter. What needs explaining is how TBC
> expresses the idea, and where its expression differs from the conventional one.

## 17.2 How control participates — three independent choices per point

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905, 26473)*
>
> In the **Control Points** list, each point carries three checkboxes:
>
> | Column | Effect |
> |---|---|
> | **Use XY** | The **horizontal** coordinates of this point are used to optimise the trajectory |
> | **Use Z** | The **vertical** coordinate is used |
> | **As Check** | The point is a **validation point**. Its residuals are computed and reported but **are not taken into account in the registration** |
>
> "For the selected ground control point (GCP), choose to optimize only the XY coordinates (Use
> XY), or only the Z coordinate (Use Z), or both by checking the corresponding check box(es)."

### The validation point definition, in full

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "A validation point (VP) (As Check) is a ground control point (GCP) that is used **only for
> measuring the quality of the registration**. In the same manner as a normal ground control
> point (GCP), **you need to pair a validation point (VP) with a picked target**. The resulting
> XYZ residual values **will not be taken into account in the registration**, which is why all
> the selected ground control points (GCPs) cannot be set as validation points (VPs). If you set
> all the selected ground control points (GCPs) as validation points (VPs), **an error will
> pop-up** and will prompt you to have at least one ground control point (GCP) for the
> calculation." *(TBC 22905, 26473)*

Three consequences worth stating plainly:

1. **A check point still has to be picked.** Holding a point out of the adjustment does not save
   the operator any work — the target must be identified in the cloud exactly as for a control
   point, and picked with the same care. A carelessly picked check point produces a bad residual
   that says nothing about the data.
2. **TBC does not permit every point to be a check point**, because the adjustment still requires
   control. The software enforces a minimum of one. **That is a mathematical floor, not a survey
   standard.**
3. **The split is per component.** A point can be horizontal control and vertical check, or the
   reverse, by combining the checkboxes. This is genuinely useful where the horizontal control is
   strong and the vertical is the question — or where a feature is well defined in plan and
   poorly defined in height, which describes most painted road markings.

## 17.3 Horizontal and vertical are separable, and usually should be considered separately

> **WHY THIS MATTERS**
>
> A painted stop-bar corner is an excellent horizontal target — a crisp intensity edge the cloud
> resolves well. It is a poor vertical one: it lies in the road surface, the scan hits it at a
> grazing angle, and the height of the picked point depends on exactly which return the operator
> snapped to.
>
> Checking **Use XY** and leaving **Use Z** unchecked on such a point uses it for what it is good
> at and keeps it out of the vertical solution. TBC supports this directly. A processor who
> checks both boxes on every point because that is the default has made a survey decision without
> noticing.

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** This is answerable empirically on a test site with a variety of
> features surveyed conventionally, and the answer will shape control design (§6) far more than
> any software setting. *(Appendix E)*

## 17.4 The independence requirement

This is the part the software cannot enforce.

> **IMPORTANT**
>
> **A check point is only meaningful if it was designated before the adjustment and did not
> change.**
>
> Residuals on points that took part in the adjustment measure how well the adjustment fits the
> observations that shaped it. They are a measure of internal consistency. They tend to look good
> and they are not evidence of accuracy.
>
> Residuals on points held out of the adjustment measure something entirely different: whether
> the adjusted trajectory predicts a position it was never told about. **That is the only
> numerical evidence of accuracy this workflow produces.**

### The failure mode to design against

A conscientious processor registers a mission, inspects the residuals, finds one check point with
a residual larger than they expected, and adds it to the adjustment to bring it in. Every step is
well intentioned. The result is an adjustment with no independent check at all, and a set of
residuals that now measure nothing.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> - **Check points are designated by the Project Surveyor before registration begins** (§3.4)
> - **A point's As Check status is not changed during processing.** If the designation was wrong,
>   it is changed by the Project Surveyor, recorded, and the registration is redone from the
>   imported trajectory using **Edit** (§15.8) — not layered on top
> - **The designation is recorded in the project record** and travels with the accuracy statement
>
> **Not adopted.** *(Register item 15; §3.3 D-3.3)*

## 17.5 How much control, and where

> **PARAMETRIX DECISION REQUIRED**
>
> **How many control points, at what spacing, and how many held as independent checks?**
>
> **No Trimble source states a minimum, a spacing, or a ratio.** TBC's software minimum is one
> control pair and one check point, which is a mathematical floor and has no bearing on survey
> adequacy.
>
> The decision must account for:
>
> - **Corridor length and the project accuracy requirement**
> - **The registration method.** A **Local** adjustment interpolates between control points and
>   **does not extrapolate beyond them** *(TBC 22905)*, so control must **bracket** the delivered
>   extent, not merely fall within it (§15.5)
> - **The bundle adjustment interval** — 250 m checked, 70 m unchecked *(§15.7)* — which is
>   Trimble's own indication of the scale at which control density matters
> - **GNSS conditions along the corridor.** Control is most valuable where the trajectory is
>   weakest, which is precisely where it is hardest to survey conventionally
> - **Redundancy.** Enough that removing any single point would not materially change the result
>
> *(Register item 16)*

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **A structure for the decision, not the decision:**
>
> - Control **bracketing** each end of the delivered extent, outside it where the corridor allows
> - Control at intervals along the corridor, with the interval set from the project accuracy
>   requirement and tightened where GNSS is degraded
> - **Independent check points distributed across the corridor, not clustered**, and including at
>   least one in each distinct GNSS environment — open sky, tree cover, urban canyon
> - **A check point near each end**, because that is where a Local adjustment stops working and
>   where the smoother has data on one side only (§2.2)
>
> **Not adopted.** No counts, no spacings and no ratios appear here deliberately — those are the
> content of the decision above. *(Register item 16)*

## 17.6 What TBC reports, and what it does not

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Per pick, live in the **Validate Picking** window and in the **Targets** pane: **Easting
> residual**, **Northing residual**, **Elevation residual**, "with their corresponding directional
> signs" *(TBC 22905)*.
>
> From TBC 2025.21: those residuals "are now **signed** and included in **the report**"
> *(TBC RN 2025.21)*.

> **VENDOR CLARIFICATION REQUIRED**
>
> **Which report?** The 2025.21 release note says the signed residuals are included in "the
> report" without naming it. The only mobile mapping report topic — *Run a Mission Report*
> *(TBC 23991_1)* — describes the report as showing "capture devices, runs, trajectories and
> generated scans" and **does not mention residuals at all**.
>
> This matters because the residuals on check points are the primary numerical evidence in the
> accuracy statement, and whether they can be produced as a report — rather than transcribed by
> hand from a dialog — determines how the record is kept (§23, §25). *(Appendix F)*

> **FIELD TESTING REQUIRED · T21**
>
> Register a mission, run a Mission Report, and look. This is answerable in ten minutes with the
> software in front of you. *(Appendix E)*

### What TBC does not report

❌ TBC does not produce, in any captured topic, a statement of **which points were used as
control and which as checks** in a registration that has already been applied. The Use XY / Use Z
/ As Check state is visible while the command is open and reloaded by **Edit** *(TBC 25362,
26578)* — but no report of it has been found.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Record the control/check designation outside TBC**, in the project record, at the time of
> registration: point ID, Use XY, Use Z, As Check, and the resulting residual on each.
>
> This is the single most important record in the whole workflow and the software does not appear
> to produce it. Six columns in a spreadsheet, written once. **Not adopted.**
> *(Register item 17; §23)*

## 17.7 Control for calibration is a different thing

A brief warning against a natural confusion.

The calibration procedures in §14 use a specific **run geometry** — four runs, two orthogonal
pairs, each driven in both directions, 250–300 m per strip *(TBC 24886, 28972)* — and derive
boresight angles from **scan-to-scan agreement**, not from control. Surveyed control plays no
part in TBC's laser scanner calibration.

Control and check points are for registration. They do not validate a calibration, and a
calibration does not substitute for them.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We separated the surveyed points into two groups: ones the adjustment is
> allowed to use, and ones it is not allowed to see. TBC does this with three checkboxes per
> point — horizontal, vertical, and *hold this one back as a check* — and it lets you split a
> single point between the groups, using it horizontally while holding its height back.
>
> **Why it matters.** This is the difference between an accuracy statement and an opinion. If
> every surveyed point went into the adjustment, then the residuals you report are just telling
> you how well the maths fitted the numbers you gave it. Of course it fitted. The only figure
> that means anything to a client is the residual on a point the adjustment never saw — that is
> the one that says "the system predicted a position it was not told about, and it was right to
> within this much."
>
> **What can go wrong.** The dangerous failure is not carelessness, it is diligence pointed the
> wrong way. A processor sees a check point with a residual bigger than they hoped, ticks it into
> the adjustment, and re-runs. The number improves. The check has been destroyed, and nothing in
> the software records that it ever existed. This is why the designation should be made by
> somebody other than the person doing the adjustment, and why it should be written down outside
> TBC — because TBC does not appear to report it afterwards.
>
> **What good looks like.** Points held out of the adjustment, chosen before it ran, spread along
> the corridor rather than clustered, with at least one in each kind of GNSS environment and one
> near each end. Their residuals in the same range as the control points that were used — not
> much worse, which would mean the adjustment is only fitting locally, and not suspiciously
> better either. And a written record of which was which, because in two years the project file
> will not tell you.

---

# 18. Point Cloud QC

## 18.1 The governing principle

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

Stated by Trimble in identical wording in two separate topics — the laser scanner calibration
topic and the run-to-run registration topic. It is the single most important sentence in the
office workflow, and the whole of this section is built on it.

### Why the asymmetry is real and not a hedge

A residual measures the fit between an adjustment and **the observations that shaped it**.

An adjustment with few observations fits them exactly — with three unknowns and three
observations there is no redundancy and the residuals are zero by construction. An adjustment
whose observations all share a systematic error fits them beautifully and carries the error
through untouched. In both cases the numbers are excellent and the data is wrong.

The reverse does not hold. If an adjustment *cannot* fit its own observations, something is
genuinely broken — bad control coordinates, misidentified targets, a trajectory too poor to
correct, a calibration that has drifted.

> **A number can prove failure. A number cannot prove success.**
>
> Only two things can suggest success: **observations that took no part in the adjustment**
> (§17), and **looking at the data** (§18.5).

## 18.2 What TBC gives you, at four levels

| Level | Indicator | Where | Source |
|---|---|---|---|
| **Per pick, live** | Easting, Northing, Elevation residual to the GCP, signed; **RMS of the fitted plane** | Validate Picking, Targets pane | *(TBC 22905)* |
| **Per run pair, every 20 m** | RMS in **Tangential, Orthogonal, Vertical**; `No overlap` where absent | Results tab, Register Run to Run | *(TBC 25096)* |
| **Whole calibration** | Overall Overlap %, Overall RMS, per-pair RMS in three axes | Calibrate Laser Scanners | *(TBC 24886)* |
| **Trajectory-wide** | Position, orientation and velocity RMS after smoothing, from `smrmsg_xxx.out` — rendered as **trajectory colour** | Plan View | *(TBC 25943, 27248)* |

Plus the visual check (§18.5) and the records in §18.8.

> **Note what is missing from that table: a single number that describes the quality of a
> registration.** There is no registration report equivalent to a least-squares adjustment
> summary. The evidence is distributed across a dialog, a results tab, a trajectory colour and
> the operator's eyes — which is why the recordkeeping in §18.8 and §23 matters more here than it
> would in a conventional adjustment.

## 18.3 Reading the three axes

Tangential, orthogonal and vertical appear in both calibration and run-to-run registration. They
diagnose, not just describe.

| Dominant component | What it points at |
|---|---|
| **Tangential** — along travel | Timing, or along-track scale. Check the DMI scale factor (§12.3) and the time synchronisation |
| **Orthogonal** — across travel, horizontal | Heading. The hardest attitude component, and the one a single direction of travel cannot resolve (§14.3) |
| **Vertical** | Pitch, or the height component of the trajectory. Check the antenna model (§12.3) and the geoid |

> **WHY THIS MATTERS**
>
> A combined RMS hides this. Three numbers of similar size mean random disagreement, which is
> what good data looks like. One number much larger than the other two means a specific,
> identifiable part of the solution is struggling — and tells you where to look rather than
> leaving you to regenerate everything and hope.

## 18.4 Reading the trajectory RMS colouring

Set at **Mobile Mapping ▸ Trajectory Settings ▸ Rendering Settings ▸ RMS values**, with
user-definable ranges and colours. Settings persist between projects *(TBC 27248)*.

> **This is the highest-value, lowest-effort QC view in the workflow**, and it is available
> before any point cloud exists (§12.4).

What to read from it:

- **Where the solution degraded** — and therefore where control is most valuable (§17) and where
  registration will struggle
- **How long each degraded stretch was.** A short gap bracketed by good data is bridged well by
  the smoother. A long one is not (§2.2)
- **Whether the degradation is at the ends of the mission**, where the smoother has data on one
  side only — the reason the closing sequence in §8 exists

> **OBSERVED SOFTWARE BEHAVIOR**
>
> "If the mission contains some registrations then the modified segments will be colorized with
> the **'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
> `smrmsg` file, so adjusted stretches lose their RMS colour.
>
> **Incidentally useful:** this makes the extent of a registration visible in plan. A **Local**
> registration that stopped adjusting beyond the outermost control point (§15.5) shows the
> boundary directly.

## 18.5 The visual check

Trimble requires it and does not describe how to do it thoroughly. What follows assembles the
mechanics Trimble does give *(TBC 24886, 25096)* into a method.

### Cutting Plane View — checking agreement between overlapping data

The tool for the question *do two passes of the same feature land in the same place?*

1. **Point Clouds ▸ View ▸ Cutting Plane View** (it opens automatically after calibration or
   run-to-run registration if the option was checked)
2. Set rendering to **Scan Color** — one colour per scan, so the two data sets are
   distinguishable. **This is the step that makes the check possible**; in a single colour, two
   offset surfaces read as one thick surface
3. Increase **Point Size**
4. Set **Cutting plane thickness** (§18.6)
5. In Project Explorer, **check only the scans in the pair** and uncheck everything else
6. **Drag the slider along the run**, watching the gap
7. Optionally **Show surface-plane intersection** where a surface exists

What you are looking for: **one wall, one kerb, one pole.** Two of anything is a disagreement,
and its size in the profile is its size in the data.

> **FIELD TIP**
>
> Drag the slider through the **whole** run, not a representative sample. Trajectory error is
> correlated in time (§2.3), so disagreement is concentrated in stretches rather than scattered.
> A pass that is perfect for 2 km and 5 cm out for 300 m will look perfect at every point you
> spot-check and be unacceptable where it matters.

### What else to look at, and what nothing automates

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> A visual QC pass over a registered mission should cover:
>
> | Check | Looking for |
> |---|---|
> | **Overlapping passes in Cutting Plane View**, dragged full length | Doubled surfaces |
> | **Flat surfaces at range** — a wall, a building face | Thickening with distance, which indicates attitude error or a calibration issue (§14.2) |
> | **The ends of the corridor** | Where a Local adjustment stopped; where the smoother was weakest |
> | **The degraded stretches identified in §18.4** | Whether the registration actually fixed them |
> | **Vertical surfaces against horizontal** | Systematic tilt |
> | **Features near control** versus **features far from control** | Residual growth with distance from constraint |
>
> **Not adopted.** *(Register item 27)*

## 18.6 Cutting plane thickness

> **FIELD TESTING REQUIRED · T16**
>
> Trimble's screenshots show **0.030** in the calibration topic *(TBC 24886)* and **5.000** in the
> run-to-run topic *(TBC 25096)*, with no stated basis for either.
>
> The value determines what the check can see. Too thin and the profile is empty. Too thick and a
> real 3 cm offset is buried inside a 5 m band of points collected from either side of the plane.
>
> Establish working values for the checks in §18.5 and record them. *(Appendix E)*

## 18.7 Periodic system verification

Distinct from per-project QC. This is the check that the **instrument** is still performing.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B, p.7)*
>
> Scan approximately **eight flat retro-reflecting targets** at varied distances over **more than
> 180° horizontally**, previously surveyed by total station. The system passes if residuals fall
> within the specified accuracy.
>
> Trimble recommends doing this "regularly" and "especially before starting an extensive data
> acquisition campaign" — and **gives no interval**.

> **PARAMETRIX DECISION REQUIRED**
>
> **Is this the periodic verification Parametrix adopts, and at what interval?**
>
> It is the only independent check on the system in any source — the only one that compares the
> MX60 against conventionally surveyed truth rather than against itself. Calibration (§14) checks
> the system's internal consistency; this checks its accuracy.
>
> Needs: an interval, a site, a target specification, and a pass criterion tied to the
> manufacturer's specified accuracy for the configuration Parametrix owns (§4.1).
> *(Register item 28; Appendix F)*

## 18.8 What to record

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> For each registered mission:
>
> | Record | Source |
> |---|---|
> | Residuals on **control** points used, by component | Targets pane / the report *(§17.6)* |
> | Residuals on **independent check** points | Same |
> | **Which points were control and which were checks** | **Recorded manually — TBC does not report it** *(§17.6)* |
> | Run-to-run RMS statistics, if used | Results tab *(TBC 25096)* |
> | Trajectory RMS picture | Screen capture of the RMS-coloured trajectory |
> | Visual check performed, by whom, covering what | **No software artefact exists** |
> | Results of Scan Generation | *(TBC 22499; §13.5)* |
> | Mission Report | *(TBC 23991_1)* |
>
> Two of those eight have no software artefact at all. **Not adopted.** *(Register item 29; §23)*

## 18.9 Acceptance

> **PARAMETRIX DECISION REQUIRED**
>
> **What constitutes an acceptable point cloud at Parametrix?**
>
> **No numerical acceptance criterion appears anywhere in this document. No Trimble source in the
> set provides one, and inventing one would be indefensible.**
>
> The framework must combine four things. A rule built on any one alone will fail:
>
> | Component | Why it is necessary | Why it is not sufficient |
> |---|---|---|
> | **Numerical residuals** on control used | Objective, repeatable | Measures fit to its own observations — see §18.1 |
> | **Independent check information** | The only numerical evidence of accuracy | Sparse; a handful of points cannot characterise a whole corridor |
> | **Visual inspection** | Catches what no number reports | Subjective, unrecorded, and dependent on who looked |
> | **Project accuracy requirement** | The only thing that makes any threshold meaningful | Varies per job; not a property of the system |
>
> **Under no circumstances should this SOP acquire a statement of the form "RMS below X equals
> pass."** *(Register item 13; §15.9, §24)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We looked at the evidence the software produces about how good the data
> is — residuals on control, agreement between overlapping passes broken into three directions, a
> colour-coded picture of where the trajectory solution struggled — and then we went and looked at
> the actual point cloud, because the numbers cannot finish the job.
>
> **Why it matters.** Trimble says this outright, twice, in two unrelated parts of its
> documentation: a good RMS does not prove the work succeeded, though a bad one proves it failed.
> That is not corporate caution. A residual tells you how well the adjustment fitted the numbers
> you handed it. Hand it three points and it fits them perfectly. Hand it three points that share
> a common error and it fits those perfectly too, and passes the error straight through. The
> arithmetic is not lying to you; it is answering a narrower question than the one you care about.
>
> **What can go wrong.** The spot-check. Mobile mapping error comes in stretches, not speckles,
> because it is driven by a filter that changes smoothly over minutes. A corridor that is
> flawless for two kilometres and 5 cm out for three hundred metres will pass every sample you
> take and fail the one place the client happens to measure. Dragging the cutting plane along the
> whole run is tedious and it is the check.
>
> The other one is subtler: forgetting to set the rendering to one colour per scan. In a single
> colour, two surfaces 4 cm apart look exactly like one surface 4 cm thick. You will look straight
> at the defect and not see it.
>
> **What good looks like.** Residuals on points the adjustment never saw, in the same range as the
> ones it used. Three axes of similar size rather than one dominating. A trajectory that is mostly
> one colour with short, expected degraded stretches. A wall at 50 m that is as thin as a wall at
> 10 m. And a cutting plane dragged the length of every overlap showing one of everything. None of
> that is a number you can put in a spreadsheet, which is exactly why somebody has to look.

---

# 19. Imagery QC

## 19.1 What the MX60 imagery is for

| Camera | Output | Typical use |
|---|---|---|
| **360° spherical** | Panoramic images along the corridor | Feature identification, asset attribution, virtual site visits, client review |
| **Rear-downward** | Pavement-facing imagery | Pavement condition, orthomosaics, line-marking work |

Imagery is positioned from the trajectory, exactly as the point cloud is. It inherits the same
errors and improves — or does not — in the same way.

> **OBSERVED SOFTWARE BEHAVIOR · unverified**
>
> **Whether imagery positions inherit a registration is not documented.** Registration produces a
> new trajectory and Update Scans recomputes the point cloud from it (§13.6). No captured Trimble
> topic states whether station positions and panorama orientations are recomputed too.
>
> It is plausible that they are, since imagery is positioned from the trajectory. **It is not
> stated, and must not be assumed.**
>
> **FIELD TESTING REQUIRED · T26** — compare a station's position before and after a registration.
> This is answerable in minutes and nobody has done it. *(Appendix E)*

## 19.2 Resolution depends on the configuration

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22501, 23888)*

| Image | MX60 **Core** | MX60 **Pro** / **Premium** |
|---|---|---|
| Panoramic | **8192 × 4096 px** | **12288 × 6144 px** |
| Side / planar | 4096 × 3008 px | 4096 × 3008 px |

> **IMPORTANT**
>
> **Core delivers a quarter of the panoramic pixels of Pro and Premium.** Any commitment to a
> client about imagery deliverable quality — legibility of sign text, identification of small
> assets, orthomosaic ground sample distance — depends on which configuration is on the roof, and
> Parametrix does not currently know which that is (§4.1).
>
> *(Register item 2; Appendix F)*

### A configuration note about side cameras

> **OBSERVED SOFTWARE BEHAVIOR**
>
> Trimble's export folder-structure examples show the MX60 tree containing **Camera 3 Back Down**
> and **Camera 4 360°**, with per-face `.cal` files for the 360° camera (Front, Rear, Left, Right,
> Top, Bottom). The MX9 and MX50 trees additionally show **Planar 1** and **Planar 2** side
> cameras; **the MX60 tree does not** *(TBC 23339, 22501)*.
>
> This suggests the **Export side images** option has nothing to export on an MX60. **Trimble does
> not state this**, and the option remains present in the dialog.
>
> **FIELD TESTING / VENDOR CLARIFICATION REQUIRED · T27** — **what imagery streams actually
> exist on the MX60, and which are exposed through TBC export?** Run an export with side images
> enabled and see what appears; confirm with the vendor what the MX60 camera complement is.
>
> **Do not write MX9 or MX90 camera behaviour into MX60 procedure on the strength of a shared
> dialog.** The option's presence in the export pane is not evidence that the sensor exists.
> *(Appendix E; Appendix F)*

## 19.3 What to check

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> | Check | Looking for |
> |---|---|
> | **Coverage** — is there imagery for the full corridor? | Gaps where a camera stopped, or where a run was not colorized |
> | **Exposure** | Blown highlights on bright surfaces, blocked shadows under tree cover and in underpasses — both are unrecoverable |
> | **Motion blur** | Speed too high for the light available |
> | **Obstruction** | The survey vehicle's own aerials, a following vehicle, a smear on the dome |
> | **Focus and contamination** | Rain, dust, insects on the optical surface |
> | **Corrupted images** | See §19.4 — these are **silent** |
> | **Alignment with the point cloud** | Colorized points in the wrong colour at feature edges indicates a camera boresight issue (§14.4) |
>
> **Not adopted.** *(Register item 30)*

## 19.4 Corrupted side camera images are exported as black

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "**Corrupted side camera images are exported as black images.**" *(TBC 23339, 22501)*

> **CAUTION**
>
> **This is a silent failure.** The export completes. The file count is right. The images are
> there. Some of them are black.
>
> Nothing in TBC reports it, and a deliverable can pass every automated check with a proportion of
> its imagery blank. **The only detection is looking at the imagery**, which on a corridor job
> means sampling systematically rather than opening the first few.

> **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED**
>
> **This is not a Trimble procedure. It is a screening method proposed by this document and not
> yet validated.**
>
> Include a **file-size scan** of the exported imagery in the delivery check (§24). The logic: a
> uniformly black JPEG typically compresses far smaller than a valid image, so **anomalously small
> files are a useful screening flag** and a sorted file listing surfaces candidates without
> opening a single image.
>
> **File size alone cannot establish image validity.** It is a screening method, not proof. A
> small file may be a legitimately low-detail frame — a plain sky, a blank wall, an unlit tunnel —
> and a corrupted image is not guaranteed to be small. Anything the scan flags must be opened and
> looked at; anything it does not flag is not thereby verified.
>
> **Validation required** before adoption: run it against a known-good export and a known-bad one
> and establish whether a usable threshold exists for MX60 imagery.
>
> *(Register item 31)*

## 19.5 Colorized point clouds

Colour on the point cloud comes from the imagery, at scan generation (§13.4).

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Colour is exported "if the scans have been generated with the color option set to on"
> *(TBC 23339, 22501)*.

Two failure modes worth checking specifically:

**Colour fringing at feature edges** — points on a kerb taking the colour of the road, or points
on a pole taking the colour of the sky behind it. Small amounts are inherent: the camera and the
scanner are at different positions and see slightly different things. Large or systematic
fringing indicates a **camera boresight problem** (§14.4), and is one of the few places where a
calibration issue is directly visible.

**Colour from the wrong exposure** — a stretch of cloud markedly darker or lighter than its
neighbours, where the camera's automatic exposure changed between passes.

> **FIELD TESTING REQUIRED · T6**
>
> The colouriser offers a forward versus backward camera preference with no stated selection rule
> *(§13.4)*. Its effect on fringing is untested. *(Appendix E)*

## 19.6 Privacy and blurring

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **Blur people** and **Blur vehicles** options exist on the **Publish to TRCPS** command
> *(TBC 29527)*, and the export commands cross-reference a **Blur Exported Images** topic
> *(TBC 23339, 23888, 22501, 20927_1, 21713_1)*.
>
> On Publish to TRCPS, the blur options are **greyed out until an images option is selected**, and
> blurring prompts to use **GPU (if compatible) or CPU** *(TBC 29527)*.

> **The Blur Exported Images topic has not been captured.** It is the one remaining Trimble topic
> identified as worth collecting, and it should be captured before imagery privacy becomes a
> requirement on a live job. It is not a gap in the technical workflow — blurring is a delivery
> option, not a processing stage.

> **PARAMETRIX DECISION REQUIRED**
>
> **What is Parametrix's position on imagery privacy?**
>
> Mobile mapping imagery routinely captures pedestrians, vehicle licence plates, private property
> and building interiors visible through windows. This is not a Trimble question and no Trimble
> setting answers it.
>
> The decision needs to cover:
>
> - Whether blurring is applied by default, on request, or by jurisdiction
> - Whether **unblurred originals are retained** after a blurred deliverable is issued, and for
>   how long (§25)
> - What the client is told about what was captured
> - Whether any client or jurisdiction imposes a requirement Parametrix must meet
>
> Blurring is irreversible in the delivered product and the decision has legal and reputational
> dimensions that sit well outside this SOP. *(Register item 32)*

## 19.7 Imagery in the delivered dataset

Where imagery travels, and what travels with it:

| Path | Imagery | GPS attributes in the image file |
|---|---|---|
| **Export to TMX** | Panoramic, side, back-facing | Optional — latitude, longitude, altitude, acquisition time |
| **Export to TopoDot** | Panoramic, side, back-facing, as cubical images | Optional |
| **Export to Solv3D** | Panoramic | Optional |
| **Publish to TRCPS** | Panoramic, side, back-facing — each optional | — |

*(TBC 22501, 23339, 23888, 29527)*

> **OBSERVED SOFTWARE BEHAVIOR**
>
> An exported panoramic image's file properties show **`Program name: Trimble Business Center`**
> *(TBC 21713_1)*. Software provenance does reach the imagery, in EXIF. **It names the software,
> not the trajectory** (§23).

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We checked the photographs: that they cover the whole route, that they are
> properly exposed and sharp, that nothing is blocking the lens, and that where the imagery has
> been draped onto the point cloud the colours land on the right points.
>
> **Why it matters.** Imagery is often what the client actually looks at. A project manager who
> will never open a point cloud will click through panoramas, and an asset inventory job may
> depend entirely on being able to read a sign face. It is also the part of the deliverable where
> defects are most obvious to a non-specialist, which cuts both ways — easy to catch, and
> embarrassing if you do not.
>
> **What can go wrong.** Two things stand out. First, resolution is not a property of the MX60; it
> is a property of *which MX60*. Core panoramas are a quarter of the pixels of Pro and Premium,
> which is the difference between reading a sign at 20 m and guessing at it. Promising imagery
> quality without knowing which unit is on the roof is promising blind.
>
> Second, Trimble states that corrupted side camera images are exported as black. Not flagged,
> not reported, not missing — present, and black. The export succeeds, the file count is right,
> and a client opens image 4,712 to find nothing there. Sorting the exported files by size takes
> two minutes and finds every one of them, because a black JPEG is tiny.
>
> **What good looks like.** Continuous coverage with no unexplained gaps. Exposure that holds
> through the shaded stretches as well as the open ones. Colour on the point cloud that lands
> cleanly on feature edges — a kerb coloured like a kerb, not like the road beside it, because
> that fringing is the visible symptom of a camera boresight problem. And a systematic sample of
> the imagery actually opened and looked at, not just counted.

---

# 20. Degraded GNSS Conditions

## 20.1 This section is a branch, not a stage

Everything from §11 to §19 describes one path through the workflow. This section describes what
to do when that path does not produce an acceptable trajectory — and **two of its three remedies
loop backwards** into earlier stages.

```
                        §12  Trajectory processing
                               │
                               ├──────────── LiDAR QC ──────────┐   inside §12
                               │                                 │   needs a large workstation
                               ▼                                 │
                        §13  Generate scans                      │
                               │                                 │
                               ▼                                 │
                        §15  Register to control ────────────────┤   needs more control
                               │                                 │
                               ▼                                 │
                        §18  QC  ── not acceptable ──────────────┤
                               │                                 │
                               │            PFIX ────────────────┘   needs POSPac
                               │            loops back to §12, second pass
                               ▼
                             accept
```

Read it after the normal path is understood. Placing it in sequence would imply it happens after
QC, which is true only in the sense that QC is where you discover you need it.

## 20.2 Why GNSS degradation is the dominant risk

From §2.3: the point cloud inherits the trajectory's error, attitude error multiplies with range,
and **error is correlated in time rather than scattered**. GNSS degradation is the principal cause
of all three.

When GNSS is obstructed, the inertial solution carries on alone and drifts. The drift is smooth,
so the cloud stays crisp and internally consistent — it simply moves. Under tree cover, in an
urban canyon, beneath a structure, the data looks exactly as good as the rest of the corridor and
is not.

> **The environments that degrade GNSS are also the environments clients most often want
> surveyed**: downtown corridors, treed arterials, under-bridge inspections, tunnel approaches.
> This is not an edge case.

### Seeing it before it costs you

The trajectory RMS colouring (§12.4, §18.4) shows degraded stretches **in plan, before any point
cloud exists**. That is the earliest and cheapest warning available, and it should be looked at
on every mission.

## 20.3 The three remedies

| | **More control** | **PFIX** | **LiDAR QC** |
|---|---|---|---|
| What it is | Register to additional surveyed GCPs | POSPac position fixes from GCP/target offsets | Scan data as an aiding sensor in the solution |
| Where it acts | **After** the navigation solution | **Inside** the navigation solution | **Inside** the navigation solution |
| Needs POSPac | No | **Yes** | Not stated |
| Needs extra field control | **Yes** | **Yes** | **No** |
| Needs a large workstation | No | No | **Yes** — 128–256 GB RAM (§4.5) |
| Passes | One | **Two** | One |
| Section | §15, §17 | §20.5 | §20.6 |

> **Without a POSPac licence, Parametrix has two remedies, not three: place more control, or buy a
> much larger workstation.** That is a procurement consequence of a licensing decision, and it is
> worth knowing before quoting a job through a difficult corridor. *(§4.4, Register item 10)*

## 20.4 Remedy one — more control

The conventional answer, and the one that needs no software Parametrix may not have.

Registration to surveyed GCPs (§15) corrects the trajectory **after** the navigation solution.
Where GNSS was poor, the trajectory has drifted, and control in that stretch pulls it back.

Two constraints from §15 govern how control must be placed for this to work:

- **A Local adjustment does not extrapolate** beyond the outermost control point *(TBC 22905)*.
  Control must **bracket** the degraded stretch, not sit in the middle of it
- **Target-Bundle Adjustment** operates at 250 m or 70 m intervals (§15.7), which is Trimble's own
  indication of the scale at which control density matters

> **The difficulty is practical rather than technical.** The stretches that most need control are
> the ones where conventional survey is hardest — under the canopy, between the buildings, where
> the GNSS you would use to establish the control is as obstructed as the vehicle's was. Control
> there has to be carried in by traverse or total station, which is the real cost of this remedy.

> **PARAMETRIX DECISION REQUIRED**
>
> **Does mission planning require control density to vary with predicted GNSS conditions?** A
> uniform spacing along a corridor puts the same control in the open sections, where it adds
> little, as in the obstructed ones, where it is the only thing holding the data together.
> *(Register item 33; §6, §17)*

## 20.5 Remedy two — Generate POSPac Position Fixes (PFIX)

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24460)*
>
> "**Generate POSPac Position Fixes** is a method that lets you improve the trajectories of a
> mission in the Applanix's POSPac MMS software **where there is no GNSS coverage or the coverage
> is extremely poor**. At these locations, trajectories are corrected by measuring the distance
> between ground control points (GCPs) collected in the field and targets extracted from the
> acquired scan data. The results of these measurements are **Offset values that are projected
> back to the trajectories**. New positions of the modified trajectories are then exported to a
> text file, which is used by the POSPac MMS software to do a **second-pass on the trajectory
> data**."

### The distinction from registration — and why it matters

> Registration corrects **the answer**. PFIX corrects **the computation**.
>
> Registration takes a finished trajectory and bends it to fit control. PFIX takes the same
> control observations and feeds them back into the navigation solver as position fixes, so the
> filter re-solves with that information available. The difference is that PFIX's corrections are
> propagated by the filter's own model of how the system behaves, rather than by interpolation
> between control points.
>
> ⚠ *That framing is this document's, inferred from Trimble's descriptions of the two commands.
> Trimble never states the contrast directly.* **VENDOR CLARIFICATION REQUIRED** — when should
> PFIX be preferred over registration? *(Appendix F)*

### Prerequisites

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24460)*
>
> - **POSPac MMS installed, with a valid licence** for the IN-Fusion processing methods
> - An SBET processed in POSPac, or the real-time NAV trajectory "in case of POSPac processing not
>   possible"
> - A VCE project whose coordinate system matches the data
> - The `.mxdb` imported with that trajectory applied
> - **Scan data generated from at least one run**
> - A GCP file imported in the project coordinate system

### The procedure

1. Right-click the **Mission** node ▸ **Generate Pospac Position Fixes**. *The command does not
   open if the mission has no generated scan*
2. Select a GCP under **Points** ▸ **Add Selection to Control Points**
3. Pick the target in the cloud — **the same Point Cloud Smart Picking tool as registration**
   (§15.6), with the same live residuals and the same **30 m** maximum pair separation
4. **Validate**. Easting, Northing and Elevation residuals display
5. Add further pairs — one pair is sufficient for TBC, and §15.6's caution applies equally
6. **Compute.** "The computation consists in reducing the global error between the ground control
   point(s) (GCPs) and their corresponding targets"
   - Updated targets are named `Mission_Name-PFIX-GCP_Name`
   - **A `custom_events.txt` file is generated in a `PFIX` folder under the TBC project folder**
7. Close the dialog

### The second pass, in POSPac

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24460)*
>
> 1. Start POSPac MMS, create and save a project
> 2. Import the POS logged files from `POS_1/raw`
> 3. **Copy the `custom_events.txt` from TBC into the `Extract` folder of the POSPac project**
> 4. Open the **GNSS-Inertial Processor**
> 5. Optionally open **Position Fixes and Satellite Events** to inspect the fixes
> 6. Select the IN-Fusion processing mode
> 7. **All Processings**. A new SBET appears in the `Proc` folder

### Bringing it back

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 24460)*
>
> 1. Select the mission in Project Explorer and display its properties
> 2. **Replace the initial trajectory file with the new SBET** computed with PFIXes
> 3. **Update the scan data with the Update Scans command** (§13.6)

> **IMPORTANT**
>
> Step 3 is the one that is skipped. A PFIX pass that produces a better SBET but never reaches the
> point cloud has cost a day and changed nothing in the deliverable (§13.6).

## 20.6 Remedy three — LiDAR QC

Covered in §12.7, because it runs **inside** trajectory processing rather than after it.

In summary: it uses the scan data as an aiding sensor, generating 3D voxels matched in overlap
regions, solving the constant IMU boresight angles and correcting the post-processed trajectory in
position and orientation *(TBC 28972)*.

**What makes it distinctive:** it is the only remedy that needs **no additional field control**.
The information comes from the overlap in the data already collected.

**What makes it expensive:** 128 GB RAM minimum, 256 GB recommended, dedicated SSDs, a paging file
at six times installed RAM, and the MATLAB Runtime (§4.5).

> **It requires overlap.** "Select the runs from the Project Tree **with overlap** (parallel runs,
> or crossing runs)" *(TBC 28972)*. A single pass down a difficult corridor gives it nothing to
> work with — which is a **planning** consequence (§6), not a processing one. If a corridor is
> known to be GNSS-hostile and LiDAR QC is a possible remedy, the overlap has to be collected on
> the day.

## 20.7 Choosing

> **PARAMETRIX DECISION REQUIRED**
>
> **What is the decision rule when a corridor produces an unacceptable trajectory?**
>
> The remedies are not equivalent and the choice has cost consequences:
>
> | If… | Then |
> |---|---|
> | Degradation is short and bracketed by good data | More control may be sufficient |
> | Degradation is long, and POSPac is available | PFIX re-solves rather than interpolates |
> | Degradation is long, control is impractical, and overlap exists | LiDAR QC — **if** the workstation exists |
> | Degradation is severe and none of the above is available | **The corridor may need re-collection under different conditions, or a different technology** |
>
> That last row is a real option and belongs in the rule. Mobile mapping is not always the right
> tool for a particular 400 m of a project, and recognising that early is cheaper than three
> remedies and a compromise.
>
> *(Register item 34)*

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Identify GNSS-hostile stretches at planning, not at QC** (§6). The RMS colouring (§18.4) tells
> you after the fact; a desktop review of canopy, built form and structures tells you before. Where
> a hostile stretch is identified, decide *then* whether the mitigation is extra control, planned
> overlap for LiDAR QC, or a different method — because two of the three have to be arranged in
> the field.
>
> **Not adopted.** *(Register item 33)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We set out what to do when the satellites were not visible enough for long
> enough, and the computed path drifted. There are three fixes: put in more surveyed control and
> pull the path back onto it; feed the control measurements back into the navigation solver and
> re-solve from scratch; or let the software use the overlapping scan data itself as a substitute
> for satellites.
>
> **Why it matters.** The places where GNSS fails are the places clients most want surveyed —
> downtown streets, tree-lined arterials, under bridges. This is not an unusual case to plan for;
> on many corridors it is most of the job. And because the failure is invisible in the data, the
> only thing standing between a drifted stretch and a delivered deliverable is somebody having
> looked.
>
> **What can go wrong.** Two of the three fixes have to be set up *before* you drive. More control
> means surveying points in exactly the places where conventional survey is hardest, because the
> sky is just as obstructed for your control crew as it was for the vehicle. LiDAR QC needs
> overlapping passes, which means driving the corridor more than once — and if you did not, the
> remedy is not available in the office no matter how large the workstation. Discovering at QC that
> you needed overlap you did not collect means going back.
>
> The third failure is subtler: doing a PFIX pass properly, producing a genuinely better path, and
> then forgetting to run Update Scans. The trajectory improves, the point cloud does not, and the
> file you deliver is the one you started with.
>
> **What good looks like.** The hostile stretches were identified from a desk review before anyone
> drove, the mitigation was chosen then, and the field work was planned around it. After
> processing, the trajectory RMS picture shows short degraded stretches where you expected them.
> Independent check points in those stretches — and there should be some, specifically there — come
> back in the same range as the ones in the open. And if none of that could be arranged, somebody
> said so early enough that the client could choose a different approach for that 400 m rather
> than receiving it quietly mixed in with the rest.

---

# 21. Cleanup Mobile Mapping Mission

> **CAUTION**
>
> **This operation is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: **"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."** *(TBC 26466)*
>
> **Do not run this command until §21.4 has been decided by Parametrix.**

## 21.1 What it does

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 26466)*
>
> "The feature enables you to cleanup your project by **keeping the most recent registration (and
> related scans), and trajectory consistent with the latest version of navigation and trajectory
> information file (SBET or NAV)**. This feature can be run at the end of the data preparation
> process (registration, colorization, etc.), it allows you to **share a light project**, before
> moving on to a feature extraction phase. Please, have a backup copy of your project prior
> performing the operation, it cannot be undone."

Run from the **Mission** node context menu. That is the entire published procedure — the topic is
four sentences long.

## 21.2 Why the command exists, and why it is genuinely useful

A mission that has been through several registration attempts accumulates layers. Each
registration produces a trajectory node and a numbered SBET on disk; each Update Scans produces a
scan set beneath it (§13.6, §15.3). A project with four registration attempts holds four
trajectories and up to four full scan sets of the same data.

That is large, slow to open, and confusing to hand to someone else. Cleanup reduces it to one
answer.

> **There is a real quality argument for it, not just a disk-space one.** After Cleanup, the
> project contains exactly one trajectory and one set of scans, so **the question "which
> trajectory produced this cloud?" has only one possible answer**. Before Cleanup, a person
> exporting from the project can select the wrong node and never know (§22, §23).
>
> Cleanup makes the deliverable unambiguous. It does so by destroying the alternatives.

## 21.3 What it removes, and why that matters

The command keeps the most recent registration and removes the rest. What is removed:

| Removed | Why it mattered |
|---|---|
| **Earlier registration trajectories** | The record that earlier attempts existed, and what they produced |
| **Their scan sets** | The data those attempts produced |
| **The sequence itself** | That there *were* three attempts before this one |

> **IMPORTANT**
>
> **The evidence destroyed is the audit trail, not the deliverable.**
>
> Consider a reviewer, or an expert in a dispute, asking a reasonable question: *was this result
> arrived at directly, or was it the fourth attempt, and what did the first three produce?*
>
> Before Cleanup, the project answers that: the numbered `sbet_<date>_reg_####.out` files are
> still on disk, the trajectory nodes still carry `Origin: Registration result` and their input
> trajectory and registration type (§15.3), and the sequence is legible.
>
> After Cleanup, the project shows one registration and no history. **Nothing indicates that
> anything was removed.**
>
> This is not an accusation of bad practice — iterating a registration is normal and proper work.
> It is an observation that Cleanup removes the ability to demonstrate what was done, at exactly
> the moment the project is being prepared to hand to someone else.

### On the numbered SBET files

> **OBSERVED SOFTWARE BEHAVIOR**
>
> The registered SBETs are written **to the project folder on disk**, not inside the TBC database
> *(TBC 22905, 26473)*. Trimble does not state whether Cleanup deletes them or only removes the
> project's references to them.
>
> **FIELD TESTING REQUIRED · T28** — list the project folder before and after Cleanup and
> compare. If the files survive, they are a partial audit trail that outlives the operation; if
> they do not, the record is gone entirely. **This materially changes what must be archived
> first.** *(Appendix E)*

## 21.4 The Parametrix decision

> **PARAMETRIX DECISION REQUIRED**
>
> **When may Cleanup Mobile Mapping Mission be performed, by whom, and what must be archived
> first?**
>
> **This SOP does not contain a rule of the form "always run Cleanup" or "never run Cleanup," and
> must not acquire one until this decision is made.** Both positions are defensible and the choice
> is Parametrix's:
>
> | The case for running it | The case against |
> |---|---|
> | The delivered project is unambiguous — one trajectory, one cloud | The audit trail is destroyed |
> | A person exporting later cannot select the wrong node | Nothing records that earlier attempts existed |
> | Smaller, faster, easier to hand on | Not undoable; a mistake is unrecoverable |
> | It is Trimble's intended end-of-preparation step | The project as handed on cannot demonstrate its own derivation |
>
> The decision needs to answer four things:
>
> 1. **When** — at what point in the workflow, and after which approvals
> 2. **By whom** — and with whose authorisation (§3.3 D-3.4)
> 3. **What must be archived first**, and where the archive lives (§25)
> 4. **Whether it is required, permitted, or prohibited** on Parametrix projects
>
> *(Register item 35 — flagged P1. This is among the decisions that should be settled before the
> first production job, because the first person to reach the end of a project will otherwise
> decide it by default.)*

## 21.5 What Trimble recommends, precisely

Stated carefully, because the gap matters.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Trimble recommends **one** thing before Cleanup: **"have a backup copy of your project."**
> *(TBC 26466)*

**No captured Trimble topic recommends exporting, reporting, archiving or otherwise recording
registration information before Cleanup.** No topic links Cleanup to the Mission Report, to
`Targets.csv`, to the numbered SBET files, or to any export.

> **No vendor-prescribed preservation step was found beyond the project backup.**

That recommendation is adequate **on its own terms** — a full project backup preserves everything,
including the history. It is not a records requirement, it does not survive being skipped, and it
says nothing about where the backup lives, how long it is kept, or whether anyone can find it in
three years.

## 21.6 A recordkeeping framework, offered for decision

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted. Offered so that the decision in §21.4 has something concrete to react to.**
>
> A sequence in which Cleanup destroys nothing that matters:
>
> | # | Step | Why, in this order |
> |---|---|---|
> | 1 | **Complete and accept QC** (§18, §24) | Cleanup is an end-of-preparation step; running it before acceptance removes the alternatives you might need to go back to |
> | 2 | **Run the Mission Report** and archive it | It records capture devices, runs, trajectories, generated scans, and per-sensor calibration with date *(TBC 23991_1, 24868)*. **Run it before Cleanup** — afterwards it can only report what survives |
> | 3 | **Record the registration evidence** (§17.6, §18.8) | Control/check designation and residuals. TBC does not appear to report these, so they are recorded manually or not at all |
> | 4 | **Archive `Targets.csv`** *(TBC 22905)* | The picked registration observations — the registration's field book |
> | 5 | **Archive the numbered SBET files** `sbet_<date>_reg_####.out` | Pending T28, assume Cleanup removes them |
> | 6 | **Archive the calibration JSON** (§14.5) | The system state the mission was processed under |
> | 7 | **Take the project backup Trimble asks for**, to a location that is part of the project archive (§25) — not a local copy on the processor's machine | A backup nobody can find is not a backup |
> | 8 | **Obtain the authorisation** §21.4 requires | — |
> | 9 | **Run Cleanup** | — |
> | 10 | **Record that it was run**, by whom, on what date, and what was archived first | Otherwise the absence of history is itself unexplained |
>
> Steps 2 through 6 are small files. The whole set is a few megabytes beside a project of tens of
> gigabytes, and they are the difference between a deliverable that can account for itself and one
> that cannot.
>
> *(Register item 35; §23, §25)*

## 21.7 The relationship to provenance

Cleanup is the sharpest instance of the problem §23 is about.

The provenance evidence inside a TBC project is genuinely good — trajectory properties naming the
origin, the input trajectory and the registration type; numbered SBET files; scans nested beneath
the trajectory that produced them; a `_reg_####` station suffix (§15.3, §13.6).

**IMPORTANT PROVENANCE LIMITATION.** Exported mobile mapping data may retain coordinate, timing,
and in some formats trajectory information, but **the captured Trimble documentation does not
establish that the output uniquely identifies the adjusted trajectory or registration result used
to create it** (§23).

> **The two findings compound.** Cleanup reduces the registration history available in the
> project; export is not documented as providing unique registration lineage. **A LAS point cloud
> exported after project cleanup may retain spatial and point-level metadata, but the captured
> Trimble documentation does not establish that it preserves sufficient registration and
> trajectory lineage to reconstruct how the final cloud was produced.**
>
> The practical concern is therefore not literally "no history." It is that **the deliverable may
> not contain enough documented provenance to reconstruct its processing history independently of
> the TBC project and Parametrix records.**
>
> That is not an argument against Cleanup. It is the reason §21.4 remains a Parametrix decision,
> and the reason §21.6 steps 2–6 are proposed to happen first.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We looked at a command that tidies a finished project by throwing away
> every registration attempt except the last one, along with the point clouds those attempts
> produced. It cannot be undone. Trimble's entire published guidance on it is four sentences, one
> of which says to back up first.
>
> **Why it matters.** Working on a difficult corridor, you will register, look at the result,
> change something, and register again. That is normal, careful work — it is what an adjustment
> looks like when you are paying attention. By the end, the project holds several versions of the
> same data, it is enormous, and it is genuinely confusing for whoever picks it up next. Cleanup
> is the obvious answer, and it is a reasonable one.
>
> **What can go wrong.** What it removes is not the deliverable. It is the ability to show how you
> got there. Before Cleanup, anyone can open the project and see that there were four attempts,
> what each produced, and which one was kept. After it, there is one result and no indication that
> anything else ever existed. Nobody has done anything wrong — but if a reviewer asks how the
> number was arrived at, the honest answer is now "from memory."
>
> This matters more than it would elsewhere because of §23: almost none of that history leaves the
> project when you export anyway. So the project file is where the evidence lives, and Cleanup is
> the thing that thins it, at the exact moment the job is being wrapped up and handed on.
>
> **What good looks like.** Cleanup is not the enemy. Running it blind is. A sound sequence is:
> finish QC, get the result accepted, run the Mission Report and keep it, write down which points
> were control and which were checks and what the residuals were, keep the small files — the
> picked targets, the numbered trajectory files, the calibration — take the backup Trimble asks
> for and put it somewhere the company can find it in three years, get whoever is supposed to
> authorise it to authorise it, and then run the command. Ten minutes and a few megabytes, and the
> deliverable can still account for itself.

---

# 22. Export and Deliverables

## 22.1 Export is a QA/QC step, not a file conversion

By the time a processor reaches this section the analytical work is done. It is tempting to treat
what follows as mechanical.

It is not. Export is the last point at which the project and the deliverable can diverge, and
several documented ways exist for them to do so silently:

- The scans exported may not be the registered ones (§22.2)
- The scans exported may not be the scans TBC generated at all (§22.3)
- Coordinates may be grid or ground, and one of those does not tell you its own scale factor
  (§22.5)
- Imagery may be present and black (§19.4)
- A selection drawn in a view may span scans built on different trajectories (§22.4)

**Every one of those produces a file that opens correctly, looks right, and is wrong.**

## 22.2 QC CHECK — CONFIRM SCANS WERE UPDATED AFTER REGISTRATION BEFORE EXPORT

> **CAUTION · the most consequential check in this section**
>
> **Registration does not modify the point cloud until Update Scans is performed** (§13.6, §15).
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> **export point cloud data that still reflects the pre-registration trajectory.** The export
> succeeds. The file is valid. The data is unregistered.
>
> Nothing in the export dialog references the registration state.

### How to verify, using documented evidence

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> | Evidence | What it shows | Source |
> |---|---|---|
> | **Scans are nested beneath the trajectory they were computed from** in Project Explorer | Scans under `Reg. Trajectory` / `RegTrajectory` were computed against it; scans under `Sbet` were not | *(TBC 22638, 22905, 26473)* |
> | **Updated scan stations carry a `_reg_####` suffix** — e.g. `Run_14_Laser Right_reg_0001 (S3)` | That station was produced by Update Scans against a registered trajectory | *(TBC 22638)* |
> | **The adjusted trajectory's properties** — `Origin: Registration result`, `Input trajectory`, `Registration type` | Which trajectory is the registered one | *(TBC 22905, 26473)* |
> | **Registered segments render in the "Undefined RMS" colour** | Which stretches of trajectory an adjustment actually affected | *(TBC 27248)* |

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Before any export from a registered mission, confirm in Project Explorer that the scan nodes
> selected for export sit beneath the intended registered trajectory, and that their stations
> carry the `_reg_####` suffix.**
>
> **Not adopted.** *(Register item 36)*

> **FIELD TESTING REQUIRED · T29**
>
> **Establish the reliable verification method for each export path.** Tree position and the
> station suffix are evidence *inside the project*. What is **not** established is how an export
> dialog resolves its selection — in particular:
>
> - Whether the **Mobile Mapping tab** exporters, which select by run, take the currently active
>   trajectory or a specific one
> - Whether the **Point Cloud tab** exporters, which select by region or by a rectangle drawn in a
>   view (§22.4), can be made to respect a trajectory at all
>
> Until tested, the only defensible verification is the project-side one above, performed
> immediately before export and recorded. *(Appendix E)*

## 22.3 Export timestamps — an unresolved question about what is exported

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Stated in identical wording in two export topics *(TBC 23339, 22501)*:
>
> "If the TIMESTAMP option has been set to **No**, the exported scans are **the ones processed
> with the Generate Scans feature**, and the color information will be exported if the generated
> scans have been processed with the color option set to on.
>
> If the TIMESTAMP option has been set to **Yes**, the exported scans are **reprocessed from the
> raw data** and directly written to the LAS format files, the color information will be exported
> in the LAS format files."

> **VENDOR CLARIFICATION REQUIRED**
>
> **When Export timestamps causes TBC to reprocess from the raw source data, which trajectory is
> used for that reprocessing?**
>
> **The captured documentation does not establish this.** Trimble states that reprocessing occurs
> and does not state what it reprocesses against. Both readings — the mission's currently applied
> trajectory, or the originally imported one — are consistent with the wording.
>
> **No speculation is offered here.** *(Appendix F)*

> **FIELD TESTING REQUIRED · T18 — the highest-priority test in this document**
>
> Export the same registered run twice, once with timestamps off and once on, and compare the
> point geometry.
>
> **Why it is the highest priority:** every quality step in the workflow — registration, Update
> Scans, filtering, colorization — acts on the **generated** scans. If reprocessing does not
> reflect the registered trajectory, then a documented, innocuous-sounding export option can
> deliver data that was never the data that was checked. *(Appendix E)*

Until T18 and the vendor question are resolved:

> **PARAMETRIX DECISION REQUIRED**
>
> **May exports be made with Export timestamps enabled before this behaviour is established?**
>
> GPS Time per point is genuinely useful and some downstream software requires it. The question is
> not whether timestamps are wanted but whether the cost of obtaining them is understood.
> *(Register item 37)*

## 22.4 Two export tabs that behave differently

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Mobile mapping exporters: **Home ▸ Data Exchange ▸ Export ▸ Mobile Mapping tab.** "A list of
> available exporters displays" *(TBC 23339, 23888, 22501)*.
>
> Generic point cloud exporters: **Home ▸ Data Exchange ▸ Export ▸ Point Cloud tab**
> *(TBC 11769)*.

| | **Mobile Mapping tab** | **Point Cloud tab** |
|---|---|---|
| Selection | **By run**, from Project Explorer or Plan View | **By point cloud region**, or a **Rectangle / Polygon Select** drawn in a graphic view |
| Run-aware | Yes | **No** |
| Imagery | Yes, per exporter | No |

> **IMPORTANT**
>
> **The Point Cloud tab exporters do not select by run or by trajectory.** Trimble's step is to
> "select the region(s) you want to export in the Project Explorer or graphic view", or draw a
> rectangle or polygon *(TBC 11769)*.
>
> ⚠ **OBSERVED SOFTWARE BEHAVIOR — assessment, flagged** · Nothing in the command ties the export
> to a trajectory. A rectangle drawn across a view could, in principle, span scans generated from
> different trajectories. **Whether TBC prevents, warns about, or silently permits this is not
> stated.**
>
> **FIELD TESTING REQUIRED · T23** — draw a selection across scans from two trajectories and
> observe. *(Appendix E)*

## 22.5 Coordinate handling — common to the point cloud exporters

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 11769, 27279)*
>
> Identical wording appears in both the generic exporter and the classified-regions exporter, so
> this is TBC's standard point-cloud export behaviour rather than a mobile mapping special case.

| Setting | Behaviour |
|---|---|
| **Scaling: Grid** | Points expressed in the current projected coordinate system, with the current combined scale factor. **"An associated .txt file is also created to specify the coordinate system and scale factor used."** Trimble warns: *"re-importing this file into TBC may cause some inconsistencies due to a double-scaling effect"* |
| **Scaling: Ground** | Points exported as ground coordinates "as they were measured in the field, independent of the coordinate system used", scaled from the 0,0 origin by the average combined scale factor. **"The scale factor is not exposed during export when this option is selected"** — recoverable only by exporting to grid and reading the `.txt` |
| **Applicability** | Selectable for e57, LAS, LAZ, POD, PTS, RCP. **TDX and PTX are always ground-based** |
| **ECEF export** | LAS or LAZ in ground-based scaling "that includes the project's global coordinate system information" |

> **IMPORTANT**
>
> **A ground-scaled export does not carry a record of the scale factor it used.** For a surveyor
> this is a familiar grid-versus-ground question with an unfamiliar wrinkle: the file cannot tell
> the recipient which it is, and one of the two options actively withholds the number needed to
> convert.
>
> The grid-scaled `.txt` sidecar and the ECEF option are the two documented ways to make an
> exported cloud self-describing about its coordinate frame. **Neither says anything about the
> trajectory** (§23).

## 22.6 The MX60 export paths

Six documented paths. **No preference between them is expressed or implied here — the choice of
deliverable format is a project and client matter that Parametrix has not decided.**

> **PARAMETRIX DECISION REQUIRED**
>
> **What are Parametrix's standard mobile mapping deliverable formats, and which export path
> produces each?** *(Register item 38)*

### 22.6.1 Export to LAS (Trajectory Split) — classified point cloud regions

*(TBC 27279)* · **Mobile Mapping tab**

**Prerequisite:** run **Extract Classified Point Cloud** in *Point Clouds ▸ Regions* first.

| | |
|---|---|
| **What leaves TBC** | Classified point cloud regions of one run, as LAS. "The classification code is added to the exported points" |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Grid or ground per §22.5; `.txt` sidecar on grid |
| **Timing** | LAS point records per §22.7 |
| **Imagery** | None |
| **Sidecars** | The scaling `.txt` |

**Settings** *(TBC 27279)*:

| Setting | Behaviour |
|---|---|
| **Splitting distance** | "a value in meter multiple of 250" |
| **Export both lasers in the same file** | Yes merges left and right. "You need to select at least one laser to export" |
| **Export laser left / right** | Independent Yes/No |
| **Split into files** | Splits the LAS per the Splitting Distance |
| **Sample points** | "random sampling be performed on the exported point cloud regions", with a target **Number of points** |
| **Format** | LAS **1.2 or 1.4** |
| **Export unit** | Unit of distance in the file |
| **Use inspection colors** | Exports Scan Inspection heat-map colours instead of true colour |

> **FIELD TESTING REQUIRED · T17**
>
> **Sample points performs *random* sampling to a fixed point count.** On a survey deliverable
> that is a destructive thinning with no documented spatial rule — no minimum spacing, no
> preservation of edges or breaklines. Its default state is not stated. *(Appendix E)*

> **Provenance implication:** the exporter is named *Trajectory Split*, and splits by distance
> along the trajectory. Despite the name, **no trajectory information is documented as
> accompanying the output.**

### 22.6.2 Export to TMX

*(TBC 22501)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images, side camera images, laser point clouds **and trajectory** |
| **Trajectory geometry** | **YES** — "The trajectory file is created **once for all devices**. It resides in a folder under the Mission folder" |
| **Specific trajectory identified** | **Not documented** |
| **Coordinate system** | Per §22.5. **"For the MX9 Export to TMX, the user must use a coordinate system without Geoid"** — *stated for the MX9 only; whether it applies to the MX60 is not stated* |
| **Timing** | Export timestamps option — **see §22.3** |
| **Imagery** | Panoramic (Pano), side (Sideview, Planar 1/2), back-facing (Planar 3); optional GPS attributes in the image files |
| **Sidecars** | `reference.csv` |

Output structure: a **Mission folder** plus one folder per device, with `laser`, `panorama`,
`planar*` and **`trajectory`** sub-folders. The MX60 example is illustrated in Trimble's topic.

> **Provenance implication:** this is one of two paths on which **trajectory geometry accompanies
> the deliverable.** A run carrying both an imported `Sbet` and a registered trajectory has two
> candidates, and **the topic does not state which is written.**
>
> **VENDOR CLARIFICATION REQUIRED** — which trajectory does the TMX export write when several
> exist under a run? *(Appendix F)* · **FIELD TESTING REQUIRED · T20** *(Appendix E)*

### 22.6.3 Export to TopoDot

*(TBC 23339)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images, side camera images, laser point clouds — as a *Raw Project Data* folder with *Image Project* and *LAS Files* sub-folders |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §22.5 |
| **Timing** | Export timestamps option — **see §22.3** |
| **Imagery** | Cubical images from the panoramic and side cameras, one set per camera per run |
| **Sidecars** | `.iprj` image project, `.lst` containing all image position and orientation, `.cal` camera models — one per camera |

**Prerequisites** *(TBC 23339)*: "You need to first generate scans from the raw data before
exporting them to the TopoDot software. Otherwise, nothing will be exported." And: **"You must
close all run views prior to export. Otherwise, a warning message will pop up."**

**LAS files:** "a couple of 1.4 LAS format files, one couple per run."

> **Provenance implication:** the `.lst` file carries **image position and orientation**, which is
> trajectory-derived information at the station level. **It is not documented as identifying the
> trajectory it came from.**

### 22.6.4 Export to Solv3D

*(TBC 23888)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images and laser point clouds |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §22.5 |
| **Timing** | **Trimble recommends No** — "Solv3D does not need the Timestamps information. Trimble recommends turning this option to No" |
| **Imagery** | Panoramic only, in a `Panorama` folder; a `reference.csv` alongside "which contains Roll, Pitch and Yaw information and X, Y, Z as well" |
| **Sidecars** | `reference.csv` |

Output: a folder named for the mission, with `Lasers` and `Panorama` sub-folders. LAS 1.4, "one
couple per run in case of a single scanner system and two when a double laser system is used."

> **Note the interaction.** Trimble's recommendation to disable timestamps here has a second
> effect it does not mention: per §22.3, timestamps off means the **generated** scans are
> exported rather than reprocessed ones. On this path the recommended setting is also the one
> that preserves the processing you performed.

### 22.6.5 Generic Point Cloud Export

*(TBC 11769)* · **Point Cloud tab**

| | |
|---|---|
| **What leaves TBC** | Point cloud only, in `.e57` (plain or **structured**), `.las`, `.laz`, `.pod`, `.pts`, `.ptx`, `.rcp`, `.tdx` |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §22.5, including the ECEF option |
| **Timing** | LAS point records per §22.7 |
| **Imagery** | None |
| **Sidecars** | The scaling `.txt` |
| **Split** | *By station* — a separate LAS per scan station; *None* — a single LAS from all stations |

> **This is the path most likely to be used for an ordinary LAS or E57 deliverable, and it is the
> one with the least documented provenance and no run awareness** (§22.4).

### 22.6.6 Publish to TRCPS

*(TBC 29527)* · **Home ▸ Data Exchange ▸ Publish to TRCPS**, then the **Mobile Mapping** tab

Uploads to a **Trimble Connect** project via the **Trimble Desktop Utility (TDU)**, installed with
TBC. Requires a **Trimble ID**; uploads consume the account's Trimble Connect storage quota.

| | |
|---|---|
| **What leaves TBC** | Point cloud, **trajectories**, and optionally imagery |
| **Trajectory geometry** | **YES, MANDATORY** — "By default, mobile mapping point cloud and trajectories will be **automatically exported**" |
| **Specific trajectory identified** | **Not documented** |
| **Selection** | **Run-aware** — an individual run, multiple runs (Shift/Ctrl+Click), or the entire mission (Ctrl+A). The selection must include scan data; if not, Trimble says run **Generate Scans** first |
| **Imagery** | Publish panoramic / side / back-facing images, each optional |
| **Privacy** | **Blur people**, **Blur vehicles** — greyed out until an images option is selected; prompts for **GPU (if compatible) or CPU** |
| **In the delivered dataset** | The **3D+ View** offers 3D, Map, Image and Panorama modes; in 3D and Panorama, **"trajectories and camera markers can be included or hidden as needed"** |

> **Provenance implication:** the trajectory is **not optional** on this path — the publishing
> options govern imagery only — and it is a first-class, viewable object in the delivered dataset.
> **Which trajectory is published when several exist under a run is not documented.**
>
> **VENDOR CLARIFICATION REQUIRED** *(Appendix F)* · **FIELD TESTING REQUIRED · T19** *(Appendix E)*

> **OBSERVED SOFTWARE BEHAVIOR** · Trimble Connect's **UK region** is currently unavailable for
> Publish to TRCPS and Trimble Mobile Mapping data *(TBC RN 2026.10)*. Not applicable to
> Parametrix, but it confirms Publish to TRCPS is a Connected Workspace function.

## 22.7 Summary — what is documented as leaving TBC

| Path | Trajectory geometry travels? | Specific trajectory identified? |
|---|---|---|
| Classified LAS, Trajectory Split | **No** | **No** |
| Export to TMX | **Yes** | **Not documented** |
| TopoDot | No | No |
| Solv3D | No | No |
| Generic Point Cloud Export | No | No |
| **Publish to TRCPS** | **Yes, mandatory** | **Not documented** |

### Metadata documented as travelling, where applicable

| Metadata | Where |
|---|---|
| **Coordinate system and scale factor**, in a `.txt` sidecar | Any grid-scaled point cloud export *(TBC 11769, 27279)* |
| **Project global coordinate system**, embedded | ECEF option, LAS/LAZ *(TBC 11769)* |
| **GPS Time per point** | LAS exports with timestamps on. "According to the ASPRS LAS 1.4 specification, the Timestamp information refers to the GPS Time in the point records, i.e., standard GPS Time (satellite GPS Time) minus 1 billion of seconds. The origin of standard GPS Time is defined as midnight of the morning of January 6, 1980" *(TBC 23339, 22501)* |
| **Image position and orientation** | TopoDot `.lst`; Solv3D `reference.csv` (Roll, Pitch, Yaw, X, Y, Z) |
| **Latitude, longitude, altitude, acquisition time** in image files | Where GPS attributes are enabled |
| **`Program name: Trimble Business Center`** in image EXIF | *(TBC 21713_1)* |
| **Trajectory geometry** | TMX export; Publish to TRCPS |

> **IMPORTANT PROVENANCE LIMITATION**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**
>
> A further limit on that statement: **Trimble's help topics describe dialogs, options and output
> structures. They do not exhaustively enumerate LAS header fields or VLR content.** Something may
> be written that the documentation does not mention.
>
> This is therefore a **software-behaviour testing question**, not an unresolved documentation
> research question. All known MX60 export and publish paths have been reviewed.
> **FIELD TESTING REQUIRED · T22** — export and inspect the file directly. *(Appendix E; §23)*

## 22.8 Known limitations and silent failures

| Limitation | Path | Source |
|---|---|---|
| **Corrupted side camera images are exported as black images** | TopoDot, TMX | *(TBC 23339, 22501)* |
| All run views must be closed before export | TopoDot | *(TBC 23339)* |
| Scans must be generated first or nothing is exported | TopoDot, Solv3D | *(TBC 23339, 23888)* |
| Ground scaling does not expose its scale factor | All point cloud exports | *(TBC 11769, 27279)* |
| Grid-scaled re-import may double-scale | All point cloud exports | *(TBC 11769, 27279)* |
| MX9 Export to TMX requires a coordinate system without Geoid | TMX — **MX60 applicability not stated** | *(TBC 22501)* |
| Random sampling with no spatial rule | Classified LAS | *(TBC 27279)* · T17 |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We wrote the finished data out of TBC in whatever format the client needs
> — a LAS file, a package for TopoDot or Solv3D, or a publication to Trimble Connect — and we
> looked carefully at what each of those paths actually carries with it.
>
> **Why it matters.** This is the last moment the project and the deliverable are the same thing.
> Everything after this, the client has; everything before this, you can still fix. And there are
> several documented ways for the two to quietly diverge here.
>
> **What can go wrong.** The one to burn into memory: **registering a mission does not change the
> point cloud.** If nobody ran Update Scans, the file you export is the unregistered data. It
> opens fine, it looks identical, the residuals in your notes were good — and the client has the
> version from before the adjustment. Check that the scans you are exporting sit under the
> registered trajectory and carry the `_reg_` suffix, every time.
>
> Two more. There is an innocuous-looking option called **Export timestamps** that, when switched
> on, makes TBC rebuild the cloud from the raw data instead of exporting the scans you processed.
> Trimble does not say what trajectory that rebuild uses. Until somebody tests it, treat that
> switch as a decision rather than a convenience. And if you export in ground coordinates, the
> file does not record the scale factor it used — the grid option writes a small text file beside
> the cloud that does.
>
> **What good looks like.** Before exporting: the scan nodes you have selected sit beneath the
> trajectory you intended, the stations carry the registration suffix, and you know whether you
> are writing grid or ground. After exporting: the file opens, the extents match the corridor, the
> point count is plausible, the sidecar is present if you expected one, and somebody has opened a
> sample of the imagery rather than counting it. That is ten minutes, and it is the difference
> between a delivery and a re-delivery.

---

# 23. Data Provenance and Audit Trail

## 23.1 The question this section answers

> *A client, a reviewer, or opposing counsel is looking at a point cloud Parametrix delivered
> three years ago. They ask: how do we know this is the adjusted version, and which adjustment
> was it?*

That question is ordinary in survey work. A conventional adjustment produces a report naming its
observations, its constraints and its residuals, and the report travels with the deliverable.
Mobile mapping does not work that way, and this section sets out precisely what can and cannot be
demonstrated.

## 23.2 Four things that are related and not interchangeable

Conflating these is the most common error in discussing mobile mapping provenance, and it leads
people to believe a question has been answered when it has not.

| | What it establishes | What it does **not** establish |
|---|---|---|
| **Spatial reference metadata** | Which coordinate system and scale the coordinates belong to | Which trajectory produced them |
| **Trajectory information** | The sensor path through space and time | Which *version* of that path this is |
| **Registration history** | What adjustments were applied after the original trajectory solution | — |
| **Data provenance** | Where the data came from and how it was processed, end to end | — |

Stated as plainly as possible:

> **A coordinate system does not prove which trajectory produced the points.**
>
> **GPS Time does not prove which registration was applied.**
>
> **Trajectory geometry without trajectory identity does not necessarily reconstruct the
> processing lineage.**

That last one deserves a sentence of its own, because it is the subtlest. The TMX export and
Publish to TRCPS both carry **trajectory geometry** out of TBC (§22). A recipient therefore holds
a path through space. What they do not hold is a statement of **which** path it is — the imported
one, the first registration, or the fourth — and on a project where several existed, geometry
alone may not distinguish them, particularly where a registration made a small correction.

## 23.3 The provenance chain

Each transition, with what exists at that point, what Cleanup can remove, and what survives
export.

### Legend

**In TBC** = a project object · **On disk** = a file in the project or raw data folder ·
**Cleanup** = may be removed by §21 · **Export** = documented as surviving export

---

### 1 · Raw MX60 mission → imported mission

| | |
|---|---|
| **In TBC** | Mission node; runs; Capture Devices; start/stop, duration, **covered distance**, active trajectory file *(TBC 22499)* |
| **On disk** | The `.mxdb`, raw POS data, raw scanner and camera data, `Extcal.json`, mission logs *(TBC 25943)* |
| **Cleanup** | The raw data is outside the project and unaffected |
| **Export** | Not applicable |
| **Parametrix record** | **The field record** — conditions, incidents, what was not collected. No software artefact exists (§9) |

### 2 · Imported mission → trajectory

| | |
|---|---|
| **In TBC** | The trajectory node under each run; RMS colouring from `smrmsg_xxx.out` *(TBC 27248)* |
| **On disk** | `sbet_[mission].out` **or** `sbet_[mission]_[frame].out` in `NAVPROC/Export/`; the processing report in `NAVPROC/Report/`; with **Backup SBET Next to MXDB**, a copy **and a log of the frame and epoch used** beside the `.mxdb` *(TBC 25943)* |
| **Cleanup** | Keeps the trajectory "consistent with the latest version of navigation and trajectory information file (SBET or NAV)" *(TBC 26466)* |
| **Export** | Trajectory **geometry** on TMX and TRCPS; **identity not documented** |
| **Parametrix record** | Which computation mode, which base station, which settings — **no single artefact captures these** (§12.3) |

> **The frame-and-epoch log written by Backup SBET Next to MXDB is the only artefact found in the
> whole workflow that records the frame a trajectory was computed in, and it lives with the raw
> data rather than inside the project.** That is why enabling the option is proposed in §12.4.

### 3 · Trajectory → generated scans

| | |
|---|---|
| **In TBC** | Scan nodes **nested beneath the trajectory that produced them** *(TBC 22638)*; the **Results of Scan Generation** dialog recording filters, range and colorization per run *(TBC 22499)* |
| **On disk** | RWCX point cloud data in the project |
| **Cleanup** | Scans associated with removed registrations are removed *(TBC 26466)* |
| **Export** | The cloud itself. **Filter and colorization settings are not documented as travelling** |
| **Parametrix record** | **Capture the Results of Scan Generation** — proposed §13.5 |

### 4 · Calibration state

| | |
|---|---|
| **In TBC** | Camera and sensor properties: **Boresight installation** vs **Boresight refinement**, lever arm installation vs refinement *(TBC 24868)* |
| **On disk** | `Extcal.json` with the raw data; an exported calibration JSON containing the **Installation Matrix** and **Refinement Matrix** for each sensor *(TBC 22920)* |
| **Cleanup** | Not addressed by Trimble's description |
| **Export** | **Not documented as travelling with any deliverable** |
| **Parametrix record** | The **Mission Report** carries per-sensor boresight and lever-arm calibration **with a date of calibration** *(TBC 24868)* — the only dated calibration record found |

### 5 · Registration → adjusted trajectory

| | |
|---|---|
| **In TBC** | The adjusted trajectory node with properties **`Origin: Registration result`**, **`Input trajectory`**, **`Registration type`** *(TBC 22905, 26473)*; picked and updated targets named for the registration; registered segments rendered in the **"Undefined RMS"** colour *(TBC 27248)* |
| **On disk** | **`sbet_<date>_reg_####.out`**, incrementing per registration, in the project folder *(TBC 22905)*; **`Targets.csv`** holding the picked targets, when Registration Auto-Saving is on *(TBC 22905)* |
| **Cleanup** | **Keeps only the most recent registration.** Earlier trajectories and their scans are removed. **Whether the numbered SBET files are deleted from disk is untested — T28** |
| **Export** | **No export path is documented as identifying the registration result** (§22.7) |
| **Parametrix record** | **Which points were control and which were checks, and the residuals on each** — TBC is not documented as reporting this after the fact (§17.6) |

### 6 · Update Scans → final point cloud state

| | |
|---|---|
| **In TBC** | New scan nodes beneath the adjusted trajectory; stations carrying a **`_reg_####`** suffix *(TBC 22638)* |
| **On disk** | RWCX data in the project |
| **Cleanup** | Scans of removed registrations are removed |
| **Export** | The cloud. **The `_reg_####` suffix is a station name inside TBC and is not documented as appearing in exported filenames** |
| **Parametrix record** | Confirmation that Update Scans was performed before export (§22.2) |

### 7 · Export → delivered dataset

| | |
|---|---|
| **Travels** | Coordinate system and scale factor (`.txt`, grid); project global CRS (ECEF); GPS Time per point; image position and orientation in some paths; image EXIF naming TBC; **trajectory geometry on TMX and TRCPS** |
| **Not documented as travelling** | Trajectory name or ID; SBET filename; registration result; registration type; `_reg_####` sequence; source run or mission identifier within the data; calibration identity |
| **Cleanup** | Not applicable — but what Cleanup removed is no longer available to be recorded |
| **Parametrix record** | **The delivery record** — what was exported, from which node, on what date, by whom |

---

## 23.4 The limitation, stated precisely

> **IMPORTANT PROVENANCE LIMITATION**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**

### What this does and does not mean

| It does **not** mean | It **does** mean |
|---|---|
| That exports carry no metadata | That the metadata they carry answers *where are these coordinates*, not *how were they produced* |
| That the trajectory never leaves TBC | That where it does leave (TMX, TRCPS), **which** trajectory it is is not documented |
| That provenance is impossible | That it depends on the TBC project and on Parametrix's own records, not on the deliverable |
| That Trimble's software lacks the information | That **Trimble's documentation does not establish it**, and does not enumerate LAS headers or VLR content — so something undocumented may be written (T22) |

> **The practical concern is therefore not "no history."** It is:
>
> **The deliverable may not contain enough documented provenance to reconstruct its processing
> history independently of the TBC project and Parametrix records.**

### Classification

> **PARTLY CONFIRMED.**
>
> **This no longer represents missing documentation.** All known MX60 export and publish paths
> have been reviewed (§22.6). The remaining uncertainty is about **software behaviour Trimble does
> not document**, resolvable by test (T18–T23), not by further reading.

## 23.5 Cleanup and provenance, combined

> Cleanup reduces the registration history available in the project.
>
> Export is not documented as providing unique registration lineage.
>
> **Therefore performing Cleanup before preserving the appropriate project evidence may reduce
> Parametrix's ability to reconstruct the processing history later.**

That is a finding, not a prohibition.

> **PARAMETRIX DECISION REQUIRED**
>
> This is precisely why the Cleanup policy (§21.4) remains open. **This document does not prohibit
> Cleanup and does not require it.** The combined finding above is the reason the decision matters
> more than it appears to, and it is the input Parametrix needs in order to make it.
> *(Register item 35)*

### T28 — why it is high priority here

> **FIELD TESTING REQUIRED · T28 — high priority**
>
> **Does Cleanup delete the `sbet_*_reg_####.out` files physically from storage, or only remove
> the corresponding project objects and references?**
>
> **Until tested, distinguish two things and do not assume one implies the other:**
>
> | **Project object retention** | **Underlying file retention** |
> |---|---|
> | Whether the trajectory node still appears in Project Explorer | Whether the `.out` file still exists in the project folder |
>
> The registered SBETs are written to the project folder on disk, not inside the TBC database
> *(TBC 22905, 26473)*. Removing a project object does not necessarily delete the file it points
> at, and Trimble does not address this.
>
> **The result materially changes what must be archived before Cleanup.** If the files survive,
> they are a partial lineage record that outlives the operation. If they do not, that record must
> be copied out beforehand or it is gone. *(Appendix E; §21.6, §25)*

## 23.6 What Parametrix would need to record

Stated as a gap analysis, not as policy.

> **PARAMETRIX DECISION REQUIRED**
>
> **What provenance record must accompany a mobile mapping deliverable, and where does it live?**
>
> Six facts cannot be reconstructed from the deliverable on current evidence. Each is cheap to
> record at the time and effectively unrecoverable later:
>
> | Fact | Why it is not in the deliverable |
> |---|---|
> | Which trajectory the delivered cloud was built on | §23.4 |
> | Which registration was applied, and which of several | §23.4 |
> | Which points were control and which were independent checks | TBC not documented as reporting it (§17.6) |
> | The residuals on each | Live in a dialog; the report question is open (§17.6) |
> | The calibration state at processing | In the Mission Report, if run (§14.6) |
> | Whether Cleanup was run, and what was archived first | No artefact (§21) |
>
> **This document does not establish a recordkeeping policy.** It establishes that without one,
> the six facts above are lost. *(Register item 29)*

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted.** A minimal record that would close the gap, offered for decision:
>
> - **A one-page delivery record** per dataset: mission ID, trajectory node name, SBET filename
>   including its `_reg_####` number, registration type, export path and date, exported by whom
> - **The Mission Report**, run before Cleanup (§21.6)
> - **The control/check table** — point ID, Use XY, Use Z, As Check, residual (§17.6)
> - **The calibration JSON** in force (§14.5)
> - **`Targets.csv`** (§21.6)
>
> Five artefacts, four of them small files that already exist. *(Register item 29)*

## 23.7 Reconstruction paths that do exist

Where a delivered dataset must be tied back after the fact, two routes exist on current evidence.
**Both are reconstruction, not provenance, and both depend on Parametrix having retained
something.**

**Timestamp matching.** LAS point records carry GPS Time *(TBC 23339, 22501)*, and a retained SBET
is a time series. A point's timestamp can be matched to an epoch in a specific SBET. This
identifies *a* trajectory only if the candidate SBETs differ measurably at that epoch, and it
requires the SBETs to have been kept.

**Trajectory geometry comparison.** A TMX or TRCPS delivery contains trajectory geometry
(§22.6.2, §22.6.6), which could be compared against retained `sbet_*_reg_####.out` files. Same
caveat: it requires retention, and it distinguishes candidates only where they differ.

> **FIELD TESTING REQUIRED · T30** — establish whether either reconstruction path works in
> practice on a real dataset with two candidate trajectories. Neither has been attempted.
> *(Appendix E)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We traced the data from the raw mission to the delivered file and asked, at
> every step, what record exists of what was done — inside TBC, on disk, and in the file the client
> receives.
>
> **Why it matters.** In conventional survey work, an adjustment comes with a report. It names the
> observations, the constraints and the residuals, and it goes out with the job. If somebody
> queries the result in five years, you open the report. Mobile mapping does not produce that
> document. The evidence exists — it is genuinely good inside the TBC project — but it is spread
> across node names, file suffixes, a dialog and a colour, and the documentation does not establish
> that any of it reaches the delivered file.
>
> **What can go wrong.** Be careful about what the problem actually is, because it is easy to
> overstate. The exported file is not empty of information: it knows its coordinate system, it may
> carry a scale factor sidecar, its points may be timestamped, and on two of the six paths the
> trajectory itself travels with it. What it does not do, as far as Trimble's documentation
> establishes, is say *which* trajectory — the original, or the first registration, or the fourth.
> So a delivered cloud can tell you where its coordinates belong and not how they were arrived at.
>
> The practical failure is a client query three years on, a project file that was cleaned up, and a
> processor who has left. The data is fine. Nobody can demonstrate that it is fine.
>
> **What good looks like.** The deliverable is not the record — the project and a short written
> note are. A page per dataset naming the trajectory, the registration and its number, which points
> were control and which were checks, what the residuals were, and what was archived before the
> project was tidied up. Five minutes at the end of a job, and the difference between "we are
> confident in it" and "here is why."

---

# 24. Final QA/QC

## 24.1 What this section is

The point where every earlier check converges, performed once, before the data leaves Parametrix.

> **IMPORTANT**
>
> **Final QA/QC is not a single RMS number and cannot be reduced to one.**
>
> Trimble's own position, stated in two separate topics: **bad RMS can demonstrate failure; good
> RMS does not by itself demonstrate success** *(TBC 24886, 25096)*. A final check built on one
> number would pass exactly the datasets most likely to be wrong — those with sparse control, or
> with a systematic error common to every observation (§18.1).
>
> What follows is a **layered verification**. No layer is sufficient alone; the confidence comes
> from their agreement.

## 24.2 The ten layers

| # | Layer | Answers |
|---|---|---|
| 1 | **Mission completeness** | Did we collect what we said we would? |
| 2 | **Trajectory quality** | Where was the navigation solution weak? |
| 3 | **Coordinate system verification** | Do the coordinates belong where we think? |
| 4 | **Control usage** | Were the checks genuinely independent? |
| 5 | **Registration results** | Did the adjustment work? |
| 6 | **Point cloud visual QC** | Does the data look right where numbers cannot reach? |
| 7 | **Corridor continuity** | Is it right *everywhere*, not just where we looked? |
| 8 | **Imagery QC** | Is the imagery complete and usable? |
| 9 | **Export state verification** | Is the exported file the data we checked? |
| 10 | **Deliverable review** | Is the package correct and openable? |

---

### Layer 1 · Mission completeness

Was all intended corridor coverage actually collected?

| Check | Evidence |
|---|---|
| **Covered distance** against the planned extent and the field record | Mission properties *(TBC 22499)* |
| **Run count** against the field record | Project Explorer |
| **Coverage in plan** — drive the trajectory in Plan View against the project extent | Plan View |
| Gaps, aborted runs and re-drives noted in the field record | §9, §10 |

> Trimble provides covered distance and run count. **The planned extent and the field record are
> Parametrix artefacts** — this layer only works if §9 produced them.

### Layer 2 · Trajectory quality

Review the trajectory solution rather than treating the mission as uniformly good or bad.

| Check | Evidence |
|---|---|
| **RMS colouring** of the trajectory in Plan View | *(TBC 25943, 27248; §12.4, §18.4)* |
| **Trajectory Plots** from the SBET computation | *(TBC 27415)* |
| **Suspect stretches identified and listed**, not averaged away | — |

> **The purpose of this layer is to produce a list, not a verdict.** A mission is not "good" or
> "bad"; it has stretches. Identifying them directs Layers 5, 6 and 7 to where they matter, and
> tells a reviewer where the residual risk sits.

> **Note the limit.** Registered segments render in the **"Undefined RMS"** colour *(TBC 27248)*,
> so a registered trajectory no longer shows its original RMS in those stretches. Where possible,
> review the RMS picture **before** registration as well as after.

### Layer 3 · Coordinate system verification

| Check | Evidence |
|---|---|
| **Project CRS** matches the control network and the client requirement | Project settings; §5 |
| **Vertical datum and geoid** as specified | Project settings |
| **Epoch**, where a time-dependent datum is in use | *(TBC RN 2026.10; §12.6)* |
| **SBET filename** — `sbet_[mission].out` or `sbet_[mission]_[frame].out` | *(TBC 25943; §12.4)* |
| **Scale factor handling at export** — grid or ground, sidecar present | *(TBC 11769, 27279; §22.5)* |

> **IMPORTANT · read the SBET filename correctly**
>
> The `_[frame]` form is a **documented indicator that POSPac used the frame-transformation
> workflow** — it computed in ITRF00 and then transformed. That is all it is.
>
> | It tells you | It does **not** tell you |
> |---|---|
> | That an additional transformation occurred | That the transformation parameters were right |
> | Where to direct scrutiny | That the project CRS is set up correctly |
> | | That the final point cloud is accurate |
>
> **The plain filename is equally not proof of correctness** — it means only that POSPac
> recognised the datum and epoch it was given, which may still be the wrong ones. Treat either
> form as a flag for review, never as a verdict.

### Layer 4 · Control usage

Confirm that the checks were genuinely independent.

| Check | Evidence |
|---|---|
| **Which points were Use XY, Use Z, As Check** | *(TBC 22905, 26473)*. **Reloadable via Edit a Run / Edit a Mission** *(TBC 25362, 26578)* — TBC is not documented as reporting it otherwise (§17.6) |
| **Check points were designated before the adjustment and not changed during it** | Parametrix record (§17.4) |
| **At least one point was not a check** — TBC enforces this, but the near-miss is invisible | *(TBC 22905)* |
| **Check point distribution** — along the corridor, in each GNSS environment, near each end | §17.5 |

> **CAUTION**
>
> **Confirm that check points were not allowed to drive the adjustment.** The failure this guards
> against is a processor who saw a check residual they disliked and ticked the point into the
> adjustment. Every step of that is well intentioned; the result is an adjustment measured against
> itself.
>
> On current evidence the only way to confirm this after the fact is to **reload the registration
> through Edit**, which restores the original Use XY / Use Z / As Check choices *(TBC 25362,
> 26578)*, and compare against the designation recorded before processing began.

### Layer 5 · Registration results

| Check | Evidence |
|---|---|
| **Numerical residuals on control used**, by component | Targets pane; signed in the report from 2025.21 *(TBC RN 2025.21; §17.6)* |
| **Residuals on independent check points** | Same |
| **Run-to-run RMS statistics**, where used — three axes, every 20 m, `No overlap` rows read | *(TBC 25096; §16.6)* |
| **Registration type used, and whether it suited the error** | *(TBC 22905; §15.5)* |
| **For a Local adjustment: was the delivered extent bracketed by control?** | §15.5 — it does not extrapolate |
| **Visual alignment** | Layer 6 |

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> **Bad RMS can demonstrate failure. Good RMS does not by itself demonstrate success.** This layer
> is not complete without Layers 6 and 7.

### Layer 6 · Point cloud visual QC

| Check | Method |
|---|---|
| **Overlapping passes** | Cutting Plane View, **rendering set to Scan Color**, point size increased, plane dragged along the run *(TBC 25096, 24886; §18.5)* |
| **Flat surfaces at range** | Thickening with distance |
| **Ends of the corridor** | Where a Local adjustment stopped; where the smoother had data on one side only |
| **The suspect stretches from Layer 2** | Did the registration actually fix them? |
| **Features near control vs far from control** | Residual growth with distance from constraint |

> **IMPORTANT · the rendering setting is part of the check**
>
> **Set rendering to Scan Color — one colour per scan — before looking for misalignment.**
>
> In a single colour, **two surfaces 4 cm apart look exactly like one surface 4 cm thick.** You
> will look directly at the defect and not see it. The visualisation setting is not a display
> preference here; it is what makes the check possible.

### Layer 7 · Corridor continuity

> **CAUTION**
>
> **Do not rely solely on isolated spot checks.**
>
> Mobile mapping error is **correlated in time, not scattered** (§2.3). It arrives in stretches
> because it is driven by a filter that evolves smoothly over seconds and minutes. A corridor that
> is excellent for 2 km and 5 cm out for 300 m **will pass every spot check you take** and fail at
> the one place the client happens to measure.
>
> The inspection strategy must be capable of identifying **localised** degradation, which means
> traversing the corridor rather than sampling it.

> **PARAMETRIX DECISION REQUIRED**
>
> **What is the corridor continuity inspection method, and at what interval or coverage?**
>
> No Trimble source prescribes one. The method must be able to detect a degraded stretch shorter
> than the sampling interval, which rules out sparse spot checks. Candidate approaches — dragging
> the cutting plane continuously, a systematic interval tied to the Layer 2 suspect list,
> deviation analysis against a reference surface — have different costs and different detection
> limits.
>
> *(Register item 39)*

### Layer 8 · Imagery QC

| Check | Evidence |
|---|---|
| **Coverage** for the full corridor | §19.3 |
| **Exposure, blur, obstruction, contamination** | §19.3 |
| **Corrupted images** — exported as **black**, silently | *(TBC 23339, 22501; §19.4)* |
| **Colour fringing at feature edges** on colorized clouds | §19.5 — indicates camera boresight (§14.4) |
| **Blur applied where required** | §19.6 |

> **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED**
>
> A **file-size scan** of exported imagery as a screening method for black images. **Not a Trimble
> procedure and not yet validated** — see §19.4 for the logic and its limits. **File size alone
> cannot establish image validity.**
>
> **This is not mandatory and should not be treated as a required step until validated.**
> *(Register item 31)*

### Layer 9 · Export state verification

> **CAUTION · carry this from §22.2**
>
> **Confirm that the exported point cloud represents the intended final trajectory and
> registration state, to the extent TBC permits that to be verified.**
>
> **Registration does not modify the point cloud until Update Scans is performed** (§13.6). An
> operator can complete a registration, obtain good residuals, pass Layer 5 — and export data that
> still reflects the pre-registration trajectory.

| Check | Evidence |
|---|---|
| **Scan nodes selected for export sit beneath the intended registered trajectory** | *(TBC 22638, 22905, 26473)* |
| **Stations carry the `_reg_####` suffix** | *(TBC 22638)* |
| **The trajectory's properties** read `Origin: Registration result`, with the expected `Input trajectory` and `Registration type` | *(TBC 22905, 26473)* |
| **Export timestamps setting recorded** — and §22.3 understood | *(TBC 23339, 22501)* |
| **Scaling recorded** — grid or ground; sidecar present if grid | *(TBC 11769, 27279)* |

> **FIELD TESTING REQUIRED · T29** — the reliable verification method **for each export path** is
> not established; how an export dialog resolves its selection is undocumented (§22.2). Until
> tested, the project-side checks above, performed immediately before export and recorded, are the
> only defensible verification. *(Appendix E)*

### Layer 10 · Deliverable review

Performed on the exported files, not in TBC.

| Check |
|---|
| **Expected files exist** — the full set, named as agreed |
| **Expected extents are present** — open the data and compare against the project extent |
| **Coordinate system is correct** |
| **Units are correct** |
| **Each file opens successfully** in software other than the one that wrote it |
| **Point count and file size are plausible** for the extent and density |
| **Imagery exists where required**, and a systematic sample has been opened and looked at |
| **Sidecars exist where required** — the scaling `.txt`, `reference.csv`, `.lst`, `.cal`, per §22.6 |
| **No obviously corrupted output** |
| **Project-specific deliverable requirements are met** |

> **No acceptance limits are stated here.** Point count, file size and extent are checked for
> **plausibility against the project**, not against any figure in this document. Project-specific
> acceptance limits are set per job and are not invented here.

---

## 24.3 Acceptance

> **PARAMETRIX DECISION REQUIRED**
>
> **What constitutes acceptance of a mobile mapping deliverable at Parametrix, who signs it, and
> against what?**
>
> **No numerical acceptance criterion appears anywhere in this document. No Trimble source in the
> set provides one, and inventing one would be indefensible.**
>
> The framework must combine four things, and a rule built on any one alone will fail:
>
> | Component | Why necessary | Why not sufficient |
> |---|---|---|
> | **Numerical residuals** on control used | Objective, repeatable | Measures fit to its own observations (§18.1) |
> | **Independent check information** | The only numerical evidence of accuracy | Sparse — a handful of points cannot characterise a corridor |
> | **Visual inspection** | Catches what no number reports | Subjective, and dependent on who looked and how |
> | **Project accuracy requirement** | The only thing that makes a threshold meaningful | Varies per job; not a property of the system |
>
> **Under no circumstances should this SOP acquire a statement of the form "RMS below X equals
> pass."**
>
> *(Register item 13; §15.9, §18.9)*

## 24.4 The record

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted.** A final QA/QC record covering the ten layers, naming who performed each and
> when, plus the provenance record proposed in §23.6.
>
> Two layers — 6 and 7 — produce **no software artefact whatsoever**. If a reviewer asks whether
> the visual check was performed and over what extent, the only possible answer is a record
> somebody wrote. *(Register item 29)*

## 24.5 Blocked pending resolution

These should be settled before a final QA/QC procedure is signed off:

| Item | Why it blocks |
|---|---|
| **T18** — Export timestamps and reprocessing | Layer 9 cannot be completed while it is unknown whether a documented export option substitutes different data |
| **T29** — per-path export verification | Layer 9's method is not established |
| **T28** — Cleanup and the SBET files | Determines what must be archived before the project is tidied (§21, §23.5) |
| **Register item 39** — continuity method | Layer 7 has no defined method |
| **Register item 13** — acceptance framework | Layers 5 and 10 have no threshold |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We ran a single, structured check over the whole job before it left the
> building — ten layers, from "did we collect the whole corridor" through to "does the file the
> client gets actually open."
>
> **Why it matters.** Every layer catches something the others cannot. The numbers catch a broken
> adjustment. The independent check points catch an adjustment that fitted its own observations
> beautifully and is still in the wrong place. The visual check catches what neither number
> reports. And the last two layers catch the case where all the analysis was right and the wrong
> file went out.
>
> **What can go wrong.** Three things, and they are the same three throughout this document.
>
> **Trusting a good number.** Trimble says it plainly, twice: a bad RMS proves failure, a good one
> proves nothing on its own. If the only evidence is a small residual, you have not checked the
> work — you have checked the arithmetic.
>
> **Spot-checking a corridor.** The error comes in stretches. Two kilometres perfect and three
> hundred metres out will pass every sample you take, and the client will measure in the three
> hundred.
>
> **Exporting before updating the scans.** The adjustment lives on the trajectory until somebody
> runs Update Scans. Skip it and you deliver the version from before the registration — same file
> size, same extents, opens fine, centimetres out.
>
> **What good looks like.** The covered distance matches the plan. The trajectory picture shows
> short degraded stretches where you expected them, and you have a list of them. Points the
> adjustment never saw come back in the same range as the ones it used. A cutting plane dragged
> the length of every overlap — in scan colour — shows one wall, not two. The imagery has been
> opened, not counted. The exported scans sit under the registered trajectory. And somebody has
> written down that all of that happened, because two of these checks leave no trace in the
> software at all.

---

# 25. Archiving and Records

## 25.1 Why this section carries more weight than usual

In most survey work the archive is a formality — the deliverable and its report tell the story,
and the archive is insurance.

In mobile mapping it is the primary evidence. §23 established that **the captured Trimble
documentation does not establish that an exported deliverable uniquely identifies the adjusted
trajectory or registration result used to create it.** The project and Parametrix's own records
are therefore where the processing history lives, and an archive that does not hold them holds a
point cloud and a coordinate system.

> **PARAMETRIX DECISION REQUIRED · D-55**
>
> **What is retained, where, for how long, and who is responsible?**
>
> **This document does not establish a retention policy.** What follows is a gap analysis and a
> proposal, so the decision has something concrete to react to.

## 25.2 What exists, and what is at risk

| Artefact | Where it is | At risk from |
|---|---|---|
| **Raw mission folder** — `.mxdb`, `POS_1/raw`, imagery, scanner data, `Extcal.json` | The offload location (§10) | Disk reuse; storage cost pressure |
| **Base station data** | `Base/` in the mission folder | Same |
| **SBET and its processing report** | `NAVPROC/Export/`, `NAVPROC/Report/` *(TBC 25943)* | Project deletion |
| **Frame and epoch log** — from **Backup SBET Next to MXDB** | Beside the `.mxdb` *(TBC 25943)* | **Only exists if the option was enabled** (§12.4) |
| **Numbered registered SBETs** `sbet_<date>_reg_####.out` | Project folder *(TBC 22905)* | **Cleanup — untested, T28** |
| **`Targets.csv`** — the picked registration observations | Project *(TBC 22905)* | Cleanup; a "No" answer to the reload prompt |
| **Calibration JSON** — Installation and Refinement matrices | Exported on demand *(TBC 22920)* | Never created unless someone exports it |
| **Mission Report** — devices, runs, trajectories, scans, **calibration with date** | Run on demand *(TBC 23991_1, 24868)* | **Only exists if run, and only reports what survives Cleanup** |
| **Results of Scan Generation** — filters, range, colorization | A dialog *(TBC 22499)* | Not persisted unless captured |
| **Run-to-run RMS statistics** | Results tab *(TBC 25096)* | Not persisted unless captured |
| **Control / check designation and residuals** | **Nowhere — TBC is not documented as reporting it** (§17.6) | Lost unless recorded manually |
| **Visual QC performed** | **Nowhere** (§24 Layers 6–7) | Lost unless recorded manually |
| **Field record** | **Nowhere — a Parametrix artefact** (§8.9) | Lost unless written |
| **The TBC project itself** | Storage | Size; Cleanup (§21) |
| **The delivered files** | Delivery location | — |

> **Four of those artefacts have no software home at all.** The control/check designation, the
> residuals on each, the visual QC record, and the field record exist only if a person writes them
> down.

## 25.3 A proposed retention framework

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted. Offered for D-55.*
>
> ### Tier 1 — retain for the life of the record
>
> Small, irreplaceable, and the basis of any later defence.
>
> | Artefact | Size |
> |---|---|
> | Field record | kB |
> | Control / check designation table with residuals | kB |
> | Mission Report, run **before** Cleanup | kB |
> | Calibration JSON in force at processing | kB |
> | Results of Scan Generation | kB |
> | Delivery record — §23.6 | kB |
> | Final QA/QC record — §24.4 | kB |
> | The accuracy statement issued to the client | kB |
>
> **The whole of Tier 1 is a few hundred kilobytes.** There is no storage argument against
> retaining it indefinitely.
>
> ### Tier 2 — retain for a defined period
>
> | Artefact | Size |
> |---|---|
> | SBET, its processing report, and the frame/epoch log | MB |
> | Numbered registered SBETs `sbet_*_reg_####.out` | MB |
> | `Targets.csv` | kB |
> | Base station data | MB |
> | The delivered files | GB |
>
> ### Tier 3 — retain per the decision
>
> | Artefact | Size | Note |
> |---|---|---|
> | Raw mission folder | **Tens to hundreds of GB** | **The only thing that permits reprocessing.** Once gone, the deliverable cannot be improved, only re-collected |
> | TBC project | **Tens to hundreds of GB** | The provenance record (§23) |

> **The Tier 3 decision is the substantive one**, and it is a genuine trade-off. Raw data permits
> reprocessing when a better trajectory solution, a correction to a lever arm, or a client's
> changed requirement makes it worthwhile. It is also the largest single storage cost Parametrix
> will carry from this workflow.

## 25.4 Sequencing — archive before Cleanup

> **CAUTION**
>
> **Cleanup Mobile Mapping Mission is destructive and not undoable** (§21). Several Tier 1 and
> Tier 2 artefacts are produced from the project and **can only report what still exists**.
>
> The Mission Report in particular must be run **before** Cleanup, not after.

The ten-step sequence is in §21.6. It is a proposal, pending D-35.

> **FIELD TESTING REQUIRED · T28 — high priority**
>
> **Does Cleanup delete the `sbet_*_reg_####.out` files from storage, or only remove the
> corresponding project objects?** Distinguish **project object retention** from **underlying file
> retention**; do not assume one implies the other. The answer determines whether those files must
> be copied out beforehand. *(§23.5; Appendix I)*

## 25.5 Imagery and privacy retention

> **PARAMETRIX DECISION REQUIRED · D-32**
>
> **Are unblurred originals retained after a blurred deliverable is issued, and for how long?**
>
> Mobile mapping imagery routinely captures pedestrians, licence plates, private property and
> building interiors visible through windows (§19.6). Retaining the unblurred originals preserves
> the ability to re-derive a deliverable; it also retains the material the blurring existed to
> remove. This has legal and reputational dimensions outside the scope of this SOP and should not
> be settled by default.

## 25.6 The archive record

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> One page per project, in the archive, stating: what was archived, where, when, by whom; the
> retention tier applied; whether Cleanup was run and what was archived first; and where the raw
> mission data is, if retained elsewhere.
>
> **Without it, the archive is a folder somebody has to reverse-engineer.** *(Register item 55)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We worked out what has to be kept, and — more importantly — which of it
> exists only if somebody deliberately creates it.
>
> **Why it matters.** In ordinary survey work the archive is insurance you hope never to open. Here
> it is the primary evidence, because the delivered file does not carry its own processing history.
> If somebody queries a result in three years, the answer comes from the project and from what
> Parametrix wrote down, or it does not come at all.
>
> **What can go wrong.** Four of the most important records have no home in the software. Which
> points were control and which were checks, what the residuals were on each, whether the visual
> check was done and over what extent, and what the conditions were like in the field — TBC does
> not produce any of that. It exists if a person writes it down and it does not exist otherwise.
>
> The second failure is sequencing. Several of the records are produced *from* the project, so
> running the tidy-up command before generating them means they can only report what survived.
>
> **What good looks like.** A few hundred kilobytes per project that you keep forever — the field
> record, the control/check table with residuals, the mission report, the calibration file, the
> delivery note and the QA record. A clear decision about the big stuff: how long the raw mission
> data stays, knowing that once it goes the job can only be re-collected, never re-processed. And
> one page saying what was archived, where, and by whom — so the next person does not have to work
> it out from folder names.

---

# 26. Troubleshooting

Symptom first. Each entry gives the likely cause, what to check, and where the procedure is.

## 26.1 Field — before and during collection

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **System will not power up** | Supply, battery, or hold duration | Supply live; hold the Control Unit button **≥ 15 s**; battery above the Battery Protect threshold | 7.5 |
| **Audible alarm during operation** | **Battery Protect** — power cut in **78–90 s** | Restore charge immediately. Do not continue | 7.5, 8.6 |
| **TMI will not load** | Browser, network, or system not ready | Use **Chrome**; `http://tmi.mx-scan.net`; allow the startup sequence to complete | 7.6 |
| **Navigation will not reach ready** | Poor sky view, insufficient manoeuvres, or a heading problem | Move to genuinely open sky; repeat the dynamic manoeuvres; ask TMI which parameter is holding it | 8.2 |
| **Navigation degrades mid-run** | GNSS obstruction | Note it and continue if brief; if sustained, this is a §20 planning problem, not a driving one | 8.6, 20 |
| **A sensor stops reporting** | Cable, power, or sensor fault | Stop. A run collected with a sensor down is incomplete and may need re-driving | 9.4 |
| **Storage filling faster than expected** | Settings, or a longer corridor than planned | Reassess before the disk fills mid-run — an interrupted run loses the closing sequence | 7.8, 8.7 |
| **Imagery obviously degraded** | Contamination, precipitation, low sun | Clean the optics. Weather is a go/no-go decision, not a driving adjustment | 6.5, 19.3 |
| **Vehicle stationary in direct sun** | Outside the rated envelope below 10 km/h | Move, or shut down. A queue on a hot day is a real risk | 8.5 |

## 26.2 Office — import and trajectory

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Covered distance shorter than expected** | A run is missing, or a transfer was incomplete | Compare against the field record. **Catch this at import** | 11.4 |
| **Fewer runs than the crew logged** | Incomplete transfer | Re-verify the offload before processing | 10.3 |
| **Process Raw Trajectory Data unavailable** | **POSPac MMS 8.6+ with a valid licence not installed** | §4.4. Without it the trajectory must be produced elsewhere | 12.1 |
| **Base station data not recognised** | Ephemeris imported instead of observation, or not imported before running | Import **only** the `.YYo`. **Do not import `.YYn` or `.YYg`** | 12.2 |
| **Antenna model wrong** | Read automatically from the RINEX | **Must read `Trimble 112735`** for the MX60. Verify before computing | 12.3 |
| **SBET named `sbet_<mission>_<frame>.out`** | POSPac did not recognise the datum and epoch; computed in ITRF00 then transformed | A **processing-path indicator**, not a verdict. Direct scrutiny to the CRS and epoch setup | 12.4, 24 L3 |
| **Trajectory Plots greyed out** | No SBET computed yet, or no mission | Plots open once after computation; this command reopens them | 12.5 |
| **Plots vanished after computing** | They open only once | Use **Mobile Mapping ▸ Reports ▸ Trajectory Plots** — do **not** recompute | 12.5 |
| **LiDAR QC tab unavailable** | MATLAB Runtime R2024b not installed | §4.5 | 12.7 |

## 26.3 Office — scans and calibration

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Scans did not appear after generation** | Display setting, or generation not complete | Check beneath the trajectory node in Project Explorer | 13.2 |
| **Scan generation failed or was interrupted** | Various | **Recover Mobile Mapping Scans** *(TBC 28155)* | 13.7 |
| **Expected returns missing — signs, line marking** | A filter removed them | Review the filters applied. **Reflective Panels is the suspect** — T3 | 13.3 |
| **Point cloud not coloured** | Generated with colour off | Colour must be on at generation; it propagates to export | 13.4, 19.5 |
| **MTA configuration guidance appears not to apply** | It does not — **the MX60 has no MTA stage** | Ignore MTA topics; they are MX9/MX90 | 13.1 |
| **Calibration RMS good but data still disagrees** | **Good RMS does not prove success** | Perform the visual check, on **both** run pairs | 14.3, 18.1 |
| **Calibration will not compute** | Run geometry does not meet the pattern | Four runs, two roads crossing near 90° ± 30°, ≥ 20 m each side, façades present | 14.3 |
| **Camera imagery misaligned with the cloud** | Camera boresight | Manual Camera Calibration; colour fringing at edges is the symptom | 14.4, 19.5 |

## 26.4 Office — registration

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Register a Run dimmed** | No generated scan on the run | Generate scans first | 15.3 |
| **Error: all points set As Check** | The adjustment requires at least one control point | TBC enforces this. Reconsider the designation with the Project Surveyor | 17.2 |
| **Pair rejected** | GCP-to-target separation exceeds **30 m** | The wrong feature was picked | 15.6 |
| **Warning: not a 3D point / not in this run's scan** | Pick landed off the scan or with no Z | Pick again | 15.6 |
| **Warning: not the most recent scan** | Pick landed on a **superseded** scan set | Pick again. Consider whether superseded sets should still be in the project | 15.6, 21 |
| **Picked targets lost on reopening** | Registration Auto-Saving, and the reload prompt | Answering "No" **empties `Targets.csv` permanently** | 15.3 |
| **Residuals improve each time you register** | **Adjustments are stacking** | Use **Edit**, which starts from the imported trajectory and supports **Reset** | 15.8 |
| **Ends of the corridor still misaligned** | **Local does not extrapolate** | Control must bracket the extent | 15.5, 5.6 |
| **Run-to-run Results mostly `No overlap`** | Insufficient overlap between the pair | The adjustment is based on a small fraction of the run | 16.6 |
| **Run-to-run made absolute accuracy worse** | The reference run carried absolute error, and it propagated | Choose the reference deliberately; re-check against control afterwards | 16.2 |

## 26.5 Office — QC, export and delivery

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Surfaces look thick rather than doubled** | **Rendering is not set to Scan Color** | One colour per scan, or two offset surfaces read as one thick one | 18.5, 24 L6 |
| **Everything passes but the client finds an error** | **Spot-checking** — error arrives in stretches, not speckles | Traverse the corridor rather than sampling it | 18.5, 24 L7 |
| **Exported cloud does not reflect the registration** | **Update Scans was not run** | Confirm scans sit under the registered trajectory and stations carry `_reg_####` | 22.2, 13.6 |
| **Exported data differs from what was QC'd** | **Export timestamps = Yes reprocesses from raw** | Unresolved — **T18 / vendor**. Record the setting used | 22.3 |
| **Scale factor unknown in a delivered file** | Ground scaling does not expose it | Export to grid to obtain the `.txt` sidecar, or use ECEF | 22.5 |
| **Re-imported cloud is wrongly scaled** | **Double-scaling** on re-import of a grid-scaled export | Trimble's own warning | 22.5 |
| **Some delivered images are black** | **Corrupted side camera images export as black** — silently | Screen by file size, then open the flagged ones | 19.4 |
| **Nothing exported to TopoDot** | Scans not generated, or run views open | Generate first; close all run views | 22.6.3 |
| **Cannot determine which trajectory produced a delivered cloud** | **The documented provenance limitation** | §23. Reconstruct from retained SBETs if they exist; record it next time | 23 |

## 26.6 When the answer is "this segment is not suitable for mobile mapping"

> **IMPORTANT · a legitimate outcome, not a failure**
>
> Where GNSS degradation is severe, no remedy is available, and the accuracy requirement cannot be
> met, **the correct professional answer may be that mobile mapping is not the appropriate
> acquisition method for that segment** (§6.8, §20.7).
>
> Conventional survey, static scanning or total station work may produce a more defensible result.
> Saying so — early, in writing, to the client — is better practice than delivering a weak segment
> mixed in with a good corridor.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We put the common failures in one place, organised by what you actually
> see rather than by what causes it.
>
> **Why it matters.** Most of these have a cheap fix if caught at the right moment and an expensive
> one if caught later. A missing run found at import is a transfer problem; found at delivery it is
> a mobilisation.
>
> **What can go wrong.** The entries worth memorising are the silent ones — they do not produce an
> error and you only find them by looking: exporting before Update Scans, surfaces that look thick
> because the rendering is wrong, black images in a delivery that counted correctly, and residuals
> that improve every time you re-register because the adjustments are stacking.
>
> **What good looks like.** Most of this table never gets used, because the checks in §9, §18 and
> §24 catch things while they are still cheap. When you do need it, you look up the symptom, not
> the cause.

---

# 27. Terminology

Terms as used in this document and in Trimble's software. Where TBC uses a word differently from
ordinary survey usage, that is noted.

## 27.1 The trajectory and navigation

| Term | Meaning |
|---|---|
| **Trajectory** | The computed position and attitude of the sensor head over time. Everything the system collects is referenced to it (§2.1) |
| **SBET** | **Smoothed Best Estimate of Trajectory** — the post-processed trajectory, computed forward and backward through time and merged. The normal input for survey work |
| **NAV** | The real-time trajectory computed in the vehicle. A fallback, not an option (§11.2) |
| **POSPac MMS** | Applanix software that computes the SBET. **A licence is required** for both the external route and TBC's in-application command (§4.4) |
| **IN-Fusion+ Single Base** | POSPac computation mode using corrections from a local base station |
| **IN-Fusion+ PP-RTX** | POSPac computation mode using Trimble RTX corrections, with no local base |
| **GNSS/INS integration** | Combining satellite positioning with inertial sensing so each covers the other's failure mode (§2.2) |
| **IMU** | Inertial Measurement Unit. Precise instant to instant, **drifts without limit** over time |
| **GAMS** | GNSS Azimuth Measurement System — a second antenna giving a direct heading measurement. Speeds initialization *(TBC 25943)* |
| **DMI** | Distance Measuring Indicator — a wheel sensor giving independent along-track distance. Scale factor sign depends on the mounting side *(TBC 25943)* |
| **Initialization** | The static period, straight run and dynamic manoeuvres that let the filter resolve attitude and sensor bias (§8.2) |
| **`smrmsg_xxx.out`** | POSPac file describing position, orientation and velocity RMS after smoothing. **The source of the trajectory's RMS colouring** *(TBC 27248)* |
| **ITRF00 path** | Where POSPac does not recognise the project datum and epoch, the SBET is computed in ITRF00 and then transformed — indicated by the filename `sbet_[mission]_[frame].out` *(TBC 25943; §5.3)* |

## 27.2 Missions, runs and data objects

| Term | Meaning |
|---|---|
| **Mission** | One deployment. The `.mxdb` and everything beneath it |
| **Run** | One continuous stretch of collection within a mission. A mission has many |
| **Station** | One instant of imagery capture along a run |
| **`.mxdb`** | The mission database written in the field. **The file you import** |
| **TMX** | Polar scan data — ranges and angles, sensor-relative. Not georeferenced |
| **RWCX** | The point cloud — XYZ, intensity, colour, normals. Produced by applying the trajectory to TMX |
| **MTA** | Multiple Times Around — range-ambiguity correction. **Not part of the MX60 workflow** *(TBC 22503; §13.1)* |
| **`Extcal.json`** | The calibration file written with the raw mission data |
| **Capture Devices** | The TBC node listing the sensors: for the MX60, **Camera 3 Back Down**, **Camera 4 360°**, and the two lasers |

## 27.3 Processing commands

| Term | Meaning |
|---|---|
| **Process Raw Trajectory Data** | Computes an SBET inside TBC. **Requires POSPac 8.6+ and a licence** *(TBC 25943)* |
| **Generate Scans** | Applies the trajectory to raw scanner data, producing the point cloud (§13) |
| **Update Scans** | **Recomputes scans against a different trajectory.** How a registration reaches the point cloud. No Filters pane *(TBC 22638; §13.6)* |
| **Recover Mobile Mapping Scans** | Recovery for failed or interrupted scan generation *(TBC 28155)* |
| **LiDAR QC** | Uses scan data as an aiding sensor, SLAM-like, to refine the trajectory. Runs inside trajectory processing *(TBC 28972; §12.7)* |
| **PFIX** · **Generate POSPac Position Fixes** | Projects GCP-to-target offsets back into the navigation solution for a **second POSPac pass** *(TBC 24460; §20.5)* |
| **Cleanup Mobile Mapping Mission** | Keeps the most recent registration and removes the rest. **Destructive and not undoable** *(TBC 26466; §21)* |

## 27.4 Calibration

| Term | Meaning |
|---|---|
| **Boresight** | The fixed **angular** offset between a sensor and the inertial reference frame. **This is what a calibration estimates** |
| **Lever arm** | The fixed **distance** offset between two sensors. **Known from manufacture and measurement — not estimated** *(TBC 24886; §14.2)* |
| **Installation Matrix** | Parameters **before** calibration — the as-built values *(TBC 22920)* |
| **Refinement Matrix** | Parameters **after** calibration *(TBC 22920)* |
| **Boresight installation / Boresight refinement** | The same distinction as it appears in TBC's sensor properties *(TBC 24868)* |
| **Vehicle frame** | **+X forward, +Y right, +Z downward.** Governs lever arms and boresight angles *(TBC 25943; §7.3)* |

## 27.5 Registration

| Term | Meaning |
|---|---|
| **Registration** | Adjusting a **trajectory** to fit surveyed control, or to fit another run. **It does not move points** (§15.1) |
| **Register a Run** | GCPs matched to picked targets, one run *(TBC 22905)* |
| **Register a Mission** | The same, across a set of runs, with each GCP reusable *(TBC 26473)* |
| **Register Run to Run** | **Cloud-to-cloud** against a fixed Reference Run. **Uses no surveyed control** *(TBC 25096; §16)* |
| **Reference Run** | In run-to-run, the run whose trajectory does not change |
| **Run to Adjust** | The run optimised to the Reference Run |
| **GCP** | Ground control point — "an accurately surveyed coordinate location for a physical feature that can be identified on the ground" *(TBC 22905)* |
| **Target** | **In TBC's registration sense: a point picked in the point cloud.** Not a physical panel (§15.2) |
| **Validation point (VP)** | A GCP set **As Check** — paired and measured, but **excluded from the adjustment** *(TBC 22905; §17.2)* |
| **Use XY · Use Z · As Check** | The three independent per-point choices in the Control Points list (§17.2) |
| **Global** | A shift of the whole trajectory, without rotation *(TBC 22905)* |
| **Local** | Local adjustment interpolating **between** control points. **Does not extrapolate beyond them** *(TBC 22905; §15.5)* |
| **Global, and then Local** | Global first, then Local. No separate selection guidance published |
| **Target-Bundle Adjustment** | Checked = **250 m** intervals (coarser); unchecked = **70 m** *(TBC 22905; §15.7)* |
| **Point Cloud Smart Picking** | The picking tool. Types: Default, Intersected Plane, Road Mark *(TBC 22905)* |
| **`Targets.csv`** | Where picked targets are saved when Registration Auto-Saving is on. **Emptied permanently by answering "No" to the reload prompt** *(TBC 22905)* |
| **`sbet_<date>_reg_####.out`** | The registered SBET on disk, incrementing per registration *(TBC 22905)* |
| **`_reg_####` suffix** | Carried by scan stations updated against a registered trajectory *(TBC 22638)* |
| **Reg. Trajectory · RegTrajectory** | The adjusted trajectory node, from Register a Run and Register a Mission respectively |

## 27.6 Quality

| Term | Meaning |
|---|---|
| **Tangential / Orthogonal / Vertical** | TBC's three-axis agreement convention: along travel, across travel, and up. Diagnostic, not just descriptive (§18.3) |
| **Overall Overlap** | Percentage of points used against those generated, in calibration *(TBC 24886)* |
| **The RMS asymmetry** | **Good RMS does not prove success; bad RMS proves failure; a visual check is necessary** *(TBC 24886, 25096)* |
| **Cutting Plane View** | Profile view across a plane, used to check agreement between overlapping data. **Set rendering to Scan Color** or two offset surfaces read as one thick one (§18.5) |
| **Scan Color** | Rendering mode giving one colour per scan. **Part of the QC method, not a display preference** |
| **`No overlap`** | In run-to-run Results, a timestamp where the two runs do not overlap. Informative, not noise (§16.6) |
| **Undefined RMS colour** | How registered trajectory segments render, having lost their match to the `smrmsg` file *(TBC 27248)* |
| **Mission Report** | Capture devices, runs, trajectories, generated scans, and **per-sensor calibration with date** *(TBC 23991_1, 24868)* |

## 27.7 Export and delivery

| Term | Meaning |
|---|---|
| **Mobile Mapping tab** | Export pane tab holding the **run-aware** exporters |
| **Point Cloud tab** | Export pane tab holding the generic exporters. **Selects by region or drawn rectangle — not by run** *(TBC 11769; §22.4)* |
| **Export to LAS (Trajectory Split)** | The classified-regions exporter. Splits by distance; **carries no trajectory** *(TBC 27279)* |
| **Scaling: Grid** | Projected coordinates with the combined scale factor. **Writes a `.txt` sidecar naming the CRS and scale factor** *(TBC 11769)* |
| **Scaling: Ground** | Ground coordinates. **Does not expose the scale factor used** *(TBC 11769)* |
| **ECEF export** | Ground-scaled LAS/LAZ including the project's global CRS *(TBC 11769)* |
| **Export timestamps** | **Not merely an attribute toggle.** Set to Yes, "the exported scans are reprocessed from the raw data" *(TBC 23339, 22501; §22.3)* |
| **Publish to TRCPS** | Upload to Trimble Connect. **Point cloud and trajectories are exported by default** *(TBC 29527)* |
| **TRCPS** | Trimble Reality Capture Platform Service — an extension of Trimble Connect |
| **TDU** | Trimble Desktop Utility, installed with TBC, which performs the upload |

## 27.8 Evidence tags used in this document

| Tag | Meaning |
|---|---|
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble states this, in the cited topic or page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software; not stated by Trimble as procedure |
| **PARAMETRIX PROCEDURE (PROPOSED)** | Recommended by this document. **Not company policy** |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Decided by Parametrix, with a date and owner in Appendix H |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make |
| **FIELD TESTING REQUIRED** | Answerable by testing, not reading |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble |
| **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** | Carried from the v1 draft; not yet re-sourced |
| **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED** | A screening method proposed here and not yet validated |

---

# Appendix A — Working Checklists

Thirteen standalone checklists, written to be used at the bench or in the vehicle rather than read
as summaries. Each names its section for the detail.

> **Items marked ⚠ depend on an open Parametrix decision** (Appendix I). Perform them using
> project-specific direction until the decision is made.

---

## A1 · Project Planning

*§5, §6*

| ☐ | Item |
|---|---|
| ☐ | Client accuracy requirement stated **in writing, per component** |
| ☐ | Deliverable formats agreed ⚠ *D-38* |
| ☐ | **Grid or ground** agreed, and what accompanies it ⚠ *D-40* |
| ☐ | Project CRS, vertical datum and geoid fixed |
| ☐ | **Epoch** confirmed where a time-dependent datum is in use ⚠ *D-21* |
| ☐ | Corridor extent defined, including extent beyond the deliverable needed to bracket control |
| ☐ | Pass pattern and directions decided ⚠ *D-41* |
| ☐ | **Overlap planned** where a degraded-GNSS remedy may be needed — §20.3 |
| ☐ | Control network designed, **bracketing both ends** of the delivered extent — §5.6 |
| ☐ | Control points chosen for **findability in a point cloud**, not just occupiability — §5.5 |
| ☐ | **Independent check points designated in writing by the Project Surveyor** — §17.4 ⚠ *D-15* |
| ☐ | Check points distributed across GNSS environments, including near each end |
| ☐ | Base station strategy fixed ⚠ *D-42* |
| ☐ | GNSS almanac checked for the planned window |
| ☐ | **GNSS-hostile stretches mapped, with outage duration estimated** — not length |
| ☐ | Mitigation chosen for each hostile stretch — control, overlap, or another method |
| ☐ | **Segments unsuitable for mobile mapping identified and communicated** — §6.8 |
| ☐ | Initialization locations identified — primary and backup, scouted on imagery |
| ☐ | Collection window agreed against GNSS, imagery and traffic |
| ☐ | Weather go/no-go understood by the operator ⚠ *D-44* |
| ☐ | **Calibration currency confirmed** — §14.7 ⚠ *D-26* |
| ☐ | Road occupancy, permits, access and notifications arranged |

---

## A2 · Field Preflight

*§7 · every mission*

| ☐ | Item |
|---|---|
| ☐ | Sensor Unit mounted and secured — **two people**, 24–28 kg |
| ☐ | Unit seated as it was when lever arms were measured |
| ☐ | All cables connected, routed, secured, and not able to be shut in a door |
| ☐ | Power supply live — **30 A or more**; 35 A fuse close to the battery |
| ☐ | Battery healthy; **no Battery Protect warning** (audible below 10.5 V) |
| ☐ | Control Unit powered up — hold **≥ 15 s**; LEDs through the startup sequence |
| ☐ | TMI reachable in **Chrome** at `http://tmi.mx-scan.net` |
| ☐ | **All sensors reporting present** — two lasers, 360° camera, back-down camera |
| ☐ | **Vehicle Preset / lever arms correct for this vehicle and this installation** ⚠ *D-46* |
| ☐ | **Z sign checked** — positive is **downward** |
| ☐ | DMI mounting side recorded, if fitted — determines the scale factor sign |
| ☐ | Capture settings configured **and written down** |
| ☐ | Dust filter set appropriately — unpaved or mine sites only |
| ☐ | Data disk installed, correct disk, **sufficient free space with margin** ⚠ *D-47* |
| ☐ | Scanner windows and camera dome clean |
| ☐ | Initialization location confirmed available |
| ☐ | Weather within the go/no-go rule |
| ☐ | **Field record started** |

---

## A3 · End-of-Mission Field QC

*§8.7, §9 · before the vehicle leaves*

**Closing sequence**

| ☐ | Item |
|---|---|
| ☐ | Last run finished |
| ☐ | Driven to an **open-sky** location |
| ☐ | **Dynamic manoeuvres performed** — the mirror of initialization |
| ☐ | **Stationary 2–3 minutes**, logging static data |
| ☐ | Mission closed in TMI |
| ☐ | **Power button light out** — up to 90 s — before power or disk is disturbed |

**Verification**

| ☐ | Item |
|---|---|
| ☐ | Mission folder present on the disk, plausible size |
| ☐ | **Run count matches what was driven** |
| ☐ | **`POS_1/raw` present and non-empty** — without it there is no post-processed trajectory |
| ☐ | Base station data captured, if a local base was used |
| ☐ | **Every planned pass driven, in the planned direction** |
| ☐ | **Planned overlap actually collected** — §9.3 |
| ☐ | Sections not collected recorded, with the reason |
| ☐ | Field record complete — conditions, incidents, occlusions, comments |
| ☐ | **Any re-drive decided and performed now** ⚠ *D-51* |

> **The overlap check is the one worth being pedantic about.** Missed overlap removes two of the
> three office remedies for degraded GNSS, with no software warning.

---

## A4 · Office Intake

*§10, §11*

| ☐ | Item |
|---|---|
| ☐ | **Copy, do not move** — source disk remains the source |
| ☐ | Copy verified — file count, total size, checksum where tooling allows |
| ☐ | **Verified copy exists in two locations** |
| ☐ | **`.mxdb` confirmed to open** — import into a scratch project. The only definitive test |
| ☐ | `POS_1/raw` present and non-empty |
| ☐ | Base station data present if a local base was used |
| ☐ | **Raw-data backup taken before any processing begins** |
| ☐ | Field record filed with the data |
| ☐ | **Only then** may the source disk be cleared |
| ☐ | Project CRS set **before import** — §11.2 |
| ☐ | **Covered distance checked against the field record** — §11.4 |
| ☐ | Run count matches the field record |
| ☐ | Active trajectory is the intended one, and is **SBET not NAV** unless recorded otherwise |
| ☐ | Capture Devices lists the expected sensors |

---

## A5 · Trajectory Processing

*§12*

| ☐ | Item |
|---|---|
| ☐ | **Base station `.YYo` imported into TBC first** |
| ☐ | **`.YYn` and `.YYg` ephemeris NOT imported** |
| ☐ | Raw POS files located — `POS_1/raw`, processed from the first selected |
| ☐ | **Antenna model reads `Trimble 112735`** — verify before computing |
| ☐ | Computation mode set ⚠ *D-19* |
| ☐ | Initialization mode reviewed — default Gyro-compassing |
| ☐ | Multipath reviewed — default Medium ⚠ *T11* |
| ☐ | GAMS settings reviewed, if fitted |
| ☐ | DMI lever arm, **scale factor and sign**, and SD reviewed, if fitted ⚠ *T12* |
| ☐ | Vehicle-frame convention confirmed — **+X forward, +Y right, +Z down** |
| ☐ | **Backup SBET Next to MXDB enabled** ⚠ *D-20* |
| ☐ | LiDAR QC considered where GNSS was degraded and overlap exists — §12.7 |
| ☐ | Generate QC Report enabled |
| ☐ | **SBET filename read** — `sbet_<mission>.out` or `sbet_<mission>_<frame>.out` |
| ☐ | If `_<frame>`: CRS and epoch setup reviewed. **The filename is an indicator, not a verdict** |
| ☐ | **Trajectory switched to RMS colouring and inspected in plan** |
| ☐ | **Degraded stretches listed** — this list drives QC layers 5, 6 and 7 |
| ☐ | Trajectory Plots reviewed |

---

## A6 · Generate Scans

*§13*

| ☐ | Item |
|---|---|
| ☐ | Correct trajectory active on the mission |
| ☐ | Filter settings chosen deliberately, not accepted ⚠ *T1–T5* |
| ☐ | **Reflective Panels considered** if signs or line marking are in the deliverable ⚠ *T3* |
| ☐ | Range max considered against useful range in the day's conditions ⚠ *T4* |
| ☐ | Colorization decision made ⚠ *D-22* |
| ☐ | **One representative run generated and inspected before committing the mission** |
| ☐ | Expected features still present — signs, line marking, a wall at range |
| ☐ | Mission generated |
| ☐ | **Results of Scan Generation captured into the project record** ⚠ *D-23* |
| ☐ | Scans visible beneath the expected trajectory node |

---

## A7 · Calibration

*§14 · periodic, not per project*

| ☐ | Item |
|---|---|
| ☐ | Calibration currency checked — is one actually due? ⚠ *D-26* |
| ☐ | Calibration site available ⚠ *D-24* |
| ☐ | **Four runs collected** — two roads crossing, each driven both ways |
| ☐ | Crossing angle **90° ± 30°** |
| ☐ | Run length **≥ 20 m each side; ideally 80 m total** |
| ☐ | **Façades present in each direction**; little or no vegetation |
| ☐ | Project created, CRS set, `.mxdb` imported with SBET applied |
| ☐ | **Scans generated** — the calibration consumes them |
| ☐ | Calibrate Laser Scanners run |
| ☐ | Overall Overlap, Overall RMS and per-pair three-axis RMS reviewed |
| ☐ | **Visual check performed in Cutting Plane View, rendering set to Scan Color** |
| ☐ | **BOTH run pairs checked** — `Run_0 ↔ Run_1` **and** `Run_2 ↔ Run_3` |
| ☐ | Applied only after both visual checks |
| ☐ | Camera calibration performed if required — §14.4 |
| ☐ | **Calibration JSON exported and archived** with serial number and date ⚠ *D-25* |
| ☐ | Mission Report run — it carries the **date of calibration** per sensor |

> **Good RMS does not prove the calibration succeeded. Bad RMS proves it failed. Look at the
> data.**

---

## A8 · Registration

*§15, §16, §17*

**Before**

| ☐ | Item |
|---|---|
| ☐ | Scans generated on every run to be registered |
| ☐ | GCP file imported in the project CRS |
| ☐ | **Control / check designation received in writing from the Project Surveyor** ⚠ *D-15* |
| ☐ | **Registration Auto-Saving state confirmed** ⚠ *T7* |
| ☐ | Command chosen deliberately — Run, Mission, or Run-to-Run. **They are not interchangeable** |

**During**

| ☐ | Item |
|---|---|
| ☐ | Registration Name set — **this is what you will identify months later** |
| ☐ | Registration Type chosen ⚠ *T15* |
| ☐ | If **Local**: control **brackets** the delivered extent — it does not extrapolate |
| ☐ | Target-Bundle Adjustment state chosen knowingly — **checked = coarser (250 m)** ⚠ *T9* |
| ☐ | **Use XY / Use Z / As Check set per the written designation** |
| ☐ | Each target picked with the residual read **before** validating |
| ☐ | Pick warnings resolved — not a 3D point; not the most recent scan |
| ☐ | No pair exceeding **30 m** separation |
| ☐ | Redundancy sufficient that removing any one pair would not change the answer much |
| ☐ | Computed; adjusted trajectory (blue) compared against original (green) |
| ☐ | **To improve: use Edit, not Register again** — avoids stacking adjustments |
| ☐ | Applied |

**After**

| ☐ | Item |
|---|---|
| ☐ | Adjusted trajectory node present, with `Origin: Registration result` |
| ☐ | Numbered `sbet_<date>_reg_####.out` present in the project folder |
| ☐ | **Residuals on control and on independent checks recorded outside TBC** ⚠ *D-17* |
| ☐ | **Update Scans run** — §13.6 |
| ☐ | Scan stations carry the **`_reg_####`** suffix |
| ☐ | `Targets.csv` archived |

---

## A9 · Point Cloud QC

*§18*

| ☐ | Item |
|---|---|
| ☐ | Residuals on control reviewed, by component |
| ☐ | **Residuals on independent check points reviewed** — the only numerical evidence of accuracy |
| ☐ | Run-to-run three-axis RMS reviewed where used; **`No overlap` rows read** |
| ☐ | One axis much larger than the other two investigated — it names the problem |
| ☐ | **Rendering set to Scan Color before looking for misalignment** |
| ☐ | Point size increased; cutting plane thickness set ⚠ *T16* |
| ☐ | **Cutting plane dragged the full length of every overlap** — not sampled |
| ☐ | Flat surfaces checked at range for thickening |
| ☐ | **Ends of the corridor checked** — where Local stops and the smoother was weakest |
| ☐ | Degraded stretches from A5 revisited — did the registration fix them? |
| ☐ | Features near control compared with features far from control |
| ☐ | **Visual QC recorded — who, when, what extent.** No software artefact exists |

> **Two surfaces 4 cm apart look exactly like one surface 4 cm thick in a single colour.**

---

## A10 · Imagery QC

*§19*

| ☐ | Item |
|---|---|
| ☐ | Coverage continuous for the full corridor |
| ☐ | Exposure holds through shaded stretches and underpasses |
| ☐ | No motion blur at the speed collected |
| ☐ | No obstruction — aerials, following vehicles, dome contamination |
| ☐ | **Systematic sample opened and looked at**, not counted |
| ☐ | **Black images screened** — corrupted side camera images export as black, silently ⚠ *D-31* |
| ☐ | Colour fringing at feature edges checked on colorized clouds — indicates camera boresight |
| ☐ | Exposure consistency between passes |
| ☐ | Blur applied where required ⚠ *D-32* |
| ☐ | Resolution matches the configuration commitment — §19.2 ⚠ *D-2* |

---

## A11 · Export

*§22*

| ☐ | Item |
|---|---|
| ☐ | **Scan nodes selected sit beneath the intended registered trajectory** |
| ☐ | **Stations carry the `_reg_####` suffix** |
| ☐ | Trajectory properties read `Origin: Registration result`, with expected input and type |
| ☐ | Correct export tab chosen — **Mobile Mapping (run-aware)** or **Point Cloud (region-based)** |
| ☐ | Export path chosen ⚠ *D-38* |
| ☐ | **Export timestamps setting decided and recorded** ⚠ *D-37 · T18 · V-1* |
| ☐ | Scaling decided — **grid writes a `.txt` sidecar; ground does not expose its scale factor** |
| ☐ | ECEF considered where the global CRS must travel |
| ☐ | Path-specific prerequisites met — scans generated; run views closed for TopoDot |
| ☐ | Blur applied where required |
| ☐ | **Delivery record written** — mission, trajectory node, SBET filename and `_reg_` number, registration type, export path, date, by whom ⚠ *D-29* |

> **Registration does not modify the point cloud until Update Scans is performed.** An export can
> succeed, open correctly, and contain pre-registration data.

---

## A12 · Final QA/QC

*§24 · the ten layers*

| ☐ | Layer |
|---|---|
| ☐ | **1 Mission completeness** — covered distance, run count, coverage in plan vs the field record |
| ☐ | **2 Trajectory quality** — RMS colouring reviewed; **suspect stretches listed, not averaged** |
| ☐ | **3 Coordinate system** — CRS, vertical datum, geoid, epoch; SBET filename read as an indicator |
| ☐ | **4 Control usage** — Use XY / Use Z / As Check confirmed against the written designation; checks did not drive the adjustment |
| ☐ | **5 Registration results** — residuals on control and checks; run-to-run RMS; registration type suited the error; Local bracketed the extent |
| ☐ | **6 Visual QC** — Scan Color, cutting plane, overlaps, range, corridor ends |
| ☐ | **7 Corridor continuity** — traversed, not sampled ⚠ *D-39* |
| ☐ | **8 Imagery QC** — A10 |
| ☐ | **9 Export state** — scans under the registered trajectory; `_reg_` suffix; settings recorded ⚠ *T29* |
| ☐ | **10 Deliverable review** — files exist, extents present, CRS and units correct, each file opens in other software, point count and size plausible, imagery present and sampled, sidecars present, no corrupt output, project requirements met |
| ☐ | **Acceptance against the project accuracy requirement** ⚠ *D-13* |
| ☐ | **QA/QC record written** — who performed each layer, and when |

> **Bad RMS can demonstrate failure. Good RMS does not by itself demonstrate success.**

---

## A13 · Archive and Cleanup

*§21, §25*

**Archive first — in this order**

| ☐ | Item |
|---|---|
| ☐ | QC complete and **accepted** |
| ☐ | **Mission Report run and archived** — it can only report what still exists |
| ☐ | Control / check designation and residuals recorded |
| ☐ | `Targets.csv` archived |
| ☐ | **Numbered `sbet_*_reg_####.out` files archived** ⚠ *T28 — assume Cleanup removes them* |
| ☐ | Calibration JSON archived |
| ☐ | Results of Scan Generation archived |
| ☐ | Delivery record and QA/QC record filed |
| ☐ | **Project backup taken to a location that is part of the project archive** — not a local copy |

**Cleanup**

| ☐ | Item |
|---|---|
| ☐ | **Authorisation obtained** ⚠ *D-6 · D-35* |
| ☐ | Cleanup Mobile Mapping Mission run |
| ☐ | **Recorded** — by whom, on what date, and what was archived first |

**Close out**

| ☐ | Item |
|---|---|
| ☐ | Retention tier applied ⚠ *D-55* |
| ☐ | Raw mission data disposition recorded |
| ☐ | Archive record page completed — what, where, when, by whom |

> **Cleanup is destructive and cannot be undone.** Trimble recommends a project backup and nothing
> else; no vendor-prescribed preservation step exists.

---

# Appendix B — TMI Status and Warning Reference

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> This appendix is carried forward from the v1 draft and is sourced to the **TMI Software User
> Guide Rev L** and the **MX60 Quick Start Guide Rev B**. **The TMI version installed on the
> Parametrix system has not been confirmed** *(V-2)*, and TMI's interface has changed between
> versions. Verify against the system before issue.

## B1 · Reaching TMI

| | |
|---|---|
| Browser | **Chrome** |
| Capture interface | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |
| Modules | TMI.Capture · TMI.AI |

*(TMI UG Rev L)*

TMI is served by the Control Unit. It requires no internet access, and the addresses resolve only
on the Control Unit's network.

## B2 · Status colours

Learn these before driving. The operator's only view of system health is this interface.

| Colour | Meaning |
|---|---|
| **Green** | The parameter meets its accuracy threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Red** | Not meeting threshold |

> **CAUTION**
>
> **Orange permits recording. Survey-grade work does not.**
>
> TMI will let a mission be recorded on an orange navigation status. Whether Parametrix work may
> be collected on anything other than green is **D-3 / D-49** — an operator decision rule that has
> not been made. Until it is, treat orange as a stop-and-assess condition and record it.

> **Green means the solution met its accuracy figures — not that it has finished converging**
> (§8.3). Trimble asks for **up to ten more minutes** of settling before recording data that
> matters *(MX60 QSG Rev B)*.

## B3 · The navigation status

What to do when it will not reach its ready state:

| Holding parameter | Likely cause | Action |
|---|---|---|
| **Heading** | Insufficient dynamic manoeuvres, or GAMS unavailable | More turns and speed changes. Heading is the hardest component to resolve (§8.3) |
| **Position** | Poor sky view | Move to a genuinely open location |
| **Attitude** | Insufficient motion variety | Complete the full manoeuvre profile |

> **FIELD TIP**
>
> Ask TMI **which** parameter is holding the solution rather than waiting. Heading means drive
> more; position means move the vehicle. The two remedies are different and waiting helps neither.

## B4 · Alarms and protective behaviour

| Indication | Meaning | Response |
|---|---|---|
| **Audible alarm** | **Battery Protect** — supply below **10.5 V** | Power is cut in **78–90 seconds**. Restore charge immediately; do not continue *(MX60 UG Rev B)* |
| Sensor absent from the device list | Cable, power or sensor fault | Stop. A run with a sensor down is incomplete (§9.4) |
| Storage warning | Disk filling | Reassess before it fills mid-run — an interrupted run loses the closing sequence (§8.7) |

## B5 · Capture settings

> **VENDOR CLARIFICATION REQUIRED · V-2 · unresolved presentation conflict**
>
> | Source | Presentation |
> |---|---|
> | **MX60 Quick Start Guide Rev B, p.10** | Two controls — *Measurement Prog* `[500 kHz, 1000 kHz]` and *Line Speed* `[120 Hz, 200 Hz]` |
> | **TMI User Guide Rev L, p.29** | A single combined **Laser Mode** for the MX60 |
>
> **Which the operator sees depends on the TMI version installed.** Expect either; record which
> was used. *(`CONFLICT-005`)*

Also:

- Trimble states the **measurements-per-second values shown in the interface are rounded**
  *(TMI UG Rev L, pp.28–29)*
- **Lateral Range Limit** is settable **5–50 m** *(TMI UG Rev L, p.29)*. Whether it affects
  accuracy or is purely a data-volume control is **V-7**
- A **dust filter** is available and is intended for **unpaved roads and mine sites**
  *(Product Bulletin, January 2025)*

### Resolved specification conflict, recorded for reference

> The spec sheet quotes **1000 / 2000 kHz** and **240 / 400 Hz** where the User Guide quotes
> **500 / 1000 kHz** and **120 / 200 Hz** — a factor of exactly two, being system totals against
> per-scanner figures. **The Quick Start Guide confirms TMI uses the User Guide's per-scanner
> numbering**, so the values the operator selects in TMI are the User Guide values.
> *(`RESOLVED-001` in `reference/mx60-reference-data.csv`)*

## B6 · Calibration import

TMI accepts a boresight calibration JSON via **USB1** *(TMI UG Rev L, p.18)*. Relevant where a
calibration is computed in TBC (§14) and applied to the system rather than to a project.

## B7 · Comments

> **FIELD TIP**
>
> **Use the Comments feature during collection.** A note made at the moment — *"heavy canopy from
> the bridge"*, *"stopped 4 min, traffic control"*, *"parked truck occluding the north side"* — is
> worth an hour of office guesswork three weeks later (§8.6, §9.5).

---

> **The full TMI procedure is §7 and §8.** This appendix is a reference for the indications, not a
> substitute for the procedure.

---

# Appendix C — Trimble Source Index

Every Trimble source cited in this SOP. **`reference/mx60-reference-data.csv` (402 records) is the
authority for numbers**; this document explains what they mean.

## C1 · Manuals and bulletins

| Document | Revision | Cited for |
|---|---|---|
| **Trimble MX60 User Guide** | Rev B, May 2025 (P/N T001983), 68 pp | Hardware, installation, power, safety, specifications, periodic verification |
| **Trimble MX60 Quick Start Guide** | Rev B, March 2025, 16 pp | Field sequence, initialization, capture settings |
| **Trimble Mobile Imaging (TMI) Software User Guide** | **Rev L, April 2026** (P/N T001242), 56 pp | Field software, status, capture settings, calibration import |
| **Trimble MX60 Spec Sheet** | PN 022516-737C (04/25), 4 pp | Specifications |
| **Trimble MX Shock Absorbing Mounting Rack User Guide** | Rev B, May 2025 (P/N 37000001), 10 pp | Vehicle installation |
| **Product Bulletin: Enabling the Dust Filter in TMI for MX60** | January 2025, 3 pp | Dust filter |
| **TBC Technical Notes: For Mobile Mapping** | October 2022, 8 pp | **Predates MX60 support — used with caution** |

## C2 · TBC help portal — **TBC 2026.10**

The captured help documents **TBC 2026.10**, confirmed by cross-reference: a registration feature
listed as new in the 2026.10 release notes is present in the captured topic *(TBC RN 2026.10;
TBC 22905)*. URLs follow `https://help.fieldsystems.trimble.com/tbc/<id>.htm`.

### Understanding and structure

| ID | Topic | Cited in |
|---|---|---|
| 20717 | Understanding Mobile Mapping | 2 |
| 22503 | Mobile Mapping System Data Structure | 2.5, 13.1 |
| 21243-1 | Mobile Mapping Options | 15.3 |
| 22554 | View the Mobile Mapping Data in the Project Explorer | 11.3 |

### Import, view and process

| ID | Topic | Cited in |
|---|---|---|
| 20736-1 | Import the Mobile Mapping Data | 11.3 |
| **22499** | **Generate Mobile Mapping Scans** | 11.4, 13.2–13.5 |
| **22638** | **Update Mobile Mapping Scans** | 13.6, 22.2, 23.3 |
| 22567 | Hide, Display and Center on a Mobile Mapping Trajectory | — |
| 22863 | Go to a Mobile Mapping Station Position | — |
| 20727 | Navigate a long Mobile Mapping Run | — |
| 24024 | Split a Mobile Mapping Run | — |
| 26947 | Define a Region of Interest | — |
| **28155** | **Recover Mobile Mapping Scans** | 13.7, 26.3 |
| 28912 | Display Mobile Mapping Rectified Camera Views | 19 |
| 23856 | Configure your Graphic Card Driver When Using the MTA Correction | **13.1 — does not apply to MX60** |
| **23991_1** | **Run a Mission Report** | 14.6, 17.6, 23.3, 25.2 |

### Register Mobile Mapping Trajectories

| ID | Topic | Cited in |
|---|---|---|
| **22905** | **Register a Run** | 15.2–15.9, 17.2, 22.2, 23.3 |
| **26473** | **Register a Mission** | 15.4, 17.2, 22.2, 23.3 |
| **25096** | **Register Multiple Pairs of Runs** (Register Run to Run) | 16, 18.2–18.3 |
| 25362 | Edit a Run | 15.8, 16.8, 24 L4 |
| 26578 | Edit a Mission | 15.8, 24 L4 |

### Perform Mobile Mapping Calibrations

| ID | Topic | Cited in |
|---|---|---|
| **24886** *(also 20716)* | **Calibrate Mobile Mapping Laser Scanners** | 14.2–14.3, 18.1 |
| 24868 | Calibrate Mobile Mapping Cameras | 14.4, 14.6 |
| 20728 | Perform a Manual Camera Calibration | 14.4 |
| 22920 | Import and Export Mobile Mapping Calibration File (.json) | 14.5 |
| **25943** | **Process Raw Trajectory Data** | 5.3, 10.1, 12.2–12.4, 23.3 |
| **28972** | **LiDAR QC Processing** | 4.5, 12.7, 20.6 |
| 24460 | Generate POSPac Position Fixes | 11.2, 20.5 |
| 27248 | Change the Real-time or Post-processed Trajectory Color Settings | 12.4, 18.4, 22.2 |
| 27415 | View Trajectory Plots | 12.5, 24 L2 |

### Cleanup

| ID | Topic | Cited in |
|---|---|---|
| **26466** | **Cleanup Mobile Mapping Mission** | 21, 23.5, 25.4 |

### Export and publish

| ID | Topic | Cited in |
|---|---|---|
| **11769** | **Export Point Cloud Files** (.e57, .las, .laz, .pod, .pts, .ptx, .rcp, .tdx) | 22.4–22.6.5 |
| **27279** | **Export Mobile Mapping Classified Point Cloud Regions to LAS** | 22.5, 22.6.1 |
| **22501** | **Export to Trimble TMX** | 19.2, 22.3, 22.6.2 |
| **23339** | **Export to TopoDot** | 19.2, 22.3, 22.6.3 |
| **23888** | **Export to Solv3D** | 19.2, 22.6.4 |
| **29527** | **Publish Mobile Mapping Point Cloud Data, Trajectories, and Images to Trimble Connect** | 4.6, 22.6.6 |
| 28963 | Workflow: Publish Point Cloud Data and Panoramic Images to Trimble Connect | **Publish Scan Data — a static-scanner path** |

### MX7-only exporters — **do not apply to the MX60**

| ID | Topic | Why excluded |
|---|---|---|
| 20926 | Station Positions and Panorama Orientations (.xml) | **"MX7 Export to XML Horus"** — converts PGR files from an MX7 360° camera |
| 20927_1 | Panoramic Images and Trajectory Files (.csv) | **"MX7 Export to TMX"** — starts from a Trident `.tridb`; 8000 × 4000 px panorama |
| 21713_1 | Cubical Images and Trajectory Files (.csv) | **"MX7 Export to Mapillary"** — same panorama size |

> **The MX7 panorama is 8000 × 4000 px; the MX60 is 8192 × 4096 (Core) or 12288 × 6144
> (Pro/Premium).** Pixel counts are a reliable way to tell which system a TBC topic describes when
> the title does not say.

### Release notes

| Release | Cited for |
|---|---|
| **2025.21** | Signed GCP residuals "in the report"; Publish to TRCPS; Smart Picking window instability; licence eligibility |
| **2026.10** | Direct residuals to GCP **(the version cross-reference)**; dynamic datum epoch; two-step verification; dark theme; Rectified Camera Views naming |

## C3 · Not held, and needed

| Document | Needed for | Item |
|---|---|---|
| **Trimble GAMS Antenna Kit Installation & Operation Manual** | Lever-arm procedure if GAMS is fitted | V-5 |
| **Trimble DMI Installation & Operation Manual** | DMI scale factor for the measured wheel diameter | V-6 |
| **TBC Help: Blur Exported Images** | Imagery privacy procedure | §19.6 — capture when privacy is drafted |

## C4 · Non-Trimble sources — reference only

> **These are cited as examples of how others have answered questions Parametrix has not. They are
> not Parametrix standards and not Trimble requirements.**

| Source | Used for |
|---|---|
| **Queensland TMR, Mobile Laser Scanning Technical Guideline**, March 2023, CC BY 4.0 | An example of a published agency specification for control layout, accuracy tiers, and wet-weather practice — §5.6, §6.5 |
| **NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data**, 2024 | Background |

## C5 · Unresolved source conflicts

| ID | Conflict | Status |
|---|---|---|
| `CONFLICT-002` | Scanner FOV — 346° *(UG p.54)* vs 360° *(spec sheet p.2)* | **V-15** |
| `CONFLICT-003` | Which mounting rack is fitted | **D-2 / V-4** |
| `CONFLICT-004` | Minor numeric discrepancies between sources | Recorded in the CSV |
| `CONFLICT-005` | Laser control presentation — QSG vs TMI Rev L | **V-2** |
| `RESOLVED-001` | Spec sheet vs User Guide laser rates — **system total vs per-scanner, a factor of 2.** QSG confirms TMI uses the User Guide numbering | **Resolved** |

## C6 · Analysis record

The source ingestion and classification that produced this SOP:

| Document | Content |
|---|---|
| `analysis/STAGE-1-SOURCE-ANALYSIS.md` | Initial manual assessment |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-2.md` | 16 TBC topics classified |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-3.md` | Chain model tested; the registration gap identified |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-4.md` | Registration and calibration branches; six of eight questions answered |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-5.md` | Export provenance pass; release notes |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-6.md` | Four export topics; **version confirmed as TBC 2026.10** |
| `analysis/SOURCE-INVENTORY-TBC-BATCH-7.md` | Export surface closed; ingestion declared sufficient |
| `analysis/GUIDE-REQUIREMENTS.md` | Branding and comprehension-layer requirements |
| `analysis/VENDOR-QUESTIONS.md` | Vendor question record — mirrored in Appendix I Table 3 |

---

# Appendix D — First-Week Training Exercise

A structured introduction for someone new to the MX60. It uses a real site and produces a real,
throwaway dataset — nothing here should be delivered to a client.

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> **Is this exercise a requirement before operating alone, and who signs it off?** The exercise is
> offered as a structure; whether it is a qualification gate is not decided.

## D1 · Before the exercise — reading

| Order | Read | Why |
|---|---|---|
| 1 | **§2** Mobile Mapping in Plain Terms | Everything else depends on it |
| 2 | **§1.5** the evidence tags | So the reader knows what is and is not policy |
| 3 | **All In Plain English boxes, end to end** | A complete picture of the workflow in ordinary language |
| 4 | §4 Equipment and Software | What the system is |

> **The In Plain English boxes read end to end are a document in their own right.** A trainee who
> reads only those has a true, if simplified, picture of the whole workflow — deliberately so.

## D2 · Day one — the system

**Goal:** understand what is on the vehicle and why.

| Task | § |
|---|---|
| Identify every component: Sensor Unit, Control Unit, Power Unit, disk, rack, and GAMS/DMI if fitted | 4.1 |
| Locate the two scanners, the 360° camera, the back-down camera | 4.1 |
| **Understand the vehicle frame: +X forward, +Y right, +Z down.** Point at each axis on the vehicle | 7.3 |
| Find where the lever arms are recorded, and read them | 7.3 |
| Connect to TMI in Chrome; identify every status indication | 7.6, App. B |
| Power the system up and down correctly | 7.5, 8.8 |

**Check of understanding:** *Why is Z negative for a sensor mounted above the reference point?*

## D3 · Day two — a mission, done properly

**Goal:** a complete mission with a full initialization and a full closing sequence.

Choose an easy corridor: open sky, light traffic, 20–30 minutes of driving.

| Task | § |
|---|---|
| Complete the preflight checklist — **A2** | 7.9 |
| Initialize: static 2–3 min, straight run, dynamic manoeuvres | 8.2 |
| **Wait out the settling time** and understand why green is not finished | 8.3 |
| Collect the corridor, recording Comments as things happen | 8.4–8.6 |
| **Perform the full closing sequence** | 8.7 |
| Complete the field QC checklist — **A3** | 9 |
| Offload and verify — **A4** | 10.3 |

**Check of understanding:** *Why does the end of the mission matter as much as the start?*

## D4 · Day three — a mission done badly, deliberately

**Goal:** see the failure modes, safely, on data that does not matter.

> **This is the most valuable day of the week.** Mobile mapping failures are invisible in the
> data. The only way to recognise one is to have seen one.

| Deliberate error | What to observe |
|---|---|
| Initialize under tree cover or beside a building | How long the solution takes, or whether it reaches ready at all |
| Record immediately on green, with no settling | Compare the first minutes against the rest, later, in §12 |
| Drive a stretch under heavy canopy | The RMS colouring in §12.4 |
| **Skip the closing sequence** | The trajectory quality at the end of the mission |
| Drive one stretch once, with no overlap | That LiDAR QC and run-to-run are unavailable there |

Collect a second, correct mission over the same corridor for comparison.

**Check of understanding:** *Looking at both point clouds, can you tell which is which without
being told?* — Usually not. That is the point.

## D5 · Day four — the office chain

**Goal:** take the good mission from raw data to a point cloud.

| Task | § | Checklist |
|---|---|---|
| Set the project CRS **before** import | 11.2 | A4 |
| Import; **check covered distance against the field record** | 11.4 | A4 |
| Process the trajectory; **verify the antenna model reads Trimble 112735** | 12.3 | A5 |
| **Read the SBET filename** and say what it indicates | 12.4 | A5 |
| **Colour the trajectory by RMS and find the degraded stretches** | 12.4 | A5 |
| Compare against the day-three bad mission | 12.4 | — |
| Generate scans on one run; inspect; then the mission | 13 | A6 |
| Find the scans in Project Explorer and say which trajectory they are under | 11.3 | — |

**Check of understanding:** *Show the degraded stretches in plan and explain what caused each.*

## D6 · Day five — registration and QC

**Goal:** register to control, and understand what the numbers do and do not prove.

| Task | § | Checklist |
|---|---|---|
| Import control; identify targets in the cloud | 15.2, 15.6 | A8 |
| **Designate control and check points before starting** | 17.4 | A8 |
| Register the mission; read residuals **before** validating each pick | 15.4, 15.6 | A8 |
| Compute, inspect, apply | 15.3 | A8 |
| **Run Update Scans** and find the `_reg_####` suffix | 13.6 | A8 |
| **Set rendering to Scan Color** and inspect in Cutting Plane View | 18.5 | A9 |
| Drag the cutting plane the **full length** of an overlap | 18.5 | A9 |
| Compare check-point residuals against control-point residuals | 17, 18 | A9 |

**Exercises in judgement:**

1. **Register the same run twice instead of using Edit.** Watch the residuals improve. Explain why
   that is not an improvement.
2. **Turn Scan Color off** and look at a known 4 cm misalignment. Explain what you see.
3. **Export before running Update Scans.** Open the file. Explain what is wrong with it and how
   you would have caught it.

**Check of understanding:** *Trimble says good RMS does not prove success but bad RMS proves
failure. Why is that asymmetry true?*

## D7 · Competence check

A trainee should be able to answer these without the document open:

| # | Question | § |
|---|---|---|
| 1 | What is the trajectory, and why does everything depend on it? | 2.1 |
| 2 | Why does the end of a mission matter as much as the start? | 2.2, 8.7 |
| 3 | Why does bad mobile mapping data look fine? | 2.3 |
| 4 | What does green mean in TMI, and what does it not mean? | 8.3 |
| 5 | Name the three registration commands and what constrains each | 15.1 |
| 6 | What does **As Check** do, and why can't every point be one? | 17.2 |
| 7 | Why does a good RMS not prove the registration worked? | 18.1 |
| 8 | What happens if you export without running Update Scans? | 13.6, 22.2 |
| 9 | Why is Cleanup dangerous, and what should happen first? | 21 |
| 10 | Can you tell which trajectory produced a delivered point cloud? | 23.4 |
| 11 | Name two degraded-GNSS remedies that must be arranged **before** driving | 20.3 |
| 12 | Which parts of this SOP are binding Parametrix policy? | 1.5 — **none yet** |

> Question 12 is not a trick. A trainee who answers "all of it" has misread the document, and a
> trainee who can explain why the answer is "none yet" has understood what it is for.

---

# Appendix G — Figure List and Placeholders

Figures identified during source ingestion, to be cropped from the Trimble help captures held in
`sources/`. **No figure has been cropped or placed yet** — this is the production list.

> **Crops, not whole pages.** A full help-portal screenshot carries Trimble's navigation, header
> and footer, which would make the SOP look like a Trimble document (§1, branding requirement).
> Each entry below names the specific element to crop.

## G1 · Captions and attribution

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Every figure carries: a Parametrix-style caption stating what the reader should see; the source
> citation; and a note that the interface shown is **TBC 2026.10** *(§1.6)*.
>
> Trimble screenshots are preserved as technical evidence and are **not** redrawn or paraphrased
> away. Trimble's page layout, typography and iconography are **not** carried over.

## G2 · The list

### Field and system

| # | Figure | Source | § |
|---|---|---|---|
| F01 | MX60 sensor layout — two scanners, 360° camera, back-down camera | MX60 UG Rev B | 4.1 |
| F02 | Vehicle frame axes — **+X forward, +Y right, +Z down** | TBC 24886 / 25943 | 7.3 |
| F03 | Lever arm vs boresight, on a vehicle | TBC 24886 | 14.2 |
| F04 | TMI status display with colour indications | TMI UG Rev L | App. B |
| F05 | Initialization manoeuvre profile — **speed against time** | *To be drawn — Parametrix original* | 8.2 |

### Trajectory and scans

| # | Figure | Source | § |
|---|---|---|---|
| F06 | Raw mission folder tree — `POS_1/raw`, `Base`, `Camera_*`, `Laser_*`, `Extcal.json`, `.mxdb` | TBC 25943 | 10.1 |
| F07 | Process Raw Trajectory Data settings pane | TBC 25943 | 12.3 |
| F08 | **Trajectory coloured by RMS in Plan View** — the single most useful QC view | TBC 25943 / 27248 | 12.4 |
| F09 | The data chain — TMX → RWCX, one step on MX60 | *To be drawn — Parametrix original* | 2.5, 13.1 |
| F10 | Generate Scans filter pane | TBC 22499 | 13.3 |
| F11 | Results of Scan Generation dialog | TBC 22499 | 13.5 |
| F12 | Project Explorer showing scans nested beneath their trajectory | TBC 22638 | 11.3, 22.2 |

### Calibration

| # | Figure | Source | § |
|---|---|---|---|
| F13 | Calibration site geometry — two roads crossing, four runs, 90° ± 30° | *To be drawn from TBC 24886 values* | 6.7, 14.3 |
| F14 | Calibration results — Overall Overlap, Overall RMS, per-pair three-axis RMS | TBC 24886 | 14.3 |
| F15 | **Mission Report Capture devices table** — boresight installation vs calibration, **date of calibration** | TBC 24868 | 14.6 |
| F16 | Camera properties — Boresight installation vs Boresight refinement | TBC 24868 | 14.4 |

### Registration

| # | Figure | Source | § |
|---|---|---|---|
| F17 | Control Points grid — **Use XY / Use Z / As Check / Target** columns | TBC 22905 | 17.2 |
| F18 | Targets pane with signed E / N / Elev residuals populated | TBC 22905 | 15.6, 17.6 |
| F19 | **Validate Picking** — overhead view, perpendicular side view, RMS of plane | TBC 22905 | 15.6 |
| F20 | Project Explorer — `Unnamed Run 0 › Sbet` / `Reg. Trajectory` | TBC 22905 | 15.3 |
| F21 | **Trajectory properties** — `Origin: Registration result`, Input trajectory, Registration type | TBC 22905 / 26473 | 15.3, 23.3 |
| F22 | Project folder listing `sbet_…_reg_0001…0004.out` | TBC 22905 | 15.3, 23.3 |
| F23 | Mission control list — one GCP, five instances, one per run | TBC 26473 | 15.4 |
| F24 | Project Explorer after mission registration — `RegTrajectory` under each run | TBC 26473 | 15.4 |
| F25 | **Tangential / Orthogonal / Vertical** axes on a curved trajectory | TBC 25096 | 16.6, 18.3 |
| F26 | Run-to-run **Results tab** — RMS statistics with `No overlap` rows | TBC 25096 | 16.6 |
| F27 | **Cutting Plane View** profile across two runs | TBC 25096 | 16.7, 18.5 |
| F28 | Plan View — Run to Adjust green, Reference Run red | TBC 25096 | 16.4 |

### Export and delivery

| # | Figure | Source | § |
|---|---|---|---|
| F29 | **MX60** export folder tree — Camera 3 Back Down, Camera 4 360° with six `.cal` faces | TBC 23339 | 19.2, 22.6.3 |
| F30 | **TMX MX60 tree showing the `trajectory` sub-folder** beside `laser` and `panorama` | TBC 22501 | 22.6.2, 23.3 |
| F31 | Classified LAS Settings pane — splitting distance, per-laser, Format, Export unit | TBC 27279 | 22.6.1 |
| F32 | Solv3D output tree with `reference.csv` | TBC 23888 | 22.6.4 |
| F33 | Export Point Cloud Files Settings — Scaling, ECEF, Split | TBC 11769 | 22.5, 22.6.5 |
| F34 | **Publish to TRCPS** — "point cloud and trajectories will be automatically exported" | TBC 29527 | 22.6.6 |
| F35 | Trimble Connect 3D+ view — colorized cloud with **trajectory and camera markers** | TBC 29527 | 22.6.6 |

### Parametrix originals to be drawn

| # | Figure | § |
|---|---|---|
| F36 | **The workflow at a glance** — field to delivery, one page | 2.6, 4 |
| F37 | **The degraded-GNSS branch diagram** — showing the two backward loops | 20.1 |
| F38 | **The provenance chain** — seven transitions, what survives each | 23.3 |
| F39 | **The ten QA/QC layers** | 24.2 |

## G3 · Source availability

| Batch | Held as files? |
|---|---|
| TBC help batch 2 — 17 topics | ✅ `sources/tbc-help-captures/` |
| TBC help batch 4 — 15 topics | ✅ `sources/tbc-help-captures-batch4/` |
| TBC help batch 7 — 7 topics | ✅ `sources/tbc-help-captures-batch7/` |
| **TBC help batch 6 — 4 export topics** (27279, 22501, 23339, 23888) | ❌ **Arrived inline; not archived** |
| MX60 / TMI / QSG manuals | ✅ repository root |

> **F29–F32 cannot be cropped until the batch 6 pages are supplied as files.** Their content is
> recorded and cited in §22; only the images are missing. This blocks figure production, not
> drafting.

## G4 · Branding

> **PARAMETRIX BRANDING — PLACEHOLDER**
>
> The document is **unstyled**. Branding is applied once, at the end, when content and structure
> are stable *(`analysis/GUIDE-REQUIREMENTS.md` §1)*.
>
> **Held:** `brand/parametrix-wordmark.png`, `brand/parametrix-x-mark.png`; sampled colours
> **charcoal `#343433`** and **red `#EB2A2B`**.
>
> **Still needed:** vector logo (SVG/EPS), a reversed variant for dark backgrounds, and whatever
> template, example and brand-standard material exists.
>
> **Note for capture consistency:** TBC 2026.10 introduced a **dark theme** *(TBC RN 2026.10)*.
> **All screenshots must be captured in one theme** — light, matching every existing capture.
> Mixed light and dark TBC screenshots in a Parametrix manual read as an error.

---

# Appendix H — Decision Adoption Record

**This appendix is empty on first issue, and that is correct.**

## H1 · What this appendix is for

The SOP tags every Parametrix procedure as **PROPOSED** or **ADOPTED** (§1.5). On first issue
**there are no ADOPTED entries** — the technical content is complete and evidenced; the company
decisions on top of it have not been made.

This appendix is where they are recorded as they are made. It is the mechanism by which a
proposal becomes policy.

## H2 · How a decision is adopted

1. The decision is identified in **Appendix I**, with its ID
2. Parametrix decides it
3. **The decision is recorded here** — ID, what was decided, by whom, on what date
4. The relevant SOP section's tag changes from **PARAMETRIX PROCEDURE (PROPOSED)** or
   **PARAMETRIX DECISION REQUIRED** to **PARAMETRIX PROCEDURE (ADOPTED)**, with a cross-reference
   to this appendix
5. The Appendix I row is struck through, with a pointer here

> **A decision that is made but not recorded here has not been adopted.** The tag in the body is
> the reader's only indication of whether something is binding, and it must be traceable to a
> named person and a date.

## H3 · The record

| ID | Decision | What was decided | Decided by | Date | SOP §§ updated |
|---|---|---|---|---|---|
| — | *No decisions adopted* | — | — | — | — |

## H4 · Priority order for the first round

From **Appendix I**, the ten items that genuinely block operation:

| ID | Decision | Why it blocks |
|---|---|---|
| **D-2 / V-4** | MX60 configuration, GAMS, DMI, rack | Imagery and accuracy commitments cannot be made |
| **D-10** | POSPac MMS licence | Determines whether trajectory processing and PFIX exist at all |
| **D-13** | Acceptance criteria | Acceptance cannot be signed |
| **D-16** | Control density and check ratio | Control design cannot be specified |
| **D-19** | Computation mode — Single Base or PP-RTX | Field logistics on every mission |
| **D-21** | Datum and epoch | A silent failure mode with a user-settable control |
| **D-35** | Cleanup policy | Otherwise decided by default by whoever finishes a project first |
| **D-41** | Pass pattern | Two of three degraded-GNSS remedies need overlap collected on the day |
| **D-42** | Base station strategy | Field logistics; interacts with D-19 |

Fourteen further **P1** items should follow. The remaining items improve consistency and
efficiency without preventing defensible work.

## H5 · Review

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> **Who owns this SOP, and on what cycle is it reviewed?**
>
> TBC is on an annual release cycle — 2023.10 through 2026.10 — and **each release has changed
> mobile mapping behaviour**. This SOP documents TBC 2026.10. Without an owner and a cycle, it
> will describe software nobody is running within about eighteen months.

---

# Appendix I — Open Parametrix Decisions, Field Tests, and Vendor Questions

**This appendix is the backlog. It is not a blocker to using this SOP.**

Every unresolved item in the document is collected here so it can be worked through
systematically. The SOP is usable now; these items determine how much of it becomes binding
company procedure and how much remains proposal.

**"Can the SOP operate without it?"** means: can a competent processor follow this document and
produce defensible work while this item is open. **Yes** usually means the item makes the work
less efficient or less consistent, not less correct.

---

## Table 1 — Parametrix Decisions Required

Company policy choices. Only Parametrix can make these.

| ID | Question | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|
| **D-1** | Who owns this SOP, who approves revisions, on what review cycle? | TBC is on an annual release cycle and each release has changed mobile mapping behaviour. A procedure with no owner decays silently | 1.7 | **P2** | Yes |
| **D-2** | Which MX60 configuration is ours — Core, Pro or Premium? Are GAMS and DMI fitted? Which rack? | Panoramic imagery is **8192×4096 on Core, 12288×6144 on Pro/Premium**. Changes every imagery and accuracy statement. Rack determines whether published GAMS offsets apply | 4.1, 19.2 | **P1** | **No** — imagery commitments cannot be made |
| **D-3** | Who may operate the MX60? Qualification, training, supervised runs? | Field acquisition determines what the office can ever do | 3.3 | **P1** | Yes, with risk |
| **D-4** | Who may perform a registration? | Registration is an adjustment | 3.3 | **P1** | Yes, with risk |
| **D-5** | Who accepts a registration — and must it be someone other than the person who performed it? | Independence of the check | 3.3, 17.4 | **P1** | Yes, with risk |
| **D-6** | Who may run Cleanup Mobile Mapping Mission? | Destructive and not undoable | 3.3, 21.4 | **P1** | **No** — see D-35 |
| **D-7** | Who signs the accuracy statement, under what licensure, against what evidence? | — | 3.3 | **P1** | Yes, with risk |
| **D-8** | Who owns calibration currency? | Nobody owns it today | 3.3, 14.7 | **P2** | Yes |
| **D-10** | Do we hold a POSPac MMS 8.6+ licence, and where is it installed? | Determines whether trajectory processing and PFIX are available at all, and removes one of three degraded-GNSS remedies | 4.4, 12.1, 20.3 | **P1** | **No** — shapes the entire office workflow |
| **D-11** | Is LiDAR QC a capability we intend to have? | 128–256 GB RAM, dedicated SSDs, MATLAB Runtime. A procurement question that becomes urgent only when it is too late | 4.5, 12.7 | **P2** | Yes |
| **D-12** | Is Register a Mission the corridor default, with Register a Run the exception? | Production convention; affects consistency across processors | 15.4 | **P3** | Yes |
| **D-13** | **What constitutes an acceptable registration and an acceptable point cloud?** | **No Trimble source provides a threshold.** Must combine numerical residuals, independent checks, visual inspection and the project accuracy requirement | 15.9, 18.9, 24.3 | **P1** | **No** — acceptance cannot be signed |
| **D-14** | Where does run-to-run registration sit in a controlled workflow? | It uses no control and propagates the reference run's absolute error | 16.2 | **P2** | Yes |
| **D-15** | Is the control/check designation fixed before registration and unchangeable during it? | Guards the one failure that looks like diligence | 17.4 | **P1** | Yes, with risk |
| **D-16** | How many control points, at what spacing, and how many independent checks? | No Trimble source states any. TBC's minimum of one pair is a mathematical floor | 5.6, 17.5 | **P1** | **No** — control design cannot be specified |
| **D-17** | Where is the control/check designation and its residuals recorded? | **TBC is not documented as reporting it.** The single most important record in the workflow | 17.6, 23.6 | **P1** | Yes, with risk |
| **D-18** | What is verified at import, and by whom? | Six checks, each cheaper now than later | 11.5 | **P3** | Yes |
| **D-19** | IN-Fusion+ Single Base or PP-RTX? | Determines whether a base station is occupied every mission, and the reference frame | 5.3, 12.3 | **P1** | **No** — field logistics depend on it |
| **D-20** | Is Backup SBET Next to MXDB enabled as standard? | Its log is the only record of the frame and epoch a trajectory was computed in | 12.4, 23.3 | **P2** | Yes |
| **D-21** | Which datum and epoch do we work in, who sets it, who checks it? | Silent failure mode, plus a new user-settable control Trimble flags as risky | 5.4, 12.6 | **P1** | **No** |
| **D-22** | Are scans generated coloured by default? | Discovering later that colour was wanted means regenerating the mission | 13.4 | **P3** | Yes |
| **D-23** | Is the Results of Scan Generation captured into the project record? | The only artefact stating which filters produced a cloud | 13.5, 23.3 | **P3** | Yes |
| **D-24** | Where is the calibration site, and who maintains it? | Establishing one is a morning's work; finding one under schedule pressure is not | 6.7, 14.3 | **P2** | Yes |
| **D-25** | Is the calibration JSON exported and archived after every calibration? | The only portable record of the system's angles on a date | 14.5, 25.3 | **P2** | Yes |
| **D-26** | Recalibration interval and triggering events — **does daily removal of the Sensor Unit count as disturbing it?** | If the head comes off nightly, calibration is routine rather than periodic | 14.7 | **P1** | Yes, with risk |
| **D-27** | What does a visual QC pass cover? | Two QC layers produce no software artefact at all | 18.5 | **P2** | Yes |
| **D-28** | Is the retro-reflective target check our periodic verification, and at what interval? | The only independent check on the **instrument** in any source | 18.7 | **P2** | Yes |
| **D-29** | What provenance record accompanies a deliverable, and where does it live? | Six facts cannot be reconstructed from the deliverable | 23.6, 24.4 | **P1** | Yes, with risk |
| **D-30** | What does an imagery QC pass cover? | — | 19.3 | **P3** | Yes |
| **D-31** | Is the imagery file-size scan adopted? **Validation required first** | Screening only; file size cannot establish validity | 19.4, 24 L8 | **P3** | Yes |
| **D-32** | What is our position on imagery privacy? Are unblurred originals retained, and for how long? | Legal and reputational dimensions outside this SOP. Blurring is irreversible in the delivered product | 19.6, 25.5 | **P1** | Yes, with risk |
| **D-33** | Does control density vary with predicted GNSS conditions? | Uniform spacing puts the same control where it adds little as where it holds the data together | 20.4, 6.3 | **P2** | Yes |
| **D-34** | What is the decision rule when a corridor produces an unacceptable trajectory? | Includes the legitimate answer that mobile mapping is not the right method for that segment | 20.7 | **P2** | Yes |
| **D-35** | **When may Cleanup be performed, by whom, and what must be archived first?** | Destructive, not undoable, and reduces the registration history at the moment the project is handed on | 21.4, 23.5 | **P1** | **No** — the first person to reach the end of a project decides it by default |
| **D-36** | Is the pre-export trajectory-node confirmation mandatory? | The most consequential check in export | 22.2 | **P1** | Yes, with risk |
| **D-37** | May exports be made with Export timestamps enabled before T18 resolves? | A documented option may substitute reprocessed data for the data that was checked | 22.3 | **P1** | Yes, with risk |
| **D-38** | What are our standard deliverable formats, and which export path produces each? | — | 22.6 | **P2** | Yes |
| **D-39** | What is the corridor continuity inspection method and coverage? | Must detect a degraded stretch shorter than the sampling interval | 24 L7 | **P1** | Yes, with risk |
| **D-40** | What is our default deliverable scaling, and what accompanies it? | Ground scaling does not record its own scale factor | 5.7, 22.5 | **P2** | Yes |
| **D-41** | How many passes, in what pattern, by roadway type? | **Two of three degraded-GNSS remedies require overlap collected on the day** | 6.2 | **P1** | **No** — mission planning cannot be specified |
| **D-42** | Base station strategy and maximum baseline? | Interacts with D-19 | 6.3 | **P1** | **No** |
| **D-43** | Is night collection permitted, and under what conditions? | Solves traffic occlusion, makes imagery unusable for interpretation | 6.4 | **P3** | Yes |
| **D-44** | One clear wet-weather rule, with operator authority to stand down | Neither Trimble nor TMR defines "wet". An operator who must phone will drive | 6.5 | **P2** | Yes |
| **D-45** | Are marginal segments and proposed alternative methods recorded before mobilising? | Professional judgement point | 6.8 | **P2** | Yes |
| **D-46** | Where are lever arms, the Vehicle Preset and the installation configuration recorded and verified? | Entered once, used every mission. An error is systematic and invisible | 7.3 | **P1** | Yes, with risk |
| **D-47** | What free-space margin is required before a mission may start? | A disk filling mid-corridor ends the run and the closing sequence with it | 7.8 | **P3** | Yes |
| **D-48** | What collection speed, by deliverable type? | Trimble publishes maxima and no relationship to deliverable quality | 8.5 | **P2** | Yes |
| **D-49** | What does the mission field record contain? | No software produces it; §9, §11, §24 all depend on it | 8.9 | **P1** | Yes, with risk |
| **D-50** | What coverage verification happens before leaving site? | Missed overlap removes office options irrecoverably | 9.3 | **P1** | Yes, with risk |
| **D-51** | What triggers a re-drive, and may the operator decide alone? | On site, minutes. From the office, a mobilisation | 9.4 | **P1** | Yes, with risk |
| **D-52** | Offload, verification and backup procedure | The only irreversible step in the workflow | 10.3, 10.4 | **P1** | Yes, with risk |
| **D-53** | Folder structure, naming and storage location | Several provenance artefacts are small files loose in a project folder | 10.5 | **P2** | Yes |
| **D-54** | Is a chain-of-custody record required? | The deliverable may not be able to speak for itself | 10.6 | **P3** | Yes |
| **D-55** | What is retained, where, for how long, and by whom? | Tier 1 is a few hundred kB. Tier 3 is hundreds of GB and determines whether reprocessing is ever possible | 25.1, 25.3 | **P1** | Yes, with risk |

**P1 items: 24.** These should be settled before the first production job.

---

## Table 2 — Field Tests Required

Answerable with the software or the system in front of you. **No further documentation research
will resolve any of these.**

| ID | Test | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|
| **T18** | **Export the same registered run twice, timestamps off and on, and compare the point geometry.** Does reprocessing from raw reflect the registered trajectory? | **The highest-priority test in the project.** A documented export option may deliver data that was never the data that was checked | 22.3, 13.8 | **P1** | Yes — by keeping timestamps off |
| **T28** | **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?** Distinguish project object retention from underlying file retention | Determines what must be archived before Cleanup | 21.3, 23.5, 25.4 | **P1** | Yes — by archiving them anyway |
| **T29** | Establish the reliable export-state verification method **for each export path** | How an export dialog resolves its selection is not documented | 22.2, 24 L9 | **P1** | Yes — by verifying project-side |
| **T19** | Publish a registered run to TRCPS and inspect what arrives. Which trajectory is sent? | Trajectory is exported by default; which one is not stated | 22.6.6 | **P2** | Yes |
| **T20** | Same, for the TMX export path | The trajectory file is written "once for all devices"; which one is not stated | 22.6.2 | **P2** | Yes |
| **T21** | Register a mission, run a Mission Report, and look. Does it contain the signed GCP residuals? | The 2025.21 release note says residuals are "included in the report"; the Mission Report topic does not mention them | 17.6 | **P2** | Yes |
| **T22** | Export a LAS and inspect the file directly — header fields, VLRs, sidecar contents | Trimble's topics do not enumerate LAS headers. Something undocumented may be written | 22.7, 23.4 | **P2** | Yes |
| **T23** | Draw a Point Cloud tab selection across scans from two trajectories and observe | Whether TBC warns, prevents or silently permits is not stated | 22.4 | **P2** | Yes |
| **T26** | **Does exported imagery inherit or otherwise reflect a registration adjustment?** Compare a station's position before and after | Imagery is positioned from the trajectory; nothing states whether it is recomputed | 19.1 | **P2** | Yes |
| **T27** | **What imagery streams actually exist on the MX60, and which are exposed through TBC export?** Resolve the apparent inconsistency between the side-images export option and the MX60 export tree lacking Planar cameras. **Also a vendor question — V-8** | **Do not write MX9/MX90 camera behaviour into MX60 procedure.** The option's presence in a dialog is not evidence the sensor exists | 19.2 | **P2** | Yes |
| **T30** | Attempt both reconstruction paths — timestamp matching and trajectory geometry comparison — on a dataset with two candidate trajectories | Neither has been attempted; both are the fallback if provenance is queried | 23.7 | **P3** | Yes |
| **T1** | Default vs High Quality filter preset — selection criteria | High Quality enables three filters unconditionally | 13.3 | **P2** | Yes |
| **T2** | Isolated Points default state | Trimble's own text contradicts itself | 13.3 | **P3** | Yes |
| **T3** | **Does Reflective Panels remove legitimate retro-reflective returns from signs and line marking?** | On sign and retroreflectivity work, those returns **are** the deliverable | 13.3 | **P1** | Yes, with risk |
| **T4** | Range Max default vs useful range in bright sun and at oblique incidence | Points may be retained well beyond useful range | 13.3 | **P2** | Yes |
| **T5** | Fog and Sun filters applied when those conditions did not occur | Both remove real returns | 13.3 | **P2** | Yes |
| **T6** | Colouriser forward vs backward camera preference, and its effect on fringing | No selection rule given | 13.4, 19.5 | **P3** | Yes |
| **T7** | Registration Auto-Saving **default state** | `Targets.csv` is the registration's field book, and a wrong dialog answer empties it | 15.3 | **P2** | Yes |
| **T9** | **Target-Bundle Adjustment** — test both states with independent checks | Checking it makes the adjustment **coarser** (250 m vs 70 m); the name reads backwards | 15.7 | **P2** | Yes |
| **T10** | Which Parametrix coordinate systems does POSPac recognise directly, and which trigger the ITRF00 path? | Answerable once, then known | 5.3, 12.4 | **P2** | Yes |
| **T11** | Multipath default **Medium** on open-sky corridors | Medium is described as being for *degraded* coverage | 12.3 | **P3** | Yes |
| **T12** | DMI scale factor SD default **5 %** — was the wheel actually measured? | Trimble says set it to 100 % if unknown | 12.3 | **P3** | Yes |
| **T13** | LiDAR QC range default 3–100 m | Useful scanner range and useful aiding range are different questions | 12.7 | **P3** | Yes |
| **T14** | LiDAR QC **Lasers = All** | **The default contradicts the guidance printed beside it** | 12.7 | **P3** | Yes |
| **T15** | **Which registration type, when?** Test Global, Local and Global-then-Local with independent checks | No selection rule published; Global-then-Local gets no guidance and appears in every screenshot | 15.5 | **P1** | Yes, with risk |
| **T16** | Working cutting plane thickness for the visual checks | Trimble's own screenshots show 0.030 and 5.000 with no basis | 16.7, 18.6 | **P2** | Yes |
| **T17** | **Sample points** random sampling in the classified LAS exporter | A destructive thinning with no documented spatial rule; default state not stated | 22.6.1 | **P2** | Yes |
| **T24** | How much run overlap is enough for run-to-run registration? | Trimble states the requirement qualitatively only | 16.6 | **P2** | Yes |
| **T25** | Which feature types are fit for horizontal control, vertical control, or both, at MX60 density and incidence? | Will shape control design more than any software setting | 5.5, 17.3 | **P1** | Yes, with risk |

**P1 tests: 6.**

---

## Table 3 — Vendor Clarifications Required

Only Trimble can answer these.

| ID | Question | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|
| **V-1** | **When Export timestamps causes reprocessing from raw data, which trajectory is used?** | Pairs with T18. A direct yes/no question with the largest consequence in the workflow | 22.3 | **P1** | Yes — by keeping timestamps off |
| **V-2** | Is the MX60 laser control presented as *Measurement Prog* + *Line Speed*, or as a combined *Laser Mode*? Which TMI version applies? | The Quick Start Guide and TMI Rev L disagree | 7.7 | **P2** | Yes |
| **V-3** | Which TBC version is installed on our workstation? | Two version-dependent behaviours, both legacy | 1.6, 4.3 | **P2** | Yes |
| **V-4** | Which MX60 configuration do we have — from the serial number? Are GAMS and DMI fitted? Which rack? | Pairs with D-2 | 4.1 | **P1** | **No** |
| **V-5** | **Trimble GAMS Antenna Kit Installation & Operation Manual** — not held | Needed to complete the lever-arm procedure if GAMS is fitted | 7.3 | **P2** | Only if GAMS is not fitted |
| **V-6** | **Trimble DMI Installation & Operation Manual** — not held | Contains the scale factor for the measured wheel diameter, which §12.3 needs | 7.3, 12.3 | **P2** | Only if DMI is not fitted |
| **V-7** | Does the **Lateral Range Limit** affect accuracy, or is it purely a data-volume tool? | Undocumented | 7.7 | **P3** | Yes |
| **V-8** | **What is the MX60's actual camera complement, and which streams are exposed through TBC export?** | Pairs with T27. The MX60 export tree shows no Planar cameras while the export option persists | 19.2 | **P2** | Yes |
| **V-9** | Does **LiDAR QC** have its own POSPac dependency? | Trimble does not state one, but directs configuration questions to Applanix Support | 4.5 | **P2** | Yes |
| **V-10** | Which trajectory do **TMX export** and **Publish to TRCPS** send when a run has both an imported and a registered trajectory? | Both carry trajectory geometry; neither says which | 22.6.2, 22.6.6 | **P1** | Yes, with risk |
| **V-11** | **Which report contains the signed GCP residuals** added in TBC 2025.21? | The only mobile mapping report topic does not mention residuals | 17.6 | **P2** | Yes |
| **V-12** | Does any TBC export write the source trajectory into a LAS header, VLR or sidecar? | The one provenance question documentation cannot answer | 23.4 | **P1** | Yes, with risk |
| **V-13** | Does removing and refitting the Sensor Unit disturb the calibration? What symptoms indicate drift? | Determines whether calibration is periodic or routine | 14.7 | **P1** | Yes, with risk |
| **V-14** | Is the retro-reflective target check the recommended periodic verification for the MX60, and at what interval? | Trimble says "regularly" and defines nothing | 18.7 | **P2** | Yes |
| **V-15** | Scanner field of view — **346°** *(UG p.54)* or **360°** *(spec sheet p.2)*? | Matters for occlusion geometry | 4.1 | **P3** | Yes |
| **V-16** | When should PFIX be preferred over registration? | This document's framing of the distinction is inferred, not stated by Trimble | 20.5 | **P2** | Yes |
| **V-17** | Does the "coordinate system without Geoid" restriction on TMX export apply to the MX60, or only the MX9? | Stated for the MX9 only | 22.6.2 | **P2** | Yes |

**P1 vendor questions: 5.**

---

## Summary

| | Total | P1 | Blocks operation |
|---|---|---|---|
| **Parametrix Decisions** | 54 | 24 | 9 |
| **Field Tests** | 29 | 6 | 0 |
| **Vendor Clarifications** | 17 | 5 | 1 |
| **Total** | **100** | **35** | **10** |

> **Ten items genuinely block operation.** They are: D-2/V-4 (configuration), D-10 (POSPac
> licence), D-13 (acceptance criteria), D-16 (control design), D-19 (computation mode), D-21
> (datum and epoch), D-35 (Cleanup policy), D-41 (pass pattern), D-42 (base station strategy).
>
> **The remaining ninety do not prevent defensible work.** They make it less consistent, less
> efficient, or dependent on individual judgement — which is what an SOP exists to reduce, and is
> exactly the work this backlog represents.

*Contact for vendor questions: `mx_support@trimble.com` · Americas +1-289-695-4416
*(MX60 UG Rev B, p.51)*
