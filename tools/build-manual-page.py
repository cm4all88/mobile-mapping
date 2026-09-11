#!/usr/bin/env python3
"""Build the browsable Technical Manual page from the section markdown files."""
import re, pathlib, html, json, base64

REPO = pathlib.Path('/home/user/mobile-mapping')
SOP = REPO / 'deliverables/technical-manual'
OUT = REPO / 'deliverables/technical-manual/technical-manual.html'

ORDER = [
    ('00-front-matter', '0', 'Front Matter'),
    ('01-purpose-and-scope', '1', 'Purpose and Scope'),
    ('02-mobile-mapping-in-plain-terms', '2', 'Mobile Mapping in Plain Terms'),
    ('03-how-error-behaves', '3', 'How Error Behaves'),
    ('04-the-workflow-end-to-end', '4', 'The Workflow, End to End'),
    ('05-the-data-chain', '5', 'The Data Chain'),
    ('06-terminology', '6', 'Terminology'),
    ('07-mx60-system-architecture', '7', 'MX60 System Architecture'),
    ('08-gnss-ins-integration', '8', 'GNSS/INS Integration'),
    ('09-gams-and-dmi', '9', 'GAMS and DMI'),
    ('10-tmi-tbc-pospac', '10', 'TMI, TBC and POSPac'),
    ('11-lidar-qc', '11', 'LiDAR QC'),
    ('12-coordinate-systems', '12', 'Coordinate Systems, Datums and Epochs'),
    ('13-initialization', '13', 'Initialization'),
    ('14-the-closing-sequence', '14', 'The Closing Sequence'),
    ('15-gnss-environment-and-outage-duration', '15', 'GNSS Environment and Outage Duration'),
    ('16-point-density-and-useful-range', '16', 'Point Density and Useful Range'),
    ('17-trajectory-processing', '17', 'Trajectory Processing'),
    ('18-scan-generation', '18', 'Scan Generation'),
    ('19-update-scans', '19', 'Update Scans'),
    ('20-calibration', '20', 'Calibration'),
    ('21-registration', '21', 'Registration'),
    ('22-gcps-check-points-and-residuals', '22', 'GCPs, Check Points and Residuals'),
    ('23-rms-and-what-it-can-prove', '23', 'RMS and What It Can Prove'),
    ('24-trajectory-rms-colouring', '24', 'Trajectory RMS Colouring'),
    ('25-visual-qc', '25', 'Visual QC'),
    ('26-imagery', '26', 'Imagery'),
    ('27-degraded-gnss', '27', 'Degraded GNSS'),
    ('28-cleanup', '28', 'Cleanup Mobile Mapping Mission'),
    ('29-export', '29', 'Export'),
    ('30-provenance', '30', 'Provenance'),
    ('31-periodic-system-verification', '31', 'Periodic System Verification'),
    ('appendix-A-trimble-source-index', 'A', 'Trimble Source Index'),
    ('appendix-B-reference-dataset', 'B', 'The Reference Dataset'),
    ('appendix-C-figures', 'C', 'Figures and Screenshots'),
    ('appendix-D-observed-software-behaviour', 'D', 'Observed Software Behaviour'),
    ('appendix-E-open-technical-questions', 'E', 'Open Technical Questions'),
    ('appendix-F-test-results', 'F', 'Test Results'),
    ('appendix-G-source-conflicts', 'G', 'Source Conflicts and Resolutions'),
]

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
    ('WHY THIS MATTERS', 'why'),
    ('FIELD TIP', 'tip'),
    ('IMPORTANT', 'important'),
    ('CAUTION', 'caution'),
    ('ADVANCED', 'advanced'),
]

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\*\w])\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
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
            for ln in blk:
                if not ln.strip(): flush(); continue
                if re.match(r'^[-*]\s+', ln.strip()):
                    flush()
                    txt = re.sub(r'^[-*]\s+', '', ln.strip())
                    body.append('<p class="co-li">' + inline(txt) + '</p>')
                elif re.match(r'^\d+\.\s+', ln.strip()):
                    # numbered item: keep the number, suppress the bullet marker
                    flush(); body.append(f'<p class="co-li co-num">{inline(ln.strip())}</p>')
                elif ln.strip().startswith('|'):
                    flush(); body.append(f'<p>{inline(ln.strip().strip("|"))}</p>')
                else: buf.append(ln.strip())
            flush()
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
                items.append(inline(re.sub(r'^\s*\d+\.\s+', '', lines[i]))); i += 1
                while i < len(lines) and re.match(r'^\s{3,}\S', lines[i]) and not re.match(r'^\s*\d+\.', lines[i]):
                    items[-1] += ' ' + inline(lines[i].strip()); i += 1
            out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>')
            continue

        if re.match(r'^[-*]\s+', t):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*]\s+', lines[i]):
                items.append(inline(re.sub(r'^\s*[-*]\s+', '', lines[i]))); i += 1
                while i < len(lines) and re.match(r'^\s{3,}\S', lines[i]) and not re.match(r'^\s*[-*]', lines[i]):
                    items[-1] += ' ' + inline(lines[i].strip()); i += 1
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
        f'<h2>{html.escape(title)}</h2></header>{body}</section>')
    nav.append(f'<li class="{kind}"><a href="#{sid}"><span class="n">{num}</span>'
               f'<span class="t">{html.escape(title)}</span></a></li>')
    plain = re.sub(r'<[^>]+>', ' ', body)
    plain = html.unescape(re.sub(r'\s+', ' ', plain))
    search.append({'id': sid, 'n': num, 't': title, 'x': plain[:6000].lower()})

logo = base64.b64encode((REPO / 'brand/parametrix-wordmark.png').read_bytes()).decode()
# count decisions from the source markdown, not the truncated search text
alltext = ''.join((SOP / f'{fn}.md').read_text() for fn, _, _ in ORDER)
stats = {
    'decisions': alltext.count('Open Parametrix decision'),
    'raw': alltext.count('TRIMBLE DOCUMENTED PROCEDURE'),
    'words': sum(len(s['x'].split()) for s in search),
}

TPL = pathlib.Path(__file__).with_name('manual-page-template.html').read_text()
page = (TPL.replace('{{LOGO}}', logo)
           .replace('{{NAV}}', '\n'.join(nav))
           .replace('{{BODY}}', '\n'.join(sections))
           .replace('{{INDEX}}', json.dumps(search))
           .replace('{{DECISIONS}}', str(stats['decisions'])))
OUT.write_text(page)
print(f'wrote {OUT}  {len(page)/1024:.0f} KB  ·  {len(ORDER)} sections  ·  Trimble-documented blocks: {stats["raw"]}')
