---
title: Intel Panther Lake Teardown, 18A, BSPD, GAAFET, SemiAnalysis STEEL
url: https://newsletter.semianalysis.com/p/intel-panther-lake-teardown
date: 2026-09-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-28T13:23:12.802127
---

# Intel Panther Lake Teardown, 18A, BSPD, GAAFET, SemiAnalysis STEEL

# Intel Panther Lake Teardown Summary

## Overview
- Panther Lake is Intel’s first commercial chip using the 18 Å (18A) process, featuring backside power delivery (BSPD) branded as PowerVia and Intel’s initial gate‑all‑around (GAA) transistors called RibbonFETs.  
- The chip demonstrates Intel’s shift from roadmap speculation to shipped silicon, marking a milestone in its effort to regain competitiveness.  
- The teardown was performed by the SemiAnalysis STEEL lab, focusing on the PTL‑U compute tile, both GPU tile options, and the 12‑lane I/O tile.

## Architecture & Packaging
- The package uses Intel’s Foveros‑S advanced 3‑D stacking: a passive base tile supports one compute tile, one GPU tile, and one I/O tile.  
- Compute tiles (both variants) are built on Intel 18A; the GPU tiles are either a 4‑core GT1 on Intel 3 Å or a 12‑core GT2 on TSMC N3E.  
- I/O tiles are fabricated on TSMC N6.  
- Logic density of Intel 18A compute logic is comparable to TSMC N3E GPU logic, but lags behind TSMC N3P, N2, and Samsung SF2 in peak density.

## PowerVia – Backside Power Delivery
- Traditional chips route power and signals through the same front‑side metal stack, consuming routing resources near transistors.  
- PowerVia moves the main power network to the backside, separating it from front‑side signal routing.  
- The backside power stack (BM0‑BM5) connects to nano‑TSVs that link to local source/drain contacts; the front‑side stack (M0‑M14) carries signals.  
- Process flow: after forming front‑side contacts, nano‑TSVs are etched from the front, the wafer is bonded to a carrier, flipped, the original substrate is removed, and backside metal is deposited on exposed TSV tips.  
- This approach shortens and widens power paths, reducing resistance but still occupies some standard‑cell area, unlike a direct backside contact.

## Backside Interconnect Details
- PowerVia’s supply path: backside Cu rails → Mo‑lined W nano‑TSVs → local transistor contacts.  
- The tapered TSV‑to‑rail connection spans ~150 nm. A Ta liner ensures Cu adhesion; AlOₓ acts as an etch‑stop and protects the metal during dielectric removal.  
- Intel uses a double AlOₓ layer (AlOₓ/SiN/AlOₓ) to provide two protected endpoints, widening the process window and preventing metal erosion.  
- Comparisons: Samsung SF2 (the incumbent GAA node) lacks BSPD; its backside stack uses a single AlOₓ layer. TSMC’s stack typically employs AlN/AlOₓ/SiOC with optional second AlOₓ layer.

## Comparison with Competing Nodes
- Intel 18A RibbonFETs show a half‑pitch of 550 nm versus Samsung SF2’s 423 nm in comparable logic.  
- Despite the advanced PowerVia architecture, 18A does not surpass TSMC N3P, N2, or Samsung SF2 in peak logic density.  
- The high‑end GPU in Panther Lake still relies on TSMC N3E, indicating Intel’s current reliance on external foundry technology for top‑performance graphics.

## Conclusions
- Panther Lake validates Intel’s 18A process, PowerVia BSPD, and Foveros‑S 3‑D integration, representing a tangible step toward a competitive product portfolio.  
- The implementation improves gate control and reduces front‑side power congestion, though it adds capacitance, thermal resistance, and manufacturing complexity.  
- Logic density remains competitive with TSMC N3E but trails newer nodes, suggesting further scaling work is needed for Intel to lead in peak density.  
- The teardown provides a detailed view of material choices, interconnect schemes, and the trade‑offs inherent in Intel’s latest manufacturing approach.