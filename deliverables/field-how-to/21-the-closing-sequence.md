# 21. The Closing Sequence

> **CAUTION · W-09**
>
> The post-processed trajectory is computed **forward and backward** and merged. A degraded stretch
> mid-mission is bracketed by good data on both sides. **A degraded stretch at the end has good
> data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

## 21.1 Do

1. Finish the last run
2. **Drive to an open-sky location — with the mission still running**
3. **Dynamic steering manoeuvres**
4. **Vary the speed**
5. **Drive straight**
6. **Remain stationary for 2–3 minutes**, logging static data
7. **Close the mission** in TMI
8. **Wait for the Control Unit power button light to go out — up to 90 seconds**

**[TRIMBLE METHOD]** *(MX60 QSG Rev B, §5.5 p.13)* — Trimble's documented sequence. It instructs
that the mission be finalized *"according to the following sequence"*, and gives the reason rather
than an obligation: symmetrical start and end *"supports forward and reverse processing modes in
the office software"*. **Not a manufacturer requirement — and still the right thing to do**, because
W-09 above is a fact about the data regardless of who requires what. Whether Parametrix makes it
mandatory is **SOP D-56**.

## 21.2 It is initialization, backwards

Steps 3–6 are the initialization sequence in reverse order *(MX60 QSG Rev B, p.13)* — manoeuvres,
speed variation, straight, static, where the start was static, straight, speed variation,
manoeuvres.

That is not a mnemonic. The backward pass runs through the data in reverse, so what it meets first
is what the forward pass met last.

## 21.3 The mistake

> **IMPORTANT**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and *then*
> driving to open sky achieves nothing. The manoeuvres have to be inside the logged data.

## 21.4 Five minutes

**It takes about five minutes and it is the cheapest quality improvement available in the entire
workflow.**

You cannot append it the next day — a new mission is a new trajectory. There is no office
procedure that buys it back *(Technical Manual §14.3)*.

## 21.5 Record

**That the closing sequence was performed**, and the time. The office will look for it.
