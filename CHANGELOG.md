# ChinaOps Changelog

All notable changes to the ChinaOps project will be documented in this file.

---

## [v1.14.0] - 2026-07-21

### 💊 Tools
- **Child dose calculator** (`dose-calculator.html`): weight × mg/kg reference, common presets, browser-only.
- Links from parenting symptom paths and scripts README.

### 🏙️ City deltas
- **Chengdu** and **Hangzhou** delta sheets (with existing Beijing / GZ–SZ set).

### ⚖️ Long-stay
- **Long-stay risk boundaries** SOP: status, banking, SIM lock-in, work grey zones (explicitly not legal advice).

### 🧪 Field-test readiness
- **Next trip field-test pack** under `docs/00-Maintenance/`.
- Money Runtime added to high-churn registry watch list.
- Catalog **47** guides.

---

## [v1.13.0] - 2026-07-21

### 💰 Money, stay, apps (72h → 30–90 days)
- **Money Runtime:** ATM cash, pre-auth freezes, visitor pay modes, fapiao invoices (`money-runtime.md`).
- **Stay Beyond Hotel:** homestay registration, refused foreigner check-in, short-term Plan B (`stay-beyond-hotel.md`).
- **China App Stack:** install order + WeChat/Alipay account hygiene (`china-app-stack.md`).

### 🏙️ City deltas
- **Beijing** and **Guangzhou & Shenzhen** delta sheets vs Shanghai defaults.

### 🧾 Insurance + tools
- **Insurance & hospital bills** claim-pack SOP.
- **Phrase / allergy card generator** (`phrase-card-tool.html`) — browser-only print/PDF.
- Symptom Index, home library, and catalog updated (**44 guides**).

---

## [v1.12.0] - 2026-07-21

### 🔎 Full-text search
- New **`search-fulltext.html`**: body search across SOP content.
- **Pagefind** index (`pagefind/`) with auto-fallback to **`assets/search/fulltext.json`** when the bundle is missing.
- Build pipeline: `scripts/build_fulltext_index.py` + `npm run build:search`.
- Title-only catalog search remains at `search.html`.

### 🚄 MRZ browser tool
- New **`mrz-tool.html`**: passport given + surname → `LASTNAME<<FIRSTNAME` for 12306 (client-side only).
- Linked from Train Ticket Trap guide, nav, and home “More paths”.

### 🧰 Maintenance
- Static asset CI requires `search-fulltext.html`, `mrz-tool.html`, and `fulltext.json`.
- CI rebuilds fulltext JSON on each health check.

---

## [v1.11.0] - 2026-07-21

### 🔍 Guide search
- New **`search.html`**: client-side search over `index.json` with alias expansion (payment, passport, train…).
- Quick-tag chips; links to Jekyll pretty paths.

### 🛫 Landing checklist
- New **`landing-checklist.html`**: ordered airport gates with localStorage (separate key from pre-flight).
- Linked from Landing Protocol verification loop + home “Before your flight”.

### 🧰 CI
- **`scripts/check_static_assets.py`** + workflow step: required HTML/CSS/JS entry points must exist.

---

## [v1.10.0] - 2026-07-21

### 🔎 Symptom search
- Search field on Symptom Index filters **table rows** by keyword (works with category chips).
- Clear button + live count; full list remains visible without JavaScript.

### ✅ Pre-flight checklist
- Interactive **`preflight-checklist.html`** with localStorage progress + reset.
- Markdown mirror `docs/preflight-checklist.md`; linked from home “Before your flight”.

### 🎨 Design tokens doc
- Contributor reference: `docs/00-Maintenance/design-tokens.md` (tokens, components, a11y rules).

---

## [v1.9.0] - 2026-07-21

### 🎨 UI/UX (task-first)
- **Home:** calm light background (no full purple wash); primary CTA row; **4 main tasks** only; extra paths under collapsible “More paths”.
- **Print Hub** (`print-hub.html`): one decision page — A4 duplex recommended, bilingual, standard.
- **Mobile library tables → cards** (no horizontal scroll) via CSS.
- **Guide pages:** sticky bottom action bar (Symptom · Print · Report); mobile sticky H2 TOC strip.
- **Symptom filters** sticky under mobile bar; larger chip touch targets.
- Critical path cards use stronger red semantic accent.

