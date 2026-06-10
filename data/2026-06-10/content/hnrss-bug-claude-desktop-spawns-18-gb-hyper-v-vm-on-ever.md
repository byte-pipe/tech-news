---
title: '[BUG] Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use · Issue #29045 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/29045
site_name: hnrss
content_file: hnrss-bug-claude-desktop-spawns-18-gb-hyper-v-vm-on-ever
fetched_at: '2026-06-10T19:51:35.478748'
original_url: https://github.com/anthropics/claude-code/issues/29045
date: '2026-06-10'
description: Preflight Checklist I have searched existing issues and this hasn't been reported yet This is a single bug report (please file separate reports for different bugs) I am using the latest version of Claude Code What's Wrong? [BUG] Claude D...
tags:
- hackernews
- hnrss
---

anthropics

 

/

claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork21.3k
* Star132k

# [BUG] Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use#29045

Open
Open
[BUG] Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only use
#29045
Labels
invalid
Issue doesn't seem to be related to Claude Code
Issue doesn't seem to be related to Claude Code

## Description

davidellett
opened 
on 
Feb 26, 2026
Issue body actions

### Preflight Checklist

* I have searchedexisting issuesand this hasn't been reported yet
* This is a single bug report (please file separate reports for different bugs)
* I am using the latest version of Claude Code

### What's Wrong?

[BUG] Claude Desktop spawns 1.8 GB Hyper-V VM on every launch, even for chat-only useEnvironment

Note: This issue is specific to the Claude Desktop app (Windows), not Claude Code CLI.

OS: Windows 11 Pro 25H2, Build 26200.7840Hardware: Razer Blade 15 Base Model (Late 2020), i7-10750H, 16 GB RAMClaude Desktop: Latest version as of 2/26/2026Windows Features: VirtualMachinePlatform enabled; Hyper-V, WSL, Docker, and Windows Sandbox are all disabledCore Isolation / Memory Integrity: Off

SummaryThe Claude Desktop app launches a Hyper-V virtual machine (Vmmem) consuming approximately 1.8 GB of RAM every time it starts — even when the user only needs chat functionality and has no intention of using Cowork or agent mode. On a 16 GB laptop, this represents over 11% of total memory consumed by infrastructure that isn't being used.Steps to Reproduce

Install Claude Desktop on Windows 11 with VirtualMachinePlatform enabledUse Cowork/agent mode at least once (this creates session files)Close and reopen Claude Desktop — or simply reboot the machineOpen Task Manager and observe Vmmem consuming ~1,800 MB

What HappensOn every launch, the Claude Desktop app triggers the Hyper-V Host Compute Service (vmcompute) via an RPC interface event, which spawns a vmwp.exe process hosting a full virtual machine. This VM appears as "Vmmem" in Task Manager at approximately 1,796–1,846 MB.The Hyper-V Compute Admin event log shows repeated errors:"The specified property query is invalid: The virtual machine or container JSON document is invalid. (0xC037010D, 'Invalid JSON document '$'')"These errors have been occurring since at least 2/19/2026, triggered on every boot and app launch.Root Cause InvestigationThrough extensive PowerShell diagnostics, we confirmed:

WSL is not installed — wsl --shutdown returns "not installed"Hyper-V management tools are not installed — Get-VM failsDocker is not installed — no Docker processes foundWindows Sandbox is disabledCore Isolation / Memory Integrity is off (and was off before this issue started)VirtualizationBasedSecurityStatus shows 2 (running), likely due to LSA Protection being enabled — but this alone doesn't explain the 1.8 GB VMThe only enabled virtualization feature is VirtualMachinePlatform

The vmcompute service is set to Manual start but is triggered at boot by an RPC interface event (GUID: bc90d167-9470-4139-a9ba-be0bbbf5b74d). The parent process is services.exe (PID 1400), confirming it's a service trigger, not a user-initiated launch.We found 2,689 stale session files in %APPDATA%\Claude\local-agent-mode-sessions\ — all from previous Cowork sessions that were never cleaned up. Session names follow Docker-style naming (e.g., "nifty-dreamy-volta", "tender-vigilant-goodall", "admiring-elegant-johnson"). Even after deleting all 2,689 files and killing vmcompute/vmwp, simply reopening the Claude Desktop app immediately respawned the VM and the 1.8 GB Vmmem process.ImpactOn a 16 GB system, this bug causes memory usage to jump from ~50% to ~62% at idle before the user does anything. Combined with normal application load, this pushes total usage to 70–75%, causing system sluggishness and forcing the user to manually kill VM processes after every launch.Expected Behavior

The Claude Desktop app should not spawn a VM for chat-only sessionsIf Cowork infrastructure is needed, it should initialize on demand — only when the user actually starts a Cowork/agent sessionStale session files from previous Cowork sessions should be cleaned up automatically, not accumulate indefinitely (2,689 files in our case)The app should fall back to chat-only mode if VM initialization fails or is unnecessary, rather than unconditionally starting VM infrastructure

Current WorkaroundThe only reliable workaround is to disable VirtualMachinePlatform entirely:powershellDisable-WindowsOptionalFeature -Online -FeatureName "VirtualMachinePlatform" -NoRestartThis prevents the VM from launching but also disables Cowork functionality. Alternatively, the user can kill the VM processes after every launch:powershellStop-Process -Name vmwp -ForceStop-Process -Name vmcompute -ForceChat functionality continues to work normally after killing these processes.RequestPlease modify the Claude Desktop app so that:

VM/container infrastructure only initializes when Cowork or agent mode is actively requestedOld session data is cleaned up automatically after sessions endThe app gracefully handles the absence of VM infrastructure without degraded chat performance

### What Should Happen?

The Claude Desktop app should not spawn a Hyper-V VM (Vmmem, ~1.8 GB RAM) when launching for chat-only use. VM/container infrastructure should only initialize when the user actively starts a Cowork or agent session. Stale session files should be cleaned up automatically after sessions end.

### Error Messages/Logs

Hyper-V Compute Admin log shows repeated errors on every boot:

"
The specified property query is invalid: The virtual machine or container JSON document is invalid. (0xC037010D, 'Invalid JSON document '$'')
"

### Steps to Reproduce

1. Install Claude Desktop on Windows 11 with VirtualMachinePlatform enabled
2. Use Cowork at least once
3. Close and reopen Claude Desktop (or reboot)
4. Observe Vmmem in Task Manager consuming ~1,800 MB at 0% CPU

### Claude Model

Not sure / Multiple models

### Is this a regression?

I don't know

### Last Working Version

No response

### Claude Code Version

Claude Desktop (Windows) latest as of 2/26/2026

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

PowerShell

### Additional Information

See detailed bug report in description above.

Reactions are currently unavailable

## Metadata

## Metadata