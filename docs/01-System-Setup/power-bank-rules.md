---
layout: guide
title: "Power Bank & Hardware Rules"
description: "Practical ChinaOps guide: Power Bank & Hardware Rules. Step-by-step checks, fallbacks, and field tips."
metadata:
  version: 1.2
  last_validated: 2026-07-21
  ttl_days: 30
  churn: "high"
  stability_status: "critical"
  validation_method: "desktop_review"
  scope: "national"
---

# 🔋 Power Bank & Hardware Rules

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>Power banks go in carry-on, not checked bags. Domestic flights may require CCC marks and a scannable traceability code.</p>
  <p>If security rejects your bank, buy a compliant one after security or in the city — do not force the old one through.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">充电宝可以带上飞机吗？</div>
  <div class="py">chōngdiàn bǎo kěyǐ dài shàng fēijī ma?</div>
  <div class="en">Can I take this power bank on the plane?</div>
</div>


**TL;DR:** Max capacity **20,000mAh (100Wh)**. Labeling must be clearly visible. **Must be in carry-on.** From **March 1, 2026**, domestic flights strictly require a **CCC logo** and a **scannable QR traceability code** on the device. Non-compliant units are confiscated. Never let your phone hit 0% or you can't rent a shared bank.

**Prerequisites:**
- **Power Bank:** Brand-name (Anker/Xiaomi) with spec label intact.
- **CCC & QR Compliance:** Must feature the CCC mark + QR traceability code for domestic aviation.
- **Carry-on Bag:** Power banks are banned from checked luggage.

---

## 📋 The Runbook

### 1. The Capacity & Certification Audit (Pre-Flight)
- **Step 1:** Check the label on your power bank. If it says >100Wh or >27,000mAh (some airports use 100Wh as the hard limit), it will be confiscated.
- **Step 2:** If the label is worn out or scratched, replace the bank. Security will not "guess" the capacity.
- **Step 3 (Critical 2026 Rule):** Ensure the device has the **CCC (China Compulsory Certification) logo** AND a **traceability QR code** printed/engraved on it.
  > [!IMPORTANT]
  > **CCC & QR Enforcement (Since March 1, 2026):** All power banks carried onto **China domestic flights** must have a valid CCC logo and a QR code that links to verification data. International inbound segments can be more lenient, but **domestic legs** (e.g., PVG → PEK) enforce this aggressively. Non-compliant banks are confiscated.
  >
  > **Desktop re-check (Jul 21, 2026):** Rule still treated as in force for domestic aviation planning. Prefer buying a clearly labeled Anker/Xiaomi/Huawei unit in-city if your imported bank lacks CCC+QR.
- **Verification:** Ensure both the "CCC" (3C) logo and the QR code are clearly legible before packing.

### 2. High-Speed Rail (HSR) Protocol
- **Step 1:** Be ready to pull the bank out at the station X-ray machine.
- **Step 2:** Locate the power outlet under your seat (Standard and First Class have them).
- **Verification:** Confirm the green LED on the outlet is lit before plugging in.

### 3. Shared Power Bank Rental (The Recovery Hack)
- **Step 1:** Open Alipay or Meituan. Search `充电宝` (Power bank).
- **Step 2:** Scan the QR code on the machine (Meituan, Jiedian, or Energy Monster).
- **Verification:** The bank should pop out automatically.
- **Critical Alert:** You need at least 1-2% battery to perform this action. If your phone is dead, you're locked out of the shared economy.

---

## 🚨 Fallback (Plan B)

### If your power bank is confiscated at security:
1. **Airport Retail:** Go to a **Xiaomi (Mi)** or **Huawei** store inside the airport terminal. They sell fully-compliant, CCC-certified models with scannable QR codes for ~150 RMB (~$21 USD).
2. **Charging Poles:** Look for physical charging stations near the boarding gates. Note: These often require a USB-A cable; USB-C ports are less common in older terminals.
3. **Emergency Charge:** Ask the staff at a high-end cafe (Starbucks/Costa) if they have a "USB hub." Some will allow you to plug in for 10 mins if you buy a drink.

---

## 💡 TechDad's Tips

- **The Umbrella Patch:** Shanghai weather is erratic. Buy a small, manual foldable umbrella. Automatic ones are heavy and often break after one typhoon gust.
- **Type-C is Dominant:** While China used to be micro-USB heavy, everything in 2026 is Type-C. Ensure your "Go-bag" has at least two Type-C cables.
- **Don't Buy "Street" Banks:** Avoid buying power banks from non-branded kiosks or street vendors. They often have fake capacity labels and will be rejected at the airport next time you fly.

---

## 🚩 Strategic Gap: The "SPOF" Warning
**Single Point of Failure:** Relying on a single USB cable.
- **Hotfix:** Keep a spare charging cable in your jacket pocket, separate from your main gear bag.

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
