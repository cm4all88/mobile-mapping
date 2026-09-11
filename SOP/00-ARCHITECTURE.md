# Parametrix Mobile Mapping SOP — Document Architecture

**Trimble MX60 · Trimble Business Center 2026.10**

**Prepared:** 2026-09-11 · **Status:** Architecture fixed, drafting in progress

This is the build specification for the SOP. It is a working document for whoever drafts,
reviews or maintains the SOP — **it is not part of the issued document.**

---

## 1. What this document is, and what it is not

**It is** a standard operating procedure for mobile mapping production at Parametrix, covering
field acquisition with the Trimble MX60 and office processing in Trimble Business Center,
written so that a competent survey professional who has never operated an MX60 can understand
the workflow, the terminology, the risks, the checks and who is responsible for each.

**It is not** an introduction to land surveying. The reader knows control networks, datums,
residuals, least squares and check points. The SOP explains those only where **mobile mapping
makes them behave differently** — and it does so at the point of difference, not in a primer.

**It is not** a rewrite of the Trimble help. Trimble's topics are the evidence base and are
cited throughout. Where Trimble gives a keystroke sequence that is stable and well documented,
the SOP points to it rather than copying it. Where Trimble gives a setting without a selection
rule, the SOP says so and marks the gap.

### Title

**Mobile Mapping Standard Operating Procedure — Trimble MX60 and Trimble Business Center**

> `analysis/GUIDE-REQUIREMENTS.md` §0 proposed retitling this the *Field, Processing and QC
> Guide*. **That is set aside.** The current instruction consistently calls it an SOP and the
> document is structured as one, with roles, responsibilities, controlled operations and a
> decision register. The earlier note is superseded rather than overlooked.

---

## 2. The five readers

The SOP serves five people with different needs. Every section is written for at least one of
them, and §1.4 of the issued document tells each where to start.

| Reader | Needs from this document | Primary sections |
|---|---|---|
| **Surveyor new to mobile mapping** | What this technology is, what it can and cannot do, how its errors behave | 2, 5, 12, 15, 17, 18, and every *In Plain English* box |
| **Field technician** | What to do at the vehicle, in what order, and what "wrong" looks like | 4, 6, 7, 8, 9, 10, App. A–C |
| **Office technician** | The processing chain, settings, what each command actually changes | 11–16, 18–22, App. D–F |
| **Project surveyor** | Whether the result meets the project's accuracy requirement and how that was demonstrated | 5, 15, 17, 18, 23, 24 |
| **Project manager** | What was done, what it cost in time, whether the deliverable is defensible | 1, 3, 23, 24, 25, and the *In Plain English* boxes alone |

> **A PM should be able to read only the section headings and the *In Plain English* boxes and
> come away with a true picture.** That is a design constraint on those boxes, not a nicety.

---

## 3. Structure — 27 sections and 8 appendices

The order follows the **production workflow**, not the TBC help hierarchy. Two structural
decisions are worth stating.

**Calibration sits at §14, between Generate Scans and Registration.** It is not a per-project
step — it is periodic, and it belongs to the system rather than the job. It sits there because
TBC's calibration requires generated scans as an input and because a reader meeting
registration at §15 must already understand what boresight angles are. §14 opens by saying so.

**Degraded GNSS (§20) is a branch, not a stage.** Two of its three remedies loop *backwards* —
PFIX returns to trajectory processing (§12), LiDAR QC belongs inside it. The section is placed
after the normal path is understood and cross-references backwards explicitly. Putting it in
sequence would imply it happens after QC, which is wrong.

### Part I — Orientation

| § | Title | Approx. words | Notes |
|---|---|---|---|
| 1 | **Purpose and Scope** | 900 | Includes the reader-path table from §2 above |
| 2 | **Mobile Mapping in Plain Terms** | 2,000 | The trajectory is the job; error behaviour; what differs from static |
| 3 | **Roles and Responsibilities** | 1,100 | **Almost entirely PARAMETRIX DECISION REQUIRED** |
| 4 | **Equipment and Software** | 1,800 | MX60 configurations, TMI, TBC, POSPac, licensing gates |

### Part II — Before the field

| § | Title | Approx. words | Notes |
|---|---|---|---|
| 5 | **Coordinate Systems, Control, and Project Setup** | 2,200 | Only what mobile mapping does differently — epochs, ITRF00 path, grid/ground at export, geoid restriction |
| 6 | **Mission Planning** | 2,000 | Corridor geometry, GNSS environment, control layout, speed, overlap |
| 7 | **Field Preparation and Preflight** | 1,600 | Mounting, lever arms, power, disk, preflight checks |

### Part III — Acquisition

