# 9. Field Quality Checks

## 9.1 What can and cannot be checked in the field

> **The distinction matters more than the checks themselves.** A great deal of what determines
> dataset quality cannot be assessed until the trajectory is post-processed in the office — which
> may be days later, and always after the vehicle has left.

| Can be checked in the field | Cannot be checked until the office |
|---|---|
| The mission recorded and closed | **Post-processed trajectory quality** (§12.4) |
| All planned runs exist | **Point cloud accuracy against control** (§15, §17) |
| Data written to disk and readable | **Whether GNSS degradation was bridged adequately** |
| Coverage — was the corridor driven | **Point density at the achieved standoff** |
| Sensors reported present throughout | **Imagery detail sufficiency** |
| Gross imagery problems — obstruction, contamination | **Colour fringing, boresight symptoms** (§19.5) |
| Free space and disk health | **Anything requiring the SBET** |

> **IMPORTANT**
>
> **Nothing available in the field confirms that the data is of survey quality.** The field checks
> confirm that the data **exists, is complete, and is readable**. That is a genuinely valuable
> thing to confirm before leaving — and it is not the same as confirming it is good.

## 9.2 The checks, in order

### Before leaving the initialization location

| ☐ | Check |
|---|---|
| ☐ | Navigation status reached its ready indication |
| ☐ | **Settling time allowed** (§8.3) |
| ☐ | All sensors reporting present in TMI |
| ☐ | Storage sufficient for the planned mission |

### During collection

| ☐ | Check |
|---|---|
| ☐ | Navigation status held |
| ☐ | No sensor dropped out |
| ☐ | No Battery Protect event |
| ☐ | Storage tracking against remaining corridor |
| ☐ | Comments recorded as events occurred (§8.6) |

### Immediately after closing the mission — before the vehicle moves

| ☐ | Check |
|---|---|
| ☐ | **Closing sequence performed in full** (§8.7) |
| ☐ | Mission closed in TMI |
| ☐ | **Power button light out** before power or disk is disturbed (§8.8) |

### Before leaving site

| ☐ | Check |
|---|---|
| ☐ | **Mission folder present on the disk, with a plausible size** |
| ☐ | **Run count matches what was driven** |
| ☐ | Raw POS data present in `POS_1/raw` (§11.3) |
| ☐ | Base station data captured, if a local base was used |
| ☐ | Field record complete (§8.9) |
| ☐ | **Any re-drive decided and performed now** (§9.4) |

> **CAUTION**
>
> **Do these before the vehicle leaves the corridor.** Every item above is recoverable on site in
> minutes and costs a mobilisation from the office.

## 9.3 Coverage verification

The one substantive quality check available in the field.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Before leaving, confirm against the plan (§6.9):
>
> - Every planned pass was driven, in the planned direction
> - The corridor was driven end to end, including any extent beyond the deliverable required to
>   bracket control (§5.6)
> - **Planned overlap was actually collected** — this is the one that removes office options if
>   missed (§20.3)
> - Sections not collected, and why, are recorded
>
> *(D-49)*

> **IMPORTANT**
>
> **Overlap is the check worth being pedantic about.** If a GNSS-hostile stretch was planned for
> two passes and got one, **both LiDAR QC and run-to-run registration become unavailable** in the
> office (§20). There is no software warning and no way to tell later except by looking at what is
> there.

## 9.4 The re-collection decision

> **IMPORTANT · this is a field decision with office consequences**
>
> Re-driving a run while the vehicle is on site costs minutes. Re-driving from the office costs a
> mobilisation and, on a corridor requiring traffic control, considerably more.

> **PARAMETRIX DECISION REQUIRED · D-49**
>
> **What triggers a re-drive, and who decides?**
>
> Candidate triggers, offered for decision, not adopted:
>
> - Navigation status degraded through a section that matters
> - A sensor dropped out mid-run
> - A run interrupted by a power or storage event
> - Significant occlusion by traffic through a section that matters
> - The closing sequence not completed
> - Conditions moved outside the weather rule mid-mission (§6.5)
>
> The decision needs to state **whether the operator may re-drive on their own judgement**, or
> must seek approval. An operator who must phone will usually drive on.

## 9.5 What the field record must carry into the office

Field notes are not administrative. **Three later sections depend on them**, and no software
produces any of it:

| Field record item | Where the office needs it |
|---|---|
| Planned versus driven extent | §11.4 — covered distance check; §24 Layer 1 |
| Run count and which runs are which | §11.5; §16 pair selection |
| **GNSS conditions observed** | §12.4 — corroborates the RMS picture; §18.4 |
| Occlusion and traffic events | §18.5 — explains a gap that is not a defect |
| Sections not collected, and why | §24 Layer 1; the client conversation |
| Capture settings used | §13; §24 Layer 3 |
| Incidents, stoppages, re-drives | §26 — troubleshooting a dataset after the fact |

> **FIELD TIP**
>
> The most useful single thing an operator can write is **why the corridor looks the way it does**
> at any point where it is unusual. Three weeks later, the office is looking at a stretch with
> poor residuals and cannot tell whether it was tree canopy, a stopped truck, or a system problem.
> One sentence at the time settles it.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** Before the vehicle left, we confirmed the data exists, is complete, is
> readable, and covers what it was supposed to cover — and we wrote down what the conditions were
> like.
>
> **Why it matters.** Almost nothing about *quality* can be judged in the field. You cannot tell
> whether the trajectory is good until it has been post-processed in the office, days later. What
> you can tell is whether the data is there. Those are different questions, and confusing them is
> how people talk themselves into leaving.
>
> **What can go wrong.** The expensive miss is overlap. If a difficult stretch was meant to get two
> passes and got one, two of the three office remedies for bad GNSS have just become unavailable —
> and nothing warns anyone. It looks like a complete dataset. It is a complete dataset with fewer
> options.
>
> The other is the field record. Three weeks on, the office is staring at a stretch with poor
> residuals and no way to know whether it was tree cover, a parked truck, or a fault. One sentence
> written at the time — "heavy canopy from the bridge to the school" — saves a day of guessing and
> sometimes a return visit.
>
> **What good looks like.** Every planned pass driven, in the planned direction, including the
> overlap. The mission closed properly and confirmed written. A run count that matches what was
> actually driven. A short honest note of conditions, incidents, and anything not collected. And
> any re-drive done *now*, while the vehicle is still here and it costs twenty minutes.
