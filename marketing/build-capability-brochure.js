/**
 * Parametrix Mobile Mapping — client-facing capability brochure.
 *
 *   node marketing/build-capability-brochure.js
 *
 * Working file for the marketing team: they place imagery, restyle in the
 * licensed faces, and delete the internal pages. The words and the numbers are
 * the part that has been checked.
 *
 * SPECIFICATION AUTHORITY
 *   reference/mx60-reference-data.csv is the project's authority for numbers.
 *   The "system" page was re-verified line by line on 2026-09-19 against the
 *   primary source held in this repository:
 *
 *     022516737C_TrimbleMX60_SpecSheet_USL_0425_LR_SEC.pdf
 *     Trimble MX60 Spec Sheet, PN 022516-737C, 04/25
 *
 *   Every figure carries its source in a comment. Three findings from that
 *   check are written up on the internal pages; the heading figure in
 *   particular is conditional on GAMS and is labelled as such.
 *
 * Colours and faces from deliverables/_control/style/brand-tokens.css
 * (Parametrix Brand Guide v6, p.16, p.18). No tagline: the guide puts
 * "client-facing document" in the Do Not Use Tagline column (p.12).
 */
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  PageBreak, PageOrientation, LevelFormat, VerticalAlign,
} = require('docx');
const fs = require('fs');

const RED = 'EE3D24';
const CHARCOAL = '333333';
const GRAY = '676768';
const GRAY1 = 'B3B4B5';
const GRAY3 = 'E5E5E5';
const GRAY4 = 'F2F2F2';
const WHITE = 'FFFFFF';

const HEAD = 'Klinic Slab';
const BODY = 'Franklin Gothic Book';
const QUOTE = 'Freight Text Pro';

const LETTER = { width: 12240, height: 15840 };
const MARGIN = { top: 1080, right: 1080, bottom: 1080, left: 1080 };
const CW = LETTER.width - MARGIN.left - MARGIN.right; // 10080 dxa

const NONE = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE,
                    insideHorizontal: NONE, insideVertical: NONE };

// ---------- builders -----------------------------------------------------

const run = (t, f = {}, o = {}) => new TextRun({
  text: t, font: f.font ?? o.font ?? BODY, size: f.size ?? o.size ?? 21,
  color: f.color ?? o.color ?? CHARCOAL, bold: f.bold, italics: f.italics,
});

const rich = (parts, o = {}) => new Paragraph({
  alignment: o.align,
  spacing: { before: o.before ?? 0, after: o.after ?? 130, line: o.line ?? 280 },
  indent: o.indent,
  children: (Array.isArray(parts) ? parts : [parts]).map(x => {
    const [t, f] = Array.isArray(x) ? x : [x, {}];
    return run(t, f, o);
  }),
});

const p = (text, o = {}) => rich([[text, {}]], o);

const h1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1, keepNext: true,
  spacing: { before: 0, after: 60 },
  children: [run(text, { font: HEAD, size: 50, bold: true, color: RED })],
});

const titleRule = () => new Paragraph({
  spacing: { before: 0, after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: RED, space: 8 } },
  children: [run('', { size: 2 })],
});

const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2, keepNext: true, keepLines: true,
  spacing: { before: 300, after: 110 },
  children: [run(text, { font: HEAD, size: 28, bold: true, color: RED })],
});

const h3 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_3, keepNext: true, keepLines: true,
  spacing: { before: 220, after: 90 },
  children: [run(text, { size: 22, bold: true, color: CHARCOAL })],
});

/** The guide's one precedent for a marked-off block: a red left rule (p.16). */
const pullquote = (text) => new Paragraph({
  spacing: { before: 180, after: 200, line: 300 },
  indent: { left: 240 },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: RED, space: 12 } },
  children: [run(text, { font: QUOTE, size: 24, color: RED })],
});

const aside = (text) => new Paragraph({
  spacing: { before: 140, after: 150, line: 270 },
  indent: { left: 200 },
  border: { left: { style: BorderStyle.SINGLE, size: 10, color: GRAY3, space: 10 } },
  children: [run(text, { size: 19, color: GRAY })],
});

const bullet = (parts) => new Paragraph({
  numbering: { reference: 'px-bullets', level: 0 },
  spacing: { after: 90, line: 275 },
  children: (Array.isArray(parts) ? parts : [parts]).map(x => {
    const [t, f] = Array.isArray(x) ? x : [x, {}];
    return run(t, f);
  }),
});

const placeholder = (text) => new Paragraph({
  spacing: { before: 140, after: 140 },
  children: [run(text, { size: 18, color: GRAY, italics: true })],
});

