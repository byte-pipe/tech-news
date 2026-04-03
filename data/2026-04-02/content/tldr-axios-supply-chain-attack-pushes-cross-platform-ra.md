---
title: Axios Supply Chain Attack Pushes Cross-Platform RAT via Compromised npm Account
url: https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html
site_name: tldr
content_file: tldr-axios-supply-chain-attack-pushes-cross-platform-ra
fetched_at: '2026-04-02T11:20:51.818531'
original_url: https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html
author: The Hacker News
date: '2026-04-02'
description: Axios 1.14.1 and 0.30.4 injected malicious plain-crypto-js@4.2.1 after npm compromise on March 31, 2026, deploying cross-platform RAT malware.
tags:
- tldr
---

# Axios Supply Chain Attack Pushes Cross-Platform RAT via Compromised npm Account


Ravie Lakshmanan

Mar 31, 2026
Open Source / Supply Chain Attack

The popular HTTP client known asAxioshas suffered a supply chain attack after two newly published versions of the npm package introduced a malicious dependency that delivers a trojan capable of targeting Windows, macOS, and Linux systems.

Versions 1.14.1 and 0.30.4 of Axios have been found to inject "plain-crypto-js" version 4.2.1 as a fake dependency.

According to StepSecurity, the two versions werepublishedusing the compromised npm credentials of the primary Axios maintainer ("jasonsaayman"), allowing the attackers to bypass the project's GitHub Actions CI/CD pipeline.

"Its sole purpose is to execute a postinstall script that acts as a cross-platform remote access trojan (RAT) dropper, targeting macOS, Windows, and Linux," security researcher Ashish Kurmisaid. "The dropper contacts a live command and control server and delivers platform-specific second-stage payloads. After execution, the malware deletes itself and replaces its own package.json with a clean version to evade forensic detection."

Users who have Axios versions 1.14.1 or 0.30.4 installed are required to rotate their secrets and credentials with immediate effect, and downgrade to a safe version (1.14.0 or 0.30.3). The malicious versions, as well as "plain-crypto-js," are no longer available for download from npm.

With more than 83 million weekly downloads, Axios is one of the most widely used HTTP clients in the JavaScript ecosystem across frontend frameworks, backend services, and enterprise applications.

"This was not opportunistic," Kurmi added. "The malicious dependency was staged 18 hours in advance. Three separate payloads were pre-built for three operating systems. Both release branches were hit within 39 minutes. Every trace was designed to self-destruct."

The timeline of the attack is as follows -

* March 30, 2026, 05:57 UTC - A clean version of the package "plain-crypto-js@4.2.0" is published.
* March 30, 2026, 23:59 UTC - A new version ("plain-crypto-js@4.2.1") with the payload added is published.
* March 31, 2026, 00:21 UTC - A new version of Axios ("axios@1.14.1") that injects "plain-crypto-js@4.2.1" as a runtime dependency is published using the compromised "jasonsaayman" account.
* March 31, 2026, 01:00 UTC - A new version of Axios ("axios@0.30.4") that injects "plain-crypto-js@4.2.1" as a runtime dependency is published using the compromised "jasonsaayman" account.

According to StepSecurity, the threat actor behind the campaign is said to have compromised the npm account of "jasonsaayman" and changed its registered email address to a Proton Mail address under their control ("ifstap@proton.me"). The "plain-crypto-js" was published by an npm user named "nrwise" with the email address "nrwise@proton.me."

It's believed that the attacker obtained a long-lived classic npm access token for the account to take control and directly publish poisoned versions of Axios to the registry.

The embedded malware, for its part, is launched via anobfuscated Node.js dropper("setup.js") and is designed to branch into one of three attack paths based on the operating system -

* On macOS, it runs an AppleScript payload to fetch a trojan binary from an external server ("sfrclak.com:8000"), save it as "/Library/Caches/com.apple.act.mond," change its permissions to make it executable, and launch it in the background via /bin/zsh. The AppleScript file is deleted after execution to cover up the tracks.
* On Windows, it locates the PowerShell binary path, copies it to the "%PROGRAMDATA%\wt.exe" (disguising it as the Windows Terminal app), and writes a Visual Basic Script (VBScript) to the temp directory and executes it. The VBScript contacts the same server to fetch a PowerShell RAT script and execute it. The downloaded file is then deleted.
* On other platforms (e.g., Linux), the dropper runs a shell command via Node.js’s execSync to fetch a Python RAT script from the same server, save it to "/tmp/ld.py," and execute it in the background using the nohup command.

"Each platform sends a distinct POST body to the same C2 URL — packages.npm.org/product0 (macOS), packages.npm.org/product1 (Windows), packages.npm.org/product2 (Linux)," StepSecurity said. "This allows the C2 server to serve a platform-appropriate payload in response to a single endpoint."

The downloaded second-stage binary for macOS is a C++ RAT that fingerprints the system and beacons to a remote server every 60 seconds to retrieve commands for subsequent execution. It supports capabilities to run additional payloads, execute shell commands, enumerate the file system, and terminate the RAT.

SafeDep's analysis of the Linux RAT has revealed that it supports the same commands as its macOS counterpart. The absence of a persistence mechanism means that the malware does not survive across reboots. This indicates that the attack is either geared towards quick data exfiltration or leverages the RAT's ability to run binaries and shell commands to deploy persistence.

"The attack is notable for its restraint. No Axios source files were modified, making traditional diff-based code review less likely to catch it," SafeDepsaid. "The malicious behavior lives entirely in a transitive dependency, triggered automatically by npm's postinstall lifecycle."

