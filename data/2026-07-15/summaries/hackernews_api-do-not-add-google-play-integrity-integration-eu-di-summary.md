---
title: Do not add Google Play Integrity integration · eu-digital-identity-wallet/av-doc-technical-specification · Discussion #19 · GitHub
url: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/discussions/19
date: 2026-07-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:49:34.876727
---

# Do not add Google Play Integrity integration · eu-digital-identity-wallet/av-doc-technical-specification · Discussion #19 · GitHub

# Do not add Google Play Integrity integration – Discussion Summary

## Main concerns raised by TheLastProject
- The README mentions “App and device verification based on Google Play Integrity API and Apple App Attestation.”
- The author urges abandoning this plan, arguing that reliance on American tech giants deepens EU dependency and gives the USA undue control over the internet.
- Emphasizes the political risk and the undesirability of such dependence.

## Supporting arguments from other contributors
- **Dependency on specific OS vendors**: Tying age verification to Google Play (or Apple) violates the principles of making the solution available to anyone and keeping it user‑controlled.
- **Interoperability principle**: Age‑verification must work across diverse operating systems; using proprietary integrity services breaks this design goal.
- **Digital sovereignty**: Any external third‑party service introduces additional security risks; a sovereign solution should avoid such dependencies.
- **Legal concerns**: Some participants claim that Play Integrity systems are illegal under EU competition rules.

## Alternative solutions proposed
- **Yivi (formerly IRMA)**: An open‑source identity app already used for age verification in the Netherlands, available on F‑Droid and without Google Play dependencies.
- **Standard Android hardware attestation**: Use the native Android attestation API instead of Google Mobile Services.
- **Web‑based approach**: Implement age verification via a web app using the Digital Credentials API or a challenge‑response flow similar to SSH/WebAuthn, eliminating the need for a dedicated mobile app.
- **Certificate security without proprietary tools**: Multiple methods exist to secure app certificates without relying on Google’s proprietary systems.

## Additional perspectives
- Some commenters question the threat model, suggesting that the risk of remote exploitation to steal proof of age is low.
- Others note that strict age verification may be less effective than parental controls or client‑side filters already present on smartphones.
- A few participants express frustration with the technical specification authors’ lack of understanding of the technologies they propose.

## Overall consensus
- The majority of participants oppose integrating Google Play Integrity, citing sovereignty, interoperability, legal, and security concerns.
- There is strong support for exploring open‑source, platform‑agnostic alternatives that align with EU design principles for digital identity and age verification.