# 5. Competence and Training

## 5.1 The principle

Mobile mapping fails quietly. A weak trajectory produces a clean, dense, internally consistent
point cloud in the wrong place *(Technical Manual §3.2)*. There is no visual tell, so the
protection is a person who knows what to check and is required to check it.

**Competence here is not "has operated the system once" and it is not "has read the Technical
Manual." It is the ability to perform the assigned MX60 workflow, recognize when the system or data
is not behaving normally, and know when to stop rather than guess.**

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

## 5.3 The five failure modes a qualified person is expected to recognize

This is not a survey theory syllabus. It is a list of MX60 specific misconceptions that can let a
job look successful when it is not. Each is covered in the Technical Manual at the reference given.

| | | Where |
|---|---|---|
| 1 | **The trajectory is the job.** Every point inherits its error, and an attitude error grows with range | Technical Manual §2, §3 |
| 2 | **A good RMS does not prove success. A bad RMS proves failure.** Trimble states this in identical words in two places | Technical Manual §23 |
| 3 | **Registration does not move points.** The cloud is unchanged until Update Scans runs | Technical Manual §19 |
| 4 | **A Local adjustment does not extrapolate** beyond the outermost control point, and nothing shows where it stopped | Technical Manual §21 |
| 5 | **Cleanup cannot be undone** | Technical Manual §28 |

> **The Field How To and Office How To are the intended training route.** A qualified person should
> be able to carry out the relevant workflow, use the common-problems section when something goes
> wrong, and identify the point where the work must stop or be raised. The Technical Manual is the
> reference for why the condition matters; reading it alone is not qualification.

> **LIVING-DRAFT TRAINING POSTURE — not an adopted qualification rule**
>
> Until **D-3** establishes the actual qualification and sign-off process, this document set does
> not treat a person's first field mission or first MX60 processing job as evidence that they are
> qualified to work independently. The Field How To §1.8 and Office How To §1.7 are written as
> **first supervised workflows** for exactly that reason. D-3 will decide what demonstration,
> review or sign-off converts supervised training into independent qualification.

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
