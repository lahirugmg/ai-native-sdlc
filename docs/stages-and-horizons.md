# Stages and Horizons

## Purpose

The horizon guides answer one question: what must be true before a team does more. They do
not answer a second question that teams ask just as often — what assistance actually looks
like in a particular part of the lifecycle.

This document supplies the second answer by crossing the two axes. Horizons describe
readiness and are entered on evidence. Stages describe where in the lifecycle the work
sits and are entered by doing the work at all. Every organization already has all six
stages; none of them is an achievement.

Read this after [Finding your organization's path](finding-your-path.md), which maps the
flow of work, and alongside the horizon guide for whichever cell is under discussion. The
horizon guides remain the source of truth where they and this summary disagree.

## How to Read the Matrix

- **Stages are not a maturity sequence.** Reaching the maintain stage is not progress. A
  change passes through all six stages whether or not any assistance is involved.
- **Only horizons are gated.** The evidence gates in
  [the journey guide](journey-to-ai-native-sdlc.md) govern movement across columns. Nothing
  governs movement across rows, because rows are not movement.
- **Different stages sit at different horizons, normally.** Long term in test and short term
  in design is an ordinary position for a team, not an inconsistency to resolve.
- **The dependency runs along the row, not down the column.** A stage's long-term cell
  requires that same stage's medium-term cell. Trusted context for testing does not qualify
  a design workflow for a harness.
- **Every cell names a failure mode.** Cells describe what the work looks like and what goes
  wrong there. They are not targets to reach.

## The Matrix

| Stage | Short term · fluency | Medium term · context | Long term · harness |
| --- | --- | --- | --- |
| Plan | Assistance sharpens a problem statement | The intent record is versioned and owned | Findings enter as intent records; a person triages |
| Design | Options and trade-offs drafted for a decision | Specifications grounded in current decisions | Policy checks applied as the specification is written |
| Build | Task briefs on bounded, reviewable work | Repository instructions carry the conventions | Guardrails, scoped agents, bounded concurrency |
| Test | Drafted tests an engineer revises and runs | Test conventions and fixtures are owned context | Verification before review; evaluated configuration |
| Deploy | Drafted descriptions and review preparation | Review standards documented and owned | Advisory review; gates enforced outside the model |
| Maintain | Assistance assembles incident context | Runbooks current and reachable from the response | Deterministic detection with tiered response |

## Plan

Produces the statement of what problem is being solved and why it is worth solving.

| Horizon | What assistance looks like | Failure it invites |
| --- | --- | --- |
| Short term | Assistance sharpens a problem statement in conversation. The originator writes the record and owns it. | A fluent restatement of a vague request, which reads as clarity without adding any. |
| Medium term | The intent record is a versioned artifact with an owner, traceable to the product context that justifies it. | A second, unowned backlog that duplicates the tracker and drifts from it. |
| Long term | Operational findings enter as intent records without a human in the detection path. A person triages them. | A triage queue nobody reads, which turns detection into noise and hides the signal it was built to surface. |

## Design

Produces the decision about how the change will be made, and the record of why.

| Horizon | What assistance looks like | Failure it invites |
| --- | --- | --- |
| Short term | Options and trade-offs drafted to widen a human decision. Decision records are still written by people. | Plausible options that ignore a local constraint nobody supplied. |
| Medium term | Specifications grounded in current decision records and standards, with policy applied while the specification is written rather than discovered in review. | Policy encoded from a source that has since changed, then applied confidently. |
| Long term | Policy checks run as the specification is produced, and flagged concerns route to named owners before engineering begins. | Routing to an owner who does not answer, which stalls work behind a control that only looks active. |

## Build

Produces the change itself.

| Horizon | What assistance looks like | Failure it invites |
| --- | --- | --- |
| Short term | Task briefs on bounded work, with every output inspected, tested, and owned by the person who used it. | Fluency mistaken for correctness. |
| Medium term | Repository instructions carry conventions, commands, and deprecated patterns. A change plan is agreed before implementation. | Silence in the instructions filled by invention. Fabrication appears where the context package is empty, not where it is wrong. |
| Long term | Deterministic guardrails on protected paths, scoped agents with least privilege, and concurrency bounded by review capacity rather than by tooling. | Parallelism that outruns review, which moves the constraint rather than removing it. |

## Test

Produces the evidence that the change does what was intended.

| Horizon | What assistance looks like | Failure it invites |
| --- | --- | --- |
| Short term | Drafted tests that an engineer revises and runs, with assertions checked against behavior. | A coverage gate met by assertions that would still pass with the logic removed. |
| Medium term | Test conventions, fixtures, and a single verification command are owned context, current with the code. | Verification that passes locally and fails in the pipeline, because the documented command is not the one that runs there. |
| Long term | Verification runs before human review, and an evaluation set gates changes to the configuration that steers the work. | An evaluation set built only from past successes, which encodes the assumption that future inputs resemble them. |

## Deploy

Produces the decision to release, and the record supporting it.

| Horizon | What assistance looks like | Failure it invites |
| --- | --- | --- |
| Short term | Drafted change descriptions and review preparation. Normal approvals are unchanged. | Disclosure that a change was assisted, with no corresponding change in the scrutiny applied. |
| Medium term | Review standards are documented, versioned, and owned, so a reviewer can cite them rather than remember them. | A checklist that lives outside the workflow and is therefore applied inconsistently. |
| Long term | An advisory review capability, with approval gates enforced outside the model and separation of duties verified rather than assumed. | Findings dismissed faster than they are read, which is worse than no findings because it consumes attention and returns nothing. |

## Maintain

Produces the operational response, and frequently the next problem statement.

| Horizon | What assistance looks like | Failure it invites |
| --- | --- | --- |
| Short term | Assistance assembles incident context for a responder who decides and acts. | A confident timeline nobody checked against the underlying records. |
| Medium term | Runbooks, service ownership, and incident learnings are current and reachable from the response itself. | A runbook that drifts between incidents and is trusted anyway. |
| Long term | Deterministic detection against a stable baseline, tiered response, read-only diagnosis, and proposals that re-enter at the plan stage. | Response thresholds tuned by dismissal rather than by evidence, until detection stops firing at all. |

## Reconciling With Capability Areas

[Finding your organization's path](finding-your-path.md) maps work through eight capability
areas. Six of them correspond to a stage. Two do not, and that is the useful part.

| Capability area | Stage | Note |
| --- | --- | --- |
| Product and requirements | Plan | Direct correspondence |
| Architecture and design | Design | Direct correspondence |
| Engineering | Build | Direct correspondence |
| Quality and testing | Test | Direct correspondence |
| Platform and delivery | Deploy | Direct correspondence |
| Operations and reliability | Maintain | Direct correspondence |
| Security and risk | Every stage | Not a stage. Security decisions arise in design, build, deploy, and maintain, and treating them as a late stage is the failure the capability-area table already warns about |
| Documentation and communication | Every stage | Not a stage. Documentation produced only at the end is the artifact most likely to be skipped under delivery pressure |

The two cross-cutting areas are the reason this document is a matrix rather than a
pipeline. A stage model that made security a step would place it after build, which is
where teams already find it too late.

## What This Document Does Not Cover

- **Which stage to improve first.** That is a question about local friction, answered by
  the [opportunity map](../templates/sdlc-opportunity-map.md), not by looking for the
  emptiest cell.
- **Whether a workflow should be automated at all.** The long-term column describes what a
  qualified workflow looks like, not which workflows qualify. Qualification is defined in
  [Long term: Harness engineering](long-term-harness-engineering.md).
- **Any claim that a cell has been reached.** Advancement across columns is evidence-gated
  and audited against [the journey guide](journey-to-ai-native-sdlc.md). This document
  describes positions; it does not award them.

[Journey guide](journey-to-ai-native-sdlc.md) | [Finding your organization's path](finding-your-path.md) | [Back to the repository overview](../README.md)
