---
layout: guide
title: "Taxi & Mobility SOP"
description: "Practical ChinaOps guide: Taxi & Mobility SOP. Step-by-step checks, fallbacks, and field tips."
metadata:
  version: 1.1
  last_validated: 2026-07-21
  ttl_days: 90
  stability_status: "stable"
  validation_method: "desktop_review"
  scope: "national"
---

# 🚕 Taxi & Mobility SOP

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>Prefer Didi or official taxi stands. Pay by QR when possible; refuse unsolicited “helpers” in arrival halls.</p>
  <p>Screenshot the plate number before the ride starts.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">请打表</div>
  <div class="py">qǐng dǎ biǎo</div>
  <div class="en">Please use the meter.</div>
</div>


**TL;DR:** Use **DiDi (International)** app or the **Alipay "Transport"** mini-program. Do not hail on the street unless you have the destination address in **Chinese characters**. Always ask for a **receipt (fàpiào)**.

**Prerequisites:**
- **App:** DiDi (English version) or Alipay.
- **Address:** Destination written in Chinese (screenshot or physical card).
- **Payment:** Linked Visa/Mastercard in Alipay or DiDi.

---

## 📋 The Runbook

### 1. Hailing: The "App-First" Protocol
- **Step 1:** Open **DiDi** (Global) or the **Alipay "Didi"** mini-program.
- **Step 2:** Enter destination (search works in English).
- **Step 3:** Select `Express` or `Premier`. Premier drivers are more likely to wait for you and help with luggage.
- **Verification:** Match the license plate shown in the app with the physical car.

### 2. The Street-Hail Protocol
- **Step 1:** Look for taxis with a **green** (available) light in the window. **Red** means occupied.
- **Step 2:** Show the driver your destination in **Chinese characters**.
- **Step 3:** Ensure the meter (Jìjiàqì) is flipped down (starting price typically 14-16 RMB in SH).
- **Verification:** Receive a physical **fàpiào** (receipt) at the end. This is your only "trace" if you leave your bag in the car.

### 3. Payment Execution
- **Step 1:** If using the app, payment is automatic (Server-side).
- **Step 2:** If street-hailing, scan the driver's QR code on the dashboard or headrest.
- **Verification:** Show the "Payment Success" screen to the driver before exiting.

---

## 🚨 Fallback (Plan B)

### If the app keeps spinning or no cars are available (Peak Hours):
1. **The Metro Node:** If it's 5:30 PM and you're in a busy district, do not wait for a DiDi. Go to the nearest **Metro station**. Use Alipay's "Transport" QR to ride.
2. **Luxury Hotel Hack:** Walk into the lobby of any 5-star hotel (Westin, Fairmont, etc.). Ask the concierge to **hail an official taxi** for you. They have a direct line to taxi dispatch.
3. **Cash Flow:** If your app payment fails, pay with **physical cash**. New regulations effective **Feb 1, 2026** strictly mandate that all merchants (including taxis) **must accept cash**. If they claim "no change," stay calm—they are legally required to find a solution. Always ask for the receipt (fàpiào) to prove you paid.

---

## 💡 TechDad's Tips

- **The "Lost Phone" SOP:** If you leave your phone in the car, you are in a "Critical Failure" state. **The Fa-Piao is your only hope.** It has the car's ID and base phone number. Never leave without it.
- **Parent Alert:** DiDi cars **do not have car seats**. If traveling with a baby, use the Metro (Safer) or look for "Luxury" cars in the app, which *occasionally* have them.
- **Visual Check:** Red light = Busy. Green light = Free. Don't wave at a red light; you'll look like a rookie.
- **Translation:** If the driver calls you, use the **In-app Chat**. It auto-translates your English messages into Chinese for the driver.

---

## 🚩 Strategic Gap: The "SPOF" Warning
**Single Point of Failure:** Relying on the driver's phone GPS.
- **Hotfix:** Keep your own map (Amap or Apple Maps) open to ensure the driver isn't taking a "scenic" (expensive) route.

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