The PowerShell RAT targeting Windows is no different in that it also facilitates the same functionality to execute arbitrary DLLs in memory, run PowerShell commands, list directories with file metadata, and gracefully kill itself. Unlike the macOS and Linux variants, the RAT creates "%PROGRAMDATA%\system.bat" with a download cradle that re-fetches the malware from the server on every login and adds a Registry Run key pointing to the batch script.

"On every compromised host, the RAT performed immediate system reconnaissance: enumerating user directories, filesystem drive roots, and running processes, and transmitted this data to the C2," Huntress researcher John Hammondsaid. "The RAT maintained a 60-second beacon loop, ready to accept further commands including arbitrary script execution and in-memory binary injection."

As Elastic Security Labspointed out, the attack makes use of three parallel implementations of the same RAT – PowerShell for Windows, compiled C++ for macOS, Python for Linux – that shares an identical C2 protocol, command set, message format, and operational behavior. "The consistency strongly indicates a single developer or tightly coordinated team working from a shared design document," the company said.

Once the main payload is launched, the Node.js malware also takes steps to perform three forensic cleanup steps by removing the postinstall script from the installed package directory, deleting the "package.json" the references the postinstall hook to launch the dropper, and renaming "package.md" to "package.json."

It's worth noting that the "package.md" file is included in "plain-crypto-js" and is a clean "package.json" manifest without the postinstall hook that triggers the entire attack. In switching the package manifests, the idea is to avoid raising any red flags during post-infection inspection of the package.

"Neither malicious version contains a single line of malicious code inside Axios itself," StepSecurity said. "Instead, both inject a fake dependency, plain-crypto-js@4.2.1, a package that is never imported anywhere in the Axios source, whose only purpose is to run a postinstall script that deploys a cross-platform remote access trojan (RAT)."

It's currently not known who is behind the supply chain compromise, but Elastic said the macOS Mach-O binary delivered by the "plain-crypto-js" postinstall hook exhibits significant overlap withWAVESHAPER, a C++ backdoor tracked by Google-owned Mandiant last month and attributed to a North Korean threat actor known as UNC1069.

Users are advised to perform the following actions toascertain compromise-

* Check for the malicious Axios versions.
* Check for RAT artifacts: "/Library/Caches/com.apple.act.mond" (macOS), "%PROGRAMDATA%\wt.exe" (Windows), and "/tmp/ld.py" (Linux).
* Downgrade to Axios versions 1.14.0 or 0.30.3.
* Remove "plain-crypto-js" from the "node_modules" directory.
* If RAT artifacts are detected, assume compromise and rotate all credentials on the system.
* Audit CI/CD pipelines for runs that installed the affected versions.
* Block egress traffic to the command-and-control domain ("sfrclak[.]com")

Socket, in its own analysis of the attack, said identified two additional packages distributing the same malware through vendored dependencies -

* @shadanai/openclaw(versions 2026.3.28-2, 2026.3.28-3, 2026.3.31-1, and 2026.3.31-2)
* @qqbrowser/openclaw-qbot(version 0.0.130)

In the case of "@shadanai/openclaw," the packagevendors the malicious "plain-crypto-js" payloaddirectly (e.g., @shadanai/openclaw/files/2026.3.31-1/dist/extensions/slack/node_modules/plain-crypto-js/setup.js). On the other hand, "@qqbrowser/openclaw-qbot@0.0.130," ships a tampered "axios@1.14.1" in its "node_modules/" folder with "plain-crypto-js" injected as a dependency.

"The real axios has only three dependencies (follow-redirects, form-data, proxy-from-env)," the supply chain security companysaid. "The addition of plain-crypto-js is unambiguous tampering. When npm processes this vendored axios, it installs plain-crypto-js and triggers the same malicious postinstall chain."

Found this article interesting? Follow us on 
Google News
, 
Twitter
 and 
LinkedIn
 to read more exclusive content we post.

SHARE










Tweet


Share


Share


Share

SHARE 


CI/CD Security
, 
cybersecurity
, 
JavaScript
, 
Malware
, 
NPM
, 
Open Source
, 
Remote Access Trojan
, 
Software Integrity
, 
supply chain attack

Trending News

Citrix NetScaler Under Active Recon for CVE-2026-3055 (CVSS 9.3) Memory Overread Bug

CISA Adds CVE-2025-53521 to KEV After Active F5 BIG-IP APM Exploitation

TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files

China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks

ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing Kits and 20 More Stories

Coruna iOS Kit Reuses 2023 Triangulation Exploit Code in Recent Mass Attacks

FCC Bans New Foreign-Made Routers Over Supply Chain and Cyber Risk Concerns

Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks

TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 via Trivy CI/CD Compromise

FBI Warns Russian Hackers Target Signal, WhatsApp in Mass Phishing Attacks

Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal CI/CD Secrets

Google Adds 24-Hour Wait for Unverified App Sideloading to Reduce Malware and Scams

Apple Warns Older iPhones Vulnerable to Coruna, DarkSword Exploit Kit Attacks

54 EDR Killers Use BYOVD to Exploit 35 Signed Vulnerable Drivers and Disable Security

New Perseus Android Banking Malware Monitors Notes Apps to Extract Sensitive Data

⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches Numbers and More

Popular Resources

Detect AI-Driven Threats Faster With Full Network Visibility

[Demo] Discover SaaS Risks and Monitor Every App in Your Environment

[Guide] Learn How to Govern AI Agents With Proven Market Guidance

SANS SEC401: Get Hands On Skills to Detect and Respond to Cyber Threats