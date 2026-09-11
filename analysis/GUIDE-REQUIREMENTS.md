# Parametrix MX60 Mobile Mapping Field, Processing and QC Guide
## Permanent requirements governing the final build

**Established:** 2026-09-11
**Status:** Requirements only. **No rewrite performed.**

These are standing requirements, not suggestions. They apply to every section of the final
guide and survive any restructure.

---

## 0. Document identity

**Title:** Parametrix MX60 Mobile Mapping **Field, Processing and QC Guide**

This supersedes the working title "Standard Operating Procedure." The scope is broader than
an SOP: it is a training, operating and quality-control manual covering field collection,
office processing, and QC.

Existing drafted material remains valid; the title, framing and structure will be revised
at the rewrite.

---

## 1. PARAMETRIX BRANDING

### Requirement

The finished product **must look like a professional Parametrix internal training,
operating and QC manual — not a Trimble help document.**

### Sequencing

| When | What |
|---|---|
| On receipt | **Ingest and inventory** branding assets — logos, templates, examples, brand standards |
| While content is in progress | **Do not fully style.** Structure and technical content come first |
| Once content is substantially complete | Apply the full visual treatment |

> Styling early would mean restyling repeatedly as the structure changes. The inventory is
> cheap and can happen at any time; the application should happen once.

### What "belongs to Parametrix" means

- Parametrix typography, palette, page furniture, cover and running heads
- Parametrix voice throughout the prose
- The reader's impression on opening should be "this is our manual"

### What is preserved as source material

**Trimble screenshots and citations stay.** They are the technical evidence base and are not
to be redrawn, paraphrased away, or stripped of attribution.

The distinction to hold:

| Element | Treatment |
|---|---|
| Trimble **screenshots** | Preserved — cropped per the figure lists, captioned in Parametrix style, clearly attributed |
| Trimble **page citations** | Preserved — every specification traceable to source and page |
| Trimble **page layout, typography, colour, iconography** | **Not** carried over |
| Trimble **wording** | Re-expressed in Parametrix voice, except where a direct quotation is doing real work |

### Current asset state

`brand/` holds two raster PNGs — wordmark and X mark — with sampled colours `#343433`
charcoal and `#EB2A2B` red. **Vector versions and a reversed variant are still needed**, plus
whatever template, example and brand-standard material exists.

> Asset inventory will be appended here when the assets arrive.

---

## 2. COMPREHENSION LAYER

### The principle

Technical completeness is not enough. **The reader must actually understand what is
happening.**

### The three levels

Every substantial topic operates at three levels, and all three must be present:

| Level | Answers | Voice |
|---|---|---|
| **1. Procedure** | Exactly what the user does | Imperative, numbered, unambiguous |
| **2. Technical explanation** | What the MX60 or TBC is actually doing, and why | Precise, cited, complete |
| **3. Plain language comprehension** | What the reader needs to understand and remember | Ordinary language, as if speaking to a colleague |

**The detailed technical content remains authoritative.** The plain-language layer
reinforces comprehension; it does not replace or outrank the technical material.

### Requirement A — every substantial technical section ends with:

> **IN PLAIN ENGLISH**

Addressed to **an experienced land surveyor who is new to mobile mapping.** It must answer:

1. **What just happened?**
2. **Why does it matter?**
3. **What could go wrong?**
4. **What does "good" look like, in practical terms?** — and what to remember before moving on

> **Amended 2026-09-11 (batch 5).** Questions 3 and 4 replace the original single closing
> question. The addition is deliberate: several of the most important facts in the source set
> are **failure modes**, not procedures — a target picked on a superseded scan, Local
> registration silently not extrapolating past the outermost control point, `Targets.csv`
> emptied by the wrong answer to a dialog, Cleanup run without a backup. A box that only
> summarises the procedure leaves all of those out.
>
> "What good looks like" is likewise not decoration. Trimble's own position is that good RMS
> cannot prove success — so the reader needs a practical picture of a sound result, not a
> number to clear.

**Rules:**

- **Re-explain, do not shorten.** A compressed restatement of the preceding paragraphs
  fails this requirement. Come at the idea from a different direction
- **Ordinary language.** Minimal software jargon. Where a term must be used, it has already
  been defined
- **Analogies where they genuinely help** — and not where they don't. A forced analogy is
  worse than a plain sentence
- **Assume real competence.** The reader knows survey. They do not know this system. Never
  explain what a residual is; do explain what TBC means by a Registration Trajectory
- **Short.** A box, not a section

### Requirement B — every major chapter ends with:

> **WHAT YOU SHOULD KNOW BEFORE MOVING ON**

A concise set of the most important **concepts, decisions, hazards and checks** the reader
should retain from that chapter.

**Rules:**

- Retention, not summary. Include what would cost money or data if forgotten
- Hazards belong here — the silent failures especially
- Decisions the reader must make belong here
- Keep it scannable — a short list, not prose

---

## 3. Worked examples — the pattern to follow

These fix the voice. They are drawn from already-drafted material and are illustrative, not
final text.

### Example A — IN PLAIN ENGLISH, after §8.4 (initialization theory)

