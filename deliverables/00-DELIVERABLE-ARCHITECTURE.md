# Parametrix MX60 Mobile Mapping — Four-Deliverable Architecture

**Proposal. Nothing has been split yet.**
**Prepared:** 2026-09-11 · Against the 71,800-word single-document draft in `../SOP/`

---

## 0. The organising idea

The current document works because it is complete. It does not work as four documents because it
mixes four *kinds* of content on every page:

| Kind | Answers | Currently |
|---|---|---|
| **Explanation** | Why does the system behave this way? | Interleaved |
| **Evidence** | What does Trimble document, and what have we observed? | Interleaved |
| **Requirement** | What does Parametrix demand? | Interleaved, all PROPOSED |
| **Task** | What do I click, in what order? | Interleaved |

The four deliverables are those four kinds, separated:

```
   TECHNICAL MANUAL        explanation + evidence      "why it works, and how we know"
           │
           │ referenced by
           ▼
   SOP                     requirement                 "what Parametrix requires"
           │
           │ supported by
           ├──────────────────────┬──────────────────────┐
           ▼                      ▼                      ▼
   FIELD HOW TO            OFFICE HOW TO          (checklists live in the How Tos)
   task, field             task, office
```

**The test for where anything belongs:** if you removed it, which question becomes unanswerable?
*Why* → Manual. *Must I?* → SOP. *How?* → How To.

---

## A. Technical Manual — table of contents

**Parametrix MX60 Mobile Mapping Technical Manual**
Explains what the system does and why. Carries the evidence base and every **In Plain Language**
box. May remain long.

### Part I — Principles

| § | Title | From |
|---|---|---|
| 1 | Purpose, scope and how to read this manual | §1 (rewritten for this role) |
| 2 | **Mobile mapping in plain terms** — the trajectory is the job | §2.1–2.3 |
| 3 | **How error behaves** — attitude × range, correlation in time, why bad data looks fine | §2.3 (expanded) |
| 4 | **The workflow, end to end** | §2.7 |
| 5 | The data chain — `.mxdb`, SBET, TMX, RWCX, and why the MX60 has no MTA stage | §2.5, §11.3, §13.1 |
| 6 | Terminology | §27 |

### Part II — The system

| § | Title | From |
|---|---|---|
| 7 | MX60 system architecture — sensors, configurations, units | §4.1 |
| 8 | **GNSS/INS integration** — why two sensor types, how they fail, what the filter does | §2.2 (expanded) |
| 9 | GAMS and DMI — what each contributes | §2.2, §12.3 |
| 10 | TMI, TBC, POSPac — and the licensing gates | §4.2–4.4 |
| 11 | LiDAR QC — what it is, what it needs | §4.5, §12.7 |
| 12 | Coordinate systems, datums and epochs **as mobile mapping uses them** | §5.2–5.4, §5.7 |

### Part III — Acquisition, explained

| § | Title | From |
|---|---|---|
| 13 | **Initialization and GAMS** — what the static period and manoeuvres actually solve | §8.3 (expanded) |
| 14 | Why the closing sequence exists — forward and backward filter passes | §2.2, §8.7 |
| 15 | GNSS environment, outage duration, and the 60-second specification boundary | §6.3 |
| 16 | What determines point density and useful range | §8.5, §2.3 |

### Part IV — Processing, explained

| § | Title | From |
|---|---|---|
| 17 | Trajectory processing — settings, what each does, SBET naming and the ITRF00 path | §12 |
| 18 | **Scan generation** — filters, colorization, what each filter removes | §13.1–13.5 |
| 19 | **Update Scans** — why registration does not move points | §13.6 |
| 20 | **Calibration** — boresight vs lever arm, why angular error scales with range, site geometry | §14 |
| 21 | **Registration** — the three commands, the methods, target picking | §15, §16 |
| 22 | **GCPs, check points and residuals** — Use XY / Use Z / As Check | §17 |
| 23 | **RMS and what it can and cannot prove** — the Trimble asymmetry | §18.1–18.3 |
| 24 | Reading trajectory RMS colouring | §12.4, §18.4 |
| 25 | Visual QC — Cutting Plane View, Scan Color, why surfaces hide misalignment | §18.5–18.6 |
| 26 | Imagery — resolution by configuration, colorization, failure modes | §19 |
| 27 | **Degraded GNSS** — the three remedies and what each costs | §20 |
| 28 | **Cleanup Mobile Mapping Mission** — what it destroys | §21.1–21.3 |
| 29 | **Export** — all six MX60 paths, what each carries | §22 |
| 30 | **Provenance** — the chain, the limitation, what can be reconstructed | §23 |
| 31 | Periodic system verification | §18.7 |

