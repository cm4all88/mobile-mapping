# Before it goes in a vehicle — the iPad test

**None of this was run here.** The app was driven end to end in Chromium: all eight forms
completed, the gate verified to refuse an incomplete form, eight PDFs written, records verified to
survive a reload, deletion of an unsent record verified to be refused, no console errors, and no
horizontal scrolling at phone width. **A desktop browser is not an iPad**, and the two things that
matter most here — iOS storage eviction and the iOS share sheet — have no desktop equivalent.

Run this on the iPad that will be used, with the file installed as in `README.md`. Thirty minutes.

## 1 · Install and first run

- [ ] File opens from Files in Safari
- [ ] **Share ▸ Add to Home Screen** offered and completed
- [ ] Opening from the home screen fills the screen, with no Safari address bar
- [ ] The "Add this to the home screen" caution is **not** shown when opened that way
- [ ] All eight forms and the job card are listed

## 2 · Offline

- [ ] **Aeroplane mode on**
- [ ] Close the app, reopen from the home screen — it opens and is complete
- [ ] Fill the job header and complete the Preflight Checklist
- [ ] The gate refuses until every item is cleared and it is signed
- [ ] Confirming writes the record; the PDF opens

## 3 · It survives

Do these in order, offline, with at least one record waiting to send:

- [ ] Switch to another app and back — the record is still there
- [ ] **Close the app from the app switcher**, reopen — record still there
- [ ] **Restart the iPad**, reopen — record still there
- [ ] Leave it overnight, reopen — record still there
- [ ] Leave it **eight days** without opening, reopen — record still there
      *(this is the one that proves the home-screen install; if it fails, the app was
      not installed to the home screen, and no record should be trusted to it)*

## 4 · Printing

- [ ] Open a completed record, tap **Print**
- [ ] The iPad print sheet shows the Parametrix record sheet, not the app
- [ ] Pinch out on the preview, share, **Save to Files** — a readable PDF
- [ ] Print to a real printer: the header, the item states and the footer are legible

## 5 · Transferring

- [ ] **Send to the office** opens the share sheet with a `.pdf` and a `.json`
- [ ] Send to Mail — both attach, and open at the other end
- [ ] Send to Files — both save
- [ ] Cancelling the share sheet leaves the record **Waiting to send**, not Handed over
- [ ] After a successful share the record reads **Handed over**, never Delivered
- [ ] *The office has it* (two taps) moves it to **Delivered**
- [ ] A record that is not Delivered offers no Delete
- [ ] *Delete this record* on a Delivered record takes two taps

## 6 · In the vehicle

- [ ] Readable through the windscreen in direct sun
- [ ] Every row can be tapped wearing work gloves
- [ ] Typing a time or a note does not lose the keyboard focus mid-word
- [ ] The search finds an item by a word from its text
- [ ] It works in portrait and in landscape, and in the dark cab at night

## 7 · The whole mission

- [ ] Preflight, Field Record and End of Mission completed on one job without re-entering
      the project number, task number, date, operator or vehicle
- [ ] All three records carry the same project and task in their record ids
- [ ] The office receives all three and can tell which operator completed each

## If something fails

Note which box, on which iPad and which iOS version. Anything in section 3 is serious: it means a
record could be lost, which is the one thing this app exists to prevent.
