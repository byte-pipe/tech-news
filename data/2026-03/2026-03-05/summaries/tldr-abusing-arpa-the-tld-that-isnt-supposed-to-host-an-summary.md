---
title: Abusing .arpa: The TLD That Isn’t Supposed to Host Anything
url: https://www.infoblox.com/blog/threat-intelligence/abusing-arpa-the-tld-that-isnt-supposed-to-host-anything/
date: 2026-03-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:03:22.115094
---

# Abusing .arpa: The TLD That Isn’t Supposed to Host Anything

# Summary of “Abusing .arpa: The TLD That Isn’t Supposed to Host Anything”

## Overview
- Phishing campaigns are using a novel technique that leverages the `.arpa` top‑level domain (TLD) together with IPv6 reverse DNS strings to host malicious content.
- `.arpa` is intended only for reverse DNS (mapping IP addresses to domain names) and is not expected to resolve to web‑hosted IP addresses.
- Threat actors exploit a DNS management feature in some providers that allows creation of A records for `.arpa` subdomains, enabling them to serve phishing pages from domains that are unlikely to be blocked.

## Attack Mechanics
- **Email payload**: Images with hidden hyperlinks that point to long reverse DNS strings such as `d.d.e.0.6.3.0.0.0.7.4.0.1.0.0.2.ip6.arpa`.
- **Domain creation**:
  1. Acquire an IPv6 /64 address block (often via free IPv6 tunnels).
  2. Use the corresponding reverse DNS zone (`ip6.arpa`) and add A records for the reverse‑lookup names instead of the expected PTR records.
  3. Optionally prepend random subdomains to make each fully‑qualified domain name (FQDN) unique.
- **Resolution flow**:
  - The victim’s device performs a standard A query on the reverse DNS name.
  - Authoritative name servers (e.g., Cloudflare) return IP addresses that belong to the provider’s edge network, masking the actual malicious host.
- **Result**: The victim is redirected through a traffic distribution system, fingerprinted, and served fraudulent content while the domain appears benign to security controls.

## Provider Abuse
- Actors have abused reputable DNS providers such as Hurricane Electric and Cloudflare, which allow the creation of A records for `.arpa` zones.
- The researchers notified affected providers; vulnerability depends on whether the provider blocks ownership claims for `.arpa` domains.
- Not all providers are vulnerable; the critical check is the ability to claim and configure a reverse DNS zone.

## Additional Tactics Observed
- **Dangling CNAME hijacking**: Exploiting expired or abandoned domains’ CNAME records that point to high‑profile organizations (government agencies, universities, telecoms, media, retailers).
- **Domain shadowing**: Creating attacker‑controlled subdomains via compromised credentials.
- Over 100 instances of hijacked CNAMEs were found, some in use since 2020 and others appearing in more than 100 phishing emails in a single day.
- These techniques are used alongside the `.arpa` abuse to increase the likelihood of bypassing security filters.

## Implications and Recommendations
- Reverse DNS zones should be restricted to PTR records; providers must prevent creation of A (or other address) records for `.arpa` subdomains.
- Organizations should monitor for unusual reverse DNS lookups, especially long `ip6.arpa` strings, and implement detection for dangling CNAMEs and shadow subdomains.
- Collaboration with DNS providers to close the configuration gap is essential to stop this emerging phishing vector.
