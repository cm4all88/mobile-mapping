# Parametrix MX60 document style specification

**One system, four documents.** Every named style below applies identically in the Technical
Manual, the SOP, the Field How To and the Office How To, except where §3 says otherwise.

**Authority:** *Parametrix Brand Guide* v6, November 2023. Page citations are to that guide.

> **Read the Source column.** **brand p.N** means the rule is a Parametrix brand rule, cited.
> **extension** means the guide is silent and the rule was built from brand values for this
> document family — it is not a Parametrix brand rule and is not to be quoted as one.
> `brand-source-status.md` lists every extension and why it exists.

---

## 1 · Foundations

### Colour

| Role | Value | Source |
|---|---|---|
| Parametrix Red | `#EE3D24` | **brand p.18** |
| Charcoal | `#333333` | **brand p.18** |
| Medium Gray | `#676768` | **brand p.18** |
| White | `#FFFFFF` | **brand p.18** |
| Secondary — Progress Orange, Optimistic Yellow, Future Green, Clean Blue | `#F36E21` `#FCC214` `#3FB549` `#0073BB` | **brand p.18** |
| Tertiary — Calm Red / Orange / Blue / Yellow, Light Gray 1–4 | see `brand-tokens.css` | **brand p.18** |
| **Red is used sparingly** | "Red text should always be used sparingly" | **brand p.23** |
| Secondary colours are accents, for personality and **categorization** | | **brand p.18** |
| Tertiary colours are used **sparingly**, for "mapping, charts, graphs, and highlighting" | | **brand p.18** |

### Type

| Role | Face | Fallback | Source |
|---|---|---|---|
| Headlines | **Klinic Slab** | Rockwell | **brand p.16** |
| Body and subheadings | **Franklin Gothic URW** | Franklin Gothic | **brand p.16** |
| Quotes and accents | **Freight Text Pro** | Georgia | **brand p.16** |
| Filenames, paths, identifiers | — | system monospace | extension |

The three licensed faces are not held. Each stack requests the licensed face and falls back to the
alternate **the guide itself names**. No fourth typeface is introduced.

### Space

| | | Source |
|---|---|---|
| "White space and balanced geometry are thoughtfully employed … to maximize clarity and scanability" | the governing principle | **brand p.9** |
| Body line spacing is **increased** for readability | 1.68 | **brand p.23**, value extension |
| Base unit 4 px; scale 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 | | extension |
| Measure 78 characters | | extension |
| Square corners | the guide's compositions have no rounded corners | **brand pp.15, 23, 25** |

### The logo

| | Source |
|---|---|
| Primary (charcoal/red) on white and light grounds; **knockout on dark or busy grounds** | **brand p.11** |
| Clear space on all four sides **≥ the height of the right side of the x** | **brand p.13** |
| **Minimum 1 inch wide** | **brand p.13** |
| The red square is never recoloured | **brand p.11** |
| No recolouring, added elements, boxes, underlines, distortion, rotation, effects or drop shadows | **brand p.14** |
| **No tagline** — "client-facing document" sits in the *Do Not Use Tagline* column | **brand p.12** |

### The two graphic elements

| | | Source |
|---|---|---|
| **Spacer arrow** | The divider. Always **1 pt**, barbed head, red or charcoal, with room above and below. Sits between a heading and the body that follows it | **brand pp.16, 19** |
| **ix formation** | The "i" and "x" of the logo, isolated. **Justified to the left edge**, bleeding off the left and bottom. A floating element, a corner element, or a watermark. **It is not the logo** | **brand pp.10, 15, 23** |

---

## 2 · The named styles

