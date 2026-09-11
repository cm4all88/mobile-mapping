# 24. Reading Trajectory RMS Colouring

Set at **Mobile Mapping ▸ Trajectory Settings ▸ Rendering Settings ▸ RMS values**, with
user-definable ranges and colours. Settings persist between projects *(TBC 27248)*.

> **This is the highest-value, lowest-effort QC view in the workflow**, and it is available
> before any point cloud exists (§17.4).

What to read from it:

- **Where the solution degraded** — and therefore where control is most valuable (§22) and where
  registration will struggle
- **How long each degraded stretch was.** A short gap bracketed by good data is bridged well by
  the smoother. A long one is not (§8)
- **Whether the degradation is at the ends of the mission**, where the smoother has data on one
  side only — the reason the closing sequence in §14 exists

> **OBSERVED SOFTWARE BEHAVIOR**
>
> "If the mission contains some registrations then the modified segments will be colorized with
> the **'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
> `smrmsg` file, so adjusted stretches lose their RMS colour.
>
> **Incidentally useful:** this makes the extent of a registration visible in plan. A **Local**
> registration that stopped adjusting beyond the outermost control point (§21.5) shows the
> boundary directly.