# field-app

**MX60 Field Tools** — the eight MX60 appendices as one application on an iPad, from preflight
through field collection to office processing, with the job entered once.

```bash
python3 tools/build-field-app.py          # rebuild after editing any source appendix
python3 tools/build-field-app.py --check  # a gate in tools/check-all.py
python3 tools/build-field-app.py --dump preflight   # one parsed form, as JSON
```

| | |
|---|---|
| `MX60-Field-Tools.html` | **the file that goes on the iPad.** One file, no network, ~630 KB |
| `MX60-Office-Intake.html` | **the office side.** Drop the records in and see what arrived, what has not, and who did it |
| `review-copy/` | the same two pages for claude.ai links. They cannot print and will not open without a signal |

## The eight forms

| | Form | Source | |
|---|---|---|---|
| PF | Preflight Checklist | Field How To Appendix A | 36 items |
| FR | Field Record Form | Field How To Appendix C | 31 fields, 15 required, 4 repeating tables |
| EM | End-of-Mission Checklist | Field How To Appendix B | 25 items |
| OP | Office Processing Checklist | Office How To Appendix A | 31 items |
| RG | Registration Checklist | Office How To Appendix B | 28 items |
| QC | QC Checklist | Office How To Appendix C | 27 items |
| ED | Export and Delivery Checklist | Office How To Appendix D | 19 items |
| AC | Archive and Cleanup Checklist | Office How To Appendix E | 23 items |

## It is built, not written

Every item, field, choice, callout and section reference is read out of the eight markdown
appendices at build time. There is no second copy of any checklist to drift, and
`build-field-app.py --check` is a gate in `tools/check-all.py`. It was mutation-tested seven ways —
an item added, an item reworded, a `§` column changed, a required field losing its emphasis, a
callout edited, a reference with no heading, and an override matching nothing — and all seven are
caught.

Each `§` is resolved to the heading it points at, in this form's own document or in the SOP where
the cell names one, so the operator reads **§9.3 Confirm every sensor is present** rather than a
bare number. A reference with no matching heading fails the build.

## What binds, and where it comes from

**N/A is not a general escape.** An item can be set aside only where the document makes it
conditional — its own text reads *if fitted* or opens with *If …*, or its group is qualified, as
*Run-to-run, if used* is. Fourteen of the two hundred and twenty items qualify. The record says
N/A, not cleared.

**Required fields are the ones the document emphasises.** The Field Record Form has thirty-one
fields and requiring all of them would make the form unusable and the requirement a lie —
*Weather changes during* is blank on most missions. The document already says which ones matter:
it sets them in bold. Those fifteen are required. Nothing was added to that list.

**Three checklist items take a value, not a tick**, because their own text asks for one — the
presentation seen, the time green was reached, the time recording began, the time the mission was
closed, the run count, the SBET filename, the registration number. They are declared in
`deliverables/_control/field-app-fields.csv`; a row that matches no item fails the build.

**The signature is at the end**, not in the header, because signing is what follows the work.

## The job, entered once

Project number, task number, date, operator and vehicle are entered on the home screen and carried
into every form. The Field Record Form's own Date, Operator, Vehicle and Project rows show the
carried value rather than asking again. **The project and task numbers go into every record id and
into every PDF and JSON**, so the office can file a record in that project's Survey field records
folder without opening it.

## The gate

A form cannot be finalised until every applicable item is cleared or marked N/A, every required
value is present, the job header is complete, and it is signed. The panel at the end names what is
outstanding; tapping an entry goes to it. Confirming closes the record: it becomes read-only, a
Parametrix PDF is written for it, and it is kept until the office has it.

## Correcting a record

**A record is never edited and never deleted.** A mistake is corrected one of two ways, and both
keep the original.

**Replace** starts a new record of the same form with everything carried over from the one it
replaces, so correcting one field does not mean re-ticking thirty-six items. It will not close
without a reason. The new record carries `supersedes`, the old one gains `supersededBy`, and both
say so on screen, on the printed sheet and on the PDF.

**Void** marks a record as not counting, and asks why. A voided record **still has to reach the
office**: *"the preflight for this task was voided because the wrong vehicle was on it"* and
*"there is no preflight for this task"* are different answers, and only one of them is useful.
Voiding frees the form to be started again.

