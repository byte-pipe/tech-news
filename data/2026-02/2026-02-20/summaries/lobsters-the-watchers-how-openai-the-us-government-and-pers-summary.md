---
title: the watchers: how openai, the US government, and persona built an identity surveillance machine that files reports on you to the feds
url: https://vmfunc.re/blog/persona/
date: 2026-02-20
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-20T06:01:25.549438
---

# the watchers: how openai, the US government, and persona built an identity surveillance machine that files reports on you to the feds

# the watchers: how openai, the US government, and persona built an identity surveillance machine that files reports on you to the feds

## Summary
This article details the discovery of a hidden, publicly accessible database operated by Persona, a KYC (Know Your Customer) service, in collaboration with OpenAI and potentially the US government. The database, accessible at openai-watchlistdb.withpersona.com, contains a vast amount of code and data related to identity verification, including facial recognition, watchlist checks against 14 categories of adverse media, and the filing of Suspicious Activity Reports (SARs) with FinCEN. The authors of the article found this infrastructure through passive reconnaissance on Google Cloud and discovered that the entire codebase was unintentionally exposed on the public internet. They emphasize that no systems were accessed or data modified during their research, which was conducted using publicly available sources and falls under protected journalism and security research. The article highlights the concerning implications of commercial AI and government operations working together to potentially violate privacy.

## Key Points
- Persona, a KYC company, operates a hidden database (openai-watchlistdb.withpersona.com) containing code and data for identity verification.
- The database utilizes facial recognition to compare selfies against watchlist photos and screens individuals against 14 categories of adverse media.
- It also includes functionality for filing Suspicious Activity Reports (SARs) with FinCEN, utilizing intelligence code names.
- The entire codebase was unintentionally exposed on the public internet via a Google Cloud endpoint.
- The discovery was made through passive reconnaissance using Shodan, certificate transparency logs, DNS resolution, and publicly available web pages.
- The authors emphasize that no systems were accessed or data modified during their research, and the findings are based on publicly accessible information.
- The article details the infrastructure of Persona and its relationship with Cloudflare, highlighting how the watchlist database service is an exception to the standard wildcard DNS setup.
- The authors have reached out to Persona and OpenAI's legal teams, urging them to audit their compliance and answer specific questions outlined in a document (0x14).
- The authors have taken measures to ensure the dissemination of this information even if they face legal or other repercussions.

## Infrastructure Details
- The target IP address is 34.49.93.177, hosted on Google Cloud in Kansas City.
- The service utilizes an Envoy proxy with a "fault filter abort" response, indicating a locked-down backend service not intended for public access.
- Persona's standard infrastructure runs behind Cloudflare, with various subdomains pointing to Cloudflare's IP addresses.
- The openai-watchlistdb.withpersona.com service bypasses the wildcard DNS record that points to Cloudflare, making it publicly accessible.
- The SSL certificate for openai-watchlistdb.withpersona.com was valid from January 24, 2026, to April 24, 2026.
- The service is associated with SANs (Subject Alternative Names) including openai-watchlistdb.withpersona.com and openai-watchlistdb-testing.withpersona.com.
