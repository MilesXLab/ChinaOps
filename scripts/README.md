# ChinaOps Scripts Directory

Practical Python utilities to help with common China travel challenges.

---

## Available Scripts

### 1. **Passport MRZ Converter** (`passport_mrz_converter.py`)

Converts your passport name into the format required by 12306 (China Railways).

**Problem Solved:** 12306 rejects foreign names because it doesn't parse First Name / Last Name separately. It needs MRZ format (LASTNAME<<FIRSTNAME).

**Browser UI (no install):** open **`mrz-tool.html`** on the site — same rules, runs entirely in the browser.

**Usage:**
```bash
python passport_mrz_converter.py John Smith
```

**Output:**
```
MRZ Format: SMITH<<JOHN
Copy this into 12306 account registration
```

**When to Use:**
- Before registering on 12306 for train tickets
- If 12306 rejects your name during verification
- When setting up backup identity in apps

**What It Does:**
- ✅ Removes accents (José → JOSE)
- ✅ Removes hyphens (Mary-Jane → MARYJANE)
- ✅ Converts to uppercase
- ✅ Formats as LASTNAME<<FIRSTNAME

---

### 1c. **SOP format audit** (`check_sop_format.py`)

Strict checks for guide markdown: required metadata, balanced HTML, phrase-cards, tables, orphan content after footers.

```bash
python scripts/check_sop_format.py
```

Optional bulk normalizer (metadata, badges, footer orphans):

```bash
python scripts/fix_sop_format.py
```

### 1b. **Full-text search index** (`build_fulltext_index.py`)

Exports SOP bodies for search:

1. `assets/search/fulltext.json` — client fallback used by `search-fulltext.html`
2. `_pagefind_src/` — HTML tree for Pagefind (gitignored scratch)

**Usage:**
```bash
# JSON + HTML export only
python scripts/build_fulltext_index.py

# Full Pagefind bundle (needs Node once: npm install)
npm run build:search
```

**When to Use:**
- After editing guide content that should be searchable
- Before release if `pagefind/` or `fulltext.json` is stale
- CI rebuilds `fulltext.json` on each health check

---

### 2. **Child Medication Dose Calculator** (`child_medication_calculator.py`)

Calculates appropriate medication dosage for children based on weight.

**Browser UI (no install):** open **`dose-calculator.html`** — same weight × mg/kg math, reference only.

**Problem Solved:** Unfamiliar with Chinese dosing systems; parents need reliable dose calculations for common children's medications.

**Usage:**
```bash
python child_medication_calculator.py --name "Ibuprofen" --weight 25 --dosage-per-kg 10
```

**Output:**
```
Medication:      Ibuprofen
Child's Weight:  25 kg
Dosage per kg:   10 mg/kg
Calculated Dose: 250 mg
```

**Common Medications & Dosages:**

| Medication | Dosage | Example |
|-----------|--------|---------|
| Paracetamol/Acetaminophen | 15 mg/kg | `--weight 20 --dosage-per-kg 15` |
| Ibuprofen | 10 mg/kg | `--weight 20 --dosage-per-kg 10` |
| Amoxicillin | 25 mg/kg | `--weight 20 --dosage-per-kg 25` |
| Cough Syrup | Varies | See package label |

**When to Use:**
- Before giving medication to your child
- To verify pharmacist's recommended dose
- If medication label is unclear

**Important:**
- Always consult a doctor or pharmacist
- This is for reference only, not medical advice
- Show calculation to pharmacist for verification
- Do not exceed recommended maximum daily dose

---

### 3. **Train Ticket Verification Checker** (`train_ticket_checker.py`)

Pre-verifies name format, travel date, and common issues before booking 12306 tickets.

**Problem Solved:** Foreign travelers don't know if their name will work on 12306 or if the travel date is within the booking window. Prevents wasted time and failed bookings.

**Usage:**
```bash
python train_ticket_checker.py --first-name John --last-name Smith --date 2026-05-15 --from BJS --to SHA
```

**Output:**
```
📝 NAME FORMAT CHECK:
   MRZ Format: SMITH<<JOHN
   ✅ Status: Name format is VALID for 12306

📅 TRAVEL DATE CHECK:
   Days Until Travel: 24
   Booking Status: ✅ GOOD - Available to book

✅ Ready to book! Your details appear to be correct.
```

**City Codes:**
```
BJS = Beijing        |  SHA = Shanghai      |  GZ = Guangzhou
CQ = Chongqing       |  CDW = Chengdu       |  HGH = Hangzhou
XA = Xi'an           |  SH = Shenyang       |  NJ = Nanjing
WH = Wuhan           |  JN = Jinan          |  CS = Changsha
```

**When to Use:**
- BEFORE you register on 12306
- If you're unsure about name format
- To check if travel date is in valid booking window
- To identify common issues early

**Booking Window:**
- ✅ **OPTIMAL:** 20-30 days before travel (tickets most available)
- ✅ **GOOD:** 1-20 days before travel (tickets available, some sold out)
- ⏰ **NOT YET:** 30+ days before travel (check back later)
- ⚠️ **RISKY:** Less than 24 hours (may fail, name verification incomplete)

