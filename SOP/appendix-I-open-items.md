# Appendix I — Open Parametrix Decisions, Field Tests, and Vendor Questions

**This appendix is the backlog. It is not a blocker to using this SOP.**

Every unresolved item in the document is collected here. The SOP is usable now; these items
determine how much of it becomes binding company procedure and how much remains proposal.

**"Operate without?"** means: can a competent processor follow this document and produce
defensible work while the item is open. **Yes** usually means the item makes the work less
consistent or less efficient, not less correct.

> **Consolidated 2026-09-11.** The first draft raised 100 separate items. Reviewing them for
> duplication and dependency reduced that to **74** — several were the same decision asked in
> different chapters, and several subordinate choices belong under one primary decision. Merged
> items are named in the **Covers** column so nothing has been dropped, only grouped.

---

## Table 1 — Parametrix Decisions Required

Company policy choices. Only Parametrix can make these. **34 items.**

| ID | Decision | Covers | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|---|
| **D-1** | **Who owns this SOP, who approves revisions, on what review cycle?** | — | TBC is on an annual release cycle and **each release has changed mobile mapping behaviour**. A procedure with no owner decays silently | 1.7 | P2 | Yes |
| **D-2** | ~~Which MX60 configuration is ours?~~ **Answered: MX60 Premium** *(Appendix H)*. Still open: **are GAMS and DMI fitted, and which rack?** | — | The configuration settled the imagery figures (**12288×6144**) and the navigation grade. What remains: GAMS decides whether GAMS-assisted initialization exists; DMI decides whether DMI settings appear in trajectory processing; the rack determines whether published GAMS corner offsets apply. **Remainder answered by V-4** | 4.1, 19.2 | **P1** | Yes, with risk |
| **D-3** | **Roles and authorities.** Who may operate the MX60; who may perform a registration; who accepts one; who may run Cleanup; who signs the accuracy statement; who owns calibration currency | *was D-3 to D-8* | One meeting, one output. **The accepting person should not be the person who performed the adjustment** — that separation is the whole basis of the independent check | 3.2–3.4 | **P1** | Yes, with risk |
| **D-10** | **Do we hold a POSPac MMS 8.6+ licence, and where is it installed?** | — | Determines whether trajectory processing and PFIX are available **at all**, and removes one of three degraded-GNSS remedies | 4.4, 12.1, 20.3 | **P1** | **No** |
| **D-11** | Is LiDAR QC a capability we intend to have? | — | 128–256 GB RAM, dedicated SSDs, MATLAB Runtime. A procurement question that becomes urgent only when it is too late | 4.5, 12.7 | P2 | Yes |
| **D-12** | **Registration command selection.** Is Register a Mission the corridor default? Where does run-to-run sit in a controlled workflow? | *was D-12, D-14* | The three commands are not interchangeable. Run-to-run uses **no control** and propagates the reference run's absolute error | 15.4, 16.2 | P2 | Yes |
| **D-13** | **What constitutes an acceptable registration and an acceptable point cloud?** | — | **No Trimble source provides a threshold.** Must combine numerical residuals, independent checks, visual inspection and the project accuracy requirement | 15.9, 18.9, 24.3 | **P1** | **No** |
| **D-15** | **Is the control/check designation fixed before registration and unchangeable during it?** | — | Guards the one failure that looks like diligence — a processor who dislikes a check residual and ticks the point into the adjustment | 17.4 | **P1** | Yes, with risk |
| **D-16** | **Control design.** How many control points, at what spacing, how many independent checks — and does density vary with predicted GNSS conditions? | *was D-16, D-33* | No Trimble source states any. TBC's minimum of one pair is a **mathematical floor**. Control must bracket the extent because Local does not extrapolate | 5.6, 17.5, 20.4 | **P1** | **No** |
| **D-18** | What is verified at import, and by whom? | — | Seven checks, each cheaper now than later. Includes recording the calibration state the mission was collected under | 11.5 | P3 | Yes |
| **D-19** | **IN-Fusion+ Single Base or PP-RTX?** | — | Determines whether a base station is occupied every mission, **and** the reference frame the solution is computed in | 5.3, 12.3 | **P1** | **No** |
| **D-21** | **Which datum and epoch do we work in, who sets it, who checks it?** | — | A silent failure mode (the ITRF00 path), plus a user-settable epoch control Trimble itself flags as capable of producing inaccurate results | 5.4, 12.6 | **P1** | **No** |
| **D-22** | Are scans generated coloured by default? | — | Discovering later that colour was wanted means regenerating the mission | 13.4 | P3 | Yes |
| **D-24** | Where is the calibration site, and who maintains it? | — | Establishing one is a morning's work; finding one under schedule pressure is not | 6.7, 14.3 | P2 | Yes |
| **D-26** | **Recalibration interval and triggers — does daily removal of the Sensor Unit count as disturbing it? And what happens to data collected on a stale calibration?** | — | If the head comes off nightly, calibration is routine rather than periodic. **Answered in part by V-13** | 11.5, 14.7 | **P1** | Yes, with risk |
| **D-27** | **QC inspection content.** What does a visual point-cloud QC pass cover, and what does an imagery QC pass cover? | *was D-27, D-30* | **Two QC layers produce no software artefact at all** — if a reviewer asks whether the visual check happened, the only answer is a record somebody wrote | 18.5, 19.3, 24 L6 | P2 | Yes |
| **D-28** | Is the retro-reflective target check our periodic verification, and at what interval? | — | The only independent check on **the instrument** in any source — the only one comparing the MX60 against conventionally surveyed truth. **Answered in part by V-14** | 18.7 | P2 | Yes |
| **D-29** | **The record package.** What provenance record accompanies a deliverable, where does it live, and where is the control/check designation and its residuals recorded? | *was D-17, D-29* | **Six facts cannot be reconstructed from the deliverable**, and TBC is not documented as reporting the control/check designation at all | 17.6, 23.6, 24.4 | **P1** | Yes, with risk |
| **D-31** | Is the imagery file-size scan adopted? | — | **Validation required first** — file size alone cannot establish image validity. It is a screening method, not proof | 19.4, 24 L8 | P3 | Yes |
| **D-32** | **What is our position on imagery privacy? Are unblurred originals retained, and for how long?** | — | Legal and reputational dimensions outside this SOP. **Blurring is irreversible in the delivered product** | 19.6, 25.5 | **P1** | Yes, with risk |
| **D-34** | **Handling segments mobile mapping cannot serve.** What is the decision rule when a corridor produces an unacceptable trajectory, and are marginal segments recorded before mobilising? | *was D-34, D-45* | Includes the legitimate professional answer that **another method would produce a more defensible result** | 6.8, 20.7 | P2 | Yes |
| **D-35** | **When may Cleanup be performed, by whom, and what must be archived first?** | — | Destructive, not undoable, and reduces the registration history at the moment the project is handed on. **Otherwise decided by default by whoever finishes a project first** | 21.4, 23.5 | **P1** | **No** |
| **D-36** | **The export release gate.** Is the pre-export trajectory-node confirmation mandatory, and may exports be made with Export timestamps enabled before T18 resolves? | *was D-36, D-37* | Registration does not reach the point cloud until Update Scans runs, and a documented export option may substitute reprocessed data for the data that was checked | 22.2, 22.3 | **P1** | Yes, with risk |
| **D-38** | **Deliverable specification.** What are our standard formats, which export path produces each, and what is our default scaling? | *was D-38, D-40* | Ground scaling **does not record its own scale factor**; grid writes a sidecar that does | 5.7, 22.5, 22.6 | P2 | Yes |
| **D-39** | **What is the corridor continuity inspection method and coverage?** | — | Must detect a degraded stretch **shorter than the sampling interval**, which rules out sparse spot checks | 24 L7 | **P1** | Yes, with risk |
| **D-41** | **How many passes, in what pattern, by roadway type?** | — | **Two of three degraded-GNSS remedies require overlap collected on the day.** Without it they are unavailable in the office | 6.2 | **P1** | **No** |
| **D-42** | **Base station strategy and maximum baseline?** | — | Field logistics on every mission. Interacts with D-19 | 6.3 | **P1** | **No** |
| **D-43** | **Field operating rules.** Wet-weather go/no-go **with explicit operator authority to stand down**; whether night collection is permitted; collection speed by deliverable type; free-space margin before a mission may start | *was D-43, D-44, D-47, D-48* | One document the operator needs. **An operator who must phone for permission will drive.** Trimble publishes speed maxima and no relationship to deliverable quality | 6.4, 6.5, 7.8, 8.5 | P2 | Yes |
| **D-46** | Where are lever arms, the Vehicle Preset and the installation configuration recorded and verified? | — | Entered once, used every mission. **An error is systematic, invisible, and persists until someone re-measures** | 7.3 | **P1** | Yes, with risk |
| **D-49** | **Field close-out.** What does the mission field record contain, what coverage verification happens before leaving site, and what triggers a re-drive — may the operator decide alone? | *was D-49, D-50, D-51* | No software produces the field record, and §9, §11 and §24 all depend on it. **Missed overlap removes office options irrecoverably.** On site a re-drive is minutes; from the office it is a mobilisation | 8.9, 9.3, 9.4 | **P1** | Yes, with risk |
| **D-52** | Offload, verification and backup procedure | — | **The only irreversible step in the workflow** | 10.3, 10.4 | **P1** | Yes, with risk |
| **D-53** | Folder structure, naming and storage location | — | Several provenance artefacts are **small files loose in a project folder** | 10.5 | P2 | Yes |
| **D-54** | Is a chain-of-custody record required? | — | The deliverable may not be able to speak for itself | 10.6 | P3 | Yes |
| **D-55** | **Capture and retention.** What is retained, where, for how long, by whom — including whether Backup SBET Next to MXDB is enabled, the Results of Scan Generation captured, and the calibration JSON exported and archived as standard | *was D-20, D-23, D-25, D-55* | Tier 1 is a **few hundred kilobytes**. Tier 3 is hundreds of GB and determines whether reprocessing is ever possible. The frame/epoch log exists **only if the option was enabled** | 12.4, 13.5, 14.5, 25.3 | **P1** | Yes, with risk |

