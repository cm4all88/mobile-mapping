#!/usr/bin/env python3
"""Build a browsable page for one of the four MX60 documents.

    python3 tools/build-doc-page.py manual|sop|field|office

All four share one template and one token file. The only things that differ are the
section list, the document-type label, the hero, and --pmx-id-pos: the position of the
red quarter in the document identity rule (0 = Manual, 1 = SOP, 2 = Field, 3 = Office).
See deliverables/_control/style/style-system.md.
"""
import re, sys, pathlib, html, json, base64


REPO = pathlib.Path('/home/user/mobile-mapping')

# --- the four documents --------------------------------------------------
# id_pos is the quarter of the identity rule that is red. It is the one visual
# value that differs between the four, and it uses no colour that is not in the
# supplied Parametrix marks.
MANUAL_ORDER = [
 ('00-front-matter','0','Front Matter'),
 ('01-purpose-and-scope','1','Purpose and Scope'),
 ('02-mobile-mapping-in-plain-terms','2','Mobile Mapping in Plain Terms'),
 ('03-how-error-behaves','3','How Error Behaves'),
 ('04-the-workflow-end-to-end','4','The Workflow, End to End'),
 ('05-the-data-chain','5','The Data Chain'),
 ('06-terminology','6','Terminology'),
 ('07-mx60-system-architecture','7','MX60 System Architecture'),
 ('08-gnss-ins-integration','8','GNSS/INS Integration'),
 ('09-gams-and-dmi','9','GAMS and DMI'),
 ('10-tmi-tbc-pospac','10','TMI, TBC and POSPac'),
 ('11-lidar-qc','11','LiDAR QC'),
 ('12-coordinate-systems','12','Coordinate Systems, Datums and Epochs'),
 ('13-initialization','13','Initialization'),
 ('14-the-closing-sequence','14','The Closing Sequence'),
 ('15-gnss-environment-and-outage-duration','15','GNSS Environment and Outage Duration'),
 ('16-point-density-and-useful-range','16','Point Density and Useful Range'),
 ('17-trajectory-processing','17','Trajectory Processing'),
 ('18-scan-generation','18','Scan Generation'),
 ('19-update-scans','19','Update Scans'),
 ('20-calibration','20','Calibration'),
 ('21-registration','21','Registration'),
 ('22-gcps-check-points-and-residuals','22','GCPs, Check Points and Residuals'),
 ('23-rms-and-what-it-can-prove','23','RMS and What It Can Prove'),
 ('24-trajectory-rms-colouring','24','Trajectory RMS Colouring'),
 ('25-visual-qc','25','Visual QC'),
 ('26-imagery','26','Imagery'),
 ('27-degraded-gnss','27','Degraded GNSS'),
 ('28-cleanup','28','Cleanup Mobile Mapping Mission'),
 ('29-export','29','Export'),
 ('30-provenance','30','Provenance'),
 ('31-periodic-system-verification','31','Periodic System Verification'),
 ('appendix-A-trimble-source-index','A','Trimble Source Index'),
 ('appendix-B-reference-dataset','B','The Reference Dataset'),
 ('appendix-C-figures','C','Figures and Screenshots'),
 ('appendix-D-observed-software-behaviour','D','Observed Software Behaviour'),
 ('appendix-E-open-technical-questions','E','Open Technical Questions'),
 ('appendix-F-test-results','F','Test Results'),
 ('appendix-G-source-conflicts','G','Source Conflicts and Resolutions'),
]

