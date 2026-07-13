---
title: 'GitHub - tiliondev/fortress: Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change. · GitHub'
url: https://github.com/tiliondev/fortress
site_name: tldr
content_file: tldr-github-tiliondevfortress-stealth-chromium-engine-t
fetched_at: '2026-07-13T12:27:09.035285'
original_url: https://github.com/tiliondev/fortress
date: '2026-07-13'
description: Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change. - tiliondev/fortress
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 tiliondev

 

/

fortress

Public

* NotificationsYou must be signed in to change notification settings
* Fork20
* Star341

 
 
 
 
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

87 Commits
87 Commits
.github
.github
 
 
build
build
 
 
docs
docs
 
 
examples
examples
 
 
fonts
fonts
 
 
mcp
mcp
 
 
packaging
packaging
 
 
patches
patches
 
 
sdk
sdk
 
 
tools
tools
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.lycheeignore
.lycheeignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CHROMIUM_VERSION
CHROMIUM_VERSION
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
llms.txt
llms.txt
 
 
View all files

## Repository files navigation

### One browser engine to rule them all

Stealth Chromium engine

 
 
 

 

 

 

Fortress is a stealth Chromium engine that stops your scrapers and browser agents from getting blocked, with one line of code change.Bot detectors flag automation by reading the browser fingerprint; Fortress corrects that fingerprint inside Chromium's C++, so the browser presents as an ordinary Chrome install. Scrapers finish their runs, agents reach the pages they were sent to, and CreepJS, Sannysoft, BrowserScan, and live Cloudflare Turnstile all read it as human. Point your existing Playwright or Puppeteer at Fortress over CDP, and nothing else in your code changes.

Blink · V8 · BoringSSLpatched in-tree ·ANGLE / D3D11-backed WebGL ·JA3/JA4-coherentTLS ·monthlyupstream rebase ·reproducible, gauntlet-gatedreleases

### 34

single-surface
C++ patches

### 0%

CreepJS
headless / stealth

### [native code]

across every
realm

### BSD-3

open engine,
rebuild it yourself

Unedited capture of the Fortress binary in a real window: it clears a liveCloudflarechallenge, turnsbot.sannysoft.comall green, then readsBrowserScan“Normal”. Reproduce withtools/gauntlet.py.

#### Native-code parity

Every spoofed getterisa C++ getter:toStringreturns[native code],realm-invariantacross main frame, iframes, and Web Workers.

#### Drop-in CDP

nodriver-styleraw CDP on:9222, with noRuntime.enableleak. Keep Playwright, Puppeteer, or any CDP client; swap the browser, keep your code.

#### Clears the gauntlet

0% headlesson CreepJS; Sannysoft, BrowserScan, and live Cloudflare Turnstile cleared, all as a stock Chrome install.

#### Auditable patches

34 small single-purpose diffs inpatches/. Read one in a minute; rebuild the engine with one script.

#### Coherent by construction

Real V8, Blink, and BoringSSL keep engine, user-agent, andJA3/JA4 TLS shapein agreement: a Windows persona on a matching stack.

#### Tunable persona

One binary, acoherence-checkedWindows identity;--uxr-*switches override any surface: GPU, screen, timezone, hardware, Client-Hints.

## What's new — 151.0.7908.0 · Engine Refresh

Released.Per-launch coherent personas, hardened.

* Per-locale keyboard(QWERTY / QWERTZ / AZERTY) ·per-persona media devices· a fulldelivery-paritycoherence pass.
* Platform ↔ GPU ↔ timezone ↔ language ↔ voices ↔ keyboard move asone coherent real device— on every launch, from a single binary.
* Native-code parity(toString()stays[native code]),realm-invariant(main / worker / iframe) — coherence compiled into the browser, not patched in JavaScript.

pip install -U tilion-fortress 
#
 or: docker run --rm -p 9222:9222 tilion/fortress:latest

→ full release notes

## Contents

What it is
 · 
Quick start

what it is, install, first script, AI-agent setup

The Fortress MCP

29 stealth-browser tools for AI agents (Beta)

Why patch the engine, not the page

the self-revealing-JS thesis + the three detection layers

How Fortress compares

vs puppeteer-stealth · Camoufox · CloakBrowser · closed vendors