---

### 4. **SOP Health Check (TTL Audit)** (`ttl_check.py`)

Scans all SOP files (skips hubs like `index.md` / `symptom-index.md`) and validates metadata freshness. Tags high-churn guides (`churn: high` or `ttl_days ≤ 30`) as `[HIGH]`. Exits `1` if expired or missing `metadata`.

### 5. **Catalog Sync** (`check_catalog.py`)

Fails if `index.json` and on-disk SOPs drift (missing file or uncatalogued guide).

### 6. **Static assets** (`check_static_assets.py`)

Fails if required entry HTML/CSS/JS files are missing (print packs, search, checklists).

**Problem Solved:** SOPs can become stale without anyone noticing. This script flags guides whose `last_validated` date has exceeded their `ttl_days` limit.

**Usage:**
```bash
pip install pyyaml  # one-time setup
python ttl_check.py
```

**Output:**
```
Checking docs/01-System-Setup/vpn-esim-payment.md...
  ✅ Valid (28/30 days remaining)
Checking docs/03-Emergency-DR/hospital-access.md...
  ⚠️ EXPIRED — last validated 95 days ago (TTL: 90 days)

Summary: 36 OK, 1 expired, 0 missing metadata
```

**When to Use:**
- Runs automatically every Monday via GitHub Actions
- Run locally before releases to catch stale content
- After bulk content updates to verify metadata

**Requires:** `PyYAML` (`pip install pyyaml` or `pip install -r requirements.txt`)

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- `PyYAML` (Required for `ttl_check.py`: `pip install pyyaml`)
- Other scripts use standard library only (no external modules needed)

### Running Scripts

**Option 1: Direct Python**
```bash
python passport_mrz_converter.py John Smith
python child_medication_calculator.py --name "Ibuprofen" --weight 25 --dosage-per-kg 10
python train_ticket_checker.py --first-name John --last-name Smith --date 2026-05-15
```

**Option 2: Make Executable (macOS/Linux)**
```bash
chmod +x *.py
./passport_mrz_converter.py John Smith
```

**Option 3: Run from Windows PowerShell**
```powershell
python .\passport_mrz_converter.py John Smith
```

---

## Example Scenarios

### Scenario 1: Preparing for Train Travel

```bash
# Step 1: Check if your name will work on 12306
python train_ticket_checker.py --first-name Maria --last-name Garcia --date 2026-05-20

# Step 2: Get the correct MRZ format
python passport_mrz_converter.py Maria Garcia

# Output: GARCIA<<MARIA
# Copy this into 12306 registration

# Step 3: Register on 12306, verify 24 hours later, then book
```

### Scenario 2: Child Gets Fever in China

```bash
# Need to know dose for 15kg child
python child_medication_calculator.py --name "Paracetamol" --weight 15 --dosage-per-kg 15

# Output: 225 mg per dose
# Show pharmacist this number to confirm
# Administer every 6-8 hours, max 3-4 times per day
```

### Scenario 3: Verify Multiple Family Members' Names

```bash
python train_ticket_checker.py --first-name John --last-name Smith --date 2026-05-15
python train_ticket_checker.py --first-name Mary --last-name Smith --date 2026-05-15
python train_ticket_checker.py --first-name Emma --last-name Smith --date 2026-05-15

# Book all family members together with verified names
```

---

## Troubleshooting

### "Command not found: python"
- Make sure Python is installed: `python --version`
- Try `python3` instead of `python`
- On Windows, use `python.exe` or PowerShell

### "ModuleNotFoundError"
- Most scripts use standard library only; `ttl_check.py` requires `PyYAML`
- Run `pip install -r requirements.txt` from the project root to install dependencies
- If errors persist, verify your Python installation: `python --version`

### Script Output Looks Wrong
- For name conversion: Double-check spelling and special characters
- For medication: Verify weight and dosage per kg are correct
- For ticket checker: Ensure date format is YYYY-MM-DD

---

## Future Scripts (Planned)

- 🩺 **SafeFeed Action** - [Already live](https://milesxlab.github.io/safefeed-action/) — global infant formula recall checker
- 🗺️ **Hospital Locator** - Find nearest hospital with English support by location
- 💰 **Currency Exchange Calculator** - Quick CNY conversions with current rates
- 🚕 **Didi Fare Estimator** - Pre-calculate ride-sharing costs
- 🏥 **Health Insurance Claim Helper** - Format medical documents for reimbursement

---

## Contributing

Found a bug or want to add a script?

- Test scripts thoroughly before submitting
- Include clear usage examples
- Document all assumptions and limitations
- Ensure cross-platform compatibility (Windows/macOS/Linux)

---

## Disclaimer

⚠️ **These tools are for informational purposes only:**

- **Medications:** Always consult a doctor or pharmacist before administering medication
- **Train Tickets:** 12306 rules change; verify current requirements on official website
- **Personal Information:** Only enter your own information; never share results with untrusted parties

---

**Author:** TechDadShanghai  
**Last Updated:** July 2026  
**License:** CC BY-NC 4.0