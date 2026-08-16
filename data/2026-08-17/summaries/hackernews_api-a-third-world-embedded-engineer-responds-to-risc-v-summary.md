---
title: "A Third World Embedded Engineer Responds to \"RISC-V: They Should Have Known Better\""
url: https://rvembedded.com/blog_post/12/
date: 2026-08-17
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-17T08:45:04.745214
---

# A Third World Embedded Engineer Responds to "RISC-V: They Should Have Known Better"

# Summary of “A Third World Embedded Engineer Responds to ‘RISC‑V: They Should Have Known Better’”

## Context and Motivation
- The author works in Trinidad and Tobago, where shipping costs for development boards are high (US $60–200) and free‑shipping offers from major distributors do not apply.  
- For students and hobbyists in the same region, the price difference between a ten‑cent chip and a one‑dollar chip determines whether a class can have individual boards or must share a single demo unit.  
- The author feels Dmitry Grinberg’s criticism of RISC‑V focuses on architectural elegance while ignoring the practical accessibility issues that matter most to developers outside the US/Europe.

## Points of Agreement with Grinberg
- Acknowledges some quirks of the RISC‑V ISA, such as compressed store offsets and the optional Zicsr extension.  
- Confirms that the RV32EC profile (few registers, no multiplier/divider, machine‑mode only) matches the requirements of ultra‑cheap microcontrollers.  
- Shares Grinberg’s belief that RISC‑V will eventually dominate the “cheap‑as‑dirt” MCU market.

## Core Disagreements
- Grinberg argues that a single ISA cannot serve both high‑end CPUs and low‑cost microcontrollers; the author disputes this claim.  
- He demonstrates three categories of RISC‑V silicon that illustrate the ISA’s scalability:

  1. **CH32V003** – A ten‑cent RV32EC part with 2 KB SRAM, 16 KB flash, 16 registers, no multiplier or divider. Used in a bin‑monitor product, an agricultural door‑controller, and a low‑cost whistle switch.  
  2. **CH32H417** – A dual‑core MCU (400 MHz and 144 MHz) with 896 KB SRAM, 960 KB flash, USB 3.2, 100 M Ethernet, graphics accelerator, etc. Runs a web browser, GAN‑based image generation, and real‑time facial recognition within 150 KB RAM.  
  3. **Baochip‑1x** – A 22 nm SoC with an MMU, capable of running the Rust microkernel Xous, the seL4 microkernel, and mainline Linux. Featured in the DEF CON 34 badge as an open‑source security key.

- Additional examples: the ESP32‑C3 (≈ $1) running an NES emulator, and the Orange Pi RV2 booting Ubuntu Linux in five minutes.

## Implications for Education and Development
- Low‑cost RISC‑V boards enable each student to have a personal development platform, unlike expensive ARM alternatives that limit hands‑on learning.  
- Shipping constraints make the availability of inexpensive RISC‑V parts essential for regions that are often overlooked by mainstream hardware blogs.  
- The “space” created by RISC‑V is less about ISA elegance and more about practical accessibility for the 99 % of the world outside the US and Europe.

## Conclusion
- While Grinberg’s technical complaints have merit, they do not affect developers in resource‑constrained environments who care first about whether the hardware can reach their desk.  
- Real‑world RISC‑V ecosystems already span from ten‑cent microcontrollers to high‑performance SoCs, disproving the notion that a single ISA cannot serve both ends of the performance spectrum.  
- The author remains optimistic that RISC‑V will continue to expand affordable hardware options worldwide, benefiting engineers and educators in the “third world” and beyond.