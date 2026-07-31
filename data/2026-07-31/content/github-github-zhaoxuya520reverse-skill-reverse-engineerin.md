---
title: 'GitHub - zhaoxuya520/reverse-skill: Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 · GitHub'
url: https://github.com/zhaoxuya520/reverse-skill
site_name: github
content_file: github-github-zhaoxuya520reverse-skill-reverse-engineerin
fetched_at: '2026-07-31T11:44:06.192541'
original_url: https://github.com/zhaoxuya520/reverse-skill
author: zhaoxuya520
description: Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工具链 + 自动进化经验库 | 支持 Claude Code / Kiro / Cursor / Cline 等代码 AI 客户端 - zhaoxuya520/reverse-skill
---

zhaoxuya520

 

/

reverse-skill

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star10k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

95 Commits
95 Commits
.github
.github
 
 
CTF-Sandbox-Orchestrator
CTF-Sandbox-Orchestrator
 
 
burp-mcp-full
burp-mcp-full
 
 
docs
docs
 
 
kali
kali
 
 
reports
reports
 
 
scripts
scripts
 
 
skills
skills
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README-kali.md
README-kali.md
 
 
README.md
README.md
 
 
README_AI.md
README_AI.md
 
 
README_zh.md
README_zh.md
 
 
RULES.md
RULES.md
 
 
RULES_zh.md
RULES_zh.md
 
 
VERSION
VERSION
 
 
reverse-skill.png
reverse-skill.png
 
 
View all files

## Repository files navigation

# reverse-skill

### Cybersecurity Skills Router · 逆向技能路由包

Navigate the dark waters, sail against the stream.

About·Getting Started·Usage·Fast route·Routing·Ops contracts·AI Bootstrap·Sponsors·Contributing

🌐中文

## About

If you are an AI Agent, jump toREADME_AI.mdand follow the instructions strictly.

When an AI agent (Claude Code, Codex CLI, Cursor, etc.) encounters an APK, a binary, frontend JS encryption, a CTF challenge, or a pentesting target, this package routes it to the right methodology, checks available tools, and executes a repeatable workflow instead of guessing commands.

User task
 → RULES.md
 → MASTER-ROUTING / master-route.ps1 (PRIMARY)
 → case-init / scope.md (auth + network_profile; no target ACT until ready)
 → Scenario skill → tools / MCP / scripts
 → timeline + Evidence→Finding→Path → report + field-journal

Why this exists:

* AI agents don't know whether to use jadx, apktool, Frida, IDA, or BurpSuite for a given task
* APK, ELF, JS, PCAP, and CTF tasks each need different playbooks
* Tools, MCP servers, and scripts are scattered across machines
* The same mistakes get repeated because experience isn't reused

PRIMARY ladder:skills/MASTER-ROUTING.md· Full matrix:skills/routing.md· Ops:skills/ops/

(back to top)

### Built With

IDA Pro·radare2·Ghidra

(back to top)

## Getting Started

### Prerequisites

* Java / JDK— for jadx and apktool
* Node.js 22.12+— for JS toolchain and MCP servers
* Python 3.x— for Frida and helper scripts
* A code AI client— Claude Code, Codex CLI, Cursor, etc.

### Installation

git clone https://github.com/zhaoxuya520/reverse-skill.git

Then refresh the tool index per platform:

Platform

Command

Windows

powershell -File skills/scripts/refresh-tool-index.ps1

Linux / macOS

bash skills/scripts/refresh-tool-index.sh

Kali Linux

bash kali/scripts/refresh-tool-index.sh

Checkskills/tool-index.mdto see detected tools.

Platform-specific docs:

* Kali Linux→kali/README-kali.md
* Ubuntu/Debian→docs/platforms/linux.md
* macOS→docs/platforms/macos.md

(back to top)

## Usage

### Supported scenarios

Scenario

Entry

APK / Android analysis

skills/apk-reverse/