/** A framed box standing in for a photograph marketing will drop in. */
const imageBox = (caption, heightDxa) => new Table({
  width: { size: CW, type: WidthType.DXA },
  columnWidths: [CW],
  borders: noBorders,
  rows: [new TableRow({
    height: { value: heightDxa, rule: 'atLeast' },
    children: [new TableCell({
      width: { size: CW, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: GRAY4, color: 'auto' },
      verticalAlign: VerticalAlign.CENTER,
      margins: { top: 200, bottom: 200, left: 200, right: 200 },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: GRAY1 },
        bottom: { style: BorderStyle.SINGLE, size: 4, color: GRAY1 },
        left: { style: BorderStyle.SINGLE, size: 4, color: GRAY1 },
        right: { style: BorderStyle.SINGLE, size: 4, color: GRAY1 },
      },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 0 },
        children: [run(caption, { size: 18, color: GRAY, italics: true })],
      })],
    })],
  })],
});

const pageBreak = () => new Paragraph({ children: [new PageBreak()] });
const spacer = (h = 200) => new Paragraph({ spacing: { after: h }, children: [run('', { size: 2 })] });

/** Two-column reference table. */
function refTable(rows, cols, opts = {}) {
  const w = cols ?? [3200, CW - 3200];
  const cell = (text, width, o = {}) => new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade, color: 'auto' } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: GRAY3 },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: GRAY3 },
      left: NONE, right: NONE,
    },
    children: [new Paragraph({
      spacing: { before: 0, after: 0, line: 255 },
      children: [run(text, { size: o.size ?? 19, color: o.color ?? CHARCOAL, bold: o.bold })],
    })],
  });
  return new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: w, borders: noBorders,
    rows: rows.map(([a, b], i) => new TableRow({
      children: [
        cell(a, w[0], { bold: true, shade: opts.head && i === 0 ? GRAY4 : undefined }),
        cell(b, w[1], { shade: opts.head && i === 0 ? GRAY4 : undefined }),
      ],
    })),
  });
}

/** Two columns of bullets side by side, for the long deliverable lists. */
function twoCol(left, right) {
  const half = Math.floor(CW / 2);
  const col = (items) => items.map(t => new Paragraph({
    numbering: { reference: 'px-bullets', level: 0 },
    spacing: { after: 70, line: 265 },
    children: [run(t, { size: 19 })],
  }));
  return new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: [half, CW - half], borders: noBorders,
    rows: [new TableRow({ children: [left, right].map((items, i) => new TableCell({
      width: { size: i === 0 ? half : CW - half, type: WidthType.DXA },
      margins: { top: 40, bottom: 40, left: 0, right: 180 },
      borders: noBorders,
      children: col(items),
    })) })],
  });
}

/** DRIVE → PROCESS → VERIFY → DELIVER. */
function workflowStrip() {
  const stages = [
    ['1', 'DRIVE', 'MX60 LiDAR, 360° imagery and GNSS/inertial collection along the corridor'],
    ['2', 'PROCESS', 'Trajectory, point cloud, imagery and feature extraction'],
    ['3', 'VERIFY', 'Survey control, independent check points and targeted conventional observations'],
    ['4', 'DELIVER', 'CAD, surfaces, inventories, clearance reports, pavement analysis, ADA design mapping'],
  ];
  const w = Math.floor(CW / 4);
  const widths = [w, w, w, CW - 3 * w];
  return new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: widths, borders: noBorders,
    rows: [new TableRow({
      children: stages.map(([n, title, body], i) => new TableCell({
        width: { size: widths[i], type: WidthType.DXA },
        margins: { top: 120, bottom: 140, left: 130, right: 130 },
        borders: {
          top: { style: BorderStyle.SINGLE, size: 18, color: RED },
          bottom: NONE,
          left: i === 0 ? NONE : { style: BorderStyle.SINGLE, size: 4, color: GRAY3 },
          right: NONE,
        },
        children: [
          new Paragraph({
            spacing: { before: 0, after: 40 },
            children: [run(`${n}  ${title}`, { font: HEAD, size: 20, bold: true, color: RED })],
          }),
          new Paragraph({
            spacing: { before: 0, after: 0, line: 250 },
            children: [run(body, { size: 17, color: CHARCOAL })],
          }),
        ],
      })),
    })],
  });
}

// ---------- 1 · cover ----------------------------------------------------

