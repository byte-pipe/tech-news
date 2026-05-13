---
title: Checkmarx Jenkins plugin compromised in new supply chain attack - Techzine Global
url: https://www.techzine.eu/news/security/141212/checkmarx-jenkins-plugin-compromised-in-new-supply-chain-attack/
site_name: tldr
content_file: tldr-checkmarx-jenkins-plugin-compromised-in-new-supply
fetched_at: '2026-05-14T06:01:08.458194'
original_url: https://www.techzine.eu/news/security/141212/checkmarx-jenkins-plugin-compromised-in-new-supply-chain-attack/
date: '2026-05-14'
description: TeamPCP has infected the Checkmarx Jenkins AST plugin with malware. CVSS 9.4. Check your plugin version and rotate your secrets immediately.
tags:
- tldr
---

A tampered version of the Checkmarx Jenkins AST plugin has appeared in the Jenkins Marketplace. The attack has been assigned a CVE identifier (CVE-2026-33634) with a CVSS score of 9.4. Checkmarx has confirmed the incident and advises users to take immediate action.

The hacker group TeamPCP renamed the Checkmarx Jenkins AST plugin’s GitHub repository to “Checkmarx-Fully-Hacked-by-TeamPCP-and-Their-Customers-Should-Cancel-Now.” The repository description was changed to: “Checkmarx fails to rotate secrets again. with love â€“ TeamPCP.” The group then backdoored the plugin release itself. Jenkins instances thatinstalledversion 2026.5.09 are therefore running a compromised plugin.

The malware has a Dune theme. Repositories on the compromised cx-plugins-releases account have names like kralizec-navigator-709 and mentat-navigator-124, all with the description “A Mini Shai-Hulud has Appeared.”

This is not the first time TeamPCP has targeted Checkmarx. In March 2026, the group had already compromised checkmarx/ast-github-action and checkmarx/kics-github-action. During that same campaign, more than 66 npm packages were compromised, andat least 1,000 enterprise SaaS environmentswere potentially exposed. Trivy and LiteLLM were also targeted.Previous findings revealedhow these supply chain attacks target developer endpoints, with attackers specifically hunting for cloud credentials, npm publication tokens, and SSH keys.

## What should users do?

Checkmarx recommendsusingonlyversion 2.0.13-829.vc72453fa_1c16, published on December 17, 2025. Anyone who has installed version 2026.5.09 must rotate all secrets that were visible to the Jenkins runner: GitHub tokens, cloud credentials (AWS/GCP/Azure), Kubernetes configurations, Docker credentials, and SSH keys. In addition, SOCRadar recommends checking Jenkins build logs for outbound traffic to unknown domains and searching for Dune-related repository names in GitHub organizations.

Checkmarx is working on a new, clean version of the plugin and promises further updates.