---
layout: guide
title: "Release notes draft: v1.12 → v1.16"
description: "Maintainer release notes for the product stack shipped on PR #9."
---

# Release notes draft: v1.12 → v1.16

**Audience:** maintainers / GitHub release body  
**Branch:** `release/v1.12-fulltext-mrz` → `main` (PR #9)  
**Site version badge:** v1.16.x · **Guides:** 49

---

## Highlights

### Find answers faster
- **Full-text search** (`search-fulltext.html`) with Pagefind + `fulltext.json` fallback  
- **Title search** (`search.html`) with aliases  
- **Symptom Index** with filters + keyword search  

### Browser tools (no upload)
- **MRZ tool** — passport name → `SURNAME<<GIVEN` for 12306  
- **Phrase / allergy card** — printable bilingual staff card  
- **Child dose calculator** — weight × mg/kg, kg/lb, OTC presets only  

### Offline paper
- **72h survival pack** (3 pages) + Print Hub (A4 / bilingual / standard)  
- Offline folder builder: `python scripts/build_offline_pack.py [--zip]`  

### Longer stays & cities
- Money Runtime · Stay Beyond Hotel · App Stack · Long-stay risk boundaries  
- Insurance & hospital bills · multi-city hospital triage  
- City deltas: Beijing, Guangzhou/Shenzhen, Chengdu, Hangzhou, Xi’an, Chongqing  

### Quality bar
- SOP format audit · catalog/link/static gates · tool smoke tests  
- Playwright E2E for tools · honesty note that high-churn is still desktop-reviewed  

---

## Suggested GitHub Release body

```markdown
## ChinaOps v1.16

Practical runbook updates for travelers and parents in China.

### New
- Full-text + catalog search
- MRZ, phrase-card, and dose tools (browser-only)
- 72h printable survival pack + offline pack script
- Money / housing / app hygiene / long-stay risk SOPs
- Six city delta sheets + first-night corridors
- Insurance & hospital bills; clearer national vs Shanghai hospital guidance

### Fixed (traveler review)
- 12306 name format aligned with MRZ tool
- Pre-flight includes 72h pack
- Dose tool no longer suggests antibiotics
- Home: trip stages + desktop-review honesty banner

### Maintainers
- `npm test` — static tool smoke + Playwright E2E
- `python scripts/check_sop_format.py` and existing CI health checks
- Field-test pack ready for the first real trip log (do not invent field_test)

**Guides:** 49 · **License:** CC BY-NC 4.0 (personal use)
```

---

## Merge checklist

1. CI green: SOP Health + tools E2E  
2. Spot-check live preview (Pages / Cloudflare) for `mrz-tool`, `survival-72h`, `search-fulltext`  
3. Merge PR #9  
4. Tag `v1.16.0` (or `v1.16.1` if tool-hardening commits count)  
5. Paste release body above  
6. Optional: run `npm run build:search` on main if Pages build does not  

---

## Not in this release

- Fabricated field_test log (requires a real trip)  
- Chinese UI localization  
- Mobile app  

[← High-churn registry](../high-churn-registry/)
