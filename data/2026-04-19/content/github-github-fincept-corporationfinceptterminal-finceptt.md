---
title: 'GitHub - Fincept-Corporation/FinceptTerminal: FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment. · GitHub'
url: https://github.com/Fincept-Corporation/FinceptTerminal
site_name: github
content_file: github-github-fincept-corporationfinceptterminal-finceptt
fetched_at: '2026-04-19T11:34:37.477777'
original_url: https://github.com/Fincept-Corporation/FinceptTerminal
author: Fincept-Corporation
description: FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment. - Fincept-Corporation/FinceptTerminal
---

Fincept-Corporation



/

FinceptTerminal

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork864
* Star5.1k




 
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

814 Commits
814 Commits
.github
.github
 
 
docs
docs
 
 
fincept-qt
fincept-qt
 
 
images
images
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
fincept_icon.ico
fincept_icon.ico
 
 
funding.json
funding.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
setup.sh
setup.sh
 
 
updates.json
updates.json
 
 
View all files

## Repository files navigation

# Fincept Terminal






### Your Thinking is the Only Limit. The Data Isn't.

State-of-the-art financial intelligence platform with CFA-level analytics, AI automation, and unlimited data connectivity.

📥 Download·📚 Docs·💬 Discussions·💬 Discord·🤝 Partner

Equity Research

Portfolio

News

Node Editor

## About

Fincept Terminal v4is a pure native C++20 desktop application. It usesQt6for UI and rendering, embeddedPythonfor analytics, and delivers Bloomberg-terminal-class performance in a single native binary.

## Features

Feature

Description

📊
CFA-Level Analytics

DCF models, portfolio optimization, risk metrics (VaR, Sharpe), derivatives pricing via embedded Python

🤖
AI Agents

37 agents across Trader/Investor (Buffett, Graham, Lynch, Munger, Klarman, Marks…), Economic, and Geopolitics frameworks; local LLM support; multi-provider (OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama)

🌐
100+ Data Connectors

DBnomics, Polygon, Kraken, Yahoo Finance, FRED, IMF, World Bank, AkShare, government APIs, plus optional alternative-data overlays such as Adanos market sentiment for equity research

📈
Real-Time Trading

Crypto (Kraken/HyperLiquid WebSocket), equity, algo trading, paper trading engine, 16 broker integrations (Zerodha, Angel One, Upstox, Fyers, Dhan, Groww, Kotak, IIFL, 5paisa, AliceBlue, Shoonya, Motilal, IBKR, Alpaca, Tradier, Saxo)

🔬
QuantLib Suite

18 quantitative analysis modules — pricing, risk, stochastic, volatility, fixed income

🚢
Global Intelligence

Maritime tracking, geopolitical analysis, relationship mapping, satellite data

🎨
Visual Workflows

Node editor for automation pipelines, MCP tool integration

🧠
AI Quant Lab

ML models, factor discovery, HFT, reinforcement learning trading

## Installation

### Option 1 — Download Installer (Recommended)

Latest release:v4.0.2—View all releases

Platform

Download

Run

Windows x64

FinceptTerminal-Windows-x64-setup.exe

Run installer → launch
FinceptTerminal.exe

Linux x64

FinceptTerminal-Linux-x64.run

chmod +x
 → run installer

macOS Apple Silicon

FinceptTerminal-macOS-arm64.dmg

Open DMG → drag to Applications

### Option 2 — Quick Start (One-Click Build)

Clone and run the setup script — it installs all dependencies and builds the app automatically:

#
 Linux / macOS

git clone https://github.com/Fincept-Corporation/FinceptTerminal.git

cd
 FinceptTerminal
chmod +x setup.sh
&&
 ./setup.sh

# Windows — run from Developer Command
Prompt

for
 VS
2022

git clone https://github.com/Fincept-Corporation/FinceptTerminal.git

cd
 FinceptTerminal
setup.bat

The script handles: compiler check, CMake, Qt6, Python, build, and launch.

### Option 3 — Docker

#
 Pull and run

docker pull ghcr.io/fincept-corporation/fincept-terminal:latest
docker run --rm -e DISPLAY=
$DISPLAY
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 ghcr.io/fincept-corporation/fincept-terminal:latest

#
 Or build from source

git clone https://github.com/Fincept-Corporation/FinceptTerminal.git

cd
 FinceptTerminal
docker build -t fincept-terminal
.

docker run --rm -e DISPLAY=
$DISPLAY
 -v /tmp/.X11-unix:/tmp/.X11-unix fincept-terminal

Note:Docker is primarily intended for Linux. macOS and Windows require additional XServer configuration.

### Option 4 — Build from Source (Manual)

Versions are pinned.Use the exact versions below. Newer or older versions are unsupported and may fail to build or produce unstable binaries.

#### Prerequisites (exact versions)

Tool

Pinned Version

Notes

Git

latest

—

CMake

3.27.7

Download

Ninja

1.11.1

Download

C++ compiler

MSVC 19.38
 (VS 2022 17.8) /
GCC 12.3
 /
Apple Clang 15.0
 (Xcode 15.2)

C++20 required

Qt

6.8.3

Qt Online Installer

Python

3.11.9

python.org

Platform SDK

Win10 SDK 10.0.22621.0 / macOS SDK 14.0 (deploy 11.0+) / glibc 2.31+

—

#### Install Qt 6.8.3

Windows:Qt Online Installer → selectQt 6.8.3 > MSVC 2022 64-bit(install path:C:/Qt/6.8.3/msvc2022_64)

