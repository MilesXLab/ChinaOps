---
layout: guide
title: "Phrase Card Style Guide"
---

# Phrase Card Style Guide

**Audience:** contributors adding Chinese phrases to ChinaOps SOPs.

**Goal:** one clear phrase per real situation — useful under stress, not a phrasebook dump.

---

## Required HTML shape

```html
<div class="phrase-card">
  <div class="zh">中文句子</div>
  <div class="py">pīn yīn with tone marks when possible</div>
  <div class="en">Short plain English.</div>
</div>
```

CSS for `.phrase-card` lives in `assets/css/chinaops.css`. Do not invent alternate class names.

---

## Rules (must)

| Rule | Why |
|------|-----|
| **One card per scene** | Multiple cards for the same need confuse printers and readers |
| **Spoken language** | Prefer what people say at a counter, not textbook formal |
| **Short English** | ESL + stress: under ~12 English words |
| **No dual meanings** | One English gloss only |
| **Place after Plain English** | Readers see meaning first, then the phrase |
| **Match the guide** | Taxi guide → meter phrase; do not paste random food phrases |

---

## Rules (should)

- Use **tone-marked pinyin** (`qǐng`) when you can; spaces between syllables.
- Keep **full-width Chinese punctuation** natural: `？` `。` `！`
- Prefer **polite forms** (`请…`) for service staff.
- If the phrase is Shanghai-only slang, mark scope in the surrounding text.

---

## Do not

- Do not add three synonyms for the same action on one page.
- Do not use machine-translated nonsense without a native or field check.
- Do not put secrets, personal data, or hotel-specific numbers inside phrase cards.
- Do not style with inline CSS; use the shared component.

---

## Dedup checklist before PR

1. Search the repo for the same `zh` string.
2. If it already exists on the **print pack** or a more central emergency guide, link there instead of copying.
3. Update repo-root `print-pack.html` only for **high-frequency** phrases used offline.

---

## Good vs weak examples

**Good**
```html
<div class="phrase-card">
  <div class="zh">请打表</div>
  <div class="py">qǐng dǎ biǎo</div>
  <div class="en">Please use the meter.</div>
</div>
```

**Weak**
```html
<div class="phrase-card">
  <div class="zh">劳驾请您使用计价器进行本次行程的计费工作好吗</div>
  <div class="py">very long formal sentence</div>
  <div class="en">Would you be so kind as to utilize the taximeter for the purpose of calculating the fare for this journey?</div>
</div>
```

---

## Related

- Template: `TEMPLATE_ENHANCED_SOP.md` (repo root)
- Print pack: [Print Pack](../../print-pack/) · raw file `print-pack.html`
- Contributing: `CONTRIBUTING.md` (repo root)

[← High-churn registry](../high-churn-registry/)
