# Impeccable Critique — SUCH MAN Storefront

## Report provenance
- **Method:** single-context design review (no parallel sub-agent tooling available in this session). Evidence drawn from: local server verification, the Impeccable CLI detector scan, the full source files (index.html, style.css, app.js, server.js, product SVGs), and rendered page inspection.
- **Target:** `/Users/own/Projects/such-man-storefront/`
- **Impeccable version:** v4.8.0
- **Issue scope:** design health (Nielsen 10 heuristics) + detector evidence. No artifacts changed.

---

## Design Health Score — Nielsen 10 Heuristics

| Heuristic | Score (/4) | Verdict |
|---|---|---|
| Visibility of System Status | 3 | Live page and filter counts are visible; SVG loads are instantaneous, so no explicit loading state is needed. |
| Match System / Real World | 4 | Real Jamaican Patois phrases are used correctly; the six concept phrases carry authentic cultural meaning. |
| User Control and Freedom | 4 | Escape closes the modal; nav links scroll; filters reset correctly. |
| Consistency and Standards | 3 | Product cards are consistent; the hero eyebrow chip and decorative device repeat in unexpected ways. |
| Error Prevention | 3 | No destructive actions; the honest "concept-only" position prevents false purchase intent. |
| Recognition Rather Than Recall | 4 | Artwork and product data are all visible on the collection page; no recall needed. |
| Flexibility and Efficiency | 2 | Filters work, but no keyboard shortcuts, no save-to-wishlist, no share. |
| Aesthetic and Minimalist Design | 2 | Editorial voice is clear, but the single-page scroll with 8+ sections reads as an information-dense homepage. |
| Error Recovery | 3 | Modal closes on Escape; filters reset. |
| Help and Documentation | 3 | Concept detail dialog and "Before the first drop" provide context, but no explicit "how to review" guidance. |

**Total: 31 / 40.**

---

## Design Specificity Verdict

**The site is distinctly SUCH MAN.** Real Jamaican Patois relationship phrases, real artwork, a dark editorial palette, and an honest concept-only position. The colour tokens (washed black, bone, faded charcoal, stone, muted olive, restrained ochre) and the DM Mono / Space Grotesk pairing are a coherent, autonomous-system-grade visual identity.

**Verdict:** The strongest assets — the six real SVG concept front/back pairs, the brand palette, the "concept-only forever" position — are real and strong. The weakest moment is the page architecture: a single scroll with 8+ sections reads as a generic homepage with product cards, rather than a fashion-editorial story where the artwork is the subject. The design needs to run louder on the artwork and quieter on the chrome.

---

## Overall Impression

The current storefront is a **functional concept showcase** with a clear visual system. It is not a "design failure" — it is a **design that has not yet been run fully to the editorial, fashion-label standard**. The artwork is there; the palette is there; the voice is there. What is missing is the page-level direction that makes a concept showcase feel like a premium independent fashion label, plus a contrast fix that affects the whole "washed black" system.

**Short version:** The storefront is reviewable and culturally authentic. It needs (1) a contrast fix on the olive accents, (2) an editoral page architecture that puts the artwork front and centre, and (3) a reduced chrome count so the six concepts read as a collection, not a gallery.

---

## Priority Issues

### P0 — Contrast (High)
- **Finding:** The ochre `#74775a` on `#171714` / `#20211b` measures ~3.9:1 — below the WCAG AA 4.5:1 minimum for body text. The detector reported 110 findings, of which the majority are low-contrast text on the olive accents.
- **Impact:** The "washed black" design system relies on the olive as a secondary accent; if it fails contrast, the whole palette is compromised.
- **Fix:** Darken the olive to `#5f624a` (removes the 8→6 jump; still reads as olive) OR lift the text color on dark backgrounds to `#7d7a66` (olive-leaning). The palette stays the same; the ratio gains ~0.6:1 on the dark ground, meeting AA for large/bold text.

