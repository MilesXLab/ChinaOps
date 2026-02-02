# ChinaOps SRE Runbook Standards (LINTS.md)

This document defines the technical and editorial standards for all SOPs in the ChinaOps repository. Every contribution must pass these lints to ensure a high-availability (HA) experience for travelers.

---

## 1. Structural Standardization (The 5-Module Logic)

Every `.md` file in the `docs/` directory **must** contain exactly these five sections in this order:

### I. TL;DR
- **Rule:** Maximum 3 sentences.
- **Goal:** Provide the core conclusion immediately. What is the fastest path to success?

### II. Prerequisites
- **Rule:** List specific requirements (physical or digital).
- **Items:** Passport, specific Apps (pre-installed), local currency, or time-buffer (e.g., "Allow 24h for KYC").

### III. Step-by-Step (The Runbook)
- **Rule:** Use numbered lists. Instructions should read like code or terminal commands.
- **Editorial:** No "fluff." Every step must be an action.

### IV. Verification (The SRE Patch)
- **Rule:** Tell the user exactly what "success" looks like.
- **Example:** "You should receive an SMS from 10010," or "The green health code must show your correct name."

### V. Fallback (Anti-SPOF)
- **Rule:** Identify the Single Point of Failure (SPOF) and provide a Plan B.
- **Example:** "If the kiosk fails, use the physical yellow arrival card."

---

## 2. Tone & Voice: The "TechDad in Shanghai"

- **Persona:** Professional, direct, slightly witty, and highly practical. Think of an expert SRE explaining a production fix to a junior dev during a 2 AM outage.
- **Conclusion First:** Start with the answer. Explain the "why" only if necessary for safety.
- **Critical Alerts:** Use bold (**Critical Alert**) or emojis (🚨) for risks that could lead to being stranded or losing money.

---

## 3. Forbidden Vocabulary (AI-Fluff Filter)

To keep the runbook efficient, the following phrases are strictly **prohibited**:
- "Dear readers..."
- "I am honored to..."
- "With the development of technology..."
- "A friendly reminder..." (Use **"TechDad Rule:"** or **"Critical Alert:"** instead).
- "In conclusion..." (The TL;DR should have already concluded).

---

## 4. Technical Requirements

- **Links:** Use relative paths for internal documents. Check for broken links before PR.
- **Images:** Use descriptive alt-text.
- **Metadata:** Every guide should have valid YAML frontmatter (layout, title, version).
