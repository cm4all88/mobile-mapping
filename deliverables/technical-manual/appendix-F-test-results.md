# Appendix F — Test Results

**Empty on issue.** This appendix is populated as the tests in **Appendix E** are run. It exists
now, with nothing in it, because a test that is run and not written down has to be run again.

## F1 · Why the results live here and not in the body

A test answers a question the manual currently states as open. When one is answered, three things
happen, in this order:

1. **The result is recorded here**, with enough detail that someone else could repeat it
2. **The master register is updated** — `resolution` and `date_resolved` — and the views are
   regenerated (`tools/build-register-views.py`)
3. **The manual body changes**, replacing the open statement with the finding, citing this
   appendix

Doing (3) without (1) and (2) produces a manual that asserts something with no evidence behind it,
which is the thing this whole structure exists to prevent.

## F2 · What a usable record contains

Not a conclusion. A conclusion with its working attached.

| | |
|---|---|
| **Question** | The Appendix E identifier, verbatim |
| **Date and who ran it** | |
| **System state** | TBC version, POSPac version if used, the MX60's configuration and calibration date |
| **Method** | What was actually done, in enough detail to repeat. Including what was *not* varied |
| **Data used** | Which mission, which runs. Where it is now |
| **Result** | The observation. Numbers where there are numbers |
| **What it does not establish** | The boundary of the finding. A test on one corridor in open sky has not established behaviour in an urban canyon |
| **Consequence** | What changes in the Manual, the SOP, or a How To — and whether anything already delivered is affected |

> **The "what it does not establish" row is the one that gets skipped, and it is the one that
> keeps a finding honest.** A single test on a single dataset is evidence, not proof. Recording
> its boundary is what allows the next person to know whether their situation is covered.

## F3 · Tests whose results affect a deliverable already issued

Some of the open questions concern what has already been exported and handed over — most directly
**T18** (whether exporting with timestamps substitutes reprocessed data) and **T19** (which
trajectory travels with a publish or an export).

> **CAUTION**
>
> If one of these tests returns a result that means a past deliverable was not what it was
> believed to be, that is not a documentation problem. Record it here, and escalate it — the
> decision about what to tell a client is not the tester's to make and not this manual's to
> specify.
>
> Who that escalation goes to is an open Parametrix decision (**D-3**, roles and authorities).

## F4 · The record

*No tests have been run. Entries are added below, newest first, one heading per Appendix E
identifier.*
