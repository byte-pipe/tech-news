---
title: Quake Shareware, a CD-ROM just a little too full
url: https://fabiensanglard.net/quake_shareware_cd/index.html
date: 2026-08-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-18T12:12:30.338926
---

# Quake Shareware, a CD-ROM just a little too full

# Quake Shareware, a CD‑ROM just a little too full

## Background and motivation
- In the mid‑1990s CD‑ROM drives were prized for their 640 MiB capacity, enabling multimedia content such as high‑resolution photos, VOC soundtracks, and low‑frame‑rate videos.
- Game developers struggled to fill the disc; some titles added full‑motion video or high‑quality music.
- John Carmack (id Software) joked that a CD version of DOOM would include “The Making of DOOM” as a one‑hour feature film.

## id Software’s shareware experiment
- By June 1996 id completed **Quake**, a 22 MiB game, and decided to exploit the remaining CD space by encrypting the full id catalogue on the same disc.
- The plan: sell the shareware CD for $9.95, let buyers call an 800‑number, pay, and receive a password to unlock the full game and other titles.
- The CD was announced on 3 July 1996 and released on 30 August 1996.

## Implementation details
- The disc contained a “Shareware version” label, a phone number (1‑800‑669‑9342), and a “SOURCE CODE” field for the order.
- The unlock GUI generated a **CHALLENGE** code; after payment the user received a **SERIAL** (unlock code) to enter.
- The system used TestDrive Corp.’s encryption: original executables were denatured into *.MJ3 files, with encrypted headers (*.ST3) and a secret seed derived from the SERIAL.

## Failure of the model
- Hackers quickly cracked the shareware, using the tool **QCRACK.EXE** (released 39 days after the CD’s launch) to generate valid SERIALs from any CHALLENGE.
- The SERIAL turned out to be merely a proof of payment; the unlock program could recompute it locally, making the protection rely solely on obscurity.
- Retail distribution collapsed: id was left with ~150 000 unsold CDs, and the phone‑based unlock service became unmanageable.

## Technical breakdown of the crack
- The CHALLENGE (11 digits) splits into a 4‑digit GAME‑ID, a 7‑digit OFFSET, and a DEPTH.
- GAME‑ID indexes an encrypted database (SKU.17) to obtain a codename (e.g., “doom2”).
- The codename retrieves a 512‑byte DOC file from FLOWLIB.LIB; combined with “Testdrive Corp.” it creates a unique 254‑entry table.
- DEPTH and OFFSET walk the table backwards, XOR‑ing DEPTH to produce a 16‑bit MEM value.
- The SERIAL is calculated from MEM, GAME‑ID, and fixed constants using a reversible algorithm (reverse7, XOR, arithmetic, and a leading “B”).

## Additional flaws and observations
- The unlock process required users to back up the game after unlocking because the CHALLENGE changed every run and every 5 minutes, preventing reuse of a SERIAL.
- The phone number remained active after CompUSA’s closure, but now only an automated message plays.
- Retailer codes (e.g., “12‑BSTBY” for BestBuy) were embedded in the ordering system, indicating a planned revenue‑share model that never materialized.