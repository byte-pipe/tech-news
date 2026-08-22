---
title: CFETs Forge Better Connections
url: https://semiengineering.com/cfets-forge-better-connections/
date: 2026-08-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-23T06:00:57.607595
---

# CFETs Forge Better Connections

# CFETs Forge Better Connections

## Overview
- CFETs (complementary field‑effect transistors) will soon be introduced by leading‑edge manufacturers, stacking p‑ and n‑type nanosheet transistors vertically.  
- Expected benefits: ~40 % higher packing density, 50 % performance improvement, and up to 70 % efficiency gain.  
- The main technical hurdle is creating reliable vertical interconnects for signal, power, and backside connections while maintaining defect‑free epitaxy and precise alignment.

## Key Takeaways
- Intel, Samsung, TSMC, and IBM all plan to use direct backside vias for backside power delivery, but differ in nanosheet‑tier connection strategies.  
- Core CFET requirements: defect‑free epitaxial layers, ALD‑deposited high‑k dielectrics, work‑function‑optimized metals, and possibly layer‑transfer techniques.  
- Multi‑physics virtual simulation accelerates pathfinding, integration, and yield optimization, reducing the need for costly silicon iterations.

## Approaches by Major Foundries
- **IBM**: Sequential flow; first set of transistors fully fabricated before the second set, with a slight offset between tiers.  
- **Intel**: Explores both monolithic stacks and a hybrid‑substrate method that matches each transistor type to its optimal silicon substrate, improving p‑FET performance.  
- **TSMC**: Uses backside gate contacts and two variants of vertical contact plugs for SRAM bit‑cell connections; emphasizes advanced wafer bonding, backside thinning, and precise front‑to‑back alignment.  
- **Samsung**: Introduced a novel dielectric stack separating the two gate regions and demonstrated 42 nm gate‑pitch CFETs with triple‑stack channels and a middle‑dielectric‑isolation (MDI) layer containing three germanium concentrations.

## Material and Process Challenges
- Nanometer‑scale misalignments (as little as 2 nm) can cause catastrophic yield loss.  
- Warpage at micro‑ or nanoscale impacts device performance and reliability.  
- Backside power delivery adds complexity, increasing sensitivity to process variation and requiring highly accurate alignment.  
- Adding more nanosheets raises drive current but also multiplies process steps; a 3‑sheet transistor is significantly harder to fabricate than a 2‑sheet version.

## Role of Simulation
- Multi‑physics modeling predicts warpage, copper density variation, and other defects early in the design cycle.  
- Enables creation of a “bank” of design options; at any design milestone (e.g., 60 % or 90 % complete) engineers can evaluate the best copper‑density dispersal or interconnect scheme.  
- Prevents last‑minute surprises that would be too late to fix before tape‑out.

## Impact on Device Architecture
- Standard‑cell height is expected to shrink from ~5T to 4T or less, depending on the process.  
- In SRAM, CFETs could move from a conventional 6T cell to a compact 4F2 configuration, leveraging the higher density.  
- The technology, first applied in advanced logic, is expected to cascade to DRAM and NAND, creating synergistic performance gains across the product portfolio.

## Nanosheet Flow Highlights
- Epitaxial growth creates a Si/SiGe heterostack; SiGe layers are later removed to release suspended silicon nanosheets that form the channel.  
- Typical stack for a 3‑nanosheet nFET over a 3‑nanosheet pFET: 6 Si layers and 5 SiGe layers.  
- Nanosheet widths range from ~11 nm to 25 nm; thickness is only a few nanometers.  
- Surrounding each sheet is an ALD‑deposited high‑k dielectric and a metal gate; CFETs add a middle‑dielectric‑isolation (MDI) layer to separate top and bottom gates.  
- Example Samsung MDI process (post‑dummy gate): wafer prep → STI → dummy gate → bottom S/D etch/growth → S/D isolation → top S/D growth → GAA formation → replacement metal gate → MOL formation → BEOL integration.  

These points capture the current state, divergent strategies, and critical technical considerations shaping the rollout of CFET technology.