const cover = [
  spacer(300),
  placeholder('[ Parametrix logo — charcoal and red, minimum 1 inch wide, clear space on all four sides at least the height of the right side of the x. Master EPS from Templafy. Brand Guide pp.10–14. ]'),
  spacer(500),
  new Paragraph({
    spacing: { after: 60 },
    children: [run('MOBILE MAPPING', { font: HEAD, size: 74, bold: true, color: RED })],
  }),
  new Paragraph({
    spacing: { after: 320 },
    children: [run('Corridor survey at traffic speed', { size: 32, color: CHARCOAL })],
  }),
  imageBox('[ Cover image — the MX60 collecting on a live corridor, or a finished CAD deliverable over the point cloud it came from. Full bleed where the layout allows. ]', 3200),
  spacer(320),
  new Paragraph({
    spacing: { after: 200, line: 340 },
    border: { top: { style: BorderStyle.SINGLE, size: 12, color: RED, space: 14 } },
    children: [run('', { size: 2 })],
  }),
  rich([
    ['Parametrix delivers a finished survey product, not a point cloud.', { bold: true, size: 25 }],
    ['  Our Trimble MX60 Premium captures an entire corridor or paved site in a single pass, and we ' +
     'turn it into the base mapping, surfaces, inventories and reports your project actually runs on.',
     { size: 25 }],
  ], { line: 350, after: 200 }),
  spacer(500),
  placeholder('[ Office · address · phone · email — marketing to complete ]'),
];

// ---------- 2 · why mobile mapping ---------------------------------------

const why = [
  h1('Why mobile mapping'),
  titleRule(),

  p('A conventional corridor survey puts people on the ground, in or beside live traffic, for as ' +
    'long as the work takes. Mobile mapping changes where the measurement happens. The instrument ' +
    'travels with traffic, and the corridor is measured in the time it takes to drive it.'),

  pullquote('One of the greatest safety exposures in corridor surveying is working on foot near ' +
            'live traffic. Mobile mapping moves most of that work into the vehicle, and then into ' +
            'the office.'),

  h2('What it changes'),

  refTable([
    ['Reduced field exposure',
     'During mobile collection the survey crew remains in the vehicle, significantly reducing time ' +
     'spent on foot in or adjacent to live traffic. Control, monuments, obscured features and ' +
     'targeted verification may still require conventional observations'],
    ['Reduced traffic disruption',
     'In many corridor applications the MX60 can collect with live traffic and without a dedicated ' +
     'survey lane closure. Where traffic control is still required, the exposure is usually shorter'],
    ['Efficient corridor collection',
     'Long corridors and large paved areas are captured continuously rather than set-up by set-up, ' +
     'which is where the schedule advantage comes from'],
    ['A complete digital record',
     'The full visible environment is measured and photographed, dated, and tied to the project ' +
     'coordinate system — not only the features on the original pick list'],
    ['Work the data in the office',
     'Features are extracted from a measured dataset at a desk, with the imagery alongside, rather ' +
     'than from notes taken at the roadside'],
    ['Faster repeat collection',
     'Revisiting a corridor may require another drive rather than another full conventional survey ' +
     'effort'],
  ], [2700, CW - 2700]),

  h2('Collect once, answer later'),

  p('Because the corridor is captured comprehensively, additional visible features can often be ' +
    'extracted later without returning to the field. A designer who asks in month four for the ' +
    'driveway aprons, the pole attachments or the drainage grates that were never in the original ' +
    'scope is usually asking a question the dataset can already answer.'),

  p('One coordinated collection can therefore support several disciplines at once — existing ' +
    'conditions, ADA design, pavement assessment, drainage and utility surface features, signs and ' +
    'markings, clearance, and the design questions nobody has asked yet. That is where the economic ' +
    'argument sits: not in the speed of one survey, but in how many times the same collection gets ' +
    'used.'),

  aside('Not every future question can be answered from an existing dataset. Features hidden at ' +
        'the time of collection, anything below the surface, and measurements needing a precision ' +
        'the method does not carry will still require field work.'),
];

// ---------- 3 · what you receive -----------------------------------------

const receive = [
  h1('What you receive'),
  titleRule(),

  rich([['A finished survey product, not a point cloud.',
         { bold: true, size: 25, color: CHARCOAL }]], { after: 140 }),

  p('The MX60, the imagery, the trajectory, the point cloud, the control and the processing are the ' +
    'means. What you are buying is the drawing, the surface, the inventory or the report — in the ' +
    'format your workflow already uses. You do not need to hold, process or understand raw LiDAR to ' +
    'use what we deliver. If you want the cloud and the imagery as well, they are yours.'),

  spacer(140),
  workflowStrip(),
  spacer(260),

  h2('Deliverables'),

  refTable([
    ['Existing conditions base mapping',
     'Planimetric features, edge of pavement, curb and gutter, striping, drainage and utility ' +
     'surface features, signing and roadside furniture — drafted to your CAD standard'],
    ['Surfaces and terrain',
     'Digital terrain models, breaklines, contours, cross sections and pavement surfaces'],
    ['Asset inventories',
     'Signs, pavement markings, drainage structures, barrier, lighting, poles and other corridor ' +
     'assets — located, attributed, and linked to the imagery showing the feature and its condition'],
    ['ADA and sidewalk design mapping',
     'Curb, gutter, sidewalk, ramp and landing geometry with running and cross slope information, ' +
     'for accessibility evaluation and replacement design'],
    ['Pavement analysis',
     'Roughness, surface condition, rutting and deformation, cross slope and distress mapping, from ' +
     'the same collection as the base mapping'],
    ['Clearance reports',
     'Vertical and horizontal clearance at bridges and overhead structures, clearance envelopes and ' +
     'CAD sections'],
    ['Monitoring and change reports',
     'Where a corridor has moved, settled or eroded between surveys, and by how much'],
    ['Survey record and QC documentation',
     'The control used, the independent check point results and their residuals, and the coordinate ' +
     'system, datum and epoch the deliverable sits on'],
  ], [3000, CW - 3000]),

  aside('Mobile mapping is not simply a faster scanner. It is a survey workflow — collection, ' +
        'control, processing, verification and production — that turns a corridor into ' +
        'engineering-ready deliverables.'),
];

