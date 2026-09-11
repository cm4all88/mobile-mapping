const fs = require('fs');
const path = require('path');
const D = require('docx');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, ImageRun,
  TableOfContents, Header, Footer, PageNumber, LevelFormat, convertInchesToTwip,
} = D;

const REPO = '/home/user/mobile-mapping';
const SRC = path.join(REPO, 'SOP/MX60-SOP-COMPLETE.md');
const OUT = path.join(REPO, 'SOP/Parametrix-MX60-Mobile-Mapping-SOP.docx');

const CHARCOAL = '343433';
const RED = 'EB2A2B';
const GREY = '6B6B6A';
const LIGHT = 'F2F2F1';

// Letter, 1" margins -> content width 9360 DXA
const CONTENT_W = 9360;

const CALLOUTS = {
  'WHAT YOU SHOULD KNOW BEFORE MOVING ON': { color: CHARCOAL, bg: 'EFEFEC' },
  'IN PLAIN ENGLISH':             { color: '1F5C86', bg: 'EDF2F8' },
  'CAUTION':                      { color: RED,      bg: 'FDECEC' },
  'IMPORTANT':                    { color: CHARCOAL, bg: 'FFF6E0' },
  'FIELD TIP':                    { color: '1F6B3B', bg: 'EDF6F0' },
  'WHY THIS MATTERS':             { color: '1F4E79', bg: 'EDF2F8' },
  'PARAMETRIX PROCEDURE (PROPOSED)': { color: '5B3E8E', bg: 'F4F0F8' },
  'PARAMETRIX PROCEDURE (ADOPTED)':  { color: '1F6B3B', bg: 'EDF6F0' },
  'PARAMETRIX DECISION REQUIRED': { color: RED,      bg: 'F4F0F8' },
  'TRIMBLE DOCUMENTED METHOD': { color: '1F4E79', bg: 'F2F5F9' },
  'OBSERVED SOFTWARE BEHAVIOR':   { color: '5A5A55', bg: 'F4F4F1' },
  'VENDOR CLARIFICATION REQUIRED':{ color: '8A5A1F', bg: 'FBF3E8' },
  'FIELD TESTING REQUIRED':       { color: '8A5A1F', bg: 'FBF3E8' },
  'ADVANCED':                     { color: GREY,     bg: LIGHT  },
};

// ---------- inline markdown -> TextRun[] ----------
function runs(text, base = {}) {
  const out = [];
  // tokenise **bold**, *italic*, `code`
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g;
  let last = 0, m;
  const push = (t, extra) => { if (t) out.push(new TextRun({ text: t, ...base, ...extra })); };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index));
    const tok = m[0];
    if (tok.startsWith('**')) push(tok.slice(2, -2), { bold: true });
    else if (tok.startsWith('`')) push(tok.slice(1, -1), { font: 'Consolas', size: 18, shading: { type: ShadingType.CLEAR, fill: LIGHT } });
    else push(tok.slice(1, -1), { italics: true });
    last = m.index + tok.length;
  }
  push(text.slice(last));
  return out.length ? out : [new TextRun({ text: '', ...base })];
}

