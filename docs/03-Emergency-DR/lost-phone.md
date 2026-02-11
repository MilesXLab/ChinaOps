---
layout: guide
title: "Lost or Stolen Phone Recovery SOP"
metadata:
  version: 1.1
  last_validated: 2026-02-05
  stability_status: "critical"
  ttl_days: 90
---

![v1.1.0 Verified](https://img.shields.io/badge/v1.1.0-Verified-brightgreen)
# 📱 Lost or Stolen Phone Recovery SOP

**TL;DR:** Immediately lock your phone remotely, freeze Alipay/WeChat Pay, contact your carrier to suspend the SIM, then recover contacts/photos from cloud backup. Your payment apps are the highest priority.

**Prerequisites:**
- **Cloud Account:** iCloud/Google Account credentials (to lock phone remotely).
- **Payment App Access:** Another device or computer to access Alipay/WeChat Pay web portals.
- **Backup Device:** A spare phone or tablet (if available).
- **SIM Card Info:** Your phone number and carrier name.

---

## 📋 The Runbook

### 1. Immediate Lockdown (The "Freeze" Protocol)
- **Step 1:** If you have another device, use **Find My iPhone** (iOS) or **Find My Device** (Android) to lock the phone remotely and display a message with your contact info.
- **Step 2:** If no other device, borrow a phone or use a computer to access:
  - iOS: [iCloud.com/find](https://www.icloud.com/find)
  - Android: [google.com/android/find](https://www.google.com/android/find)
- **Verification:** Confirm the phone is locked and location tracking is enabled (if possible).

### 2. Payment App Security (Critical Priority)
- **Step 1:** Immediately log into **Alipay** web portal ([alipay.com](https://www.alipay.com)) or use another device with the app.
- **Step 2:** Go to **Security Settings** → **Freeze Account** (冻结账户). This prevents any transactions.
- **Step 3:** Repeat for **WeChat Pay** (WeChat → Me → Pay → Wallet → Security → Freeze Account).
- **Verification:** Check transaction history to ensure no unauthorized payments occurred before freezing.

### 3. SIM Card Suspension
- **Step 1:** Contact your carrier's customer service:
  - **China Mobile:** Call **10086** (English: Press 9)
  - **China Unicom:** Call **10010** (English: Press 9)
  - **China Telecom:** Call **10000** (English: Press 9)
- **Step 2:** Request **"SIM Card Suspension"** (停机 Tíngjī). You'll need your ID number or passport.
- **Verification:** Confirm the SIM is suspended (try calling your number from another phone; it should not ring).

---

## 🚨 Fallback (Plan B)

### If you cannot access payment apps or carrier service:
1. **The "Bank Card" Failover:** If your payment apps are linked to bank cards, call your bank immediately to freeze the cards. Most international banks have 24/7 hotlines.
2. **Police Report:** Go to the nearest police station (派出所) and file a report. This is required if you need to replace your SIM card later.
3. **Embassy Assistance:** If you're completely locked out and need emergency funds, contact your embassy. They can help with emergency loans or contacting family.

---

## 💡 TechDad's Tips

- **The "Two-Device" Strategy:** Always carry a backup device (old phone or tablet) with your payment apps pre-installed. This allows immediate account freezing.
- **Cloud Backup is Life:** Enable automatic photo/contact backup (iCloud/Google Photos). If your phone is lost, you can recover everything except the physical device.
- **SIM Card PIN:** Set a PIN for your SIM card (Settings → SIM PIN). Even if someone steals your phone, they cannot use your SIM without the PIN.
- **The "Find My" Hack:** Enable "Send Last Location" (iOS) or "Location History" (Android). This sends your phone's last known location before the battery dies.

---

## 🔄 Recovery Protocol (After Securing Accounts)

### 1. Replace SIM Card
- **Step 1:** Go to your carrier's service center with your passport and police report (if required).
- **Step 2:** Request a **"SIM Card Replacement"** (补卡 Bǔkǎ). Cost: 10-20 RMB.
- **Verification:** Your old number will be restored, but all contacts stored on the SIM are lost (use cloud backup).

### 2. Restore Payment Apps
- **Step 1:** On your new device, reinstall Alipay and WeChat Pay.
- **Step 2:** Log in using your phone number and SMS verification code.
- **Step 3:** Unfreeze your accounts from the Security Settings.
- **Verification:** Test with a small transaction (e.g., 1 RMB mobile top-up).

### 3. Recover Contacts & Photos
- **Step 1:** Log into your cloud account (iCloud/Google) on the new device.
- **Step 2:** Enable sync for Contacts and Photos.
- **Verification:** Wait for sync to complete (may take hours for large photo libraries).

---

## 🚩 Strategic Gap: The "SPOF" Warning
**Single Point of Failure:** Relying on a single device for all critical functions (payments, navigation, communication).
- **Hotfix:** Always maintain a backup device with payment apps installed and cloud backup enabled. Keep a physical list of emergency contacts separate from your phone.

---

**Last Updated:** Feb 5, 2026 | **Author:** TechDadShanghai

[← Back to Guide Library](../)
