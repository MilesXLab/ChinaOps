# ChinaOps - Technical Runbook for Travelers & Parents

**Real-world solutions from a parent living in Shanghai**

---

## Quick Start

### What is ChinaOps?
A practical, non-commercial guide for travelers and families navigating China. Written by someone who's actually lived through these challenges.

**16 Step-by-Step Guides** | **3 Helper Tools** | **No Ads or Sponsorships**

### Choose Your Path:

#### First-Time Traveler?
Start with **[System Setup](docs/01-System-Setup/)** 
- Get your phone/SIM card working
- Set up VPN and payments
- Find pharmacies and medications

#### Traveling with Kids?
Go to **[Parenting Guide](docs/04-Parenting-Patch/)**
- Handle diapers & baby supplies
- Manage food allergies
- Check milk recall status

#### Emergency?
Check **[Emergency/DR](docs/03-Emergency-DR/)**
- Hospital access & procedures
- Lost passport recovery
- Network/WiFi outages

#### Browse Everything?
Use **[Interactive Web Interface](site/index.html)** or see full list below

---

## Full Library

### System Setup (5 Guides)
| Title | What You'll Learn | Time |
|-------|------------------|------|
| [Mobile Number & Activation](docs/01-System-Setup/mobile-number-and-activation.md) | Getting a Chinese phone number, eSIM vs physical SIM | 10 min |
| [Pharmacy & Medications](docs/01-System-Setup/pharmacy-and-medications.md) | How to buy medicine, common drug names in Chinese | 12 min |
| [VPN & eSIM / Payment Setup](docs/01-System-Setup/vpn-esim-payment.md) | Set up VPN, Alipay, WeChat Pay | 15 min |
| [Power Bank Rules](docs/01-System-Setup/power-bank-rules.md) | Safe power banks, charging rules, outlets | 8 min |
| [SIM Card Options](docs/01-System-Setup/sim-card-options.md) | Comparing carriers and plans | 10 min |

### Daily Runtime (4 Guides)
| Title | What You'll Learn | Time |
|-------|------------------|------|
| [Train Tickets (12306)](docs/02-Daily-Runtime/train-ticket-trap.md) | Booking system, name format issues, how to fix rejections | 10 min |
| [Taxis & Mobile Payment](docs/02-Daily-Runtime/taxi-payment.md) | Didi, DiDi International, fare negotiation | 8 min |
| [Maps & Toilets](docs/02-Daily-Runtime/maps-and-toilets.md) | Google Maps alternative, finding bathrooms | 7 min |
| [Public Transport](docs/02-Daily-Runtime/public-transport-tips.md) | Subways, buses, ferries, transit apps | 12 min |

### Emergency/DR (3 Guides)
| Title | What You'll Learn | Time |
|-------|------------------|------|
| [Hospital Access](docs/03-Emergency-DR/hospital-access.md) | Finding hospitals, language barriers, insurance, costs | 15 min |
| [Lost Passport](docs/03-Emergency-DR/lost-passport.md) | Emergency embassy contacts, replacement procedures | 12 min |
| [Network Outage](docs/03-Emergency-DR/network-outage.md) | VPN backup, WeChat without WiFi, offline navigation | 8 min |

### Parenting (4 Guides)
| Title | What You'll Learn | Time |
|-------|------------------|------|
| [Food Allergies & Diet](docs/04-Parenting-Patch/food-allergies-and-dietary-restrictions.md) | Restaurant communication, safe foods, allergy cards | 15 min |
| [Diapers & Baby Supplies](docs/04-Parenting-Patch/diapers-and-stores.md) | Where to buy, brands to trust, pricing | 10 min |
| [Milk Recall Check](docs/04-Parenting-Patch/milk-recall-check.md) | How to verify formula batches, safety databases | 8 min |
| [Nursing Rooms](docs/04-Parenting-Patch/nursing-rooms.md) | Locations, facilities, cultural tips | 5 min |

