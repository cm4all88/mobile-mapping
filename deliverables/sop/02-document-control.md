# 2. Document Control and Related Documents

## 2.1 What this section is for

A procedure that cannot say which revision of itself was in force on a given date cannot support a
deliverable produced on that date. This section reserves the machinery. **It does not invent it.**

## 2.2 What is not established

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> None of the following is established, and none is invented here:
>
> | | |
> |---|---|
> | **Document identifier** | The scheme, and this document's number |
> | **Revision convention** | Letters, numbers, draft-versus-issued, and how a revision is incremented |
> | **Approval authority** | Who approves an issue, and whether technical and procedural approval are separate |
> | **Effective date rule** | When a revision takes effect relative to its approval, and what happens to work in progress |
> | **Controlled-copy terminology** | Whether copies are controlled, how, and what an uncontrolled copy is called |
> | **Distribution** | Who receives a revision, and how receipt is recorded |
>
> **The Parametrix Brand Guide does not settle these.** It is authoritative for visual identity —
> colour, typography, logo, layout — and says nothing about document control. The two should not be
> confused: applying the brand to this document does not make it a controlled document.

Until D-1 is answered, this procedure carries a **Working Version** on its front matter — a
circulation date, not a revision — and the status **LIVING DRAFT — INTERNAL REVIEW**. The term is
deliberately not *revision*: a Working Version exists so two reviewers can tell whether they are
reading the same text, and it does not become a revision convention by being used.

## 2.3 The document family

Four documents, issued as a set.

| Document | Role | Changes when |
|---|---|---|
| **SOP** *(this document)* | What Parametrix requires | A requirement changes, or a decision is adopted |
| **Technical Manual** | Why the system behaves as it does, and the evidence | The evidence changes — a TBC release, a test result, a vendor answer |
| **Field How To** | Field method and checklists | A field method changes |
| **Office How To** | Processing method | A processing method changes, or TBC changes |

### The rule between them

**This SOP is the governing document.** The other three are issued in support of a stated revision
of it.

| Change | Triggers |
|---|---|
| A change to this SOP | Review of all three supporting documents |
| A change to the Technical Manual | Review of this SOP **only where the change touches a requirement** |
| A change to a How To | No review of this SOP. A How To may not create a requirement |

> **A How To cannot create a requirement.** If a How To states something that must be done and
> this SOP does not require it, one of the two is wrong. Resolve it here, not there.

## 2.4 What binds while this procedure is a draft

Two different things are easily confused, and this procedure keeps them apart.

| | Count at this Working Version |
|---|---|
<!-- derived:binding-summary -->
| **Parametrix-originated requirements adopted** | **0** |
| **Externally binding requirements restated here** | **10** — 7 trimble requirement · 3 equipment limit |
<!-- /derived -->

**Parametrix has adopted nothing.** Every Parametrix-originated clause in this procedure is a
proposal, carries **PARAMETRIX PROCEDURE (PROPOSED)**, and uses **should**. Nothing in this
document becomes company policy by being written down here.

**The externally binding requirements are not Parametrix's and do not wait for Parametrix.** They
are restated here because an operator needs them in one place, not because this procedure creates
them. They would bind an MX60 operator at any company, working from no SOP at all.

The table below is **generated** from `deliverables/_control/binding-requirements.csv`, where each
row carries its exact source quotation. The count is generated with it, so the two cannot drift
apart — and if the evidence audit changes the number, the number changes.

