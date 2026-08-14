---
id: decision-records-and-operational-documentation
type: operating-thought
title: Decision Records and Operational Documentation
status: active
authority: advisory
confidence: high
confidence_basis:
  - The guidance reflects established operational documentation practice and direct local failures from stale duplication, missing rationale, and unauditable changes.
scope:
  - decision records, operational documentation, claim-to-evidence traceability, canonicality, generated views, and change traceability
consult_when:
  - making a durable architecture, authority, integration, product, or governance choice
  - a consequential recommendation, report, audit, or release depends materially on evidence-bearing claims
  - a future operator needs rationale, constraints, rollback, or ownership to change the system safely
  - documentation is duplicated, stale, or competing with a canonical source
  - a migration must prove semantic survival rather than merely preserve files
  - consequential analysis may become stale because the inspected system changes before execution
do_not_use_when:
  - the task is temporary session work with no durable decision or handoff
  - a canonical source already answers the question and another summary would only drift
  - routine authoritative-source lookup or reversible low-stakes work would not become easier to verify or repair through a formal record
router_summary: Record durable choices and consequential evidence claims at the minimum detail needed for safe future change, verification, repair, and rollback.
decision_effect:
  - preserve rationale and constraints without copying every implementation detail
  - connect load-bearing claims to inspectable evidence and audit coverage separately from support correctness
  - make canonical versus generated versus historical status explicit
  - stop documentation when additional prose no longer improves future action
implemented_by: []
lineage: LINEAGE.md
known_failures:
  - documentation theater that describes activity but not decisions
  - polished conclusions whose citations exist but do not support the wording, scope, result, specification, or method claimed
  - duplicate summaries drifting from their source of record
  - decision records missing authority, alternatives, assumptions, or reconsideration triggers
  - generated indexes edited as canonical prose
  - analysis applied to a materially different system state than the one inspected
review_when:
  - future work repeatedly cannot determine why a choice was made
  - claim-to-evidence records add ceremony without catching errors or improving repair
  - documentation survives while the behavior it describes changes
  - maintaining the document costs more than its decision or recovery value
  - a generated view and canonical source disagree
last_material_revision: 2026-08-06
---

# Decision Records and Operational Documentation

## Governing principle

> **Document what future action needs: ownership, decision, rationale, constraints, evidence, verification, rollback, and revision conditions. Do not create prose merely to prove that documentation happened.**

Documentation earns its keep when it lowers future coordination cost, prevents unsafe change, preserves a hard-won distinction, or makes recovery possible.

## Decide what kind of record is needed

| Need | Record |
|---|---|
| Why a durable choice was made | Decision record |
| How to execute repeatably | Skill |
| What is currently true | Source of record or configuration |
| Cross-domain judgment | Operating thought |
| What happened in one application | Evidence case or material log entry |
| Historical explanation | Archive |
| Temporary work state | Session/task list |

Do not turn one kind into another. A README is not a substitute for live configuration; a session transcript is not a decision record.

## Minimum decision record

A durable record should usually answer:

1. **Decision:** what was chosen?
2. **Owner and scope:** who authorized it and where does it apply?
3. **Context:** what problem required a decision?
4. **Constraints:** what boundaries or operational realities mattered?
5. **Alternatives:** what materially different options were considered?
6. **Rationale:** why did this option win?
7. **Consequences:** what costs, risks, dependencies, and follow-on work result?
8. **Verification:** what proves the architecture is actually in effect?
9. **Rollback or exit:** how can it be reversed or retired when relevant?
10. **Reconsideration:** what evidence or condition should trigger review?

Not every record needs a novel. Include detail in proportion to consequence and future ambiguity.

Design for the next reader and task. Start with the decision, owner, consequence, and next action; let readers zoom into rationale, evidence, and mechanics only as needed. Prefer plain text when sequence, ownership, and branching are already clear. Use a diagram only when spatial structure, state transitions, interfaces, or concurrency would otherwise be materially harder to understand, and keep the decisive labels readable without decorative tooling.

## Operational documentation

A repeatable operator needs:

- purpose and trigger;
- prerequisites;
- authoritative paths and systems;
- exact procedure where mechanics matter;
- side effects and approval boundaries;
- secrets handling;
- verification;
- common failure modes;
- recovery and stop conditions;
- current owner.

Commands belong in skills or operational runbooks, not universal operating thought.

## Canonical, generated, mirrored, and historical

Every maintained document should make its role legible:

- **canonical:** edited source that governs its subject;
- **generated:** reproducible derivative; never edited independently;
- **mirror:** mechanically synchronized continuity copy;
- **snapshot:** point-in-time backup of another canonical source;
- **evidence:** preserved observation or source;
- **historical:** non-normative prior state.

If a reader can reasonably mistake a derivative for canonical authority, fix the document—not the reader.

## Semantic traceability

Migrations and consolidations must preserve behavior-changing meaning, not merely files.

Trace every:

