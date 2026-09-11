# 17. Destructive Operation Controls

## 17.1 What this section governs

An operation that removes data or history and cannot be undone within the software. In the MX60
workflow, one command is in this class.

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*

Clearing a data disk before a verified copy exists (§11.2) and deleting raw mission data (§20) are
destructive in the same sense, and are governed by the same principle: **authorisation, and the
record made before the act, not after.**

## 17.2 Authorisation

> **PARAMETRIX DECISION REQUIRED · D-35 · P1 · blocks operation**
>
> **When may Cleanup be performed, by whom, and what must be archived first?**

> **PARAMETRIX PROCEDURE (PROPOSED) · D-3, D-35**
>
> **Cleanup shall not be run without written authorisation** from the person with the authority
> under §4 — proposed there as the Project Surveyor. "In writing" carries the meaning in §3.3.

## 17.3 What is archived first

> **PARAMETRIX PROCEDURE (PROPOSED) · D-35**
>
> A sequence in which Cleanup destroys nothing that matters:
>
> | # | Step | Why in this order |
> |---|---|---|
> | 1 | **Complete and accept QC** (§15, §16) | Cleanup is an end-of-preparation step. Running it before acceptance removes the alternatives you might need to go back to |
> | 2 | **Run the Mission Report and archive it** | It records capture devices, runs, trajectories, generated scans, and per-sensor calibration with date *(TBC 23991_1, 24868)*. **Run it before Cleanup** — afterwards it can only report what survives |
> | 3 | **Record the registration evidence** (§15.8) | Control/check designation and residuals. TBC does not appear to report these |
> | 4 | **Archive `Targets.csv`** *(TBC 22905)* | The picked registration observations — the registration's field book, and not recoverable |
> | 5 | **Archive the numbered SBET files** `sbet_<date>_reg_####.out` | Pending **T28**, assume Cleanup removes them |
> | 6 | **Archive the calibration JSON** (§14.5) | The system state the mission was processed under |
> | 7 | **Take the project backup Trimble asks for**, to a location that is part of the project archive (§20) | A backup nobody can find is not a backup. Not a local copy on the processor's machine |
> | 8 | **Obtain the authorisation** §17.2 requires | |
> | 9 | **Run Cleanup** | |
> | 10 | **Record that it was run** — by whom, on what date, and what was archived first | Otherwise the absence of history is itself unexplained |
>
> Steps 2 to 6 are small files. The whole set is a few megabytes beside a project of tens of
> gigabytes, and they are the difference between a deliverable that can account for itself and one
> that cannot.

> **TESTING REQUIRED · T28**
>
> **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?**
> The answer determines what step 5 has to cover. Until it is known, assume the worse case.

## 17.4 Why this matters more here than elsewhere

Cleanup removes the evidence of how a deliverable was produced, and MX60 provenance is already the
hardest part of this workflow *(Technical Manual §30)*. A project that has been cleaned up can no
longer show which of several trajectories a delivered cloud was built on, because the alternatives
are gone along with the record of which one was chosen.

**That is not an argument against running Cleanup.** It is the argument for §17.3.

## 17.5 Records this section requires

| Record | State |
|---|---|
| Authorisation — who, when, for which mission | **D-35** |
| What was archived before, and where it is | **D-35, D-55** |
| That Cleanup was run, by whom, on what date | **D-35** |
