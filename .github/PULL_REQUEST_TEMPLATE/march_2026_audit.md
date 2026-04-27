# [Content] March 2026 Audit: Critical Fixes, Stub Expansions & v1.1 Update

## Summary

This PR is the result of a systematic content audit conducted in March 2026. It addresses **5 confirmed factual errors**, **10 content updates**, **3 stub document expansions**, and **1 new guide** — plus a full `index.json` rebuild and version bump to **v1.1**.

> **Branch:** `content/march-2026-audit-fixes`  
> **Base:** `main`  
> **Commits:** 2  
> **Files changed:** 18 | +558 / -120

---

## 🚨 P1 — Critical Errors Fixed (Confirmed Wrong Facts)

These were not opinions or outdated preferences — they were **objectively incorrect** and could cause real harm or wasted effort for travelers.

### 1. Mothercare removed from `diapers-and-stores.md`
- **Problem:** Mothercare was listed as a recommended store. The brand entered bankruptcy in 2019 and **all China mainland stores are closed**.
- **Fix:** Replaced with **Kidswant (孩子王)** (China's largest dedicated baby chain) and **BabyCare** (popular WeChat + physical presence brand).

### 2. Whole Foods removed from `food-allergies-and-dietary-restrictions.md`
- **Problem:** Whole Foods was listed as a grocery option. **Whole Foods has no stores in mainland China.**
- **Fix:** Replaced with **Ole'** and **City'Super** — both are actually accessible in Shanghai's premium malls (IFC, Jing'an Kerry Centre, etc.).

### 3. Emergency phrase `Pǐngān` corrected in both safety guides
- **Problem:** Both `safety-and-common-scams.md` and `shanghai-safety-guide.md` instructed travelers to say `"Pǐngān"` (平安) to call for help. This word means "peace/safety" — it is **not a help signal** and would confuse bystanders.
- **Fix:** Replaced with the correct emergency phrases: `救命！(Jiùmìng! = Help!)` and `帮帮我！(Bāng bāng wǒ! = Help me!)` in both files.

### 4. Nestlé recall status updated in `baby-survival-master-runbook.md`
- **Problem:** The Jan 2026 recall warning used alarming present-tense language ("DO NOT FEED") without acknowledging that by March 2026, the affected batches have been identified and withdrawn from major retailers.
- **Fix:** Updated to "Resolved (Mar 2026)" status with targeted guidance: check existing stock against the batch list, link to official recall page, and recommend Aptamil/Friso as alternatives.

### 5. 2026 holiday dates corrected in `holiday-survival-guide.md`
- **Problem:** (a) CNY (Feb 15–23) was shown without a "passed" indicator. (b) Labor Day was listed as May 1–5 — the **actual 2026 dates are Apr 30–May 4**. (c) No mention of 调休 (diàoxiū) make-up work days.
- **Fix:** CNY and New Year's marked as ✅ passed. Labor Day corrected. All remaining holidays marked with 🗓️. Diàoxiū explanation added. Official [gov.cn](https://www.gov.cn) reference linked.

---

## 🟡 P2 — Content Updates

| File | Change |
|:---|:---|
| `visa-and-entry.md` | Removed hardcoded "46+ countries" figure; replaced with dynamic official link + "verify 2 weeks before travel" warning |
| `vpn-esim-payment.md` | Removed absolute "Jan 2026 best VPN" claim; added note to verify on expat communities 1 week before departure |
| `emergency-contacts-card.md` | Added official consulate website links to embassy table; added `[!WARNING]` block reminding users to verify phone numbers before travel |
| `food-allergies-and-dietary-restrictions.md` | Updated allergy app FAQ: acknowledged no dedicated Chinese restaurant allergy app exists; added Yuka for packaged food scanning |

---

## 📖 Stub Document Expansions

Three documents existed as near-empty placeholders (< 35 lines each). They have been fully rewritten as proper SOPs.

### `lost-passport.md` — 31 lines → ~110 lines
**New content includes:**
- Immediate 30-minute response checklist (search → Didi lost item → police report)
- Police report SOP with Chinese phrase to use at 派出所
- Embassy contacts table (with official website links)
- Emergency Travel Document vs Emergency Passport comparison table
- Required documents checklist for embassy visit
- Hotel/flight/train instructions during document limbo
- Pre-trip prevention checklist

