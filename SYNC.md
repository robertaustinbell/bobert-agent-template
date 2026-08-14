# Synchronization model

This repository is a curated public projection of a private agent architecture. It is deliberately **not** a mirror.

## Update trigger

Every material change to the source agent's constitutional identity, governance, active operating thought, routing, or reusable operating principles receives a public-impact review in the same work cycle.

The review has two valid outcomes:

1. **Transferable change:** generalize it, update this repository, run the public-boundary checks, publish it, and verify a fresh clone.
2. **No public delta:** keep the private change private because it concerns personal continuity, local capabilities, domain records, evidence, paths, permissions, or history rather than reusable architecture.

No empty parity commit is required. Commit counts and histories are intentionally independent.

## Checkpoint and release policy

Continuous projection commits and numbered releases serve different jobs. Commit and push transferable improvements as they are ready. Publish a numbered release only for a coherent adopter-facing checkpoint: a deliberate public-review milestone; a material identity, operating thought, adoption, runtime, security, schema, or interface change; a migration; or a deliberately bundled improvement set. A documentation-only reference addition, ordinary maintenance commit, or private/public parity event does not earn a release by itself. Before tagging, state the checkpoint's audience and decision effect, review the complete delta since the prior release, and bind the annotated tag, release notes, CI, and fresh-clone verification to one exact commit.

## Projection boundary

A public update may carry:

- constitutional posture and character;
- agency, privacy, integrity, and authorization boundaries;
- reusable operating thought;
- source-authority and knowledge-placement rules;
- adoption and customization procedures;
- deterministic routing and integrity checks.

It must not carry:

- biography, relationships, preferences, or domain records;
- memories, sessions, messages, evidence cases, or private history;
- credentials, permissions, capability state, or local configuration;
- machine paths, private repository references, or private provenance;
- authority granted in the source relationship;
- language that causes an adopting agent to impersonate the source agent.

## Release checks

Before every public update:

1. inspect the private change semantically;
2. extract only the class-level decision effect;
3. depersonalize by meaning, not blind replacement;
4. regenerate derived files from canonical frontmatter;
5. run `python3 scripts/check_template.py`;
6. run syntax, link, staged-diff, secret-pattern, and semantic reviews;
7. push only to the intended public remote;
8. clone the public HTTPS URL into a fresh directory and rerun validation;
9. verify local and remote heads, public visibility, and template status.

Static checks establish packaging integrity. They do not prove that an adopted agent will exercise good judgment.
