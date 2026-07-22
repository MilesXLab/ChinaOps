#!/usr/bin/env python3
"""
Normalize ChinaOps SOP markdown formatting:

1) Ensure required metadata fields
2) Add description from title when missing
3) Remove shields.io version badges
4) Collapse 3+ blank lines to 2
5) Strip orphan content after the *closing* Last Updated footer
   (footer is the last **Last Updated:** that appears after a Runbook/Tips block,
    or any Last Updated in the final 35% of the file when followed by more body)
6) Ensure a single back-to-library footer
7) Normalize trailing whitespace

Does not rewrite narrative structure of clean problem-first SOPs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SKIP = {
    "index.md",
    "symptom-index.md",
    "print-pack.md",
    "preflight-checklist.md",
}


def split_fm(text: str) -> tuple[dict, str, str]:
    if not text.startswith("---"):
        return {}, text, ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text, ""
    front = yaml.safe_load(parts[1]) or {}
    return front, parts[2], parts[1]


def dump_fm(front: dict) -> str:
    # Stable, readable frontmatter
    lines = ["---"]
    if "layout" in front:
        lines.append(f"layout: {front['layout']}")
    if "title" in front:
        title = str(front["title"]).replace('"', '\\"')
        lines.append(f'title: "{title}"')
    if front.get("description"):
        desc = str(front["description"]).replace('"', '\\"')
        lines.append(f'description: "{desc}"')
    md = front.get("metadata") or {}
    if isinstance(md, dict):
        lines.append("metadata:")
        order = [
            "version",
            "last_validated",
            "ttl_days",
            "churn",
            "stability_status",
            "validation_method",
            "scope",
        ]
        seen = set()
        for k in order:
            if k in md and md[k] is not None:
                seen.add(k)
                v = md[k]
                if isinstance(v, str):
                    lines.append(f'  {k}: "{v}"')
                else:
                    lines.append(f"  {k}: {v}")
        for k, v in md.items():
            if k in seen:
                continue
            if isinstance(v, str):
                lines.append(f'  {k}: "{v}"')
            else:
                lines.append(f"  {k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def ensure_metadata(front: dict) -> dict:
    if front.get("layout") is None:
        front["layout"] = "guide"
    md = front.get("metadata")
    if not isinstance(md, dict):
        md = {}
        front["metadata"] = md
    md.setdefault("version", 1.1)
    md.setdefault("last_validated", "2026-07-21")
    md.setdefault("ttl_days", 90)
    md.setdefault("stability_status", "stable")
    md.setdefault("validation_method", "desktop_review")
    md.setdefault("scope", "national")
    if md.get("churn") == "high":
        md["ttl_days"] = 30
    # stringify stability/validation/scope
    for k in ("stability_status", "validation_method", "scope"):
        if k in md and md[k] is not None:
            md[k] = str(md[k]).strip().strip('"')
    if not front.get("description") and front.get("title"):
        front["description"] = (
            f"Practical ChinaOps guide: {front['title']}. "
            "Step-by-step checks, fallbacks, and field tips."
        )
    return front


def strip_badges(body: str) -> str:
    body = re.sub(
        r"(?m)^!\[.*?\]\(https://img\.shields\.io[^)]+\)\s*\n?",
        "",
        body,
    )
    return body


def collapse_blank_lines(body: str) -> str:
    body = re.sub(r"\n{4,}", "\n\n\n", body)
    # after phrase-card often has double blank — leave max 2
    return body


def find_closing_footer_index(lines: list[str]) -> int | None:
    """
    Closing footer = Last Updated that comes AFTER an end-matter section
    (TechDad/Miles tips, strategic gap), not the early metadata-style Last Updated
    used in problem-first SOPs.
    """
    lu_idxs = [i for i, l in enumerate(lines) if "**Last Updated:**" in l]
    if not lu_idxs:
        return None
    end_markers = (
        "TechDad's Tips",
        "Miles' Tips",
        "Strategic Gap",
        "## FAQ",
        "## Contacts",
        "Contacts & resources",
        "Contacts & Resources",
    )
    for i in reversed(lu_idxs):
        window = "\n".join(lines[max(0, i - 80) : i])
        # Must look like document end-matter, not header block
        if any(k in window for k in end_markers):
            # Reject if ## Problem or major body starts within next 15 lines
            ahead = "\n".join(lines[i + 1 : i + 16])
            if re.search(r"(?m)^## (Problem|Root Cause|Part 1|Immediate)", ahead):
                continue
            return i
    return None


def trim_orphan_after_footer(body: str) -> tuple[str, bool]:
    lines = body.splitlines()
    idx = find_closing_footer_index(lines)
    if idx is None:
        return body if body.endswith("\n") else body + "\n", False

    rest = lines[idx + 1 :]
    # Detect orphan: non-empty content after footer that is not only a back link
    orphan_lines = [
        l
        for l in rest
        if l.strip()
        and "Back to Guide" not in l
        and "Back to Library" not in l
    ]
    if not orphan_lines:
        # ensure back link
        tail = "\n".join(lines[idx:])
        if "Back to Guide" not in tail and "Back to Library" not in tail:
            head = lines[: idx + 1]
            return "\n".join(head + ["", "[← Back to Guide Library](../)"]) + "\n", True
        return body if body.endswith("\n") else body + "\n", False

    # Only strip if orphan looks like leftovers (####, bare bullets, old Steps)
    first = orphan_lines[0].lstrip()
    looks_orphan = (
        first.startswith("####")
        or first.startswith("- ")
        or first.startswith("### Local")
        or first.startswith("### Step")
        or first.startswith("## Miles")
        or first.startswith("## Recommendations")
        or first.startswith("## Emergency")
        or first.startswith("## FAQ")
        or first.startswith("## Contacts")
        or first.startswith("### Option")
    )
    if not looks_orphan:
        return body if body.endswith("\n") else body + "\n", False

    kept = lines[: idx + 1]
    back = next(
        (l for l in rest if "Back to Guide" in l or "Back to Library" in l),
        "[← Back to Guide Library](../)",
    )
    return "\n".join(kept + ["", back]) + "\n", True


def strip_trailing_ws(body: str) -> str:
    lines = [ln.rstrip(" \t") for ln in body.splitlines()]
    return "\n".join(lines) + "\n"


def ensure_h1_blank_after_fm(body: str) -> str:
    # body should start with optional blank then H1 or content
    body = body.lstrip("\n")
    if not body.startswith("\n"):
        body = "\n" + body
    return body


def process(path: Path) -> list[str]:
    notes: list[str] = []
    text = path.read_text(encoding="utf-8")
    front, body, _raw = split_fm(text)
    if not front:
        notes.append("skip: no frontmatter")
        return notes

    before = text
    front = ensure_metadata(front)
    body2 = strip_badges(body)
    if body2 != body:
        notes.append("removed shields badge")
        body = body2
    body = collapse_blank_lines(body)
    body, trimmed = trim_orphan_after_footer(body)
    if trimmed:
        notes.append("trimmed orphan after footer / normalized footer")
    body = strip_trailing_ws(body)
    body = ensure_h1_blank_after_fm(body)

    # Ensure single trailing newline
    new_text = dump_fm(front) + body
    if not new_text.endswith("\n"):
        new_text += "\n"

    if new_text != before:
        path.write_text(new_text, encoding="utf-8", newline="\n")
        if not notes:
            notes.append("normalized frontmatter/whitespace")
    return notes


def main() -> int:
    changed = 0
    for p in sorted(DOCS.rglob("*.md")):
        if p.name in SKIP or "00-Maintenance" in p.parts:
            continue
        notes = process(p)
        if notes and notes != ["skip: no frontmatter"]:
            rel = p.relative_to(ROOT).as_posix()
            print(f"{rel}: {', '.join(notes)}")
            changed += 1
    print(f"\nUpdated {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
