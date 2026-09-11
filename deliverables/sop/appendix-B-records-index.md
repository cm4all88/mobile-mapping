# Appendix B — Index of Required Records

**Generated view — do not edit by hand.** Produced by `tools/build-records-index.py` from the
*Records this section requires* table at the end of each section. Edit the section; regenerate this.

**69 records**, across 19 sections.
Last generated 2026-09-11.

> **Read the State column.** A record whose state names a **D-** identifier is required by a clause
> that has not been adopted. It is proposed, not mandatory, and the identifier is where the decision
> is tracked (Appendix A).

> **Five of these records have no software artefact behind them** — the control and check
> designation, the visual inspection, the imagery inspection, the field conditions, and the
> disposition of a non-conformance. They are written by a person or they do not exist (§19.1).

---

## B1 · By section

| § | Section | Record | State |
|---|---|---|---|
| 2 | Document Control and Related Documents | Revision history of this procedure | **D-1** |
|  |  | Which supporting revisions were issued with this one | **D-1** |
|  |  | Distribution and receipt | **D-1** |
| 4 | Roles, Responsibilities and Authorities | Who holds each role on a given project | **D-3** |
|  |  | Who designated control versus independent check, and when | **D-15** |
|  |  | Any exercise of stand-down authority, and its reason | **D-43** |
| 5 | Competence and Training | Who holds which qualification, and from when | **D-3** |
|  |  | Training delivered, and against which document revision | **D-3** |
| 6 | Project Setup Requirements | Accuracy requirement, and its source | **D-13** |
|  |  | CRS, datum, epoch, geoid — and who set them | **D-21** |
|  |  | Grid or ground, as agreed | **D-38** |
|  |  | Configuration and fitment assumed | **D-2** |
| 7 | Control Requirements | Control network, with coordinates and their source | Existing practice |
|  |  | **Which points are control and which are independent checks, fixed before registration** | **D-15** |
|  |  | Who designated them, and when | **D-3** |
| 8 | Mission Planning Requirements | The mission plan — route, passes, direction, overlap | **D-41** |
|  |  | GNSS assessment, with duration estimates and mitigations | **D-41, D-42** |
|  |  | Initialization locations, primary and backup | **PROPOSED** |
|  |  | Segments mobile mapping will not serve, and what is proposed instead | **D-34** |
| 9 | Field Acquisition Requirements | Pre-flight confirmation, including aiding-sensor activation where fitted | **D-46** |
|  |  | The field record, per §9.6 | **D-49** |
|  |  | Any exercise of stand-down authority, and its reason | **D-43** |
|  |  | Operating-limit exceedance, if any, and what was done | **D-43** |
| 10 | Field Close-out and Handoff | Coverage verification, performed and by whom | **D-49** |
|  |  | Deviations from the mission plan | **D-49** |
|  |  | Handoff — what was transferred, to whom, when | **D-52, D-54** |
| 11 | Data Transfer and Custody | Offload performed, verified how, by whom, when | **D-52** |
|  |  | Location of the raw-data backup | **D-52, D-55** |
|  |  | Custody, where required | **D-54** |
| 12 | Office Intake Requirements | Intake checks performed, by whom, with the result of each | **D-18** |
|  |  | Calibration state at collection — `Extcal.json` and the Mission Report | **D-55** |
|  |  | Any intake check that failed, and what was done | **D-18, §21** |
| 13 | Processing Requirements | Trajectory processing settings, and the frame and epoch log | **D-55** |
|  |  | Results of Scan Generation | **D-55** |
|  |  | Registration type, trajectory node, SBET filename with its `_reg_####` number | **D-29** |
|  |  | Confirmation that Update Scans was run | **D-36** |
|  |  | `Targets.csv` | **D-55** |
| 14 | Calibration Control | Calibration performed — date, site, who, and the result including the visual check | **D-26** |
|  |  | The calibration JSON, archived outside the project | **D-55** |
|  |  | Which calibration each mission was processed against | **D-55** |
|  |  | Periodic verification, when performed | **D-28** |
| 15 | Quality Control Requirements | Residuals on control points used, by component | Targets pane |
|  |  | Residuals on independent check points, by component | Same |
|  |  | **Which points were control and which were checks** | **Manual — TBC does not report it** |
|  |  | Run-to-run RMS statistics, if used | Results tab |
|  |  | Trajectory RMS picture | Screen capture |
|  |  | **Visual check performed, by whom, covering what extent** | **No software artefact exists** |
|  |  | **Imagery check performed, by whom** | **No software artefact exists** |
|  |  | Results of Scan Generation | §13.3 |
|  |  | Mission Report | §17.3 |
| 16 | Acceptance and Approval | Acceptance decision — dataset, by whom, date, against what requirement | **D-3, D-13** |
|  |  | The evidence the decision rested on | **D-29** |
|  |  | The accuracy statement issued | **D-29** |
| 17 | Destructive Operation Controls | Authorisation — who, when, for which mission | **D-35** |
|  |  | What was archived before, and where it is | **D-35, D-55** |
|  |  | That Cleanup was run, by whom, on what date | **D-35** |
| 18 | Export and Delivery Controls | Export-state confirmation, before export | **D-36** |
|  |  | The delivery record — §19 | **D-29** |
|  |  | What was delivered, to whom, when, in what format and scaling | **D-38** |
| 19 | Documentation and Records | The delivery record, per §19.2 | **D-29** |
|  |  | The control and check table, with residuals | **D-29** |
|  |  | Where the record package lives for a given project | **D-53** |
| 20 | Retention and Archive | The archive record | **D-55** |
|  |  | Retention tier applied, and the date the period runs from | **D-55** |
|  |  | Disposal, where it occurs — what, when, authorised by whom | **D-55** |
| 21 | Non-conformance and Re-collection | The non-conformance — what, when, found by whom | **D-3** |
|  |  | Disposition — accepted with qualification, reprocessed, re-collected, or rejected | **D-3** |
|  |  | Where re-collection occurred, what changed | **D-3** |
|  |  | Any deliverable affected, and what was done about it | **D-29** |

## B2 · Where the state stands

| | |
|---|---|
| Records required by an **adopted** clause | **0** |
| Records required by a clause awaiting a decision | **69** |
| Distinct decisions they depend on | **23** — D-1, D-2, D-3, D-13, D-15, D-18, D-21, D-26, D-28, D-29, D-34, D-35, D-36, D-38, D-41, D-42, D-43, D-46, D-49, D-52, D-53, D-54, D-55 |

**Every record in this index is currently proposed.** That follows from no clause having been
adopted, not from any doubt about whether the records are worth keeping.

## B3 · The records with no software artefact

These are the ones that get lost, because nothing in the software produces them and nothing
complains when they are absent.

| Record | Section | Why nothing produces it |
|---|---|---|
| **Which points were control and which were independent checks** | §7.3, §15.4 | TBC shows the state while the command is open and reloads it on Edit, but no report of it has been found *(Technical Manual §22.7)* |
| **That the visual inspection was performed, and over what extent** | §15.5 | It is a human act in a viewer |
| **That the imagery inspection was performed** | §15.6 | The same |
| **Conditions at collection** — occlusion, weather, traffic, what was not collected and why | §9.6 | Nothing in the vehicle records them |
| **Disposition of a non-conformance** | §21.7 | — |

## B4 · The smallest package that would satisfy the record

§19.2 proposes seven artefacts totalling a few hundred kilobytes. **Five of the seven already exist
as files** and need only to be copied out of the project before it is cleaned up (§17.3). Two are
written by a person.
