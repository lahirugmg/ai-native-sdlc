# Reference Implementation: Claude Code

## Scope of This Document

The horizon guides in this repository name no vendor or product, and that is deliberate —
the organizational conditions they describe hold regardless of tooling. This document is
the exception. It shows what the three horizons look like when instantiated in one specific
tool, so that the guidance has somewhere concrete to land.

Claude Code is used because its artifacts happen to separate along the same lines the
horizons do. Another tool would produce a different mapping and the same journey. Nothing
here is a recommendation to adopt a particular product; the
[readiness assessment](../assessments/adoption-readiness.md) governs that decision.

Read this after the horizon guide it corresponds to, not instead of it.

## The Mapping

| Horizon | What the guide asks for | Artifact in this tool | Worked example |
| --- | --- | --- | --- |
| Short term | Task briefs, verified output, retained accountability | No artifact — a person, a chat, and a review | [ai-task-brief](../examples/01-simple-integration/ai-task-brief.md) |
| Medium term | Repository instructions, context products, a context map | `CLAUDE.md` in the repository | [repository-instructions](../examples/02-context-engineering/repository-instructions.md) |
| Medium term | A repeatable procedure a team shares | A skill — `SKILL.md` in `.claude/skills/` | [.claude/skills/](../.claude/skills/) |
| Long term | Task contract, permitted context and tools, refusal behavior | An agent definition in `.claude/agents/` | [pr-standards-reviewer](../examples/03-harness-engineering/agents/pr-standards-reviewer.md) |
| Long term | Deterministic controls that do not depend on prose | Permission settings and hooks in `settings.json` | Below |
| Long term | Evaluation as a product feature | A maintained case set in the repository | [evaluation-set](../examples/03-harness-engineering/evaluation-set/) |

The important property is that the artifacts are ordered by how much they constrain
behaviour. Instructions ask, skills prescribe, agents bound, and settings enforce. That
ordering is the same one the journey uses, which is why a team that skips ahead usually
finds itself writing prose where it needed a control.

## Short Term: No Artifact Is the Right Answer

The short-term horizon needs a person who can frame a task and verify a result. It does not
need configuration. A team that responds to its first pilot by building a skill library has
usually mistaken enthusiasm for evidence — the pilot has not yet shown which procedures are
worth encoding.

The [task brief template](../templates/ai-task-brief.md) is a thinking aid used in a chat.
Its value is that it forces the same information a thoughtful colleague would need. Nothing
about it requires tooling.

Move past this only when the same context is being re-supplied by hand in task after task.
That repetition is the signal, and it is what the
[worked pilot](../examples/01-simple-integration/pilot-charter.md) detected in its review.

## Medium Term: Repository Instructions

`CLAUDE.md` is the repository-instructions context product. It loads automatically for work
in its repository, so it is the delivery mechanism for context the
[medium-term guide](medium-term-context-engineering.md) calls "versioned repository
guidance."

| Location | Loads |
| --- | --- |
| `~/.claude/CLAUDE.md` | Every project for one person. Personal preference, not team context |
| `<repo>/CLAUDE.md` | Any work in that repository. Checked in, reviewed, shared — this is the team context product |
| `<repo>/<subdir>/CLAUDE.md` | Only when work touches that subtree. For genuinely local conventions |

Three properties make it a context product rather than a prompt file, and all three come
from the medium-term guide:

- **It has an owner and a freshness mechanism.** Changing a convention without updating the
  instructions in the same pull request is a review finding. This is why repository
  instructions stay current while wiki pages rot.
