# MX60 Mobile Mapping Technical Manual

**Trimble MX60 · Trimble Business Center 2026.10**

> **LIVING DRAFT — INTERNAL REVIEW**
>
> **This document is a living draft for internal Parametrix review, training, testing and workflow
> development.** It is not an issued Parametrix standard, and it does not replace professional
> judgement, project requirements, safety procedures or approved company policy.
>
> **Items marked Parametrix Decision Required, Proposed, Testing Required or Vendor Clarification
> Required are unresolved.** There are a lot of them, and that is deliberate — an open question is
> shown as an open question rather than filled in with a guess.
>
> **Two things follow from that.** Some requirements here **bind anyway** — Trimble's and the
> equipment's, because their authority was never Parametrix's to grant or withhold; they are listed
> with their sources at **SOP §2.4**. And there is **no Parametrix MX60 acceptance standard** to
> claim, because **D-13** is open.

---

## How to review this draft

**This is not primarily a copy-editing exercise.** Typos and awkward sentences are worth reporting,
but they are not what this draft needs. Four questions matter:

| | |
|---|---|
| **1** | **Is anything technically wrong?** |
| **2** | **Is anything impractical in actual field or office use?** |
| **3** | **Is anything presented more strongly than Parametrix has actually decided?** |
| **4** | **What would prevent you from performing the work using these documents?** |

**Question 3 is the one most likely to be missed.** Every statement with procedural force in this
set carries a label saying whose authority it rests on — Trimble's, the equipment's, or
Parametrix's — and **no Parametrix requirement is adopted at this draft.** If something reads as
settled company practice when it is not, that is a defect, and it is the kind this project is least
able to catch on its own.

**Question 4 is the one that finds gaps.** If you could not actually do the work from these
documents — because a step is missing, a decision is open, a tool is not available, or the
instruction assumes something you were never told — say so. A gap is more useful than a correction.

### Who is being asked

Reviewers are identified by role, because each role sees a different failure.

| Role | What this draft most needs from you |
|---|---|
| **Survey leadership and the responsible PLS** | **Question 3.** Where does this overstate what Parametrix has decided? And which of the open decisions are actually yours to make |
| **MX60 field operators** | **Question 2**, in the vehicle. Sequence, timing, what is realistic on a real shift, and anything the Field How To gets wrong about the machine |
| **TBC mobile mapping processors** | **Questions 1 and 2.** Whether the software behaves as described, in the version you are running, and whether the workflow order survives contact with a real project |
| **QA/QC reviewers** | **Question 1**, and the records. Whether the evidence a section asks for is evidence you could actually review, and whether anything is claimed that the evidence does not support |
| **Project managers who may scope or rely on mobile mapping** | **Question 4.** What you would need to know before scoping this work, pricing it, or promising it to a client — and whether you could find it here |
| **Survey staff with conventional experience and limited mobile mapping experience** | **Question 4, and you are the most important reviewer for it.** Where does this assume something nobody explained? An unexplained assumption is invisible to the people who wrote it, and obvious to you |

### How to point at something

**When commenting, identify the document and the section.** For example: **`Manual §21.4`**, or
**`SOP D-13`**.

Every section and subsection is numbered, and every warning, open decision, test and vendor
question carries an identifier that is the same in all four documents:

| Identifier | Means |
|---|---|
| **§n.n** | A numbered subsection of the document named |
| **W-n** | A warning. Worded identically wherever it appears |
| **D-n** | An open Parametrix decision |
| **Tn** | An open test — something nobody has measured yet |
| **V-n** | An open question for Trimble |

> *"The registration part is confusing"* cannot be acted on. *"`Manual §21.4` is confusing"* can.

**Comments go to the MX60 Internal Review Log.** That is the working channel until Parametrix
assigns a document owner and a review process under **D-1** — there is no named owner to send them
to, and inventing one would be worse than saying so.

---

## Document control

> **Provisional.** Parametrix's document-control convention has not been confirmed (**D-1**). The
> block below is a temporary working scheme for this review only; **it is not a Parametrix
> revision convention and must not be treated as one.**

### Working Version — internal circulation only

> **This is a temporary working identifier, used only while the set is in internal review.** It is
> deliberately **not** a revision letter or number, so it cannot be mistaken for the Parametrix
> document-control convention that **D-1** will establish. A second circulation package on the same
> date becomes `-b`, then `-c`. When D-1 is answered, this block is replaced by the real one.

| | |
|---|---|
| **Document** | **MX60 Mobile Mapping Technical Manual** |
| **Working Version** | `2026-09-11-a` |
| **Status** | **LIVING DRAFT — INTERNAL REVIEW** |
| **Supersedes** | — first circulated draft |
| **Formal revision** | *Not assigned* — **D-1** |
| **Document owner** | *Not assigned* — **D-1** |
| **Approval status** | **Not approved — Living Draft** |
| **Circulated for** | Internal review, training, testing and workflow development |
| **Prepared by** | MX60 mobile mapping documentation project |
| **Review comments** | Record in the **MX60 Internal Review Log** |
| **Set circulated together** | Technical Manual · SOP · Field How To · Office How To, all at Working Version `2026-09-11-a` |

### Evidence revision

This manual documents **the state of the evidence, not a version of the software alone.**

| | |
|---|---|
| **Software documented** | Trimble Business Center **2026.10** · Trimble Mobile Imaging **Rev L** |
| **Trimble help topics** | **38**, captured and classified |
| **Manuals and bulletins** | **7** |
| **Release notes** | 2025.21, 2026.10 |
| **Structured reference records** | **402** — `reference/mx60-reference-data.csv` |
| **Evidence revision** | **E1 — 2026-09-11** |

> The version cross-reference: a registration feature listed as new in the TBC 2026.10 release
> notes is present in the captured help topic *(TBC RN 2026.10; TBC 22905)*. The captured material
> is therefore current, not stale.

### Related documents

| Document | Relationship |
|---|---|
| **MX60 Mobile Mapping SOP** | States what Parametrix requires. **Cites this manual for technical basis** |
| **MX60 Field How To** | Field task instructions. Cites this manual for explanation |
| **MX60 Office How To** | Processing task instructions. Cites this manual for explanation |

---

## What this manual is

**It explains what the MX60 and Trimble Business Center are actually doing, and how we know.**

It is the technical reference from which the SOP and the two How To guides are derived. Where
those documents say *you must* or *click here*, this one says *because*.

| Question | Document |
|---|---|
| **Why does it work this way?** | **This manual** |
| Must I? | SOP |
| How do I do it in the field? | Field How To |
| How do I do it in the office? | Office How To |

### What it assumes

The reader is a competent survey professional. Control networks, datums, geoids, residuals, least
squares and check points are taken as known and are not taught here.

**No prior mobile mapping experience is assumed.** Trajectories, SBETs, GNSS/INS integration,
boresight calibration, scan generation, registration and mobile LiDAR quality control are
explained from the beginning.

### What it is not

**It is not a procedure.** Nothing in this manual is a Parametrix requirement. Where it describes
what Trimble's software does, that is a statement of fact about the software — not an instruction
to do it. **Requirements live in the SOP.**

---

## How to read the evidence tags

Every technical statement carries a tag saying where its authority comes from.

| Tag | Meaning |
|---|---|
| **TRIMBLE DOCUMENTED METHOD** | Trimble documents this, in the cited topic or manual page. **It records what Trimble says, not how strongly.** Where a statement is a Trimble *requirement*, the SOP says so and cites it there — see SOP §2.4 |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software or a captured screenshot; Trimble does not state it |
| **FIELD TESTING REQUIRED** | Answerable by test, not by reading. Appendix E |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble. Appendix E |

> **This manual contains no Parametrix procedure tags.** It does not decide anything. Where a
> Parametrix decision would resolve a question, the manual names the decision — **D-n**, cross-
> referenced to the SOP — and moves on.

> **A documented procedure is not a requirement, here or anywhere in the set.** Trimble publishes a
> great deal of method and requires comparatively little of it. This manual explains the method;
> **SOP §2.4** lists the seven things Trimble and the equipment actually require.

### Citations

`*(TBC 22905)*` a help topic · `*(MX60 UG Rev B, p.54)*` a manual page · `*(TBC RN 2025.21)*` a
release note. Every cited topic is indexed in **Appendix A** with the TBC version it was captured
from.

> **Appendix B — the reference dataset — is the authority for numbers.** This manual explains
> what they mean. When a Trimble revision changes a value, the dataset row changes and the prose
> usually does not.

---

## In Plain Language

Every major technical section ends with a box addressed to **an experienced land surveyor who is
new to mobile mapping**, answering four questions:

**What we just did** · **Why it matters** · **What can go wrong** ·
**What a good result generally looks like**

They re-explain rather than summarise. **Read end to end, with nothing else, they describe the
whole workflow in ordinary language** — a reviewer or project manager can get a true picture from
them alone.

> The SOP and the How To guides do **not** repeat them. The How To guides carry short **Why This
> Matters** notes that point here.

**28 sections carry one.** Three do not, deliberately: **§6** is a glossary, and **§24** and
**§31** are short reference sections with nothing to re-explain. **§21** carries two, because
registration to control and registration run-to-run are different enough to need separate
treatment.

---

## Terminology

**§6 is the authoritative glossary for all four documents.** The SOP and the How To guides carry
only the handful of abbreviations needed to use each of them safely, and point here.

Workflow stage names are frozen and identical across all four documents — see §4.

---

## Contents

**Part I — Principles** · 1 Purpose and scope · 2 Mobile mapping in plain terms · 3 How error
behaves · 4 The workflow end to end · 5 The data chain · 6 Terminology

**Part II — The system** · 7 MX60 system architecture · 8 GNSS/INS integration · 9 GAMS and DMI ·
10 TMI, TBC and POSPac · 11 LiDAR QC · 12 Coordinate systems, datums and epochs

**Part III — Acquisition explained** · 13 Initialization · 14 The closing sequence ·
15 GNSS environment and outage duration · 16 Point density and useful range

**Part IV — Processing explained** · 17 Trajectory processing · 18 Scan generation ·
19 Update Scans · 20 Calibration · 21 Registration · 22 GCPs, check points and residuals ·
23 RMS and what it can prove · 24 Trajectory RMS colouring · 25 Visual QC · 26 Imagery ·
27 Degraded GNSS · 28 Cleanup · 29 Export · 30 Provenance · 31 Periodic system verification

**Part V — Evidence** · A Trimble source index · B Reference dataset · C Figures ·
D Observed software behaviour · E Open technical questions · F Test results · G Source conflicts

---

## Visual identity

This manual follows the **Parametrix Brand Guide v6, November 2023**. Colour, typography, the logo
and its clear space, the spacer arrow and the ix formation are all cited to that guide in
`deliverables/_control/style/style-system.md`. Where the guide is silent — monospace type, tables,
callouts, iconography, screen behaviour — the decision is marked there as an **extension** and is
not a Parametrix brand rule.

All four MX60 documents share one visual system. Each carries one **secondary** brand colour as its
document accent, which the guide permits as a categorisation device: this manual is **Clean Blue**,
the SOP Progress Orange, the Field How To Future Green, the Office How To Optimistic Yellow.

---


---

# Part I — Principles

---


---

# 1. Purpose and Scope

## 1.1 What this manual does

It explains **what the Trimble MX60 and Trimble Business Center are actually doing, and how we
know.** It is the technical reference from which the SOP and the two How To guides are derived.

Three specific jobs:

1. **Preserve the technical knowledge.** Mobile mapping at Parametrix is new. What is understood
   about it today lives in this manual, not in the heads of the people who worked it out.
2. **Preserve the evidence.** Every statement about the software is traceable to a Trimble topic
   or manual page. When Trimble changes something, the change can be found and its consequences
   traced.
3. **Make the other three documents derivable.** A requirement in the SOP, or a step in a How To
   guide, should be traceable to an explanation here.

## 1.2 What it assumes

The reader is a **competent survey professional**. Control networks, datums, geoids, residuals,
least squares adjustment and check points are taken as known and are not taught here.

**No prior mobile mapping experience is assumed.** Trajectories, SBETs, GNSS/INS integration,
boresight calibration, scan generation, registration and mobile LiDAR QC are explained from the
beginning.

Where conventional survey practice and mobile mapping differ, the difference is explained **at the
point where it matters**. Nearly all of those differences reduce to one thing, and §2 is about it:
the instrument never stops, so everything it measures is referenced to a computed path rather than
to an occupied point.

## 1.3 Scope

**In scope** — the MX60 system and its sensors; TMI and TBC as they apply to mobile mapping;
POSPac where the workflow depends on it; the technical basis of every stage from project setup to
archive; the evidence base and its limits.

**Out of scope** — basic land surveying; establishing the control network, which is conventional
survey work; feature extraction and CAD production downstream of the point cloud; static
terrestrial scanning, UAS and aerial workflows except where TBC behaviour is shared; vehicle
operation, traffic control and site safety.

## 1.4 What this manual is not

> **IMPORTANT**
>
> **It is not a procedure, and nothing in it is a Parametrix requirement.**
>
> Where this manual describes what Trimble's software does, that is a statement of fact about the
> software — not an instruction to do it. Where it describes a technique, that is an explanation of
> how the technique works — not a decision that Parametrix uses it.
>
> **Requirements live in the SOP. Steps live in the How To guides.**

Where a Parametrix decision would resolve an open question, this manual **names the decision**
— **D-n** — and moves on. It does not propose an answer.

## 1.5 The four documents

| Question | Document |
|---|---|
| **Why does it work this way?** | **This manual** |
| **Must I?** | MX60 Mobile Mapping SOP |
| **How do I do it in the field?** | MX60 Field How To |
| **How do I do it in the office?** | MX60 Office How To |

**Cross-references** use four fixed forms:

> For technical background, see **Technical Manual §X.X**.
> For the required company procedure, see **SOP §X.X**.
> For step-by-step field instructions, see **Field How To §X.X**.
> For processing instructions, see **Office How To §X.X**.

## 1.6 How to read this manual

| If you are… | Start at |
|---|---|
| **New to mobile mapping** | §2, then §3, then the **In Plain Language** boxes end to end |
| **Looking up one behaviour** | The contents, or **Appendix A** — the Trimble source index |
| **Checking a number** | **Appendix B** — the reference dataset is the authority for numbers |
| **Deriving a requirement** | The relevant Part IV section, then the SOP clause it supports |
| **Reviewing after a TBC update** | **Appendix A** — the source index, topic by topic |

> **The In Plain Language boxes are a complete document in themselves.** Read end to end, with
> nothing else, they describe the whole workflow in ordinary language. That is deliberate — a
> reviewer or project manager can get a true picture without working through the technical detail.

## 1.7 Evidence base and its limits

| | |
|---|---|
| Trimble help topics captured and classified | **38** |
| MX60, TMI and accessory manuals and bulletins | **7** |
| Release notes | 2025.21, 2026.10 |
| Structured reference records | **402** |
| Software documented | **TBC 2026.10** · TMI Rev L |
| Evidence revision | **E1 — 2026-09-11** |

### Three limits, stated plainly

**Trimble's help describes dialogs, options and outputs.** It does not exhaustively enumerate file
formats — LAS header fields and VLR content in particular. Where this manual says a behaviour is
not documented, that is a statement about Trimble's documentation, not a claim that the software
lacks the capability (§30).

**Twenty-four questions require testing rather than reading.** They are not gaps in
the research; they are questions no documentation would answer.

**Sixteen questions require Trimble**, and remain open with them.

> **Source ingestion is complete for the purposes of this manual.** Every export and publish path
> available to an MX60 has been read, and the remaining uncertainty is about software behaviour
> that Trimble does not document.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We set out what this manual is for — explaining how the system works and
> recording how we know — and, just as importantly, what it is not: it decides nothing and requires
> nothing.
>
> **Why it matters.** Mobile mapping produces enormous, convincing datasets very quickly. A point
> cloud with a hundred million points looks authoritative whether or not the path underneath it was
> ever checked. The only thing between "looks right" and "is right" is understanding what the
> software actually did — which is what this manual is for — and a procedure that says what must be
> verified, which is the SOP's job.
>
> **What can go wrong.** Reading a description here as an instruction. This manual explains that
> TBC can register a run from a single control point. That is true, and it is not a
> recommendation — it is a fact about the software with a warning attached. If you find yourself
> citing this manual as authority for doing something, you want the SOP.
>
> **What good looks like.** You can point at any technical statement in this manual and answer in
> one sentence: *who says so, and where?* Every one of them carries a citation. If one does not,
> that is a defect worth reporting.

---

# 2. Mobile Mapping in Plain Terms

This section is for the reader who knows surveying and has never operated a mobile mapping
system. Everything else in this manual depends on the ideas here.

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

- Why initialization matters, and why it is not a formality (§13)
- Why GNSS conditions dominate the accuracy conversation (§15, §27)
- Why everything downstream of the trajectory has to be recomputed when it changes (§18, §21)
- Why the office work is largely about improving the trajectory, not the points (§17, §21)
- Why proving *which trajectory* produced a deliverable turns out to be hard (§30)

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
> practical reason the field procedure requires a proper closing sequence (§14), and it is the
> single most commonly skipped step in mobile mapping.

Two supporting sensors appear throughout this document:

- **GAMS** — a second GNSS antenna. Two antennas a known distance apart give a direct heading
  measurement, which is otherwise the hardest attitude component to determine. It speeds up
  initialization considerably *(TBC 25943)*
- **DMI** — a distance measuring indicator on a wheel. It provides an independent along-track
  distance, which constrains the inertial solution when GNSS is poor *(TBC 25943)*

## 2.3 What the office actually does

A surveyor coming from static scanning expects office work to mean registration of scans to
each other and to control. Mobile mapping is different in an instructive way.

| Stage | What is being improved |
|---|---|
| **Trajectory processing** (§17) | The trajectory itself, from raw observations and base station data |
| **Scan generation** (§18) | Nothing — this applies the trajectory to produce the cloud |
| **Calibration** (§20) | The fixed angular offsets between sensors. Periodic, not per-job |
| **Registration** (§21) | **The trajectory again**, now using surveyed control or overlapping cloud |
| **Update Scans** (§19) | Nothing — this reapplies the improved trajectory to produce a new cloud |

> **Three of the five stages improve the trajectory. Two of them just recompute points.**
>
> This is the shape of mobile mapping office work, and it is why the phrase "registering the
> point cloud" is misleading. You are not moving points. You are improving the path the sensor
> took, and then recomputing where the points must therefore have been.


---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We established the one idea the rest of this manual rests on: a mobile
> mapping system has no occupied point. It computes where it was, continuously, and every point it
> collects is hung off that computed path. The path is called the trajectory, and it is the job.
>
> **Why it matters.** Think of it as a very long, very fast resection that never stops — except
> that instead of resecting from known points, the system is dead-reckoning with an inertial sensor
> and correcting itself with satellites whenever the sky allows. When the sky does not allow, it
> keeps going on inertial alone and quietly gets worse. Almost everything the office does later is
> an attempt to improve that path, not to move the points around.
>
> **What can go wrong.** The thing that catches people is that the office work does not look like
> registration in the static scanning sense. Three of the five office stages improve the
> trajectory; two of them just recompute points from it. A processor who thinks they are moving a
> point cloud will eventually be surprised by something — most often by discovering that a
> registration they performed never reached the data (§19).
>
> **What good looks like.** You can say, for any point in a delivered cloud, which trajectory put
> it there and what the quality of that trajectory was at that instant. §30 is about how far that
> is currently possible.

---

# 3. How Error Behaves

This is where a surveyor's intuition needs adjusting, and it is worth being precise. The
three properties below explain most of what is unusual about mobile mapping QC.

## 3.0 Error is not uniform across the dataset

This is where a surveyor's intuition needs adjusting, and it is worth being precise.

**Error is not uniform across the dataset.** It varies along the corridor with GNSS quality, and
it varies within a single scan line with range.

## 3.1 Attitude error multiplies with range

An error in the *position* of the sensor head displaces every point by the same amount. An
error in the *attitude* — which way it was pointing — displaces points by an amount
proportional to how far away they are.

The relationship is simple geometry: lateral displacement is range multiplied by the angular
error in radians. A given attitude error therefore costs five times as much at 50 m as at 10 m.

> This is arithmetic, not a specification. **No Trimble source in the set publishes an attitude
> error budget for the MX60**, so the useful range for a given tolerance has to be established
> from the manufacturer's accuracy statement for the configuration Parametrix owns (§7.3), or by
> test.

> **WHY THIS MATTERS**
>
> This is why *useful range* is a shorter distance than *maximum range*. The scanner can return
> a point at its maximum range; whether that point is good enough to measure from is a
> different question, and the answer depends on the attitude accuracy of the trajectory at that
> instant. Two clouds collected on the same day with the same instrument can have quite
> different useful ranges if one was collected under open sky and the other in an urban canyon.

## 3.2 Error is correlated in time, not scattered

Conventional survey errors tend to be independent — one shot's error tells you little about the
next. Mobile mapping error is **strongly correlated over seconds and minutes**, because it is
dominated by the state of a filter that evolves smoothly.

The practical consequence: a bad stretch of trajectory produces a whole *region* of cloud that
is consistently displaced, not a scatter of bad points. It will look internally consistent and
perfectly clean. **It will simply be in the wrong place**, and only comparison against
independent control will reveal it.

> That is the most important thing in this section. **Mobile mapping data does not look wrong
> when it is wrong.**


## 3.3 Why this changes the QC method

The three properties above have direct consequences, and each has its own section later:

| Property | Consequence | § |
|---|---|---|
| Error is not uniform | A mission is not "good" or "bad" — it has stretches. QC produces a list, not a verdict | 24 |
| Attitude error scales with range | **Useful range is shorter than maximum range**, and varies with the trajectory quality at that instant | 16 |
| Error is correlated in time | **Spot-checking does not work.** A bad stretch shorter than the sampling interval passes every sample | 25 |

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at how mobile mapping gets things wrong, which is not how a
> total station gets things wrong.
>
> **Why it matters.** Conventional survey errors tend to be independent — one shot's error tells
> you little about the next, so a scatter of bad values stands out. Mobile mapping error is
> dominated by a filter that evolves smoothly over seconds and minutes, so it arrives in **runs of
> consistently displaced data** rather than in scattered bad points.
>
> **What can go wrong.** The consequence people find hardest to accept: **bad mobile mapping data
> does not look bad.** If the trajectory drifted through a tree-lined stretch, the cloud from that
> stretch is still crisp, still dense, still internally consistent — and sitting several
> centimetres from where it should be. There is no noise, no scatter, no visual tell. You find it
> by checking against control you surveyed independently, or you do not find it at all.
>
> **What good looks like.** A dataset where you know *where* the weak stretches are, because you
> looked at the trajectory quality before you ever generated a point cloud (§24), and where
> independent check points in those specific stretches came back in the same range as the ones in
> the open.

---

# 4. The Workflow, End to End

Every stage, in order, with what it produces and where it is. **Read this once and the rest of
the document has a shape.**

| | Stage | What it produces | § |
|---|---|---|---|
| **Plan** | Project setup and control | A CRS, a control network that brackets the job, designated check points | 5 |
| | Mission planning | A route, a pass pattern, mapped GNSS-hostile stretches and a mitigation for each | 6 |
| **Field** | Preparation and preflight | A mounted, calibrated, measured system | 7 |
| | Acquisition | A mission: raw scanner, imagery and navigation data | 8 |
| | Field QC | Confirmation the data **exists and is complete** — not that it is good | 9 |
| | Transfer | A verified copy, in two places | 10 |
| **Office** | Import | An **index** in TBC. Still no point cloud | 11 |
| | **Trajectory processing** | The **SBET** — the computed path. *The accuracy ceiling is set here* | 12 |
| | **Generate Scans** | The point cloud, by applying the trajectory to the raw scanner data | 13 |
| | *(Calibration)* | Sensor boresight angles. **Periodic — most projects skip this** | 14 |
| | **Registration** | A **better trajectory**, fitted to surveyed control. *The cloud has not moved* | 15, 16 |
| | **Update Scans** | A **new point cloud**, on the registered trajectory. **Without this the registration reaches nothing** | 13.6 |
| | QC | Residuals, independent checks, and a visual inspection | 17, 18, 19 |
| | *(Degraded GNSS)* | A branch, if QC fails — and two of its three remedies had to be arranged in the field | 20 |
| | *(Cleanup)* | A light project with one answer. **Destructive and not undoable** | 21 |
| **Deliver** | Export | The deliverable — which may not identify the trajectory that produced it | 22, 23 |
| | Final QA/QC | Ten layers of verification, before it leaves | 24 |
| | Archive | The records that let the work be defended later | 25 |

Three things to carry out of that table:

1. **The trajectory is computed once and improved twice** — at §17, then at §21. Everything
   else either applies it or checks it.
2. **Registration and Update Scans are two steps.** Doing the first without the second leaves the
   deliverable unadjusted, and it looks identical.
3. **Bracketed stages are conditional.** Calibration is periodic. The degraded-GNSS branch and
   Cleanup happen only when the job calls for them.


## 4.1 Frozen stage names

The stage names in the table above are **frozen**. They are used identically in this manual, the
SOP, both How To guides, every checklist and form, and future training material.

| | |
|---|---|
| Project setup · Mission planning · Field preparation · Acquisition · Field QC · Transfer | |
| Intake · Trajectory processing · Scan generation · Calibration · Registration · Update Scans | |
| QC · Degraded-GNSS handling · Cleanup · Export · Final QA/QC · Archive | |
| **Provenance** — cross-cutting rather than a stage | |

> **A stage is not a command.** *Registration* is the stage; **Register a Run**, **Register a
> Mission** and **Register Run to Run** are three commands that perform it (§21). **Update Scans**
> is unusual in being both a stage name and a command name, and that is Trimble's doing.

The authoritative list, with the synonyms that are not to be used, is
the glossary at **§6**.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We laid out every stage from planning to archive on one page, with what
> each produces.
>
> **Why it matters.** Read once, it gives the rest of the manual a shape. The three things worth
> carrying away are in the table's closing notes: the trajectory is computed once and improved
> twice; registration and Update Scans are two separate steps; and several stages are conditional
> rather than routine.
>
> **What can go wrong.** Treating the conditional stages as routine, or the routine ones as
> optional. Calibration is periodic — most projects skip it. Cleanup is destructive — some projects
> should skip it. Update Scans is neither, and skipping it silently undoes a registration.
>
> **What good looks like.** Anyone on the team using the same word for the same stage. That sounds
> trivial until two people are discussing "registration" and one means the adjustment while the
> other means the whole office process.

