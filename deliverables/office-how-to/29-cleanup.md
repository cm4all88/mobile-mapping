# 29. Cleanup Mobile Mapping Mission

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*

### Do — the archive-first sequence

**[EQUIPMENT] Cleanup cannot be undone.** That is Trimble's own statement about the command and it
binds today. **[PROPOSED · SOP §18.3 · D-35]** — the ten-step sequence, and the requirement for
written authorisation, are this project's recommendation. **Who may authorise a Cleanup is D-35 and
is not settled**, which is why step 8 names an authority that does not exist yet.

**In this order.** Steps 2 to 6 are small files; the whole set is a few megabytes.

| # | Step | Why here |
|---|---|---|
| 1 | **Complete and accept QC** (§22, §32) | Cleanup is an end-of-preparation step. Before acceptance it removes the alternatives you might need |
| 2 | **Run the Mission Report and archive it** | It records capture devices, runs, trajectories, generated scans, and **per-sensor calibration with date**. **Run it before Cleanup** — afterwards it can only report what survives |
| 3 | **Record the registration evidence** (§20, §28) | Control/check designation and residuals. TBC does not report these |
| 4 | **Archive `Targets.csv`** | The picked registration observations — not recoverable |
| 5 | **Archive the numbered SBET files** `sbet_<date>_reg_####.out` | Pending **T28**, assume Cleanup removes them |
| 6 | **Archive the calibration JSON** (§13.3) | The system state the mission was processed under |
| 7 | **Take the project backup Trimble asks for** — into the project archive, not a local copy | A backup nobody can find is not a backup |
| 8 | **Obtain the written authorisation** | SOP §18.2 |
| 9 | **Run Cleanup** | |
| 10 | **Record that it was run** — by whom, on what date, what was archived first | Otherwise the absence of history is itself unexplained |

*(SOP §18.3)*

### Look at

Before running it: the project tree, so you know what you are about to lose. Registered
trajectories, their scans, and the numbered SBET files.

### Expect

Only the most recent registration surviving.

### Stop if

- **You do not have written authorisation** — **[PROPOSED · D-35]** *(SOP §18.2)*. Until D-35 is
  answered there is no appointed authoriser; raise it rather than proceeding on your own
- Any of steps 2 to 6 is not done
- The backup went to your own machine rather than into the project archive

> **TESTING REQUIRED · T28**
>
> **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?**
> Until it is known, assume the worse case and archive them.

> **PARAMETRIX DECISION REQUIRED · D-35 · blocks operation** — when Cleanup may be performed, by
> whom, and what must be archived first.

### Record

Authorisation; what was archived and where; that Cleanup was run, by whom, on what date.
