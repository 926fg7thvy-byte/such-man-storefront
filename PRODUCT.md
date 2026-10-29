# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JavaScript + Node static server (`node server.js`). No framework. No build tooling. The storefront is a single-page concept showcase with inline CSS (`style.css`), behavior (`app.js`), and the real brand SVGs under `assets/`.

## Users

**Primary audience:** The brand owner (THE B.A.R.) curating an exclusive, first limited drop (~10–12 shirts) of original SUCH MAN streetwear concepts for review and eventual manufacture.

**Secondary audience:** Design-minded visitors, potential first customers, manufacturers, and press. Dark, confident, editorial. The site is a *concept showcase*, not an e-commerce store — there are no prices, no stock claims, no cart, no checkout.

## Product Purpose

Present six original shirt design concepts (SUCH MAN Streetwear, "Rare by Design") as a premium, fashion-editorial concept storefront. Communicate that these are proposed designs, not manufactured products. Every concept is clearly marked `CONCEPT` — no orders, no stock claims, no checkout. The site is the review vehicle for the first limited drop (~10–12 shirts).

## Positioning

Independent Jamaican streetwear: contemporary, confident, editorial, culturally authentic. A premium independent-brand presentation — washed black, bone, faded charcoal, stone, muted olive, restrained ochre. The site must look like a real fashion-label concept storefront, not a generic ecommerce template, and must not copy another brand.

## Operating Context

- Locally served via `node server.js` (port 3000 by default; Railway-assigned port via `PORT`).
- The six shirt concepts are concept-stage: real print files, garment blanks, sizing, sample approval, and manufacture are pending (proposed manufacturer: Sun Island Jamaica Ltd.).
- The site deliberately has no shopping functionality: no prices, no inventory claims, no checkout.
- All artwork is the brand's own SVG library (`assets/`); the review contact sheets live in `review-exports/`.

## Capabilities and Constraints

- **No shopping capabilities.** No prices, no inventory, no cart, no checkout, no buy buttons (verified: not present).
- **No production capacity has been signed.** Manufacturing quotes are proposals (e.g., Sun Island Jamaica Ltd: JA$1,320/shirt before GCT, JA$18,216 for 12 incl. taxes, 10–15 business days); no signed NDA or production agreement.
- **Original artwork must be preserved.** Six concept front/back SVGs + brand assets are the real product imagery.
- **Design direction (pinned):** solid surfaces, strong borders, tactile UI; no translucency/glassmorphism/gradients; no fake luxury claims. Washed black ground with ochre accent; DM Mono type; Space Grotesk display.
- **Brand commitment:** "Rare by Design" — solid surfaces, strong borders, tactile UI, no translucency/glassmorphism/gradients; dark #171714 ground with ochre #a77a52 accents.

## Brand Commitments

- Name: SUCH MAN® — "Rare by Design", independent Jamaican streetwear.
- Voice: confident, editorial, culturally authentic (subtle Jamaican influence, not tourist clichés).
- Visual system already committed: solid surfaces, strong borders, tactile UI; no glassmorphism/translucency/gradients; dark ground + ochre accent + DM Mono display + Space Grotesk.
- The six approved concept phrases must each have its own distinctive visual treatment while remaining one cohesive collection.
- Review artifacts (contact sheets) must show the actual artwork and carry the "DESIGN CONCEPT — NOT FOR SALE" mark.

## Evidence on Hand

- Six concept front/back SVG pairs: `such-man-knows-code`, `such-man-she-a-mi-cousin`, `such-man-deh-deh`, `mi-innocent`, `just-a-friend`, `no-evidence-no-case` (in `assets/product/`).
- Brand assets: `assets/brand/` (hero-art, story-art, hat-capsule, favicon, hoodie, longsleeve, buckethat, beanie, tote, specialcap).
- Review contact sheets: `review-exports/contact-sheet-shirts.png` (1920×2400) and `review-exports/contact-sheet-hats.png` (1920×1500).
- Storefront scaffold: `index.html`, `style.css`, `app.js`, `server.js` (static server with `/healthz`).
- Six approved phrases: SUCH MAN KNOWS CODE / SUCH MAN, SHE A MI COUSIN / SUCH MAN DEH DEH / MI INNOCENT / JUST A FRIEND / NO EVIDENCE, NO CASE.

## Product Principles

1. **Real artwork, real truth.** The six SVG concepts and brand assets are the product; never substitute generic or AI-made imagery for the brand's own art.
2. **Concept-only forever.** No prices, no stock, no cart, no checkout, no "manufactured" claims — these are proposed designs.
3. **Premium independent brand.** Solid surfaces, strong borders, tactile UI; no translucency or glassmorphism; confident editorial presence.
4. **Distinctive per concept, cohesive collection.** Each of the six phrases gets its own visual treatment while reading as one collection.
5. **Dark, confident, editorial.** Washed black ground, ochre accents, DM Mono + Space Grotesk; oversized type, deliberate negative space.

## Accessibility & Inclusion

Keyboard-operable navigation and product interaction (filter, concept detail dialog, Escape/close, focus management); visible focus indicators; sufficient color contrast (WCAG AA); meaningful alt text on all product images; reduced-motion respect; semantic headings and landmarks.

## Product Principles (design)

- Real artwork, real truth.
- Concept-only forever.
- Premium independent brand.
- Distinctive per concept, cohesive collection.
- Dark, confident, editorial.
