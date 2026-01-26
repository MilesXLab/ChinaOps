---
layout: guide
title: "12306 Train Tickets: The MRZ Name Hack"
metadata:
  version: 2.0
  last_validated: 2026-01-26
  ttl_days: 180
  stability_status: "stable"
  validation_method: "field_test"
---

![v1.1.0 Verified](https://img.shields.io/badge/v1.1.0-Verified-brightgreen)

# 12306 Train Tickets: The MRZ Name Hack

**Last Updated:** Jan 2026 | **Author:** TechDadShanghai

### 🚨 Failover Procedure (If 12306 App Rejects You)
1.  **Fallback to Trip.com:** Their backend is more robust for foreign cards. If the official 12306 app hangs during payment, Trip.com is the #1 alternative.
2.  **The "Pink Paper" Ticket:** If your passport won't scan at the gate, go to the **Manual Verification** booth (usually at the far right or left). Show your passport and the booking ID (starts with E) from your app.
3.  **Physical Ticket Window:** If all apps fail, go to the railway station. **Bring your physical passport.** Look for the "English Speaking" or "Ticket Refund/Change" window.

### Problem
Foreign tourists often face "Identity Verification Failed" errors on the 12306 app, even when they think they've entered their names correctly.

---

## The "Single String" Logic (Crucial)

The 12306 backend does not distinguish between "First," "Middle," and "Last" names the same way Western systems do. It checks a single consolidated string.

### The Fix: Match the MRZ Code
The system cares about only one thing: **The string of letters must exactly match the MRZ code** (the two lines of text at the very bottom of your passport photo page).
1.  Use **ALL CAPS**.
2.  Include **every space** exactly as it appears in those two lines.
3.  If your name is long and has symbols like `<<`, ignore the symbols but keep the letter sequence.

### Verification Latency
- **New Accounts:** Identity verification for foreign passports can take up to **24 hours**. 
- **Recommendation:** Register your account at least 2 days before you actually need to buy a ticket.

---

## The "Green Channel" for Parents

If you are traveling with a stroller or young children:
- **Avoid Automated Gates:** Do not even try the e-gates. They are notoriously slow at scanning foreign passports and often fail with multiple family members.
- **Manual Lane:** Look for the **"Manual Lane"** or **"Green Channel"** on the far ends of the ticket gate row. Staff are highly trained to prioritize parents with strollers; they will scan your passport manually and wave you through.

---

## TechDad's Tips (High-Speed Rail Realities)

- **Security Gate Fluid Limits:** Security scanners are strict about liquids. If you have "unsealed" water, they might ask you to take a sip to prove it's safe.
- **12306 Character Limit:** The app has a weird limit on name length. If your name is very long, it might be cut off. **Priority: Ensure the first 15 letters match your passport exactly.**
- **Seat Selection (Strollers):**
  - **First Class:** Highly recommended for families. The massive legroom allowing you to keep a stroller unfolded for a nap is worth the premium.
  - **Second Class:** Aim for the **First or Last row** of the carriage. There is usually extra space behind the seats or in front for bulky items.
- **Hot Water Nodes:** Every high-speed carriage has a hot water dispenser. It is boiling (100°C), making it perfect for sterilizing bottles or mixing formula on the go.

### Local Hacks / Money-saving Tips
- **Trip.com Failover:** If the 12306 app's payment gateway hangs (common with foreign cards), use **Trip.com**. Their small commission is a "service fee" for a much higher success rate and English support.
- **Waitlist API:** If a train is "Sold Out," use the **"Waitlist"** (hòubǔ) feature in the app. It is surprisingly efficient at clearing as people cancel.
