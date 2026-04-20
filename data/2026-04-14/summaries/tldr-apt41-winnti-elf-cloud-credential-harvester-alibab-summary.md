---
title: APT41 Winnti ELF Cloud Credential Harvester: Alibaba Typosquat Infrastructure & 6-Year Lineage - Breakglass Intelligence
url: https://intel.breakglass.tech/post/apt41-winnti-elf-cloud-credential-harvester-alibaba-typosquat
date: 2026-04-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-14T06:02:01.372872
---

# APT41 Winnti ELF Cloud Credential Harvester: Alibaba Typosquat Infrastructure & 6-Year Lineage - Breakglass Intelligence

# APT41 Winnti ELF Cloud Credential Harvester: Alibaba Typosquat Infrastructure & 6-Year Lineage

## Executive Summary
- Zero‑detection ELF backdoor linked to APT41 (Winnti) targets Linux cloud workloads on AWS, GCP, Azure, and Alibaba Cloud.
- Uses SMTP port 25 as a covert command‑and‑control channel and harvests cloud provider credentials and metadata.
- C2 is hosted on three Alibaba‑themed typosquat domains in Singapore, employing a selective handshake that hides the server from scanners.
- Initial lead by @TuringAlex; classification and family linkage provided by @Xlab_qax.

## New Contributions
- Detailed infrastructure mapping (Alibaba Cloud Singapore, NameSilo burst registration on 20‑21 Jan 2026).
- Six‑year lineage tracing from PWNLNX (2020) through intermediate variants to the current sample.
- Breakdown and analysis of the three typosquat domains impersonating Alibaba services.
- Technical description of the scanner‑evasion handshake used by the C2 server.

## Technical Highlights
- Implant: stripped, statically linked x86‑64 ELF, zero VirusTotal detections, compiled with GCC.
- Credential harvesting: queries metadata services of AWS, GCP, Azure, and Alibaba Cloud; reads local credential files; encrypts data with a hard‑coded AES‑256 key before exfiltration.
- C2 over SMTP: sends SMTP‑formatted messages on port 25; commands are returned via reply codes and extended status messages.
- Selective handshake: server requires a specific token in the EHLO string; scanners receive only a generic 220 banner and the connection is closed.
- Lateral movement: UDP broadcast to 255.255.255.255:6006 carries encoded beacons for peer‑to‑peer coordination without additional C2 traffic.

## Infrastructure Details
- C2 IP: 43.99.48.196 (Alibaba Cloud, Singapore, port 25, invisible to scanners).
- Typosquat domains:
  - ai.qianxing.co – impersonates Qianxin, registered 2026‑01‑20 via NameSilo.
  - ns1.a1iyun.top – mimics Aliyun, registered 2026‑01‑20 via NameSilo.
  - ai.aliyuncs.help – mimics Alibaba Cloud CDN, registered 2026‑01‑21 via NameSilo.
- All registrations used WHOIS privacy and occurred within a 24‑hour burst, matching known APT41 procurement patterns.

## Campaign Timeline (6‑Year Lineage)
- 2020: PWNLNX – first documented Winnti ELF implant, basic reverse shell, XOR encoding.
- 2021‑2022: Winnti 4.0 Linux – modular plugin architecture, kernel rootkit components.
- 2023: KEYPLUG – HTTPS C2, cloud‑aware.
- 2024: Intermediate variants – improved evasion, initial cloud metadata collection.
- 2025‑2026: Current sample – full cloud credential harvesting, SMTP C2, selective handshake, typosquat infrastructure.

## Indicators of Compromise
- File MD5: f1403192ad7a762c235d670e13b703c3.
- Network:
  - IP 43.99.48.196 (C2 server).
  - Domains ai.qianxing.co, ns1.a1iyun.top, ai.aliyuncs.help (C2/typosquat).
  - Ports 25/tcp (SMTP C2) and 6006/udp (lateral‑movement broadcast).
  - Broadcast address 255.255.255.255:6006 (peer discovery).

## MITRE ATT&CK Mapping
- Initial Access – T1190 (Exploit Public‑Facing Application).
- Execution – T1059.004 (Unix Shell).
- Persistence – T1547 (Boot or Logon Autostart Execution).
- Credential Access – T1552.005 (Cloud Instance Metadata API) and T1555 (Credentials from Password Stores).
- Discovery – T1580 (Cloud Infrastructure Discovery) and T1016 (System Network Configuration Discovery).
- Lateral Movement – T1021 (Remote Services).
- Command & Control – T1071.003 (Mail Protocols) and T1571 (Non‑Standard Port).
- Exfiltration – T1041 (Exfiltration Over C2 Channel).

## Confidence Assessment
- APT41 attribution: High (based on code lineage and infrastructure patterns).
- Cloud credential harvesting purpose: High (direct observation of metadata queries and file reads).
- SMTP C2 mechanism: High (network traffic analysis and binary strings).
- Selective handshake evasion: High (differential testing with scanner‑like vs. implant‑like connections).
- NameSilo burst registration pattern: Moderate (temporal correlation with known APT41 behavior).
- Six‑year lineage linkage: Moderate (code similarity and capability progression, some intermediate samples lack strong attribution).

## Detection Guidance
- Monitor outbound SMTP (port 25) from hosts that do not run mail services.
- Inspect SMTP payloads for non‑standard encoded data and unusual reply codes.
- Flag connections to the listed IP address and the three typosquat domains.
- Detect UDP broadcasts to 255.255.255.255:6006 as potential peer‑discovery traffic.
- Correlate accesses to cloud metadata endpoints and reads of local credential files on cloud instances.
