---
title: GTFOBins
url: https://gtfobins.org/
date: 2026-04-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-29T06:01:33.877781
---

# GTFOBins

# GTFOBins Summary

## Overview
- GTFOBins is a curated collection of Unix‑like executables that can be leveraged to bypass local security restrictions on misconfigured systems.  
- The repository documents legitimate functionalities of these binaries that attackers can “live off the land” to obtain shells, elevate privileges, transfer files, and perform other post‑exploitation actions.  
- It is maintained by Emilio Pinna, Andrea Cardaci, and numerous contributors; anyone can submit new entries or techniques.  
- For Windows binaries, a separate project called **LOLBAS** is recommended.  
- GTFOBins is **not** a list of vulnerabilities; the binaries themselves are not inherently exploitable.

## Key Features
- **Functions** covered include:
  - Shell access, command execution, reverse and bind shells  
  - File read/write, upload/download, library loading  
  - Privilege escalation, inheritance of privileges, and more
- **Execution contexts** supported:
  - Unprivileged user  
  - `sudo`  
  - Set‑UID (SUID) binaries  
  - Binaries with specific Linux capabilities
- Provides additional resources:
  - GitHub repository for source and contributions  
  - JSON API for programmatic access  
  - MITRE ATT&CK® Navigator integration for mapping techniques

## Usage
- Security professionals use GTFOBins to understand potential abuse paths for binaries present on a target system.  
- Penetration testers reference the list to craft post‑exploitation payloads when only limited tools are available.  
- defenders can audit systems for the presence of high‑risk binaries in sensitive contexts (e.g., SUID) and mitigate misuse.

## Contribution
- The project welcomes community submissions of new binaries, techniques, or improvements.  
- Contributors can submit pull requests via the GitHub repository, ensuring the list stays up‑to‑date with emerging Unix‑like tools.