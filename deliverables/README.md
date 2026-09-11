# MX60 Mobile Mapping — Internal Review

**Working Version `2026-09-11-a` · LIVING DRAFT — INTERNAL REVIEW**

These four documents are a living draft for internal Parametrix review, training, testing and
workflow development. **They are not an issued Parametrix standard**, and they do not replace
professional judgement, project requirements, safety procedures or approved company policy.

**Some of what is in them binds anyway.** Ten requirements come from Trimble or from the equipment
itself — they would bind an MX60 operator at any company, working from no SOP at all. They are
listed with their sources at **SOP §2.4**. Everything Parametrix-originated is a proposal:
**Parametrix-originated requirements adopted: 0.**

---

## Open this one

| You are | Open | Start at |
|---|---|---|
| **A field operator** | **Field How To** | The **Quick Card** (Appendix E), then the **Preflight Checklist** (Appendix A) |
| **An office processor** | **Office How To** | §1, then the section for the step you are on |
| **A surveyor new to mobile mapping** | **Technical Manual** | §4 *The workflow end to end*, then the **In Plain English** box at the end of each section |
| **A PLS or QA reviewer** | **SOP** and the **Technical Manual** | SOP §2.4, §16, §17 — what binds, what QC is, what acceptance is not |
| **A manager or policy reviewer** | **SOP** and the **decision register** | SOP §17.2 (**D-13**), then SOP Appendix A |

**Everyone should read the front matter of whichever document they open.** It is short, and it says
what the document is and is not.

---

## What feedback matters

**This is not primarily a copy-editing exercise.** Four questions matter:

| | |
|---|---|
| **1** | **Is anything technically wrong?** |
| **2** | **Is anything impractical in actual field or office use?** |
| **3** | **Is anything presented more strongly than Parametrix has actually decided?** |
| **4** | **What would prevent you from performing the work using these documents?** |

**Question 3** is the one this project is least able to catch on its own. **Question 4** finds gaps,
and a gap is more useful than a correction.

### How to comment

**Identify the document and the section.** For example: `Field How To §17.3`, `Office How To §31`,
or `SOP D-13`.

Every section and subsection is numbered, and warnings (`W-n`), open decisions (`D-n`), tests (`Tn`)
and vendor questions (`V-n`) carry identifiers that mean the same thing in all four documents.

**Comments go to the MX60 Internal Review Log** — `_control/mx60-internal-review-log.md`. There is
no document owner to send them to yet; that is **D-1**.

---

## The documents

| | Answers | Words |
|---|---|---|
| **[Technical Manual](technical-manual/technical-manual.html)** | Why does it work this way? What is the evidence? | ~58,000 |
| **[SOP](sop/sop.html)** | Must I? And on whose authority? | ~23,000 |
| **[Field How To](field-how-to/field-how-to.html)** | How do I do it in the vehicle? | ~12,000 |
| **[Office How To](office-how-to/office-how-to.html)** | How do I do it in TBC? | ~18,000 |

**The SOP governs.** A How To cannot create a requirement; if one says something must be done and
the SOP does not require it, the SOP is right and the How To is wrong — that is a Q1 comment.

### Print on its own

Four Field sheets are built to print without the browser navigation:
**Preflight Checklist** · **End-of-Mission Checklist** · **Field Record Form** · **Quick Card**
(Field How To appendices A, B, C and E). Each carries the Working Version and the Living Draft
status on the page.

---

## What is deliberately unresolved

**Open questions are shown as open questions.** There are 77 of them — 36 Parametrix decisions,
25 tests and 16 vendor questions — tracked in one register at
`_control/master-register.csv` and surfaced as filtered views in the documents. No document carries
an item's status independently.

**Almost none of them blocks anything.** The exceptions are listed at `_control/views/blocking.md`.

### D-13, which is the one people ask about

**D-13 blocks formal acceptance.** It does not block collection, exploratory processing,
registration testing, comparison against control, training or workflow development.

The unresolved question is: *until a general Parametrix acceptance standard exists, may MX60 work be
accepted against a project-specific written accuracy requirement, using independent check evidence,
visual QC and documented professional judgement?* Options **A**, **B** and **C** are set out at
**SOP §17.2** and **this draft does not choose between them.**

**No numerical acceptance tolerance appears anywhere in these documents**, because Trimble publishes
none and none has been established by test. Inventing one would be worse than the gap.

---

## Control artefacts

Not reader material, but this is where the machinery lives.

| | |
|---|---|
| `_control/master-register.csv` | The one register of open items. Documents carry filtered views, never their own copies |
| `_control/binding-requirements.csv` | The ten externally binding requirements, one source quotation each. SOP §2.4 is generated from it |
| `_control/authority-model.md` | What makes a statement binding, and on whose authority |
| `_control/warning-register.md` | Registered warnings, and the verbatim wording each must carry |
| `_control/ownership-matrix.md` | Which document owns each topic, and which only reference it |
| `_control/workflow-stage-names.md` | The frozen stage names, identical in all four documents |
| `_control/style/` | The shared visual system, cited to the Parametrix Brand Guide v6 |
| `_control/circulation/` | The Living Draft banner, review panel and Working Version block — one source, four documents |
| `_control/living-draft-change-log.md` | What changed at each Working Version, and why |
| `_control/mx60-internal-review-log.md` | The comment log template |
| `_control/figure-production-register.md` | Figures still to be produced. Project material |

Run `python3 tools/check-all.py` before circulating anything. It is the gate.