- positive trigger;
- negative trigger;
- boundary;
- exception;
- failure mode;
- stop condition;
- scope qualifier;
- source qualifier that changes confidence or application;
- implementation link;
- reconsideration condition.

A line-by-line copy is not required. A proposition-level destination is.

## Source and evidence links

Cite the source needed to evaluate the claim. Preserve author or package identity only when provenance changes meaning, confidence, or scope.

Do not:

- cite a source you did not inspect;
- convert an external source's recommendation into the principal's policy;
- treat a worked case as universal proof;
- manufacture examples to make a framework look mature;
- paste private source contents when a pointer suffices.

## Consequential claim-to-evidence audit (candidate)

For consequential recommendations, reports, audits, releases, quantitative results, or synthesized conclusions, build claim-to-evidence links while investigating and producing the work rather than reconstructing plausible support after the prose is polished. A claim is **load-bearing** when its falsity would materially change the recommendation, decision, reported result, or verification conclusion.

For each load-bearing claim, retain only what makes it inspectable and repairable:

- the claim's exact wording and scope;
- a stable source or artifact identity plus a decision-relevant locator such as a page, section, line range, result row, log span, run identifier, or content hash;
- whether support is direct, derived, inferred, or absent;
- limitations, contradiction, and confidence;
- the verification method and result, including whether review was genuinely independent;
- what evidence would change or retire the claim.

Audit **completeness** and **correctness** separately. Completeness asks whether every load-bearing claim in the final output resolves to evidence or is explicitly marked unsupported; inspect the output for claims missing from the record rather than checking only records already created. Correctness asks whether the declared evidence supports the claim's actual wording, scope, and strength.

Record each relevant audit class as `performed`, `not applicable — rationale`, or `blocked — reason`:

1. **Reference:** verify source existence, identity, locator, and attributed support.
2. **Result:** independently rerun decision-bearing calculations, queries, tests, or code when feasible.
3. **Specification:** test the actual objective and constraints rather than a convenient proxy or evaluator loophole.
4. **Method–artifact:** compare described methods, configuration, and procedures with what actually executed.

When evidence does not carry the claim, preserve the mismatch and narrow the wording, label the inference, or mark the claim unsupported. Do not make the conclusion appear cleaner by erasing contradiction or uncertainty. A second pass by the same model can detect discrepancies but is not independent proof.

Do not impose this as a universal ledger. Routine authoritative-source lookup, casual explanation, and reversible low-stakes work should not incur formal recordkeeping when it would not improve verification or repair. Commands, schemas, and automation belong in runtime-specific skills or runbooks.

This candidate is adapted from the Chain-of-Evidence approach described in Google Research's [Science One Framework](https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/) and Meng et al.'s [ScientistOne preprint](https://arxiv.org/abs/2605.26340). It transfers a bounded verification practice, not the paper's research pipeline or a claim that traceability eliminates hallucination.

## Versioned analysis of evolving systems

When the inspected system can change before a consequential recommendation is executed, bind the analysis proportionally to:

- the observed version or material state;
- observation time when freshness matters;
- the analysis boundary and its observed, stipulated, inferred, or unresolved status when load-bearing;
- assumptions about what remains stable;
- changes that would invalidate the recommendation;
- the current-state check required before execution.

Before acting, compare current canonical state with the analyzed state. Revalidate the reasoning branches affected by material drift; do not blindly apply stale analysis, and do not restart unaffected analysis merely because some state changed. A document can faithfully preserve an earlier observation without remaining current authority for the present system.

## Documentation stop rule

Stop writing when the next section will not materially improve:

- decision quality;
- safe operation;
- verification;
- recovery;
- ownership;
- or future modification.

Prefer links to maintained canonical sources over repeated explanation. Delete stale duplication before adding another summary.

## Maintenance

When behavior changes:

1. update the canonical owner;
2. regenerate derivatives;
3. refresh mirrors or snapshots according to policy;
4. repair links;
5. archive superseded rationale when it retains value;
6. remove stale competing prose;
7. verify a clean checkout or real operator can still act.

## Failure modes

- **Documentation theater:** activity and headings without decision effect.
- **Orphan rationale:** current behavior exists but no one knows why.
- **Canonicality blur:** two files appear equally authoritative.
- **Generated-source inversion:** derivative edits are overwritten or compete with source.
- **Snapshot drift:** a continuity copy is mistaken for current truth.
- **Transcript retention:** raw conversation stands in for maintained knowledge.
- **Page-count Goodharting:** more notes are treated as more understanding.
- **Migration-by-file-count:** consolidation is declared successful while exceptions or negative triggers disappear.

## Stop conditions

Stop or ask the principal when:

- the owner or authority of a policy cannot be identified;
- preserving the needed rationale would require duplicating sensitive data;
- two canonical documents conflict;
- the receiving operational home does not exist or cannot be verified;
- or documentation is being created only to satisfy a quota or appearance of completeness.
