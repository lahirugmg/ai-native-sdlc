# Harness Design Review

Use this template before implementing or materially expanding a long-term harness. It makes the task contract, action boundaries, evaluation, operations, and decision rights reviewable.

## Ownership and Scope

| Field | Record |
| --- | --- |
| Harness name |  |
| Product or workflow owner |  |
| Technical owner |  |
| Risk, security, privacy, and operations partners |  |
| Users and affected systems |  |
| Decision requested | Prototype, shadow mode, assisted mode, constrained action, or wider rollout |

## Task Contract

| Question | Record |
| --- | --- |
| Supported job and value hypothesis |  |
| Valid inputs and source of each input |  |
| Expected output and required schema |  |
| Quality bar and task-specific rules |  |
| Unsupported cases and refusal or escalation behavior |  |
| Human decision, approval, or override point |  |
| Side effects and reversibility |  |

## Context, Capabilities, and Access

| Area | Record |
| --- | --- |
| Context sources, owners, freshness, and permissions |  |
| Integrated tools and least-privilege permissions |  |
| Service identity and authentication path |  |
| Data classification, minimization, retention, and residency constraints |  |
| Secrets handling |  |
| Source or tool output treated as untrusted data |  |

## Controls and Failure Handling

| Control | Design |
| --- | --- |
| Input and output validation |  |
| Policy checks and allowlists |  |
| Timeouts, retries, rate limits, quotas, and idempotency |  |
| Audit record and required metadata |  |
| Kill switch and manual fallback |  |
| Incident route and first-response owner |  |
| Rollback or remediation plan |  |

## Evaluation and Release Plan

| Field | Record |
| --- | --- |
| Representative evaluation cases and owners |  |
| Quality, grounding, safety, and operational metrics |  |
| Baseline or comparison workflow |  |
| Minimum gate for progression |  |
| Shadow-mode design, if applicable |  |
| Change triggers that require re-evaluation |  |
| Release, monitoring, and support plan |  |

## Approval Record

| Reviewer | Decision | Conditions or open items | Date |
| --- | --- | --- | --- |
| Workflow owner |  |  |  |
| Technical or platform owner |  |  |  |
| Security, privacy, or risk owner |  |  |  |
| Operations or support owner |  |  |  |

[Long-term playbook](../docs/long-term-harness-engineering.md) | [Governance and risk](../docs/governance-and-risk.md)
