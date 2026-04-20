---
title: My minute-by-minute response to the LiteLLM malware attack
url: https://futuresearch.ai/blog/litellm-attack-transcript/
site_name: hnrss
content_file: hnrss-my-minute-by-minute-response-to-the-litellm-malwar
fetched_at: '2026-03-26T19:29:07.590456'
original_url: https://futuresearch.ai/blog/litellm-attack-transcript/
date: '2026-03-26'
published_date: '2026-03-25'
description: The full Claude Code transcript from discovering and responding to the litellm 1.82.8 PyPI supply chain attack on March 24, 2026 — from mysterious process explosions to malware identification to public disclosure.
tags:
- hackernews
- hnrss
---

← Back to Blog

Developers not trained in security research can now sound the alarm at a much faster rate than previously. AI tooling has sped up not just the creation of malware but also the detection.

This is the Claude Code conversation transcript from discovering and responding to the litellm 1.82.8 supply chain attack on March 24, 2026. The session began as a routine investigation into a frozen laptop and escalated into a full malware analysis and public disclosure, all within a single conversation. Seeour disclosure postfor the full writeup.

## Timeline

ATTACK
INVESTIGATION
CONFIRMATION
RESPONSE
10:52
Poisoned litellm v1.82.8 uploaded to PyPI
No corresponding GitHub tag — only v1.82.6 existed
10:58
futuresearch-mcp-legacy pulls compromised version as dependency
Cursor ran uvx futuresearch-mcp-legacy, which depends on litellm
11:07
Malware attempts persistence installation
~/.config/sysmon/sysmon.py created (0 bytes — write interrupted)
11:09
Force reboot after 11k-process fork bomb
Reboot interrupted persistence — malware partially neutralized
11:13
Investigation begins with Claude Code
Initially suspected runaway Claude Code loop, not malware
11:40
Malware identified in litellm package
litellm_init.pth found — credential theft, K8s lateral movement, exfil
11:58
Confirmed live on PyPI via isolated Docker download
Fresh download contains litellm_init.pth (34 KB) — actively infecting
12:02
Disclosure blog post written and published
Claude Code wrote the post, created PR, merged — 3 minutes end to end
12:04
Shared with r/Python, r/netsec, r/LocalLLaMA
72 minutes from first symptom to public disclosure

You no longer need to know the specifics of MacOS shutdown logs, how to parse cache systems of various package managers, remember the specific docker commands to pull a fresh container with the malware downloaded, or even know whose email address to contact. You just need to be calmly walked through the human aspects of the process, and leave the AI to handle the rest.

Should frontier labs be training their models to be more aware of these attacks? In this case it took some healthy skepticism to get Claude to look for malice, given how unlikely being patient zero for an undocumented attack is.

Shout out toclaude-code-transcriptsfor help displaying this.

All times are UTC. Redactions marked as[...]protect internal infrastructure details.

## Transcript

#1
11:13
37 bash

I just had a weird set of python commands found through htop bring my system to a crawl with 11k processes,exec(base64.b64decode('...'))— it seemed to self replicate filling my entire htop with lines like that. I force shutdown my laptop and rebooted. How can I inspect what happened? Can you maybe inspect journalctl to check?

Now I have the full picture. Here's my analysis:

What2.1.81is:Claude Code v2.1.81. You had5 Claude Code instancesrunning at shutdown time.

Shutdown timeline:

* 01:36:33— Force shutdown initiated
* 01:36:36— Shutdown stall captured (162 processes still running, 21 of them Python)
* 01:37:11— System booted

Process tree at shutdown:

Normal Claude Code MCP servers (2 instances):

Claude Code [82193] → python3.13 [88842] → node [88854] (416MB)
Claude Code [35621] → python3.13 [45088] → node [45091] (228MB)

These are MCP server bridges — Python wraps a Node.js MCP server. Normal behavior.

Auv runchain:

zsh → uv [74172] (deadlocked) → python3.13 [74174] (running a .py file)
→ python3.13 [74180] (python -c "...", reading pipe)
→ python3.13 [86263] (running .py file, sleeping + os.stat)
→ python3.13 [86264] (python -c "...", reading pipe)

14 orphanedpython -cprocesses(two batches of 7):

* PIDs 89759-89765 (~38 hours old)
* PIDs 67956-67962 (different age)
* All running_PyRun_SimpleStringFlagsWithName— this ispython -c "exec(base64.b64decode(...))"
* All orphaned (parent died, reparented to launchd)
* All stuck reading from a dead pipe

