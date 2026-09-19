/**
 * Parametrix Mobile Mapping — capability brochure for the marketing team.
 *
 *   node marketing/build-capability-brochure.js
 *
 * Editable working file. Marketing restyles it and places the logo; the words
 * and the numbers are the part that has been checked.
 *
 * EVERY specification figure traces to reference/mx60-reference-data.csv, which
 * is the project's authority for numbers. The SPEC ids are in comments beside
 * each one so a reviewer can follow them back.
 *
 * Colours and faces from deliverables/_control/style/brand-tokens.css
 * (Parametrix Brand Guide v6, p.16, p.18). No tagline: the guide puts
 * "client-facing document" in the Do Not Use Tagline column (p.12).
 */
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  PageBreak, PageOrientation, LevelFormat,
} = require('docx');
const fs = require('fs');

const RED = 'EE3D24';
const CHARCOAL = '333333';
const GRAY = '676768';
const GRAY4 = 'F2F2F2';
const GRAY3 = 'E5E5E5';
const WHITE = 'FFFFFF';

const HEAD = 'Klinic Slab';       // falls back to Rockwell, the guide's own alternate
const BODY = 'Franklin Gothic Book';
const QUOTE = 'Freight Text Pro';

const LETTER = { width: 12240, height: 15840 };
const MARGIN = { top: 1080, right: 1080, bottom: 1080, left: 1080 };
const CONTENT_W = LETTER.width - MARGIN.left - MARGIN.right; // 10080 dxa

const NONE = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE,
                    insideHorizontal: NONE, insideVertical: NONE };

// ---------- small builders ----------------------------------------------

const p = (text, o = {}) => new Paragraph({
  alignment: o.align,
  spacing: { before: o.before ?? 0, after: o.after ?? 140, line: o.line ?? 280 },
  indent: o.indent,
  border: o.border,
  children: [new TextRun({
    text, font: o.font ?? BODY, size: o.size ?? 21,
    color: o.color ?? CHARCOAL, bold: o.bold, italics: o.italics,
  })],
});

/** A paragraph from parts: ['plain', ['bold bit', {bold:true}], ...] */
const rich = (parts, o = {}) => new Paragraph({
  alignment: o.align,
  spacing: { before: o.before ?? 0, after: o.after ?? 140, line: o.line ?? 280 },
  indent: o.indent,
  children: parts.map(x => {
    const [t, f] = Array.isArray(x) ? x : [x, {}];
    return new TextRun({
      text: t, font: f.font ?? o.font ?? BODY, size: f.size ?? o.size ?? 21,
      color: f.color ?? o.color ?? CHARCOAL, bold: f.bold, italics: f.italics,
    });
  }),
});

const h1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 0, after: 200 },
  children: [new TextRun({ text, font: HEAD, size: 52, bold: true, color: RED })],
});

const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  keepNext: true, keepLines: true,
  spacing: { before: 320, after: 140 },
  children: [new TextRun({ text, font: HEAD, size: 30, bold: true, color: RED })],
});

const h3 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_3,
  keepNext: true, keepLines: true,
  spacing: { before: 240, after: 100 },
  children: [new TextRun({ text, font: BODY, size: 22, bold: true, color: CHARCOAL })],
});

/** The brand's one precedent for a marked-off block: a red left rule (p.16). */
const pullquote = (text) => new Paragraph({
  spacing: { before: 200, after: 220, line: 300 },
  indent: { left: 240 },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: RED, space: 12 } },
  children: [new TextRun({ text, font: QUOTE, size: 23, color: RED })],
});

/** Real bullets come from the numbering config below, never a literal glyph. */
const bullet = (parts) => {
  const q = rich(Array.isArray(parts) ? parts : [parts], { after: 110 });
  return new Paragraph({
    numbering: { reference: 'px-bullets', level: 0 },
    spacing: { after: 110, line: 280 },
    children: q.root.filter(c => c.constructor.name === 'TextRun'),
  });
};

const rule = () => new Paragraph({
  spacing: { before: 60, after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GRAY3, space: 4 } },
  children: [new TextRun({ text: '', size: 2 })],
});

const placeholder = (text) => new Paragraph({
  spacing: { before: 160, after: 160 },
  children: [new TextRun({ text, font: BODY, size: 19, color: GRAY, italics: true })],
});

const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

