# 11. DATA HANDLING

The data on those two SSDs cost a day of crew time and cannot be re-collected without
another mobilisation. Treat it accordingly.

## 11.1 What is on the disks

| Disk | Contents |
|---|---|
| **SSD 1** (upper) | Mission database files · mission log file · **Mission Report** · **navigation data** · laser 1 and 2 data · panoramic camera data |
| **SSD 2** (lower) | Oblique camera data — on the MX60, the back-down camera |

*(TMI UG Rev L, p.44; QSG Rev B, p.8)*

> **IMPORTANT**
>
> **Both disks are one dataset.** SSD 1 holds the navigation data — without it there is no
> trajectory, and without a trajectory everything on SSD 2 is a folder of ungeoreferenced
> photographs. Never separate them.

**Mission directory naming** is automatic:

```
TMX60<serial number>-<mission ID> - <MissionName>
```

The mission ID comes from an increasing counter. Mission name and area name are also saved
as attributes inside the mission database file *(TMI UG Rev L, p.44)*.

A **system log file** is written automatically to removable Disk 1 during shutdown
*(TMI UG Rev L, p.43)*.

## 11.2 Removing the disks

> **CAUTION**
>
> **Never connect the USB cable while an exchangeable data disk is inside the Control
> Unit.** Remove the disk first. *(MX60 UG Rev B, p.10)*

1. Confirm the system is fully shut down — power button light out
2. **Unlock both SSDs** with the provided key
3. Remove both
4. Keep them together, labelled with the mission

## 11.3 Offloading

Use the **MX SCAN Data Carrier Dock** — two are supplied.

1. Connect the Dock's AC adapter to power, and the other end to the rear of the Dock
2. Connect the **USB 3** cable from the rear of the Dock to a USB 3 port on the office
   computer
3. Insert the Exchangeable Data Disk into the Dock
4. **Lock the disk with the key and turn 90° clockwise** to secure it
5. Power on the Dock
6. Download the mission

*(MX60 UG Rev B, p.24; QSG Rev B, p.13)*

> **FIELD TIP**
>
> Two Docks are supplied for a reason — you can offload both disks at once, which roughly
> halves the wait on a full day's data. With 2 × 4 TB of capacity, this is not a quick copy.

## 11.4 Verify before you do anything else

> **IMPORTANT**
>
> A copy that ran without an error message is not a verified copy. Confirm the data is
> genuinely readable **before** the disks go back in the vehicle for tomorrow.

| ☐ | Check |
|---|---|
| ☐ | Mission folder present, correctly named |
| ☐ | **Navigation data present on the SSD 1 copy** |
| ☐ | Laser data present for both scanners |
| ☐ | Panoramic imagery present |
| ☐ | Back-down camera imagery present from the SSD 2 copy |
| ☐ | Mission Report and mission log copied |
| ☐ | System log file copied |
| ☐ | File count and total size match the source |
| ☐ | Project opens in TBC from the `mxdb` database file |

> **CAUTION**
>
> **Do not format or reuse the SSDs until the transfer is verified and backed up.** The
> Quick Start Guide's office procedure is "back up the data" and *then* "prepare SSDs for
> the next mission" *(QSG Rev B, p.15)* — in that order. Reversing it has ended projects.

## 11.5 Back up before you work

Once verified, back up **before** any processing begins.

**The principle:** the raw mission data is the only irreplaceable thing you have. Every
derived product — trajectory, point cloud, colorized cloud, extracted features — can be
regenerated from it. It cannot be regenerated from them.

**Work from a copy.** Never process against the only instance of the raw data.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the Parametrix backup standard for mobile mapping data: how many copies, on
> what media, in which locations, and how long they are retained.
>
> *Recommended practice:* three copies on two media types with one off-site or in cloud
> storage. Raw mission data retained for the life of the project plus the firm's records
> retention period — the point cloud's long-term value depends on the raw data still
> existing. NCHRP's synthesis documents state DOTs treating lidar data as a long-term
> asset with governance attached, not as project scratch *(NCHRP 2024, Ch.3)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Determine the standard MX60 raw data storage location and project folder structure.
>
> *Recommended practice:* one project folder per job, containing `01-raw` (untouched
> mission directories exactly as offloaded), `02-trajectory`, `03-pointcloud`,
> `04-imagery`, `05-control`, `06-qc`, `07-deliverables`, and `08-field-records` (field
> protocol, photos, notes). Make `01-raw` read-only as soon as it is verified.

