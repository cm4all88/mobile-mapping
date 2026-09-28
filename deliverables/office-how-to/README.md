# MX60 Office How To

**Working Version `2026-09-11-a` · LIVING DRAFT — INTERNAL REVIEW**

One of four coordinated deliverables. This is the **primary office training and processing guide**
for a survey employee who may have minimal MX60 processing experience. It shows how to move an
MX60 job through Trimble Business Center in the correct order, what normal results look like, what
to check when something is wrong, and when to stop and raise the issue.

It assumes the reader already has the survey and CAD knowledge appropriate to the assignment. It
does not teach basic survey adjustment, datums or coordinate system theory.

| Question | Document |
|---|---|
| Why does it work this way? | Technical Manual |
| Must I? | SOP |
| **How do I do it in the office?** | **This guide** |
| How do I do it in the field? | Field How To |

**This guide cannot create a requirement.** If it says something must be done and the SOP does not
require it, the SOP governs.

## The four questions

Every section answers the same four, in the same order: **Do · Look at · Expect · Stop if**.
If you read nothing else in a section, read **Stop if**.

## Files

| File | § |
|---|---|
| `00-front-matter.md` | |
| `01-how-to-use-this-guide.md` | 1 |
| **Intake and setup** | |
| `02-data-intake.md` · `03-checking-mission-information.md` · `04-calibration-state-intake.md` | 2–4 |
| `05-project-setup.md` · `06-coordinate-systems.md` · `07-importing-the-mission.md` | 5–7 |
| **Trajectory and scans** | |
| `08-trajectory-processing.md` · `09-pospac-requirements.md` · `10-reading-the-trajectory.md` | 8–10 |
| `11-generate-scans.md` · `12-checking-the-scans.md` · `13-calibration.md` | 11–13 |
| **Registration** | |
| `14-importing-control.md` · `15-gcp-and-check-point-configuration.md` | 14–15 |
| `16-register-a-run.md` · `17-register-a-mission.md` · `18-register-run-to-run.md` | 16–18 |
| `19-editing-a-registration.md` · `20-residual-review.md` · `21-update-scans.md` | 19–21 |
| **QC and remedies** | |
| `22-visual-qc.md` · `23-imagery-qc.md` · `24-lidar-qc.md` | 22–24 |
| `25-degraded-gnss.md` · `26-pfix.md` | 25–26 |
| **Identify, export, record** | |
| `27-identifying-registration-results.md` · `28-trajectory-provenance.md` | 27–28 |
| `29-cleanup.md` · `30-export.md` · `31-the-pre-export-check.md` | 29–31 |
| `32-final-qa-qc.md` · `33-archiving.md` · `34-documentation-required.md` | 32–34 |
| `35-common-problems.md` | 35 |
| **Appendices** | |
| `appendix-A-office-processing-checklist.md` | A |
| `appendix-B-registration-checklist.md` | B |
| `appendix-C-qc-checklist.md` | C |
| `appendix-D-export-and-delivery-checklist.md` | D |
| `appendix-E-archive-and-cleanup-checklist.md` | E |
| `appendix-F-record-templates.md` | F — the five records with no software artefact |

## Build

```
python3 tools/build-doc.py office            # the assembled markdown
python3 tools/build-doc-page.py office       # the browsable page
python3 tools/check-warnings.py              # every registered warning is verbatim
```
