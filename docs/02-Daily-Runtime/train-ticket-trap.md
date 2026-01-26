---
layout: guide
title: "12306 Train Tickets: The MRZ Name Hack"
---

# 12306 Train Tickets: The MRZ Name Hack

**Last Updated:** Jan 2026 | **Author:** TechDadShanghai

---

## Problem
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

## TechDad's Tips (Technical HSR Hacks)

- **Seat Selection (Strollers):**
  - **First Class:** Highly recommended for families. The massive legroom allowing you to keep a stroller unfolded for a nap is worth the premium.
  - **Second Class:** Aim for the **First or Last row** of the carriage. There is usually extra space behind the seats or in front for bulky items.
- **Hot Water Nodes:** Every high-speed carriage has a hot water dispenser. It is boiling (100°C), making it perfect for sterilizing bottles or mixing formula on the go.

### Local Hacks / Money-saving Tips
- **Trip.com Failover:** If the 12306 app's payment gateway hangs (common with foreign cards), use **Trip.com**. Their small commission is a "service fee" for a much higher success rate and English support.
- **Waitlist API:** If a train is "Sold Out," use the **"Waitlist"** (hòubǔ) feature in the app. It is surprisingly efficient at clearing as people cancel.
