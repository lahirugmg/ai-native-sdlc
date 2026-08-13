---
name: context-map-build
description: "Build a context map for one recurring AI-assisted workflow, identifying trusted sources, owners, freshness, and access boundaries. Use when: a pilot review shows context is the constraint; assistance keeps producing plausible output that violates local conventions; repository instructions or a context product need designing; a workflow must qualify for the long-term horizon. Produces a completed context map plus a draft context product."
---

# Context Map Build

Fills [templates/context-map.md](../../../templates/context-map.md), and drafts the context
product the map calls for.

A context map is a contract for one workflow. It points at sources of truth and makes
missing ownership visible. It is not a place to copy organizational knowledge into.

## When to Invoke

- A short-term pilot review identified context as the binding constraint.
- Assistance repeatedly produces plausible output that violates current conventions.
- A workflow needs trusted context before it can qualify for a harness.

## Inputs

- One **recurring** workflow, named. Not a system, not a team — a workflow.
- Its owner, and what decision or artifact it produces.
- The sources practitioners actually consult, including the informal ones.
- Known stale, contradictory, or unowned sources.

## Procedure

1. **Start from the workflow, not the knowledge.** Ask what decision must be produced, what
   facts are needed to produce it well, which are authoritative, and what is stale or
   missing. A map built by inventorying available documents produces a catalogue nobody uses.

2. **For every source, require an owner and a freshness expectation.** A source with no
   owner is a gap, and recording it as a gap is the map's most useful output. Do not assign
   an owner who has not agreed.

3. **Decide the include, exclude, or transform rule per source.** Excluding is a real
   answer. Production data, customer records, and credentials are excluded at the boundary,
   not filtered afterwards.

4. **Find the smallest useful package.** More context is not better: it obscures key facts,
   raises cost and exposure, and makes verification harder. Record the minimum set for a
   normal task, and prefer it to the complete set.

5. **Choose the simplest delivery pattern that works.** Versioned repository guidance beats
   retrieval for a workflow whose sources are few and live with the code. Retrieval is not
   the default answer — justify it if chosen.

6. **State what the workflow does when context is missing or conflicting.** The correct
   behaviour is to surface the conflict and stop, not to average two conventions or silently
   prefer the more recent.

7. **Draft the context product.** Usually repository instructions. Three properties make it
   a product rather than a prompt file:
   - It changes in the same pull request as the thing it describes.
   - It links to sources of truth instead of restating them.
   - It states its own coverage boundary.

   Write it for a new human engineer. If it would not help a joiner in their first week, it
   is not context.

8. **Run the four evaluation cases** in the template: normal, edge or ambiguous, missing or
   stale context, and unauthorized source. The missing-context case is the one that matters
   most — it detects invention where the package is silent rather than wrong.

## Output

The completed map, plus a draft context product. Report separately:

- Sources with no owner, and who should own them.
- Contradictions found between sources, and which is the fact.
- What the context product does **not** cover, stated explicitly.
- Evaluation results, including any case where silence was filled with invention.

## Red Flags

- A map that duplicates content instead of pointing at it.
- An owner assigned without their agreement.
- Every source marked "include" — no exclusion decision was made.
- Retrieval chosen for a workflow with four sources.
- A context product with no coverage boundary. Silence then reads as coverage.
- Skipping the missing-context evaluation case, which is where invention appears.
- Building the map without asking practitioners which sources they actually consult.

## Verification

- [ ] The map covers one workflow, not a system or a team.
- [ ] Every source has an owner who agreed, and a freshness expectation.
- [ ] At least one source is excluded, with a stated reason.
- [ ] The smallest useful package is recorded and is smaller than the full source list.
- [ ] Behaviour on missing or conflicting context is specified.
- [ ] The context product states what it does not cover.
- [ ] All four evaluation cases ran, and failures were recorded rather than fixed silently.

[Template](../../../templates/context-map.md) | [Worked example](../../../examples/02-context-engineering/context-map.md) | [Medium-term playbook](../../../docs/medium-term-context-engineering.md)
