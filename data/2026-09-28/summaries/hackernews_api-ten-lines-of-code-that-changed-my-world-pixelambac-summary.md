---
title: Ten Lines Of Code That Changed My World – Pixelambacht
url: https://pixelambacht.nl/2026/ten-lines-of-code/
date: 2026-09-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-28T13:23:05.289367
---

# Ten Lines Of Code That Changed My World – Pixelambacht

# Ten Lines Of Code That Changed My World

## Hello World
- The classic BASIC program that prints “HELLO, WORLD!” and loops forever.  
- It was my first successful communication with a computer and taught me that a computer will obey exactly what you tell it to.

## Holy JavaScript weirdness, Batman!
- A one‑liner that builds a string using `Array(16).join('wat')-1 + ' Batman'`.  
- Running it in the browser console produces a funny mash‑up of pop‑culture and the “JavaScript is stupid” feeling that made me laugh.

## Self modifying 6502 assembly code
- A small 6502 routine that copies bytes from `$2000` to `$0400`, then modifies its own instruction bytes to change the source and destination ranges.  
- Seeing code that can rewrite itself showed me how low‑level programming removes all safety nets and gives you total freedom (and danger).

## touch.bat
- A batch one‑liner: `type nul > ".\%*"` that creates an empty file on Windows.  
- I used it from NT through Windows 7 via the Total Commander mini‑shell to quickly generate placeholder files.

## CSS debugger
- A single rule `border: 10px solid hotpink;` that acts as a visual “debugger” for CSS.  
- The bright hot‑pink border makes layout problems instantly visible, serving as the `printf` of styles.

## Infinite lives
- The cheat `POKE 9450,173` writes a byte directly into a game’s memory.  
- It gave me unlimited lives/energy and revealed that any game value can be altered if you know where to peek and poke.

## The speed‑up loop
- A dummy loop `for(i=0;i<1000000;i++) {;}` that can be sped up by removing a zero.  
- The anecdote illustrates how developers sometimes claim “optimizations” by simply reducing loop iterations.

## RTFM or `rm -rf /`
- The infamous command `rm -rf /` that, when run as root, wipes a Linux system.  
- In early‑2000s IRC help channels it was jokingly presented as the universal fix for any Linux problem.

## SKAN2.PAS
- A Borland Pascal program that iterates through all three‑letter username combinations and launches `full.exe` with each as an argument.  
- It was a crude scanner used on a school LAN to discover default‑password accounts, showing early hacking experimentation.

## CSS280
- A 280‑character CSS snippet that animates a poem without any HTML or JavaScript.  
- It demonstrates how expressive CSS can be within tight character limits, using a massive `1e+9` animation duration to simulate “infinite”.