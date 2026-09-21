# 35. Common Problems — What to Check First

## 35.1 Troubleshooting pattern

Do not troubleshoot an MX60 project by trying commands until the picture looks better.

1. **State the symptom.** Name the command, object, residual, visual condition or missing output.
2. **Find the last known good stage.** Intake, trajectory, scan generation, registration, Update
   Scans, QC and export are separate states. Go back to the first state that is wrong.
3. **Change one thing at a time.** Stacked registrations and repeated processing can hide the cause.
4. **Verify visually as well as numerically.** A clean number is not proof that the cloud is right.
5. **Preserve the evidence.** Do not run Cleanup or overwrite a useful intermediate state while you
   are still diagnosing the problem.
6. **Raise field failures as field failures.** Missing coverage, missing overlap, a dead sensor or
   a missing closing sequence cannot be repaired by clever office processing.

## 35.2 Symptom table

| What you see | Check first | If that is not it | Stop or raise when |
|---|---|---|---|
| **A registration command is dimmed** | Does the run have at least one **generated scan**? | Return to §11 and confirm scan generation completed | The required object still is not available after the prerequisite exists |
| **GAMS or DMI settings are dimmed** in Process Raw Trajectory Data | Was the sensor enabled during acquisition? | Check the field record and Field How To §10 | If it did not log, treat it as a field configuration issue, not a TBC setting to invent |
| **Trajectory is NAV, not SBET** | Is `POS_1/raw/` present and is POSPac available? | §§2, 8 and 9 | The required trajectory processing path is unavailable |
| **Picked targets vanished** | Was a reload prompt answered **No**? | Check §19 and the state of `Targets.csv` | The target record was emptied and cannot be reconstructed reliably |
| **Residuals got worse after a second registration** | Did you register twice? | Use **Edit** per §19 instead of stacking another adjustment | You no longer know which adjustment state produced the current result |
| **Exported cloud is not the registered one** | Was **Update Scans** run? | Confirm the stations carry `_reg_####` and use §31 | The export state cannot be positively tied to the reviewed registration |
| **Update Scans was run but export still points at `Sbet` scans** | Check the exact scan nodes selected for export | Re-run the §31 pre-export check and select the `_reg_####` scans beneath the intended registered trajectory | The export selection cannot be positively tied to the checked registration |
| **Two passes are offset in the cutting plane** | Is rendering set to **Scan Color**? | Follow §22 and check whether the offset changes with range | The passes remain visibly inconsistent after the correct view is established |
| **Surface looks thick even though numbers look fine** | Attitude error or calibration | Inspect whether thickening grows with range; §§13 and 22 | Visual QC contradicts the numerical result |
| **Side camera images export black** | Corrupted imagery | Check the rest of the image set using §23 | Imagery is required and corruption is not isolated |
| **Imagery color sits beside feature edges** | Camera boresight | §13.2 and visual QC | The offset persists and affects the intended use |
| **Nothing exports to TopoDot** | Were scans generated and run views closed? | Follow §30 from its beginning | The expected objects exist but the exporter still produces nothing |
| **Extract Classified Point Cloud produced nothing** | Was it run before **Export to LAS (Trajectory Split)**? | Repeat the documented sequence in §30 | The documented order still does not produce the expected object |
| **A wrong antenna model is found before processing** | It must read **Trimble 112735** | Correct the input before computing; §8 | The correct MX60 antenna model cannot be established |
| **A wrong antenna model is discovered after downstream work exists** | Stop using the derived scans/registration/export as the current state | Return to §8, correct and recompute the trajectory, then rebuild the downstream products that depended on it | You cannot establish which derived products were built from the corrected trajectory |
| **Whole trajectory is degraded** | Antenna model must read **Trimble 112735** | Base data, coordinate information and §8 | The model or trajectory inputs cannot be verified |
| **Height bias across the whole job** | Antenna model, geoid and base coordinate | §§5 and 8 | The bias is systematic or its cause cannot be isolated |
| **RMS coloring has gaps** | Registered segments can show **Undefined RMS** | §§10 and 27 | The gap is accompanied by another trajectory or registration problem |
| **No overlap rows in run-to-run results** | Confirm the runs truly overlap there | §18 | Required overlap was not collected |
| **LiDAR QC does not produce a useful result** | Do the runs overlap and does the machine meet the memory requirement? | §24 | The prerequisite data or hardware is not available |
| **MTA or GPU driver documentation appears relevant** | It is not the MX60 path | Return to §11 | Stop using MX9/MX90 instructions on an MX60 job |
| **TBC sign-in asks for an emailed code** | TBC 2026.10 uses Trimble ID two-step verification | Follow the current sign-in path | Access cannot be established without bypassing company or Trimble controls |

## 35.3 When the answer is "re-collect"

> **Equipment/software validation note:** screenshots of the actual TBC 2026.10 dialogs, tree
> states and result panes are intentionally deferred until a real Parametrix mission is processed.
> The capture list is in `_control/equipment-arrival-validation-checklist.md`. Do not substitute
> screenshots from a different MX platform merely to make this draft look complete.


Missing coverage, missing overlap, a mission with no closing sequence and a sensor that logged
nothing are field problems. The office guide may help identify them, but it cannot manufacture the
missing observations.

**Raise the non-conformance. Do not absorb it.** A quiet workaround makes the current job harder to
defend and teaches the next processor the wrong recovery method *(SOP §22.3)*.