**P1 decisions: 19.**

---

## Table 2 — Field Tests Required

Answerable with the software or the system in front of you. **No further documentation research
will resolve any of these.** **24 items.**

| ID | Test | Covers | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|---|
| **T18** | **Export the same registered run twice, timestamps off and on, and compare the point geometry.** Does reprocessing from raw reflect the registered trajectory? | — | **The highest-priority test in the project.** A documented export option may deliver data that was never the data that was checked. Pairs with **V-1** | 22.3, 13.8 | **P1** | Yes — by keeping timestamps off |
| **T28** | **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?** | — | Distinguish **project object retention** from **underlying file retention**; do not assume one implies the other. Determines what must be archived before Cleanup | 21.3, 23.5, 25.4 | **P1** | Yes — by archiving them anyway |
| **T29** | Establish the reliable export-state verification method **for each export path** | — | How an export dialog resolves its selection is not documented | 22.2, 24 L9 | **P1** | Yes — by verifying project-side |
| **T3** | **Does Reflective Panels remove legitimate retro-reflective returns from signs and line marking?** | — | On sign and retroreflectivity work, **those returns are the deliverable** | 13.3 | **P1** | Yes, with risk |
| **T15** | **Which registration type, when?** Test Global, Local and Global-then-Local with independent checks | — | No selection rule published. **Global-then-Local gets no guidance and appears in every Trimble screenshot** | 15.5 | **P1** | Yes, with risk |
| **T25** | Which feature types are fit for horizontal control, vertical control, or both, at MX60 density and incidence? | — | Will shape control design more than any software setting | 5.5, 17.3 | **P1** | Yes, with risk |
| **T1** | **Filter selection and defaults.** Default vs High Quality preset; Isolated Points default state; Range Max against useful range in bright sun and at oblique incidence; Fog and Sun applied when those conditions did not occur | *was T1, T2, T4, T5* | The largest block of untested settings in the workflow. Each removes real returns under conditions that may not have applied. **Trimble's own text contradicts itself on Isolated Points** | 13.3 | P2 | Yes |
| **T6** | Colouriser forward vs backward camera preference, and its effect on fringing | — | No selection rule given | 13.4, 19.5 | P3 | Yes |
| **T7** | Registration Auto-Saving **default state** | — | `Targets.csv` is the registration's field book, and a wrong answer to a dialog empties it permanently | 15.3 | P2 | Yes |
| **T9** | **Target-Bundle Adjustment** — test both states with independent checks | — | **Checking it makes the adjustment coarser** (250 m vs 70 m); the name reads backwards | 15.7 | P2 | Yes |
| **T10** | Which Parametrix coordinate systems does POSPac recognise directly, and which trigger the ITRF00 path? | — | Answerable once, then known | 5.3, 12.4 | P2 | Yes |
| **T11** | Multipath default **Medium** on open-sky corridors | — | Medium is described as being for *degraded* coverage | 12.3 | P3 | Yes |
| **T12** | DMI scale factor SD default **5 %** — was the wheel actually measured? | — | Trimble says set it to 100 % if unknown | 12.3 | P3 | Yes |
| **T13** | **LiDAR QC settings.** Range default 3–100 m, and Lasers = All | *was T13, T14* | Useful scanner range and useful aiding range are different questions. **The Lasers default contradicts the guidance printed beside it** | 12.7 | P3 | Yes |
| **T16** | Working cutting plane thickness for the visual checks | — | Trimble's own screenshots show 0.030 and 5.000 with no basis. **Too thick buries a real offset** | 16.7, 18.6 | P2 | Yes |
| **T17** | **Sample points** random sampling in the classified LAS exporter | — | A destructive thinning with no documented spatial rule; default state not stated | 22.6.1 | P2 | Yes |
| **T19** | **Which trajectory travels?** Publish a registered run to TRCPS, and export the same run to TMX, and inspect what arrives | *was T19, T20* | Both paths carry trajectory geometry; **neither states which trajectory**. Pairs with **V-10** | 22.6.2, 22.6.6 | P2 | Yes |
| **T21** | Register a mission, run a Mission Report, and look. Does it contain the signed GCP residuals? | — | The 2025.21 release note says residuals are "included in the report"; the Mission Report topic does not mention them. Pairs with **V-11** | 17.6 | P2 | Yes |
| **T22** | Export a LAS and inspect the file directly — header fields, VLRs, sidecar contents | — | Trimble's topics do not enumerate LAS headers. **Something undocumented may be written.** Pairs with **V-12** | 22.7, 23.4 | P2 | Yes |
| **T23** | Draw a Point Cloud tab selection across scans from two trajectories and observe | — | Whether TBC warns, prevents or silently permits is not stated | 22.4 | P2 | Yes |
| **T24** | How much run overlap is enough for run-to-run registration? | — | Trimble states the requirement qualitatively only. A pair overlapping for 200 m of a 2 km run is registered on a tenth of its length | 16.6 | P2 | Yes |
| **T26** | **Does exported imagery inherit or otherwise reflect a registration adjustment?** Compare a station's position before and after | — | Imagery is positioned from the trajectory; **nothing states whether it is recomputed** | 19.1 | P2 | Yes |
| **T27** | **What imagery streams actually exist on the MX60, and which are exposed through TBC export?** | — | The MX60 export tree shows no Planar cameras while the side-images export option persists. **Do not write MX9/MX90 camera behaviour into MX60 procedure.** Pairs with **V-8** | 19.2 | P2 | Yes |
| **T30** | Attempt both reconstruction paths — timestamp matching and trajectory geometry comparison — on a dataset with two candidate trajectories | — | Neither has been attempted; both are the fallback if provenance is queried | 23.7 | P3 | Yes |