/** Two-column reference table. cols is [leftDxa, rightDxa]. */
function refTable(rows, cols, opts = {}) {
  const widths = cols ?? [3600, CONTENT_W - 3600];
  const cell = (text, w, o = {}) => new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade, color: 'auto' } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: GRAY3 },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: GRAY3 },
      left: NONE, right: NONE,
    },
    children: [new Paragraph({
      spacing: { before: 0, after: 0, line: 260 },
      children: [new TextRun({
        text, font: BODY, size: o.size ?? 20,
        color: o.color ?? CHARCOAL, bold: o.bold,
      })],
    })],
  });

  const body = rows.map(([a, b], i) => new TableRow({
    children: [
      cell(a, widths[0], { bold: true, shade: opts.head && i === 0 ? GRAY4 : undefined }),
      cell(b, widths[1], { shade: opts.head && i === 0 ? GRAY4 : undefined }),
    ],
  }));

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: noBorders,
    rows: body,
  });
}

const spacer = (h = 200) => new Paragraph({ spacing: { after: h }, children: [new TextRun({ text: '', size: 2 })] });

// ---------- page 1 · cover ----------------------------------------------

const cover = [
  spacer(1400),
  placeholder('[ Parametrix logo — charcoal and red, minimum 1 inch wide, clear space on all four sides at least the height of the right side of the x. Master EPS from Templafy. Brand Guide pp.10–14. ]'),
  spacer(900),
  new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: 'MOBILE MAPPING', font: HEAD, size: 76, bold: true, color: RED })],
  }),
  new Paragraph({
    spacing: { after: 420 },
    children: [new TextRun({ text: 'Corridor survey at traffic speed', font: BODY, size: 32, color: CHARCOAL })],
  }),
  new Paragraph({
    spacing: { after: 200, line: 320 },
    border: { top: { style: BorderStyle.SINGLE, size: 12, color: RED, space: 14 } },
    children: [new TextRun({ text: '', size: 2 })],
  }),
  rich([
    'Parametrix operates a ',
    ['Trimble MX60 Premium', { bold: true }],
    ' mobile mapping system — survey-grade laser scanning and imaging on a vehicle. It measures ' +
    'continuously while driving, which suits corridors where stopping is unsafe, slow or expensive.',
  ], { size: 24, line: 340, after: 200 }),
  spacer(4700),
  placeholder('[ Office · address · phone · email — marketing to complete ]'),
];

// ---------- page 2 · what it is, where it fits --------------------------

const whatItIs = [
  h1('What it is'),

  rich([
    'A total station or a static scanner measures from a fixed, occupied point. ',
    ['The MX60 never stops.', { bold: true }],
    ' Two laser scanners record range and angle continuously while the system computes, for every ' +
    'instant, where the sensor head was and which way it was pointing. A mile of roadway is ' +
    'captured in the time it takes to drive it.',
  ], { line: 300 }),

  p('Two cameras run alongside the scanners — a 360° spherical camera and a downward camera on the ' +
    'pavement — so the imagery and the measurements come from the same pass, at the same instant, ' +
    'in the same coordinate system.'),

  h2('Where it fits'),

  refTable([
    ['Roadway corridors', 'Pavement surface, striping, signing, barrier, drainage structures, clear zone'],
    ['Interchanges and arterials', 'Complex geometry captured in passes rather than in set-ups'],
    ['Rail and transit', 'Track-adjacent measurement without putting a crew in the corridor on foot'],
    ['Ports, yards, large sites', 'Large paved areas in a fraction of the time static methods take'],
    ['Asset inventory', 'Every asset in the corridor located and photographed on the same pass'],
    ['Existing-conditions base', 'A measured, dated record of the whole corridor, not only what was staked'],
  ], [3200, CONTENT_W - 3200]),

  h2('Why a client asks for it'),

  bullet([['Traffic stays open. ', { bold: true }],
    'The vehicle collects at up to 50 mph. The survey itself needs no lane closure.']),
  bullet([['Crews stay out of the roadway. ', { bold: true }],
    'The measurement is made from inside a moving vehicle.']),
  bullet([['The whole corridor is captured. ', { bold: true }],
    'A question asked three months later is answered from the same dataset, without going back.']),
  bullet([['It is imaged as well as measured. ', { bold: true }],
    'The panoramas are a dated visual record of conditions on the day of collection.']),

  h2('What you receive'),

  refTable([
    ['Point cloud', 'LAS or LAZ, in the project coordinate system, classified to the project scope'],
    ['Panoramic imagery', '360°, geo-referenced, 72 megapixel'],
    ['Pavement imagery', 'Downward-facing, 12 megapixel, geo-referenced'],
    ['Derived products', 'Surfaces, breaklines, planimetric features, asset inventories and orthomosaics, ' +
                         'extracted to the project scope'],
    ['Survey record', 'The control used, the check point results, and the coordinate system, datum and epoch ' +
                      'the deliverable is on'],
  ], [3200, CONTENT_W - 3200]),
];