> **PARAMETRIX DECISION REQUIRED**
>
> Set the project and mission naming convention.
>
> *Recommended practice:* let TMI's automatic directory naming stand — it encodes system
> serial and mission ID, which is exactly what you want for traceability — and carry the
> Parametrix project number in the **mission name** field you type at mission start. That
> puts the project number inside the mission database as an attribute, where it travels
> with the data.

## 11.6 Never delete source data prematurely

> **CAUTION**
>
> Do not delete raw mission data because processing succeeded, because the deliverable
> shipped, or because storage is short.

Reasons this rule exists:

- Processing parameters change. A trajectory reprocessed with better base station data,
  or a cloud re-registered against new control, can be materially better
- Deliverables get revised. The client asks for something nobody extracted the first time
- Boresight calibration improves. A new JSON file can be imported and prior missions
  reprocessed *(TMI UG Rev L, p.18)*
- **The point cloud's long-term value is the whole argument for mobile mapping.** Someone
  measuring something in three years that nobody thought to record is only possible while
  the source exists

> **PARAMETRIX DECISION REQUIRED**
>
> Define the retention and archive policy, including who may authorise deletion of raw
> mission data and after what period.
>
> *Recommended practice:* raw mission data is never deleted by the project team.
> Deletion requires sign-off by the survey technology group owner, and only after the
> retention period has elapsed.

## 11.7 Field records

Trimble requires a field protocol recording, at minimum:

- **Order of runs**
- **Direction of runs**
- **Date**
- **Mission**
- **System serial number**

*(QSG Rev B, p.14)*

Add to that everything from the mission that a processor or reviewer would want:

| Field | Why |
|---|---|
| Operator and driver names | Accountability, and who to ask |
| Vehicle | Ties to the Vehicle Preset |
| **Installation height used** | Affects dust filter, lateral range limit, imagery |
| **Vehicle Preset and Capture Preset names** | Reproducibility |
| Initialization location and time, both ends | Trajectory quality investigation |
| Weather and surface conditions | Explains point cloud and imagery anomalies |
| Events during collection | Occlusions, NAV degradation, traffic incidents |
| Control occupied / base station used | Processing input |

> **FIELD TIP**
>
> TMI's **Comments** feature time-tags notes into the mission database
> *(TMI UG Rev L, p.9)*. Use it *and* the paper protocol. The comments travel with the
> data; the protocol survives if the data does not.

**Also worth exporting:** TMI can download **Mission Coverage as a `.kmz`** containing the
trajectory *(TMI UG Rev L, p.14)*. That is a lightweight, universally readable record of
exactly where you drove — useful in the project file and useful to send a client.

## 11.8 Chain of custody

For most survey work this is informal. It stops being informal when the data supports
litigation, a claim, or a boundary determination.

> **PARAMETRIX DECISION REQUIRED**
>
> Determine whether mobile mapping data requires formal chain of custody, and under what
> circumstances.
>
> *Recommended practice:* standard projects need no formal chain of custody beyond the
> field protocol and dated backups. For any project identified as litigation-related or
> forensic, apply a documented chain of custody from the moment the disks leave the
> vehicle, and preserve the raw data unaltered with checksums.

## 11.9 Preparing for the next mission

Only after verification and backup:

1. Return both SSDs to the Control Unit
2. Insert and **lock** them
3. On next startup, watch the **disk check** result — no icon is what you want; a Warning
   or Error means investigate before committing to a mission *(TMI UG Rev L, pp.33–34)*

> **PARAMETRIX DECISION REQUIRED**
>
> Decide how many SSD sets are in circulation.
>
> *Recommended practice:* hold at least one spare set. A single set means the crew cannot
> mobilise until the previous day's offload finishes and verifies — which is precisely the
> pressure that causes someone to skip verification.

---

## References — Section 11

| Source | Pages |
|---|---|
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 9, 14, 18, 33–34, 43–44 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 8, 13–15 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 10, 24 |

## Other References — Section 11

| Source | Chapter |
|---|---|
| NCHRP, *Practices for Collecting, Managing, and Using Lidar Data*, 2024 | Ch.3, Lidar Data Life Cycle |