*The preceding section explains GNSS/INS filter convergence, observability, and why heading
is the hardest attitude component.*

> **IN PLAIN ENGLISH**
>
> **What just happened?** You sat still for a few minutes, drove straight, then deliberately
> sped up, slowed down and turned. The system used all of that to work out three things it
> cannot see directly: how its inertial sensors are drifting, and exactly how the vehicle is
> tilted and pointed.
>
> Sitting still is the useful part people skip. When the vehicle is parked, the system knows
> its true speed is zero — so anything its motion sensors report is pure error, and it can
> measure and remove it. The manoeuvres do the same job for orientation: while you drive at
> a steady speed in a straight line, a small tilt error and a sensor bias look identical to
> the software. Change speed and direction and they stop looking identical, so it can tell
> them apart.
>
> **Why does it matter?** Everything the MX60 collects is positioned off that solution. It is
> like resection — the instrument has to know where it is and which way it is facing before
> any shot means anything. The difference is that here the answer degrades over time and
> distance, so you re-establish it at both ends of the job.
>
> **What do I need to remember?** Green means the solution met your accuracy figures — not
> that it is finished converging. That is why Trimble asks for up to ten more minutes before
> you record anything that matters. The first data after the light turns green is the
> weakest data of the day, so do not spend it on the most important part of the corridor.

### Example B — WHAT YOU SHOULD KNOW BEFORE MOVING ON, after the Initialization chapter

> **WHAT YOU SHOULD KNOW BEFORE MOVING ON**
>
> - **The trajectory is the whole job.** Every point inherits its error. A perfect scanner on
>   a poor trajectory gives a poor point cloud, and nothing in the office fixes it.
> - **Initialization is not a formality.** Static period, straight run, speed changes, turns —
>   each one is solving something specific.
> - **Green is a threshold, not a finish line.** Allow the settling time.
> - **Orange lets you record. It should not.** TMI permits it; survey-grade work does not.
> - **Navigation logging has already started** before you press Record — and stops the instant
>   you close the mission.
> - **Do the end sequence.** It is a mirror of the start, it takes five minutes, and it is the
>   only thing giving the reverse-processing pass an anchor. You cannot add it later.
> - **If NAV will not go green**, ask which parameter is holding it. Heading means more
>   manoeuvres; position means move to a better location.

---

## 4. Structural implications

Recorded now so the rewrite does not rediscover them.

### Scale

| Item | Estimate |
|---|---|
| Sections needing **IN PLAIN ENGLISH** | ~40–55 boxes across the guide |
| Chapters needing **WHAT YOU SHOULD KNOW** | One per major chapter — currently 14, plus appendices as appropriate |
| Added length | Roughly 15–20% |

### Which sections qualify as "substantial technical"

Needs a box: anything explaining a mechanism, a trade-off, a quality indicator, or a failure
mode. Trajectory, attitude error and range, initialization theory, GNSS outage behaviour,
filtering, colorization and masking, Generate vs Update Scans, registration, calibration,
useful range, control versus check points, point cloud quality factors.

Does not need one: pure reference tables, contact details, checklists, the glossary.

### Tooling

The callout system must gain two types. Both build scripts need them before the rewrite:

| File | Change |
|---|---|
| `tools/build-sop-page.py` | Add to the `CALLOUTS` list |
| `tools/sop-page-template.html` | Add `.co-plain` and `.co-retain` styles |
| `tools/build-sop.js` | Add to the `CALLOUTS` map |

These two callouts should be **visually distinct from the existing six** — they are a
different kind of content, addressed to a different need. They should read as a pause in the
technical flow, not another warning.

### Interaction with existing callouts

The guide already uses **WHY THIS MATTERS**. That stays — it is a short inline explanation of
a single procedure. **IN PLAIN ENGLISH** is different: it lands at the end of a section and
re-explains the whole of it.

> Watch for redundancy at the rewrite. Where a section's WHY THIS MATTERS already carries the
> comprehension load, the closing box should go somewhere else conceptually rather than
> repeat it.

---

## 5. Acceptance criteria

The guide meets these requirements when:

- [ ] Titled *Parametrix MX60 Mobile Mapping Field, Processing and QC Guide*
- [ ] Visually reads as a Parametrix manual — cover, typography, palette, running heads
- [ ] Trimble screenshots preserved, cropped, captioned in Parametrix style, attributed
- [ ] Every specification still traceable to its Trimble source and page
- [ ] Every substantial technical section ends with **IN PLAIN ENGLISH** answering all four questions — including **what could go wrong** and **what "good" looks like**
- [ ] Every major chapter ends with **WHAT YOU SHOULD KNOW BEFORE MOVING ON**
- [ ] Plain-language boxes **re-explain** rather than compress
- [ ] All three levels present: procedure, technical explanation, comprehension
- [ ] Technical content remains authoritative; comprehension layer is additive
- [ ] Parametrix decisions still marked as open, never presented as adopted policy

---

*Source ingestion continues. No rewrite has been performed. These requirements govern the
rewrite when the technical content and structure are substantially complete.*
