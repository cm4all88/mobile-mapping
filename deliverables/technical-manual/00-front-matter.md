# MX60 Mobile Mapping Technical Manual

**Trimble MX60 · Trimble Business Center 2026.10**

<!-- circulation:banner -->
> **LIVING DRAFT — INTERNAL REVIEW**
>
> **This document is a living draft for internal Parametrix review, training, testing and workflow
> development.** It is not an issued Parametrix standard, and it does not replace professional
> judgement, project requirements, safety procedures or approved company policy.
>
> **Items marked Parametrix Decision Required, Proposed, Testing Required or Vendor Clarification
> Required are unresolved.** There are a lot of them, and that is deliberate — an open question is
> shown as an open question rather than filled in with a guess.
<!-- /circulation -->

---

<!-- circulation:how-to-review -->
## How to review this draft

**This is not primarily a copy-editing exercise.** Typos and awkward sentences are worth reporting,
but they are not what this draft needs. Four questions are:

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
<!-- /circulation -->

---

## Document control

> **Provisional.** Parametrix's document-control convention has not been confirmed (**D-1**). The
> block below is a temporary working scheme for this review only; **it is not a Parametrix
> revision convention and must not be treated as one.**

<!-- circulation:working-revision -->
### Working revision — internal draft only

> **This is a temporary working revision scheme, used only while the set is in internal review.**
> It is deliberately **not** a revision letter or number, so it cannot be mistaken for the
> Parametrix document-control convention that **D-1** will establish. When D-1 is answered, this
> block is replaced by the real one.

| | |
|---|---|
| **Document** | **MX60 Mobile Mapping Technical Manual** |
| **Working draft** | `2026-09-11-a` — date of circulation, plus a letter for same-day reissues |
| **Supersedes** | — first circulated draft |
| **Status** | **LIVING DRAFT — INTERNAL REVIEW.** Not issued, not approved |
| **Circulated for** | Internal review, training, testing and workflow development |
| **Prepared by** | MX60 mobile mapping documentation project |
| **Document identifier** | *Not assigned* — **D-1** |
| **Formal revision** | *Not assigned* — **D-1** |
| **Owner** | *Not assigned* — **D-1** |
| **Approved by** | **Nobody.** This draft is not approved and not issued |
| **Comments to** | *Not assigned* |
| **Set circulated together** | Technical Manual · SOP · Field How To · Office How To, all at `2026-09-11-a` |
<!-- /circulation -->

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
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble documents this, in the cited topic or manual page. **It records what Trimble says, not how strongly.** Where a statement is a Trimble *requirement*, the SOP says so and cites it there — see SOP §2.4 |
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

## In Plain English

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
