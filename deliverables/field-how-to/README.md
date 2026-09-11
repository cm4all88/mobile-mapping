# MX60 Field How To

**Draft A · Not issued · 2026-09-11**

One of four coordinated deliverables. This one shows **how to run the MX60 in the field**. Meant to
be used in or near the vehicle.

| Question | Document |
|---|---|
| Why does it work this way? | Technical Manual |
| Must I? | SOP |
| **How do I do it in the field?** | **This guide** |
| How do I do it in the office? | Office How To |

**This guide cannot create a requirement.** If it says something must be done and the SOP does not
require it, the SOP governs.

**Start with Appendix E** — the ten things that cost the most if missed. One page, for the vehicle.

## Files

| File | § |
|---|---|
| `00-front-matter.md` · `01-how-to-use-this-guide.md` | 1 |
| **Setting up** | |
| `02-before-you-leave-the-yard.md` · `03-equipment-inspection.md` | 2–3 |
| `04-mounting-the-sensor-unit.md` · `05-connections-and-cables.md` | 4–5 |
| `06-power-system-checks.md` · `07-battery-protect.md` | 6–7 |
| `08-starting-the-system.md` · `09-connecting-to-tmi.md` | 8–9 |
| `10-mission-setup.md` · `11-disk-check.md` | 10–11 |
| **Initialization** | |
| `12-navigation-initialization.md` · `13-gams-considerations.md` · `14-reading-navigation-status.md` | 12–14 |
| **Collecting** | |
| `15-recording-runs.md` · `16-driving-practices.md` · `17-gnss-while-driving.md` | 15–17 |
| `18-field-qc-indicators.md` · `19-using-comments.md` · `20-stopping-and-restarting.md` | 18–20 |
| **Finishing** | |
| `21-the-closing-sequence.md` · `22-shutdown.md` · `23-field-close-out.md` | 21–23 |
| `24-re-collect-or-not.md` · `25-data-transfer-and-handoff.md` | 24–25 |
| `26-what-must-accompany-the-data.md` · `27-common-problems.md` | 26–27 |
| **Appendices** | |
| `appendix-A-preflight-checklist.md` | A — printable |
| `appendix-B-end-of-mission-checklist.md` | B — printable |
| `appendix-C-field-record-form.md` | C — the template. **No software produces this** |
| `appendix-D-tmi-status-reference.md` | D |
| `appendix-E-quick-card.md` | **E — the quick card** |

## Build

```
python3 tools/build-doc.py field            # the assembled markdown
python3 tools/build-doc-page.py field       # the browsable page
python3 tools/check-warnings.py             # every registered warning is verbatim
```
