---
layout: guide
title: "12306 Train Tickets: The MRZ Name Hack"
description: "Register on 12306 with passport MRZ-style name (SURNAME<<GIVEN), pass real-name check, then book — with Trip.com fallback."
metadata:
  version: 1.2
  last_validated: 2026-07-21
  ttl_days: 90
  stability_status: "stable"
  validation_method: "desktop_review"
  scope: "national"
---

# 🚄 12306 Train Tickets: The MRZ Name Hack

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>12306 needs your name in MRZ-style format. Register early, pass real-name checks, then book in the open window.</p>
  <p>Prefer the browser <a href="../../../mrz-tool.html">MRZ name tool</a> (same rules as <code>passport_mrz_converter.py</code>). Do not mix formats on repeated submissions.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">我要买高铁票</div>
  <div class="py">wǒ yào mǎi gāotiě piào</div>
  <div class="en">I want to buy a high-speed train ticket.</div>
</div>


**TL;DR:** Build the name as **`SURNAME<<GIVENNAMES`** (ALL CAPS) with the [MRZ tool](../../../mrz-tool.html). Register **2–3 days** before travel. Use the **manual passport lane** at the station.

**Prerequisites:**
- **App:** 12306 (Global/English version) and/or Trip.com as backup booking path.
- **ID:** Original Passport.
- **Time:** Register 2-3 days before travel (KYC verification latency is real).

---

## 📋 The Runbook

### 1. The Name String Protocol (single source of truth)

**Canonical format (use this first):**

1. Open **[mrz-tool.html](../../../mrz-tool.html)** (or `python scripts/passport_mrz_converter.py Given Surname`).
2. Enter **given name(s)** and **surname** as on the passport.
3. Copy the result: **`SURNAME<<GIVENNAMES`** — uppercase ASCII, accents stripped, hyphens/spaces inside names removed (e.g. `Mary-Jane` → `MARYJANE`, `José` → `JOSE`).
4. In 12306:
   - If there is a **single full-name** field → paste the tool output as-is.
   - If the UI splits **Surname / Given name** → fill the two boxes from your passport; do **not** also paste `<<` into both boxes.
5. **Long names:** some backends effectively care most about the first ~15 letters of the surname+given block. Include the full legal string until the field stops accepting input; do not invent a shortened legal name.

**Do not mix formats:** pick tool output **or** the split fields for one registration attempt. Resubmitting alternating `SMITH<<JOHN` and `SMITH JOHN` can prolong “Verifying” failures.

**Verification:** Status must change from "Verifying" to "Verified" (often ~24h).

### 2. The Boarding Procedure
- **Step 1:** Use your Passport at the gate. **Do not use the automated e-gates** with a foreign passport; they fail 50% of the time.
- **Step 2:** Head straight to the **Manual Lane** (far left or right).
- **Verification:** The staff will scan your passport on a handheld device. It should beep "Success."

---

## 🚨 Fallback (Plan B)

### If 12306 hangs or rejects payment:
1. **Trip.com:** Their international payment gateway is 10x more stable. Pay the $2 fee for the sanity of a verified booking.
2. **"Verify at Station":** If the app says "Manual Verification Required," you **must** go to a physical ticket window with your passport before you can buy online.
3. **The Electronic ID Hack:** If you lose your physical passport, go to the station police office for a "Temporary Travel Document." It takes 15 minutes and allows you to travel for 24h.

---

## 💡 TechDad's Tips

- **Stroller Strategy:** If traveling with kids, the **Manual Lane** is your "Priority Lane." Staff will wave you through the wide gate without you even asking.
- **Sterilization Station:** Every G-train carriage has 100°C boiling water. Perfect for formula or instant coffee.
- **Row Zero:** In Second Class, always aim for the **Last Row** of the carriage. There is a massive gap behind the seats for strollers or oversized luggage.

---

## 🚩 Strategic Gap: The "SPOF" Warning
**Single Point of Failure:** Relying on the 12306 automated gates.
- **Hotfix:** Always allot an extra 20 minutes for the Manual Lane queue. One person in front of you with a passport issue can block the line for minutes.

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
