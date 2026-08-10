# AI Workflow Evaluation Record

Use this record to establish a baseline, compare a changed workflow, and preserve regressions. One record can describe a short-term practice, a medium-term context product, or a long-term harness.

## Evaluation Identity

| Field | Record |
| --- | --- |
| Workflow or harness |  |
| Owner and evaluators |  |
| Date and environment |  |
| Decision supported | Pilot continuation, release, scope expansion, rollback, or retirement |
| Variant under test | Model, instructions, context, tool configuration, policy, or workflow version |
| Baseline or comparison variant |  |

## Task and Evaluation Set

| Field | Record |
| --- | --- |
| Supported task contract |  |
| Evaluation cases and sources |  |
| Case mix | Normal, edge, ambiguous, missing-context, prohibited, and operational failure cases |
| Expected behavior or rubric |  |
| Sensitive-data handling for fixtures |  |
| Known limitations of the set |  |

## Results

| Dimension | Measure or rubric | Baseline | Variant | Interpretation |
| --- | --- | --- | --- |
| Task quality |  |  |  |  |
| Grounding and source use |  |  |  |  |
| Safety and policy behavior |  |  |  |  |
| Human review burden or override rate |  |  |  |  |
| Latency, cost, reliability, and integration behavior |  |  |  |  |
| Downstream workflow outcome |  |  |  |  |

## Case-Level Findings

| Case ID | Expected behavior | Observed behavior | Severity | Disposition |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

## Decision and Follow-Up

| Field | Record |
| --- | --- |
| Gate decision |  |
| Rationale and evidence |  |
| Regressions to preserve in the evaluation set |  |
| Required remediation and owner |  |
| Monitoring signals after release |  |
| Next evaluation trigger or review date |  |

Avoid treating aggregate model scores as the whole answer. Preserve representative failures, human review notes, and the task-specific rationale behind the decision.

[Long-term playbook](../docs/long-term-harness-engineering.md)