iOS / mobile

skills/mobile-reverse/

Binary reverse (exe/dll/so/elf)

skills/ida-reverse/
 / 
skills/radare2/

.NET / C#

skills/dotnet-reverse/

Frontend JS / encrypted params

skills/js-reverse/

DSL VM / custom JS opcode VM

skills/reverse-engineering/dsl-vm-reverse/

HTTP capture / request replay

anything-analyzer + 
js-reverse/

Malware / YARA

skills/malware-analysis/

Penetration testing / scanning

skills/pentest-tools/

Attack chain / red-team orchestration

skills/attack-chain/

CTF competition

CTF-Sandbox-Orchestrator/
 (40+ sub-skills)

Firmware / IoT

skills/firmware-pentest/

Patch diff / N-day

skills/patch-diff-exploit/

Pwn / exploit development

skills/pwn-chain/

EDR bypass

skills/edr-bypass-re/

API / GraphQL

skills/api-security/

Supply chain / SBOM

skills/supply-chain-security/

LLM / AI security

skills/llm-security/

OLLVM deobfuscation

skills/reverse-engineering/references/ollvm-deobfuscation.md

Diagrams / reports

skills/diagram-generator/
 / 
skills/docs-generator/

### Key files

File

Purpose

README_AI.md

AI agent bootstrap and configuration

RULES.md

Global routing rules (scope gate before ACT)

skills/MASTER-ROUTING.md

PRIMARY fast ladder

skills/routing.md

Task → skill routing matrix

skills/SKILL.md

Master entry point

skills/tool-index.md

Local tool status (auto-generated)

skills/scripts/master-route.ps1

One-shot PRIMARY triage

skills/scripts/case-init.ps1

Case dir: scope / timeline / workitems

skills/ops/

Scope, Evidence chain, roles, timeline (skill-router form)

### Repository layout

.
├── README.md / README_zh.md / README_AI.md
├── RULES.md / RULES_zh.md
├── skills/
│ ├── MASTER-ROUTING.md / SKILL.md / routing.md
│ ├── ops/ # ops contracts
│ ├── scripts/ # master-route, case-init, bootstrap, verify
│ ├── field-journal/
│ ├── apk-reverse/ mobile-reverse/ js-reverse/ dotnet-reverse/
│ ├── ida-reverse/ radare2/ reverse-engineering/ malware-analysis/
│ ├── pentest-tools/ attack-chain/ pwn-chain/ firmware-pentest/
│ ├── api-security/ supply-chain-security/ llm-security/
│ └── ...
├── CTF-Sandbox-Orchestrator/
├── docs/
├── kali/ # see kali/README-kali.md
└── work/ # local cases (gitignored)

(back to top)

## Sponsors

For sponsorship or business inquiries:

(back to top)

## Contributing

Contributions are welcome! Fork the repo, create a feature branch, and open a PR.

1. Fork the Project
2. git checkout -b feature/AmazingFeature
3. git commit -m 'Add some AmazingFeature'
4. git push origin feature/AmazingFeature
5. Open a Pull Request

### Contributors

(back to top)

## License

This project (reverse-skill) is primarily licensed under theMIT License(seeLICENSE).

Submodule and third-party dependencies:

* CTF-Sandbox-Orchestrator/:GNU GPLv3
* Pentest Swarm AI: Original project isAGPL-3.0. This repo only invokes it via CLI or MCP and does not include its source code
* Other tools (jadx, frida, nmap, burpsuite-mcp, etc.) are subject to their respective official licenses

(back to top)

## Acknowledgments

Thanks to all open-source tool authors. This project integrates tools across reverse engineering, penetration testing, CTF, and security analysis — every tool is the fruit of community effort.

Special thanks to the OLLVM deobfuscation ecosystem contributors and everyone who submitted test samples, issues, and PRs.

(back to top)

## Contact

* Email:24781737@qq.com
* Discord:reverse-skill