**P1 tests: 6.**

---

## Table 3 — Vendor Clarifications Required

Only Trimble can answer these. **16 items.**

| ID | Question | Covers | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|---|
| **V-1** | **When Export timestamps causes reprocessing from raw data, which trajectory is used?** | — | A direct yes/no question with the largest consequence in the workflow. Pairs with **T18** | 22.3 | **P1** | Yes — by keeping timestamps off |
| **V-4** | ~~Which MX60 configuration do we have?~~ **Answered: Premium**, stated by the system owner — confirm against the serial number. Still open: **are GAMS and DMI fitted, and which rack?** | — | Imagery and accuracy commitments can now be made. The remainder decides initialization options, trajectory-processing settings and whether published GAMS offsets apply | 4.1 | **P1** | Yes, with risk |
| **V-10** | Which trajectory do **TMX export** and **Publish to TRCPS** send when a run has both an imported and a registered trajectory? | — | Both carry trajectory geometry; neither says which. Pairs with **T19** | 22.6.2, 22.6.6 | **P1** | Yes, with risk |
| **V-12** | Does any TBC export write the source trajectory into a **LAS header, VLR or sidecar**? | — | **The one provenance question documentation cannot answer.** Pairs with **T22** | 23.4 | **P1** | Yes, with risk |
| **V-13** | Does removing and refitting the Sensor Unit disturb the calibration? What symptoms indicate drift? | — | Determines whether calibration is **periodic or routine**. Answers part of D-26 | 14.7 | **P1** | Yes, with risk |
| **V-2** | Is the MX60 laser control presented as *Measurement Prog* + *Line Speed*, or as a combined *Laser Mode*? Which TMI version applies? | — | The Quick Start Guide and TMI Rev L disagree — `CONFLICT-005` | 4.2, 7.7 | P2 | Yes |
| **V-3** | Which TBC version is installed on our workstation? | — | Two version-dependent behaviours, **both legacy** — 5.21 and 5.80 both predate the oldest published release note | 1.6, 4.3 | P2 | Yes |
| **V-5** | **Accessory manuals not held** — Trimble **GAMS Antenna Kit** and **DMI** Installation & Operation Manuals | *was V-5, V-6* | Needed to complete the lever-arm procedure if fitted. The DMI manual contains the scale factor for the measured wheel diameter, which §12.3 needs | 7.3, 12.3 | P2 | Only if neither is fitted |
| **V-7** | Does the **Lateral Range Limit** affect accuracy, or is it purely a data-volume tool? | — | Undocumented | 7.7 | P3 | Yes |
| **V-8** | What is the MX60's actual camera complement, and which streams are exposed through TBC export? | — | Pairs with **T27** | 19.2 | P2 | Yes |
| **V-9** | Does **LiDAR QC** have its own POSPac dependency? | — | Trimble does not state one, but directs configuration questions to **Applanix Support** | 4.5 | P2 | Yes |
| **V-11** | **Which report contains the signed GCP residuals** added in TBC 2025.21? | — | The only mobile mapping report topic does not mention residuals. Pairs with **T21** | 17.6 | P2 | Yes |
| **V-14** | Is the retro-reflective target check the recommended periodic verification for the MX60, and at what interval? | — | Trimble says "regularly" and defines nothing. Answers part of D-28 | 18.7 | P2 | Yes |
| **V-16** | When should PFIX be preferred over registration? | — | This document's framing of the distinction is **inferred, not stated by Trimble** | 20.5 | P2 | Yes |
| **V-17** | Does the "coordinate system without Geoid" restriction on TMX export apply to the MX60, or only the MX9? | — | Stated for the MX9 only | 22.6.2 | P2 | Yes |
| **V-15** | Scanner field of view — **346°** *(UG p.54)* or **360°** *(spec sheet p.2)*? | — | Matters for occlusion geometry — `CONFLICT-002` | 4.1 | P3 | Yes |

