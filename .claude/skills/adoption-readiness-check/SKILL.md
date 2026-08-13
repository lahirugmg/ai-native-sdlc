---
name: adoption-readiness-check
description: "Rate a team's readiness across the seven adoption areas and decide whether a pilot can responsibly start. Use when: a pilot is proposed and its foundation is unverified; a team asks whether it is ready for AI adoption; a horizon advance is being considered; readiness gaps need to be separated from enablement gaps. Produces per-area ratings with evidence and one of four readiness decisions."
---

# Adoption Readiness Check

Fills the evidence record in
[assessments/adoption-readiness.md](../../../assessments/adoption-readiness.md).

This is a structured conversation and evidence record. It is not a maturity score, and the
ratings are never averaged — a strong tool platform does not compensate for unclear data
boundaries.

## When to Invoke

- A pilot has been proposed and its foundation has not been checked.
- A team wants to move to the next horizon.
- A readiness gap needs to be distinguished from a training gap.

## Inputs

- The proposed pilot and its workflow.
- Who the sponsor and accountable owner are.
- The horizon being considered.
- Access to the people who own security, privacy, platform, and delivery decisions — this
  assessment cannot be completed from the repository.

## Procedure

1. **Rate each of the seven areas** using the assessment's four-level language: 0 unknown or
   absent, 1 emerging, 2 usable for a bounded pilot, 3 repeatable and scalable.

   For each rating, record the **evidence observed**, not the impression formed. A rating
   without evidence is an opinion, and this record exists to survive disagreement.

2. **Apply each area's stated threshold** rather than a general sense of readiness. The
   thresholds differ by horizon and are not interchangeable:

   | Area | Threshold |
   | --- | --- |
   | 1. Outcome and ownership | 2 for any horizon |
   | 2. People and change readiness | 2 for any horizon |
   | 3. Tool, identity, and support | 2 for short term |
   | 4. Data, privacy, security, legal | 2 for short term |
   | 5. Delivery, quality, measurement | 1 for short term, aiming for 2 |
   | 6. Knowledge and context | 2 for medium term |
   | 7. Engineering and operational capability | 2 for long term |

3. **Do not average.** Report the seven ratings individually. If asked for one number,
   explain why the assessment refuses to produce one.

4. **Separate the gap types.** For every area below threshold, classify the gap:
   - **Enablement gap** — training or practice closes it.
   - **Ownership gap** — someone must accept accountability.
   - **Control gap** — a boundary, permission, or process must exist.
   - **Evidence gap** — a baseline must be captured.

   Training closes only the first. Proposing training for the other three is the most common
   error this check exists to prevent.

5. **Reach one of the four decisions** in the assessment: start a bounded experiment, start
   with constraints, invest in a foundation first, or prepare a medium- or long-term
   candidate. When choosing "start with constraints," state the constraint precisely enough
   that a participant could follow it without interpretation.

## Output

The evidence record, with per-area ratings and evidence. Then:

- The decision, with the specific ratings that drove it.
- For each below-threshold area: the gap, its type, its owner, and whether it blocks.
- The data and tool boundary, written so a participant can apply it without asking.

## Red Flags

- Averaging ratings, or reporting a single readiness score.
- Rating from documentation without talking to the owners named in it.
- Rating area 4 at 2 because a policy exists somewhere, rather than because participants
  can state what they may and may not do.
- Proposing training for an ownership or control gap.
- Rating area 6 or 7 at 2 to unblock a horizon the team wants to reach. These are the two
  areas most often inflated, because the work they imply is slow.
- Treating a low rating as failure. A 1 with a named owner is a plan.

## Verification

- [ ] All seven areas rated, each with observed evidence.
- [ ] Ratings compared against per-area thresholds for the horizon in question.
- [ ] No average or composite score produced.
- [ ] Every below-threshold area has a gap type and an owner.
- [ ] The data boundary is stated in terms a participant can apply.
- [ ] The decision follows from the ratings rather than from the team's preference.

[Assessment](../../../assessments/adoption-readiness.md) | [Worked example](../../../examples/00-start/adoption-readiness.md) | [Journey guide](../../../docs/journey-to-ai-assisted-sdlc.md)