- **It links rather than restates.** ADRs and READMEs remain sources of truth.
- **It states its own boundary.** Naming what the file does not cover is what stops silence
  being filled with invention — a failure the
  [context map's evaluation](../examples/02-context-engineering/context-map.md#evaluation-cases)
  caught.

Write it for a new human engineer. If it would not help a joiner in their first week, it is
prompt decoration rather than context.

## Medium Term: Skills

A skill is a procedure stored as `SKILL.md` with a `name` and `description`. The
description is how it is selected, so it must state when the procedure applies, not just
what it does.

| Location | Scope |
| --- | --- |
| `~/.claude/skills/<name>/SKILL.md` | Every project for one person |
| `<repo>/.claude/skills/<name>/SKILL.md` | That repository, for everyone who clones it |

Skills belong to the medium term because they are context products: a repeatable procedure
with an owner, versioned with the work it describes. They are not a harness. A skill
prescribes steps but enforces nothing — there is no contract, no refusal behaviour, no
evaluation, and no rollback. Treating a skill library as a harness is the most common way to
arrive at the long term without having done the long term's work.

Encode a procedure as a skill when a team performs it repeatedly and agrees on its shape.
Encoding it earlier freezes a practice before anyone knows whether it is correct. This
repository's own [skills](../.claude/skills/) operate its templates, and exist only because
the templates stabilized first.

## Long Term: Agents, Settings, and Evaluations

The [long-term guide](long-term-harness-engineering.md) lists eight harness components. They
map onto tooling unevenly, and where they map poorly is exactly where the engineering work
is:

| Harness component | Where it lives | Notes |
| --- | --- | --- |
| Task contract | The agent definition | Inputs, outputs, refusal conditions, and the human decision point |
| Context and capabilities | The agent's tool grants and read scope | Least privilege: a reviewer that can edit is not a reviewer |
| Orchestration | CI, a script, or a scheduled job | Deterministic. Not the model's responsibility |
| Validation | Code around the call, not instructions inside it | Schema checks and citation validation. The example's citation validator is load-bearing |
| Human interaction | The workflow the output enters | A pull request comment a reviewer may dismiss |
| Evaluation | A case set in the repository | See below |
| Observability | Structured logs from the surrounding job | Prompt hashes, sources read, refusal reasons, cost |
| Operations | An owner, a kill switch, a runbook entry | A harness without an owner is a pilot with delayed risk |

Only the first two are tool artifacts. The rest are ordinary software engineering, which is
the guide's point about keeping the deterministic shell strong: the more important the
control, the less it should depend on a model following prose.

**Settings enforce what prose only requests.** `settings.json` holds permission rules and
hooks. A permission denial is a control; an instruction not to do something is a
preference. When the design review says an agent must not write to the repository, the tool
grant is what makes that true.

**Evaluation is where most harnesses fail.** The
[worked evaluation record](../examples/03-harness-engineering/evaluation-record.md) is
included specifically because its result is negative: the harness passed its curated case
set and failed on live traffic, and the gate correctly refused progression. A case set
assembled from historical successes encodes the assumption that future inputs resemble past
ones.

## Where the Analogy Breaks

Three places, worth naming so the mapping is not over-read:

- **Skills auto-activate; agents mostly do not.** A skill is selected from its description
  during ordinary work. An agent generally has to be invoked. So the artifact that feels
  more powerful is the one less likely to run, which inverts the intuition that agents are
  the "more advanced" thing to build.
- **A composite skill is not orchestration.** A skill that chains sub-skills runs in one
  context, with no isolation between steps and no gate between them. Real phase gates need
  either separate agent invocations or deterministic code.
- **`CLAUDE.md` is not a policy engine.** It is read as instruction, and instructions can be
  overridden by content the model reads later. Anything that must hold — data boundaries,
  authorization, action limits — belongs in tool grants, permissions, or the surrounding
  code. The [governance guide](governance-and-risk.md) treats this as a control question,
  and it is.

## Adoption Order

The artifacts have a natural order, and it is the journey's order:

1. **Nothing.** Run the pilot. Find out which context is re-supplied by hand every time.
2. **`CLAUDE.md`.** Encode that context where the work happens. Review it like code.
3. **Skills**, once a procedure has proven stable enough to be worth freezing.
4. **An agent with a task contract**, once a workflow qualifies under the long-term gates.
5. **Settings, hooks, and an evaluation set**, before that agent takes any action.

Teams commonly start at 3 or 4 because those artifacts are the most visible and the most
satisfying to build. The result is a well-organized library that encodes procedures nobody
validated, running against context nobody owns.

[Journey guide](journey-to-ai-native-sdlc.md) | [Worked examples](../examples/) | [Skill library integration](skill-library-integration.md)
