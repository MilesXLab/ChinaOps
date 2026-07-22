"""
v1.5 content pass:
- Insert Plain English summary blocks (if missing)
- Set metadata.scope where missing
- Inject a few high-value phrase-cards into key guides
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# path relative to repo → (plain_paragraphs, scope, optional phrase_card html after plain summary)
GUIDES: dict[str, dict] = {
    "docs/01-System-Setup/alipay-wechat-setup-foreigners.md": {
        "scope": "national",
        "plain": [
            "You need Alipay and usually WeChat Pay for daily life. Link a foreign Visa/Mastercard, finish identity checks, and keep a backup card ready.",
            "If payment fails, try the other app, another card, or cash — do not panic at the counter.",
        ],
        "phrase": None,
    },
    "docs/01-System-Setup/hotel-check-in.md": {
        "scope": "national",
        "plain": [
            "Hotels must register foreign guests with the police. Bring your passport and expect a scan or photo of it.",
            "If the front desk says they cannot accept foreigners, ask for another hotel or call your booking platform support.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">我有预订</div>
  <div class="py">wǒ yǒu yùdìng</div>
  <div class="en">I have a reservation.</div>
</div>
""",
    },
    "docs/01-System-Setup/mobile-number-and-activation.md": {
        "scope": "national",
        "plain": [
            "A Chinese number helps with SMS codes for apps and delivery. Choose eSIM before the trip or a physical SIM after landing.",
            "Keep your home number working for bank OTPs if you can.",
        ],
        "phrase": None,
    },
    "docs/01-System-Setup/pharmacy-and-medications.md": {
        "scope": "national",
        "plain": [
            "Many common cold and pain medicines are sold over the counter. Know the Chinese name or show a photo of the box.",
            "Some drugs need a hospital prescription — do not argue at the counter; go to a clinic.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">我需要退烧药</div>
  <div class="py">wǒ xūyào tuìshāo yào</div>
  <div class="en">I need fever medicine.</div>
</div>
""",
    },
    "docs/01-System-Setup/power-bank-rules.md": {
        "scope": "national",
        "plain": [
            "Power banks go in carry-on, not checked bags. Domestic flights may require CCC marks and a scannable traceability code.",
            "If security rejects your bank, buy a compliant one after security or in the city — do not force the old one through.",
        ],
        "phrase": None,
    },
    "docs/01-System-Setup/sim-card-options.md": {
        "scope": "national",
        "plain": [
            "Compare China Mobile / Unicom / Telecom tourist SIMs and travel eSIMs by price, hotspot support, and whether they bypass the firewall.",
            "Register with your passport; keep the receipt.",
        ],
        "phrase": None,
    },
    "docs/01-System-Setup/translation-tools.md": {
        "scope": "national",
        "plain": [
            "Download offline translation before you lose data. Screenshots of hotel address and key phrases beat live typing in a rush.",
            "Point-camera translate helps menus; for medical or legal talk, use a human or hospital interpreter when possible.",
        ],
        "phrase": None,
    },
    "docs/01-System-Setup/visa-and-entry.md": {
        "scope": "national",
        "plain": [
            "Check if your passport gets visa-free entry for your stay length. Complete the digital arrival card early to avoid queue stress.",
            "Rules change by nationality and pilot programs — confirm on official sources before you fly.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/car-rental.md": {
        "scope": "national",
        "plain": [
            "Driving needs the right license paperwork. Many visitors use a chauffeur or Didi instead of self-drive.",
            "If you rent, clarify insurance, tolls, and where you may not park.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/international-domestic-transit.md": {
        "scope": "national",
        "plain": [
            "Changing from an international to a domestic flight can mean leaving security, collecting bags, and re-checking in.",
            "Leave long buffers; do not assume airside transfer like in some other countries.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/lost-luggage.md": {
        "scope": "national",
        "plain": [
            "Report delayed bags at the airline desk before you leave the airport. Keep the PIR reference number.",
            "Photograph essentials you still carry; ask about delivery to your hotel.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/maps-and-toilets.md": {
        "scope": "national",
        "plain": [
            "Google Maps is weak offline for China navigation. Use Amap (Gaode) or Apple Maps with Chinese address text.",
            "Public toilets are common in malls and metro stations; carry tissues.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">请问卫生间在哪里？</div>
  <div class="py">qǐngwèn wèishēngjiān zài nǎlǐ?</div>
  <div class="en">Where is the toilet?</div>
</div>
""",
    },
    "docs/02-Daily-Runtime/public-transport-tips.md": {
        "scope": "national",
        "plain": [
            "Metro is usually the fastest city option. Pay with a transit QR in Alipay/WeChat or a physical card.",
            "Keep bags close in crowds; follow exit numbers, not only station names.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/shanghai-attractions-guide.md": {
        "scope": "shanghai",
        "plain": [
            "Plan big sights with booking apps and weekday mornings when you can. Bund, museums, and theme parks need different ticket rules.",
            "This guide is Shanghai-first; other cities use similar apps but different queues.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/shanghai-food-guide.md": {
        "scope": "shanghai",
        "plain": [
            "Order with app photos or point at the menu. Xiaolongbao and local breakfast spots get crowded — go early.",
            "Shanghai-focused; flavors and chains differ elsewhere.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">不要香菜</div>
  <div class="py">bú yào xiāngcài</div>
  <div class="en">No cilantro, please.</div>
</div>
""",
    },
    "docs/02-Daily-Runtime/shanghai-local-hacks.md": {
        "scope": "shanghai",
        "plain": [
            "Resident-style tips: delivery apps, shared bikes, quieter hours, and stroller-friendly routes.",
            "Verify hours after holidays; Shanghai-specific.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/shanghai-vegan-guide.md": {
        "scope": "shanghai",
        "plain": [
            "Say clearly you eat no meat, fish, or animal broth. Temple and vegan restaurants are safer than standard kitchens.",
            "Use short Chinese phrases; Shanghai has more vegan options than smaller cities.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">我吃素，不要肉和鱼</div>
  <div class="py">wǒ chī sù, bú yào ròu hé yú</div>
  <div class="en">I am vegetarian — no meat or fish.</div>
</div>
""",
    },
    "docs/02-Daily-Runtime/shanghai-visual-signs-guide.md": {
        "scope": "national",
        "plain": [
            "Learn a few symbols for metro, toilets, taxis, and nursing rooms so you can move without reading full Chinese.",
            "Symbols are mostly national; examples use Shanghai photos where noted.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/shanghai-weather-guide.md": {
        "scope": "shanghai",
        "plain": [
            "Pack for humidity, sudden rain, and winter cold snaps. Check AQI on bad air days and limit outdoor time with kids.",
            "Typhoon season needs flexible plans — Shanghai-focused calendar.",
        ],
        "phrase": None,
    },
    "docs/02-Daily-Runtime/taxi-payment.md": {
        "scope": "national",
        "plain": [
            "Prefer Didi or official taxi stands. Pay by QR when possible; refuse unsolicited “helpers” in arrival halls.",
            "Screenshot the plate number before the ride starts.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">请打表</div>
  <div class="py">qǐng dǎ biǎo</div>
  <div class="en">Please use the meter.</div>
</div>
""",
    },
    "docs/02-Daily-Runtime/train-ticket-trap.md": {
        "scope": "national",
        "plain": [
            "12306 needs your name in MRZ-style format. Register early, pass real-name checks, then book in the open window.",
            "Use the passport MRZ helper script if registration fails on name format.",
        ],
        "phrase": None,
    },
    "docs/03-Emergency-DR/emergency-contacts-card.md": {
        "scope": "national",
        "plain": [
            "Print or screenshot police, ambulance, embassy, and your hotel address before you need them.",
            "Share the card with family traveling with you.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">请帮我叫救护车</div>
  <div class="py">qǐng bāng wǒ jiào jiùhùchē</div>
  <div class="en">Please call an ambulance for me.</div>
</div>
""",
    },
    "docs/03-Emergency-DR/hospital-access.md": {
        "scope": "national",
        "plain": [
            "For serious issues go to a large hospital or international clinic. Bring passport and payment method; expect registration first.",
            "English help varies — use translation apps and write symptoms down.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">我要看急诊</div>
  <div class="py">wǒ yào kàn jízhěn</div>
  <div class="en">I need the emergency department.</div>
</div>
""",
    },
    "docs/03-Emergency-DR/lost-bank-card.md": {
        "scope": "national",
        "plain": [
            "Freeze the card in your bank app, then freeze linked Alipay/WeChat wallets if needed.",
            "Keep one backup payment path (second card or cash) before you travel.",
        ],
        "phrase": None,
    },
    "docs/03-Emergency-DR/lost-phone.md": {
        "scope": "national",
        "plain": [
            "Lock or erase the phone remotely if you can. Freeze payments tied to that device and suspend the SIM.",
            "Your phone is also your map and wallet — restore access in that order.",
        ],
        "phrase": None,
    },
    "docs/03-Emergency-DR/network-outage.md": {
        "scope": "national",
        "plain": [
            "When VPN or data dies, switch network path: other eSIM, hotel Wi‑Fi, offline maps, and cash.",
            "Do not wait until 1% battery to fix connectivity.",
        ],
        "phrase": None,
    },
    "docs/03-Emergency-DR/prescription-refill.md": {
        "scope": "national",
        "plain": [
            "Bring enough chronic meds for the whole trip plus a paper prescription and generic drug names.",
            "Refills may need a Chinese doctor visit — plan extra days.",
        ],
        "phrase": None,
    },
    "docs/03-Emergency-DR/safety-and-common-scams.md": {
        "scope": "national",
        "plain": [
            "Most cities are safe for normal tourism. Watch tea-house scams, unofficial taxis, and “too friendly” strangers near tourist spots.",
            "If it feels rushed or secret, walk away.",
        ],
        "phrase": None,
    },
    "docs/03-Emergency-DR/shanghai-safety-guide.md": {
        "scope": "shanghai",
        "plain": [
            "Shanghai is generally safe; focus on petty theft awareness and social-engineering scams in tourist zones.",
            "Use official taxis/Didi at night; Shanghai-specific notes included.",
        ],
        "phrase": None,
    },
    "docs/04-Parenting-Patch/baby-survival-master-runbook.md": {
        "scope": "national",
        "plain": [
            "Plan milk, diapers, sleep, and transport with kids before peak hours. Malls often have nursing rooms.",
            "Many tips are national; Shanghai examples appear where useful.",
        ],
        "phrase": None,
    },
    "docs/04-Parenting-Patch/diapers-and-stores.md": {
        "scope": "national",
        "plain": [
            "Buy diapers at large pharmacies, supermarkets, or delivery apps. Know your size in cm/weight, not only brand names.",
            "Stock up before holidays when shops thin out.",
        ],
        "phrase": None,
    },
    "docs/04-Parenting-Patch/food-allergies-and-dietary-restrictions.md": {
        "scope": "national",
        "plain": [
            "Carry a written allergy card in Chinese. Show it before ordering; do not rely on English menus alone.",
            "When unsure, choose simpler dishes or cook at the hotel.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">我对花生过敏</div>
  <div class="py">wǒ duì huāshēng guòmǐn</div>
  <div class="en">I am allergic to peanuts.</div>
</div>
""",
    },
    "docs/04-Parenting-Patch/milk-recall-check.md": {
        "scope": "national",
        "plain": [
            "Check formula brand and batch before you open a new can, especially after any global recall news.",
            "Use official notices or SafeFeed Action; when unsure, do not feed that can.",
        ],
        "phrase": None,
    },
    "docs/04-Parenting-Patch/nursing-rooms.md": {
        "scope": "national",
        "plain": [
            "Look for nursing room signs in malls, museums, and big stations. Ask staff with a short Chinese phrase if needed.",
            "Facilities vary widely — have a backup quiet corner plan.",
        ],
        "phrase": """
<div class="phrase-card">
  <div class="zh">母婴室在哪里？</div>
  <div class="py">mǔyīng shì zài nǎlǐ?</div>
  <div class="en">Where is the nursing room?</div>
</div>
""",
    },
    "docs/05-Event-Operations/holiday-survival-guide.md": {
        "scope": "national",
        "plain": [
            "Golden Week and Spring Festival mean sold-out trains and crowded attractions. Book early or travel against the peak.",
            "Confirm official holiday dates and make-up workdays each year — they change.",
        ],
        "phrase": None,
    },
}


def build_summary(plain: list[str], scope: str) -> str:
    scope_label = "Shanghai-first" if scope == "shanghai" else "national"
    badges = f'<span class="scope-badge">Scope: {scope_label}</span>'
    if scope == "shanghai":
        badges += ' <span class="scope-badge">Other cities may differ</span>'
    paras = "\n".join(f"  <p>{p}</p>" for p in plain)
    return (
        '<div class="plain-summary">\n'
        '  <strong class="plain-summary-label">Plain English</strong>\n'
        f"{paras}\n"
        f"  <p>{badges}</p>\n"
        "</div>\n\n"
    )


def ensure_scope_in_frontmatter(text: str, scope: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    fm, body = parts[1], parts[2]
    if re.search(r"^\s*scope:\s*", fm, re.M):
        fm = re.sub(r"^\s*scope:\s*.*$", f'  scope: "{scope}"', fm, count=1, flags=re.M)
    elif "metadata:" in fm:
        # insert under metadata block after stability or at end of metadata-ish area
        if re.search(r"validation_method:", fm):
            fm = re.sub(
                r"(validation_method:\s*[\"']?[\w_]+[\"']?\s*\n)",
                rf'\1  scope: "{scope}"\n',
                fm,
                count=1,
            )
        else:
            fm = fm.rstrip() + f'\n  scope: "{scope}"\n'
    else:
        return text
    # avoid double-indent issues if scope already at root
    fm = re.sub(r"\n  scope:", r"\n  scope:", fm)
    return f"---{fm}---{body}"


def insert_after_h1(text: str, block: str) -> str:
    if "plain-summary" in text:
        return text
    # After first markdown H1 line
    m = re.search(r"(^# .+\n)", text, re.M)
    if not m:
        return text
    idx = m.end()
    return text[:idx] + "\n" + block + text[idx:]


def inject_phrase(text: str, phrase_html: str | None) -> str:
    if not phrase_html or "phrase-card" in text:
        return text
    # Prefer after plain-summary block
    if "plain-summary" in text:
        return re.sub(
            r"(</div>\n\n)",
            r"\1" + phrase_html.strip() + "\n\n",
            text,
            count=1,
        )
    return text


def main() -> None:
    changed = 0
    for rel, cfg in GUIDES.items():
        p = ROOT / rel
        if not p.exists():
            print("missing", rel)
            continue
        original = p.read_text(encoding="utf-8")
        text = original
        text = ensure_scope_in_frontmatter(text, cfg["scope"])
        summary = build_summary(cfg["plain"], cfg["scope"])
        text = insert_after_h1(text, summary)
        text = inject_phrase(text, cfg.get("phrase"))
        # Ensure existing OK files still get scope in metadata
        if text != original:
            p.write_text(text, encoding="utf-8")
            changed += 1
            print("updated", rel)
        else:
            print("unchanged", rel)

    # Also set scope on already-summarized guides
    extras = {
        "docs/01-System-Setup/landing-protocol.md": "national",
        "docs/01-System-Setup/vpn-esim-payment.md": "national",
        "docs/03-Emergency-DR/lost-passport.md": "national",
    }
    for rel, scope in extras.items():
        p = ROOT / rel
        original = p.read_text(encoding="utf-8")
        text = ensure_scope_in_frontmatter(original, scope)
        if text != original:
            p.write_text(text, encoding="utf-8")
            changed += 1
            print("scope-only", rel)

    print("total changed files:", changed)


if __name__ == "__main__":
    main()