### Part V — Evidence

| App. | Title | From |
|---|---|---|
| A | Trimble source index — every cited topic, with TBC version | Appendix C |
| B | **Reference dataset** — 402 records, the authority for numbers | `reference/*.csv` |
| C | Figures and screenshots | Appendix G |
| D | **Observed software behaviour** — consolidated | extracted from all sections |
| E | **Open technical questions** — T-items and V-items, with why each matters | Appendix I Tables 2–3 |
| F | **Test results** — populated as tests are run | *new, empty on issue* |
| G | Source conflicts and resolutions | Appendix C §C5 |

> **The In Plain Language boxes live here and nowhere else.** ~26 of them, one per major technical
> section. They are the manual's comprehension layer and the reason it remains usable by someone
> learning mobile mapping.

---

## B. SOP — table of contents

**Parametrix MX60 Mobile Mapping Standard Operating Procedure**
Defines what Parametrix requires. **The primary controlled procedural document.** Short by
design — it states requirements and points to the manual for explanation.

| § | Title | Content |
|---|---|---|
| **1** | **Purpose, scope and application** | What work this governs; what it does not |
| **2** | **Document control and related documents** | Revision, owner, approver; which manual and How To revisions this SOP is issued with |
| **3** | **Definitions** | Only terms with procedural force — *shall*, *approved*, *retained*, *independent check*. Everything else → Manual §6 |
| **4** | **Roles, responsibilities and authorities** | Who may operate, register, accept, run destructive operations, sign accuracy statements |
| **5** | **Competence and training requirements** | Qualification to operate alone; to register; to accept |
| **6** | **Project setup requirements** | CRS, datum, epoch, accuracy requirement in writing |
| **7** | **Control requirements** | Density, bracketing, **designation of independent checks before processing** |
| **8** | **Mission planning requirements** | Pass pattern, overlap, GNSS assessment, unsuitable segments |
| **9** | **Field acquisition requirements** | Operating limits, stand-down authority, initialization and closing sequence, field record |
| **10** | **Field close-out and handoff** | Verification before leaving site; what must accompany the data |
| **11** | **Data transfer and custody** | Verified copies, retention of source, chain of custody |
| **12** | **Office intake requirements** | What is verified, what is recorded, calibration-state capture |
| **13** | **Processing requirements** | Trajectory and scan generation — what must be done, not how |
| **14** | **Registration requirements** | Authority, the control/check designation, command selection, records. **Its own section** because it is the step that decides whether the deliverable sits where it is supposed to |
| **15** | **Calibration control** | Interval, triggers, currency, records |
| **16** | **QC requirements** | The layered verification; what must be inspected and recorded |
| **17** | **Acceptance and approval** | Acceptance framework, who signs, against what |
| **18** | **Destructive operation controls** | **Cleanup** — authorisation, prerequisites, records |
| **19** | **Export and delivery controls** | The release gate; what must be confirmed before export |
| **20** | **Documentation and records** | What is produced, by whom, where it lives |
| **21** | **Retention and archive** | Tiers, periods, responsibility |
| **22** | **Non-conformance and re-collection** | When work is rejected; who decides |

### SOP appendices

| App. | Title |
|---|---|
| A | **Parametrix Decision Register** — the D-items, and the adoption record |
| B | Required records index — every record the SOP requires, and its home |
| C | Approval and revision history |