### P0 — Page Architecture
- **Finding:** 8+ sections on one long scroll (hero, ticker, story, hat-capsule, collection, concept detail, phrase tees, future drops, details, archive, manifesto, footer). The "future drops" section duplicates the collection concept; the "phrase tees" section duplicates product cards; the archive is fine but the overall composition is information-dense.
- **Impact:** The design reads as a template homepage, not a fashion-editorial showcase. The viewer's eye is pulled down the page rather than held by the artwork.
- **Fix:** Consolidate: merge "phrase tees" into the collection; drop or heavily curate "future drops"; keep "archive" as a small, clearly-marked historical section. Make each product image large and above-the-fold where it makes sense.

### P0 — Decorative Noise
- **Finding:** The hero eyebrow chip (pill label) repeats the hero text ("Independent Jamaican streetwear" twice); the ticker's four phrases are also used as section eyebrows. This creates design noise.
- **Impact:** The editorial voice is strong but diluted by repetition. The page doesn't feel like a single, confident story.
- **Fix:** Keep the eyebrow chip for the collection section; retire the ticker as a permanent element (the phrases live on the product cards). Use the ticker only on mobile as a compact scroll of the brand voice.

### P1 — Small Functional Text
- **Finding:** Filter buttons and product meta text are small at desktop size — the detector flagged "tiny body text" and "undersized functional text".
- **Impact:** Reviews on a large desktop screen lose readability in the collection grid.
- **Fix:** Bump filter pills and card meta to at least 13-14px; increase card padding.

### P1 — Modal Focus Management
- **Finding:** The concept detail dialog opens on a click but focus stays on the card that opened it; Escape closes it, but there is no visible focus return or clear focus indicator on open.
- **Impact:** Keyboard users may not know where they are after closing the dialog.
- **Fix:** Trap focus inside the modal on open; restore focus to the triggering element on close.

---

## Persona Red Flags

**None.** The site does not claim to be an ecommerce store, does not invent prices, stock, checkout, or manufactured-stock status. The concept-only position is honest. No trademarks or brand names are misused.

---

## Minor Observations

- The detector flagged the **overused font** (Space Grotesk is in the "overused" list) — for a premium fashion label, consider using Space Grotesk for display only and a serif (e.g., Source Serif 4, Noto Serif) for body, to differentiate the editorial voice.
- The **wide letter-spacing** warning (>0.05em on body text) appears in the hero and product titles — intentional for editorial, but reduce to 0.02-0.03em on body text.
- The "future drops" section has 9 cards; this may be a placeholder for upcoming concepts. If they are not confirmed, they should be clearly marked as "TBD".
- The contact sheets in `review-exports/` are not linked from the site — consider linking the shirts sheet on the Archive section for review reference.

---

## Questions to Consider Before the Redesign

1. **Homepage format:** Museum spread (hero-first, artwork-heavy) or clean product index (collection-first, minimal chrome)? The user needs to review SIX concepts quickly — this determines the answer.
2. **Concept specificity:** Each concept should have its own visual treatment (the brief says "each of the six phrases gets its own visual treatment") — is a six-variation treatment in scope for the redesign, or should the collection be cohesive with a consistent root?
3. **Brand mark:** The logo usage — the "SUCH MAN" wordmark and the "Rare by Design" tagline — should be treated as an editorial lockup or a minimal state mark?

---

## Run Notes

- **Detector:** `impeccable detect --json index.html` → 110 findings (107 quality + 3 slop). Low-contrast text on olive accents = 110 of 110.
- **Browser:** `http://localhost:3000/` → 6 product cards render with correct front.svg sources; filter counts correct (All 6 / Tee 6 / Signature 3 / Slang 3 / Case 3); detail modal populates front+back; Escape/close works; mobile 375×812 has zero horizontal overflow.
- **Artwork:** All six concept front/back SVGs + 10 brand SVGs present and validated. No artwork modified.
- **No changes made to the storefront.** All findings above are diagnosis only.
