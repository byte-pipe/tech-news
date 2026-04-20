---
title: 'AI Coding Tools in a Sandbox: Why Your File System Needs Protection | Dirk Holtwick'
url: https://holtwick.de/en/blog/bx-sandbox
site_name: tldr
content_file: tldr-ai-coding-tools-in-a-sandbox-why-your-file-system
fetched_at: '2026-04-01T11:24:25.231173'
original_url: https://holtwick.de/en/blog/bx-sandbox
date: '2026-04-01'
published_date: '2026-03-28T23:00:00.000Z'
description: AI coding tools like Claude Code or Copilot have full access to your file system. bx protects everything except the current project directory with a single command.
tags:
- tldr
---

# AI Coding Tools in a Sandbox: Why Your File System Needs Protection

ai
apple
opensource
project
release

If you work with AI-powered coding tools today — be it Claude Code, Copilot, or Cursor — you quickly get used to the productivity boost. What’s easy to overlook: these tools have full access to your entire file system. Every command the AI executes runs with the same permissions as you.

That might be fine for a hobby project. But if you’re handling client data, have license keys on disk, SSH keys for production servers, or simply private photos in your home directory — at some point, you start feeling uneasy.

## The Existing Options

Of course, there are ways to protect yourself:

Docker containersoffer good isolation, but they’re cumbersome for typical macOS development workflows. You need to mount volumes, configure IDE integration, and the workflow never feels quite native.

Claude’s built-in restrictions— the tool politely asks before modifying files. But “asking” isn’t protection. A hallucinated file path, a misinterpreted command, and suddenly the AI reads something it shouldn’t have seen. The trust is based on the model’s behavior, not on a technical barrier.

VSCode Workspace Trustprotects against automatic code execution, but not against file system access from a terminal or an extension.

None of these solutions really convinced me.

## The Idea: Use the macOS Sandbox

macOS ships withsandbox-exec, a kernel-level sandbox that Apple itself uses for App Store apps. The idea: a tool that launches any application so it can only see the current project directory — and nothing else.

The result isbx. A CLI tool you put in front of your actual command:

bx
 claude
 ~/work/my-project

That’s it. Claude Code starts with full access to~/work/my-project— but~/Documents,~/Desktop,~/.ssh, other projects, and everything else in the home directory is invisible.

## Built in Two Days — with Claude Code Itself

The ironic part: bx was built entirely with the tool it’s designed to protect against. In two intensive days, Claude Code wrote the bulk of the code — from sandbox profile generation to CLI argument parsing to app discovery via macOS Spotlight.

It worked surprisingly well. Claude knew the (undocumented!) Apple Sandbox Profile Language and correctly handled its quirks — for instance, the fact thatdenyrules in SBPL always take precedence overallowrules, regardless of order. This means you can’t simply lock down the entire home directory and then add exceptions. bx solves this by scanning the home directory and selectively blocking only sibling directories.

## More Than Just Claude Code

bx isn’t limited to one tool. It supports VSCode, Xcode, Terminal, and arbitrary commands out of the box. Any app can be added via a TOML configuration file:

[
apps
.
cursor
]

bundle =
"com.todesktop.230313mzl4w4u92"

binary =
"Contents/MacOS/Cursor"

The tool finds apps automatically via their macOS bundle ID — no hardcoded paths needed. And if you regularly work with the same projects, you can configure default directories per app:

[
apps
.
code
]

workdirs = [
"~/work/project-a"
,
"~/work/shared-lib"
]

A simplebx codethen opens VSCode with exactly those directories — sandboxed.

## Fine-Grained Control

What makes bx especially practical: you can hide files even within an allowed project directory. A.bxignorefile in the project works like.gitignore:

.env

.env.*

*.pem

secrets/

This keeps environment variables and certificates invisible, even when the project directory itself is fully accessible.

Withbx --dryyou can preview exactly what will be protected — without launching anything. It gives you a clear picture of the actual isolation.

## The Growing Attack Surface

What many people underestimate: modern AI coding tools are far more than chat interfaces. Claude Code, for example, can execute shell commands, create and delete files, and access external services via MCP servers (Model Context Protocol) — databases, APIs, cloud infrastructure. On top of that, there are skills and hooks that can trigger actions automatically.

All of this happens in the user’s context, with their full permissions. bx’s sandbox operates at the kernel level: whether it’s anrmcommand, an MCP tool, or an automated hook trying to access~/Documents— the operating system blocks the access before it even happens. This is fundamentally different from a software-level restriction that could be bypassed.

Important to note: within the allowed project directory, everything is permitted — that’s intentional, otherwise you couldn’t work. If you have sensitive files there, you can selectively exclude them via.bxignore.

## Being Honest

bx is not a high-security vault.sandbox-execis an undocumented Apple API that could change with any macOS update. There’s no network protection — API calls, git push, and npm install all work normally. And sandbox rules are generated once at launch; directories created afterwards are not automatically protected.

But as a pragmatic security layer for everyday development, it works remarkably well. It’s the difference between “the AI can theoretically read everything” and “the AI can only see this one project.”

That said, to be clear: bx was built with the best of intentions and to the best of my knowledge, but it comes with no guarantees. It’s not a replacement for a professional security solution, and it doesn’t absolve anyone from thinking for themselves. If you’re working with truly critical data, don’t rely blindly on any single tool — no matter how well it works. bx is an additional layer of protection, not a substitute for common sense.

## Try It Out

bx can be installed via Homebrew or npm:

brew
 install
 holtwick/tap/bx

# or

npm
 install
 -g
 bx-mac

The code is open source on GitHub:github.com/holtwick/bx-mac

I’d love to hear your feedback, feature requests, and of course stars. And if you have interesting use cases — let me know!

This blog post was written by Claude (Anthropic’s AI) and reviewed and approved by me. Fitting, given the topic, I’d say.

Published on March 29, 2026

 
Back to posts listing
