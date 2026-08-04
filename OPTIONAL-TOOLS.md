# Optional tool stack

> **Curated source-agent reference, not template state.** This is a privacy-safe list of tools or capability patterns Bobert uses or deliberately maintains as task-triggered escalation paths. The template does not install, configure, enable, or grant authority to any of them. Adopters must choose their own tools, inspect current official documentation, provide their own credentials, and verify their actual runtime.
>
> Last reviewed: 2026-08-04.

## Why this list exists

The starter publishes portable identity and operating judgment, not Bobert's live configuration. That boundary is correct, but it can hide useful implementation options. This page provides a menu of tools that have earned a place in the source system without copying endpoints, account state, private procedures, personal records, permissions, or secrets.

The governing rule is still **job first, tool second**. More integrations can reduce routing quality, increase data egress, broaden authority, and create maintenance work. None of these tools is a default requirement.

## Research, web, and technical documentation

| Tool or capability | Job it earns | Why it is not a template default |
|---|---|---|
| [Hermes Agent native web and browser tools](https://hermes-agent.nousresearch.com/docs/) | Ordinary search, page extraction, PDFs, browser interaction, and source inspection | Runtime-specific; usually the first retrieval path before adding another service |
| [Firecrawl capability](https://docs.firecrawl.dev/quickstarts/python), available through the Python SDK (`firecrawl-py`), CLI, or API | Multi-page crawling, site maps, structured extraction, difficult JavaScript pages, and repeatable web-research pipelines | Adds site egress, credentials or managed-service dependence, possible usage cost, and maintenance; use only when native retrieval is insufficient |
| [AnyDoc](https://github.com/firecrawl/anydoc) local document-to-Markdown conversion | Convert supported office documents and ebooks locally when Markdown is useful downstream and private source files should remain on-device | Format coverage and structure fidelity vary; this is neither OCR nor a replacement for page-aware PDF extraction or native spreadsheet inspection. Verify a representative input before relying on output |
| [Consensus MCP](https://docs.consensus.app/docs/mcp) | Discover peer-reviewed literature and build a research trail | Search results are discovery evidence, not a substitute for reading and citing the underlying papers |
| [Context7 MCP](https://context7.com/) | Retrieve current, version-specific library documentation and examples | Package documentation changes; verify examples against the project's actual dependency version |
| [CourtListener MCP](https://mcp.courtlistener.com/) | Search legal opinions, dockets, judges, and related public legal material | Legal research requires jurisdiction, date, citation, and authority checks; tool output is not legal advice |

Naming an SDK or CLI here identifies an available implementation path; it does not claim that package is installed in Bobert's current runtime or in an adopter's environment.

## Computation and maps

| Tool or capability | Job it earns | Boundary to preserve |
|---|---|---|
| [Wolfram Cloud MCP](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) | Symbolic and numerical computation, units, equations, and curated Wolfram\|Alpha data | Validate inputs and units; polished computation does not become a personal or business source of record |
| [Mapbox MCP](https://docs.mapbox.com/api/guides/mcp-server/) | Geocoding, places, directions, matrices, isochrones, geometry, and static maps | Location queries can be sensitive; send the minimum geography needed and do not treat the service as a personal-location record |

## Browser, infrastructure, and development

| Tool or capability | Job it earns | Boundary to preserve |
|---|---|---|
| [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) | Structured browser automation, accessibility snapshots, forms, screenshots, and browser diagnostics | Page interaction can mutate accounts or publish identity-bearing actions; separate read-only inspection from writes |
| [Cloudflare MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) | Workers, DNS, observability, AI Gateway, and other Cloudflare operations | The available surface can be broad and consequential; scope credentials and expose only the required operations |
| Git and [GitHub CLI](https://cli.github.com/) | Repository inspection, issues, pull requests, releases, and CI evidence | Repository access is not permission to commit, push, merge, publish, or rewrite history |
| Python 3.11 and [uv](https://docs.astral.sh/uv/) | Local scripts, deterministic checks, temporary verifiers, and dependency-isolated tooling | Pin compatibility where it matters and avoid installing into the system Python |
| Node.js, npm, and npx | JavaScript builds and on-demand MCP/CLI execution | Pin durable dependencies; an unpinned `npx` command is executable supply-chain exposure |
| `curl` and `jq` | Small HTTP and JSON inspection tasks | Do not place secrets in command arguments, logs, or versioned examples |
| [Docker](https://docs.docker.com/) | Isolated services, reproducible development environments, and bounded experiments | Containers are not a security boundary by default; inspect mounts, ports, networks, images, and persistence |
| [FFmpeg](https://ffmpeg.org/) | Audio/video conversion, extraction, compression, and generated-media verification | Media can contain private voices, faces, location clues, and metadata; minimize inputs and retention |

## Private or domain-specific patterns

Bobert also uses narrow local connectors for some domains. These are listed as **patterns**, not redistributable integrations:

- read-only sleep-device metrics;
- selected Apple Health reads through a local bridge;
- read-only network-health summaries;
- sanitized camera inventory and event metadata rather than unrestricted raw surveillance feeds;
- local Apple Notes and Reminders command-line adapters;
- governed memory/profile continuity whose conclusions remain subordinate to canonical domain records.

These patterns are intentionally not packaged into the starter. Health, home, communications, cameras, location, and network data require ownership-specific privacy rules, local authorization, narrow schemas, and explicit retention decisions.

## Managed model and media capabilities

Depending on the chosen runtime and provider, Bobert may use managed or local capabilities for:

- image generation and editing;
- text-to-speech and speech-to-text;
- video analysis or generation;
- coding-agent delegation;
- scheduled jobs and background monitors.

Provider availability changes. Treat each as a separate capability with its own authority, cost, egress, retention, and verification boundary rather than assuming the template supplies it.

## Adoption checklist

Before adding any item from this page:

1. Name the task or decision it must improve.
2. Confirm existing tools are insufficient.
3. Read current official documentation and identify licensing or usage cost.
4. Classify read, write, messaging, device-control, and unattended authority separately.
5. Map credentials, input data, egress, provider retention, logs, and callbacks.
6. Connect the minimum useful surface with adopter-owned secret storage.
7. Run one bounded representative probe and inspect the actual evidence.
8. Test a prohibited or out-of-scope path when scoping should block it.
9. Record the tool owner, known limitation, disable path, and removal trigger.
10. Remove or constrain the integration if decision value does not justify its carrying cost.

See [External Capability Governance](doctrine/capabilities/external-capability-governance.md) for the full decision framework. Connection proves transport; it does not prove usefulness, safety, authority, or source quality.

## Deliberately omitted

This public page does not publish:

- credentials, tokens, account identifiers, endpoints tied to private infrastructure, or secret-storage locations;
- live connection status, enabled tool counts, local paths, schedules, or machine inventory;
- personal, household, health, finance, business, communication, network, camera, or location data;
- private skills, internal operating procedures, or authorization grants;
- copied provider schemas or installation transcripts that will drift from official documentation.

That omission is part of the design, not an incomplete export.
