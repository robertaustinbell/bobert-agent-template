# Material operating log

Record only material doctrine failures, contradictions, retrieval misses, scope or confidence changes, and architecture revisions. Ordinary success does not require an entry.

## 2026-07-30 — Added critical-capability mapping as a field-test candidate

- **Protocol:** `FIELD-TESTING.md` — `Critical-capability mapping candidate test`
- **Decision effect:** tests whether mapping objective → indispensable capability → enabling requirements → conditional vulnerabilities exposes a dependency that changes protection, verification, redundancy, simplification, sequencing, or explicit risk acceptance
- **Scope:** consequential work where capability or dependency concentration may change the move; not a universal centre, attack-first method, label for people, or replacement for critical-path analysis
- **Evidence:** Eystein L. Meyer, “The Centre of Gravity Concept: Contemporary Theories, Comparison, and Implications” (2022), [DOI 10.1080/14702436.2022.2030715](https://doi.org/10.1080/14702436.2022.2030715)
- **Remaining uncertainty:** the source compares contested military planning theories rather than demonstrating agent effectiveness; retain, narrow, or remove the candidate according to prospective decision effects, null results, and false-concentration failures

## 2026-07-30 — Added operational friction as a field-test candidate

- **Protocol:** `FIELD-TESTING.md` — `Operational-friction candidate test`; `doctrine/design/right-sized-change.md` — `Operational-friction check (candidate)`
- **Decision effect:** tests whether individually tolerable delays, handoffs, state mismatches, degraded conditions, or capacity limits interact or compound across the real operating path enough to change simplification, margin, rehearsal, recovery, or read-back
- **Scope:** consequential multi-step work where cumulative practical resistance may change the move; not a seventh situational-awareness stage, exhaustive hazard inventory, mandatory checklist, label for people, manufactured live disruption, or commander-centric doctrine
- **Evidence:** Clausewitz, *On War*, Book I, Chapter VII; Eugenia C. Kiesling, “On War Without the Fog” (2001)
- **Correction:** independent review caught two release blockers before publication: the generated index had displaced the established stable-component-removal trigger, and the validator protected field-test safeguards without protecting the same load-bearing active-doctrine text. The trigger was consolidated and both surfaces now carry lexical regression canaries; these remain deletion/drift checks, not semantic proof.
- **Remaining uncertainty:** the candidate may only rename existing preflight, critical-path, resilience, and situational-understanding controls; retain, narrow, or remove it according to prospective decision effects and clean null, negative, harmful, or confounded results

## 2026-07-30 — Opened bounded public field testing

- **Architecture:** `FIELD-TESTING.md` and `.github/ISSUE_TEMPLATE/concept-field-test.yml`
- **Decision effect:** gives adopters a structured path to report prospective, retrospective, positive, null, negative, and confounded results from real work
- **Scope:** active doctrine in this starter; situational understanding is the initial worked protocol, not a universal or mandatory checklist
- **Boundary:** public reports must contain sanitized minimum-necessary evidence, exclude runtime state and dumps, and remain inside already-granted authority
- **Correction:** independent review found the direct issue form had a weaker privacy warning than the protocol and could encourage reconstructed predictions or causal overstatement; the form and validator were hardened before treating the release as complete
- **Remaining uncertainty:** reports may be self-selected, correlated, or influenced by extra attention; volume alone does not establish general validity

## 2026-07-30 — Added situational-understanding diagnostics

- **Doctrine:** `doctrine/decisions/decision-quality-under-uncertainty.md`
- **Decision effect:** distinguishes perception, comprehension, projection, decision, execution, and feedback failures so agents can repair the earliest supported failed layer
- **Scope:** consequential dynamic work where changing state or projection can alter the action; not a mandatory checklist for routine factual or mechanical tasks
- **Evidence:** `evidence/sources/situational-awareness-munir-aved-blasch-2022.md`
- **Remaining uncertainty:** language-model transfer is an operational extrapolation and should be narrowed or removed if it adds ceremony without changing observation, action, verification, or repair

## 2026-07-31 — Strengthened cross-domain operating safeguards

- **Doctrine:** Right-Sized Change, Decision Quality, External Capability Governance, Decision Records, Strategic Response, Information Placement, and Governance
- **Decision effect:** adds compact bounds, negative triggers, evidence/value separation, competence checks, sensor minimization, and exception conditions to the active doctrine users consult directly
- **Scope:** portable cross-domain judgment only; no personal product contract, machine state, live integration status, or archived source-agent authority
- **Correction:** file preservation or destination mapping does not by itself prove that behavior-changing meaning remains active; compare triggers, boundaries, exceptions, failure modes, confidence qualifiers, and implementation ownership proposition by proposition
- **Remaining uncertainty:** the additions are structurally and semantically reviewable but remain guidance rather than proof of improved outcomes; future field evidence should narrow or remove wording that adds ceremony without changing decisions or repairs

## 2026-07-31 — Clarified runtime enforcement and identity updates

- **Architecture:** `README.md`, `RUNTIMES.md`, `SOUL.md`, Governance, Least-Privilege Capability Access, and Permissions, Controls, and Discretion
- **Decision effect:** distinguishes prompt policy from technical containment, assigns identity-version comparison to installation or runtime integration, limits session-start comparison to runtimes with the required state, and gives adopters one paired mechanical-versus-decision example
- **Identity change:** the public starter SOUL now separates stewardship's relational posture from the operative access boundary and keeps a compact causal reflex while detailed causal analysis remains doctrine-owned
- **Correction:** independent mutation review found that the initial validator guarded headings and slogans but allowed removal or inversion of load-bearing update and causal semantics; focused canaries now reject those mutations
- **Remaining uncertainty:** technical enforcement and identity provenance remain runtime-specific, and field use may show that the paired example or update contract needs narrower wording or stronger integration guidance
