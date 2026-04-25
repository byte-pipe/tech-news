---
title: Bitwarden CLI npm package compromised to steal developer credentials
url: https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/
site_name: tldr
content_file: tldr-bitwarden-cli-npm-package-compromised-to-steal-dev
fetched_at: '2026-04-25T11:37:29.807544'
original_url: https://www.bleepingcomputer.com/news/security/bitwarden-cli-npm-package-compromised-to-steal-developer-credentials/
date: '2026-04-25'
description: The Bitwarden CLI was briefly compromised after attackers uploaded a malicious @bitwarden/cli package to npm containing a credential-stealing payload capable of spreading to other projects.
tags:
- tldr
---

# Bitwarden CLI npm package compromised to steal developer credentials

 By 

###### Lawrence Abrams

* April 23, 2026
* 03:21 PM
* 0

Updated with further information from Bitwarden.

The Bitwarden CLI was briefly compromised after attackers uploaded a malicious @bitwarden/cli package to npm containing a credential-stealing payload capable of spreading to other projects.

According to reports bySocket,JFrog, andOX Security, the malicious package was distributed as version 2026.4.0 and remained available between 5:57 PM and 7:30 PM ET on April 22, 2026, before being removed.

Bitwarden confirmed the incident, stating that the breach affected only its npm distribution channel for the CLI npm package and only those who downloaded the malicious version.

"The investigation found no evidence that end user vault data was accessed or at risk, or that production data or production systems were compromised. Once the issue was detected, compromised access was revoked, the malicious npm release was deprecated, and remediation steps were initiated immediately," Bitwarden shared in astatement.

"The issue affected the npm distribution mechanism for the CLI during that limited window, not the integrity of the legitimate Bitwarden CLI codebase or stored vault data."

Bitwarden says it revoked the compromised access and deprecated the affected CLI npm release.

## The Bitwarden supply chain attack

According to Socket, threat actors appear to have used a compromised GitHub Action in Bitwarden's CI/CD pipeline to inject malicious code into the CLI npm package.

According to JFrog, the package was modified so that the preinstall script and the CLI entry point use a custom loader namedbw_setup.js, which checks for the Bun runtime and, if it does not exist, downloads it.

The loader then uses the Bun runtime to launch an obfuscated JavaScript file namedbw1.js, which acts as credential-stealing malware.

Loader executing the malicious bw1.js file
Source: Jfrog

Once executed, the malware collects a wide range of secrets from infected systems, including npm tokens, GitHub authentication tokens, SSH keys, and cloud credentials for AWS, Azure, and Google Cloud.

The malware encrypts the collected data using AES-256-GCM and exfiltrates it by creating public GitHub repositories under the victim's account, where the encrypted data is stored.

OX Security says that these created repositories contain the string "Shai-Hulud: The Third Coming," a reference toprevious npm supply chain attacksthat used a similar method and text string when exfiltrating stolen data.

Data exfiltration repository with a "Shai-Hulud: The Third Coming" string
Source: OX Security

The malware also features self-propagation capabilities, with OX Security reporting that it can use stolen npm credentials to identify packages the victim can modify and inject them with malicious code.

Socket also observed that the payload targets CI/CD environments and attempts to harvest secrets that can be reused to expand the attack.

The attack comes afterCheckmarx disclosed a separate supply chain incidentyesterday that impacts its KICS Docker images, GitHub Actions, and developer extensions.

While it is not known exactly how attackers gained access, Bitwarden told BleepingComputer the incident was linked to the Checkmarx supply chain attack, with a compromised Checkmarx-related development tool enabling abuse of the npm delivery path for the CLI during a limited time window.

Socket told BleepingComputer that there are overlapping indicators between the Checkmarx breach and this attack.

"The connection is at the malware and infrastructure level. In the Bitwarden case, the malicious payload uses the sameaudit.checkmarx[.]cx/v1/telemetryendpoint that appeared in the Checkmarx incident. It also uses the same__decodeScrambledobfuscation routine with the seed0x3039, and shows the same general pattern of credential theft, GitHub-based exfiltration, and supply chain propagation behavior," Socket told BleepingComputer.

"That overlap goes beyond a superficial resemblance. The Bitwarden payload contains the same kind of embedded gzip+base64 components we saw in the earlier malware, including tooling for credential collection and downstream abuse."

Both campaigns have been linked to a threat actor known as TeamPCP, who previously targeted developer packages in the massiveTrivyandLiteLLMsupply chain attacks.

Developers who installed the affected version should treat their systems and credentials as compromised and rotate all exposed credentials, especially those used for CI/CD pipelines, cloud storage, and developer environments.

Update 4/23/26: Updated the story with information from Bitwarden confirming the incident was linked to the Checkmarx supply chain attack.

## 99% of What Mythos Found Is Still Unpatched.

AI chained four zero-days into one exploit that bypassed both renderer and OS sandboxes. A wave of new exploits is coming.

At the Autonomous Validation Summit (May 12 & 14), see how autonomous, context-rich validation finds what's exploitable, proves controls hold, and closes the remediation loop.

Claim Your Spot

### Related Articles:

Popular LiteLLM PyPI package backdoored to steal credentials, auth tokens

GlassWorm malware hits 400+ code repos on GitHub, npm, VSCode, OpenVSX

New Checkmarx supply-chain breach affects KICS analysis tool

New npm supply-chain attack self-spreads to steal auth tokens

The silent “Storm”: New infostealer hijacks sessions, decrypts server-side