---

## [v1.8.0] - 2026-07-21

### 🖨️ Print pack variants
- **`print-pack-a4.html`**: compact **A4 duplex** — emergency on front, phrases on back (one sheet).
- **`print-pack-bilingual.html`**: single A4 **EN + 简体中文** emergency + phrase one-pager.
- Cross-links among Standard / A4 / Bilingual; homepage recommends A4 duplex.

### 🧪 Field re-test log
- New **`docs/00-Maintenance/field-retest-log.md`**: copy-paste trip log template + sample shape for the first real field-test PR.
- Checklist + log + registry form the full “next trip” maintenance loop.

---

## [v1.7.0] - 2026-07-21

### 🖨️ Offline Print Pack
- New **`print-pack.html`**: two-page printable emergency card + essential phrase sheet (browser Print / Save PDF).
- Guide wrapper: `docs/print-pack.md` with usage notes.
- Linked from homepage path cards, sidebars, README, docs library.

### 📐 Contributor quality
- **Phrase style guide:** `docs/00-Maintenance/phrase-style-guide.md` (one card per scene, shared HTML component, dedup rules).
- CONTRIBUTING updated for phrases + field-test expectations.

### 🧪 Field re-test readiness
- **Field re-test checklist:** `docs/00-Maintenance/field-retest-checklist.md` for payments, eSIM/VPN, power banks, visa, holidays, formula.
- High-churn registry points maintainers at the checklist for true `validation_method: field_test` bumps.

---

## [v1.6.0] - 2026-07-21

### 🗣️ Phrase cards everywhere that needed them
- Injected Chinese / pinyin / English cards into **27** additional SOPs (payments, SIM, visa, trains, lost items, safety, parenting, holidays, etc.).
- Library coverage: essentially all traveler-facing guides now include at least one phrase card.

### 🔎 Symptom Index filters
- Tag chips (Payment, Phone, Arrival, Transport, Health, Food, Kids, Holidays) with show/hide sections.
- CSS + JS in `chinaops.css` / `chinaops.js` (`aria-pressed`, live count text).

### ⏱️ High-churn desktop re-check
- **Holiday guide:** fixed outdated Labor Day “this week” copy; next peaks Mid-Autumn + National Day Golden Week.
- **Visa:** clarify list is illustrative; always re-check NIA.
- **Power banks:** domestic vs international enforcement note refreshed.
- Registry log expanded in `docs/00-Maintenance/high-churn-registry.md`.

### 🛠️ Tooling
- `scripts/apply_v16_phrases.py`

---

## [v1.5.0] - 2026-07-21

### ✍️ Plain English on every SOP
- All **38 guides** now open with a `.plain-summary` block (short sentences, ESL-friendly).
- Frontmatter **`scope: national | shanghai`** on every SOP.

### 🗣️ Phrase cards (high-value scenes)
Added Chinese / pinyin / English cards for:
- Hotel reservation, pharmacy fever meds, toilet ask
- Taxi meter, vegetarian order, food allergy, nursing room
- Ambulance call, emergency department
- Food “no cilantro” (Shanghai dining)

### 🗺️ Regional honesty
- Category hubs label **Shanghai-first** vs national content.
- Shanghai-specific guides badge: “Other cities may differ”.

### 🛠️ Tooling
- `scripts/apply_v15_content.py` for bulk Plain English + scope + phrase injection.

---

## [v1.4.0] - 2026-07-21

### 🔎 Find guides by symptom
- New **[Symptom Index](docs/symptom-index.md)**: payment, connectivity, transport, health, kids, holidays → correct SOP.
- Linked from homepage path cards, docs library, and sidebar navigation.

### ⏱️ High-churn content governance
- New **[High-Churn Registry](docs/00-Maintenance/high-churn-registry.md)** with 30-day re-check rules.
- Marked 6 critical guides `churn: high` + `ttl_days: 30`: VPN/payments, Alipay foreigners, visa/entry, power banks, holidays, milk recall.
- `ttl_check.py` reports `[HIGH]` items and counts high-churn due within 7 days.