SOP_ORDER = [
 ('00-front-matter','0','Front Matter'),
 ('01-purpose-and-scope','1','Purpose, Scope and Application'),
 ('02-document-control','2','Document Control and Related Documents'),
 ('03-definitions','3','Definitions'),
 ('04-roles-and-authorities','4','Roles, Responsibilities and Authorities'),
 ('05-competence-and-training','5','Competence and Training'),
 ('06-project-setup','6','Project Setup Requirements'),
 ('07-control-requirements','7','Control Requirements'),
 ('08-mission-planning','8','Mission Planning Requirements'),
 ('09-field-acquisition','9','Field Acquisition Requirements'),
 ('10-field-close-out','10','Field Close-out and Handoff'),
 ('11-data-transfer-and-custody','11','Data Transfer and Custody'),
 ('12-office-intake','12','Office Intake Requirements'),
 ('13-processing-requirements','13','Processing Requirements'),
 ('14-calibration-control','14','Calibration Control'),
 ('15-qc-requirements','15','Quality Control Requirements'),
 ('16-acceptance-and-approval','16','Acceptance and Approval'),
 ('17-destructive-operations','17','Destructive Operation Controls'),
 ('18-export-and-delivery','18','Export and Delivery Controls'),
 ('19-documentation-and-records','19','Documentation and Records'),
 ('20-retention-and-archive','20','Retention and Archive'),
 ('21-non-conformance','21','Non-conformance and Re-collection'),
 ('appendix-A-decision-register','A','Parametrix Decision Register'),
 ('appendix-B-records-index','B','Index of Required Records'),
 ('appendix-C-approval-and-revision-history','C','Approval and Revision History'),
]

OFFICE_ORDER = [
 ('00-front-matter','0','Front Matter'),
 ('01-how-to-use-this-guide','1','How to Use This Guide'),
 ('02-data-intake','2','Data Intake'),
 ('03-checking-mission-information','3','Checking Mission Information'),
 ('04-calibration-state-intake','4','Calibration-State Intake'),
 ('05-project-setup','5','Project Setup'),
 ('06-coordinate-systems','6','Coordinate Systems'),
 ('07-importing-the-mission','7','Importing the Mission'),
 ('08-trajectory-processing','8','Trajectory Processing'),
 ('09-pospac-requirements','9','POSPac Requirements'),
 ('10-reading-the-trajectory','10','Reading the Trajectory'),
 ('11-generate-scans','11','Generate Scans'),
 ('12-checking-the-scans','12','Checking the Scans'),
 ('13-calibration','13','Calibration'),
 ('14-importing-control','14','Importing Control'),
 ('15-gcp-and-check-point-configuration','15','GCP and Check Point Configuration'),
 ('16-register-a-run','16','Register a Run'),
 ('17-register-a-mission','17','Register a Mission'),
 ('18-register-run-to-run','18','Register Run to Run'),
 ('19-editing-a-registration','19','Editing a Registration'),
 ('20-residual-review','20','Residual Review'),
 ('21-update-scans','21','Update Scans'),
 ('22-visual-qc','22','Visual QC'),
 ('23-imagery-qc','23','Imagery QC'),
 ('24-lidar-qc','24','LiDAR QC'),
 ('25-degraded-gnss','25','Degraded GNSS'),
 ('26-pfix','26','PFIX'),
 ('27-identifying-registration-results','27','Identifying Registration Results'),
 ('28-trajectory-provenance','28','Trajectory Provenance'),
 ('29-cleanup','29','Cleanup Mobile Mapping Mission'),
 ('30-export','30','Export'),
 ('31-the-pre-export-check','31','The Pre-export Check'),
 ('32-final-qa-qc','32','Final QA/QC'),
 ('33-archiving','33','Archiving'),
 ('34-documentation-required','34','Documentation Required'),
 ('35-common-problems','35','Common Problems'),
 ('appendix-A-office-processing-checklist','A','Office Processing Checklist'),
 ('appendix-B-registration-checklist','B','Registration Checklist'),
 ('appendix-C-qc-checklist','C','QC Checklist'),
 ('appendix-D-export-and-delivery-checklist','D','Export and Delivery Checklist'),
 ('appendix-E-archive-and-cleanup-checklist','E','Archive and Cleanup Checklist'),
 ('appendix-F-record-templates','F','Record Templates'),
]

