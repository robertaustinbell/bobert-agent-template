---
id: decision-records-and-operational-documentation
type: doctrine
title: Decision Records and Operational Documentation
status: active
authority: advisory
confidence: high
confidence_basis:
  - The guidance reflects established operational documentation practice and direct local failures from stale duplication, missing rationale, and unauditable changes.
scope:
  - decision records, operational documentation, canonicality, generated views, and change traceability
consult_when:
  - making a durable architecture, authority, integration, product, or governance choice
  - a future operator needs rationale, constraints, rollback, or ownership to change the system safely
  - documentation is duplicated, stale, or competing with a canonical source
  - a migration must prove semantic survival rather than merely preserve files
do_not_use_when:
  - the task is temporary session work with no durable decision or handoff
  - a canonical source already answers the question and another summary would only drift
router_summary: Record durable choices and operational knowledge at the minimum detail needed for safe future change, ownership, verification, and rollback.
decision_effect:
  - preserve rationale and constraints without copying every implementation detail
  - make canonical versus generated versus historical status explicit
  - stop documentation when additional prose no longer improves future action
implemented_by: []
lineage: LINEAGE.md
known_failures:
  - documentation theater that describes activity but not decisions
  - duplicate summaries drifting from their source of record
  - decision records missing authority, alternatives, assumptions, or reconsideration triggers
  - generated indexes edited as canonical prose
review_when:
  - future work repeatedly cannot determine why a choice was made
  - documentation survives while the behavior it describes changes
  - maintaining the document costs more than its decision or recovery value
  - a generated view and canonical source disagree
last_material_revision: 2026-07-31
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
| Cross-domain judgment | Doctrine |
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

Commands belong in skills or operational runbooks, not universal doctrine.

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
