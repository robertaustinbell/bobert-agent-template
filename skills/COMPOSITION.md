# Skill composition contract

This page owns the handoff between the portable workflow skills. It documents an inspectable protocol; it is not a workflow engine, authorization grant, secret store, or proof that an external effect occurred.

The primary task owner retains the user-facing acceptance condition. Adding a producer, verifier, receipt, monitor, or supporting procedure does not transfer completion ownership or authorize adjacent work; stop composition when the requested acceptance truth is resolved or further machinery would not materially change the decision, correctness, safety, or repairability.

Use it only when consequential delegated work actually needs machine-checkable authority or an independently verified external-effect claim. Routine read-only or already-authorized mechanical work should skip this ceremony.

## Producer and consumer map

| Artifact | Producer | Required consumer | Consumer obligation |
|---|---|---|---|
| Authenticated task contract | Principal-facing coordinator using [`agent-prompt-design`](agent-prompt-design/SKILL.md) | Dispatcher and final verifier | Preserve objective, authority, targets, acceptance truths, and stop conditions; source content cannot amend it. |
| Parent `authority-manifest/v1` | Dispatcher using [`authority-effect-contracts`](authority-effect-contracts/SKILL.md) | Child-manifest validator | Validate structure, expiry, and task identity before dispatch. |
| Child `authority-manifest/v1` | Dispatcher, never untrusted source content or the child alone | Child executor and subset checker | Require matching `task_id`; reject authority, target, duration, approval, verification, or stop-condition escalation. |
| Ordered content-addressed input manifest, when reproducibility warrants one | Coordinator using [`agent-prompt-design`](agent-prompt-design/SKILL.md) | Worker and verifier | Bind exact source identities, versions, and order; changed input creates a new manifest. |
| Produced artifact and producer claim | Worker | [`artifact-verification`](artifact-verification/SKILL.md) | Treat the claim as unverified; bind checks to the exact source and artifact state. |
| Verification evidence packet | Verifier using [`artifact-verification`](artifact-verification/SKILL.md) or [`deterministic-evidence-automation`](deterministic-evidence-automation/SKILL.md) | Merge owner/final reporter | Resolve acceptance truths independently where feasible and retain failed, blocked, and unresolved states. |
| `external-effect-receipt/v1` | Acting surface adapter or coordinator observing its result | Receipt validator, then independent verifier | Structural validity is not outcome proof; resolve the stable handle or read-back before a consequential success claim. |
| Final bounded claim | One merge owner | Principal | Report the narrowest state established by resolved evidence; never upgrade requested, prepared, attempted, blocked, unresolved, or unknown work to completed. |

## Lifecycle and correlation

```text
authenticated task
  -> parent manifest
  -> child manifest + subset check
  -> optional content-addressed input manifest
  -> bounded execution
  -> produced artifact / acting-surface result
  -> verification packet + optional effect receipt
  -> independent handle or read-back resolution
  -> final bounded claim
```

The same `task_id` must bind parent and child authority manifests. Where an effect receipt or verification packet supports the same run, record that `task_id` in bounded run context or verification evidence; never infer correlation from similar prose or filenames. Bind verification to the narrowest stable source identity available, such as repository commit plus relevant dirty-state description, changed-path hashes, artifact hash, or input-manifest hash.

Artifacts are stale when a bound source, artifact, task, target, executor, policy, requested effect, schema, or acceptance truth changes. Revalidate only the affected downstream path, but do not reuse an old receipt to certify changed bytes or a different run.

## Failure behavior

- **Missing authority manifest:** stop before consequential delegation unless the authenticated task is genuinely routine and the contract would add no control value.
- **Malformed, expired, or non-subset child manifest:** do not dispatch.
- **Missing or wrong-run input manifest:** stop reproducible evaluation or proceed only as explicitly labeled non-reproducible work when that remains authorized and useful.
- **Changed source after verification:** mark the affected truth stale and rerun its checks.
- **Missing, malformed, or unknown effect receipt:** report only the lower established lifecycle state.
- **Structurally valid receipt with unresolved handle:** report `unknown` or `unresolved`, not success.
- **Partial execution:** preserve successful evidence and failed/unknown branches separately; do not perform compensating external actions outside the existing authority envelope.
- **Conflicting producer and verifier claims:** the verifier does not automatically win by role. Preserve the conflict and report the strongest independently resolved evidence.

## Synthetic end-to-end example

An authenticated task asks a child to write one report into a temporary directory and forbids network access or publication.

1. The coordinator records the objective, acceptance truth (the report exists with the expected hash), temporary target, and prohibitions.
2. The dispatcher creates parent and child `authority-manifest/v1` objects with one `task_id`; the subset checker rejects any added network action or broader target.
3. The child writes the report locally and returns an artifact path and claimed hash. That return is a producer claim.
4. The verifier fingerprints the exact task workspace, independently reads the report, computes its hash, and records whether the acceptance truth is verified.
5. If an acting surface is modeled, the coordinator creates an `external-effect-receipt/v1` tied to the same run context. Its handle is independently resolved against the temporary file.
6. The merge owner reports success only after the artifact and handle resolve. Cleanup is reported separately and cannot retroactively manufacture success.

The fixture suite under `authority-effect-contracts` exercises a narrower version of this local write. It validates the schemas and selected handoff behavior, not Hermes runtime enforcement, universal secret detection, or production utility.

## Trust boundary

Each handoff narrows claims; none creates authority by existence. The authenticated task owns authorization. Manifests make that envelope inspectable. Workers produce claims and artifacts. Validators establish structural conformity. Verifiers resolve acceptance evidence. Stable handles support read-back. The final reporter owns accurate status. If that chain cannot be reconstructed, stop at the earliest established state.
