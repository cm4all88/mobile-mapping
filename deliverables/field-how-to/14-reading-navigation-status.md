# 14. Reading Navigation Status

## 14.1 The colours

| Colour | Meaning |
|---|---|
| **Red** | Not meeting threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Green** | The parameter meets its accuracy threshold |

## 14.2 What green does not mean

> **IMPORTANT · [TRIMBLE]**
>
> **Green means the solution met the accuracy thresholds — not that it has finished converging.**
> That is why Trimble asks for **up to ten more minutes** before recording anything that matters
> *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day. Do not spend it on
> the most important part of the corridor.**

The light does not change again when the estimate improves, so nothing tells you. This is the one
part of initialization the system does not enforce, and therefore the part that gets skipped.

## 14.3 If it will not reach green

**Ask TMI which parameter is holding it.** The remedies are different and waiting helps neither.

| Holding | Likely cause | Do |
|---|---|---|
| **Heading** | Not enough dynamic manoeuvres, or no GAMS | **More turns and speed changes** |
| **Position** | Poor sky view | **Move the vehicle** to genuinely open sky |
| **Attitude** | Not enough motion variety | Complete the full manoeuvre profile |

## 14.4 Orange

**Orange permits recording. Survey-grade work does not.**

Until **D-3 / D-49** is decided, treat orange as a **stop-and-assess** condition: work out why,
record it, and decide deliberately rather than by default.

## 14.5 Record

The time green was reached, and the time recording of significant data began. The gap between them
is the settling time, and it is the evidence that §14.2 was respected.
