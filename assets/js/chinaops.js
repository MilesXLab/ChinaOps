/**
 * ChinaOps shared UI: mobile nav + optional TOC
 */
(function () {
  function closeNav() {
    document.body.classList.remove("nav-open");
    var btn = document.getElementById("menuToggle");
    if (btn) {
      btn.setAttribute("aria-expanded", "false");
      btn.setAttribute("aria-label", "Open menu");
    }
  }

  function openNav() {
    document.body.classList.add("nav-open");
    var btn = document.getElementById("menuToggle");
    if (btn) {
      btn.setAttribute("aria-expanded", "true");
      btn.setAttribute("aria-label", "Close menu");
    }
  }

  function toggleNav() {
    if (document.body.classList.contains("nav-open")) {
      closeNav();
    } else {
      openNav();
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("menuToggle");
    var backdrop = document.getElementById("sidebarBackdrop");

    if (toggle) {
      toggle.addEventListener("click", toggleNav);
    }
    if (backdrop) {
      backdrop.addEventListener("click", closeNav);
    }

    // Close drawer after in-page / sidebar link click (mobile)
    document.querySelectorAll(".sidebar a").forEach(function (a) {
      a.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 1100px)").matches) {
          closeNav();
        }
      });
    });

    // Escape closes nav
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });

    // TOC for guide pages (+ mobile sticky strip from H2 only)
    var tocContainer = document.getElementById("toc-container");
    var mobileToc = document.getElementById("mobileToc");
    var root =
      document.querySelector(".guide-container") ||
      document.querySelector(".docs-container");
    if (root && (tocContainer || mobileToc)) {
      var headers = root.querySelectorAll("h2, h3");
      var h2Count = 0;
      headers.forEach(function (header, index) {
        if (!header.id) {
          header.id = "section-" + index;
        }
        var label = header.textContent.replace(/^\s+|\s+$/g, "");
        if (tocContainer) {
          var li = document.createElement("li");
          var a = document.createElement("a");
          a.href = "#" + header.id;
          a.textContent = label;
          a.className =
            header.tagName.toLowerCase() === "h2" ? "toc-h2" : "toc-h3";
          li.appendChild(a);
          tocContainer.appendChild(li);
        }
        if (mobileToc && header.tagName.toLowerCase() === "h2" && h2Count < 8) {
          var ma = document.createElement("a");
          ma.href = "#" + header.id;
          ma.textContent = label.length > 28 ? label.slice(0, 26) + "…" : label;
          mobileToc.appendChild(ma);
          h2Count += 1;
        }
      });
      if (tocContainer && headers.length === 0) {
        tocContainer.innerHTML =
          '<li><span class="plain">No sub-sections on this page</span></li>';
      }
      if (mobileToc && h2Count === 0) {
        mobileToc.style.display = "none";
      }
    }

    // Home back-to-top
    var backToTop = document.getElementById("backToTop");
    if (backToTop) {
      window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
          backToTop.classList.add("visible");
        } else {
          backToTop.classList.remove("visible");
        }
      });
      backToTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }

    // Symptom index: chips + search (row-level)
    var filterBar = document.getElementById("symptomFilters");
    var searchInput = document.getElementById("symptomSearch");
    if (filterBar || searchInput) {
      var sections = document.querySelectorAll(".symptom-section");
      var countEl = document.getElementById("symptomCount");
      var chips = filterBar
        ? filterBar.querySelectorAll(".filter-chip")
        : [];
      var clearBtn = document.getElementById("symptomSearchClear");
      var activeTag = "all";

      function applySymptomView() {
        var q = (searchInput && searchInput.value
          ? searchInput.value
          : ""
        )
          .toLowerCase()
          .replace(/^\s+|\s+$/g, "");
        var visibleSections = 0;
        var visibleRows = 0;

        sections.forEach(function (sec) {
          var tags = (sec.getAttribute("data-tags") || "").split(/\s+/);
          var tagOk = activeTag === "all" || tags.indexOf(activeTag) !== -1;
          var rows = sec.querySelectorAll("tbody tr, table tr");
          var sectionHasRow = false;

          // Skip header rows (those with th)
          rows.forEach(function (row) {
            if (row.querySelector("th")) {
              row.classList.remove("is-hidden-row");
              return;
            }
            var text = (row.textContent || "").toLowerCase();
            var textOk = !q || text.indexOf(q) !== -1;
            var showRow = tagOk && textOk;
            row.classList.toggle("is-hidden-row", !showRow);
            if (showRow) {
              sectionHasRow = true;
              visibleRows += 1;
            }
          });

          var showSec = tagOk && (sectionHasRow || (!q && tagOk));
          // If searching, hide empty sections even if tag matches
          if (q) showSec = sectionHasRow;
          if (!tagOk) showSec = false;

          sec.classList.toggle("is-hidden", !showSec);
          if (showSec) visibleSections += 1;
        });

        if (chips.length) {
          chips.forEach(function (chip) {
            var active = chip.getAttribute("data-filter") === activeTag;
            chip.classList.toggle("is-active", active);
            chip.setAttribute("aria-pressed", active ? "true" : "false");
          });
        }

        if (clearBtn) {
          clearBtn.hidden = !q;
        }

        if (countEl) {
          var parts = [];
          if (q) parts.push('search "' + q + '"');
          if (activeTag !== "all") parts.push("filter: " + activeTag);
          countEl.textContent =
            "Showing " +
            visibleRows +
            " symptom(s) in " +
            visibleSections +
            " group(s)" +
            (parts.length ? " · " + parts.join(" · ") : "");
        }
      }

      if (chips.length) {
        chips.forEach(function (chip) {
          chip.setAttribute(
            "aria-pressed",
            chip.classList.contains("is-active") ? "true" : "false"
          );
          chip.addEventListener("click", function () {
            activeTag = chip.getAttribute("data-filter") || "all";
            applySymptomView();
          });
        });
      }

      if (searchInput) {
        searchInput.addEventListener("input", applySymptomView);
      }
      if (clearBtn) {
        clearBtn.addEventListener("click", function () {
          if (searchInput) searchInput.value = "";
          applySymptomView();
          if (searchInput) searchInput.focus();
        });
      }

      applySymptomView();
    }

    // Checklist pages (pre-flight / landing) — localStorage via data-storage-key
    var preflight = document.getElementById("preflightList");
    if (preflight) {
      var key = preflight.getAttribute("data-storage-key") || "chinaops-preflight-v1";
      var boxes = preflight.querySelectorAll('input[type="checkbox"][data-id]');
      var progressEl = document.getElementById("preflightProgress");
      var resetBtn = document.getElementById("preflightReset");
      var saved = {};
      try {
        saved = JSON.parse(localStorage.getItem(key) || "{}") || {};
      } catch (e) {
        saved = {};
      }

      function updateProgress() {
        var total = boxes.length;
        var done = 0;
        boxes.forEach(function (box) {
          if (box.checked) done += 1;
        });
        if (progressEl) {
          var completeMsg =
            key.indexOf("landing") !== -1
              ? " · Cleared to leave ✓"
              : " · Ready to fly ✓";
          progressEl.textContent =
            done +
            " / " +
            total +
            (key.indexOf("landing") !== -1 ? " gates" : " done") +
            (done === total && total ? completeMsg : "");
          progressEl.classList.toggle("is-complete", done === total && total > 0);
        }
      }

      boxes.forEach(function (box) {
        var id = box.getAttribute("data-id");
        if (saved[id]) box.checked = true;
        box.addEventListener("change", function () {
          saved[id] = box.checked;
          try {
            localStorage.setItem(key, JSON.stringify(saved));
          } catch (err) {}
          updateProgress();
        });
      });

      if (resetBtn) {
        resetBtn.addEventListener("click", function () {
          boxes.forEach(function (box) {
            box.checked = false;
          });
          saved = {};
          try {
            localStorage.removeItem(key);
          } catch (err) {}
          updateProgress();
        });
      }

      updateProgress();
    }
  });
})();


