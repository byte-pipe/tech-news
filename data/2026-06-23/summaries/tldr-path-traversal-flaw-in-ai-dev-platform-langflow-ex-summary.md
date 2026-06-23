---
title: Path traversal flaw in AI dev platform Langflow exploited in attacks
url: https://www.bleepingcomputer.com/news/security/path-traversal-flaw-in-ai-dev-platform-langflow-exploited-in-attacks/
date: 2026-06-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:20:09.969910
---

# Path traversal flaw in AI dev platform Langflow exploited in attacks

# Path traversal flaw in AI dev platform Langflow exploited in attacks

## Overview
- CVE‑2026‑5027 is a high‑severity path traversal vulnerability in Langflow’s file‑upload endpoint.
- Attackers are actively exploiting the flaw to write arbitrary files on exposed servers.
- Langflow is a popular open‑source visual AI development platform with over 149 k GitHub stars.

## Vulnerability details
- The `POST /api/v2/files` endpoint does not sanitize the `filename` parameter from multipart form data.
- Path traversal sequences (`../`) allow writing files to any location on the filesystem.
- The issue was discovered by Tenable early in 2026 and publicly disclosed on March 27, 2026 after no response from the Langflow team.
- Fixes:
  - `langflow-base` package version 0.8.3 (reported by Snyk Security on March 30, 2026).
  - Langflow application patched in version 1.9.0.

## Exploitation activity
- VulnCheck honeypots have observed attackers dropping test files on vulnerable instances.
- Langflow’s default unauthenticated auto‑login lets attackers obtain a session token with a single request.
- Censys scans show roughly 7 000 publicly exposed Langflow instances (historical data, may not reflect current exposure).
- Exploitation follows earlier attacks on other Langflow CVEs (CVE‑2026‑0770, CVE‑2026‑21445, CVE‑2026‑33017) and ongoing activity on CVE‑2025‑3248 linked to the MuddyWater group.

## Mitigation recommendations
- Upgrade Langflow to the latest release, version 1.10.0, which includes the patch for CVE‑2026‑5027.
- Review and restrict unauthenticated auto‑login settings.
- Monitor for unexpected file writes and anomalous API activity.

## Related security notes
- Recent AI‑related vulnerabilities include:
  - Microsoft AutoGen Studio code‑execution flaw.
  - Max‑severity flaw in ChromaDB enabling server hijacking.
  - 18‑year‑old NGINX vulnerability allowing DoS and potential RCE.
  - Google report of AI‑generated zero‑day exploit for a web admin tool.
  - Critical LiteLLM pre‑auth SQL injection flaw.