#!/usr/bin/env python3
"""Strict SOP markdown format audit for ChinaOps guides."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SKIP_NAMES = {
    "index.md",
    "symptom-index.md",
    "print-pack.md",
    "preflight-checklist.md",
    "phrase-style-guide.md",
    "field-retest-checklist.md",
    "field-retest-log.md",
    "high-churn-registry.md",
    "design-tokens.md",
}

REQUIRED_META = (
    "version",
    "last_validated",
    "ttl_days",
    "stability_status",
    "validation_method",
    "scope",
)

Issue = tuple[str, str, str]  # severity, path, message


def collect_sops() -> list[Path]:
    out: list[Path] = []
    for p in sorted(DOCS.rglob("*.md")):
        if p.name in SKIP_NAMES:
            continue
        if "00-Maintenance" in p.parts:
            continue
        out.append(p)
    return out


def meta_blob(front: dict) -> dict:
    md = front.get("metadata")
    if isinstance(md, dict):
        return md
    return {}


def check_file(path: Path) -> list[Issue]:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    issues: list[Issue] = []

    if not text.startswith("---"):
        return [("ERROR", rel, "missing YAML frontmatter")]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return [("ERROR", rel, "broken frontmatter delimiters")]

    try:
        front = yaml.safe_load(parts[1]) or {}
    except Exception as e:  # noqa: BLE001
        return [("ERROR", rel, f"YAML parse error: {e}")]

    body = parts[2]
    if body.startswith("\n"):
        body_lstrip = body[1:]
    else:
        body_lstrip = body

    if front.get("layout") != "guide":
        issues.append(("WARN", rel, f"layout is {front.get('layout')!r}, expected 'guide'"))
    if not front.get("title"):
        issues.append(("ERROR", rel, "missing title"))
    if not front.get("description"):
        issues.append(("WARN", rel, "missing description (SEO / cards)"))

    md = meta_blob(front)
    if not md:
        issues.append(("ERROR", rel, "missing metadata: block"))
    else:
        for key in REQUIRED_META:
            if key not in md or md[key] in (None, ""):
                issues.append(("ERROR", rel, f"missing metadata.{key}"))
        if md.get("churn") == "high" and md.get("ttl_days") not in (30, "30"):
            issues.append(("WARN", rel, "churn: high but ttl_days is not 30"))
        lv = str(md.get("last_validated", ""))
        if lv and not re.match(r"^\d{4}-\d{2}-\d{2}$", lv):
            issues.append(("ERROR", rel, f"last_validated not YYYY-MM-DD: {lv}"))

    # --- Body structure ---
    h1s = re.findall(r"(?m)^#\s+(.+)$", body)
    if not h1s:
        issues.append(("ERROR", rel, "no H1 heading"))
    elif len(h1s) > 1:
        issues.append(("WARN", rel, f"multiple H1 headings ({len(h1s)})"))

    # Badge on same physical line as H1 only
    if re.search(r"!\[.*\]\([^)]+\)[^\n]*#\s", body):
        issues.append(("ERROR", rel, "image/badge and H1 on same line"))
    if re.search(r"img\.shields\.io", body):
        issues.append(("WARN", rel, "shields.io badge still present"))

    # Orphan body after closing Last Updated (runbook-style docs)
    lines = body.splitlines()
    lu_idxs = [i for i, l in enumerate(lines) if "**Last Updated:**" in l]
    if lu_idxs:
        for i in reversed(lu_idxs):
            prev = "\n".join(lines[max(0, i - 60) : i])
            if any(
                k in prev
                for k in ("TechDad's Tips", "Miles' Tips", "Strategic Gap", "## FAQ")
            ):
                after = [
                    l
                    for l in lines[i + 1 :]
                    if l.strip()
                    and "Back to Guide" not in l
                    and "Back to Library" not in l
                ]
                if after:
                    issues.append(
                        (
                            "ERROR",
                            rel,
                            f"orphan content after closing Last Updated ({len(after)} lines)",
                        )
                    )
                break

    # Heading level skips (# then ####)
    levels = [len(m.group(1)) for m in re.finditer(r"(?m)^(#{1,6})\s+", body)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1:
            issues.append(("WARN", rel, f"heading level skip {a} → {b}"))
            break

    # Unclosed code fences
    fence_count = len(re.findall(r"(?m)^```", body))
    if fence_count % 2:
        issues.append(("ERROR", rel, f"unclosed code fence (count={fence_count})"))

    # Unbalanced common HTML tags
    for tag in ("div", "table", "details", "summary", "section", "ul", "ol"):
        opens = len(re.findall(rf"<{tag}(?:\s|>)", body, flags=re.I))
        closes = len(re.findall(rf"</{tag}>", body, flags=re.I))
        if opens != closes:
            issues.append(
                ("ERROR", rel, f"unbalanced <{tag}> open={opens} close={closes}")
            )

    # phrase-card integrity (nested divs: count class markers, not non-greedy slice)
    card_starts = list(re.finditer(r'<div class="phrase-card">', body, flags=re.I))
    if not card_starts:
        issues.append(("WARN", rel, "no phrase-card block"))
    else:
        zh_n = len(re.findall(r'class="zh"', body))
        py_n = len(re.findall(r'class="py"', body))
        en_n = len(re.findall(r'class="en"', body))
        n = len(card_starts)
        if min(zh_n, py_n, en_n) < n:
            issues.append(
                (
                    "WARN",
                    rel,
                    f"phrase-card count={n} but zh={zh_n} py={py_n} en={en_n}",
                )
            )

    if "plain-summary" not in body and "Plain English" not in body:
        issues.append(("WARN", rel, "no plain-summary / Plain English block"))

    # Double-escaped entities
    if any(x in body for x in ("&amp;lt;", "&amp;gt;", "&amp;amp;", "&amp;quot;")):
        issues.append(("WARN", rel, "double-escaped HTML entities"))

    # Control chars (except tab/newline)
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", body):
        issues.append(("ERROR", rel, "control characters in body"))

    # NBSP-heavy or weird spaces
    nbsp = body.count("\u00a0")
    if nbsp > 5:
        issues.append(("INFO", rel, f"{nbsp} non-breaking spaces"))

    # Tables: header row without |---| separator
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not (s.startswith("|") and s.endswith("|") and s.count("|") >= 3):
            continue
        # skip separator rows
        if re.match(r"^\|[\s:\-|]+\|$", s):
            continue
        # look ahead for separator
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            continue
        nxt = lines[j].strip()
        # if this looks like a header (next is also pipe) and next is NOT separator
        # only flag when previous line is blank or heading (start of table)
        prev = lines[i - 1].strip() if i else ""
        if (
            (not prev or prev.startswith("#") or prev.startswith(">") or prev.startswith("<"))
            and nxt.startswith("|")
            and not re.match(r"^\|[\s:\-|]+\|$", nxt)
            and re.search(r"[A-Za-z\u4e00-\u9fff]", s)
        ):
            # next data row without separator is broken GFM table
            issues.append(
                ("ERROR", rel, f"table missing separator after L{i + 1}: {s[:70]}")
            )

    # Empty ## sections
    empty = re.findall(r"(?m)^##[^\n]+\n+(?=## |\Z)", body)
    if empty:
        issues.append(("WARN", rel, f"{len(empty)} empty ## section(s)"))

    # Trailing whitespace
    tw = sum(1 for ln in lines if ln != ln.rstrip(" \t"))
    if tw >= 10:
        issues.append(("INFO", rel, f"{tw} lines with trailing whitespace"))

    # 3+ consecutive blank lines
    if re.search(r"\n{4,}", body):
        issues.append(("WARN", rel, "3+ consecutive blank lines (sparse formatting)"))

    # TODO leftovers
    if re.search(r"\b(TODO|FIXME|XXX)\b", body):
        issues.append(("INFO", rel, "contains TODO/FIXME/XXX"))

    # Broken list markers mixed (• alone without space issues)
    if re.search(r"(?m)^•[^ \t]", body):
        issues.append(("WARN", rel, "bullet • without following space"))

    # Markdown list with tab indent only mess
    if re.search(r"(?m)^\t+- ", body):
        issues.append(("INFO", rel, "tab-indented list items"))

    # Expected runbook-ish sections (soft)
    has_runbook = bool(
        re.search(
            r"(?im)^## .*(runbook|steps|plan a|immediate|how to|protocol)",
            body,
        )
    )
    has_fallback = bool(
        re.search(r"(?im)^## .*(fallback|plan b|emergency|if .*fail)", body)
    )
    if not has_runbook:
        issues.append(("INFO", rel, "no clear Steps/Runbook ## section"))
    if not has_fallback:
        issues.append(("INFO", rel, "no clear Fallback/Plan B ## section"))

    # Footer back-link consistency
    if not re.search(r"Back to Guide Library|Back to", body, re.I):
        issues.append(("INFO", rel, "no back-to-library footer link"))

    # validation_method missing already ERROR; duplicate Last Updated lines
    lu = len(re.findall(r"\*\*Last Updated:\*\*", body))
    if lu > 1:
        issues.append(("WARN", rel, f"duplicate Last Updated lines ({lu})"))

    # Frontmatter title vs H1 rough match (optional soft)
    title = str(front.get("title") or "")
    if h1s and title:
        h1_clean = re.sub(r"[^\w\s]", "", h1s[0], flags=re.U).lower()
        t_clean = re.sub(r"[^\w\s]", "", title, flags=re.U).lower()
        # if completely disjoint words
        h1_words = set(h1_clean.split())
        t_words = set(t_clean.split())
        if h1_words and t_words and not (h1_words & t_words):
            issues.append(
                ("WARN", rel, f"H1 may not match title: H1={h1s[0]!r} title={title!r}")
            )

    return issues


def main() -> int:
    sops = collect_sops()
    all_issues: list[Issue] = []
    for p in sops:
        all_issues.extend(check_file(p))

    by_sev: dict[str, list[Issue]] = defaultdict(list)
    for sev, rel, msg in all_issues:
        by_sev[sev].append((sev, rel, msg))

    print(f"Scanned {len(sops)} SOP files\n")
    for sev in ("ERROR", "WARN", "INFO"):
        items = by_sev[sev]
        print(f"=== {sev} ({len(items)}) ===")
        # group by file
        by_file: dict[str, list[str]] = defaultdict(list)
        for _, rel, msg in items:
            by_file[rel].append(msg)
        for rel in sorted(by_file):
            for msg in by_file[rel]:
                print(f"  {rel}: {msg}")
        print()

    err_n = len(by_sev["ERROR"])
    warn_n = len(by_sev["WARN"])
    print(f"TOTAL: {len(all_issues)}  (ERROR={err_n} WARN={warn_n} INFO={len(by_sev['INFO'])})")
    # fail CI only on ERROR
    return 1 if err_n else 0


if __name__ == "__main__":
    sys.exit(main())
