---
title: 'GitHub - openclaw/openclaw-windows-node: Windows companion suite for OpenClaw - System Tray app, Shared library, Node, and PowerToys Command Palette extension · GitHub'
url: https://github.com/openclaw/openclaw-windows-node
site_name: github
content_file: github-github-openclawopenclaw-windows-node-windows-compa
fetched_at: '2026-06-04T12:02:18.117871'
original_url: https://github.com/openclaw/openclaw-windows-node
author: openclaw
description: Windows companion suite for OpenClaw - System Tray app, Shared library, Node, and PowerToys Command Palette extension - openclaw/openclaw-windows-node
---

openclaw

 

/

openclaw-windows-node

Public

* NotificationsYou must be signed in to change notification settings
* Fork156
* Star1.2k

 
 
 
 
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

955 Commits
955 Commits
.agents/
skills/
autoreview
.agents/
skills/
autoreview
 
 
.config
.config
 
 
.github
.github
 
 
docs
docs
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
DEVELOPMENT.md
DEVELOPMENT.md
 
 
GitVersion.yml
GitVersion.yml
 
 
LICENSE
LICENSE
 
 
NuGet.Config
NuGet.Config
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
build.ps1
build.ps1
 
 
global.json
global.json
 
 
installer.iss
installer.iss
 
 
openclaw-windows-node.slnx
openclaw-windows-node.slnx
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
run-app-local.ps1
run-app-local.ps1
 
 
View all files

## Repository files navigation

# 🦞 OpenClaw Windows Hub

A native Windows companion suite forOpenClaw- the AI-powered personal assistant.

Made with 🦞 love by Scott Hanselman and Molty

## Projects

This monorepo contains the Windows hub, shared client libraries, and CLI utilities:

Project

Description

OpenClaw.Tray.WinUI

System tray application (WinUI 3) for quick access to OpenClaw

OpenClaw.Shared

Shared gateway client library

OpenClaw.Cli

CLI validator for WebSocket connect/send/probe using tray settings

## 🚀 Quick Start

End-user installer?Download the latest stable x64 or ARM64 installer from theOpenClaw Windows docs, or seedocs/SETUP.mdfor step-by-step installation (no build required).

Managed WSL gateway?Local setup creates a locked-down app-ownedOpenClawGatewaydistro. Seedocs/WSL_GATEWAY_ADMIN.mdfor editingopenclaw.jsonas theopenclawuser and using root for protected-file administration.

Direct downloads from the latest OpenClaw release:

* OpenClawCompanion-Setup-x64.exe
* OpenClawCompanion-Setup-arm64.exe
* OpenClawCompanion-SHA256SUMS.txt

### Prerequisites

* Windows 10 (20H2+) or Windows 11
* .NET 10.0 SDK -https://dotnet.microsoft.com/download/dotnet/10.0
* Windows 10 SDK (for WinUI build) - install via Visual Studio or standalone
* WebView2 Runtime - pre-installed on modern Windows, or get fromhttps://developer.microsoft.com/microsoft-edge/webview2

### Build

Use the build script to check prerequisites and build:

#
 Check prerequisites

.\build.ps1 
-
CheckOnly

#
 Build all projects

.\build.ps1

#
 Build specific project

.\build.ps1 
-
Project WinUI

Or build directly with dotnet:

#
 Build all (use build.ps1 for best results)

dotnet build

#
 Build WinUI (requires runtime identifier for WebView2 support)

dotnet build src
/
OpenClaw.Tray.WinUI
/
OpenClaw.Tray.WinUI.csproj 
-
r win
-
arm64 
#
 ARM64

dotnet build src
/
OpenClaw.Tray.WinUI
/
OpenClaw.Tray.WinUI.csproj 
-
r win
-
x64 
#
 x64

#
 Build MSIX package (for camera/mic consent prompts)

dotnet build src
/
OpenClaw.Tray.WinUI 
-
r win
-
arm64 
-
p:PackageMsix
=
true 
#
 ARM64 MSIX

dotnet build src
/
OpenClaw.Tray.WinUI 
-
r win
-
x64 
-
p:PackageMsix
=
true 
#
 x64 MSIX

### Run Tray App

#
 Build and launch the unpackaged WinUI tray app

.\run
-
app
-
local.ps1

