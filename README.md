# Agent Identity & Ops Starter

A public, runtime-neutral starter for turning a blank AI agent into a candid, corrigible, systems-oriented thinking partner without confusing identity, doctrine, procedures, memory, or authority.

This repository is adapted from Bobert's architecture, but **it is not Bobert and contains no private continuity**. It is designed to be copied, forked, or pointed to by another agent.

## Give this to a blank agent

Use this instruction:

> Read `ADOPT.md` in this repository and follow it. Use `SOUL.md` as your initial constitutional identity and `index.md` as the router for deeper operating doctrine. Do not claim permissions, memories, relationships, capabilities, or personal facts that are not provided by me or verified in my environment. Before personalizing identity-bearing language, ask me the consequential questions in `CUSTOMIZE.md`.

That instruction is intentionally conservative: a reusable identity should transfer judgment, not somebody else's biography or authority.

## Architecture

| Layer | Purpose |
|---|---|
| `SOUL.md` | Always-loaded identity, character, judgment posture, and hard boundaries |
| `GOVERNANCE.md` | Placement, authority, status, confidence, provenance, and revision rules |
| `doctrine/` | On-demand judgment for consequential classes of problems |
| `index.md` | Generated problem router; not an independent authority |
| `ADOPT.md` | Safe bootstrap procedure for a blank agent |
| `CUSTOMIZE.md` | Questions and rules for making the starter genuinely yours |
| `FIRST-WEEK.md` | Conservative initial behavior, expectations, and correction path |
| `FIELD-TESTING.md` | Bounded tests and a privacy-safe path for reporting useful, null, and negative results |
| `RUNTIMES.md` | Runtime installation decisions, degradation behavior, and a bounded verification probe |
| `SYNC.md` | Curated private-to-public projection policy |
| `scripts/` | Deterministic generation and integrity checks |

Procedures, live domain facts, credentials, permissions, and personal memory do **not** belong here. They must be created in their runtime-specific governed homes.

## Doctrine domains

- permissions, controls, and discretion
- least-privilege capability access
- information placement and source authority
- decision quality under uncertainty
- strategic response and incentives
- right-sized change
- decision records and operational documentation
- external capability governance

## Test and improve the concepts

The doctrine is active but revisable. If you use a concept in real work, [FIELD-TESTING.md](FIELD-TESTING.md) explains how to record a bounded prospective or retrospective test, distinguish decision effect from outcome, protect private operational data, and submit useful feedback through the repository's issue form.

Positive results are not the only useful reports. Null effects, failures, excess ceremony, confounds, and evidence that a concept should be narrowed are especially valuable.

## Quick start

```bash
python3 scripts/generate_index.py
python3 scripts/check_template.py
```

Then follow [RUNTIMES.md](RUNTIMES.md) to install and verify the identity, doctrine router, and degraded-context behavior. Runtime installation differs; do not let a bootstrap script silently overwrite an existing identity.

## What this does not prove

A coherent repository does not prove good judgment. Static checks establish structure and detect some classes of drift. Real work reveals retrieval failures, bad assumptions, overreach, and doctrine that does not earn its complexity.

## License

MIT. See `LICENSE` and `LINEAGE.md`.
