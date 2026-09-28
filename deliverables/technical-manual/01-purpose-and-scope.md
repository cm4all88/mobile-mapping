# 1. Purpose and Scope

## 1.1 What this manual does

It explains **what the Trimble MX60 and Trimble Business Center are actually doing, why they behave
that way, and how we know.** It is the technical reference behind the SOP and the two How To guides.

It is intentionally **not** the first document handed to a new MX60 operator or processor. The How
To guides carry the operating sequence and troubleshooting path; this manual supplies the deeper
answer when the user needs to understand a behavior, diagnose an abnormal result, or verify the
technical basis of a step.

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

**No prior MX60 specific experience is assumed when this manual is used as a reference.** The
reader is still assumed to know surveying. Trajectories, SBETs, GNSS/INS integration, boresight
calibration, scan generation, registration and mobile LiDAR QC are explained only because they are
specific to operating, processing or troubleshooting this system.

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
| **Learning to operate or process the MX60** | Start in the **Field How To** or **Office How To**. Come here only where the operating guide points you or where something is abnormal |
| **Looking up one behaviour** | The contents, or **Appendix A** — the Trimble source index |
| **Checking a number** | **Appendix B** — the reference dataset is the authority for numbers |
| **Deriving a requirement** | The relevant Part IV section, then the SOP clause it supports |
| **Reviewing after a TBC update** | **Appendix A** — the source index, topic by topic |

> **The In Plain Language boxes are a comprehension layer, not an operator course.** They let a
> reviewer or project manager understand the workflow without working through the technical detail.
> The Field and Office How To guides remain the operating and training path.

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
