---
title: 77 Open VSX extensions found harvesting developer info
url: https://www.bleepingcomputer.com/news/security/77-open-vsx-extensions-found-harvesting-developer-info/
site_name: tldr
content_file: tldr-77-open-vsx-extensions-found-harvesting-developer
fetched_at: '2026-08-07T11:44:08.492734'
original_url: https://www.bleepingcomputer.com/news/security/77-open-vsx-extensions-found-harvesting-developer-info/
date: '2026-08-07'
description: 77 extensions on the Open VSX marketplace impersonated legitimate developer tools while transmitting information about the systems and development environments where they were installed.
tags:
- tldr
---

# 77 Open VSX extensions found harvesting developer info

 By 

###### Lawrence Abrams

* August 4, 2026
* 02:50 PM
* 0

77 extensions on the Open VSX marketplace impersonated legitimate developer tools while transmitting information about the systems and development environments where they were installed.

The so-called "evil twin" campaign was discovered byManifold Security, which detected the extensions between July 26 and August 1, 2026. Researchers linked all 77 extensions to the same activity through a shared data-exfiltration domain, as well as code and network behavior.

While 58 extensions sent only a small amount of system information, the remaining 19 contained more extensive reconnaissance that exfiltrated developer, Git repository, and continuous integration (CI) metadata.

However, Manifold found that the extensions did not access source code, credentials, authentication tokens, SSH material, or browser data, and declined to speculate on the campaign's purpose.

## Evil Twin extensions linked through shared infrastructure

An "evil twin" extension is a counterfeit package that copies the identity of a legitimate extension to trick people into installing it.

In this campaign, the packages reused the names, namespaces, and descriptions of real VS Code Marketplace extensions but were published through unrelated accounts.

Most were assigned the low version number 0.0.1, while the legitimate extension's bundledextension.jsfile was replaced with code designed primarily to collect and transmit data.

Manifold says the extensions did not provide the functionality advertised in their listings and instead displayed a status bar indicator or message saying the extension was active before transmitting data to the attacker's server.

The packages impersonated extensions associated with a wide range of technologies and organizations, including AMD, Azure, Salesforce, Hyperledger, LEGO Education, IOTA, and a U.S. government agency namespace.

Example extension used in this campaign
Source: Manifold

All 77 extensions communicated with a server atmangorbit[.]com, which was registered on July 15, 2026, eleven days before the first packages appeared.

Manifold says that most samples contactedpulse.mangorbit[.]comorpulse2.mangorbit[.]com, while others used api.mangorbit[.]com or randomized subdomains under cb.mangorbit[.]com.

Each package included its own tracking identifier, allowing the operator to determine which counterfeit extension had been installed.

Fifty-eight of the extensions contained payloads that mainly exfiltrated the machine's hostname, with some variants also sending the workspace folder name and editor version.

The other 19 extensions collected significantly more information approximately four to five seconds after activation, including the operating system username and hostname, machine identifier, editor name and version, platform architecture, locale, timezone, and the name and full filesystem path of the workspace open in the editor.

The extensions also inspected some files in the workspace's .git directory to obtain Git remote hosts and organizations, the domain of the developer's configured email, the current branch, and the HEAD commit hash.

They enumerated up to 60 installed extensions and collected identifiers from CI and cloud development environments, including GitHub, GitLab, Azure DevOps, Buildkite, CircleCI, GitHub Codespaces, and Gitpod.​

Data collected by the malicious extension
Source: Manifold

What is unusual about this campaign is that the Open VSX listings disclosed that they collected what they called "anonymous usage metrics" and accurately said they did not access source code or credentials.

However, Manifold reports that the extensions sent more data than disclosed, including CI information that could expose private repository names or paths. Some also checked whether they had been installed manually or automatically through a project configuration.

Some variants were designed to keep trying to transmit the collected data for up to seven days. They also supported multiple collection endpoints and could query a DNS TXT record for a replacement URL if the hardcoded infrastructure stopped responding.

Manifold did not attribute the campaign and declined to speculate on the operator’s intent. However, the 19 reconnaissance extensions collected enough metadata to profile organizations, development environments, and private repositories.

The packages were removed from Open VSX by August 3, 2026, but the packages would still need to be manually removed from developers' systems and applications.

Manifold recommends checking systems and workspace configuration files for extension IDs listed in its report and blocking the mangorbit[.]com domain, which is used by all 77 packages in the campaign.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

Google Chrome may soon block New Tab hijacker extensions by default

CISA warns of actively exploited RCE flaws in Joomla extensions

Malicious Edge extension abuses Native Messaging as bridge to malware