---

# 5. The Data Chain

The names in this section matter because TBC's commands are named after them. A processor who
does not know which object a command acts on will eventually act on the wrong one — and several
of the commands are not undoable.

## 5.1 The chain, once

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

Two things are worth stating now and are returned to in §18.

**The MX60 converts TMX to RWCX in one step.** Older MX9 and MX90 systems go through an
intermediate stage requiring a range-ambiguity correction called MTA. **The MX60 workflow has no
MTA stage**, which removes a whole category of setup and a whole category of failure
*(TBC 22503)*.

**The trajectory is applied at scan generation, not at collection.** The raw scan data is
sensor-relative. It becomes a georeferenced point cloud only when combined with a trajectory —
which is why improving the trajectory later means regenerating the cloud (§19, §21).

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22503)*
>
> MX50 and MX60 convert **TMX → RWCX in one step**. MX9 and MX90 go RXP → TMX → RWCX in two, and
> the intermediate stage requires **MTA** (Multiple Times Around) range-ambiguity correction.

> **The MX60 has no MTA configuration and no MTA failures.** If you encounter TBC documentation
> about configuring a GPU driver for MTA correction *(TBC 23856)*, it does not apply to this
> system. It is mentioned here only because it is prominent in the TBC help and causes confusion.

## 5.2 The mission on disk

What the system writes in the field:

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 20736-1, 22503, 22554, 25943)*

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

Three observations about this structure that matter operationally:

**The `.mxdb` is an index, not the data.** It is small. Copying it alone copies nothing useful.
Everything the chain depends on sits in the sibling folders, which is why the transfer requirement
is the whole mission folder and not a file.

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

**`Extcal.json` travels with the mission.** The calibration state that produced the data is
recorded alongside the data rather than held only in the software. This is the single most
useful provenance artifact in the chain and is discussed in §30.

**`POS_1/raw/` is the irreducible original.** Every trajectory the office ever computes — the
first SBET, a LiDAR QC refinement, a PFIX second pass, a registered variant — derives from those
files. They are the only thing in the mission that cannot be recomputed.

## 5.3 The mission in Project Explorer

What the same mission looks like after import into TBC:

```
Mobile Mapping
  └── <mission id>
        ├── Capture Devices          Camera 3 Back Down, Camera 4 360°, Laser Left, Laser Right
        └── Run 0, Run 1, Run 2 …
              └── Sbet                the imported trajectory
                    └── (scans appear here after Generate Scans)
```

> **Note the shape. Scans are children of a trajectory, not of a run.**
>
> That is the structural fact that makes tree position meaningful evidence of which trajectory a
> cloud was built on (§30) — and it is why a run with two trajectories has two independent sets of
> scans beneath it.

A run that has been registered therefore does not *replace* its scans. It gains a second
trajectory node, and after **Update Scans** (§19) a second set of scans hanging off it. Both sets
remain in the project, look identical in plan, and are distinguishable only by their position in
the tree and by the `_reg_####` suffix on the newer stations. Everything difficult about MX60
provenance follows from that one sentence.

## 5.4 What each object can and cannot be regenerated from

| Object | Regenerated from | Lost if deleted |
|---|---|---|
| **SBET** | `POS_1/raw/` + base data, through POSPac | Recoverable — but the processing settings that produced *this* SBET are not recorded in the file |
| **Registered SBET** | The parent SBET + the registration + surveyed control | Recoverable only if the picked targets survive (`Targets.csv`, §21) |
| **TMX** | `Laser_1`, `Laser_2` raw | Recoverable |
| **RWCX** | TMX + a trajectory | Recoverable — **against whichever trajectory is selected at the time**, which is not necessarily the one that produced the original |
| **Picked targets** | Nothing. A human picked them | **Not recoverable.** Re-picking produces different points |
| **`POS_1/raw/`** | Nothing | **Not recoverable.** Re-collect the mission |

> **CAUTION**
>
> Read the middle rows carefully. Most of the chain is reproducible, which makes it tempting to
> treat any individual file as disposable. The two rows that are not reproducible — raw
> observations and human target picks — are also the two most likely to be discarded, because one
> is large and the other is small enough to overlook.

## 5.5 Where each stage's quality is decided

The chain is worth reading a second time as a sequence of irreversible commitments:

| Stage | What is fixed here | What can still be fixed later |
|---|---|---|
| **Field collection** | Geometry, coverage, GNSS conditions, initialization quality | Nothing. This is the only stage with no office remedy |
| **Trajectory processing** | Which corrections and which base data were used | Reprocess — cheap, as long as the raw data is intact |
| **Scan generation** | Filters applied, colorization | Regenerate — cheap in effort, expensive in time |
| **Registration** | The fit to surveyed control | Register again, or re-pick. But adjustments stack (§21) |
| **Export** | What the client receives | Re-export, if the project still exists in the state that produced it (§29, §30) |

> **WHY THIS MATTERS**
>
> Every stage after the first is recoverable, and the first is not. That asymmetry is the reason
> this manual spends more of its length on field method than the office's share of the schedule
> would suggest. An office error costs hours. A field error costs a mobilisation.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We named the four things the data passes through — the mission database,
> the trajectory, the polar scan data, and the point cloud — and said which command turns each one
> into the next.
>
> **Why it matters.** Nearly every confusing thing in the office workflow makes sense once you
> know that the point cloud is *computed*, not *collected*. The scanner measured ranges and angles
> from a sensor that was moving. The trajectory says where that sensor was. Multiply the two
> together and you get coordinates. That is what **Generate Scans** does, and it is why changing
> the trajectory later means doing it again.
>
> **What can go wrong.** Two things, both common. The first is copying the `.mxdb` and thinking
> you have the mission — you have the table of contents. The second is looking at a run in Project
> Explorer, seeing two sets of scans, and assuming one is a duplicate to be tidied away. They are
> the same raw data computed against two different trajectories, and which one you keep is a
> decision about the accuracy of the deliverable, not about disk space.
>
> **What good looks like.** You can point at any point cloud in the project and say which
> trajectory produced it, without guessing. If you cannot, §30 explains how to work it out and how
> far that evidence actually goes.

---

# 6. Terminology

**This section is the authoritative glossary for all four Parametrix MX60 deliverables.** The
SOP, the Field How To and the Office How To carry at most a short list of essential abbreviations
and point here. Where a term appears to be defined twice, this section governs.

Terms are grouped by where you meet them rather than alphabetically, because most of the
confusion in this subject is between two terms that sit next to each other in the workflow —
boresight and lever arm, Register a Run and Register a Mission, Global and Local.

## 6.1 Five words that do not mean what they usually mean

Ordinary survey usage and TBC usage diverge on a small number of words. Every one of them has
caused a real mistake, and they are collected here so that the divergence is seen once rather
than discovered five sections apart.

| Word | Ordinary survey usage | What it means here |
|---|---|---|
| **Target** | A physical panel or prism you place and observe | **A point picked in the point cloud** by the operator, which is then paired with a surveyed GCP *(TBC 22905; §21)* |
| **Registration** | Bringing scans into a common frame by moving them | **Adjusting a trajectory.** It does not move points, and does not touch the cloud at all until **Update Scans** runs (§19) |
| **Calibration** | A broad word covering any instrument check | In TBC, specifically **boresight estimation** — the angular offset between sensor and inertial frame. Lever arms are *not* estimated (§20) |
| **Local** | Nearby, or a local coordinate system | An adjustment method that interpolates **between** control points and **does not extrapolate beyond the outermost one** *(TBC 22905; §21)* |
| **Station** | An occupied instrument setup | **One instant of imagery capture** along a run. A mobile mapping system occupies nothing |

> **"Target" is the trap that catches people first.** A checkerboard panel is one kind of feature
> you might pick, but so is the corner of a painted road marking, or a manhole rim. The physical
> thing in the field is the **GCP**. The thing in TBC's Targets pane is a *pick*.

## 6.2 The trajectory and navigation

| Term | Meaning |
|---|---|
| **Trajectory** | The computed position and attitude of the sensor head over time. Everything the system collects is referenced to it (§2.1) |
| **SBET** | **Smoothed Best Estimate of Trajectory** — the post-processed trajectory, computed forward and backward through time and merged. The normal input for survey work |
| **NAV** | The real-time trajectory computed in the vehicle. A fallback, not an option (§17.1) |
| **POSPac MMS** | Applanix software that computes the SBET. **A licence is required** for both the external route and TBC's in-application command (§10.3) |
| **IN-Fusion+ Single Base** | POSPac computation mode using corrections from a local base station |
| **IN-Fusion+ PP-RTX** | POSPac computation mode using Trimble RTX corrections, with no local base |
| **GNSS/INS integration** | Combining satellite positioning with inertial sensing so each covers the other's failure mode (§8) |
| **IMU** | Inertial Measurement Unit. Precise instant to instant, **drifts without limit** over time |
| **GAMS** | GNSS Azimuth Measurement System — a second antenna giving a direct heading measurement. Speeds initialization *(TBC 25943)* |
| **DMI** | Distance Measuring Indicator — a wheel sensor giving independent along-track distance. Scale factor sign depends on the mounting side *(TBC 25943)* |
| **Initialization** | The static period, straight run and dynamic manoeuvres that let the filter resolve attitude and sensor bias (§13) |
| **`smrmsg_xxx.out`** | POSPac file describing position, orientation and velocity RMS after smoothing. **The source of the trajectory's RMS colouring** *(TBC 27248)* |
| **ITRF00 path** | Where POSPac does not recognise the project datum and epoch, the SBET is computed in ITRF00 and then transformed — indicated by the filename `sbet_[mission]_[frame].out` *(TBC 25943; §12.3)* |

## 6.3 Missions, runs and data objects

| Term | Meaning |
|---|---|
| **Mission** | One deployment. The `.mxdb` and everything beneath it |
| **Run** | One continuous stretch of collection within a mission. A mission has many |
| **Station** | One instant of imagery capture along a run |
| **`.mxdb`** | The mission database written in the field. **The file you import** |
| **TMX** | Polar scan data — ranges and angles, sensor-relative. Not georeferenced |
| **RWCX** | The point cloud — XYZ, intensity, colour, normals. Produced by applying the trajectory to TMX |
| **MTA** | Multiple Times Around — range-ambiguity correction. **Not part of the MX60 workflow** *(TBC 22503; §18.1)* |
| **`Extcal.json`** | The calibration file written with the raw mission data |
| **Capture Devices** | The TBC node listing the sensors: for the MX60, **Camera 3 Back Down**, **Camera 4 360°**, and the two lasers |

## 6.4 Processing commands

| Term | Meaning |
|---|---|
| **Process Raw Trajectory Data** | Computes an SBET inside TBC. **Requires POSPac 8.6+ and a licence** *(TBC 25943)* |
| **Generate Scans** | Applies the trajectory to raw scanner data, producing the point cloud (§18) |
| **Update Scans** | **Recomputes scans against a different trajectory.** How a registration reaches the point cloud. No Filters pane *(TBC 22638; §19)* |
| **Recover Mobile Mapping Scans** | Recovery for failed or interrupted scan generation *(TBC 28155)* |
| **LiDAR QC** | Uses scan data as an aiding sensor, SLAM-like, to refine the trajectory. Runs inside trajectory processing *(TBC 28972; §11)* |
| **PFIX** · **Generate POSPac Position Fixes** | Projects GCP-to-target offsets back into the navigation solution for a **second POSPac pass** *(TBC 24460; §27.5)* |
| **Cleanup Mobile Mapping Mission** | Keeps the most recent registration and removes the rest. **Destructive and not undoable** *(TBC 26466; §28)* |

## 6.5 Calibration

| Term | Meaning |
|---|---|
| **Boresight** | The fixed **angular** offset between a sensor and the inertial reference frame. **This is what a calibration estimates** |
| **Lever arm** | The fixed **distance** offset between two sensors. **Known from manufacture and measurement — not estimated** *(TBC 24886; §20.2)* |
| **Installation Matrix** | Parameters **before** calibration — the as-built values *(TBC 22920)* |
| **Refinement Matrix** | Parameters **after** calibration *(TBC 22920)* |
| **Boresight installation / Boresight refinement** | The same distinction as it appears in TBC's sensor properties *(TBC 24868)* |
| **Vehicle frame** | **+X forward, +Y right, +Z downward.** Governs lever arms and boresight angles *(TBC 25943; §7.6)* |

## 6.6 Registration

| Term | Meaning |
|---|---|
| **Registration** | Adjusting a **trajectory** to fit surveyed control, or to fit another run. **It does not move points** (§21.1) |
| **Register a Run** | GCPs matched to picked targets, one run *(TBC 22905)* |
| **Register a Mission** | The same, across a set of runs, with each GCP reusable *(TBC 26473)* |
| **Register Run to Run** | **Cloud-to-cloud** against a fixed Reference Run. **Uses no surveyed control** *(TBC 25096; §21.10)* |
| **Reference Run** | In run-to-run, the run whose trajectory does not change |
| **Run to Adjust** | The run optimised to the Reference Run |
| **GCP** | Ground control point — "an accurately surveyed coordinate location for a physical feature that can be identified on the ground" *(TBC 22905)* |
| **Target** | **In TBC's registration sense: a point picked in the point cloud.** Not a physical panel (§21.2) |
| **Validation point (VP)** | A GCP set **As Check** — paired and measured, but **excluded from the adjustment** *(TBC 22905; §22.2)* |
| **Use XY · Use Z · As Check** | The three independent per-point choices in the Control Points list (§22.2) |
| **Global** | A shift of the whole trajectory, without rotation *(TBC 22905)* |
| **Local** | Local adjustment interpolating **between** control points. **Does not extrapolate beyond them** *(TBC 22905; §21.5)* |
| **Global, and then Local** | Global first, then Local. No separate selection guidance published |
| **Target-Bundle Adjustment** | Checked = **250 m** intervals (coarser); unchecked = **70 m** *(TBC 22905; §21.7)* |
| **Point Cloud Smart Picking** | The picking tool. Types: Default, Intersected Plane, Road Mark *(TBC 22905)* |
| **`Targets.csv`** | Where picked targets are saved when Registration Auto-Saving is on. **Emptied permanently by answering "No" to the reload prompt** *(TBC 22905)* |
| **`sbet_<date>_reg_####.out`** | The registered SBET on disk, incrementing per registration *(TBC 22905)* |
| **`_reg_####` suffix** | Carried by scan stations updated against a registered trajectory *(TBC 22638)* |
| **Reg. Trajectory · RegTrajectory** | The adjusted trajectory node, from Register a Run and Register a Mission respectively |

## 6.7 Quality

| Term | Meaning |
|---|---|
| **Tangential / Orthogonal / Vertical** | TBC's three-axis agreement convention: along travel, across travel, and up. Diagnostic, not just descriptive (§23.3) |
| **Overall Overlap** | Percentage of points used against those generated, in calibration *(TBC 24886)* |
| **The RMS asymmetry** | **Good RMS does not prove success; bad RMS proves failure; a visual check is necessary** *(TBC 24886, 25096)* |
| **Cutting Plane View** | Profile view across a plane, used to check agreement between overlapping data. **Set rendering to Scan Color** or two offset surfaces read as one thick one (§25.1) |
| **Scan Color** | Rendering mode giving one colour per scan. **Part of the QC method, not a display preference** |
| **`No overlap`** | In run-to-run Results, a timestamp where the two runs do not overlap. Informative, not noise (§21.15) |
| **Undefined RMS colour** | How registered trajectory segments render, having lost their match to the `smrmsg` file *(TBC 27248)* |
| **Mission Report** | Capture devices, runs, trajectories, generated scans, and **per-sensor calibration with date** *(TBC 23991_1, 24868)* |

## 6.8 Export and delivery

| Term | Meaning |
|---|---|
| **Mobile Mapping tab** | Export pane tab holding the **run-aware** exporters |
| **Point Cloud tab** | Export pane tab holding the generic exporters. **Selects by region or drawn rectangle — not by run** *(TBC 11769; §29.4)* |
| **Export to LAS (Trajectory Split)** | The classified-regions exporter. Splits by distance; **carries no trajectory** *(TBC 27279)* |
| **Scaling: Grid** | Projected coordinates with the combined scale factor. **Writes a `.txt` sidecar naming the CRS and scale factor** *(TBC 11769)* |
| **Scaling: Ground** | Ground coordinates. **Does not expose the scale factor used** *(TBC 11769)* |
| **ECEF export** | Ground-scaled LAS/LAZ including the project's global CRS *(TBC 11769)* |
| **Export timestamps** | **Not merely an attribute toggle.** Set to Yes, "the exported scans are reprocessed from the raw data" *(TBC 23339, 22501; §29.3)* |
| **Publish to TRCPS** | Upload to Trimble Connect. **Point cloud and trajectories are exported by default** *(TBC 29527)* |
| **TRCPS** | Trimble Reality Capture Platform Service — an extension of Trimble Connect |
| **TDU** | Trimble Desktop Utility, installed with TBC, which performs the upload |

## 6.9 Evidence tags

These tags appear throughout all four deliverables. They are the mechanism that keeps verified
Trimble behaviour separate from proposed Parametrix practice, and they are load-bearing: a
statement's tag is part of its meaning.

| Tag | Meaning |
|---|---|
| **TRIMBLE DOCUMENTED METHOD** | Trimble states this, in the cited topic or page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software; not stated by Trimble as procedure |
| **PARAMETRIX PROCEDURE (PROPOSED)** | Recommended by this document. **Not company policy** |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Decided by Parametrix, with a date and owner in Appendix H |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make |
| **FIELD TESTING REQUIRED** | Answerable by testing, not reading |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble |
| **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL** | Carried from the v1 draft; not yet re-sourced |
| **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED** | A screening method proposed here and not yet validated |

> **The tag is a state, not a style.** A clause tagged **PARAMETRIX PROCEDURE (PROPOSED)** is a
> recommendation made by this project. It becomes **(ADOPTED)** only when Parametrix records a
> decision against it, with a date and an owner, in the SOP's adoption record. At the revision on
> the front matter of this manual, **no entry has been adopted.**

## 6.10 Terms deliberately not defined here

| Term | Why not |
|---|---|
| Parametrix document-control vocabulary — *controlled copy*, *document owner*, *effective date*, revision scheme | Parametrix's actual convention has not been established. This project uses temporary descriptive identifiers rather than inventing one (§1.5) |
| Accuracy classes, tolerance bands, pass/fail thresholds | No numerical acceptance criterion is defined in this manual. Trimble publishes no MX60 acceptance tolerance, and inventing one would be worse than leaving it open (§23, master register **D-13**) |
| Ordinary survey terms — *resection*, *least squares*, *geoid*, *combined scale factor* | Assumed knowledge. This manual teaches mobile mapping to surveyors, not surveying (§1.2) |

---


---

# Part II — The System

---


---

# 7. MX60 System Architecture

## 7.1 The units

The MX60 is a vehicle-roof-mounted mobile mapping system. Its components, as they appear in
this document and in TMI:

| Component | Function |
|---|---|
| **Sensor Unit** | The roof-mounted head: scanners, cameras, GNSS antenna, IMU. **24–28 kg** depending on configuration *(MX60 UG Rev B)* — a two-person lift |
| **Control Unit** | In-vehicle computer, data storage, power management. **IP30 — not waterproof**, and lives inside the vehicle *(MX60 UG Rev B, p.53)* |
| **Exchangeable data disk** | Removable storage inside the Control Unit |
| **Mounting rack** | Attaches the Sensor Unit to the vehicle |
| **GAMS antenna** *(optional)* | Second GNSS antenna for direct heading |
| **DMI** *(optional)* | Wheel-mounted distance measuring indicator |

## 7.2 The sensors

| Sensor | Count | Notes |
|---|---|---|
| Laser scanner | **2** | One per side, mounted at opposing oblique angles |
| Spherical camera | 1 | 360° panoramic |
| Rear-downward camera | 1 | Pavement-facing |

> **The two-scanner arrangement is the reason Register Run to Run can work on a single run**, and
> the reason most exports produce a pair of files — *Laser Left* and *Laser Right* — rather than
> one *(TBC 22501, 23339)*.

## 7.3 The three configurations

Three: **Core**, **Pro**, **Premium** *(MX60 UG Rev B, p.12)*. They differ in the 360° camera
and in the GNSS/IMU grade.

| | Core | Pro | **Premium — ours** |
|---|---|---|---|
| Panoramic image size | **8192 × 4096 px** | **12288 × 6144 px** | **12288 × 6144 px** |
| Side / planar image size | 4096 × 3008 px | 4096 × 3008 px | 4096 × 3008 px |

*(TBC 22501, 23888 — the panorama figures; these are the sizes TBC writes at export)*

> **The Parametrix system is the MX60 Premium.** Read the Premium column throughout this manual,
> and the larger of any two figures a Trimble topic gives. Recorded in the master register under
> **D-2**; confirmation against the serial number is still outstanding under **V-4**.

## 7.4 Specification discrepancies to be aware of

Two unresolved conflicts sit in the source documents. Neither blocks work, but neither should be
quoted to a client without checking.

| | Source A | Source B | Status |
|---|---|---|---|
| Scanner field of view | ~346° beam deflection *(MX60 UG Rev B, p.54)* | Full 360° *(Spec sheet, p.2)* | **VENDOR CLARIFICATION REQUIRED · V-15** — matters for occlusion geometry |
| Mounting rack | MX SCAN Roof Rack, 18 kg | MX Shock Absorbing Mounting Rack, 28 kg | **PARAMETRIX DECISION REQUIRED** — which is fitted. The published GAMS corner offsets apply to the standard rack **only** *(MX60 UG Rev B, p.68)* |

*(Recorded as `CONFLICT-002` and `CONFLICT-003` in `reference/mx60-reference-data.csv`.)*
## 7.5 The vehicle frame

Every offset and every angle in this system is expressed in one convention, and it is worth
fixing in mind once because it is not the convention most surveyors carry around.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943, 24886)*
>
> - **Positive X = forward driving direction**
> - **Positive Y = right side of the vehicle**
> - **Positive Z = downward**

> **WHY THIS MATTERS — Z is down**
>
> A sensor mounted **above** the reference point has a **negative Z** in this convention. Getting
> the sign wrong puts twice the offset into the solution, in the wrong direction — and it will not
> present as a sign error downstream. It will present as a height problem, which people
> reasonably attribute to the geoid, the antenna model or the base station.

The same convention governs every boresight angle in §20: **roll about X, pitch about Y, heading
about Z**, with Z pointing down.

## 7.6 Lever arms and boresight angles — the two kinds of offset

The system has to know where each sensor is relative to the inertial reference point, and how
each sensor is oriented relative to it. These are two different quantities, determined in two
different ways, and conflating them is the most common conceptual error in this subject.

| | **Lever arm** | **Boresight** |
|---|---|---|
| What it is | The **distance** offset between two sensor frames — a three-dimensional vector | The **angular** offset between a sensor and the inertial reference frame |
| How it is determined | **Measured.** Known from manufacture and from installation measurement | **Estimated.** This is what a calibration solves (§20) |
| Changes when | The hardware is remounted or the rack changes | Thermal cycling, vibration, remounting — it drifts |
| Error behaviour | A constant offset, the same at every range | **Multiplies with range** (§3.1) |

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
>
> "**Lever Arm** refers to the displacement between two body coordinate frames… expressed as a
> three-dimensional vector."

> **TBC's laser scanner calibration solves angles only** *(TBC 24886; §20.2)*. If a lever arm is
> wrong, no amount of calibration will find it — the adjustment has no parameter for it. It will
> be absorbed partly into the boresight estimate, which then compensates for a translation with a
> rotation, and the compensation is only correct at the range where it was determined.

> **CAUTION**
>
> **Changing the rack, the roof bars, the vehicle, or the Sensor Unit's position on the rack
> invalidates the lever arms and may invalidate the calibration.** None of those changes announces
> itself in the data, and the resulting error is systematic rather than noisy.

### Where the values live

`Extcal.json`, written alongside the raw mission data, carries the calibration state that
produced that mission (§5.2). TBC distinguishes the values **before** calibration from the values
**after**:

| Term | Meaning |
|---|---|
| **Installation Matrix** | Parameters **before** calibration — the as-built values *(TBC 22920)* |
| **Refinement Matrix** | Parameters **after** calibration *(TBC 22920)* |
| **Boresight installation / Boresight refinement** | The same distinction as it appears in TBC's sensor properties *(TBC 24868)* |

## 7.7 The optional sensors, and why fitment is a live question

GAMS and DMI are both optional. Whether this system has them changes the field procedure, the
office procedure, and what the data is capable of — which is why their fitment sits in the master
register as a blocking item rather than a detail.

| | Fitted | Not fitted |
|---|---|---|
| **GAMS** | Direct heading from a two-antenna baseline. Initialization is faster and heading is better determined throughout (§9.1) | Heading must be solved from motion. **Straight driving during initialization matters more, not less** *(TBC 25943; §13)* |
| **DMI** | Independent along-track distance, constraining the solution through GNSS gaps (§9.2) | The inertial sensor carries the gaps alone |

> **Open Parametrix decision — D-2 / V-4.** *Are GAMS and DMI fitted, and which rack is on the
> vehicle?* The configuration itself is answered — **Premium** — but these three are not, and each
> changes procedure: GAMS changes how the first two minutes of every mission are driven, DMI
> changes what the published no-outage accuracy assumes, and the rack decides whether the
> published GAMS corner offsets apply at all. One call to the dealer answers all three.

## 7.8 Power

The Control Unit manages vehicle power. The specifications below are what the installation has to
satisfy; the installation procedure itself is the **Field How To §6**.

> **TRIMBLE DOCUMENTED METHOD**
>
> | | Value | Source |
> |---|---|---|
> | Input voltage | **12–16 V DC** | MX60 UG Rev B |
> | Current at startup | **25 A at 12.8 V** (320 W) | MX60 UG Rev B |
> | Current in operation | 12 A (160 W) | MX60 UG Rev B |
> | **Supply rating required** | **30 A or more** | MX60 QSG Rev B, p.4 |
> | Direct-connection fuse | **35 A**, close to the battery | MX60 UG Rev B |
> | Data storage | 2 × 4 TB removable SSD | MX60 Spec Sheet, p.3 |
>
> An **auxiliary battery as a backup power source is recommended** *(MX60 QSG Rev B, p.4)*.

