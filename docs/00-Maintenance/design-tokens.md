---
layout: guide
title: "Design Tokens & UI Components"
description: "Contributor reference for ChinaOps CSS tokens and shared UI components."
---

# Design Tokens & UI Components

**Plain English:** When you change how the site looks, use these names — do not invent new hex colors in HTML.

**Source of truth:** `assets/css/chinaops.css`  
**Behavior:** `assets/js/chinaops.js`

---

## Color tokens (`:root`)

| Token | Role | Use for |
|-------|------|---------|
| `--fg-1` | Primary text | Headings, body emphasis |
| `--fg-2` | Secondary text | Body, table cells |
| `--fg-3` | Muted text | Hints, labels (check contrast) |
| `--bg-base` | Page background | Home, hubs |
| `--bg-raised` | Cards / panels | Sections, phrase cards |
| `--bg-subtle` | Soft fill | Table headers, chips |
| `--brand` | Brand / links | Primary buttons, nav active |
| `--success` | Success | Verified, checklist complete |
| `--warning` | Caution | Symptom “broke?” paths |
| `--critical` | Danger / emergency | Emergency, print urgency |
| `--info` | Informational | Tips, callouts |
| `--border-default` | Borders | Cards, tables |

Semantic soft backgrounds: `--bg-critical-soft`, `--bg-warning-soft`, `--bg-success-soft`, `--bg-info-soft`, `--bg-brand-soft`.

---

## Spacing & type

| Token family | Notes |
|--------------|--------|
| `--space-1` … `--space-8` | 4px scale (4 → 48) |
| `--radius-sm/md/lg/pill` | Corners |
| `--text-xs` … `--text-3xl` | Type scale |
| `--font-sans` | System stack (China-friendly, no Google Fonts) |
| `--dur-fast` / `--dur-med` | Motion; honor `prefers-reduced-motion` |

---

## Shared components (use these classes)

| Class | Purpose |
|-------|---------|
| `.plain-summary` | ESL summary at top of every SOP |
| `.phrase-card` + `.zh` / `.py` / `.en` | One spoken phrase |
| `.callout` + `.callout-info/warning/critical/success` | Status blocks |
| `.scope-badge` | national / shanghai-first |
| `.path-card` + `.tone-*` | Home task cards |
| `.filter-chip` | Symptom category chips |
| `.symptom-search` | Symptom search field |
| `.btn` + `.btn-brand/critical/dark/success` | Buttons |
| `.print-option` | Print hub cards |
| `.guide-action-bar` | Sticky Symptom · Print · Report |
| `.mobile-toc` | Mobile H2 jump strip |

### Phrase card (required shape)

```html
<div class="phrase-card">
  <div class="zh">中文</div>
  <div class="py">pīn yīn</div>
  <div class="en">English</div>
</div>
```

See also: [Phrase style guide](../phrase-style-guide/).

---

## Layout shells

| Surface | Body class / files |
|---------|-------------------|
| Home & hubs | `home-body` + `home-wrap` on static HTML |
| Guides | `_layouts/guide.html` → `docs-body` |
| Print HTML | Standalone CSS in each print-*.html (print-optimized) |

---

## Accessibility rules

1. Interactive targets ≥ ~40–44px tall on mobile (chips, CTAs, checklist).  
2. Keep `:focus-visible` outlines — do not remove.  
3. Critical actions use **color + text**, not color alone.  
4. Symptom list must remain readable **without JS**.  
5. Prefer system fonts for reliability inside China.

---

## Do not

- Paste random hex in `index.html` inline styles for new UI.  
- Add Google Fonts or heavy animation libraries.  
- Reintroduce marquee / auto-scrolling news tickers.  
- Ship a second conflicting stylesheet for guides.

---

## Related entry points

| Page | Path |
|------|------|
| Home | `index.html` |
| Print Hub | `print-hub.html` |
| Pre-flight checklist | `preflight-checklist.html` |
| Symptom Index | `docs/symptom-index.md` |

[← High-churn registry](../high-churn-registry/)
