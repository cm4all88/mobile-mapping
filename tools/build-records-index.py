#!/usr/bin/env python3
"""Generate SOP Appendix B — the index of every record the SOP requires.

A VIEW, built from the "Records this section requires" table at the end of each
SOP section. Edit the section; regenerate this. Never edit Appendix B by hand.

    python3 tools/build-records-index.py
"""
import re, glob, os, datetime

SOP = 'deliverables/sop'
OUT = os.path.join(SOP, 'appendix-B-records-index.md')

rows = []
for f in sorted(glob.glob(os.path.join(SOP, '[0-2][0-9]-*.md'))):
    md = open(f).read()
    m = re.match(r'^# (\d+)\. (.*)', md)
    if not m: continue
    num, title = m.group(1), m.group(2)
    # the last table under a "Records this section requires" heading
    sec = re.search(r'^## \d+\.\d+ Records this section requires\s*\n(.*?)(?=\n## |\Z)',
                    md, re.S | re.M)
    if not sec: continue
    body = sec.group(1)
    body = re.sub(r'^>\s?', '', body, flags=re.M)   # tables inside a PROPOSED block
    lines = [l.strip() for l in body.split('\n') if l.strip().startswith('|')]
    if len(lines) < 3: continue
    hdr = [c.strip() for c in lines[0].strip('|').split('|')]
    for l in lines[2:]:
        cells = [c.strip() for c in l.strip('|').split('|')]
        rec   = cells[0]
        where = cells[1] if len(cells) > 2 else ''
        state = cells[-1]
        rows.append((num, title, rec, where, state))

def sortkey(r): return (int(r[0]),)
rows.sort(key=sortkey)

open_ids = set()
for r in rows:
    open_ids |= set(re.findall(r'\bD-\d+\b', r[4]))

head = f"""# Appendix B — Index of Required Records

**Generated view — do not edit by hand.** Produced by `tools/build-records-index.py` from the
*Records this section requires* table at the end of each section. Edit the section; regenerate this.

**{len(rows)} records**, across {len(set(r[0] for r in rows))} sections.
Last generated {datetime.date.today().isoformat()}.

> **Read the State column.** A record whose state names a **D-** identifier is required by a clause
> that has not been adopted. It is proposed, not mandatory, and the identifier is where the decision
> is tracked (Appendix A).

> **Five of these records have no software artefact behind them** — the control and check
> designation, the visual inspection, the imagery inspection, the field conditions, and the
> disposition of a non-conformance. They are written by a person or they do not exist (§19.1).

---

## B1 · By section

| § | Section | Record | State |
|---|---|---|---|
"""
body = []
last = None
for num, title, rec, where, state in rows:
    label = f'**{num}** {title}' if num != last else ''
    last = num
    body.append(f'| {label and num} | {label and title} | {rec} | {state} |')

tail = f"""

## B2 · Where the state stands

| | |
|---|---|
| Records required by an **adopted** clause | **0** |
| Records required by a clause awaiting a decision | **{len(rows)}** |
| Distinct decisions they depend on | **{len(open_ids)}** — {', '.join(sorted(open_ids, key=lambda x: int(x.split('-')[1])))} |

**Every record in this index is currently proposed.** That follows from no clause having been
adopted, not from any doubt about whether the records are worth keeping.

## B3 · The records with no software artefact

These are the ones that get lost, because nothing in the software produces them and nothing
complains when they are absent.

| Record | Section | Why nothing produces it |
|---|---|---|
| **Which points were control and which were independent checks** | §7.3, §15.4 | TBC shows the state while the command is open and reloads it on Edit, but no report of it has been found *(Technical Manual §22.7)* |
| **That the visual inspection was performed, and over what extent** | §15.5 | It is a human act in a viewer |
| **That the imagery inspection was performed** | §15.6 | The same |
| **Conditions at collection** — occlusion, weather, traffic, what was not collected and why | §9.6 | Nothing in the vehicle records them |
| **Disposition of a non-conformance** | §21.7 | — |

## B4 · The smallest package that would satisfy the record

§19.2 proposes seven artefacts totalling a few hundred kilobytes. **Five of the seven already exist
as files** and need only to be copied out of the project before it is cleaned up (§17.3). Two are
written by a person.
"""
open(OUT, 'w').write(head + '\n'.join(body) + tail)
print(f'{OUT}: {len(rows)} records from {len(set(r[0] for r in rows))} sections')
