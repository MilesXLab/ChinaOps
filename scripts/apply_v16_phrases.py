"""Inject phrase-cards into SOPs that still lack them (v1.6)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PHRASES: dict[str, str] = {
    "docs/01-System-Setup/alipay-wechat-setup-foreigners.md": """
<div class="phrase-card">
  <div class="zh">可以用支付宝吗？</div>
  <div class="py">kěyǐ yòng Zhīfùbǎo ma?</div>
  <div class="en">Can I pay with Alipay?</div>
</div>
""",
    "docs/01-System-Setup/mobile-number-and-activation.md": """
<div class="phrase-card">
  <div class="zh">我要办一张电话卡</div>
  <div class="py">wǒ yào bàn yī zhāng diànhuà kǎ</div>
  <div class="en">I want to get a phone SIM card.</div>
</div>
""",
    "docs/01-System-Setup/power-bank-rules.md": """
<div class="phrase-card">
  <div class="zh">充电宝可以带上飞机吗？</div>
  <div class="py">chōngdiàn bǎo kěyǐ dài shàng fēijī ma?</div>
  <div class="en">Can I take this power bank on the plane?</div>
</div>
""",
    "docs/01-System-Setup/sim-card-options.md": """
<div class="phrase-card">
  <div class="zh">有没有上网流量套餐？</div>
  <div class="py">yǒu méiyǒu shàngwǎng liúliàng tàocān?</div>
  <div class="en">Do you have a mobile data plan?</div>
</div>
""",
    "docs/01-System-Setup/translation-tools.md": """
<div class="phrase-card">
  <div class="zh">请说慢一点</div>
  <div class="py">qǐng shuō màn yīdiǎn</div>
  <div class="en">Please speak more slowly.</div>
</div>
""",
    "docs/01-System-Setup/visa-and-entry.md": """
<div class="phrase-card">
  <div class="zh">我是免签入境</div>
  <div class="py">wǒ shì miǎnqiān rùjìng</div>
  <div class="en">I am entering visa-free.</div>
</div>
""",
    "docs/01-System-Setup/vpn-esim-payment.md": """
<div class="phrase-card">
  <div class="zh">网络连不上</div>
  <div class="py">wǎngluò lián bu shàng</div>
  <div class="en">The network will not connect.</div>
</div>
""",
    "docs/02-Daily-Runtime/car-rental.md": """
<div class="phrase-card">
  <div class="zh">我有国际驾照</div>
  <div class="py">wǒ yǒu guójì jiàzhào</div>
  <div class="en">I have an international driving permit.</div>
</div>
""",
    "docs/02-Daily-Runtime/international-domestic-transit.md": """
<div class="phrase-card">
  <div class="zh">国内航班在哪里值机？</div>
  <div class="py">guónèi hángbān zài nǎlǐ zhíjī?</div>
  <div class="en">Where do I check in for domestic flights?</div>
</div>
""",
    "docs/02-Daily-Runtime/lost-luggage.md": """
<div class="phrase-card">
  <div class="zh">我的行李没有出来</div>
  <div class="py">wǒ de xíngli méiyǒu chūlái</div>
  <div class="en">My luggage did not come out.</div>
</div>
""",
    "docs/02-Daily-Runtime/public-transport-tips.md": """
<div class="phrase-card">
  <div class="zh">这是哪一站？</div>
  <div class="py">zhè shì nǎ yī zhàn?</div>
  <div class="en">Which station is this?</div>
</div>
""",
    "docs/02-Daily-Runtime/shanghai-attractions-guide.md": """
<div class="phrase-card">
  <div class="zh">门票在哪里买？</div>
  <div class="py">ménpiào zài nǎlǐ mǎi?</div>
  <div class="en">Where can I buy tickets?</div>
</div>
""",
    "docs/02-Daily-Runtime/shanghai-local-hacks.md": """
<div class="phrase-card">
  <div class="zh">怎么用这个App？</div>
  <div class="py">zěnme yòng zhège App?</div>
  <div class="en">How do I use this app?</div>
</div>
""",
    "docs/02-Daily-Runtime/shanghai-visual-signs-guide.md": """
<div class="phrase-card">
  <div class="zh">地铁站怎么走？</div>
  <div class="py">dìtiě zhàn zěnme zǒu?</div>
  <div class="en">How do I get to the metro station?</div>
</div>
""",
    "docs/02-Daily-Runtime/shanghai-weather-guide.md": """
<div class="phrase-card">
  <div class="zh">今天空气质量怎么样？</div>
  <div class="py">jīntiān kōngqì zhìliàng zěnmeyàng?</div>
  <div class="en">How is the air quality today?</div>
