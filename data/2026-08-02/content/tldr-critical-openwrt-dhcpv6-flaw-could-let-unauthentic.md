---
title: Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root
url: https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html
site_name: tldr
content_file: tldr-critical-openwrt-dhcpv6-flaw-could-let-unauthentic
fetched_at: '2026-08-02T19:29:02.321890'
original_url: https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html
author: The Hacker News
date: '2026-08-02'
description: OpenWrt 24.10.8 fixes CVE-2026-53921, a critical odhcpd stack overflow triggered by crafted DHCPv6 requests that could enable code execution.
tags:
- tldr
---

# Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root


Swati Khandelwal

Jul 28, 2026
Network Security / Vulnerability

OpenWrthas shipped version 24.10.8 to close a critical DHCPv6 stack overflow and a wider set of remotely triggerable flaws in network services enabled by default.

The critical issue, tracked asCVE-2026-53921and rated 9.8 on CVSS 3.1 in OpenWrt's GitHub advisory, lets an unauthenticated attacker able to reach the DHCPv6 server overwrite a stack buffer in odhcpd through a crafted DHCPv6 REQUEST.

odhcpd runs as root, and the advisory notes that embedded hardware commonly lacks stack canaries and address space layout randomization (ASLR), making code execution a realistic outcome on typical devices.

The advisory includes public Python proof-of-concept code for both documented overflow paths. Users on the 24.10 branch should install 24.10.8, while users on 25.12 should install 25.12.5; firmware images are available through the OpenWrt Firmware Selector.

As of July 28, the reviewed OpenWrt materials did not report exploitation in the wild. The flaw was also absent from CISA's Known Exploited Vulnerabilities (KEV) catalogversion 2026.07.27, although absence from KEV does not establish that exploitation has not occurred.

The release arrived alongside a separate AI-assisted audit byHacker Housethat identified command-injection, path-traversal and cross-site scripting (XSS) weaknesses in optional LuCI components. OpenWrt found a separate stored-XSS issue and missing cross-site request forgery (CSRF) protection while preparing the fixes.

These separate LuCI fixes were not part of OpenWrt 24.10.8 and remained under review on July 28.

## A Packet to the Default DHCP Server

Theadvisory associated with CVE-2026-53921documents two independent overflow sites in the DHCPv6 request-processing path. In both, crafted IA options leave insufficient space in a fixed 512-byte stack buffer before the code appends additional reply data without a sufficient bounds check.

The final trigger is an unauthenticated DHCPv6 REQUEST sent to UDP port 547. The first path's proof of concept creates five IA_NA bindings with an earlier SOLICIT; the second is triggered by a single crafted REQUEST.

The advisory lists odhcpd master at commit e432dd6 and all earlier versions containing dhcpv6_ia_handle_IAs() and build_ia() as affected. OpenWrt lists 24.10.8 and 25.12.5 as the supported releases carrying the relevant odhcpd security update.

The advisory associates its two documented sites with CVE-2026-53921, but the 24.10.8 release notes list the RECONF_ACCEPT overflow separately as a high-severity issue without a CVE. OpenWrt fixed the underlying writes by checking the remaining response-buffer capacity before appending the affected data.

OpenWrt's advisory groups both overflow sites under CVE-2026-53921, while the release notes list RECONF_ACCEPT separately without a CVE. The exact mapping remains unclear.

OpenWrt's release notes describe the flaw as reachable by a network-adjacent, unauthenticated attacker. The advisory's CVSS 3.1 vector usesAV:N(Network), not AV:A (Adjacent), and neither source explains the difference. An attacker still needs network access to the DHCPv6 service. Successful exploitation could give the attacker control of the router rather than merely crash the service.

The24.10.8 releasealso addresses other pre-authentication weaknesses in odhcpd, including an out-of-bounds write, use-after-free, memory disclosure, denial of service, stack over-read and neighbour-discovery proxy spoofing. Other default-service fixes cover three HTTP request-smuggling bugs in uhttpd and a DHCPv6 hostname-injection flaw, tracked as CVE-2026-62948, that can produce stored XSS when an administrator opens the LuCI leases page.

The same release includesCVE-2026-62947in cgi-io, which can expose arbitrary root-readable files through path traversal. That issue requires an authenticated session with the cgi-io download permission and an applicable wildcard file-read grant. It is not an anonymous file-read flaw.

OpenWrt 24.10 is under security maintenance, with end of life projected for September 2026. The project recommends migrating to the25.12 seriesbefore then. Packages installed separately from the firmware image may also require separate updates.

## The Patches Still in Review

Matthew Hickey, also known as Hacker Fantastic and CTO and Co-Founder of Hacker House,said publiclythat fixes had been released for remote-code-execution and path-traversal issues he reported to OpenWrt.

OpenWrt maintainer Hauke Mehrtens publishedLuCI pull request #8878on July 26, explicitly crediting Hickey and Hacker House. A check by The Hacker News on July 28 found the pull request still open and unmerged.

Image Source: Hacker House

Hacker House said it audited the main branches of both LuCI and uhttpd, using LuCI commit3b4f44d8e3d9d5de35127b42dd449babe2d19fe5from May 27 and uhttpd commit7b1bec45826bd78c8afc993435bdc0f1df2fe399from June 13.

It described three as pre-authentication paths to device compromise: directory traversal in luci-app-bmx7, stored XSS in luci-app-olsr, and command injection in luci-app-commands. The remaining four required LuCI credentials and could be used to execute commands on the device.

