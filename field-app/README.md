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
| `MX60-Field-Tools.html` | **the file that goes on the iPad.** One file, no network, ~620 KB |
| `review-copy/MX60-Field-Tools.html` | the same app for a claude.ai link. It cannot print and it will not open without a signal |

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
