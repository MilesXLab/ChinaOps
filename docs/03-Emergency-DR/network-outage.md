---
layout: guide
title: "Internet / Network Outage Survival SOP"
---

# Internet / Network Outage Survival SOP

**Last Updated:** Mar 2026 | **Author:** TechDadShanghai

---

## Problem
VPN stops working, mobile data fails, or hotel Wi-Fi is blocked — leaving you offline in a country where your phone is your wallet, map, and translator.

---

## Root Cause Analysis

| Cause | Symptom | Frequency |
|:---|:---|:---|
| **VPN server blocked** | Apps load without VPN; VPN apps fail silently | Very common during national events |
| **GFW pattern update** | VPN connects but traffic drops after 30 sec | Regular, especially on holidays |
| **Data plan exhausted** | Mobile data shows "no connection" | Common on short tourist SIMs |
| **Hotel Wi-Fi port blocking** | VPN connects but no international traffic | Common in budget hotels |
| **SIM registration issue** | No signal at all after airport purchase | Occasional, fixable |

---

## Triage Decision Tree

```
No Internet?
├── Can you load Chinese sites (Baidu, WeChat)?
│   ├── YES → VPN issue. Go to "VPN Fix" below.
│   └── NO → Mobile data / SIM issue. Go to "SIM Fix" below.
└── VPN connects but traffic still drops?
    └── → GFW pattern block. Rotate protocol (see below).
```

---

## Fix A: VPN Troubleshooting (Most Common)

### Step 1: Switch Protocol
Most VPN apps support multiple protocols. In the app settings:
- **ExpressVPN:** Settings → Protocol → Switch to **Lightway UDP** or **Lightway TCP**
- **LetsVPN:** Switch server region (Hong Kong → Singapore → Japan)
- **Astrill:** Protocol → **WireGuard** or **OpenWeb**

### Step 2: Airplane Mode Cycle
Toggle **Airplane Mode ON → wait 10 seconds → OFF**. This forces a fresh DNS registration and clears routing deadlocks.

### Step 3: Switch Network Source
- If on hotel Wi-Fi → switch to mobile data (or vice versa)
- If hotel Wi-Fi blocks VPN ports: use **port 443 (HTTPS)** in your VPN settings — this is rarely blocked

### Step 4: Switch VPN App
If your primary VPN is down, switch to your backup:
- Install **at least 2 VPN apps before arrival**
- Recommended: LetsVPN (mobile) + ExpressVPN (backup)

> [!IMPORTANT]
> VPN landscape changes constantly. Check expat communities (Reddit r/chinalife) **1 week before departure** to verify which VPN is currently working.

---

## Fix B: Mobile Data / SIM Issues

### "No Signal" — SIM Activation Failed
1. Remove SIM and reinsert (or toggle Airplane Mode).
2. Check carrier settings: Settings → Cellular → APN (Ask carrier for correct APN string).
3. Call carrier hotline while on hotel Wi-Fi using WhatsApp/WeChat:
   - **China Unicom:** 10010
   - **China Mobile:** 10086
   - **China Telecom:** 10000

### "Data Exhausted" — Plan Topped-Up
- Go to carrier app or WeChat mini-program to top up data.
- China Unicom: Search "中国联通" in WeChat → top up online with Alipay.
- Purchase a new data add-on (流量包) without changing your number.

### eSIM Failover
If your physical SIM fails, switch to your **backup eSIM** (Airalo/Nomad):
- Settings → Cellular → Add eSIM (or activate pre-downloaded eSIM profile)
- Keep the eSIM installed but inactive — switch it on only when needed

---

## Offline Survival Mode (When Nothing Works)

These tools work **without internet**:

| Tool | What it Does | Setup Required |
|:---|:---|:---|
| **Google Maps Offline** | Navigation without data | Download area before trip |
| **Amap (高德) Offline** | More accurate in China | Download city map in-app |
| **Pleco** | Chinese dictionary + offline mode | Download offline pack |
| **WeChat** | Messaging works on any data (even 2G) | Pre-installed |
| **Alipay QR** | Payment QR can be pre-generated | Open app and screenshot QR |
| **12306 Offline Tickets** | Train tickets saved in app | Download before travel |

---

## Miles' Tips

- **The "Two VPN" Rule:** Never travel to China with only one VPN app. The firewall evolves weekly. Install LetsVPN + ExpressVPN as your primary/backup pair.
- **Pre-Cache Everything:** On the night of arrival (when Wi-Fi is most reliable), download offline maps, sync your email, and generate Alipay QR.
- **Hotel Wi-Fi Trick:** If hotel Wi-Fi blocks VPN, plug directly into the LAN port in the room (port 443 TCP mode usually works on wired connections).
- **Café Fallback:** Starbucks, Costa, and major convenience stores (FamilyMart, Lawson) provide reliable Wi-Fi. Use these as "offline recovery nodes" when mobile data fails.
- **Low-data Mode:** In a crunch, WeChat still functions on 2G speeds. Keep WeChat as your last-resort communication tool.

---

## Related Guides

- [VPN & eSIM Setup](../../01-System-Setup/vpn-esim-payment/) — Pre-trip VPN installation SOP
- [Emergency Contacts Card](../emergency-contacts-card/) — Critical numbers for when you go fully offline
