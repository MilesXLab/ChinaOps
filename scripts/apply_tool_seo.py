#!/usr/bin/env python3
"""Inject canonical / robots / OG / Twitter into static tool HTML heads."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://milesxlab.github.io/ChinaOps"
OG = f"{BASE}/images/og-default.png"

# path relative to site root, noindex?
TOOLS: list[tuple[str, bool]] = [
    ("mrz-tool.html", False),
    ("dose-calculator.html", False),
    ("phrase-card-tool.html", False),
    ("search.html", False),
    ("search-fulltext.html", False),
    ("preflight-checklist.html", False),
    ("landing-checklist.html", False),
    ("print-hub.html", False),
    ("survival-72h.html", False),
    ("print-pack.html", True),
    ("print-pack-a4.html", True),
    ("print-pack-bilingual.html", True),
]


def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    if not m:
        return "ChinaOps"
    return re.sub(r"\s+", " ", m.group(1)).strip()


def extract_desc(html: str) -> str:
    m = re.search(
        r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']',
        html,
        re.I,
    )
    if m:
        return m.group(1)
    m = re.search(
        r'<meta\s+content=["\']([^"\']*)["\']\s+name=["\']description["\']',
        html,
        re.I,
    )
    return m.group(1) if m else "ChinaOps technical runbook"


def build_block(path: str, title: str, desc: str, noindex: bool) -> str:
    canon = f"{BASE}/{path}"
    robots = "noindex, follow" if noindex else "index, follow"
    # Escape for attribute context (desc may contain quotes rarely)
    desc_attr = desc.replace('"', "&quot;")
    title_attr = title.replace('"', "&quot;")
    return f"""  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canon}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="ChinaOps">
  <meta property="og:title" content="{title_attr}">
  <meta property="og:description" content="{desc_attr}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{OG}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title_attr}">
  <meta name="twitter:description" content="{desc_attr}">
  <meta name="twitter:image" content="{OG}">
"""


def strip_existing(html: str) -> str:
    patterns = [
        r'\s*<meta\s+name=["\']robots["\'][^>]*>\s*',
        r'\s*<link\s+rel=["\']canonical["\'][^>]*>\s*',
        r'\s*<meta\s+property=["\']og:[^"\']+["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']twitter:[^"\']+["\'][^>]*>\s*',
    ]
    for p in patterns:
        html = re.sub(p, "\n", html, flags=re.I)
    return html


def apply_one(path: str, noindex: bool) -> bool:
    fp = ROOT / path
    if not fp.is_file():
        print(f"SKIP missing {path}")
        return False
    html = fp.read_text(encoding="utf-8")
    html = strip_existing(html)
    title = extract_title(html)
    desc = extract_desc(html)
    block = build_block(path, title, desc, noindex)

    # Insert after description meta if present, else after viewport
    m = re.search(
        r'(<meta\s+name=["\']description["\'][^>]*>)',
        html,
        re.I,
    )
    if m:
        html = html[: m.end()] + "\n" + block + html[m.end() :]
    else:
        m2 = re.search(r'(<meta\s+name=["\']viewport["\'][^>]*>)', html, re.I)
        if not m2:
            print(f"FAIL no insert point {path}")
            return False
        html = html[: m2.end()] + "\n" + block + html[m2.end() :]

    # Collapse excessive blank lines in head only lightly
    html = re.sub(r"\n{3,}", "\n\n", html)
    fp.write_text(html, encoding="utf-8", newline="\n")
    print(f"OK {path} robots={'noindex' if noindex else 'index'}")
    return True


def main() -> int:
    ok = 0
    for path, noindex in TOOLS:
        if apply_one(path, noindex):
            ok += 1
    print(f"Updated {ok}/{len(TOOLS)} tool pages")
    return 0 if ok == len(TOOLS) else 1


if __name__ == "__main__":
    sys.exit(main())
