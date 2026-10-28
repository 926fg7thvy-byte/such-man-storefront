# SUCH MAN — RARE BY DESIGN (concept storefront)

Independent Jamaican streetwear concept site. Six design concepts, each clearly
marked `CONCEPT` — no orders, no stock claims, no checkout.

## What's here

- `index.html` — the homepage (hero, story, hat capsule, concept collection,
  concept detail dialog, future wardrobe, details, archive, manifesto, footer)
- `style.css` — the visual system (solid surfaces, strong borders, tactile UI,
  no glass, no gradients)
- `app.js` — collection filter, concept-detail dialog, toast, year
- `server.js` — static file server (Railway "npm start", `/healthz` ready)
- `assets/`
  - `product/<slug>/front.svg` + `back.svg` — the six shirt concepts (front/back)
  - `brand/` — hero mark, story art, hat capsule, future-wardrobe illustration

## Concepts (approved phrases — exact wording preserved)

1. SUCH MAN KNOWS CODE
2. SUCH MAN, SHE A MI COUSIN
3. SUCH MAN DEH DEH
4. MI INNOCENT
5. JUST A FRIEND
6. NO EVIDENCE, NO CASE

## Local test

    npx serve .          # or: node server.js
    open http://localhost:3000

## Deployment (Railway)

The storefront is deployed on Railway from the `main` branch of the linked repo.
Push the `main` branch and Railway builds/redeploys automatically (railpack node,
`npm start`). Verify `https://such-man-storefront-production.up.railway.app/` and
`/healthz`.

## Rules followed

- Every product is marked `CONCEPT`; no prices, no stock claims, no buy buttons.
- No backdrop blur, no glassmorphism, no background gradients.
- Brand palette: washed black, bone, faded charcoal, stone, muted olive,
  restrained ochre accent.
- No copyrighted artwork, no copied designer graphics.
