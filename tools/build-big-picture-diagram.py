#!/usr/bin/env python3
"""Generate the AI-native SDLC big-picture diagram as an Excalidraw scene.

Output: docs/diagrams/ai-native-sdlc-big-picture.excalidraw

The diagram is generated rather than hand-drawn so that its wording stays reviewable
in a diff and stays consistent with the horizon guides it summarizes:

    docs/journey-to-ai-native-sdlc.md      the three horizons and their gates
    docs/short-term-simple-ai-integration.md  prompt engineering as task framing
    docs/medium-term-context-engineering.md   context products
    docs/long-term-harness-engineering.md     harness components
    docs/governance-and-risk.md               the governance frame

Re-run after editing the content blocks below:

    python3 tools/build-big-picture-diagram.py

The file opens in any Excalidraw editor. Hand edits made in the editor are lost on the
next run, so change the wording here, not there.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

RNG = random.Random(20260827)
LINE_HEIGHT = 1.25
CHAR_W = 0.6  # width-per-character factor for the hand-drawn font, deliberately generous

INK = "#1e1e1e"
MUTED = "#5c5f66"
FAINT = "#868e96"
BLUE, BLUE_BG = "#1971c2", "#e7f5ff"
GREEN, GREEN_BG = "#2f9e44", "#ebfbee"
AMBER, AMBER_BG = "#f08c00", "#fff9db"
ROSE, ROSE_BG = "#c2255c", "#fff0f6"
RED, RED_BG = "#e03131", "#fff5f5"

elements: list[dict] = []


def nonce() -> int:
    return RNG.randint(1, 2**31 - 1)


def eid(tag: str) -> str:
    return f"{tag}-{RNG.randrange(16**8):08x}"


def base(kind: str, x, y, w, h, **kw) -> dict:
    el = {
        "id": kw.pop("id", eid(kind)),
        "type": kind,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": kw.pop("stroke", INK),
        "backgroundColor": kw.pop("bg", "transparent"),
        "fillStyle": kw.pop("fill", "solid"),
        "strokeWidth": kw.pop("strokeWidth", 2),
        "strokeStyle": kw.pop("strokeStyle", "solid"),
        "roughness": 1,
        "opacity": 100,
        "groupIds": kw.pop("groups", []),
        "frameId": None,
        "roundness": kw.pop("roundness", {"type": 3}),
        "seed": nonce(),
        "version": 1,
        "versionNonce": nonce(),
        "isDeleted": False,
        "boundElements": kw.pop("boundElements", []),
        "updated": 1,
        "link": None,
        "locked": False,
    }
    el.update(kw)
    elements.append(el)
    return el


def measure(text: str, size: float) -> tuple[float, float]:
    lines = text.split("\n")
    width = max(len(ln) for ln in lines) * size * CHAR_W
    return width, len(lines) * size * LINE_HEIGHT


def label(text, x, y, size=13, color=INK, align="left", width=None, groups=None,
          container=None, valign="top") -> dict:
    w, h = measure(text, size)
    if width is not None:
        w = width
    el = base(
        "text", x, y, w, h,
        stroke=color, roundness=None, strokeWidth=1, groups=groups or [],
        boundElements=None,
        text=text, originalText=text, fontSize=size, fontFamily=1,
        textAlign=align, verticalAlign=valign, containerId=container,
        lineHeight=LINE_HEIGHT, baseline=round(h - size * 0.25),
    )
    return el


def card(x, y, w, h, stroke, bg, title, subtitle, body, title_size=19, body_size=13):
    """A titled box: rectangle, heading, optional subtitle, left-aligned body."""
    gid = eid("g")
    box = base("rectangle", x, y, w, h, stroke=stroke, bg=bg, groups=[gid])
    pad = 18
    cursor = y + 14
    label(title, x + pad, cursor, size=title_size, color=stroke, groups=[gid])
    cursor += title_size * LINE_HEIGHT + 4
    if subtitle:
        label(subtitle, x + pad, cursor, size=12, color=MUTED, groups=[gid])
        cursor += 12 * LINE_HEIGHT + 8
    label(body, x + pad, cursor, size=body_size, color=INK, groups=[gid])
    return box


def bind(el: dict, arrow_id: str) -> None:
    el.setdefault("boundElements", []).append({"id": arrow_id, "type": "arrow"})


def arrow(x, y, points, stroke=INK, start=None, end=None, dashed=False,
          end_head="arrow", start_head=None, width=2):
    aid = eid("arrow")
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    el = base(
        "arrow", x, y, max(xs) - min(xs), max(ys) - min(ys),
        id=aid, stroke=stroke, strokeWidth=width,
        strokeStyle="dashed" if dashed else "solid",
        roundness={"type": 2}, fill="solid",
        points=[list(p) for p in points], lastCommittedPoint=None,
        startArrowhead=start_head, endArrowhead=end_head,
        startBinding={"elementId": start["id"], "focus": 0, "gap": 8} if start else None,
        endBinding={"elementId": end["id"], "focus": 0, "gap": 8} if end else None,
    )
    if start:
        bind(start, aid)
    if end:
        bind(end, aid)
    return el


# --------------------------------------------------------------------------------------
# Frame: governance and security enclose everything else.
# --------------------------------------------------------------------------------------
base("rectangle", 40, 140, 1820, 1070, stroke=RED, bg=RED_BG, strokeStyle="dashed")

label("AI-Native SDLC — The Big Picture", 60, 46, size=34, color=INK)
label(
    "Three horizons of capability, one repeating loop of work, and a governance frame "
    "that encloses both.",
    62, 100, size=15, color=MUTED,
)
label("GOVERNANCE & SECURITY — inherent design, not an afterthought",
      1300, 158, size=14, color=RED, align="right", width=520)

# --------------------------------------------------------------------------------------
# Band 1: the capability journey.
# --------------------------------------------------------------------------------------
label("1  ·  Capability journey — horizons are entered on evidence, never on a "
      "calendar, a headcount, or a tool rollout",
      80, 186, size=17, color=BLUE)

JY, JH, JW = 215, 220, 460
horizons = [
    (80, "Prompt engineering", "Short term · simple AI integration",
     "Unit of change: individual and team habits.\n"
     "• Task framing: outcome, context, boundaries,\n"
     "   quality bar, verification\n"
     "• Bounded pilot — hypothesis, owner, stop\n"
     "   conditions, measured baseline\n"
     "• Every output reviewed; the person who ships\n"
     "   it stays accountable\n"
     "Fails as: fluent output taken for correct output."),
    (720, "Context engineering", "Medium term · shared, owned knowledge",
     "Unit of change: shared context products.\n"
     "• Context map: trusted source, owner, freshness,\n"
     "   access boundary\n"
     "• Repository instructions, task briefs, curated\n"
     "   architecture material — versioned, not pasted\n"
     "• Context is a product with a lifecycle, not a\n"
     "   folder of documents\n"
     "Fails as: stale context, confidently applied."),
    (1360, "Harness engineering", "Long term · operable workflows",
     "Unit of change: the end-to-end workflow.\n"
     "• Narrow task contract, scoped capabilities,\n"
     "   deterministic shell around the model\n"
     "• Validation, evaluation, observability, and a\n"
     "   rollback path are components, not extras\n"
     "• Shadow mode → scoped autonomy, with named\n"
     "   approvers at every step\n"
     "Fails as: autonomy widened past detection."),
]
boxes = [card(x, JY, JW, JH, BLUE, BLUE_BG, t, s, b) for x, t, s, b in horizons]

gates = [
    (630, "into the medium term",
     "the next constraint is\ncontext, not skill or\ntool access"),
    (1270, "into the long term",
     "context is owned,\ncurrent, and shown to\nimprove the work"),
]
for i, (cx, gate_title, criteria) in enumerate(gates):
    d = base("diamond", cx - 46, 279, 92, 92, stroke=AMBER, bg=AMBER_BG)
    gw, gh = measure("GATE", 14)
    label("GATE", cx - gw / 2, 325 - gh / 2, size=14, color="#e67700",
          align="center", container=d["id"], valign="middle")
    d["boundElements"] = [{"type": "text", "id": elements[-1]["id"]}]
    arrow(boxes[i]["x"] + JW, 325, [[0, 0], [42, 0]], stroke=AMBER,
          start=boxes[i], end=d)
    arrow(cx + 46, 325, [[0, 0], [42, 0]], stroke=AMBER, start=d, end=boxes[i + 1])
    label(gate_title, cx - 84, 252, size=11, color="#e67700", align="center", width=168)
    label(criteria, cx - 84, 382, size=11, color=MUTED, align="center", width=168)

# Manifold: the loop below runs inside every horizon above.
for cx in (310, 950, 1590):
    arrow(cx, JY + JH, [[0, 0], [0, 53]], stroke=FAINT, dashed=True, end_head=None, width=1)
base("line", 310, 488, 1280, 0, stroke=FAINT, strokeStyle="dashed", strokeWidth=1,
     roundness={"type": 2}, points=[[0, 0], [1280, 0]], lastCommittedPoint=None,
     startArrowhead=None, endArrowhead=None, startBinding=None, endBinding=None)
arrow(950, 488, [[0, 0], [0, 40]], stroke=FAINT, dashed=True, width=1)
label("the same loop runs inside every horizon — what changes is who supplies the "
      "context\nand how much of the loop is automated, never whether validation happens",
      978, 492, size=13, color=MUTED)

# --------------------------------------------------------------------------------------
# Band 2: loop engineering.
# --------------------------------------------------------------------------------------
label("2  ·  Loop engineering — the unit of work is the loop, not the prompt",
      80, 540, size=17, color=GREEN)

LY, LH, LW = 580, 220, 440
stages = [
    (170, "Pre-plan", "establish intent before anything is generated",
     "• Restate the goal and the acceptance test\n"
     "• Assemble the context the task actually needs\n"
     "• Name the blast radius and what must not change\n"
     "• Choose the smallest reversible slice\n"
     "• Make assumptions and uncertainty visible\n"
     "Leaves behind: a plan a reviewer could disagree\nwith.",
     "governance here: data classification, boundary,\napproved tool and account"),
    (730, "Execution", "do the smallest slice, traceably",
     "• Work only inside the agreed scope and access\n"
     "• One reversible change beats one large change\n"
     "• Keep the diff and the reasoning inspectable\n"
     "• Stop and re-plan when the ground moves\n"
     "• Speed never removes a step from the loop\n"
     "Leaves behind: a change that can be read in one\nsitting.",
     "governance here: least privilege, sandbox,\nscoped identity, reversible actions"),
    (1290, "Validation", "prove it, then decide",
     "• Run the acceptance test, not a vibe check\n"
     "• Review intent and risk, not only syntax\n"
     "• Record what failed and why — that is evidence\n"
     "• Feed the correction back into the context\n"
     "• Decide: accept, revise, or abandon\n"
     "Leaves behind: evidence, and context better than\nit was last pass.",
     "governance here: provenance, audit record,\nnamed human sign-off"),
]
stage_boxes = []
for x, title, sub, body, control in stages:
    b = card(x, LY, LW, LH, GREEN, GREEN_BG, title, sub, body)
    stage_boxes.append(b)
    label(control, x, LY + LH + 12, size=11, color=ROSE, align="center", width=LW)

for i in range(2):
    arrow(stage_boxes[i]["x"] + LW, LY + LH / 2, [[0, 0], [120, 0]], stroke=GREEN,
          start=stage_boxes[i], end=stage_boxes[i + 1])

arrow(1510, 850, [[0, 0], [0, 30], [-1120, 30], [-1120, 0]], stroke=GREEN)
label("repeat — each pass narrows the scope, tightens the context, and shrinks the diff",
      640, 892, size=13, color=GREEN)

# --------------------------------------------------------------------------------------
# Band 3: governance and security as design input.
# --------------------------------------------------------------------------------------
label("3  ·  Governance and security — a design input at every horizon and every "
      "pass of the loop, proportionate to impact",
      80, 940, size=17, color=ROSE)

controls = [
    ("Data boundaries",
     "What may cross the boundary is\nclassified before the first\nprompt, not after an\n"
     "incident. Retention and\nresidency are enforced by\ncontract and configuration —\n"
     "never by asking the model."),
    ("Least-privilege access",
     "Tools, repositories, and\nsecrets are scoped to the\ntask. Nothing inherits a\n"
     "person's standing access.\nIdentity, authorization, and\nlimits live outside the\n"
     "model, in the deterministic\nshell."),
    ("Provenance and audit",
     "Every AI-assisted change is\nattributable: what was asked,\nwhich context was used,\n"
     "what changed, who approved\nit. A change that cannot be\nexplained afterwards\n"
     "cannot be scaled."),
    ("Human accountability",
     "Approval and sign-off stay\nwith a named person at every\nhorizon. Autonomy may\n"
     "expand; ownership of the\noutcome does not move to the\nmodel. Refusal and\n"
     "escalation are designed\npaths."),
    ("Evaluation before scale",
     "Representative cases, shadow\nmode, and known failure modes\nprecede any widening of\n"
     "scope. Expansion is justified\nby measured value and support\ncapacity, not by\n"
     "novelty."),
    ("Reversibility",
     "Sandboxed execution, small\ndiffs, separated propose /\napprove / execute, and a\n"
     "rehearsed rollback for every\nautomated path. Assume the\nloop will be wrong\n"
     "some of the time."),
]
for i, (title, body) in enumerate(controls):
    card(80 + i * 294, 975, 270, 168, ROSE, ROSE_BG, title, None, body,
         title_size=15, body_size=11)

label(
    "Governance is a design input. A control added after a workflow is automated is a "
    "control that was already bypassed.\n"
    "The same four questions — what data, whose access, whose signature, what "
    "evidence — are asked at the first prompt and at the hundredth automated run.",
    80, 1158, size=14, color=RED,
)

# --------------------------------------------------------------------------------------
scene = {
    "type": "excalidraw",
    "version": 2,
    "source": "tools/build-big-picture-diagram.py",
    "elements": elements,
    "appState": {"gridSize": None, "viewBackgroundColor": "#ffffff"},
    "files": {},
}

out = Path(__file__).resolve().parent.parent / "docs" / "diagrams" / "ai-native-sdlc-big-picture.excalidraw"
out.write_text(json.dumps(scene, indent=2) + "\n", encoding="utf-8")
print(f"wrote {out} ({len(elements)} elements)")