The firm said five findings were initially treated as post-authentication command-execution paths, but OpenWrt's testing showed that one luci-app-commands case could work without a session when an administrator had configured a command as both public and parameterised. The OLSR payload can also be injected without LuCI credentials, although it executes only when an administrator opens the neighbours page.

OpenWrt's pull request does not map one commit to each of Hacker House's seven submissions. Within pull request #8878, six commits correspond to Hacker House's report, two address additional security weaknesses OpenWrt found while preparing the fixes, and one corrects a nonsecurity filename issue. The pull request also identifies two findings from the same report set that had already been fixed in master, so the seven submissions do not map one-for-one to its nine commits.

The Hacker News is still awaiting OpenWrt's response on the CVE mapping, affected versions, and patch status.

The security changes in pull request #8878 include:

* luci-app-commands:A bare pipe character passed the application's argument allow-list and allowed commands to run as root. OpenWrt found that the path also worked without a session cookie or CSRF token when an administrator had configured a command with both public '1' and param '1'.
* luci-app-ddns:The ddns_dateformat setting could inject commands into a root-run operation, while service_name allowed path traversal. OpenWrt found a separate stored-XSS issue while preparing the fixes.
* luci-proto-openvpn:Attacker-controlled configuration values could reach shell commands through keytype, while key-directory parameters exposed path-traversal conditions.
* luci-app-olsr:A malicious mesh node could announce a crafted hostname that executes a script in the browser when an administrator views the OLSR neighbours page.

The unauthenticated luci-app-commands path has material preconditions. The optional application must be installed, and an administrator must have deliberately exposed a parameterised command as public. The other command-execution paths require authenticated LuCI access and the relevant configuration permissions. Successful exploitation runs commands as root. They are not blanket pre-authentication flaws affecting every OpenWrt router.

A separateddns-scripts pull requestaddresses the same unsafe ddns_dateformat setting outside LuCI. A delegated DDNS operator could place shell syntax in the value, with execution occurring when the updater next starts, including after reconfiguration or reboot. The same July 28 check found that the pull request was open and unmerged.

Two other findings from the same report set had already been fixed on LuCI's master branch: anunauthenticated file-read path traversal in luci-app-bmx7and command injection through ttyd_start in luci-app-dockerman. OpenWrt said both still required backports to release branches.

Hacker House said the BMX7 traversal was included in its July 8 disclosure and characterised it as a pre-authentication path to device compromise. OpenWrt'spublic advisorydescribes the impact more narrowly as unauthenticated access to files readable by the CGI process and credits nebusecurity as the reporter. Hacker House said it does not know whether the reports were duplicates or why the credit differs.

## AI in Discovery and Patch Review

Hacker House described the OpenWrt audit as a four-stage inference-fuzzing process that begins with a threat model. The method repeatedly examines the code to generate a broad pool of possible vulnerabilities.

Because that pool contains many false positives, the final stage uses a higher-precision model to filter the results. Researchers then manually confirm the remaining findings in the code and, where practical, on a running system before reporting them.

Hacker House said Qwen 3.6 35B Heretic is used for the recall-focused inference-fuzzing stage. For stage-four triage on open-source projects, it uses a frontier model such as Anthropic's Claude Opus 4.6. Qwen 3.5 115B can be substituted when an audit must run fully offline, allowing private source code to remain inside the client's environment.

After triage, researchers manually inspect the code and, where practical, confirm the issue at runtime using standard dynamic application security testing (DAST). Hacker House said it submits only findings it has confirmed as vulnerabilities, although exploit payloads may require adjustment during manual validation.

The firm said it gives open-source projects seven to 10 business days to acknowledge a report and then works with maintainers on their preferred remediation timeline. If no acknowledgement arrives, it may publish limited details to encourage the project to respond or address the finding.

OpenWrt used AI during parts of the remediation process as well. Several proposed commits carry an Assisted-by: Claude:claude-opus-5 trailer, and an automated review on the LuCI pull request says it was generated with Claude Code. Models therefore contributed to candidate discovery, triage, and patch review, while researchers and maintainers manually verified the findings and fixes.

For shipped fixes, users should install OpenWrt 24.10.8 or 25.12.5 and update separately installed packages. Administrators should also review delegated LuCI permissions, remove optional applications they do not use, and check whether any commands in luci-app-commands are both public and parameterised.

As of July 28, the two pull requests did not list CVEs, CVSS scores, complete affected release ranges, or fixed stable-package versions. Neither reported exploitation in the wild.

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

artificial intelligence
, 
Command Injection
, 
Cross-site Scripting
, 
Firmware Security
, 
network security
, 
OpenWrt
, 
Path Traversal
, 
remote code execution
, 
router security
, 
Vulnerability

⚡ Top Stories This Week

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit

Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs

Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC

AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code

Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs

Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents

OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark

Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data

Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs

Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs

Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers

Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files

ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories

Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit, Researchers Say

Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry

ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link

Certighost Exploit Lets Low-Privileged Active Directory Users Impersonate a Domain Controller

Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git

Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available

Malvertising Sends Malware in Pieces, Then Makes the Browser Build the Executable

⭐ Featured Resources

[Webinar] How Militaries Can Trust the Data Behind Autonomous Missions

Download the 5-Step Action Plan for AI-Speed Exploitation

Get the Checklist for Gaining Control of AI Use Across Your Organization

Get the 2026 CISO Benchmark Report Based on 600 Security Leaders