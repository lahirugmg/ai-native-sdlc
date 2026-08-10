# Medium Term: Context Engineering

## Outcome

The medium-term horizon makes AI assistance more reliable by treating organizational knowledge as a product. The objective is not to give a model every document and repository. It is to supply the smallest set of authoritative, current, authorized, task-relevant context that helps a person or system perform work correctly.

At the end of this horizon, teams can identify the context a workflow needs, trace it to an owner and source, deliver it consistently, and measure whether grounding actually improves the work.

## What Context Engineering Means

Prompt engineering shapes a single interaction. Context engineering designs the information environment around repeated interactions.

Useful context has five properties:

| Property | Question |
| --- | --- |
| Relevant | Does this information materially help the task at hand? |
| Authoritative | Is it the source a practitioner should trust for this decision? |
| Current | Is its freshness known and appropriate for the decision's risk? |
| Accessible | Can the intended user or system retrieve it within approved access boundaries? |
| Usable | Is it structured, scoped, and understandable enough to guide a correct response? |

Context is more than prose. It can include source code, dependency and interface definitions, tests, architecture decisions, requirements, design tokens, runbooks, issue history, service ownership, policy rules, telemetry summaries, and verified examples. Each has different owners, permissions, and freshness needs.

## Start With a Workflow, Not a Knowledge Dump

Select one short-term workflow whose results are limited by missing, inconsistent, or hard-to-find knowledge. Examples include:

- An engineer needs architecture and repository conventions to make a change safely.
- A reviewer needs current acceptance criteria, standards, and related change history.
- A support or operations practitioner needs a current service map and runbook to investigate an incident.
- A QA practitioner needs interface contracts, risk history, and representative examples to design useful tests.

For the selected workflow, ask:

1. What decision or artifact must be produced?
2. What facts are required to produce it well?
3. Which facts are authoritative, and who owns them?
4. What facts are stale, contradictory, sensitive, or unavailable?
5. What is the smallest context package that can improve the task?
6. How will the result be verified against the underlying sources?

Avoid solving an uncertain task by adding more material. Excess context can obscure key facts, raise cost and exposure, and make a response harder to audit.

## Build a Context Map

A context map is a practical contract for a workflow. It records the information the work needs and makes missing ownership visible.

| Context category | Examples | Owner | Freshness expectation | Access boundary | How it is delivered |
| --- | --- | --- | --- | --- | --- |
| Product and requirements | Acceptance criteria, domain glossary, decision log | Product or delivery owner | Per change or release | Team or product access | Task brief or approved knowledge source |
| Architecture and interfaces | ADRs, system map, API contracts, dependency rules | Architect or owning team | Per material decision | Engineering access | Repository file, documentation site, or retrieval service |
| Code and quality | Source, tests, lint rules, contribution instructions, known issues | Code-owning team | Per merge or release | Repository permissions | Local workspace or controlled integration |
| Operations | Runbooks, dashboards, incident learnings, service ownership | SRE or service owner | Per incident or operational change | Operational access | Role-specific context package |
| Policy and risk | Security standards, data classification, compliance rules | Control owner | On policy change | Need-to-know access | Approved policy source with versioning |

A map should point to sources of truth, not duplicate them into an unmanaged prompt collection. When no owner or trustworthy source exists, record the gap as work to resolve before relying on it.

Use the [context map template](../templates/context-map.md) to capture this contract with workflow and source owners.

## Create Context Products

Context products package authoritative information for a recurring work need. They are lightweight at first and become more structured only when repeated use justifies it.

| Context product | Purpose | Design guidance |
| --- | --- | --- |
| Repository instructions | Explain local conventions, commands, boundaries, and review expectations. | Keep close to code, version with changes, and link to source material instead of restating it. |
| System or service brief | Give an orienting view of a bounded subsystem. | Include purpose, boundaries, dependencies, ownership, invariants, and paths to deeper sources. |
| Task brief | Package the context specific to one work item. | State desired outcome, relevant sources, constraints, ambiguity, and verification. |
| Approved example set | Show what good output looks like for a recurring task. | Use real but sanitized examples, explain why they are good, and review them periodically. |
| Governed knowledge collection | Make a defined information set searchable or retrievable. | Preserve source, permissions, update path, citations, and a way to remove stale material. |

Write context for the person who must validate the outcome, not only for a model. Clear context products improve onboarding and handoffs even when no AI is involved.

## Context Delivery Patterns

Use the simplest delivery mechanism that gives the workflow the required reliability:

