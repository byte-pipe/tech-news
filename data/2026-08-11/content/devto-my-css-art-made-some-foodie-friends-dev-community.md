---
title: My CSS Art Made Some Foodie Friends 🍙🧋🥟🍲 - DEV Community
url: https://dev.to/lanthanum89/my-css-art-made-some-foodie-friends-4adk
site_name: devto
content_file: devto-my-css-art-made-some-foodie-friends-dev-community
fetched_at: '2026-08-11T11:42:53.197348'
original_url: https://dev.to/lanthanum89/my-css-art-made-some-foodie-friends-4adk
author: Laura Norwood
date: '2026-08-10'
description: This is a submission for Frontend Challenge - Comfort Food Edition, CSS Art. ... Tagged with css, devchallenge, showdev, frontendchallenge.
tags: '#showdev, #css, #devchallenge, #frontendchallenge'
---

Frontend Challenge CSS Art Submission 🍲🥧

This is a submission forFrontend Challenge - Comfort Food Edition, CSS Art.

## Inspiration

Comfort food isn't just one dish, so instead of picking one I built a whole squad — and gave them somewhere to live: a dark, neon-lit restaurant with a digital menu display.Onigiri,Boba Tea,Gyoza, andHot Potdouble as the menu items, each with a price tag, blinking and bouncing on a glowing CRT-style screen. Underneath, a touchscreen self-order kiosk — the kind you'd find at a fast-food counter — asks "Can I take your order?" and prints out a ticket with your order number.

## Demo

lanthanum89.github.io

Live demo:https://lanthanum89.github.io/dev.to-Frontend-Challenge-Comfort-Food-Edition/Source:https://github.com/Lanthanum89/dev.to-Frontend-Challenge-Comfort-Food-Edition

Every character bounces on its own, blinking every few seconds — click one and it gets happy^^eyes plus a burst of sparkles, right there on the menu screen. Give the kiosk below a few seconds and watch it type out its prompt, pulse its order button, and print a receipt.

## Journey

Everything isdivs built withclip-path/border-radius+ gradients and CSS animations, with a single small vanilla-JS click handler for the food characters (the challenge allows "a sprinkle of JavaScript," so I kept it to exactly one interaction and pushed everything else — including the kiosk's whole sequence — into pure CSS):

* Shared rig: every character is a.characterwrapper with the same.face/.eye/.cheek/.mouthparts, the same infinitefloatbounce, the same blink timing, and the samesquish+ sparkle-burst reaction on click. Building this as one reusable system — instead of one-off pieces — is what made it possible to add multiple characters without the CSS ballooning out of control. Each character only overrides shape, color, and face position.
* Onigiri: aclip-pathrounded triangle with aradial-gradientdot texture for rice grains and a separate nori-band trapezoid.
* Boba Tea: a tapered cup (clip-pathpolygon) with a striped straw, a domed lid, and tapioca pearls scattered along the bottom via absolutely-positioned circles.
* Gyoza: a squashed dome shape, seared with layeredradial-gradients on the bottom half, and scalloped pleats along the top edge made from a repeating dot pattern.
* Hot Pot: a broth bowl split red/clear with a hard-edgedlinear-gradient, sitting in a separate metal "band" (with rivets) below it, ring handles on both sides, and a rising-steam animation.
* The restaurant scene: a flickering neon "COMFORT FOOD" sign (layeredtext-shadowglow + a subtle opacity@keyframes flicker), a screen bezel with arepeating-linear-gradientscanline overlay for that CRT feel, and a wood counter underneath.
* The self-order kiosk: entirely CSS-driven and timed withanimation-delayso it plays out like a little sequence on page load — "Can I take your order?" types itself out letter by letter using the classicwidth: 0 → Nch+steps(N, end)typewriter trick (no JS, no per-letter markup), the "TAP TO ORDER" button pulses with an expanding-ringbox-shadowplus a radial-gradient "ripple," and a receipt slides down and prints its order number one digit at a time, torn edge included via a repeating diagonal-gradient background.

The biggest lesson: getting thesharedcharacter mechanics right first (float, blink, squish, sparkle burst) meant each new food was mostly "draw a shape and drop it into the rig" — and having that solid meant I could spend the JS-light budget entirely on the kiosk's CSS choreography instead.

Next up: I'd like the kiosk's order number to actually reflect whichever dish you last tapped, and maybe have the characters glance toward the kiosk when its button pulses.

Thanks for reading — go tap the kiosk. 🍙

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse