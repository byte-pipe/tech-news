---
title: "Cloudflare Turnstile requiring fingerprintable WebGL - lanodan's cyber-home"
url: https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting
date: 2026-05-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:18:50.382396
---

# Cloudflare Turnstile requiring fingerprintable WebGL - lanodan's cyber-home

# Cloudflare Turnstile requiring fingerprintable WebGL

## Overview
- Since about a week ago, the author’s WebKit‑GTK based browser gets stuck in an infinite loop when encountering Cloudflare Turnstile, blocking access to many sites.  
- The issue stems from Cloudflare demanding a WebGL fingerprint of the device, which the author interprets as a tracking measure.

## Cloudflare’s Justification
- Turnstile message: “Turnstile uses browser fingerprinting to verify you're human. Privacy tools that block or randomize fingerprinting make your browser look like a bot… Temporarily allowing fingerprinting for this site will fix the issue.”

## Impact on WebKit‑GTK
- WebKit has blocked the required WebGL fingerprinting for years, treating it as a privacy‑violating technique.  
- Consequently, Cloudflare effectively bans all WebKit‑GTK browsers, while apparently allowing Safari (which has an exception).

## Firefox Situation
- Firefox 145.0 passes Turnstile without issues, showing only “Canvas Randomization Detected.”  
- When the `privacy.resistFingerprinting` setting is manually enabled, Turnstile still passes, though the author notes the setting is not automatically applied even under “Strict” or “Enhanced Privacy Protection.”  
- A recent bug (Bugzilla #1916271) caused Firefox to expose sanitized GPU characteristics, whereas WebKit and Blink return hard‑coded strings.

## Implications
- Users relying on privacy‑focused browsers that block fingerprinting may be unable to complete Cloudflare’s device verification.  
- The author invites discussion on the Fediverse for further comments.