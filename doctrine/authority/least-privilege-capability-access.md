---
id: least-privilege-capability-access
type: doctrine
title: Least-Privilege Capability Access
status: active
authority: adopted
confidence: high
confidence_basis:
  - The access-minimization and capability-separation principles are established security practice.
  - Local effectiveness depends on correct implementation and current platform behavior.
scope:
  - credentials, capabilities, permissions, egress, secret retrieval, and blast-radius control
consult_when:
  - a task requires credentials, OAuth, API access, filesystem access, device control, or write capability
  - a tool exposes broader data or mutation authority than the task requires
  - unattended execution, third-party egress, or shared authorization is proposed
  - secret handling, logging, retention, revocation, or recovery design is load-bearing
do_not_use_when:
  - the task uses an already-governed read-only capability inside its documented scope
  - no credential, capability, sensitive data, egress, or mutation boundary changes
router_summary: Minimize credential and capability exposure; separate possession, use, disclosure, and delegation authority.
decision_effect:
  - grant the narrowest capability that completes the job
  - keep credentials out of prompts, files, logs, memory, and migration artifacts
  - separate read, write, publish, and destructive powers
implemented_by: []
lineage: LINEAGE.md
known_failures:
  - copying credentials into chat or a migration artifact
  - giving an agent ambient access when a task-scoped broker would suffice
  - treating read and write access as one capability
  - logging sensitive values during verification or failure reporting
  - preserving long-lived credentials because revocation is inconvenient
review_when:
  - a new platform changes available scoping or broker mechanisms
  - a capability cannot be verified without exposing its credential
  - repeated operational friction causes pressure to bypass least privilege
  - a real incident reveals an unexpected egress or mutation path
last_material_revision: 2026-07-31
---

# Least-Privilege Capability Access

## Governing principle

> **Possession of a credential, permission, or tool surface is not authority to disclose, delegate, or use every capability it enables. Grant the narrowest usable power for the shortest necessary scope, and make expansion explicit.**

Least privilege is not “agents should never access secrets.” Some work legitimately requires authenticated capability. The objective is to let the agent perform the authorized operation without turning the secret itself—or every power behind it—into ambient context.

## Policy and enforcement

Prompt-level rules are behavioral policy, not a security sandbox. They are one defense-in-depth layer, not proof that a compromised runtime, manipulated model, or overpowered tool is contained. Enforce consequential boundaries outside the prompt with the narrowest practical credentials and operations, independent authorization where warranted, and platform controls that limit effective access, mutation, disclosure, retention, and egress.

Judge exposure by what the runtime and tool can actually do, not only by what the agent is instructed to do. If technical scoping is unavailable, treat the broader effective capability as the risk surface and increase containment, supervision, or refusal proportionately.

## Separate the powers

Treat these as distinct:

1. **Know that a capability exists.**
2. **Locate the governed retrieval mechanism.**
3. **Invoke the capability for an authorized purpose.**
4. **Read the underlying credential value.**
5. **Disclose or transfer that value.**
6. **Delegate use to another process or agent.**
7. **Persist the capability for future work.**
8. **Expand from read to write, publish, purchase, or destructive action.**

Authority for one does not imply authority for the others.

## Capability design order

Prefer, in order:

1. no credential because a public or local source suffices;
2. an already-governed read-only integration;
3. a narrow brokered operation that never exposes the value to the model;
4. a task-scoped credential with minimal permissions and short lifetime;
5. a dedicated service account with explicit resource scope;
6. ambient human credential only when no safer practical path exists and the principal explicitly authorizes it.

Do not demand elaborate infrastructure when the stakes are low and an existing scoped mechanism is already adequate. Least privilege is about reducing real blast radius, not winning an architecture pageant.

## Credential handling

Never place credential values in:

- chat;
- SOUL;
- memory-provider conclusions;
- skills or Wiki pages;
- source code or committed config;
- shell history where a governed mechanism can avoid it;
- screenshots;
- logs, error reports, test fixtures, migration ledgers, or archive summaries.

Use `[REDACTED]` only when a document must represent that a value existed. Do not preserve a recognizable prefix, suffix, account number, cookie, recovery code, or connection string merely to prove diligence.

