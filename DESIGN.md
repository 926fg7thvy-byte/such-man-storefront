---
name: SUCH MAN — Rare by Design
description: Independent Jamaican streetwear concept storefront — a premium, editorial concept showcase using the brand's real artwork
colors:
  ink:
    value: "#171714"
    role: "Primary background — deep warm black"
  ink-2:
    value: "#20211b"
    role: "Surface / panel background"
  ink-3:
    value: "#1d1e18"
    role: "Border / divider / secondary text"
  paper:
    value: "#e8e5dc"
    role: "Muted text placeholder"
  stone:
    value: "#c9c4b2"
    role: "Secondary text, tags"
  muted:
    value: "#99968b"
    role: "Muted labels, captions"
  olive:
    value: "#74775a"
    role: "Secondary accent, vintage / olive theme notes"
  line:
    value: "#393933"
    role: "Primary border / strong rules"
  line-soft:
    value: "#2a2a22"
    role: "Secondary border / hover border"
  accent:
    value: "#a77a52"
    role: "Primary brand accent — ochre / burnished copper"
  accent-soft:
    value: "#c49a6e"
    role: "Accent on dark surfaces"
  accent-ink:
    value: "#5e4a32"
    role: "Dark accent for text on light surfaces"
  display:
    fontFamily: "Space Grotesk"
    fontWeight: 600
    lineHeight: 1.1
  mono:
    fontFamily: "DM Mono"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: "2px"
  md: "6px"
  lg: "12px"
  xl: "24px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "28px"
  lg: "48px"
  xl: "80px"
  xxl: "120px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "14px 32px"
  filter-btn:
    backgroundColor: "{colors.ink-2}"
    textColor: "{colors.paper}"
    rounded: "{rounded.sm}"
    padding: "10px 22px"
  badge:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.sm}"
  product-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  card:
    backgroundColor: "{colors.ink-2}"
    border: "1px solid {colors.line-soft}"
    rounded: "{rounded.md}"
  concept-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  modal:
    backgroundColor: "{colors.ink}"
    border: "1px solid {colors.line}"
    rounded: "{rounded.lg}"
---

# Design System: SUCH MAN — Rare by Design

## Overview

**Creative North Star:** *The Rare by Design story* — an exclusive Jamaican streetwear concept showcase with a premium fashion-editorial identity: solid surfaces, strong borders, tactile UI. The brand voice is confident and culturally authentic — washed black grounds the work, ochre brings it to life.

