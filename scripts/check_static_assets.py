"""Ensure critical static HTML entry points exist."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "index.html",
    "index.json",
    "print-hub.html",
    "print-pack.html",
    "print-pack-a4.html",
    "print-pack-bilingual.html",
    "preflight-checklist.html",
    "landing-checklist.html",
    "search.html",
    "search-fulltext.html",
    "mrz-tool.html",
    "phrase-card-tool.html",
    "assets/css/chinaops.css",
    "assets/js/chinaops.js",
    "assets/search/fulltext.json",
]

# Pagefind is preferred for full-text; warn but don't fail if missing
OPTIONAL_PAGEFIND = [
    "pagefind/pagefind-ui.js",
    "pagefind/pagefind-ui.css",
]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    print("--- ChinaOps static assets ---")
    if missing:
        print("MISSING:")
        for m in missing:
            print(" ", m)
        return 1
    print(f"OK: {len(REQUIRED)} required files present.")
    pf_missing = [p for p in OPTIONAL_PAGEFIND if not (ROOT / p).is_file()]
    if pf_missing:
        print("WARN: Pagefind UI not built (fallback fulltext.json still works):")
        for m in pf_missing:
            print(" ", m)
        print("  Run: npm run build:search")
    else:
        print("OK: Pagefind UI bundle present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
