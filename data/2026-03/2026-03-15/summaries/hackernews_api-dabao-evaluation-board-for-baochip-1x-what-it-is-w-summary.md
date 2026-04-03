---
title: "Dabao Evaluation Board for Baochip-1x - What It Is, Why I'm Doing It Now, and How It Came About | Crowd Supply"
url: https://www.crowdsupply.com/baochip/dabao/updates/what-it-is-why-im-doing-it-now-and-how-it-came-about
date: 2026-03-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-15T06:01:36.683943
---

# Dabao Evaluation Board for Baochip-1x - What It Is, Why I'm Doing It Now, and How It Came About | Crowd Supply

# Dabao Evaluation Board for Baochip-1x – What It Is, Why I’m Doing It Now, and How It Came About  

## Overview  
- The Baochip‑1x is a RISC‑V microcontroller that includes a full Memory Management Unit (MMU), a rare feature in this class of embedded CPUs.  
- The board is being crowdfunded on Crowd Supply; the update explains the motivation, history, and open‑source strategy behind the project.  

## Why an MMU Matters  
- **Security & isolation:** The MMU provides per‑application virtual memory spaces, enabling secure, loadable apps and swap memory.  
- **Proven technology:** Page‑based protection has been reliable since the 1960s, similar to how AES remains trusted despite its age.  
- **Compatibility:** An MMU works alongside newer primitives (CHERI, PMP, MPU); it does not preclude their use but adds transparent address relocation.  

## Why MMUs Are Rare in Small CPUs  
- Historical cost constraints: early ARM7TDMI cores lacked MMUs to keep transistor counts and price low, leading to billions of units and a market norm.  
- ARM’s product segmentation (A‑series with MMU, M‑series with MPU) reinforced the separation, preventing price erosion of high‑end cores.  
- The entrenched “flat memory” model persisted even as transistor budgets grew dramatically.  

## Why I Chose to Include an MMU Now  
- RISC‑V’s open architecture removes the vendor‑imposed restrictions that kept MMUs out of low‑cost SoCs.  
- The Baochip‑1x can run Linux or a custom Rust OS (“Xous”) that leverages the MMU while targeting tiny memory footprints.  
- Open‑source RTL (e.g., VexRiscv) allows a “mostly open” implementation without waiting for a fully open silicon ecosystem, which may take a decade.  

## Open‑Source Philosophy & Practical Compromises  
- Goal: move toward a fully open silicon stack, but current PDKs and IP are not yet mature enough for mass‑market products.  
- The Baochip‑1x uses partially open RTL; closed‑source parts are limited to non‑computational blocks (AXI bus framework, USB PHY, PLL, regulators, I/O pads).  
- These closed components act as “wires” – they transmit data without altering it, reducing the risk of hidden functionality while still enabling a functional chip today.  

## Impact on the Community  
- Providing a partially open SoC now empowers developers who want to avoid proprietary ARM MPUs and start building open‑source firmware and OSes.  
- A larger community can begin de‑reliance on ARM, creating a mature application stack that will be ready when fully open silicon becomes economically viable.  

## Closing Note  
- All data‑processing logic in the Baochip‑1x is available for inspection and simulation; only peripheral glue logic remains closed.  
- This approach balances immediate usability with the longer‑term vision of truly open hardware.