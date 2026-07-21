"""Rebuild index.html using the shared design system (keeps guide tables)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = (ROOT / "index.html").read_text(encoding="utf-8")

# Extract library tables block
m = re.search(
    r"<!-- Full Guide Library -->(.*?)<!-- Why Open Source",
    OLD,
    re.S,
)
if not m:
    raise SystemExit("Could not find Full Guide Library section")

lib = m.group(1)
# Drop outer section wrapper if present
lib = re.sub(r'^\s*<div class="section">\s*', "", lib)
lib = re.sub(r"\s*</div>\s*$", "", lib)

# Category headings → bilingual
subs = [
    (
        r'<h3 style="color: #667eea; margin-top: 30px; margin-bottom: 15px;">✈️ System Setup \(10 Guides\)</h3>\s*'
        r'<p style="color: #666; margin-bottom: 15px;">Get your essentials working: phone, VPN, payments, medications</p>',
        '<h3 class="cat-heading">✈️ System Setup (10 guides)'
        '<span class="plain">Before you arrive — phone, VPN, payments</span></h3>',
    ),
    (
        r'<h3 style="color: #667eea; margin-top: 30px; margin-bottom: 15px;">🚗 Daily Runtime \(13 Guides\)</h3>\s*'
        r'<p style="color: #666; margin-bottom: 15px;">Navigate cities: trains, taxis, maps, public transport</p>',
        '<h3 class="cat-heading">🚗 Daily Runtime (13 guides)'
        '<span class="plain">Day-to-day life — trains, taxis, maps</span></h3>',
    ),
    (
        r'<h3 style="color: #667eea; margin-top: 30px; margin-bottom: 15px;">🚨 Emergency/DR \(9 Guides\)</h3>\s*'
        r'<p style="color: #666; margin-bottom: 15px;">When things go wrong: hospitals, lost documents, outages</p>',
        '<h3 class="cat-heading">🚨 Emergency (9 guides)'
        '<span class="plain">When things go wrong — hospital, lost docs</span></h3>',
    ),
    (
        r'<h3 style="color: #667eea; margin-top: 30px; margin-bottom: 15px;">👨‍👩‍👧 Parenting \(5 Guides\)</h3>\s*'
        r'<p style="color: #666; margin-bottom: 15px;">Child-specific challenges: supplies, allergies, safety</p>',
        '<h3 class="cat-heading">👨‍👩‍👧 Parenting (5 guides)'
        '<span class="plain">Traveling with kids — supplies and safety</span></h3>',
    ),
    (
        r'<h3 style="color: #667eea; margin-top: 30px; margin-bottom: 15px;">🏮 Event Operations \(1 Guide\)</h3>\s*'
        r'<p style="color: #666; margin-bottom: 15px;">2026 Golden Week schedules and holiday survival</p>',
        '<h3 class="cat-heading">🏮 Events (1 guide)'
        '<span class="plain">Holidays and peak travel</span></h3>',
    ),
    (
        r'<h3 style="color: #ec4899; margin-top: 30px; margin-bottom: 15px;">🛠️ Helper Tools \(Web-Only\)</h3>\s*'
        r'<p style="color: #666; margin-bottom: 15px;">Standalone technical nodes for specific safety & formatting checks\s*</p>',
        '<h3 class="cat-heading">🛠️ Helper tools'
        '<span class="plain">Optional utilities (web or local scripts)</span></h3>',
    ),
]

for pat, repl in subs:
    lib, n = re.subn(pat, repl, lib, count=1, flags=re.S)
    if n != 1:
        print(f"WARN: pattern matched {n} times: {pat[:60]}...")

# Tool cards → simpler markup
lib = re.sub(
    r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); gap: 15px;">',
    '<div class="tool-grid">',
    lib,
    count=1,
)
lib = re.sub(
    r'<div style="padding: 20px; border: 2px solid #f9a8d4; border-radius: 12px; background: #fff;">',
    '<div class="tool-card">',
    lib,
)
lib = re.sub(
    r'<div style="padding: 20px; border: 2px solid #667eea; border-radius: 12px; background: #fff;">',
    '<div class="tool-card">',
    lib,
)
lib = re.sub(
    r'<h4 style="color: #ec4899; margin-bottom: 8px;">',
    '<h4>',
    lib,
)
lib = re.sub(
    r'<h4 style="color: #667eea; margin-bottom: 8px;">',
    '<h4>',
    lib,
)
lib = re.sub(
    r'<p style="font-size: 0\.9em; color: #666; margin-bottom: 12px;">',
    '<p class="path-desc">',
    lib,
)
lib = re.sub(
    r'style="display: inline-block; padding: 6px 15px; background: #ec4899; color: white; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0\.85em;"',
    'class="btn btn-critical"',
    lib,
)
lib = re.sub(
    r'<code style="display: inline-block; padding: 6px 15px; background: #f1f5f9; color: #334155; border-radius: 6px; font-size: 0\.85em;">',
    "<code>",
    lib,
)

# Drop first h2 Full Guide Library (we re-add cleanly)
lib = re.sub(
    r'<h2 class="section-title">📚 Full Guide Library</h2>\s*',
    "",
    lib,
    count=1,
)

page = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ChinaOps - Technical Runbook for Travelers &amp; Parents | 38 Essential Guides</title>
  <meta name="description"
    content="Practical step-by-step guides for traveling in China: phone, payments, trains, hospitals, and travel with kids. Free, non-commercial runbook by TechDadShanghai.">
  <meta name="keywords"
    content="China travel guide, Shanghai travel, VPN China, Alipay setup, 12306 train tickets, China with kids, baby formula China, China emergency contacts">
  <meta name="author" content="TechDadShanghai">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="ChinaOps - Technical Runbook for Travelers &amp; Parents">
  <meta property="og:description"
    content="38 essential guides for China: payments, trains, hospitals, baby supplies, and local tips.">
  <meta property="og:site_name" content="ChinaOps">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="ChinaOps - Technical Runbook for Travelers &amp; Parents">
  <meta name="twitter:description"
    content="38 essential guides for navigating China with real-world steps and fallbacks.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>">
  <link rel="stylesheet" href="./assets/css/chinaops.css">
</head>

<body class="home-body">
  <div class="home-wrap">
    <header class="home-header">
      <h1>ChinaOps 📚</h1>
      <p class="home-tagline"><strong>Step-by-step runbook for life in China</strong></p>
      <p class="plain" style="color: var(--fg-3);">Plain English · Real fixes · Free &amp; non-commercial</p>
      <div class="version-badge">v1.3.1 · Updated Jul 21, 2026</div>
      <p class="home-lead">
        Built for first-time visitors and parents. When payment fails, apps break, or plans collapse,
        use these short procedures — not tourist brochure fluff.
      </p>

      <div class="whats-new" aria-label="What is new">
        <h3>What is new (v1.3.1)</h3>
        <ul>
          <li><strong>Clearer UI:</strong> plain-English labels next to ops names; mobile menu on guides.</li>
          <li><strong>Faster load in China:</strong> system fonts (no Google Fonts dependency).</li>
          <li><strong>Data health:</strong> all 38 SOPs have freshness metadata; 4 missing files repaired.</li>
          <li><strong>Content base:</strong> still includes July 2026 power-bank CCC rules, eSIM table, payment recovery.</li>
        </ul>
      </div>

      <div class="home-stats">
        <div class="stat">
          <div class="stat-number">38</div>
          <div class="stat-label">Guides (SOPs)</div>
        </div>
        <div class="stat">
          <div class="stat-number">5</div>
          <div class="stat-label">Categories</div>
        </div>
        <div class="stat">
          <div class="stat-number">Free</div>
          <div class="stat-label">No ads</div>
        </div>
      </div>

      <div style="margin-top: 28px;">
        <a href="https://github.com/MilesXLab/ChinaOps" class="btn btn-dark" rel="noopener noreferrer" target="_blank">
          ChinaOps on GitHub
        </a>
      </div>
    </header>

    <section class="home-section callout callout-success" style="border-left-width: 5px;">
      <h2 class="section-title" style="color: var(--success-strong); border-bottom-color: var(--success);">
        How to use this site
        <span class="plain">Pick your situation first</span>
      </h2>
      <div class="howto-grid">
        <div>
          <h3 style="color: var(--success-strong); margin: 0 0 8px;">First visit</h3>
          <p class="path-desc">Start with <strong>Choose your path</strong>, then <strong>System Setup</strong>
            (phone, payments, landing).</p>
        </div>
        <div>
          <h3 style="color: var(--success-strong); margin: 0 0 8px;">With kids</h3>
          <p class="path-desc">Open <strong>Parenting</strong> first, then print the
            <strong>Emergency contacts</strong> card.</p>
        </div>
        <div>
          <h3 style="color: var(--success-strong); margin: 0 0 8px;">Need one topic</h3>
          <p class="path-desc">Scroll the <strong>Full guide library</strong> — 38 guides with reading times.</p>
        </div>
      </div>
      <p class="callout callout-info" style="margin-top: 20px; margin-bottom: 0;">
        <strong>Tip:</strong> Found a wrong number or broken step?
        <a href="https://github.com/MilesXLab/ChinaOps/issues">Report on GitHub</a>
        or <a href="mailto:miles.x.dev@outlook.com?subject=ChinaOps%20Feedback">email feedback</a>.
      </p>
    </section>

    <section class="home-section callout callout-info">
      <h2 class="section-title">
        Before your flight
        <span class="plain">Do these checks at home</span>
      </h2>
      <p class="section-kicker">
        Next busy periods: <strong>Mid-Autumn Festival (Sep 25–27, 2026)</strong> and
        <strong>National Day Golden Week (Oct 1–7, 2026)</strong> — book high-speed rail early.
      </p>
      <div class="howto-grid">
        <ul style="margin: 0; padding-left: 1.2em; color: var(--fg-2); line-height: 1.9;">
          <li><strong>Power bank:</strong> in carry-on; phone is your wallet and map.</li>
          <li><strong>VPN / eSIM:</strong> install and test before you land.</li>
          <li><strong>Payments:</strong> bind cards in Alipay; tell your bank about China travel.</li>
        </ul>
        <ul style="margin: 0; padding-left: 1.2em; color: var(--fg-2); line-height: 1.9;">
          <li><strong>Hospital:</strong> save one international clinic in your maps app.</li>
          <li><strong>Hotel address:</strong> screenshot the Chinese characters (汉字).</li>
          <li><strong>Offline:</strong> download maps + a dictionary for offline use.</li>
        </ul>
      </div>
      <p style="margin: 16px 0 0; font-size: 0.9rem; color: var(--fg-3);">
        <span class="term-chip">SOP</span>
        <span class="term-def">= standard operating procedure (a clear step-by-step checklist)</span>
      </p>
    </section>

    <h2 class="home-paths-label">
      Choose your path
      <span class="plain">Tap the situation that matches you</span>
    </h2>
    <div class="path-grid">
      <a href="./docs/01-System-Setup/" class="path-card">
        <div class="path-emoji">👤</div>
        <div class="path-title">First-time visitor?</div>
        <div class="path-plain">System Setup · before you arrive</div>
        <div class="path-desc">Phone, eSIM, payments, and your first 30 minutes after landing.</div>
      </a>
      <a href="./docs/04-Parenting-Patch/" class="path-card">
        <div class="path-emoji">👨‍👩‍👧</div>
        <div class="path-title">Traveling with kids?</div>
        <div class="path-plain">Parenting · family tools</div>
        <div class="path-desc">Formula safety, diapers, nursing rooms, and baby runbooks.</div>
      </a>
      <a href="./docs/03-Emergency-DR/" class="path-card tone-critical">
        <div class="path-emoji">🆘</div>
        <div class="path-title">Emergency?</div>
        <div class="path-plain">When things go wrong</div>
        <div class="path-desc">Hospitals, lost passport or phone, scams, and network failures.</div>
      </a>
      <a href="./docs/02-Daily-Runtime/" class="path-card">
        <div class="path-emoji">🚀</div>
        <div class="path-title">Daily navigation?</div>
        <div class="path-plain">Day-to-day life</div>
        <div class="path-desc">Trains, taxis, metro, maps, food, and local tips.</div>
      </a>
      <a href="./docs/05-Event-Operations/" class="path-card tone-event">
        <div class="path-emoji">🏮</div>
        <div class="path-title">Chinese holiday?</div>
        <div class="path-plain">Peak travel periods</div>
        <div class="path-desc">CNY, Golden Week crowds, closures, and booking strategy.</div>
      </a>
      <a href="./docs/02-Daily-Runtime/shanghai-vegan-guide/" class="path-card tone-success">
        <div class="path-emoji">🥗</div>
        <div class="path-title">Vegetarian / vegan?</div>
        <div class="path-plain">Food without meat</div>
        <div class="path-desc">Restaurant phrases, temple food, and plant-based options.</div>
      </a>
    </div>

    <section class="home-section">
      <h2 class="section-title">
        📚 Full guide library
        <span class="plain">All 38 guides by category</span>
      </h2>
{lib}
    </section>

    <section class="home-section">
      <h2 class="section-title" style="color: var(--fg-2); border-bottom-color: var(--border-emphasis);">
        Why open source?
        <span class="plain">Transparent, community-fixed, free</span>
      </h2>
      <div class="howto-grid">
        <div class="tool-card">
          <h4>Transparency</h4>
          <p class="path-desc">Every step is open for inspection. No hidden affiliate rankings.</p>
        </div>
        <div class="tool-card">
          <h4>Community fixes</h4>
          <p class="path-desc">Apps and rules change fast — anyone can send a correction.</p>
        </div>
        <div class="tool-card">
          <h4>Zero paywall</h4>
          <p class="path-desc">Survival info for families should stay free and accessible.</p>
        </div>
      </div>
    </section>

    <section class="home-section callout callout-warning">
      <h2 class="section-title" style="color: var(--warning-strong); border-bottom-color: var(--warning);">
        Coming in v2.0
        <span class="plain">What should we build next?</span>
      </h2>
      <p class="path-desc">Search, interactive checklists, and browser tools are on the roadmap.
        Tell us what you need on the ground.</p>
      <p style="margin-top: 12px;">
        <a class="btn btn-critical" href="https://github.com/MilesXLab/ChinaOps/issues">Suggest a feature →</a>
      </p>
    </section>

    <section class="home-section callout callout-info">
      <h2 class="section-title">
        Support &amp; community
        <span class="plain">Your reports keep guides accurate</span>
      </h2>
      <p class="path-desc">ChinaOps is 100% free and open-source. The best support is speaking up when something breaks.</p>
      <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 16px;">
        <a class="btn btn-brand" href="https://github.com/MilesXLab/ChinaOps/issues">Report a problem</a>
        <a class="btn btn-success"
          href="mailto:miles.x.dev@outlook.com?subject=ChinaOps%20Feedback%20%7C%20%E4%B8%AD%E5%9B%BD%E6%97%85%E8%A1%8C%E5%8F%8D%E9%A6%88">Send email feedback</a>
      </div>
    </section>

    <section class="home-section callout callout-critical">
      <h2 class="section-title" style="color: var(--critical); border-bottom-color: var(--critical);">
        Terms of use
        <span class="plain">Personal use only</span>
      </h2>
      <div class="howto-grid">
        <div>
          <h3 style="color: var(--critical); font-size: 1rem;">Allowed</h3>
          <ul style="color: #742a2a; font-size: 0.9rem; line-height: 1.6;">
            <li>Personal trip planning</li>
            <li>Parenting &amp; family guidance</li>
            <li>Educational or non-profit use</li>
          </ul>
        </div>
        <div>
          <h3 style="color: var(--critical); font-size: 1rem;">Not allowed</h3>
          <ul style="color: #742a2a; font-size: 0.9rem; line-height: 1.6;">
            <li>Selling or charging for access</li>
            <li>Commercial subscription use</li>
            <li>Removing original attribution</li>
          </ul>
        </div>
      </div>
      <p style="margin-top: 12px; font-size: 0.85rem; color: var(--critical);">
        Licensed under CC BY-NC 4.0.
        <a href="https://github.com/MilesXLab/ChinaOps/blob/main/LICENSE">View full license →</a>
      </p>
    </section>

    <footer class="home-footer">
      <p><strong>ChinaOps</strong> — technical runbook for travelers &amp; parents</p>
      <p style="font-size: 0.9rem;">Created by a full-time dad. Real-world solutions for families and solo explorers.</p>
      <p style="margin-top: 12px;">Last updated: Jul 21, 2026 · Author: <strong>TechDadShanghai</strong></p>
      <p style="color: var(--fg-3); font-size: 0.9rem; margin-top: 16px;">
        Made for travelers, by travelers ·
        <a href="https://github.com/MilesXLab/ChinaOps">View on GitHub</a>
      </p>
      <p style="color: var(--fg-3); font-size: 0.85rem; margin-top: 8px;">
        Free &amp; open-source (non-commercial use only).<br>
        本项目免费开源，严禁商业用途。商业使用请联系作者。
      </p>
    </footer>

    <button type="button" class="back-to-top" id="backToTop" aria-label="Back to top">↑</button>
  </div>

  <script src="./assets/js/chinaops.js" defer></script>
</body>

</html>
"""

(ROOT / "index.html").write_text(page, encoding="utf-8")
print("Wrote index.html", len(page), "chars")
