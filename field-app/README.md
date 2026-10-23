# field-app

The Preflight Checklist as something a crew fills in on a tablet, instead of a sheet of paper
that gets photographed and lost. One checklist, built as a prototype so the shape can be argued
with before the other eight are built the same way.

```bash
python3 tools/build-field-app.py        # rebuild after editing Appendix A
python3 tools/build-field-app.py --check  # a gate in tools/check-all.py
```

| | |
|---|---|
| `MX60-preflight.html` | **the file that goes on the tablet.** One file, no network, 160 KB |
| `review-copy/MX60-preflight.html` | the same page as a review copy for a claude.ai link. It cannot print and it will not open without a signal |

## It is built, not written

Every item, group, section reference and header field is read out of
`deliverables/field-how-to/appendix-A-preflight-checklist.md` at build time. There is no second
copy of the checklist to drift. `--check` fails if the built file no longer matches the markdown,
and that check runs in `tools/check-all.py`, so Appendix A cannot be edited and the tablet left
behind — which is exactly what happened to the printed checklist in `SOP-v1-superseded/`.

Each `§` beside an item is resolved to the Field How To heading it points at, so the operator
reads **§9.3 Confirm every sensor is present** rather than a bare number. A reference with no
matching heading fails the build.

## The gate

The clearance panel at the end stays locked, and says what it is waiting for, until:

- all **36 items** are ticked or marked N/A,
- **Date, Operator and Vehicle** are filled in,
- the three items whose own text asks for a value have one, and
- it is **signed**.

Tapping an outstanding item in the panel goes to it. Confirming closes the record: the checklist
becomes read-only and the print and send actions appear.

**N/A is not a general escape.** Only the five items whose own text reads *if fitted* — GAMS,
the DMI, the auxiliary battery — can be marked N/A, and the record says N/A rather than cleared.
Every other item is a tick or an unfinished checklist. A gate that cannot be satisfied honestly is
a gate crews learn to tick through.

**Three items take a value, not a tick**, because Appendix A asks for one: the presentation seen
(§10.2), the time status reached green (§14.5) and the time significant recording began (§14.5).
They are declared in `deliverables/_control/field-app-fields.csv`, and a row that no longer
matches an item fails the build.

## On the tablet

Offline is the design centre, not a fallback. The file holds its own styling, the Parametrix
logo and the whole checklist; nothing is fetched.

1. Put `MX60-preflight.html` in the vehicle's Files folder (iCloud, a shared drive, AirDrop).
2. Open it in Safari and **Share ▸ Add to Home Screen**. It then opens full-screen like an app.
3. What the operator ticks is kept on that tablet, and survives closing the app and losing signal.

**Print** is Safari's own: *Share ▸ Print*, or the Print button in the closed record. It prints the
record sheet — mission header, every item with its state, the values, the notes, the signature and
the record id — not the app. An empty one prints as a paper checklist if a tablet fails.

## Getting it to the office — the one thing still to decide

A completed record is a JSON document (`schema: "mx60.preflight/1"`) carrying the mission header,
all 36 items with state, value and note, the signature, the times, and the hash of the Appendix A
it was built from. Completed records queue on the tablet until the office has them.

**There is no office endpoint yet, so the page does not invent one.** `SUBMIT_URL` at the top of
the script is empty, and *Send to the office* hands the record to the iPad share sheet — Mail,
Teams, Files, a shared drive — and keeps it queued. Set `SUBMIT_URL` in
`tools/field-app-template.html` to a real endpoint and a record filled in with no signal posts
itself the moment the tablet has one, with the share sheet still there as the fallback.

That endpoint is a decision, not a build step: where the records land, who reads them, and whether
the office wants JSON into a database or a PDF into the project folder. Nothing else in this
prototype is waiting on anything.

## What this prototype does not do

- **One checklist.** Appendix B (end of mission), the Field Record Form and the five Office
  checklists are the same shape and are not built.
- **No identity.** It records the name typed into *Signed*. It does not prove who typed it.
- **No sync between tablets.** Each tablet holds its own records until they are sent.
- **Not an adopted standard.** The checklist is a living draft, and the page says so on itself.
