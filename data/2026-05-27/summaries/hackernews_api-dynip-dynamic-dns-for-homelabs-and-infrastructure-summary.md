---
title: DynIP — Dynamic DNS for homelabs and infrastructure
url: https://dynip.dev/
date: 2026-05-26
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-27T13:41:13.423859
---

# DynIP — Dynamic DNS for homelabs and infrastructure

# DynIP — Dynamic DNS for homelabs and infrastructure

## Core value proposition
- Updates propagate in about 60 seconds, far faster than the typical 30‑minute cache of other DDNS providers.  
- Generous free tier with no hidden fees.  
- Built on RFC 2136 TSIG, so routers that support DNS UPDATE (FortiGate, MikroTik, OPNsense, OpenWRT, etc.) work out of the box.  
- Supports simultaneous A and AAAA record updates; IPv6‑only zones are also possible.  
- DNSSEC is enabled by default and can be turned on per zone.

## Technical features
- 60 s TTL, NOTIFY‑driven, multi‑region nameservers.  
- Native UDP/53 updates plus a REST API for HTTP‑based automation.  
- TSIG key management with automatic propagation handling.  
- Ready‑made configuration snippets for dozens of device types (Docker, cURL, PowerShell, Python, Arduino/ESP32, FortiGate CLI, Cisco IOS/ASA, MikroTik (HTTP API and RFC 2136), pfSense/OPNsense, Ubiquiti UniFi, OpenWrt, Synology DSM, Fritz!Box, etc.).  
- Quick‑start workflow: create a zone → generate a snippet → copy it into the router’s CLI or GUI.

## Plans and billing
- Free tier shows status (Active, Cancelled, Past Due) and limits on the number of zones.  
- When downgraded, excess zones become locked; the oldest zones remain active.  
- Pro+ tier adds unlimited zones, long‑lived API tokens, and other premium capabilities.  

## DNSSEC management
- One‑time enablement generates signing keys, publishes DS records in the parent zone, and signs all DNS records.  
- Required for automatic Let’s Encrypt certificate issuance.  

## Custom namespaces (bring‑your‑own‑domain)
- Register your own domain and delegate NS records to `ns1.dynip.dev` and `ns2.dynip.dev`.  
- After verification, you can create dynamic subdomains under your own namespace.  

## API and automation
- Session‑based quick test using a `curl` POST to `/register`.  
- Pro feature: persistent API tokens (read‑only or full access) for scripts, CI pipelines, MSP integrations.  
- Tokens are shown only once, can be revoked at any time, and do not expire on logout.  

## Quick sync and monitoring
- Detect the current external IP address and instantly update selected zones.  
- UI displays zone status, last sync time, SSL certificate actions, and DNSSEC toggle.