---
title: Path traversal flaw in AI dev platform Langflow exploited in attacks
url: https://www.bleepingcomputer.com/news/security/path-traversal-flaw-in-ai-dev-platform-langflow-exploited-in-attacks/
site_name: tldr
content_file: tldr-path-traversal-flaw-in-ai-dev-platform-langflow-ex
fetched_at: '2026-06-23T10:19:53.220319'
original_url: https://www.bleepingcomputer.com/news/security/path-traversal-flaw-in-ai-dev-platform-langflow-exploited-in-attacks/
date: '2026-06-23'
description: Attackers are actively exploiting CVE-2026-5027, a high-severity path traversal vulnerability in the AI development platform Langflow, to write arbitrary files on exposed servers.
tags:
- tldr
---

# Path traversal flaw in AI dev platform Langflow exploited in attacks

 By 

###### Bill Toulas

* June 10, 2026
* 05:23 PM
* 0

Attackers are actively exploiting CVE-2026-5027, a high-severity path traversal vulnerability in the AI development platform Langflow, to write arbitrary files on exposed servers.

Langflow is an open-source visual platform for building AI applications, AI agents, Retrieval-Augmented Generation (RAG) systems, and MCP-based workflows using a drag-and-drop interface instead of traditional coding.

AI development teams widely use the project, and it has accumulated more than149,000 stars and 9,200 forks on GitHub.

CVE-2026-5027 is a high-severity path traversal flaw in Langflow's file upload functionality that fails to properly sanitize user-supplied filenames.

"The 'POST /api/v2/files' endpoint does not sanitize the 'filename' parameter from the multipart form data, allowing an attacker to write files to arbitrary locations on the filesystem using path traversal sequences ('../'),"explains Tenable, which discovered the flaw at the start of the year.

Tenable publicly disclosed the issue on March 27, 2026, more than two months after initially reporting it to the Langflow team without receiving a response.

Although Tenable did not mention a fix in its advisory,Snyk Security reportedon March 30, 2026, that the issue was fixed in the langflow-base package version 0.8.3, while the Langflow application itself received a patch in version 1.9.0.

According to VulnCheck security researcher Caitlin Condon, their honeypots have now detected attackers exploiting the vulnerability to drop test files on vulnerable instances.

"Because Langflow enables unauthenticated auto-login by default, no credentials are required to reach the vulnerable endpoint, and a single unauthenticated request is sufficient to obtain a valid session token before proceeding with exploitation,"reads the researcher's post on LinkedIn.

Condon added that Censys scans identified roughly 7,000 publicly exposed Langflow instances. However, Censys data includes historical scan results from the previous 12 months and may not accurately reflect the number of systems currently exposed.

Exploitation of CVE-2026-5027 comes shortly after similar activity targeting other Langflow vulnerabilities earlier this year, including CVE-2026-0770, CVE-2026-21445, andCVE-2026-33017.

Last year, the U.S. Cybersecurity & Infrastructure Security Agency (CISA) also warned aboutactive exploitation of CVE-2025-3248, for which Condon says VulnCheck continues to observe activity, including activity linked to the Iranian threat group MuddyWater.

Langflow users are recommended to upgrade to the latest release,version 1.10.0, published earlier today.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

Microsoft fixes AutoGen Studio flaw that enabled code execution

Max-severity flaw in ChromaDB for AI apps allows server hijacking

18-year-old NGINX vulnerability allows DoS, potential RCE

Google: Hackers used AI to develop zero-day exploit for web admin tool

Hackers are exploiting a critical LiteLLM pre-auth SQLi flaw