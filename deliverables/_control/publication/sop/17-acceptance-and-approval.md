# 17. Acceptance and Approval

## 17.1 What acceptance is

**Acceptance is the point at which the data becomes the deliverable.** It is a decision by a named
person, recorded, that a dataset meets the project's stated accuracy requirement (§6.1).

Acceptance is always **against a requirement**. A dataset is not accepted because it looks good, or
because the residuals are small, or because the schedule has run out.

## 17.2 There is no general numerical tolerance, and none is invented here

**This SOP states no numerical acceptance tolerance.** That is deliberate, and the reason matters
more than the gap.

| | |
|---|---|
| Trimble publishes **no acceptance tolerance** for the MX60 | Its published figures are **instrument performance under stated conditions**, which is not a project acceptance criterion |
| Trimble publishes **no attitude error budget** for the point cloud | A useful range for a given tolerance therefore cannot be calculated from the documentation *(Technical Manual §16.5)* |
| **A good RMS does not prove success** | Trimble states it twice, in identical words. Only observations held out of the adjustment, and looking at the data, can suggest success *(Technical Manual §23)* |

> **A number here would be worse than the gap.** An invented tolerance would be quoted, relied on
> and eventually defended, and there would be nothing behind it. The gap is visible; a fabricated
> threshold would not be.

### What this means in practice

**The accuracy requirement comes from the project, in writing, before collection** (§6.1). Acceptance
is then a judgement against *that* requirement, supported by the evidence at §17.3 — independent
check points, their residuals by component, and the visual inspection.

> **Whoever signs an accuracy statement signs on their own professional judgement**, supported by
> the evidence in §16. That should be understood by the person signing and by whoever receives it.

### What is not yet known about this system

Two relationships have not been measured on Parametrix's MX60 and cannot be read from the
documentation:

- **How achieved accuracy varies with GNSS conditions.** Corridor geometry, canopy and urban
  reflection all degrade the trajectory, and by how much on this system is not established.
- **Which feature types are fit for horizontal or vertical control** at MX60 point density and
  incidence angle (§7.1).

Until they are measured, both are matters for judgement on the project, informed by the check
evidence actually obtained on that project.

## 17.3 What acceptance requires

Five things are required before a dataset is accepted. These are structural and do not depend on a
number.

| # | Requirement |
|---|---|
| 1 | The project's **accuracy requirement is stated in writing** (§6.1) |
| 2 | **Independent check points exist**, were designated before registration, and took no part in any adjustment (§7.3) |
| 3 | **Residuals on those check points are recorded**, by component (§16.4) |
| 4 | **The visual inspection was performed and recorded** (§16.5) |
| 5 | **Update Scans was run**, and the accepted cloud is the registered one (§13.4) |

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

**The Project Surveyor accepts a registration and signs an accuracy statement** — and not the person
who computed the registration (§4.2). Where one person must do both on a small job, the acceptance
and its evidence are recorded so that the basis of the decision can be reviewed afterwards.

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

| Record |
|---|
| Acceptance decision — dataset, by whom, date, against what requirement |
| The evidence the decision rested on |
| The accuracy statement issued |

## In Plain Language

**Accepting the data is a separate act from producing it.** Somebody puts their name to a statement
that this dataset meets the accuracy the project asked for.

**Why it matters.** There is no company-wide number to check against, and no Trimble number either.
The check is against what the project asked for in writing, using points that were deliberately kept
out of the adjustment so they could still tell you something.

**Remember this.** You cannot check accuracy with points that helped produce the answer. If nothing
was held back before registration, the dataset cannot be checked afterwards without going back out
and surveying more.

**If the steps are skipped.** A dataset gets delivered with a number attached that nobody can
support. The failure surfaces when a client or a reviewer asks how the figure was arrived at —
usually long after the corridor has changed and re-surveying it is no longer cheap.