Proof: live-detector results

CreepJS / Sannysoft / BrowserScan / Cloudflare, with screenshots

Configure the persona

the 
--uxr-*
 fingerprint surface

Works with your stack

browser-use · Crawl4AI · Stagehand · LangChain

Build & verify

reproduce from source, verify provenance

Reference

troubleshooting · FAQ · roadmap · repo layout

## What it is

Fortress is a Chromium fork that spoofs the browser fingerprint from inside the engine. The surfaces bot detectors read (canvas, WebGL, audio, fonts, navigator, and about thirty more) are corrected in Chromium'sC++, with no JavaScript patch layer sitting on top for a page to catch.

It ships as an ordinary browser binary that exposes a CDP endpoint. Point Playwright, Puppeteer, or any CDP client at it and your existing automation runs unchanged.

A JavaScript stealth patch leaves an extra layer the page can find:.toString()shows the override's source, and re-grabbing the same primitive from an iframe or worker reaches past it. Fortress corrects the surface in the engine instead, sonavigator.vendorresolves to the real C++ getter, reports[native code], and reads the same from every realm. A page inspecting itself sees stock Chromium. That is why your automation gets through where it used to get flagged, and whatever blocking is left traces to your proxies and behavior rather than the browser.Why patch the engine, not the pagecovers the detection mechanics in full.

from
 
tilion_fortress
 
import
 
Fortress

from
 
playwright
.
sync_api
 
import
 
sync_playwright

with
 
Fortress
() 
as
 
f
: 
# launches the stealth engine on a CDP endpoint

 
with
 
sync_playwright
() 
as
 
p
:
 
browser
 
=
 
p
.
chromium
.
connect_over_cdp
(
f
.
cdp_url
)
 
page
 
=
 
browser
.
new_page
()
 
page
.
goto
(
"https://bot.sannysoft.com"
)
 
page
.
screenshot
(
path
=
"all-green.png"
)

import
 
{
 
Fortress
 
}
 
from
 
"tilion-fortress"
;

import
 
{
 
chromium
 
}
 
from
 
"playwright"
;

const
 
f
 
=
 
await
 
Fortress
.
launch
(
)
;
 
// stealth engine on a CDP endpoint

const
 
browser
 
=
 
await
 
chromium
.
connectOverCDP
(
f
.
cdpUrl
)
;

const
 
page
 
=
 
await
 
browser
.
newPage
(
)
;

await
 
page
.
goto
(
"https://browserscan.net"
)
;

await
 
browser
.
close
(
)
;

await
 
f
.
close
(
)
;

### The 12-second tour

One loop, all real captures: passesCreepJS / Sannysoft / BrowserScan / rebrowser→ scrapes structured data over CDP → clearsAkamaion aa.com · lowes · macys · kohls (same residential IP).

### Real scraping, fully headless

Unedited captures of the Fortress engine driven over CDP. No stealth plugins, no JS patches: the fingerprint is corrected in the binary. Reproduce any of these withexamples/scrape_demos.py.

Structured extraction: records build into typed JSON as each item is read.

Auto-pagination
: 30 quotes across 3 pages.

Deep detail crawl
: UPC · price · tax · stock · reviews.

### Clears real Akamai — before / after

