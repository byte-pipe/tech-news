---
title: Hackers compromise Axios npm package to drop cross-platform malware
url: https://www.bleepingcomputer.com/news/security/hackers-compromise-axios-npm-package-to-drop-cross-platform-malware/
site_name: tldr
content_file: tldr-hackers-compromise-axios-npm-package-to-drop-cross
fetched_at: '2026-04-06T11:21:55.319849'
original_url: https://www.bleepingcomputer.com/news/security/hackers-compromise-axios-npm-package-to-drop-cross-platform-malware/
date: '2026-04-06'
description: Hackers hijacked the npm account of the Axios package, a JavaScript HTTP client with 100M+ weekly downloads, to deliver remote access trojans to Linux, Windows, and macOS systems.
tags:
- tldr
---

# Hackers compromise Axios npm package to drop cross-platform malware

 By 

###### Bill Toulas

* March 31, 2026
* 09:53 AM
* 0

Hackers hijacked the npm account of the Axios package, a JavaScript HTTP client with 100M+ weekly downloads, to deliver remote access trojans to Linux, Windows, and macOS systems.

According to reports from software supply chain security and application security companiesEndor Labs,Socket,Aikido, andStepSecurity, the threat actor published  on the Node Package Manager (npm) registry two malicious versions of the package

One malicious variant, axios@1.14.1, was published today at 00:21 UTC, while the second one, axios@0.30.4, emerged less than an hour later, at 01:00 UTC.

The packages were published without the automated OpenID Connect (OIDC) package origin and no matching GitHub commit appeared, which should trigger an alert immediately.

The researchers say that the threat actor gained access to the package after compromising the npm account of Jason Saayman, the main Axios maintainer.

TheOpenSourceMalwareresearch community says that the attacker also took control ofSaayman's GitHub accountand changed the associated email toifstap@proton.me, then removed a report about the compromise to which project collaborator DigitalBrainJS was trying to reply.

It is unclear how many downstream projects have been impacted by the supply-chain attack during the nearly three-hour exposure window.

Given that the Axios npm package has around400 million monthly downloads, the number may be significant.

Axios is an HTTP client for JavaScript applications that manages requests between clients, such as browsers or Node.js apps, and servers. Its purpose is to simplify communication via GET, POST, PUT/PATCH, and DELETE requests.

### Infection chain

After getting access to the package, the attacker injected a malicious dependency called plain-crypto-js@^4.2.1 into thepackage.jsonfile and did not alter the Axios code.

The dependency executes a post-install script during the package’s installation, launching an obfuscated dropper (setup.js) that contacts a command-and-control (C2) server to retrieve a next-stage payload based on the detected operating system.

Platform-specific attack chain
Source: Endor Labs

On Windows, the attack mixes VBScript and PowerShell to run a hidden Command Prompt window and execute a malicious script. The malware copies PowerShell to%PROGRAMDATA%\wt.exeto evade detection and achieve persistence across reboots, then downloads and executes a PowerShell script.

On macOS, the malware uses AppleScript to download a binary to/Library/Caches/com.apple.act.mond, mark it as executable, and run it in the background.

On Linux systems, the dropper fetches a Python-based payload stored at ‘/tmp/ld.py’ and executes it in the background with thenohup(no hang up) command.

In all cases, the malware infected the host with a remote access trojan (RAT), allowing attackers to execute commands and maintain persistence on infected systems.

The RAT can retrieve and execute a base64-encoded binary that it writes in a hidden temp file, execute shell commands via /bin/sh or AppleScript, and enumerate directories on the infected host.

After the infection is completed, the dropper deletes itself, removes the modifiedpackage.json, and replaces it with a clean copy to make forensic investigations more difficult.

Overview of the attack
Source: Socket

According to researchers at StepSecurity, the Axios supply-chain attack wasnot opportunistic, but a carefully planned activity, as "the malicious dependency was staged 18 hours in advance."

The fact that different payloads were delivered based on the detected operating system appears to support this theory, along with the self-destruct action for every artifact.

John Hultquist, chief analyst at Google Threat Intelligence Group (GTIG) told BleepingComputer that behind the Axios package compromise is a North Korean actor tracked internally as UNC1069 andknown to target"centralized exchanges (CEX), software developers at financial institutions, high-technology companies, and individuals at venture capital funds."

A securityresearcher saysthat the macWebT name of the macOS RAT is a direct reference to malware used by the BlueNoroff hackers in campaignsobserved by SentinelOnein 2023.

BlueNoroff is a North Korean threat group specialized in financially-motivated cyberattacks. The actor has targeted banks, financial institutions, and cryptocurrency exchanges.

Currently, there is no clear information about the threat actor behind the Axios supply-chain attack.

Recently, several high-profile supply-chain attacks were claimed by a group known as TeamPCP. The hackers targeted popular open-source software projects likeTelnyx,LiteLLM, andTrivy.

However, the compromise of the Axios package does not have the characteristics of a TeamPCP attack, and security researchers couldn’t link it to a specific threat actor.

Indicators of compromise (IoCs) are available from multiple organizations investigating the Axios supply-chain compromise and include the C2 domain used in the attack,sfrclak.comand other network details along with file system, packages data, and accounts observed in the attack:

* Endor Labs
* Socket
* Aikido
* StepSecurity
* OpenSourceMalware
* Elastic
* Snyk
* Huntress

Security teams are recommended to check environments for the presence ofaxios@1.14.1,axios@0.30.4, or any version ofplain-crypto-jsand treat the system as compromised if any of them is detected.

Axios should resolve to versions 1.14.0 or 0.30.3, or downgraded to an earlier version confirmed to be safe. Joe DeSimone of Elastic advises rotating credentials on systems running a compromised version of the Axios package, as the malware may have exfiltrated sensitive data such as keys and tokens.

Charles Carmakal, chief technology officer at Mandiant, says that the Axios npm supply-chain attack "is broad and extends to other popular packages that have dependencies on it."

The researcher warns that the amount of recent supply-chain incidents is overwhelming and that the secrets stolen this way over the past two weeks will lead to more compromises, crypto theft, ransomware, and extortion events.

"We are aware of hundreds of thousands of stolen credentials. A variety of actors with varied motivations are behind these attacks,"Carmakal says.

Update [March 31, 13:09 EST]:Article updated with information about indicators of compromise and reference to potential BlueNoroff connection.

Update [March 31, 14:22 EST]:Added attribution information and comments from Charles Carmakal and John Hultquist.

## Automated Pentesting Covers Only 1 of 6 Surfaces.

Automated pentesting proves the path exists. BAS proves whether your controls stop it. Most teams run one without the other.

This whitepaper maps six validation surfaces, shows where coverage ends, and provides practitioners with three diagnostic questions for any tool evaluation.

Get Your Copy Now

### Related Articles:

Trivy supply-chain attack spreads to Docker, GitHub repos

GlassWorm malware hits 400+ code repos on GitHub, npm, VSCode, OpenVSX

New PhantomRaven NPM attack wave steals dev data via 88 packages

Nigerian man gets eight years in prison for hacking tax firms

Axios npm hack used fake Teams error fix to hijack maintainer account