# Phase 1: Simple AI Integration

## Outcome

Phase 1 makes AI assistance an intentional, safe, and useful part of everyday software work. The aim is not universal use or maximum generated code. The aim is for people to know which tasks benefit from assistance, how to provide a good task brief, how to protect organizational information, and how to verify the result.

By the end of this phase, a pilot team should be able to repeat a small set of AI-assisted practices in ordinary delivery work without weakening code review, testing, security, or ownership.

## What Changes

| Before | In Phase 1 |
| --- | --- |
| AI use is ad hoc, hidden, or prohibited by uncertainty. | Approved tools and data boundaries are clear, and people can ask for help without guessing. |
| A good prompt is treated as a clever phrase. | A useful prompt is a concise task brief with context, constraints, and verification expectations. |
| Generated output is accepted because it looks plausible. | AI output is inspected, tested, and owned by the person who uses it. |
| Learning stays with early enthusiasts. | Teams share examples, failure modes, and task patterns through lightweight rituals. |

## Scope the First Pilot

Start with one or two volunteer teams and a few work types that are frequent, bounded, and easy to review. Good first candidates include:

- Explaining unfamiliar code, configurations, logs, or test failures using approved inputs.
- Drafting unit tests and test cases that engineers then revise and run.
- Producing a first-pass pull request description, release note, operational runbook, or technical summary.
- Identifying refactoring options or edge cases for a human decision.
- Preparing code-review questions, acceptance criteria, or incident timelines.

Defer workflows that allow an AI system to change production, access secrets, make authorization decisions, handle sensitive data beyond approved boundaries, or merge changes without established controls. Those may become candidates in later phases after the organization has reliable context and a harness.

Choose pilot work that represents normal delivery. A polished demonstration can show capability, but it cannot establish cost, review burden, quality, or adoption fit.

## Minimum Setup

Before inviting participants, establish the following:

| Need | Minimum standard |
| --- | --- |
| Accountable owner | A named engineering or delivery leader owns the pilot outcome and stopping decisions. |
| Tool boundary | Participants know the approved service, account type, integrations, retention expectations, and support route. |
| Data boundary | The organization states what source code, customer data, credentials, logs, documents, and regulated data may or may not be shared. |
| Baseline | Capture a small set of current flow, quality, experience, and risk signals for the selected work. |
| Review contract | Existing testing, pull request review, security review, and release controls still apply to AI-assisted work. |
| Feedback route | Participants can report a bad answer, policy question, tool issue, or useful pattern without friction. |

Do not try to finish a company-wide policy before a small pilot begins. Instead, make the pilot boundary explicit and route unresolved questions to the appropriate security, privacy, legal, procurement, or architecture partner.

## Guided Rollout

The sequence below is a common six-week shape, not a mandatory calendar. Compress or extend it based on team cadence and risk.

| Stage | Activities | Evidence |
| --- | --- | --- |
| Prepare | Define the hypothesis, selected work, participants, tool and data boundaries, baseline, and stop conditions. | A one-page pilot charter and a shared measurement plan. |
| Learn | Run role-based, hands-on sessions using representative but approved examples. | Participants can describe their boundaries and produce a task brief. |
| Practice | Use AI assistance on a small set of real tasks with normal reviews and tests. | Annotated examples of useful output, bad output, and verification. |
| Share | Hold short peer clinics or show-and-tell sessions; collect patterns and failure modes. | A growing team pattern library and a list of open questions. |
| Review | Compare outcomes with the baseline and interview participants. | A decision to adapt, repeat, stop, or prepare context improvements. |

Leads should protect time for practice. A pilot fails when people are expected to learn a new working method entirely in the gaps between urgent delivery commitments.

## Prompt Engineering as Task Framing

Prompt engineering in a professional setting is not prompt folklore. Teach participants to formulate the same information they would give a thoughtful teammate.

### The Task Brief

For any nontrivial request, include these elements:

| Element | Questions to answer |
| --- | --- |
| Outcome | What decision, change, analysis, or artifact is needed? |
| Context | Which approved code, requirements, architecture notes, examples, logs, or constraints are relevant? |
| Boundaries | What must not change, be assumed, exposed, or invented? |
| Quality bar | What correctness, security, performance, accessibility, compatibility, or style expectations apply? |
| Verification | How should the output be checked, tested, cited, or reviewed before use? |

A weak request is "write a login feature." A better task brief states the existing service boundary, authentication approach, approved data handling rules, expected tests, constraints on dependencies, and asks the assistant to identify assumptions before proposing a change.

