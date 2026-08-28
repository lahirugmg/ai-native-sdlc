# Adoption Readiness Assessment — Harbour Mutual, Claims Intake

> Fictional worked example. Fills the evidence record in
> [assessments/adoption-readiness.md](../../assessments/adoption-readiness.md).
> Scenario reference: [examples/README.md](../README.md).

Completed 10 February 2026 in a 2-hour session with the squad delivery lead, three
engineers, the Corporate IT security partner, and the platform team representative.
Ratings use the four-level language from the assessment. They are not averaged.

## Ratings by Area

| Area | Rating | Evidence | Gap or condition |
| --- | --- | --- | --- |
| 1. Outcome and ownership | 2 — usable for a bounded pilot | Delivery lead accepted the stop decision in writing; test drafting is a recurring task with a measured baseline; success is defined on quality and risk as well as speed | None blocking |
| 2. People and change readiness | 2 — usable for a bounded pilot | All 7 engineers volunteered; delivery lead removed one backlog item per person for the pilot period; code review and testing routines are healthy | Measurement principles published to the squad before start, to prevent the pilot reading as individual surveillance |
| 3. Tool, identity, and support path | 2 — usable for a bounded pilot | Corporate IT already licenses an approved assistant with organization-managed accounts and zero-retention terms; support route and cost owner known | Accounts provisioned for 7 engineers before the start date |
| 4. Data, privacy, security, and legal boundaries | 1 — emerging, constrained to proceed | Service source is classified internal; policyholder data is restricted. No existing written guidance on what may be entered into an assistant | **Condition:** pilot restricted to service source and non-production fixtures. Security partner issued a one-page boundary note before start. Re-rate before any medium-term work |
| 5. Delivery, quality, and measurement baseline | 2 — usable for a bounded pilot | 6-week baseline captured: drafting time, review latency, changed-file coverage, escaped defects; CI gates unchanged and still enforced | None blocking |
| 6. Knowledge and context | 1 — emerging | Engineers can name the sources they need; repository has a thin README; two ADRs exist for 18 months of decisions; architecture notes live in a wiki space with no owner | Accepted for short-term work. This is the area expected to constrain the next horizon |
| 7. Engineering and operational capability | 1 — emerging | CI/CD, logging, and rollback are sound; the PR-check workflow is not yet described as a contract and has no evaluation cases | Not required for short term. Blocks long-term work until rated 2 |

## Readiness Decision

| Field | Record |
| --- | --- |
| Pilot and workflow | AI-assisted drafting of unit and contract tests for `claims-intake` changes |
| Sponsor and accountable owner | Director of Engineering, Corporate IT; squad delivery lead |
| Participants and affected stakeholders | 7 Claims Intake engineers; peer reviewers; security partner; claims product owner |
| Journey horizon being considered | Short term |
| Readiness ratings by area | 1:2, 2:2, 3:2, 4:1 (constrained), 5:2, 6:1, 7:1 |
| Evidence and assumptions | Baseline drawn from 6 weeks of delivery data and a squad survey. Assumes squad composition and delivery load stay broadly stable through the pilot window |
| Known gaps and mitigation | Area 4 below the required rating — mitigated by restricting inputs to source and non-production fixtures, plus a written boundary note. Areas 6 and 7 are low but not required at this horizon |
| Data and tool boundary | Permitted: `claims-intake` source, tests, non-production fixtures, public library documentation. Prohibited: policyholder data, production logs, production database contents, credentials, claim documents, anything from the restricted classification |
| Success, safety, and stop conditions | As recorded in the [pilot charter](../01-simple-integration/pilot-charter.md) |
| Decision and review date | **Start short-term work with constraints.** Review 20 March 2026 |

## Why Not a Broader Start

Areas 6 and 7 rated 1. The assessment requires 2 for medium- and long-term work
respectively, so the PR-check idea from the opportunity map was explicitly deferred rather
than run in parallel. Training would not have closed either gap: area 6 needs owned and
current sources, and area 7 needs a described, testable workflow. Both are engineering and
ownership work, not enablement work.

[Back to the repository overview](../../README.md) | [Read the journey](../../docs/journey-to-ai-native-sdlc.md)