> **Every clause carries one of three states:**
>
> | | |
> |---|---|
> | **ADOPTED** | Binding. Recorded in Appendix A with a date and an approver |
> | **PARAMETRIX DECISION REQUIRED** | The requirement is identified; the answer is not set |
> | **TESTING REQUIRED** | The requirement depends on a test result — Manual App. E |
>
> **On first issue, ADOPTED is empty.** The SOP is a complete statement of *what must be decided*
> and, once decided, of *what is required*.

---

## C. Field How To — table of contents

**MX60 Field How To Guide**
Shows field personnel how to perform the work. Usable in or near the vehicle. Highly visual,
task-oriented, minimal theory.

| § | Title |
|---|---|
| **1** | How to use this guide · what to do if something is not covered |
| **2** | **Before you leave the yard** — pre-mission readiness |
| **3** | **Equipment inspection** — what to look at, what "wrong" looks like |
| **4** | **Mounting the Sensor Unit** — two people, seating, securing |
| **5** | **Connections and cable routing** |
| **6** | **Power system checks** — supply, battery, fusing |
| **7** | **Battery Protect** — what the alarm means and how long you have |
| **8** | **Starting the system** — sequence, LEDs, what to wait for |
| **9** | **Connecting to TMI** — and the status colours |
| **10** | **Mission setup** — vehicle settings, capture settings, what to record |
| **11** | **Disk check** |
| **12** | **Navigation initialization** — the sequence, step by step |
| **13** | **GAMS considerations** |
| **14** | **Reading navigation status** — red, orange, green, and what green does *not* mean |
| **15** | **Recording runs** — starting, stopping, minimum mission time |
| **16** | **Driving practices** — speed, smoothness, lane choice, traffic |
| **17** | **GNSS considerations while driving** |
| **18** | **Field QC indicators** — what to watch, what to do about it |
| **19** | **Using Comments** — and why the office needs them |
| **20** | **Stopping and restarting** |
| **21** | **The closing sequence** — and why it cannot be added later |
| **22** | **Shutdown** |
| **23** | **Field close-out** — verification before the vehicle moves |
| **24** | **Re-collect or not** |
| **25** | **Data transfer and handoff** |
| **26** | **What must accompany the data to the office** |
| **27** | **Common problems — what to check first** |

| App. | Title |
|---|---|
| A | **Preflight checklist** — printable |
| B | **End-of-mission checklist** — printable |
| C | **Field record form** — the template |
| D | TMI status and warning reference |
| E | Quick card — the ten things that cost the most if missed |

> **Format:** short numbered steps, a photograph or screenshot per task where it helps, and a
> one-or-two-sentence **Why This Matters** where the reason changes behaviour — each pointing to
> the Manual for the full explanation. **No extended theory.**

---

## D. Office How To — table of contents

**MX60 Office How To Guide**
Shows office personnel how to process and QC. Follows the actual processing sequence. Answers
four questions at every step: *what do I click · what should I look at · what should I expect ·
what should make me stop.*

| § | Title |
|---|---|
| **1** | How to use this guide · the four questions |
| **2** | **Data intake** — receiving, verifying, backing up |
| **3** | **Checking mission information** — covered distance, run count, sensors |
| **4** | **Calibration-state intake** — running and keeping the Mission Report |
| **5** | **Project setup** — creating the project, setting the CRS **before import** |
| **6** | **Coordinate systems** — what to set and what to check |
| **7** | **Importing the mission** |
| **8** | **Trajectory processing** — settings walk-through |
| **9** | **POSPac requirements** — what you need and what to do without it |
| **10** | **Reading the trajectory** — RMS colouring, plots, the SBET filename |
| **11** | **Generate Scans** — filters, colour, generating one run first |
| **12** | **Checking the scans** |
| **13** | **Calibration** — when, and how to run it |
| **14** | **Importing control** |
| **15** | **GCP and check point configuration** — Use XY / Use Z / As Check |
| **16** | **Register a Run** |
| **17** | **Register a Mission** |
| **18** | **Register Run to Run** |
| **19** | **Editing a registration** — and why not to register twice |
| **20** | **Residual review** |
| **21** | **Update Scans** — and confirming it worked |
| **22** | **Visual QC** — Cutting Plane View, Scan Color, working along the corridor |
| **23** | **Imagery QC** |
| **24** | **LiDAR QC** — when it applies and how to run it |
| **25** | **Degraded GNSS** — choosing and applying a remedy |
| **26** | **PFIX** — the two-pass procedure |
| **27** | **Identifying registration results** — trajectory properties, `_reg_####`, SBET files |
| **28** | **Trajectory provenance** — what to record before you go further |
| **29** | **Cleanup Mobile Mapping Mission** — the archive-first sequence |
| **30** | **Export** — by path |
| **31** | **The pre-export check** |
| **32** | **Final QA/QC** — working the ten layers |
| **33** | **Archiving** |
| **34** | **Documentation required for QC and delivery** |
| **35** | **Common problems — what to check first** |

