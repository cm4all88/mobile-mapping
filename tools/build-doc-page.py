#!/usr/bin/env python3
"""Build a browsable page for one of the four MX60 documents.

    python3 tools/build-doc-page.py manual|sop|field|office

All four share one template and one token file. The only things that differ are the
section list, the document-type label, the hero, and --pmx-id-pos: the position of the
red quarter in the document identity rule (0 = Manual, 1 = SOP, 2 = Field, 3 = Office).
See deliverables/_control/style/style-system.md.
"""
import re, sys, pathlib, html, json, base64

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import publication as pub


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
 ('02-document-control','2','Related Documents'),
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
 ('14-registration-requirements','14','Registration Requirements'),
 ('15-calibration-control','15','Calibration Control'),
 ('16-qc-requirements','16','Quality Control Requirements'),
 ('17-acceptance-and-approval','17','Acceptance and Approval'),
 ('18-destructive-operations','18','Destructive Operation Controls'),
 ('19-export-and-delivery','19','Export and Delivery Controls'),
 ('20-documentation-and-records','20','Documentation and Records'),
 ('21-retention-and-archive','21','Retention and Archive'),
 ('22-non-conformance','22','Non-conformance and Re-collection'),
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

FIELD_ORDER = [
 ('00-front-matter','0','Front Matter'),
 ('01-how-to-use-this-guide','1','How to Use This Guide'),
 ('02-before-you-leave-the-yard','2','Before You Leave the Yard'),
 ('03-equipment-inspection','3','Equipment Inspection'),
 ('04-mounting-the-sensor-unit','4','Mounting the Sensor Unit'),
 ('05-connections-and-cables','5','Connections and Cable Routing'),
 ('06-power-system-checks','6','Power System Checks'),
 ('07-battery-protect','7','Battery Protect'),
 ('08-starting-the-system','8','Starting the System'),
 ('09-connecting-to-tmi','9','Connecting to TMI'),
 ('10-mission-setup','10','Mission Setup in TMI'),
 ('11-disk-check','11','Disk Check'),
 ('12-navigation-initialization','12','Navigation Initialization'),
 ('13-gams-considerations','13','GAMS Considerations'),
 ('14-reading-navigation-status','14','Reading Navigation Status'),
 ('15-recording-runs','15','Recording Runs'),
 ('16-driving-practices','16','Driving Practices'),
 ('17-gnss-while-driving','17','GNSS While Driving'),
 ('18-field-qc-indicators','18','Field QC Indicators'),
 ('19-using-comments','19','Using Comments'),
 ('20-stopping-and-restarting','20','Stopping and Restarting'),
 ('21-the-closing-sequence','21','The Closing Sequence'),
 ('22-shutdown','22','Shutdown'),
 ('23-field-close-out','23','Field Close-out'),
 ('24-re-collect-or-not','24','Re-collect or Not'),
 ('25-data-transfer-and-handoff','25','Data Transfer and Handoff'),
 ('26-what-must-accompany-the-data','26','What Must Accompany the Data'),
 ('27-common-problems','27','Common Problems'),
 ('appendix-A-preflight-checklist','A','Preflight Checklist'),
 ('appendix-B-end-of-mission-checklist','B','End-of-Mission Checklist'),
 ('appendix-C-field-record-form','C','Field Record Form'),
 ('appendix-D-tmi-status-reference','D','TMI Status and Warning Reference'),
 ('appendix-E-quick-card','E','Quick Card'),
]

