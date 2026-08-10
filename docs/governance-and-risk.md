# Governance and Risk

## Purpose

Governance should make responsible AI-assisted work easier, not turn it into an opaque approval maze. Its job is to make decision rights, approved paths, boundaries, evidence, and escalation visible as AI capability grows across the SDLC.

This guide is an operating framework, not legal advice or a replacement for applicable regulation, contracts, security standards, records requirements, or enterprise policy. Adapt it with the organization's legal, privacy, security, procurement, risk, architecture, and employee-relations partners.

## Governance Principles

- Apply controls in proportion to potential impact, data sensitivity, access, autonomy, and reversibility.
- Keep human accountability explicit; an AI capability does not become the decision owner.
- Prefer supported, transparent paths over blanket prohibitions that drive work into unapproved tools.
- Make data classification, tool approval, and escalation answers easy to find at the point of work.
- Use evidence from real use, evaluations, incidents, and feedback to improve controls over time.
- Separate policy requirements from implementation guidance so teams know both what is required and how to comply.

## Decision Rights

AI-assisted SDLC work crosses existing responsibilities. Name a decision owner for each area rather than creating an isolated "AI committee" that must approve every prompt.

| Decision area | Accountable owner | Typical partners | Evidence needed |
| --- | --- | --- | --- |
| Business outcome and acceptable trade-off | Product, delivery, or engineering leader | Sponsor, finance, operations | Pilot or product hypothesis, success and stop conditions |
| Tool and vendor approval | Technology, procurement, or platform owner | Security, privacy, legal, finance | Capability, contract, data use, identity, cost, support, exit plan |
| Data classification and use | Data or business owner | Privacy, security, legal, records | Data categories, permitted use, retention, residency, sharing boundaries |
| Architecture and integration | Architecture or platform owner | Owning teams, security, operations | System boundary, authentication, permissions, failure modes, support plan |
| Workflow quality and human review | Workflow owner | Engineers, QA, security, operations | Task contract, test or evaluation evidence, escalation process |
| Consequential action and exceptions | Business or risk owner | Control owners, legal, compliance | Impact analysis, approval path, auditability, rollback or remediation |

For low-risk Phase 1 work, publish guardrails and allow local teams to proceed. For higher-risk integrations or actions, use a documented review that is predictable, time-bounded, and appropriate to the impact.

## Risk-Tiered Controls

Classify a use case before selecting controls. These examples describe work patterns, not formal risk categories; use the organization's existing risk taxonomy where one exists.

| Work pattern | Typical example | Minimum controls |
| --- | --- | --- |
| Assistive, no side effect | An engineer asks an approved tool to explain non-sensitive code or draft test ideas. | Approved tool and account, data boundary, human review, normal engineering controls. |
| Grounded internal assistance | A workflow retrieves approved requirements or architecture material to draft a change plan. | Source permissions, provenance, freshness and ownership, evaluation of grounding, human decision. |
| Constrained operational action | A harness opens a draft pull request, creates a ticket, or performs a reversible update. | Least-privilege identity, authorization, schema validation, audit record, approval or policy gate, rollback. |
| High-impact or sensitive decision | A system affects customers, regulated outcomes, employment, finances, production access, or sensitive personal data. | Formal risk review, domain-specific controls, independent validation as required, heightened monitoring, clear human accountability and remediation. |

The same capability may sit in different tiers depending on the data, integration, audience, and effect. For example, summarizing a public incident report is unlike summarizing customer support records.

## Minimum Guardrails for Early Adoption

Before broad Phase 1 use, make these rules and routes clear:

- Which AI services, account types, extensions, and integrations are approved for which work.
- What data may be entered, uploaded, retained, or connected, including code, secrets, customer data, internal documents, logs, and regulated information.
- How people authenticate, where organization-managed accounts are required, and how access is removed.
- That AI output remains subject to normal testing, code review, security review, change management, and release controls.
- How to report suspected data exposure, unsafe output, incorrect advice, policy ambiguity, or tool malfunction.
- Where approved examples, guidance, and support are available.

Keep this guidance short enough to be used. Link to the authoritative detailed policy where needed, but provide task-oriented answers such as "Can I use this log?" or "Which account should I use?"