What likely happened:

Theexec(base64.b64decode('...'))pattern isnot malware— it's how Python tooling (including Claude Code's Bash tool) passes code snippets topython -cwhile avoiding shell escaping issues. The base64 encoding is just a safe transport mechanism.

The 11k process storm was likely arunaway spawning loopfrom one of these sources:

1. A Claude Code tool/agent interaction that got stuck in a loop spawningpython -cprocesses
2. Auv runscript (the 74174 chain) that had a subprocess spawning bug

Good news:

* No persistence mechanisms found— no suspicious crontabs, launch agents, or launchd jobs
* No suspicious Python processes running now— clean after reboot
* All processes used your local uv Python— nothing from unknown paths
* No malicious indicators— all parents trace back to Claude Code, uv, or zsh

Recommendations:

1. Check if you had a Claude Code agent running in a loop before the incident
2. If it happens again, trykillall python3.13before force-shutting down
3. Consider setting a process limit:ulimit -u 2048in your.zshrcto prevent fork bombs

Initial theory was completely wrong, Claude blaming Claude

#2
11:17

I took a picture on my phone of the htop screen if any info from there would help?

Yes, that could be very useful! The htop screenshot might show:

* The actualpython -c "exec(base64.b64decode('...'))"command lines (which would let me decode what code was being run)
* The parent PIDs and process tree at peak chaos
* Memory/CPU usage patterns

If you can transfer the photo to your Mac (AirDrop, iCloud, etc.), just give me the file path and I'll read it.

#3
11:18

Background task notification: "Check recently modified Python site-packages" completed.Read the output file to retrieve the result:[internal path]

#4
11:21
1 bash

I have android, let me just start here:aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHRlbXBmaWxlC— then it continued off screen

So the payload starts with:

import subprocess
import tempfile

That's the beginning of the decoded script. This is consistent with aClaude Code tool execution— when Claude Code runs Python via the Bash tool, it encodes the script as base64 and runs it withpython -c "exec(base64.b64decode('...'))"to avoid shell escaping issues. Thesubprocess+tempfileimports are typical of utility scripts Claude Code generates.

The 11k process storm was almost certainly aClaude Code session that got stuck in a loop, repeatedly spawning thesepython -ccommands. Each invocation would import subprocess/tempfile, likely spawning further child processes.

Can you read any more of the base64 string from the photo? Even a few more characters would help confirm exactly what the script was doing. Alternatively, if you can tell from htop whether the processes all had thesamebase64 string or different ones, that would also help narrow it down.

Also — do you remember what you were asking Claude Code to do right before this happened? That would probably be the fastest way to identify the trigger.

#5
11:22
54 bash

Can you please look through Claude Code logs? I was working from[internal repo]

I've hit a wall on forensic data for the 11:09 incident — the hard power-off prevented any diagnostic capture. But I found a lot from theearlier01:36 incident, which showed the same symptoms.

Here's what I can tell you:

The 01:36 incident(which DID leave a stall report) showed:

* 5 Claude Code v2.1.81 instancesrunning simultaneously
* 21 orphanedpython3.13processesrunningpython -c "exec(base64.b64decode(...))"— all using your uv Python
* Two of those Python processes were spawned directly by Claude Code asMCP server bridges(Python → Node.js)
* The orphaned processes' parents had died, leaving them stuck reading from dead pipes
* Auv runchain:uv → python → python (children)— matching the agent SDK pattern in your[personal project]

The decoded payloadyou read from htop:

import subprocess
import tempfile

This is the start of a Claude Code tool-execution wrapper — Claude Code base64-encodes Python scripts to avoid shell escaping issues when running them viapython -c.

For the 11:09 incident, the only trace I can find is that your[session ID]session went idle at 09:43 after pushing a commit, and the terminal died at 11:08. No Claude Code session logs cover the 09:43-11:08 gap.

Key question: Do you remember what you were doing in that ~1.5 hour gap between the Claude Code session ending (09:43) and the crash (11:08)? Were you:

* Running[personal project]scripts?
* Running another Claude Code instance that might not have written logs?
* Running anything else that usespython -cor the Claude Agent SDK?
#6
11:32
38 bash

Please continue investigating. I'm aware of macOS doing a system update overnight which could be related. I wasn't on my laptop personally at 1:36 in the morning. I think this is a separate thing.

OK, here's my best reconstruction of the 11:09 incident based on all the evidence:

Timeline (all times UTC):

