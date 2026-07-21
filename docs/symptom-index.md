---
layout: guide
title: "Symptom Index: Find a Guide Fast"
description: "When something breaks in China, match your symptom to the right ChinaOps SOP. Filter by category."
---

# Symptom Index

**Plain English:** Something is broken or confusing. Type a word (payment, passport, train…) or tap a filter chip, then open the matching guide. Works without knowing our category names. Without JavaScript, the full list stays visible — use browser find.

<p class="symptom-count" id="symptomCount" aria-live="polite">Showing all topics</p>

<div class="symptom-search-wrap">
  <label class="visually-hidden" for="symptomSearch">Search symptoms</label>
  <input type="search" id="symptomSearch" class="symptom-search" placeholder="Search: payment, passport, train, hospital…" autocomplete="off" enterkeyhint="search" />
  <button type="button" class="filter-chip symptom-search-clear" id="symptomSearchClear" hidden>Clear</button>
</div>

<div class="symptom-filters" id="symptomFilters" role="toolbar" aria-label="Filter symptoms by topic">
  <button type="button" class="filter-chip is-active" data-filter="all">All</button>
  <button type="button" class="filter-chip" data-filter="payment">Payment</button>
  <button type="button" class="filter-chip" data-filter="phone">Phone &amp; data</button>
  <button type="button" class="filter-chip" data-filter="arrival">Arrival &amp; hotel</button>
  <button type="button" class="filter-chip" data-filter="transport">Transport</button>
  <button type="button" class="filter-chip" data-filter="health">Health &amp; safety</button>
  <button type="button" class="filter-chip" data-filter="food">Food &amp; daily</button>
  <button type="button" class="filter-chip" data-filter="kids">Kids</button>
  <button type="button" class="filter-chip" data-filter="holiday">Holidays</button>
</div>

<div class="symptom-section" data-tags="payment">

## Payment & money

| Symptom | Open this guide |
|---------|-----------------|
| Alipay / WeChat will not accept my foreign card | [Alipay & WeChat Pay (foreign visitors)](../01-System-Setup/alipay-wechat-setup-foreigners/) |
| Payment works then suddenly locks / asks for selfie | [VPN, eSIM & Payment Setup](../01-System-Setup/vpn-esim-payment/) (Payment Recovery) |
| I need cash or ATM fallback | [Landing Protocol](../01-System-Setup/landing-protocol/) · [Taxi & payment](../02-Daily-Runtime/taxi-payment/) |
| Lost bank card / need to freeze cards | [Lost bank card](../03-Emergency-DR/lost-bank-card/) |

</div>

<div class="symptom-section" data-tags="phone">

## Phone, data & apps

| Symptom | Open this guide |
|---------|-----------------|
| Google / WhatsApp / Instagram will not load | [VPN, eSIM & Payment](../01-System-Setup/vpn-esim-payment/) · [Network outage](../03-Emergency-DR/network-outage/) |
| Need a Chinese number for SMS / apps | [Mobile number & activation](../01-System-Setup/mobile-number-and-activation/) · [SIM options](../01-System-Setup/sim-card-options/) |
| Phone lost or stolen | [Lost phone](../03-Emergency-DR/lost-phone/) |
| Maps or Wi‑Fi fail; I am offline | [Network outage](../03-Emergency-DR/network-outage/) · [Maps & toilets](../02-Daily-Runtime/maps-and-toilets/) |

</div>

<div class="symptom-section" data-tags="arrival">

## Arrival, hotel & language

| Symptom | Open this guide |
|---------|-----------------|
| First 30 minutes after landing — what order? | [Landing Protocol](../01-System-Setup/landing-protocol/) |
| Digital arrival card / visa-free confusion | [Visa & entry](../01-System-Setup/visa-and-entry/) |
| Hotel will not check me in / police registration | [Hotel check-in](../01-System-Setup/hotel-check-in/) |
| Nobody understands my English | [Translation tools](../01-System-Setup/translation-tools/) |
| Cannot read metro / toilet / facility signs | [Visual signs guide](../02-Daily-Runtime/shanghai-visual-signs-guide/) |

</div>