### 📋 Contribution quality gates
- Restored **[TEMPLATE_ENHANCED_SOP.md](TEMPLATE_ENHANCED_SOP.md)** (Plain English, Action/Verify/Fallback, glossary, scope).
- **CONTRIBUTING.md** PR checklist: metadata, `index.json`, symptom links, local scripts.
- New **`scripts/check_catalog.py`**: fails if disk SOPs and `index.json` drift.
- CI workflow now runs TTL + catalog + link verification.

### ✍️ ESL content samples
- Plain English summary blocks on Landing Protocol, VPN/Payments, Lost Passport.
- System Setup hub fixed to list **10 guides** (added Alipay foreigners) + symptom link.

---

## [v1.3.1] - 2026-07-21

### 🎨 Design system & ESL readability
- **Shared tokens:** added `assets/css/chinaops.css` (foreground/background/border/brand/semantic tokens, callouts, path cards, phrase/term components).
- **No Google Fonts:** system UI stack for reliability inside China; honors `prefers-reduced-motion`.
- **Plain-English labels:** category dual labels (e.g. Daily Runtime → *Day-to-day life*) on home paths, sidebar, and docs index.
- **Static “What’s new”:** replaced dense marquee-style update banner with a scannable list.
- **Mobile nav:** hamburger + drawer for guide/default layouts (sidebar no longer disappears without alternative).
- **Home rebuild:** `index.html` uses the shared stylesheet and clearer first-visit copy.

### 🔧 Data health
- **Missing SOP metadata fixed** on 4 guides: Alipay/WeChat foreigners, lost passport, network outage, milk recall.
- **TTL refresh:** `last_validated` bumped to 2026-07-21 across all 38 SOPs (desktop/link maintenance pass).
- **`ttl_check.py`:** skips `index.md` hubs; exits non-zero on expired *or* missing metadata (CI-safe).
- **`index.json`:** `lastUpdated` → 2026-07-21.
- **Nav completeness:** Alipay & WeChat Pay guide added to guide/default sidebars.
- **Milk recall status note** refreshed for July 2026 + SafeFeed link.

### 🛠️ Tooling
- `scripts/refresh_sop_metadata.py` — metadata maintenance helper.
- `scripts/rebuild_index_html.py` — regenerates home page shell while preserving library tables.

---

## [v1.3] - 2026-07-14

### 🔧 July 2026 Freshness Audit & Critical Updates

**Scope:** Project-wide update targeting recent regulatory changes, real-world payment realities, eSIM updates, and parenting-specific transit tips.

#### 🚨 P1 Critical Updates
- **Power Bank CCC & Traceability Rules:** Documented the new domestic flight requirements (effective March 1, 2026) regarding compulsory CCC marks and scannable traceability QR codes. Added terminal replacement details.
- **Payment Verification & Account Ban Risks:** Documented mid-trip identity re-verification challenges (passport/video verification), WeChat Account lock sensitivity to SIM card switching, and random risk control declinatures on international cards. Added Payment Recovery SOP.
- **UK/Canada Visa-Free Check:** Re-verified UK & Canada 30-day visa-free entry pilot program parameters.
- **Border Kiosk Fallbacks:** Added instructions for using paper fallback cards in case of digital arrival card kiosk queues or system offline failures.

#### 📶 Connectivity & Navigation Updates
- **July 2026 eSIM Comparison Table:** Added comparative matrix of Trip.com, Holafly, Simify, and Nomad eSIM options outlining cost, speeds, bypass capability, and hotspot functionality.

#### 🍼 Parenting Patch Updates
- **High-Speed Rail Free Ticket Policy:** Documented the under-6 seat sharing rule vs. booking separate child tickets.
- **Stroller vs Carrier Transit Decision Matrix:** Added comparison guide for station transit, highlighting accessibility bottlenecks (stairs/no lifts).
- **Didi Child Seat Warnings:** Advised on child seat absence in Didi rides and mall playground alternatives.

#### 🛠️ Helper Tools
- **New Digital Entry Formatter Script:** Created `scripts/digital_entry_formatter.py` to format arrival card inputs correctly.
- **Home Page Tool Integration:** Fully integrated tool links, version tags, and badges on `index.html` to reflect v1.3.

---

## [v1.2] - 2026-04-27

### 🔧 April 2026 Freshness Audit