**Key Characteristics:**
- Solid surfaces with strong borders and tactile UI; no translucency or glassmorphism.
- Editorial fashion identity: oversized typography, intentional negative space, asymmetric layouts.
- Dark, confident ground (#171714) with ochre accents (#a77a52); DM Mono for type, Space Grotesk for display.
- Real artwork at the centre: the six concept front/back SVGs and brand assets are never replaced.
- Every product is clearly marked `CONCEPT` — no prices, no stock, no checkout.

## Colors

**Primary:**
- **Burnished Ochre** (#a77a52): primary brand accent — buttons, badges, concept tags, subtle highlights.
- **Accent Soft** (#c49a6e): accents on dark surfaces, tag backgrounds.

**Neutral:**
- **Deep Black** (#171714): primary background, the canvas.
- **Near Black** (#20211b): surface / panel background.
- **Ruled Charcoal** (#1d1e18): borders, dividers, secondary text.
- **Washing Stone** (#c9c4b2): secondary text, tags.
- **Faded Muted** (#99968b): captions, mono labels.

**Accent:**
- **Muted Olive** (#74775a): secondary accent — vintage notes, archive tags, hat-capsule accents.

**Named Rules:**
- **The One Voice Rule.** The ochre accent is used on ≤10% of any given screen. Its rarity is the point.
- **The Solid Rule.** Edges are hard and defined. No soft shadows, no translucency, no gradients.
- **The Real Art Rule.** Product imagery is the brand's own SVG artwork; never substitute generic or AI-made imagery.

## Typography

**Display Font:** Space Grotesk (fallbacks: system-ui, sans-serif)
**Body Font:** Space Grotesk (fallbacks: system-ui, sans-serif)
**Label/Mono Font:** DM Mono

**Character:** Confident, contemporary, deliberately editorial. The display type carries the brand statement; mono is reserved for labels, tags, edition numbers, and small caps caps.

### Hierarchy
- **Display** (600, clamp(3rem, 7vw, 6rem), 1.1): hero headline — "RARE BY DESIGN".
- **Headline** (700, clamp(2rem, 5vw, 3.5rem), 1.15): section titles, product titles.
- **Title** (600, clamp(1.5rem, 3vw, 2.25rem), 1.2): section sub-headers, product meta.
- **Body** (400, clamp(1rem, 1.5vw, 1.125rem), 1.6): prose, descriptions.
- **Label** (400, 11px, 0.1em, uppercase): kicker labels, eyebrows, edition numbers.

### Named Rules
- **The Mono Rule.** DM Mono (weight 400-500) carries all labels, edition tags, and technical micro-copy.
- **The Display Rule.** Space Grotesk 600–700 at clamp(3rem, 7vw, 6rem) is reserved for the hero headline.

## Layout

- **Grid:** asymmetric, editorial. One primary column on mobile; two-column editorial spreads on desktop.
- **Spacing rhythm:** xs (8px) / sm (16px) / md (28px) / lg (48px) / xl (80px) / xxl (120px). White space is a design material — generous negative space around each concept.
- **Breakpoints:** 375px (mobile) / 768px (tablet) / 1280px (desktop) / 1600px (wide editorial).
- **Borders:** strong, 1-2px solid charcoal. Borders separate, not decorate.

## Elevation & Depth

**Flat-by-default.** No shadows at rest. Depth is conveyed through:
- **Tonal layering** — near-black panels (#1d1e18) floating above #171714.
- **Border weight** — 2px ruled borders create structure.
- **State change** — hover: border weights shift, background moves to #20211b, an ochre accent appears on text.

## Shapes

- **Corner language:** sm (2px) for pills and tags; md (6px) for cards and badges; lg (12px) for panels and modals; xl (24px) for hero and large containers.
- **Form:** hard, grounded, tactile. The brand mark is angular (icons use 45° cuts and stamped squares).
- **Clip-path:** none by default — hard edges are the form language.

## Components

### Product Card
- **Shape:** md (6px) rounded card on a near-black ground.
- **Color assignment:** ink-2 background, line-soft border, white text, accent badge.
- **States:** default / hover (border weight increases, background lifts to ink-2, ochre appears) / active (dark ink ground + ochre text).
- **Internal padding:** 20px 22px.

### Concept Badge
- **Shape:** sm (2px) pill.
- **Color assignment:** ochre background, black text.
- **States:** static, labels the concept-stage status clearly.

### Filter Button
- **Shape:** sm (2px) pill.
- **Color assignment:** ink-2 background, paper text.
- **States:** default / active (ochre background, ink text).

### Concept Detail Dialog
- **Shape:** lg (12px) panel, dark ink ground, line border, z-offset above the page.
- **Color assignment:** ink-2 frame, ink-3 text, ochre for the concept tag.
- **States:** closed (hidden) / open (focus trapped, Escape closes, body scroll locks).

### Hat Capsule
- **Shape:** rounded panel with an embroidered-cap concept image.
- **Color assignment:** the hat-capsule artwork itself (washed black / ochre), over an ink-2 panel.

### Toast
- **Shape:** small, solid, ink-2 panel with ochre text.
- **Position:** fixed bottom center.

## Do's and Don'ts

### Do:
- **Do** use hard 1-2px borders as the primary structure.
- **Do** keep the ochre accent rare (≤10% of the screen).
- **Do** render real artwork as the hero of every product.
- **Do** mark every concept as CONCEPT — no prices, no stock, no checkout.
- **Do** keep DM Mono for labels, tags, and micro-copy.

### Don't:
- **Don't** use translucency, glassmorphism, or background gradients.
- **Don't** place soft shadows on surfaces.
- **Don't** use the ochre accent liberally — a screen full of ochre has no voice.
- **Don't** add fake prices, inventory, or checkout controls.
- **Don't** replace the brand's own artwork with generic or AI-made imagery.
