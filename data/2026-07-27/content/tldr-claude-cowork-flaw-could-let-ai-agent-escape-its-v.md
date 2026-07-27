---
title: Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files
url: https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
site_name: tldr
content_file: tldr-claude-cowork-flaw-could-let-ai-agent-escape-its-v
fetched_at: '2026-07-27T12:06:44.339071'
original_url: https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
author: The Hacker News
date: '2026-07-27'
description: SharedRoot exploits CVE-2026-46331 in local Claude Cowork sessions to gain guest root and read or write files across the host Mac.
tags:
- tldr
---

# Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files


Ravie Lakshmanan

Jul 23, 2026
Vulnerability / Application Security

Cybersecurity researchers have uncovered a sandbox escape vulnerability in Anthropic'sClaude Coworkthat makes it possible to break out of the confines of a Linux virtual machine (VM) within which the agent runs to read or write files anywhere on the Mac.

Accomplish AI, which shared details of the vulnerability with The Hacker News ahead of publication, said about 500,000 macOS users running local Cowork sessions were affected prior to it being patched. It has been codenamedSharedRoot.

"We connected a folder to a fresh Claude Cowork session, sent one short message, and watched the agent escape the sandbox," Oren Yomtov, principal security researcher at Accomplish AI,said. "From inside the VM, it reached the host Mac and read and wrote files all over it, far outside the folder we'd connected, with no permission prompt anywhere."

With this level of access, the agent can access any data stored on the Mac via the user's account, including SSH keys, cloud credentials, and other valuable information.

Following responsible disclosure, Anthropic closed the report as informative without issuing a fix. That said, the latest version of Cowork defaults to cloud execution, which addresses the issue. But users who opt to run the agent locally are still exposed to the problem.

Claude Cowork's macOS desktop app runs as the user who is logged into the system. The actual agent-related work, on the other hand, happens in a Linux VM created via Apple'sVirtualization framework. Every session gets its own disposable unprivileged user, along with a Secure Computing Mode (seccomp) filter for application sandboxing. The folders connected by the user are shared into the VM by a root daemon called coworkd.

"One detail matters more than the rest: the host filesystem gets shared into that VM read-write," Yomtov explained. "The entire host '/,' mounted so that only guest-root inside the VM can see it, at /mnt/.virtiofs-root."

Because the entire host file system is mounted into the agent's VM with read-write privileges, any path to guest-root can grant the agent access to the underlying host, effectively escaping the sandbox.

This involves loading the Linux kernel's "act_pedit" Traffic Control (tc) packet editing subsystem into an unprivileged user namespace and exploitingCVE-2026-46331in the guest kernel, a recently disclosed flaw called pedit COW, to obtain guest-root. From there, the agent can access the whole host ("/") with elevated privileges, allowing it to read or write files from and to the Mac's file system as the logged-in desktop user.

Or Hiltch, co-founder and CTO of Accomplish AI, told The Hacker News that creating user and network namespaces gives the sessionCAP_NET_ADMINwithin its private network namespace, allowing it to perform various network-related operations.

"That capability provides access to the vulnerable tc/act_pedit kernel path used by pedit COW," Hiltch added. "The namespaces are not the exploit; they make its normally privileged prerequisite available to an ordinary user."

The development assumes significance in the face ofrevelationsthat OpenAI's models managed to break out of its sandboxed environment during a security test that resulted in the breach of Hugging Face's production infrastructure in their quest to cheat the ExploitGym benchmark they were being graded on.

"act_pedit is one bug in a category," Yomtov said. "The Linux net/sched subsystem throws off this exact shape of privilege escalation on a regular cadence: an autoloadable module, a config path an unprivileged user can reach, a memory bug at the end of it. Patch this one and you've fixed this one. The chain re-arms on the next one, with everything above the kernel untouched."

"And the next one is always coming. At any given moment there's likely a privilege-escalation bug it's still exposed to, sometimes fixed upstream but not yet in your image, sometimes not yet fixed anywhere, with a working exploit out within hours. This isn't a patch-faster problem. You're structurally one bug behind, all the time."

To mitigate the threat, it's essential todisable unprivileged user namespaces, avoid making the seccomp filter overly permissive, stop autoloading of modules, and restrict sharing of the whole host into the VM.

"Scope it to the folders that were actually connected instead of all of /, or at least mount it read-only, and run coworkd with ProtectSystem=strict in its own mount namespace so it isn't re-execing binaries a session user can poison," Accomplish said. "Then even a full guest-root has nothing to land on, the last two steps of the chain have nowhere to go."

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

AI Security
, 
Application Security
, 
Data Exposure
, 
endpoint security
, 
linux
, 
MacOS
, 
privilege escalation
, 
Sandbox Escape
, 
Virtualization
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

Identity Fraud Is Changing Fast. See the Attacks Businesses Face in 2026

What 25 Million Alerts Reveal About the Threats SOCs Ignore

How to Find and Control Every Script Running Through Your Marketing Stack

Modern SASE Guide: Close the Gaps Traditional Network Security Cannot See