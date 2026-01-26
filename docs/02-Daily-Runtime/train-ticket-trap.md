---
layout: guide
title: "12306 Train Tickets: The MRZ Name Hack"
metadata:
  version: 1.1
  last_validated: 2026-01-26
  stability_status: "stable"
---

# 🚄 12306 Train Tickets: The MRZ Name Hack

**TL;DR:** The 12306 system only recognizes a single string from your passport. Match the **MRZ code** (bottom of passport) in **ALL CAPS**. If your name is >15 chars, truncation logic applies.

**Prerequisites:**
- **App:** 12306 (Global/English version).
- **ID:** Original Passport.
- **Time:** Register 2-3 days before travel (KYC verification latency is real).

---

## 📋 The Runbook

### 1. The Name String Protocol
- **Step 1:** Look at the bottom lines of your passport (The MRZ zone).
- **Step 2:** Enter your name in **ALL CAPS**. Use a single space where your passport has `<`.
- **Step 3 (The 15-Char Rule):** The backend often truncates at **15 characters**. If your name is long, ensure the first 15 letters match exactly; the rest is lower priority but should be included until the field stops.
- **Verification:** Status must change from "Verifying" to "Verified" (typically 24h).

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
