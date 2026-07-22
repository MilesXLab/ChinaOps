---
layout: guide
title: "China App Stack: Install Order & Account Hygiene"
description: "Which Chinese apps to install in what order, how to avoid WeChat/Alipay lockouts, and how phone-number changes break everything."
metadata:
  version: 1.0
  last_validated: 2026-07-21
  ttl_days: 90
  stability_status: "stable"
  validation_method: "desktop_review"
  scope: "national"
---

# 📱 China App Stack: Install Order & Account Hygiene

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>Life in China runs on apps. Install them in a safe order, keep one stable phone number and device for WeChat, and store backup codes offline.</p>
  <p>Changing SIM or logging out at the wrong time can lock payments and chat together.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">这个软件怎么下载？</div>
  <div class="py">zhège ruǎnjiàn zěnme xiàzǎi?</div>
  <div class="en">How do I download this app?</div>
</div>

**TL;DR:** **Day −7:** VPN + Alipay + WeChat + maps offline. **Do not** casually log out of WeChat or swap the SIM on your payment phone. Screenshot QR pays only as emergency.

**Prerequisites:**
- 15–20 GB free storage
- Apple ID / Google account that can install apps (or Chinese App Store access)
- Passport photos for KYC
- Second device or hotspot plan for recovery
- Guides: [VPN & eSIM](../vpn-esim-payment/) · [Alipay & WeChat](../alipay-wechat-setup-foreigners/) · [Network outage](../../03-Emergency-DR/network-outage/)

---

## Problem

Foreigners install apps randomly, bind everything to a **roaming number**, then lose SMS, get WeChat risk-locked, and cannot open Alipay. The stack is a **dependency graph**, not a shopping list.

---

## 📋 The Runbook

### 1. Install order (recommended)

| Phase | Apps | Why this order |
|:---|:---|:---|
| **0. Before flight** | VPN (×2), offline maps pack, translation offline pack | Without these, nothing else configures well in-country |
| **1. Money + ID** | Alipay, WeChat (+ Pay) | Wallet + super-app; KYC early |
| **2. Move** | DiDi (or Alipay transport), 12306 / Trip.com, metro in Alipay | Airport exit and trains |
| **3. Maps** | Amap 高德 and/or Baidu Maps; Apple Maps as supplement | Local POI quality |
| **4. Daily life** | Meituan 美团, Ele.me 饿了么, Taobao/JD as needed | Food and delivery need address + phone |
| **5. Optional** | Dianping 大众点评, Hellobike, railway extras | After core stack stable |

**Verification:** Each phase has one successful real action (pay, ride, route, order).

### 2. Account hygiene rules

1. **One primary device** for WeChat + Pay — treat it like a hardware token.
2. **Avoid** logging out of WeChat “to save battery.”
3. **Avoid** swapping the SIM that receives WeChat/Alipay SMS on that primary device mid-trip.
4. Use a **second phone or eSIM hotspot** for data experiments (see payment SOP warnings).
5. Store in offline album: passport, visas, hotel address, Alipay/WeChat customer numbers.
6. Prefer **email + passport KYC** backups where apps allow, not SMS-only recovery.

### 3. Phone number strategy

| Number type | Use | Risk |
|:---|:---|:---|
| Home country number | WeChat/Alipay registration if it receives SMS abroad | SMS delay in China |
| Chinese local number | Delivery, some real-name, ride share | Expires → lock cascade |
| eSIM data-only | Connectivity without replacing WeChat SIM | Good for hotspot phone |

**Rule:** If you buy a Chinese number later, **add** it carefully inside apps; do not blindly replace the only recovery number without a tested backup login path.

### 4. Mini-programs vs apps

WeChat/Alipay **mini-programs** power metro, bikes, some government services. You often need:

- Working Pay inside the host app
- Camera permission for QR
- Location permission for metro/bike

**Verification:** Open metro QR once before first real commute.

### 5. Weekly stack check (stays >7 days)

- [ ] VPN still connects 60s+
- [ ] Alipay + WeChat pay test
- [ ] Maps offline regions still present
- [ ] Delivery address still matches hotel/apartment
- [ ] Storage not full (camera rolls kill installs)

---

## 🚨 Fallback (Plan B)

| Failure | Action |
|:---|:---|
| WeChat risk lock | Stop device/SIM thrashing; complete in-app appeal with passport; use SMS/voice from original number |
| Lost SMS number | Restore number with carrier if possible; else platform human review with passport |
| App only in Chinese | System language or in-app language; Translate camera on settings menus |
| Cannot install from store | Use official APK only from vendor site on Android **with caution**; prefer App Store; hotel Wi‑Fi + VPN |
| Phone stolen | [Lost phone](../../03-Emergency-DR/lost-phone/) + freeze pay apps from any web/help path |
| Total network death | Offline maps + cash + [Network outage](../../03-Emergency-DR/network-outage/) |

---

## 💡 TechDad's Tips

- Install **two VPNs** before wheels-up — non-negotiable.
- Turn off aggressive “offload unused apps” for WeChat/Alipay.
- Name your phone `CHINA-PRIMARY` in settings so you never experiment on it.
- Family trip: each adult has Pay working; do not share one WeChat for all payments.

---

## FAQ

**Q: Do I need Taobao on day one?**
A: No. Money, maps, ride, metro first.

**Q: Can I dual-SIM WeChat safely?**
A: Possible but easy to break SMS verification. Change one variable at a time.

**Q: Are international versions enough?**
A: Often yes for Alipay visitor flows; WeChat still behaves like WeChat — friend verification may apply.

---

## Related guides

- [Mobile number & activation](../mobile-number-and-activation/)
- [SIM options](../sim-card-options/)
- [Translation tools](../translation-tools/)

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