**P1 vendor questions: 5.**

---

## Summary

| | Items | P1 | Block operation |
|---|---|---|---|
| **Parametrix Decisions** | 34 | 19 | 8 |
| **Field Tests** | 24 | 6 | 0 |
| **Vendor Clarifications** | 16 | 5 | 1 |
| **Total** | **74** | **30** | **9** |

### The eight that genuinely block operation

*Was nine. **D-2 / V-4** came off the list on 2026-09-19 when the configuration was established
as the **MX60 Premium** — see Appendix H. Its remainder (GAMS, DMI, rack) is P1 but does not
block operation.*

| ID | What it blocks |
|---|---|
| **D-10** | Whether trajectory processing and PFIX exist at all |
| **D-13** | Acceptance cannot be signed |
| **D-16** | Control design cannot be specified |
| **D-19** | Field logistics on every mission |
| **D-21** | Datum and epoch — a silent failure mode |
| **D-35** | Cleanup, otherwise decided by default |
| **D-41** | Pass pattern — overlap must be collected on the day |
| **D-42** | Base station strategy |

**The remaining sixty-six do not prevent defensible work.** They make it less consistent, less
efficient, or dependent on individual judgement — which is what an SOP exists to reduce, and is
exactly the work this backlog represents.

### Suggested sequence

| Round | Items | Why first |
|---|---|---|
| **1** | **D-10** · **V-3**, and the **V-4** remainder (GAMS, DMI, rack) | Facts about what we own and what we are licensed for. The configuration half of V-4/D-2 is answered — **Premium**; the rest is the same phone call to the dealer |
| **2** | **D-3** · **D-19** · **D-21** · **D-41** · **D-42** | The decisions that shape field work and must exist before a first job |
| **3** | **D-13** · **D-16** · **D-15** · **D-29** · **D-39** | The accuracy and evidence framework — the defensibility core |
| **4** | **T18** · **V-1** · **T28** · **T29** | The four tests that close the export and Cleanup questions. **An afternoon with the software** |
| **5** | **D-35** · **D-36** · **D-55** | Cleanup, export release and retention — answerable once round 4 is done |
| **6** | Everything else | Consistency and efficiency |

*Vendor contact: `mx_support@trimble.com` · Americas +1-289-695-4416 *(MX60 UG Rev B, p.51)*
