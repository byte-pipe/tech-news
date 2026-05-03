---
title: GitHub - F2u0a0d3/goodboy-framework: 15-stage Windows malware development & analysis course in Rust. Red team builds it, blue team detects it. All 15...
url: https://github.com/F2u0a0d3/goodboy-framework
date: 2026-05-04
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-04T06:02:43.380435
---

# GitHub - F2u0a0d3/goodboy-framework: 15-stage Windows malware development & analysis course in Rust. Red team builds it, blue team detects it. All 15...

# Goodboy Framework Overview

## What It Is
- A 15‑stage hands‑on Windows malware development and analysis course written in Rust.  
- Each stage introduces a new offensive technique and provides corresponding defensive detection (YARA, Sigma, ETW, memory forensics).  
- All 15 binaries were submitted to VirusTotal and received 0 detections out of 76+ AV engines, with hashes documented for verification.  

## The 15 Stages
| Stage | Technique | Learning Focus | Lines of Code | Status |
|------|-----------|----------------|--------------|--------|
| 01 | Basic Loader | XOR decryption, PEB‑walk API hashing, anti‑sandbox, detection rules | 1,649 | Released |
| 02 | XOR Cryptanalysis | Known‑plaintext attack, entropy classification, memory scrubbing | 1,237 | Released |
| 03 | AES + Jigsaw | RC4 stream cipher, payload fragmentation, multi‑scale entropy detection | 1,492 | Released |
| 04 | API Hashing | Additive hash, cross‑DLL resolution, rainbow tables | 1,085 | Released |
| 05 | APC Injection | Early‑bird APC, remote decryption, triple encryption | 1,133 | Released |
| 06 | Variant Analysis | Family clustering, cross‑variant YARA, invariant detection | 1,191 | Released |
| 07 | Direct Syscalls | SSN resolution, inline syscall, hook bypass | 883 | Released |
| 08 | Indirect Syscalls | Gadget scanning, CALL‑based indirection, zero syscall in .text | 783 | Released |
| 09 | Anti‑Debug | Seven techniques (PEB, NtQIP, RDTSC, hardware breakpoints, etc.) | 766 | Released |
| 10 | Anti‑Sandbox | Hardware fingerprinting, weighted scoring, CFG‑safe detection | 1,008 | Released |
| 11 | Persistence | Registry Run key, path obfuscation, direct IAT imports | 1,144 | Released |
| 12 | Module Stomping | Overwrite DLL .text, CFG‑valid execution, PE‑sieve evasion | 1,230 | Released |
| 13 | Sleep Obfuscation | XOR‑encrypted sleep, VirtualProtect RX↔RW cycling, 95 % scanner miss | 1,254 | Released |
| 14 | Combined Loader | 7‑phase attack chain, MBA XOR key derivation, multi‑DLL fallback | 1,176 | Released |
| 15 | C2 Agent | Encrypted HTTP beaconing, browser‑gate, 0/71 VT, 2,152‑line learning path | 2,152 | Released |

## How Each Stage Works
- Each stage folder contains:
  - `*.exe`: compiled 64‑bit Rust binary (~280‑300 KB) for analysis with Ghidra or x64dbg.  
  - `README.md`: quick start guide and technical overview.  
  - `LEARNING_PATH.md`: 700‑1,600 lines of theory, exercises, Python scripts, detection rules, and adversarial challenges.  
- No source code is provided; learners reverse‑engineer the binary using the learning path as a guide.

## Quick Start
1. Prepare a Windows 10/11 x64 VM (FlareVM recommended).  
2. Install Ghidra 11.x, x64dbg + ScyllaHide, Python 3.10+, PE‑bear.  
3. Begin with Stage 01 and follow the learning path sequentially.  
4. VM requirements for sandbox‑evasion gates:  
   - ≥4 CPU cores, ≥8 GB RAM, ≥100 GB disk.  
   - Run the VM for 30 + minutes before executing binaries.  
   - Screen resolution ≥1920×1080.

## What Makes This Different
- **Dual Perspective**: Every technique is taught from both red‑team (build) and blue‑team (detect) viewpoints, with exercises to break your own detections.  
- **Empirical Evasion Data**: Each binary’s VirusTotal results are recorded, showing which engines detected what and why; per‑engine bypass techniques are demonstrated with proof.  
- **Production‑Grade Code**: Binaries include Control Flow Guard, PE metadata spoofing, Rich header re‑keying, multiple evasion gates, and real shellcode execution.

## Arms‑Race Narrative
- Stage 01 introduces a basic loader; AV signatures the XOR key.  
- Stage 02 changes the key; blue team uses known‑plaintext attack to recover it.  
- Stage 03 switches to RC4 + jigsaw; blue team detects the permutation map.  
- Stage 04 hides API resolution with custom hashing; blue team builds rainbow tables.  
- Stage 07 bypasses ntdll hooks with direct syscalls; blue team flags the syscall instruction.  
- Subsequent stages add anti‑debug, hardware sandbox detection, module stomping, sleep‑time encryption, and finally a full C2 agent, each prompting new defensive counters.

## Sample Burning – The Hidden Lesson
- Submitting a sample to VirusTotal “burns” it: the submission trains the 76+ AV vendors’ ML models.  
- Stage 03 achieved 0/76 detections initially, after which ESET created the Agent.ION detection based on the submitted sample.  
- The course emphasizes that testing itself alters the detection landscape, making clean verification impossible without contaminating the sample.