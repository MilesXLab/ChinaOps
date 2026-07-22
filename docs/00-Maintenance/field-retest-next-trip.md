---
layout: guide
title: "Next Trip Field-Test Pack"
description: "Ready-to-run pack for the next real China trip: what to test, which SOPs to update, and how to log results without inventing field tests."
metadata:
  version: 1.0
  last_validated: 2026-07-21
  ttl_days: 90
  stability_status: "stable"
  validation_method: "desktop_review"
  scope: "national"
---

# 🧪 Next Trip Field-Test Pack

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>ChinaOps still needs at least one honest real-trip pass. Use this pack so the next journey updates high-churn guides instead of only desktop guesses.</p>
  <p>Do not mark <code>validation_method: field_test</code> unless you actually did the step.</p>
  <p><span class="scope-badge">Scope: national · maintainer</span></p>
</div>

**TL;DR:** Print [field-retest-checklist](../field-retest-checklist/) → run gates on trip → append [field-retest-log](../field-retest-log/) → PR with SOP fixes + `last_validated`.

---

## 📋 Pre-trip (T−7)

| Pack | Why |
|:---|:---|
| [Pre-flight checklist](../../../preflight-checklist.html) | User-facing gate |
| [Print hub](../../../print-hub.html) | Offline numbers |
| [High-churn registry](../high-churn-registry/) | Know what must be re-touched |
| [Money Runtime](../../01-System-Setup/money-runtime/) | ATM plan |
| [App stack](../../01-System-Setup/china-app-stack/) | Two VPNs installed |
| [MRZ tool](../../../mrz-tool.html) | Train name ready |

**Carry offline:** passport photo page, hotel Chinese address, insurance assist number, this checklist PDF/print.

---

## 📋 On-trip gates (map to high-churn)

| Gate | Minimum proof | Primary SOP |
|:---|:---|:---|
| **A Payments** | Foreign card Alipay success + one decline recovery | alipay / vpn-payment / money-runtime |
| **B Connectivity** | eSIM or local data + VPN 60s international site | vpn-esim / network-outage |
| **C Power bank** | Domestic flight or security interaction if any | power-bank-rules |
| **D Entry** | Digital card / stamp path as used | visa-and-entry / landing-protocol |
| **E Holiday** | Only if peak week | holiday-survival |
| **F Formula** | Only if infant tin purchased | milk-recall-check |
| **G Stay** | Passport registration completed | hotel / stay-beyond-hotel |
| **H Apps** | No accidental WeChat logout; SIM stable | china-app-stack |

---

## 📋 After trip (≤7 days)

1. Fill log entry in [field-retest-log](../field-retest-log/) (Pass / Fail / Partial / N/A).  
2. For each Fail/Partial: patch SOP body with what actually happened.  
3. Set `validation_method: field_test` and `last_validated: YYYY-MM-DD` **only** on guides you truly exercised.  
4. Desktop-only re-reads stay `desktop_review`.  
5. Run:

```bash
python scripts/ttl_check.py
python scripts/check_catalog.py
python scripts/check_sop_format.py
python scripts/verify_links.py
npm run build:search
```

6. PR title suggestion: `field-test: YYYY-MM city list — payment/connectivity notes`

---

## Privacy

Never commit: full passport numbers, card PANs, OTPs, live hotel booking codes tied to real names beyond what you accept as public.

---

## Related

- [Field re-test checklist](../field-retest-checklist/)
- [Field re-test log](../field-retest-log/)
- [Phrase style guide](../phrase-style-guide/)

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Maintenance](../high-churn-registry/)