| Style | Rule | Source |
|---|---|---|
| **Title** | Klinic Slab, 44 px / 1.08, charcoal. Cover only. Followed by a red spacer arrow | brand p.16 · sizes extension |
| **Subtitle** | Franklin Gothic, 19 px / 1.4, Medium Gray. 12 px below the Title | brand p.16 · extension |
| **H1** | Section opener. Klinic Slab 32 px / 1.14, charcoal. The section number precedes it as a **filled chip in the document accent**, numeral knocked out in `--doc-accent-on`. A red spacer arrow follows the heading | brand pp.16, 19 · chip follows the guide's own page-number device · sizes extension |
| **H2** | Franklin Gothic 22 px / 1.28, weight 600, charcoal. 40 px above, 12 px below, hairline rule above | brand p.16 · extension |
| **H3** | Franklin Gothic 17.5 px / 1.3, weight 600. 28 px above, 8 px below | extension |
| **H4** | Franklin Gothic 15 px / 1.3, weight 600, Medium Gray | extension |
| **Body** | Franklin Gothic 17 px / **1.68**. 14 px between paragraphs. Measure 78 ch. No first-line indent | brand pp.16, 23 |
| **Bullets** | Disc, 1.1 em hang, 6 px between items | extension |
| **Numbered procedures** | Decimal, 1.6 em hang, numeral in weight 600. **Procedure steps are numbered; explanatory lists are bulleted.** The distinction is meaningful and is enforced | extension |
| **Tables** | Header: Franklin Gothic 12.5 px caps, letter-spacing 0.08em, on **Light Gray 4**, charcoal text, 1 px rule below. Body 15.5 px. Row rules 1 px **Light Gray 3**. **No vertical rules, no striping.** Horizontal scroll below 640 px | extension, from the p.9 clarity principle |
| **Figure captions** | Franklin Gothic 13.5 px, Medium Gray, 8 px below the figure. `Figure n` in weight 600, then the caption, then the citation | extension |
| **Quotation** | **Freight Text Pro in Parametrix Red, with a red rule at the left.** The guide's own treatment, used for quoted source text where it carries weight | **brand p.16** |
| **Notes** | 3 px left rule in Light Gray 2, 16 px inset, Light Gray 4 ground, no label | extension |
| **CAUTION** | 3 px left rule in **Parametrix Red**, label `CAUTION` in Franklin Gothic caps 11 px red. Reserved for the consequence classes in the warning register | brand p.11 accent logic · extension |
| **IMPORTANT** | 3 px left rule in **Calm Red**, label `IMPORTANT`. Deliberately the same hue family as CAUTION, one step down in urgency | extension |
| **WARNING** | **Not used.** The register defines two levels and a third would dilute both. A brand WARNING treatment, if one is ever published, maps onto CAUTION | project rule |
| **In Plain Language** | Full panel on Light Gray 4, 20 px pad, 3 px left rule in Medium Gray. Label in caps. The four sub-headings — *What we just did · Why it matters · What can go wrong · What good looks like* — inline in weight 600 | extension |
| **Why This Matters** | 3 px left rule in charcoal, label in caps. Lighter than a panel: an aside, not an alert | extension |
| **Evidence tags** | Franklin Gothic caps 11 px, letter-spacing 0.12em, on a 3 px left rule. Charcoal for *Trimble documented procedure*, Light Gray 1 for *Observed software behavior*, Calm Blue for *proposed*, Future Green for *adopted*, Calm Yellow for *decision required*, Calm Orange for *testing or vendor clarification*. **Tag wording is never abbreviated or restyled per document** | extension, palette only |
| **Cross references** | `§n` or `§n.n` in body weight. Link-coloured on hover in HTML. **Never a bare "see above"** | project rule |
| **Citations** | `*(TBC 22905)*` — 0.94 em, Medium Gray. Brackets neither added nor removed | project rule |
| **Code and identifiers** | Monospace 0.92 em on Light Gray 4, 2 px horizontal pad. Filenames, paths and software identifiers only | extension |
| **Header** | Running: document type as a **filled accent chip**, section number and title in Franklin Gothic 11 px caps Medium Gray. A 1 px accent rule below | extension |
| **Footer** | **ix formation at the bottom-left**, as the letterhead does. Left of centre: document identifier and revision. Right: page *n* of *n*, and `Not issued` while in draft | **brand p.23** · layout extension |
| **Revision information** | Cover and footer. **The fields, their numbering convention and the approval block are document-control decisions, not branding** — see the note below | project rule |
| **Appendix headings** | As H1; the letter replaces the number, and the word `APPENDIX` precedes it at 11 px in the document accent | extension |
| **Cover** | The **ix formation cover**: ix formation justified to the left edge, bleeding off left and bottom; logo top-left with clear space; Title, Subtitle, document-type label in the accent colour; red spacer arrow. No photography — the guide specifies this archetype for exactly the case where no relevant high-quality photograph exists | **brand pp.15, 25** · adaptation extension |

> **Branding is not document control.** Revision numbering, document identifiers, approval
> authorities, effective-date rules, retention periods and controlled-copy terminology are not
> settled by a visual standard and are not settled here. They remain open Parametrix decisions
> (**D-1** and the document-control items in the master register). The styles reserve the space;
> they do not fill it.

---

## 3 · Document identity

All four are unmistakably one family: same logo, same palette, same typefaces, same callouts, same
tables, same ix formation. One token differs.

**`--doc-accent`** — one **secondary** colour per document, used for the section number chip, the
document-type chip, the header rule and the appendix letter. Nowhere else.

It is applied as a **filled chip with knocked-out text**, not as coloured type. Two reasons, and
both matter:

- The guide numbers its own pages with a filled red square and a white numeral. A filled chip is
  the brand's existing device, not a new one
- As text on white, three of the four secondary colours fail ordinary contrast — Optimistic Yellow
  at 1.6:1 is unreadable. On a chip, the ink is chosen per accent (`--doc-accent-on`): white on
  Clean Blue at 5.0:1, charcoal on the other three at 4.3:1 to 7.7:1. **All four are legible, and
  the treatment is identical across the family**

| Document | Accent | Hex |
|---|---|---|
| **Technical Manual** | Clean Blue | `#0073BB` |
| **Standard Operating Procedure** | Progress Orange | `#F36E21` |
| **Field How To** | Future Green | `#3FB549` |
| **Office How To** | Optimistic Yellow | `#FCC214` |

The guide supports the mechanism directly: secondary colours "are to be used as accent … useful
for adding specific personality to brand materials and **to enhance categorization**" *(p.18)*.

Parametrix Red is **not** used for document identity. It is the brand's main colour and stays
reserved for the logo, the spacer arrow, quotations and CAUTION — which keeps it sparing, as p.23
requires.

> **One caveat.** Page 28 correlates these four colours with sectors — green environmental, yellow
> transportation, blue water, orange community — in the context of a social-media template. These
> are internal technical documents and imply no sector. The assignment lives in one token and can
> be changed or dropped without touching anything else.

---

## 4 · Where the visual system is applied

| | |
|---|---|
| `brand-tokens.css` | Every value. Imported by all four builds |
| `tools/doc-page-template.html` | The shared page shell |
| `tools/build-doc-page.py` | `manual` · `sop` · `field` · `office` — one builder, four configurations |
| `brand/logo/` | The four logo settings, the spacer arrow, the ix formation |

**No document's content carries styling.** A change to the visual system is a change to
`brand-tokens.css` and nothing else.
