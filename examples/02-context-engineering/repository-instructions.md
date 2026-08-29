# Repository Instructions — `claims-intake`

> Fictional worked example. Fills the *repository instructions* context product from
> [Medium term: Context engineering](../../docs/medium-term-context-engineering.md#create-context-products).
> Delivers the package designed in the [context map](context-map.md).
> Scenario reference: [examples/README.md](../README.md).

Repository instructions are the first context product most teams should build. They are
cheap, they live with the code, they change through normal code review, and they improve
human onboarding whether or not AI assistance is involved.

The file below would live at the root of the `claims-intake` repository as `CLAUDE.md`. It
is reproduced here as a fenced block rather than as a live file so that it stays an
example — a real `CLAUDE.md` in this directory would be loaded as instructions for *this*
repository.

## The Artifact

````markdown
# CLAUDE.md

Instructions for working in `claims-intake`. Change this file in the same pull request as
the convention it describes.

## What This Service Is

Claims intake for the policyholder portal. Accepts claim submissions, validates them
against policy records, detects duplicates, and publishes accepted claims to the
`claims.submitted` topic for downstream adjudication.

It does **not** adjudicate claims, calculate payouts, or hold the policy system of record.
Boundaries and dependencies: `README.md`. Decisions: `docs/adr/`.

## Data Handling

This service processes policyholder personal data. Non-negotiable:

- Never paste production data, production logs, or claim documents into any tool.
- Never log a full `ClaimSubmissionRequest`. Use `ClaimLogView`, which redacts the
  claimant block.
- Test fixtures are synthetic. Do not derive a fixture from a real claim, even redacted.
- Changes touching PII or authentication require security partner review before merge.
  Record which checklist version you applied on the pull request. Current copy:
  `docs/security-checklist.md` (v4, reviewed 2026-01-20).

## Commands

| Task | Command |
| --- | --- |
| Build | `./gradlew build` |
| Unit tests | `./gradlew test` |
| Contract tests (starts Testcontainers Postgres) | `./gradlew contractTest` |
| Lint and format | `./gradlew spotlessApply` |
| Run locally against the stub policy service | `./gradlew bootRun --args='--spring.profiles.active=local'` |

`./gradlew contractTest` needs Docker running. It is the check that most often fails in CI
after passing locally — run it before opening a pull request.

## Conventions

- **Fixtures:** use `ClaimFixtures`. It is the current factory.
- **Contract tests:** `@SpringBootTest` with the shared Testcontainers Postgres. Follow the
  structure in `DuplicatePolicyLookupContractTest`.
- **Test names** state the rule being verified, not the method being called:
  `rejectsSecondSubmissionForSamePolicyAndLossDateWithin24Hours`, not `testDuplicate`.
- **Assertions verify behaviour.** A test that would still pass with the business logic
  deleted is a defect. Delete the branch locally and confirm your test fails.
- **Persistence** goes through repository interfaces in `claims.intake.store`. No
  `EntityManager` in controllers or services.
- **Times** are `Instant` in UTC at every boundary. The 24-hour duplicate window is a
  `Duration` comparison, never a local-date comparison — a naive local comparison caused a
  DST defect in March 2026.

## Deprecated — Do Not Use

Knowing what to avoid matters as much as knowing what to use. These still appear in the
codebase and are being removed:

| Pattern | Use instead | Notes |
| --- | --- | --- |
| `ClaimStub` builder | `ClaimFixtures` | Remaining usages tracked in CLAIM-2903 |
| `LocalDateTime` in domain types | `Instant` | Source of the March 2026 DST defect |
| `@MockBean` for the policy client | `PolicyClientStub` | `@MockBean` restarts the Spring context and roughly triples suite time |
| Direct `claims.submitted` publishing from a controller | `ClaimEventPublisher` | Publishing must be transactional with persistence |

## What This File Does Not Cover

Be explicit about the boundary rather than letting it be filled in silently. Not covered
here — confirm against source or ask the squad:

- The batch reconciliation job in `claims.intake.batch`, which predates current conventions.
- Deployment pipeline configuration, owned by the platform team.
- The policy service contract, owned by the Policy Platform squad.

If something needed is absent from this file and the attached sources, say so. Do not infer
a configuration property, repository method, or convention that is not present.

## Related

`README.md` · `docs/adr/` · `docs/security-checklist.md`
````

## Why It Is Shaped This Way

Each section answers a failure observed in the
[test-drafting pilot](../01-simple-integration/pilot-charter.md) or the context map's
evaluation. None of it is speculative.

| Section | Failure it answers |
| --- | --- |
| Data handling | The pilot's boundary note lived outside the workflow. Moving it next to the code puts it where the decision is made |
| Commands | Contract tests passing locally and failing in CI was the squad's most common wasted review cycle |
| Conventions | Convention drift was the pilot's largest correction cost |
| Deprecated | The deprecated `ClaimStub` builder reappeared even when the current factory was attached. Naming what *not* to use fixed the case that re-ran clean |
| What this file does not cover | The evaluation's one invented config property appeared where the package was silent. An explicit boundary makes silence visible |

## Practices Worth Copying

- **Version it with the code.** A convention change whose PR does not update the
  instructions is a review finding. This is the whole reason repository instructions stay
  fresh while wiki pages rot.
- **Link, do not restate.** ADRs and the README stay the sources of truth. Duplicating them
  here creates a second thing to keep current.
- **State the negative space.** Deprecated patterns and uncovered areas do more work than
  another paragraph of description.
- **Write it for a new engineer.** Everything above helps a human joiner in their first
  week. That is the test of whether it is real context or prompt decoration.
- **Keep it short.** This file is roughly 90 lines. The evaluation found that larger
  packages did not improve results and made verification harder.

[Medium-term playbook](../../docs/medium-term-context-engineering.md) | [Context map](context-map.md)
