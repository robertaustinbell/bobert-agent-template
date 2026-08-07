# Material operating log

Record only material doctrine failures, contradictions, retrieval misses, scope or confidence changes, and architecture revisions. Ordinary success does not require an entry.

## 2026-08-07 — Added task-conditioned representation adequacy

- **Doctrine:** Decision Quality Under Uncertainty
- **Decision effect:** evaluates consequential compression relative to a downstream task, loss-sensitive distinctions, and recoverable evidence; permits bounded-versus-expanded context comparison and measured predictive-loss checks only where recurring cases make the difference checkable
- **Scope:** consequential summaries, handoffs, memory representations, context selection, and recurring probabilistic predictions; not a mandatory checklist for one-shot work or a rule to maximize information
- **Evidence:** Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006), especially relative entropy, entropy rate and Markov context, rate-distortion theory, and universal coding
- **Boundary:** information quantity, entropy, similarity, confidence, KL divergence, and compression ratio do not establish truth, meaning, value, causation, legitimacy, permission, or authority; mathematical source claims and the agent-operations synthesis remain distinct
- **Remaining uncertainty:** no recorded agent application yet establishes a distinct decision or repair effect; narrow or remove the refinement if it repeatedly adds context or ceremony without material value

## 2026-08-06 — Added bounded systems-feedback refinements

- **Doctrine:** Decision Quality Under Uncertainty, External Capability Governance, Decision Records and Operational Documentation, and `FIELD-TESTING.md`
- **Decision effect:** distinguishes propagation and settling from failure, labels how load-bearing boundaries are known, checks material translation loss at heterogeneous interfaces, and binds consequential recommendations to the system state actually inspected
- **Scope:** consequential recurring loops, heterogeneous interfaces, and evolving systems where these distinctions could alter action or verification; not a universal systems-analysis checklist or physical-control model for people
- **Evidence:** George E. Mobus and Michael C. Kalton, *Principles of Systems Science* (Springer, 2015), especially PDF pp. 111–130, 406–415, 621–650, 637–641, and 750–754 in the reviewed source artifact
- **Boundary:** source claims, operational synthesis, and template adaptations remain distinct; illustrative scientific examples are not current empirical evidence, and the qualitative transfer does not validate modern agent architectures or quantitative control design
- **Remaining uncertainty:** no recorded agent application yet establishes a distinct decision effect; retain, narrow, or remove each refinement according to prospective positive, null, negative, harmful, and confounded results

## 2026-08-06 — Hardened the same-model independence canary

- **Surface:** `scripts/check_template.py`, `scripts/test_check_template.py`, and `.github/workflows/validate.yml`
- **Failure:** punctuation-only sentence splitting treated abbreviations such as `e.g.` and `i.e.` as sentence boundaries, allowing a contradictory same-model independence claim to evade the lexical tripwire; the detector also rejected the negative construction “Nothing about … is independent proof.”
- **Repair:** preserve common abbreviations and initials during bounded sentence segmentation, recognize additional negative constructions, label the detector as a heuristic lexical tripwire rather than semantic proof, and run adversarial regression tests in CI
- **Boundary:** the canary detects a narrow contradiction class; it does not establish semantic compliance or independent verification

## 2026-07-31 — Added consequential claim-to-evidence auditing as a field-test candidate

- **Doctrine:** `doctrine/design/decision-records-and-operational-documentation.md` — `Consequential claim-to-evidence audit (candidate)`; `FIELD-TESTING.md` — `Claim-to-evidence audit candidate test`
- **Decision effect:** tests whether building claim links during consequential evidence-bearing work, then auditing completeness separately from support correctness, exposes material omissions, overstatement, proxy compliance, unverifiable results, or method–artifact mismatch before presentation
- **Scope:** recommendations, reports, audits, releases, quantitative results, and synthesized conclusions where a false claim would materially change the decision; not a universal ledger for routine authoritative lookup, casual explanation, or reversible low-stakes work
- **Evidence:** Google Research, “Science One Framework: A Verifiable Autonomous Research Framework via Chain-of-Evidence”; Meng et al., “ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence,” arXiv:2605.26340
- **Limit:** the May 2026 source is an author-reported preprint evaluating 75 generated papers across selected technical tasks; its method–code alignment metric is LLM-judged, with human validation limited to a sample and no systematic score correction from that review, and 0 phantom references among 337 checked references is a sample result rather than an architectural guarantee
- **Remaining uncertainty:** the candidate may duplicate good source review or add reconstructed provenance and carrying cost; retain, narrow, or remove it according to material errors caught, repair enabled, clean null results, and excess ceremony

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