---

## Helper Scripts

Three Python tools for solving specific problems:

\\\ash
# Format your passport name for 12306 train tickets
python scripts/passport_mrz_converter.py "John Smith"
# Output: SMITH<<JOHN

# Calculate safe medication doses for children
python scripts/child_medication_calculator.py --name "Ibuprofen" --weight 25
# Output: Safe dose: 250mg

# Verify train booking details before purchasing
python scripts/train_ticket_checker.py --name "John Smith" --date 2026-02-15
# Output: Name check OK | Booking window: Feb 14
\\\

[Full Script Documentation](scripts/README.md)

---

## Inside Every Guide

Each guide (SOP) includes:
- **Problem** – What you're struggling with
- **Root Cause** – Why it's difficult in China
- **Step-by-Step Solution** – Exact instructions
- **Real Tips** – Insider advice
- **Trusted Brands/Apps** – Recommendations we've verified
- **FAQ** – Common questions answered
- **Emergency Fallback** – If Plan A doesn't work
- **Verified Contacts** – Phone numbers, addresses

---

## Help Improve ChinaOps

Found something wrong? Have a better solution? **Share it!**

### Easy Ways to Contribute:
- [Report an error](CONTRIBUTING.md#1-report-a-problem) – 2 minutes
- [Suggest an improvement](CONTRIBUTING.md#2-submit-a-new-sop) – 5 minutes  
- [Write a new guide](CONTRIBUTING.md#2-submit-a-new-sop) – 30 minutes

[See Full Contributing Guide](CONTRIBUTING.md) – Templates, examples, process

**Every contributor gets credited on the guide they improve!**

---

## Why ChinaOps is Different

| Feature | ChinaOps | Other Guides |
|---------|----------|--------------|
| **Based on Real Experience** | ✅ Tested by travelers actually in China | ❌ Often theoretical |
| **Safety-First** | ✅ Emergency procedures included | ❌ Often missing |
| **No Sponsorships** | ✅ Zero ads, zero promoted brands | ❌ Often monetized |
| **Quality Over Quantity** | ✅ Fewer, deeply researched guides | ❌ Lots of generic content |
| **Community Driven** | ✅ Contributions welcome & credited | ❌ Closed to public |

---

## License & Legal

**ChinaOps** is licensed under **CC BY-NC 4.0** (non-commercial use).

| Action | Allowed? |
|--------|----------|
| Use for yourself or family | ✅ Free |
| Share with credit | ✅ Free |
| Create translations | ✅ Free (non-commercial) |
| Sell as ebook | ❌ Need permission |
| Use in paid app | ❌ Need permission |
| License to company | ❌ Need permission |

[Full License Details](LICENSE)  
[Commercial Inquiries](LEGAL_NOTICE.md)

---

## Project Status

| Metric | Status |
|--------|--------|
| **SOPs** | 16 complete guides |
| **Helper Tools** | 3 Python scripts |
| **Stage** | 1 (Core content complete) |
| **Community** | Open to contributions |
| **Last Updated** | Jan 2026 |

---

## What's Next? (Stage 2 Planned)

- 🔍 Interactive search & mapping
- 📱 Mobile app & offline access
- 🌐 Chinese translations
- 📊 Community ratings & feedback
- 🛠️ More helper tools (formula checker, hospital locator, fare calculator)

---

## About the Creator

**TechDadShanghai** – A full-time parent who turned everyday survival moments with my kids into a structured guide for travelers.

Created: Jan 2026  
Location: Shanghai, China  
Mission: Help travelers & families navigate China safely

---

**Questions?** Check [Contributing Guide](CONTRIBUTING.md) or open a GitHub issue.

**Love ChinaOps?** Star us on GitHub ⭐ or share with other travelers!

---

*Last Updated: Jan 22, 2026 | Licensed under CC BY-NC 4.0*