### `network-outage.md` — 32 lines → ~130 lines
**New content includes:**
- Root cause table (VPN blocked / GFW pattern / data exhausted / hotel port blocking / SIM issue)
- Triage decision tree (ASCII flowchart)
- VPN fix: protocol switching guide (ExpressVPN, LetsVPN, Astrill — per-app instructions)
- SIM fix: APN settings, top-up via WeChat, eSIM failover steps
- Offline survival mode: tool table (Google Maps offline, Amap, Pleco, WeChat, Alipay QR screenshot)

### `milk-recall-check.md` — 31 lines → ~115 lines
**New content includes:**
- Nestlé 2026 recall current status ("Resolved Mar 2026") with batch table
- 3-step batch verification: (A) Nestlé official page, (B) SAMR China database, (C) WeChat QR on can
- Photo documentation workflow
- Safe alternative brands table (Aptamil, Friso, Similac, Enfamil) with availability by store
- Refund process for recalled cans (in-store and online)
- Pre-trip checklist

---

## ✨ New Document

### `docs/01-System-Setup/alipay-wechat-setup-foreigners.md` (120 lines)

**Why:** The existing `vpn-esim-payment.md` had only 3 lines on payments. Payment is the #1 friction point for foreign visitors, and both apps now have dedicated international flows. This guide fills a clear gap.

**Contents:**
- Part 1: Alipay International — register with foreign number, bind Visa/Mastercard, test before flying, common error table (4 errors + fixes)
- Part 2: WeChat Pay — WeChat account registration workaround (friend verification), card binding
- Metro & bike QR usage
- Offline QR screenshot (zero-data fallback) with safety warning
- Tips: bind before landing, cash buffer strategy, app coupons

---

## 📄 `index.json` Rebuilt

The previous `index.json` catalogued only 16 documents. The filesystem contained 25+.

| Before | After |
|:---|:---|
| 16 documents | 28 documents |
| 4 sections | 5 sections (added `05-Event-Operations`) |
| No section descriptions | `description` field on all sections |
| All of `02-Daily-Runtime` Shanghai guides missing | All 7 Shanghai guides now included |
| `05-Event-Operations` not in index | `holiday-survival-guide.md` now catalogued |

---

## 🏷️ Version Bump: v1.0.0 → v1.1

Updated in `index.html`, `README.md`, `CHANGELOG.md`, and `ROADMAP.md`:

- Version badge: `v1.0.0 | Jan 23, 2026` → `v1.1 | Mar 24, 2026`
- Homepage announcement banner: "v1.0 is Live" → March 2026 update summary with link to new Alipay guide
- Pre-flight checklist warning: "CNY starts Feb 16" → "Next: Qingming Apr 4–6, Labor Day Apr 30–May 4"
- System Setup count: 6 → 7 guides
- Footer date updated
- `CHANGELOG.md`: full `[v1.1]` entry added
- `ROADMAP.md`: v1.1 completed items added

---

## Testing Checklist

- [x] All modified Markdown files render without broken frontmatter
- [x] `index.json` paths validated against actual filesystem structure
- [x] Cross-reference links in new documents point to existing files
- [x] No links to Mothercare, Whole Foods, or `Pǐngān` remaining
- [x] `index.html` guide count (7) matches actual System Setup file count
- [ ] GitHub Pages render test (post-merge)

---

## Reviewer Notes

- The **Pǐngān emergency phrase fix** is the highest-risk correction — it was in two separate files and could have resulted in a traveler calling for help with an inappropriate word. Worth double-checking both files.
- The **Nestlé recall update** deliberately avoids saying the recall is "over" — it says batches have been withdrawn from major retailers, but instructs users to still check existing stock. This is the appropriate cautious framing.
- The `index.json` rebuild adds a `description` field to sections — if any frontend code parses `index.json` and doesn't expect this field, it should be checked for compatibility (current `index.html` does not read `index.json` directly).