> **WHY THIS MATTERS**
>
> The startup draw is twice the operating draw. A supply sized for the operating figure will brown
> out at every power-on, and the symptom — a system that starts unreliably — does not look like a
> supply problem.

## 7.9 The protection that ends a run

The Control Unit manages vehicle power, and it protects the vehicle's battery rather than the
mission. That priority is correct and worth knowing about in advance.

> **CAUTION · W-11**
>
> **Battery Protect** *(MX60 UG Rev B, p.27)*:
>
> | Event | Trigger |
> |---|---|
> | Audible warning | Supply below **10.5 V for longer than 12 seconds** |
> | Power cut | Supply below **10.5 V for more than 90 seconds** |
> | Recovery | Voltage rises above **12.0 V within that 90 seconds** |
>
> The alarm leaves roughly **78 seconds** to restore charge — that figure is the arithmetic of the
> two sourced timings, not a separately published one.
>
> An interrupted run loses the closing sequence with it.

> **WHY THIS MATTERS**
>
> The consequence is not "the system switched off." It is that the mission ended without a closing
> sequence, so the backward filter pass has no anchor at the end of the data (§14). The cost is
> paid at the end of the trajectory, which is often the most recent and most important part of the
> day's work.
>
> The practical response is to keep the engine running while the system is operating, and to treat
> the audible warning as an instruction to restore charge immediately rather than as information.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We took the system apart on paper: two laser scanners, two cameras, a
> GNSS/inertial unit, and optionally a second antenna and a wheel sensor — plus the conventions
> that describe where each of them sits.
>
> **Why it matters.** Almost every number in the rest of this manual depends on two things about
> this particular vehicle: which configuration it is, and what is fitted to it. The first is
> settled — **Premium**, so the panoramas are the full 12288 × 6144 px and the navigation grade is
> the best of the three. The second is not. Without GAMS, the heading has to be solved out of the
> vehicle's motion, which changes how you drive the first two minutes of every mission. That is
> not a detail to look up later — it changes the procedure.
>
> **What can go wrong.** The offset signs. Z is **down** in this convention, so a sensor on the
> roof has a negative Z. And a lever arm is measured while a boresight is estimated, so a wrong
> lever arm cannot be calibrated out — the calibration has no parameter for it, and will quietly
> absorb part of the error into an angle instead, which then only works at one range.
>
> **What good looks like.** The configuration, the fitment and the measured offsets are written
> down somewhere a processor can find them, and somebody has checked them against the vehicle
> rather than against the last project's paperwork. These values are entered once and used on
> every mission afterwards, so an error in them is systematic, invisible, and permanent until
> someone re-measures.

---

# 8. GNSS/INS Integration

§2 said the trajectory is the job. This section says how the trajectory is computed, because
almost everything the field procedure asks for is an attempt to give this computation what it
needs.

## 8.1 Two sensors that fail in opposite ways

The trajectory is a time series: position (X, Y, Z) and attitude (roll, pitch, heading) at a high
rate, for the whole mission. It is produced by combining two sensor types whose failure modes are
complementary.

| | **GNSS** | **Inertial (IMU)** |
|---|---|---|
| Measures | Absolute position | Change in orientation and velocity |
| Error behaviour | **Bounded but noisy** — it does not drift, but it jumps and can be lost entirely | **Smooth and precise instant to instant, but drifts without limit** over time |
| Fails when | Sky is obstructed — trees, buildings, bridges, tunnels | Always, gradually, by its nature |
| Rate | Low | High |

Neither is adequate alone. Combined, each covers the other's weakness: GNSS anchors the inertial
solution and stops the drift; the IMU carries the solution smoothly through the gaps when GNSS is
degraded or absent.

> **WHY THIS MATTERS**
>
> This is the whole reason mobile mapping works, and also the whole reason it fails quietly. The
> integration is *designed* to keep producing a plausible answer when one of its inputs stops. It
> does not stop, warn, or degrade visibly. It keeps going, and the error grows in a way that is
> smooth, continuous and invisible in the point cloud (§3).

## 8.2 What the filter does with them

The combination is done by a filter that maintains an estimate of the system's state — position,
velocity, attitude, and the sensor errors themselves — and updates it as observations arrive.

Three consequences follow from the way such a filter works, and all three show up in the field
procedure:

**It estimates sensor errors, not just position.** Gyro and accelerometer biases are part of what
the filter solves for. That is why a period of good observations early in the mission improves
the whole mission, and why initialization is a procedure rather than a warm-up.

**Some states are only observable under motion.** Heading, in particular, cannot be separated
from a gyro bias when the vehicle is stationary and moving in a straight line at constant speed.
It becomes observable when the vehicle accelerates, decelerates and turns. This is why
initialization requires manoeuvres and not merely time (§13).

**It weights each observation by an assumed accuracy.** Those assumptions are settings —
multipath level, DMI scale factor standard deviation, GAMS baseline standard deviation (§17.3).
A setting that overstates an input's accuracy pulls the solution toward a measurement it should
have discounted.

## 8.3 Forward, backward, and the smoother

For survey work the filter is run **twice** — once forward through time and once backward — and
the two passes are merged. The merged result is the **Smoothed Best Estimate of Trajectory**,
universally abbreviated **SBET**. The real-time solution computed in the vehicle is the **NAV**,
which is a fallback and not an option for survey deliverables (§17.2).

```
   forward pass    ────────────────────────────────────────────►
                   good data      GAP        good data
   backward pass   ◄────────────────────────────────────────────
                                   ▲
                   the gap is bridged from both sides
```

> **The backward pass is why the end of a mission matters as much as the beginning.**
>
> A gap in the middle of the drive is bracketed by good data on both sides, and the smoother can
> bridge it from both directions. A gap at the **end** has good data on one side only — the
> forward pass arrives at it already degraded, and there is no backward pass to meet it. The same
> is true in reverse at the start.

This is the practical reason the field procedure requires a proper closing sequence (§14), and it
is the single most commonly skipped step in mobile mapping. It is also why the degraded stretches
at the two ends of a trajectory are worse than an identical stretch in the middle, and why
control and check points at the ends are worth more than control in the middle (§22).

## 8.4 What the filter cannot do

Three limits are worth stating explicitly, because a good deal of misplaced confidence comes from
assuming otherwise.

**It cannot create information that was not collected.** A long GNSS outage is bridged by
propagating an inertial solution that is drifting. The smoother makes the bridge as good as the
surrounding data allows; it does not make it as good as observed data.

**It cannot tell you that it struggled, in the point cloud.** The output of a degraded stretch is
a clean, dense, internally consistent cloud in the wrong place (§3.2). The evidence of the
struggle lives in the trajectory's RMS record, not in the points (§24).

**It cannot distinguish a systematic error in its inputs from the truth.** A wrong antenna model,
a mis-keyed base station coordinate, a DMI scale factor for the wrong wheel: each is a consistent
error that the filter will happily absorb and propagate. Nothing in the RMS will look wrong,
because nothing in the internal consistency of the solution *is* wrong (§23).

## 8.5 Where each remedy acts

It helps to see the whole set of remedies as acting at different points on this diagram, because
they are not interchangeable and their costs are different (§27):

| Remedy | Acts on | Needs |
|---|---|---|
| **Better acquisition** | The observations themselves | Planning, and a second mobilisation if discovered late |
| **Reprocessing with better base data** | The GNSS side of the filter | Raw data intact, better corrections available |
| **LiDAR QC** | Adds the scan data as a third aiding sensor | Overlapping runs, a large workstation (§11) |
| **PFIX** | Injects surveyed control into a **second POSPac pass** | POSPac licence, surveyed control, picked targets (§27) |
| **Registration** | Bends the finished trajectory to fit control | Surveyed control, and it acts after the fact (§21) |

> The first four improve the *solution*. Registration improves the *fit*. That distinction matters
> because a registered trajectory has been adjusted to agree with the control it was given, and
> its agreement with that control is therefore no longer evidence of anything (§23).

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked inside the thing that produces the trajectory: two sensors that
> fail in opposite ways, a filter that combines them, and a second pass run backwards through time
> so that gaps are bridged from both ends.
>
> **Why it matters.** Every odd-sounding requirement in the field procedure comes from this. Why
> sit still for a few minutes at the start — because the filter is solving for sensor biases and
> needs quiet observations to do it. Why drive straight, then vary speed, then turn — because
> heading is not observable until the vehicle accelerates and turns. Why finish the mission the
> same way you started it — because the backward pass needs good data at the end, and a gap at the
> end of a drive has good data on one side only.
>
> **What can go wrong.** The filter never stops producing an answer. That is the point of it and
> it is also the trap. Drive under half a kilometre of tree cover and the solution keeps coming,
> smooth and confident, drifting the whole way. Nothing in the point cloud from that stretch looks
> different from the good data on either side of it.
>
> **What good looks like.** Continuous observations, short well-bracketed gaps, a proper start and
> a proper finish. Then the RMS record of the trajectory — which you can look at before any point
> cloud exists (§24) — tells you where the solution was strong and where it was not, which is
> exactly where to put your control and your check points.

---

# 9. GAMS and DMI

Both are optional. Both change what the system is capable of, and both change the field
procedure. Whether this system has them is an open item (**D-2 / V-4**, §7.7).

## 9.1 GAMS — a second antenna, and therefore a heading

**GAMS** is the GNSS Azimuth Measurement System: a second GNSS antenna mounted a known distance
from the primary one. Two antennas a known distance apart give a **direct heading measurement**.

That matters because heading is the hardest attitude component to determine. Roll and pitch are
anchored by gravity — an accelerometer knows which way is down. Nothing anchors heading. Without
a second antenna, heading has to be solved out of the vehicle's motion, which requires the
vehicle to move in ways that make it observable (§13).

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.67)*
>
> GAMS **reduces initialization time and eliminates the special driving manoeuvres** otherwise
> required.

> **Read the second half of that sentence.** It says, by implication, that **the manoeuvres are
> required when GAMS is not fitted.** Trimble's Quick Start Guide states the same thing from the
> other direction: **straight driving is more important if a GAMS antenna is not used**
> *(MX60 QSG Rev B, p.12)*. The field procedure is therefore not the same on a system with GAMS
> and a system without, and knowing which one this is precedes writing it down (§13).

### What GAMS requires to work

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, pp.67–68)*
>
> | Requirement | Value |
> |---|---|
> | Offset accuracy, **collection only** | 10 cm or better |
> | Offset accuracy, **post-processing** | **on the order of a few millimetres** |
> | Minimum baseline, post-processing | **2.0 m** between primary and secondary antennas |
> | Antenna matching | Primary and secondary **must be the same type**. Do not mix |
> | Measured to | The **L1 antenna phase centre** of the secondary antenna |
> | Re-measure | **Every time GAMS is re-installed** on the roof for a new mission |

> **The two accuracy figures are two orders of magnitude apart, and survey work is on the tight
> one.** All Parametrix mobile mapping is post-processed, so the requirement is millimetres, not
> centimetres. A GAMS offset good enough to navigate with is not good enough to survey with.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.68)*
>
> Known offsets from the **top-left front corner of the standard Trimble Roof Rack** to the
> external reference point: **X +1.006 m · Y −0.469 m · Z +0.025 m**.

> **CAUTION**
>
> Those published offsets apply to the **standard roof rack only** — not to the shock-absorbing
> mounting rack. Which rack is fitted is an open conflict in the source documents
> (`CONFLICT-003`, §7.4). Using the published corner offsets on the wrong rack puts a fixed,
> systematic error into the GAMS baseline and therefore into heading.

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* is
> not held. It is needed to complete the installation procedure if GAMS is fitted.

### What GAMS is worth

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.56)*
>
> Heading accuracy, all configurations: **0.015°**, with the GAMS option and a 2 m baseline.

Apply §3.1 to that figure to see what it means in the cloud: an angular error acts through range,
so the same heading error produces a proportionally larger position error the further the feature
is from the vehicle.

## 9.2 DMI — an independent measure of distance travelled

A **DMI** (Distance Measuring Indicator) is a wheel-mounted sensor giving an independent
along-track distance. It constrains the inertial solution when GNSS is poor: the IMU can drift in
along-track scale, and the DMI does not.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.46; TMI UG Rev L, p.21)*
>
> - The DMI wheel must be a **non-steering** wheel
> - The lever arm is measured to **the centre of the tread where the DMI wheel contacts the road**
> - TMI requires the lever arm in metres, the **mounting position — left or right, taking the
>   driving direction as reference** — and the **wheel diameter**, which is to be measured "with
>   great care"

### Two signs that point in opposite directions

This is the single most error-prone detail in the installation, and it is worth setting out
side by side because both quantities are entered by hand, both depend on the mounting side, and
they carry **opposite** signs.

| Quantity | Mounted **left** | Mounted **right** | Source |
|---|---|---|---|
| **Lever arm Y** (vehicle frame: +Y is right) | **negative** | positive | *(MX60 UG Rev B, p.46)* |
| **Scale factor** (trajectory processing, §17.3) | **positive** | negative | *(TBC 25943)* |

> **CAUTION**
>
> A left-mounted DMI has a **negative Y lever arm** and a **positive scale factor**. They are
> different quantities describing different things — one is a position, one is a correction to a
> measured distance — and their signs are not related. Anyone who reasons "it's on the left, so
> both are the same sign" will get one of them wrong.
>
> The lever arm is entered in the field, in TMI. The scale factor is entered in the office, in
> TBC. **Record which side the DMI is on at installation**, because the processor cannot see the
> vehicle.

### The 5 % that is an assumption, not a measurement

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
>
> DMI scale factor standard deviation: **default 5 %**. "Increase the setting if the scale factor
> is not known with 5% accuracy, and **set it to 100% if it is not known at all**."

> **FIELD TESTING REQUIRED · T12**
>
> **The 5 % default is only correct if the wheel diameter was actually measured.** If the value
> came out of a manual for a nominal tyre, 5 % is an assertion of accuracy that nobody verified,
> and the filter is weighting the DMI accordingly. Trimble provides the honest escape hatch — set
> it to 100 % if unknown. Determine which case applies before trusting the default.

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble MX Distance Measuring Indicator Installation & Operation Manual** *(referenced
> MX60 UG p.42)* is not held. It contains the scale-factor value for the measured wheel diameter,
> which trajectory processing needs (§17.3).

## 9.3 The failure mode both share

> **OBSERVED SOFTWARE BEHAVIOR / TRIMBLE DOCUMENTED METHOD** — *(TMI UG Rev L, p.21)*
>
> "If an aiding navigation sensor is not activated in Vehicle Settings its data will **not** be
> logged — even though all connections may have been made properly."

> **CAUTION**
>
> This applies to both DMI and GAMS. The hardware can be correctly installed, correctly wired and
> physically present, and log nothing, because a checkbox in Vehicle Settings is off. There is no
> cabling fault to find and nothing looks wrong.
>
> In the office the symptom is the corresponding pane in **Process Raw Trajectory Data** appearing
> **dimmed** — TBC dims the GAMS and DMI settings when the sensor was disabled during acquisition
> *(TBC 25943; §17.3)*. By then the mission is collected.

Two consequences: the preflight check on a system with either sensor fitted has to confirm
activation and not merely presence, and the office intake check has to look at whether those
panes are dimmed and say so, while a re-collection is still cheap.

## 9.4 Summary — what each contributes

| | **GAMS** | **DMI** |
|---|---|---|
| Gives the filter | A direct **heading** observation | An independent **along-track distance** |
| Most valuable | At initialization, and wherever heading is weakly determined | Through GNSS outages, where inertial along-track scale drifts |
| Without it | Heading is solved from motion; straight driving and manoeuvres matter more *(QSG p.12)* | The inertial solution carries outages unaided |
| Configured | In TMI Vehicle Settings, field | Lever arm in TMI, field; scale factor in TBC, office |
| Silent failure | Not activated in Vehicle Settings → not logged | Not activated → not logged; or scale factor from a nominal, unmeasured wheel |

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at the two optional sensors: a second GNSS antenna that measures
> heading directly, and a wheel sensor that measures how far the vehicle actually travelled.
>
> **Why it matters.** Heading is the attitude component nothing else pins down. Gravity tells the
> system which way is down, so roll and pitch have an anchor; nothing tells it which way is north.
> With a second antenna it gets that directly. Without one it has to work it out from how the
> vehicle moves, which is why the driving manoeuvres at the start of a mission exist and why
> Trimble says straight driving matters *more* when GAMS is absent. The DMI does a different job:
> it keeps the along-track scale honest through a tunnel or under tree cover, where the inertial
> sensor alone will quietly stretch or compress the distance travelled.
>
> **What can go wrong.** Three things, all of them silent. A sensor that is installed but not
> activated in Vehicle Settings logs nothing at all. A DMI scale factor taken from a manual rather
> than a measured wheel is a guess wearing a 5 % accuracy label. And the DMI's two signs run
> opposite ways — left-side mounting means a negative lever-arm Y and a positive scale factor —
> which catches people who assume the two must agree.
>
> **What good looks like.** Somebody knows which sensors are fitted, the offsets were measured to
> millimetres rather than centimetres because this is post-processed survey work, the activation
> was confirmed before driving, and the mounting side is written down somewhere the office can
> find it.

---

# 10. TMI, TBC and POSPac — and the Licensing Gates

## 10.1 Trimble Mobile Imaging — the field software

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

> **VENDOR CLARIFICATION REQUIRED · V-2**
>
> **Which TMI version is on the Parametrix system, and how are firmware updates distributed?**
> One documented behaviour differs between versions: the Quick Start Guide describes two separate
> MX60 laser controls (*Measurement Prog* and *Line Speed*), where TMI Rev L describes a single
> combined **Laser Mode** *(MX60 QSG p.10; TMI UG Rev L p.29)*. *(Appendix E; `CONFLICT-005`)*

## 10.2 Trimble Business Center — the office software

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
> *(TBC 11769)*. §29 covers the distinction. Choosing the wrong tab is an easy and consequential
> mistake.

### Version-dependent behaviour

Two behaviours in this document depend on TBC version. Both are legacy.

| Behaviour | Boundary | Relevance |
|---|---|---|
| Laser scanners and cameras calibrated **outside** TBC and imported as JSON | "up to the 5.21 version" *(TBC 24886, 24868)* | 5.21 predates 5.70, the oldest release Trimble publishes notes for. **Any recent installation calibrates in TBC** |
| **Select RMS File** prompt on a registration with no RMS file | "typically a project saved in TBC prior to version 5.80" *(TBC 27248)* | Affects **inherited legacy projects** only |

TBC renumbered from `5.x` to `YYYY.MM` after 5.90.1; releases run 2023.10 through 2026.10
*(TBC RN 2025.21)*.

> **VENDOR CLARIFICATION REQUIRED · V-3**
>
> **Which TBC version is installed on the Parametrix workstation?** This manual documents
> **2026.10**. Several behaviours it describes were introduced in 2025.21 or 2026.10, and an older
> installation will not have them. It is a one-line answer that nobody has written down.
> *(Appendix E)*

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

## 10.3 POSPac MMS — and the licence gate that shapes the whole workflow

**Applanix POSPac MMS** computes the SBET from raw GNSS and inertial observations. Whether
Parametrix holds a licence determines which office workflow is even available.

> **TRIMBLE DOCUMENTED METHOD**
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

> **Open Parametrix decision — D-10.** *Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?* Stated and tracked in the **SOP §13**; see also the master register.

## 10.4 Trimble Connect and TRCPS

**Publish to TRCPS** uploads point cloud data, trajectories and images from TBC to a **Trimble
Connect** project, through the **Trimble Desktop Utility (TDU)** installed alongside TBC. It
requires a Trimble ID, and uploads consume the account's Trimble Connect storage quota
*(TBC 29527)*.

It matters to this document for a reason beyond delivery convenience: **it is one of only two
paths that carries the trajectory out of TBC with the data** (§29, §30).

## 10.5 Reference documents

The full list is §1.6. Two gaps:

> **VENDOR CLARIFICATION REQUIRED · V-5, V-5**
>
> **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* and
> **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)* are both needed to
> complete the lever-arm procedure (§7.6, and the **Field How To**), **if those accessories are fitted**. Neither is held.
>
> Note that the MX60 User Guide requires millimetre-level GAMS offsets and a **≥ 2.0 m baseline**
> where navigation data will be post-processed *(p.68)* — which is all survey-grade work.
> *(Appendix E)*

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We inventoried the hardware and the three pieces of software, and
> identified the two questions that decide what the office workflow can even look like: which
> configuration of MX60 this is, and whether Parametrix has a POSPac licence.
>
> **Why it matters.** Most equipment sections are reference material you never read twice. This
> one contains a fork in the road. If there is no POSPac licence, the trajectory has to be
> computed somewhere else and one of the three fixes for bad GNSS is simply unavailable — and
> you want to know that before you quote a job through a tree-lined corridor, not during it. The
> configuration question was similar — and is now answered, **Premium**. Core and Premium differ by a factor of four in image
> resolution, so a promise about imagery deliverables made without knowing which one is on the
> roof is a promise made blind.
>
> **What can go wrong.** The quiet failure here is the Export dialog having two tabs that both
> produce point clouds. The Mobile Mapping tab knows about runs; the Point Cloud tab does not,
> and lets you export a rectangle drawn across a view. Both produce a plausible LAS file. Only
> one of them was selected with any awareness of which data it was taking. §29 comes back to
> this.
>
> **What good looks like.** Before the first production job, someone should be able to state, on
> one page: the configuration and serial number, whether GAMS and DMI are fitted, which rack is
> on the vehicle, the TMI version, the TBC version, and whether a POSPac licence exists and where
> it lives. None of that is known today. All of it is a phone call to the dealer.

---

# 11. LiDAR QC

## 11.1 What it is, and what it costs to run

**LiDAR QC Processing** uses the scan data itself as an aiding sensor to improve the trajectory
where GNSS is poor — similar in principle to SLAM *(TBC 28972)*. It is the only documented remedy
for degraded GNSS that needs **neither POSPac nor additional ground control** (§27).

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

> **Open Parametrix decision — D-11.** Stated and tracked in the **SOP §13**; see also the master register.

> **VENDOR CLARIFICATION REQUIRED · V-9**
>
> **Does LiDAR QC have its own POSPac dependency?** Trimble does not state one, but it is an
> Applanix technology and the topic directs configuration questions to the **Applanix Support
> Team** *(TBC 28972)*. *(Appendix E)*

## 11.2 What it actually computes

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 28972)*
>
> "LiDAR QC is an advanced trajectory processing technology that, **similar to LiDAR SLAM**, is
> using scan data as an aiding sensor to improve georeferencing accuracies in areas of poor GNSS
> coverage or in areas where overlapping scans are not perfectly matching. Based on a robust and
> iterative least square adjustment, LiDAR QC generates 3D Voxels that are matched in overlap
> scan regions. The result of this iterative process is solving the constant IMU boresight angles
> and making corrections to the post-processed trajectory (position and orientation)."

Enabled by the **LiDAR QC (Refine with scans)** checkbox in Process Raw Trajectory Data, which
adds a LiDAR QC tab. Requires **MATLAB Runtime R2024b (24.2)** and a substantial workstation
(§11.1).

## 11.3 Settings

| Setting | Values | Default |
|---|---|---|
| **Range** | Minimum and maximum LiDAR measurement distance used | **3 m to 100 m** |
| **Noise** | 5, 10, 50, 80, 100, 200 mm | **5 mm for MX50/MX60**; 10 mm for MX9/MX90 |
| **Lasers** | Left · Right · All | **All** |

> **FIELD TESTING REQUIRED · T13, T13**
>
> **T13 — the 3–100 m range.** The MX60's useful range and the range over which scan geometry
> usefully aids a trajectory solution are different questions. 100 m may include returns too noisy
> to help.
>
> **T13 — Lasers = All.** Trimble's own text beside the setting says using both "can increase
> computation time without significantly improving the accuracy, as it compares the left versus
> right laser of isolated runs." **The default contradicts the guidance printed next to it.**
> *(Appendix E)*

## 11.4 Running it

Select runs from the Project Tree **with overlap — parallel runs, or crossing runs** — click
**Add**, set the parameters, **Compute** *(TBC 28972)*.

## 11.5 The acquisition geometry it needs

Trimble prescribes a specific acquisition geometry for LiDAR QC:

| Element | Requirement |
|---|---|
| **Area** | "a structured scene such as a residential area with detached houses and objects within the LiDAR sensor's maximum range"; "open sky terrain for good GNSS satellite visibility" |
| **Strips** | "two perpendicular strips. **Each strip will consist of two runs (one in each direction)**" |
| **Strip length** | **250–300 m** |

*(TBC 28972)*

> This is materially the same geometry the laser scanner calibration requires (§20.3) — four runs,
> two orthogonal pairs, both directions. **One site can serve both**, which matters because
> establishing a calibration site is a real piece of work (the **SOP §15**).

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at a way of improving the trajectory using the scan data itself.
> Instead of relying only on GNSS and the inertial sensor, LiDAR QC matches overlapping scans to
> each other and works backwards to a better path — the same idea a SLAM system uses, applied
> after the fact to data you already have.
>
> **Why it matters.** It is the only remedy for poor GNSS that needs neither a POSPac licence nor
> additional surveyed control (§27). If you have overlapping runs — and the recommended pass
> pattern gives you overlapping runs anyway — the information needed to improve the solution is
> already sitting in the dataset.
>
> **What can go wrong.** It is not free. The hardware requirement is a serious workstation, not a
> good laptop: 128 GB of RAM at minimum, 256 GB recommended, plus a separate MATLAB runtime. If
> the machine cannot meet that, the capability does not exist for us regardless of what the
> checkbox says. And it needs genuine overlap — running it on isolated passes that do not see the
> same ground gives it nothing to match.
>
> **What good looks like.** Overlapping runs, a structured scene with buildings and hard edges
> rather than open field, and a machine that can hold the problem in memory. Note that the
> acquisition geometry LiDAR QC wants is nearly the same one the laser scanner calibration wants
> (§20), so one site can serve both purposes.

---

# 12. Coordinate Systems, Datums and Epochs

## 12.1 What this section covers

Coordinate systems, datums, projections and geoid models are ordinary survey knowledge and this
manual does not teach them. What it does cover is the handful of places where **mobile mapping
uses them differently from conventional survey work**, and where that difference has caused real
errors:

- The project coordinate system must be set **before** the mission is imported, not after (§12.2)
- The trajectory is computed in a frame chosen by POSPac, which may not be the project's, and the
  only outward sign is a filename (§12.3)
- Epoch matters more than usual, because the trajectory's reference frame and the project's
  control may be realised at different epochs (§12.4)
- Grid and ground scaling behave asymmetrically at export — one writes down what it did, the
  other does not (§12.5)

Everything else about datums and projections is assumed.

## 12.2 Set the project coordinate system before importing

> **TRIMBLE DOCUMENTED METHOD**
>
> "Create a VCE project and if necessary, change the coordinate system so that it matches the
> coordinate system for the mobile mapping data to import." *(TBC 24886, 24460)*

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

### The database

> **TRIMBLE DOCUMENTED METHOD**
>
> The **Coordinate System Database v115** ships with TBC 2026.10. Selecting a predefined geoid
> model now enters the vertical datum name automatically *(TBC RN 2026.10)*.
>
> Two v115 entries relevant to US work: a grid transformation from **CSRN2025 (NAD83 2011) to
> CA SRS Epoch 2017.50** for California zones 1–6, and a **beta** Canadian **NATRF2022(CSRS)**
> with SGEOID2022-beta2.

## 12.3 The frame the trajectory is computed in

The trajectory is produced by POSPac, not by TBC (§17), and POSPac has its own view of the
project's coordinate system.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
>
> | Condition | SBET filename |
> |---|---|
> | Datum and epoch **known** by POSPac | `sbet_[mission name].out` |
> | Datum and epoch **unknown** by POSPac | `sbet_[mission name]_[frame].out` — computed "first in ITRF00 and then in the datum and epoch of the project" |

> **The filename is a processing-path indicator and nothing more** (§17.4, and Layer 3 of the layered verification — the **SOP §16**). It tells
> you an additional transformation occurred. It does not tell you the parameters were right, that
> the project CRS is set up correctly, or that the result is accurate. The plain form is equally
> not proof of correctness.

> **FIELD TESTING REQUIRED · T10**
>
> **Establish which of Parametrix's normal coordinate systems POSPac recognises directly, and
> which trigger the ITRF00 path.** Answerable once, then known — and it determines whether an
> extra transformation is routine on Parametrix work or exceptional. *(Appendix E)*

### Computation mode and the reference frame

> **Open Parametrix decision — D-19.** Stated and tracked in the **SOP §6**; see also the master register.

## 12.4 Epoch

> **TRIMBLE DOCUMENTED METHOD**
>
> From TBC 2026.10: "When working with a time-dependent datum, you can now work at a specific
> epoch that is not the default reference epoch for the selected datum… **Note that this feature
> is intended for experienced users, as incorrect settings may lead to inaccurate results.**"
> *(TBC RN 2026.10)*

> **Open Parametrix decision — D-21.** Stated and tracked in the **SOP §6**; see also the master register.

## 12.5 Grid, ground, and what the deliverable carries

Decided at export (§29.5), but it belongs in project setup because the client agreement depends
on it.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 11769, 27279)*
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

> **Open Parametrix decision — D-38.** Stated and tracked in the **SOP §6**; see also the master register.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We went through the four places where mobile mapping treats coordinate
> systems differently from a conventional survey: when the CRS has to be set, what frame the
> trajectory was actually computed in, why epoch matters, and what a grid or ground export
> carries with it.
>
> **Why it matters.** In conventional work the coordinate system is something you can change your
> mind about — the observations are raw and the reductions are repeatable. Here the coordinate
> system is baked into everything downstream the moment the mission is imported, because the
> trajectory, the scans, the registration and the exports are all computed products. Change the
> CRS afterwards and you have not reprojected your data; you have orphaned it.
>
> **What can go wrong.** The one that is hardest to catch is the trajectory frame. POSPac may not
> recognise the project's datum and epoch, in which case it computes in ITRF00 and then transforms
> — and the only thing that tells you so is an extra word in the SBET filename. That is not an
> error, and the result may be perfectly correct. But it means an extra transformation happened
> that nobody chose, and if the parameters were wrong it will look like a small systematic shift
> rather than like a mistake.
>
> **What good looks like.** The CRS, datum, epoch and geoid are set and written down before the
> first mission is imported. Somebody has looked at the SBET filename and knows which path it
> took. And the client agreement says grid or ground in writing, because a ground-scaled export
> does not record the scale factor it used and the recipient cannot recover it from the file.

---


---

# Part III — Acquisition, Explained

---


---

# 13. Initialization — What It Actually Solves

Initialization looks like a warm-up. It is not. It is a short observation campaign designed to
make quantities observable that are not observable at rest or at constant velocity, and the
quality of everything collected afterwards depends on it.

The operational step list lives in the **Field How To**. This section explains what each step is
for, so that a crew that has to improvise — a site with no open sky, a route that cannot be
driven straight for 20 m — knows which part of the sequence they are trading away.

## 13.1 The sequence Trimble documents

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, pp.13–14; MX60 UG Rev B)*
>
> 1. **Park in an open-sky area** with good GNSS visibility and PDOP, avoiding high buildings and
>    obstructions
> 2. Start the mission in TMI
> 3. **Log 2–3 minutes of static data** before driving
> 4. **Drive straight ahead for approximately 20 m**, with no larger dynamic steering. The
>    navigation status switches on completing this
> 5. **Drive straight at varying speed** — accelerate then decelerate — **and perform dynamic
>    steering manoeuvres.** An example profile: **0 → 50 → 20 → 50 → 20 km/h**
> 6. Navigation status progresses **red → orange → green**. Green means the user accuracies for
>    the navigation system are met
> 7. **Allow up to 10 further minutes of settling before logging data that matters**

> **IMPORTANT**
>
> **Navigation alignment must be completed before data logging is allowed** *(MX60 QSG Rev B)*.
> The system enforces this — it is not a matter of operator discipline. What is **not** enforced
> is step 7.

## 13.2 What the static period does

Two separate things, and both are worth knowing because they fail differently.

**It lets the GNSS receiver resolve a clean solution.** A continuous set of observations from a
stationary antenna under open sky is the best conditions the receiver will see all day.

**It gives the inertial filter a constraint it can exploit: the vehicle's true velocity is zero.**
Anything the motion sensors report while parked is therefore **pure error** — measurable, and
removable. This is how the filter gets its first estimate of the gyro and accelerometer biases,
which it then carries forward through the whole mission (§8.2).

> **WHY THIS MATTERS**
>
> A static period under tree cover satisfies the clock and not the physics. The zero-velocity
> constraint still applies, so some of the benefit survives; the GNSS half does not. If open sky
> is genuinely unavailable at the start point, the honest response is to drive to open sky
> *before* starting the mission, not to start it where the vehicle happens to be parked.

## 13.3 What the manoeuvres do

At constant velocity in a straight line, a small attitude error and a sensor bias produce **the
same signature** in the observations. The filter cannot separate them, because nothing in the
data distinguishes them. Change speed and change direction and they stop looking alike — the two
quantities affect the observations differently under acceleration — so the filter can tell them
apart.

| Manoeuvre | What it makes observable |
|---|---|
| **Straight run, ~20 m** | Initial heading from the direction of travel. This is the step the navigation status is waiting on |
| **Varying speed** | Along-track accelerometer bias, and the separation of bias from pitch |
| **Dynamic steering** | **Heading** — the hardest component, and the reason the turns exist |

Heading is the hardest attitude component for the reason given in §9.1: gravity anchors roll and
pitch, and nothing anchors heading. The manoeuvres are how a system without GAMS obtains it, and
they still help a system with GAMS.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, p.12; MX60 UG Rev B, p.67)*
>
> **Straight driving is more important if a GAMS antenna is not used.** GAMS reduces
> initialization time and eliminates the special driving manoeuvres otherwise required.

> Perform the full sequence either way. It costs a few minutes, the static period is doing work
> that GAMS does not replace, and whether this system has GAMS is not yet established (**D-2**,
> §7.7).

## 13.4 Why green is not finished

> **IMPORTANT**
>
> **Green means the solution met the accuracy thresholds — not that it has finished converging.**
> That is why Trimble asks for up to ten more minutes before recording anything that matters
> *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day.** Do not spend it
> on the most important part of the corridor.

This is the one part of the sequence the system does not enforce, which makes it the one part
that gets skipped. It is also the part that costs nothing but patience.

> **WHY THIS MATTERS**
>
> There is a natural but wrong mental model in which the status light is a pass/fail gate: red
> means not ready, green means ready, and the moment it turns green the system is as good as it
> is going to get. What is actually happening is that an estimate is converging, and the threshold
> was crossed somewhere on the way. Ten minutes later the same estimate is better. The light does
> not change again, so nothing tells you.

## 13.5 What a weak initialization costs, and where it shows

A weak initialization does not produce an obviously bad dataset. It produces one where the
attitude solution is carrying more error than it should, everywhere, and §3.1 says that error
acts through range — so it is worst on the features furthest from the vehicle, which are often
the ones the client cares about.

It also cannot be repaired in the office in any general way:

| Remedy | Does it help? |
|---|---|
| Reprocessing the trajectory | Only if better base data or corrections are available. The observation geometry is what it is |
| LiDAR QC | Possibly — it solves boresight angles and corrects the trajectory using scan overlap (§11) |
| Registration | It will fit the control it is given, absorbing some of the error at the control and leaving it between (§21) |
| Re-collection | Always works. Costs a mobilisation |

> **This is the asymmetry from §5.5 in its most concrete form.** Five minutes at the start of the
> mission, or a decision later about how much residual error to accept in a deliverable.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We took the start-of-mission routine apart and said what each piece is
> for: the two or three minutes parked, the straight run, the speed changes, the turns, and the
> ten minutes of patience after the light goes green.
>
> **Why it matters.** The system is not warming up. It is solving for things it cannot see any
> other way. Parked, it knows its true speed is zero, so everything the motion sensors report is
> error it can measure and subtract. Driving straight at a steady speed, an attitude error and a
> sensor bias look exactly alike — it is only when you speed up, slow down and turn that the two
> stop resembling each other and the filter can separate them.
>
> **What can go wrong.** Green gets read as finished. It is not: green means the estimate crossed
> a threshold on its way to converging, and ten minutes later it is better. Nothing tells you
> that, because the light does not change again. So the first data after the light goes green is
> the weakest data of the day, and if that is where the important part of the corridor is, that is
> where the weakest data ends up.
>
> **What good looks like.** Open sky, the full sequence performed even if GAMS is fitted, and the
> first ten minutes spent on something that does not matter much — a drive to the site, a
> throwaway pass, the least critical end of the corridor. It costs five minutes and there is no
> office procedure that buys it back.

---

# 14. Why the Closing Sequence Exists

The closing sequence is the most commonly skipped step in mobile mapping. It takes about five
minutes, it cannot be added afterwards, and it is the cheapest quality improvement available in
the entire workflow. This section explains why it exists at all, because a crew that understands
the reason will not skip it and a crew that does not will skip it every time it is raining.

## 14.1 The reason: the trajectory is computed twice

For survey work the navigation filter is run **forward through time and backward through time**,
and the two passes are merged into the SBET (§8.3).

```
   forward pass    ──────────────────────────────────────►
                   good data       GAP        good data
   backward pass   ◄──────────────────────────────────────
                                    ▲
                   bridged from both sides — short, well constrained


   forward pass    ──────────────────────────────────────►
                   good data                      GAP    ✗ end of mission
   backward pass   ◄──────────────────────────────────────
                                                   ▲
                   nothing on this side — the smoother has one anchor, not two
```

A degraded stretch in the **middle** of a mission is bracketed by good data on both sides. The
smoother bridges it from both directions, and the two estimates constrain each other.

A degraded stretch at the **end** has good data on one side only. The forward pass arrives there
already carrying whatever error it accumulated, and there is no backward pass to meet it. The
same is true in reverse at the start of the mission, which is what initialization addresses
(§13).

> **The closing sequence is the reverse pass's anchor.** Without it, the backward pass begins
> from the system's least converged state and propagates that weakness into the end of the
> mission — which is exactly where the smoother has nothing to compensate with.

## 14.2 The sequence

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, p.13; MX60 UG Rev B)*
>
> 1. Finish the last run
> 2. Drive to an open-sky location
> 3. **Dynamic steering manoeuvres**
> 4. **Vary the speed**
> 5. **Drive straight**
> 6. **Remain stationary for 2–3 minutes**, logging static data
> 7. Close the mission in TMI
> 8. Wait for the Control Unit power button light to go out — **up to 90 seconds**

> **Steps 3–6 are the initialization sequence run in reverse order** *(MX60 QSG Rev B, p.13)* —
> manoeuvres, then speed variation, then straight, then static, where the start was static,
> straight, speed variation, manoeuvres (§13.1). That is not a coincidence or a mnemonic. The
> backward pass runs through the data in reverse, so what it encounters first is what the forward
> pass encountered last, and the sequence is arranged so that the backward pass meets the same
> conditioning the forward pass was given.

> **IMPORTANT**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and *then*
> driving to open sky achieves nothing. The manoeuvres have to be inside the logged data to be of
> any use to the smoother.

## 14.3 Why it cannot be added later

There is no office operation that supplies what the closing sequence supplies. The remedies in
§27 all act on data that exists:

| Remedy | Why it does not substitute |
|---|---|
| Reprocess the trajectory | Reprocesses the same observations. The end of the mission is still unconstrained |
| Better base station data | Improves the GNSS side where GNSS was observed. It was not observed after the mission closed |
| LiDAR QC | Needs overlapping scan data at the location concerned (§11) |
| PFIX or registration | Fits the trajectory to surveyed control. Real, but it costs surveyed control at the end of every corridor, and it acts on the fit rather than the solution (§8.5) |

> **CAUTION · W-09**
>
> The post-processed trajectory is computed **forward and backward** and merged. A degraded stretch
> mid-mission is bracketed by good data on both sides. **A degraded stretch at the end has good
> data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

Once the mission is closed the opportunity is gone, and the data at the end of the mission is
permanently weaker than it needed to be. A crew that returns to site the next day cannot append it
— a new mission is a new trajectory.

## 14.4 Where the weakness shows up

The end of a mission is not an abstract place. It is a specific stretch of corridor, and it is
often a significant one, because crews naturally finish where the work finishes.

Three practical consequences, all of them reasons to look at the trajectory before the point
cloud (§24):

- **A check point near each end of the delivered extent is worth more than one in the middle**,
  because the ends are where the smoother had one anchor rather than two (§22)
- **A Local registration stops adjusting at the outermost control point** (§21), so the end of a
  corridor is simultaneously the weakest trajectory and the place registration helps least unless
  control brackets it
- **RMS colouring shows the degradation at the ends directly** — if the last stretch of the
  trajectory is a different colour from the rest, that is the closing sequence talking

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We explained why the end of a mission gets its own five-minute routine,
> and why that routine is the start-of-mission routine performed backwards.
>
> **Why it matters.** The trajectory is computed twice, once forwards through time and once
> backwards, and then the two are blended. Anywhere in the middle of the drive, a bad patch has
> good data on both sides of it and the two passes meet in the middle. At the very end of the
> drive there is no "other side" — the forward pass arrives carrying whatever error it picked up,
> and nothing is coming the other way to correct it. The closing sequence gives the backward pass
> something solid to start from.
>
> **What can go wrong.** Two things, and both are ordinary human behaviour. The crew finishes the
> last run, closes the mission, and then drives to somewhere convenient — but logging stopped when
> the mission closed, so the drive contributed nothing. Or it is raining, the work is done, and
> five minutes of driving in circles feels like nonsense. It is not recoverable afterwards. There
> is no office procedure that buys it back.
>
> **What good looks like.** Finish the last run, drive out to open sky with the mission still
> running, do the turns, vary the speed, drive straight, park for two or three minutes, and only
> then close the mission and wait for the light to go out. Then look at the trajectory's RMS
> colouring in the office: if the last stretch is the same colour as the rest of the job, the
> closing sequence did its job.

---

# 15. GNSS Environment and Outage Duration

## 15.1 Duration, not length

The quantity that determines how much a GNSS-hostile stretch costs is **how long the vehicle is
inside it**, not how long it is on the map. The inertial solution drifts as a function of time.

> A 300 m tunnel at 80 km/h is **13 seconds**. The same tunnel at 20 km/h in traffic is nearly a
> **minute**. Same tunnel, materially different problem.

This has a planning consequence that is easy to miss: a hostile stretch in congested traffic is
worse than the same stretch on a clear road, and neither the route length nor the aerial imagery
shows it. The time of day is part of the GNSS assessment.

## 15.2 The 60-second boundary in the specification

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.56)*
>
> Trimble publishes positioning performance at **no outage** and after a **60-second GNSS
> outage**, and nothing in between or beyond:
>
> | Condition | Core / Pro | **Premium — ours** |
> |---|---|---|
> | **No outage** *(all configurations, post-processed with POSPac, with the DMI option)* | X,Y < 0.01 m · Z 0.01 m | X,Y < 0.01 m · Z 0.01 m |
> | **After 60 s GNSS outage** | X,Y **0.12 m** · Z **0.1 m** | X,Y **0.1 m** · Z **0.07 m** |
>
> **Ours is the Premium column: X,Y 0.1 m and Z 0.07 m after a minute of outage.**

Two things in that table are worth dwelling on.

**The no-outage figure is stated with the DMI option.** The configuration is established —
Premium — but **the DMI is not**. The published best-case accuracy assumes a sensor this system
may or may not carry (§9.2, **D-2**). Until that is answered, the sub-centimetre figure is not
one to quote.

**One minute of outage costs an order of magnitude.** Under 1 cm becomes 10–12 cm. That is not a
gentle degradation; it is the difference between a survey-grade deliverable and something else.

> **IMPORTANT**
>
> **Trimble publishes nothing beyond 60 seconds.** A two-minute outage is not "twice as bad as one
> minute" — inertial drift is not linear in time, and beyond the published figure you are
> extrapolating past the manufacturer's stated envelope.
>
> Treat outages materially longer than 60 seconds as a **planning** problem, not a driving
> problem: additional control, planned overlap for LiDAR QC, a DMI if one is available, or a
> different acquisition method for that segment (§27.7).

## 15.3 The environments, and what each does

| Environment | What happens | Typical duration |
|---|---|---|
| **Tunnel, long underpass** | Total loss. The solution is purely inertial | Computable from length and speed |
| **Urban canyon** | Not loss but **multipath** — reflected signals producing plausible, wrong ranges | Sustained over the whole stretch |
| **Heavy canopy** | Intermittent loss and re-acquisition, with poor geometry between | Sustained, and worse when wet |
| **Deep cut, retaining walls** | Reduced sky, degraded geometry, high PDOP | Sustained |
| **Overhead structures, sign gantries** | Brief interruptions | Seconds |

> **Urban canyon is the one that misleads.** A total outage is honest: the filter knows GNSS is
> absent and propagates inertially, and the RMS record says so. Multipath supplies *observations*
> that are wrong, and the filter has no way to know they are wrong. The TBC **Multipath** setting
> exists to tell it how much to distrust them (§17.3), and the appropriate setting for Parametrix's
> normal environments is untested (**T11**).

## 15.4 What can be known before mobilising

Satellite geometry is predictable. The route is known. Both of the things that determine GNSS
quality are therefore knowable in advance, which makes a poor window an avoidable problem rather
than a discovered one.

| Knowable in advance | How |
|---|---|
| Satellite geometry and PDOP through the window | Almanac |
| Which stretches are hostile, and roughly how hostile | Aerial and street-level imagery |
| How long the vehicle will be in each | Length ÷ realistic speed, including traffic |
| Where initialization can be done | Imagery — and **scout two**, because a lot that is fenced, occupied or under trees costs twenty minutes at the worst moment of the day |

> **FIELD TESTING REQUIRED · T31**
>
> No Trimble source relates a *predicted* PDOP or canopy condition to an *achieved* trajectory
> RMS for this system. The relationship is establishable by driving a known route and comparing
> the prediction against the RMS colouring afterwards (§24), and it is the thing that would turn
> GNSS planning from judgement into estimate.

## 15.5 What it changes downstream

A GNSS assessment made before mobilising is not a formality; it determines four later decisions.

| Predicted degradation | Consequence |
|---|---|
| Where the solution will be weak | Where control is worth most, and where check points belong (§22) |
| How long each weak stretch is | Whether the smoother can bridge it, or whether a remedy is needed (§8.3, §27) |
| Whether overlap is available there | Whether LiDAR QC is even possible — it needs overlapping runs (§11.5) |
| Whether any segment is beyond remedy | Whether **mobile mapping is the appropriate acquisition method for that segment at all** (§27.7) |

> That last row is the one people avoid. It is easier to collect a corridor and discover the
> problem in the office than to say before mobilising that a particular 400 m of it should be
> collected another way. The office discovery costs a remobilisation and, sometimes, a conversation
> with the client about accuracy that nobody wants to have.

> **Open Parametrix decision — D-42.** *Base station strategy — own base on project control, VRS,
> RTX, or CORS post-processing, and at what maximum baseline?* This interacts with **D-19**
> (§12.3): **IN-Fusion+ Single Base** requires a local base station, **IN-Fusion+ PP-RTX** does not
> *(TBC 25943)*. The decision determines field logistics on every mission. Stated and tracked in
> the **SOP §8**; see also the master register.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at what the sky does to the job: which environments hurt, how
> much, and what Trimble actually publishes about it.
>
> **Why it matters.** The number that matters is seconds, not metres. The inertial sensor drifts
> with time, so a tunnel you pass through in thirteen seconds and the same tunnel crawled through
> in a minute are different problems. And the published numbers are stark: under a centimetre with
> good GNSS, ten to twelve centimetres after one minute without it. That is the whole range from a
> survey deliverable to something you would not hand over.
>
> **What can go wrong.** Extrapolating. Trimble publishes a figure at sixty seconds and stops
> there, and the temptation is to assume two minutes is twice as bad. Drift does not work that
> way, and past the published figure you are guessing on the manufacturer's behalf. The other trap
> is urban canyon: an outage at least tells the truth about itself, whereas multipath hands the
> filter wrong measurements that look like right ones.
>
> **What good looks like.** The hostile stretches were identified on imagery before anyone
> mobilised, each one has a duration estimate at a realistic speed for that time of day, and the
> segments that cannot be done well were named before collection rather than discovered after.
> Two initialization sites were scouted, not one.

---

# 16. What Determines Point Density and Useful Range

Two questions come up on every project — *how dense will the cloud be?* and *how far out is it
good for?* — and they have different answers from different parts of the system. Density is
geometry and settings. Useful range is trajectory quality.

## 16.1 The instrument's own numbers

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, pp.54–55)*
>
> | | Value |
> |---|---|
> | Laser pulse repetition rate, **per scanner** | **500 kHz / 1000 kHz** selectable |
> | Scan speed, profiles per second, **per scanner** | **120 Hz / 200 Hz** selectable |
> | Maximum measurement range | **150 m** at the lower rate · **120 m** at the higher rate |
> | Minimum range | **0.6 m** |
> | Range accuracy | **2 mm**, one sigma under test conditions |

> **CAUTION · two ways of quoting the same instrument**
>
> The MX60 specification sheet quotes **1000 / 2000 kHz** and **240 / 400** profiles per second.
> Those are **system totals across both scanners**. The User Guide figures above are **per
> scanner**, and TMI's own **Measurement Prog** and **Line Speed** settings use the per-scanner
> labelling *(`SPEC-004`, `SPEC-005`, `SPEC-011`; QSG-008, QSG-009)*.
>
> **Do not put the system-total figures into a field instruction.** A crew told to set 2000 kHz
> will not find it on the screen.

> **The higher rate costs range.** 1000 kHz per scanner gets 120 m; 500 kHz gets 150 m. That is a
> direct trade, made at the instrument, and it is the first of the three levers below.

## 16.2 The three levers on density

Point density along a corridor is set by three things, and only three:

| Lever | Effect | Where it is set |
|---|---|---|
| **Pulse repetition rate** | More pulses per second → more points, **at the cost of maximum range** | TMI, field |
| **Scan speed (profiles/s)** | More profiles per second → profiles closer together along the direction of travel | TMI, field |
| **Vehicle speed** | Slower → profiles closer together along the corridor | The driver |

Vehicle speed is the lever that changes most between projects and the one with the least
guidance attached to it.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B)*
>
> | | Value |
> |---|---|
> | **Recommended maximum with the system operating** | **80 km/h (50 mph)** |
> | Absolute maximum, operating or not | 110 km/h (68 mph) |

> **Open Parametrix decision — D-43.** *What collection speed, by deliverable type?* Trimble
> publishes a recommended maximum and an absolute maximum and **no guidance relating speed to
> deliverable quality**. Stated and tracked in the **SOP §9**; see also the master register.

Imagery follows the same logic on its own clock: the spherical camera captures at up to **10 fps**
and the down camera at up to **9 fps**, by distance or by time *(MX60 Spec Sheet, p.2)*. Capture
by distance decouples image spacing from vehicle speed; capture by time does not.

> **VENDOR CLARIFICATION REQUIRED · V-7**
>
> **Does the Lateral Range Limit affect accuracy, or is it purely a data-volume tool?** TMI offers
> a lateral range limit at acquisition. If it only discards returns beyond a distance, it is a file
> size control and nothing else. If it changes what the scanner does, it belongs in this section as
> a fourth lever. The documentation held does not say which. *(Appendix E)*

## 16.3 Geometry does more than settings

Two effects change density more than any setting, and neither is adjustable.

**Density falls with range.** The angular spacing between pulses is fixed, so the distance
between adjacent returns grows with range. A façade at 60 m is sampled far more coarsely than the
road surface at 6 m, on the same pass with the same settings.

**Density falls with incidence angle.** A surface hit obliquely is sampled across a stretched
footprint. Road markings ahead of and behind the vehicle are hit at a grazing angle, which is why
a painted stop-bar corner is a good horizontal target and a poor vertical one (§22.3).

> These two effects are why *a second pass in the opposite direction* improves a dataset more
> than any setting change: it converts grazing incidence into direct incidence and long range into
> short range for the far side of the corridor.

## 16.4 The range specification is a laboratory figure

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.55)*
>
> The maximum range figures apply to **flat targets larger than the beam diameter, at
> perpendicular incidence, with 23 km atmospheric visibility**. Range is **shorter in bright
> sunlight than under overcast**.