Same residential IP, same site (aa.com· Akamai Bot Manager). A stock/headless browser getsAccess Denied(Reference #); Fortress loads the real page and Akamai issues its_abcksensor cookie — the Bot Manager accepts it as a real browser. The variable is thefingerprint, not the IP.

lowes.com
 · blocked → cleared

macys.com
 · blocked → cleared

kohls.com
 · blocked → cleared

Not a one-site fluke — same before/after on major Akamai-protected retailers, every run from the same residential IP.

## Quick start

#
 Python / Node: prebuilt native binary auto-fetched (Linux x64 & Windows x64), SHA-256 verified

pip install tilion-fortress
npm install tilion-fortress

#
 Any OS via Docker: raw CDP on :9222 (~302 MB pull / 851 MB on disk, stripped single-layer)

docker run --rm -p 9222:9222 tilion/fortress:latest

#
 Portable bundle (extract-and-run, like a Chromium snapshot)

tar xzf tilion-fortress-linux-x64.tar.gz 
#
 Linux

./tilion-fortress/tilion --headless=new --remote-debugging-port=9222 --user-data-dir=/tmp/p

#
 Debian / Ubuntu

sudo apt install ./tilion-fortress_151.0.7908.0_amd64.deb 
&&
 tilion https://example.com

Tip

The SDK ships the compiled buildpluspatches/, so you can rebuild the engine yourself and verify every surface correction against the source. Downloads are SHA-256-verified against the releaseSHA256SUMSautomatically.

### Versions

Fortress ships ontwo Chromium bases— pick your trade-off between blend-in and currency:

Channel

Chromium

When to use

stable
 
(default)

149

Recommended — matches the Chrome version the mass of real users run, so it blends in best

latest

151

Newest engine (reports a version slightly ahead of stable)

Fortress
().
start
() 
# Python: stable (149) by default

Fortress
(
channel
=
"latest"
).
start
() 
# opt into 151

await
 
Fortress
.
launch
(
)
;
 
// Node: stable (149) by default

await
 
Fortress
.
launch
(
{
 
channel
: 
"latest"
 
}
)
;

docker run --rm -p 9222:9222 tilion/fortress:149 
#
 or :151

#
 or set FORTRESS_CHANNEL=latest for either SDK

Native binaries:Linux x64(both versions) +Windows x64(151); Windows-149 and macOS run via the Docker image.

### Drop it into your AI agent

Fortress is the browser your agent drives: raw CDP on:9222, no stealth plugins to wire up. There are two ways in.

Option 1: open it pre-loaded in a chat assistant.One click; it reads ourAGENTS.mdand walks you through the whole setup:

 
 
 

Option 2: Copy for agent (everything, to your clipboard).Hit the copy icon at thetop-right of the boxbelow. It puts theentiresetup context on your clipboard: what it is, install, connect, persona, and rules, all ofAGENTS.mdcondensed. Paste it into Cursor, Claude Code, Copilot, ChatGPT, or any agent and it takes it from there:

You're setting up Fortress, an open-source STEALTH Chromium engine, for browser automation.
It corrects the browser fingerprint (canvas, WebGL, audio, fonts, navigator, +30 more) in Chromium's
C++ and exposes raw CDP on http://localhost:9222, a drop-in for Playwright/Puppeteer. Do NOT add
puppeteer-stealth or any JS fingerprint patching (it self-reveals and undoes Fortress).

LAUNCH (pick one; all expose CDP on http://localhost:9222):
 Docker: docker run -d --rm -p 9222:9222 tilion/fortress:latest
 Python: pip install tilion-fortress then from tilion_fortress import Fortress; f=Fortress(); f.start()
 Node: npm install tilion-fortress then import {Fortress} from "tilion-fortress"; const f=await Fortress.launch()

CONNECT (keep my existing automation code):
 Playwright(py): browser = p.chromium.connect_over_cdp("http://localhost:9222")
 Playwright(js): const browser = await chromium.connectOverCDP("http://localhost:9222")
 Puppeteer(js): const browser = await puppeteer.connect({ browserURL: "http://localhost:9222" })
 browser-use / Crawl4AI / Stagehand / LangChain: point their CDP endpoint at http://localhost:9222

PERSONA (optional; default is a coherent Windows identity). Override any surface with --uxr-* flags:
 --uxr-timezone=America/New_York --uxr-hw-concurrency=16 --uxr-languages=en-US,en

RULES:
 1) Drive over raw CDP (:9222); don't spawn chromedriver.
 2) Never pass --user-agent (use --uxr-ua-*); it desyncs UA vs UA-Client-Hints.
 3) No puppeteer-stealth / undetected-chromedriver / JS fingerprint patches.
 4) Blocked ~90% = my IP (datacenter), not the fingerprint. Use a residential/mobile proxy, then retry.

Now walk me through launching Fortress and wiring my automation to it.
Full guide: https://github.com/tiliondev/fortress/blob/main/AGENTS.md

## The Fortress MCP — stealth browsing as agent toolsBeta

