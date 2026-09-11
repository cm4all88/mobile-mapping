# 17. Acceptance and Approval

## 17.1 What acceptance is

**Acceptance is the point at which the data becomes the deliverable.** It is a decision by a named
person, recorded, that a dataset meets the project's stated accuracy requirement (§6.1).

Acceptance is always **against a requirement**. A dataset is not accepted because it looks good, or
because the residuals are small, or because the schedule has run out.

## 17.2 The criterion is not established — and the decision that follows from it

> **PARAMETRIX DECISION REQUIRED · D-13 · P1 · blocks formal acceptance**
>
> **What constitutes an acceptable registration, and an acceptable point cloud?**
>
> **This SOP states no numerical acceptance tolerance, and one has not been invented.**

### What is established

| | |
|---|---|
| Trimble publishes **no acceptance tolerance** for the MX60 | Its published figures are **instrument performance under stated conditions**, which is not a project acceptance criterion |
| Trimble publishes **no attitude error budget** for the point cloud | A useful range for a given tolerance therefore cannot be calculated from the documentation *(Technical Manual §16.5)* |
| **A good RMS does not prove success** | Trimble states it twice, in identical words. Only observations held out of the adjustment, and looking at the data, can suggest success *(Technical Manual §23)* |
| The relationship between achieved accuracy and GNSS conditions on this system **has not been tested** | **T31** |
| Which features are fit for horizontal or vertical control at MX60 density **has not been tested** | **T25** |

> **A number here would be worse than the gap.** An invented tolerance would be quoted, relied on
> and eventually defended, and there would be nothing behind it. The gap is visible; a fabricated
> threshold would not be.

### The decision Parametrix has to make

The absence of a general standard does not by itself say whether work may proceed. **That is a
separate question, and it is the one that is actually blocking:**

> ### Until a general Parametrix acceptance standard exists, may MX60 work be accepted against a **project-specific written accuracy requirement**, using independent check evidence, visual QC and documented professional judgement?

| | Outcome | What it means in practice |
|---|---|---|
| **A** | **No.** | MX60 survey-grade delivery is **blocked** until a corporate acceptance framework is adopted. The system may still be used for work where no accuracy claim is made |
| **B** | **Yes, project by project.** | Interim acceptance is permitted where the accuracy requirement is **stated in writing before collection** and the acceptance evidence at §17.3 is documented. Each acceptance stands on its own project record, not on a company standard |
| **C** | **Another Parametrix-approved interim framework.** | For example a tiered scheme, an approver-limited scheme, or acceptance restricted to named clients or work types |

> **This SOP does not choose between A, B and C, and no other document in the set implies a
> choice.** The decision is Parametrix's, it is recorded in Appendix A, and it changes §17.3 from
> proposed to adopted the day it is made.

### What is true under every outcome

**D-13 blocks formal acceptance, and nothing else.** Stated as plainly as it can be:

| With D-13 open | |
|---|---|
| **Collecting data** | **Permitted.** Nothing in D-13 touches field operation |
| **Processing, registering and inspecting it** | **Permitted.** Including exploratory and trial processing, and processing to learn the system |
| **Testing the system against known control** | **Permitted, and needed** — several register items (T25, T31) cannot close without it |
| **Delivering data with no accuracy claim attached** | **Permitted**, where the deliverable says so |
| **Formal acceptance under §17.1** | **Blocked** |
| **An accuracy claim resting on a Parametrix standard** | **Blocked**, because no such standard exists to rest on |

**Nor does this SOP authorise an accuracy statement.** It is a draft, no Parametrix requirement in
it is adopted (§2.4), and it sets no tolerance. A person may still sign an accuracy statement for
MX60 work — but they sign it on their own professional judgement and the project's own evidence,
not on the authority of this document.

> **Whoever signs an accuracy statement today is signing on their own professional judgement,
> supported by the evidence in §16 — not on a Parametrix standard, because there is not one.**
> That should be understood by the person signing and by whoever receives it.

## 17.3 What acceptance requires regardless

Even without D-13, five things are required before a dataset is accepted. These are structural and
do not depend on the number.

| # | Requirement | State |
|---|---|---|
| 1 | The project's **accuracy requirement is stated in writing** (§6.1) | **PROPOSED — D-13** |
| 2 | **Independent check points exist**, were designated before registration, and took no part in any adjustment (§7.3) | **PROPOSED — D-15** |
| 3 | **Residuals on those check points are recorded**, by component (§16.4) | **PROPOSED — D-29** |
| 4 | **The visual inspection was performed and recorded** (§16.5) | **PROPOSED — D-27** |
| 5 | **Update Scans was run**, and the accepted cloud is the registered one (§13.4) | **PROPOSED — D-36** |

> **Requirement 2 is the one that cannot be recovered afterwards.** If no point was held out, the
> dataset cannot be checked later without re-surveying, because every point it might be checked
> against helped produce it.

## 17.4 What acceptance does not rest on

| | Why |
|---|---|
| **RMS alone** | **TRIMBLE REQUIREMENT** — a visual check is needed. Trimble says so twice, in identical words (§16.1) |
| **Residuals on control points used in the adjustment** | They measure the fit of the adjustment to observations it was given |
| **A clean-looking point cloud** | Mobile mapping data does not look wrong when it is wrong *(Technical Manual §3.2)* |
| **Agreement between two passes** | Two passes can agree with each other and both be displaced, if the trajectory was drifting through the stretch |

## 17.5 Who accepts

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Who may accept a registration, and who signs an accuracy statement. Proposed at §4.2: the
> Project Surveyor, and not the person who computed the registration.

## 17.6 The accuracy statement

An accuracy statement issued to a client states:

| | |
|---|---|
| The accuracy requirement it was assessed against | |
| **The evidence** — residuals on independent check points, by component | |
| **The basis of the check** — how many points, where, in which GNSS environments | |
| The extent it applies to | Accuracy is not uniform along a corridor *(Technical Manual §3)* |
| Any segment excluded, and why | §8.6, §22 |

> **Accuracy varies along the corridor.** A single figure for a whole corridor implies a uniformity
> the method does not have. Where the statement is a single figure, the extent and the conditions
> it applies to are stated with it.

## 17.7 Records this section requires

| Record | State |
|---|---|
| Acceptance decision — dataset, by whom, date, against what requirement | **D-3, D-13** |
| The evidence the decision rested on | **D-29** |
| The accuracy statement issued | **D-29** |
