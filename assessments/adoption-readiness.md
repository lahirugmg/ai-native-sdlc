# Adoption Readiness Assessment

## Purpose

Use this assessment to choose a responsible starting point for AI-assisted SDLC adoption. It is a structured conversation and evidence record, not a maturity score to rank teams or people.

Complete it with the proposed pilot owner, representative practitioners, and the partners responsible for security, privacy, platform, architecture, and delivery where appropriate. Record evidence and open questions, then reduce the scope or resolve gaps before the pilot begins.

## How to Rate Each Area

Use these four descriptions as a common language:

| Rating | Meaning |
| --- | --- |
| 0. Unknown or absent | No owner, evidence, or repeatable practice is visible. |
| 1. Emerging | Intent exists, but practice is informal, incomplete, or dependent on a few people. |
| 2. Usable for a bounded pilot | The pilot has an owner, evidence, and a workable path; gaps are known and controlled. |
| 3. Repeatable and scalable | The practice is supported, measured, and reliable across more than one team or workflow. |

Do not average the ratings into a single maturity number. A strong tool platform cannot compensate for unclear data boundaries, and excellent individual skill cannot compensate for an unsupported production integration.

## Readiness Areas

### 1. Outcome and Ownership

| Check | Evidence to look for |
| --- | --- |
| A sponsor can set outcome boundaries and remove organizational blockers. | Named leader, decision cadence, clear problem statement. |
| A pilot owner is accountable for the workflow, evidence, and stop decision. | Pilot charter, delivery or engineering lead commitment. |
| The team has a real recurring task to improve. | Representative work items, known friction, participants who do the work. |
| Success includes quality and risk, not only output volume or speed. | Balanced measures and a baseline plan. |

**Proceed at rating 2 or higher.** If the work or owner is unclear, choose a different pilot rather than asking the tool to discover the strategy.

### 2. People and Change Readiness

| Check | Evidence to look for |
| --- | --- |
| Participants are volunteers or have meaningful local support. | Team agreement, manager capacity, identified champions. |
| People have time for guided practice and reflection. | Training plan, scheduled clinics, delivery plan that protects learning time. |
| Existing review and escalation habits are healthy enough to absorb a new tool. | Working code review, testing, incident, or quality routines. |
| Leaders will use evidence to improve the pilot rather than surveil individuals. | Stated measurement principles and feedback route. |

**Proceed at rating 2 or higher.** Early adoption should improve capability, not create a hidden performance-management mechanism.

### 3. Tool, Identity, and Support Path

| Check | Evidence to look for |
| --- | --- |
| The pilot uses an approved or reviewable service and organization-managed account where needed. | Tool inventory, account setup, vendor or procurement route. |
| Authentication, access removal, support, and cost ownership are known. | Identity design, support contact, subscription and budget owner. |
| The tool fits the selected work without requiring unplanned integrations. | Small proof of fit using approved representative material. |
| Participants know the approved path and what to do when it fails. | Onboarding guide, support channel, manual fallback. |

**Short-term work requires rating 2.** A high-integrity pilot can use a small manual setup; do not block it on a full internal platform.

### 4. Data, Privacy, Security, and Legal Boundaries

| Check | Evidence to look for |
| --- | --- |
| The pilot's inputs are classified or can be safely constrained to approved examples. | Data inventory, redaction approach, source owner confirmation. |
| Participants know what must not be entered or connected. | Short task-oriented guidance and training scenario. |
| A route exists for privacy, security, legal, procurement, or records questions. | Named contacts and escalation expectations. |
| Incidents can be reported and contained. | Existing incident route or a pilot-specific contact. |

**Short-term work requires rating 2.** If this area is at 0 or 1, use non-sensitive or synthetic examples only until a decision owner clarifies the boundary.

### 5. Delivery, Quality, and Measurement Baseline

| Check | Evidence to look for |
| --- | --- |
| The selected workflow has a visible starting point. | Cycle time, review latency, defect, rework, support, or experience signals. |
| The team can preserve normal tests, review, and release controls. | Existing definition of done, CI checks, change controls. |
| Feedback and failure evidence can be captured without excessive burden. | Short survey, examples, review findings, incident and support data. |
| The pilot has a comparison period or representative sample. | Defined baseline window or matched task set. |

**Short-term work requires rating 1, aiming for 2.** Improve measurement during the pilot, but do not claim value without a baseline.

### 6. Knowledge and Context

| Check | Evidence to look for |
| --- | --- |
| The team can identify the code, requirements, architecture, standards, or operational facts it needs. | Initial task brief, system map, source list. |
| Important sources have owners and recognizable versions or dates. | Repository ownership, document owners, ADR process, runbook owners. |
| Known contradictions, stale sources, and access gaps are visible. | Context map or backlog of knowledge gaps. |
| The team can test whether a response used the right source. | Source links, citations, peer review, task-specific checks. |

**Medium-term work requires rating 2.** A short-term experiment can begin with limited context, but recurring missing knowledge is a signal to invest here.

### 7. Engineering and Operational Capability

| Check | Evidence to look for |
| --- | --- |
| The workflow can be described with inputs, outputs, constraints, and exceptions. | Task contract, process map, representative cases. |
| Relevant integrations have an owner and a safe access path. | API documentation, service identity, least-privilege design. |
| The organization can test, deploy, monitor, and roll back automation. | CI/CD, logging, alerting, on-call or support owner, manual fallback. |
| The team can evaluate a change before allowing side effects. | Evaluation cases, test environment, approval design. |

**Long-term work requires rating 2 or higher.** Do not build a harness around a workflow that cannot be described, tested, supported, or rolled back.

## Readiness Decision

Use the evidence to make one of four decisions:

| Decision | When it fits | Next action |
| --- | --- | --- |
| Start a bounded short-term experiment | Core ownership, tool, data boundary, and review practices are usable. | Write a [pilot charter](../templates/pilot-charter.md) and run guided enablement on real work. |
| Start short-term work with constraints | The team is ready, but one boundary remains uncertain. | Narrow inputs, use synthetic material, or limit the tool until the decision is resolved. |
| Invest in a foundation first | Ownership, data boundaries, or basic delivery controls are too weak. | Resolve the specific gap with its accountable owner; do not substitute training for a missing control. |
| Prepare a medium- or long-term candidate | A short-term practice is proven and context or harness readiness is demonstrably sufficient. | Create a context map or task contract and evaluation plan. |

## Evidence Record

Capture the following on one page for each proposed pilot:

| Field | Record |
| --- | --- |
| Pilot and workflow |  |
| Sponsor and accountable owner |  |
| Participants and affected stakeholders |  |
| Journey horizon being considered |  |
| Readiness ratings by area |  |
| Evidence and assumptions |  |
| Known gaps and mitigation |  |
| Data and tool boundary |  |
| Success, safety, and stop conditions |  |
| Decision and review date |  |

[Back to the repository overview](../README.md) | [Read the journey](../docs/journey-to-ai-assisted-sdlc.md)
