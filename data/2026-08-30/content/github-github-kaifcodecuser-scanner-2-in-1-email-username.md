---
title: 'GitHub - kaifcodec/user-scanner: 🕵️‍♂️ (2-in-1) Email & Username OSINT suite for deep data extraction just from a single Email/Username. Analyzes 455+ actively maintained scan vectors (175+ email / 280+ username) for security research, investigations, and digital footprinting. · GitHub'
url: https://github.com/kaifcodec/user-scanner
site_name: github
content_file: github-github-kaifcodecuser-scanner-2-in-1-email-username
fetched_at: '2026-08-30T06:00:15.062523'
original_url: https://github.com/kaifcodec/user-scanner
author: kaifcodec
description: 🕵️‍♂️ (2-in-1) Email & Username OSINT suite for deep data extraction just from a single Email/Username. Analyzes 455+ actively maintained scan vectors (175+ email / 280+ username) for security research, investigations, and digital footprinting. - kaifcodec/user-scanner
---

kaifcodec

 

/

user-scanner

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork400
* Star3.4k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,355 Commits
1,355 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
abandoned
abandoned
 
 
docs
docs
 
 
tests
tests
 
 
user_scanner
user_scanner
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# User Scanner

A powerful2-in-1 OSINT suiteengineered for deepEmail and Username Intelligence.

With455+ total scan vectors—including175+ email-integrated sitesand280+ username platforms—you can map digital footprints, analyze target behavior, uncover interests, full metadata of usernames and verify account registrations in seconds.

## 💖 Sponsored by

Go beyond account enumeration.WebVetted turns an email or username into a complete identity investigation with deep OSINT enrichment, breach intel, AI analysis, and an interactive identity graph.Start an Investigation →

Comprehensive OSINT platform for professional investigators and analysts.Reverse email, phone number, and username search across 250+ modules. Automate your intelligence gathering with our powerful tools.Get Started →

## ✨ Key Features

* 🔎Deep Email & Username OSINT:Look up email registrations and perform advanced username profiling across 455+ platforms.
* 👤Rich Metadata Scraping:Scrapes avatars, bio descriptions, follower counts, UID numbers, seller statuses, and account attributes.
* 🔀Cross-Scan & Pivot Engine:Mines handles, profile links, and exposed email addresses from initial scans, automatically pivoting across secondary target vectors.
* 🤖Model Context Protocol (MCP) Server:Native AI agent integration for Claude Desktop, Cursor, Antigravity, and LLMs to run autonomous OSINT scans and recursive pivots.
* 🛡️Hudson Rock Infostealer Breach Intel:Query infostealer malware breach logs using the--hudsonflag for high-priority target correlation.
* ⚡High-Throughput Parallel Engine:Powered byhttpxandcurl_cffifor maximum concurrency with automated TLS fingerprint impersonation.
* 🔀Permutation & Alias Generator:Wildcard-based username variation generation to catch typosquatting or alternative aliases.
* 📂Multi-Format Reports:Automated exports toPDF(with profile photos),JSON, andCSVfor pipeline integration.
* 🌐Advanced Proxy Pivoting:Built-in proxy rotation with protocol auto-detection (http,socks5) and pre-scan health validation (--validate-proxies).
* 🎨Responsive Terminal UI:Dynamic progress tracking, self-adaptive category grids (-lu/-le), and clear status reporting.

## 🚀 Installation

### 🐍 Via PyPI (Recommended)

#
 Upgrade pip and install user-scanner

python3 -m pip install --upgrade pip
pip install user-scanner

#
 Optional: Install with MCP Server support for AI agents

pip install 
"
user-scanner[mcp]
"

### 📦 Virtual Environment Setup

#
 Create and activate virtual environment

python3 -m venv .venv

source
 .venv/bin/activate 
#
 On Windows: .venv\Scripts\Activate.ps1

#
 Install package

pip install user-scanner

### ❄️ Via Nix (Linux & macOS)

#
 Run instantly without installing permanently

nix run github:kaifcodec/user-scanner/main -- --help

#
 Drop into a temporary shell with user-scanner active

nix shell github:kaifcodec/user-scanner/main

## 💻 Usage Guide

### 1. Basic Username & Email Scanning

Scan a single username or email address across all available platform modules:

user-scanner -u johndoe 
#
 Single username scan

user-scanner -e johndoe@gmail.com 
#
 Single email scan

### 2. Cross-Scan & Pivot Intelligence

An email scan proves an account exists but rarely reveals a handle.--cross-scanmines exposed handles, profile links, and secondary email addresses from target profiles, pivoting into multi-pass reconnaissance across all matching platforms:

Pivot Direction

What it Mines

-e
 → 
username

Handles or social links exposed on an email's registered profile

-u
 → 
username

Secondary aliases advertised across target social profiles

-u
 → 
email

Public email addresses published on target profile pages

-e
 → 
email

Secondary addresses exposed by initial email profiles

user-scanner -u johndoe --cross-scan 
#
 Pivot from username scan

user-scanner -e johndoe@gmail.com --cross-scan 
#
 Pivot from email scan

