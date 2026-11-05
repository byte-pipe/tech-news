---
title: A thousand fewer paths to root | OpenAI
url: https://openai.com/index/a-thousand-fewer-paths-to-root
date: 2026-11-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:24:30.632418
---

# A thousand fewer paths to root | OpenAI

# A thousand fewer paths to root – Summary

## Methodology
- Pipeline stages:  
  1. Identify security‑relevant kernel components.  
  2. Statically scan for candidate findings.  
  3. Dynamically reproduce candidates in an isolated VM.  
  4. Generate a minimal proof‑of‑concept exploit.  
  5. Produce a candidate patch.  
  6. Human researcher reviews and reports results.  
- Outputs per finding: root‑cause analysis, crashing PoC, candidate patch, full exploit.

## Findings
- **Run statistics (mid‑October 2026)**  
  - 2,308 candidate kernel findings.  
  - 1,724 vulnerabilities dynamically reproduced.  
  - 291 information‑leak PoCs.  
  - 948 working local‑privilege‑escalation (LPE) exploits.  
- **Cost**  
  - Total API credit spend: **$1,213,430**.  
  - Approx. **$1,279 per LPE** exploit.  
- **Economic perspective**  
  - Historical Linux‑kernel LPE bounties: $20k–$70k each (Pwn2Own, TyphoonPWN).  
  - Valuing 948 exploits yields **$18.9 M–$66.3 M**, i.e., 16×–55× the pipeline cost.  
- **KernelCTF environment**  
  - 25 information‑leak PoCs and 21 LPE exploits discovered.  
  - Cost: **$32,936** in API credits.  
  - Potential bounty ≈ **$1.5 M** (≈45× scanning cost).  
- **Novel techniques**  
  - At least 10 previously unknown Linux exploitation techniques were uncovered.

## Reflections
- The Linux community responded quickly: >100 LPEs patched or staged within 10 days of the scan, with ~300 more under discussion.  
- Automated patch generation is essential to keep pace with frontier‑model vulnerability discovery and to shrink exploitation windows.  
- Human‑guided iteration can yield AI‑generated patches that are functionally correct, style‑consistent, and resistant to variant attacks.  
- The newer cyber model found >5× more novel LPEs than a GPT‑5.6 run three months earlier, despite intervening hardening.  
- Large codebases will likely need repeated scan‑fix cycles across successive model generations.  
- Low‑privileged, unpatched accounts effectively provide root‑level access to well‑resourced attackers; defense‑in‑depth measures (e.g., Firecracker, gVisor) are critical.  
- In the near future, any existing vulnerability will be discoverable by frontier models, and less capable models may generate exploits once disclosed.  
- Priorities for long‑term security: high‑assurance software, secure‑by‑default model training, attack‑surface reduction, and formal verification for core components (OS kernels, browsers, parsers, TCP/IP stacks).

## Why the Linux kernel
- Powers Android, cloud infrastructure, supercomputers, and billions of devices.  
- Over 40 million lines of code, exposing a vast attack surface via syscalls, networking, filesystems, and drivers.  
- Serves as a realistic, high‑impact target to evaluate frontier‑model capabilities at scale.

## Cost analysis (overview)
- Detailed API‑cost breakdown provided for each pipeline stage to help researchers estimate resources for replication or extension.  
- Goal: enable defenders to find and fix vulnerabilities, raising the cost for attackers and improving overall software security.