Raw CDP is for code you write. TheFortress MCPis for agents that calltools: aModel Context Protocolserver that hands Claude, Cursor, or any MCP client a stealth browser, so the moment a fetch is blocked it just calls a tool and gets the page.29 tools, local and free—fetch_protected_page,extract_page,crawl_site,recon_site_apis,search_web,run_browser_task,save_profile,get_stealth_cdp_endpoint, and more.

Real, dated run againststockx.com(PerimeterX). A stock browser getsHTTP 403 — “Access denied”; an agent with the Fortress MCP returns clean JSON — same site, same prompt. Reproduce it from the framework repo.

### Set it up in 30 seconds

Two runners — pick one.npxneeds Python on PATH;pipinstalls it directly:

pip install 
"
tilion[mcp]
"
 
#
 command: tilion-mcp

#
 —or, zero-install—

npx -y tilion-mcp 
#
 auto-runs the server via uv (no global install)

Claude Desktop— Settings → Developer →Edit Config(claude_desktop_config.json):

{ 
"mcpServers"
: { 
"fortress"
: { 
"command"
: 
"
tilion-mcp
"
 } } }

Prefer npx? Use"command": "npx", "args": ["-y", "tilion-mcp"]. Restart Claude, and thefortresstools appear.

Claude Code(CLI) — one line:

claude mcp add fortress -- tilion-mcp 
#
 or: claude mcp add fortress -- npx -y tilion-mcp

Cursor(~/.cursor/mcp.json) ·Cline / Windsurf(VS Code → MCP servers) — same block:

{ 
"mcpServers"
: { 
"fortress"
: { 
"command"
: 
"
tilion-mcp
"
 } } }

Then just ask your agent —“get the price off this StockX page”— and it callsfetch_protected_pageon its own.

### What the agent gets

tools

Get blocked pages

fetch_protected_page
 · 
read_page
 · 
get_page_html
 · 
search_web

Structured data

extract_page
 (schema-aware) · 
extract_document
 (PDF/DOCX/XLSX)

Whole sites

crawl_site
 (auto-SPA) · 
recon_site_apis
 (find the private JSON API)

Drive a page

page_elements
 · 
click_button
 · 
fill_field
 · 
press_key
 · 
wait_for
 · 
evaluate_js

Multi-step flows

run_browser_task
 (login, paginate, infinite-scroll, checkout, …)

Capture / auth

screenshot_page
 · 
save_page
 · 
download_file
 · 
save_profile
 / 
load_profile

Bring your own

get_stealth_cdp_endpoint
 → a CDP url for Playwright / Puppeteer / browser-use

Tools are annotated (reads auto-approve, writes gate),pre-warmedon startup (~100 ms first call), concurrency-safe, and timeout- and SSRF-guarded. A hosted endpoint withresidential egress is coming soon.

→ Full 29-tool table, benchmarks, and the agent skill:mcp/

## Why patch the engine, not the page

The usual approach patchesnavigator.webdriver, spoofs the WebGL vendor, and overridesnavigator.pluginsfrom script. CreepJS and similar detectors still flag it, and the reason isstructural, not one more property left uncovered. A JavaScript spoof is a function standing where a native one belongs. Detectors set the returned value aside and interrogate whether the thing returning it is native:

The tell

Why it catches a JS spoof

toString
 self-reveal

A native method stringifies to 
function get vendor() { [native code] }
; an override stringifies to its own source, so one 
.toString()
 catches it.

Descriptor and 
hasOwnProperty

getOwnPropertyDescriptor
 exposes redefined props, and 
hasOwnProperty('toString')
 returns 
true
 on a tampered function where a native one returns 
false
.

failsTypeError

Native getters throw a specific 
TypeError
 on the wrong 
this
; a naive shim stays quiet, and the silence is the signal.

Realm re-acquisition is the one that defeats every main-world patch. A detector grabs a pristine primitive from another realm and turns it on your function:

const
 
iframe
 
=
 
document
.
createElement
(
'iframe'
)
;
 
document
.
body
.
appendChild
(
iframe
)
;

const
 
realToString
 
=
 
iframe
.
contentWindow
.
Function
.
prototype
.
toString
;

realToString
.
call
(
navigator
.
__lookupGetter__
(
'vendor'
)
)
;
 
// returns your source code. Caught.

Your main-world patch lives in a different realm from that iframe. The same trap fires from a Web Worker, a thread your main-thread shim runsbesiderather thaninside.

