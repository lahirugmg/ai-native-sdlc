# AI-Assisted SDLC

A practical playbook for helping a software organization, or a Corporate IT function that builds software, adopt AI assistance across its software development lifecycle.

This repository is about changing how teams work, not merely selecting an AI product. It uses three phases so an organization can earn the right to automate more by first building fluency, then trustworthy context, then well-governed harnesses.

## Start Here

1. Read the [adoption model](docs/adoption-model.md) and name an accountable sponsor and adoption lead.
2. Establish a baseline for one or two volunteer teams: delivery flow, quality, developer experience, risk posture, and current AI use.
3. Charter a small Phase 1 pilot around real work with clear measures of success.
4. Advance a team only when it has evidence that the current phase is repeatable, safe, and useful.

## The Three Phases

| Phase | Focus | Organizational outcome |
| --- | --- | --- |
| 1. Simple AI integration | Reduce friction through safe tools, prompt engineering, and guided practice. | People know when and how to use AI while retaining ownership of their work. |
| 2. Context engineering | Make the right, governed organizational knowledge available to AI-assisted work. | Teams can reliably ground assistance in current code, architecture, standards, and delivery context. |
| 3. Harness engineering | Build repeatable workflows, evaluations, controls, and integrations around AI capabilities. | AI-assisted work becomes measurable, scalable, and operable rather than dependent on individual habits. |

## What Stays True in Every Phase

- Humans remain accountable for product, technical, security, and operational decisions.
- Evidence beats enthusiasm: measure delivery, quality, risk, and developer experience before claiming value.
- Start with real, bounded work and expand only after the team can repeat the result.
- Protect data, customer trust, intellectual property, and regulated obligations from the first pilot onward.
- Treat AI output as untrusted until an accountable person or automated control has verified it.

## Intended Audience

Engineering leaders, Corporate IT leaders, staff engineers, platform teams, security partners, delivery leaders, and enablement teams can use this material to make aligned decisions. It assumes organizations differ in tooling, regulation, architecture, and scale; adapt the practices to local constraints rather than adopting them as a rigid methodology.

## Repository Direction

The repository contains phase playbooks, governance guidance, readiness assessments, and reusable templates. It deliberately complements agent and prompt libraries by focusing on the organizational conditions required for their responsible use.

- [Adoption model](docs/adoption-model.md): the operating model, evidence gates, measures, and accountabilities.
- [Phase 1: Simple AI integration](docs/phase-1-simple-ai-integration.md): guided adoption, prompt engineering, and bounded pilots.
- [Phase 2: Context engineering](docs/phase-2-context-engineering.md): trusted, task-relevant knowledge for AI-assisted work.
- [Phase 3: Harness engineering](docs/phase-3-harness-engineering.md): repeatable AI-enabled workflows with controls and evaluations.
- [Governance and risk](docs/governance-and-risk.md): proportionate controls, decision rights, and incident handling.
- [Adoption readiness assessment](assessments/adoption-readiness.md): a practical diagnostic for choosing and preparing an initial pilot.

### Reusable Templates

- [AI task brief](templates/ai-task-brief.md): a prompt-engineering aid for bounded, verifiable work.
- [Pilot charter](templates/pilot-charter.md): hypothesis, boundaries, measures, and decision record for a Phase 1 pilot.
- [Context map](templates/context-map.md): ownership, freshness, access, and delivery design for Phase 2 knowledge.
- [Harness design review](templates/harness-design-review.md): task contract, controls, operations, and approvals for Phase 3.
- [Evaluation record](templates/evaluation-record.md): a repeatable evidence record for AI-assisted workflows and harnesses.

## Contributing

Contributions should add a decision, practice, template, or measurement approach that teams can apply. Keep recommendations tool-agnostic where possible, identify assumptions, and distinguish proven practices from hypotheses that need local validation.