function stripMd(s) {
  return s.replace(/\*\*/g, '').replace(/(^|\s)\*([^*]+)\*/g, '$1$2').replace(/`/g, '');
}

// ---------- table ----------
function splitRow(line) {
  return line.replace(/^\||\|$/g, '').split('|').map(c => c.trim());
}

function buildTable(lines) {
  const header = splitRow(lines[0]);
  const body = lines.slice(2).map(splitRow);
  const n = header.length;
  const colW = Math.floor(CONTENT_W / n);
  const widths = Array(n).fill(colW);
  widths[n - 1] = CONTENT_W - colW * (n - 1);

  const mkCell = (txt, i, isHeader) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: isHeader ? CHARCOAL : 'FFFFFF' },
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    children: [new Paragraph({
      spacing: { before: 0, after: 0 },
      children: runs(txt, isHeader ? { bold: true, color: 'FFFFFF', size: 18 } : { size: 18 }),
    })],
  });

  const rows = [new TableRow({ tableHeader: true, children: header.map((h, i) => mkCell(h, i, true)) })];
  for (const r of body) {
    const cells = [];
    for (let i = 0; i < n; i++) cells.push(mkCell(r[i] === undefined ? '' : r[i], i, false));
    rows.push(new TableRow({ children: cells }));
  }
  const thin = { style: BorderStyle.SINGLE, size: 2, color: 'D9D9D8' };
  return new Table({
    columnWidths: widths,
    width: { size: CONTENT_W, type: WidthType.DXA },
    borders: { top: thin, bottom: thin, left: thin, right: thin, insideHorizontal: thin, insideVertical: thin },
    rows,
  });
}

// ---------- callout ----------
function buildCallout(blockLines) {
  const text = blockLines.map(l => l.replace(/^>\s?/, ''));
  let label = null;
  for (const key of Object.keys(CALLOUTS)) {
    if (text[0] && stripMd(text[0]).trim().toUpperCase().startsWith(key)) { label = key; break; }
  }
  const style = label ? CALLOUTS[label] : { color: GREY, bg: LIGHT };
  const kids = [];
  let first = true;
  let buf = [];
  const flush = () => {
    if (!buf.length) return;
    const joined = buf.join(' ').trim();
    if (joined) kids.push(new Paragraph({
      spacing: { before: first ? 0 : 80, after: 0 },
      children: runs(joined, { size: 19 }),
    }));
    buf = [];
    first = false;
  };
  text.forEach((line, idx) => {
    if (idx === 0 && label) {
      const rest = stripMd(line).trim().slice(label.length).replace(/^[\s—–-]+/, '');
      kids.push(new Paragraph({
        spacing: { before: 0, after: rest ? 40 : 80 },
        children: [new TextRun({ text: label + (rest ? ' — ' + rest : ''), bold: true, color: style.color, size: 19 })],
      }));
      first = false;
      return;
    }
    if (!line.trim()) { flush(); return; }
    if (/^[-*]\s+/.test(line.trim())) {
      flush();
      kids.push(new Paragraph({
        spacing: { before: 40, after: 0 }, indent: { left: 180 },
        children: runs('• ' + line.trim().replace(/^[-*]\s+/, ''), { size: 19 }),
      }));
      first = false;
      return;
    }
    buf.push(line.trim());
  });
  flush();
  if (!kids.length) kids.push(new Paragraph({ children: [new TextRun('')] }));

  return new Table({
    columnWidths: [CONTENT_W],
    width: { size: CONTENT_W, type: WidthType.DXA },
    borders: {
      top:    { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      right:  { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      left:   { style: BorderStyle.SINGLE, size: 18, color: style.color },
      insideHorizontal: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      insideVertical:   { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
    },
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: style.bg },
      margins: { top: 120, bottom: 120, left: 200, right: 160 },
      children: kids,
    })] })],
  });
}

// ---------- main parse ----------
const md = fs.readFileSync(SRC, 'utf8').split('\n');
const body = [];
let i = 0;
const spacer = (after = 120) => new Paragraph({ spacing: { after }, children: [new TextRun('')] });

while (i < md.length) {
  const line = md[i];
  const t = line.trim();

  // skip the markdown title block at very top (handled by cover)
  if (t === '---') { i++; continue; }
  if (!t) { i++; continue; }

  // headings
  let hm = /^(#{1,4})\s+(.*)$/.exec(t);
  if (hm) {
    const lvl = hm[1].length;
    const txt = stripMd(hm[2]);
    if (/^PARAMETRIX$/i.test(txt) || /^TRIMBLE MX60 MOBILE MAPPING$/i.test(txt) || /^STANDARD OPERATING PROCEDURE$/i.test(txt)) { i++; continue; }
    const map = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4 };
    if (lvl === 1) body.push(new Paragraph({ children: [new PageBreak()] }));
    body.push(new Paragraph({
      heading: map[lvl],
      spacing: { before: lvl === 1 ? 0 : (lvl === 2 ? 320 : 240), after: lvl === 1 ? 200 : 120 },
      children: [new TextRun({ text: txt, bold: true, color: lvl <= 2 ? CHARCOAL : GREY, size: lvl === 1 ? 34 : lvl === 2 ? 26 : 22 })],
      border: lvl === 1 ? { bottom: { style: BorderStyle.SINGLE, size: 12, color: RED, space: 6 } } : undefined,
    }));
    i++; continue;
  }

  // table
  if (t.startsWith('|') && i + 1 < md.length && /^\|[\s:|-]+\|$/.test(md[i + 1].trim())) {
    const block = [];
    while (i < md.length && md[i].trim().startsWith('|')) { block.push(md[i].trim()); i++; }
    body.push(buildTable(block));
    body.push(spacer(160));
    continue;
  }

  // blockquote / callout
  if (t.startsWith('>')) {
    const block = [];
    while (i < md.length && (md[i].trim().startsWith('>') || (md[i].trim() === '' && md[i + 1] && md[i + 1].trim().startsWith('>')))) {
      if (md[i].trim().startsWith('>')) block.push(md[i].trim());
      else block.push('>');
      i++;
    }
    body.push(buildCallout(block));
    body.push(spacer(160));
    continue;
  }

  // fenced code
  if (t.startsWith('```')) {
    i++;
    const code = [];
    while (i < md.length && !md[i].trim().startsWith('```')) { code.push(md[i]); i++; }
    i++;
    body.push(new Table({
      columnWidths: [CONTENT_W],
      width: { size: CONTENT_W, type: WidthType.DXA },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 2, color: 'D9D9D8' },
        bottom: { style: BorderStyle.SINGLE, size: 2, color: 'D9D9D8' },
        left: { style: BorderStyle.SINGLE, size: 2, color: 'D9D9D8' },
        right: { style: BorderStyle.SINGLE, size: 2, color: 'D9D9D8' },
        insideHorizontal: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
        insideVertical: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      },
      rows: [new TableRow({ children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: LIGHT },
        margins: { top: 120, bottom: 120, left: 160, right: 160 },
        children: code.map(c => new Paragraph({
          spacing: { before: 0, after: 0 },
          children: [new TextRun({ text: c.replace(/\t/g, '    ') || ' ', font: 'Consolas', size: 17 })],
        })),
      })] })],
    }));
    body.push(spacer(160));
    continue;
  }

  // ordered list
  let om = /^(\d+)\.\s+(.*)$/.exec(t);
  if (om) {
    body.push(new Paragraph({
      numbering: { reference: 'sop-numbers', level: 0 },
      spacing: { before: 40, after: 40 },
      children: runs(om[2]),
    }));
    i++; continue;
  }

  // bullet list (incl. nested by leading spaces)
  let bm = /^([-*])\s+(.*)$/.exec(t);
  if (bm) {
    const indent = line.match(/^\s*/)[0].length;
    body.push(new Paragraph({
      numbering: { reference: 'sop-bullets', level: indent >= 2 ? 1 : 0 },
      spacing: { before: 40, after: 40 },
      children: runs(bm[2]),
    }));
    i++; continue;
  }

  // plain paragraph (gather wrapped lines)
  const para = [t];
  i++;
  while (i < md.length) {
    const nx = md[i].trim();
    if (!nx || nx.startsWith('#') || nx.startsWith('|') || nx.startsWith('>') || nx.startsWith('```')
      || /^[-*]\s+/.test(nx) || /^\d+\.\s+/.test(nx) || nx === '---') break;
    para.push(nx); i++;
  }
  body.push(new Paragraph({
    spacing: { before: 0, after: 140, line: 276 },
    children: runs(para.join(' ')),
  }));
}