// ---------- 4 · where it is used, part one -------------------------------

const usesA = [
  h1('Where it is used'),
  titleRule(),

  h2('Transportation corridors'),

  p('Base mapping for design, widening, resurfacing, reconstruction and asset management on state ' +
    'routes, arterials, city streets and interchanges. Complex geometry is captured in passes ' +
    'rather than in set-ups, and the whole cross section comes back together — pavement, curb, ' +
    'sidewalk, drainage, signing, illumination and the roadside.'),

  p('The same method serves rail and transit corridors, where measurement alongside an operating ' +
    'alignment is captured without putting a crew on foot in the corridor.'),

  h2('ADA curb ramp and sidewalk design surveys'),

  p('Capture the full intersection or corridor in a single mobile mapping survey. The MX60 records ' +
    'curb, gutter, roadway, sidewalk, ramp, landing, striping, drainage and surrounding features, ' +
    'creating a dense existing conditions dataset for accessibility evaluation and replacement ' +
    'design — without a field crew collecting every visible feature individually.'),

  h3('What we deliver on ramp and sidewalk projects'),

  twoCol(
    ['Existing conditions base mapping',
     'Detailed curb, gutter and sidewalk geometry',
     'Ramp and landing surfaces',
     'Running and cross slope information',
     'Roadway and gutter transitions'],
    ['Drainage structures',
     'Utility structures and surface features',
     'Street level imagery tied to the survey',
     'CAD surfaces and design-ready mapping',
     'Targeted conventional verification where required'],
  ),

  h3('Sidewalks, beyond the ramps'),

  p('The same dataset supports sidewalk assessment along the corridor: width and constrained clear ' +
    'width, cross slope and running grade, driveway crossings, vertical offsets and potential trip ' +
    'hazards, curb geometry, obstructions, poles and street furniture, surface deterioration, and ' +
    'missing segments. At corridor scale this supports accessibility screening and curb ramp ' +
    'inventories; at project scale it supports design.'),

  h3('How the accuracy question is handled'),

  p('Agencies may verify constructed or existing slopes by conventional leveling, so we do not ask ' +
    'mobile mapping to carry every controlling elevation. Mobile mapping captures the complete ' +
    'existing environment; targeted conventional survey establishes or verifies the critical design ' +
    'elevations. Point cloud analysis supports ramp geometry, running slope, cross slope, landing ' +
    'geometry, roadway transitions, identification of vertical discontinuities and ramp assessment ' +
    'reporting — as measurement and screening a designer then works from.'),

  aside('Point cloud analysis supports an accessibility assessment. It does not determine ' +
        'compliance, and it does not resolve jurisdiction-specific design requirements. Those ' +
        'remain matters of engineering judgement against the governing standard.'),
];

// ---------- 5 · where it is used, part two -------------------------------

