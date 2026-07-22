---
layout: guide
title: "Internet / Network Outage Survival SOP"
description: "When VPN or mobile data dies in China: triage VPN vs SIM, rotate protocols, switch networks, and run offline maps/pay until restored."
metadata:
  version: 1.2
  last_validated: 2026-07-21
  ttl_days: 90
  stability_status: "critical"
  validation_method: "desktop_review"
  scope: "national"
---

# Internet / Network Outage Survival SOP

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>When VPN or data dies, switch network path: other eSIM, hotel Wi‑Fi, offline maps, and cash.</p>
  <p>Do not wait until 1% battery to fix connectivity.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">这里有没有Wi‑Fi？</div>
  <div class="py">zhèlǐ yǒu méiyǒu Wi‑Fi?</div>
  <div class="en">Is there Wi‑Fi here?</div>
</div>

**TL;DR:** Triage first: Chinese sites load? → VPN problem. Nothing loads? → SIM/data problem. Always keep **two VPNs**, offline maps, and cash.

**Prerequisites:**
- Two VPN apps installed **before** arrival
- Backup eSIM profile ready (inactive)
- Offline maps + Pleco packs downloaded
- ¥500+ cash and Alipay/WeChat already set up

---

## Problem

VPN dies, mobile data fails, or hotel Wi‑Fi blocks international traffic — and in China your phone is wallet, map, and translator.

| Cause | Symptom | Frequency |
|:---|:---|:---|
| VPN server blocked | Local apps OK; VPN fails | High during big events |
| GFW pattern update | VPN “connects” then drops ~30s | Holidays / crackdowns |
| Data plan exhausted | No mobile data | Tourist SIMs |
| Hotel Wi‑Fi port block | VPN up, no useful traffic | Budget hotels |
| SIM registration issue | No signal after airport buy | Occasional |

---

## 📋 The Runbook

### 1. Triage (30 seconds)

```
No Internet?
├── Chinese sites (Baidu / WeChat) load?
│   ├── YES → VPN issue → Fix A
│   └── NO  → SIM / data issue → Fix B
└── VPN connects but traffic dies?
    └── Rotate protocol / server → Fix A
```

### 2. Fix A — VPN
1. **Switch protocol/server:** Lightway UDP/TCP (ExpressVPN), other region (LetsVPN), WireGuard/OpenWeb (Astrill).
2. **Airplane mode** ON 10s → OFF (fresh DNS/routing).
3. **Swap network source:** hotel Wi‑Fi ↔ mobile data.
4. Force VPN over **port 443 / HTTPS** if hotel blocks common VPN ports.
5. **Switch to backup VPN app** (always travel with ≥2).
6. **Verification:** open google.com or WhatsApp successfully for 60+ seconds.

> [!IMPORTANT]
> VPN reality changes weekly. Recheck expat channels (e.g. r/chinalife) ~1 week before departure.

### 3. Fix B — Mobile data / SIM
1. Reseat SIM or Airplane toggle.
2. Check **APN** (carrier-specific); call carrier on hotel Wi‑Fi:
   - Unicom **10010** · Mobile **10086** · Telecom **10000**
3. Top up data in carrier app / WeChat mini-program (流量包) if plan is empty.
4. Fail over to **backup eSIM** (Airalo/Nomad) kept pre-installed but inactive.
5. **Verification:** signal bars + Chinese site + (with VPN) international site.

### 4. Stabilize for the day
- Download offline map tiles while any link works.
- Screenshot Alipay payment QR while online.
- Prefer cafés with known Wi‑Fi (Starbucks / Costa / FamilyMart) as recovery nodes.

---

## 🚨 Fallback (Plan B)

### Full offline survival

| Tool | Use | Setup ahead |
|:---|:---|:---|
| Google Maps offline | Navigation | Download regions |
| Amap (高德) offline | Better China detail | Download city |
| Pleco offline | Dictionary | Offline packs |
| WeChat | Often works on weak data | Pre-login |
| Alipay QR screenshot | Short-window pay | Capture while online |
| 12306 saved tickets | Train proof | Download in app |
| Cash | When QR dies | ¥500–1000 |

### Nothing digital works
1. Return to **hotel desk** or **5-star lobby** for Wi‑Fi + English help.
2. Use **official taxis** with cash; show hotel card.
3. Delay non-critical bookings until VPN/data restored.
4. See [Emergency Contacts](../emergency-contacts-card/) if you are stranded.

---

## 💡 TechDad's Tips

- **Two-VPN rule** is non-negotiable.
- Night-of-arrival: cache maps, mail, payment QR while hotel Wi‑Fi is strong.
- Wired hotel LAN + port 443 sometimes beats blocked Wi‑Fi.
- WeChat can limp on 2G when everything else fails.

---

## Related guides

- [VPN & eSIM Setup](../../01-System-Setup/vpn-esim-payment/)
- [Emergency Contacts Card](../emergency-contacts-card/)

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
