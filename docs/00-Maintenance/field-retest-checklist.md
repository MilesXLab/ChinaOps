---
layout: guide
title: "Field Re-test Checklist (High-Churn)"
---

# Field Re-test Checklist

**Plain English:** Desktop review is not a substitute for using the systems in China. Use this checklist on your next real trip (or a trusted contributor’s trip). Only then bump `last_validated` with `validation_method: field_test`.

**When:** Before the 30-day TTL expires on high-churn SOPs (see [registry](../high-churn-registry/)).

---

## How to run a field re-test

1. Print or copy this checklist offline.
2. For each item: **do the action**, note **pass / fail / changed**, date, city, and evidence (screenshot note — do not commit secrets).
3. Update the matching SOP body if behavior changed.
4. Set frontmatter:
   ```yaml
   last_validated: YYYY-MM-DD
   validation_method: field_test
   ```
5. Log a one-line result in the [high-churn registry](../high-churn-registry/).
6. Run:
   ```bash
   python scripts/ttl_check.py
   python scripts/verify_links.py
   python scripts/check_catalog.py
   ```

---

## A. Payments (Alipay + WeChat)

| # | Action | Pass? | Notes |
|---|--------|-------|-------|
| A1 | Bind / re-verify foreign card in **Alipay** | ☐ | |
| A2 | Small purchase (&lt; ¥50) with Alipay | ☐ | |
| A3 | Bind / pay with **WeChat Pay** | ☐ | |
| A4 | Trigger or observe mid-trip KYC / selfie prompt? | ☐ | If yes, document recovery steps |
| A5 | Payment fail → switch app / second card / cash | ☐ | |
| A6 | Fee or limit message differs from SOP? | ☐ | Quote exact UI text |

**SOP:** `alipay-wechat-setup-foreigners.md`, `vpn-esim-payment.md` (payment section)

---

## B. Connectivity (eSIM / VPN / data)

| # | Action | Pass? | Notes |
|---|--------|-------|-------|
| B1 | Enable travel **eSIM** (or local SIM) on landing | ☐ | Provider: ______ |
| B2 | Load google.com / WhatsApp without extra VPN | ☐ | |
| B3 | Hotspot to a second device works? | ☐ | |
| B4 | If blocked: backup VPN connects | ☐ | App: ______ |
| B5 | Hotel Wi‑Fi fallback works for OTP email | ☐ | |

**SOP:** `vpn-esim-payment.md`, `sim-card-options.md`, `network-outage.md`

---

## C. Power banks (domestic flight or HSR security)

| # | Action | Pass? | Notes |
|---|--------|-------|-------|
| C1 | Bank has visible **capacity label** | ☐ | mAh / Wh: ______ |
| C2 | **CCC** mark present (if domestic flight) | ☐ | |
| C3 | **Traceability QR** present / scannable | ☐ | |
| C4 | Allowed through security without confiscation | ☐ | Airport: ______ |
| C5 | Shared rental bank works via Alipay | ☐ | |

**SOP:** `power-bank-rules.md`

---

## D. Visa / entry (if applicable this trip)

| # | Action | Pass? | Notes |
|---|--------|-------|-------|
| D1 | Confirmed visa-free / TWOV on NIA site pre-flight | ☐ | Passport country: ______ |
| D2 | Digital arrival card submitted; QR screenshot saved | ☐ | |
| D3 | Kiosk or paper fallback used? | ☐ | Which: ______ |
| D4 | Entry stamp / allowed stay matches expectation | ☐ | Days: ______ |

**SOP:** `visa-and-entry.md`, `landing-protocol.md`

---

## E. Holidays / peak load (if traveling near a holiday)

| # | Action | Pass? | Notes |
|---|--------|-------|-------|
| E1 | Official dates on gov.cn match our table | ☐ | Holiday: ______ |
| E2 | HSR sold out window observed? | ☐ | Book lead time: ______ |
| E3 | Shop / attraction closure surprises | ☐ | |

**SOP:** `holiday-survival-guide.md`

---

## F. Formula / milk (if traveling with infant)

| # | Action | Pass? | Notes |
|---|--------|-------|-------|
| F1 | Checked current recall notices / SafeFeed | ☐ | |
| F2 | Batch on can verified before opening | ☐ | Brand: ______ |

**SOP:** `milk-recall-check.md`

---

## Trip metadata (fill once)

| Field | Value |
|-------|--------|
| Tester | |
| Cities | |
| Dates | |
| Devices | |
| Notes for CHANGELOG | |

---

## After the trip

- [ ] PR opened with SOP diffs + this checklist summary (no secrets)
- [ ] Entry appended to [field-retest-log.md](../field-retest-log/)
- [ ] High-churn registry log line added
- [ ] Print packs still accurate (`print-pack-a4.html`, bilingual, standard)

[← High-churn registry](../high-churn-registry/)
