---
layout: guide
title: "Network & VPN Outage Failover"
metadata:
  version: 1.1
  last_validated: 2026-01-26
  stability_status: "critical"
---

# 📡 Network & VPN Outage Failover

**TL;DR:** Pre-install **LetsVPN** (Stable) and **ShadowFly** (Performance). Pre-download **Offline Maps**. If your VPN dies, switch to your **Travel eSIM** (which bypasses the wall natively).

**Prerequisites:**
- **App:** Two independent VPNs + One offline dictionary (Pleco).
- **Offline Data:** Amap (AutoNavi) or Google Maps offline cache.
- **eSIM:** A travel eSIM with data roaming active.

---

## 📋 The Runbook

### 1. The VPN "Hot-Swap"
- **Step 1:** If your primary VPN (e.g., ExpressVPN) stops connecting, immediately switch to your **"Stealth" VPN** (LetsVPN or LightningX).
- **Step 2:** Change protocol to "TCP" or "Stealth" in the app settings.
- **Verification:** Open a non-Chinese site (e.g., `nytimes.com`). If it loads, the tunnel is restored.

### 2. The Native Bypass (eSIM Logic)
- **Step 1:** Turn off Wi-Fi. 
- **Step 2:** Enable your **Travel eSIM** (Trip.com, Yesim, etc.).
- **Verification:** These eSIMs route traffic outside China. If your eSIM data is working, you don't need a VPN to access Google/WhatsApp. 

### 3. The "Cold Boot" (Offline Survival)
- **Step 1:** If all data is dead, switch to your **Offline Map**.
- **Step 2:** Use **Pleco** (Dictionary) which works 100% offline for translation.
- **Verification:** Use the GPS (which works without data) to find your current location on the offline map.

---

## 🚨 Fallback (Plan B)

### If you have zero data and are lost:
1. **The Starbucks Node:** Starbucks, Baker & Spice, and Wagas have stable Wi-Fi. Note: They often require an SMS code to log in. Provide your foreign number with the proper country code (e.g., +44).
2. **Apple Store Public Hub:** If you are near an **Apple Store**, they have open, high-speed Wi-Fi that does not require an SMS login and often bypasses the firewall.
3. **The "Screenshot" Failover:** Always maintain a photo album of your:
   - Hotel address in Chinese.
   - Return flight details.
   - Insurance policy.

---

## 💡 TechDad's Tips

- **The "Great Firewall" Pulse:** Connectivity often drops during major government meetings or national holidays. Don't panic; just switch to a less common VPN.
- **Power vs. Privacy:** VPNs drain your battery 30% faster. Keep it **OFF** when you are just using local apps like Didi or Alipay.
- **WeChat "Keep-Alive":** WeChat works without a VPN. If everything else is dead, message your hotel or family via WeChat.

---

## 🚩 Strategic Gap: The "SPOF" Warning
**Single Point of Failure:** Relying on a single VPN provider.
- **Hotfix:** Purchase a 24-hour "Day Pass" for a second VPN the morning you land, just in case your primary provider hit a block overnight.
