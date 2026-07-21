---
layout: guide
title: "Field Re-test Log"
---

# Field Re-test Log

**Plain English:** Use this file to record **real trip** results after filling the [field re-test checklist](../field-retest-checklist/). Desktop-only reviews stay in the [high-churn registry](../high-churn-registry/) — do not invent a field test.

**How to add an entry**

1. Complete the checklist offline during/after the trip.  
2. Open a PR that updates any failed SOP + appends a log block below.  
3. Set matching SOP frontmatter to `validation_method: field_test` and today’s `last_validated`.  
4. Never commit passport numbers, full card numbers, or live OTPs.

---

## Log template (copy for each trip)

```markdown
### YYYY-MM-DD — City list — Tester initials

| Area | Result | SOP impact |
|------|--------|------------|
| Payments A1–A6 | Pass / Fail / Partial | none / link PR section |
| Connectivity B1–B5 | | |
| Power bank C1–C5 | | |
| Visa/entry D1–D4 | N/A if not used | |
| Holiday E1–E3 | N/A if not peak | |
| Formula F1–F2 | N/A if no infant | |

**Devices / eSIM / apps:**  
**What changed in the real world:**  
**Follow-ups:**  
```

---

## Entries

_No field re-test entries yet. The next completed trip should add the first block above._

### Example shape only (not a real test)

```markdown
### 2026-09-01 — Shanghai — TDS

| Area | Result | SOP impact |
|------|--------|------------|
| Payments | Partial — WeChat KYC selfie mid-trip | Confirm recovery steps still match |
| Connectivity | Pass — Trip.com eSIM hotspot OK | none |
| Power bank | Pass — CCC+QR accepted PVG domestic | none |

**Devices / eSIM / apps:** iPhone 15 + Trip.com eSIM  
**What changed in the real world:** (fill)  
**Follow-ups:** (fill)  
```

> Delete the example when the first real entry is added, or keep it clearly labeled as sample.

---

## Related

- Checklist: [field-retest-checklist.md](../field-retest-checklist/)
- Registry: [high-churn-registry.md](../high-churn-registry/)
- Print offline: repo `print-pack-a4.html` / `print-pack-bilingual.html`

[← Maintenance hub](../high-churn-registry/)
