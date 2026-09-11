#!/usr/bin/env python3
"""Flag forbidden stage-name synonyms across the four documents.

Two things are not flagged, per workflow-stage-names.md: text inside a quotation,
and the words that are only forbidden *as a stage name* (mobilisation, audit trail,
lineage), which are ordinary English elsewhere.

    python3 tools/check-stage-names.py
"""
import re, glob, os, sys

# forbidden everywhere -> the frozen name
STRICT = {
 'job setup':'Project setup', 'project creation':'Project setup',
 'route planning':'Mission planning', 'job planning':'Mission planning',
 'nav processing':'Trajectory processing', 'SBET processing':'Trajectory processing',
 'point cloud generation':'Scan generation', 'scan extraction':'Scan generation',
 'boresighting':'Calibration',
 'control fitting':'Registration',
 'scan update':'Update Scans', 're-extraction':'Update Scans',
 'GNSS remediation':'Degraded-GNSS handling', 'gap filling':'Degraded-GNSS handling',
 'project cleanup':'Cleanup', 'tidying':'Cleanup',
 'delivery generation':'Export',
 'sign-off review':'Final QA/QC',
}
DOCS = {'Manual':'deliverables/technical-manual/*.md', 'SOP':'deliverables/sop/*.md',
        'Office':'deliverables/office-how-to/*.md', 'Field':'deliverables/field-how-to/*.md'}

bad = 0
for doc, pat in DOCS.items():
    for f in sorted(glob.glob(pat)):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md': continue
        for i, l in enumerate(open(f), 1):
            if '"' in l or '“' in l: continue      # quoted source text is reproduced as written
            for w, good in STRICT.items():
                if re.search(r'\b' + re.escape(w) + r'\b', l, re.I):
                    print(f'  {doc:7} {b[:36]:38}{i:5}  "{w}" -> {good}')
                    print(f'          {l.strip()[:100]}')
                    bad += 1
print(f'{bad} forbidden stage-name synonyms' if bad else 'no forbidden stage-name synonyms')
sys.exit(1 if bad else 0)
