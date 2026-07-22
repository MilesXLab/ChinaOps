#!/usr/bin/env python3
"""Generate images/og-default.png (1200x630) for social previews."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), "#0f172a")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 12], fill="#5b6fd8")
    draw.rectangle([0, h - 80, w, h], fill="#1e293b")
    draw.rounded_rectangle([64, 120, 280, 340], radius=24, fill="#5b6fd8")
    try:
        font_lg = ImageFont.truetype("arial.ttf", 72)
        font_md = ImageFont.truetype("arial.ttf", 40)
        font_sm = ImageFont.truetype("arial.ttf", 28)
        font_xl = ImageFont.truetype("arialbd.ttf", 88)
    except OSError:
        font_lg = font_md = font_sm = font_xl = ImageFont.load_default()

    draw.text((100, 190), "CO", fill="white", font=font_xl)
    draw.text((320, 150), "ChinaOps", fill="#f8fafc", font=font_lg)
    draw.text((320, 250), "Technical runbook for travelers", fill="#cbd5e1", font=font_md)
    draw.text((320, 320), "& parents in China", fill="#cbd5e1", font=font_md)
    draw.text(
        (64, 560),
        "49 guides  ·  free  ·  offline print packs  ·  browser tools",
        fill="#94a3b8",
        font=font_sm,
    )
    out = ROOT / "images" / "og-default.png"
    out.parent.mkdir(exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
