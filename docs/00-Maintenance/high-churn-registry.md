---
layout: guide
title: "High-Churn Content Registry"
---

# High-Churn Content Registry

**Purpose:** Some ChinaOps guides go stale faster than others. Wrong advice here can strand travelers mid-trip.

**Rule:** Files on this list use `churn: high` and **`ttl_days: 30`**. Re-validate before the TTL expires. Do **not** bump `last_validated` unless you actually re-checked the claims.

**Last registry review:** 2026-07-21 (v1.6 desktop re-check)

---

## Latest re-check log (Jul 21, 2026)

| Guide | Method | Result |
|-------|--------|--------|
| Holiday Survival | Desktop review of calendar language | **Fixed:** removed stale “Labor Day starts this week”; upcoming peaks → Mid-Autumn Sep 25–27, National Day Oct 1–7 |
| Visa & Entry | Desktop review | Kept UK/Canada + 50+ framing; stressed NIA live list over static roster |
| Power Bank | Desktop review | Domestic CCC+QR still treated as required; clarified domestic vs international legs |
| VPN / eSIM / Payment | Desktop review | Structure kept; `validation_method` set to desktop_review (no new field test this pass) |
| Alipay foreigners | Desktop review | Flow still valid as described; no structural rewrite |
| Milk recall | Desktop review | July “resolved but still verify” status retained + SafeFeed link |

**Honesty rule:** this pass is **desktop_review**, not a fresh airport field test. Bump `last_validated` only when the watch items above were actually re-read.

---

## Why these topics churn

| Topic | Why it changes often |
|-------|----------------------|
| Payments | Bank risk control, app KYC, fee rules, foreign-card limits |
| Visa / entry | Pilot visa-free lists, digital arrival card UX |
| Power banks | Airline / CAAC rules (CCC, QR traceability) |
| Holidays | Official holiday calendars + make-up workdays |
| Formula recalls | Batch lists and “resolved” status can shift |
| Connectivity | eSIM products, VPN blocks, carrier promos |

---

## High-churn SOPs (must re-check every ~30 days)

| Guide | Path | Watch items |
|-------|------|-------------|
| VPN, eSIM & Payment | [vpn-esim-payment.md](../../01-System-Setup/vpn-esim-payment/) | eSIM matrix, VPN names, payment recovery |
| Alipay & WeChat (foreigners) | [alipay-wechat-setup-foreigners.md](../../01-System-Setup/alipay-wechat-setup-foreigners/) | Card bind flow, limits, error messages |
| Visa & Entry | [visa-and-entry.md](../../01-System-Setup/visa-and-entry/) | Visa-free country list, digital card steps |
| Power Bank Rules | [power-bank-rules.md](../../01-System-Setup/power-bank-rules/) | CCC / QR / airline cabin rules |
| Holiday Survival | [holiday-survival-guide.md](../../05-Event-Operations/holiday-survival-guide/) | Official dates, make-up workdays, HSR load |
| Formula / milk recall | [milk-recall-check.md](../../04-Parenting-Patch/milk-recall-check/) | Active recalls, SafeFeed / brand notices |
| Money Runtime | [money-runtime.md](../../01-System-Setup/money-runtime/) | ATM fees, pre-auth habits, fapiao flows |

**Field-test pack:** [next-trip field-test](../field-retest-next-trip/) · [checklist](../field-retest-checklist/) · [log](../field-retest-log/)

---

## Medium-churn (default `ttl_days: 90`)

Everything else: hospitals, scams, food guides, maps, parenting supplies (non-recall), etc.

Shorten TTL only when a contributor finds the topic changing quarterly or faster.

---

## Maintainer checklist (monthly)

1. Run `python scripts/ttl_check.py` — fix any EXPIRED / MISSING.
2. Open each high-churn guide; re-read **limits, dates, product names, legal rules**.
3. Prefer a real trip pass using the [field re-test checklist](../field-retest-checklist/).
4. Update body text if needed, then set `last_validated` to today.
5. Note the change in `CHANGELOG.md` if user-facing.
6. Run `python scripts/verify_links.py` and `python scripts/check_catalog.py`.
7. Skim repo-root `print-pack.html` numbers still match emergency guides.

---

## Frontmatter convention

```yaml
metadata:
  version: 1.x
  last_validated: YYYY-MM-DD
  ttl_days: 30
  churn: high
  stability_status: critical
  validation_method: field_test | desktop_review | official_source
```

- `churn: high` — appears in TTL audit as `[HIGH]`.
- Never set `last_validated` without a real check of the watch items above.

[← Back to Guide Library](../../)
