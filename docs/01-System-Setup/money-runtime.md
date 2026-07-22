---
layout: guide
title: "Money Runtime: Cash, ATM, Pre-auth & Invoices"
description: "Keep money moving in China after Alipay works: ATM cash, card pre-auth freezes, Tour Pass vs full account, and fapiao invoices."
metadata:
  version: 1.0
  last_validated: 2026-07-21
  ttl_days: 30
  churn: "high"
  stability_status: "critical"
  validation_method: "desktop_review"
  scope: "national"
---

# 💰 Money Runtime: Cash, ATM, Pre-auth & Invoices

<div class="plain-summary">
  <strong class="plain-summary-label">Plain English</strong>
  <p>Alipay is day-to-day pay. This guide is the second money stack: ATM cash, hotel/car deposits that freeze your card, and invoices for work trips.</p>
  <p>If QR fails, cash + a working ATM is what keeps you moving.</p>
  <p><span class="scope-badge">Scope: national</span></p>
</div>

<div class="phrase-card">
  <div class="zh">我想取现金</div>
  <div class="py">wǒ xiǎng qǔ xiànjīn</div>
  <div class="en">I want to withdraw cash.</div>
</div>

**TL;DR:** Carry **¥500–1500** buffer. Prefer **Bank of China / ICBC / UnionPay-branded ATMs** for foreign cards. Watch **pre-authorization freezes**. Ask for **电子发票** when you need reimbursement.

**Prerequisites:**
- Foreign Visa/Mastercard with international cash withdrawal enabled (call issuer before trip)
- Alipay + WeChat already linked (see [Alipay & WeChat Pay](../alipay-wechat-setup-foreigners/))
- Issuer travel notice / no geo-block on China
- Phone with maps to find ATMs (or hotel concierge)

**Related:** [Lost bank card](../../03-Emergency-DR/lost-bank-card/) · [Landing Protocol](../landing-protocol/) · [VPN & payment setup](../vpn-esim-payment/)

---

## Problem

App pay covers 90% of daily life — until the terminal is offline, a stall is cash-only, a hotel holds a large deposit, or your company needs a **fapiao (发票)**. Tourists often fix Alipay once and never build a cash/ATM path.

---

## 📋 The Runbook

### 1. Decide your money layers

| Layer | Role | Target buffer |
|:---|:---|:---|
| **A. Alipay / WeChat** | Daily QR | Working + backup card |
| **B. Physical chip card** | Hotels, some taxis, backup | 1–2 cards, different networks if possible |
| **C. Cash RMB** | Offline stalls, tips, ATM downtime | ¥500–1500 on person |
| **D. Invoice path** | Work / insurance | Know how to ask 电子发票 |

Do not run only on Layer A.

### 2. ATM cash (foreign card)

1. **Find ATM:** Hotel lobby, metro hubs, **Bank of China (中国银行)**, **ICBC (工商银行)**, airport arrivals.
2. **Choose language** → English if available.
3. Select **Withdrawal from overseas / credit-debit card** (wording varies).
4. Prefer **smaller amounts first** (e.g. ¥1000) to test issuer + local fees.
5. **Verification:** Count cash at machine; keep receipt until you reconcile with bank SMS.

**Typical friction (verify with your bank; fees change):**
- Issuer foreign ATM fee + possible % markup
- Local ATM fee (often shown on screen — accept/decline)
- Daily ATM caps set by **your bank**, not the machine
- Some machines reject foreign cards; walk to another bank brand **before** panic

> [!TIP]
> **UnionPay logo** on the ATM raises odds for foreign Visa/MC that ride UnionPay networks. If one BOC machine fails, try another branch — not the same machine three times.

### 3. Breaking large notes

ATMs often spit **¥100** bills. Stalls and taxis like smaller notes.

1. Buy a small item at **FamilyMart / Lawson / 7-Eleven**.
2. Or ask hotel front desk to break change after a purchase.
3. Keep a mix of ¥10 / ¥20 / ¥50 when you can.

### 4. Card pre-authorization (hotels, cars, some stores)

**What happens:** Merchant places a **hold** (预授权) larger than the final bill. Funds look “gone” but are not a final capture.

1. Before checkout, photograph the **hold amount** and expected release window.
2. At checkout, confirm they **release** the hold and charge only the final amount.
3. If hold lingers 7–15+ days, call **merchant first**, then your **card issuer** with receipt + date.

**Verification:** Bank app shows pending hold clear; available credit returns.

### 5. Alipay Tour Pass / visitor flows vs “full” account

| Mode | Who | Limits (conceptually) |
|:---|:---|:---|
| **International / visitor bind** | Foreign passport + overseas card | Works for most QR; KYC and per-TX caps apply |
| **Tour Pass–style prepaid** | Some visitor products (product names change) | Load balance; not a full mainland bank account |
| **Mainland real-name + local bank** | Residents / long-stay with local banking | Full ecosystem; not assumed for short trips |

**Action:** In Alipay, confirm you are in the **international visitor** path you intended. Do not assume a friend’s mainland transfer tricks are legal or stable — prefer official foreign-card bind.

### 6. Invoices (发票 fāpiào) for work or insurance

1. At paid merchant: ask **我需要电子发票** (*Wǒ xūyào diànzǐ fāpiào*).
2. Provide **email** and, if required, company **tax ID (税号)** — get this from your company before the trip.
3. Some places only issue on **WeChat/Alipay** invoice mini-flow after payment.
4. **Verification:** PDF/email arrives; save with date + merchant name for expense tools.

Street stalls and many small restaurants **cannot** issue fapiao — use chains or hotel F&B when finance is strict.

### 7. Daily money health check

- [ ] Alipay test QR works  
- [ ] WeChat Pay backup works **or** you accepted single-app risk  
- [ ] Cash ≥ ¥500 on body  
- [ ] You know nearest 24h ATM to hotel  
- [ ] No surprise open pre-auth older than expected  

---

## 🚨 Fallback (Plan B)

| Failure | Do this |
|:---|:---|
| Foreign card declined at all ATMs | Try second card / second bank brand; ask hotel cash advance policy; use Alipay balance if fundable |
| ATM swallows card | Stay at machine; use on-screen help; call bank emergency number on card back; note ATM ID |
| Cash only, you have none | Find FamilyMart-class store that takes QR → buy + ask nearby ATM |
| Huge hotel hold blocks card | Second card for daily spend; escalate release with front desk manager |
| Need fapiao, shop refuses | Pay at hotel or larger chain instead; keep WeChat pay record as weak proof only |
| All digital pay dead | Cash mode — see [Network outage](../../03-Emergency-DR/network-outage/) |

---

## 💡 TechDad's Tips

- Enable **international ATM + China** with issuer **before** wheels-up.
- Keep **one card offline** (not used for every subscription) as emergency plastic.
- Screenshot bank’s **China emergency phone** into your EMERGENCY album.
- For multi-week stays, re-check **FX rate and issuer “smart pricing”** weekly — silent markups hurt more than ATM flat fees.

---

## FAQ

**Q: Can I live with zero cash?**  
A: Risky. Metro may be QR-only in big cities, but small food, some taxis, and outages still need paper RMB.

**Q: Is it safe to use random street ATMs?**  
A: Prefer bank-branch or hotel lobby machines. Cover the keypad; refuse “helper” strangers.

**Q: How fast do pre-auths release?**  
A: Often a few days; can be 1–2 billing cycles by issuer policy. Document everything.

---

**Last Updated:** Jul 21, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
