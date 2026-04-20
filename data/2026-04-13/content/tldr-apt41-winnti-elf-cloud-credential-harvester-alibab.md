---
title: 'APT41 Winnti ELF Cloud Credential Harvester: Alibaba Typosquat Infrastructure & 6-Year Lineage - Breakglass Intelligence'
url: https://intel.breakglass.tech/post/apt41-winnti-elf-cloud-credential-harvester-alibaba-typosquat
site_name: tldr
content_file: tldr-apt41-winnti-elf-cloud-credential-harvester-alibab
fetched_at: '2026-04-13T20:05:35.745577'
original_url: https://intel.breakglass.tech/post/apt41-winnti-elf-cloud-credential-harvester-alibaba-typosquat
date: '2026-04-13'
published_date: '2026-04-10 12:10:34'
description: 'APT41 Winnti ELF Cloud Credential Harvester: Alibaba Typosquat Infrastructure & 6-Year Lineage Executive Summary A zero-detection ELF backdoor attributed to APT41 (Winnti) has been identified targeting Linux cloud workloads across AWS, GCP, Azure, and Alibaba Cloud environments. The implant uses'
tags:
- tldr
---

Back to reports

# APT41 Winnti ELF Cloud Credential Harvester: Alibaba Typosquat Infrastructure & 6-Year Lineage

## Executive Summary

A zero-detection ELF backdoor attributed to APT41 (Winnti) has been identified targeting Linux cloud workloads across AWS, GCP, Azure, and Alibaba Cloud environments. The implant uses SMTP port 25 as a covert command-and-control channel, harvests cloud provider credentials and metadata, and phones home to three Alibaba-themed typosquat domains hosted on Alibaba Cloud infrastructure in Singapore. A selective C2 handshake validation mechanism renders the server invisible to conventional scanning tools like Shodan and Censys.

Credit for the initial lead goes to@TuringAlex, whose work surfaced the sample.@Xlab_qaxprovided the original Winnti classification and family linkage.

## What This Report Adds to the Public Record

This report extends the existing body of work with:

* Infrastructure mapping— Alibaba Cloud Singapore C2 hosting, NameSilo registration burst pattern across a 24-hour window (Jan 20-21, 2026)
* Campaign timeline— A 6-year Winnti ELF lineage tracing from PWNLNX (2020) through intermediate variants to this sample
* Typosquat analysis— Breakdown of three domains impersonating Alibaba Cloud services (Qianxin, Aliyun)
* Selective handshake validation— Technical analysis of the C2 protocol's scanner-evasion mechanism

We acknowledge that prior researchers identified and classified this sample first. This report aims to complement that work with additional infrastructure and lineage context.

## Technical Analysis

### Implant Overview

The ELF binary is a stripped, statically linked x86-64 executable designed for persistence on Linux cloud instances. At the time of analysis, it carrieszero detections on VirusTotal.

Property
Value
File type
ELF 64-bit LSB executable, x86-64
MD5
f1403192ad7a762c235d670e13b703c3
VT detections
0/72
Compilation
GCC, stripped symbols
Target environments
AWS, GCP, Azure, Alibaba Cloud

### Cloud Credential Harvesting

The implant enumerates cloud provider metadata services and credential stores:

* AWS: Queries169.254.169.254/latest/meta-data/iam/security-credentials/for IAM role credentials, reads~/.aws/credentials
* GCP: Queries metadata server for service account tokens, reads application default credentials
* Azure: Queries IMDS endpoint for managed identity tokens, reads~/.azure/profiles
* Alibaba Cloud: Queries ECS metadata for RAM role credentials, reads Alibaba CLI config

Harvested credentials are encrypted with a hardcoded AES-256 key and staged locally before exfiltration.

### SMTP Port 25 Covert C2

Rather than using conventional HTTPS callbacks, the implant establishes C2 communication overSMTP port 25. This is a deliberate choice:

* Port 25 traffic is expected in cloud environments running mail services
* Many cloud security tools do not deeply inspect SMTP traffic for C2 patterns
* Egress filtering on port 25 is inconsistent across cloud providers

The implant constructs SMTP-formatted messages with encoded payloads in the message body, directed at the C2 server. Commands are returned in SMTP reply codes and extended status messages.

### Selective C2 Handshake Validation

The C2 server at43[.]99[.]48[.]196implements a selective handshake mechanism that rejects connections lacking a valid client-side token in the initial EHLO string. Connections from scanners, crawlers, or probes that do not present the correct token receive a standard SMTP banner and are immediately closed after a benign 220 response.

This means:

* Shodan/Censyssee a generic SMTP server and move on
* Automated threat feedsdo not flag the IP as malicious
* Only implants with the correct tokenreceive tasking

This is a meaningful evolution in Winnti operational security for Linux implants.

### Lateral Movement via UDP Broadcast

The implant periodically sends UDP broadcast packets to255.255.255.255:6006within the local network segment. These broadcasts contain an encoded beacon that other compromised hosts can receive, enabling peer-to-peer coordination and lateral tasking distribution without additional C2 traffic.

## Infrastructure Analysis

### C2 Server

Property
Value
IP
43[.]99[.]48[.]196
Hosting
Alibaba Cloud
Region
Singapore (ap-southeast-1)
Port
25/tcp (SMTP)
Scanner visibility
None (selective handshake)

### Typosquat Domains

Three domains impersonate Alibaba Cloud services and Chinese cybersecurity brand Qianxin:

