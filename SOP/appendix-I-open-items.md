# Appendix I — Open Parametrix Decisions, Field Tests, and Vendor Questions

**This appendix is the backlog. It is not a blocker to using this SOP.**

Every unresolved item in the document is collected here so it can be worked through
systematically. The SOP is usable now; these items determine how much of it becomes binding
company procedure and how much remains proposal.

**"Can the SOP operate without it?"** means: can a competent processor follow this document and
produce defensible work while this item is open. **Yes** usually means the item makes the work
less efficient or less consistent, not less correct.

---

## Table 1 — Parametrix Decisions Required

Company policy choices. Only Parametrix can make these.

| ID | Question | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|
| **D-1** | Who owns this SOP, who approves revisions, on what review cycle? | TBC is on an annual release cycle and each release has changed mobile mapping behaviour. A procedure with no owner decays silently | 1.7 | **P2** | Yes |
| **D-2** | Which MX60 configuration is ours — Core, Pro or Premium? Are GAMS and DMI fitted? Which rack? | Panoramic imagery is **8192×4096 on Core, 12288×6144 on Pro/Premium**. Changes every imagery and accuracy statement. Rack determines whether published GAMS offsets apply | 4.1, 19.2 | **P1** | **No** — imagery commitments cannot be made |
| **D-3** | Who may operate the MX60? Qualification, training, supervised runs? | Field acquisition determines what the office can ever do | 3.3 | **P1** | Yes, with risk |
| **D-4** | Who may perform a registration? | Registration is an adjustment | 3.3 | **P1** | Yes, with risk |
| **D-5** | Who accepts a registration — and must it be someone other than the person who performed it? | Independence of the check | 3.3, 17.4 | **P1** | Yes, with risk |
| **D-6** | Who may run Cleanup Mobile Mapping Mission? | Destructive and not undoable | 3.3, 21.4 | **P1** | **No** — see D-35 |
| **D-7** | Who signs the accuracy statement, under what licensure, against what evidence? | — | 3.3 | **P1** | Yes, with risk |
| **D-8** | Who owns calibration currency? | Nobody owns it today | 3.3, 14.7 | **P2** | Yes |
| **D-10** | Do we hold a POSPac MMS 8.6+ licence, and where is it installed? | Determines whether trajectory processing and PFIX are available at all, and removes one of three degraded-GNSS remedies | 4.4, 12.1, 20.3 | **P1** | **No** — shapes the entire office workflow |
| **D-11** | Is LiDAR QC a capability we intend to have? | 128–256 GB RAM, dedicated SSDs, MATLAB Runtime. A procurement question that becomes urgent only when it is too late | 4.5, 12.7 | **P2** | Yes |
| **D-12** | Is Register a Mission the corridor default, with Register a Run the exception? | Production convention; affects consistency across processors | 15.4 | **P3** | Yes |
| **D-13** | **What constitutes an acceptable registration and an acceptable point cloud?** | **No Trimble source provides a threshold.** Must combine numerical residuals, independent checks, visual inspection and the project accuracy requirement | 15.9, 18.9, 24.3 | **P1** | **No** — acceptance cannot be signed |
| **D-14** | Where does run-to-run registration sit in a controlled workflow? | It uses no control and propagates the reference run's absolute error | 16.2 | **P2** | Yes |
| **D-15** | Is the control/check designation fixed before registration and unchangeable during it? | Guards the one failure that looks like diligence | 17.4 | **P1** | Yes, with risk |
| **D-16** | How many control points, at what spacing, and how many independent checks? | No Trimble source states any. TBC's minimum of one pair is a mathematical floor | 5.6, 17.5 | **P1** | **No** — control design cannot be specified |
| **D-17** | Where is the control/check designation and its residuals recorded? | **TBC is not documented as reporting it.** The single most important record in the workflow | 17.6, 23.6 | **P1** | Yes, with risk |
| **D-18** | What is verified at import, and by whom? | Six checks, each cheaper now than later | 11.5 | **P3** | Yes |
| **D-19** | IN-Fusion+ Single Base or PP-RTX? | Determines whether a base station is occupied every mission, and the reference frame | 5.3, 12.3 | **P1** | **No** — field logistics depend on it |
| **D-20** | Is Backup SBET Next to MXDB enabled as standard? | Its log is the only record of the frame and epoch a trajectory was computed in | 12.4, 23.3 | **P2** | Yes |
| **D-21** | Which datum and epoch do we work in, who sets it, who checks it? | Silent failure mode, plus a new user-settable control Trimble flags as risky | 5.4, 12.6 | **P1** | **No** |
| **D-22** | Are scans generated coloured by default? | Discovering later that colour was wanted means regenerating the mission | 13.4 | **P3** | Yes |
| **D-23** | Is the Results of Scan Generation captured into the project record? | The only artefact stating which filters produced a cloud | 13.5, 23.3 | **P3** | Yes |
| **D-24** | Where is the calibration site, and who maintains it? | Establishing one is a morning's work; finding one under schedule pressure is not | 6.7, 14.3 | **P2** | Yes |
| **D-25** | Is the calibration JSON exported and archived after every calibration? | The only portable record of the system's angles on a date | 14.5, 25.3 | **P2** | Yes |
| **D-26** | Recalibration interval and triggering events — **does daily removal of the Sensor Unit count as disturbing it?** | If the head comes off nightly, calibration is routine rather than periodic | 14.7 | **P1** | Yes, with risk |
| **D-27** | What does a visual QC pass cover? | Two QC layers produce no software artefact at all | 18.5 | **P2** | Yes |
| **D-28** | Is the retro-reflective target check our periodic verification, and at what interval? | The only independent check on the **instrument** in any source | 18.7 | **P2** | Yes |
| **D-29** | What provenance record accompanies a deliverable, and where does it live? | Six facts cannot be reconstructed from the deliverable | 23.6, 24.4 | **P1** | Yes, with risk |
| **D-30** | What does an imagery QC pass cover? | — | 19.3 | **P3** | Yes |
| **D-31** | Is the imagery file-size scan adopted? **Validation required first** | Screening only; file size cannot establish validity | 19.4, 24 L8 | **P3** | Yes |
| **D-32** | What is our position on imagery privacy? Are unblurred originals retained, and for how long? | Legal and reputational dimensions outside this SOP. Blurring is irreversible in the delivered product | 19.6, 25.5 | **P1** | Yes, with risk |
| **D-33** | Does control density vary with predicted GNSS conditions? | Uniform spacing puts the same control where it adds little as where it holds the data together | 20.4, 6.3 | **P2** | Yes |
| **D-34** | What is the decision rule when a corridor produces an unacceptable trajectory? | Includes the legitimate answer that mobile mapping is not the right method for that segment | 20.7 | **P2** | Yes |
| **D-35** | **When may Cleanup be performed, by whom, and what must be archived first?** | Destructive, not undoable, and reduces the registration history at the moment the project is handed on | 21.4, 23.5 | **P1** | **No** — the first person to reach the end of a project decides it by default |
| **D-36** | Is the pre-export trajectory-node confirmation mandatory? | The most consequential check in export | 22.2 | **P1** | Yes, with risk |
| **D-37** | May exports be made with Export timestamps enabled before T18 resolves? | A documented option may substitute reprocessed data for the data that was checked | 22.3 | **P1** | Yes, with risk |
| **D-38** | What are our standard deliverable formats, and which export path produces each? | — | 22.6 | **P2** | Yes |
| **D-39** | What is the corridor continuity inspection method and coverage? | Must detect a degraded stretch shorter than the sampling interval | 24 L7 | **P1** | Yes, with risk |
| **D-40** | What is our default deliverable scaling, and what accompanies it? | Ground scaling does not record its own scale factor | 5.7, 22.5 | **P2** | Yes |
| **D-41** | How many passes, in what pattern, by roadway type? | **Two of three degraded-GNSS remedies require overlap collected on the day** | 6.2 | **P1** | **No** — mission planning cannot be specified |
| **D-42** | Base station strategy and maximum baseline? | Interacts with D-19 | 6.3 | **P1** | **No** |
| **D-43** | Is night collection permitted, and under what conditions? | Solves traffic occlusion, makes imagery unusable for interpretation | 6.4 | **P3** | Yes |
| **D-44** | One clear wet-weather rule, with operator authority to stand down | Neither Trimble nor TMR defines "wet". An operator who must phone will drive | 6.5 | **P2** | Yes |
| **D-45** | Are marginal segments and proposed alternative methods recorded before mobilising? | Professional judgement point | 6.8 | **P2** | Yes |
| **D-46** | Where are lever arms, the Vehicle Preset and the installation configuration recorded and verified? | Entered once, used every mission. An error is systematic and invisible | 7.3 | **P1** | Yes, with risk |
| **D-47** | What free-space margin is required before a mission may start? | A disk filling mid-corridor ends the run and the closing sequence with it | 7.8 | **P3** | Yes |
| **D-48** | What collection speed, by deliverable type? | Trimble publishes maxima and no relationship to deliverable quality | 8.5 | **P2** | Yes |
| **D-49** | What does the mission field record contain? | No software produces it; §9, §11, §24 all depend on it | 8.9 | **P1** | Yes, with risk |
| **D-50** | What coverage verification happens before leaving site? | Missed overlap removes office options irrecoverably | 9.3 | **P1** | Yes, with risk |
| **D-51** | What triggers a re-drive, and may the operator decide alone? | On site, minutes. From the office, a mobilisation | 9.4 | **P1** | Yes, with risk |
| **D-52** | Offload, verification and backup procedure | The only irreversible step in the workflow | 10.3, 10.4 | **P1** | Yes, with risk |
| **D-53** | Folder structure, naming and storage location | Several provenance artefacts are small files loose in a project folder | 10.5 | **P2** | Yes |
| **D-54** | Is a chain-of-custody record required? | The deliverable may not be able to speak for itself | 10.6 | **P3** | Yes |
| **D-55** | What is retained, where, for how long, and by whom? | Tier 1 is a few hundred kB. Tier 3 is hundreds of GB and determines whether reprocessing is ever possible | 25.1, 25.3 | **P1** | Yes, with risk |