DOCS = {
 'manual': dict(
    dir='deliverables/technical-manual', out='technical-manual.html', accent='var(--brand-blue)', accent_on='var(--brand-white)',
    doctype='Technical Manual', docname='MX60 Mobile Mapping',
    title='MX60 Mobile Mapping Technical Manual',
    sub='Draft A · Evidence revision E1 · TBC 2026.10',
    order=MANUAL_ORDER,
    lead=('Why the system behaves the way it does, and how we know. '
          'The evidence base for the SOP and the two How To guides.'),
    stats=[('Sections','31 + 7 appendices'),('Words','57,000'),
           ('In Plain English','29 boxes'),('Open technical questions','41')],
    flag=('<b>This manual states no Parametrix procedure.</b> It explains what Trimble\'s software '
          'does and what has been observed; it decides nothing. Requirements live in the SOP. '
          'Where a Parametrix decision would resolve a question, the manual names the decision and '
          'moves on. Nothing here may be quoted to a client as an existing Parametrix standard.'),
 ),
 'sop': dict(
    dir='deliverables/sop', out='sop.html', accent='var(--brand-orange)', accent_on='var(--brand-charcoal)',
    doctype='Standard Operating Procedure', docname='MX60 Mobile Mapping',
    title='MX60 Mobile Mapping SOP',
    sub='Draft A · Not issued · TBC 2026.10',
    order=SOP_ORDER,
    lead=('What Parametrix requires of MX60 mobile mapping work. Short by design: it states '
          'requirements and points to the Technical Manual for explanation and to the How To '
          'guides for method.'),
    stats=[('Sections','21 + 3 appendices'),('Words','18,800'),
           ('Clauses adopted','0 of 34'),('Blocking decisions','9')],
    flag=('<b>No clause in this SOP has been adopted.</b> Every requirement is marked '
          '<b>PROPOSED</b> until Parametrix records a decision against it, with a date and an '
          'owner, in Appendix A. Nothing here may be quoted to a client as an existing '
          'Parametrix standard.'),
 ),
 'field': dict(
    dir='deliverables/field-how-to', out='field-how-to.html', accent='var(--brand-green)', accent_on='var(--brand-charcoal)',
    doctype='Field How To', docname='MX60 Mobile Mapping',
    title='MX60 Field How To', sub='Draft A · Not issued',
    order=None, lead='How to run the MX60 in the field.', stats=[], flag='',
 ),
 'office': dict(
    dir='deliverables/office-how-to', out='office-how-to.html', accent='var(--brand-yellow)', accent_on='var(--brand-charcoal)',
    doctype='Office How To', docname='MX60 Mobile Mapping',
    title='MX60 Office How To', sub='Draft A · Not issued · TBC 2026.10',
    order=OFFICE_ORDER,
    lead=('How to process MX60 data in Trimble Business Center, in the order you do it. '
          'Every section answers four questions: what to do, what to look at, what to expect, '
          'and what should make you stop.'),
    stats=[('Sections','35 + 6 appendices'),('Words','15,800'),
           ('Checklists','5'),('Record templates','5')],
    flag=('<b>Read &ldquo;Stop if&rdquo; in every section.</b> Three mistakes cost more than all '
          'the others and all three are silent: registration does not change the point cloud until '
          '<b>Update Scans</b> runs; a good RMS does not prove the work succeeded; and '
          '<b>Cleanup cannot be undone</b>. This guide cannot create a requirement &mdash; where it '
          'differs from the SOP, the SOP governs.'),
 ),
}

KEY = sys.argv[1] if len(sys.argv) > 1 else 'manual'
CFG = DOCS[KEY]
SOP = REPO / CFG['dir']
OUT = SOP / CFG['out']
ORDER = CFG['order'] or [
    (p.stem, p.stem.split('-')[0].lstrip('0') or '0', p.stem)
    for p in sorted(SOP.glob('*.md'))]


CALLOUTS = [
    ('WHAT YOU SHOULD KNOW BEFORE MOVING ON', 'retain'),
    ('IN PLAIN ENGLISH', 'plain'),
    # evidence tags -- longest first, so PARAMETRIX PROCEDURE (ADOPTED) is not
    # matched by a shorter PARAMETRIX PROCEDURE prefix
    ('PARAMETRIX PROCEDURE (PROPOSED)', 'proposed'),
    ('PARAMETRIX PROCEDURE (ADOPTED)', 'adopted'),
    ('PARAMETRIX DECISION REQUIRED', 'decision'),
    ('TRIMBLE DOCUMENTED PROCEDURE', 'trimble'),
    ('OBSERVED SOFTWARE BEHAVIOR', 'observed'),
    ('VENDOR CLARIFICATION REQUIRED', 'vendor'),
    ('FIELD TESTING REQUIRED', 'testing'),
    ('TESTING REQUIRED', 'testing'),
    ('WHY THIS MATTERS', 'why'),
    ('FIELD TIP', 'tip'),
    ('IMPORTANT', 'important'),
    ('CAUTION', 'caution'),
    ('ADVANCED', 'advanced'),
]