The office page shows the record that counts for each job and form: the newest that has been
neither voided nor replaced.

## Records, and what "sent" means

A completed record is kept on the tablet as JSON (`schema: mx60.fieldtools/1`) carrying the job,
every item and field with its state and value, the signature, the device, and the hash of the
appendix it was built from. The PDF is held beside it in IndexedDB.

Record history shows three states, and the difference between them is the point:

| | |
|---|---|
| **Waiting to send** | completed, on this tablet, nowhere else |
| **Handed over** | given to the iPad share sheet. **Not** delivered — a share sheet opening is not an arrival |
| **Delivered** | the office is confirmed to have it: a 2xx from the office endpoint, or the operator confirming it arrived |

**Nothing is ever removed on its own, and a record that is not Delivered cannot be deleted at all.**
`Store.remove` refuses it. Deleting a delivered record takes two deliberate taps.

### Getting a record out

*Send to the office* hands the PDF and the JSON to the iPad share sheet — Mail, Teams, Files, a
shared drive. *Print* opens the iPad print sheet on the record; pinch out on the preview to save it
to Files as a PDF. *Save the PDF* writes the file directly.

### The office endpoint — the one thing still to decide

`SUBMIT_URL` at the top of the script in `tools/field-app-template.html` is empty, so nothing
leaves the tablet by itself. Set it to a real endpoint and every record waiting posts itself the
moment the tablet has a signal, and is marked Delivered only on a 2xx. The share sheet stays as the
fallback.

What has to be settled is not code: where records land, who reviews them, and whether the office
wants the JSON into a database or the PDF into the project folder. The record already carries what
an office review needs — project, task, form, operator, completion time, and a record id that is
unique per project and task — so missing records can be identified by what is absent for a given
project and task.

## The office side — `MX60-Office-Intake.html`

A desk page, no install and no backend. Drop in the `.json` files the tablet sends — one mission
or a season of them — and it answers the three questions the office asks:

- **Coverage.** A grid of project · task against the forms, showing which were received, by whom
  and on what date, which exist only as voided records, and **which are not received at all.**
  Expected can be set to the three field forms or to all eight.
- **Records.** Every record, filterable by project, task, form or operator, each showing its
  transfer state and whether it has been voided or replaced. Downloadable as a CSV for a
  spreadsheet.
- **One record.** The full record, rendered by the **same code the tablet uses**
  (`tools/field-app-record-sheet.js` is injected into both), and printable.

A record is replaced, not duplicated, when it is read in twice, so the same files can be dropped
again without harm. A file that is not a record is rejected by name with the reason.

**It is a viewer, not the record.** What is loaded lives in that browser on that computer. The
project's Survey field records folder is the record, and the page says so on itself.

The one gap it cannot close: a job appears only once one of its records has arrived, so a task
nobody sent anything for cannot be seen from the records alone. Closing that needs a list of
expected tasks from somewhere else — the project schedule — which is a decision, not a build.

## On the iPad

Offline is the design centre, not a fallback. The file holds its own styling, the Parametrix logo,
the PDF writer and all eight forms; nothing is fetched, ever.

1. Put `MX60-Field-Tools.html` in the vehicle's Files folder (iCloud, a shared drive, AirDrop).
2. Open it in Safari and **Share ▸ Add to Home Screen**.
3. Open it from the home screen from then on.

**Step 2 is not cosmetic.** iOS clears the stored data of a site it decides is idle. A page added
to the home screen is treated as installed and is kept — and so are the records waiting in it. The
app says so on its own home screen when it detects it is running in a Safari tab.

**Before it is deployed, run `IPAD-TEST.md` on a real iPad.** None of it could be run here.

## What this does not do

- **No identity.** It records the name typed into *Signed*. It does not prove who typed it.
- **No sync between tablets.** Each tablet holds its own records until they are sent.
- **No automatic submission yet** — `SUBMIT_URL` is empty by design, above.
- **The PDF is set in Helvetica.** That is where the brand body stack resolves; the Klinic Slab
  headline face is not embeddable at this file size and is not faked.
- **Not an adopted standard.** Every form is a living draft, and every page and every PDF says so.
