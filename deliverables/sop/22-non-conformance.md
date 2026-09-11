# 22. Non-conformance and Re-collection

## 22.1 What counts

A non-conformance is a departure from a **shall** in this procedure, or a dataset that does not
meet the project's accuracy requirement (§17).

It is not a non-conformance to be unable to meet a requirement that has not been adopted. At this
revision that covers most of this document, which is a reason to answer the decisions rather than a
reason to relax.

## 22.2 Raise it, do not absorb it

**Anyone who identifies a non-conformance raises it.** The person who finds it is frequently the
person who caused it, and the procedure is designed so that raising it is the normal thing to do.

> **A non-conformance that is fixed quietly leaves no trace that the workflow failed** — which
> means it will happen again, to somebody else, on a job where it costs more.

## 22.3 The two categories

| | |
|---|---|
| **Recoverable in the office** | Reprocess the trajectory, regenerate scans, re-register, re-export. Costs hours. **Requires that the raw data was retained** (§21) |
| **Recoverable only in the field** | Missing coverage, missing overlap, a mission with no closing sequence, a weak initialization. Costs a mobilisation |

The second category is why §10 exists: **the field stage is the only stage with no office remedy**
*(Technical Manual §5.5)*.

## 22.4 Re-collection

> **PARAMETRIX DECISION REQUIRED · D-3, D-34**
>
> **Who decides that a dataset is rejected and that re-collection is required, and who bears it?**
>
> The decision is uncomfortable and is therefore the one most likely to be deferred until it is
> more expensive. Naming the decision-maker in advance is most of the control.

## 22.5 When a segment cannot be served

Where a corridor segment produces an unacceptable trajectory and no remedy applies, the honest
finding is that **mobile mapping may not be the appropriate acquisition method for that segment**.

> **PARAMETRIX DECISION REQUIRED · D-34**
>
> The decision rule: who decides, against what, and what the client is told. The planning-stage
> counterpart is §8.6 — identifying such segments before mobilising is much cheaper than finding
> them afterwards.

## 22.6 When a test result changes what a past deliverable means

Two open tests have this shape: **T18** (whether exporting with timestamps substitutes reprocessed
data) and **T19** (which trajectory travels with an export or publish).

> **CAUTION**
>
> If either test returns a result meaning a past deliverable was not what it was believed to be,
> **that is not a documentation problem.** It is recorded in the Technical Manual Appendix F and
> escalated.
>
> **The decision about what a client is told is not the tester's to make**, and it is not specified
> here. Who it escalates to is part of **D-3**.

## 22.7 Records this section requires

| Record | State |
|---|---|
| The non-conformance — what, when, found by whom | **D-3** |
| Disposition — accepted with qualification, reprocessed, re-collected, or rejected | **D-3** |
| Where re-collection occurred, what changed | **D-3** |
| Any deliverable affected, and what was done about it | **D-29** |