| App. | Title |
|---|---|
| A | **Office processing checklist** — intake to delivery |
| B | **Registration checklist** |
| C | **QC checklist** — the ten layers |
| D | **Export and delivery checklist** |
| E | **Archive and Cleanup checklist** |
| F | Record templates — control/check table, delivery record, QA record |

---

## E. Cross-reference model

### One authoritative home per topic

| Topic | **Owner** | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| How GNSS/INS integration works | **Manual** | ● | — | ref | ref |
| What a trajectory/SBET is | **Manual** | ● | ref | ref | ref |
| Why initialization works | **Manual** | ● | — | ref | — |
| **How to initialize** | **Field How To** | ref | ref | ● | — |
| **That initialization is required** | **SOP** | — | ● | ref | — |
| Filter behaviour, what each removes | **Manual** | ● | — | — | ref |
| **Which filters to use** | **SOP** *(decision)* | ref | ● | — | ref |
| **How to set filters** | **Office How To** | ref | ref | — | ● |
| Registration theory, the three commands | **Manual** | ● | ref | — | ref |
| **Who may register, who accepts** | **SOP** | — | ● | — | ref |
| **How to register** | **Office How To** | ref | ref | — | ● |
| Control vs check, why independence matters | **Manual** | ● | ref | — | ref |
| **Control density, designation rule** | **SOP** | ref | ● | ref | ref |
| The RMS asymmetry | **Manual** | ● | ref | — | ref |
| **Acceptance criteria** | **SOP** | ref | ● | — | ref |
| Cleanup — what it destroys | **Manual** | ● | ref | — | ref |
| **Cleanup authorisation and prerequisites** | **SOP** | — | ● | — | ref |
| **How to run Cleanup safely** | **Office How To** | ref | ● ref | — | ● |
| Export paths, what each carries | **Manual** | ● | — | — | ref |
| **Export release gate** | **SOP** | ref | ● | — | ref |
| **How to export** | **Office How To** | ref | ref | — | ● |
| Provenance chain and limitation | **Manual** | ● | ref | — | ref |
| **Required provenance records** | **SOP** | ref | ● | ref | ref |
| Battery Protect behaviour | **Manual** | ● | — | ref | — |
| **What to do when the alarm sounds** | **Field How To** | ref | — | ● | — |
| Field checklists | **Field How To** | — | ref | ● | — |
| Office checklists | **Office How To** | — | ref | — | ● |
| **Decision register (D-items)** | **SOP App. A** | ref | ● | ref | ref |
| **Test and vendor register (T, V)** | **Manual App. E** | ● | ref | ref | ref |
| Test results | **Manual App. F** | ● | ref | — | ref |

● = owns it · ref = cross-references it · — = does not mention it

### Cross-reference wording — fixed forms

| Use | Form |
|---|---|
| To the Manual | **For technical background, see Technical Manual §X.X.** |
| To the SOP | **For the required company procedure, see SOP §X.X.** |
| To Field How To | **For step-by-step field instructions, see Field How To §X.X.** |
| To Office How To | **For processing instructions, see Office How To §X.X.** |

