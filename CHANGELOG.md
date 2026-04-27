# ChinaOps Changelog

All notable changes to the ChinaOps project will be documented in this file.

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

- **v1.1** (2026-03-24) - March audit: 5 P1 fixes, 3 stub expansions, 1 new guide, index.json expanded to 28 docs.
- **v1.0.0** (2026-01-23) - Initial official release with 28 comprehensive guides.

---

**Maintained by:** TechDadShanghai  
**Last Updated:** March 2026
