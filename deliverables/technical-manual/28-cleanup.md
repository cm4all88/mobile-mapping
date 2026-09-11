# 28. Cleanup Mobile Mapping Mission

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*
>
> **Do not run this command until §28.4 has been decided by Parametrix.**

## 28.1 What it does

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 26466)*
>
> "The feature enables you to cleanup your project by **keeping the most recent registration (and
> related scans), and trajectory consistent with the latest version of navigation and trajectory
> information file (SBET or NAV)**. This feature can be run at the end of the data preparation
> process (registration, colorization, etc.), it allows you to **share a light project**, before
> moving on to a feature extraction phase. Please, have a backup copy of your project prior
> performing the operation, it cannot be undone."

Run from the **Mission** node context menu. That is the entire published procedure — the topic is
four sentences long.

## 28.2 Why the command exists, and why it is genuinely useful

A mission that has been through several registration attempts accumulates layers. Each
registration produces a trajectory node and a numbered SBET on disk; each Update Scans produces a
scan set beneath it (§19, §21.3). A project with four registration attempts holds four
trajectories and up to four full scan sets of the same data.

That is large, slow to open, and confusing to hand to someone else. Cleanup reduces it to one
answer.

> **There is a real quality argument for it, not just a disk-space one.** After Cleanup, the
> project contains exactly one trajectory and one set of scans, so **the question "which
> trajectory produced this cloud?" has only one possible answer**. Before Cleanup, a person
> exporting from the project can select the wrong node and never know (§29, §30).
>
> Cleanup makes the deliverable unambiguous. It does so by destroying the alternatives.

## 28.3 What it removes, and why that matters

The command keeps the most recent registration and removes the rest. What is removed:

| Removed | Why it mattered |
|---|---|
| **Earlier registration trajectories** | The record that earlier attempts existed, and what they produced |
| **Their scan sets** | The data those attempts produced |
| **The sequence itself** | That there *were* three attempts before this one |

> **IMPORTANT**
>
> **The evidence destroyed is the audit trail, not the deliverable.**
>
> Consider a reviewer, or an expert in a dispute, asking a reasonable question: *was this result
> arrived at directly, or was it the fourth attempt, and what did the first three produce?*
>
> Before Cleanup, the project answers that: the numbered `sbet_<date>_reg_####.out` files are
> still on disk, the trajectory nodes still carry `Origin: Registration result` and their input
> trajectory and registration type (§21.3), and the sequence is legible.
>
> After Cleanup, the project shows one registration and no history. **Nothing indicates that
> anything was removed.**
>
> This is not an accusation of bad practice — iterating a registration is normal and proper work.
> It is an observation that Cleanup removes the ability to demonstrate what was done, at exactly
> the moment the project is being prepared to hand to someone else.

### On the numbered SBET files

> **OBSERVED SOFTWARE BEHAVIOR**
>
> The registered SBETs are written **to the project folder on disk**, not inside the TBC database
> *(TBC 22905, 26473)*. Trimble does not state whether Cleanup deletes them or only removes the
> project's references to them.
>
> **FIELD TESTING REQUIRED · T28** — list the project folder before and after Cleanup and
> compare. If the files survive, they are a partial audit trail that outlives the operation; if
> they do not, the record is gone entirely. **This materially changes what must be archived
> first.** *(Appendix E)*

## 28.4 The Parametrix decision

> **Open Parametrix decision — D-3, D-35.** Stated and tracked in the **SOP §18**; see also the master register.

## 28.5 What Trimble recommends, precisely

Stated carefully, because the gap matters.

> **TRIMBLE DOCUMENTED METHOD**
>
> Trimble recommends **one** thing before Cleanup: **"have a backup copy of your project."**
> *(TBC 26466)*

**No captured Trimble topic recommends exporting, reporting, archiving or otherwise recording
registration information before Cleanup.** No topic links Cleanup to the Mission Report, to
`Targets.csv`, to the numbered SBET files, or to any export.

> **No vendor-prescribed preservation step was found beyond the project backup.**

That recommendation is adequate **on its own terms** — a full project backup preserves everything,
including the history. It is not a records requirement, it does not survive being skipped, and it
says nothing about where the backup lives, how long it is kept, or whether anyone can find it in
three years.

## 28.6 A recordkeeping framework, offered for decision

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §18** (D-35); it is not decided here.

## 28.7 The relationship to provenance

Cleanup is the sharpest instance of the problem §30 is about.

The provenance evidence inside a TBC project is genuinely good — trajectory properties naming the
origin, the input trajectory and the registration type; numbered SBET files; scans nested beneath
the trajectory that produced them; a `_reg_####` station suffix (§21.3, §19).

**IMPORTANT PROVENANCE LIMITATION.** Exported mobile mapping data may retain coordinate, timing,
and in some formats trajectory information, but **the captured Trimble documentation does not
establish that the output uniquely identifies the adjusted trajectory or registration result used
to create it** (§30).

> **The two findings compound.** Cleanup reduces the registration history available in the
> project; export is not documented as providing unique registration lineage. **A LAS point cloud
> exported after Cleanup may retain spatial and point-level metadata, but the captured
> Trimble documentation does not establish that it preserves sufficient registration and
> trajectory lineage to reconstruct how the final cloud was produced.**
>
> The practical concern is therefore not literally "no history." It is that **the deliverable may
> not contain enough documented provenance to reconstruct its processing history independently of
> the TBC project and Parametrix records.**
>
> That is not an argument against Cleanup. It is the reason §28.4 remains a Parametrix decision,
> and the reason §28.6 steps 2–6 are proposed to happen first.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We looked at a command that tidies a finished project by throwing away
> every registration attempt except the last one, along with the point clouds those attempts
> produced. It cannot be undone. Trimble's entire published guidance on it is four sentences, one
> of which says to back up first.
>
> **Why it matters.** Working on a difficult corridor, you will register, look at the result,
> change something, and register again. That is normal, careful work — it is what an adjustment
> looks like when you are paying attention. By the end, the project holds several versions of the
> same data, it is enormous, and it is genuinely confusing for whoever picks it up next. Cleanup
> is the obvious answer, and it is a reasonable one.
>
> **What can go wrong.** What it removes is not the deliverable. It is the ability to show how you
> got there. Before Cleanup, anyone can open the project and see that there were four attempts,
> what each produced, and which one was kept. After it, there is one result and no indication that
> anything else ever existed. Nobody has done anything wrong — but if a reviewer asks how the
> number was arrived at, the honest answer is now "from memory."
>
> This matters more than it would elsewhere because of §30: almost none of that history leaves the
> project when you export anyway. So the project file is where the evidence lives, and Cleanup is
> the thing that thins it, at the exact moment the job is being wrapped up and handed on.
>
> **What good looks like.** Cleanup is not the enemy. Running it blind is. A sound sequence is:
> finish QC, get the result accepted, run the Mission Report and keep it, write down which points
> were control and which were checks and what the residuals were, keep the small files — the
> picked targets, the numbered trajectory files, the calibration — take the backup Trimble asks
> for and put it somewhere the company can find it in three years, get whoever is supposed to
> authorise it to authorise it, and then run the command. Ten minutes and a few megabytes, and the
> deliverable can still account for itself.
