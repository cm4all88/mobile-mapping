# Appendix G — Source Conflicts and Resolutions

Conflicts between two Trimble sources, or between a Trimble source and observed behaviour. Each is
recorded in `reference/mx60-reference-data.csv` under a `CONFLICT-` identifier so that the numbers
on both sides remain traceable.

**None of these blocks work.** Each is a statement that should not be quoted to a client, or put
into a specification, until it is resolved.

| ID | Conflict | Status |
|---|---|---|
| `CONFLICT-002` | Scanner FOV — 346° *(UG p.54)* vs 360° *(spec sheet p.2)* | **V-15** |
| `CONFLICT-003` | Which mounting rack is fitted | **D-2 / V-4** |
| `CONFLICT-004` | Minor numeric discrepancies between sources | Recorded in the CSV |
| `CONFLICT-005` | Laser control presentation — QSG vs TMI Rev L | **V-2** |
| `RESOLVED-001` | Spec sheet vs User Guide laser rates — **system total vs per-scanner, a factor of 2.** QSG confirms TMI uses the User Guide numbering | **Resolved** |
