# Parametrix brand assets

**Authority:** *Parametrix Brand Guide*, version 6, November 2023 —
`parametrix_full_brandguide_v6_11-29-23.pdf`, 32 pp. Every value in this directory and in
`deliverables/_control/style/` is cited to a page of that guide.

> **The guide is not held in this repository.** Every page citation below is therefore uncheckable
> from the repository alone. Obtain the PDF and keep it with the other sources before anything is
> issued — it is listed under *What to fetch* in
> [`../deliverables/_control/style/brand-source-status.md`](../deliverables/_control/style/brand-source-status.md).

> **The company name is written in full.** The guide, p.5: *"Please use our full name, Parametrix,
> spelled out in its entirety. Please refrain from abbreviating our name to 'PMX' or other
> short-hand spelling."* This applies to document text, file names and identifiers alike.

## Logo files

Extracted from the brand guide at 600 dpi and keyed to transparency. All four approved colour
settings *(guide p.11)*.

| File | Setting | Use |
|---|---|---|
| `logo/parametrix-logo-primary.png` | **Primary — charcoal/red** | The default. White and light backgrounds |
| `logo/parametrix-logo-charcoal.png` | Charcoal | Where the red does not work with the background colour |
| `logo/parametrix-logo-red.png` | Red | Where the name needs to stand out |
| `logo/parametrix-logo-knockout.png` | Reversed / knockout | Dark or busy backgrounds — **including dark-mode screen use** |
| `logo/spacer-arrow-red.png` | Spacer arrow | The brand divider *(p.19)* |
| `parametrix-x-mark.png` | ix formation, solid | Corner element, watermark *(p.15)* |
| `parametrix-wordmark.png` | Superseded | The earlier 605 px capture. Kept only so older builds resolve |

All are 2187 px wide — about 7 in at 300 dpi, well clear of the 1 in minimum.

> **These are raster extractions, not the master assets.** The real EPS, JPG and PNG assets are
> distributed through **Templafy** *(guide p.21)*. Fetch them before anything is printed or issued
> outside the project, and replace these files. Questions:
> **marketingtoolbox@parametrix.com** *(p.32)*.

## The rules that govern use

| Rule | Source |
|---|---|
| **Clear space** on all four sides ≥ the height of the right side of the letter **x** in the logo | p.13 |
| **Minimum size: 1 inch wide.** Never smaller | p.13 |
| Primary version on white and light grounds; **knockout on dark or busy grounds** | p.11 |
| In the primary version, **the red square is never changed to another colour** | p.11 |
| **Do not** change the logo's colour, add underlines, boxes or symbols, distort, rotate, warp, apply effects, use drop shadows, or place it on a background without enough contrast | p.14 |
| **The tagline is not used on a client-facing document** *(p.12 — "Do Not Use Tagline" column)* | p.12 |

## Colours

The guide's own values *(p.18)* govern. Note that the artwork extracted from the guide renders
red as `#EB2C29` in the PDF's colour space; **the specified hex is `#EE3D24` and that is what the
documents use.**

| | Name | Hex | RGB | Pantone |
|---|---|---|---|---|
| **Primary** | Parametrix Red | `#EE3D24` | 238, 61, 36 | Bright Red |
| | Charcoal | `#333333` | 51, 51, 51 | Black |
| | Medium Gray | `#676768` | 103, 103, 104 | 424 |
| | White | `#FFFFFF` | 255, 255, 255 | White |
| **Secondary** | Progress Orange | `#F36E21` | 243, 110, 33 | 1505 |
| | Optimistic Yellow | `#FCC214` | 252, 194, 20 | 123 |
| | Future Green | `#3FB549` | 63, 181, 73 | 361 |
| | Clean Blue | `#0073BB` | 0, 115, 187 | Medium Blue |
| **Tertiary** | Calm Red | `#ED715D` | 237, 113, 93 | 7416 |
| | Calm Orange | `#F89957` | 248, 153, 87 | 714 |
| | Calm Blue | `#B2D3DB` | 178, 211, 219 | 552 |
| | Calm Yellow | `#F4E39C` | 244, 227, 156 | 7499 |
| | Light Gray 1 | `#B3B4B5` | 179, 180, 181 | Cool Gray 6 |
| | Light Gray 2 | `#DBDDDC` | 219, 221, 220 | Cool Gray 4 |
| | Light Gray 3 | `#E5E5E5` | 229, 229, 229 | Cool Gray 2 |
| | Light Gray 4 | `#F2F2F2` | 242, 242, 242 | Cool Gray 1 |

Roles, in the guide's words: **Parametrix Red is the main colour associated with the brand.**
Secondary colours are **accent** — "useful for adding specific personality to brand materials and
to enhance categorization." Tertiary colours are used **sparingly**, for "mapping, charts, graphs,
and highlighting." Red text "should always be used sparingly" *(p.23)*.

## Typography

| Role | Face | System alternate named by the guide |
|---|---|---|
| Headlines | **Klinic Slab** | **Rockwell** |
| Body and subheadlines | **Franklin Gothic URW** | **Franklin Gothic** — ships with Microsoft Office |
| Quotes and accents | **Freight Text Pro** | **Georgia** |

*(guide p.16)*

The three licensed faces are not held by this project. The document builds therefore request the
licensed face first and fall back to the guide's own named alternate — no third typeface is
substituted.

## What the guide does not cover

Recorded in `deliverables/_control/style/brand-source-status.md`. In short: monospace type, table
styling, callout styling, iconography, screen and dark-mode behaviour, and a cover convention for
a technical report. Those are handled in the style specification and each one is marked as an
extension rather than a brand rule.