// ---------- page 3 · the system -----------------------------------------

const theSystem = [
  h1('The system'),

  rich([
    ['Trimble MX60 Premium', { bold: true }],
    ' — the top of the three MX60 configurations. Every figure on this page is Trimble’s published ' +
    'specification for this system, under the conditions Trimble states.',
  ], { line: 300, after: 220 }),

  h3('Laser scanning'),
  refTable([
    ['Scanners', 'Two, time-of-flight'],                              // SPEC-002, SPEC-003
    ['Measurement rate', '1,000,000 or 2,000,000 points per second, selectable — system total'], // SPEC-005
    ['Maximum range', '150 m at the lower rate; 120 m at the higher'], // SPEC-006
    ['Minimum range', '0.6 m'],                                        // SPEC-008
    ['Range accuracy', '2 mm'],                                        // SPEC-009
    ['Precision', '2.5 mm at 30 m'],                                   // SPEC-010
    ['Profile rate', '240 or 400 profiles per second, selectable — system total'], // SPEC-011
    ['Laser class', 'Class 1 — eye safe'],                             // SPEC-016
  ], [3200, CONTENT_W - 3200]),
  p('Range is specified against flat targets larger than the beam, at perpendicular incidence, in ' +
    '23 km visibility. Working distance on a real corridor is shorter.',
    { size: 18, color: GRAY, after: 60 }),

  h3('Imaging'),
  refTable([
    ['Spherical camera', '72 megapixel, six cameras, global shutter, about 90% of the full sphere, up to 10 fps'], // SPEC-021,022,024,029,030
    ['Downward camera', '12 megapixel, up to 9 fps'],                  // SPEC-035, SPEC-040
    ['Capture trigger', 'By distance or by time'],
  ], [3200, CONTENT_W - 3200]),

  h3('Positioning'),
  refTable([
    ['Integration', 'Applanix IN-Fusion+ GNSS-inertial'],              // SPEC-052
    ['GNSS tracking', '2 × 336 channels'],                             // SPEC-051
    ['Roll and pitch', '0.0025°'],                                     // SPEC-047 (Premium)
    ['Heading', '0.015°'],                                             // SPEC-048
    ['Position after a 60-second GNSS outage', '0.10 m horizontal · 0.07 m vertical'], // SPEC-050 (Premium)
  ], [3200, CONTENT_W - 3200]),

  h3('Collection'),
  refTable([
    ['Recommended maximum speed, system operating', '80 km/h (50 mph)'],
    ['Onboard storage', '2 × 4 TB removable SSD'],                     // SPEC-067
  ], [3200, CONTENT_W - 3200]),
];

// ---------- page 4 · accuracy -------------------------------------------

const accuracy = [
  h1('How accuracy is established'),

  pullquote('There is no single accuracy figure for a mobile mapping deliverable. ' +
            'A firm that quotes you one before asking about your corridor is guessing.'),

  p('Every point in the cloud is the sum of two things: a range and angle measured by the scanner, ' +
    'and the position and orientation of the scanner at that instant. The scanner part is excellent ' +
    'and nearly constant. The second part is a computed path, and its quality changes along the ' +
    'corridor with the sky — open highway, tree canopy, an underpass, an urban canyon.'),

  p('So the accuracy question is answered per project, against control, and the evidence is part of ' +
    'the deliverable:'),

  bullet([['The accuracy requirement is agreed in writing before collection. ', { bold: true }],
    'It drives the control design, the number of passes and the driving pattern — none of which can ' +
    'be fixed afterwards.']),
  bullet([['The trajectory is fitted to surveyed control, ', { bold: true }],
    'established conventionally and bracketing the extent of the work.']),
  bullet([['Independent check points are measured against the finished product. ', { bold: true }],
    'Points that helped compute the answer cannot test it. Points held out of the adjustment can, ' +
    'and those are the residuals that get reported.']),
  bullet([['Quality is reported along the corridor, not averaged over it. ', { bold: true }],
    'A single project-wide number hides the stretch that matters to you.']),

  h2('When mobile mapping is the wrong tool'),

  p('We will say so. A corridor under heavy continuous canopy, a site needing measurements the ' +
    'vehicle cannot see, or a tolerance tighter than the method supports are all cases where ' +
    'conventional survey or static scanning produces a more defensible result. Sometimes the answer ' +
    'is a combination. Recommending the right method, including when it is not this one, is part of ' +
    'the service.'),

  h2('Behind the deliverable'),

  p('The system is operational and has been run. The procedures behind it — field collection, office ' +
    'processing, quality control, and the records that make a deliverable traceable to what produced ' +
    'it — are written down: a technical manual, a standard operating procedure, and field and office ' +
    'guides, currently in internal review.'),

  rule(),
  placeholder('[ Contact block — name, title, phone, email. Marketing to complete. ]'),
];

