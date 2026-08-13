# SDLC Opportunity Map — Harbour Mutual, Claims Intake

> Fictional worked example. Fills [templates/sdlc-opportunity-map.md](../../templates/sdlc-opportunity-map.md).
> Scenario reference: [examples/README.md](../README.md).

Mapped workflow: **a routine change to the `claims-intake` service** — from an accepted
backlog item to a deployed change. Mapped in a 90-minute session on 3 February 2026 with
the squad, its delivery lead, and the Corporate IT security partner.

## Flow of Work

| Step or capability area | Decision or artifact produced | Accountable owner | Receiving person or system | Acceptance evidence or quality gate | Friction, delay, or rework observed |
| --- | --- | --- | --- | --- | --- |
| Product and requirements | Backlog item with acceptance criteria | Claims product owner | Squad refinement | Refinement sign-off; criteria stated as examples | Criteria often restate the title; edge cases surface mid-implementation |
| Architecture and design | Change approach agreed in refinement; ADR if a boundary moves | Staff Engineer, Claims Platform | Implementing engineer | ADR merged for boundary changes | Only 2 ADRs written in 18 months; most decisions live in chat threads |
| Engineering | Pull request against `claims-intake` | Implementing engineer | Peer reviewer | 2 approvals, CI green | Newer engineers spend 2–4 days orienting before a first change |
| Quality and testing | Unit and contract tests in the PR; regression suite in CI | Implementing engineer | CI pipeline | Coverage gate at 70% on changed files | Test drafting is the slowest step; coverage gate met by weak assertions |
| Security and risk | Threat review for changes touching PII or auth | Corporate IT security partner | Release approver | Security checklist attached to the PR | Checklist is a static wiki page; reviewers apply it inconsistently |
| Platform and delivery | Deploy via shared pipeline to staging then production | Platform team | Claims Intake squad | Staging smoke tests, change record | Not a squad constraint; queueing on shared pipeline is occasional |
| Operations and reliability | On-call ownership, service runbook | Claims Intake squad | On-call rotation | Runbook reviewed after each Sev2 | Runbook drifts between incidents |
| Documentation and communication | Release note, API changelog | Implementing engineer | Claims portal team, support | Release note in the change record | Written last, sometimes skipped under delivery pressure |

## Candidate Opportunities

| Candidate task | Workflow step | User or beneficiary | Friction to reduce | Journey horizon | Human verification or decision | Data and access boundary | Expected value | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Draft unit and contract tests from acceptance criteria and the changed code | Quality and testing | Implementing engineers | Slowest step in the flow; weak assertions pass the coverage gate | Short term | Engineer revises and runs every test; normal PR review applies | Service source and non-production fixtures only; no policyholder data | Faster test drafting, and better assertions if quality holds | Squad delivery lead |
| Orient a new engineer in the service before a first change | Engineering | Engineers new to the squad | 2–4 day orientation cost per joiner | Medium term | Engineer confirms findings against source before acting | Repository contents; architecture notes are scattered and partly stale | Shorter time to first safe change | Staff Engineer, Claims Platform |
| Check a pull request against the security checklist and service standards | Security and risk | Reviewers, security partner | Checklist applied inconsistently; findings arrive late | Long term | Advisory only; reviewer and security partner still decide | Diff and repository standards; no production or customer data | Consistent early findings, less rework after security review | Corporate IT security partner |

Horizon selection followed the guide in the template. Test drafting is bounded, low risk,
and reviewable, so it is short term. Orientation depends on architecture facts that are
currently scattered and partly stale, so it is medium term — the constraint is trustworthy
context, not tool access. The PR check is recurring and describable but has no evaluation
set, no owner for the standards it would enforce, and no rollback story, so it is long term
and not yet qualified.

## Select the Next Experiment

| Field | Record |
| --- | --- |
| Chosen candidate | Draft unit and contract tests from acceptance criteria and changed code |
| Why this is the best next learning opportunity | It is the squad's slowest step, it is reviewable by people who already own the review, and it needs no new integration or data boundary. A failure is visible in the pull request rather than in production. |
| Current journey horizon | Short term |
| Sponsor and accountable owner | Director of Engineering, Corporate IT (sponsor); squad delivery lead (accountable owner) |
| Participants and affected stakeholders | 7 Claims Intake engineers; peer reviewers; Corporate IT security partner as consulted party |
| Baseline evidence | 6-week window before the pilot: median 4.5 hours to draft tests for a standard change; PR review latency median 9 hours; changed-file coverage 71%; 3 escaped defects attributable to missing test cases |
| Success, safety, and stop conditions | Success: test drafting time falls with no fall in coverage, review findings, or escaped defects. Safety: no policyholder data enters the tool. Stop: any confirmed data-handling incident, or reviewers reporting that AI-drafted tests are increasing review burden without quality gain. |
| Required tool, data, security, privacy, architecture, or operations decisions | Confirm the approved assistant and account type with Corporate IT; confirm that non-production fixtures are acceptable inputs; no architecture or operations decision required |
| Manual fallback and escalation route | Engineers write tests as they do today; escalate tool or data questions to the security partner through the existing #corp-it-security channel |
| Review date and decision | 20 March 2026 — see [pilot charter](../01-simple-integration/pilot-charter.md) |

## Revisit After Review

Reviewed 20 March 2026. The evidence confirmed value in the selected task but relocated the
constraint: engineers repeatedly needed architecture and convention facts that the
repository did not hold reliably. The map's second candidate was promoted, and the squad
moved to medium-term work. See [context map](../02-context-engineering/context-map.md).

[Finding your organization's path](../../docs/finding-your-path.md) | [Journey to AI-Assisted SDLC](../../docs/journey-to-ai-assisted-sdlc.md)