**Scope:** Project-wide date validation, link integrity check, and discovery of uncatalogued content.

#### 🚨 P1 Critical Fixes
- **Corrected 2026 Labor Day dates:** Fixed error in `holiday-survival-guide.md` (official dates: May 1–5, make-up workday: May 9).
- **Updated Visa-free Policy:** Confirmed UK and Canada added to the 30-day visa-free list (effective Feb 17, 2026). Expanded country list to 50+.
- **Fixed Payment Limits:** Corrected Alipay per-transaction limit from ¥5,000 to $5,000 USD for verified users.

#### 📄 Discovery & Indexing
- **Recovered 9 "Lost" Guides:** Identified 9 fully-written guides that were missing from `index.json`.
  - *System Setup:* Hotel Check-in, Landing Protocol, Translation Tools.
  - *Daily Runtime:* Car Rental, Transit Protocol, Lost Luggage.
  - *Emergency/DR:* Lost Bank Card, Lost Phone, Prescription Refill.
- **index.json:** Expanded from 22 → 31 documents catalogued.

#### 🔄 Maintenance
- **TTL Reset:** Validated and bumped `last_validated` timestamps for 31 documents to April 27, 2026.
- **UI Update:** Updated homepage announcement and version badges to v1.2.

---

## [v1.1] - 2026-03-24

### 🔧 March 2026 Content Audit & Fixes

**Scope:** Content integrity audit identified 5 critical errors, 10 items requiring updates, 7 stub documents, and 12 uncatalogued files.

#### 🚨 P1 Critical Fixes
- **Removed Mothercare** from diapers guide — brand went bankrupt globally in 2019, all China locations closed. Replaced with Kidswant (孩子王) + BabyCare.
- **Removed Whole Foods** from food allergies guide — does not exist in mainland China. Replaced with Ole' / City'Super.
- **Fixed emergency phrase error:** `Pĭngān` was incorrectly listed as a help call. Corrected to `救命！ Jiùmìng!` / `帮帮我！ Bāng bāng wǒ!` in both safety guides.
- **Updated Nestlé recall status:** Jan 2026 event now shows "Resolved (Mar 2026)" with batch verification guidance.
- **Fixed 2026 holiday table:** CNY marked as passed; Labor Day corrected to Apr 30–May 4 (was May 1–5); added 调休 (diàoxiū) explanation.

#### 🟡 P2 Content Updates
- `visa-and-entry.md`: Removed hardcoded "46+ countries", added dynamic verification reminder.
- `vpn-esim-payment.md`: Removed absolute "Jan 2026 best VPN" claim; added "verify 1 week before departure" guidance.
- `emergency-contacts-card.md`: Added official consulate website links and verification warning.

#### 📖 Stub Document Expansions
- `lost-passport.md`: 31 lines → full SOP with police report steps, embassy contacts, document checklist.
- `network-outage.md`: 32 lines → triage decision tree, VPN protocol switching, SIM fix, offline tool table.
- `milk-recall-check.md`: 31 lines → full Nestlé recall verification SOP with 3 verification methods.

#### ✨ New Documents
- `docs/01-System-Setup/alipay-wechat-setup-foreigners.md`: Complete Alipay/WeChat Pay setup for foreign visitors.

#### 📄 index.json
- Expanded from 16 → 28 documents catalogued.
- Added `05-Event-Operations` section.
- Added `description` field to all sections.

---

## [v1.0.0] - 2026-01-23


### 🎉 Initial Release - Complete Travel Runbook

**Total Guides:** 27 comprehensive SOPs across 5 categories (expanded to 30 in v1.0.1 patch)

### ✨ New Features

#### Homepage Enhancements
- **SEO Optimization**
  - Added comprehensive meta descriptions for better search visibility
  - Implemented Open Graph tags for social media sharing (Facebook, Twitter)
  - Added keyword optimization for China travel searches
  - Enhanced page title with guide count

- **User Experience Improvements**
  - Added "How to Use This Guide" section with personalized paths for different traveler types
  - Implemented smooth scroll behavior throughout the site
  - Added floating "Back to Top" button with smooth animations
  - Created version badge (v1.0) with last updated date
  - Added "What's New in v1.0" highlight banner