**P1 items: 24.** These should be settled before the first production job.

---

## Table 2 — Field Tests Required

Answerable with the software or the system in front of you. **No further documentation research
will resolve any of these.**

| ID | Test | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|
| **T18** | **Export the same registered run twice, timestamps off and on, and compare the point geometry.** Does reprocessing from raw reflect the registered trajectory? | **The highest-priority test in the project.** A documented export option may deliver data that was never the data that was checked | 22.3, 13.8 | **P1** | Yes — by keeping timestamps off |
| **T28** | **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?** Distinguish project object retention from underlying file retention | Determines what must be archived before Cleanup | 21.3, 23.5, 25.4 | **P1** | Yes — by archiving them anyway |
| **T29** | Establish the reliable export-state verification method **for each export path** | How an export dialog resolves its selection is not documented | 22.2, 24 L9 | **P1** | Yes — by verifying project-side |
| **T19** | Publish a registered run to TRCPS and inspect what arrives. Which trajectory is sent? | Trajectory is exported by default; which one is not stated | 22.6.6 | **P2** | Yes |
| **T20** | Same, for the TMX export path | The trajectory file is written "once for all devices"; which one is not stated | 22.6.2 | **P2** | Yes |
| **T21** | Register a mission, run a Mission Report, and look. Does it contain the signed GCP residuals? | The 2025.21 release note says residuals are "included in the report"; the Mission Report topic does not mention them | 17.6 | **P2** | Yes |
| **T22** | Export a LAS and inspect the file directly — header fields, VLRs, sidecar contents | Trimble's topics do not enumerate LAS headers. Something undocumented may be written | 22.7, 23.4 | **P2** | Yes |
| **T23** | Draw a Point Cloud tab selection across scans from two trajectories and observe | Whether TBC warns, prevents or silently permits is not stated | 22.4 | **P2** | Yes |
| **T26** | **Does exported imagery inherit or otherwise reflect a registration adjustment?** Compare a station's position before and after | Imagery is positioned from the trajectory; nothing states whether it is recomputed | 19.1 | **P2** | Yes |
| **T27** | **What imagery streams actually exist on the MX60, and which are exposed through TBC export?** Resolve the apparent inconsistency between the side-images export option and the MX60 export tree lacking Planar cameras. **Also a vendor question — V-8** | **Do not write MX9/MX90 camera behaviour into MX60 procedure.** The option's presence in a dialog is not evidence the sensor exists | 19.2 | **P2** | Yes |
| **T30** | Attempt both reconstruction paths — timestamp matching and trajectory geometry comparison — on a dataset with two candidate trajectories | Neither has been attempted; both are the fallback if provenance is queried | 23.7 | **P3** | Yes |
| **T1** | Default vs High Quality filter preset — selection criteria | High Quality enables three filters unconditionally | 13.3 | **P2** | Yes |
| **T2** | Isolated Points default state | Trimble's own text contradicts itself | 13.3 | **P3** | Yes |
| **T3** | **Does Reflective Panels remove legitimate retro-reflective returns from signs and line marking?** | On sign and retroreflectivity work, those returns **are** the deliverable | 13.3 | **P1** | Yes, with risk |
| **T4** | Range Max default vs useful range in bright sun and at oblique incidence | Points may be retained well beyond useful range | 13.3 | **P2** | Yes |
| **T5** | Fog and Sun filters applied when those conditions did not occur | Both remove real returns | 13.3 | **P2** | Yes |
| **T6** | Colouriser forward vs backward camera preference, and its effect on fringing | No selection rule given | 13.4, 19.5 | **P3** | Yes |
| **T7** | Registration Auto-Saving **default state** | `Targets.csv` is the registration's field book, and a wrong dialog answer empties it | 15.3 | **P2** | Yes |
| **T9** | **Target-Bundle Adjustment** — test both states with independent checks | Checking it makes the adjustment **coarser** (250 m vs 70 m); the name reads backwards | 15.7 | **P2** | Yes |
| **T10** | Which Parametrix coordinate systems does POSPac recognise directly, and which trigger the ITRF00 path? | Answerable once, then known | 5.3, 12.4 | **P2** | Yes |
| **T11** | Multipath default **Medium** on open-sky corridors | Medium is described as being for *degraded* coverage | 12.3 | **P3** | Yes |
| **T12** | DMI scale factor SD default **5 %** — was the wheel actually measured? | Trimble says set it to 100 % if unknown | 12.3 | **P3** | Yes |
| **T13** | LiDAR QC range default 3–100 m | Useful scanner range and useful aiding range are different questions | 12.7 | **P3** | Yes |
| **T14** | LiDAR QC **Lasers = All** | **The default contradicts the guidance printed beside it** | 12.7 | **P3** | Yes |
| **T15** | **Which registration type, when?** Test Global, Local and Global-then-Local with independent checks | No selection rule published; Global-then-Local gets no guidance and appears in every screenshot | 15.5 | **P1** | Yes, with risk |
| **T16** | Working cutting plane thickness for the visual checks | Trimble's own screenshots show 0.030 and 5.000 with no basis | 16.7, 18.6 | **P2** | Yes |
| **T17** | **Sample points** random sampling in the classified LAS exporter | A destructive thinning with no documented spatial rule; default state not stated | 22.6.1 | **P2** | Yes |
| **T24** | How much run overlap is enough for run-to-run registration? | Trimble states the requirement qualitatively only | 16.6 | **P2** | Yes |
| **T25** | Which feature types are fit for horizontal control, vertical control, or both, at MX60 density and incidence? | Will shape control design more than any software setting | 5.5, 17.3 | **P1** | Yes, with risk |

