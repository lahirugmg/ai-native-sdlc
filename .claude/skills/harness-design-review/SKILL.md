---
name: harness-design-review
description: "Review a proposed AI harness before implementation: task contract, access, controls, evaluation, and approvals. Use when: someone proposes automating an AI-assisted workflow; an agent or pipeline is being designed; a harness needs sign-off before shadow mode or wider rollout; an existing harness is expanding scope or gaining new permissions. Produces a completed harness design review with a qualification verdict and named approvals."
---

# Harness Design Review

Fills [templates/harness-design-review.md](../../../templates/harness-design-review.md).

The review's first job is to decide whether the workflow should be a harness at all. Most
proposals arrive before their workflow qualifies, and approving those is how organizations
automate unreliable processes.

## When to Invoke

- A workflow is proposed for automation.
- An agent, pipeline, or scheduled AI job is being designed.
- An existing harness is expanding its scope, permissions, or autonomy.

## Inputs

- The proposed workflow and its value hypothesis.
- Evidence that short-term fluency and medium-term context exist for it — a context map,
  ideally.
- Proposed integrations and the permissions they need.
- Named candidates for product, technical, risk, and support ownership.

## Procedure

1. **Qualify the workflow first.** Check every condition in the long-term playbook: a clear
   recurring outcome, describable inputs and exceptions, trusted context with owners, an
   observable definition of quality, an owner who can accept or roll back, and enough volume
   or risk reduction to justify the engineering.

   If it does not qualify, say so and stop. Name the missing condition and its owner. A
   harness does not compensate for unclear requirements, a broken process, or missing
   context — it amplifies them.

2. **Narrow the task contract until it is boring.** "Check a PR against standards" is not a
   contract. "Check against these named sources, refuse outside them, post advisory findings
   only" is. Push until inputs, output schema, refusal conditions, and the human decision
   point are all specific.

3. **Write the refusal conditions explicitly.** Every harness must recognize what it does
   not support: missing context, contradictory sources, oversized input, unsupported paths,
   sensitive data. A refusal that names its condition is a successful outcome.

4. **Apply least privilege to every grant.** A reviewer that can edit is not a reviewer. Ask
   what the harness could do if the model behaved arbitrarily, and confirm the answer is
   bounded by permissions rather than by instructions.

5. **Separate controls from prose.** For each control, ask where it is enforced. Schema
   validation, path allowlists, citation checking, secret scanning, and timeouts belong in
   code around the call. A control that depends on the model following instructions is a
   preference. The more important the control, the less it may depend on prose.

6. **Confirm retrieved content is treated as data.** PR descriptions, tickets, code
   comments, and tool output may contain instructions. The design must state that these
   cannot alter behaviour, and an evaluation case must prove it.

7. **Require an evaluation set before rollout,** with a stated case mix: normal, edge,
   ambiguous, missing-context, prohibited or adversarial, and operational failure. A set of
   only normal cases measures fluency, not reliability. Require a minimum progression gate
   stated numerically in advance.

8. **Require the operational floor:** named owner, kill switch reachable without approval,
   manual fallback that is complete on its own, audit record, incident route, and rollback.
   A harness without an owner is a pilot with delayed risk.

9. **Place the decision on the staged progression** — offline prototype, shadow mode,
   assisted mode, constrained action, wider rollout. Do not skip shadow mode for anything
   with customer, production, compliance, financial, or security impact unless a risk owner
   explicitly accepts an equivalent.

## Output

The completed review, with an explicit verdict: qualified or not qualified, and the stage
approved. Then:

- Each control, and whether it is enforced in code or requested in prose.
- Conditions attached by each approver.
- What would have to be true to reach the next stage.

## Red Flags

- A task contract broad enough that its refusal conditions cannot be enumerated.
- Controls that exist only as instructions to the model.
- Permissions granted for a plausible future need rather than the current contract.
- An evaluation set of only normal cases, or one assembled after the harness was built.
- A progression gate defined after results were seen.
- No kill switch, or one requiring approval to use.
- A manual fallback that has already been dismantled.
- Reviewers approving without conditions. A clean approval on a first design review usually
  means the contract was not pushed on.

## Verification

- [ ] The workflow was qualified against every long-term condition before design was reviewed.
- [ ] Refusal conditions are enumerated and each names its trigger.
- [ ] Every permission traces to a specific need in the contract.
- [ ] Each control is classified as code-enforced or prose-requested.
- [ ] Untrusted-content handling is specified and has an evaluation case.
- [ ] The evaluation set has a stated case mix and a numeric gate set in advance.
- [ ] Owner, kill switch, fallback, audit record, and rollback all exist and are named.
- [ ] Four approval roles recorded, with conditions.

[Template](../../../templates/harness-design-review.md) | [Worked example](../../../examples/03-harness-engineering/harness-design-review.md) | [Long-term playbook](../../../docs/long-term-harness-engineering.md)
