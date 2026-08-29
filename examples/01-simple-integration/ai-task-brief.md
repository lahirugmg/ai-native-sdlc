# AI Task Brief — Contract Tests for Duplicate Claim Rejection

> Fictional worked example. Fills [templates/ai-task-brief.md](../../templates/ai-task-brief.md).
> One bounded task from inside the [test-drafting pilot](pilot-charter.md).
> Scenario reference: [examples/README.md](../README.md).

## Task

| Field | Record |
| --- | --- |
| Title | Contract tests for duplicate claim rejection in `POST /claims` |
| Requester and accountable practitioner | Implementing engineer, Claims Intake squad — accountable for the merged result |
| Desired outcome | A set of contract tests covering the new duplicate-detection rule, written against the existing test conventions, that an engineer will review and run before opening the pull request |
| Audience | The implementing engineer, then two squad peer reviewers |
| Completion condition | Tests compile, run, and fail if the duplicate-detection branch is removed; every acceptance criterion has at least one corresponding case; edge cases are listed even where a test was not written |

## Relevant Context

| Context | Source or location | Why it matters | Approved to share or connect? |
| --- | --- | --- | --- |
| Requirements or acceptance criteria | CLAIM-2841, four GIVEN/WHEN/THEN criteria | Defines what "duplicate" means: same policy number, same loss date, submitted within 24 hours | Yes — internal backlog item, no policyholder data |
| Code, interfaces, or architecture | `ClaimIntakeController`, `DuplicateClaimDetector`, `ClaimSubmissionRequest` | The rule's implementation and the request contract under test | Yes — internal source |
| Standards, policies, or constraints | `src/test/java/.../ClaimFixtures.java`; squad convention that contract tests use `@SpringBootTest` with the shared Testcontainers Postgres | Drafts must use current conventions; the `ClaimStub` builder is deprecated and must not be used | Yes — internal source |
| Representative examples | `DuplicatePolicyLookupContractTest` — the closest existing test in shape | Shows the expected structure, naming, and assertion style | Yes — internal source |
| Known ambiguity or missing information | Criteria do not state behavior when the loss date is absent, or when two submissions arrive in the same second | Both are plausible production cases and the rule is silent on them | Ambiguity to surface, not to resolve unilaterally |

Only the four files above were attached. The full repository was not, because the task is
bounded and a larger context package would have made the result harder to check.

## Instructions and Boundaries

```text
Outcome:
Draft contract tests for the duplicate claim rejection rule added to POST /claims.

Relevant context:
- Acceptance criteria from CLAIM-2841 (attached, four GIVEN/WHEN/THEN cases)
- DuplicateClaimDetector and ClaimIntakeController (attached)
- ClaimFixtures.java — the current fixture factory (attached)
- DuplicatePolicyLookupContractTest — follow this file's structure and naming (attached)

Constraints and non-goals:
- Do not modify implementation code. Tests only.
- Use ClaimFixtures. Do not use ClaimStub; it is deprecated and being removed.
- Use @SpringBootTest with the shared Testcontainers Postgres, as the reference test does.
- Do not invent repository methods, fields, or configuration. If something needed is
  absent from the attached files, say so rather than assuming it exists.
- No real or realistic policyholder data. Synthetic values only.

Quality expectations:
- Every acceptance criterion has at least one test.
- Each test must fail if the duplicate-detection branch is removed. Assertions on
  behaviour, not on the shape of the response alone.
- Test names state the rule being verified, following the reference file's convention.

Assumptions to surface:
List every assumption made about behaviour not stated in the criteria, before the tests.
Two are already known to be unspecified: absent loss date, and two submissions in the
same second. Do not silently choose behaviour for these — flag them.

Requested output format:
1. A short list of assumptions and open questions.
2. The test file.
3. Edge cases you did not write tests for, and why.

Verification requested:
State which attached file each assertion is grounded in, so I can check it without
re-reading everything.
```

## Verify Before Use

- [x] Check claims against the cited or underlying sources. — Two assertions referenced a
      `findByPolicyAndLossDate` method that does not exist; the repository exposes
      `findRecentByPolicy`. Corrected by the engineer.
- [x] Review assumptions, omissions, and contradictions. — Both known ambiguities were
      surfaced as asked. A third was raised that the engineer had not considered: whether a
      duplicate submitted by a different user should be rejected. Taken back to the product
      owner; criteria updated.
- [x] Run relevant tests, linters, security checks, or operational validation. — All tests
      run. One failed against the real implementation and correctly identified a gap: the
      24-hour window used a naive local-time comparison, wrong across a DST boundary.
- [x] Apply normal peer review and approval requirements. — Two approvals obtained.
- [x] Remove or correct unsupported content before sharing or acting on it. — Fabricated
      repository method removed; deprecated `ClaimStub` usage in one test replaced.
- [x] Record a useful pattern or a notable failure for the team. — Posted to
      `#claims-ai-pilot`: attaching the closest existing test as a structural reference
      materially improved convention adherence, though it did not eliminate drift.

## Result Record

| Field | Record |
| --- | --- |
| What was used | 6 of 7 drafted tests, after correction. The seventh duplicated existing coverage and was dropped |
| What was changed by the practitioner | Removed a fabricated repository method and repointed two assertions; replaced deprecated `ClaimStub` usage; renamed three tests to match squad convention; added the DST case as its own test |
| Verification performed | Full test run; mutation check by deleting the duplicate-detection branch and confirming failures; peer review by two engineers |
| Outcome and value observed | Drafting took 1.5 h against a typical 4 h for comparable work. The DST defect would probably have reached production; the baseline suite had no equivalent case |
| Failure modes, risks, or follow-up | Convention drift is the recurring cost — the deprecated builder appeared despite the current factory being attached. Fabricated methods appear when a needed capability is absent from the attached context. Both point at repository-level context rather than better task briefs, which became the [medium-term work](../02-context-engineering/context-map.md) |

[Short-term playbook](../../docs/short-term-simple-ai-integration.md)
