# Finding Your Organization's Path

## Start With the Work, Not the Tool

A journey to AI-assisted SDLC should begin with how your organization already creates, changes, operates, and explains software. The path is not a maturity score or a mandatory sequence of vendors. It is a set of choices about where assistance can remove real friction while preserving the people, controls, and feedback loops that make delivery trustworthy.

Use this guide with a delivery team, Corporate IT group, or software organization to find a sensible starting point. It works whether the capability areas below are separate teams, a small group of people wearing multiple hats, or external partners. What matters is that someone owns the work and its quality gate.

## Map One Real Flow of Work

Choose one recent feature, production change, incident, or compliance-driven change. Follow it from request to customer or operational outcome. For each handoff, record:

- The decision or artifact that moves the work forward.
- The accountable capability area, even if one person performs several roles.
- The evidence that makes the next person comfortable accepting the work.
- The information people repeatedly search for, reconcile, rewrite, or explain.
- The loop-backs caused by ambiguity, defects, security concerns, operational gaps, or missing documentation.

The goal is not to draw a perfect process map. It is to find the points where work becomes slow, error-prone, or dependent on institutional memory.

## Use Capability Areas, Not a Fixed Org Chart

Most software delivery flows need the following capability areas. They may overlap in a small organization, but their decisions and evidence should still be visible.

| Capability area | Typical handoff or evidence | Questions that reveal useful AI opportunities |
| --- | --- | --- |
| Product and requirements | Problem statement, acceptance criteria, scope, priorities | Where do people repeatedly clarify intent, reconcile stakeholder language, or find prior decisions? |
| Architecture and design | System design, interfaces, decision records, constraints | Where is technical rationale difficult to find, compare, or keep current? |
| Engineering | Implemented change, tests, review context, migration notes | Where do engineers spend time understanding code, tracing behavior, drafting tests, or preparing reviews? |
| Quality and testing | Test plan, defects, sign-off evidence, performance findings | Where are edge cases missed, test coverage hard to plan, or failures difficult to diagnose? |
| Security and risk | Threat model, findings, accepted-risk record, compliance evidence | Where do teams need help applying known controls or gathering evidence without replacing expert judgment? |
| Platform and delivery | Supported delivery path, pipeline records, infrastructure definitions, rollback plan | Where do teams repeat configuration, deployment, or environment work that has clear policy boundaries? |
| Operations and reliability | Service ownership, SLOs, dashboards, incident records, runbooks | Where do responders need to assemble context quickly or turn learnings into owned action? |
| Documentation and communication | Runbooks, guides, release notes, stakeholder summaries | Where is accurate information re-created after every change or difficult for the next person to follow? |

The table is not a waterfall. Security, operations, quality, and documentation should influence work early. A healthy journey makes the necessary loop-back visible: a failed test returns to engineering, a security finding can return to design, and an incident can generate work across requirements, architecture, and implementation.

## Find the Friction Worth Solving

For the flow you mapped, mark work that is frequent, bounded, reviewable, and currently costly. Favor the source of friction, not the most impressive demonstration.

| Friction pattern | What to investigate before selecting AI assistance |
| --- | --- |
| Searching and re-explaining | Is the needed information authoritative, current, permitted to use, and owned? |
| Drafting routine material | Is there a clear quality bar and a human who can efficiently review the draft? |
| Repeated analysis | Can inputs, expected output, exceptions, and correct behavior be described? |
| Slow or inconsistent handoffs | Can the receiving person name the evidence or quality gate they need? |
| Rework and late discoveries | Is the underlying problem a missing requirement, control, test, or decision rather than a lack of AI? |

Avoid using AI to hide a broken handoff. If acceptance criteria are unclear, a test draft may look helpful but it cannot make the feature testable. Improve the missing artifact or quality gate first.

## Choose the Next Horizon

Choose a horizon based on the current constraint, not an organization-wide calendar. Different teams and workflows can occupy different horizons at the same time.

| If you observe this | Start here | What to prove next |
| --- | --- | --- |
| People have useful low-risk tasks but lack approved tools, confidence, and shared practices. | Short term: simple AI integration | People can use assistance responsibly, verify results, and retain ownership. |
| Useful work repeatedly stalls because reliable requirements, architecture, code, policy, or operational facts are hard to locate or trust. | Medium term: context engineering | The workflow can receive the smallest authoritative, current, authorized context it needs. |
| A grounded workflow is frequent and predictable enough to describe, test, observe, and support. | Long term: harness engineering | The workflow is repeatable with evaluation, controls, human escalation, and a rollback path. |

Do not force every opportunity toward a harness. A well-used task brief or a maintained repository guide can be the best long-lived solution for a low-volume task.

## Run a Pathfinding Workshop

Bring the people who perform the work, own the relevant systems and information, and carry the risk when it goes wrong. A focused workshop can take 60 to 90 minutes.

1. Pick one real flow of work and define its outcome.
2. Name the capability areas, artifacts, handoffs, and quality gates involved.
3. Identify the top three sources of delay, rework, uncertainty, or cognitive load.
4. List candidate AI-assisted tasks and rule out work with unclear data, ownership, verification, or action boundaries.
5. Classify the remaining candidates by short, medium, or long-term horizon.
6. Choose one bounded experiment, owner, baseline, success measure, safety boundary, and review date.

Use the [SDLC opportunity map](../templates/sdlc-opportunity-map.md) to capture the result. Use the [adoption readiness assessment](../assessments/adoption-readiness.md) to test whether the selected experiment is ready to begin.

## Keep a Journey Portfolio

Maintain a small, visible portfolio rather than one enterprise claim that the organization is "AI mature." For each opportunity, record the workflow, current horizon, accountable owner, expected value, relevant risk, evidence, and next decision. This lets leaders compare learning across teams while leaving teams free to move at a pace that fits their work.

The path forward is a sequence of useful, verified changes to the way work moves through the SDLC. Begin where the organization can learn safely, make context trustworthy where it matters, and engineer a harness only when a workflow has earned the investment.

[Back to the repository overview](../README.md)