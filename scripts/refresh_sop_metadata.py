"""One-shot / maintenance helper: add missing SOP metadata and bump last_validated."""
from __future__ import annotations

import re
from pathlib import Path

TODAY = "2026-07-21"
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

MISSING = {
    "docs/01-System-Setup/alipay-wechat-setup-foreigners.md": {
        "version": "1.2",
        "ttl_days": 60,
        "stability_status": "critical",
        "validation_method": "desktop_review",
    },
    "docs/03-Emergency-DR/lost-passport.md": {
        "version": "1.1",
        "ttl_days": 90,
        "stability_status": "critical",
        "validation_method": "desktop_review",
    },
    "docs/03-Emergency-DR/network-outage.md": {
        "version": "1.1",
        "ttl_days": 90,
        "stability_status": "critical",
        "validation_method": "desktop_review",
    },
    "docs/04-Parenting-Patch/milk-recall-check.md": {
        "version": "1.1",
        "ttl_days": 60,
        "stability_status": "critical",
        "validation_method": "desktop_review",
    },
}


def meta_block(cfg: dict) -> str:
    return (
        "metadata:\n"
        f"  version: {cfg['version']}\n"
        f"  last_validated: {TODAY}\n"
        f"  ttl_days: {cfg['ttl_days']}\n"
        f'  stability_status: "{cfg["stability_status"]}"\n'
        f'  validation_method: "{cfg["validation_method"]}"\n'
    )


def bump_footer(body: str) -> str:
    body = re.sub(
        r"\*\*Last Updated:\*\*\s*[^\n|]+",
        f"**Last Updated:** Jul 21, 2026",
        body,
        count=1,
    )
    body = re.sub(
        r"\*\*Last Updated:\*\*\s*Apr 27, 2026\s*\|\s*\*\*Author:\*\*",
        "**Last Updated:** Jul 21, 2026 | **Author:**",
        body,
        count=1,
    )
    return body


def main() -> None:
    writes = 0

    for rel, cfg in MISSING.items():
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            print(f"skip (no frontmatter): {p}")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            print(f"skip (bad frontmatter): {p}")
            continue
        fm, body = parts[1], parts[2]
        if "metadata:" in fm:
            print(f"already has metadata: {p}")
            continue
        new_fm = fm.rstrip() + "\n" + meta_block(cfg)
        body = bump_footer(body)
        p.write_text("---" + new_fm + "---" + body, encoding="utf-8")
        writes += 1
        print(f"added metadata: {rel}")

    for p in DOCS.rglob("*.md"):
        if p.name == "index.md":
            continue
        text = p.read_text(encoding="utf-8")
        if "last_validated:" not in text:
            continue
        new = re.sub(
            r"last_validated:\s*\d{4}-\d{2}-\d{2}",
            f"last_validated: {TODAY}",
            text,
            count=1,
        )
        if new == text:
            continue
        new = bump_footer(new)
        p.write_text(new, encoding="utf-8")
        writes += 1
        print(f"bumped last_validated: {p.relative_to(ROOT)}")

    print(f"done, writes={writes}")


if __name__ == "__main__":
    main()
