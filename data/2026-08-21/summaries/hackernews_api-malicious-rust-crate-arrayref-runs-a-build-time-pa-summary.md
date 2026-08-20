---
title: Malicious Rust Crate arrayref Runs a Build-Time Payload - Real-time Open Source Software Supply Chain Security
url: https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/
date: 2026-08-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-21T06:52:16.391870
---

# Malicious Rust Crate arrayref Runs a Build-Time Payload - Real-time Open Source Software Supply Chain Security

# Malicious Rust Crate arrayref Runs a Build‑Time Payload

## Summary
- On 20 August 2026 a malicious release of the popular Rust crate **arrayref** (version 0.3.10) appeared on crates.io.  
- The crate added a dependency on a typosquatted crate **proc‑macro1**; its build script downloads and executes a remote binary during compilation.  
- Because the payload runs at build time, merely compiling a project that depends on the compromised version triggers the attack.  
- crates.io removed the malicious versions after discovery.

## Packages involved
| Crate | Version(s) | Publisher | Status |
|------|------------|-----------|--------|
| arrayref | 0.3.10 | droundy (compromised) | Malicious, removed |
| internment | 0.8.7 | droundy (compromised) | Malicious, removed |
| append‑only‑vec | 0.1.9 | droundy (compromised) | Malicious, removed |
| proc‑macro1 | all | dtolney (impersonation) | Malicious typosquat, removed |
| proc‑macro‑en | all | – | Malicious dependency, removed |
| aovine | all | – | Malicious dependency, removed |
| arone | all | – | Malicious dependency, removed |
| aronenao | all | – | Malicious dependency, removed |
| tinymember | all | – | Malicious dependency, removed |

- The genuine crates **arrayref** and **append‑only‑vec** are maintained by the compromised account *droundy*; their GitHub repositories are now 404.  
- *dtolney* impersonates David Tolnay; the forged metadata lists an email and repository that do not exist.

## What the build script does
- The malicious code resides in `proc-macro1-1.0.107/build.rs`.  
- It stores the payload host and C2 address as Base64 fragments, reassembles them at build time, and fetches an architecture‑specific binary over TLS with certificate validation disabled.  
- On Unix the binary is written to `/tmp/rust-setup` and executed detached.  
- On Windows a PowerShell script and a VBScript launcher are written to `%TEMP%` and started hidden; the child process is detached so Cargo does not wait for it.

## How it spread
- The attacker yanked earlier releases of **arrayref** (0.3.5–0.3.9). Cargo then warns developers to update, nudging them toward the only non‑yanked version, the malicious 0.3.10.  
- **arrayref** is a deep transitive dependency in many Rust GUI ecosystems (e.g., tiny‑skia, sctk‑adwaita, winit, egui, eframe, iced).  
- At the time of writing the crate had ~245 million total downloads; ~152 million correspond to the clean 0.3.9 release, indicating a large potential exposure.

## Indicators of compromise
- **Network**: `23.254.165.112:9089` (payload host, HTTPS) and `23.254.165.112:443` (C2 address).  
- **Unix file**: `/tmp/rust-setup` (downloaded executable).  
- **Windows files**: `%TEMP%\rust-setup.ps1` (PowerShell script) and `%TEMP%\rust-setup-launch.vbs` (VBScript launcher).  
- **Second‑stage binaries**: `rust-crate_0.1.0`, `_0.2.0`, `_0.3.0`, `_0.4.0` (chosen by OS/architecture).  

### SHA‑256 of removed artifacts
| Artifact | SHA‑256 |
|----------|---------|
| arrayref 0.3.10 | 25ad700976873c76af785cb99b33c48db7df8b81f21d1e9e06b3676b9a9373ae |
| proc‑macro1 1.0.107 | 61198155da51b838772eecf5bfaac6cbc4dcc388dccc56658fc28a8e831b34d4 |
| proc‑macro1 1.0.106 | b5c1b5b0763a8809a644a8f92224653f0aca623a98eecc714d27f74b80fbe436 |

## Technical analysis

### Injection point in **arrayref**
- Up to version 0.3.9 the crate had no build script or runtime dependencies.  
- Version 0.3.10 adds a single manifest entry:

```
[dependencies]
proc-macro1 = "1.0.107"
```

- Cargo builds every declared non‑optional dependency, so the malicious `proc-macro1` is fetched and built even though the `arrayref` source never references it.

### **proc‑macro1** is a renamed copy of **proc‑macro2**
- The source code is essentially `proc-macro2` with a mechanical rename (`proc-macro2 → proc-macro1`).  
- Documentation links, issue references, and the `html_root_url` still point to the original project, making the crate appear legitimate.  
- The forged `Cargo.toml` lists David Tolnay as author and a non‑existent repository, while adding unusual build‑time dependencies (`base64`, `rustls`, `ureq`) that enable the payload download.

### Build‑script payload
- The script decodes Base64 fragments to obtain the host `https://23.254.165.112:9089/` and C2 address `23.254.165.112:443`.  
- It uses `ureq` for HTTP, `rustls` for TLS, and `base64` for decoding.  
- After downloading the binary, it executes it in a detached manner, leaving no trace in the Cargo build process.