<div class="symptom-section" data-tags="transport">

## Transport

| Symptom | Open this guide |
|---------|-----------------|
| 12306 rejects my name | [Train ticket trap](../02-Daily-Runtime/train-ticket-trap/) · run `passport_mrz_converter.py` |
| International → domestic flight connection | [Transit protocol](../02-Daily-Runtime/international-domestic-transit/) |
| Taxi / Didi issues or cash vs QR | [Taxi & payment](../02-Daily-Runtime/taxi-payment/) |
| Metro, bus, ferry basics | [Public transport](../02-Daily-Runtime/public-transport-tips/) |
| Want to drive / rent a car | [Car rental](../02-Daily-Runtime/car-rental/) |
| Luggage delayed or lost | [Lost luggage](../02-Daily-Runtime/lost-luggage/) |
| Power bank taken at airport security | [Power bank rules](../01-System-Setup/power-bank-rules/) |

</div>

<div class="symptom-section" data-tags="health">

## Health & safety

| Symptom | Open this guide |
|---------|-----------------|
| Need a hospital / clinic with English help | [Hospital access](../03-Emergency-DR/hospital-access/) |
| Need OTC medicine / pharmacy phrases | [Pharmacy & medications](../01-System-Setup/pharmacy-and-medications/) |
| Chronic meds / prescription refill | [Prescription refill](../03-Emergency-DR/prescription-refill/) |
| Possible scam (tea, taxi, QR) | [Safety & scams](../03-Emergency-DR/safety-and-common-scams/) · [Shanghai safety](../03-Emergency-DR/shanghai-safety-guide/) |
| Need emergency numbers on one card | [Emergency contacts card](../03-Emergency-DR/emergency-contacts-card/) |
| Passport lost or stolen | [Lost passport](../03-Emergency-DR/lost-passport/) |

</div>

<div class="symptom-section" data-tags="food">

## Food & daily life (Shanghai-heavy)

| Symptom | Open this guide |
|---------|-----------------|
| Where / what to eat | [Shanghai food guide](../02-Daily-Runtime/shanghai-food-guide/) |
| Vegetarian / vegan ordering | [Vegan guide](../02-Daily-Runtime/shanghai-vegan-guide/) |
| Weather, AQI, typhoon prep | [Weather guide](../02-Daily-Runtime/shanghai-weather-guide/) |
| Local apps and resident tips | [Shanghai local hacks](../02-Daily-Runtime/shanghai-local-hacks/) |
| Sightseeing nodes | [Attractions](../02-Daily-Runtime/shanghai-attractions-guide/) |

> **Region note:** Many daily-life guides are **Shanghai-first**. Payments, trains, and emergencies are mostly national.

</div>

<div class="symptom-section" data-tags="kids">

## Traveling with kids

| Symptom | Open this guide |
|---------|-----------------|
| Formula batch / recall worry | [Milk safety / recall](../04-Parenting-Patch/milk-recall-check/) · [SafeFeed Action](https://milesxlab.github.io/safefeed-action/) |
| Diapers and baby supplies | [Diapers & stores](../04-Parenting-Patch/diapers-and-stores/) |
| Food allergies at restaurants | [Food allergies](../04-Parenting-Patch/food-allergies-and-dietary-restrictions/) |
| Need a nursing / pumping room | [Nursing rooms](../04-Parenting-Patch/nursing-rooms/) |
| Full baby/toddler playbook | [Baby survival runbook](../04-Parenting-Patch/baby-survival-master-runbook/) |

</div>

<div class="symptom-section" data-tags="holiday">

## Holidays & peak travel

| Symptom | Open this guide |
|---------|-----------------|
| CNY / Golden Week crowds, closures, tickets | [Holiday survival](../05-Event-Operations/holiday-survival-guide/) |

</div>

---

## Still stuck?

1. Browse the [full library](../) by category.  
2. Report a gap: [GitHub Issues](https://github.com/MilesXLab/ChinaOps/issues).  
3. Email: [miles.x.dev@outlook.com](mailto:miles.x.dev@outlook.com?subject=ChinaOps%20Symptom%20Index).

[← Back to Home](../../)
