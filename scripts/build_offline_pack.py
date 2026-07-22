#!/usr/bin/env python3
"""
Copy a minimal offline-capable file set for ChinaOps 72h survival.

Usage:
  python scripts/build_offline_pack.py
  python scripts/build_offline_pack.py --zip

Output:
  _offline_pack/   (gitignored by default if listed)
  chinaops-offline-72h.zip  (with --zip)
"""
from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_offline_pack"

# Keep small: tools + print + survival + shared assets
FILES = [
    "survival-72h.html",
    "print-hub.html",
    "print-pack.html",
    "print-pack-a4.html",
    "print-pack-bilingual.html",
    "preflight-checklist.html",
    "landing-checklist.html",
    "mrz-tool.html",
    "phrase-card-tool.html",
    "dose-calculator.html",
    "search.html",
    "search-fulltext.html",
    "index.html",
    "index.json",
    "assets/css/chinaops.css",
    "assets/js/chinaops.js",
    "assets/search/fulltext.json",
]

DIRS_OPTIONAL = [
    "pagefind",  # full-text search offline if present
]

README = """# ChinaOps offline 72h pack

1. Open survival-72h.html in a browser (works offline for this folder if paths stay relative).
2. Print / Save PDF of survival-72h.html and print-pack-a4.html before you fly.
3. Tools (MRZ, phrase card, dose) need the files in this folder; full-text search needs the pagefind/ folder if included.

Not a substitute for live SOP updates — re-download after major rule changes.
Personal use only · CC BY-NC 4.0
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", action="store_true", help="Also write chinaops-offline-72h.zip at repo root")
    args = ap.parse_args()

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    missing = []
    for rel in FILES:
        src = ROOT / rel
        if not src.is_file():
            missing.append(rel)
            continue
        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    for d in DIRS_OPTIONAL:
        src = ROOT / d
        if src.is_dir():
            shutil.copytree(src, OUT / d, dirs_exist_ok=True)

    (OUT / "README-OFFLINE.txt").write_text(README, encoding="utf-8")

    print(f"Wrote offline pack → {OUT.relative_to(ROOT)}")
    if missing:
        print("MISSING (skipped):")
        for m in missing:
            print(" ", m)

    if args.zip:
        zpath = ROOT / "chinaops-offline-72h.zip"
        if zpath.exists():
            zpath.unlink()
        with zipfile.ZipFile(zpath, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for f in OUT.rglob("*"):
                if f.is_file():
                    zf.write(f, arcname=str(Path("chinaops-offline-72h") / f.relative_to(OUT)))
        print(f"Wrote zip → {zpath.name} ({zpath.stat().st_size // 1024} KB)")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
