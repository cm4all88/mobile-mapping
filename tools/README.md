# tools

## build-sop.js

Builds `SOP/Parametrix-MX60-Mobile-Mapping-SOP.docx` from
`SOP/MX60-SOP-COMPLETE.md`.

Converts markdown headings, tables, blockquote callouts, code blocks and lists into
Word equivalents, and adds a Parametrix cover page and a table of contents.

Callouts are styled by their leading label — CAUTION, IMPORTANT, FIELD TIP,
WHY THIS MATTERS, PARAMETRIX DECISION REQUIRED, ADVANCED — each getting a coloured
left rule and tinted background.

### Running it

```bash
npm install docx          # not preinstalled in every environment
node tools/build-sop.js
```

Re-run after any change to the markdown sections. Regenerate the assembled markdown
first if individual section files were edited.

### Note on verification

This environment has no working LibreOffice, pandoc or pdftoppm, so the output could
not be rendered and visually checked. It passes OOXML XSD validation and structural
checks (parts, relationships, content types, image references), but **open it in Word
and look at it before issuing**.


## build-checklist.py

Renders `tools/field-checklist.html` to `SOP/Parametrix-MX60-Field-Checklist.pdf` —
the four-page vehicle quick reference, a condensed form of Appendix A.

```bash
pip install playwright pypdfium2
python tools/build-checklist.py
```

Uses headless Chromium (preinstalled at `/opt/pw-browsers`) rather than LibreOffice,
which does not work in this environment. Edit the HTML to change the checklist; the
layout is plain CSS with `@page` print rules.

Output was rendered to images and visually checked — all four pages verified.