</div>
""",
    "docs/02-Daily-Runtime/train-ticket-trap.md": """
<div class="phrase-card">
  <div class="zh">我要买高铁票</div>
  <div class="py">wǒ yào mǎi gāotiě piào</div>
  <div class="en">I want to buy a high-speed train ticket.</div>
</div>
""",
    "docs/03-Emergency-DR/lost-bank-card.md": """
<div class="phrase-card">
  <div class="zh">我的银行卡丢了</div>
  <div class="py">wǒ de yínháng kǎ diū le</div>
  <div class="en">I lost my bank card.</div>
</div>
""",
    "docs/03-Emergency-DR/lost-passport.md": """
<div class="phrase-card">
  <div class="zh">我的护照丢了</div>
  <div class="py">wǒ de hùzhào diū le</div>
  <div class="en">I lost my passport.</div>
</div>
""",
    "docs/03-Emergency-DR/lost-phone.md": """
<div class="phrase-card">
  <div class="zh">我的手机丢了</div>
  <div class="py">wǒ de shǒujī diū le</div>
  <div class="en">I lost my phone.</div>
</div>
""",
    "docs/03-Emergency-DR/network-outage.md": """
<div class="phrase-card">
  <div class="zh">这里有没有Wi‑Fi？</div>
  <div class="py">zhèlǐ yǒu méiyǒu Wi‑Fi?</div>
  <div class="en">Is there Wi‑Fi here?</div>
</div>
""",
    "docs/03-Emergency-DR/prescription-refill.md": """
<div class="phrase-card">
  <div class="zh">我需要这个药的处方</div>
  <div class="py">wǒ xūyào zhège yào de chǔfāng</div>
  <div class="en">I need a prescription for this medicine.</div>
</div>
""",
    "docs/03-Emergency-DR/safety-and-common-scams.md": """
<div class="phrase-card">
  <div class="zh">不需要，谢谢</div>
  <div class="py">bù xūyào, xièxie</div>
  <div class="en">No need, thank you. (polite refusal)</div>
</div>
""",
    "docs/03-Emergency-DR/shanghai-safety-guide.md": """
<div class="phrase-card">
  <div class="zh">请帮我报警</div>
  <div class="py">qǐng bāng wǒ bào jǐng</div>
  <div class="en">Please help me call the police.</div>
</div>
""",
    "docs/04-Parenting-Patch/baby-survival-master-runbook.md": """
<div class="phrase-card">
  <div class="zh">有没有儿童座椅？</div>
  <div class="py">yǒu méiyǒu értóng zuòyǐ?</div>
  <div class="en">Do you have a child seat?</div>
</div>
""",
    "docs/04-Parenting-Patch/diapers-and-stores.md": """
<div class="phrase-card">
  <div class="zh">纸尿裤在哪里？</div>
  <div class="py">zhǐniàokù zài nǎlǐ?</div>
  <div class="en">Where are the diapers?</div>
</div>
""",
    "docs/04-Parenting-Patch/milk-recall-check.md": """
<div class="phrase-card">
  <div class="zh">这个奶粉批次安全吗？</div>
  <div class="py">zhège nǎifěn pīcì ānquán ma?</div>
  <div class="en">Is this formula batch safe?</div>
</div>
""",
    "docs/05-Event-Operations/holiday-survival-guide.md": """
<div class="phrase-card">
  <div class="zh">现在人太多了</div>
  <div class="py">xiànzài rén tài duō le</div>
  <div class="en">There are too many people right now.</div>
</div>
""",
}


def inject(text: str, card: str) -> str:
    if "phrase-card" in text:
        return text
    card = card.strip() + "\n\n"
    if "</div>\n\n" in text and "plain-summary" in text:
        # after first plain-summary close
        return re.sub(
            r"(</div>\n\n)",
            r"\1" + card,
            text,
            count=1,
        )
    m = re.search(r"(^# .+\n)", text, re.M)
    if m:
        return text[: m.end()] + "\n" + card + text[m.end() :]
    return text


def main() -> None:
    n = 0
    for rel, card in PHRASES.items():
        p = ROOT / rel
        if not p.exists():
            print("missing", rel)
            continue
        t = p.read_text(encoding="utf-8")
        nt = inject(t, card)
        if nt != t:
            p.write_text(nt, encoding="utf-8")
            n += 1
            print("added", rel)
        else:
            print("skip", rel)
    print("done", n)


if __name__ == "__main__":
    main()