<!-- derived:binding-table -->
| # | Requirement | Authority | Source | SOP | Enforced by |
|---|---|---|---|---|---|
| **1** | Navigation alignment is complete before data logging begins | TRIMBLE REQUIREMENT | MX60 QSG Rev B, §5.3 p.11 — "Navigation alignment must be done first before data logging is allowed!" | §9.2 | Software — TMI does not allow logging until alignment is done |
| **2** | A mission is at least 30 minutes long | TRIMBLE REQUIREMENT | MX60 QSG Rev B, §5.4 p.13 — "Important! A minimum mission time of >=30 min is required." Repeated §6 p.14 | §9.2 | Not established |
| **3** | A ground control point and its picked target are no more than 30 m (100 ft) apart | TRIMBLE REQUIREMENT | TBC 22905 — "NOTE: The distance in a pair of points cannot exceed the allowed maximum distance of 30 meters (or 100 feet)." | §14.5 | Software — stated as an allowed maximum that cannot be exceeded |
| **4** | At least one control point in a registration is not a validation point | TRIMBLE REQUIREMENT | TBC 22905 — "If you set all the selected ground control points (GCPs) as validation points (VPs), an error will pop-up and will prompt you to have at least one ground control point (GCP) for the calculation." | §14.3 | Software — an error blocks the calculation |
| **5** | Data outside the outermost control point is not described as registered to that control | TRIMBLE REQUIREMENT | TBC 22905 — Local is "suitable for a local adjustment of a run, not for systematic error along the run or for adjusting outside the ground control points set" (W-08) | §7.2, §14.5 | None — the software gives no indication of where the adjustment stopped |
| **6** | A calibration is not accepted on RMS alone; a visual check is performed | TRIMBLE REQUIREMENT | TBC 24886 — "Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the other side, bad RMS values mean that the calibration failed." | §15.4 | None |
| **7** | A registration is not judged on its residuals alone; a visual check is performed | TRIMBLE REQUIREMENT | TBC 25096 — the same sentence, word for word, in the run-to-run registration topic | §14.9, §16.7 | None |
| **8** | Vehicle speed does not exceed 110 km/h (68 mph), system operating or not | EQUIPMENT LIMIT | MX60 UG Rev B, p.53 specification table — "Maximum Vehicle Speed (with operating or non-operating system on board) 110 km/h (68 mph)" | §9.4 | None |
| **9** | Supply voltage is kept above the Battery Protect thresholds | EQUIPMENT LIMIT | MX60 UG Rev B, p.27 — audible warning below 10.5 V for longer than 12 s; power cut below 10.5 V for more than 90 s; normal status recovered if voltage rises above 12.0 V within those 90 s | §9.4 | Hardware — the Power Unit cuts power itself (W-11) |
| **10** | The system is operated inside its rated environmental envelope | EQUIPMENT LIMIT | MX60 UG Rev B, p.53 — operating -10 to +50 C, 20-80 % RH, footnote 1: "Not exposed to direct sun and without driving less than 10 km/h (6 mph)" | §9.4 | None |

**Qualifications.** 3 of the 10 carry none. These do.

| # | |
|---|---|
| **2** | Trimble states the requirement but not whether TMI enforces it, and gives no reason. V-18 |
| **3** | The topic states the limit. It does not describe what TBC does when a pair exceeds it |
| **5** | Trimble states the scope of the method, not a prohibition. What follows — that unadjusted data is not described as adjusted — is a statement of fact, not a Parametrix policy choice |
| **7** | Trimble writes "calibration" in both topics. One of the two is a registration topic, which is why it is read as covering both |
| **8** | The specification table states it as the maximum. The body text at p.9 words it "should not exceed" |
| **9** | The roughly 78 s of usable warning is arithmetic from the two published figures, not a Trimble number |
| **10** | The temperature rating is conditional. Stationary or below 10 km/h in direct sun is outside the stated envelope, whatever the air temperature |
<!-- /derived -->

> **CAUTION**
>
> **A documented Trimble method is not in this table.** Trimble's initialization sequence, its
> closing sequence and its in-field checklist are documented method — Trimble writes *"should"*,
> *"it is advised"*, and *"Proposal of a checklist for system operation"*. They carry
> **TRIMBLE DOCUMENTED METHOD** and **should**, and whether Parametrix makes them mandatory is
> **D-56**.
>
> Presenting a manufacturer's method as a manufacturer's requirement borrows an authority the
> manufacturer did not grant. It also makes the real requirements harder to see.

<!-- derived:binding-enforced -->
> **6 of the 10 are enforced by nothing.** Software or hardware stops you breaking 4 of these. The rest are true whether or not anyone notices, which is the harder kind.
<!-- /derived -->

> **This procedure does not authorise an accuracy statement.** It restates what Trimble and the
> equipment require, and it proposes how Parametrix might work. It sets no accuracy tolerance, no
> error budget, and no acceptance threshold, and **D-13** is unresolved. Whoever signs an accuracy
> statement for MX60 work today signs on their own professional judgement (§17.2).

## 2.5 Evidence revision

The Technical Manual carries an **evidence revision** alongside its document revision, recording
the state of the source material rather than the state of the prose: which TBC version, how many
help topics, how many manuals, how many structured reference records.

**This SOP states which evidence revision it was written against** — on the front matter — because
a requirement derived from evidence is only as current as that evidence.

## 2.6 Records this section requires

| Record | Held by | State |
|---|---|---|
| Revision history of this procedure | Appendix C | **D-1** |
| Which supporting revisions were issued with this one | Front matter | **D-1** |
| Distribution and receipt | — | **D-1** |
