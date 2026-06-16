---
title: Hacking Google with A.I. for $500,000 · Brutecat
url: https://brutecat.com/articles/hacking-google-with-ai/
date: 2026-06-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-17T06:02:22.132077
---

# Hacking Google with A.I. for $500,000 · Brutecat

# Hacking Google with A.I. for $500,000 · Brutecat – Summary

## Background and Motivation
- After attending bugSWAT Mexico (Oct 2025) the author returned to Google research, intrigued by the possibility of fuzzing Google’s APIs at scale using AI.
- The approach hinges on Google’s **Discovery documents**, machine‑readable specifications (similar to Swagger) that list endpoints, parameters, and methods for both public and internal APIs.

## Collecting API Keys
- API keys are embedded in virtually every Google app; a key from one service often enables many other APIs within the same GCP project.
- Methodology:
  - Scraped ~60 000 Android APKs (all versions of Google apps) and extracted keys.
  - Built a Chrome extension using the Chrome Debugger API to intercept network traffic across >2.8 k Google web domains.
  - Decrypted Google iOS IPAs and analyzed binaries.
- Filtering to retain only Google‑owned projects:
  - Used an endpoint in the Cloud Marketplace API to retrieve the project’s `company` field.
  - Discarded keys whose `company` was not `google.com` (or known acquisitions such as `nest.com`, `fitbit.com`, `wing.com`).

## Enumerating Google API Domains
- Combined data from the Chrome extension, keyword‑based brute‑force generation, and Certificate Transparency logs.
- Verified live API services by sending a request to `GET /` and checking the `Server` header (e.g., `ESF`, `GSE`, `scaffolding`).

## Scanning for Discovery Documents
- Mass‑scanned the collected domains with valid API keys to locate open discovery documents.
- Bypassed the removal of the `/$discovery/rest` path (July 2025) where possible.
- Handled **visibility labels**:
  - Some projects expose hidden endpoints only when the `labels` query parameter is supplied (e.g., `labels=GOOGLE_INTERNAL`).
  - Required exhaustive testing of each known label per API key across all APIs, generating a large request volume.
- Result: retrieved discovery documents for **1,500+ APIs**, combined with previously archived docs.

## Authentication Challenges
- API keys alone grant access, but many endpoints also require authentication credentials tied to a specific GCP project.
- Bearer token authentication fails when the token’s project differs from the API key’s project.
- `X-Goog-User-Project` works only if the authenticated account holds the `roles/serviceusage.serviceUsageConsumer` role in that project.
- **First Party Authentication (FPA)** works with API keys:
  - Uses session cookies (`SAPISID`, `SAPISIDHASH`, etc.) and is sent to `*.clients6.google.com` hosts rather than `*.googleapis.com`.

## Preparing for AI‑Driven Fuzzing
- With a large corpus of discovery documents and a filtered set of Google‑owned API keys, the author is ready to employ AI (e.g., Claude) to automatically generate and execute fuzzing requests across the exposed API surface.