DOCS = {
 'manual': dict(
    dir='deliverables/technical-manual', out='technical-manual.html', accent='var(--brand-blue)', accent_on='var(--brand-white)',
    doctype='Technical Manual', docname='MX60 Mobile Mapping',
    title='MX60 Mobile Mapping Technical Manual',
    sub='Trimble MX60 · Trimble Business Center 2026.10',
    order=MANUAL_ORDER,
    lead=('Why the system behaves the way it does, and how we know. '
          'The evidence base for the SOP and the two How To guides.'),
    orient=('<b>This manual explains; it does not require.</b> It sets out what the MX60 and '
            'Trimble Business Center actually do, and how that is known. What Parametrix requires '
            'is in the SOP. Every section ends with an <b>In Plain Language</b> recap written for '
            'a surveyor who is new to mobile mapping.'),
 ),
 'sop': dict(
    dir='deliverables/sop', out='sop.html', accent='var(--brand-orange)', accent_on='var(--brand-charcoal)',
    doctype='Standard Operating Procedure', docname='MX60 Mobile Mapping',
    title='MX60 Mobile Mapping SOP',
    sub='Trimble MX60 · Trimble Business Center 2026.10',
    order=SOP_ORDER,
    lead=('What Parametrix requires of MX60 mobile mapping work. Short by design: it states '
          'requirements and points to the Technical Manual for explanation and to the How To '
          'guides for method.'),
    orient=('<b>Every instruction here says who is telling you.</b> A <b>Trimble requirement</b> '
            'or an <b>equipment limit</b> comes from the manufacturer and is not negotiable on a '
            'project. A <b>recommended practice</b> is Parametrix\'s, and a project may have a '
            'reason to differ &mdash; if it does, that is recorded. See &sect;3.2.'),
 ),
 'field': dict(
    dir='deliverables/field-how-to', out='field-how-to.html', accent='var(--brand-green)', accent_on='var(--brand-charcoal)',
    doctype='Field How To', docname='MX60 Mobile Mapping',
    title='MX60 Field How To',
    sub='Trimble MX60 · Trimble Mobile Imaging',
    order=FIELD_ORDER,
    lead=('How to run the MX60 in the field. Short numbered steps, meant to be used in or near '
          'the vehicle.'),
    orient=('<b>Start with Appendix E, the Quick Card</b> &mdash; the ten things that cost the '
            'most if missed. Four of them cannot be fixed from the office: an aiding sensor that '
            'was never activated, missed overlap, a mission with no closing sequence, and a disk '
            'cleared before the copy was verified.'),
 ),
 'office': dict(
    dir='deliverables/office-how-to', out='office-how-to.html', accent='var(--brand-yellow)', accent_on='var(--brand-charcoal)',
    doctype='Office How To', docname='MX60 Mobile Mapping',
    title='MX60 Office How To',
    sub='Trimble Business Center 2026.10 · Trimble MX60',
    order=OFFICE_ORDER,
    lead=('How to process MX60 data in Trimble Business Center, in the order you do it. '
          'Every section answers four questions: what to do, what to look at, what to expect, '
          'and what should make you stop.'),
    orient=('<b>Read &ldquo;Stop if&rdquo; in every section.</b> Three mistakes cost more than '
            'all the others and all three are silent: registration does not change the point cloud '
            'until <b>Update Scans</b> runs; a good RMS does not prove the work succeeded; and '
            '<b>Cleanup cannot be undone</b>.'),
 ),
}

KEY = sys.argv[1] if len(sys.argv) > 1 else 'manual'
CFG = DOCS[KEY]

# ---- the publication layer decides what a reader sees -----------------------
_amap = pub.appendix_map(KEY)
CFG = dict(CFG, order=[(fn, _amap.get(num, num), title)
                       for fn, num, title in CFG['order']
                       if fn not in pub.DROP_FILES.get(KEY, ())])
SOP = REPO / CFG['dir']
OUT = SOP / CFG['out']
ORDER = CFG['order'] or [
    (p.stem, p.stem.split('-')[0].lstrip('0') or '0', p.stem)
    for p in sorted(SOP.glob('*.md'))]


WORKING_VERSION = re.search(r"^DRAFT = '([^']+)'", open('tools/sync-circulation.py').read(),
                            re.M).group(1)

# The publication layer has already rewritten these, so the labels below are the
# reader-facing ones. Longest first, so a short prefix never wins.
CALLOUTS = [
    ('WHAT YOU SHOULD KNOW BEFORE MOVING ON', 'retain'),
    ('IN PLAIN LANGUAGE', 'plain'),
    ('IN PLAIN LANGUAGE', 'plain'),
    ('SCREENING METHOD — NOT VALIDATED', 'proposed'),
    ('NOT DOCUMENTED BY TRIMBLE', 'vendor'),
    ('PARAMETRIX REQUIREMENT', 'adopted'),
    ('RECOMMENDED PRACTICE', 'proposed'),
    ('SET BY THE PROJECT', 'decision'),
    ('NO PUBLISHED FIGURE', 'testing'),
    ('TRIMBLE REQUIREMENT', 'binding'),
    ('TRIMBLE METHOD', 'trimble'),
    ('EQUIPMENT LIMIT', 'binding'),
    ('OBSERVED IN THE SOFTWARE', 'observed'),
    ('WHY THIS MATTERS', 'why'),
    ('FIELD TIP', 'tip'),
    ('IMPORTANT', 'important'),
    ('CAUTION', 'caution'),
    ('ADVANCED', 'advanced'),
]

