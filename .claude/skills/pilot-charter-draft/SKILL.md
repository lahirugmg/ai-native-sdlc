---
name: pilot-charter-draft
description: "Draft an evidence-gated experiment charter for a bounded AI-assistance pilot. Use when: an experiment has been selected and needs boundaries, measures, and stop conditions; a pilot is running without a written hypothesis; a charter needs a review record completed. Produces a one-to-two page charter with hypothesis, data boundaries, a balanced evidence plan, and stop conditions."
---

# Pilot Charter Draft

Fills [templates/pilot-charter.md](../../../templates/pilot-charter.md).

A charter's job is to make the pilot falsifiable before it starts. A pilot without a stated
hypothesis and stop conditions cannot fail, and a pilot that cannot fail produces no
evidence.

## When to Invoke

- An experiment has been selected, typically by the sdlc-opportunity-scan skill.
- A pilot is already running without written boundaries.
- A pilot has concluded and its review record needs completing.

## Inputs

- The selected experiment and the workflow it touches.
- Baseline evidence, or an explicit statement that none exists.
- The approved tool, account type, and data-handling position.
- Sponsor and accountable owner, both named.

## Procedure

1. **Write the hypothesis as a falsifiable claim.** Use the template's form: if we use this
   assistance for this work, then we expect this outcome, because this mechanism. The
   "because" is what makes it testable — without a mechanism, any result confirms the
   hypothesis.

2. **Bound the use case narrowly.** State what is out of scope explicitly, including
   adjacent work the team will be tempted toward. "Drafting tests for an implemented change"
   is bounded; "improving testing" is not.

3. **Write the data boundary as instructions, not principles.** A participant under
   deadline pressure needs a list they can check against, not a policy to interpret. Name
   the permitted inputs and the prohibited ones separately.

4. **Build a balanced evidence plan.** Fill all five dimensions — flow, quality, developer
   experience, risk and trust, adoption health. A plan measuring only flow will report
   success whenever work moves faster, including when it moves faster because quality fell.

   For each dimension: the baseline, the measure during the pilot using the same definition,
   and the threshold. Where no baseline exists, say so rather than inventing one.

   Never make prompt counts, generated-line counts, or raw activity a primary measure.

5. **Write stop conditions that would actually be noticed.** "Quality degrades" is not a
   stop condition. "Any escaped defect traced to an unverified AI-drafted test" is. Each
   condition needs an observer who would see it.

6. **Protect practice time.** Record the specific workload reduction. A pilot expecting
   people to learn a new working method in the gaps between delivery commitments has a
   predictable outcome.

7. **When completing the review record**, report what the evidence shows, including where it
   contradicts the hypothesis. A pilot that relocates the constraint has succeeded even if
   its headline measure barely moved — record that reasoning explicitly, because it is the
   result most likely to be misread as failure.

## Output

The completed charter. When drafting, flag separately:

- Any measure that lacks a baseline.
- Any stop condition without an observer.
- Any data-boundary question the charter cannot answer, and who owns it.

## Red Flags

- A hypothesis with no mechanism, so no result can contradict it.
- An evidence plan filling only the flow row.
- Success thresholds set after the pilot began.
- Out-of-scope left blank. Scope creep is the default, not the exception.
- A stop condition nobody is positioned to observe.
- Claiming value against a baseline that was never captured.

## Verification

- [ ] The hypothesis states a mechanism and could be contradicted by a plausible result.
- [ ] Out-of-scope is explicit and includes the adjacent temptations.
- [ ] The data boundary lists permitted and prohibited inputs separately.
- [ ] All five evidence dimensions have a baseline, a measure, and a threshold — or a
      recorded gap.
- [ ] No activity-volume measure is primary.
- [ ] Each stop condition has an observer.
- [ ] Practice time is quantified, not asserted.

[Template](../../../templates/pilot-charter.md) | [Worked example](../../../examples/01-simple-integration/pilot-charter.md) | [Short-term playbook](../../../docs/short-term-simple-ai-integration.md)