#
 If you already built, skip rebuild and launch the existing Debug output

.\run
-
app
-
local.ps1 
-
NoBuild

#
 Run isolated from your normal tray settings so multiple worktrees can run together

.\run
-
app
-
local.ps1 
-
Isolated

#
 Alpha update testing from a Release build

.\run
-
app
-
local.ps1 
-
Configuration Release 
-
Isolated 
-
UpdateChannel alpha

#
 Optional: launch through WinAppCLI with Package.appxmanifest

.\run
-
app
-
local.ps1 
-
UseWinApp 
-
NoBuild

The default path starts the unpackaged executable directly.-UseWinApprequires
Microsoft WinAppCLI (winget install Microsoft.WinAppCLI) and is only needed when
you want manifest/MSIX-adjacent launch validation.

### Run CLI WebSocket Validator

Use the CLI to validate gateway connectivity andchat.sendoutside the tray UI.

#
 Show help

dotnet run 
--
project src
/
OpenClaw.Cli 
--
 
--
help

#
 Use tray settings from %APPDATA%\OpenClawTray\settings.json and send one message

dotnet run 
--
project src
/
OpenClaw.Cli 
--
 
--
message 
"
quick send validation
"

#
 Loop sends and also probe sessions/usage/nodes APIs

dotnet run 
--
project src
/
OpenClaw.Cli 
--
 
--
repeat 
5
 
--
delay
-
ms 
1000
 
--
probe
-
read 
--
verbose

#
 Override gateway URL/token for isolated testing

dotnet run 
--
project src
/
OpenClaw.Cli 
--
 
--
url ws:
//
127.0
.
0.1
:
18789
 
--
token 
"
<token>
"
 
--
message 
"
override test
"

## 📦 OpenClaw.Tray (Molty)

Modern Windows 11-style system tray companion that connects to your local OpenClaw gateway.

### Features

* 🦞Lobster branding- Pixel-art lobster tray icon with status colors
* 🎨Modern UI- Windows 11 flyout menu with dark/light mode support
* 💬Quick Send- Send messages via global hotkey (Ctrl+Alt+Shift+C)
* 🔄Auto-updates- Automatic updates from GitHub Releases
* 🌐Web Chat- Embedded chat window with WebView2
* 📊Live Status- Real-time sessions, channels, and usage display
* 🧭Command Center- Dense gateway, channel, usage, node, pairing, and allowlist diagnostics from one window
* ⚡Activity Stream- Command Center page for live session, usage, node, and notification events
* 🔔Toast Notifications- Clickable Windows notifications withsmart categorization
* 📡Channel Control- Start/stop Telegram & WhatsApp from the menu
* 🖥️Node Observability- Node inventory with online/offline state and copyable summary
* ⏱Cron Jobs- Quick access to scheduled tasks
* 🚀Auto-start- Launch with Windows
* ⚙️Settings- Full configuration page
* 🎯First-run onboarding— 6-screen setup wizard (connection, permissions, chat, configuration)

#### Quick Send scope requirement

Quick Send uses the gatewaychat.sendmethod and requires the operator device to haveoperator.writescope.

If Quick Send fails withmissing scope: operator.write, Molty now copies identity + remediation guidance to your clipboard, including:

* operator role andclient.idused by the tray app
* gateway-reported operator device id (if provided)
* currently granted scopes (if provided)

For this specific error (missing scope: operator.write), the cause is anoperator token scope issue. Update the token used by the tray app so it includesoperator.write, then retry Quick Send.

If Quick Send fails withpairing required/NOT_PAIRED, that is adevice approvalissue. Approve the tray device in gateway pairing approvals, reconnect, and retry.

### Menu Sections

* Status- Gateway connection status with click-to-view details
* Command Center- Hub with diagnostics, channel health, usage, sessions, nodes, and copyable repair commands
* Sessions- Active agent sessions with preview and per-session controls
* Usage- Provider/cost summary with quick jump to activity details
* Channels- Telegram/WhatsApp status with toggle control
* Nodes- Online/offline node inventory and copyable summary
* Recent Activity- Timestamped event stream for sessions, usage, nodes, and notifications
* Actions- Dashboard, Web Chat, Quick Send, Activity Stream, History
* Support & Debug- Logs, config, diagnostics folder, redacted support context, browser setup, port/capability/node/channel/activity summaries, and managed SSH tunnel restart
* Settings- Configuration and auto-start

