---
title: DNSSEC Debugger - nic.de
url: https://dnssec-analyzer.verisignlabs.com/nic.de
date: 2026-05-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-06T11:31:39.374624
---

# DNSSEC Debugger - nic.de

# DNSSEC Debugger Report – nic.de  

## Overview  
- The report analyzes DNSSEC configuration for the domain **nic.de** as of **2026‑05‑06 01:29:55 UTC**.  
- It checks the chain‑of‑trust from the root through the .de zone down to the domain’s DNSKEY records.  

## DS Records (Delegation Signer)  
- Two DS records are present for the zone:  
  - **Key tag 20326**, algorithm SHA‑256, digest `e06d44b80b8f1d39a95c0b0d7c65d08458e880409bbc683457104237c7f8ec8d`.  
  - **Key tag 38696**, algorithm SHA‑256, digest `683d2d0acb8c9b712a1948b27f741219298d0a450d612c483af444a4c0fb2b16`.  
- Both DS records are reported as “now in the chain‑of‑trust”.  

## DNSKEY Records (Domain Keys)  
- Three DNSKEY records were retrieved for the apex (.) zone:  
  - **Key tag 38696** – SEP (Secure Entry Point) flag set, algorithm RSA/SHA‑256.  
  - **Key tag 20326** – SEP flag set, algorithm RSA/SHA‑256.  
  - **Key tag 54393** – non‑SEP key (algorithm RSA/SHA‑256).  
- An RRSIG covering the DNSKEY RRset is present, signed by key tag 20326.  

## Chain‑of‑Trust Verification  
- DS = 38696 (SHA‑256) successfully verifies DNSKEY = 38696 (SEP).  
- DS = 20326 (SHA‑256) successfully verifies DNSKEY = 20326 (SEP).  
- The RRSIG signed by key tag 20326 validates the DNSKEY RRset, confirming the integrity of the key set.  

## Queries to Root and TLD Servers  
| Query | Server | Response Summary |
|-------|--------|------------------|
| `./DNSKEY` | g.root‑servers.net (192.112.36.4) | Returned the three DNSKEY records and the RRSIG. |
| `nic.de A` | b.root‑servers.net (170.247.170.2) | No answer; authority section lists the .de NS set and the DS record for .de (key tag 26755). |
| `de DNSKEY` | e.root‑servers.net (192.203.230.10) | No answer; authority section repeats the .de NS set and its DS record (key tag 26755). |

## Authority Information for .de  
- NS records for the .de TLD: `a.nic.de.`, `f.nic.de.`, `l.de.net.`, `n.de.net.`, `s.de.net.`, `z.nic.de.` with both IPv4 and IPv6 addresses.  
- DS record for .de: **Key tag 26755**, SHA‑256 digest `f341357809a5954311ccb82ade114c6c1d724a75c0395137aa3978035425e78d`.  
- Corresponding RRSIG validates the DS record, signed by key tag 54393.  

## Conclusions  
- The DNSSEC chain‑of‑trust for **nic.de** is intact: root → .de (DS 26755) → nic.de (DS 20326 & 38696) → DNSKEYs (38696, 20326, 54393).  
- All signatures (RRSIGs) verify correctly, indicating no DNSSEC misconfiguration for the domain at the time of analysis.