#!/usr/bin/env python3
"""Smoke checks for ChinaOps browser tools and parity helpers."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from passport_mrz_converter import format_mrz_name  # noqa: E402  single source of truth


def main() -> int:
    errors: list[str] = []
    tools = [
        "mrz-tool.html",
        "dose-calculator.html",
        "phrase-card-tool.html",
        "search.html",
        "search-fulltext.html",
        "preflight-checklist.html",
        "landing-checklist.html",
        "survival-72h.html",
        "print-hub.html",
        "print-pack.html",
        "print-pack-a4.html",
        "print-pack-bilingual.html",
    ]
    print("--- ChinaOps tool smoke ---")
    for t in tools:
        p = ROOT / t
        if not p.is_file():
            errors.append(f"missing {t}")
            continue
        text = p.read_text(encoding="utf-8")
        if 'href="./assets/css/chinaops.css"' not in text and t.startswith("print-pack"):
            # print packs use inline CSS — ok
            pass
        elif t.startswith("print-pack") or t == "print-hub.html" or t == "survival-72h.html":
            pass
        elif 'href="./assets/css/chinaops.css"' not in text and "chinaops.css" not in text:
            if t not in ("print-pack.html", "print-pack-a4.html", "print-pack-bilingual.html", "survival-72h.html"):
                errors.append(f"{t}: missing chinaops.css link")
        # script tools should not call remote analytics
        if re.search(r"google-analytics|gtag\(|facebook\.net|hotjar", text, re.I):
            errors.append(f"{t}: unexpected third-party tracker")

    # MRZ parity cases
    cases = [
        ("John", "Smith", "SMITH<<JOHN"),
        ("José", "García", "GARCIA<<JOSE"),
        ("Mary-Jane", "O'Brien", "OBRIEN<<MARYJANE"),
        ("Jean Luc", "Picard", "PICARD<<JEANLUC"),
    ]
    for first, last, expect in cases:
        got = format_mrz_name(first, last)
        if got != expect:
            errors.append(f"MRZ {first}/{last}: got {got!r} want {expect!r}")
        else:
            print(f"  OK MRZ {first} {last} -> {got}")

    # Browser tool must still embed the same letter-cleanup contract (not a full re-parse)
    mrz_html = (ROOT / "mrz-tool.html").read_text(encoding="utf-8")
    mrz_needles = (
        'return last + "<<" + first',
        'replace(/[-\']/g, "")',
        'replace(/[^A-Z]/g, "")',
    )
    missing = [n for n in mrz_needles if n not in mrz_html]
    if missing:
        for n in missing:
            errors.append(f"mrz-tool.html missing expected rule fragment: {n!r}")
    else:
        print("  OK mrz-tool.html rule fragments present")

    # fulltext index
    ft = ROOT / "assets" / "search" / "fulltext.json"
    if not ft.is_file():
        errors.append("missing assets/search/fulltext.json")
    else:
        data = json.loads(ft.read_text(encoding="utf-8"))
        docs = data.get("documents") or []
        print(f"  OK fulltext.json documents={len(docs)}")
        if len(docs) < 40:
            errors.append(f"fulltext.json only {len(docs)} docs (expected ~49)")
        for d in docs[:3]:
            u = d.get("url") or ""
            if not u.endswith("/"):
                errors.append(f"fulltext url missing trailing slash: {u}")
            if u.startswith("http"):
                errors.append(f"fulltext url should be site-relative: {u}")

    # dose tool: no antibiotic preset
    dose = (ROOT / "dose-calculator.html").read_text(encoding="utf-8")
    if "amox" in dose.lower() and "Amoxicillin" in dose:
        errors.append("dose-calculator still exposes Amoxicillin preset")
    else:
        print("  OK dose-calculator has no antibiotic preset")

    # checklists load shared JS
    for name in ("preflight-checklist.html", "landing-checklist.html"):
        t = (ROOT / name).read_text(encoding="utf-8")
        if "assets/js/chinaops.js" not in t:
            errors.append(f"{name}: missing chinaops.js")
        if "data-storage-key" not in t:
            errors.append(f"{name}: missing data-storage-key")
        else:
            print(f"  OK {name} storage key present")

    if errors:
        print("FAIL:")
        for e in errors:
            print(" ", e)
        return 1
    print(f"OK: {len(tools)} tools + MRZ parity + indexes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