Every one of those conditions is optimistic relative to a corridor survey. Real targets are small,
oblique, and frequently wet or dark. The published maximum is the ceiling, not the working
distance.

## 16.5 Useful range is a different question, with a different answer

The scanner can return a point at 150 m. Whether that point is good enough to measure from is a
question about the **trajectory**, not the scanner.

From §3.1: an attitude error displaces a point by the range multiplied by the angular error in
radians. Range accuracy is 2 mm and does not change with distance. Attitude error does not change
with distance either — but its *effect* does, in direct proportion.

| | At 10 m | At 50 m | At 100 m |
|---|---|---|---|
| Range error contribution | 2 mm | 2 mm | 2 mm |
| Attitude error contribution | ×1 | ×5 | ×10 |

> **This is arithmetic, not a specification.** **No Trimble source in the set publishes an
> attitude error budget for the MX60 point cloud.** The published attitude figures — roll and
> pitch 0.005° Core/Pro and **0.0025° Premium, which is ours**, heading 0.015° with GAMS — the
> last of those conditional on a GAMS fitment not yet established *(MX60 UG Rev B, p.56)*. These are
> trajectory accuracies under stated conditions, not point cloud accuracies at range. Converting
> one into the other requires assumptions this manual does not make.

> **WHY THIS MATTERS**
>
> **Useful range is not a property of the instrument. It is a property of the job.** Two clouds
> collected on the same day with the same instrument and the same settings have different useful
> ranges if one was collected under open sky and the other in an urban canyon, because the
> attitude solution was better in one than the other. That is why there is no single number to
> publish, and why the honest answer to "how far out is this good for?" begins with looking at the
> trajectory RMS for that stretch (§24).

> **This is where D-13 comes from.** Because no attitude error budget is published, a useful range
> for a given tolerance cannot be derived from the documentation — so an acceptance criterion cannot
> be calculated either. It has to be **tested**, or **decided**. The decision Parametrix faces
> meanwhile is set out in the **SOP §17.2**; this manual does not propose an answer to it.

> **FIELD TESTING REQUIRED · T1**
>
> **Establishing a working useful range for Parametrix deliverables is a test, not a calculation.**
> Survey features conventionally at a spread of ranges from the vehicle path, collect over them
> under known GNSS conditions, and compare. The result would give a defensible range statement for
> each deliverable class — which is currently the largest gap between what this manual can say and
> what a project manager needs to promise a client.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We separated two questions that get asked as if they were one: how many
> points you get, and how far out you can trust them.
>
> **Why it matters.** Density you control — pulse rate, scan speed, how fast you drive. Faster
> pulses give more points but less range; driving slower puts the profiles closer together. None
> of that is subtle and all of it is decided before or during collection. Useful range is a
> different animal. The scanner will happily return a point at 150 m. Whether that point is where
> it says it is depends on how well the system knew which way it was pointing at that instant, and
> a pointing error acts through distance — the same error that is invisible at 10 m is ten times
> as large at 100 m.
>
> **What can go wrong.** Quoting the maximum range as if it were a working range. The published
> figure assumes flat targets bigger than the beam, hit square on, in clear air, and says range is
> shorter in bright sun. A wet oblique kerb line at 120 m is none of those things. The other trap
> is the specification sheet's system-total pulse rates, which are double the numbers the crew will
> see on the screen in TMI.
>
> **What good looks like.** Nobody promises a range figure without knowing what the trajectory was
> doing over that stretch. A second pass in the opposite direction, which fixes the far side of the
> corridor better than any setting will. And eventually a tested range statement per deliverable
> class, because right now that number is the biggest thing this manual cannot give you.

---


---

# Part IV — Processing, Explained

---


---

# 17. Trajectory Processing

This is where the accuracy of the whole dataset is decided. Everything after it either applies
the trajectory or improves it — nothing else creates it.

## 17.1 The three routes, and the licence that chooses between them

| Route | Where it runs | Requires |
|---|---|---|
| **POSPac MMS, externally** | A workstation with POSPac | A POSPac licence |
| **Process Raw Trajectory Data, inside TBC** | TBC | **POSPac MMS 8.6+ installed alongside TBC, with a valid licence** *(TBC 25943)* |
| **Real-time NAV** | Already computed in the vehicle | Nothing — but see the **Office How To** |

> **Both post-processing routes require POSPac.** TBC's in-application command is a convenience
> wrapper, not an alternative to owning the software. There is no route to a survey-grade
> trajectory that does not involve a POSPac licence somewhere.

> **Open Parametrix decision — D-10.** Stated and tracked in the **SOP §13**; see also the master register.

## 17.2 What Process Raw Trajectory Data does

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
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

## 17.3 Settings — with Trimble's stated defaults

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
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

> **Open Parametrix decision — D-19.** Stated and tracked in the **SOP §13**; see also the master register.

### The rest

| Setting | Values | Default |
|---|---|---|
| **Time Start / Time End** | GPS seconds of the start week | — |
| **Initialization Mode** | VNAV · **Gyro-compassing** · GAMS · GAMS and Gyro-Compassing | **Gyro-compassing** |
| **Multipath** | Low (good coverage) · **Medium** · High (urban canyon, narrow streets, dense foliage) | **Medium** |
| **Antenna Manufacturer / Type** | Read from the RINEX automatically | — |
| **GAMS** | On/off, with a lever arm and a standard deviation | Dimmed if GAMS was disabled during acquisition |
| **DMI** | Lever arm, standard deviation, scale factor, scale factor SD | Dimmed if DMI was disabled during acquisition |
| **LiDAR QC (Refine with scans)** | On/off | Off — see §11 |
| **Generate QC Report** | On/off | — |

### The MX60 antenna model — check this one

> **TRIMBLE DOCUMENTED METHOD**
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
| **Scale factor value** | From "the Trimble MX Distance Measuring Indicator Installation & Operation Manual, in the DMI Scale Factor section" — **a manual Parametrix does not hold** (§10.5) |
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

> **TRIMBLE DOCUMENTED METHOD**
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

## 17.4 Outputs, and a filename that means something

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
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
> trigger the ITRF00 path. This is answerable once and then known. *(Appendix E; §12)*

### Where the outputs go

| Output | Location |
|---|---|
| SBET | `NAVPROC/Export/` under the project folder |
| Processing report | `NAVPROC/Report/` |
| **Backup SBET Next to MXDB** *(option)* | Copies the SBET **and a log containing the frame and epoch information used to create it** into the raw data folder beside the `.mxdb` |

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-55); it is not decided here.

### The SBET is coloured by its own quality

> **TRIMBLE DOCUMENTED METHOD**
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
> That tells you where to concentrate control (§22), where to expect trouble at registration, and
> whether a degraded-GNSS remedy (§27) is going to be needed — while there is still time to do
> something about it.

> **OBSERVED SOFTWARE BEHAVIOR**
>
> A registered trajectory no longer matches its `smrmsg` file, so adjusted stretches lose their
> RMS colour and render as **Undefined RMS** *(TBC 27248)*. **§24 quotes the behaviour in full and
> makes a QC technique out of that side effect.**

## 17.5 Trajectory Plots

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 27415)*
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

## 17.6 Datum and epoch

§12 covers the coordinate system decisions. Two things belong here because they are specific to
trajectory processing.

**The ITRF00 path (§17.4)** is the practical expression of an epoch mismatch, and the filename is
its only symptom.

**Dynamic datum epoch selection**, added in TBC 2026.10:

> **TRIMBLE DOCUMENTED METHOD**
>
> "When working with a time-dependent datum, you can now work at a specific epoch that is not the
> default reference epoch for the selected datum… **Note that this feature is intended for
> experienced users, as incorrect settings may lead to inaccurate results.**" *(TBC RN 2026.10)*

> **Open Parametrix decision — D-21.** *Which datum and epoch does Parametrix work in for mobile mapping, and who sets it?* Stated and tracked in the **SOP §13**; see also the master register.

## 17.7 LiDAR QC

Trajectory processing can take the **scan data itself** as an additional aiding sensor, through
the **LiDAR QC (Refine with scans)** checkbox in this same dialog. It is a capability with a
substantial hardware requirement and its own acquisition geometry, and it is treated on its own in
**§11**.

---

> **IN PLAIN LANGUAGE**
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

# 18. Scan Generation

## 18.1 What it does

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
> the whole basis of registration (§21) and of Update Scans (§19).

### The MX60 has no MTA stage

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22503)*
>
> MX50 and MX60 convert **TMX → RWCX in one step**. MX9 and MX90 go RXP → TMX → RWCX in two, and
> the intermediate stage requires **MTA** (Multiple Times Around) range-ambiguity correction.

> **The MX60 workflow has no MTA configuration and no MTA failures.** If you encounter TBC
> documentation about configuring a GPU driver for MTA correction *(TBC 23856)*, it does not
> apply to this system. Mentioned because it is prominent in the TBC help and causes confusion.

## 18.2 Running it

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22499)*

Select a run or a mission in **Project Explorer** and choose **Generate Scans** from the context
menu. Scans appear beneath the trajectory node they were computed from.

Generating at mission level processes all runs. Generating at run level processes one — useful
when a single run has been re-collected or when testing filter settings before committing to a
full mission.

## 18.3 Filters

The Filters pane is where most of the judgement in this command lives, and where most of the
untested defaults are.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22499)*

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

> **FIELD TESTING REQUIRED · T1–T1**
>
> **The filter defaults are the largest block of untested settings in the workflow.** Each removes
> real returns under conditions that may or may not have occurred.
>
> **T1 — Default vs High Quality.** Trimble states what each preset contains and gives no
> selection criteria. High Quality enables three filters unconditionally, including on data
> collected in conditions where none of them applies.
>
> **T1 — Isolated Points.** Trimble's own text contradicts itself: the prose says the filter is
> on, the Restore Default Values behaviour says off.
>
> **T3 — Reflective Panels.** "Removes the noise before and after a target." **Does it also
> remove legitimate retro-reflective returns from signs and line marking?** This bears directly on
> sign inventory and retroreflectivity work, where those returns are the deliverable.
>
> **T1 — Range Max.** The MX60 default matches the scanner's maximum range at the lower pulse
> rate. The User Guide separately warns that real-world range is shorter in bright sunlight and at
> oblique incidence *(MX60 UG Rev B)*, so points may be retained well beyond useful range.
>
> **T1 — Fog and Sun.** Both remove real returns under defined conditions. Applying them when
> those conditions did not occur removes valid data.
>
> *(Appendix E)*

> **CAUTION**
>
> **Filtering is not reversible within a scan set.** A filtered return is not flagged, it is
> absent. Recovering it means regenerating the scans with different settings — which is cheap in
> effort and expensive in time on a large mission, and impossible once the raw data has been
> archived and the project cleaned up (§28).
>
> **Generate one representative run with the intended settings and look at the result before
> committing a whole mission.**

## 18.4 Colorization

Scans can be generated with colour from the imagery, or without.

> **TRIMBLE DOCUMENTED METHOD**
>
> Colour is exported "if the scans have been generated with the color option set to on"
> *(TBC 23339, 22501)* — so the decision made here propagates all the way to the deliverable.

> **FIELD TESTING REQUIRED · T6**
>
> The colouriser offers a forward versus backward camera preference with no stated selection rule.
> *(Appendix E)*

> **Open Parametrix decision — D-22.** Stated and tracked in the **SOP §13**; see also the master register.

## 18.5 The Results record

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22499)*
>
> A **Results of Scan Generation** dialog records, per run: the **filters applied**, the **range**,
> and whether **colorization** was on.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-55); it is not decided here.

## 18.6 Recovering failed scans

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 28155)*
>
> **Recover Mobile Mapping Scans** exists for scan generation that failed or was interrupted.
> Treated as a recovery procedure in §26.

## 18.7 A hazard that lives in §29 but starts here

> **CAUTION · cross-reference to §29.3**
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
> **FIELD TESTING REQUIRED · T18 — the highest-priority test in this document.** See §29.3 and
> Appendix E.

---

> **IN PLAIN LANGUAGE**
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

# 19. Update Scans — Why Registration Does Not Move Points

Registration produces a **new trajectory**. The point cloud is untouched until this
command is run. That separation is the single most consequential sequencing fact in the
office workflow, and it is why Update Scans has a section of its own.

## 19.1 What it does

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22638)*

**Update Scans** regenerates scans against a different trajectory. It is how a registration (§21)
reaches the point cloud.

| | **Generate Scans** | **Update Scans** |
|---|---|---|
| Purpose | Create scans from raw data | **Switch existing scans to a different trajectory** |
| Filters pane | Yes | **No** |
| Trajectory choice | The run's current trajectory | **Switches between the imported trajectory and an adjusted one** |

Updated scan stations carry a **`_reg_####`** suffix — for example
`Run_14_Laser Right_reg_0001 (S3)`.

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**
>
> This is the most consequential sequencing fact in the office workflow, and the mistake it
> guards against is invisible: the project contains a registration, the residuals were good, the
> processor moved on — and the delivered cloud never received the adjustment.

Update Scans works in **both directions**: it switches between imported and adjusted, so it is
also the mechanism for reverting.

> **The exception.** **Register Run to Run** has an **Update Scans** checkbox inside the command,
> which regenerates the Run to Adjust's scans inline *(TBC 25096; §21.14)*. That is the only place
> where the two steps merge.


---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We took a point cloud that had been built on one version of the vehicle's
> path and rebuilt it on a better one. Nothing else in the software does this, and nothing does it
> automatically.
>
> **Why it matters.** Registering a mission improves the *path*. It leaves the points exactly
> where they were. If you stop after registering, the project contains a perfectly good adjustment
> and a point cloud that never received it — and the two look identical in every view.
>
> **What can go wrong.** The failure is silent and it is common: register, read good residuals,
> accept the result, export. The file opens, the extents are right, the residuals in your notes
> were fine, and the client has the version from before the adjustment. Nothing warns you at any
> point in that sequence.
>
> **What good looks like.** After Update Scans the scans sit beneath the registered trajectory in
> Project Explorer and their stations carry a `_reg_####` suffix. If you cannot see that suffix,
> the adjustment has not reached the data. **For the required check before export, see SOP §19;
> for how to verify it, see Office How To §21.**

---

# 20. Calibration

## 20.1 Why this section sits here

Calibration is **periodic, not per-project.** It belongs to the system, not to the job, and most
missions will not involve it at all.

It appears here, between scan generation and registration, for two reasons: TBC's calibration
procedures **consume generated scans** as their input, so it cannot be explained before §18; and
a reader meeting registration in §21 needs to already know what a boresight angle is.

> **Calibration and registration are different things and are easy to confuse.** Calibration
> determines the fixed angular relationship **between sensors on the vehicle**, and is valid for
> months. Registration ties a **particular mission's trajectory** to surveyed control, and is
> valid for that mission only. A current calibration does not reduce the control requirement, and
> a good registration does not indicate the calibration is sound.

## 20.2 What is calibrated, and what is not

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886, 24868)*
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
pointing**, and it displaces points **in proportion to range** — exactly as described in §3.

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

## 20.3 Calibrating the laser scanners

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886; also documented at TBC 20716)*

### Where it runs

"In TBC, up to the 5.21 version, laser scanners are calibrated out of the application and the
calibration values are imported into TBC from a JSON format file. The **Calibrate Laser
Scanners** feature allows you to calibrate the laser scanners of the MX series mobile mapping
systems in TBC."

> Version 5.21 predates 5.70, the oldest release Trimble still publishes notes for (§10.2). **Any
> recent TBC calibrates in the application.** The JSON import path (§20.5) remains available and
> is how a calibration moves between projects.

### The acquisition geometry

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886 / 20716)*
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

Compare with the LiDAR QC pattern *(TBC 28972; §11)*:

| | Laser scanner calibration *(TBC 24886)* | LiDAR QC *(TBC 28972)* |
|---|---|---|
| Runs | Four — two orthogonal pairs, both directions | Four — two perpendicular strips, both directions |
| Crossing angle | **90°, ± 30°** | Perpendicular |
| Length | **≥ 20 m each side; ideally 80 m total** | **250–300 m per strip** |
| Scene | **Façades in each direction; little or no vegetation** | Structured — "a residential area with detached houses and objects within the LiDAR sensor's maximum range" |
| Sky | Not stated | **Open sky for good GNSS satellite visibility** |

> **The two are compatible, and LiDAR QC is the stricter on length.** A site of two roads crossing
> near 90°, with 125–150 m of façade-lined street available on each arm, satisfies both.
>
> ⚠ **One assumption is being made and should be stated.** Trimble specifies the laser scanner
> pattern as two roads **crossing**, and specifies the LiDAR QC pattern as two **perpendicular
> strips** without saying the strips intersect. Treating a LiDAR QC strip as centred on the
> crossing — and therefore needing half its length on each arm — is this document's reading, not
> Trimble's statement. It is the conservative reading: a site meeting it also meets any
> non-intersecting arrangement of the same total length.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §15** (D-24); it is not decided here.

### The result, and how to read it

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886)*
>
> The calibration reports:
>
> - **Overall Overlap** — the percentage of points used against those generated
> - **Overall RMS** — the average of the RMS between the scans used
> - **Per-pair RMS**, in **Tangential, Orthogonal and Vertical**

The same three-axis convention as run-to-run registration (§21.15), and it diagnoses the same way:
a large tangential component points at along-track scale or timing, a large orthogonal component
at heading, a large vertical component at pitch or height.

### The rule that governs acceptance

> **TRIMBLE DOCUMENTED METHOD**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886)*

> **This is the origin of the principle that governs §21, §23 and §25**, and of the QC
> requirements in the **SOP §16**. Trimble states it here and repeats it verbatim in the
> run-to-run registration topic. It is not a hedge — it
> follows from what a residual measures. **A number can prove failure. A number cannot prove
> success.**

### The visual check

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24886)*
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

## 20.4 Calibrating the cameras

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24868, 20728)*

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

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24868)*
>
> In the camera properties, as **Boresight refinement** — distinct from **Boresight
> installation**, which is the as-built value. Lever arm installation and lever arm refinement
> appear alongside, and are equal, because lever arms are not estimated (§20.2).

## 20.5 The calibration file

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22920)*
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

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §15** (D-55); it is not decided here.

## 20.6 The calibration record — and the date

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24868)*
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
> property and it costs one report to capture (§30).

## 20.7 When to recalibrate

> **Open Parametrix decision — D-26, D-3.** *On what interval, and after what events, is the MX60 recalibrated?* Stated and tracked in the **SOP §15**; see also the master register.

> **VENDOR CLARIFICATION REQUIRED · V-13**
>
> **Does removing and refitting the Sensor Unit disturb the calibration?** And what symptoms
> indicate a calibration has drifted? *(Appendix E)*

## 20.8 Calibration is not validated by control

A warning against a natural but wrong inference.

TBC's laser scanner calibration derives boresight angles from **scan-to-scan agreement**. No
surveyed control participates. A calibration can therefore be internally excellent and carry a
systematic error common to all four runs.

The independent check on calibration is the periodic target verification in §31 — retro-
reflective targets previously surveyed by total station — which is a different activity with a
different geometry, and one Parametrix has not yet scheduled.

---

> **IN PLAIN LANGUAGE**
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

# 21. Registration

This is the section the rest of the office workflow exists to support. Read §2 and §18 first.

## 21.1 What registration is, in this system

**Registration adjusts the trajectory.** It does not move points.

TBC takes surveyed ground control points, pairs each with a point the operator picks in the
point cloud, and computes a correction to the trajectory that reduces the difference between
the pairs. The output is a **new trajectory**, stored beside the imported one. The existing
point cloud is untouched until you deliberately recompute it (§19).

> **This is the single most important structural fact about TBC registration, and it surprises
> people from a static scanning background.** In static work, registration moves scans. Here it
> produces a better path, and the points follow only when you ask them to.

### The three commands

They are **not interchangeable**. Each solves a different problem with a different kind of
observation.

| Command | What constrains it | Scope | Section |
|---|---|---|---|
| **Register a Run** | Surveyed GCPs ↔ targets picked in the cloud | One run | §21.3 |
| **Register a Mission** | The same, with each GCP reusable across runs and passes | A set of runs at once | §21.4 |
| **Register Run to Run** | **Cloud-to-cloud overlap** against a fixed reference run | Pairs, batched | **§21.10** |

> **IMPORTANT**
>
> Register Run to Run uses **no surveyed control at all**. It makes two runs agree with each
> other. Two runs can agree perfectly and both be in the wrong place. It is a relative tool, and
> §21.10 explains where it belongs in a controlled workflow.

## 21.2 What TBC means by "target"

> **TRIMBLE DOCUMENTED METHOD**
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
> This shapes control design (§22.5). A GCP for mobile mapping registration has to be something you
> can *find in a point cloud* at the density and incidence angle the vehicle produced — which is
> a different requirement from something you can occupy with a prism. A painted stop-bar corner
> is excellent. A survey nail in asphalt is nearly useless: it is a few millimetres across, and
> the cloud will not resolve it.

## 21.3 Register a Run

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*

### Prerequisites

- **At least one generated scan on the run.** The command is dimmed otherwise
- **A GCP file imported into the project** — Shape, ASCII or CSV. Imported points appear in Plan
  View and under the **Points** node

### The sequence

1. In **Project Explorer**, select a run
2. Generate its scans if not already done (§18)
3. Import the GCP file
4. **Mobile Mapping ▸ Processing ▸ Register a Run**
5. Accept the default **Registration Name** (*RunName* Trajectory) or enter one. **This name is
   given to the computed trajectory** — it is what you will be identifying months later (§30)
6. Choose a **Registration Type** (§21.5)
7. Select a GCP under the **Points** node and click **Add Selection to Control Points**
8. Set **Use XY**, **Use Z**, **As Check** for that point (§22)
9. Optionally enable **Activate Limit Box** — a flat box in Plan View or a 3D box in 3D View that
   hides everything outside it, "to remove potential parasitic points over the target"
10. Optionally set **Activate Target-Bundle Adjustment** (§21.7)
11. Select the point in the **Control Points** list. It centres in Plan View and **Point Cloud
    Smart Picking** opens
12. Pick the target, read the residuals, and **Validate** (§21.6)
13. Repeat for further points, or adjust an existing pick
14. **Compute**. The adjusted trajectory draws in **blue**; the original stays **green**
15. Add or modify pairs and recompute as needed
16. **Apply**

### What Apply produces

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*
>
> - An **adjusted trajectory node** nested beneath the run, beside `Sbet`
> - A new **SBET file on disk**: `sbet_<date>_reg_####.out`, in the project folder,
>   **incrementing** with each registration — `_reg_0001`, `_reg_0002`, and so on
> - Picked targets renamed *RunName TrajectoryGCPName*; the updated targets carry a trailing `*`
> - Trajectory properties carrying **`Origin: Registration result`**, **`Input trajectory:
>   Imported trajectory`**, and **`Registration type:`** the method used

> **Those four properties and the numbered SBET file are your provenance record.** They are the
> strongest evidence available that a given point cloud was built on a given adjustment. §30 is
> about how far that evidence travels — and it does not travel as far as you would like.

### A note for single-scanner acquisition

> **TRIMBLE DOCUMENTED METHOD**
>
> "In case of a single head configuration (one high-end laser scanner acquisition), it does not
> matter which scan is used (left or right) for the registration." *(TBC 22905)*

## 21.4 Register a Mission

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 26473)*

Register a Mission registers "a set of runs at the same time" rather than sequentially, and —
this is the point of it — **lets every GCP be used more than once**, with different run point
clouds or different passes of the same run.

### How it differs from Register a Run

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs |
| GCP reuse | Once | **Every GCP, as many times as it appears** |
| Control list | One row per GCP | **One row per GCP `instance`** |
| Instances | — | TBC creates one per **250 m scan section** whose bounding box contains the GCP |
| Side | — | An instance binds to the **left, right, or both** sides of the scan section |
| Default name | *RunName* Trajectory | **Reg** |
| Target naming | `RunName TrajectoryGCPName` | `RegistrationName_GCPName_RunName` |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** |
| Unused instances | — | "All unused instances are removed from the Control Points list" |

### Why this is probably the normal case

Consider an ordinary corridor: driven in both directions, perhaps twice, with control set along
it. A single painted mark is visible in four passes. Under Register a Run it constrains one of
them. Under Register a Mission it constrains all four **simultaneously**, and the four runs come
out mutually consistent because they were adjusted against the same observation.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-12); it is not decided here.

## 21.5 Registration Type — and the one that does not extrapolate

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905, 26473)*

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
> 400 m unadjusted at the tails. §22.6 and §22 return to this.

> **FIELD TESTING REQUIRED · T15**
>
> **Which registration type, when?** Trimble describes the mechanism of each and gives no
> selection rule beyond "consistent differences." **Global, and then Local** receives no guidance
> at all, and is the method shown in every screenshot Trimble publishes.
>
> Do not adopt a default from the screenshots. Test the three methods on a representative
> corridor with independent check points and compare. *(Appendix E)*

## 21.6 Target picking, and reading residuals before you commit

This is where the operator's judgement enters the adjustment, and TBC gives real help.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*

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

> **TRIMBLE DOCUMENTED METHOD**
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
> a good illustration of why superseded scan sets are a hazard worth managing (§28, §30).

### The 30 m rule

> **TRIMBLE DOCUMENTED METHOD**
>
> "The distance in a pair of points cannot exceed the allowed maximum distance of **30 meters (or
> 100 feet)**." *(TBC 22905, 26473)*

A pair exceeding it is rejected. In practice this is a sanity limit, not a working tolerance — a
GCP and its picked target should be a few centimetres apart, not tens of metres. Hitting this
limit means the wrong feature was picked.

### Minimum observations

> **TRIMBLE DOCUMENTED METHOD**
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

> **CAUTION · W-06**
>
> If Registration Auto-Saving is on, picked targets are written to **`Targets.csv`**. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

> **FIELD TESTING REQUIRED · T7**
>
> **Is Registration Auto-Saving on by default?** The consequence of the reload prompt depends on
> it, and the answer is a glance at the dialog. *(Appendix E)*

## 21.7 Target-Bundle Adjustment — the option whose name reads backwards

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905, 26473)*

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

## 21.8 Editing a registration — not the same as registering again

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25362, 26578)*

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

## 21.9 Judging the result

Covered fully in §23, but the governing principle belongs here because it is where the temptation
to shortcut is greatest.