- **Visual Enhancements**
  - Improved visual hierarchy with color-coded sections
  - Enhanced Pre-flight Checklist prominence
  - Better mobile responsiveness
  - Consistent gradient design language

- **Community Features**
  - Added GitHub repository links
  - Added issue reporting link
  - Included contribution call-to-action
  - Enhanced footer with community engagement prompts

#### Content Additions

**Shanghai-Specific Guides (Daily Runtime)**
1. **Shanghai Weather & AQI Guide** - Monthly weather patterns, AQI management, typhoon SOPs
2. **Shanghai Attractions: 2026 Top Nodes** - Classic and modern attractions with booking tips
3. **Shanghai Food: Benbang & Street Hacks** - Authentic local cuisine and the "Dianping Hack"
4. **Shanghai Vegetarian & Vegan Survival** - Comprehensive plant-based dining guide with verified 2026 restaurant data
5. **Shanghai Local Hacks** - Enhanced with stroller safety and local app recommendations

**Emergency Resources**
6. **Emergency Contacts Reference Card** - Printable card with critical numbers, embassy contacts, and essential phrases

**Event Operations**
7. **2026 China Holiday Survival Guide** - Consolidated guide covering all 7 major Chinese holidays (CNY, May Day, National Day, etc.)

**Parenting Resources**
8. **Baby & Toddler Survival Runbook** - Updated with global formula recall info (SafeFeed Action) and Shanghai hospital hacks

### 🔧 Improvements

#### Branding & Consistency
- Unified all author attribution to **"TechDadShanghai"**
- Replaced all "SRE" terminology with "Technical" for broader accessibility
- Standardized project origin story across all pages
- Consistent emoji usage for visual scanning

#### Navigation
- Updated all category index pages with new guides
- Fixed broken cross-reference links (removed trailing slashes)
- Enhanced sidebar navigation with Shanghai-specific guides
- Added "Vegetarian/Vegan?" quick link to homepage

#### Content Quality
- Added verification timestamps to restaurant recommendations
- Included specific prices in RMB for all recommendations
- Enhanced with 2026-specific dates and information
- Improved actionable advice with real-world examples

### 📊 Guide Count by Category

- **System Setup:** 6 guides
- **Daily Runtime:** 9 guides (5 new Shanghai-specific)
- **Emergency/DR:** 6 guides (2 new)
- **Parenting Patch:** 5 guides (1 updated)
- **Event Operations:** 1 guide (consolidated)

### 🐛 Bug Fixes
- Fixed broken internal links caused by trailing slashes in Markdown
- Corrected guide counts across all index pages
- Fixed inconsistent terminology (SRE → Technical)
- Resolved broken cross-references in Emergency Contacts Card

### 📝 Documentation
- Added comprehensive SEO meta tags
- Improved guide descriptions for clarity
- Enhanced "What You'll Learn" summaries
- Added estimated reading times for all guides

---

## [v2.0] - Planned Features

### 🚀 Coming Soon

**Content Expansion**
- Beijing-specific local hacks
- Inter-city travel guides (Shanghai ↔ Beijing, etc.)
- Advanced parenting topics (international schools, healthcare insurance)
- Seasonal packing lists integrated into weather guides

**Technical Features**
- Search functionality
- Contextual sidebar navigation (shows relevant guides based on current page)
- Print-friendly CSS for all guides
- PDF export functionality
- User feedback widget ("Was this helpful?")
- "Report Outdated Info" mechanism

**Content Enhancements**
- More printable quick reference cards (Essential Phrases, App Cheat Sheet)
- Video tutorials for complex processes (VPN setup, Alipay binding)
- Interactive maps for Shanghai attractions
- Emergency scenario flowcharts

---

## Version History

- **v1.2** (2026-04-27) - April audit: Fixed holiday dates, visa expansions, and payment limits. Recovered 9 unindexed guides (Total: 31).
- **v1.1** (2026-03-24) - March audit: 5 P1 fixes, 3 stub expansions, 1 new guide, index.json expanded to 28 docs.
- **v1.0.0** (2026-01-23) - Initial official release with 28 comprehensive guides.

---

**Maintained by:** TechDadShanghai  
**Last Updated:** April 2026
