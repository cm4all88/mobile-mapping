# 3. Checking Mission Information

Do this immediately after import (§7), before any processing. Seven checks, none taking a minute.

### Do

Open the mission properties and the **Mobile Mapping** node in Project Explorer and check:

| # | Check | Against |
|---|---|---|
| 1 | **Project coordinate system** | The control network and the client requirement |
| 2 | **Covered distance** | The field record |
| 3 | **Run count** | The field record |
| 4 | **Active trajectory** — is it SBET, not NAV? | Intent |
| 5 | **Capture Devices** — the sensors listed | The configuration: **Camera 3 Back Down**, **Camera 4 360°**, and the two lasers |
| 6 | **Base station data** present in the project | Whether you will process the trajectory in house |
| 7 | **Calibration state recorded** | §4 |

### Look at

The **Capture Devices** node, and the **Sbet** node under each run.

### Expect

The tree looks like this — **note that scans will hang off the trajectory, not off the run**:

```
Mobile Mapping
  └── <mission id>
        ├── Capture Devices     Camera 3 Back Down, Camera 4 360°, Laser Left, Laser Right
        └── Run 0, Run 1, Run 2 …
              └── Sbet          the imported trajectory
```

### Stop if

- **Run count is lower than the field record.** Data was lost in transfer. Do not process it —
  go back to the copy
- **A sensor is missing from Capture Devices.** It was disabled or it failed in the field. That is
  a field-record and re-collection question, not a processing one
- **Covered distance is materially short** of what the crew logged
- **The trajectory is NAV, not SBET,** and you have no recorded reason

> **Intake does not fix anything.** If a check fails, record it and raise it *(SOP §12.4)*. A
> processor who quietly corrects a coordinate system mismatch at intake has removed the evidence
> that field and office disagreed.

### Record

Each check, with its result. Anything that failed, and what was done.