> **TRIMBLE DOCUMENTED METHOD**
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
> wrong. Only observations that took no part in the adjustment (§22) and a direct look at the
> data (§25) can distinguish the two.

> **Open Parametrix decision — D-13.** *What constitutes an acceptable registration at Parametrix?* Stated and tracked in the **SOP §13**; see also the master register.

---

## 21.10 Register Run to Run — the cloud-to-cloud path

## 21.11 What it is, and what it is not

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
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
> **absolute** accuracy. It cannot replace registration to control (§21), and a dataset that has
> only been run-to-run registered has not been tied to the ground at all.

## 21.12 Where it belongs

Run-to-run registration solves a specific problem: two passes down the same corridor that are
each individually acceptable against control, but that do not sit on top of each other.

That mismatch is real and visible — a doubled curb line, a wall with two faces 4 cm apart — and
it is the thing a client notices first in a delivered cloud. It arises because the two passes
were collected at different times with different GNSS conditions, and each carries its own
trajectory error.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-12); it is not decided here.

> **The choice of which run is the Reference is a survey decision, not a processing convenience.**
> Whatever the Reference Run's absolute error is, the Run to Adjust inherits it.

## 21.13 Prerequisites

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
>
> In a pair, the two runs need to have:
>
> - **At least one scan**, whatever the scan (left or right)
> - **Enough overlapping scan data** along the trajectories

### A useful exception

> **TRIMBLE DOCUMENTED METHOD**
>
> *"Missing TMX Files for 'Runname_X and Runname_X+1'" in the Status column means that no scan
> data has been generated… "Missing TMX files" does not prevent you from launching the Register
> Run to Run directly, and you do not need to generate the scans first, **TMX files will be
> generated on the fly**.* *(TBC 25096)*

This is the only registration command that does not require pre-generated scans. Every other one
is dimmed without them.

## 21.14 The sequence

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*

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
9. Set the **Update Scans** option (§21.15)
10. Check **Open Cutting Plane View** to inspect visually
11. **Compute**

### What Compute produces

- A new trajectory nested beneath the **Run to Adjust**, named
  `GivenName: Runname_X To Runname_X+1`
- **RMS statistics in the Results tab** (§21.16)
- If **Update Scans** was checked, new Scan nodes beneath the created trajectory
- A cutting plane named `MissionID Last Two Digits - Run to Adjust`, one per pair

## 21.15 Update Scans is an option inside this command

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
>
> - **Unchecked** — do not generate the scan data after the registration
> - **Checked** — generate the scan data for the **Run to Adjust** on the adjusted trajectory,
>   and enable the **Open Cutting Plane View** option

> **This is the one place in TBC where Update Scans is not a separate step.** Everywhere else,
> registration produces a trajectory and the cloud is recomputed later and deliberately (§19).
> Here it can happen inline.
>
> The consequence for provenance is worth noting: a run-to-run registration with Update Scans
> checked produces a new scan set immediately, and the previous scan set remains in the project.
> Which one is delivered becomes a question of which node is selected at export (§29, §30).

## 21.16 The result — and TBC's most informative QC output

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
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
trajectories" — the prerequisite in §21.13. The registration may still compute, on the few
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

## 21.17 The visual check

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*

Checking **Open Cutting Plane View** creates, per pair, a plane named
`MissionID Last Two Digits - Run to Adjust`, appearing as:

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

## 21.18 Improving a run-to-run result

> **TRIMBLE DOCUMENTED METHOD**
>
> "You can use the **Register a Run** command to improve the trajectory resulting from
> registering two runs together. The improvement can be done by editing the same (run_to_run)
> trajectory." *(TBC 25362)*

So a run-to-run result can subsequently be adjusted against surveyed control through Edit — which
supports the sequencing in §21.12, in reverse order, for situations where the relative fit was
addressed first.

---

> **IN PLAIN LANGUAGE**
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

> **IN PLAIN LANGUAGE**
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

# 22. GCPs, Check Points and Residuals

## 22.1 Why this section is separate

Every accuracy claim Parametrix makes about a mobile mapping deliverable rests on this section.

Registration (§21) is the mechanism. This section is about the **survey decision** underneath it:
which surveyed points participate in the adjustment, which are held back to measure it, and who
decides. TBC reduces that decision to three checkboxes, which makes it easy to make
inadvertently.

> A surveyor needs no explanation of why check points matter. What needs explaining is how TBC
> expresses the idea, and where its expression differs from the conventional one.

## 22.2 How control participates — three independent choices per point

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905, 26473)*
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

> **TRIMBLE DOCUMENTED METHOD**
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

## 22.3 Horizontal and vertical are separable, and usually should be considered separately

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

> **IMPORTANT · control cannot be added afterwards**
>
> A point can be surveyed at any time. It can only be *used* if the feature it marks is visible in
> data that was already collected — at the density and incidence angle the vehicle produced, on the
> pass that was driven. **You cannot go back and occupy a new point to strengthen a registration.**
>
> That reverses the usual order of work: on a corridor job the control design has to be right
> before the vehicle drives, not after the office has seen the residuals.

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** This is answerable empirically on a test site with a variety of
> features surveyed conventionally, and the answer will shape control design (§22.6) far more than
> any software setting. *(Appendix E)*

## 22.4 The independence requirement

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

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §7** (D-15, D-3); it is not decided here.

## 22.5 What makes a feature usable as a mobile mapping GCP

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*
>
> A **GCP** is "an accurately surveyed coordinate location for a physical feature that can be
> identified on the ground, e.g., **a corner on the pavement markings**." A **target** is "a point
> extracted from the acquired scan data."

> **IMPORTANT · this changes control design**
>
> A mobile mapping GCP must be **findable in a point cloud** at the density and incidence angle
> the vehicle produced. That is a different requirement from *occupiable with a prism*, and it is
> the requirement that governs.
>
> | Works well | Works poorly |
> |---|---|
> | Painted stop-bar and lane-line corners — crisp intensity edges | A survey nail in asphalt — a few millimetres across, below cloud resolution |
> | Checkerboard, diamond, rectangular and L-shape (GV) target panels, for which TBC has templates *(TBC 22905)* | Small features at grazing incidence (§21.12) |
> | Painted arrow and legend corners | Anything that moves, is repainted, or is worn |

A painted stop-bar corner is an excellent **horizontal** target and a poor **vertical** one: it
lies in the road surface, the scan hits it at a grazing angle, and the picked height depends on
which return the operator snapped to. TBC's per-component control (§22.2) exists precisely so that
a feature can be used for what it is good at.

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** Answerable on a test site with features surveyed conventionally,
> and the answer will shape control design more than any software setting.

## 22.6 How much control, and where

No Trimble source states a minimum, a spacing, or a ratio. TBC's software minimum is one control
pair — a mathematical floor with no bearing on survey adequacy (§28.6). What Trimble does give is
two indications of the **scale** at which control matters, and one hard constraint.

### The constraint: Local does not extrapolate

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*
>
> A **Local** registration is "suitable for a local adjustment of a run, **not for systematic error
> along the run or for adjusting outside the ground control points set**."

> **CAUTION · W-08**
>
> **Local does not extrapolate.** Beyond the outermost control point the trajectory is not
> adjusted, and nothing in the software indicates where the adjustment stopped. **Control must
> bracket the extent you intend to deliver, not merely fall within it.**
>
> The trajectory RMS colouring makes the boundary visible after the fact — adjusted segments render
> as *Undefined RMS* (§24) — but that is a check, not a substitute for designing the control layout
> correctly.

### The scale indication

**Target-Bundle Adjustment** operates at **250 m** intervals when checked and **70 m** when
unchecked *(TBC 22905; §28.7)*. That is Trimble's own indication of the scale at which control
density matters, and the two figures differ by more than a factor of three.

The second indication is §20.4: the ends of a mission are where the smoother had one anchor rather
than two, so control and checks at the ends are worth more than control in the middle.

> **Open Parametrix decision — D-16.** *How many control points, at what spacing, and how many held
> as independent checks?* Stated and tracked in the **SOP §7**; see also the master register.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §7** (D-16); it is not decided here.

> **EXTERNAL REFERENCE — NOT PARAMETRIX PROCEDURE**
>
> The Queensland TMR *Mobile Laser Scanning Technical Guideline* (March 2023, CC BY 4.0) is a
> published transport-agency specification in the source set. It defines survey-grade,
> engineering-grade and asset-grade tiers, and for its higher tiers specifies control adjacent to
> the start and end of the project and at intersections of controlled roads *(TMR §11)*.
>
> **It is cited as an example of how another agency has answered D-16 — not as a Parametrix
> standard and not as a Trimble requirement.** Parametrix's own accuracy tiers, if it sets any,
> are D-16.

## 22.7 What TBC reports, and what it does not

> **TRIMBLE DOCUMENTED METHOD**
>
> Per pick, live in the **Validate Picking** window and in the **Targets** pane: **Easting
> residual**, **Northing residual**, **Elevation residual**, "with their corresponding directional
> signs" *(TBC 22905)*.
>
> From TBC 2025.21: those residuals "are now **signed** and included in **the report**"
> *(TBC RN 2025.21)*.

> **VENDOR CLARIFICATION REQUIRED · V-11**
>
> **Which report?** The 2025.21 release note says the signed residuals are included in "the
> report" without naming it. The only mobile mapping report topic — *Run a Mission Report*
> *(TBC 23991_1)* — describes the report as showing "capture devices, runs, trajectories and
> generated scans" and **does not mention residuals at all**.
>
> This matters because the residuals on check points are the primary numerical evidence in the
> accuracy statement, and whether they can be produced as a report — rather than transcribed by
> hand from a dialog — determines how the record is kept (§30, and the **SOP §21**). *(Appendix E)*

> **FIELD TESTING REQUIRED · T21**
>
> Register a mission, run a Mission Report, and look. This is answerable in ten minutes with the
> software in front of you. *(Appendix E)*

### What TBC does not report

❌ TBC does not produce, in any captured topic, a statement of **which points were used as
control and which as checks** in a registration that has already been applied. The Use XY / Use Z
/ As Check state is visible while the command is open and reloaded by **Edit** *(TBC 25362,
26578)* — but no report of it has been found.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §7** (D-29); it is not decided here.

## 22.8 Control for calibration is a different thing

A brief warning against a natural confusion.

The calibration procedures in §20 use a specific **run geometry** — four runs, two orthogonal
pairs, each driven in both directions, 250–300 m per strip *(TBC 24886, 28972)* — and derive
boresight angles from **scan-to-scan agreement**, not from control. Surveyed control plays no
part in TBC's laser scanner calibration.

Control and check points are for registration. They do not validate a calibration, and a
calibration does not substitute for them.

---

> **IN PLAIN LANGUAGE**
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

# 23. RMS and What It Can Prove

## 23.1 The governing principle

> **TRIMBLE DOCUMENTED METHOD**
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
> (§22), and **looking at the data** (§25.1).

## 23.2 What TBC gives you, at four levels

| Level | Indicator | Where | Source |
|---|---|---|---|
| **Per pick, live** | Easting, Northing, Elevation residual to the GCP, signed; **RMS of the fitted plane** | Validate Picking, Targets pane | *(TBC 22905)* |
| **Per run pair, every 20 m** | RMS in **Tangential, Orthogonal, Vertical**; `No overlap` where absent | Results tab, Register Run to Run | *(TBC 25096)* |
| **Whole calibration** | Overall Overlap %, Overall RMS, per-pair RMS in three axes | Calibrate Laser Scanners | *(TBC 24886)* |
| **Trajectory-wide** | Position, orientation and velocity RMS after smoothing, from `smrmsg_xxx.out` — rendered as **trajectory colour** | Plan View | *(TBC 25943, 27248)* |

Plus the visual check (§25.1) and the records in the **SOP §20**.

> **Note what is missing from that table: a single number that describes the quality of a
> registration.** There is no registration report equivalent to a least-squares adjustment
> summary. The evidence is distributed across a dialog, a results tab, a trajectory colour and
> the operator's eyes — which is why §30, the provenance problem, matters more here than it would
> in a conventional adjustment, and why the records the **SOP §20** requires are not a formality.

## 23.3 Reading the three axes

Tangential, orthogonal and vertical appear in both calibration and run-to-run registration. They
diagnose, not just describe.

| Dominant component | What it points at |
|---|---|
| **Tangential** — along travel | Timing, or along-track scale. Check the DMI scale factor (§17.3) and the time synchronisation |
| **Orthogonal** — across travel, horizontal | Heading. The hardest attitude component, and the one a single direction of travel cannot resolve (§20.3) |
| **Vertical** | Pitch, or the height component of the trajectory. Check the antenna model (§17.3) and the geoid |

> **WHY THIS MATTERS**
>
> A combined RMS hides this. Three numbers of similar size mean random disagreement, which is
> what good data looks like. One number much larger than the other two means a specific,
> identifiable part of the solution is struggling — and tells you where to look rather than
> leaving you to regenerate everything and hope.


---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at what a residual actually measures, and why Trimble says —
> twice, in two unrelated parts of its documentation — that a good RMS does not prove the work
> succeeded although a bad one proves it failed.
>
> **Why it matters.** A residual tells you how well the adjustment fitted the numbers you handed
> it. That is a narrower question than the one you care about. Hand it three points and it fits
> them perfectly, because with three observations and three unknowns there is nothing left over to
> disagree. Hand it three points that share a common error — a mis-keyed coordinate, a control
> network with a systematic bias — and it fits those perfectly too, and passes the error straight
> through into the deliverable. The arithmetic is not lying. It is answering the question it was
> asked.
>
> **What can go wrong.** Reporting a small residual as evidence of accuracy. It is evidence that
> the adjustment is internally consistent, which is a different claim and a much weaker one. The
> failure is most likely on a job with sparse control, because that is exactly where the residuals
> look best.
>
> **What good looks like.** Two things the numbers cannot give you on their own: residuals on
> points the adjustment never saw (§22), and a direct look at the data (§25). Where the three-axis
> breakdown is available, three components of similar size means random disagreement — which is
> what good data looks like. One component much larger than the other two is the solution telling
> you which part of itself is struggling.

---

# 24. Reading Trajectory RMS Colouring

Set at **Mobile Mapping ▸ Trajectory Settings ▸ Rendering Settings ▸ RMS values**, with
user-definable ranges and colours. Settings persist between projects *(TBC 27248)*.

> **This is the highest-value, lowest-effort QC view in the workflow**, and it is available
> before any point cloud exists (§17.4).

What to read from it:

- **Where the solution degraded** — and therefore where control is most valuable (§22) and where
  registration will struggle
- **How long each degraded stretch was.** A short gap bracketed by good data is bridged well by
  the smoother. A long one is not (§8)
- **Whether the degradation is at the ends of the mission**, where the smoother has data on one
  side only — the reason the closing sequence in §14 exists

> **OBSERVED SOFTWARE BEHAVIOR**
>
> "If the mission contains some registrations then the modified segments will be colorized with
> the **'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
> `smrmsg` file, so adjusted stretches lose their RMS colour.
>
> **Incidentally useful:** this makes the extent of a registration visible in plan. A **Local**
> registration that stopped adjusting beyond the outermost control point (§21.5) shows the
> boundary directly.

---

# 25. Visual QC

## 25.1 The visual check

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
4. Set **Cutting plane thickness** (§25.2)
5. In Project Explorer, **check only the scans in the pair** and uncheck everything else
6. **Drag the slider along the run**, watching the gap
7. Optionally **Show surface-plane intersection** where a surface exists

What you are looking for: **one wall, one kerb, one pole.** Two of anything is a disagreement,
and its size in the profile is its size in the data.

> **FIELD TIP**
>
> Drag the slider through the **whole** run, not a representative sample. Trajectory error is
> correlated in time (§3), so disagreement is concentrated in stretches rather than scattered.
> A pass that is perfect for 2 km and 5 cm out for 300 m will look perfect at every point you
> spot-check and be unacceptable where it matters.

### What else to look at, and what nothing automates

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-27); it is not decided here.

## 25.2 Cutting plane thickness

> **FIELD TESTING REQUIRED · T16**
>
> Trimble's screenshots show **0.030** in the calibration topic *(TBC 24886)* and **5.000** in the
> run-to-run topic *(TBC 25096)*, with no stated basis for either.
>
> The value determines what the check can see. Too thin and the profile is empty. Too thick and a
> real 3 cm offset is buried inside a 5 m band of points collected from either side of the plane.
>
> Establish working values for the checks in §25.1 and record them. *(Appendix E)*


---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We went and looked at the point cloud — specifically at places where two
> passes should agree — using a profile view with one colour per scan, dragged along the whole
> corridor rather than sampled at a few spots.
>
> **Why it matters.** This is the half of QC that no number can do. Trimble requires it and does
> not describe how to do it thoroughly, which is why this section assembles the mechanics into a
> method. What you are looking for is simple: one wall, one kerb, one pole. Two of anything is a
> disagreement, and its size in the profile is its size in the data.
>
> **What can go wrong.** Two things, and both are about how you set the view up rather than what
> you are looking at. If the rendering is left in a single colour, **two surfaces four centimetres
> apart look exactly like one surface four centimetres thick** — you will stare straight at the
> defect and not see it. And if the cutting plane is too thick, a real offset is buried inside a
> band of points collected from either side of the plane.
>
> The third failure is sampling. Mobile mapping error arrives in stretches, not speckles, because
> it is driven by a filter that changes smoothly over minutes. A corridor that is flawless for two
> kilometres and five centimetres out for three hundred metres will pass every spot check you take.
>
> **What good looks like.** Scan Color on, point size up, a sensible plane thickness, and the
> slider dragged the full length of every overlap — showing one of everything. Flat surfaces that
> are as thin at fifty metres as at ten. And the ends of the corridor checked specifically, because
> that is where a Local adjustment stops working and where the trajectory smoother had data on one
> side only.

---

# 26. Imagery

## 26.1 What the MX60 imagery is for

| Camera | Output | Typical use |
|---|---|---|
| **360° spherical** | Panoramic images along the corridor | Feature identification, asset attribution, virtual site visits, client review |
| **Rear-downward** | Pavement-facing imagery | Pavement condition, orthomosaics, line-marking work |

Imagery is positioned from the trajectory, exactly as the point cloud is. It inherits the same
errors and improves — or does not — in the same way.

> **OBSERVED SOFTWARE BEHAVIOR · unverified**
>
> **Whether imagery positions inherit a registration is not documented.** Registration produces a
> new trajectory and Update Scans recomputes the point cloud from it (§19). No captured Trimble
> topic states whether station positions and panorama orientations are recomputed too.
>
> It is plausible that they are, since imagery is positioned from the trajectory. **It is not
> stated, and must not be assumed.**
>
> **FIELD TESTING REQUIRED · T26** — compare a station's position before and after a registration.
> This is answerable in minutes and nobody has done it. *(Appendix E)*

## 26.2 Resolution depends on the configuration

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22501, 23888)*

| Image | MX60 **Core** | MX60 **Pro** / **Premium — ours** |
|---|---|---|
| Panoramic | **8192 × 4096 px** | **12288 × 6144 px** |
| Side / planar | 4096 × 3008 px | 4096 × 3008 px |

> **IMPORTANT**
>
> **This system is the Premium, so panoramas are 12288 × 6144 px** — four times the pixels of a
> Core (§7.3). Commitments to a client about imagery deliverable quality — legibility of sign
> text, identification of small assets, orthomosaic ground sample distance — are made against that
> figure.
>
> A panorama that exports at 8192 × 4096 px did not come from this system. Find out which mission
> it belongs to before it goes anywhere.

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
> *(Appendix E; V-8)*

## 26.3 What to check

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §16** (D-27); it is not decided here.

## 26.4 Corrupted side camera images are exported as black

> **TRIMBLE DOCUMENTED METHOD**
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
> Include a **file-size scan** of the exported imagery in the delivery check (the **SOP §19**). The logic: a
> uniformly black JPEG typically compresses far smaller than a valid image, so **anomalously small
> files are a useful screening flag** and a sorted file listing surfaces candidates without
> opening a single image.
>
> **File size alone cannot establish image validity.** It is a screening method, not proof. A
> small file may be a legitimately low-detail frame — a plain sky, a blank wall, an unlit tunnel —
> and a corrupted image is not guaranteed to be small. Anything the scan flags must be opened and
> looked at; anything it does not flag is not thereby verified.
>
> **Validation required** before it is relied on: run it against a known-good export and a known-bad one
> and establish whether a usable threshold exists for MX60 imagery.
>
> *(D-31)*

## 26.5 Colorized point clouds

Colour on the point cloud comes from the imagery, at scan generation (§18.4).

> **TRIMBLE DOCUMENTED METHOD**
>
> Colour is exported "if the scans have been generated with the color option set to on"
> *(TBC 23339, 22501)*.

Two failure modes worth checking specifically:

**Colour fringing at feature edges** — points on a kerb taking the colour of the road, or points
on a pole taking the colour of the sky behind it. Small amounts are inherent: the camera and the
scanner are at different positions and see slightly different things. Large or systematic
fringing indicates a **camera boresight problem** (§20.4), and is one of the few places where a
calibration issue is directly visible.

**Colour from the wrong exposure** — a stretch of cloud markedly darker or lighter than its
neighbours, where the camera's automatic exposure changed between passes.

> **FIELD TESTING REQUIRED · T6**
>
> The colouriser offers a forward versus backward camera preference with no stated selection rule
> *(§18.4)*. Its effect on fringing is untested. *(Appendix E)*

## 26.6 Privacy and blurring

> **TRIMBLE DOCUMENTED METHOD**
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

> **Open Parametrix decision — D-32.** *What is Parametrix's position on imagery privacy?* Stated and tracked in the **SOP §16**; see also the master register.

## 26.7 Imagery in the delivered dataset

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
> not the trajectory** (§30).

---

> **IN PLAIN LANGUAGE**
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
> which is the difference between reading a sign at 20 m and guessing at it. Ours is the Premium,
> so the larger figure is the one to quote — but quote it from this section, because a Trimble
> topic showing 8192 × 4096 px may have been describing a Core, and one showing 8000 × 4000 px is
> describing an MX7.
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

# 27. Degraded GNSS Conditions

## 27.1 This section is a branch, not a stage

Everything from §17 to §26 describes one path through the workflow. This section describes what
to do when that path does not produce an acceptable trajectory — and **two of its three remedies
loop backwards** into earlier stages.

```
                        §17  Trajectory processing
                               │
                               ├──────────── LiDAR QC ──────────┐   inside §17
                               │                                 │   needs a large workstation
                               ▼                                 │
                        §18  Generate scans                      │
                               │                                 │
                               ▼                                 │
                        §21  Register to control ────────────────┤   needs more control
                               │                                 │
                               ▼                                 │
                        §23  QC  ── not acceptable ──────────────┤
                               │                                 │
                               │            PFIX ────────────────┘   needs POSPac
                               │            loops back to §17, second pass
                               ▼
                             accept
```

Read it after the normal path is understood. Placing it in sequence would imply it happens after
QC, which is true only in the sense that QC is where you discover you need it.

## 27.2 Why GNSS degradation is the dominant risk

From §3: the point cloud inherits the trajectory's error, attitude error multiplies with range,
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

The trajectory RMS colouring (§17.4, §24) shows degraded stretches **in plan, before any point
cloud exists**. That is the earliest and cheapest warning available, and it should be looked at
on every mission.

## 27.3 The three remedies

| | **More control** | **PFIX** | **LiDAR QC** |
|---|---|---|---|
| What it is | Register to additional surveyed GCPs | POSPac position fixes from GCP/target offsets | Scan data as an aiding sensor in the solution |
| Where it acts | **After** the navigation solution | **Inside** the navigation solution | **Inside** the navigation solution |
| Needs POSPac | No | **Yes** | Not stated |
| Needs extra field control | **Yes** | **Yes** | **No** |
| Needs a large workstation | No | No | **Yes** — 128–256 GB RAM (§11.1) |
| Passes | One | **Two** | One |
| Section | §15, §17 | §27.5 | §27.6 |

> **Without a POSPac licence, Parametrix has two remedies, not three: place more control, or buy a
> much larger workstation.** That is a procurement consequence of a licensing decision, and it is
> worth knowing before quoting a job through a difficult corridor. *(§10.3, D-10)*

## 27.4 Remedy one — more control

The conventional answer, and the one that needs no software Parametrix may not have.

Registration to surveyed GCPs (§21) corrects the trajectory **after** the navigation solution.
Where GNSS was poor, the trajectory has drifted, and control in that stretch pulls it back.

Two constraints from §21 govern how control must be placed for this to work:

- **A Local adjustment does not extrapolate** beyond the outermost control point *(TBC 22905)*.
  Control must **bracket** the degraded stretch, not sit in the middle of it
- **Target-Bundle Adjustment** operates at 250 m or 70 m intervals (§21.7), which is Trimble's own
  indication of the scale at which control density matters

> **The difficulty is practical rather than technical.** The stretches that most need control are
> the ones where conventional survey is hardest — under the canopy, between the buildings, where
> the GNSS you would use to establish the control is as obstructed as the vehicle's was. Control
> there has to be carried in by traverse or total station, which is the real cost of this remedy.

> **Open Parametrix decision — D-16.** Stated and tracked in the **SOP §8**; see also the master register.

## 27.5 Remedy two — Generate POSPac Position Fixes (PFIX)

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
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
> Trimble never states the contrast directly.* **VENDOR CLARIFICATION REQUIRED · V-16** — when should
> PFIX be preferred over registration? *(Appendix E)*

### Prerequisites

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
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
   (§21.6), with the same live residuals and the same **30 m** maximum pair separation
4. **Validate**. Easting, Northing and Elevation residuals display
5. Add further pairs — one pair is sufficient for TBC, and §21.6's caution applies equally
6. **Compute.** "The computation consists in reducing the global error between the ground control
   point(s) (GCPs) and their corresponding targets"
   - Updated targets are named `Mission_Name-PFIX-GCP_Name`
   - **A `custom_events.txt` file is generated in a `PFIX` folder under the TBC project folder**
7. Close the dialog

### The second pass, in POSPac

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
>
> 1. Start POSPac MMS, create and save a project
> 2. Import the POS logged files from `POS_1/raw`
> 3. **Copy the `custom_events.txt` from TBC into the `Extract` folder of the POSPac project**
> 4. Open the **GNSS-Inertial Processor**
> 5. Optionally open **Position Fixes and Satellite Events** to inspect the fixes
> 6. Select the IN-Fusion processing mode
> 7. **All Processings**. A new SBET appears in the `Proc` folder

