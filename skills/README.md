# Skills

This directory contains portable, sanitized procedures that an adopting runtime may install deliberately. Their presence in the repository does **not** mean they are installed, enabled, connected to tools, or granted authority.

Included packages:

- [`COMPOSITION.md`](COMPOSITION.md) — the handoff contract between skills and their artifacts, distinct from the procedures owned by each individual skill page.
- [`agent-prompt-design`](agent-prompt-design/SKILL.md) — executable task contracts, bounded agent graphs and loops, verification, and evaluation discipline.
- [`artifact-verification`](artifact-verification/SKILL.md) — outcome-backward, source-bound verification for local artifacts.
- [`deterministic-evidence-automation`](deterministic-evidence-automation/SKILL.md) — deterministic collection plus bounded model judgment for recurring evidence-heavy work.
- [`authority-effect-contracts`](authority-effect-contracts/SKILL.md) — machine-checkable authority manifests and external-effect receipts.

These are curated class-level projections, not exports of the source agent's private runtime. Private paths, case histories, live capability state, credentials, schedules, domain records, and standing permissions are excluded. `metadata.hermes.related_skills` names optional recommendations for runtimes that support them; those entries are not bundled dependencies. Verify compatibility and review each package before installation.

The linked `SKILL.md` pages are the stable parent procedures unless they explicitly say otherwise. A parent may link nested experimental instruments under its existing `references/`, `scripts/`, or fixture surfaces; those instruments remain trial-only, carry their own evidence and lifecycle boundaries, and do not become stable merely because the parent links them or CI protects them.