def inline(t):
    t = html.escape(t, quote=False)
    # protect code spans: an identifier such as sbet_*_reg_####.out contains
    # asterisks that must not be read as emphasis
    code = []
    def stash(m):
        code.append(m.group(1)); return f'\x00{len(code)-1}\x00'
    t = re.sub(r'`([^`]+)`', stash, t)
    # non-greedy, so bold may contain italics or a stashed code span
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\*\w])\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'\x00(\d+)\x00', lambda m: f'<code>{code[int(m.group(1))]}</code>', t)
    # (MX60 UG Rev B, p.54) -> citation
    t = re.sub(r'\(((?:MX60|Trimble|TMI|QSG|TMR|NCHRP|Rack|Dust|TBC|Queensland)[^()]*?(?:p\.|pp\.|§)[^()]*?)\)',
               r'<span class="cite">\1</span>', t)
    return t

def split_row(l):
    return [c.strip() for c in l.strip().strip('|').split('|')]

def render(md, sec_id):
    out, i, lines = [], 0, md.split('\n')
    while i < len(lines):
        raw = lines[i]; t = raw.strip()
        if not t or t == '---':
            i += 1; continue

        m = re.match(r'^(#{1,4})\s+(.*)$', t)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            if lvl == 1: i += 1; continue           # section title handled by the shell
            hid = re.sub(r'[^a-z0-9]+', '-', txt.lower()).strip('-')[:60]
            tag = 'h3' if lvl == 2 else 'h4'
            out.append(f'<{tag} id="{sec_id}-{hid}">{inline(txt)}</{tag}>')
            i += 1; continue

        if t.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
            blk = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                blk.append(lines[i].strip()); i += 1
            hdr = split_row(blk[0]); rows = [split_row(r) for r in blk[2:]]
            th = ''.join(f'<th>{inline(c)}</th>' for c in hdr)
            tb = ''.join('<tr>' + ''.join(
                f'<td>{inline(r[k]) if k < len(r) else ""}</td>' for k in range(len(hdr))) + '</tr>'
                for r in rows)
            out.append(f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            continue

        if t.startswith('>'):
            blk = []
            while i < len(lines) and (lines[i].strip().startswith('>') or
                   (not lines[i].strip() and i+1 < len(lines) and lines[i+1].strip().startswith('>'))):
                blk.append(re.sub(r'^>\s?', '', lines[i].strip())); i += 1
            kind, label = 'note', None
            first = re.sub(r'\*', '', blk[0]).strip().upper() if blk else ''
            for name, cls in CALLOUTS:
                if first.startswith(name): kind, label = cls, name; break
            body, buf, head = [], [], ''
            if label:
                rest = re.sub(r'\*', '', blk[0]).strip()[len(label):].lstrip(' —–-')
                head = f'<p class="co-h">{html.escape(label)}{(" — " + inline(rest)) if rest else ""}</p>'
                blk = blk[1:]
            def flush():
                if buf:
                    s = ' '.join(buf).strip()
                    if s: body.append(f'<p>{inline(s)}</p>')
                    buf.clear()
            # list items may wrap over several lines; gather the raw text of an
            # item before rendering it, so emphasis spanning a line break pairs up
            item, item_cls = [], None
            def flush_item():
                if item:
                    body.append(f'<p class="{item_cls}">{inline(" ".join(item))}</p>')
                    item.clear()
            for ln in blk:
                st = ln.strip()
                if not st: flush_item(); flush(); continue
                if re.match(r'^[-*]\s+', st):
                    flush(); flush_item()
                    item_cls = 'co-li'; item.append(re.sub(r'^[-*]\s+', '', st))
                elif re.match(r'^\d+\.\s+', st):
                    # numbered item: keep the number, suppress the bullet marker
                    flush(); flush_item()
                    item_cls = 'co-li co-num'; item.append(st)
                elif item and re.match(r'^\s{2,}\S', ln):
                    item.append(st)                      # a continuation of the item
                elif st.startswith('|'):
                    flush_item(); flush(); body.append(f'<p>{inline(st.strip("|"))}</p>')
                else:
                    flush_item(); buf.append(st)
            flush_item(); flush()
            out.append(f'<aside class="co co-{kind}">{head}{"".join(body)}</aside>')
            continue

        if t.startswith('```'):
            i += 1; code = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(html.escape(lines[i])); i += 1
            i += 1
            out.append('<pre><code>' + '\n'.join(code) + '</code></pre>')
            continue

        if re.match(r'^\d+\.\s+', t):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+\.\s+', lines[i]):
                raw = re.sub(r'^\s*\d+\.\s+', '', lines[i]); i += 1
                while i < len(lines) and re.match(r'^\s{3,}\S', lines[i]) and not re.match(r'^\s*\d+\.', lines[i]):
                    raw += ' ' + lines[i].strip(); i += 1
                items.append(inline(raw))
            out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>')
            continue

        if re.match(r'^[-*]\s+', t):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*]\s+', lines[i]):
                raw = re.sub(r'^\s*[-*]\s+', '', lines[i]); i += 1
                while i < len(lines) and re.match(r'^\s{3,}\S', lines[i]) and not re.match(r'^\s*[-*]', lines[i]):
                    raw += ' ' + lines[i].strip(); i += 1
                items.append(inline(raw))
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')
            continue

        para = [t]; i += 1
        while i < len(lines):
            n = lines[i].strip()
            if (not n or n.startswith(('#', '|', '>', '```', '---')) or
                re.match(r'^[-*]\s+', n) or re.match(r'^\d+\.\s+', n)): break
            para.append(n); i += 1
        out.append(f'<p>{inline(" ".join(para))}</p>')
    return '\n'.join(out)


