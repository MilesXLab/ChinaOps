---
layout: guide
title: "Alipay & WeChat Pay Setup for Foreign Visitors"
description: "Set up Alipay and WeChat Pay with a foreign Visa/Mastercard: identity checks, card binding, metro QR, and what to do when payment fails."
metadata:
  version: 1.3
  last_validated: 2026-07-21
  ttl_days: 30
  churn: "high"
  stability_status: "critical"
  validation_method: "desktop_review"
  scope: "national"
---

# Alipay & WeChat Pay Setup for Foreign Visitors

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>You need Alipay and usually WeChat Pay for daily life. Link a foreign Visa/Mastercard, finish identity checks, and keep a backup card ready.</p>
  <p>If payment fails, try the other app, another card, or cash — do not panic at the counter.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">可以用支付宝吗？</div>
  <div class="py">kěyǐ yòng Zhīfùbǎo ma?</div>
  <div class="en">Can I pay with Alipay?</div>
</div>

**TL;DR:** Set up **both** Alipay and WeChat Pay **before or right after landing**. Bind a major Visa/Mastercard, finish passport KYC, and test a small purchase. Cashless is default almost everywhere.

**Prerequisites:**
- Passport (photo ready for in-app KYC)
- Foreign Visa or Mastercard (credit/debit; avoid obscure prepaid/virtual cards)
- Working phone number for SMS / 3D-Secure
- Optional: ¥500–1000 cash buffer

---

## Problem

Cashless payment is nearly universal in China. Without Alipay or WeChat Pay you will struggle at restaurants, taxis, convenience stores, and many metro gates. Foreign cards work in both apps with an international visitor flow — but setup and mid-trip KYC still fail often enough that you need a Plan B.

| App | Best for | Foreign-friendliness |
|:---|:---|:---|
| **Alipay (支付宝)** | Shopping, metro, bikes, delivery | Dedicated international flow |
| **WeChat Pay (微信支付)** | Restaurants, mini-programs, transfers | Works once card is linked |

> [!TIP]
> Set up **both**. Some merchants accept only one. Dual apps are your payment redundancy layer.

---

## 📋 The Runbook

### 1. Alipay international setup
1. Download **Alipay** → open **International** flow (or auto-detect region).
2. Register with your **foreign phone number** → SMS code → 6-digit payment PIN.
3. **Identity:** Me → Settings → Identity Information → upload **passport** photo.
4. **Bind card:** Profile → Bank Card → Add → Visa/Mastercard → complete 3D-Secure.
5. **Limit note:** Verified foreign users often face ~**$5,000 USD** single-transaction caps; contact support for large purchases.
6. **Verification:** Make a tiny test payment or transfer **before you rely on it in China**. Prefer binding at home so 3D-Secure SMS arrives quickly.

### 2. WeChat Pay setup
1. Download **WeChat** → register with your foreign number.
2. Complete **friend verification** if prompted (a WeChat user registered 6+ months scans your QR). Ask hotel staff, colleagues, or a Chinese contact.
3. **Me → Services → Wallet** → bind Visa/Mastercard (AmEx is inconsistent).
4. **In store:** Me → Pay → show QR, or Scan the merchant code.
5. **Verification:** Wallet shows a usable payment method and a successful test pay.

### 3. Metro & bikes (Shanghai example)
- **Alipay:** Search “Metro” → transit QR → scan at gate.
- **NFC:** Shanghai Metro often accepts contactless Visa/Mastercard/AmEx/JCB at the gate (enable small-amount password-free on the card).
- **Apple Wallet:** Shanghai Metro Card → Express Mode.
- **Bikes:** Alipay → HelloBike / Meituan mini-program → scan; 7-day passes are cheap for multi-day stays.

### 4. Zero-data payment snapshot
1. Open Alipay → **Pay** → screenshot the QR.
2. Show quickly — codes **rotate (~60s)**; this is last resort only.

---

## 🚨 Fallback (Plan B)

### Payment declined at the counter
1. Switch **Alipay ↔ WeChat Pay**.
2. Choose a **second card** inside the app.
3. Pay with **physical chip card** if the terminal allows.
4. Use **cash** (FamilyMart/Lawson are good for breaking ¥100 notes).

### Common errors (quick table)

| Error / reality | Cause | Fix |
|:---|:---|:---|
| Card not supported | Prepaid/virtual blocked | Major bank Visa/MC |
| Verification failed | 3D-Secure / SMS | Call issuer; enable international SMS |
| Limit reached | Daily/TX caps | Support or other card |
| Mid-trip KYC audit | Security review after a few days | Re-upload passport + video KYC with physical passport |
| WeChat account lock | SIM/device swap | Do not log out/swap SIM on the WeChat phone; hotspot from another device |
| Random risk decline | POS risk engine | Other app/card immediately |
| App in Chinese only | Locale reset | Globe icon or Settings (齿轮) → Language (语言) |

### Network dead
- Screenshot Alipay QR while online; use hotel Wi‑Fi; see [Network Outage](../../03-Emergency-DR/network-outage/) and [VPN & eSIM](../vpn-esim-payment/).

---

## 💡 TechDad's Tips

- **Bind before you land** so 3D-Secure SMS is instant (in China, foreign SMS can lag 5–10 minutes).
- Carry **¥500–1000** small bills for stalls and glitching taxis.
- Check Alipay supermarket mini-programs (Hema, ALDI) for new-user coupons.
- False declines are often timeouts — swap apps before assuming the card is dead.

---

## Related guides

- [VPN & eSIM Setup](../vpn-esim-payment/)
- [Mobile Number & Activation](../mobile-number-and-activation/)
- [Public Transport Tips](../../02-Daily-Runtime/public-transport-tips/)

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
