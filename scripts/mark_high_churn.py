"""Mark high-churn SOPs with ttl_days=30 and churn: high."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "docs/01-System-Setup/vpn-esim-payment.md",
    "docs/01-System-Setup/alipay-wechat-setup-foreigners.md",
    "docs/01-System-Setup/visa-and-entry.md",
    "docs/01-System-Setup/power-bank-rules.md",
    "docs/05-Event-Operations/holiday-survival-guide.md",
    "docs/04-Parenting-Patch/milk-recall-check.md",
]


def main() -> None:
    for rel in FILES:
        p = ROOT / rel
        t = p.read_text(encoding="utf-8")
        t = re.sub(r"ttl_days:\s*\d+", "ttl_days: 30", t, count=1)
        if re.search(r"^\s*churn:\s*", t, re.M) is None:
            t = re.sub(r"(ttl_days:\s*30\n)", r"\1  churn: high\n", t, count=1)
        else:
            t = re.sub(r"churn:\s*\S+", "churn: high", t, count=1)
        t = re.sub(
            r'stability_status:\s*"?stable"?',
            'stability_status: "critical"',
            t,
            count=1,
        )
        p.write_text(t, encoding="utf-8")
        print("updated", rel)


if __name__ == "__main__":
    main()
