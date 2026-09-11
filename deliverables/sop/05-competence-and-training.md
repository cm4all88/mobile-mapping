# 5. Competence and Training

## 5.1 The principle

Mobile mapping fails quietly. A weak trajectory produces a clean, dense, internally consistent
point cloud in the wrong place *(Technical Manual §3.2)*. There is no visual tell, so the
protection is a person who knows what to check and is required to check it.

**Competence here is not "has operated the system." It is "knows what the system cannot tell
you."**

## 5.2 What qualification covers

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Three qualifications are distinguished. Who holds each, how it is obtained and how it is
> evidenced is part of D-3.

| Qualification | Covers |
|---|---|
| **Qualified to operate** | Installation and pre-flight; initialization and the closing sequence, and why each exists; operating limits and stand-down authority; field quality checks and the field record |
| **Qualified to process and register** | The data chain and what regenerates from what; trajectory processing; scan generation; registration and the three commands; **what RMS can and cannot prove**; the layered QC in §16 |
| **Qualified to accept** | All of the above, plus the accuracy framework in §17 and the authority under §4 |

## 5.3 The five things a qualified person is expected to know

Not a training syllabus — a list of the misconceptions that have actual consequences. Each is
covered in the Technical Manual at the reference given.

| | | Where |
|---|---|---|
| 1 | **The trajectory is the job.** Every point inherits its error, and an attitude error grows with range | Technical Manual §2, §3 |
| 2 | **A good RMS does not prove success. A bad RMS proves failure.** Trimble states this in identical words in two places | Technical Manual §23 |
| 3 | **Registration does not move points.** The cloud is unchanged until Update Scans runs | Technical Manual §19 |
| 4 | **A Local adjustment does not extrapolate** beyond the outermost control point, and nothing shows where it stopped | Technical Manual §21 |
| 5 | **Cleanup cannot be undone** | Technical Manual §28 |

> **The In Plain Language boxes in the Technical Manual are the intended route to this.** Read end
> to end with nothing else, they describe the whole workflow in ordinary language.

## 5.4 Currency

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Whether a qualification lapses, and what refreshes it. One trigger is not discretionary: **a TBC
> release can change mobile mapping behaviour** (§2.3), and a processor working from a prior
> release's understanding is working from a stale procedure.

## 5.5 Records this section requires

| Record | State |
|---|---|
| Who holds which qualification, and from when | **D-3** |
| Training delivered, and against which document | **D-3** |