### Mac Parity Status

Comparing againstopenclaw-menubar(macOS Swift menu bar app):

Feature

Mac

Windows

Notes

Menu bar/tray icon

✅

✅

Color-coded status

Gateway status display

✅

✅

Connected/Disconnected

PID display

✅

✅

Command Center shows gateway listener process/PID

Channel status

✅

✅

Mac: Discord / Win: Telegram+WhatsApp

Sessions count

✅

✅

Last check timestamp

✅

✅

Shown in tray tooltip

Gateway start/stop/restart

✅

⚠️

Windows can restart the managed SSH tunnel from tray Support & Debug and Command Center; external gateway process control is not implemented

View Logs

✅

✅

Open Web UI

✅

✅

Refresh

✅

✅

Auto-refresh on menu open

Launch at Login

✅

✅

Notifications toggle

✅

✅

### Windows-Only Features

These features are available in Windows but not in the Mac app:

Feature

Description

Quick Send hotkey

Ctrl+Alt+Shift+C global hotkey

Embedded Web Chat

WebView2-based chat window

Toast notifications

Clickable Windows notifications

Channel control

Start/stop Telegram & WhatsApp

Modern flyout menu

Windows 11-style with dark/light mode

Deep links

openclaw://
 URL scheme with IPC

First-run onboarding

6-screen guided setup wizard (Welcome → Connection → Wizard → Permissions → Chat → Ready)

### 🔌 Node Mode (Agent Control)

When Node Mode is enabled in Settings, your Windows PC becomes anodethat the OpenClaw agent can control - just like the Mac app! The agent can:

Capability

Commands

Description

System

system.notify
, 
system.run
, 
system.run.prepare
, 
system.which
, 
system.execApprovals.get
, 
system.execApprovals.set

Show Windows toast notifications, execute commands with policy controls

Canvas

canvas.present
, 
canvas.hide
, 
canvas.navigate
, 
canvas.eval
, 
canvas.snapshot
, 
canvas.a2ui.push
, 
canvas.a2ui.pushJSONL
, 
canvas.a2ui.reset

Display and control a WebView2 window

Screen

screen.snapshot
, 
screen.record

Capture screenshots and fixed-duration MP4 screen recordings

Camera

camera.list
, 
camera.snap
, 
camera.clip

Enumerate cameras and capture still photos or short video clips

Speech-to-text

stt.transcribe

Capture audio from the default microphone for a bounded duration and return transcribed text. Default-off; opt-in via Settings. When enabled, advertised to both gateway callers (subject to gateway allowlist) and local MCP clients (subject to bearer token).

Location

location.get

Return Windows geolocation when permission is available

Device

device.info
, 
device.status

Return Windows host/app metadata and lightweight status

Text-to-speech

tts.speak

Speak text aloud through Windows speech synthesis, or ElevenLabs when configured

Packaged installs declare camera, microphone, and location capabilities. Windows may ask for consent the first time a node capability uses one of those protected resources.

#### Node Setup

