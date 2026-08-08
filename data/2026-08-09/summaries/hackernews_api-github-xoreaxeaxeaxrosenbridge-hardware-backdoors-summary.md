---
title: GitHub - xoreaxeaxeax/rosenbridge: Hardware backdoors in some x86 CPUs · GitHub
url: https://github.com/xoreaxeaxeax/rosenbridge
date: 2026-08-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:36:04.717120
---

# GitHub - xoreaxeaxeax/rosenbridge: Hardware backdoors in some x86 CPUs · GitHub

# project:rosenbridge – hardware backdoors in x86 CPUs

## Overview
- The repository documents a hardware backdoor discovered in certain x86 processors, primarily VIA C3 CPUs.  
- The backdoor lets user‑mode (ring 3) code bypass processor protections to read and write kernel‑mode (ring 0) memory.  
- Although normally disabled and requiring kernel execution to enable, it has been found enabled by default on some systems.

## Backdoor description
- Implements a small, non‑x86 core embedded alongside the main x86 core.  
- Activation is controlled by a model‑specific‑register (MSR) bit and a special launch instruction.  
- Commands are delivered via specially formatted x86 instructions that the hidden core interprets as its own “deeply embedded instruction set” (DEIS).  
- The hidden core executes these commands with full access to memory, registers, and the execution pipeline, bypassing all privilege checks.  
- It is distinct from known coprocessors such as the Management Engine or Platform Security Processor and resides deeper within the CPU.

## Affected systems
- Currently believed to affect only VIA C3 processors, which are used in industrial automation, point‑of‑sale, ATMs, healthcare devices, and various consumer desktops and laptops.  
- Later CPU generations no longer contain this feature.

## Checking your CPU
- Clone the repository, build the utility, load the `msr` kernel module, and run `./bin/check` on bare metal (not in a VM).  
- The tool is in an alpha state; it may crash, panic, or hang systems that do not contain the backdoor.  
- It is tailored to a specific processor family; variations of the backdoor may not be detected.

## Closing the backdoor
- If the check indicates vulnerability, build and install the script in the `fix` directory, then reboot.  
- The script disables the backdoor early in the boot process via MSR updates.  
- An attacker with kernel privileges could re‑enable the backdoor, so the fix is not a permanent safeguard for compromised systems.

## Tools and techniques
- **asm** – Assembler for the Deeply Embedded Instruction Set, converting custom rosenbridge assembly into x86 instructions.  
- **esc** – Proof‑of‑concept demonstrating privilege escalation through the backdoor.  
- **fix** – Script outline for disabling the backdoor via MSR writes.  
- **fuzz**, **wrap**, **deis**, **exit**, **manager**, **kern**, **lock**, **proc**, **test**, **util** – A suite of fuzzers, monitoring utilities, and helper programs used to discover the launch instruction, decode the DEIS format, explore hidden core behavior, and manage distributed fuzzing tasks.

## Looking forward
- The vulnerability is limited to early C3 CPUs; newer generations are unaffected.  
- The work serves as a case study and thought experiment on how hidden backdoors can arise in increasingly complex processors and how researchers can detect them.  
- The provided tools form a foundation for deeper processor‑level vulnerability research.

## Disclaimer
- The findings represent the authors’ interpretations of their research.  
- The hidden functionality was likely intended as a legitimate feature for embedded markets and unintentionally left enabled on some early processors.  
- No malicious intent is implied.

## Author
- Christopher Domas (@xoreaxeaxeax) – research lead for project:rosenbridge.