| Pattern | When it fits | Control to keep |
| --- | --- | --- |
| Explicit task attachments or references | A small task has a known set of relevant sources. | Confirm the versions and permissions before use. |
| Versioned repository guidance | Developers need stable local instructions with code. | Review changes with normal code review and test referenced commands. |
| Curated team knowledge base | Information crosses repositories or disciplines but changes at a manageable cadence. | Assign document owners and expiry or review dates. |
| Retrieval from governed sources | The relevant facts vary across many authorized sources. | Enforce source-level permissions, return provenance, measure retrieval quality, and test for leakage. |
| Tool or service integration | A workflow needs live, structured facts from a system of record. | Limit scope, authenticate with least privilege, log access, and define fallbacks. |

Do not make retrieval a default answer. A carefully maintained file or task brief can be safer and more effective for a narrow workflow.

## Design for Trust and Safety

Context expands an AI system's reach into organizational information. Treat it as an information-security and reliability concern from the start.

- Preserve source identity, version or timestamp, owner, and relevant permissions whenever possible.
- Apply access controls before retrieval, not only after an answer has been assembled.
- Minimize sensitive data and avoid indexing credentials, secrets, unnecessary personal data, or material prohibited by policy.
- Treat retrieved documents, tickets, web content, and code comments as untrusted instructions. They may contain misleading or malicious content that must not override the workflow's system-level controls.
- Require citations, links, or source references for material claims when a workflow's risk warrants it.
- Define how stale, superseded, or revoked material is removed and how users can report a bad source.
- Test that a user or agent cannot retrieve content outside its authorization boundary.

Context quality is a shared concern. The owner of a source is responsible for its content; the workflow owner is responsible for whether and how it is used.

## Implement Incrementally

Use a narrow improvement loop:

1. Pick one recurring task with a clear short-term baseline.
2. Create its context map and identify the one or two most valuable gaps.
3. Build a small context product or delivery path with named ownership.
4. Test it on representative tasks, including ambiguous and failure cases.
5. Compare outcomes with the unguided workflow and inspect sources used.
6. Improve, retire, or standardize the context product based on evidence.

Test both answer quality and retrieval quality. A strong response based on an incorrect or unauthorized source is not a successful result.

## Evaluate the Result

| Dimension | Questions and examples |
| --- | --- |
| Task quality | Are recommendations more accurate, complete, and compatible with local constraints? |
| Grounding | Does the result cite or faithfully use the relevant authoritative sources? |
| Efficiency | Did time spent finding, reconciling, or re-explaining context decrease without shifting effort elsewhere? |
| Freshness | Does the workflow notice or avoid outdated and superseded material? |
| Security and privacy | Are permissions honored and sensitive sources excluded or handled appropriately? |
| Maintainability | Are owners, update paths, and usage expectations realistic for the value delivered? |

Use a small evaluation set containing normal cases, edge cases, incomplete-context cases, and cases that should be refused or escalated. Review it whenever the workflow, sources, or policies materially change.

## Operating Responsibilities

| Role | Responsibility in the medium term |
| --- | --- |
| Workflow owner | Defines the decision, success criteria, exceptions, and verification required. |
| Source owner | Maintains content accuracy, access rules, and lifecycle information for a source of truth. |
| Platform or knowledge enablement owner | Provides supported storage, retrieval, integration, observability, and support paths. |
| Security, privacy, and risk partners | Review classification, access, retention, third-party exposure, and escalation needs. |
| Practitioners | Flag missing, misleading, stale, or hard-to-use context and verify outcomes in real work. |

Do not create a central context team that silently owns every team's knowledge. Central capability should make ownership and delivery easier while domain teams retain stewardship of their facts.

## Exit Criteria

Prepare a workflow for the long term only when it has:

- A repeatable task with clear inputs, outputs, exceptions, and a human accountable for the result.
- A context map that identifies trusted sources, owners, freshness expectations, and access boundaries.
- A reliable context delivery pattern demonstrated on representative work.
- Evaluation evidence that grounded assistance improves the task or reduces a meaningful risk or friction.
- A practical process for updating, withdrawing, and reporting problems with context.

If a workflow still relies on heroic prompt writing or manual copying of uncertain information, improve its context before attempting a harness.

[Continue to Long term: Harness engineering](long-term-harness-engineering.md)

[Back to Short term](short-term-simple-ai-integration.md) | [Back to the journey](journey-to-ai-assisted-sdlc.md)