1. Enable Node Modein Settings (enabled by default)
2. First connectioncreates a pairing request on the gateway
3. Approve the deviceon your gateway:openclaw devices list#Find your Windows deviceopenclaw devices approve<id>#Approve it
4. Configure gateway allowCommands- Add the commands you want to allow undergateway.nodesin~/.openclaw/openclaw.json:{"gateway": {"nodes": {"allowCommands": ["system.notify","system.run","system.run.prepare","system.which","system.execApprovals.get","system.execApprovals.set","canvas.present","canvas.hide","canvas.navigate","canvas.eval","canvas.snapshot","canvas.a2ui.push","canvas.a2ui.pushJSONL","canvas.a2ui.reset","screen.snapshot","camera.list","camera.snap","camera.clip","location.get","device.info","device.status","tts.speak"]
 }
 }
}⚠️Important: The gateway has a server-side allowlist. Commands must be listed explicitly - wildcards likecanvas.*don't work! Privacy-sensitive commands such asscreen.recordand agent-driven audio playback viatts.speakshould only be added toallowCommandswhen you explicitly want to allow them.
5. Test itfrom your Mac/gateway:#Show a notificationopenclaw nodes notify --node<id>--title"Hello"--body"From Mac!"#Open a canvas windowopenclaw nodes canvas present --node<id>--url"https://example.com"#Execute JavaScript (note: CLI sends "javaScript" param)openclaw nodes canvaseval--node<id>--javaScript"document.title"#Render A2UI JSONL in the canvas (pass the file contents as a string)openclaw nodes canvas a2ui push --node<id>--jsonl"$(cat ./ui.jsonl)"#Take a screenshotopenclaw nodes invoke --node<id>--command screen.snapshot --params'{"screenIndex":0,"format":"png"}'#Record a short screen clip (requires explicitly allowing screen.record on the gateway)openclaw nodes screen record --node<id>--duration 3000 --fps 10 --screen 0 --no-audio --out /tmp/openclaw-windows-screen-record-test.mp4 --json#List camerasopenclaw nodes invoke --node<id>--command camera.list#Take a photo (NV12/MediaCapture fallback)openclaw nodes invoke --node<id>--command camera.snap --params'{"deviceId":"<device-id>","format":"jpeg","quality":80}'#Speak text aloud on the Windows node (requires TTS enabled in Settings and tts.speak allowed on the gateway)openclaw nodes invoke --node<id>--command tts.speak --params'{"text":"Hello from OpenClaw","provider":"windows"}'#Execute a command on the Windows nodeopenclaw nodes invoke --node<id>--command system.run --params'{"command":"Get-Process | Select -First 5","shell":"powershell","timeoutMs":10000}'#View exec approval policyopenclaw nodes invoke --node<id>--command system.execApprovals.get#Update exec approval policy (add custom rules)openclaw nodes invoke --node<id>--command system.execApprovals.set --params'{"rules":[{"pattern":"echo *","action":"allow"},{"pattern":"*","action":"deny"}],"defaultAction":"deny"}'📷Camera permission: Desktop builds rely on Windows Privacy settings. Packaged MSIX builds will show the system consent prompt.🔒Exec Policy:system.runis gated by an approval policy on the Windows node at%LOCALAPPDATA%\OpenClawTray\exec-policy.json(schema:{ "defaultAction": "...", "rules": [...] }). This is separate from gateway-side~/.openclaw/exec-approvals.json.Rules are matched against the full command line. Known wrapper payloads such ascmd /c ...,powershell -Command ...,pwsh -EncodedCommand ..., andbash -c ...are also evaluated before execution. Dangerous environment overrides likePATH,PATHEXT,NODE_OPTIONS,GIT_SSH_COMMAND,LD_*, andDYLD_*are rejected.

#### Command Center diagnostics

Open the status detail/Command Center from the tray menu or withopenclaw://commandcenter. It shows:

* channel health from gatewayhealthevents, including node-mode health received without a separate operator connection
* active sessions, usage/cost data, node inventory, declared commands, and Mac parity notes
* allowlist diagnostics that separate safe companion commands from privacy-sensitive opt-ins likescreen.record,camera.snap, andcamera.clip
* copyable repair commands for safe allowlist fixes and pending pairing approval
* recent activity and node invoke results through the Activity Stream, storing command names/status/duration only (not payloads, screenshots, recordings, or secrets)openclaw nodes invoke --node<id>--command system.execApprovals.set --params'{"rules":[{"pattern":"powershell.exe","action":"allow"},{"pattern":"pwsh.exe","action":"allow"},{"pattern":"echo *","action":"allow"},{"pattern":"*","action":"deny"}],"defaultAction":"deny"}'🔐Web Chat secure context: Remote web chat requireshttps://(or localhost). If using a self-signed cert, trust it in Windows (Trusted Root Certification Authorities) or use an SSH tunnel to localhost.

#### Node Status in Tray Menu

The tray menu shows node connection status:

* 🔌 Node Modesection appears when enabled
* ⏳ Waiting for approval...- Device needs approval on gateway
* ✅ Paired & Connected- Ready to receive commands
* Click the device ID to copy it for the approval command

### Deep Links

OpenClaw registers theopenclaw://URL scheme for automation and integration:

Link

Description

openclaw://settings

Open the Settings page

openclaw://setup

Open Setup Wizard

openclaw://chat

Open the Chat page

openclaw://commandcenter

Open Command Center diagnostics

openclaw://activity

Open the Activity page

openclaw://history

Open the Activity page filtered to notification history

