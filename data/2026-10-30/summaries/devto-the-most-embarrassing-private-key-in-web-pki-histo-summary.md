---
title: The Most Embarrassing Private Key in Web PKI History - DEV Community
url: https://dev.to/varshithvhegde/the-most-embarrassing-private-key-in-web-pki-history-f9b
date: 2026-10-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:32.647486
---

# The Most Embarrassing Private Key in Web PKI History - DEV Community

# Summary of “The Most Embarrassing Private Key in Web PKI History”

## Short version
- On 30 April 2025 eMudhra’s key‑generation ceremony produced weak EC private keys for eight intermediate CAs.  
- The keys, meant to be random 384‑bit numbers, were below 256; one example had the value **4**.  
- Public certificates contained the matching public keys, allowing anyone to recover the private key by brute‑forcing a few hundred possibilities in under a second.  
- The compromised intermediates were trusted for ~18 months before a researcher reported the issue on 17 October 2026.  
- Chrome and Firefox revoked the certificates quickly; eMudhra revoked the intermediates and offered migration support.  
- No public evidence shows the weak keys were exploited before disclosure.

## Role of an intermediate CA
- Root CA (trusted anchor) signs intermediate CAs; intermediates sign end‑entity certificates (websites, code‑signing, etc.).  
- Possession of an intermediate’s private key enables creation of many apparently legitimate certificates, making the intermediate key far more valuable than a single leaf certificate.

## Why a private key of “4” is catastrophic
- EC public key Q = d × G, where d is the private key and G is a fixed base point.  
- With a normal 384‑bit d, reversing Q is infeasible.  
- If d < 256, an attacker can compute 1 × G, 2 × G … 255 × G and compare each to Q, instantly revealing d.  
- The algorithm itself was not broken; the key‑generation process supplied a trivially small d, nullifying security.

## Publicly reported failure chain
1. Ceremony intended to generate RSA‑4096 and P‑384 key pairs for several intermediates.  
2. A deviation introduced a “wrap‑and‑unwrap” test for HSM key handling.  
3. The ceremony script inadvertently created a second set of weak EC keys alongside the proper ones.  
4. Both key sets received similar labels.  
5. Certificate‑signing requests mistakenly selected the weak key objects.  
6. Weak public keys were signed into intermediate certificates and cross‑signed for compatibility.  
7. Strong keys remained on the HSM but were never represented in the published certificates.  

The root‑cause analysis is still ongoing, but the visible chain shows a generation defect combined with a selection/verification defect.

## Missed warning that should have halted the incident
- In May 2025 CRL (Certificate Revocation List) signatures began failing verification because the signing key did not match the public key in the intermediate certificate.  
- Instead of investigating the mismatch, the CRL signer was reconfigured to use the weak key set, making signatures verify again.  
- This “quick fix” silenced the symptom without addressing why two key sets existed or why the published certificate did not correspond to the intended HSM key.

## RCA (Root‑Cause Analysis) shortcomings
- Shallow RCA: “Wrong key was configured → fix by pointing to the other key → closed.”  
- Deeper RCA should trace each step:
  - Why did CRL verification fail? → signer key mismatched certificate.  
  - Why mismatched? → certificate request used a different key pair than the HSM signing key.  
  - Why two key pairs? → ceremony produced extra key material during the wrap‑and‑unwrap test.  
  - Why was the wrong pair selected? → ambiguous labeling and selection controls.  
  - Why was the mismatch not caught before issuance? → lack of independent post‑ceremony reconciliation between certificates and HSM keys.

## Current status
- Chrome and Firefox have blocked the eight intermediates.  
- eMudhra has revoked the compromised certificates and is assisting customers in migrating to trusted keys.  
- Final root‑cause analysis remains pending; no known exploitation of the weak keys has been reported.