// ---------- page 5 · internal notes, to be deleted -----------------------

const notes = [
  new Paragraph({
    spacing: { after: 160 },
    shading: { type: ShadingType.CLEAR, fill: RED, color: 'auto' },
    children: [new TextRun({
      text: '  DELETE THIS PAGE BEFORE THE BROCHURE GOES OUT  ',
      font: HEAD, size: 30, bold: true, color: WHITE,
    })],
  }),

  h2('Notes for the marketing team'),

  p('The numbers on page 3 were taken from the project’s reference dataset, ' +
    'reference/mx60-reference-data.csv, which is the authority for every figure in the MX60 ' +
    'documentation. They are Trimble’s published specifications for the equipment. They are not ' +
    'claims about what a Parametrix deliverable achieves, and the wording keeps that distinction.'),

  h3('Four things that must not be added'),

  refTable([
    ['Do not add', 'Why'],
    ['A delivered accuracy figure — "1 cm mobile mapping", "survey-grade to 0.02 ft"',
     'What constitutes an acceptable result has not been decided (register D-13), and the control ' +
     'design that would support it has not been specified (D-16). Accuracy is a per-project ' +
     'statement made against that project’s control.'],
    ['Trimble’s no-outage figure of "better than 1 cm horizontal"',
     'Trimble states it with the DMI option fitted. Whether this system carries a DMI is not yet ' +
     'established (D-2). Until it is, that figure is not ours to quote.'],
    ['Any claim of delivered project experience, corridor miles or client names',
     'The system has been run internally. Nothing has been delivered to a client under it. Add ' +
     'project references only once there are projects, and only with the numbers from the projects.'],
    ['"Certified", "compliant with", or a named accuracy standard',
     'No procedure in the MX60 document set has been adopted as Parametrix policy yet, and no ' +
     'external certification has been sought.'],
  ], [3200, CONTENT_W - 3200], { head: true }),

  h3('Two things worth keeping'),

  bullet([['The accuracy page is the strongest page. ', { bold: true }],
    'Competitors quote a number. Explaining why a single number is meaningless, and what you do ' +
    'instead, reads as competence to anyone technical enough to be choosing a surveyor.']),
  bullet([['"When mobile mapping is the wrong tool" is not a weakness. ', { bold: true }],
    'It is the paragraph a public agency remembers.']),

  h3('Before it is issued'),

  bullet('Master logo assets — EPS for print — from Templafy. The files in brand/ are 600 dpi ' +
         'extractions from the guide, fine for drafting, not masters.'),
  bullet('Licensed faces: Klinic Slab, Franklin Gothic URW, Freight Text Pro. Not held here, so ' +
         'this file falls back to the alternates the guide itself names (Rockwell, Franklin Gothic, ' +
         'Georgia). Restyle in the licensed faces.'),
  bullet('No tagline: the Brand Guide puts "client-facing document" in the Do Not Use Tagline ' +
         'column (p.12).'),
  bullet('Have someone technical read page 3 against reference/mx60-reference-data.csv before print.'),
];

// ---------- assemble -----------------------------------------------------

const doc = new Document({
  creator: 'Parametrix',
  numbering: {
    config: [{
      reference: 'px-bullets',
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: '\u2022', alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 200 } },
                 run: { color: RED, font: BODY, size: 21 } },
      }],
    }],
  },
  title: 'Mobile Mapping — capability brochure',
  description: 'Capability brochure, working draft for the marketing team.',
  styles: {
    default: {
      document: { run: { font: BODY, size: 21, color: CHARCOAL } },
    },
  },
  sections: [{
    properties: {
      page: { size: { width: LETTER.width, height: LETTER.height, orientation: PageOrientation.PORTRAIT },
              margin: MARGIN },
    },
    children: [
      ...cover, pageBreak(),
      ...whatItIs, pageBreak(),
      ...theSystem, pageBreak(),
      ...accuracy, pageBreak(),
      ...notes,
    ],
  }],
});

Packer.toBuffer(doc).then(b => {
  const out = 'marketing/Parametrix-Mobile-Mapping-Capability-Brochure.docx';
  fs.writeFileSync(out, b);
  console.log(`wrote ${out}  ${(b.length / 1024).toFixed(0)} KB`);
});
