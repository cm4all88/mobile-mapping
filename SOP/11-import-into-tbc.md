# 11. Import into TBC

## 11.1 What import does, and what it does not

Importing a mission brings the **mission database** into a TBC project and makes its contents
visible in Project Explorer. It does **not** produce a point cloud, and it does not compute
anything.

> **The most common misunderstanding at this stage:** after import you can see runs,
> trajectories and capture devices, and the Plan View draws a line along the corridor. It looks
> like data. It is an index. The point cloud does not exist until Generate Scans is run (§13).

## 11.2 Before you import — the project must be right first

> **IMPORTANT**
>
> **Set the project coordinate system before importing the mission.** Trimble states the
> prerequisite as "Create a VCE project and if necessary, change the coordinate system so that it
> matches the coordinate system for the mobile mapping data to import" *(TBC 24886, 24460)*.
>
> Changing it afterwards is possible in TBC generally, but on a mobile mapping project it means
> every derived product — scans, registrations, exports — was computed in the previous frame.
> §5 covers the coordinate system decisions; this is simply the point at which they become
> irreversible in practice.

The trajectory must also be decided before or during import (§12). A mission can be imported
with either:

- the **post-processed SBET** — the normal case for survey work, or
- the **real-time NAV** trajectory, "in case POSPac processing not possible" *(TBC 24460)*

> **CAUTION**
>
> **NAV is a fallback, not an option.** It is the trajectory the system computed in the vehicle,
> in real time, without the benefit of a reverse pass or base station corrections. It is
> appropriate for a quick look and for checking coverage. It is not appropriate for a survey
> deliverable, and a project that reaches export still on NAV has skipped the single largest
> quality step in the workflow.

## 11.3 The data objects, and where they appear

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 20736-1, 22503, 22554)*

The mission on disk, as written in the field:

```
TMX<serial>-<mission id>/
  ├── Backup/
  ├── Base/                 base station RINEX, if collected      .YYo .YYn .YYg
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── NavProc_01/           navigation processing outputs
  ├── POS_1/
  │     ├── raw/            raw IMU + GNSS — posl_*.000, .001, .002 …
  │     └── realtime/
  ├── Extcal.json           the calibration file
  ├── readme_*.txt
  ├── <mission>.mxdb        the mission database — this is what you import
  ├── <mission>.tridb
  └── <mission>_*.log
```

*(TBC 25943)*

In Project Explorer after import:

```
Mobile Mapping
  └── <mission id>
        ├── Capture Devices          Camera 3 Back Down, Camera 4 360°, Laser Left, Laser Right
        └── Run 0, Run 1, Run 2 …
              └── Sbet                the imported trajectory
                    └── (scans appear here after Generate Scans)
```

> Note the shape. **Scans are children of a trajectory, not of a run.** That is the structural
> fact that makes tree position meaningful evidence of which trajectory a cloud was built on
> (§23) — and it is why a run with two trajectories has two independent sets of scans beneath it.

## 11.4 Mission properties worth reading at import

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*

Selecting the mission node shows properties including start and stop times, duration, **covered
distance**, and the **active trajectory file**.

> **FIELD TIP**
>
> **Read the covered distance against what the crew said they collected.** It is the fastest
> available check that the mission is complete — a corridor the crew reported as 14 km that
> imports as 9 km means a run is missing, a file did not transfer, or a collection stopped
> without anyone noticing. Catching that at import costs a minute. Catching it at QC costs a
> return visit.

## 11.5 What to verify before going further

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> At import, before any processing:
>
> 1. **Project coordinate system** matches the control network and the client's requirement
> 2. **Covered distance** is consistent with the field record (§11.4)
> 3. **Run count** matches the field record — a mission with fewer runs than the crew logged has
>    lost data in transfer
> 4. **The active trajectory** is the intended one, and is SBET rather than NAV unless there is a
>    recorded reason
> 5. **Capture Devices** lists the sensors expected for the configuration (§4.1) — a missing
>    camera or laser here means a sensor was disabled or failed in the field
> 6. **Base station data** is present in `Base/` if the trajectory will be processed in-house
>    (§12)
> 7. **The calibration state the mission was collected under is recorded.** `Extcal.json` sits
>    with the raw data, and the **Mission Report** carries per-sensor boresight and lever-arm
>    calibration **with a date of calibration** *(TBC 24868; §14.6)* — the only dated calibration
>    record found anywhere in the workflow (§23.3)
>
> **Not adopted.** Seven checks, none taking more than a minute, all cheaper now than later.
> *(D-18)*

> **Check 7 exists because of a handoff.** Calibration currency is confirmed in the field (§7.9)
> and owned by the System Owner (§3.2), but **the processor is the last person who can record what
> it was** before the project moves on. If a mission turns out to have been collected on a stale
> calibration, that is a §14.7 question — and it can only be asked if somebody noted the date.

> **PARAMETRIX DECISION REQUIRED · D-26**
>
> **What happens to data collected on an out-of-date calibration?** Reprocess after
> recalibration, accept with a note, or re-collect? The question belongs to the recalibration
> policy in §14.7 and is recorded there.

## 11.6 Multiple missions in one project

A TBC project can hold several missions, and both **Register Run to Run** *(TBC 25096)* and
**LiDAR QC** *(TBC 28972)* can work across them. Runs are identified in those commands as
`<last two digits of mission ID> - Run <n>`.

> **FIELD TIP**
>
> Those last two digits come from the `.mxdb` filename — `TMX50320120101-000033.mxdb` is mission
> `33` *(TBC 25096)*. On a project with several days of collection, write the mapping down. The
> pair selectors in Register Run to Run show only the two digits, and choosing the wrong run
> because two missions ended in similar numbers is an easy and expensive mistake.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We pointed TBC at the mission database the vehicle wrote, and it read the
> index: which runs exist, which sensors were on, how far the vehicle travelled, and which
> trajectory is currently attached. It drew the route on the map.
>
> **Why it matters.** This is the moment the project's coordinate system gets locked in for
> practical purposes, and it is the cheapest moment in the entire workflow to notice that
> something is missing. Everything downstream is built on what came in here.
>
> **What can go wrong.** The thing to watch for is that it all looks fine. A mission missing two
> runs imports without complaint and draws a perfectly convincing line on the map — just a
> shorter one than it should be. Nobody notices until the deliverable is short a section of
> corridor, by which time the crew and the vehicle are three jobs away. The other one is
> importing with the real-time NAV trajectory attached because the post-processed SBET was not
> ready, and then simply never going back. NAV works. It produces a cloud. It is just not
> survey-grade, and nothing in the software will remind you.
>
> **What good looks like.** The covered distance matches what the crew wrote down. The run count
> matches. The sensors listed are the ones that were supposed to be running. The trajectory
> attached is the post-processed one. Five minutes of looking, before any processing starts.