### Terminology and warnings

- **Manual §6 is the single glossary.** The other three define nothing; they use the terms.
- **A warning is worded once, in its owning document, and quoted verbatim elsewhere** — never
  paraphrased. Candidate shared warnings: the RMS asymmetry, Cleanup's irreversibility,
  registration not reaching the cloud until Update Scans, Export timestamps reprocessing.
- **Stage names are fixed across all four.** The canonical list is Manual §4 (the workflow map):
  *project setup · mission planning · field preparation · acquisition · field QC · transfer ·
  intake · trajectory processing · scan generation · calibration · registration · update scans ·
  QC · degraded-GNSS handling · cleanup · export · final QA/QC · archive.*

---

## F. Where the current 71,800 words go

| Current § | Words | → Manual | → SOP | → Field | → Office | Notes |
|---|---|---|---|---|---|---|
| 1 Purpose and scope | 1,611 | ◐ | ◐ | ○ | ○ | Splits four ways; each gets its own |
| 2 Mobile mapping in plain terms | 2,553 | ●●● | — | — | — | Manual Part I core |
| 3 Roles and responsibilities | 1,538 | — | ●●● | — | — | **SOP §4** |
| 4 Equipment and software | 2,081 | ●●● | ○ | ○ | ○ | Manual Part II |
| 5 Coordinate systems, control, setup | 1,970 | ●● | ●● | — | ○ | Theory → Manual; requirements → SOP §6–7 |
| 6 Mission planning | 1,952 | ● | ●● | ○ | — | Requirements → SOP §8 |
| 7 Field preparation and preflight | 1,880 | ○ | ○ | ●●● | — | **Field How To §2–11** |
| 8 MX60 data collection | 1,949 | ● | ○ | ●●● | — | Theory → Manual §13; steps → Field |
| 9 Field quality checks | 1,252 | — | ● | ●● | — | **Field How To §18, §23** |
| 10 Data transfer and organisation | 1,086 | — | ●● | ● | ● | SOP §11; steps split |
| 11 Import into TBC | 1,300 | ● | ○ | — | ●● | **Office How To §2–7** |
| 12 Trajectory processing | 2,957 | ●●● | ○ | — | ●● | Manual §17; walk-through → Office §8–10 |
| 13 Generate scans | 1,729 | ●● | ○ | — | ●● | Manual §18–19; steps → Office §11–12 |
| 14 Calibration | 2,901 | ●●● | ● | — | ● | Manual §20; control → SOP §14 |
| 15 Registration | 3,367 | ●●● | ○ | — | ●● | **The largest single split** |
| 16 Run to run registration | 2,061 | ●● | ○ | — | ●● | Manual §21; steps → Office §18 |
| 17 Control and check points | 2,084 | ●● | ●● | — | ● | Theory → Manual §22; rule → SOP §7 |
| 18 Point cloud QC | 2,150 | ●●● | ● | — | ●● | Manual §23–25; method → Office §20–22 |
| 19 Imagery QC | 1,815 | ●● | ○ | — | ● | Manual §26 |
| 20 Degraded GNSS | 2,165 | ●●● | ○ | ○ | ● | Manual §27; Office §24–26 |
| 21 Cleanup | 2,036 | ●● | ●● | — | ● | **Split three ways deliberately** |
| 22 Export and deliverables | 3,655 | ●●● | ● | — | ●● | Manual §29; Office §30–31 |
| 23 Provenance and audit trail | 2,556 | ●●● | ● | — | ● | Manual §30; records → SOP §19 |
| 24 Final QA/QC | 2,754 | ● | ●● | — | ●● | Requirements → SOP §15–16; method → Office §32 |
| 25 Archiving and records | 1,380 | — | ●●● | — | ● | **SOP §20** |
| 26 Troubleshooting | 1,599 | — | — | ●● | ●● | **Split by audience** |
| 27 Terminology | 1,631 | ●●● | ○ | — | — | **Manual §6 — the single glossary** |
| App. A Checklists | 2,668 | — | ○ | ●● | ●● | A1–A3 → Field; A4–A13 → Office |
| App. B TMI status | 843 | ○ | — | ●●● | — | **Field How To App. D** |
| App. C Source index | 1,334 | ●●● | — | — | — | **Manual App. A** |
| App. D Training exercise | 1,275 | ○ | ● | ● | ● | **Becomes SOP §5 competence + an exercise in each How To** |
| App. G Figures | 1,150 | ●●● | — | ○ | ○ | **Manual App. C** — figures are shared, catalogued once |
| App. H Adoption record | 507 | — | ●●● | — | — | **SOP App. A** |
| App. I Open items | 3,869 | ●● | ●● | — | — | **D-items → SOP App. A · T and V → Manual App. E** |

