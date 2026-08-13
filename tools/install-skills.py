#!/usr/bin/env python3
"""Convert an external skill library into Claude Code skills.

Worked tooling for docs/skill-library-integration.md. Written against the layout of
se-agent-team (https://github.com/lahirugmg/se-agent-team):

    <source>/skills/<role>/<skill>.md     one markdown file per skill
    <source>/agents/COMMON.md             behavioral rules shared by every role
    <source>/agents/<role>/agent.md       role-specific behavioral rules

and producing:

    <target>/skills/<prefix>-<skill>/SKILL.md
    <target>/se-agent-rules/{COMMON.md,<role>.md}

Idempotent: re-running regenerates the installed skills in place. Existing skills that
were not produced by this script are left alone.

Examples
--------
    # engineering subset into the user scope, the default
    ./install-skills.py --source ~/src/se-agent-team

    # everything, into a repository so the team shares it
    ./install-skills.py --source ~/src/se-agent-team --target .claude --roles all

    # see what would happen
    ./install-skills.py --source ~/src/se-agent-team --dry-run
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

# Role directory -> (name prefix, human label). Prefixes keep installed skills clear of
# built-in names and make provenance visible at the prompt.
ROLE_PREFIXES = {
    "business-analyst": ("ba", "Business Analyst"),
    "technical-architect": ("ta", "Technical Architect"),
    "software-engineer": ("swe", "Software Engineer"),
    "qa-engineer": ("qa", "QA Engineer"),
    "security-engineer": ("sec", "Security Engineer"),
    "platform-engineer": ("plat", "Platform Engineer"),
    "sre": ("sre", "SRE"),
    "technical-writer": ("tw", "Technical Writer"),
}

# The default subset. Every installed skill's description is loaded in every session, so
# installing the full library is a standing context cost on unrelated work.
ENGINEERING_ROLES = [
    "software-engineer",
    "qa-engineer",
    "security-engineer",
    "technical-architect",
]

DESCRIPTION_LIMIT = 1000  # frontmatter allows 1024; leave headroom


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Convert an external skill library into Claude Code skills.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples")[-1],
    )
    p.add_argument(
        "--source", required=True, type=Path,
        help="Checkout of the skill library.",
    )
    p.add_argument(
        "--target", type=Path, default=Path.home() / ".claude",
        help="Where to install. Default ~/.claude (user scope). Pass a repository's "
             ".claude directory to scope the skills to that project.",
    )
    p.add_argument(
        "--roles", default="engineering",
        help="'engineering' (default), 'all', or a comma-separated list of role "
             f"directories. Known roles: {', '.join(sorted(ROLE_PREFIXES))}.",
    )
    p.add_argument(
        "--knowledge-source", type=Path, default=None,
        help="Optional directory holding knowledge files that skills cite. Needed when "
             "the library references core/knowledge/ but no longer ships it.",
    )
    p.add_argument("--dry-run", action="store_true", help="Report actions, write nothing.")
    return p.parse_args(argv)


def resolve_roles(spec: str) -> list[str]:
    if spec == "engineering":
        return list(ENGINEERING_ROLES)
    if spec == "all":
        return list(ROLE_PREFIXES)
    roles = [r.strip() for r in spec.split(",") if r.strip()]
    unknown = [r for r in roles if r not in ROLE_PREFIXES]
    if unknown:
        sys.exit(f"error: unknown role(s): {', '.join(unknown)}")
    return roles


def field(body: str, key: str) -> str:
    m = re.search(rf"^\*\*{key}:\*\*\s*(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def when_to_invoke(body: str) -> list[str]:
    m = re.search(r"^## When to Invoke\s*\n(.*?)(?=\n## )", body, re.M | re.S)
    if not m:
        return []
    return [
        re.sub(r"\s+", " ", ln.lstrip("-* ").strip()).rstrip(".")
        for ln in m.group(1).splitlines()
        if ln.strip().startswith(("-", "*"))
    ]


def build_description(body: str, role_label: str) -> str:
    """Selection depends on this text, so it must say when the skill applies."""
    parts = [f"{field(body, 'Trigger').rstrip('.')}."]
    bullets = when_to_invoke(body)
    if bullets:
        parts.append("Use when: " + "; ".join(b[0].lower() + b[1:] for b in bullets) + ".")
    if field(body, "Type") == "composite" and field(body, "Sub-skills"):
        parts.append(f"Composite workflow: {field(body, 'Sub-skills')}.")
    parts.append(f"{role_label} skill from the installed library.")

    desc = re.sub(r"\s+", " ", " ".join(parts)).strip()
    if len(desc) > DESCRIPTION_LIMIT:
        desc = desc[: DESCRIPTION_LIMIT - 3].rsplit(" ", 1)[0] + "..."
    # Emitted double-quoted: descriptions contain ": ", illegal in a plain YAML scalar.
    return desc.replace("\\", "\\\\").replace('"', "'")


def rewrite_refs(body: str, role: str, name_map: dict, rules_dir: Path) -> str:
    """Point sibling-skill references and knowledge citations at what was installed."""
    body = re.sub(r"@?core/knowledge/([a-z-]+\.md)", rf"`{rules_dir}/\1`", body)
    for (r, base), new in name_map.items():
        if r != role:
            continue
        body = re.sub(rf"@{re.escape(base)}\b", new, body)
        body = re.sub(rf"\b{re.escape(base)} skill\b", f"{new} skill", body)
        body = re.sub(
            rf"(^\*\*(?:Sub-skills|Phases):\*\*.*?)\b{re.escape(base)}\b",
            rf"\g<1>{new}", body, flags=re.M,
        )
    return body


def insert_after_metadata(body: str, note: str) -> str:
    """Place the note below the title and its **Type:**/**Trigger:** lines."""
    lines = body.splitlines(keepends=True)
    at = 1
    for i, ln in enumerate(lines[1:], start=1):
        if ln.startswith("**"):
            at = i + 1
        elif ln.strip():
            break
    return "".join(lines[:at]).rstrip("\n") + "\n\n" + note + "".join(lines[at:]).lstrip("\n")


def main(argv=None) -> int:
    args = parse_args(argv)
    source, target = args.source.expanduser(), args.target.expanduser()
    roles = resolve_roles(args.roles)

    if not (source / "skills").is_dir():
        sys.exit(f"error: {source}/skills not found — is --source a library checkout?")
    missing = [r for r in roles if not (source / "skills" / r).is_dir()]
    if missing:
        sys.exit(f"error: role directories absent from {source}/skills: {', '.join(missing)}")

    skills_dir, rules_dir = target / "skills", target / "se-agent-rules"

    name_map = {
        (role, f.stem): f"{ROLE_PREFIXES[role][0]}-{f.stem}"
        for role in roles
        for f in sorted((source / "skills" / role).glob("*.md"))
    }
    if not name_map:
        sys.exit("error: no skill files found for the selected roles")

    def write(path: Path, text: str) -> None:
        if args.dry_run:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    # --- shared behavioral rules, extracted once rather than per skill ---------------
    common = source / "agents" / "COMMON.md"
    if common.is_file():
        write(
            rules_dir / "COMMON.md",
            common.read_text().replace("`agents/<role>/agent.md`", f"`{rules_dir}/<role>.md`"),
        )

    if args.knowledge_source:
        ks = args.knowledge_source.expanduser()
        for kf in sorted(ks.glob("*.md")):
            if not args.dry_run:
                rules_dir.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(kf, rules_dir / kf.name)

    for role in roles:
        agent_md = source / "agents" / role / "agent.md"
        if not agent_md.is_file():
            continue
        prefix = ROLE_PREFIXES[role][0]
        txt = re.sub(
            r"^Invoked on demand\..*$",
            f"Invoked on demand. Installed as skills prefixed `{prefix}-`.",
            agent_md.read_text(), flags=re.M,
        )
        txt = txt.replace("[agents/COMMON.md](../COMMON.md)", "[COMMON.md](./COMMON.md)")
        write(rules_dir / f"{role}.md", rewrite_refs(txt, role, name_map, rules_dir))

    # --- skills ---------------------------------------------------------------------
    installed = []
    for role in roles:
        label = ROLE_PREFIXES[role][1]
        has_rules = (source / "agents" / role / "agent.md").is_file()
        for src in sorted((source / "skills" / role).glob("*.md")):
            name = name_map[(role, src.stem)]
            raw = src.read_text()
            desc = build_description(raw, label)

            body = rewrite_refs(raw, role, name_map, rules_dir)
            body = re.sub(
                r"^# Skill: .*$", f"# {src.stem.replace('-', ' ').title()}",
                body, count=1, flags=re.M,
            )
            if has_rules:
                body = insert_after_metadata(
                    body,
                    f"> **Standing rules.** Before executing, load `{rules_dir}/COMMON.md` "
                    f"and `{rules_dir}/{role}.md` — they define the three-phase workflow "
                    f"and gates this skill assumes.\n\n",
                )

            write(
                skills_dir / name / "SKILL.md",
                f'---\nname: {name}\ndescription: "{desc}"\n---\n\n{body.lstrip()}',
            )
            installed.append((name, len(desc)))

    verb = "Would install" if args.dry_run else "Installed"
    print(f"{verb} {len(installed)} skills from {len(roles)} role(s) into {skills_dir}")
    print(f"{'Would write' if args.dry_run else 'Wrote'} shared rules to {rules_dir}")
    for name, dlen in installed:
        print(f"  {name:<40} description {dlen}c")
    if args.dry_run:
        print("\nDry run — nothing written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
