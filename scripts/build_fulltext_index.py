"""
Build full-text search sources for ChinaOps.

1) Writes minimal HTML tree under `_pagefind_src/` for Pagefind indexing.
2) Writes `assets/search/fulltext.json` for client-side fallback (no Pagefind required).

Usage:
  python scripts/build_fulltext_index.py
  npx --yes pagefind --site _pagefind_src --output-path pagefind
"""
from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT_HTML = ROOT / "_pagefind_src"
OUT_JSON = ROOT / "assets" / "search" / "fulltext.json"

SKIP_NAMES = {
    "index.md",
    "symptom-index.md",
    "high-churn-registry.md",
    "print-pack.md",
    "phrase-style-guide.md",
    "field-retest-checklist.md",
    "field-retest-log.md",
    "design-tokens.md",
    "preflight-checklist.md",
    "survival-72h.md",
}


def strip_frontmatter(text: str) -> tuple[dict, str]:
    meta: dict = {}
    if not text.startswith("---"):
        return meta, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return meta, text
    # light parse title
    for line in parts[1].splitlines():
        if line.strip().startswith("title:"):
            meta["title"] = line.split(":", 1)[1].strip().strip("\"'")
    return meta, parts[2]


def md_to_plain(md: str) -> str:
    text = md
    # remove HTML blocks but keep text inside simple tags
    text = re.sub(r"<[^>]+>", " ", text)
    # images / links
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # code fences
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # headings / emphasis
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"[*_~]{1,3}", "", text)
    # tables pipes
    text = text.replace("|", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def md_to_simple_html_body(md: str) -> str:
    """Very small markdown-ish to HTML for Pagefind (good enough for search)."""
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False
    in_code = False
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            chunk = " ".join(para).strip()
            if chunk:
                # inline code/links/bold light
                chunk = re.sub(r"`([^`]+)`", r"<code>\1</code>", chunk)
                chunk = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", chunk)
                chunk = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", chunk)
                out.append(f"<p>{chunk}</p>")
            para = []

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            flush_para()
            close_ul()
            if not in_code:
                out.append("<pre><code>")
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            out.append(escape(line) + "\n")
            continue
        if not line.strip():
            flush_para()
            close_ul()
            continue
        if re.match(r"^#{1,3}\s+", line):
            flush_para()
            close_ul()
            level = len(line) - len(line.lstrip("#"))
            level = min(max(level, 1), 3)
            title = line.lstrip("#").strip()
            out.append(f"<h{level}>{escape(title)}</h{level}>")
            continue
        if re.match(r"^[-*]\s+", line):
            flush_para()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            item = re.sub(r"^[-*]\s+", "", line)
            item = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", item)
            out.append(f"<li>{escape(item)}</li>" if "<strong>" not in item else f"<li>{item}</li>")
            continue
        close_ul()
        # strip raw HTML lines partially
        if line.strip().startswith("<") and line.strip().endswith(">"):
            # keep text from simple phrase cards later via plain export
            continue
        para.append(line)

    flush_para()
    close_ul()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def pretty_url(rel_md: Path) -> str:
    # docs/a/b.md -> docs/a/b/
    p = rel_md.as_posix()
    if p.endswith(".md"):
        p = p[:-3] + "/"
    return p


def main() -> None:
    records = []
    # reset html tree
    if OUT_HTML.exists():
        import shutil

        shutil.rmtree(OUT_HTML)
    OUT_HTML.mkdir(parents=True)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(DOCS.rglob("*.md"))
    for path in files:
        if path.name in SKIP_NAMES:
            continue
        if "00-Maintenance" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        meta, body = strip_frontmatter(path.read_text(encoding="utf-8"))
        title = meta.get("title") or path.stem.replace("-", " ").title()
        plain = md_to_plain(body)
        url = pretty_url(rel)
        section = rel.parts[1] if len(rel.parts) > 1 else "docs"

        records.append(
            {
                "title": title,
                "url": url,
                "path": rel.as_posix(),
                "section": section,
                "text": plain[:50000],
            }
        )

        # HTML for Pagefind
        html_body = md_to_simple_html_body(body)
        # also inject plain text block for coverage
        dest_dir = OUT_HTML / rel.parent / path.stem
        dest_dir.mkdir(parents=True, exist_ok=True)
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(title)} — ChinaOps">
  <link rel="canonical" href="/ChinaOps/{url}">
</head>
<body>
  <main data-pagefind-body>
    <h1>{escape(title)}</h1>
    <p data-pagefind-meta="section">{escape(section)}</p>
    {html_body}
    <section data-pagefind-weight="0.2">
      <h2>Full text</h2>
      <p>{escape(plain[:20000])}</p>
    </section>
  </main>
</body>
</html>
"""
        (dest_dir / "index.html").write_text(html, encoding="utf-8")

    OUT_JSON.write_text(
        json.dumps(
            {
                "generated": True,
                "count": len(records),
                "baseUrl": "/ChinaOps/",
                "documents": records,
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(records)} docs → {OUT_JSON.relative_to(ROOT)}")
    print(f"Wrote Pagefind source tree → {OUT_HTML.relative_to(ROOT)}")
    print("Next: npx --yes pagefind --site _pagefind_src --output-path pagefind")


if __name__ == "__main__":
    main()