The important skill is not prompt length. It is selecting relevant facts, stating constraints, breaking large work into reviewable pieces, and asking for uncertainty to be made visible.

Use the [AI task brief template](../templates/ai-task-brief.md) in workshops and early real-work pilots. The [pilot charter template](../templates/pilot-charter.md) records the boundaries and evidence plan around the work.

### Productive Interaction Patterns

- Ask for an explanation and assumptions before asking for a change in unfamiliar code.
- Request options with trade-offs when the decision is architectural or ambiguous.
- Supply a small, representative example and ask the assistant to reason from it rather than inventing a system.
- Ask for a test plan, edge cases, and failure modes alongside an implementation draft.
- Request a review against explicit acceptance criteria, conventions, or a threat model.
- Compare the response with source material and challenge unsupported claims.

### Habits to Avoid

- Pasting credentials, customer data, proprietary material, or sensitive logs into an unapproved service.
- Treating a fluent response as evidence of correctness.
- Asking an assistant to infer undocumented business rules without marking the result as a hypothesis.
- Skipping tests, review, or design discussion because a change was generated quickly.
- Measuring only time spent generating output while ignoring rework, defects, and review effort.

## Role-Based Enablement

Run short, practical sessions by role. Each session should use real work shapes, a shared task brief, and an explicit verification step.

| Audience | Focus | Practice outcomes |
| --- | --- | --- |
| Engineers | Code explanation, test drafting, refactoring proposals, debugging hypotheses, review preparation. | Can use a task brief, identify assumptions, run or write checks, and revise an answer. |
| Engineering leads | Choosing safe use cases, setting review expectations, coaching teams, and interpreting evidence. | Can charter a pilot, spot unsupported productivity claims, and maintain accountability. |
| Architects and staff engineers | Design exploration, decision records, constraints, and architectural review. | Can use assistance to broaden options while retaining decision quality and traceability. |
| QA and test engineers | Test design, boundary analysis, exploratory ideas, and test-data-safe examples. | Can turn generated suggestions into executable, risk-based verification. |
| Security, privacy, and platform partners | Tool boundaries, data handling, integration risks, and escalation paths. | Can make safe use easy through clear guardrails and supported paths. |
| Product, delivery, and operations partners | Requirements clarification, summaries, planning support, incident analysis, and documentation. | Can distinguish a helpful draft from an approved decision or operational fact. |

Avoid lecture-only training. A good session has participants perform a task from their own work, review the output with a peer, and name what they would change next time.

## Team Practices

Introduce lightweight practices that make learning visible:

- A shared channel or brief weekly clinic for questions, examples, and failure reports.
- A small library of approved task briefs tied to common work, each including how its output was verified.
- Pull request or work-item disclosure when AI assistance materially affected a change, where this helps reviewers apply appropriate scrutiny.
- A recurring lead review of pilot evidence, policy questions, and support requests.
- An explicit incident route for suspected data leakage, harmful output, security concerns, or unexpected tool behavior.

The goal is not surveillance of every prompt. Collect enough information to improve practices, assess risk, and help teams reuse what works.

## Measure the Pilot

Use a balanced set of measures for the specific work being tested:

| Question | Possible evidence |
| --- | --- |
| Did flow improve? | Time to understand a subsystem, time to draft tests, review latency, cycle time for the selected task. |
| Did quality hold or improve? | Review findings, test failures, rework, escaped defects, rollback or incident signals. |
| Did people gain useful capability? | Confidence, repeat use on appropriate tasks, ability to explain verification, peer-shared patterns. |
| Did risk remain controlled? | Policy exceptions, data handling events, unsafe suggestions caught, unanswered escalation items. |

Use the data to learn, not to rank individuals. Individual activity counts such as prompt volume or generated-line counts are poor proxies for useful work and encourage unsafe behavior.

## Exit Criteria

Consider a team ready to invest in Phase 2 when it can demonstrate all of the following:

- Participants use approved tools and can explain applicable data and review boundaries.
- A few AI-assisted practices are embedded in real work and produce evidence of value or clear limits.
- The team has retained normal quality and security controls and knows how to escalate concerns.
- Leads can distinguish adoption noise from a real workflow improvement.
- The dominant constraint is now finding, trusting, and supplying relevant organizational context.

If the team cannot meet these conditions, continue Phase 1 with a narrower scope. More automation will not repair missing fluency, unclear guardrails, or weak engineering discipline.

## Next Step

When participants repeatedly need current architecture, codebase, policy, product, or operational knowledge that is scattered or hard to trust, move to [Phase 2: Context engineering](phase-2-context-engineering.md).

[Back to the adoption model](adoption-model.md)