---
title: I Found 39 Algolia Admin Keys Exposed Across Open Source Documentation Sites - Ben Zimmermann
url: https://benzimmermann.dev/blog/algolia-docsearch-admin-keys
date: 2026-03-13
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-15T06:02:50.611170
---

# I Found 39 Algolia Admin Keys Exposed Across Open Source Documentation Sites - Ben Zimmermann

# I Found 39 Algolia Admin Keys Exposed Across Open Source Documentation Sites - Ben Zimmermann

## Background
- In October I reported a full‑permission Algolia admin API key exposed on vuejs.org; Vue rotated the key and added me to their Security Hall of Fame.
- This made me wonder how many other DocSearch sites might have the same issue.

## How Algolia DocSearch works
- DocSearch is a free search service for open‑source documentation.
- Algolia crawls the site, builds an index, and provides a frontend API key that should be **search‑only**.
- Some projects mistakenly embed keys with full admin permissions.

## Methodology
- Started with Algolia’s public (now archived) `docsearch-configs` repository containing configs for >3,500 sites.
- Scraped ~15,000 documentation sites for embedded credentials using regex patterns for App IDs and 32‑character API keys.
- Complemented scraping with GitHub code search in documentation framework configs.
- Ran TruffleHog on 500+ documentation repos to catch keys that had been committed and later removed.

## Findings
- Discovered 39 admin keys; 35 were found via frontend scraping, 4 through git history.
- All 39 keys were active at the time of discovery.
- Affected projects include high‑profile open‑source software such as Home Assistant (85 k GitHub stars), KEDA (CNCF project), and vcluster (largest index with >100 k records).

## Capabilities of the exposed keys
- Permissions common to all keys: `search`, `addObject`, `deleteObject`, `deleteIndex`, `editSettings`, `listIndexes`, `browse`.
- Some keys also granted analytics, logs, and NLU access.
- With these keys an attacker can:
  - Add, modify, or delete any record in the index.
  - Delete the entire index.
  - Change index settings and ranking.
  - Browse and export all indexed content.
  - Potentially poison search results, redirect users to malicious sites, or completely disable search for the documentation site.

## Disclosure and response
- SUSE/Rancher acknowledged the report within two days and revoked the key.
- Home Assistant responded and began remediation, though the original key remained active.
- I emailed the full list of keys to Algolia; no response was received and all remaining keys remain active.

## Root cause and recommendation
- The problem is systemic: many sites run their own crawler and mistakenly use a write or admin key in the frontend configuration, despite Algolia’s documentation warning against it.
- Fix: verify that the key placed in the frontend config is a **search‑only** key.
- Given that 39 admin keys were found with relatively simple scripts, the true number of exposed keys is likely higher.
