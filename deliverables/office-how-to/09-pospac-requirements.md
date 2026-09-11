# 9. POSPac Requirements — and What to Do Without It

### 9.1 What the licence gates

| Route | Needs POSPac? |
|---|---|
| **Process Raw Trajectory Data** inside TBC | **Yes** — POSPac MMS **8.6 or later**, licensed *(TBC 25943)* |
| **Generate POSPac Position Fixes (PFIX)** — §26 | **Yes** |
| Processing in POSPac externally and importing the SBET | Yes, obviously |
| Using the SBET the vehicle or a bureau produced | No |
| **LiDAR QC** — §24 | Not stated by Trimble. See below |

### 9.2 Do — if you have the licence

Confirm the version is 8.6 or later and that TBC can see it. **Support ▸ License Manager**.

### 9.3 Do — if you do not

1. Obtain a post-processed SBET from whoever holds a licence, and import it
2. Or, if no post-processed trajectory is available at all, **stop and raise it** — see below
3. Record which route was used, on every job

### 9.4 Stop if

- **The only trajectory available is the NAV solution** and the deliverable is survey-grade. NAV is
  the real-time solution computed in the vehicle. It is a fallback, not an option
  *(Technical Manual §17.2)*

> **PARAMETRIX DECISION REQUIRED · D-10 · blocks operation**
>
> **Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?**
>
> Without it, two of the three degraded-GNSS remedies disappear: reprocessing with different
> settings, and PFIX *(SOP §13.1)*.

> **VENDOR CLARIFICATION REQUIRED · V-9**
>
> Whether **LiDAR QC** has its own POSPac dependency. Trimble does not state one, but it is an
> Applanix technology and the topic directs configuration questions to the Applanix Support Team
> *(TBC 28972)*.
