---
title: Windows When? Windows Now — Zed's Blog
url: https://zed.dev/blog/zed-for-windows-is-here
site_name: hackernews_api
fetched_at: '2025-10-16T11:08:22.386873'
original_url: https://zed.dev/blog/zed-for-windows-is-here
author: meetpateltech
date: '2025-10-15'
published_date: 10/15/2025
description: 'From the Zed Blog: Zed for Windows is finally here. Download it today.'
tags:
- hackernews
- trending
---

← Back to Blog

# Windows When? Windows Now

Zed is now available on Windows. You can download thestable release here. Or if you prefer to live on the bleeding edge, you can use thepreview release, which receives new features one week earlier.

Windows is now a fully supported platform for Zed. We'll be shipping updates every week, like we do with Mac and Linux. Several Zed engineers use Windows as their daily driver, and we will maintain a full-time Windows team, including@localcc, our Windows platform lead.

Read on to learn about the key Windows features.

## Windows Platform Integration

Zed isn't an Electron app; we integrate directly with the underlying platform for maximal control. The Windows build uses DirectX 11 for rendering, and DirectWrite for text rendering, to match the Windows look and feel.

## WSL and SSH Remoting

Zed integrates directly withWindows Subsystem for Linux(WSL). From the WSL terminal, you can open a folder in Zed using thezedcommand-line script. And from within Zed, you can open a folder in any of your WSL distros by clickingFile > Open Remote(or runningproject: open remotefrom the command palette) and selectingAdd WSL Distro.

Opening a folder in WSL from within Zed

Similarly, if you're connecting to aremoteLinux machine, selectConnect New Server.

Under the hood, when editing under WSL or SSH, Zed runs a lightweight "remote server" process underwsl.exe/ssh.exe, and all I/O operations are routed through that process. Most features in Zed are designed to work with remote editing: loading and saving files, git integration, terminals, tasks, language servers, and debuggers.

## Extension Compatibility

Zed extensions work on Windows; no special steps, no caveats. You can install them from the Extensions panel and get back to coding. And if you want to create a new extension, you can do so without any Windows-specific workarounds.

Zed extensions areWebAssembly Components, and they have sandboxed access to the file system via theWebAssembly System Interface(WASI). Zed manages the conversions of file system paths as they are passed into and out of extensions, so that extension authors don't need to worry about the differences between Windows and Unix paths.

## Agentic Coding on Windows

All of Zed’s AI features, includingedit predictionsandACP-powered agents, are fully supported on Windows, and in combination with WSL/SSH remoting. LeverageClaude Code directly in Zedthrough ACP,trial Zed Profor free for 14 days, or bring your own keys.

## Use It Today

Thank you to everyone who participated in our Alpha & Beta testing, reporting issues on GitHub and Discord. We've fixed a lot of bugs, but we know the work is not over. If you find something amiss,please let us know.
We’re especially looking for feedback on WSL workflows, IME and keyboard layouts, multi-monitor setups, and 120–144 Hz displays.

Your reports will shape the next set of fixes, features, and polish.Download Zed for Windows, take it for a spin, and tell us what to build next.

### Looking for a better editor?

You can try Zed today on macOS, Windows, or Linux.Download now!

### We are hiring!

If you're passionate about the topics we cover on our blog, please considerjoining our teamto help us ship the future of software development.