const usesB = [
  h2('Pavement assessment'),

  p('The same mobile mapping collection can support pavement and ride quality analysis in addition ' +
    'to conventional base mapping — so a pavement question and a design question can be answered ' +
    'from one mobilisation.'),

  refTable([
    ['Roadway pavement roughness',
     'International Roughness Index derived from the mobile mapping surface, with segmented results ' +
     'identifying problem areas along the route'],
    ['Airfield pavement roughness',
     'Boeing Bump Index and International Roughness Index derived from dense runway surface scans ' +
     'along the centerline and the left and right wheel paths, evaluating bump locations by the ' +
     'Boeing Bump methodology'],
    ['Surface condition and distress',
     'Pavement distress mapping and surface condition assessment across the corridor'],
    ['Rutting and deformation',
     'Measured from the pavement surface rather than estimated from spot cross sections'],
    ['Cross slope',
     'Continuous along the corridor, from the same surface'],
    ['Surface models and profiles',
     'Pavement surfaces and longitudinal or transverse profiles for design and analysis'],
    ['Repeat deterioration surveys',
     'The same route collected again, with the change between surveys reported'],
  ], [3000, CW - 3000]),

  p('Airfield pavement roughness can therefore be evaluated from a dense mobile mapping surface ' +
    'rather than relying solely on sparse conventional observations. Roughness indices and distress ' +
    'mapping differ in how much of the work is computed and how much is reviewed; the method and the ' +
    'level of review are set per project.'),

  h2('Airports'),

  p('Runways, taxiways, aprons and service roads. Applications include existing conditions mapping, ' +
    'pavement surface modeling, pavement roughness, markings, signage, drainage, clearance, asset ' +
    'inventory and construction documentation.'),

  p('Airside collection is planned and coordinated with airport operations. The advantage is not ' +
    'that coordination becomes unnecessary — it is that a drive takes far less time inside a ' +
    'restricted operational area than a conventional survey of the same pavement, which shortens ' +
    'the window that has to be arranged.'),
];

// ---------- 6 · where it is used, part three -----------------------------

const usesC = [
  h2('Bridge and overhead clearance'),

  p('Measure vertical and horizontal clearance across an entire corridor or route from one ' +
    'coordinated dataset, instead of setting up beneath each individual structure. Deliverables ' +
    'include minimum clearance, the clearance envelope, bridge underside mapping, oversize load ' +
    'route information, CAD sections, clearance reports, and repeat monitoring where appropriate.'),

  h2('Utilities and right of way'),

  p('Above-ground utilities, poles and attachments, vaults, lids, surface features and the ' +
    'surrounding right-of-way improvements are captured as part of the corridor dataset, with the ' +
    'imagery that shows each one. For utility engineering that gives a complete surface picture of ' +
    'the corridor from a single collection.'),

  aside('Mobile mapping records visible above-ground features and surface evidence. It does not ' +
        'locate underground utilities. Right-of-way boundary establishment depends on appropriate ' +
        'survey evidence and conventional boundary surveying.'),

  h2('Ports, yards and campuses'),

  p('Large paved facilities are where continuous collection pays off most. A single collection can ' +
    'support existing conditions, pavement surfaces, asset inventory, clearance, striping, drainage, ' +
    'utility surface features, construction planning and repeat condition surveys.'),

  h2('Repeat survey and monitoring'),

  p('Drive the same corridor twice and the difference between the two datasets is a measurement in ' +
    'its own right — practical over lengths and areas that would not justify instrumented ' +
    'monitoring.'),

  twoCol(
    ['Settlement and subsidence',
     'Approach slabs and transition zones',
     'Embankments and fill areas',
     'Slope movement',
     'Erosion'],
    ['Pavement deterioration',
     'Construction progress',
     'As-built conformance',
     'Post-event assessment',
     'Repeat condition surveys'],
  ),

  aside('Repeat-survey monitoring finds and measures change at corridor scale. It does not replace ' +
        'millimetre-level instrumentation or precise leveling. Where a millimetre-level answer is ' +
        'required at a known point, use the appropriate precision monitoring method — and we will ' +
        'say so.'),
];

// ---------- 7 · accuracy -------------------------------------------------

const accuracy = [
  h1('How accuracy is established'),
  titleRule(),

  pullquote('There is no single accuracy figure for every mobile mapping deliverable. A firm that ' +
            'quotes you one before asking about your corridor is quoting a brochure, not a project.'),

  p('Every measured point combines two things: the range and angle measured by the scanner, and the ' +
    'position and orientation of the vehicle at that instant. Scanner performance is highly ' +
    'consistent. Trajectory quality is not — it changes along the corridor with GNSS conditions and ' +
    'the surrounding environment, between open highway, tree canopy, an underpass and an urban ' +
    'canyon. That is why an instrument specification is not a project accuracy, and why we will not ' +
    'present one as the other.'),

  h2('What we do instead'),

  bullet([['Agree the accuracy requirement before collection. ', { bold: true }],
    'It drives the control design, the number of passes and the driving pattern — none of which can ' +
    'be fixed afterwards.']),
  bullet([['Design control appropriate to that requirement. ', { bold: true }],
    'Established conventionally, and bracketing the extent of the work.']),
  bullet([['Fit the trajectory to surveyed control. ', { bold: true }],
    'The corridor is brought onto your coordinate system, datum and epoch, and the deliverable ' +
    'states which.']),
  bullet([['Use independent check points, kept out of the adjustment. ', { bold: true }],
    'A point that helped compute the answer cannot test it. Points held independent can.']),
  bullet([['Report the residuals. ', { bold: true }],
    'The check results are part of the deliverable, not a number that stays in the office.']),
  bullet([['Evaluate quality along the corridor. ', { bold: true }],
    'A single project-wide average hides the local stretch that matters to your design.']),

  h2('Mobile mapping and conventional survey, together'),

  p('The most efficient survey is often a combination. Mobile mapping captures the complete corridor ' +
    'or site; conventional observations establish control and monuments, reach obscured features, ' +
    'set critical elevations and provide targeted verification. That is particularly true for ADA ' +
    'design, utility engineering, right-of-way work, airport pavement, high accuracy deformation ' +
    'work, and anywhere the vehicle cannot see the feature the project needs.'),

  p('Parametrix runs both. Deciding which parts of a project belong to which method — and saying so ' +
    'before the work starts — is the part that protects the schedule and the deliverable.'),
];

