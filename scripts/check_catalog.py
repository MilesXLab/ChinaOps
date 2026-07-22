"""Ensure index.json, docs SOPs, and catalog stay in sync."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CATALOG = ROOT / "index.json"

# Navigation-only markdown (not SOPs)
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
    "release-notes-v1.16.md",
}


def sop_files() -> set[Path]:
    files: set[Path] = set()
    for p in DOCS.rglob("*.md"):
        if p.name in SKIP_NAMES:
            continue
        if "00-Maintenance" in p.parts:
            continue
        files.add(p.relative_to(ROOT).as_posix())
    return files


def catalog_paths() -> set[str]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    paths: set[str] = set()
    for section in data.get("sections", []):
        for f in section.get("files", []):
            paths.add(f["path"].replace("\\", "/"))
    return paths


def main() -> int:
    sops = sop_files()
    cat = catalog_paths()

    missing_on_disk = sorted(cat - sops)
    # catalog uses docs/... paths; sops are same style
    uncatalogued = sorted(sops - cat)

    print("--- ChinaOps catalog check ---")
    print(f"SOPs on disk (excl. hubs): {len(sops)}")
    print(f"index.json entries:        {len(cat)}")

    errors = 0
    if missing_on_disk:
        errors += len(missing_on_disk)
        print("\n[ERROR] In index.json but file missing:")
        for p in missing_on_disk:
            print(f"  - {p}")

    if uncatalogued:
        errors += len(uncatalogued)
        print("\n[ERROR] SOP on disk but not in index.json:")
        for p in uncatalogued:
            print(f"  - {p}")

    if errors == 0:
        print("\nCatalog OK: disk and index.json match.")
        return 0

    print(f"\nCatalog FAILED ({errors} issue(s)).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