LEGEND_ROWS = {
 'caution':   ('Caution', 'Data loss, an irreversible operation, a lost result, or safety'),
 'important': ('Important', 'Gets the job wrong if ignored'),
 'why':       ('Why this matters', 'The reason behind a behaviour or a requirement'),
 'plain':     ('In Plain English', 'What we did, why it matters, what can go wrong, what good looks like'),
 'trimble':   ('Trimble documented procedure', 'Trimble states this, in the cited topic or page'),
 'observed':  ('Observed software behavior', 'Seen in the software; not stated by Trimble as procedure'),
 'proposed':  ('Parametrix procedure (proposed)', 'Recommended &mdash; <b style="color:inherit">not company policy</b>'),
 'adopted':   ('Parametrix procedure (adopted)', 'Decided by Parametrix, with a date and an owner'),
 'decision':  ('Parametrix decision required', 'An internal standard still to be established'),
 'testing':   ('Testing / vendor clarification required', 'The answer depends on a result nobody has obtained yet'),
}
MARKERS = {
 'caution':'CAUTION','important':'IMPORTANT','why':'WHY THIS MATTERS','plain':'IN PLAIN ENGLISH',
 'trimble':'TRIMBLE DOCUMENTED PROCEDURE','observed':'OBSERVED SOFTWARE BEHAVIOR',
 'proposed':'PARAMETRIX PROCEDURE (PROPOSED)','adopted':'PARAMETRIX PROCEDURE (ADOPTED)',
 'decision':'PARAMETRIX DECISION REQUIRED','testing':'TESTING REQUIRED',
}

