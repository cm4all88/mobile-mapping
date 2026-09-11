# 27. Identifying Registration Results

**Which trajectory is this cloud built on?** You will be asked. This section is how you answer.

### Do

Work the four layers, in this order.

| # | Layer | Where |
|---|---|---|
| 1 | **Tree position** | Scans hang beneath the trajectory that produced them |
| 2 | **Station suffix** | Updated stations carry **`_reg_####`** |
| 3 | **Trajectory properties** | **`Origin: Registration result`** · **`Input trajectory:`** · **`Registration type:`** *(TBC 22905, 26473)* |
| 4 | **SBET filename on disk** | `sbet_<date>_reg_####.out`, incrementing per registration, in the project folder |

### Look at

Project Explorer, expanded. A run that has been registered has **two trajectories and two sets of
scans**:

```
Run 14
  ├── Sbet                        the imported trajectory
  │     └── Run_14_Laser Right (S1)          ← unregistered scans
  └── Reg. Trajectory             Origin: Registration result
        └── Run_14_Laser Right_reg_0001 (S3) ← registered scans
```

**They look identical in plan.** Tree position and the suffix are the difference.

### A fifth, incidental indicator

Registered trajectory segments render as **"Undefined RMS"** in the RMS colouring (§10), because a
registered trajectory no longer matches its `smrmsg` file *(TBC 27248)*.

That makes the **extent** of a registration visible in plan — including where a **Local**
adjustment stopped adjusting, which nothing else shows you.

### Expect

All four layers agreeing.

### Stop if

- **They disagree.** A cloud beneath `Sbet` whose stations carry `_reg_####` is telling you
  something you need to resolve before exporting
- **You cannot tell which trajectory a cloud was built on.** Do not export it (§31)

> **Nothing in this is conclusive once the data leaves the project.** That is what §28 is about.

### Record

The trajectory node name and the SBET filename **with its `_reg_####` number**, in the delivery
record.
