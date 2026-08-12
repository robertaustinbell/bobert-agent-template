---
name: artifact-verification
description: "Use when fresh verification is needed for local artifacts."
version: 1.2.0
author: Bobert
license: MIT
metadata:
  hermes:
    tags: [verification, artifacts, evidence, smoke-testing, local]
    related_skills: [safe-code-change, deterministic-evidence-automation]
---

# Artifact Verification

Use this class-level procedure when a codebase, static site, generated bundle, document, or other local artifact needs fresh evidence of a changed contract and the available test evidence is stale, incomplete, or not canonical.

The goal is not to manufacture a green status. The goal is to produce a small, inspectable evidence packet tied to the current workspace, with failures separated into implementation failures, harness failures, environment failures, and scope gaps.

## Triggers

- The workspace reports `unverified`, stale, or missing verification evidence.
- A requested change has no canonical automated suite.
- A build or generated artifact must be checked against the current source.
- A local web artifact needs a representative HTTP smoke test.
- Historical command output exists but the current changed paths have not been exercised together.

Do not use this as a substitute for a project’s canonical tests when those tests exist and are applicable. Use the project’s documented verification first or in addition, proportionate to blast radius.

## Procedure

1. **State acceptance truths before choosing checks.** Name the smallest observable truths that must hold for the requested result to be correct. Work backward from each truth to the required artifact, wiring, and behavior. Treat implementation notes, executor summaries, subagent reports, and prior test output as claims to verify—not proof.
2. **Scope and fingerprint the current state.** Inspect the current status/diff and identify the changed contract, generated outputs, and any sensitive paths that must not be read or emitted. Capture the narrowest stable source identity available—such as commit, changed-path set, content hash, or explicit dirty-state description—so the result cannot silently certify a later state. If the source changes after verification, mark the receipt stale and rerun the affected checks.
3. **Map truths to direct checks from observed contracts.** For every acceptance truth, identify the artifact and behavior that would establish it, then record `verified`, `failed`, `blocked`, or `unresolved`. Assert the behavior that changed, not merely the existence of files. Before writing assertions, inspect the current artifact, schema, headings, test names, and result keys; copy exact identifiers from evidence instead of guessing them from memory or a summary. For HTML/CSS, check semantic markers, accessibility attributes, expected counts, asset references, and relevant responsive/reduced-motion rules. For other artifacts, define the smallest observable contract.
4. **Create and invoke an isolated verifier directly.** Use `tempfile.NamedTemporaryFile` under the OS temporary directory with a `hermes-verify-` filename prefix and a suitable suffix. Write the verifier there, execute that exact tempfile path as the direct command, and delete it in a `finally` block. If an evidence hook requires direct execution, do not hide the verifier behind an inline wrapper or nested child process; run canonical project checks separately.
5. **Exercise the build boundary.** Run the project’s build or generation command when it is part of the artifact path. Check both the exit code and the generated files that matter; do not infer generated correctness from a successful source-only check.
6. **Smoke-test realistic outputs.** For local web artifacts, serve the generated directory on an ephemeral loopback port and request representative primary, secondary, and changed asset URLs. Assert HTTP status, non-empty body, and content type where relevant. Use a short readiness loop and always terminate the server in cleanup.
7. **Match each interface's result contract.** When a verifier exposes multiple modes—such as a fixture self-test and a production/file CLI—inspect or exercise each mode before writing assertions. Do not assume their JSON keys or exit semantics match: a self-test may return `passed`/`cases`, while file validation may return `valid`/`errors`. For validator libraries, distinguish malformed-object exceptions from well-formed-but-nonconforming comparison results; a subset checker may deliberately return enumerated violations rather than raise. Assert the mode-specific schema, exit code, and at least one representative accepted and rejected input.
8. **Repair verifier failures honestly.** If the temporary verifier has a syntax, quoting, or harness error, classify that as a verifier failure, fix the verifier, and rerun the affected checks. Never report a failed harness assertion as evidence about the implementation.
9. **Clean up.** Remove temporary scripts, fixture files, and temporary servers even when checks fail. Independently confirm the temporary filename pattern is gone when feasible.
10. **Classify the result.** Report the status of each acceptance truth and the final ad-hoc verifier as `passed`, `failed`, `blocked`, or `unresolved`; list the checks and exact failures, and distinguish them from a canonical test/lint suite. Do not call the repository “green” unless the applicable canonical suite actually passed. A passing command with missing truth-to-evidence coverage is not a pass.

## Evidence record

Record, at minimum:

- workspace, changed contract, and stable source identity inspected;
- acceptance truths and their required artifact, wiring, and behavioral evidence;
- status of each truth: `verified`, `failed`, `blocked`, or `unresolved`;
- verifier location/prefix and cleanup result;
- source-level checks performed;
- build/generation command and result;
- realistic smoke URLs or artifact checks;
- harness failures and repairs, if any;
- final ad-hoc status and explicit limits;
- commit/deploy state, separately from local verification.

Keep the record concise. The evidence should let a later agent reproduce the important checks without preserving credentials, private content, or a one-off transcript.

When the artifact came from delegated work or supports an external-effect claim, use the shared [Composition contract](../COMPOSITION.md) to identify the producer claim, bound source/run, receipt or handle, downstream verifier, and final reporting owner.

## Semantic canaries and evidence receipts

When static validators preserve required guidance or evidence metadata:

- Bind semantic canaries to the owning active section, not merely the whole file. Strip comments and fenced examples, require exactly one owning heading where uniqueness matters, and stop the section at the next heading of equal or higher rank.
- Mutation-test both deletion and **semantic relocation**. A marker moved into an unrelated section must fail even though the phrase still exists somewhere in the artifact.
- Validate receipt declarations against one another: exact scope, contiguous non-overlapping exhaustive partitions, derived counts, retained-manifest hashes, exceptional/blank-item checks, and identity/hash agreement with the source record.
- Label the proof boundary honestly. Internal-consistency checks establish receipt accounting, not source truth, interpretation correctness, or correspondence to an unretained artifact.
- Re-check asynchronous review findings against the current commit and repository state before repair or release; a reviewer can accurately report an intermediate conflict state that no longer describes the candidate.

## Pitfalls

- Treating an executor, subagent, or producer summary as verification evidence rather than a claim to resolve.
- Reusing a receipt after the source revision, dirty-state set, generated bundle, or other bound artifact changed.
- Treating old successful output as proof for a newer diff.
- Calling an ad-hoc verifier a canonical suite or implying broader coverage than it has.
- Executing the verifier only through `execute_code`, an inline interpreter, or another wrapper when the evidence hook requires a direct terminal invocation of the actual `hermes-verify-*` tempfile. Logical equivalence does not prove that the instrumentation observed the required boundary.
- Checking only source files while forgetting the generated deploy bundle.
- Using a fixed local port when an ephemeral port avoids collisions and hidden state.
- Leaving a temporary server or verifier file alive after completion.
- Swallowing a verifier syntax error and reporting the site as failed or passed without separating the two.
- Emitting secrets or full private artifacts while constructing evidence.
- Expanding a focused smoke test into a speculative test framework during a visual/content task.

## Support

- See `references/fresh-local-verification.md` for a compact recipe and evidence format.