●●● primary home · ●● substantial · ● some · ◐ splits evenly · ○ a reference only · — none

### What has to be newly written

| Document | New material |
|---|---|
| **Manual** | §3 error behaviour (expanded from §2.3) · §8 GNSS/INS (expanded from §2.2) · §13 initialization theory (expanded from §8.3) · App. D observed-behaviour consolidation · App. F test results shell |
| **SOP** | Front matter and document control · §3 procedural definitions · §5 competence · §21 non-conformance · App. B required-records index · **the conversion of every PROPOSED practice into a clause with a state** |
| **Field How To** | Task decomposition of §7–§10 into numbered steps · App. C field record form · App. E quick card · photograph list |
| **Office How To** | Task decomposition of §11–§24 into *click / look / expect / stop* · App. F record templates |

> **Roughly 80 % of the existing text moves. Roughly 20 % is new** — mostly the SOP's procedural
> scaffolding and the How To guides' step decomposition, which the current document implies but
> does not spell out.

---

## G. What remains unresolved

The 74 open items, mapped to what blocks them and which document is affected.

| Blocked by | Items | Affects | Consequence |
|---|---|---|---|
| **Management decision** | 34 D-items | **SOP** almost entirely | The SOP can be *written* in full — every clause stated with its decision marked. It cannot be *issued as binding* until the P1 items are decided |
| **Field testing** | T3, T9, T15, T25, T1, T6, T7, T24 | Manual, SOP, Office How To | Filter and registration defaults stay described, not prescribed |
| **Office / software testing** | T18, T28, T29, T19, T21, T22, T23, T26, T27, T30 | Manual App. E–F, Office How To | **T18 gates the export procedure.** Until settled, Office How To §31 says "record the setting" rather than "use this setting" |
| **Licensing confirmation** | D-10, V-3 | All four | Without POSPac, Office How To §8–9 and §26 describe a workflow Parametrix cannot run |
| **Vendor clarification** | 16 V-items | Manual App. E | Mostly descriptive gaps; five are P1 |
| **Acceptance criteria** | D-13 | **SOP §16** | **The single largest blocker.** Acceptance cannot be signed, so the SOP's approval clause is a placeholder |
| **Configuration confirmation** | D-2, V-4 | Manual §7, Office §23 | Imagery specifications cannot be stated for *our* system |

### What this means per document

| Document | Can be completed now? |
|---|---|
| **Technical Manual** | **Yes, essentially in full.** It documents what Trimble states and what we have observed. Open questions are content, not blockers — they belong in App. E and are part of what the manual is for |
| **SOP** | **Written in full; issued as DRAFT.** Every clause present with its state. Becomes CONTROLLED when the nine operation-blocking items are decided |
| **Field How To** | **Yes, with three gaps** — speed policy (D-43), re-drive authority (D-43/D-49), and stand-down authority (D-43). Each appears as "per SOP §9, pending decision" |
| **Office How To** | **Yes, with two gaps** — the export timestamp setting (T18/V-1) and acceptance thresholds (D-13). Both appear as "record and refer" rather than as an instruction |

> **None of the four is blocked from being written.** Only the SOP is blocked from being *issued
> as binding*, and only on nine items.

---

## H. Recommended relative size

Estimated from the existing content, allowing for de-duplication and the new material.

