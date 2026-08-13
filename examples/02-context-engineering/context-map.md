# Context Map — `claims-intake` Change Workflow

> Fictional worked example. Fills [templates/context-map.md](../../templates/context-map.md).
> Follows the [test-drafting pilot review](../01-simple-integration/pilot-charter.md),
> which identified context as the binding constraint.
> Scenario reference: [examples/README.md](../README.md).

## Workflow

| Field | Record |
| --- | --- |
| Workflow name | Making a routine change to the `claims-intake` service |
| Workflow owner | Staff Engineer, Claims Platform |
| Task outcome | A pull request that follows current service conventions, respects the service's boundaries, and carries tests an engineer can defend in review |
| Users or systems consuming the result | Claims Intake engineers, including joiners in their first weeks; peer reviewers; AI assistance used within the squad |
| Risk if context is wrong, missing, stale, or exposed | Wrong or stale conventions produce plausible changes that violate current boundaries — the pilot saw a deprecated builder resurface repeatedly. A change built on a superseded architecture assumption can bypass the PII-handling path, which is a privacy and audit risk, not only a quality one |
| Human verification or escalation point | Two-approval PR review, unchanged. Security partner review for any change touching PII or auth. Convention disputes escalate to the Staff Engineer |

## Context Sources

| Context needed | Source of truth | Owner | Freshness expectation | Access boundary | Delivery method | Include, exclude, or transform rule |
| --- | --- | --- | --- | --- | --- | --- |
| Service purpose, boundaries, and dependencies | `README.md` in `claims-intake` | Staff Engineer, Claims Platform | Reviewed each quarter and on any boundary change | Engineering access | Repository file | Include. Link to the ADR index rather than restating decisions |
| Local conventions, commands, and current patterns | `CLAUDE.md` in `claims-intake` | Claims Intake squad, via normal code review | Versioned with the code; changed in the PR that changes the convention | Engineering access | Repository file | Include. Name deprecated patterns explicitly — knowing what *not* to use proved as valuable as knowing what to use |
| Architectural decisions | `docs/adr/` in `claims-intake` | Staff Engineer, Claims Platform | Written per material decision; superseded ADRs marked, never deleted | Engineering access | Repository file | Include the index and current ADRs. Exclude superseded ones unless the task is historical |
| Acceptance criteria for the change | Backlog item in the tracker | Claims product owner | Per change | Team access | Explicit task attachment | Include the specific item only. Do not connect the whole tracker |
| Test conventions and fixtures | `src/test/.../ClaimFixtures.java` and the reference contract test | Claims Intake squad | Versioned with the code | Engineering access | Repository file, attached per task | Include. Attaching the closest existing test as a structural reference measurably improved output during the pilot |
| Security checklist for PII- and auth-touching changes | Corporate IT security wiki page | Corporate IT security partner | Reviewed twice a year | Engineering access | Repository copy, synchronized on review | Include as a repository copy with a version stamp and a link to the source. The wiki is not reachable from the engineer's local workflow |
| Runtime behaviour and incident history | Observability platform, incident records | Claims Intake squad | Continuous | Operational access, some records restricted | Not delivered to AI assistance in this workflow | **Exclude.** Production data carries policyholder information. Summarized incident learnings may be added to the runbook by a person |

## Context Package

| Question | Record |
| --- | --- |
| Smallest useful set of sources for a normal task | Repository `CLAUDE.md`, the specific backlog item, the files being changed, and the closest existing test. Four sources. The pilot showed larger packages made results harder to verify without making them better |
| Required citations, versions, timestamps, or provenance | The security checklist copy carries a version and a review date. ADRs carry status and date. For changes touching PII or auth, the engineer records which checklist version was applied on the pull request |
| Context that must never be included | Policyholder data, claim documents, production logs, production database contents, credentials, anything classified restricted. Unchanged from the pilot boundary |
| Known gaps, contradictions, or stale sources | The wiki architecture space is stale and partly contradicts current code; it is being retired rather than maintained, with anything worth keeping moved to ADRs by 30 June 2026. Two 2024 ADRs describe a queue topology that no longer exists — both marked superseded rather than deleted |
| What the workflow must do when context is missing or conflicting | Surface the conflict and stop. Do not average two conventions or pick the more recent silently. Where an ADR and the code disagree, the code is the fact and the ADR is the defect — raise it |

## Delivery and Control Design

| Area | Design |
| --- | --- |
| Delivery pattern | Versioned repository guidance. Chosen over a retrieval service because the workflow's sources are few, they live with the code, and they change through code review. Retrieval was considered and rejected as disproportionate for one service |
| Authorization | Repository permissions. Anyone who can read the code can read the context; nothing in the package is more sensitive than the source itself. No new access path was created |
| Data minimization | The package is source and documentation only. Production and customer data are excluded at the boundary rather than filtered afterwards. Fixtures are synthetic and were audited once for real-data contamination |
| Source lifecycle | `CLAUDE.md` changes in the same PR as the convention it describes — a convention change with no instruction update is a review finding. README reviewed quarterly. Security checklist copy re-synchronized when the source page is revised, tracked by a calendar reminder held by the security partner |
| Feedback route | An engineer who finds the instructions wrong, stale, or missing opens a PR against them directly, or raises `#claims-ai-pilot` if unsure. Correcting them is squad work, not the Staff Engineer's queue |
| Observability | Deliberately light. The squad tracks convention-drift findings raised in code review as the primary signal, and reviews them monthly. No per-prompt logging: it would not have caught the drift problem, and the pilot committed to not surveilling individual use |

## Evaluation Cases

Run 8 May 2026 against ten representative changes drawn from the previous quarter.

| Case | Expected source use or behavior | Result | Follow-up |
| --- | --- | --- | --- |
| Normal task | Uses the current fixture factory and `@SpringBootTest` convention; no deprecated patterns | 9 of 10 clean. One drafted a test with the deprecated builder, which appeared in a file the instructions did not mention | Added an explicit deprecated-patterns section to `CLAUDE.md`; re-ran that case clean |
| Edge or ambiguous task | Surfaces the ambiguity rather than choosing | 3 of 3 surfaced it. One also proposed a resolution, correctly labelled as a proposal | Acceptable. Labelling made the difference |
| Missing or stale context | States what is missing instead of inventing it | 2 of 3 stated it. The third invented a config property that does not exist, when asked about a subsystem the instructions do not cover | Documented the boundary of what the instructions cover, so the uncovered area is visible rather than silently filled |
| Unauthorized or prohibited source | Does not request or use production data; declines to proceed on a task requiring it | 2 of 2 declined and escalated | No change |

The one invented config property is the finding worth keeping. It appeared where the
context package was *silent* rather than wrong, which is the failure mode a context map
tends to hide: the map records what is included, not what the inclusion fails to cover.

## Decision Record

| Field | Record |
| --- | --- |
| Context map reviewers | Staff Engineer, Claims Platform; squad delivery lead; Corporate IT security partner |
| Approved delivery boundary | Repository sources and the specific backlog item. No production data, no cross-service retrieval, no tracker-wide connection |
| Open gaps and owner | Wiki architecture space retirement by 30 June 2026 — Staff Engineer. Subsystems not covered by the instructions to be enumerated — squad, ongoing |
| Next review date | 15 August 2026, or on any material boundary change |

Exit assessment: the workflow now has trusted sources with owners, a delivery path proven
on representative work, and evaluation evidence. It meets the medium-term exit criteria and
qualifies a candidate for the [long-term horizon](../03-harness-engineering/harness-design-review.md).

[Medium-term playbook](../../docs/medium-term-context-engineering.md)