## Data and Information Handling

Build AI rules on the organization's existing data classification model. When classification is unclear, treat the material as more sensitive until its owner clarifies the boundary.

| Information concern | Control intent |
| --- | --- |
| Credentials and secrets | Do not include them in prompts, context stores, logs, evaluation fixtures, or tool calls unless a reviewed architecture explicitly protects the use. |
| Personal, customer, and regulated data | Limit use to approved systems and purposes; minimize, mask, or use synthetic data where practical; apply retention and residency requirements. |
| Source code and intellectual property | Use approved accounts, vendor terms, access controls, and repositories; consider export, training, and retention terms. |
| Operational data | Restrict access by role, redact unnecessary sensitive values, and preserve incident or audit obligations. |
| Documents and retrieved content | Apply source-level permissions, ownership, lifecycle, and provenance; do not assume internal content is safe to treat as instructions. |

Do not rely on a prompt instruction such as "do not retain this" as a data control. Use contractual, account, configuration, access, and technical safeguards appropriate to the approved service.

## Secure Harness Design

Phase 3 work introduces integration and action risk. Require engineering controls at the boundary:

- Enforce authentication and authorization outside the model, using service identities with least privilege.
- Validate inputs, tool responses, and structured output before they drive downstream actions.
- Use allowlists, scoped permissions, sandboxes, rate limits, timeouts, quotas, and idempotency for tool use.
- Separate proposal, approval, and execution where a change has material impact.
- Treat retrieved text, tickets, documents, and tool output as untrusted data that cannot override system policy.
- Record material task inputs, policy decisions, actions, approvals, errors, and outcome references within applicable retention rules.
- Design a fallback, kill switch, and incident response route before enabling consequential actions.

An approval button is not a complete control. Reviewers need enough source, context, and explanation to make a real decision, and the system must behave safely when that decision is unavailable.

## Evaluation and Change Control

Changes to a model, prompt, context source, retrieval behavior, tool permission, workflow logic, or policy can change system behavior. Establish a change process proportional to risk:

1. Identify the intended change and affected task contract.
2. Run relevant offline evaluations, contract checks, safety cases, and operational checks.
3. Review material regressions, new failure modes, changed data exposure, and changes in action scope.
4. Approve, deploy progressively, monitor, and retain a rollback path.
5. Record outcomes and update documentation, known limitations, and evaluation sets.

For simple Phase 1 tools, this may be a short review of updated vendor settings and guidance. For a consequential harness, it should integrate with established software change management and risk controls.

## Incident and Exception Handling

Define these paths before a scaled rollout:

| Situation | Immediate action | Follow-up |
| --- | --- | --- |
| Suspected data exposure or unauthorized access | Stop affected sharing or integration, preserve relevant evidence, notify the security or privacy incident route. | Contain, assess impact, meet notification obligations, remediate controls, and communicate lessons. |
| Unsafe, inaccurate, or policy-violating output | Prevent or reverse the outcome where possible; escalate to the workflow owner. | Classify the failure, improve context, validation, training, or scope, and add a regression case. |
| Tool or integration malfunction | Disable the affected path or fall back to the manual workflow. | Investigate reliability, vendor, configuration, and observability gaps before re-enabling. |
| Policy ambiguity | Pause only the uncertain use, not unrelated work; route to the named decision owner. | Publish a clear, reusable answer and update guidance or controls. |

Exceptions should be documented, time-bounded, and owned. Repeated exceptions are evidence that the standard path needs attention.

## Governance Signals

Monitor whether governance enables good work as well as whether it catches problems:

- Time to obtain a decision on a well-scoped use case.
- Usage of approved paths versus requests for unapproved workarounds.
- Training completion and participant understanding of boundaries.
- Policy questions, exceptions, incidents, and recurring ambiguity.
- Evaluation failures, human overrides, permission denials, and rollback events.
- Evidence that controls preserve delivery quality, security, privacy, and customer trust.

Review these signals with the adoption portfolio. Good governance is visible when teams can move quickly within clear limits and higher-risk work receives the attention it actually needs.

[Back to the adoption model](adoption-model.md)