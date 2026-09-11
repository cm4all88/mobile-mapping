# 6. Coordinate Systems — What to Set and What to Check

This is not a lesson in datums. It is the four places mobile mapping treats them differently
*(Technical Manual §12)*.

### 6.1 Do

| # | | |
|---|---|---|
| 1 | Set the CRS **before** import | §5 |
| 2 | Set the epoch deliberately if the datum is time-dependent | TBC 2026.10 allows a non-default epoch and warns it "is intended for experienced users" *(TBC RN 2026.10)* |
| 3 | After trajectory processing, **read the SBET filename** | §10 |
| 4 | At export, know whether you are producing grid or ground | §30 |

### 6.2 Look at

The SBET filename once the trajectory exists:

| Filename | What POSPac did |
|---|---|
| `sbet_[mission].out` | Computed directly in the project's datum and epoch |
| `sbet_[mission]_[frame].out` | **Computed first in ITRF00, then transformed** into the project datum and epoch |

*(TBC 25943)*

### 6.3 Expect

Either form. Neither is an error.

### 6.4 Stop if

Nothing here stops you on its own. But **record which form you got**, because the second means an
additional transformation happened that nobody chose.

> **The filename is an indicator, not a verdict.** It tells you a transformation occurred. It does
> not tell you the parameters were right or that the result is accurate — and the plain form is
> equally not proof of correctness *(Technical Manual §12.3)*.

> **TESTING REQUIRED · T10**
>
> Which of Parametrix's normal coordinate systems POSPac recognises directly, and which trigger the
> ITRF00 path. Answerable once, then known.

### 6.5 Record

The SBET filename, in full, in the delivery record (§28).