Domain
Impersonates
Registrar
Registration Date
ai[.]qianxing[.]co
Qianxin (qianxin.com)
NameSilo
2026-01-20
ns1[.]a1iyun[.]top
Aliyun / Alibaba Cloud (aliyun.com)
NameSilo
2026-01-20
ai[.]aliyuncs[.]help
Alibaba Cloud CDN (aliyuncs.com)
NameSilo
2026-01-21

All three domains were registered throughNameSilowithin a24-hour burst window(January 20-21, 2026) with privacy protection enabled. This registration pattern is consistent with APT41 infrastructure procurement tradecraft — bulk registration through budget registrars with WHOIS privacy, followed by immediate deployment.

Thea1iyuntyposquat substitutes the numeral1for the letterl— a classic homoglyph technique. Thealiyuncs[.]helpdomain mimics the legitimate Alibaba Cloud CDN domainaliyuncs.comused in China's cloud ecosystem.

## Campaign Timeline: 6-Year Winnti ELF Lineage

APT41's investment in Linux/ELF tooling is not new. This sample fits within a documented lineage:

Year
Variant
Key Characteristics
2020
PWNLNX
First documented Winnti ELF implant, basic reverse shell, XOR encoding
2021-2022
Winnti 4.0 Linux
Modular plugin architecture, kernel rootkit components
2023
KEYPLUG (Linux)
Reported by Mandiant, HTTPS C2, cloud-aware
2024
Intermediate variants
Improved evasion, initial cloud metadata collection
2025-2026
This sample
Full cloud credential harvesting, SMTP C2, selective handshake, typosquat infrastructure

This trajectory shows a consistent 6-year investment in making Winnti's Linux tooling cloud-native — progressing from basic reverse shells to purpose-built cloud credential harvesters with scanner-resistant C2.

## Indicators of Compromise

### File Indicators

Type
Value
MD5
f1403192ad7a762c235d670e13b703c3

### Network Indicators

Type
Value
Context
IPv4
43[.]99[.]48[.]196
C2 server (Alibaba Cloud SG)
Domain
ai[.]qianxing[.]co
Typosquat / C2
Domain
ns1[.]a1iyun[.]top
Typosquat / C2
Domain
ai[.]aliyuncs[.]help
Typosquat / C2
Port
25/tcp
SMTP C2 channel
Port
6006/udp
Lateral movement broadcast
Broadcast
255.255.255.255:6006
Peer discovery

## MITRE ATT&CK Mapping

Tactic
Technique
ID
Initial Access
Exploit Public-Facing Application
T1190
Execution
Command and Scripting Interpreter: Unix Shell
T1059.004
Persistence
Boot or Logon Autostart Execution
T1547
Credential Access
Unsecured Credentials: Cloud Instance Metadata API
T1552.005
Credential Access
Credentials from Password Stores
T1555
Discovery
Cloud Infrastructure Discovery
T1580
Discovery
System Network Configuration Discovery
T1016
Lateral Movement
Remote Services
T1021
Command and Control
Application Layer Protocol: Mail Protocols
T1071.003
Command and Control
Non-Standard Port
T1571
Exfiltration
Exfiltration Over C2 Channel
T1041

## Confidence Assessment

Assessment
Confidence
Basis
APT41 attribution
HIGH
Winnti family classification by @Xlab_qax, code lineage from PWNLNX, infrastructure patterns
Cloud credential harvesting purpose
HIGH
Direct observation of metadata API queries and credential file reads
SMTP C2 mechanism
HIGH
Network traffic analysis and binary string extraction
Selective handshake as evasion
HIGH
Differential testing: scanner-like vs. implant-like connection behavior
NameSilo burst registration pattern
MODERATE
Temporal correlation; registrar choice consistent with prior APT41 campaigns
6-year lineage from PWNLNX
MODERATE
Code similarity analysis and capability progression; some intermediate samples lack strong attribution

## Detection Guidance

### Network-Based

* Monitor foroutbound SMTP (port 25) traffic from non-mail workloads— cloud instances not designated as mail servers should not initiate port 25 connections
* Alert onUDP broadcast traffic to port 6006— this is not a standard service port and broadcast usage in cloud VPCs is anomalous
* Block or monitor connections to43[.]99[.]48[.]196and the three typosquat domains

### Host-Based

* Audit forunexpected reads of cloud credential files(~/.aws/credentials,~/.azure/, GCP application default credentials, Alibaba CLI config)
* Monitorcloud instance metadata API callsfrom non-standard processes — legitimate SDKs and CLIs have known process names
* Hunt forstripped, statically linked ELF binariesin unexpected locations (/tmp,/var/tmp,/dev/shm)
* Check forcron entries or systemd servicesreferencing unknown ELF binaries

### Cloud-Native

* EnableCloudTrail / Cloud Audit Logsand alert on credential usage from unexpected source IPs
* ReviewIAM role assumption eventsfor anomalous patterns
* ImplementIMDSv2 (AWS)to require session tokens for metadata access, raising the bar for credential theft

## Prior Art & References

* @TuringAlex— Initial identification and lead on this sample
* @Xlab_qax— Winnti family classification and technical analysis
* Mandiant — KEYPLUG Linux variant reporting (2023)
* Chronicle / Google TAC — APT41 operational patterns and infrastructure procurement

Breakglass Intelligence | GHOST Offensive Intelligence

We don't wait for advisories. We map the infrastructure before it moves.

Share
