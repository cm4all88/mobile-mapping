# marketing

Outward-facing material. **Everything else in this repository is internal**; this folder is the
exception, and it is governed differently because of it.

## The rule that applies here

The four documents under `deliverables/` carry an explicit warning that **nothing in them may be
quoted to a client as an existing Parametrix standard**. Zero Parametrix procedures have been
adopted. That constraint does not disappear when the audience changes — it binds hardest here,
because this is the only material that leaves the building.

So a brochure in this folder may state:

- **Trimble's published equipment specifications**, with the conditions Trimble attaches
- **What Parametrix owns and operates** — an MX60 Premium
- **What mobile mapping produces**, and how accuracy is established per project

and may not state:

- a **delivered accuracy figure** — `D-13` and `D-16` are open
- Trimble's **no-outage sub-centimetre figure** — it assumes a DMI, and `D-2` has not established
  whether this system carries one
- **delivered project experience** — the system has been run internally and nothing has been
  delivered to a client under it
- **certification or compliance** with any named standard

Each brochure carries those four as a final page headed *delete before it goes out*, so the
constraint travels with the file rather than living only here.

## Parametrix-Mobile-Mapping-Capability-Brochure.docx

Five pages: cover, what it is and where it fits, the system, how accuracy is established, and the
internal notes page marketing deletes.

```bash
node marketing/build-capability-brochure.js
```

Every specification figure on page 3 traces to `reference/mx60-reference-data.csv` — the project's
authority for numbers — and the `SPEC-` ids are in comments beside each one in the build script.
Change a number there, not here.

Colours and type come from `deliverables/_control/style/brand-tokens.css` (Parametrix Brand Guide
v6, pp.16, 18). No tagline: the guide puts *client-facing document* in the **Do Not Use Tagline**
column, p.12.

### Not verified

**The .docx has not been rendered and looked at.** LibreOffice in the build environment cannot load
a `.docx` at all — a one-paragraph test file fails the same way — so the same limitation noted in
`tools/README.md` for `build-sop.js` applies. The file's XML parses, its tables carry dual widths,
its bullets are a real numbering definition, and the content was proofed from the packed document.
**Open it in Word and look at it before anything is printed.**

The page proofs in the commit that added this file were rendered from an HTML mirror of the packed
document, which confirms the copy and that each page's content fits a page. It is not a
substitute for opening the file.