**P1 tests: 6.**

---

## Table 3 — Vendor Clarifications Required

Only Trimble can answer these.

| ID | Question | Why it matters | § | Priority | Operate without? |
|---|---|---|---|---|---|
| **V-1** | **When Export timestamps causes reprocessing from raw data, which trajectory is used?** | Pairs with T18. A direct yes/no question with the largest consequence in the workflow | 22.3 | **P1** | Yes — by keeping timestamps off |
| **V-2** | Is the MX60 laser control presented as *Measurement Prog* + *Line Speed*, or as a combined *Laser Mode*? Which TMI version applies? | The Quick Start Guide and TMI Rev L disagree | 7.7 | **P2** | Yes |
| **V-3** | Which TBC version is installed on our workstation? | Two version-dependent behaviours, both legacy | 1.6, 4.3 | **P2** | Yes |
| **V-4** | Which MX60 configuration do we have — from the serial number? Are GAMS and DMI fitted? Which rack? | Pairs with D-2 | 4.1 | **P1** | **No** |
| **V-5** | **Trimble GAMS Antenna Kit Installation & Operation Manual** — not held | Needed to complete the lever-arm procedure if GAMS is fitted | 7.3 | **P2** | Only if GAMS is not fitted |
| **V-6** | **Trimble DMI Installation & Operation Manual** — not held | Contains the scale factor for the measured wheel diameter, which §12.3 needs | 7.3, 12.3 | **P2** | Only if DMI is not fitted |
| **V-7** | Does the **Lateral Range Limit** affect accuracy, or is it purely a data-volume tool? | Undocumented | 7.7 | **P3** | Yes |
| **V-8** | **What is the MX60's actual camera complement, and which streams are exposed through TBC export?** | Pairs with T27. The MX60 export tree shows no Planar cameras while the export option persists | 19.2 | **P2** | Yes |
| **V-9** | Does **LiDAR QC** have its own POSPac dependency? | Trimble does not state one, but directs configuration questions to Applanix Support | 4.5 | **P2** | Yes |
| **V-10** | Which trajectory do **TMX export** and **Publish to TRCPS** send when a run has both an imported and a registered trajectory? | Both carry trajectory geometry; neither says which | 22.6.2, 22.6.6 | **P1** | Yes, with risk |
| **V-11** | **Which report contains the signed GCP residuals** added in TBC 2025.21? | The only mobile mapping report topic does not mention residuals | 17.6 | **P2** | Yes |
| **V-12** | Does any TBC export write the source trajectory into a LAS header, VLR or sidecar? | The one provenance question documentation cannot answer | 23.4 | **P1** | Yes, with risk |
| **V-13** | Does removing and refitting the Sensor Unit disturb the calibration? What symptoms indicate drift? | Determines whether calibration is periodic or routine | 14.7 | **P1** | Yes, with risk |
| **V-14** | Is the retro-reflective target check the recommended periodic verification for the MX60, and at what interval? | Trimble says "regularly" and defines nothing | 18.7 | **P2** | Yes |
| **V-15** | Scanner field of view — **346°** *(UG p.54)* or **360°** *(spec sheet p.2)*? | Matters for occlusion geometry | 4.1 | **P3** | Yes |
| **V-16** | When should PFIX be preferred over registration? | This document's framing of the distinction is inferred, not stated by Trimble | 20.5 | **P2** | Yes |
| **V-17** | Does the "coordinate system without Geoid" restriction on TMX export apply to the MX60, or only the MX9? | Stated for the MX9 only | 22.6.2 | **P2** | Yes |

**P1 vendor questions: 5.**

---

## Summary

| | Total | P1 | Blocks operation |
|---|---|---|---|
| **Parametrix Decisions** | 54 | 24 | 9 |
| **Field Tests** | 29 | 6 | 0 |
| **Vendor Clarifications** | 17 | 5 | 1 |
| **Total** | **100** | **35** | **10** |

> **Ten items genuinely block operation.** They are: D-2/V-4 (configuration), D-10 (POSPac
> licence), D-13 (acceptance criteria), D-16 (control design), D-19 (computation mode), D-21
> (datum and epoch), D-35 (Cleanup policy), D-41 (pass pattern), D-42 (base station strategy).
>
> **The remaining ninety do not prevent defensible work.** They make it less consistent, less
> efficient, or dependent on individual judgement — which is what an SOP exists to reduce, and is
> exactly the work this backlog represents.

*Contact for vendor questions: `mx_support@trimble.com` · Americas +1-289-695-4416
*(MX60 UG Rev B, p.51)*
