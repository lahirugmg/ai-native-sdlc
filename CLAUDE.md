# CLAUDE.md

Instructions for Claude Code when working in this repository.

This file is also a worked example of the first context product named in
[Medium term: Context engineering](docs/medium-term-context-engineering.md) — repository
instructions. It is kept short, versioned with the content it describes, and it links to
sources of truth rather than restating them.

## What This Repository Is

An organization-led guide for adopting AI assistance across the software development
lifecycle. It is about changing how work moves through the SDLC, not about selecting a
product.

The material is organized as three evidence-gated horizons: short term (simple AI
integration), medium term (context engineering), and long term (harness engineering).
[docs/journey-to-ai-native-sdlc.md](docs/journey-to-ai-native-sdlc.md) is the spine —
read it before making structural changes.

## What This Repository Is Not

It is **not** an agent, prompt, or skill library. The README states that it "deliberately
complements agent and prompt libraries by focusing on the organizational conditions
required for responsible use." That is the differentiator.

Do not add role definitions, a skill catalogue, or agent personas to `docs/`. When
external libraries are relevant, point to them and explain adoption —
see [docs/skill-library-integration.md](docs/skill-library-integration.md) for how that is
done.

## Structure

| Path | Contains | Audience |
| --- | --- | --- |
| `docs/` | Tool-agnostic journey guidance, one file per horizon plus governance | Engineering and IT leaders |
| `templates/` | Blank, reusable artifacts teams fill in | Practitioners |
| `examples/` | One fictional organization's filled-in artifacts across all three horizons | Practitioners |
| `assessments/` | Diagnostics for choosing and preparing a pilot | Adoption leads |
| `.claude/skills/` | Project-scoped skills that operate this playbook | Anyone using the repo with Claude Code |
| `.claude/agents/` | Project-scoped subagents, currently one gate reviewer | Anyone using the repo with Claude Code |
| `tools/` | Supporting scripts | Maintainers |

## Writing Conventions

These are observable in every existing file. Match them.

- **Tool-agnostic in `docs/`.** Name no vendor, product, or model in the horizon guides or
  governance. Concrete tooling belongs in
  [docs/claude-code-reference-implementation.md](docs/claude-code-reference-implementation.md),
  `examples/`, and `.claude/`, which are explicitly scoped as one instantiation.
- **Tables over prose lists** for anything comparative, and every table gets a header row
  whose delimiter row has a matching column count.
- **Measured register.** Declarative sentences, no marketing language, no exclamation
  marks, no second-person exhortation. State the practice and its failure mode.
- **Every document ends with a navigation line** of relative links, formatted as
  `[Label](target.md) | [Label](target.md)` — see the last line of any horizon guide.
- **Templates are blank; examples are filled.** Never add sample data to a file in
  `templates/`. Add it to `examples/` instead and link the two.
- **Mermaid for flow diagrams**, used sparingly and only where sequence or feedback is the
  point.
- **Relative links between documents**, so the repository reads correctly on any host.
- **"AI-native" names the destination; "AI-assisted" names the work.** `AI-native` modifies
  `SDLC` and nothing else — it is the lifecycle this journey leads to. Work at every
  horizon, including a long-term harness, is `AI-assisted`. The distinction is defined in
  [the journey guide](docs/journey-to-ai-native-sdlc.md#an-ai-native-sdlc-is-the-destination-not-the-starting-position)
  and carries invariant 4: calling a practice AI-native asserts an advancement no evidence
  has established.

## Invariants

1. Each horizon guide keeps its section contract: an outcome statement, the horizon's
   substance, evaluation guidance, and exit or scale criteria.
2. Every template referenced from a horizon guide exists in `templates/`, and every
   template links back to the guide that governs it.
3. Every template has a corresponding filled artifact under `examples/`.
4. Advancement language stays evidence-gated. Never describe a horizon as reached by
   elapsed time, headcount, or tool rollout.
5. Human accountability is never delegated to an AI system in any recommendation.

## Common Tasks

**Add or change a horizon guide.** Read the adjacent horizons first — the exit criteria of
one are the entry gates of the next, and they must stay consistent.

**Add a template.** Create the blank in `templates/`, add a filled instance under the
matching `examples/` horizon directory, link it from the governing horizon guide, and add
a row to the README's template list.

**Change the journey model.** `docs/journey-to-ai-native-sdlc.md` holds the gate
definitions. Changing a gate means checking every horizon guide's exit criteria and
`.claude/agents/evidence-gate-reviewer.md`, which encodes those gates.

**Work with the examples.** They describe one fictional organization, Harbour Mutual, and
chain together — the opportunity map selects the pilot, the pilot exposes the context gap,
the context work qualifies the harness. Keep the scenario facts consistent across files;
`examples/README.md` is the reference for names, dates, and systems.

## Verification

There is no build or test suite. Before proposing a change:

- [ ] Relative links resolve.
- [ ] Table delimiter rows match their header column counts.
- [ ] No vendor or product name entered `docs/` outside the reference implementation.
- [ ] Templates remained blank; new sample content went to `examples/`.
- [ ] Cross-horizon claims still agree with the gates in the journey guide.

## Related

[README](README.md) | [Journey guide](docs/journey-to-ai-native-sdlc.md) | [Reference implementation](docs/claude-code-reference-implementation.md)
