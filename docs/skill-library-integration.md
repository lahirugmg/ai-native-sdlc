# Adopting an External Skill Library

## Why This Is a Separate Question

This repository is about the organizational conditions for AI-assisted work. Agent and
skill libraries are a different kind of artifact: catalogues of procedures, usually
organized by role. The two are complementary, and conflating them is a common way to spend
effort without changing outcomes.

A library gives a team procedures. It does not give them owned context, an evidence
baseline, review capacity, or a decision about which work should be assisted at all. A team
that installs 70 skills before running a pilot has acquired a catalogue, not a capability.

This document covers how to adopt an external library once a team has reached the point
where one helps, and what to check before doing so.

## When a Library Helps

| Situation | Library value |
| --- | --- |
| The team has run a pilot and knows which procedures it repeats | High — the library supplies shape for practices already identified as valuable |
| The team wants to see how others structure a procedure | Moderate — useful as reference even if nothing is installed |
| The team has not yet established what work benefits from assistance | Low — the catalogue will substitute for the decision rather than inform it |
| The organization lacks owned context for the relevant systems | Low — procedures will run against the same untrusted knowledge as before |

The [medium-term guide](medium-term-context-engineering.md) places skills as context
products, which is the useful frame: a library is *someone else's* context product. It
carries their conventions, their assumptions about tooling, and their idea of what a good
procedure looks like. That is a reasonable starting point and a poor finishing one.

## Evaluate Before Installing

Apply the same questions the medium-term guide applies to any context source:

| Property | Question to ask of the library |
| --- | --- |
| Relevant | Do these procedures match work the team actually does, or an idealized version of it? |
| Authoritative | Who wrote them, and against what experience? Are they maintained? |
| Current | When did the library last change? Do its procedures assume tooling the team does not use? |
| Accessible | Can the team read, modify, and re-review the content, or is it opaque? |
| Usable | Are procedures scoped small enough to verify, or are they long enough that nobody reads them? |

Two additional checks apply specifically to installed skills:

- **Context cost.** Every user-level skill's description is loaded in every session, in
  every project. A large library installed globally is a standing tax on every task,
  including tasks it has nothing to do with. Install the subset the team uses.
- **Name collisions.** Skills are addressed by name. A library skill named `code-review`
  will collide with a built-in of the same name. Prefixing by role resolves this and makes
  provenance visible at the prompt.

## Scoping Decisions

| Scope | Path | Use when |
| --- | --- | --- |
| Personal, all projects | `~/.claude/skills/` | An individual's own working procedures |
| Project, everyone | `<repo>/.claude/skills/` | Procedures specific to one codebase, reviewed with it |

Project scope is the better default for team adoption. It is version-controlled, it is
reviewed like code, it arrives with the repository, and it disappears when the work does.
User scope suits an individual's cross-project habits and cannot be reviewed by anyone else.

## Worked Case: se-agent-team

[`se-agent-team`](https://github.com/lahirugmg/se-agent-team) is a tool-agnostic library of
eight SDLC roles, each with atomic and composite skills. It is a reasonable subject because
it is structured, maintained, and not written for any particular tool — which means
adopting it requires a conversion step, and the conversion is where the decisions live.

[`tools/install-skills.py`](../tools/install-skills.py) performs that conversion. What it
does, and why each step matters:

| Step | Reason |
| --- | --- |
| Selects a role subset | The full library is 70 skills. Installing all of them globally taxes every session. The default is the engineering roles |
| Prefixes names by role | Avoids collisions with built-ins and makes provenance visible — `swe-code-review` is evidently from the library |
| Generates descriptions from each skill's stated trigger and invocation conditions | Selection depends on the description. A description that says only what a skill does, not when it applies, will not be chosen correctly |
| Quotes the description in frontmatter | Descriptions contain colons. An unquoted YAML scalar containing `: ` does not parse |
| Rewrites cross-references to installed names | Composite skills chain sub-skills by name. Unrewritten, those references point at names that do not exist |
| Extracts shared behavioral rules once | The library's role rules are shared by all of a role's skills. Copying them into each skill directory creates many copies to keep current |
| Resolves dangling citations | Some skills cite knowledge files the library moved. An unresolved citation is a silent failure at run time |

Run it with `--help` for options. The conversion is idempotent and re-runnable when the
upstream library changes.

## After Installing

An installed library is a starting point that has not yet been evaluated. Treat it as a
context product with an owner:

1. **Assign an owner.** Someone decides when to re-sync, which skills to keep, and which to
   modify. Unowned skills rot exactly as unowned wiki pages do.
2. **Modify freely.** The library's conventions are not the team's. A procedure that
   references practices the team does not follow should be edited, not tolerated.
3. **Prune.** Skills that go unused for a quarter are context cost with no return. Remove
   them; they remain in the upstream repository.
4. **Evaluate the ones that matter.** For any skill whose output feeds a consequential
   decision, the [evaluation record template](../templates/evaluation-record.md) applies.
   Procedures are not exempt from evidence because they came from a library.
5. **Do not let the catalogue set the agenda.** The presence of a `threat-modeling` skill is
   not a reason to do threat modeling. The [opportunity map](../templates/sdlc-opportunity-map.md)
   decides what work to improve; the library supplies shape once that decision is made.

## A Note on Role Orchestrators

Libraries organized by role often include an orchestrator per role that holds behavioral
rules and dispatches procedures. That structure is worth understanding before copying it.

Dispatch is frequently already handled — skills are selected from their descriptions
without an orchestrator's involvement. What an orchestrator adds is a separate context and
enforced phase gates. The separate context genuinely matters for procedures where
independence is the mechanism, such as reviewing work the same session produced. Phase gates
matter when they are enforced by something other than prose.

Adopt the orchestrator pattern where one of those two properties is actually needed. Adopting
it wholesale reproduces an organizational chart in configuration, which is satisfying to
build and rarely changes what the work produces.

[Reference implementation](claude-code-reference-implementation.md) | [Medium-term playbook](medium-term-context-engineering.md) | [Back to the repository overview](../README.md)
