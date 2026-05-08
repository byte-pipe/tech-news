---
title: Ask HN: We just had an actual UUID v4 collision... | Hacker News
url: https://news.ycombinator.com/item?id=48060054
date: 2026-05-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-09T07:56:35.485909
---

# Ask HN: We just had an actual UUID v4 collision... | Hacker News

# Ask HN: We just had an actual UUID v4 collision...

## Incident description
- A database flagged a duplicate UUID‑v4: `b6133fd6-70fe-4fe3-bed6-8ca8fc9386cd`.
- The first occurrence was inserted in 2025; the second appeared today in a fresh insert.
- The project uses the npm package `uuid` and generates IDs with `uuidv4()`.
- The database holds only about 15 000 records, making a collision seem statistically impossible.

## Why collisions can happen
- UUID‑v4 relies on a high‑quality source of entropy; if the source is weak, collisions become possible.
- Entropy sources can be degraded by hardware defects, software bugs, or developer misunderstandings.
- Detecting a broken entropy source is expensive, so many systems only notice the problem when a collision occurs.
- Because of this risk, UUID‑v4 is often prohibited in high‑assurance or high‑reliability software.

## Community discussion on entropy sources
- **Cloudflare’s lava‑lamp wall**: used as a visible, non‑deterministic entropy source, combined with many other inputs.
- Additional physical entropy ideas mentioned:
  - Pendulums, wave machines, mobiles.
  - Ant farms, hamster wheels, other critter‑driven mechanisms.
  - Background radiation (Fourmilab Hotbits).
  - Camera noise in total darkness.
  - Johnson–Nyquist noise from a resistor.
  - Atmospheric noise (random.org).
  - High‑gain amplifiers connected to resistors or diodes, even via a PC microphone jack.
- Software techniques to improve randomness:
  - Collect many independent parameters (mouse movements, timing, frame counts) before seeding a PRNG.
  - Use algorithms like the Von Neumann extractor to turn biased randomness into unbiased bits.
  - Apply cryptographic hashing to the collected entropy, making collisions astronomically unlikely.

## Alternatives to UUID‑v4 for identifiers
- High‑reliability systems prefer identifier schemes that do not depend solely on random entropy.
- Approaches include:
  - Deterministic, monotonic IDs (e.g., Snowflake, ULID) that combine timestamps, machine IDs, and counters.
  - Cryptographically secure hashes of unique data (e.g., SHA‑256 of a combination of attributes).
  - Using hardware true‑random number generators (TRNGs) as the entropy source for any random‑based IDs.