| Document | Words | vs today | Rationale |
|---|---|---|---|
| **Technical Manual** | **38,000 – 44,000** | ~55 % of current + expansion | Holds all explanation, all evidence, all In Plain Language boxes, the glossary, the source index and the figure catalogue. **No reduction in technical detail** |
| **SOP** | **9,000 – 12,000** | new form | Requirements only. Should read in under an hour. The decision register is a further ~4,000 as an appendix |
| **Field How To** | **6,000 – 8,000** | new form | Must be usable in a vehicle. Heavily illustrated — figure count matters more than word count. Target **30–40 printed pages** including checklists |
| **Office How To** | **10,000 – 13,000** | new form | More steps than the field guide and more screenshots. Target **50–60 printed pages** |
| **Total** | **~63,000 – 77,000** | comparable | Duplication removed roughly offsets the new scaffolding |

> **The How To guides are the ones that fail if they get long.** The discipline is that anything
> answering *why* moves to the Manual, leaving a cross-reference. If Office How To passes ~15,000
> words, explanation has leaked back in.

---

## Document control scheme — proposed

> **Superseded on two points.** Document numbers are **not** assigned — Parametrix's actual
> document-control convention has not been established, and the brand guide does not settle it
> (p.5 also forbids abbreviating the company name to "PMX"). Revision conventions are likewise
> open. Temporary descriptive identifiers are used instead. See the master register, **D-1**.

| Field | Manual | SOP | Field How To | Office How To |
|---|---|---|---|---|
| Number | *not assigned — D-1* | *not assigned — D-1* | *not assigned — D-1* | *not assigned — D-1* |
| Revision | *convention open — D-1* | *convention open — D-1* | *convention open — D-1* | *convention open — D-1* |
| Controlled? | Reference | **Yes — controlled** | Supporting | Supporting |
| Owner | System Owner | *D-1* | System Owner | System Owner |
| Approver | Technical reviewer | **Per D-3** | Per SOP §4 | Per SOP §4 |
| Identifies | **Evidence revision** — TBC 2026.10, 38 topics, 402 records | — | **SOP revision supported** | **SOP revision supported** |
| Also carries | — | Which Manual and How To revisions it is issued with | — | — |

> **The SOP is the controlled document.** The other three are issued in support of a stated SOP
> revision. A change to the SOP triggers a review of all three; a change to the Manual triggers a
> review of the SOP only where it touches a requirement.

---

## Branding — applied

Settled by the **Parametrix Brand Guide v6, November 2023**. The visual system is specified once,
in `_control/style/style-system.md`, and all four documents build from a single token file.

| | |
|---|---|
| Palette, typography, logo rules, clear space, spacer arrow, ix formation | Cited to the guide, page by page |
| Monospace type, tables, callouts, iconography, screen behaviour, technical-report cover | **Extensions** — the guide is silent; each is built from brand values and recorded in `_control/style/brand-source-status.md` |
| Document identity | One **secondary** brand colour per document, which the guide permits as a categorisation device (p.18): Manual Clean Blue · SOP Progress Orange · Field How To Future Green · Office How To Optimistic Yellow |

**Branding is not document control.** The guide settles visual identity and nothing else.
Numbering, revision conventions, approval authorities, effective dates, retention and
controlled-copy terminology remain open Parametrix decisions.

---

## Recommended sequence

| Step | Work | Why this order |
|---|---|---|
| 1 | **Approve this architecture** | Everything downstream depends on it |
| 2 | **Technical Manual** | It is the source the other three reference. ~80 % is re-homing existing text |
| 3 | **SOP** | Needs the Manual's section numbers to reference |
| 4 | **Office How To**, then **Field How To** | Both reference Manual and SOP numbering |
| 5 | **Cross-reference pass** | Verify every pointer resolves, as done for the single document |
| 6 | **Branding** | Once, across all four, when content is stable |

> Splitting before the architecture is agreed would mean splitting twice.

---

*Proposal only. The single-document draft in `../SOP/` remains intact and is unchanged.*
