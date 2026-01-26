---
layout: guide
title: "Connectivity: SIM & eSIM Options"
metadata:
  version: 1.1
  last_validated: 2026-01-26
  stability_status: "stable"
---

# 📶 Connectivity: SIM & eSIM Options

**TL;DR:** For 100% "Firewall Bypass," use a **Travel eSIM** (Trip.com/Yesim). For local services (receiving SMS/Didi), you need a **Physical SIM** from China Unicom or Telecom. 

**Prerequisites:**
- **Unlocked Phone:** Crucial. Check with your home carrier.
- **Physical ID:** Passport (for local SIM registration).
- **Setup Time:** 15 mins (eSIM) vs 45 mins (Store visit).

---

## 📋 The Runbook

### 1. The "Tourist Pass" (The Easy Link)
- **Step 1:** Purchase a **Travel eSIM** via the **Trip.com** app *before* landing.
- **Step 2:** Choose the "China + HK/Macao" plan. This routes data through HK, bypassing the firewall natively.
- **Verification:** Switch your data to the eSIM. Open `google.com`. If it loads, you are "off-wall."

### 2. The Local SIM "Full-Stack"
- **Step 1:** Go to a **China Unicom (中国联通)** or **China Telecom (中国电信)** official service center.
- **Step 2:** Ask for the **"Short-term Tourist SIM"** (usually 100-200 RMB). Give them your physical passport.
- **Step 3:** The staff will perform a face-scan for registration (mandatory).
- **Verification:** Reboot your phone. Try sending an SMS to your hotel. Look for the `4G/5G` icon.

### 3. Comparison of Nodes
| Type | Best For | VPN Required? | SMS Verification? |
| :--- | :--- | :--- | :--- |
| **Travel eSIM** | Short stays (7-14 days) | **No** (Native Bypass) | Limited |
| **Local Physical SIM** | Long stays (1 month+) | **YES** (Firewall Active) | **Full Support** |
| **Home Roaming** | Zero-effort (Expensive) | **No** (Native Bypass) | Varies |

---

## 🚨 Fallback (Plan B)

### If your eSIM fails to activate:
1. **Airport Kiosks:** PVG and SHA arrivals have dedicated "Tourist SIM" kiosks. They are 2x the price of a city store but have English staff and will fix your settings on the spot.
2. **The "Hotspot" Patch:** If only one member of the family has a working SIM, use **Personal Hotspot**. Note: This drains batteries fast—carry your power bank.
3. **Wi-Fi + VPN:** Use the airport/hotel Wi-Fi. It will likely require an SMS code. Providing your foreign country code (e.g., +1, +44) usually works for these portals.

---

## 💡 TechDad's Tips

- **The "Data Only" Trap:** Some eSIMs give you data but **no phone number**. Without a number (starting with +86), you cannot register for **Didi** or **Meituan**. Check the fine print.
- **China Mobile:** Unless your phone specifically supports TDD-LTE/TD-SCDMA (most modern iPhones do, but some older Androids don't), stick to **China Unicom**. They use a more global standard (GMS).
- **The "Verification" King:** If you plan to use local apps heavily, the +86 phone number is more valuable than the data itself. Use the +86 for the apps and your eSIM for the actual internet.

---

## 🚩 Strategic Gap: The "SPOF" Warning
**Single Point of Failure:** Relying on a data-only eSIM for a 3-week trip. 
- **Hotfix:** Get a local physical SIM for the primary traveler and travel eSIMs for the rest of the family.