openclaw://dashboard

Open Dashboard in browser

openclaw://dashboard/sessions

Open specific dashboard page

openclaw://dashboard/channels

Open Channels dashboard page

openclaw://dashboard/skills

Open Skills dashboard page

openclaw://dashboard/cron

Open Cron dashboard page

openclaw://healthcheck

Run a manual health check

openclaw://check-updates

Run a manual update check

openclaw://logs

Open the current tray log file

openclaw://log-folder

Open the logs folder

openclaw://config

Open the config folder

openclaw://diagnostics

Open the diagnostics JSONL folder

openclaw://support-context

Copy redacted support context

openclaw://debug-bundle

Copy a combined debug bundle for support

openclaw://browser-setup

Copy browser.proxy/browser-control setup guidance

openclaw://port-diagnostics

Copy gateway/browser/tunnel port diagnostics with owner PID stop hints

openclaw://capability-diagnostics

Copy permissions, allowlist, and parity diagnostics

openclaw://node-inventory

Copy node capabilities, commands, and policy status

openclaw://channel-summary

Copy channel health and start/stop availability

openclaw://activity-summary

Copy recent tray activity for troubleshooting

openclaw://extensibility-summary

Copy channel, skills, and cron dashboard surface guidance

openclaw://restart-ssh-tunnel

Restart the tray-managed SSH tunnel when enabled

openclaw://send?message=Hello

Open Quick Send with pre-filled text

openclaw://agent?message=Hello

Send message directly to the connected gateway

Deep links work even when Molty is already running - they're forwarded via IPC.

## 📦 OpenClaw.Shared

Shared library containing:

* OpenClawGatewayClient- WebSocket client for gateway protocol
* IOpenClawLogger- Logging interface
* Data models (SessionInfo, ChannelHealth, etc.)
* Channel control (start/stop channels via gateway)

## Development

### Project Structure

openclaw-windows-node/
├── src/
│ ├── OpenClaw.Shared/ # Shared gateway library
│ └── OpenClaw.Tray.WinUI/ # System tray app (WinUI 3)
├── tests/
│ ├── OpenClaw.Shared.Tests/ # Shared library tests
│ └── OpenClaw.Tray.Tests/ # Tray app helper tests
├── docs/
│ └── images/ # Screenshots
├── openclaw-windows-node.slnx # Solution file
├── README.md
├── LICENSE
└── .gitignore

### Configuration

Settings are stored in:

* Settings:%APPDATA%\OpenClawTray\settings.json
* Logs:%LOCALAPPDATA%\OpenClawTray\openclaw-tray.log
* Easy-button setup summary:%LOCALAPPDATA%\OpenClawTray\Logs\Setup\easy-setup-latest.txt
* Easy-button setup JSONL:%LOCALAPPDATA%\OpenClawTray\Logs\Setup\easy-setup-latest.jsonl

Default gateway:ws://localhost:18789

### First Run

On first run, Molty launches a guided onboarding wizard that walks you through setup:

1. Welcome— introduces OpenClaw and starts the setup flow
2. Connection— choose Local gateway, Remote gateway, or configure later. Paste a setup code or enter gateway URL and token manually. Tests the connection with Ed25519 device authentication.
3. Wizard— gateway-driven configuration steps (AI provider selection, personality setup, communication channels). Steps are defined by your gateway.
4. Permissions— reviews Windows system permissions (notifications, camera, microphone, screen capture, location) and links to system settings to grant them.
5. Chat— meet your agent in a live chat powered by the gateway's web UI.
6. Ready— summary of available features, option to launch at startup, and a Finish button.

For detailed setup instructions, seedocs/SETUP.md. For the full onboarding architecture, seedocs/ONBOARDING_WIZARD.md.

## License

MIT License - seeLICENSE

Formerly known as Moltbot, formerly known as Clawdbot

## About

Windows companion suite for OpenClaw - System Tray app, Shared library, Node, and PowerToys Command Palette extension

### Resources

 Readme

 

### License

 MIT license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.2k

 stars
 

### Watchers

5

 watching
 

### Forks

156

 forks
 

 Report repository

 

## Releases26

v0.6.0

 Latest

 

Jun 2, 2026

 

+ 25 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C#94.5%
* PowerShell4.1%
* Python1.2%
* Other0.2%