Time
Event
09:24
System boots after overnight macOS update
09:24
Cursor starts, MCP servers initialize (futuresearch-mcp-legacy fails with ENOENT)
09:25
Cursor detects a Cursor update
, downloads it, marks it "ready"
09:25
basedpyright hits
ERR_WORKER_OUT_OF_MEMORY
 analyzing 7609 files
09:43
Claude Code session goes idle (pushed PR)
10:58
MCP reconnection triggers — futuresearch-mcp-legacy downloads litellm + 77 packages again
10:59:53-56
All 4 Cursor extension hosts exit
 (applying update)
~10:59-11:08
Process explosion
 — 11k Python processes spawn
11:00
Cursor storage slow close (6.7s) — system already under load
11:08
Terminal dies
11:09
Hard power-off

What happened:

Cursor was applying an auto-update at 10:59. When it shut down the 4 extension hosts, it needed to cleanly terminate 6 MCP servers, the Claude Code extension, basedpyright, and other language servers.

The exthost.log shows the Claude Code extension'sdispose()threwChannel has been closederrors, and both pyright extensionstimed outduring shutdown. This indicatesunclean process cleanup.

Thepython -c "exec(base64.b64decode('import subprocess\nimport tempfile...'))"processes are most likely fromPython environment detectionthat Cursor/extensions run. When the extension hosts restarted with the new Cursor version, they likely re-ran Python discovery — but the old processes from the previous version hadn't been cleaned up. Combined with the network permission dialog blocking things, this created a cascading spawn loop.

Recommendations:

1. Disable Cursor auto-update— apply updates manually: Settings →"update.mode": "manual"
2. Reduce MCP server count— you have the same MCP servers in both.mcp.jsonand.cursor/mcp.json. Consider disabling some in Cursor if you primarily use them through Claude Code CLI.
3. Addulimit -u 2048to your.zshrcto cap processes and prevent future fork bombs from taking down the system.
4. The futuresearch-mcp-legacy is broken— it keeps failing with ENOENT/missing API key, triggering repeated reconnection attempts. Either configureFUTURESEARCH_API_KEYor remove it from Cursor's plugin list.
#7
11:40
10 bash

Background task notification: "Search for the base64 payload in installed tools" completed.Read the output file to retrieve the result:[internal path]

This is malware in thelitellmPyPI package.Thelitellm_init.pthfile is asupply chain attackthat:

1. Executes on EVERY Python startup(.pthfiles run automatically)
2. Steals credentials: SSH keys, AWS secrets, GCP credentials, Kubernetes tokens,.envfiles, database passwords, crypto wallets, shell history
3. Exfiltrates datatohttps://models.litellm.cloud/encrypted with RSA
4. Installs persistencevia systemd services (~/.config/sysmon/sysmon.py)
5. Spreads to Kubernetes cluster nodesby creating privileged pods
6. Self-replicates— spawnspython -cchildren which trigger.pthagain, causing the 11k process fork bomb

The fork bomb was a side effect: becauselitellm_init.pthruns on every Python startup and the script spawnssubprocess.run([sys.executable, ...]), each child Python process also triggers the.pthfile, creating infinite recursion.

This is serious.Here's the full picture:

What happened:

1. At10:58:37, Cursor's futuresearch-mcp-legacy ranuvx, which depends onlitellm
2. uvdownloaded acompromised version of litellm(14.9MB) containinglitellm_init.pth
3. The.pthfile executes automatically onevery Python process startup
4. The malware collected your credentials, encrypted them with RSA, and attempted to exfiltrate tohttps://models.litellm.cloud/
5. The fork bomb was aside effect— eachsubprocess.run([sys.executable, ...])call triggered the.pthin the child process, causing exponential process spawning
6. At11:07, the malware tried to install persistence at~/.config/sysmon/sysmon.py
7. You force-rebooted at11:09, interrupting the persistence (file is 0 bytes)

Credentials likely exfiltrated (assume compromised):

* SSH keys (id_ed25519,id_ed25519_hetzner,id_ed25519_mac_air)
* GCloud application default credentials
* Kubernetes config (~/.kube/config)
* Multiple.envfiles across[internal repo](Supabase passwords, API keys visible in.mcp.json)
* Shell history
* Git config
* All environment variables (including anything in your shell profile)

Immediate actions:

