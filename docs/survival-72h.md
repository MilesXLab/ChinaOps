---
layout: guide
title: "72-Hour Survival Pack (offline)"
description: "How to use the printable 72-hour survival pack and optional offline file folder before a China trip."
---

# 72-Hour Survival Pack

**Plain English:** Before you fly, print or PDF a **3-page survival pack** that works when the phone is dead. It is a subset of ChinaOps — landing gates, money, network, emergency numbers, phrases, and a 72h checklist.

## Open / print

| Asset | Use |
|-------|-----|
| **[survival-72h.html](../../survival-72h.html)** | Full 3-page pack — browser **Print / Save PDF** |
| **[print-hub.html](../../print-hub.html)** | Wallet-size emergency / phrase layouts |
| **[phrase-card-tool.html](../../phrase-card-tool.html)** | Custom allergy / emergency card |

## What is inside the pack

1. **Page 1** — Handwrite hotel/embassy · landing gates · money layers · network triage  
2. **Page 2** — 110/120 · scam basics · essential phrases · hospital claim notes  
3. **Page 3** — 0–72h checklist · “open later” SOP paths · notes box  

## Optional offline folder (maintainers / power users)

From repo root:

```bash
python scripts/build_offline_pack.py
# optional zip:
python scripts/build_offline_pack.py --zip
```

Creates `_offline_pack/` (gitignored) with survival pack, print packs, tools, and `assets/` CSS/JS so you can copy the folder to a phone or USB.

## Related SOPs

- [Landing Protocol](../01-System-Setup/landing-protocol/)
- [Money Runtime](../01-System-Setup/money-runtime/)
- [Network outage](../03-Emergency-DR/network-outage/)
- [Emergency contacts](../03-Emergency-DR/emergency-contacts-card/)

[← Back to Guide Library](../)
