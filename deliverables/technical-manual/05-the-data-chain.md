# 5. The Data Chain

The names in this section matter because TBC's commands are named after them. A processor who
does not know which object a command acts on will eventually act on the wrong one — and several
of the commands are not undoable.

## 5.1 The chain, once

```
  .mxdb          The mission database written in the field. The index to everything
     │
     ├── raw GNSS + IMU observations  ──►  SBET (or NAV)      the trajectory
     │
     └── raw scanner + camera data
              │
              ▼
            TMX          polar scan data — ranges and angles, sensor-relative
              │
              │   Generate Scans  ◄── applies the trajectory
              ▼
           RWCX          the point cloud — XYZ, intensity, colour, normals
```

Two things are worth stating now and are returned to in §18.

**The MX60 converts TMX to RWCX in one step.** Older MX9 and MX90 systems go through an
intermediate stage requiring a range-ambiguity correction called MTA. **The MX60 workflow has no
MTA stage**, which removes a whole category of setup and a whole category of failure
*(TBC 22503)*.

**The trajectory is applied at scan generation, not at collection.** The raw scan data is
sensor-relative. It becomes a georeferenced point cloud only when combined with a trajectory —
which is why improving the trajectory later means regenerating the cloud (§19, §21).

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22503)*
>
> MX50 and MX60 convert **TMX → RWCX in one step**. MX9 and MX90 go RXP → TMX → RWCX in two, and
> the intermediate stage requires **MTA** (Multiple Times Around) range-ambiguity correction.

> **The MX60 has no MTA configuration and no MTA failures.** If you encounter TBC documentation
> about configuring a GPU driver for MTA correction *(TBC 23856)*, it does not apply to this
> system. It is mentioned here only because it is prominent in the TBC help and causes confusion.

## 5.2 The mission on disk

What the system writes in the field:

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 20736-1, 22503, 22554, 25943)*

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

Three observations about this structure that matter operationally:

**The `.mxdb` is an index, not the data.** It is small. Copying it alone copies nothing useful.
Everything the chain depends on sits in the sibling folders, which is why the transfer requirement
is the whole mission folder and not a file.

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

**`Extcal.json` travels with the mission.** The calibration state that produced the data is
recorded alongside the data rather than held only in the software. This is the single most
useful provenance artifact in the chain and is discussed in §30.

**`POS_1/raw/` is the irreducible original.** Every trajectory the office ever computes — the
first SBET, a LiDAR QC refinement, a PFIX second pass, a registered variant — derives from those
files. They are the only thing in the mission that cannot be recomputed.

## 5.3 The mission in Project Explorer

What the same mission looks like after import into TBC:

```
Mobile Mapping
  └── <mission id>
        ├── Capture Devices          Camera 3 Back Down, Camera 4 360°, Laser Left, Laser Right
        └── Run 0, Run 1, Run 2 …
              └── Sbet                the imported trajectory
                    └── (scans appear here after Generate Scans)
```

> **Note the shape. Scans are children of a trajectory, not of a run.**
>
> That is the structural fact that makes tree position meaningful evidence of which trajectory a
> cloud was built on (§30) — and it is why a run with two trajectories has two independent sets of
> scans beneath it.

A run that has been registered therefore does not *replace* its scans. It gains a second
trajectory node, and after **Update Scans** (§19) a second set of scans hanging off it. Both sets
remain in the project, look identical in plan, and are distinguishable only by their position in
the tree and by the `_reg_####` suffix on the newer stations. Everything difficult about MX60
provenance follows from that one sentence.

## 5.4 What each object can and cannot be regenerated from

| Object | Regenerated from | Lost if deleted |
|---|---|---|
| **SBET** | `POS_1/raw/` + base data, through POSPac | Recoverable — but the processing settings that produced *this* SBET are not recorded in the file |
| **Registered SBET** | The parent SBET + the registration + surveyed control | Recoverable only if the picked targets survive (`Targets.csv`, §21) |
| **TMX** | `Laser_1`, `Laser_2` raw | Recoverable |
| **RWCX** | TMX + a trajectory | Recoverable — **against whichever trajectory is selected at the time**, which is not necessarily the one that produced the original |
| **Picked targets** | Nothing. A human picked them | **Not recoverable.** Re-picking produces different points |
| **`POS_1/raw/`** | Nothing | **Not recoverable.** Re-collect the mission |

> **CAUTION**
>
> Read the middle rows carefully. Most of the chain is reproducible, which makes it tempting to
> treat any individual file as disposable. The two rows that are not reproducible — raw
> observations and human target picks — are also the two most likely to be discarded, because one
> is large and the other is small enough to overlook.

## 5.5 Where each stage's quality is decided

The chain is worth reading a second time as a sequence of irreversible commitments:

| Stage | What is fixed here | What can still be fixed later |
|---|---|---|
| **Field collection** | Geometry, coverage, GNSS conditions, initialization quality | Nothing. This is the only stage with no office remedy |
| **Trajectory processing** | Which corrections and which base data were used | Reprocess — cheap, as long as the raw data is intact |
| **Scan generation** | Filters applied, colorization | Regenerate — cheap in effort, expensive in time |
| **Registration** | The fit to surveyed control | Register again, or re-pick. But adjustments stack (§21) |
| **Export** | What the client receives | Re-export, if the project still exists in the state that produced it (§29, §30) |

> **WHY THIS MATTERS**
>
> Every stage after the first is recoverable, and the first is not. That asymmetry is the reason
> this manual spends more of its length on field method than the office's share of the schedule
> would suggest. An office error costs hours. A field error costs a mobilisation.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We named the four things the data passes through — the mission database,
> the trajectory, the polar scan data, and the point cloud — and said which command turns each one
> into the next.
>
> **Why it matters.** Nearly every confusing thing in the office workflow makes sense once you
> know that the point cloud is *computed*, not *collected*. The scanner measured ranges and angles
> from a sensor that was moving. The trajectory says where that sensor was. Multiply the two
> together and you get coordinates. That is what **Generate Scans** does, and it is why changing
> the trajectory later means doing it again.
>
> **What can go wrong.** Two things, both common. The first is copying the `.mxdb` and thinking
> you have the mission — you have the table of contents. The second is looking at a run in Project
> Explorer, seeing two sets of scans, and assuming one is a duplicate to be tidied away. They are
> the same raw data computed against two different trajectories, and which one you keep is a
> decision about the accuracy of the deliverable, not about disk space.
>
> **What good looks like.** You can point at any point cloud in the project and say which
> trajectory produced it, without guessing. If you cannot, §30 explains how to work it out and how
> far that evidence actually goes.
