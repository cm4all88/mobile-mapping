# Appendix B — The Reference Dataset

## B1 · What it is

`reference/mx60-reference-data.csv` holds **402 records** extracted from the source documents.
It is the **authority for numbers** in this manual: where a figure appears in the body, it was
taken from this file, and where the two disagree the CSV is correct and the body is a
transcription error to be fixed.

It exists because the same number appears in three or four places in a document set of this size,
sometimes in two different forms (per-scanner and system-total; centimetres and millimetres), and
because a number in prose has no source attached to it.

## B2 · Schema

| Column | Contents |
|---|---|
| `id` | Prefixed identifier — see B3. Stable; cite it |
| `category` | Broad grouping: Scanner, Positioning, TMI, Registration, Export, Safety … |
| `topic` | The narrower subject within the category |
| `item` | What the record is about, in words |
| `value` | The number, string, or statement |
| `notes` | Conditions, caveats, and any conflict with another record |
| `source` | The document, by short name |
| `page` | Page number where the source has one; `-` for web help topics |
| `sop_section` | Where it is used. Written against the single-document draft — see the note in B5 |

## B3 · What the identifier prefixes mean

| Prefix | Count | Meaning |
|---|---|---|
| `SPEC` | 56 | Manufacturer specification — an instrument or system performance figure |
| `TMI` | 50 | Trimble Mobile Imaging field software behaviour and settings |
| `QSG` | 42 | From the MX60 Quick Start Guide — mostly field procedure |
| `REG` | 34 | Registration behaviour and parameters |
| `EXP` | 28 | Export paths, options and outputs |
| `INST` | 27 | Installation — lever arms, mounting, offsets |
| `CAL` | 26 | Calibration procedure and geometry |
| `OPS` | 25 | Operating procedure and limits |
| `LIMIT` | 22 | A stated limit: environmental, electrical, operational |
| `TBC` | 22 | Trimble Business Center behaviour, versions and licensing |
| `TRAJ` | 16 | Trajectory processing settings and defaults |
| `SAFE` | 15 | Safety statement from a source document |
| `VEH` | 9 | Vehicle configuration |
| `SUPPORT` | 9 | Support routes and contacts |
| `QC` | 8 | Quality control indicators |
| `CONN` | 6 | External connectors |
| `CONFLICT` | 4 | **Two sources disagree.** See Appendix G |
| `CLEAN` | 2 | Cleanup behaviour |
| `RESOLVED` | 1 | A conflict that has since been resolved, kept for the record |

## B4 · Where the records come from

| Source | Records |
|---|---|
| MX60 User Guide Rev B | 153 |
| TMI User Guide Rev L | 50 |
| MX60 Quick Start Guide Rev B | 42 |
| TBC help topics (all) | ~120 across 30 topics |
| TBC release notes 2025.21 and 2026.10 | 14 |
| MX60 specification sheet | 5 |
| Dust filter bulletin | 7 |
| Roof rack user guide | 1 |

Full citations are in **Appendix A**.

## B5 · How to use it

**To check a number in this manual.** Search the CSV for the value or the topic. The `source` and
`page` columns give the citation; the `notes` column usually explains any condition attached to
it.

**To answer a question this manual does not address.** The CSV contains records that no section
needed — connector pinouts, cable lengths, screw torques, support addresses. Search it before
assuming the answer is not in the source set.

**Before quoting a number to a client.** Check whether it carries a `CONFLICT` note. Four figures
in the set are contradicted by another source (Appendix G), and two more are quoted in two
different forms by Trimble itself — the scanner pulse rate and scan speed, which the specification
sheet gives as system totals and the User Guide gives per scanner (§16.1).

> **IMPORTANT · the `sop_section` column is stale**
>
> That column was written against the single 71,800-word draft that preceded the four-deliverable
> structure. Its numbers do **not** correspond to this manual's sections. It is retained because it
> records which topic each number was used for, which is still useful, but it should not be used as
> a cross-reference until it is regenerated.
>
> Regenerating it against the four-deliverable structure is straightforward and is on the
> project's own task list. It does not affect any value in the file.
