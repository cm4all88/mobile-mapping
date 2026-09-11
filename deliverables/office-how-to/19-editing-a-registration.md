# 19. Editing a Registration — and Why Not to Register Twice

### The problem

> **CAUTION · W-07**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.

Running a registration command a second time on a run that has already been registered adjusts the
**adjusted** trajectory, not the imported one — and no number in the result shows it.

### Do

1. Select the **registered trajectory node**
2. **Edit** from the context menu *(TBC 25362, 26578)*
3. The command reopens with the control points, their Use XY / Use Z / As Check states and the
   picked targets reloaded
4. Change what needs changing
5. **Compute**, then **Apply**

### Look at

That the reloaded state is the one you expect — particularly the **As Check** settings. Edit is
also how you confirm what a previous registration actually used, since no report of it has been
found (§20).

### Expect

The registration recomputed **from the imported trajectory**, not from the adjusted one.

### Stop if

- **A reload prompt appears and you are about to answer "No".** See below
- You cannot find the Edit command. Do not fall back to running the registration again

> **CAUTION · W-06**
>
> If Registration Auto-Saving is on, picked targets are written to **`Targets.csv`**. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

> **TESTING REQUIRED · T7** — whether Registration Auto-Saving is on by default. One glance at the
> dialog answers it.

### Record

That the registration was edited rather than repeated, and what changed.
