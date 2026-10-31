---
title: A Supply Chain Attack Put Malicious Anthropic Claude Extensions on Thousands of Devices | WIRED
url: https://www.wired.com/story/trojan-malware-targets-thousands-of-anthropic-claude-developer-systems/
date: 2026-10-30
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:40.943146
---

# A Supply Chain Attack Put Malicious Anthropic Claude Extensions on Thousands of Devices | WIRED

# Summary of “A Supply Chain Attack Put Malicious Anthropic Claude Extensions on Thousands of Devices | WIRED”

## Incident overview
- Cursor, the AI‑driven development platform owned by SpaceX, listed a malicious version of Anthropic’s Claude Code extension for Windows, macOS, and Linux in its IDE marketplace.  
- The rogue extension was available for roughly 11 hours on a Thursday before the marketplace was temporarily shut down.  
- Up to **5,000 users** downloaded the tainted extension.

## Malware characteristics
- The extension contained a backdoor that could grant attackers remote access to infected devices, serving as a foothold for deeper network compromise.  
- A flaw in the malware’s design prevented it from fully establishing on the vast majority of targets, limiting overall impact.

## Detection and response
- Phorion co‑founder and CEO **Calum Hall** was the first researcher to spot the malicious extension on a customer’s Mac.  
- Cursor issued remediation steps on the same day for the affected users.  
- Anthropic staff (Felix Rieseberg and David Dworken) posted on X that Anthropic’s systems and employees were **not** compromised; the malicious copy was uploaded directly to Cursor’s marketplace, and the official Anthropic channels remain clean.

## Unresolved questions
- How the tampered extension entered Cursor’s marketplace is still unclear; initial speculation about a compromised Anthropic system has been dismissed.  
- Cursor did not respond to WIRED’s request for details on the upload process or whether a breach at Cursor occurred.

## Impact and implications
- Although the backdoor could have provided a dangerous foothold, the built‑in flaw limited widespread exploitation.  
- The incident underscores supply‑chain vulnerabilities in AI‑powered development tools and the need for stricter vetting of marketplace extensions.