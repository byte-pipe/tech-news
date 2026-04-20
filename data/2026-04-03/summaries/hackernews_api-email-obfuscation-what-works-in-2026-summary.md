---
title: Email obfuscation: What works in 2026?
url: https://spencermortensen.com/articles/email-obfuscation/
date: 2026-04-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-03T01:03:20.131134
---

# Email obfuscation: What works in 2026?

# Email obfuscation: What works in 2026?

## Overview
- The article evaluates a range of methods for hiding plain‑text email addresses from spambots, reporting the percentage of 318 tested spammers each technique blocks.
- Combining multiple techniques by splitting the address into segments is recommended for stronger protection.

## Techniques and effectiveness

- **No protection** – blocks 0% of spammers. Plain address is fully exposed.
- **HTML entities** – blocks 95%. Easy for most harvesters to decode; still stops many basic bots.
- **HTML comments** – blocks 98%. Stops only harvesters that cannot parse comment tags; still effective against most simple bots.
- **HTML SVG** – blocks 100%. Stores the address in an SVG object; accessible to screen readers but the address remains in plain text within the SVG file.
- **CSS `display:none`** – blocks 100%. Hides parts of the address via CSS; most harvesters ignore style rules. Must use true `display:none` to remain accessible.
- **JavaScript concatenation** – blocks 100%. Builds the address from string fragments at runtime; the full address is still present in the source code, so not fully safe.
- **JavaScript ROT‑18** – blocks 100%. Encodes the address with ROT‑18; easy for harvesters that ignore JavaScript or use a different rotation scheme.
- **JavaScript conversion** – blocks 100%. Stores gibberish in HTML and converts it with a custom script; harvesters that cannot execute JavaScript cannot retrieve the address.
- **JavaScript AES encryption** – blocks 100%. Encrypts the address with AES‑256 and decrypts in the browser using SubtleCrypto; requires HTTPS and a modern browser.
- **JavaScript user interaction** – blocks 100%. Reveals the address only after a user action, raising the bar for automated harvesting.
- **HTML symbol substitution** – blocks 97%. Uses “AT” and “DOT” text; easily reversible and harms usability.
- **HTML instructions** – blocks 100%. Provides manual instructions to edit the address; relies on human or AI interpretation and reduces usability.
- **HTML image** – blocks 100%. Shows the address as an image; completely inaccessible to screen readers and inconvenient for all users.

## Recommendations
- Use a combination of techniques, preferably mixing CSS hiding, JavaScript‑based methods, and server‑side rendering to maximize protection.
- Prioritize accessibility: methods that rely on `display:none` or proper semantic markup keep content reachable for screen‑reader users.
- Ensure HTTPS when employing cryptographic JavaScript (AES) to avoid context restrictions.
- Avoid approaches that break usability (symbol substitution, instructional text, image‑only addresses) unless the site’s audience can tolerate the extra effort.