Fortress has no such layer. The getter fornavigator.vendoristhe C++ getter: it reports[native code]because it is native code, identical across every realm. Camoufox puts it well:"there is no JavaScript hijacking to be detected."Fortress applies the same idea toV8 and Blinkin place of Gecko.

### The three layers of bot detection, and where Fortress fits

Modern anti-bots (Cloudflare, DataDome, Kasada, HUMAN, Akamai) read three structurally different surfaces, in three separate places. One tool rarely fixes all three:

Layer

The tells

Where the fix lives

Fortress

A: driver / binary artifacts

cdc_
 ChromeDriver vars, WebDriver protocol surface

Drive raw CDP, skip chromedriver

 built to be driven this way

B: CDP side-effects

Runtime.enable
 leaks via sourceURL + init-script footprints, however clean the binary is

The control / CDP-client layer: hold back 
Runtime.enable
, use 
Runtime.addBinding
 + isolated worlds

 no leak (verified)

C: fingerprint surface

canvas, WebGL, audio, fonts, navigator, across main frame, iframes, workers

The engine (C++), because JS overrides self-reveal

 
this is Fortress

Fortress is theLayer-C engine, built to be driven so A and B hold too. The binary alone leaves the CDP channel open. That part is on the control layer, and pretending otherwise is how you get caught.

## How Fortress compares

Stock Playwright

puppeteer-extra-stealth

undetected-chromedriver

Camoufox

CloakBrowser

Fortress

Spoof layer

none

JS injection

CDP/config patch

C++ engine

C++ engine

C++ engine

toString
 yields 
[native code]

n/a

n/a

Survives realm re-acquisition (iframe/worker)

No 
Runtime.enable
 leak

Engine = Chrome / 
V8
 (majority traffic)

 Firefox

Coherent Chromium TLS shape

 Firefox

Fully open-source engine

 latest major paywalled

Published, auditable patch series

n/a

n/a

n/a

 binary only

Reproducible from-source build

n/a

n/a

n/a

States its own limits

n/a

n/a

n/a

Fortress builds on real prior art:fingerprint-chromium,ChromiumFish, and CloakBrowser came first, and commercial vendors (Multilogin, Kameleo, GoLogin, AdsPower, Browserbase, Surfsky) recompile Chromium behind closed source. Most of that work stays closed: the paywalled forks hand you a binary and ask you to trust it, and the vendors keep their patches in-house.

Fortress goes the other way, becausea stealth engine only stays useful when the people relying on it can see how it works.Every surface correction lives inpatches/as a small, single-purpose diff you can read in a minute, and the whole engine rebuilds from source with one script. When a detector finds a new tell, you trace the fix, patch it, and send it back. That feedback loop is the point, and it only works while the engine stays open enough to read, extend, and rebuild.

## Proof: live-detector results

Reproduce any row withtools/gauntlet.py --bundle ./tilion-fortress. Verified against live detectors; re-run dated indocs/GAUNTLET_RESULTS.md.

Suite

Stock Chromium

Fortress

CreepJS

flagged headless

0% headless · 0% stealth
, worker signals coherent

bot.sannysoft.com

red rows

0 failed
 · WebDriver Advanced passed · WebGL = NVIDIA RTX 3060 / ANGLE D3D11

browserscan.net

bot detected

“No bots detected, could be a human”

rebrowser bot-detector

Runtime.enable
 LEAK

no leak
 · 
webdriver=false
 · clean init-scripts (raw CDP)

Cloudflare Turnstile

blocked

bypassed
: a human click cleared a live challenge (headed, datacenter IP)

Proof: real, unedited screenshots

BrowserScan

CreepJS

Cloudflare

## Configure the persona

The binary carrieszero brand strings; the launcher applies a coherent default Windows persona. Override any surface with--uxr-*switches, or setTILION_NO_DEFAULTS=1for a bare launch.

--uxr-platform / --uxr-ua-platform / --uxr-ua-os / --uxr-ua-arch / --uxr-ua-bitness
--uxr-ua-platform-version / --uxr-ua-brand / --uxr-hw-concurrency / --uxr-device-memory
--uxr-webgl-vendor / --uxr-webgl-renderer / --uxr-webgl-fullparams
--uxr-canvas-seed / --uxr-audio-seed / --uxr-timezone / --uxr-languages
--uxr-screen-width / --uxr-screen-height / --uxr-webrtc-policy=disable_non_proxied_udp

