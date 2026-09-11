# Appendix A — Office Processing Checklist

**Intake to delivery.** Tick as you go; the § column is where the detail is.

## A1 · Intake

| ☐ | | § |
|---|---|---|
| ☐ | Copy verified — file count and size, checksum if available | 2 |
| ☐ | `POS_1/raw/` present and non-empty | 2 |
| ☐ | Base station data present, if a local base was occupied | 2 |
| ☐ | Raw-data backup taken **before** any processing | 2 |
| ☐ | Field record received | 2 |
| ☐ | `Extcal.json` copied into the project record | 4 |
| ☐ | Mission Report run and archived; **calibration date established** | 4 |

## A2 · Project and import

| ☐ | | § |
|---|---|---|
| ☐ | Accuracy requirement stated in writing | 5 |
| ☐ | **CRS, datum, epoch, geoid set — before import** | 5 |
| ☐ | Grid or ground agreed in writing | 5 |
| ☐ | `.mxdb` imported; base `.YYo` imported (**not** `.YYn`/`.YYg`) | 7 |
| ☐ | Coordinate system matches the control network | 3 |
| ☐ | Covered distance consistent with the field record | 3 |
| ☐ | **Run count matches the field record** | 3 |
| ☐ | Active trajectory is SBET, not NAV | 3 |
| ☐ | Capture Devices lists the expected sensors | 3 |

## A3 · Trajectory

| ☐ | | § |
|---|---|---|
| ☐ | **Antenna model reads `Trimble 112735`** | 8 |
| ☐ | Computation mode set deliberately | 8 |
| ☐ | GAMS / DMI panes checked — dimmed means the sensor logged nothing | 8 |
| ☐ | **Backup SBET Next to MXDB enabled** | 8 |
| ☐ | Trajectory computed | 8 |
| ☐ | **RMS colouring reviewed and captured** | 10 |
| ☐ | SBET filename recorded — plain or `_frame` | 6 |

## A4 · Scans

| ☐ | | § |
|---|---|---|
| ☐ | One run generated first, filters checked | 11 |
| ☐ | Filters appropriate to the deliverable | 11 |
| ☐ | **Results of Scan Generation captured** | 11 |
| ☐ | Mission generated | 11 |
| ☐ | First look done — coverage, both lasers, voids | 12 |

## A5 · Registration

See **Appendix B**.

## A6 · QC and delivery

See **Appendix C** and **Appendix D**.

## A7 · Close-out

| ☐ | | § |
|---|---|---|
| ☐ | Record package complete — seven artefacts | 28 |
| ☐ | Cleanup, if run, followed the archive-first sequence | 29 |
| ☐ | Archive record written | 33 |