// ---------- 8 · the system -----------------------------------------------

const system = [
  h1('The system'),
  titleRule(),

  rich([
    ['Trimble MX60 Premium', { bold: true }],
    ' — the top of the three MX60 configurations. The figures below are Trimble’s published ' +
    'specifications for the equipment, under the conditions Trimble states. They describe the ' +
    'instrument. Project accuracy is established as set out on the previous page.',
  ], { line: 290, after: 200 }),

  h3('Laser scanning'),
  refTable([
    ['Scanners', 'Two, time-of-flight'],                                                      // UG Rev B
    ['Effective measurement rate', '1,000,000 or 2,000,000 points per second, selectable — system total'], // spec sheet p.2
    ['Scan speed', '240 or 400 profiles per second, selectable — system total'],               // spec sheet p.2; UG p.54 gives 120/200 per scanner
    ['Maximum range', '150 m at 1,000 kHz · 120 m at 2,000 kHz, target reflectivity above 80%'], // spec sheet p.2
    ['Minimum range', '0.6 m'],                                                                // spec sheet p.2
    ['Accuracy · precision', '2 mm · 2.5 mm at 30 m'],                                         // spec sheet p.2
    ['Field of view', 'Full 360°'],                                                            // spec sheet p.2
    ['Laser class', 'Class 1, eye safe'],                                                      // spec sheet p.2
  ], [3000, CW - 3000]),
  p('Range figures are stated on a matte surface at normal angle of incidence. Working distance on a ' +
    'corridor is shorter.', { size: 17, color: GRAY, after: 40 }),

  h3('Imaging'),
  refTable([
    ['Spherical camera', '72 MP, 90% of the full sphere, by distance or by time at up to 10 fps'], // spec sheet p.2
    ['Rear/down camera', '12 MP, H 82.9° × V 65.9°, by distance or by time at up to 9 fps'],       // UG Rev B p.54 (CONFLICT-004: prefer the UG)
  ], [3000, CW - 3000]),

  h3('Positioning'),
  refTable([
    ['Integration', 'Trimble GNSS-inertial, Applanix IN-Fusion+'],        // UG Rev B
    ['Roll and pitch', '0.0025° — Premium'],                              // spec sheet p.2
    ['Heading', '0.015°, with GAMS on a 2 m baseline'],                   // spec sheet p.2 fn.6
    ['Position after a 60-second GNSS outage', '0.10 m horizontal · 0.07 m vertical — Premium'], // spec sheet p.2
  ], [3000, CW - 3000]),
  p('Positioning figures are measured in a controlled test area under Trimble conditions and ' +
    'procedures. They are not a statement of delivered project accuracy.',
    { size: 17, color: GRAY, after: 40 }),

  h3('Collection and storage'),
  refTable([
    ['Recommended maximum speed, system operating', '80 km/h (50 mph)'],  // UG Rev B
    ['Maximum speed', '110 km/h (68 mph)'],                               // spec sheet p.3
    ['Onboard storage', '2 × 4 TB removable SSD'],                        // spec sheet p.3
    ['Operating temperature', '−10 °C to +50 °C (14 °F to 122 °F)'], // spec sheet p.3
  ], [3000, CW - 3000]),

  p('Source: Trimble MX60 Spec Sheet, PN 022516-737C (04/25), and the Trimble MX60 User Guide Rev B. ' +
    'Specifications are subject to change without notice.', { size: 17, color: GRAY }),
];

// ---------- 9 · closing --------------------------------------------------