Env var

Purpose

TILION_NO_DEFAULTS=1

Skip the default persona (bare launch)

TILION_TZ
 / 
TILION_LANG

Quick timezone / language override

Note

The persona rides on the command line today.The--uxr-*switches are world-readable via/proc/<pid>/cmdline, so it's one persona per launch and visible to other processes on the host. TheMaskConfigruntime lands next: it delivers the persona over IPC and lifts the one-per-process limit (seewhat's next).

## Works with your stack

Fortress exposes raw CDP on:9222, so it drops in under anything that speaks Playwright, Puppeteer, or CDP.

Framework

Connect via

browser-use
 (~70k stars)

cdp_url="http://localhost:9222"

Crawl4AI
 (~58k stars)

CDP endpoint

Stagehand
 (~21k stars)

connectOverCDP

LangChain
 Playwright toolkit

Playwright CDP

Playwright / Puppeteer
 (Python & JS)

connect_over_cdp
 / 
connect

from
 
playwright
.
sync_api
 
import
 
sync_playwright

with
 
sync_playwright
() 
as
 
p
:
 
browser
 
=
 
p
.
chromium
.
connect_over_cdp
(
"http://localhost:9222"
) 
# Fortress under the hood

## Build & verify

### Reproduce from source

export
 CHROMIUM_VERSION=
$(
cat CHROMIUM_VERSION
)

build/build.sh 
#
 depot_tools, sync the tag, apply patches, gn gen, ninja

build/rebase-monthly.sh 152.0.XXXX.0 
#
 bump + 3-way apply + rebuild + gauntlet-gate

Output:out/Fortress/chrome. The fork is 34 small single-surface patches (patches/), so most re-apply cleanly across upstream releases; the gauntlet then gates the release on any regression.

Platform

Status

Linux x64 (native) · 
Windows x64 (native)
 · any OS via Docker

 
shipping

Code-signed installers · macOS 
.app
 · 
linux/arm64

in progress

### Verify it's really ours

Fortress ships from four official channels. Treat anything else as untrusted:

Official source

Source

github.com/tiliondev/fortress

Docker

tilion/fortress

Python

tilion-fortress

Node

tilion-fortress

Verify a download.Every release shipsSHA256SUMS, and thepip/npmSDKs run this for you on install:

BASE=https://github.com/tiliondev/fortress/releases/download/v151.0.7908.0
curl -LO 
$BASE
/tilion-fortress-linux-x64.tar.gz
curl -Ls 
$BASE
/SHA256SUMS 
|
 sha256sum -c --ignore-missing 
#
 -> OK

Verify the Docker imageby digest (not just the tag):

docker pull tilion/fortress:151.0.7908.0
docker inspect --format 
'
{{index .RepoDigests 0}}
'
 tilion/fortress:151.0.7908.0

#
 compare the printed sha256:... against the digest in the GitHub Release notes

Or trust nothing and rebuild it.The whole fork is 34 readable patches inpatches/;build/build.shreproduces the binary from Chromium source, so you can diff what you built against what we ship.

## Reference

Troubleshooting

Still blocked on Cloudflare, DataDome, or Kasada.Most of the time this is yourIP, not your fingerprint: a datacenter range gets flagged before any page script runs. Route egress through residential or mobile proxies and retry; if it clears, the fingerprint was fine.

The fingerprint looks off on a Linux host.The default persona is Windows, but the TLS shape and some OS-facing signals follow the machine underneath. Match the persona to your egress OS, or set the relevant--uxr-*flags so the OS story agrees with where the traffic leaves from.

macOS pulls a Docker image.Native Linux + Windows binaries ship today; macOS still runs Fortress through the official Docker image (tilion/fortress). Install Docker Desktop, or run on Linux/Windows x64 for the native binary.

The persona shows up in/proc/<pid>/cmdline.The--uxr-*flags are readable by other processes on the host, one persona per launch. Until the runtimeMaskConfiglands, keep one persona per process and avoid sharing the host with untrusted code.