| § | Title | Approx. words | Notes |
|---|---|---|---|
| 8 | **MX60 Data Collection** | 2,400 | Initialization, the drive, laser and camera settings, ending a mission |
| 9 | **Field Quality Checks** | 1,400 | What can be verified before leaving site, and what cannot |
| 10 | **Data Transfer and Project Organization** | 1,200 | Offload, integrity, folder structure — **structure is a Parametrix decision** |

### Part IV — Office processing

| § | Title | Approx. words | Notes |
|---|---|---|---|
| 11 | **Import into TBC** | 1,400 | `.mxdb`, the data object chain, what import does and does not do |
| 12 | **Trajectory Processing** | 2,600 | POSPac vs in-TBC, settings, licensing gate, LiDAR QC, SBET naming and the ITRF00 trap |
| 13 | **Generate Scans** | 2,000 | TMX→RWCX, filters, colorization, the Results record |
| 14 | **Calibration** | 2,200 | Boresight vs lever arm, laser and camera, the JSON, calibration record and date |
| 15 | **Registration** | 3,200 | **The core section.** Register a Run, Register a Mission, methods, Use XY / Use Z / As Check, target picking, residuals |
| 16 | **Run to Run Registration** | 1,600 | Cloud-to-cloud, reference vs adjust, the 20 m RMS statistics |
| 17 | **Control and Independent Check Points** | 1,800 | How control participates; why not everything can be a check |
| 18 | **Point Cloud QC** | 2,400 | Indicators at four levels; the RMS asymmetry; Cutting Plane View |
| 19 | **Imagery QC** | 1,200 | Resolution by configuration, coverage, blur, corrupted images |
| 20 | **Degraded GNSS Conditions** | 2,000 | Three remedies, what each costs, the branch diagram |
| 21 | **Cleanup Mobile Mapping Mission** | 1,400 | **Controlled destructive operation.** Prominent warning |

### Part V — Delivery and closeout

| § | Title | Approx. words | Notes |
|---|---|---|---|
| 22 | **Export and Deliverables** | 2,400 | Five MX60 paths + TRCPS; scaling; the timestamp reprocessing hazard |
| 23 | **Data Provenance and Audit Trail** | 2,200 | The partly-confirmed finding, the table, what to record |
| 24 | **Final QA/QC** | 1,600 | The acceptance framework — structure without numbers |
| 25 | **Archiving and Records** | 1,400 | What is retained, for how long — **decision** |
| 26 | **Troubleshooting** | 2,000 | Field and office, symptom-first |
| 27 | **Terminology** | 1,800 | Full glossary, promoted out of the appendices |

### Appendices

| App. | Title | Notes |
|---|---|---|
| A | **Working Checklists** | Thirteen, standalone |
| B | **TMI Status and Warning Reference** | Carried forward from v1 |
| C | **Office Processing Checklist** | New — mirrors §11–22 |
| D | **Parametrix Decision Register** | Every open decision, prioritised |
| E | **Field Testing Register (T-items)** | T7, T9–T23 with method and priority |
| F | **Vendor Questions** | Mirrors `analysis/VENDOR-QUESTIONS.md` |
| G | **Trimble Source Index** | Every cited topic, with its TBC version |
| H | **First-Day Training Exercise** | Carried forward from v1 |

**Target:** ~52,000 words of body text plus appendices. Larger than v1 by design — the
registration, provenance and export material did not exist in v1.

---

## 4. The two-level convention

Every major technical section carries both levels. Neither substitutes for the other.

### Technical Procedure

The default voice of the document. Detailed, cited, complete: workflow, terminology, settings,
commands, warnings, evidence and decision points. Written for the technician who will execute
it and the surveyor who will defend it.

**This level is never simplified to make the plain-language box easier to write.**

### In Plain English

A short closing box. Addressed to an experienced land surveyor who is new to mobile mapping,
and answering four questions in order:

1. **What we just did**
2. **Why it matters**
3. **What can go wrong**
4. **What good results generally look like, in practical terms**

**Rules:**

- **Re-explain; do not compress.** A shortened restatement of the section above fails. Come at
  the idea from a different direction
- **Ordinary language.** Any term used has already been defined
- **Analogies where they genuinely help.** A forced analogy is worse than a plain sentence
- **Assume real competence.** Never explain what a residual is. Do explain what TBC means by a
  *Registration Trajectory*
- **"What good looks like" is practical, not numerical.** Parametrix tolerances do not exist
  yet, and the box must not invent them. Describe the *shape* of a good result — a cutting
  plane where two runs sit on top of each other, residuals that do not grow with distance from
  control — not a number

> The fourth question is the one that will be got wrong. It is not "state the tolerance." It is
> "tell a competent surveyor what a sound result looks and feels like, so that an unsound one
> stands out."

---

## 5. Evidence discipline — the tag system

Every statement that becomes an instruction is tagged. This is the discipline that keeps the
document defensible, and it is not decorative.