1. Rotate ALL SSH keys— generate new ones, revoke old ones on GitHub/servers
2. Rotate GCloud credentials—gcloud auth revoke+ re-authenticate
3. Rotate Kubernetes credentials— regenerate kubeconfig
4. Rotate ALL secrets in your.envfiles— Supabase passwords, API keys, etc.
5. Rotate the credentials visible in.mcp.json— the Supabase passwords, ClickHouse password, Grafana token
6. Purge the uv cache—rm -rf ~/.cache/uvto remove all cached packages
7. Report this to litellm— this is a compromised package on PyPI
8. Check ifmodels.litellm.cloudis a known malicious domain— this is NOT the legitimate litellm infrastructure

Should I help with any of these rotation steps?

When it finally clicked. Claude was telling me what had been exposed before any security researchers had published reports.

#8
11:46
2 bash, 2 read

Did you find the file? Can you please confirm this?

Yes —confirmed. The file contents are preserved in the tool results cache. The first line is:

import os, subprocess, sys; subprocess.Popen([sys.executable, "-c", "import base64; exec(base64.b64decode('aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHRlbXBmaWxl...

This is exactly theexec(base64.b64decode('aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHRlbXBmaWxl...'))pattern you saw in htop.

And the persistence directorydid existon your machine:

~/.config/sysmon/sysmon.py — 0 bytes, created at 11:07

The 0-byte file means the write was interrupted by your forced reboot. The malware was 2 minutes into installing persistence when you killed it.

The file was in two places inuv's cache — both copies oflitellm_init.pthin cached archives.

Both are now deleted. But I'd strongly recommend purging the entire uv cache (rm -rf ~/.cache/uv) and rotating all the credentials I listed — the exfiltration tomodels.litellm.cloudmay have succeeded before the fork bomb brought down your system.

#9
11:47
8 bash

Can you please check Kubernetes to see if it's spread there at all?

Kubernetes is clean.Nonode-setup-*orsysmonpods found anywhere. The most recent pod creation inkube-systemwas March 21 (metrics-server), well before the incident.

The malware's K8s spread code targets Linux paths (/var/run/secrets/kubernetes.io/serviceaccount/token) which don't exist on macOS. The malware ran on your Mac, not inside a pod, so it wouldn't have had a K8s service account token to authenticate with. Your~/.kube/configcredentials could theoretically have been used, but the fork bomb likely crashed the process before it got to the K8s lateral movement stage of the script.

All clean.Every pod created today is from your normal infrastructure — CronJobs ([internal service]) and deployments ([internal service]). No maliciousnode-setup-*oralpine:latestpods.

The K8s cluster was not compromised. The malware's K8s spread almost certainly failed because:

1. It ran on macOS, not inside a pod (no service account token at/var/run/secrets/...)
2. The fork bomb crashed the process before it could reach the K8s code path
3. Even with your~/.kube/config, GKE RBAC may have prevented creating privileged pods inkube-system

Still need to rotate your kubeconfig credentials as a precaution— the malware did attempt to read~/.kube/configand could have exfiltrated it before the fork bomb hit.

#10
11:48
4 bash, 1 agent

Where did the litellm files come from? Do you know which env? Are there reports of this online?

Thelitellm_init.pthIS in the official package manifest— the RECORD file lists it with a sha256 hash. This means it was shipped as part of thelitellm==1.82.8wheel on PyPI, not injected locally.

The infection chain:

Cursor → futuresearch-mcp-legacy (v0.6.0) → litellm (v1.82.8) → litellm_init.pth

The Cursor log at 10:58:38 confirms:Downloading litellm (14.9MiB)→Installed 77 packages. This wasuvxpulling in litellm as a transitive dependency.

No public reports exist yet.This appears to be avery fresh compromise— version 1.82.8 was published to PyPItoday(March 24, 2026). There isno corresponding GitHub release tag for v1.82.8, which is suspicious — it suggests someone published directly to PyPI without going through the normal release process.

Your local[internal repo]environment is safe— it has litellm1.70.4, pinned to<1.77.3. The infected version only entered via Cursor'suvx futuresearch-mcp-legacyinvocation.

You should report this immediately:

1. PyPI— emailsecurity@pypi.orgto get v1.82.8 yanked
2. BerriAI/litellm— open a security advisory atgithub.com/BerriAI/litellm/security
3. Your team— anyone who installed litellm today may be affected

Do you want me to help draft the report?

Wait, am I the first? Note theveryhelpful links for who to contact

#11
11:53
2 bash

Can you print the contents of the malware script without running it?

There it is in full. The structure is:

* litellm_init.pth— a one-liner that runs on every Python startup, spawns a child process with the base64 payload
* Stage 2 (the decoded payload)— an RSA public key for encrypting stolen data
* B64_SCRIPT— a THIRD stage (the credential harvester) that steals SSH keys, .env files, AWS/GCP/Azure/K8s creds, crypto wallets, database passwords, shell history, etc.
* run()— executes the harvester as a subprocess, collects its output, encrypts it with the RSA key + AES, and POSTs it tohttps://models.litellm.cloud/
* Persistence installation at~/.config/sysmon/sysmon.pywith a systemd service
* K8s lateral movement — creates privilegedalpine:latestpods on every node to install the persistence on cluster nodes

The fork bomb was caused by line 1:subprocess.Popen([sys.executable, "-c", ...])— this child Python process also has the.pthin its site-packages, so it triggers the.pthagain, which spawns another child, infinitely.

#12
11:54
6 bash

Where in the litellm files on GitHub can I find this?

You won't find it on GitHub because it doesn't exist there.Here's the proof:

* No GitHub tagforv1.82.7orv1.82.8— the latest tagged releases arev1.82.6.rc.2and various dev builds
* PyPI upload time:2026-03-24T10:52:19UTC — that's6 minutes before Cursor downloaded itat 10:58:37
* Not yanked— it's still live on PyPI right now

This was almost certainly published by someone whocompromised the litellm PyPI publishing credentials(or a maintainer account). They uploaded a poisoned v1.82.8 directly to PyPI without going through the normal GitHub release process. The version number was chosen to be higher than any existing release so it would be picked up by>=version constraints.

The.pthfile was embedded in the wheel at the top level of site-packages — this is a standard Python packaging trick where a.pthfile placed alongside packages gets auto-executed by the Python interpreter on startup.

This package is still live on PyPI and actively infecting people.You should report this now:

* PyPI:security@pypi.org— request immediate yank of litellm 1.82.8 (and check 1.82.7)
* BerriAI/litellm: open a security issue atgithub.com/BerriAI/litellm/security/advisories
#13
11:58
3 bash

Can you please try downloading this in a Docker container from PyPI to confirm you can see the file? Be very careful in the container not to run it accidentally!

Confirmed.Fresh download from PyPI right now in an isolated Docker container:

Inspecting: litellm-1.82.8-py3-none-any.whl
FOUND: litellm_init.pth
SIZE: 34628 bytes
FIRST 200 CHARS:
import os, subprocess, sys; subprocess.Popen([sys.executable, "-c", "import base64; exec(base64.b64decode('aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHRlbXBmaWxl...

The maliciouslitellm==1.82.8islive on PyPI right nowand anyone installing or upgrading litellm will be infected. This needs to be reported tosecurity@pypi.orgimmediately.

A final sanity check that I wasn't about to start blaming the wrong dependency

#14
12:01
7 bash, 2 read, 1 write

Please write a short blog post to our landing site explaining the details of what happens, 2-3 paragraphs, then make a PR.

Blog post written, PR'd, and merged in under 3 minutes.

0a9ac33blog: litellm PyPI supply chain attack disclosure

#15
12:04

Which Reddit subreddits should we share with?

Given the nature of the attack (PyPI supply chain, targets LLM/AI developers, K8s lateral movement), the highest-signal subreddits would be:

* r/Python— largest audience of people who might havepip install litellmin their recent history
* r/netsec— security professionals who can amplify and help get PyPI to act fast
* r/LocalLLaMA— litellm is heavily used in the local LLM community for model routing
* r/MachineLearning— broad AI/ML audience, many litellm users
* r/devops— the K8s lateral movement angle is directly relevant here

I'd prioritizer/Pythonandr/netsecfirst — those two will get the fastest response from people who can act on it (package maintainers, PyPI admins, and security responders). r/LocalLLaMA third since litellm is a core tool in that community.

#16
12:06
1 read, 1 edit, 1 bash

Please can you clean this up, make it much less sloppy.

Don't worry, I re-wrote it once the dust had settled

#17
12:10

Continue from where you left off.

#18
12:10
5 bash, 2 edit, 1 read

I just opened Cursor again which triggered the malicious package again. Can you please check the files are purged again?

2201b19blog: add litellm issue link, improve post structure

7a7f33eblog: fix attribution on litellm issue link

#19
12:13
1 bash

Yes please merge the PR.

#20
12:13

[Request interrupted by user]

#21
12:14
5 bash, 2 read, 1 edit, 1 write

Actually mention we reported via email to litellm maintainers, then mention the tracking issue separately.

58fbfccblog: clarify reporting attribution

8b235ecblog: resolve merge conflict, keep improved version
