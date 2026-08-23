---
title: Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second
url: https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html
date: 2026-08-24
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-24T07:47:37.952385
---

# Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second

# Cloudflare Workers Spectre Attack Leaks JWT From Co‑Located Worker at 12 Bits/Second

## Overview
- Researchers demonstrated a remote Spectre variant that extracts a JSON Web Token (JWT) from a co‑located Cloudflare Worker at up to 12 bits per second, 360 × faster than the 2021 proof‑of‑concept.  
- The experiment used an attacker Worker and a victim Worker under the researchers’ control; the JWT was deliberately placed in the victim’s memory.  
- No real customer data was accessed during the study.

## Attack Mechanics
- Cloudflare Workers run multiple tenants in separate V8 isolates within a single OS process, relying on language‑level isolation rather than full process isolation.  
- The attack requires the attacker and victim Workers to be co‑located in the same process but in different V8 isolates.  
- No native code execution, V8 exploit, or sandbox escape is needed; the attacker controls valid JavaScript in its own isolate.  
- Timing side‑channels are obtained remotely via WebSocket communication, while Durable Objects keep an isolate alive for many hours, allowing prolonged observation.  
- Heavy WebSocket I/O increases iTLB activity, suppressing the branch‑misprediction signal that DyPrIs uses for detection, letting the attack proceed unnoticed.  
- Tests were run on Linux servers with AMD EPYC Zen 2/Zen 3 CPUs during low system load (10‑25 % CPU); higher load reduced the leakage rate but did not stop it.

## Results
- Leakage rate: up to **12 bits per second** with **99.16 % accuracy**.  
- Compared to the 2021 attack: 2 bits per minute (≈ 0.033 bits per second).  
- False‑positive rate reported as 0.61 % in the earlier study; the new attack shows the detection limits of DyPrIs.

## Cloudflare’s Response
- Immediate mitigation in production:  
  - Improved Dynamic Process Isolation (DyPrIs) detection.  
  - Integration of the V8 Sandbox to limit transient 64‑bit pointer exposure.  
  - Deployment of Memory Protection Keys (MPK)‑based in‑process isolation, rotating keys and memory layout to prevent cross‑isolate access.  
- No evidence of active exploitation in the past three years.  
- Cloudflare notes the issue as a limitation of the DyPrIs detection approach rather than a simple implementation bug.

## Mitigation Details (September 2025 rollout)
- **Improved DyPrIs** – stronger detection of anomalous execution patterns.  
- **V8 Sandbox** – caps transient pointer leakage to 64 bits.  
- **MPK‑based isolation** – places each Worker heap behind hardware‑enforced protection keys; about 12 keys are available on modern x64 systems, combined with rotating layouts to avoid key reuse across sandboxes.

## Context and Comparison
- The 2021 Spectre attack on Workers achieved 120 bits per hour (≈ 0.033 bits per second) and introduced DyPrIs as a defense.  
- The new attack demonstrates that DyPrIs, as originally designed, can be bypassed when I/O activity masks the detection signal.  
- Researchers argue that robust detection must occur during execution and rely on signals that cannot be suppressed by I/O.

## Implications
- Highlights the risk of side‑channel attacks in multi‑tenant serverless environments that share a process.  
- Shows that language‑level isolation may be insufficient against sophisticated micro‑architectural attacks.  
- Emphasizes the need for hardware‑assisted isolation (e.g., MPK) and continuous monitoring of execution characteristics.