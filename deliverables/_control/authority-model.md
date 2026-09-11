# The authority model

**What makes a statement in these documents binding, and on whose authority.**

The four documents contain a great deal of language that creates procedural force — *shall*,
*must*, *never*, *do not*, *stop*, *required*, *only*, *authorised*. Until now that language did
not say **where its authority comes from**, which produced a contradiction: the SOP declared that
no requirement is adopted, and then issued 19 requirements in the imperative.

## The contradiction, and how it is resolved

The error was treating *adoption by Parametrix* as the only source of authority. It is not.

| Source | Binding now? | Why |
|---|---|---|
| **Trimble** states it as a requirement or a documented procedure | **Yes** | The manufacturer's instruction does not wait for a Parametrix decision |
| **Equipment or safety limit** with manufacturer evidence | **Yes** | A voltage threshold is a fact about the hardware |
| **Parametrix has adopted it** | **Yes** | Recorded in SOP Appendix A with a date and an approver |
| **Parametrix procedure, proposed** | **No** | A recommendation from this project |
| **Depends on a Parametrix decision** | **No** | The requirement's shape is known; its content is not |
| **Depends on a test result** | **No** | Nobody has the answer yet |

**The distinction is the source of authority, not the strength of the wording.** A Trimble
requirement is stated as firmly as it deserves whether or not Parametrix has adopted this SOP.

## The six labels

Every statement that carries procedural force carries one of these.

| Label | Meaning | Verb |
|---|---|---|
| **TRIMBLE REQUIREMENT** | Trimble states it, in the cited topic or manual page | **shall** / **do not** |
| **EQUIPMENT LIMIT** | A hardware or safety limit, with manufacturer evidence | **shall** / **do not** |
| **PARAMETRIX REQUIREMENT (ADOPTED)** | Recorded in SOP Appendix A with a date and an approver | **shall** |
| **PARAMETRIX PROCEDURE (PROPOSED)** | Recommended by this project. **Not company policy** | **should** |
| **PARAMETRIX DECISION REQUIRED** | The requirement is identified; the answer is not set | *no imperative* |
| **TESTING REQUIRED** | The requirement depends on a result nobody has obtained | *no imperative*, or a stated interim posture |

## The verb rule

> **`shall` and `shall not` are reserved for the three authorities that bind now** — Trimble,
> equipment limit, and adopted Parametrix requirement.
>
> **A proposed Parametrix practice uses `should`.** When Parametrix adopts it, the label changes
> to **(ADOPTED)** and the verb changes to `shall` — one edit, in one place, recorded in Appendix A.

At this revision **no clause carries PARAMETRIX REQUIREMENT (ADOPTED)**, and every `shall` in the
SOP therefore rests on Trimble or on an equipment limit.

## What this does not change

| | |
|---|---|
| **Warnings** | The warning register governs their wording, verbatim. A warning's authority is recorded there alongside it |
| **The How To guides** | They still cannot create a requirement. They **inherit** the label from the SOP clause or the source, and stay as decisive as that authority allows |
| **Direct language in the How Tos** | *Do not clear the disk* stays direct. It now says whose instruction it is |

## Where it is enforced

`tools/check-authority.py` reports procedural-force language that carries no authority label, and
any `shall` that rests on a proposed or undecided clause. Run it with `tools/check-all.py`.
