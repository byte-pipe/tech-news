---
title: Cloud Threat Highlights: H1 2026 | Wiz Blog
url: https://www.wiz.io/blog/cloud-threat-highlights-h1-2026
date: 2026-08-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-10T15:31:12.424203
---

# Cloud Threat Highlights: H1 2026 | Wiz Blog

# Cloud Threat Highlights: H1 2026 | Wiz Blog

## Overview
- Wiz’s Research and CIRT teams observed a sharp rise in cloud‑security incidents in the first half of 2026.  
- Supply‑chain attacks reached unprecedented scale, while developer toolchains and AI infrastructure became prime targets.  
- Stolen credentials were reused months later, often fueling subsequent compromises.

## H1 2026 In Numbers
- Significant incidents highlighted to customers ↑ 60 % vs. H2 2025 – the highest single‑period count.  
- Compared with H1 2025, the count nearly doubled.  
- **Supply‑chain attacks:** grew from ~10 % (H2 2025) to 25 % of incidents; multiple ecosystems (npm, PyPI, Composer, VSCode extensions, Jenkins plugins, AUR) were hit.  
- **New vulnerability disclosures:** roughly doubled, driven by AI‑assisted research and weaponisation.  
- **AI‑infrastructure attacks:** ↑ ≈ 2× vs. H2 2025; unauthenticated RCE and credential leaks affected tools in ~⅓ of monitored cloud environments.  
- **Internet‑facing appliance exploits:** share fell from 30 % to 17 % of incidents, remaining relatively stable in absolute terms.

## Software Supply‑Chain Sprees

### TeamPCP
- Dominant supply‑chain campaign; compromised hundreds of organizations and GitHub (via a poisoned VSCode extension).  
- Core technique: poisoned npm package steals developer credentials, then pivots to cloud environments, chaining from one victim to the next.  
- April‑May variant added PyPI distribution, abused GitHub Actions CI misconfigurations, harvested OIDC tokens from runner memory.  
- May “AntV” compromise seized maintainer accounts, pushed malicious versions across hundreds of packages, and used token‑revocation‑triggered wipers with taunting commit messages.  
- Tokens with admin scope were used to strip branch protection and force‑push malicious commits.  
- At peak, ~4 000 stolen private repositories were listed for sale; follow‑on activity showed a long tail of credential reuse weeks later by other groups.  
- Wiz now detects such compromises within minutes; “cool‑down” policies (e.g., avoid packages < 24 h old) help reduce exposure.  

### Follow‑on Campaigns & IronWorm
- **Shai‑Hulud worm** (source released 12 May) spawned rapid variants; “Megalodon” back‑doored CI workflows at scale.  
- **Miasma** (June) compromised dozens of packages in the `@redhat-cloud-services` npm namespace; added cloud‑identity collectors for GCP/Azure and unique encrypted payloads.  
- **Hades** variant appeared on PyPI shortly after.  
- **IronWorm** (early June, second wave July) used a compiled Rust binary with a C‑compiled eBPF rootkit, concealed via Tor‑routed communications.  

### Credential Spillover
- TeamPCP‑stolen credentials were sold to other actors (e.g., Lapsus$) for > $50 k; Lapsus$ extorted a victim whose initial breach stemmed from a TeamPCP‑stolen key.

### North Korea – Midnight Neptune (UNC‑1069)
- Continued supply‑chain ops from 2025.  
- March 2026: trojanized the `axios` package; June 2026: compromised > 140 packages in the `@mastra` namespace via a single developer account.  
- The `axios` compromise affected more customers than any single TeamPCP operation; `@mastra` operation progressed faster than TeamPCP’s.  
- Unlike TeamPCP, initial backdoors lacked automated exfiltration; later `@mastra` added limited crypto and cloud‑secret exfiltration.

## JINX‑0163’s Emergence
- New cloud‑native extortion gang identified by Wiz’s AI‑enabled threat hunting in 2026.  
- Targets non‑human identities (service accounts, IAM roles) and can pivot from a single over‑privileged identity or exposed state file to harvest an organization’s full secret inventory.  
- Operates across AWS, Azure, GCP, Okta, and Snowflake at scale and speed.  
- Notable incident: compromised a cloud‑hosted AI development platform, gaining initial access through the described techniques.