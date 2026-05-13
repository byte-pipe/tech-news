---
title: Checkmarx Jenkins plugin compromised in new supply chain attack - Techzine Global
url: https://www.techzine.eu/news/security/141212/checkmarx-jenkins-plugin-compromised-in-new-supply-chain-attack/
date: 2026-05-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-14T06:02:20.713679
---

# Checkmarx Jenkins plugin compromised in new supply chain attack - Techzine Global

# Checkmarx Jenkins plugin compromised in new supply chain attack

## Overview
- A tampered version of the Checkmarx Jenkins AST plugin (version 2026.5.09) was found in the Jenkins Marketplace.  
- The incident is tracked as CVE‑2026‑33634 with a CVSS score of 9.4.  
- Checkmarx has confirmed the breach and urges immediate remediation.

## Attack details
- Hacker group **TeamPCP** renamed the plugin’s GitHub repository to a warning message and altered its description to criticize Checkmarx’s secret‑rotation practices.  
- The group back‑doored the plugin release itself, embedding malware with a **Dune** theme. Compromised repositories under the `cx-plugins-releases` account carry names such as `kralizec-navigator-709` and `mentat-navigator-124`, all described as “A Mini Shai‑Hulud has Appeared.”  
- This follows earlier supply‑chain attacks by TeamPCP in March 2026 that compromised `checkmarx/ast-github-action`, `checkmarx/kics-github-action`, over 66 npm packages, and affected roughly 1,000 enterprise SaaS environments.  
- Prior campaigns targeted developer endpoints to steal cloud credentials, npm publication tokens, and SSH keys, also hitting projects like Trivy and LiteLLM.

## Recommended user actions
- **Switch to a safe version:** install only `2.0.13-829.vc72453fa_1c16` (published Dec 17 2025).  
- **If version 2026.5.09 was used:**  
  - Rotate all secrets that could have been accessed by the Jenkins runner, including GitHub tokens, AWS/GCP/Azure credentials, Kubernetes configs, Docker credentials, and SSH keys.  
  - Review Jenkins build logs for outbound connections to unknown domains.  
  - Search GitHub organizations for Dune‑related repository names that may indicate further compromise.

## Next steps
- Checkmarx is preparing a clean replacement of the plugin and will issue further updates as they become available.