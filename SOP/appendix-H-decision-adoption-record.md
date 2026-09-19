# Appendix H — Decision Adoption Record

**This appendix is empty on first issue, and that is correct.**

## H1 · What this appendix is for

The SOP tags every Parametrix procedure as **PROPOSED** or **ADOPTED** (§1.5). On first issue
**there are no ADOPTED entries** — the technical content is complete and evidenced; the company
decisions on top of it have not been made.

This appendix is where they are recorded as they are made. It is the mechanism by which a
proposal becomes policy.

## H2 · How a decision is adopted

1. The decision is identified in **Appendix I**, with its ID
2. Parametrix decides it
3. **The decision is recorded here** — ID, what was decided, by whom, on what date
4. The relevant SOP section's tag changes from **PARAMETRIX PROCEDURE (PROPOSED)** or
   **PARAMETRIX DECISION REQUIRED** to **PARAMETRIX PROCEDURE (ADOPTED)**, with a cross-reference
   to this appendix
5. The Appendix I row is struck through, with a pointer here

> **A decision that is made but not recorded here has not been adopted.** The tag in the body is
> the reader's only indication of whether something is binding, and it must be traceable to a
> named person and a date.

## H3 · The record

| ID | Decision | What was decided | Decided by | Date | SOP §§ updated |
|---|---|---|---|---|---|
| **D-2** *(part)* | Which MX60 configuration is ours | **MX60 Premium** — the top configuration. Panoramic imagery **12288 × 6144 px**; highest of the three navigation grades | **Stated by the system owner — name to be recorded** | 2026-09-19 | 2.4, 4.1, 19.2, App I |

> **This is an equipment fact, not a policy decision**, and it is recorded here because the same
> traceability applies: the body of the SOP now asserts a configuration, and a reader must be able
> to see where that assertion came from.
>
> **It has not been confirmed against the serial number.** Trimble can do that, and the same call
> answers the rest of V-4 — whether GAMS and DMI are fitted, and which rack is on the vehicle.
> Until then this row rests on the owner's statement, which is good enough to write imagery
> figures against and not good enough to put in front of a client without checking.

**No Parametrix policy decision has been adopted.** Every procedure in this document remains
**PROPOSED**.

## H4 · Priority order for the first round

From **Appendix I**, the eight items that genuinely block operation — **D-2 / V-4 came off this
list on 2026-09-19**, see H3:

| ID | Decision | Why it blocks |
|---|---|---|
| **D-10** | POSPac MMS licence | Determines whether trajectory processing and PFIX exist at all |
| **D-13** | Acceptance criteria | Acceptance cannot be signed |
| **D-16** | Control design | Control design cannot be specified |
| **D-19** | Computation mode — Single Base or PP-RTX | Field logistics on every mission |
| **D-21** | Datum and epoch | A silent failure mode with a user-settable control |
| **D-35** | Cleanup policy | Otherwise decided by default by whoever finishes a project first |
| **D-41** | Pass pattern | Two of three degraded-GNSS remedies need overlap collected on the day |
| **D-42** | Base station strategy | Field logistics; interacts with D-19 |

Ten further **P1** items should follow. **Appendix I §Suggested sequence** sets out six rounds,
and the fourth of them is a single afternoon with the software that closes the export and
Cleanup questions.

The remaining items improve consistency and efficiency without preventing defensible work.

## H5 · Review

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> **Who owns this SOP, and on what cycle is it reviewed?**
>
> TBC is on an annual release cycle — 2023.10 through 2026.10 — and **each release has changed
> mobile mapping behaviour**. This SOP documents TBC 2026.10. Without an owner and a cycle, it
> will describe software nobody is running within about eighteen months.
