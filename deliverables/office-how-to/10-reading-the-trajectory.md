# 10. Reading the Trajectory

**Do this before you generate a single scan.** It is the highest-value, lowest-effort check in the
whole workflow, it takes seconds, and it tells you where everything else is going to be difficult.

### Do

1. **Mobile Mapping ▸ Trajectory Settings ▸ Rendering Settings ▸ RMS values**
2. Set the ranges and colours you want. **The settings persist between projects** *(TBC 27248)*
3. Look at the trajectory in **Plan View**
4. For detail: **Mobile Mapping ▸ Reports ▸ Trajectory Plots**

### Look at

Three things, in this order:

| | |
|---|---|
| **Where the solution degraded** | That is where control is worth most (§14), and where registration will struggle |
| **How long each degraded stretch is** | A short gap bracketed by good data is bridged well. A long one is not |
| **Whether the degradation is at the ends of the mission** | The ends are where the smoother had data on one side only. If the last stretch is a different colour from the rest, that is the closing sequence talking *(Technical Manual §14.4)* |

### Expect

Mostly one colour, with the degraded stretches where the mission plan predicted them — under the
overpass, through the tree cover — and short.

### Stop if

- A degraded stretch is long and you have **no control bracketing it** and **no overlapping pass**.
  You have no remedy for it, and that is a conversation to have now rather than after registration
  (§25)
- The whole trajectory is degraded. Something is wrong upstream — check §8 and §35

> **Segments that have been registered render as "Undefined RMS"** *(TBC 27248)*. A registered
> trajectory no longer matches its `smrmsg` file, so the colouring drops out. That is a side
> effect, and §27 turns it into a useful one: it makes the extent of a registration visible in
> plan, including where a **Local** adjustment stopped.

### Record

A screen capture of the RMS-coloured trajectory. It is a required QC record (SOP §15.8) and it is
one click.