Linux:Qt Online Installer →Qt 6.8.3 > Desktop gcc 64-bit(install path:~/Qt/6.8.3/gcc_64).Orfor system packages, installqt6-base-dev qt6-charts-dev qt6-tools-dev qt6-base-private-dev libqt6websockets6-dev libgl1-mesa-dev— note system packages may be a different 6.x minor.

macOS:Qt Online Installer →Qt 6.8.3 > macOS(install path:~/Qt/6.8.3/macos)

#### Build (using CMake presets — recommended)

git clone https://github.com/Fincept-Corporation/FinceptTerminal.git

cd
 FinceptTerminal/fincept-qt

#
 Configure + build (pick your platform)

cmake --preset win-release
&&
 cmake --build --preset win-release
#
 Windows (Dev Cmd for VS 2022)

cmake --preset linux-release
&&
 cmake --build --preset linux-release
#
 Linux

cmake --preset macos-release
&&
 cmake --build --preset macos-release
#
 macOS

Debug variants:win-debug,linux-debug,macos-debug.

#### Build (manual — if presets can't resolve your Qt path)

#
 Windows (Developer Command Prompt for VS 2022)

cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release ^
 -DCMAKE_PREFIX_PATH=
"
C:/Qt/6.8.3/msvc2022_64
"

cmake --build build

#
 Linux

cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=
"
$HOME
/Qt/6.8.3/gcc_64
"

cmake --build build

#
 macOS

cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_OSX_DEPLOYMENT_TARGET=11.0 \
 -DCMAKE_PREFIX_PATH=
"
$HOME
/Qt/6.8.3/macos
"

cmake --build build

#### Run

./build/
<
preset
>
/FinceptTerminal
#
 Linux / macOS (preset build)

.
\b
uild
\<
preset
>
\F
inceptTerminal.exe
#
 Windows (preset build)

#### Troubleshooting

1. "Could not find Qt6 6.8.3"— verifyCMAKE_PREFIX_PATHpoints to the Qt 6.8.3 install, not 6.5/6.6/6.8.
2. MSVC version error— use VS 2022 17.8+ (MSVC 19.38+). Check withcl /?.
3. Need to unblock with a different Qt minor?Pass-DFINCEPT_ALLOW_QT_DRIFT=ON(local testing only — never for releases or CI).
4. Clean rebuild: deletebuild/<preset>/and re-run configure.

## What Sets Us Apart

Fincept Terminalis an open-source financial platform built for those who refuse to be limited by traditional software. We compete onanalytics depthanddata accessibility— not on insider info or exclusive feeds.

Recent builds also support optionalAdanos Market Sentimentconnectivity inData Sources → Alternative Data. When configured, Equity Research can surface cross-source retail sentiment snapshots across Reddit, X, finance news, and Polymarket. Without an active Adanos connection, the feature remains dormant and the rest of the app behaves exactly as before.

* Native performance— C++20 with Qt6, no Electron/web overhead
* Single binary— no Node.js, no browser runtime, no JavaScript bundler
* CFA-level analytics— complete curriculum coverage via Python modules
* 100+ data connectors— from Yahoo Finance to government databases
* Free & Open Source(AGPL-3.0) with commercial licenses available

## Roadmap

Timeline

Milestone

Shipped

Real-time streaming, 16 broker integrations, multi-account trading, PIN authentication, theme system

Q2 2026

Options strategy builder, multi-portfolio management, 50+ AI agents

Q3 2026

Programmatic API, ML training UI, institutional features

Future

Mobile companion, cloud sync, community marketplace

## Contributing

We're building the future of financial analysis — together.

Contribute:New data connectors, AI agents, analytics modules, C++ screens, documentation

* Contributing Guide
* C++ Contributing Guide
* Python Contributor Guide
* Report Bug
* Request Feature

## For Universities & Educators

Bring professional-grade financial analytics to your classroom.

* $799/monthfor 20 accounts
* Full access to Fincept Data & APIs
* Perfect for finance, economics, and data science courses
* CFA curriculum analytics built-in

Interested?Emailsupport@fincept.inwith your institution name.

University Licensing Details

## License

Dual Licensed: AGPL-3.0 (Open Source) + Commercial

### Open Source (AGPL-3.0)

* Free for personal, educational, and non-commercial use
* Requires sharing modifications when distributed or used as network service
* Full source code transparency

### Commercial License

* Required for business use or to access Fincept Data/APIs commercially
* Contact:support@fincept.in
* Details:Commercial License Guide

### Trademarks

"Fincept Terminal" and "Fincept" are trademarks of Fincept Corporation.

© 2025-2026 Fincept Corporation. All rights reserved.

### Your Thinking is the Only Limit. The Data Isn't.

⭐Star· 🔄Share· 🤝Contribute

## About

FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment.

fincept.in

### Topics

 python

 finance

 machine-learning

 opensource

 foss

 investing

 stock-market

 help-wanted

 stocks

 quantitative-finance

 investment

 financial-markets

 contributions-welcome

 bloomberg-terminal

 good-first-issue

 investment-research

### Resources

 Readme



### License

 View license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

5.1k

 stars


### Watchers

55

 watching


### Forks

864

 forks


 Report repository



## Releases25

Fincept Terminal v4.0.1

 Latest



Apr 15, 2026



+ 24 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.





## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors20

+ 6 contributors

## Languages

* Python63.4%
* C++36.1%
* CMake0.4%
* Shell0.1%
* Qt Script0.0%
* PowerShell0.0%
