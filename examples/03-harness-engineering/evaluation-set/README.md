# Evaluation Set — PR Standards Reviewer

> Fictional worked example. The cases behind the [evaluation record](../evaluation-record.md).
> Scenario reference: [examples/README.md](../../README.md).

An evaluation set is the artifact that lets a harness change without silently regressing.
It is small, maintained, and versioned with the harness. This one holds 27 cases and is
deliberately not larger — the long-term playbook's point is that a maintained small set
beats an unmaintained large one.

## Structure

Each case is a directory holding the inputs captured at a real pull request's merge base,
plus the expected behaviour:

```
evaluation-set/
  cases.md                  ← the case index and expected behaviour, in this repository
  N-01/
    diff.patch              ← the change under review
    standards/              ← CLAUDE.md, security-checklist.md, adr/ as they were
    acceptance-criteria.md
    expected.md             ← what a correct run produces, and why
```

Only `cases.md` is reproduced here. The fixture directories would live alongside the
harness in the real repository.

## Why Cases Are Captured at the Merge Base

Standards move. A case that reads `CLAUDE.md` from `main` stops testing what it was written
to test as soon as the conventions change — the expected output silently becomes wrong, and
the set degrades without anyone noticing. Capturing sources alongside the diff freezes the
case.

This also makes a class of harness defect visible. Case M-05 exists because a live pull
request modified `CLAUDE.md` and code together, and the harness reviewed the code against
the pre-change standards. That behaviour is defensible, but it was not *decided* — it fell
out of the merge-base choice. The case pins the decision that the harness should refuse.

## Case Mix

The mix matters more than the count. A set of only normal cases measures fluency, not
reliability.

| Category | Count | Purpose |
| --- | --- | --- |
| Normal | 8 | The harness does its job on ordinary work |
| Edge | 4 | Unusual but supported inputs |
| Ambiguous | 3 | Compliance is genuinely unclear; the harness must say so rather than assert |
| Missing context | 5 | The standards are silent; the harness must name the gap, not invent a rule |
| Prohibited or adversarial | 3 | Refusal conditions and prompt injection |
| Operational failure | 4 | Transport failure, oversized diff, unreadable sources, missing backlog item |

## Maintenance Rules

- **Every confirmed failure becomes a case** before its fix is merged. A-01, M-04, and M-05
  entered the set this way.
- **Never delete a case to make a number improve.** Retire a case only when the behaviour
  it pins is no longer part of the contract, and record why in `cases.md`.
- **Re-run the whole set** on any change trigger listed in the
  [design review](../harness-design-review.md#evaluation-and-release-plan) — standards,
  prompt, model, schema, or allowlist.
- **Keep a live comparison.** The evaluation record's central finding was that the set
  passed while live traffic failed. A curated set drawn from merged pull requests
  systematically under-represents messy inputs, so it can never be the only evidence.

## What This Set Does Not Cover

Stated explicitly, because an unstated limitation reads as coverage:

- Only merged pull requests, so changes abandoned for quality reasons are absent.
- No case exercises concurrent edits by two authors on the same files.
- No case covers a standards source that is syntactically valid but internally
  contradictory.
- 27 cases is small. Precision computed on it carries a wide confidence interval and must
  not be reported as a precise figure.

[Evaluation record](../evaluation-record.md) | [Long-term playbook](../../../docs/long-term-harness-engineering.md)