const closing = [
  h1('Start a conversation'),
  titleRule(),

  p('A single mobile mapping collection can support multiple engineering, survey, asset and ' +
    'condition assessment needs across the same corridor. The most useful first conversation is ' +
    'usually about the deliverable rather than the technology: what you need to design, inventory or ' +
    'assess, to what accuracy, and by when. We will tell you which parts of that are mobile mapping ' +
    'work, which parts are conventional survey, and how the two fit together.'),

  spacer(180),
  imageBox('[ Closing image — a delivered product: CAD base mapping, an ADA intersection, a pavement ' +
           'surface or a clearance section. ]', 2600),
  spacer(300),

  refTable([
    ['We are a good fit when',
     'The work runs along a corridor or across a large paved area · putting people on the ground is ' +
     'slow, unsafe or disruptive · several disciplines need the same site · the corridor will be ' +
     'revisited · the deliverable is a drawing, surface, inventory or report rather than raw data'],
    ['Talk to us early when',
     'The accuracy requirement is demanding · the schedule is tight · traffic control is expensive or ' +
     'hard to obtain · the site is operationally restricted, such as airside'],
  ], [2700, CW - 2700]),

  spacer(360),
  placeholder('[ Contact block — name, title, phone, email, office. Marketing to complete. ]'),
  spacer(180),
  placeholder('[ Parametrix logo — knockout version if this page is set on a dark or image ground. ]'),
];

// ---------- internal pages ----------------------------------------------

const stopBanner = () => new Paragraph({
  spacing: { after: 160 },
  shading: { type: ShadingType.CLEAR, fill: RED, color: 'auto' },
  children: [run('  INTERNAL — REMOVE BEFORE CLIENT ISSUE  ',
                 { font: HEAD, size: 28, bold: true, color: WHITE })],
});

const internal1 = [
  stopBanner(),
  h2('Notes for the marketing team'),

  h3('One specification is in dispute — resolve before issue'),

  p('The revision request asked for the scanner precision to be changed from 2.5 mm at 30 m to a ' +
    'laser precision of 1.5 mm. That change has not been made, and here is why.'),

  p('Both controlled Trimble documents held here give the same figure, and neither gives 1.5 mm:'),

  refTable([
    ['Trimble MX60 Spec Sheet, PN 022516-737C (04/25), SCANNING table',
     '"Accuracy/Precision  2 mm, 2.5 mm @ 30 m"'],
    ['Trimble MX60 User Guide Rev B (May 2025), p.54',
     '"Accuracy 2 mm · Precision 2.5 mm @ 30 m"'],
  ], [4200, CW - 4200]),

  p('The spec sheet we hold is revision C; the one circulating on distributor sites is 737B, dated ' +
    '10/24, so ours is the newer. The Trimble Geospatial comparison page cited as the source for ' +
    '1.5 mm could not be reached from the build environment, but it is a web comparison table rather ' +
    'than a controlled document, and it is contradicted by both of the ones that are.'),

  p('The page therefore carries 2.5 mm at 30 m. If 1.5 mm is correct it will appear in a revision of ' +
    'the spec sheet or the user guide, and that revision is what should change this line — not the ' +
    'comparison page. This number will be read by agency surveyors.'),

  h3('Two further findings from the same verification pass'),

  refTable([
    ['Heading 0.015° is conditional',
     'Spec sheet footnote 6 states the heading figure applies "With GAMS, 2 m baseline." Whether this ' +
     'system carries GAMS is still open (register D-2). The page prints the condition alongside the ' +
     'figure rather than the figure alone.'],
    ['Trimble\u2019s own two documents disagree on small numbers',
     'The user guide gives the down camera field of view as H 82.9° and the Core focal length as ' +
     '4.40 mm; the spec sheet gives H 82.0° and 4.44 mm. The register already records this as ' +
     'CONFLICT-004 and sets the rule: prefer the user guide, as the revision-tracked controlled ' +
     'document. The page follows that rule. Nothing needs correcting.'],
  ], [2900, CW - 2900]),

];

const internal1b = [
  stopBanner(),
  h3('The claims that must not be added'),

  refTable([
    ['Do not add', 'Why'],
    ['A universal delivered accuracy — "1 cm mobile mapping", "survey-grade to 0.02 ft"',
     'What constitutes an acceptable result has not been decided (D-13) and the control design that ' +
     'would support it has not been specified (D-16). Accuracy is a per-project statement.'],
    ['A Trimble instrument specification presented as project accuracy',
     'The two are different quantities. The accuracy page exists to make that distinction, and it is ' +
     'a differentiator — do not undo it on another page.'],
    ['A delivered Boeing Bump Index or IRI project',
     'Parametrix has not yet completed a client-delivered BBI project. The capability is real and is ' +
     'in the equipment and the software. Sell the capability, not a record.'],
    ['Any other claim of project experience that does not exist',
     'No corridor miles, no client names, no case studies until there are projects and the client has ' +
     'agreed to be named.'],
    ['"MX60 determines ADA compliance", or "replaces leveling"',
     'Point cloud analysis supports assessment. Compliance is determined against the governing ' +
     'standard by engineering judgement, and agencies may verify slopes by conventional leveling.'],
    ['"Without closing the runway", or any unqualified airside claim',
     'Airside collection is coordinated with airport operations. The defensible point is a shorter ' +
     'window inside the restricted area, not the absence of coordination.'],
  ], [2900, CW - 2900], { head: true }),
];