### Bringing it back

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
>
> 1. Select the mission in Project Explorer and display its properties
> 2. **Replace the initial trajectory file with the new SBET** computed with PFIXes
> 3. **Update the scan data with the Update Scans command** (§19)

> **IMPORTANT**
>
> Step 3 is the one that is skipped. A PFIX pass that produces a better SBET but never reaches the
> point cloud has cost a day and changed nothing in the deliverable (§19).

## 27.6 Remedy three — LiDAR QC

Covered in §11, because it runs **inside** trajectory processing rather than after it.

In summary: it uses the scan data as an aiding sensor, generating 3D voxels matched in overlap
regions, solving the constant IMU boresight angles and correcting the post-processed trajectory in
position and orientation *(TBC 28972)*.

**What makes it distinctive:** it is the only remedy that needs **no additional field control**.
The information comes from the overlap in the data already collected.

**What makes it expensive:** 128 GB RAM minimum, 256 GB recommended, dedicated SSDs, a paging file
at six times installed RAM, and the MATLAB Runtime (§11.1).

> **It requires overlap.** "Select the runs from the Project Tree **with overlap** (parallel runs,
> or crossing runs)" *(TBC 28972)*. A single pass down a difficult corridor gives it nothing to
> work with — which is a **planning** consequence (§15), not a processing one. If a corridor is
> known to be GNSS-hostile and LiDAR QC is a possible remedy, the overlap has to be collected on
> the day.

> **CAUTION · W-10**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

## 27.7 Choosing

> **Open Parametrix decision — D-34.** *What is the decision rule when a corridor produces an unacceptable trajectory?* Stated and tracked in the **SOP §8**; see also the master register.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §8** (D-16); it is not decided here.

---

> **IN PLAIN LANGUAGE**
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

# 28. Cleanup Mobile Mapping Mission

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*
>
> **Do not run this command until §28.4 has been decided by Parametrix.**

## 28.1 What it does

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 26466)*
>
> "The feature enables you to cleanup your project by **keeping the most recent registration (and
> related scans), and trajectory consistent with the latest version of navigation and trajectory
> information file (SBET or NAV)**. This feature can be run at the end of the data preparation
> process (registration, colorization, etc.), it allows you to **share a light project**, before
> moving on to a feature extraction phase. Please, have a backup copy of your project prior
> performing the operation, it cannot be undone."

Run from the **Mission** node context menu. That is the entire published procedure — the topic is
four sentences long.

## 28.2 Why the command exists, and why it is genuinely useful

A mission that has been through several registration attempts accumulates layers. Each
registration produces a trajectory node and a numbered SBET on disk; each Update Scans produces a
scan set beneath it (§19, §21.3). A project with four registration attempts holds four
trajectories and up to four full scan sets of the same data.

That is large, slow to open, and confusing to hand to someone else. Cleanup reduces it to one
answer.

> **There is a real quality argument for it, not just a disk-space one.** After Cleanup, the
> project contains exactly one trajectory and one set of scans, so **the question "which
> trajectory produced this cloud?" has only one possible answer**. Before Cleanup, a person
> exporting from the project can select the wrong node and never know (§29, §30).
>
> Cleanup makes the deliverable unambiguous. It does so by destroying the alternatives.

## 28.3 What it removes, and why that matters

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
> trajectory and registration type (§21.3), and the sequence is legible.
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

## 28.4 The Parametrix decision

> **Open Parametrix decision — D-3, D-35.** Stated and tracked in the **SOP §18**; see also the master register.

## 28.5 What Trimble recommends, precisely

Stated carefully, because the gap matters.

> **TRIMBLE DOCUMENTED METHOD**
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

## 28.6 A recordkeeping framework, offered for decision

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §18** (D-35); it is not decided here.

## 28.7 The relationship to provenance

Cleanup is the sharpest instance of the problem §30 is about.

The provenance evidence inside a TBC project is genuinely good — trajectory properties naming the
origin, the input trajectory and the registration type; numbered SBET files; scans nested beneath
the trajectory that produced them; a `_reg_####` station suffix (§21.3, §19).

**IMPORTANT PROVENANCE LIMITATION.** Exported mobile mapping data may retain coordinate, timing,
and in some formats trajectory information, but **the captured Trimble documentation does not
establish that the output uniquely identifies the adjusted trajectory or registration result used
to create it** (§30).

> **The two findings compound.** Cleanup reduces the registration history available in the
> project; export is not documented as providing unique registration lineage. **A LAS point cloud
> exported after Cleanup may retain spatial and point-level metadata, but the captured
> Trimble documentation does not establish that it preserves sufficient registration and
> trajectory lineage to reconstruct how the final cloud was produced.**
>
> The practical concern is therefore not literally "no history." It is that **the deliverable may
> not contain enough documented provenance to reconstruct its processing history independently of
> the TBC project and Parametrix records.**
>
> That is not an argument against Cleanup. It is the reason §28.4 remains a Parametrix decision,
> and the reason §28.6 steps 2–6 are proposed to happen first.

---

> **IN PLAIN LANGUAGE**
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
> This matters more than it would elsewhere because of §30: almost none of that history leaves the
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

# 29. Export — What Each Path Carries

## 29.1 Export is a QA/QC step, not a file conversion

By the time a processor reaches this section the analytical work is done. It is tempting to treat
what follows as mechanical.

It is not. Export is the last point at which the project and the deliverable can diverge, and
several documented ways exist for them to do so silently:

- The scans exported may not be the registered ones (§29.2)
- The scans exported may not be the scans TBC generated at all (§29.3)
- Coordinates may be grid or ground, and one of those does not tell you its own scale factor
  (§29.5)
- Imagery may be present and black (§26.4)
- A selection drawn in a view may span scans built on different trajectories (§29.4)

**Every one of those produces a file that opens correctly, looks right, and is wrong.**

## 29.2 QC CHECK — CONFIRM SCANS WERE UPDATED AFTER REGISTRATION BEFORE EXPORT

> **CAUTION · the most consequential check in this section**
>
> **Registration does not modify the point cloud until Update Scans is performed** (§19, §21).
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> **export point cloud data that still reflects the pre-registration trajectory.** The export
> succeeds. The file is valid. The data is unregistered.
>
> Nothing in the export dialog references the registration state.

### How to verify, using documented evidence

> **TRIMBLE DOCUMENTED METHOD**
>
> | Evidence | What it shows | Source |
> |---|---|---|
> | **Scans are nested beneath the trajectory they were computed from** in Project Explorer | Scans under `Reg. Trajectory` / `RegTrajectory` were computed against it; scans under `Sbet` were not | *(TBC 22638, 22905, 26473)* |
> | **Updated scan stations carry a `_reg_####` suffix** — e.g. `Run_14_Laser Right_reg_0001 (S3)` | That station was produced by Update Scans against a registered trajectory | *(TBC 22638)* |
> | **The adjusted trajectory's properties** — `Origin: Registration result`, `Input trajectory`, `Registration type` | Which trajectory is the registered one | *(TBC 22905, 26473)* |
> | **Registered segments render in the "Undefined RMS" colour** | Which stretches of trajectory an adjustment actually affected | *(TBC 27248)* |

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §19** (D-36); it is not decided here.

> **FIELD TESTING REQUIRED · T29**
>
> **Establish the reliable verification method for each export path.** Tree position and the
> station suffix are evidence *inside the project*. What is **not** established is how an export
> dialog resolves its selection — in particular:
>
> - Whether the **Mobile Mapping tab** exporters, which select by run, take the currently active
>   trajectory or a specific one
> - Whether the **Point Cloud tab** exporters, which select by region or by a rectangle drawn in a
>   view (§29.4), can be made to respect a trajectory at all
>
> Until tested, the only defensible verification is the project-side one above, performed
> immediately before export and recorded. *(Appendix E)*

## 29.3 Export timestamps — an unresolved question about what is exported

> **TRIMBLE DOCUMENTED METHOD**
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

> **VENDOR CLARIFICATION REQUIRED · V-1**
>
> **When Export timestamps causes TBC to reprocess from the raw source data, which trajectory is
> used for that reprocessing?**
>
> **The captured documentation does not establish this.** Trimble states that reprocessing occurs
> and does not state what it reprocesses against. Both readings — the mission's currently applied
> trajectory, or the originally imported one — are consistent with the wording.
>
> **No speculation is offered here.** *(Appendix E)*

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

> **Open Parametrix decision — D-36.** *May exports be made with Export timestamps enabled before this behaviour is established?* Stated and tracked in the **SOP §19**; see also the master register.

## 29.4 Two export tabs that behave differently

> **TRIMBLE DOCUMENTED METHOD**
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

## 29.5 Coordinate handling — common to the point cloud exporters

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 11769, 27279)*
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
> trajectory** (§30).

## 29.6 The MX60 export paths

Six documented paths. **No preference between them is expressed or implied here — the choice of
deliverable format is a project and client matter that Parametrix has not decided.**

> **Open Parametrix decision — D-38.** Stated and tracked in the **SOP §19**; see also the master register.

### 29.6.1 Export to LAS (Trajectory Split) — classified point cloud regions

*(TBC 27279)* · **Mobile Mapping tab**

**Prerequisite:** run **Extract Classified Point Cloud** in *Point Clouds ▸ Regions* first.

| | |
|---|---|
| **What leaves TBC** | Classified point cloud regions of one run, as LAS. "The classification code is added to the exported points" |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Grid or ground per §29.5; `.txt` sidecar on grid |
| **Timing** | LAS point records per §29.7 |
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

### 29.6.2 Export to TMX

*(TBC 22501)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images, side camera images, laser point clouds **and trajectory** |
| **Trajectory geometry** | **YES** — "The trajectory file is created **once for all devices**. It resides in a folder under the Mission folder" |
| **Specific trajectory identified** | **Not documented** |
| **Coordinate system** | Per §29.5. **"For the MX9 Export to TMX, the user must use a coordinate system without Geoid"** — *stated for the MX9 only; whether it applies to the MX60 is not stated* |
| **Timing** | Export timestamps option — **see §29.3** |
| **Imagery** | Panoramic (Pano), side (Sideview, Planar 1/2), back-facing (Planar 3); optional GPS attributes in the image files |
| **Sidecars** | `reference.csv` |

Output structure: a **Mission folder** plus one folder per device, with `laser`, `panorama`,
`planar*` and **`trajectory`** sub-folders. The MX60 example is illustrated in Trimble's topic.

> **Provenance implication:** this is one of two paths on which **trajectory geometry accompanies
> the deliverable.** A run carrying both an imported `Sbet` and a registered trajectory has two
> candidates, and **the topic does not state which is written.**
>
> **VENDOR CLARIFICATION REQUIRED · V-10** — which trajectory does the TMX export write when
> several exist under a run? *(Appendix E)* · **FIELD TESTING REQUIRED · T19** *(Appendix E)*

### 29.6.3 Export to TopoDot

*(TBC 23339)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images, side camera images, laser point clouds — as a *Raw Project Data* folder with *Image Project* and *LAS Files* sub-folders |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §29.5 |
| **Timing** | Export timestamps option — **see §29.3** |
| **Imagery** | Cubical images from the panoramic and side cameras, one set per camera per run |
| **Sidecars** | `.iprj` image project, `.lst` containing all image position and orientation, `.cal` camera models — one per camera |

**Prerequisites** *(TBC 23339)*: "You need to first generate scans from the raw data before
exporting them to the TopoDot software. Otherwise, nothing will be exported." And: **"You must
close all run views prior to export. Otherwise, a warning message will pop up."**

**LAS files:** "a couple of 1.4 LAS format files, one couple per run."

> **Provenance implication:** the `.lst` file carries **image position and orientation**, which is
> trajectory-derived information at the station level. **It is not documented as identifying the
> trajectory it came from.**

### 29.6.4 Export to Solv3D

*(TBC 23888)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images and laser point clouds |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §29.5 |
| **Timing** | **Trimble recommends No** — "Solv3D does not need the Timestamps information. Trimble recommends turning this option to No" |
| **Imagery** | Panoramic only, in a `Panorama` folder; a `reference.csv` alongside "which contains Roll, Pitch and Yaw information and X, Y, Z as well" |
| **Sidecars** | `reference.csv` |

Output: a folder named for the mission, with `Lasers` and `Panorama` sub-folders. LAS 1.4, "one
couple per run in case of a single scanner system and two when a double laser system is used."

> **Note the interaction.** Trimble's recommendation to disable timestamps here has a second
> effect it does not mention: per §29.3, timestamps off means the **generated** scans are
> exported rather than reprocessed ones. On this path the recommended setting is also the one
> that preserves the processing you performed.

### 29.6.5 Generic Point Cloud Export

*(TBC 11769)* · **Point Cloud tab**

| | |
|---|---|
| **What leaves TBC** | Point cloud only, in `.e57` (plain or **structured**), `.las`, `.laz`, `.pod`, `.pts`, `.ptx`, `.rcp`, `.tdx` |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §29.5, including the ECEF option |
| **Timing** | LAS point records per §29.7 |
| **Imagery** | None |
| **Sidecars** | The scaling `.txt` |
| **Split** | *By station* — a separate LAS per scan station; *None* — a single LAS from all stations |

> **This is the path most likely to be used for an ordinary LAS or E57 deliverable, and it is the
> one with the least documented provenance and no run awareness** (§29.4).

### 29.6.6 Publish to TRCPS

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
> **VENDOR CLARIFICATION REQUIRED · V-10** *(Appendix E)* · **FIELD TESTING REQUIRED · T19** *(Appendix E)*

> **OBSERVED SOFTWARE BEHAVIOR** · Trimble Connect's **UK region** is currently unavailable for
> Publish to TRCPS and Trimble Mobile Mapping data *(TBC RN 2026.10)*. Not applicable to
> Parametrix, but it confirms Publish to TRCPS is a Connected Workspace function.

## 29.7 Summary — what is documented as leaving TBC

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
> **FIELD TESTING REQUIRED · T22** — export and inspect the file directly. **VENDOR CLARIFICATION
> REQUIRED · V-12** — does any TBC export write the source trajectory into a LAS header, VLR or
> sidecar? *(Appendix E; §30)*

## 29.8 Known limitations and silent failures

| Limitation | Path | Source |
|---|---|---|
| **Corrupted side camera images are exported as black images** | TopoDot, TMX | *(TBC 23339, 22501)* |
| All run views must be closed before export | TopoDot | *(TBC 23339)* |
| Scans must be generated first or nothing is exported | TopoDot, Solv3D | *(TBC 23339, 23888)* |
| Ground scaling does not expose its scale factor | All point cloud exports | *(TBC 11769, 27279)* |
| Grid-scaled re-import may double-scale | All point cloud exports | *(TBC 11769, 27279)* |
| MX9 Export to TMX requires a coordinate system without Geoid | TMX — **MX60 applicability not stated · V-17** | *(TBC 22501)* |
| Random sampling with no spatial rule | Classified LAS | *(TBC 27279)* · T17 |

---

> **IN PLAIN LANGUAGE**
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

# 30. Provenance

## 30.1 The question this section answers

> *A client, a reviewer, or opposing counsel is looking at a point cloud Parametrix delivered
> three years ago. They ask: how do we know this is the adjusted version, and which adjustment
> was it?*

That question is ordinary in survey work. A conventional adjustment produces a report naming its
observations, its constraints and its residuals, and the report travels with the deliverable.
Mobile mapping does not work that way, and this section sets out precisely what can and cannot be
demonstrated.

## 30.2 Four things that are related and not interchangeable

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
Publish to TRCPS both carry **trajectory geometry** out of TBC (§29). A recipient therefore holds
a path through space. What they do not hold is a statement of **which** path it is — the imported
one, the first registration, or the fourth — and on a project where several existed, geometry
alone may not distinguish them, particularly where a registration made a small correction.

## 30.3 The provenance chain

Each transition, with what exists at that point, what Cleanup can remove, and what survives
export.

### Legend

**In TBC** = a project object · **On disk** = a file in the project or raw data folder ·
**Cleanup** = may be removed by §28 · **Export** = documented as surviving export

---

### 1 · Raw MX60 mission → imported mission

| | |
|---|---|
| **In TBC** | Mission node; runs; Capture Devices; start/stop, duration, **covered distance**, active trajectory file *(TBC 22499)* |
| **On disk** | The `.mxdb`, raw POS data, raw scanner and camera data, `Extcal.json`, mission logs *(TBC 25943)* |
| **Cleanup** | The raw data is outside the project and unaffected |
| **Export** | Not applicable |
| **Parametrix record** | **The field record** — conditions, incidents, what was not collected. No software artefact exists (the **Field How To**) |

### 2 · Imported mission → trajectory

| | |
|---|---|
| **In TBC** | The trajectory node under each run; RMS colouring from `smrmsg_xxx.out` *(TBC 27248)* |
| **On disk** | `sbet_[mission].out` **or** `sbet_[mission]_[frame].out` in `NAVPROC/Export/`; the processing report in `NAVPROC/Report/`; with **Backup SBET Next to MXDB**, a copy **and a log of the frame and epoch used** beside the `.mxdb` *(TBC 25943)* |
| **Cleanup** | Keeps the trajectory "consistent with the latest version of navigation and trajectory information file (SBET or NAV)" *(TBC 26466)* |
| **Export** | Trajectory **geometry** on TMX and TRCPS; **identity not documented** |
| **Parametrix record** | Which computation mode, which base station, which settings — **no single artefact captures these** (§17.3) |

> **The frame-and-epoch log written by Backup SBET Next to MXDB is the only artefact found in the
> whole workflow that records the frame a trajectory was computed in, and it lives with the raw
> data rather than inside the project.** That is why enabling the option is proposed in §17.4.

### 3 · Trajectory → generated scans

| | |
|---|---|
| **In TBC** | Scan nodes **nested beneath the trajectory that produced them** *(TBC 22638)*; the **Results of Scan Generation** dialog recording filters, range and colorization per run *(TBC 22499)* |
| **On disk** | RWCX point cloud data in the project |
| **Cleanup** | Scans associated with removed registrations are removed *(TBC 26466)* |
| **Export** | The cloud itself. **Filter and colorization settings are not documented as travelling** |
| **Parametrix record** | **Capture the Results of Scan Generation** — proposed §18.5 |

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
| **Export** | **No export path is documented as identifying the registration result** (§29.7) |
| **Parametrix record** | **Which points were control and which were checks, and the residuals on each** — TBC is not documented as reporting this after the fact (§22.7) |

### 6 · Update Scans → final point cloud state

| | |
|---|---|
| **In TBC** | New scan nodes beneath the adjusted trajectory; stations carrying a **`_reg_####`** suffix *(TBC 22638)* |
| **On disk** | RWCX data in the project |
| **Cleanup** | Scans of removed registrations are removed |
| **Export** | The cloud. **The `_reg_####` suffix is a station name inside TBC and is not documented as appearing in exported filenames** |
| **Parametrix record** | Confirmation that Update Scans was performed before export (§29.2) |

### 7 · Export → delivered dataset

| | |
|---|---|
| **Travels** | Coordinate system and scale factor (`.txt`, grid); project global CRS (ECEF); GPS Time per point; image position and orientation in some paths; image EXIF naming TBC; **trajectory geometry on TMX and TRCPS** |
| **Not documented as travelling** | Trajectory name or ID; SBET filename; registration result; registration type; `_reg_####` sequence; source run or mission identifier within the data; calibration identity |
| **Cleanup** | Not applicable — but what Cleanup removed is no longer available to be recorded |
| **Parametrix record** | **The delivery record** — what was exported, from which node, on what date, by whom |

---

## 30.4 The limitation, stated precisely

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
> have been reviewed (§29.6). The remaining uncertainty is about **software behaviour Trimble does
> not document**, resolvable by test (T18–T23), not by further reading.

## 30.5 Cleanup and provenance, combined

> Cleanup reduces the registration history available in the project.
>
> Export is not documented as providing unique registration lineage.
>
> **Therefore performing Cleanup before preserving the appropriate project evidence may reduce
> Parametrix's ability to reconstruct the processing history later.**

That is a finding, not a prohibition.

> **Open Parametrix decision — D-35.** Stated and tracked in the **SOP §20**; see also the master register.

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
> be copied out beforehand or it is gone. *(Appendix E; §28.6, §25)*

## 30.6 What Parametrix would need to record

Stated as a gap analysis, not as policy.

> **Open Parametrix decision — D-29.** *What provenance record must accompany a mobile mapping deliverable, and where does it live?* Stated and tracked in the **SOP §20**; see also the master register.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §20** (D-29); it is not decided here.

## 30.7 Reconstruction paths that do exist

Where a delivered dataset must be tied back after the fact, two routes exist on current evidence.
**Both are reconstruction, not provenance, and both depend on Parametrix having retained
something.**

**Timestamp matching.** LAS point records carry GPS Time *(TBC 23339, 22501)*, and a retained SBET
is a time series. A point's timestamp can be matched to an epoch in a specific SBET. This
identifies *a* trajectory only if the candidate SBETs differ measurably at that epoch, and it
requires the SBETs to have been kept.

**Trajectory geometry comparison.** A TMX or TRCPS delivery contains trajectory geometry
(§29.6.2, §29.6.6), which could be compared against retained `sbet_*_reg_####.out` files. Same
caveat: it requires retention, and it distinguishes candidates only where they differ.

> **FIELD TESTING REQUIRED · T30** — establish whether either reconstruction path works in
> practice on a real dataset with two candidate trajectories. Neither has been attempted.
> *(Appendix E)*

---

> **IN PLAIN LANGUAGE**
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

# 31. Periodic System Verification

## 31.1 The check Trimble describes

Distinct from per-project QC. This is the check that the **instrument** is still performing.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.7)*
>
> Scan approximately **eight flat retro-reflecting targets** at varied distances over **more than
> 180° horizontally**, previously surveyed by total station. The system passes if residuals fall
> within the specified accuracy.
>
> Trimble recommends doing this "regularly" and "especially before starting an extensive data
> acquisition campaign" — and **gives no interval**.

> **VENDOR CLARIFICATION REQUIRED · V-14**
>
> **Is the retro-reflective target check the recommended periodic verification for the MX60, and
> at what interval?** The User Guide describes the check and says to do it "regularly" without
> naming a period. Trimble or the dealer can say what interval they expect, and whether any other
> verification is expected alongside it. *(Appendix E)*

> **Open Parametrix decision — D-28.** *Is this the periodic verification Parametrix uses, and at what interval?* Stated and tracked in the **SOP §13**; see also the master register.

---


---

# Part V — Evidence

---


---

# Appendix A — Trimble Source Index

Every Trimble source cited in this SOP. **`reference/mx60-reference-data.csv` (402 records) is the
authority for numbers**; this document explains what they mean.

## A1 · Manuals and bulletins

| Document | Revision | Cited for |
|---|---|---|
| **Trimble MX60 User Guide** | Rev B, May 2025 (P/N T001983), 68 pp | Hardware, installation, power, safety, specifications, periodic verification |
| **Trimble MX60 Quick Start Guide** | Rev B, March 2025, 16 pp | Field sequence, initialization, capture settings |
| **Trimble Mobile Imaging (TMI) Software User Guide** | **Rev L, April 2026** (P/N T001242), 56 pp | Field software, status, capture settings, calibration import |
| **Trimble MX60 Spec Sheet** | PN 022516-737C (04/25), 4 pp | Specifications |
| **Trimble MX Shock Absorbing Mounting Rack User Guide** | Rev B, May 2025 (P/N 37000001), 10 pp | Vehicle installation |
| **Product Bulletin: Enabling the Dust Filter in TMI for MX60** | January 2025, 3 pp | Dust filter |
| **TBC Technical Notes: For Mobile Mapping** | October 2022, 8 pp | **Predates MX60 support — used with caution** |

## A2 · TBC help portal — **TBC 2026.10**

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

## A3 · Not held, and needed

| Document | Needed for | Item |
|---|---|---|
| **Trimble GAMS Antenna Kit Installation & Operation Manual** | Lever-arm procedure if GAMS is fitted | V-5 |
| **Trimble DMI Installation & Operation Manual** | DMI scale factor for the measured wheel diameter | V-5 |
| **TBC Help: Blur Exported Images** | Imagery privacy procedure | §26.6 — capture when privacy is drafted |

## A4 · Non-Trimble sources — reference only

> **These are cited as examples of how others have answered questions Parametrix has not. They are
> not Parametrix standards and not Trimble requirements.**

| Source | Used for |
|---|---|
| **Queensland TMR, Mobile Laser Scanning Technical Guideline**, March 2023, CC BY 4.0 | An example of a published agency specification for control layout, accuracy tiers, and wet-weather practice — §22.6, the **Field How To** |
| **NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data**, 2024 | Background |

## A5 · Analysis record

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

> Unresolved conflicts between these sources are listed separately in **Appendix G**.

---

# Appendix B — The Reference Dataset

## B1 · What it is

`reference/mx60-reference-data.csv` holds **402 records** extracted from the source documents.
It is the **authority for numbers** in this manual: where a figure appears in the body, it was
taken from this file, and where the two disagree the CSV is correct and the body is a
transcription error to be fixed.

It exists because the same number appears in three or four places in a document set of this size,
sometimes in two different forms (per-scanner and system-total; centimetres and millimetres), and
because a number in prose has no source attached to it.

## B2 · Schema

| Column | Contents |
|---|---|
| `id` | Prefixed identifier — see B3. Stable; cite it |
| `category` | Broad grouping: Scanner, Positioning, TMI, Registration, Export, Safety … |
| `topic` | The narrower subject within the category |
| `item` | What the record is about, in words |
| `value` | The number, string, or statement |
| `notes` | Conditions, caveats, and any conflict with another record |
| `source` | The document, by short name |
| `page` | Page number where the source has one; `-` for web help topics |
| `sop_section` | Where it is used. Written against the single-document draft — see the note in B5 |

## B3 · What the identifier prefixes mean

