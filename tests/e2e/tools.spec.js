// @ts-check
const { test, expect } = require("@playwright/test");

test.describe("ChinaOps browser tools", () => {
  test("MRZ tool formats and copies name", async ({ page, context }) => {
    await context.grantPermissions(["clipboard-read", "clipboard-write"]).catch(() => {});
    await page.goto("/mrz-tool.html");
    await page.fill("#firstName", "José");
    await page.fill("#lastName", "García");
    await expect(page.locator("#mrzOut")).toHaveText("GARCIA<<JOSE");

    await page.fill("#firstName", "Mary-Jane");
    await page.fill("#lastName", "O'Brien");
    await expect(page.locator("#mrzOut")).toHaveText("OBRIEN<<MARYJANE");

    await page.click("#btnCopy");
    await expect(page.locator("#msg")).toContainText("Copied:");
    // clipboard may be blocked in some CI; soft-check when available
    const clip = await page.evaluate(async () => {
      try {
        return await navigator.clipboard.readText();
      } catch {
        return null;
      }
    });
    if (clip !== null) {
      expect(clip).toBe("OBRIEN<<MARYJANE");
    }

    await page.click("#btnClear");
    await expect(page.locator("#mrzOut")).toHaveText("—");
    await expect(page.locator("#firstName")).toHaveValue("");
  });

  test("MRZ copy requires both name parts", async ({ page }) => {
    await page.goto("/mrz-tool.html");
    await page.fill("#firstName", "OnlyFirst");
    await page.fill("#lastName", "");
    await page.click("#btnCopy");
    await expect(page.locator("#msg")).toContainText("Need both");
  });

  test("dose calculator kg and lb", async ({ page }) => {
    await page.goto("/dose-calculator.html");
    await page.selectOption("#preset", "paracetamol");
    await page.fill("#weight", "20");
    await page.selectOption("#weightUnit", "kg");
    await page.click("#btnCalc");
    await expect(page.locator("#resultDose")).toHaveText("300.0 mg per dose");
    await expect(page.locator("#result")).toBeVisible();

    await page.selectOption("#weightUnit", "lb");
    await page.fill("#weight", "44.092"); // ~20 kg
    await page.click("#btnCalc");
    const text = await page.locator("#resultDose").textContent();
    // ~20kg * 15 ≈ 300mg
    const mg = parseFloat((text || "").replace(/[^\d.]/g, ""));
    expect(mg).toBeGreaterThan(298);
    expect(mg).toBeLessThan(302);

    await page.click("#btnClear");
    await page.click("#btnCalc");
    await expect(page.locator("#doseMsg")).toContainText("Enter a positive weight");
  });

  test("dose calculator has no antibiotic preset", async ({ page }) => {
    await page.goto("/dose-calculator.html");
    const options = await page.locator("#preset option").allTextContents();
    expect(options.join(" ").toLowerCase()).not.toContain("amoxicillin");
  });

  test("phrase card allergy chips and preview", async ({ page }) => {
    await page.goto("/phrase-card-tool.html");
    await page.fill("#name", "Alex");
    const peanut = page.locator("#allergyChips button").filter({ hasText: "Peanuts" });
    await peanut.click();
    await expect(peanut).toHaveAttribute("aria-pressed", "true");
    await expect(page.locator("#printArea")).toContainText("Alex");
    await expect(page.locator("#printArea")).toContainText("花生");
    await expect(page.locator("#printArea")).toContainText("Peanuts");

    await page.selectOption("#mode", "emergency");
    await expect(page.locator("#emergencyBox")).toBeVisible();
    await page.fill("#ice", "Sam +86 100");
    await expect(page.locator("#printArea")).toContainText("110");
    await expect(page.locator("#printArea")).toContainText("Sam");
  });

  test("catalog search loads guides and aliases", async ({ page }) => {
    await page.goto("/search.html");
    // After load, empty query shows first N of total
    await expect(page.locator("#searchStatus")).toContainText(/all \d+|Loaded \d+/i, {
      timeout: 15_000,
    });
    await expect(page.locator("#searchResults li").first()).toBeVisible();

    await page.fill("#guideSearch", "mrz");
    await expect(page.locator("#searchResults li")).not.toHaveCount(0);
    await expect(page.locator("#searchResults")).toContainText(/12306|Train|MRZ/i);

    await page.click('#quickTags [data-q="payment"]');
    await expect(page.locator("#guideSearch")).toHaveValue("payment");
    await expect(page.locator("#searchResults li").first()).toBeVisible();
  });

  test("fulltext search page boots (Pagefind or fallback)", async ({ page }) => {
    await page.goto("/search-fulltext.html");
    await expect(page.locator("#engineBadge")).toBeVisible();
    // Either Pagefind UI appears or fallback activates
    await page.waitForTimeout(1500);
    const badge = (await page.locator("#engineBadge").textContent()) || "";
    const pagefindVisible = await page.locator(".pagefind-ui").count();
    const fallbackActive = await page.locator("#fallbackBox.active").count();
    expect(
      badge.toLowerCase().includes("pagefind") ||
        badge.toLowerCase().includes("fallback") ||
        pagefindVisible > 0 ||
        fallbackActive > 0
    ).toBeTruthy();

    // Fallback path with ?q= if fallback is active
    if (fallbackActive > 0 || badge.toLowerCase().includes("fallback")) {
      await page.goto("/search-fulltext.html?q=alipay");
      await page.waitForTimeout(800);
      const fb = page.locator("#fbInput");
      if (await fb.isVisible()) {
        await expect(fb).toHaveValue("alipay");
      }
    }
  });

  test("preflight checklist persists in localStorage", async ({ page }) => {
    await page.goto("/preflight-checklist.html");
    const box = page.locator("#pf-power");
    await box.check();
    await expect(box).toBeChecked();
    await page.reload();
    await expect(page.locator("#pf-power")).toBeChecked();
    await page.click("#preflightReset");
    await expect(page.locator("#pf-power")).not.toBeChecked();
  });

  test("landing checklist uses separate storage key", async ({ page }) => {
    await page.goto("/landing-checklist.html");
    await page.locator("#ld-imm").check();
    await page.goto("/preflight-checklist.html");
    // preflight power should still be false after landing-only check
    await expect(page.locator("#pf-power")).not.toBeChecked();
    await page.goto("/landing-checklist.html");
    await expect(page.locator("#ld-imm")).toBeChecked();
    await page.click("#preflightReset");
  });

  test("survival 72h pack page renders three pages", async ({ page }) => {
    await page.goto("/survival-72h.html");
    await expect(page.locator("h1")).toContainText("72-hour");
    await expect(page.locator(".page")).toHaveCount(3);
    await expect(page.getByRole("button", { name: /Print/i })).toBeVisible();
  });
});
