# ChinaOps Roadmap

## v1.0 → v1.16.0 (Current — Jul 2026)
**Release Focus:** Traveler review fixes (MRZ consistency, hospital scope, trip-stage home)

✅ **Completed (v1.0 — Jan 2026):**
- 16 comprehensive SOPs across 4 categories
- Standardized 10-section SOP template
- Professional HTML guide site with 4 quick-path navigation
- CC BY-NC 4.0 non-commercial license
- Contribution framework (CONTRIBUTING.md)
- Legal protection (LEGAL_NOTICE.md)
- Brand identity: TechDadShanghai

✅ **Completed (v1.1 — Mar 2026):**
- Content audit: 5 P1 critical errors fixed
- 3 stub documents fully expanded (lost-passport, network-outage, milk-recall-check)
- 1 new guide: Alipay & WeChat Pay for Foreign Visitors
- index.json: 16 → 28 documents catalogued
- Holiday dates corrected; Nestlé recall status updated
✅ **Completed (v1.2 — Apr 2026):**
- Freshness audit: Corrected 2026 Labor Day dates and Visa-free expansions (UK/Canada).
- "Lost" Content Recovery: Identified and added 9 previously unindexed guides to `index.json`.
- TTL Reset: Validated and bumped `last_validated` timestamps for all 31 catalogued guides.
- Content Correction: Alipay per-transaction limit corrected to $5,000 USD for verified users.
- Homepage UI: Updated announcement bar and version badges to v1.2.

✅ **Completed (v1.3 — Jul 14, 2026):**
- Power bank CCC/QR rules, payment recovery SOP, eSIM comparison, HSR child/stroller notes.

✅ **Completed (v1.3.1 — Jul 21, 2026):**
- Shared design tokens + ESL plain-English path labels.
- Mobile guide navigation; system fonts for China connectivity.
- All 38 SOPs have SRE metadata; TTL audit skips index hubs and fails on missing meta.

✅ **Completed (v1.4.0 — Jul 21, 2026):**
- Symptom Index (problem → guide).
- High-churn registry + 30-day TTL on 6 critical SOPs.
- TEMPLATE_ENHANCED_SOP.md + CONTRIBUTING PR gates.
- `check_catalog.py` + CI (TTL + catalog + links).

✅ **Completed (v1.5.0 — Jul 21, 2026):**
- Plain English summary on all 38 SOPs.
- `scope: national | shanghai` metadata + UI badges.
- Phrase cards for hotel/taxi/hospital/allergy/vegan/nursing/pharmacy scenes.
- Category hubs clarify Shanghai-first vs national content.

✅ **Completed (v1.6.0 — Jul 21, 2026):**
- Phrase cards on remaining SOPs (27 more).
- Symptom Index filter chips + count.
- High-churn desktop re-check; holiday calendar staleness fixed.

✅ **Completed (v1.7.0 — Jul 21, 2026):**
- Offline print pack (`print-pack.html`).
- Phrase style guide + CONTRIBUTING hooks.
- Field re-test checklist for next real trip.

✅ **Completed (v1.8.0 — Jul 21, 2026):**
- A4 duplex compact pack + bilingual EN/ZH one-pager.
- Field re-test log template for first real trip PR.

✅ **Completed (v1.9.0 — Jul 21, 2026):**
- Home: 4 primary tasks + more-paths disclosure; calmer surface.
- Print Hub; mobile guide cards; guide bottom bar + mobile TOC.

✅ **Completed (v1.10.0 — Jul 21, 2026):**
- Symptom Index keyword search + chip combo.
- Interactive pre-flight checklist (localStorage).
- Design tokens / component reference for contributors.

✅ **Completed (v1.11.0 — Jul 21, 2026):**
- Catalog search (`search.html`) with aliases.
- Landing Protocol interactive gates (`landing-checklist.html`).
- CI static asset check (`check_static_assets.py`).

✅ **Completed (v1.12.0 — Jul 21, 2026):**
- Full-text body search (`search-fulltext.html`) via Pagefind + `fulltext.json` fallback.
- Browser MRZ name tool for 12306 (`mrz-tool.html`).
- `npm run build:search` / `scripts/build_fulltext_index.py` pipeline.

✅ **Completed (v1.13.0 — Jul 21, 2026):**
- Money Runtime, Stay Beyond Hotel, China App Stack SOPs.
- City deltas: Beijing · Guangzhou & Shenzhen.
- Insurance & hospital bills SOP.
- Phrase/allergy card generator (`phrase-card-tool.html`).
- Catalog at **44** guides.

✅ **Completed (v1.14.0 — Jul 21, 2026):**
- Child dose calculator Web UI.
- City deltas: Chengdu · Hangzhou.
- Long-stay risk boundaries SOP.
- Next-trip field-test pack for maintainers.
- Catalog at **47** guides.

✅ **Completed (v1.15.0 — Jul 21, 2026):**
- 72h survival printable pack + offline pack builder script.
- City deltas: Xi'an · Chongqing.
- Catalog at **49** guides.

✅ **Completed (v1.16.0 — Jul 21, 2026):**
- Traveler review P0–P2: MRZ consistency, hospital multi-city triage, preflight 72h, dose safety, home stages, description cleanup, first-night corridors.
---

## Next (v2.0 / community)
- First **real** field_test log entry from an actual trip (pack + honesty banner ready).
- Optional: CI artifact that runs `build_offline_pack.py --zip`.
- Community-contributed city deltas / language packs (ZH UI).

## v2.0 (Planned)
**Release Focus:** Visualization & deeper interactive tools

### 🛠️ Interactive Web Features
- ~~Pre-flight + Landing checklists~~ → v1.10–1.11
- ~~Catalog search~~ → v1.11 `search.html`
- ~~Full-text search~~ → v1.12 Pagefind + JSON fallback
- ~~MRZ browser UI~~ → v1.12 `mrz-tool.html`
- **Script Web UI**: more Python helpers (dose / train checker) in browser

### 🎨 UI/UX Improvements
- **Zebra-striped guide tables** — Alternate row colors for better readability
- **Clickable table rows** — Full row click to guide, not just title text
- **Mobile table optimization** — Improved responsive layout for small screens
- **Quick-path card enhancements** — Show pulse animation for "Emergency" paths

### 📊 Analytics & User Feedback
- Basic usage analytics (with privacy in mind)
- Feedback form/issue template for user suggestions

### 📝 Content Expansion
- User-contributed tips & local variations
- Regional section (Shanghai vs. other cities)
- Multi-language support consideration (EN → ZH)

---

## Future Considerations (v3.0+)
- Interactive checklist tools
- Offline downloadable PDF versions
- Mobile app companion
- Community forum/discussion area
- Video tutorials for key SOPs

---

**Last Updated:** Jul 21, 2026  
**Maintained by:** TechDadShanghai
