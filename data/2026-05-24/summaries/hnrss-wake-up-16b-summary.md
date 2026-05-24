---
title: wake up! 16b
url: https://hellmood.111mb.de/wake_up_16b_writeup.html
date: 2026-05-24
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-24T18:02:20.450144
---

# wake up! 16b

# wake up! 16b

## Overview
- Released at Outline Demoparty (May 2026, Ommen, NL) as a 16‑byte x86 real‑mode DOS intro that visualises and sonifies a Sierpinski triangle.
- Author revisits old sketches after being inspired by Plex’s “Rainbow Surf” (16 bytes) and discovers a compact algorithm that intertwines graphics and audio.
- Core idea: each time step draws one line of the Sierpinski fractal to video memory and simultaneously outputs the same bit pattern to the PC speaker.

## Code (16 bytes)
```
int 10h          ; set video mode 0 (40×25 text)
mov bh, 0xb8     ; video memory segment (0xb800)
mov ds, bx
L:
lodsb            ; load byte from DS:SI, increment SI
sub si, byte 57  ; move back 56 bytes (‑57 + 1 from lodsb)
xor [si], al     ; XOR loaded byte with memory at new SI
out 61h, al      ; send byte to speaker port
jmp short L
```

## The Canvas: Video Memory as Working Space
- `int 10h` clears the screen to spaces (0x20) with attribute 0x07, leaving a uniform pattern in the 2 000 character cells.
- Video buffer at 0xb800 serves as both display and calculation area; the algorithm mutates this memory in‑place.

## Engine: Additive Prefix Sums (Mathematical View)
- If the memory were zeroed and `add` used instead of `xor`, stepping 16 bytes would traverse the 64 KB segment in exactly 4 096 steps (65 536 / 16).
- The accumulator follows a scaled binomial sequence:  
  `A⁽ᵖ⁾[k] ≡ 2·C(k+p, p‑1) (mod 256)`.
- Because 4 096 is a multiple of 256, carries align on each wrap, resetting the accumulator cleanly.

## Crystallisation: XOR Produces the Sierpinski Pattern
- Using XOR (carry‑free addition) on the least‑significant bit yields the elementary cellular automaton rule 60, which generates the Sierpinski triangle.
- Starting value `2` (binary 0000 0010) toggles only bit 1, so the visual and audio output correspond to that single bit plane.

## Voice of the Machine: Audio Generation
- `out 61h, al` writes the current byte directly to the PC‑speaker port; bit 1 drives the speaker on/off.
- The XOR‑derived bit stream creates a self‑similar square‑wave pattern (a bytebeat) whose frequency and pulse width evolve with the fractal.
- Additional bytes from the surrounding 64 KB segment (including shadowed BIOS code) add a gritty, “punky” texture to the sound.

## 56‑Byte Step: Visual Shear and Octave Shift
- The `sub si, 57` together with `lodsb` moves the pointer back 56 bytes each iteration, effectively stepping –56 bytes.
- 56 does not divide the segment evenly; the loop visits only offsets that are multiples of 8, taking 8 192 steps and wrapping seven times before repeating, halving the fundamental frequency (one octave lower).
- On an 80‑byte wide text screen this backward step appears as a forward shift of 24 bytes (12 columns), visiting only 10 distinct columns and producing diagonal “pillars” of characters.

## Real‑Hardware Test and Final Thoughts
- A community member ran the demo on a 286 with an EGA card emulating MDA (address changed to 0xb000) and an IBM 5151 monitor; the green text matched the intended aesthetic.
- Phosphor persistence of the monitor blurred the fast visual motion, but the audio behaved as described.
- Author appreciates the feedback and notes that the Sierpinski‑driven sound remains compelling even when minor byte changes alter the timbre.