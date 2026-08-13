---
name: sdlc-opportunity-scan
description: "Map one real flow of work through an SDLC and select a safe next AI-assistance experiment. Use when: a team is deciding where to start with AI adoption; someone asks which workflow to pilot; an opportunity map needs filling in; a proposed AI use case needs a horizon assigned. Produces a completed SDLC opportunity map with candidates, horizons, and one selected experiment."
---

# SDLC Opportunity Scan

Fills [templates/sdlc-opportunity-map.md](../../../templates/sdlc-opportunity-map.md) for one
real flow of work.

The output is a decision about where to start, supported by observed friction. It is not an
idealized process diagram, and it is not a list of everything AI could theoretically do.

## When to Invoke

- A team is deciding where to begin with AI assistance.
- Someone proposes an AI use case and its horizon is unclear.
- A previous experiment's review has relocated the constraint and a new candidate is needed.

## Inputs

Ask for these before starting. Do not infer them from the codebase alone — the friction
lives in how people work, not in the source:

- One **real, recent** unit of work: a feature, change, incident, or operational request.
  Not a representative composite.
- Who owns each decision in that flow, and who receives each artifact.
- Where the work actually stalls, and how the team knows.
- Any known data, tool, or regulatory boundary.

If the team offers a hypothetical workflow, ask for a specific recent example instead. A
composite workflow hides exactly the friction the map exists to find.

## Procedure

1. **Trace one unit of work end to end.** For each capability area in the template, record
   the decision or artifact produced, the accountable owner, the receiver, the acceptance
   evidence, and the friction observed. Use only rows that exist in this workflow — an empty
   row is a finding about ownership, not a gap to fill with plausible text.

2. **Locate friction with evidence.** "Testing is slow" is not usable. "Median 4.5 hours to
   draft tests, and reviewers flag weak assertions on one in four PRs" is. Where the team
   has no measure, record that the baseline is missing; it becomes pilot work.

3. **Derive candidates from observed friction only.** Every candidate must trace to a
   specific row in the flow. Do not add candidates because they are common elsewhere.

4. **Assign a horizon per candidate** using the template's selection guide. Apply the
   disqualifiers honestly:
   - Short term needs clear tool access, data boundaries, and existing review controls.
   - Medium term needs a known source of truth, owner, freshness, and access boundary. If
     those are unknown, the candidate is not medium term — establishing them *is* the work.
   - Long term needs a task that can be tested, supported, and safely stopped.

   Most candidates a team proposes are one horizon further along than their evidence
   supports. Say so when that is the case.

5. **Select one experiment.** Prefer the candidate where a failure is most visible and
   cheapest — a bad result caught in code review beats one caught in production. Record
   baseline evidence, stop conditions, and the manual fallback.

6. **Record deferred candidates and why.** A candidate deferred with a stated reason
   becomes the next horizon's agenda. A candidate silently dropped is re-proposed in three
   months.

## Output

The completed template with every section filled. Then, separately:

- The **one** selected experiment and why it is the best next learning opportunity.
- Deferred candidates, each with the specific gap that defers it and who owns closing it.
- Missing baselines that must be captured before the experiment starts.

## Red Flags

- A flow with no friction recorded — the workflow was described aspirationally, not observed.
- Every candidate assigned to the same horizon.
- A candidate whose value depends on the AI system making an unreviewed decision.
- Selecting the highest-value candidate rather than the highest-learning one. Early
  experiments buy information, not throughput.
- Filling the map from the repository without talking to anyone who does the work.

## Verification

- [ ] Every candidate traces to a specific friction row in the flow.
- [ ] Every horizon assignment was checked against the disqualifiers, not only the criteria.
- [ ] The selected experiment has baseline evidence, or a named gap to capture it.
- [ ] Stop conditions are stated and would actually be noticed if they occurred.
- [ ] A manual fallback exists and needs no approval to use.

[Template](../../../templates/sdlc-opportunity-map.md) | [Worked example](../../../examples/00-start/sdlc-opportunity-map.md) | [Finding your path](../../../docs/finding-your-path.md)