A detector flags something the gauntlet passes.Detection moves. Confirm you're on the current Chromium rebase, then open an issue with the test page. That page becomes the next patch.

FAQ

Is this legal?Fortress is a browser engineering project for legitimate automation, testing, and scraping of publicly available data. Respect each site's ToS and the law in your jurisdiction.

Is it really free?Yes. BSD-3, fully open, and self-hostable. The patch series is published, so you can build the current engine from source yourself.

Why not just use puppeteer-stealth or undetected-chromedriver?They patch the JS/CDP layerafterthe page can inspect the browser, so they self-reveal viatoStringand realm re-acquisition. Fortress moves the spoof into C++, where the page finds native code. (See "Why patch the engine, not the page.")

How is this different from Camoufox?Same C++-interception idea. Camoufox forks Firefox (~3% of traffic, a standing anomaly) while Fortress forks Chromium and V8 (the majority engine), so a Chrome user-agent is coherent by construction.

Will it pass everything forever?No. Detection keeps moving, so we ship a dated, reproducible gauntlet and a monthly Chromium rebase; you can always see exactly what passes today.

Roadmap

* Runtime JSON config into a C++MaskConfig(one binary, many coherent fingerprints, nothing on the command line)
* First-party MCP server plus Puppeteer / raw-CDP SDKs (drop-in for AI agents)
* Code-signed Windows.exeand macOS.app
* linux/arm64Docker image
* Migratepatches/to Brave-stylechromium_src/overrides
* Published reCAPTCHA v3 / DataDome / Kasada benchmark rows (dated, reproducible)

Repo layout

patches/ 34 per-surface C++ patches (+ series), the source of truth for the fork
build/ args.gn, build.sh, apply-patches.sh, rebase-monthly.sh, windows/, macos/
packaging/ tilion launcher, fonts.conf, Dockerfile, .deb + bundle builders
fonts/ 33 metric-compatible Windows-named fonts (incl. color emoji)
sdk/ python + node (tilion-fortress) prebuilt-binary SDKs
tools/ gauntlet.py, the CreepJS / Sannysoft / BrowserScan CI gate
docs/ GAUNTLET_RESULTS, BUILD_NATIVE, BENCHMARK

### Contributing

Found a detection vector or a leak we missed? Open an issue with a reproducible test page. A page that reliably flags Fortress is the most valuable thing you can send. It becomes the next patch. Two house rules: every capability claim ships with a command that reproduces it, and every limit is written down.The word "undetectable" stays out of the repo.

### License

BSD-3-Clause for the Fortress patches and tooling (matching Chromium). Chromium and the bundled fonts retain their own licenses; seeLICENSEandNOTICE. The patch series is published, so you can audit and rebuild the engine yourself.

### What's next

Important

v2: MaskConfig runtime personas.AnIPC-delivered, seed-driven persona graphfeeding a process-global C++MaskConfigsingleton:thousands of coherence-invariant fingerprints from a single binary,per-BrowserContextidentity isolation, andzero command-line footprint. The rest is on theroadmap.

### Staying current

Detection keeps moving, so a stealth engine is only as good as its last rebase. Fortress tracks the latest Chromium monthly, re-runs the full gauntlet, and ships a patch whenever a detector finds a new tell, so what you run keeps matching what a real Chrome install looks like.Watch the releasesto follow thev2MaskConfig work, orstar the repoif it's useful to you.

Stealth you can read, rebuild, and run yourself.

## About

Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change.

tilion.dev/

### Topics

 python

 testing

 crawler

 automation

 scraping

 selenium

 chromium

 web-scraping

 fingerprinting

 anti-bot

 stealth

 webscraping

 web-crawling

 browser-automation

 data-scraping

 bot-detection

 headless-chrome

 puppeteer

 headless-browser

 playwright

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

341

 stars
 

### Watchers

2

 watching
 

### Forks

20

 forks
 

 Report repository

 

## Releases2

Fortress 149.0.7827.232 (stable)

 Latest

 

Jul 4, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python68.4%
* JavaScript12.5%
* Shell11.7%
* PowerShell3.6%
* Dockerfile1.8%
* Batchfile1.0%
* Makefile1.0%