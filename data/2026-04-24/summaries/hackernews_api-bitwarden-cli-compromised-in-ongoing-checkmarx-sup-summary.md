---
title: Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain ...
url: https://socket.dev/blog/bitwarden-cli-compromised
date: 2026-04-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:05:24.431685
---

# Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain ...

# Malicious Checkmarx Artifacts Found in Official KICS Docker Repository and Code Extensions

## Overview
- Docker and Socket identified malicious images of Checkmarx’s KICS tool and suspicious releases of related code extensions.  
- The findings are part of a larger supply‑chain compromise affecting Checkmarx products.

## Key Findings
- **Compromised Docker Images**: Official KICS Docker repository contained images that included malicious payloads.  
- **Suspicious Code Extensions**: Several code extension releases associated with KICS exhibited unexpected or harmful behavior.  
- **Supply‑Chain Scope**: The artifacts are linked to an ongoing broader attack targeting Checkmarx’s software supply chain.

## Impact
- Users pulling the compromised Docker images or installing the affected extensions risk exposure to malicious code.  
- Potential for credential theft, unauthorized access, or further propagation within downstream environments.

## Recommendations
- Stop using KICS Docker images and code extensions from the official repository until they are verified clean.  
- Verify image digests and signatures against trusted sources before deployment.  
- Monitor for any unusual activity in environments where KICS may have been used.  
- Follow updates from Docker, Socket, and Checkmarx for remediation steps and patched releases.