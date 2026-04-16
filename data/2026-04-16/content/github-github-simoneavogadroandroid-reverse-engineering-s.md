---
title: 'GitHub - SimoneAvogadro/android-reverse-engineering-skill: Claude Code skill to support Android app''s reverse engineering · GitHub'
url: https://github.com/SimoneAvogadro/android-reverse-engineering-skill
site_name: github
content_file: github-github-simoneavogadroandroid-reverse-engineering-s
fetched_at: '2026-04-16T19:59:47.402046'
original_url: https://github.com/SimoneAvogadro/android-reverse-engineering-skill
author: SimoneAvogadro
description: Claude Code skill to support Android app's reverse engineering - SimoneAvogadro/android-reverse-engineering-skill
---

SimoneAvogadro

 

/

android-reverse-engineering-skill

Public

* NotificationsYou must be signed in to change notification settings
* Fork245
* Star2.1k

 
 
 
 
master
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

9 Commits
9 Commits
.claude-plugin
.claude-plugin
 
 
plugins/
android-reverse-engineering
plugins/
android-reverse-engineering
 
 
.gitattributes
.gitattributes
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Android Reverse Engineering & API Extraction — Claude Code skill

A Claude Code skill that decompiles Android APK/XAPK/JAR/AAR files andextracts the HTTP APIsused by the app — Retrofit endpoints, OkHttp calls, hardcoded URLs, authentication patterns — so you can document and reproduce them without the original source code.

## What it does

* DecompilesAPK, XAPK, JAR, and AAR files using jadx and Fernflower/Vineflower (single engine or side-by-side comparison)
* Extracts and documents APIs: Retrofit endpoints, OkHttp calls, hardcoded URLs, auth headers and tokens
* Traces call flowsfrom Activities/Fragments through ViewModels and repositories down to HTTP calls
* Analyzesapp structure: manifest, packages, architecture patterns
* Handles obfuscated code: strategies for navigating ProGuard/R8 output

## Requirements

Required:

* Java JDK 17+
* jadx(CLI)

Optional (recommended):

* VineflowerorFernflower— better output on complex Java code
* dex2jar— needed to use Fernflower on APK/DEX files

Seeplugins/android-reverse-engineering/skills/android-reverse-engineering/references/setup-guide.mdfor detailed installation instructions.

## Installation

### From GitHub (recommended)

Inside Claude Code, run:

/plugin marketplace add SimoneAvogadro/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill

The skill will be permanently available in all future sessions.

### From a local clone

git clone https://github.com/SimoneAvogadro/android-reverse-engineering-skill.git

Then in Claude Code:

/plugin marketplace add /path/to/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill

## Usage

### Slash command

/decompile path/to/app.apk

This runs the full workflow: dependency check, decompilation, and initial structure analysis.

### Natural language

The skill activates on phrases like:

* "Decompile this APK"
* "Reverse engineer this Android app"
* "Extract API endpoints from this app"
* "Follow the call flow from LoginActivity"
* "Analyze this AAR library"

### Manual scripts

The scripts can also be used standalone:

#
 Check dependencies

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/check-deps.sh

#
 Install a missing dependency (auto-detects OS and package manager)

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/install-dep.sh jadx
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/install-dep.sh vineflower

#
 Decompile APK with jadx (default)

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh app.apk

#
 Decompile XAPK (auto-extracts and decompiles each APK inside)

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh app-bundle.xapk

#
 Decompile with Fernflower

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh --engine fernflower library.jar

#
 Run both engines and compare

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh --engine both --deobf app.apk

#
 Find API calls

bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/ --retrofit
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/ --urls

## Repository Structure

android-reverse-engineering-skill/
├── .claude-plugin/
│ └── marketplace.json # Marketplace catalog
├── plugins/
│ └── android-reverse-engineering/
│ ├── .claude-plugin/
│ │ └── plugin.json # Plugin manifest
│ ├── skills/
│ │ └── android-reverse-engineering/
│ │ ├── SKILL.md # Core workflow (5 phases)
│ │ ├── references/
│ │ │ ├── setup-guide.md
│ │ │ ├── jadx-usage.md
│ │ │ ├── fernflower-usage.md
│ │ │ ├── api-extraction-patterns.md
│ │ │ └── call-flow-analysis.md
│ │ └── scripts/
│ │ ├── check-deps.sh
│ │ ├── install-dep.sh
│ │ ├── decompile.sh
│ │ └── find-api-calls.sh
│ └── commands/
│ └── decompile.md # /decompile slash command
├── LICENSE
└── README.md

## References

* jadx — Dex to Java decompiler
* Fernflower — JetBrains analytical decompiler
* Vineflower — Fernflower community fork
* dex2jar — DEX to JAR converter
* apktool — Android resource decoder

## Disclaimer

This plugin is provided strictly forlawful purposes, including but not limited to:

* Security research and authorized penetration testing
* Interoperability analysis permitted under applicable law (e.g., EU Directive 2009/24/EC, US DMCA §1201(f))
* Malware analysis and incident response
* Educational use and CTF competitions

You are solely responsiblefor ensuring that your use of this tool complies with all applicable laws, regulations, and terms of service. Unauthorized reverse engineering of software you do not own or do not have permission to analyze may violate intellectual property laws and computer fraud statutes in your jurisdiction.

The authors disclaim any liability for misuse of this tool.

## License

Apache 2.0 — seeLICENSE

## About

Claude Code skill to support Android app's reverse engineering

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.1k

 stars
 

### Watchers

9

 watching
 

### Forks

245

 forks
 

 Report repository

 

## Releases

2

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Shell100.0%