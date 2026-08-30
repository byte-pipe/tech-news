---
title: RISC-V is now officially supported by CPython! | Python Insider
url: https://blog.python.org/2026/08/riscv-now-officially-supported/
date: 2026-08-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-31T02:22:34.403547
---

# RISC-V is now officially supported by CPython! | Python Insider

# RISC‑V is now officially supported by CPython

## What is RISC‑V?
- An open instruction set architecture (ISA) that anyone can implement.  
- Unlike proprietary ISAs such as x86 and ARM, it is developed as an open standard.  
- The ecosystem has been growing rapidly and is projected to quadruple by 2032, making reliable Python support increasingly important.

## Getting here
- The support reached tier‑3 status thanks to extensive community contributions: testing on real hardware, fixing architecture‑specific bugs, improving build scripts, and reviewing patches.  
- Reliable testing on actual RISC‑V machines was crucial; the RISE Project supplied hardware, buildbots, and debugging assistance.  
- Specific thanks were given to Ludovic Henry (RISE), Furkan Onder, Emma Smith, and many others.  
- The author’s work was funded by a fellowship from the Sovereign Tech Agency.

## What’s next?
- Integrate RISC‑V testing directly into CPython’s continuous‑integration pipeline, using the RISE RISC‑V Runners initiative, to provide faster feedback before patches are merged.  
- Aim to promote RISC‑V from tier‑3 to tier‑2 support in the long term.  
- Explore architecture‑specific optimizations that could improve CPython performance on RISC‑V.  
- Encourage users with RISC‑V hardware to build, run, and test CPython, report breakages, and contribute feedback.  
- Continue community efforts across the broader Python ecosystem—packages, compilers, tooling, and infrastructure—to strengthen overall RISC‑V support.