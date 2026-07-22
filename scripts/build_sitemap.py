#!/usr/bin/env python3
"""Build sitemap.xml for indexable ChinaOps URLs (GH Pages + baseurl)."""
from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Match live host casing used by GitHub Pages
SITE = "https://milesxlab.github.io/ChinaOps"

# Public hubs / tools (not print sheet variants)
STATIC_INDEXABLE = [
    "",  # home
    "docs/",
    "docs/symptom-index/",
    "search.html",
    "search-fulltext.html",
    "mrz-tool.html",
    "phrase-card-tool.html",
    "dose-calculator.html",
    "preflight-checklist.html",
    "landing-checklist.html",
    "print-hub.html",
    "survival-72h.html",
]

# Intentionally omitted (noindex / thin): print-pack*.html, 00-Maintenance


def md_to_pretty_url(path: str) -> str:
    p = path.replace("\\", "/").lstrip("/")
    if p.endswith(".md"):
        p = p[: -len(".md")] + "/"
    if not p.endswith("/"):
        p += "/"
    return p


def add_url(urlset: ET.Element, loc: str, lastmod: str, priority: str, changefreq: str) -> None:
    u = ET.SubElement(urlset, "url")
    ET.SubElement(u, "loc").text = loc
    ET.SubElement(u, "lastmod").text = lastmod
    ET.SubElement(u, "changefreq").text = changefreq
    ET.SubElement(u, "priority").text = priority


def main() -> int:
    today = date.today().isoformat()
    catalog = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    last = str(catalog.get("lastUpdated") or today)

    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    seen: set[str] = set()

    def push(path: str, priority: str, changefreq: str = "weekly", lastmod: str = last) -> None:
        path = path.lstrip("/")
        loc = f"{SITE}/{path}" if path else f"{SITE}/"
        if loc in seen:
            return
        seen.add(loc)
        add_url(urlset, loc, lastmod, priority, changefreq)

    push("", "1.0", "weekly")
    for p in STATIC_INDEXABLE[1:]:
        push(p, "0.8" if p.startswith("docs") else "0.7")

    for section in catalog.get("sections", []):
        for f in section.get("files", []):
            rel = f.get("path") or ""
            if "00-Maintenance" in rel:
                continue
            push(md_to_pretty_url(rel), "0.9", "monthly")

    # Category indexes if present
    for hub in (
        "docs/01-System-Setup/",
        "docs/02-Daily-Runtime/",
        "docs/03-Emergency-DR/",
        "docs/04-Parenting-Patch/",
        "docs/05-Event-Operations/",
    ):
        if (ROOT / hub.rstrip("/") / "index.md").is_file() or (
            ROOT / "docs" / hub.split("/")[1] / "index.md"
        ).is_file():
            push(hub, "0.6", "monthly")

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    out = ROOT / "sitemap.xml"
    tree.write(out, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {out} ({len(seen)} URLs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