// ---------- cover ----------
const logo = fs.readFileSync(path.join(REPO, 'brand/parametrix-wordmark.png'));
const cover = [
  new Paragraph({ spacing: { before: 2400, after: 0 }, children: [
    new ImageRun({ data: logo, type: 'png', transformation: { width: 360, height: 51 } }),
  ]}),
  new Paragraph({ spacing: { before: 900, after: 0 }, children: [
    new TextRun({ text: 'TRIMBLE MX60', bold: true, size: 56, color: CHARCOAL }),
  ]}),
  new Paragraph({ spacing: { before: 0, after: 0 }, children: [
    new TextRun({ text: 'MOBILE MAPPING', bold: true, size: 56, color: CHARCOAL }),
  ]}),
  new Paragraph({
    spacing: { before: 200, after: 0 },
    border: { top: { style: BorderStyle.SINGLE, size: 18, color: RED, space: 10 } },
    children: [new TextRun({ text: '' })],
  }),
  new Paragraph({ spacing: { before: 260, after: 0 }, children: [
    new TextRun({ text: 'STANDARD OPERATING PROCEDURE', size: 30, color: GREY, characterSpacing: 30 }),
  ]}),
  new Paragraph({ spacing: { before: 2600, after: 0 }, children: [
    new TextRun({ text: 'DRAFT — NOT APPROVED FOR USE', bold: true, size: 22, color: RED }),
  ]}),
  new Paragraph({ spacing: { before: 120, after: 0 }, children: [
    new TextRun({ text: 'Revision 1.0-draft   ·   10 September 2026', size: 20, color: GREY }),
  ]}),
  new Paragraph({ spacing: { before: 40, after: 0 }, children: [
    new TextRun({ text: 'Internal document', size: 20, color: GREY }),
  ]}),
  new Paragraph({ children: [new PageBreak()] }),
  new Paragraph({
    spacing: { before: 0, after: 240 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: RED, space: 6 } },
    children: [new TextRun({ text: 'Contents', bold: true, size: 34, color: CHARCOAL })],
  }),
  new TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-3' }),
];

// ---------- document ----------
const doc = new Document({
  creator: 'Parametrix',
  title: 'Parametrix Trimble MX60 Mobile Mapping SOP',
  description: 'Standard Operating Procedure for the Trimble MX60 mobile mapping system',
  features: { updateFields: true },
  styles: {
    default: {
      document: { run: { font: 'Calibri', size: 21, color: '2B2B2A' }, paragraph: { spacing: { line: 276 } } },
    },
  },
  numbering: {
    config: [
      { reference: 'sop-bullets', levels: [
        { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 200 } } } },
        { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 200 } } } },
      ]},
      { reference: 'sop-numbers', levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 200 } } } },
      ]},
    ],
  },
  sections: [
    {
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
      children: cover,
    },
    {
      properties: {
        page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } },
      },
      headers: { default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'D9D9D8', space: 4 } },
        children: [new TextRun({ text: 'Parametrix  ·  Trimble MX60 Mobile Mapping SOP', size: 16, color: GREY })],
      })] }) },
      footers: { default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [
          new TextRun({ text: 'DRAFT   ', size: 16, color: RED, bold: true }),
          new TextRun({ text: 'Page ', size: 16, color: GREY }),
          new TextRun({ children: [PageNumber.CURRENT], size: 16, color: GREY }),
        ],
      })] }) },
      children: body,
    },
  ],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT, buf);
  console.log('wrote', OUT, (buf.length / 1024 / 1024).toFixed(2), 'MB');
  console.log('body elements:', body.length);
});