const internal2 = [
  stopBanner(),
  h2('Before quoting specialty work'),

  refTable([
    ['Confirm the control and validation scheme',
     'Before quoting high accuracy work, establish how the mobile mapping elevations will be proven ' +
     'and against what. Agreed with the client before collection, not after.'],
    ['Confirm owner and reviewing authority requirements',
     'For specialty deliverables — airfield roughness, ADA design, clearance for load posting — ask ' +
     'the receiving authority what it will accept from a mobile-mapping-derived product. Do not ' +
     'assume.'],
    ['Validate new TBC workflows internally first',
     'A command existing in Trimble Business Center is not the same as an established Parametrix ' +
     'production workflow. Run it, document it, then sell it.'],
  ], [2900, CW - 2900]),

  h2('Recommended capability validation'),

  h3('ADA and sidewalk — the highest priority'),

  p('Clients such as SDOT and Seattle City Light may independently verify ramp slopes, so the ' +
    'agreement between our derived slopes and level observations needs to be known before it is ' +
    'discovered on a live project.'),

  bullet('Select several real intersections and collect them with the MX60.'),
  bullet('Run the TBC ramp analysis.'),
  bullet('Establish precise conventional vertical control, and level critical ramp and landing points.'),
  bullet('Compare MX60-derived slopes and elevations against the independent level observations.'),
  bullet('Determine where mobile mapping is sufficient on its own and where conventional observations ' +
         'should remain a standard part of the workflow.'),

  h3('Boeing Bump and pavement'),

  bullet('Use an appropriate paved test area and run the complete TBC Boeing Bump workflow.'),
  bullet('Run IRI on the same surface.'),
  bullet('Compare the mobile mapping surface and profile against independent survey observations.'),
  bullet('Document the procedure, the control requirements and the repeatability before Parametrix ' +
         'markets BBI as an established delivered service.'),

  h3('Repeatability'),

  bullet('Drive the same test corridor several times.'),
  bullet('Compare horizontal features, pavement elevations, hard surfaces, known check points and ' +
         'repeated extracted features between runs.'),
  bullet('Use the spread to set realistic internal expectations by project type — which is what turns ' +
         'the accuracy page from a position into a number we can stand behind.'),

];

const internal3 = [
  stopBanner(),
  h3('Production notes'),

  bullet('Master logo assets — EPS for print — from Templafy. The files in brand/ are 600 dpi ' +
         'extractions from the guide: fine for drafting, not masters.'),
  bullet('Licensed faces are Klinic Slab, Franklin Gothic URW and Freight Text Pro. They are not held ' +
         'here, so this file falls back to the alternates the guide itself names — Rockwell, Franklin ' +
         'Gothic, Georgia. Restyle in the licensed faces.'),
  bullet('No tagline: the Brand Guide puts "client-facing document" in the Do Not Use Tagline column, ' +
         'p.12.'),
  bullet('Image boxes are placeholders. Photography selection guidance is Brand Guide p.20.'),
  bullet('Have a surveyor read The system against the spec sheet before anything is printed.'),
];

// ---------- assemble -----------------------------------------------------

const doc = new Document({
  creator: 'Parametrix',
  title: 'Mobile Mapping — capability brochure',
  description: 'Client-facing capability brochure, working draft for the marketing team.',
  numbering: {
    config: [{
      reference: 'px-bullets',
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 340, hanging: 190 } },
                 run: { color: RED, font: BODY, size: 21 } },
      }],
    }],
  },
  styles: { default: { document: { run: { font: BODY, size: 21, color: CHARCOAL } } } },
  sections: [{
    properties: {
      page: { size: { width: LETTER.width, height: LETTER.height, orientation: PageOrientation.PORTRAIT },
              margin: MARGIN },
    },
    children: [
      ...cover, pageBreak(),
      ...why, pageBreak(),
      ...receive, pageBreak(),
      ...usesA, pageBreak(),
      ...usesB, pageBreak(),
      ...usesC, pageBreak(),
      ...accuracy, pageBreak(),
      ...system, pageBreak(),
      ...closing, pageBreak(),
      ...internal1, pageBreak(),
      ...internal1b, pageBreak(),
      ...internal2, pageBreak(),
      ...internal3,
    ],
  }],
});

Packer.toBuffer(doc).then(b => {
  const out = 'marketing/Parametrix-Mobile-Mapping-Capability-Brochure.docx';
  fs.writeFileSync(out, b);
  console.log(`wrote ${out}  ${(b.length / 1024).toFixed(0)} KB`);
});