| Tag | Meaning | Where the authority comes from |
|---|---|---|
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble states this, in a cited topic or manual | Trimble |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software or in a captured screenshot, but not stated as procedure by Trimble | Observation |
| **PARAMETRIX PROCEDURE (PROPOSED)** | This document recommends it. **Not yet adopted.** | Nobody yet |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Signed off by Parametrix, with a date and an owner | Parametrix |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make; the SOP states the question and the options | Nobody yet |
| **FIELD TESTING REQUIRED** | Answerable by testing, not by reading. Cross-referenced to a T-item in Appendix I | Nobody yet |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble. Cross-referenced to Appendix I | Nobody yet |

### The PROPOSED / ADOPTED split, and why it exists

The instruction says not to silently convert Trimble defaults into Parametrix requirements, and
not to convert software behaviour into company procedure. Taken strictly, that would leave a
document with no Parametrix procedure in it at all — because **as of this writing, Parametrix
has adopted none.** That document would be accurate and nearly useless.

The split resolves it. Every recommendation this SOP makes is tagged **PROPOSED** and is
visibly not yet company policy. Parametrix converts a proposal to **ADOPTED** by deciding it,
and the decision is recorded in Appendix H with a date and an owner.

> **On first issue, every Parametrix procedure in this document is PROPOSED.** There are no
> ADOPTED entries. That is the honest state, it is stated in §1, and it is the work the
> document exists to make possible.

### Rendering

Tags appear as a bold label at the head of the paragraph or block they govern, in the same
family as the existing callouts. `PARAMETRIX DECISION REQUIRED` already has a callout style;
the others are added to the build scripts before drafting completes.

Where a whole section is governed by one tag, it is stated once under the heading rather than
repeated on every paragraph.

### Citation format

`*(TBC 22905)*` for a help topic · `*(MX60 UG Rev B, p.54)*` for a manual page ·
`*(TBC RN 2025.21)*` for a release note. Every cited topic is listed in Appendix G with the
TBC version it was captured from.

**`reference/mx60-reference-data.csv` remains the authority for numbers.** The prose explains
what they mean. When a Trimble revision changes a value, the CSV row changes and the prose
usually does not.

---

## 6. Callouts

Eight, unchanged from v1 except in emphasis.

| Callout | Use |
|---|---|
| **CAUTION** | Safety, or irreversible data loss |
| **IMPORTANT** | Gets the job wrong if ignored |
| **FIELD TIP** | Practical, learned, non-obvious |
| **WHY THIS MATTERS** | Short inline explanation of one procedure |
| **PARAMETRIX DECISION REQUIRED** | An open decision, stated as a question |
| **ADVANCED** | Depth a first-time reader can skip |
| **IN PLAIN ENGLISH** | The closing box, §4 |
| **WHAT YOU SHOULD KNOW BEFORE MOVING ON** | End of each Part, not each section |

> **WHY THIS MATTERS and IN PLAIN ENGLISH must not duplicate each other.** The first is inline
> and covers one procedure; the second closes a section and re-explains the whole of it. Where a
> section's WHY THIS MATTERS already carries the comprehension load, the closing box goes
> somewhere else conceptually.

---

## 7. The four findings that must survive drafting

These are the results the evidence work produced. Each has a specific section that owns it, and
none may be softened for readability.

### 7.1 The RMS asymmetry — §18, referenced from §14, §15, §16, §24

Trimble's documented position, stated in identical wording in two separate topics
*(TBC 24886, 25096)*:

> Good RMS values do not prove that a calibration or registration succeeded. Poor RMS values
> indicate that it failed. **A visual check is necessary.**

**The SOP must not contain any statement of the form "RMS below X equals pass."** Where an
acceptance rule is needed, the section sets out the *framework* — numerical residuals,
independent check information, visual inspection, project accuracy requirement — and marks the
threshold **PARAMETRIX DECISION REQUIRED**.

### 7.2 Cleanup is destructive and not undoable — §21

*(TBC 26466)*. It keeps the most recent registration and its scans and removes the rest,
including the record of earlier attempts. Trimble recommends a project backup first and
**recommends nothing else** — no export, no report, no archive step.

**No rule of the form "always clean up" or "never clean up" may appear.** The section is built
around the question: *when may Cleanup be performed, by whom, and what must be archived first?*
A recordkeeping framework is offered as **PROPOSED**, never as adopted policy.

### 7.3 Export provenance — §22 and §23

**Partly confirmed**, and this no longer represents missing documentation. All known MX60
export and publish paths have been reviewed.

| Export / publish path | Trajectory travels with output? | Specific trajectory identified? |
|---|---|---|
| Classified LAS, Trajectory Split | No | No |
| Export to TMX | **Yes** | **Not documented** |
| TopoDot | No | No |
| Solv3D | No | No |
| Generic Point Cloud Export | No | No |
| Publish to TRCPS | **Yes, mandatory** | **Not documented** |

