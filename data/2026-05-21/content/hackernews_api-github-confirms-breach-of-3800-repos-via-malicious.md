---
title: GitHub confirms breach of 3,800 repos via malicious VSCode extension
url: https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/
site_name: hackernews_api
content_file: hackernews_api-github-confirms-breach-of-3800-repos-via-malicious
fetched_at: '2026-05-21T12:05:46.323188'
original_url: https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/
author: Timofeibu
date: '2026-05-20'
description: GitHub has confirmed that roughly 3,800 internal repositories were breached after one of its employees installed a malicious VS Code extension.
tags:
- hackernews
- trending
---

# GitHub confirms breach of 3,800 repos via malicious VSCode extension

 By 

###### Sergiu Gatlan

* May 20, 2026
* 04:14 AM
* 1

GitHub has confirmed that roughly 3,800 internal repositories were breached after one of its employees installed a malicious VS Code extension.

The company has since removed the unnamed trojanized extension from the VS Code marketplace and has secured the compromised device.

"Yesterday we detected and contained a compromise of an employee device involving a poisoned VS Code extension. We removed the malicious extension version, isolated the endpoint, and began incident response immediately,"the company said.

"Our current assessment is that the activity involved exfiltration of GitHub-internal repositories only. The attacker's current claims of ~3,800 repositories are directionally consistent with our investigation so far."

This comes after GitHub told BleepingComputer on Tuesday evening that it wasinvestigating claims of unauthorized accessto its internal repositories and added that it has no evidence that customer data stored outside the affected repos has been affected.

While GitHub has yet to attribute the breach, the TeamPCP hacker group claimed access to GitHub source code and "~4,000 repos of private code" on the Breached cybercrime forum on Tuesday, asking for at least $50,000 for the stolen data.

"As always this is not a ransom, We do not care about extorting Github, 1 buyer and we shred the data on our end, it looks like our retirement is soon so if no buyer is found we will leak it free," the cybercriminals said. "If you are interested. Send your offers to the communications below, we are not interested in under 50k, the best offer will get it."

​TeamPCP was previously linked to massive supply chain attacks targeting developer code platforms, includingGitHub,PyPI,NPM, andDocker, and, more recently, tothe "Mini Shai-Hulud" supply chain campaign(which also impacted two OpenAI employees).

TeamPCP GitHub breach claims (
Matthew Maynard
)

​VS Code extensions are plugins that can be installed from the VS Code Marketplace (the official store for add-ons for Microsoft's code editor) to add features or integrate tools into the editor.

This isn't the first time a trojanized VS Code extension has been spotted on the marketplace, as multiple other malicious extensions with millions of installs have been used to steal developer credentials and other sensitive data over the last several years.

For instance, last year, VSCode extensions with 9 million installswere pulled over security risks, and 10 more, posing as legitimate development tools,infected users with the XMRig cryptominer.

Later in the year, amalicious extension with basic ransomware capabilitiessnuck onto the VS Code marketplace after a threat actor named WhiteCobraflooded it with 24 crypto-stealing extensions.

More recently, in January, two malicious extensions advertised as AI-based coding assistants with 1.5 million installsexfiltrated data from compromised developer systems to servers in China.

GitHub's cloud-based platform is now used by over 4 million organizations (including 90% of the Fortune 100) and more than 180 million developers who contribute to over 420 million code repositories.

## The Validation Gap: Automated Pentesting Answers One Question. You Need Six.

Automated pentesting tools deliver real value, but they were built to answer one question: can an attacker move through the network? They were not built to test whether your controls block threats, your detection rules fire, or your cloud configs hold.

This guide covers the 6 surfaces you actually need to validate.

Download Now

### Related Articles:

GitHub links repo breach to TanStack npm supply-chain attack

GitHub investigates internal repositories breach claimed by TeamPCP

Grafana breach caused by missed token rotation after TanStack attack

7-Eleven confirms data breach claimed by the ShinyHunters gang

Grafana says stolen GitHub token let hackers steal codebase