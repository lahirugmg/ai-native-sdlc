# Experiment Charter — AI-Assisted Test Drafting

> Fictional worked example. Fills [templates/pilot-charter.md](../../templates/pilot-charter.md).
> Scenario reference: [examples/README.md](../README.md).

## Identity and Decision

| Field | Record |
| --- | --- |
| Pilot name | AI-assisted test drafting for `claims-intake` |
| Journey horizon | Short term |
| Sponsor | Director of Engineering, Corporate IT |
| Accountable pilot owner | Claims Intake delivery lead |
| Participating team and roles | 7 Claims Intake engineers; peer reviewers within the squad; Corporate IT security partner consulted on the data boundary |
| Start date and review date | 17 February 2026 to 20 March 2026 (5 weeks) |
| Decision requested at review | Adapt, repeat, expand, pause, or stop |

## Problem and Hypothesis

| Field | Record |
| --- | --- |
| Current workflow and friction | Engineers write unit and contract tests by hand after implementing a change. It is the slowest step in the flow at a median 4.5 hours per standard change. The 70% changed-file coverage gate is met, but reviewers report assertions that would not fail if the business logic were removed |
| Bounded use case | Drafting unit and contract tests for a change already implemented in `claims-intake`, from the acceptance criteria and the diff |
| Hypothesis | If engineers use AI assistance to draft tests from acceptance criteria and the diff, then drafting time will fall without reducing assertion quality, because the assistant handles test scaffolding while the engineer supplies intent and verifies the assertions |
| Expected value | Delivery: less time in the slowest step. Quality: more edge cases considered. Learning: a first read on whether the squad's review controls absorb AI-assisted work |
| Out of scope | Generating implementation code; changing production; test data creation from real claims; any workflow touching policyholder data; modifying CI configuration |
| Assumptions and dependencies | Accounts provisioned before start; squad composition stable; the 6-week baseline is representative; delivery load does not spike during the window |

## Participants and Operating Design

| Field | Record |
| --- | --- |
| Participants and workload impact | All 7 engineers. One backlog item removed per engineer for the pilot period to protect practice time |
| Training and practice plan | 90-minute hands-on session in week 1 using the squad's own recent changes; weekly 30-minute clinic through week 5 |
| Approved tool, account, and support route | Corporate IT approved assistant, organization-managed accounts, zero-retention terms. Support through #corp-it-tooling; data and policy questions to #corp-it-security |
| Shared examples, clinics, or feedback channel | `#claims-ai-pilot` channel; a shared page of task briefs that worked, with the verification each one received; failures posted with equal prominence |
| Manual fallback | Write tests by hand, as today. No approval needed to fall back, and falling back is not treated as a negative signal |

## Data and Risk Boundaries

| Question | Record |
| --- | --- |
| What information may be used? | `claims-intake` source and existing tests; acceptance criteria from the backlog item; non-production fixtures; public library and framework documentation |
| What information must not be used? | Policyholder data, claim documents, production logs, production database contents, credentials or secrets, anything classified restricted |
| Does the work involve customer, personal, regulated, confidential, operational, or security-sensitive data? | The service processes policyholder personal data, so the boundary matters. The pilot's permitted inputs exclude it. Fixtures are synthetic and were checked for real-data contamination before the pilot |
| Required reviewers or escalation contacts | Normal two-approval PR review; Corporate IT security partner for boundary questions; delivery lead for stop decisions |
| Existing delivery, quality, security, and release controls that still apply | All of them, unchanged: two approvals, CI green, 70% changed-file coverage gate, security checklist for PII- or auth-touching changes, staging smoke tests, change record |
| Known failure modes and mitigation | Plausible tests with weak assertions — mitigated by an explicit reviewer instruction to check that each test would fail if the logic were removed. Fabricated API usage — mitigated by running every test before the PR. Boundary drift under deadline pressure — mitigated by the written boundary note and the weekly clinic |
| Stop or pause conditions | Any confirmed data-handling incident; reviewers reporting increased review burden without quality gain for two consecutive weeks; any escaped defect traced to an unverified AI-drafted test |

## Evidence Plan

| Dimension | Baseline | Measure during pilot | Success or safety threshold |
| --- | --- | --- | --- |
| Flow | Median 4.5 h to draft tests per standard change; PR review latency median 9 h | Same measures, same definitions, per change | Drafting time down at least 25% with review latency not worse than baseline |
| Quality | Changed-file coverage 71%; 3 escaped defects from missing test cases in the baseline window; reviewer-reported weak assertions on roughly 1 in 4 PRs | Coverage; escaped defects; a reviewer flag for weak assertions on every PR | Coverage not below 70%; no increase in escaped defects; weak-assertion flags not more frequent than baseline |
| Developer experience | Survey: median confidence 3/5 in test suite meaningfulness; orientation cost 2–4 days for new joiners | Repeat survey in week 5; short interviews | Confidence not lower; no participant reporting the practice as net-negative |
| Risk and trust | No prior AI-related policy exceptions recorded | Data-handling events; unsafe suggestions caught in review; escalations raised | Zero confirmed data-handling incidents |
| Adoption health | Not applicable before pilot | Engineers using the practice on appropriate tasks; clinic attendance; patterns contributed | At least 5 of 7 engineers using it on real work by week 4 |

## Review Record

Completed 20 March 2026.

| Question | Record |
| --- | --- |
| What evidence supports or contradicts the hypothesis? | **Supported in part.** Median drafting time fell from 4.5 h to 2.6 h (−42%). Coverage held at 72%. No increase in escaped defects. **But** review latency rose from 9 h to 12 h, because reviewers spent longer checking assertions they had not written. Net change to cycle time for a standard change was within noise. Weak-assertion flags fell slightly, from roughly 1 in 4 PRs to 1 in 6 |
| What did participants find useful or difficult? | Useful: enumerating edge cases from acceptance criteria, and scaffolding contract tests. Difficult: the assistant did not know squad conventions, so drafts used patterns the codebase had abandoned — for example the deprecated `ClaimStub` builder rather than the current fixture factory. Engineers spent meaningful time correcting convention drift rather than logic |
| What quality, security, privacy, or operational signals changed? | No data-handling incidents. No policy exceptions. Two occasions where an engineer asked in-channel whether a production log excerpt was permitted — the boundary note answered it, which is the control working |
| What context, tooling, training, or policy gap was exposed? | **Context, decisively.** The recurring cost was the assistant not knowing the service's conventions, current architecture, or which patterns were deprecated. That knowledge exists in people, chat threads, and an unowned wiki space. Engineers were re-supplying it by hand in every task brief |
| Decision, owner, and next review date | **Repeat and prepare medium-term work.** Continue the practice as normal squad work, unmeasured. Staff Engineer, Claims Platform owns the context work. Next review 15 May 2026 against the [context map](../02-context-engineering/context-map.md) |

The pilot's most valuable output was not the 42% drafting reduction, which review effort
largely absorbed. It was locating the constraint. A charter measuring only generation speed
would have reported a clean win and moved on with the real bottleneck untouched.

[Adoption readiness assessment](../../assessments/adoption-readiness.md) | [Short-term playbook](../../docs/short-term-simple-ai-integration.md)