user-scanner -e johndoe@gmail.com --cross-scan --cross-links verified 
#
 Platform-verified links only

user-scanner -u johndoe --cross-scan --cross-depth 2 
#
 Follow links two hops deep

💡For confidence scoring, link classification rules, and cost models, seedocs/CROSS_SCAN.md.

### 3. Hudson Rock Malware Breach Intelligence

Check if a target username or email address has been exposed ininfostealer malware infection logs:

user-scanner -u johndoe --hudson 
#
 Username malware log check

user-scanner -e johndoe@gmail.com --hudson 
#
 Email malware log check

🖼️To view output terminal screenshots and visual previews, seedocs/EXAMPLES.md.

### 4. Targeted Category & Module Scanning

Scan specific categories or individual modules, or list available modules in a responsive grid:

user-scanner -u johndoe -c dev 
#
 Developer platforms only

user-scanner -e johndoe@gmail.com -m github 
#
 Single module check

user-scanner -u johndoe -m github,instagram 
#
 Specific comma-separated modules

user-scanner -lu 
#
 List user categories & modules grid

user-scanner -le 
#
 List email categories & modules grid

### 5. Bulk File Scanning

Scan multiple targets from an input file (one target per line):

user-scanner -uf usernames.txt 
#
 Bulk username scan

user-scanner -ef emails.txt 
#
 Bulk email scan

### 6. Report Exports, Options & Proxies

#
 Export results to PDF, JSON, or CSV

user-scanner -u johndoe -f pdf -o report.pdf
user-scanner -u johndoe -f json -o results.json

#
 Verbose URL reporting and show all results (including not found)

user-scanner -u johndoe -v --all

#
 Rotate proxies with pre-scan validation check

user-scanner -u johndoe -P proxies.txt --validate-proxies

### 7. AI & LLM Agent Integration (MCP Server)

Connectuser-scannerdirectly to AI coding assistants and LLM platforms via theModel Context Protocol (MCP). This enables AI agents (Claude Desktop, Cursor, Antigravity, Open-WebUI) to autonomously investigate handles and emails, pivot on exposed profiles, and analyze digital footprints.

#### Starting the Server

#
 Start the MCP server over standard I/O (stdio)

user-scanner-mcp

#
 Optional: Enable verbose logging to stderr

user-scanner-mcp -v

#### MCP Client Configuration

Adduser-scannerto your client configuration (e.g.claude_desktop_config.jsonormcp_config.json):

{
 
"mcpServers"
: {
 
"user-scanner"
: {
 
"command"
: 
"
user-scanner-mcp
"

 }
 }
}

#### Exposed AI Tools

Tool

Description

Capabilities

scan_username

Deep username OSINT & profile enrichment across platforms

Targeted scans (
category
, 
module
), recursive 
cross_scan
, proxy injection, loudness toggles

scan_email

Deep email verification & account discovery across platforms

Target scoping, automated link pivoting (
cross_scan
), custom proxies, loudness toggles

list_available_modules

Dynamic catalog & module discovery

Allows AI agents to query all supported platforms and categories dynamically

## 📚 Documentation Hub

Explore detailed documentation guides in thedocs/directory:

* 📋CLI Flags Reference— Complete breakdown of every CLI flag and option.
* 🔀Cross-Scan & Pivoting Guide— In-depth guide to multi-pass cross-scan reconnaissance.
* 🔀Pattern Syntax Guide— Wildcard and permutation patterns for username generation.
* 🐍Library Mode Guide— Calling the Python engine programmatically from your own scripts.
* 🌐Proxy & Network Guide— Proxy rotation formats, health checks, and regional VPN troubleshooting.
* 🖼️Media & Output Gallery— Video demonstrations, terminal recordings, and screenshot previews.

## 🐍 Python Library Mode

Integrate the User Scanner engine directly into your Python scripts:

import
 
asyncio

from
 
user_scanner
.
core
 
import
 
engine

from
 
user_scanner
.
email_scan
.
shopping
 
import
 
etsy

async
 
def
 
main
():
 
# Engine validates target against module and returns Result object

 
result
 
=
 
await
 
engine
.
check
(
etsy
, 
"test@gmail.com"
)
 
print
(
result
.
to_json
())

asyncio
.
run
(
main
())

💡For complete Python API documentation and batch category checking examples, seedocs/USAGE.md.

## 💖 Support the Project

Web platforms constantly update authentication flows. Maintaining over 455+ scan modules requires around-the-clock commitment to keep the suite reliable and free for the cybersecurity community.

Ifuser-scannerhas saved you hours of manual pivoting or aided your investigations, consider supporting the project:

👉Sponsor on GitHub

### Project Sponsors

Huge thanks to our amazing sponsors who support the ongoing development ofuser-scanner!

@soxoj

@hienyimba

@InDieTasten

## 📜 Contributing

We welcome community contributions! Please read ourContributing Guidelinesbefore opening a PR or submitting new scan modules.

## ⚠️Disclaimer

This tool is provided strictly foreducational purposes,authorized security research, anddefensive OSINT investigations. The developers assume no liability and are not responsible for any misuse, unintended consequences, or legal actions resulting from the deployment of this software.