Metadata that *is* carried, where applicable: coordinate system and scale factor in a `.txt`
sidecar; the project's global CRS via the ECEF option; GPS Time per point; TBC identified in
image EXIF; and the trajectory geometry itself on the two paths above.

**The SOP must state explicitly:** Trimble documentation does not establish that exported data
uniquely identifies the adjusted trajectory used to create it, and Trimble documentation does
not fully enumerate LAS header fields or VLR content. **The remaining question is therefore a
software-behaviour testing issue, not an unresolved documentation research issue.** Cross-refer
T18–T23.

### 7.4 Export timestamps and reprocessing from raw — §22, flagged in §13 and §24

Trimble states, identically in two export topics *(TBC 23339, 22501)*:

> "If the TIMESTAMP option has been set to **No**, the exported scans are the ones processed
> with the Generate Scans feature… If the TIMESTAMP option has been set to **Yes**, the
> exported scans are **reprocessed from the raw data** and directly written to the LAS format
> files."

Every quality step in the workflow — registration, Update Scans, filtering, colorization —
acts on the **generated** scans. **Which trajectory the reprocessing uses is not stated**, and
both readings are consistent with Trimble's wording.

**This must be carried as an open, prominent hazard**, not resolved by assumption in either
direction. It is **T18**, the highest-priority test in the register, and a vendor question. §22
carries the full treatment; §13 notes that the scans it produces may not be the ones exported;
§24 requires the question be settled before an export procedure can be signed off.

---

## 8. Registration — the correctness requirement for §15 and §16

The three commands are **not interchangeable** and the SOP must never imply otherwise.

| Command | Constraint used | Scope | Section |
|---|---|---|---|
| **Register a Run** | Surveyed GCPs matched to targets picked in the point cloud | One run | §15 |
| **Register a Mission** | The same, with GCP *instances* per 250 m scan section, each GCP reusable across runs and passes | A set of runs at once | §15 |
| **Register Run to Run** | Cloud-to-cloud overlap against a **Reference Run** whose trajectory does not change | Pairs, batched | §16 |

**Control participation** must be explained as three independent choices per point
*(TBC 22905, 26473)*:

- **Use XY** — the horizontal coordinates of this point are optimised
- **Use Z** — the vertical coordinate is optimised
- **As Check** — the point is a **validation point**. It is still paired with a picked target,
  and its XYZ residuals are computed, but **they are not taken into account in the
  registration**

And the constraint that follows: **TBC does not permit every selected point to be a check
point**, because the adjustment still requires control. Setting all of them raises an error.

> This is the conventional control/check split, implemented per point and per component. A
> surveyor needs no explanation of why check points matter — only of how TBC expresses it.

---

## 9. Drafting order

Not the reading order. Sections are drafted where the evidence is strongest and the
dependencies resolve.

| Block | Sections | Why this order |
|---|---|---|
| **1** | 1, 2, 3, 4 | Fix the voice, the audience and the tag system on easy ground |
| **2** | 15, 16, 17 | The hardest and most load-bearing material, drafted while fresh |
| **3** | 11, 12, 13, 14 | The processing chain that leads into it |
| **4** | 18, 19, 20, 21 | QC and the branch cases, which depend on 15–17 |
| **5** | 22, 23, 24 | Delivery and provenance, which depend on everything |
| **6** | 5, 6, 7, 8, 9, 10 | Field sections — largely carried forward from v1 and revised |
| **7** | 25, 26, 27 | Closeout, troubleshooting, terminology |
| **8** | Appendices A–H | Assembled last, from the body |

---

## 10. Acceptance criteria

The SOP is ready for Parametrix review when:

- [ ] All 27 sections and 8 appendices drafted
- [ ] Every major technical section ends with **In Plain English** answering all four questions
- [ ] Every instruction carries an evidence tag; no untagged imperative survives
- [ ] **No PARAMETRIX PROCEDURE (ADOPTED) entries exist** — correct on first issue
- [ ] No numerical acceptance tolerance is stated anywhere
- [ ] The RMS asymmetry appears in §14, §15, §16, §18 and §24 and is never contradicted
- [ ] Cleanup carries no "always" or "never" rule
- [ ] The export provenance table appears in full, with the testing-not-research framing
- [ ] The timestamp reprocessing hazard appears in §13, §22 and §24
- [ ] The three registration commands are never described as interchangeable
- [ ] Every Trimble statement is cited to a topic or a page
- [ ] Every open item appears in Appendix I — none only in the body
- [ ] Parametrix branding applied (`analysis/GUIDE-REQUIREMENTS.md` §1), once, at the end

---

*Architecture fixed 2026-09-11. Drafting proceeds per §9.*