def strip_markers(s):
    """The circulation markers steer tools/sync-circulation.py. They are not content."""
    return re.sub(r'^<!-- /?circulation.*?-->\n?', '', s, flags=re.M)


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
    # markdown links: used by the landing page, not by the four documents
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', t)
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
                while i < len(lines) and re.match(r'^\s{2,}\S', lines[i]) and not re.match(r'^\s*[-*]', lines[i]):
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
 'plain':     ('In Plain Language', 'What the section means, why it matters, what to remember'),
 'trimble':   ('Trimble method', 'Trimble documents this &mdash; <b style="color:inherit">not necessarily a requirement</b>'),
 'binding':   ('Trimble requirement &middot; Equipment limit', 'Binding on the work, on the manufacturer\'s authority'),
 'observed':  ('Observed in the software', 'Seen in the software; not stated by Trimble'),
 'proposed':  ('Recommended practice', 'Parametrix recommendation &mdash; <b style="color:inherit">follow it unless the project says otherwise</b>'),
 'adopted':   ('Parametrix requirement', 'Required on Parametrix work'),
 'decision':  ('Set by the project', 'No single company-wide answer. The project decides, and records it'),
 'testing':   ('No published figure', 'No published number exists. Judgement, and the evidence on the job'),
}
MARKERS = {
 'caution':'CAUTION','important':'IMPORTANT','why':'WHY THIS MATTERS','plain':'IN PLAIN LANGUAGE',
 'trimble':'TRIMBLE METHOD','observed':'OBSERVED IN THE SOFTWARE',
 'proposed':'RECOMMENDED PRACTICE','adopted':'PARAMETRIX REQUIREMENT',
 'decision':'SET BY THE PROJECT','testing':'NO PUBLISHED FIGURE',
 'binding':'TRIMBLE REQUIREMENT','status':'\x00never\x00',
}

_OLD_LEGEND = """    <div class="legend">
      <div class="lg-caution"><b>Caution</b>Data loss, an irreversible operation, a lost result, or safety</div>
      <div class="lg-important"><b>Important</b>Gets the job wrong if ignored</div>
      <div class="lg-why"><b>Why this matters</b>The reason behind a behaviour or a requirement</div>
      <div class="lg-plain"><b>In Plain Language</b>What we did, why it matters, what can go wrong, what good looks like</div>
      <div class="lg-trimble"><b>Trimble documented method</b>Trimble documents this &mdash; not necessarily a requirement</div>
      <div class="lg-observed"><b>Observed software behavior</b>Seen in the software; not stated by Trimble as procedure</div>
      <div class="lg-proposed"><b>Parametrix procedure (proposed)</b>Recommended &mdash; <b style="color:inherit">not company policy</b></div>
      <div class="lg-decision"><b>Parametrix decision required</b>An internal standard still to be established</div>
      <div class="lg-testing"><b>Field testing / vendor clarification required</b>Answerable by test, or only by Trimble</div>
    </div>
"""
# ---- assemble ----
sections, nav, search = [], [], []
for fn, num, title in ORDER:
    md = pub.publish(KEY, fn, strip_markers((SOP / f'{fn}.md').read_text()))
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
alltext = ''.join(pub.publish(KEY, fn, strip_markers((SOP / f'{fn}.md').read_text()))
                  for fn, _, _ in ORDER)
stats = {
    'decisions': alltext.count('Open Parametrix decision'),
    'raw': alltext.count('TRIMBLE DOCUMENTED METHOD'),
    'plain': alltext.count('IN PLAIN LANGUAGE'),
    'words': len(re.sub(r'[#>|*`_\-]', ' ', alltext).split()),
}

# ---- the legend, listing only the callouts this document actually uses ----
used = {k for k, marker in MARKERS.items() if marker in alltext}
if 'NOT DOCUMENTED BY TRIMBLE' in alltext: used.add('testing')
if 'EQUIPMENT LIMIT' in alltext: used.add('binding')
order = [k for k in LEGEND_ROWS if k in used]
LEGEND = ('    <div class="legend">\n'
          + ''.join(f'      <div class="lg-{k}"><b>{LEGEND_ROWS[k][0]}</b>{LEGEND_ROWS[k][1]}</div>\n'
                    for k in order)
          + '    </div>\n')

# ---- the cover ----
hero = (f'  <div class="hero">\n'
        f'    <div class="k">{html.escape(CFG["doctype"])}</div>\n'
        f'    <h2>{html.escape(CFG["docname"])}</h2>\n'
        f'    <p>{CFG["lead"]}</p>\n'
        f'    <div class="cover-sub">{html.escape(CFG["sub"])}</div>\n'
        + (f'    <div class="flag">{CFG["orient"]}</div>\n' if CFG.get('orient') else '')
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
           .replace('{{ACCENT_ON}}', CFG['accent_on'])
           )
OUT.write_text(page)
print(f'{KEY:7} -> {OUT.name}  {len(page)/1024:.0f} KB  ·  {len(ORDER)} sections  ·  accent {CFG["accent"]}')