_OLD_LEGEND = """    <div class="legend">
      <div class="lg-caution"><b>Caution</b>Data loss, an irreversible operation, a lost result, or safety</div>
      <div class="lg-important"><b>Important</b>Gets the job wrong if ignored</div>
      <div class="lg-why"><b>Why this matters</b>The reason behind a behaviour or a requirement</div>
      <div class="lg-plain"><b>In Plain English</b>What we did, why it matters, what can go wrong, what good looks like</div>
      <div class="lg-trimble"><b>Trimble documented procedure</b>Trimble states this, in the cited topic or page</div>
      <div class="lg-observed"><b>Observed software behavior</b>Seen in the software; not stated by Trimble as procedure</div>
      <div class="lg-proposed"><b>Parametrix procedure (proposed)</b>Recommended &mdash; <b style="color:inherit">not company policy</b></div>
      <div class="lg-decision"><b>Parametrix decision required</b>An internal standard still to be established</div>
      <div class="lg-testing"><b>Field testing / vendor clarification required</b>Answerable by test, or only by Trimble</div>
    </div>
"""
# ---- assemble ----
sections, nav, search = [], [], []
for fn, num, title in ORDER:
    md = (SOP / f'{fn}.md').read_text()
    sid = 's' + num.lower()
    body = render(md, sid)
    kind = 'nv-app' if num.isalpha() else 'nv-sec'
    sections.append(
        f'<section id="{sid}" class="sec">'
        f'<header class="sec-h"><span class="sec-n">{num}</span>'
        f'<h2>{html.escape(title)}</h2></header>'
        f'<div class="arrow" aria-hidden="true"></div>{body}</section>')
    nav.append(f'<li class="{kind}"><a href="#{sid}"><span class="n">{num}</span>'
               f'<span class="t">{html.escape(title)}</span></a></li>')
    plain = re.sub(r'<[^>]+>', ' ', body)
    plain = html.unescape(re.sub(r'\s+', ' ', plain))
    search.append({'id': sid, 'n': num, 't': title, 'x': plain[:6000].lower()})

def b64(rel): return base64.b64encode((REPO / rel).read_bytes()).decode()
logo    = b64('brand/logo/parametrix-logo-primary.png')
logo_ko = b64('brand/logo/parametrix-logo-knockout.png')
ixmark  = b64('brand/parametrix-x-mark.png')
# count decisions from the source markdown, not the truncated search text
alltext = ''.join((SOP / f'{fn}.md').read_text() for fn, _, _ in ORDER)
stats = {
    'decisions': alltext.count('Open Parametrix decision'),
    'raw': alltext.count('TRIMBLE DOCUMENTED PROCEDURE'),
    'words': sum(len(s['x'].split()) for s in search),
}

# ---- the legend, listing only the callouts this document actually uses ----
used = {k for k, marker in MARKERS.items() if marker in alltext}
if 'VENDOR CLARIFICATION REQUIRED' in alltext: used.add('testing')
order = [k for k in LEGEND_ROWS if k in used]
LEGEND = ('    <div class="legend">\n'
          + ''.join(f'      <div class="lg-{k}"><b>{LEGEND_ROWS[k][0]}</b>{LEGEND_ROWS[k][1]}</div>\n'
                    for k in order)
          + '    </div>\n')

# ---- the hero, built from the document's config ----
meta = ''.join(f'<div><dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd></div>'
               for k, v in CFG['stats'])
hero = (f'  <div class="hero">\n'
        f'    <div class="k">Draft — not approved for use</div>\n'
        f'    <h2>{html.escape(CFG["docname"])} — {html.escape(CFG["doctype"])}</h2>\n'
        f'    <p>{CFG["lead"]}</p>\n'
        + (f'    <div class="meta">{meta}</div>\n' if meta else '')
        + (f'    <div class="flag">{CFG["flag"]}</div>\n' if CFG['flag'] else '')
        + LEGEND + '  </div>')

TPL = pathlib.Path(__file__).with_name('doc-page-template.html').read_text()
page = (TPL.replace('{{LOGO}}', logo)
           .replace('{{NAV}}', '\n'.join(nav))
           .replace('{{HERO}}', hero)
           .replace('{{BODY}}', '\n'.join(sections))
           .replace('{{INDEX}}', json.dumps(search))
           .replace('{{DOCTITLE}}', html.escape(CFG['title']))
           .replace('{{DOCTYPE}}', html.escape(CFG['doctype']))
           .replace('{{DOCNAME}}', html.escape(CFG['docname']))
           .replace('{{DOCSUB}}', html.escape(CFG['sub']))
           .replace('{{LOGO_KO}}', logo_ko)
           .replace('{{IX}}', ixmark)
           .replace('{{ACCENT}}', CFG['accent'])
           .replace('{{ACCENT_ON}}', CFG['accent_on']))
OUT.write_text(page)
print(f'{KEY:7} -> {OUT.name}  {len(page)/1024:.0f} KB  ·  {len(ORDER)} sections  ·  accent {CFG["accent"]}')