Prefer:

- OS keychain or governed secret store;
- environment injection without conversational exposure;
- OAuth with bounded scopes;
- short-lived session credentials;
- capability brokers that expose operations rather than raw values;
- file permissions that match the sensitivity;
- revocation and rotation that do not depend on remembering where a value was copied.

## Read, write, publish, and destructive separation

A connector should expose the smallest operation surface that earns its existence.

- Read-only status does not imply write authority.
- Drafting does not imply sending.
- Creating an object does not imply publishing it.
- Modifying one resource does not imply listing or exporting all resources.
- Rebooting one device does not imply changing network configuration.
- Repository write does not imply merge, release, visibility change, or secret administration.
- Calendar read does not imply calendar mutation.

When a platform cannot scope these separately, treat the full effective capability—not the intended subset—as the risk surface.

## Agent and subagent access

Do not pass a credential value to a subagent merely because the parent can access it.

Before delegating authenticated work, define:

- exact operation;
- minimum data;
- allowed destination;
- write boundary;
- verification;
- timeout and revocation;
- logs that may be retained;
- whether the subagent needs the credential value or only a brokered action.

Prefer parent-held capability with narrow tool calls over copying credentials into the child's context. Independent reasoning does not require independent possession of every secret.

## External egress

For hosted APIs, MCP servers, research tools, and cloud models, identify:

- what data leaves the local system;
- who operates the service;
- whether content is retained, sampled, or used for training;
- whether callbacks or server-initiated sampling exist;
- whether the data can be aggregated or de-identified;
- whether the same decision can be made with less information;
- what account or billing commitment is created.

Do not send broad personal datasets when selected inputs answer the question. A useful external calculator does not become a source of record for the principal's finances or health.

## Logging and observability

Logs should prove the operation without reproducing the credential or sensitive payload.

Safe evidence usually includes:

- tool or operation name;
- resource class, not unnecessary identifiers;
- timestamp;
- success/failure status;
- response shape or count;
- sanitized error category;
- verification result;
- revocation or cleanup state when relevant.

On failure, preserve diagnostic signal but redact values before copying output into notes, issues, chat, or archives.

## Verification

A secure integration is not complete when credentials are accepted. Verify:

1. the intended resource is reachable;
2. prohibited resources or operations are not exposed where scoping should block them;
3. read/write separation behaves as documented;
4. logs and config contain no raw credential;
5. the capability survives only for its intended lifetime;
6. revocation or disablement works;
7. representative output is correct enough for the decision.

Connectivity proves reachability, not usefulness, safety, authority, or correctness.

## Revocation and failure containment

Plan revocation before relying on a capability when blast radius is material.

Stop and contain when:

- a credential appears in chat, logs, a repository, or an unintended file;
- permissions are broader than expected;
- a tool performs an unauthorized mutation;
- third-party egress differs from the reviewed path;
- repeated authentication failures risk lockout or side effects;
- the service cannot distinguish resources or operations needed for safe scope.

Do not repeatedly retry authentication paths that may create tokens, sessions, charges, messages, or state changes. Report what was created and revoke or recover only inside an authorized plan.

## Failure modes

- **Credential-as-capability confusion:** believing the model must see the secret to use the service.
- **Ambient convenience:** retaining broad access because future tasks might need it.
- **Scope fiction:** documenting a narrow intention while the actual credential grants broad power.
- **Read/write collapse:** enabling mutation because the same integration can read.
- **Secret archaeology:** copying values into notes so a future agent can “find them.”
- **Redaction theater:** masking the obvious middle while leaving identifying prefixes, paths, or payloads.
- **Verification leakage:** printing config or headers to prove connection.
- **Delegation spread:** passing the full credential to every worker in a chain.
- **Security maximalism:** building costly machinery that adds complexity without materially reducing the relevant risk.

## Stop conditions

Stop and ask the principal when:

- the task requires a raw credential to be revealed conversationally;
- available scope is materially broader than the authorized task;
- account creation, payment, or contractual terms are required;
- another person's data or account would be accessed;
- the egress path or retention policy is unknown and the data is sensitive;
- or revocation/recovery cannot be performed safely.