| Prefix | Count | Meaning |
|---|---|---|
| `SPEC` | 56 | Manufacturer specification — an instrument or system performance figure |
| `TMI` | 50 | Trimble Mobile Imaging field software behaviour and settings |
| `QSG` | 42 | From the MX60 Quick Start Guide — mostly field procedure |
| `REG` | 34 | Registration behaviour and parameters |
| `EXP` | 28 | Export paths, options and outputs |
| `INST` | 27 | Installation — lever arms, mounting, offsets |
| `CAL` | 26 | Calibration procedure and geometry |
| `OPS` | 25 | Operating procedure and limits |
| `LIMIT` | 22 | A stated limit: environmental, electrical, operational |
| `TBC` | 22 | Trimble Business Center behaviour, versions and licensing |
| `TRAJ` | 16 | Trajectory processing settings and defaults |
| `SAFE` | 15 | Safety statement from a source document |
| `VEH` | 9 | Vehicle configuration |
| `SUPPORT` | 9 | Support routes and contacts |
| `QC` | 8 | Quality control indicators |
| `CONN` | 6 | External connectors |
| `CONFLICT` | 4 | **Two sources disagree.** See Appendix G |
| `CLEAN` | 2 | Cleanup behaviour |
| `RESOLVED` | 1 | A conflict that has since been resolved, kept for the record |

## B4 · Where the records come from

| Source | Records |
|---|---|
| MX60 User Guide Rev B | 153 |
| TMI User Guide Rev L | 50 |
| MX60 Quick Start Guide Rev B | 42 |
| TBC help topics (all) | ~120 across 30 topics |
| TBC release notes 2025.21 and 2026.10 | 14 |
| MX60 specification sheet | 5 |
| Dust filter bulletin | 7 |
| Roof rack user guide | 1 |

Full citations are in **Appendix A**.

## B5 · How to use it

**To check a number in this manual.** Search the CSV for the value or the topic. The `source` and
`page` columns give the citation; the `notes` column usually explains any condition attached to
it.

**To answer a question this manual does not address.** The CSV contains records that no section
needed — connector pinouts, cable lengths, screw torques, support addresses. Search it before
assuming the answer is not in the source set.

**Before quoting a number to a client.** Check whether it carries a `CONFLICT` note. Four figures
in the set are contradicted by another source (Appendix G), and two more are quoted in two
different forms by Trimble itself — the scanner pulse rate and scan speed, which the specification
sheet gives as system totals and the User Guide gives per scanner (§16.1).

> **IMPORTANT · the `sop_section` column is stale**
>
> That column was written against the single 71,800-word draft that preceded the four-deliverable
> structure. Its numbers do **not** correspond to this manual's sections. It is retained because it
> records which topic each number was used for, which is still useful, but it should not be used as
> a cross-reference until it is regenerated.
>
> Regenerating it against the four-deliverable structure is straightforward and is on the
> project's own task list. It does not affect any value in the file.

---

# Appendix C — Figures

**There are no figures in this manual at this Working Version.** That is a deliberate state, not an
omission in progress, and it is worth one page of explanation because the absence is visible.

## C1 · Why there are none yet

Every figure this manual would use is a crop from a Trimble help topic or manual page held in
`sources/`. A full help-portal screenshot carries Trimble's navigation, header and footer, which
would make a Parametrix document look like a Trimble one. **Crops, not whole pages** — and the crop
list, the caption rule and the attribution rule are production work that has not been done.

The list of figures to produce — 40-odd of them, across all four documents — is held at
`deliverables/_control/figure-production-register.md`. It is project material and does not belong
in a document a reader opens.

## C2 · What this means for a reviewer

**Where this manual describes a dialog, a pane or a reading, it describes it in words.** If a
description is one you cannot follow without seeing the screen, that is exactly the feedback the
review needs — say which section, and it goes on the production list with a reason attached.

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> Figure captions, source attribution and the statement of which TBC version is shown are all
> document-control conventions, and none is established. The proposed form is recorded in the
> production register, unadopted.

---

# Appendix D — Observed Software Behaviour

**Generated view — do not edit by hand.** Produced by `tools/build-observed-behaviour.py` from the
**OBSERVED SOFTWARE BEHAVIOR** blocks in the body of this manual. Edit the section; regenerate
this.

An entry here is something seen in the software, or stated in a release note, that Trimble does
**not** document as procedure. It is weaker evidence than a **TRIMBLE DOCUMENTED METHOD** block
and stronger than an inference. Where behaviour of this kind carries a real consequence, it also
appears in the warning register.

**9 entries.** Last generated 2026-09-11.

---

### §9.3 · The failure mode both share

"If an aiding navigation sensor is not activated in Vehicle Settings its data will **not** be
logged — even though all connections may have been made properly."

### §10.2 · Trimble Business Center — the office software

From TBC 2026.10, **Trimble ID sign-in requires two-step verification** — a code by email each
time *(TBC RN 2026.10)*. Anyone signing in to TBC or Trimble Connect needs access to the
account's email at that moment. Worth knowing before it stops a session.

### §17.4 · Outputs, and a filename that means something

A registered trajectory no longer matches its `smrmsg` file, so adjusted stretches lose their
RMS colour and render as **Undefined RMS** *(TBC 27248)*. **§24 quotes the behaviour in full and
makes a QC technique out of that side effect.**

### §24 · Reading Trajectory RMS Colouring

"If the mission contains some registrations then the modified segments will be colorized with
the **'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
`smrmsg` file, so adjusted stretches lose their RMS colour.

**Incidentally useful:** this makes the extent of a registration visible in plan. A **Local**
registration that stopped adjusting beyond the outermost control point (§21.5) shows the
boundary directly.

### §26.1 · What the MX60 imagery is for

**Whether imagery positions inherit a registration is not documented.** Registration produces a
new trajectory and Update Scans recomputes the point cloud from it (§19). No captured Trimble
topic states whether station positions and panorama orientations are recomputed too.

It is plausible that they are, since imagery is positioned from the trajectory. **It is not
stated, and must not be assumed.**

**FIELD TESTING REQUIRED · T26** — compare a station's position before and after a registration.
This is answerable in minutes and nobody has done it. *(Appendix E)*

### §26.2 · Resolution depends on the configuration

Trimble's export folder-structure examples show the MX60 tree containing **Camera 3 Back Down**
and **Camera 4 360°**, with per-face `.cal` files for the 360° camera (Front, Rear, Left, Right,
Top, Bottom). The MX9 and MX50 trees additionally show **Planar 1** and **Planar 2** side
cameras; **the MX60 tree does not** *(TBC 23339, 22501)*.

This suggests the **Export side images** option has nothing to export on an MX60. **Trimble does
not state this**, and the option remains present in the dialog.

**FIELD TESTING / VENDOR CLARIFICATION REQUIRED · T27** — **what imagery streams actually
exist on the MX60, and which are exposed through TBC export?** Run an export with side images
enabled and see what appears; confirm with the vendor what the MX60 camera complement is.

**Do not write MX9 or MX90 camera behaviour into MX60 procedure on the strength of a shared
dialog.** The option's presence in the export pane is not evidence that the sensor exists.
*(Appendix E; V-8)*

### §26.7 · Imagery in the delivered dataset

An exported panoramic image's file properties show **`Program name: Trimble Business Center`**
*(TBC 21713_1)*. Software provenance does reach the imagery, in EXIF. **It names the software,
not the trajectory** (§30).

### §28.3 · What it removes, and why that matters

The registered SBETs are written **to the project folder on disk**, not inside the TBC database
*(TBC 22905, 26473)*. Trimble does not state whether Cleanup deletes them or only removes the
project's references to them.

**FIELD TESTING REQUIRED · T28** — list the project folder before and after Cleanup and
compare. If the files survive, they are a partial audit trail that outlives the operation; if
they do not, the record is gone entirely. **This materially changes what must be archived
first.** *(Appendix E)*

### §29.6 · The MX60 export paths

Publish to TRCPS and Trimble Mobile Mapping data *(TBC RN 2026.10)*. Not applicable to
Parametrix, but it confirms Publish to TRCPS is a Connected Workspace function.

---

# Appendix E — Open Technical Questions

**44 items.** Generated from `deliverables/_control/master-register.csv` on 2026-09-19. **Do not edit this file** — edit the register and re-run `tools/build-register-views.py`.

This appendix is the Technical Manual's **view** of the project's single master register. It shows
the questions that are answerable by **evidence** — by running a test, or by asking Trimble. The
decisions that are Parametrix's to make are the SOP's view of the same register and are not
repeated here.

| | Count |
|---|---|
| **FIELD TESTING REQUIRED** — answerable by testing | **27** |
| **VENDOR CLARIFICATION REQUIRED** — answerable only by Trimble | **17** |
| Of those, priority P1 | 12 |
| Of those, blocking something | 0 |

> **An open item here is not a defect in this manual.** It is a statement that the evidence does
> not yet reach, recorded rather than papered over. Where a question is open, the body of the
> manual says so at the point where it matters, rather than presenting a guess as a fact.

---

## E1 · Field testing required

*Answerable with the equipment and the software. Each entry says what to do, not merely what is
unknown.*

### T1 · Filter selection and defaults - Default vs High Quality, Isolated Points default state, Range Max against useful range, Fog and Sun when conditions did not occur

**P2** · open

**Why it matters.** The largest block of untested settings. Trimble text contradicts itself on Isolated Points

**Evidence.** TBC 22499

*Stage: scan generation · Documents: Manual; SOP; Office*

### T3 · Does Reflective Panels remove legitimate retro-reflective returns from signs and line marking?

**P1** · open

**Why it matters.** On sign and retroreflectivity work those returns are the deliverable

**Evidence.** TBC 22499

*Stage: scan generation · Documents: Manual; SOP; Office*

### T6 · Colouriser forward vs backward camera preference and its effect on fringing

**P3** · open

**Why it matters.** No selection rule given

**Evidence.** TBC 22499

*Stage: scan generation · Documents: Manual; Office*

### T7 · Registration Auto-Saving default state

**P2** · open

**Why it matters.** Targets.csv is the registration field book and a wrong dialog answer empties it permanently

**Evidence.** TBC 22905; TBC 21243-1

*Stage: registration · Documents: Manual; SOP; Office*

### T9 · Target-Bundle Adjustment - test both states with independent checks

**P2** · open

**Why it matters.** Checking it makes the adjustment coarser, 250 m against 70 m; the name reads backwards

**Evidence.** TBC 22905

*Stage: registration · Documents: Manual; SOP; Office*

### T10 · Which Parametrix coordinate systems does POSPac recognise directly, and which trigger the ITRF00 path?

**P2** · open

**Why it matters.** Answerable once, then known

**Evidence.** TBC 25943

*Stage: trajectory processing · Documents: Manual; SOP; Office*

### T11 · Multipath default Medium on open-sky corridors

**P3** · open

**Why it matters.** Medium is described as being for degraded coverage

**Evidence.** TBC 25943

*Stage: trajectory processing · Documents: Manual; SOP; Office*

### T12 · DMI scale factor SD default 5 percent - was the wheel actually measured?

**P3** · open

**Why it matters.** Trimble says set it to 100 percent if unknown

**Evidence.** TBC 25943

*Stage: trajectory processing · Documents: Manual; SOP; Field; Office*

### T13 · LiDAR QC settings - range default 3-100 m and Lasers = All

**P3** · open

**Why it matters.** The Lasers default contradicts the guidance printed beside it

**Evidence.** TBC 28972

*Stage: trajectory processing · Documents: Manual; SOP; Office*

### T15 · Which registration type, when? Test Global, Local and Global-then-Local with independent checks

**P1** · open

**Why it matters.** No selection rule published. Global-then-Local gets no guidance and appears in every Trimble screenshot

**Evidence.** TBC 22905

*Stage: registration · Documents: Manual; SOP; Office*

### T16 · Working cutting plane thickness for the visual checks

**P2** · open

**Why it matters.** Trimble screenshots show 0.030 and 5.000 with no basis. Too thick buries a real offset

**Evidence.** TBC 24886; TBC 25096

*Stage: QC · Documents: Manual; SOP; Office*

### T17 · Sample points random sampling in the classified LAS exporter

**P2** · open

**Why it matters.** A destructive thinning with no documented spatial rule; default state not stated

**Evidence.** TBC 27279

*Stage: export · Documents: Manual; Office*

### T18 · Export the same registered run twice, timestamps off and on, and compare point geometry. Does reprocessing from raw reflect the registered trajectory?

**P1** · open

**Why it matters.** The highest-priority test. A documented export option may deliver data that was never the data that was checked

**Evidence.** TBC 23339; TBC 22501

*Stage: export · Documents: Manual; SOP; Office*

### T19 · Which trajectory travels? Publish a registered run to TRCPS and export the same run to TMX, and inspect what arrives

**P2** · open

**Why it matters.** Both paths carry trajectory geometry; neither states which trajectory

**Evidence.** TBC 22501; TBC 29527

*Stage: export · Documents: Manual; SOP; Office*

### T21 · Register a mission, run a Mission Report, and look. Does it contain the signed GCP residuals?

**P2** · open

**Why it matters.** The 2025.21 release note says residuals are in the report; the Mission Report topic does not mention them

**Evidence.** TBC RN 2025.21; TBC 23991_1

*Stage: QC · Documents: Manual; SOP; Office*

### T22 · Export a LAS and inspect the file directly - header fields, VLRs, sidecar contents

**P2** · open

**Why it matters.** Trimble topics do not enumerate LAS headers. Something undocumented may be written

**Evidence.** TBC 11769

*Stage: export · Documents: Manual; SOP; Office*

### T23 · Draw a Point Cloud tab selection across scans from two trajectories and observe

**P2** · open

**Why it matters.** Whether TBC warns, prevents or silently permits is not stated

**Evidence.** TBC 11769

*Stage: export · Documents: Manual; SOP; Office*

### T24 · How much run overlap is enough for run-to-run registration?

**P2** · open

**Why it matters.** Trimble states the requirement qualitatively only

**Evidence.** TBC 25096

*Stage: registration · Documents: Manual; SOP; Office*

### T25 · Which feature types are fit for horizontal control, vertical control, or both, at MX60 density and incidence?

**P1** · open

**Why it matters.** Will shape control design more than any software setting

**Evidence.** TBC 22905

*Stage: project setup · Documents: Manual; SOP*

### T26 · Does exported imagery inherit or otherwise reflect a registration adjustment?

**P2** · open

**Why it matters.** Imagery is positioned from the trajectory; nothing states whether it is recomputed

**Evidence.** TBC 22638

*Stage: QC · Documents: Manual; SOP; Office*

### T27 · What imagery streams actually exist on the MX60, and which are exposed through TBC export?

**P2** · open

**Why it matters.** The MX60 export tree shows no Planar cameras while the side-images option persists

**Evidence.** TBC 23339; TBC 22501

*Stage: QC · Documents: Manual; Office*

### T28 · Does Cleanup delete sbet_*_reg_####.out from storage, or only remove the project objects?

**P1** · open

**Why it matters.** Determines what must be archived before Cleanup. Distinguish project object retention from underlying file retention

**Evidence.** TBC 26466; TBC 22905

*Stage: cleanup · Documents: Manual; SOP; Office*

### T29 · Establish the reliable export-state verification method for each export path

**P1** · open

**Why it matters.** How an export dialog resolves its selection is not documented

**Evidence.** TBC 22638; TBC 11769

*Stage: export · Documents: Manual; SOP; Office*

### T30 · Attempt both reconstruction paths - timestamp matching and trajectory geometry comparison - on a dataset with two candidate trajectories

**P3** · open

**Why it matters.** Neither has been attempted; both are the fallback if provenance is queried

**Evidence.** TBC 23339; TBC 22501

*Stage: provenance · Documents: Manual; SOP; Office*

### T31 · Does a predicted GNSS environment (almanac PDOP, canopy, urban canyon) correlate with achieved trajectory RMS on this system? Drive a route with a range of predicted conditions and compare the prediction against the RMS colouring afterwards.

**P2** · open

**Why it matters.** No Trimble source relates predicted GNSS conditions to achieved trajectory quality for the MX60. Establishing it would turn mission planning from judgement into estimate, and would let control density be set from the prediction rather than after the fact.

**Evidence.** No source. MX60 UG Rev B p.56 publishes performance at no outage and at 60 s outage only

*Stage: mission planning · Documents: Manual; SOP; Field*

### T32 · Run the TBC Boeing Bump Index report end to end on an MX60 dataset: what inputs does the command take, what does it output, and does the vertical quality of an ordinary run support an FAA profile?

**P1** · open

**Why it matters.** TBC ships the analysis under Mobile Mapping - Analysis - Boeing Bump Index and it is a sellable deliverable. Nobody here has run it. The open question is not whether the tool exists but whether our vertical trajectory supports the profile it computes from, which is answered by validating against pavement control, not by the nominal accuracy

**Evidence.** TBC 29599; FAA AC 150/5380-9; nav tree capture sources/tbc-help-captures/_nav-tree-mobile-mapping.png

*Stage: QC · Documents: Manual; SOP; Office*

### T33 · Work through the six TBC mobile mapping commands this document set does not cover: Run a Batch Command, Create CAD Entities on Mobile Mapping Data, Create Orthomosaics from a Back-Camera system, Import Ortho Lane Images, Inspect Pavement Condition, and Import and Export Road Segments in AgileAssets

**P2** · open

**Why it matters.** Every one appears in the TBC Mobile Mapping navigation tree and none is documented here. They are the downstream, product-making half of the module - the half that maps to sellable deliverables - so the set currently explains how to produce a registered point cloud and stops

**Evidence.** sources/tbc-help-captures/_nav-tree-mobile-mapping.png

*Stage: export · Documents: Manual; Office*

---

## E2 · Vendor clarification required

*Not answerable from the documentation held. Each is a question for Trimble or for the dealer.*

### V-1 · When Export timestamps causes reprocessing from raw data, which trajectory is used?

**P1** · open

**Why it matters.** A direct yes/no question with the largest consequence in the workflow

**Evidence.** TBC 23339; TBC 22501

*Stage: export · Documents: Manual*

### V-2 · Is the MX60 laser control presented as Measurement Prog plus Line Speed, or a combined Laser Mode? Which TMI version applies?

**P2** · open

**Why it matters.** The Quick Start Guide and TMI Rev L disagree - CONFLICT-005

**Evidence.** MX60 QSG Rev B p.10; TMI UG Rev L p.29

*Stage: acquisition · Documents: Manual; Field*

### V-3 · Which TBC version is installed on our workstation?

**P2** · open

**Why it matters.** Two version-dependent behaviours, both legacy - 5.21 and 5.80 predate the oldest published release note

**Evidence.** TBC 24886; TBC 27248

*Stage: system · Documents: Manual*

### V-4 · Confirm the configuration from the serial number, and state whether GAMS and DMI are fitted and which rack is on the vehicle

**P1** · open - part answered

**Why it matters.** Confirms the owner's statement that this is a Premium, and answers the remainder of D-2. Imagery and accuracy commitments now rest on that statement until it is checked

**Evidence.** MX60 UG Rev B p.12,68

*Stage: system · Documents: Manual; SOP*

> **Resolved 2026-09-19 (part).** Configuration stated by the system owner 2026-09-19 as MX60 Premium - not yet checked against the serial number. GAMS, DMI and rack still unanswered

### V-5 · Accessory manuals not held - Trimble GAMS Antenna Kit and DMI Installation and Operation Manuals

**P2** · open

**Why it matters.** Needed for the lever-arm procedure if fitted. The DMI manual has the scale factor for the measured wheel diameter

**Evidence.** MX60 UG Rev B p.42,43

*Stage: field preparation · Documents: Manual; Field*

### V-7 · Does the Lateral Range Limit affect accuracy, or is it purely a data-volume tool?

**P3** · open

**Why it matters.** Undocumented

**Evidence.** TMI UG Rev L p.29

*Stage: acquisition · Documents: Manual; Field*

### V-8 · What is the MX60 actual camera complement, and which streams are exposed through TBC export?

**P2** · open

**Why it matters.** Pairs with T27

**Evidence.** TBC 23339; TBC 22501

*Stage: system · Documents: Manual*

### V-9 · Does LiDAR QC have its own POSPac dependency?

**P2** · open

**Why it matters.** Trimble does not state one but directs configuration questions to Applanix Support

**Evidence.** TBC 28972

*Stage: trajectory processing · Documents: Manual; Office*

### V-10 · Which trajectory do TMX export and Publish to TRCPS send when a run has both an imported and a registered trajectory?

**P1** · open

**Why it matters.** Both carry trajectory geometry; neither says which

**Evidence.** TBC 22501; TBC 29527

*Stage: export · Documents: Manual; Office*

### V-11 · Which report contains the signed GCP residuals added in TBC 2025.21?

**P2** · open

**Why it matters.** The only mobile mapping report topic does not mention residuals

**Evidence.** TBC RN 2025.21; TBC 23991_1

*Stage: QC · Documents: Manual; SOP; Office*

### V-12 · Does any TBC export write the source trajectory into a LAS header, VLR or sidecar?

**P1** · open

**Why it matters.** The one provenance question documentation cannot answer

**Evidence.** TBC 11769

*Stage: provenance · Documents: Manual*

### V-13 · Does removing and refitting the Sensor Unit disturb the calibration? What symptoms indicate drift?

**P1** · open

**Why it matters.** Determines whether calibration is periodic or routine

**Evidence.** MX60 UG Rev B p.7

*Stage: calibration · Documents: Manual*

### V-14 · Is the retro-reflective target check the recommended periodic verification for the MX60, and at what interval?

**P2** · open

**Why it matters.** Trimble says regularly and defines nothing

**Evidence.** MX60 UG Rev B p.7

*Stage: calibration · Documents: Manual; SOP*

### V-15 · Scanner field of view - 346 degrees (UG p.54) or 360 degrees (spec sheet p.2)?

**P3** · open

**Why it matters.** Matters for occlusion geometry - CONFLICT-002

**Evidence.** MX60 UG Rev B p.54; Spec sheet p.2

*Stage: system · Documents: Manual*

### V-16 · When should PFIX be preferred over registration?

**P2** · open

**Why it matters.** This document framing of the distinction is inferred, not stated by Trimble

**Evidence.** TBC 24460; TBC 22905

*Stage: degraded GNSS · Documents: Manual; Office*

### V-17 · Does the coordinate system without Geoid restriction on TMX export apply to the MX60, or only the MX9?

**P2** · open

**Why it matters.** Stated for the MX9 only

**Evidence.** TBC 22501

*Stage: export · Documents: Manual*

### V-18 · Is the 30-minute minimum mission time enforced by TMI, and what is the reason for it?

**P3** · open

**Why it matters.** Trimble states it as a requirement in two places and gives no reason and no indication whether the software prevents a shorter mission. A crew that has to abandon a mission at 20 minutes needs to know whether the data is unusable or merely suboptimal.

**Evidence.** MX60 QSG Rev B sec 5.4 p.13; sec 6 p.14

*Stage: Field · Documents: Manual; SOP*

---

## E3 · Recording an answer

When one of these is answered, the answer goes into the **master register** —
`deliverables/_control/master-register.csv` — in the `resolution` and `date_resolved` columns, and
the status changes. Then re-run `tools/build-register-views.py`, and this appendix and every other
view update together.

Test results with detail worth keeping — numbers, conditions, what was and was not tried — go in
**Appendix F**, and the register entry points at them.

**Do not answer one of these by editing the manual body alone.** A statement changed in one place
and not in the register is exactly the drift this structure exists to prevent.

---

# Appendix F — Test Results

**Empty on issue.** This appendix is populated as the tests in **Appendix E** are run. It exists
now, with nothing in it, because a test that is run and not written down has to be run again.

## F1 · Why the results live here and not in the body

A test answers a question the manual currently states as open. When one is answered, three things
happen, in this order:

1. **The result is recorded here**, with enough detail that someone else could repeat it
2. **The master register is updated** — `resolution` and `date_resolved` — and the views are
   regenerated (`tools/build-register-views.py`)
3. **The manual body changes**, replacing the open statement with the finding, citing this
   appendix

Doing (3) without (1) and (2) produces a manual that asserts something with no evidence behind it,
which is the thing this whole structure exists to prevent.

## F2 · What a usable record contains

Not a conclusion. A conclusion with its working attached.

| | |
|---|---|
| **Question** | The Appendix E identifier, verbatim |
| **Date and who ran it** | |
| **System state** | TBC version, POSPac version if used, the MX60's configuration and calibration date |
| **Method** | What was actually done, in enough detail to repeat. Including what was *not* varied |
| **Data used** | Which mission, which runs. Where it is now |
| **Result** | The observation. Numbers where there are numbers |
| **What it does not establish** | The boundary of the finding. A test on one corridor in open sky has not established behaviour in an urban canyon |
| **Consequence** | What changes in the Manual, the SOP, or a How To — and whether anything already delivered is affected |

> **The "what it does not establish" row is the one that gets skipped, and it is the one that
> keeps a finding honest.** A single test on a single dataset is evidence, not proof. Recording
> its boundary is what allows the next person to know whether their situation is covered.

## F3 · Tests whose results affect a deliverable already issued

Some of the open questions concern what has already been exported and handed over — most directly
**T18** (whether exporting with timestamps substitutes reprocessed data) and **T19** (which
trajectory travels with a publish or an export).

> **CAUTION**
>
> If one of these tests returns a result that means a past deliverable was not what it was
> believed to be, that is not a documentation problem. Record it here, and escalate it — the
> decision about what to tell a client is not the tester's to make and not this manual's to
> specify.
>
> Who that escalation goes to is an open Parametrix decision (**D-3**, roles and authorities).

## F4 · The record

*No tests have been run. Entries are added below, newest first, one heading per Appendix E
identifier.*

---

# Appendix G — Source Conflicts and Resolutions

Conflicts between two Trimble sources, or between a Trimble source and observed behaviour. Each is
recorded in `reference/mx60-reference-data.csv` under a `CONFLICT-` identifier so that the numbers
on both sides remain traceable.

**None of these blocks work.** Each is a statement that should not be quoted to a client, or put
into a specification, until it is resolved.

| ID | Conflict | Status |
|---|---|---|
| `CONFLICT-002` | Scanner FOV — 346° *(UG p.54)* vs 360° *(spec sheet p.2)* | **V-15** |
| `CONFLICT-003` | Which mounting rack is fitted | **D-2 / V-4** |
| `CONFLICT-004` | Minor numeric discrepancies between sources | Recorded in the CSV |
| `CONFLICT-005` | Laser control presentation — QSG vs TMI Rev L | **V-2** |
| `RESOLVED-001` | Spec sheet vs User Guide laser rates — **system total vs per-scanner, a factor of 2.** QSG confirms TMI uses the User Guide numbering | **Resolved** |
