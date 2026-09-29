---
title: 'GitHub - ahujasid/mcp-for-blender: Community plugin to control Blender 3D with any LLM of your choice · GitHub'
url: https://github.com/ahujasid/mcp-for-blender
site_name: github
content_file: github-github-ahujasidmcp-for-blender-community-plugin-to
fetched_at: '2026-09-29T16:48:34.539910'
original_url: https://github.com/ahujasid/mcp-for-blender
author: ahujasid
description: Community plugin to control Blender 3D with any LLM of your choice - ahujasid/mcp-for-blender
---

ahujasid

 

/

mcp-for-blender

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star29.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

225 Commits
225 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
assets
assets
 
 
src/
blender_mcp
src/
blender_mcp
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
TERMS_AND_CONDITIONS.md
TERMS_AND_CONDITIONS.md
 
 
addon.py
addon.py
 
 
main.py
main.py
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# MCP for Blender

Connect Blender to any LLM

formerlyblender-mcp— the PyPI package is nowmcp-for-blender.Existing setups keep working; no config change is required.Read more

Disclaimer:This is a third-party integration and not made by Blender

Prompt-assisted 3D modeling, scene creation, and manipulation — driven by AI.

Website·Full Tutorial·Discord·Sponsor·Buy me a coffee·Feedback

Supporters

CodeRabbitKevin Guanche DariasGuillermo Rauch

All supporters:Support this project

## Quickstart

Note:the PyPI packageblender-mcpis nowmcp-for-blender. Existing setups
keep working —uvx blender-mcpstill runs the server andno config change is
required. New installs should usemcp-for-blender.What changed and why

Three steps: installuv, point your MCP client at the server, install the Blender addon.

1. Install uv

#
 macOS

brew install uv

#
 Linux

curl -LsSf https://astral.sh/uv/install.sh 
|
 sh

#
 Windows

powershell -c 
"
irm https://astral.sh/uv/install.ps1 | iex
"

Warning:Do not proceed before installing uv. Use the official installer —notpip install uv.

2. Add the MCP server to your client

Claude Desktop
 — Settings → Developer → Edit Config

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
mcp-for-blender
"
]
 }
 }
}

Claude Code

claude mcp add blender uvx mcp-for-blender

Codex

codex mcp add blender -- uvx mcp-for-blender

Cursor / VS Code / OpenCode / Antigravity

SeeMCP Client Setupbelow for per-client instructions and one-click install buttons.

3. Install the Blender addon

uvx mcp-for-blender install-addon

Then in Blender:Edit → Preferences → Add-ons→ enableInterface: MCP for Blender.

4. Connect

In Blender's 3D viewport, pressN→ open theMCP for Blendertab → clickStart MCP Server. That's it — ask Claude to build something.

Note:Only runoneinstance of the MCP server (either Cursor or Claude Desktop), not both.

## Table of Contents

* Quickstart
* Features
* Premium
* Components
* InstallationPrerequisitesMake your client find uvxPin the Python versionInstall without uvRun with DockerEnvironment Variables
* Prerequisites
* Make your client find uvx
* Pin the Python version
* Install without uv
* Run with Docker
* Environment Variables
* MCP Client SetupClaude for DesktopCodexCursorVisual Studio CodeOpenCodeAntigravity
* Claude for Desktop
* Codex
* Cursor
* Visual Studio Code
* OpenCode
* Antigravity
* Installing the Blender Addon
* Upgrading (existing users)
* UsageStarting the ConnectionUsing with ClaudeCapabilitiesExample Commands
* Starting the Connection
* Using with Claude
* Capabilities
* Example Commands
* Persistent API Credentials
* Troubleshooting
* Technical Details
* Limitations & Security Considerations
* Telemetry Control
* Feedback
* Contributing
* Disclaimer
* Star History

## Features

Two-way communication

Connect Claude AI to Blender through a socket-based server

Object manipulation

Create, modify, and delete 3D objects in Blender

Material control

Apply and modify materials and colors

Scene inspection

Get detailed information about the current Blender scene

Code execution

Run arbitrary Python code in Blender from Claude

Asset & model generation

Poly Haven assets, Sketchfab models, Poly Pizza low-poly models, and AI-generated 3D models via Hyper3D Rodin and Hunyuan3D

## Premium

Generate AI 3D models (Hunyuan3D, Tripo, Hyper3D Rodin) straight into Blender without bringing your own API keys.More details

## Components

The system consists of two main components:

1. Blender Addon(addon.py) — a Blender addon that creates a socket server within Blender to receive and execute commands
2. MCP Server(src/blender_mcp/server.py) — a Python server that implements the Model Context Protocol and connects to the Blender addon

## Installation

### Prerequisites

* Blender3.0 or newer
* Python3.10 or newer
* uvpackage manager

Installing uv, per platform

macOS

brew install uv

Windows

powershell 
-
c 
"
irm https://astral.sh/uv/install.ps1 | iex
"

Then add uv to the user path in Windows (you may need to restart Claude Desktop after):

$localBin
 
=
 
"
$
env:
USERPROFILE
\.local\bin
"

$userPath
 
=
 [
Environment
]::GetEnvironmentVariable(
"
Path
"
,
 
"
User
"
)
[
Environment
]::SetEnvironmentVariable(
"
Path
"
,
 
"
$userPath
;
$localBin
"
,
 
"
User
"
)

Linux

curl -LsSf https://astral.sh/uv/install.sh 
|
 sh

It lands in~/.local/bin— open a new shell so it's on your PATH.

Otherwise, installation instructions are on their website:Install uv

On every OS, use uv'sofficial installer above — notpip install uv, which may not create theuvxcommand and can hide uv inside an environment your client can't see.

Warning:Do not proceed before installing uv.

### Make your client find uvx

MCP clients started from a GUI (Claude Desktop, Cursor, VS Code from the Dock/Start menu) donotinherit your terminal's PATH, so a bare"command": "uvx"can fail withspawn uvx ENOENTeven thoughuvxworks in your terminal. If that happens:

* Find uvx's full path —which uvx(macOS/Linux) orwhere uvx(Windows) — and use it as"command", e.g./opt/homebrew/bin/uvxorC:\Users\<you>\.local\bin\uvx.exe.
* On Windows you can instead wrap it:"command": "cmd", "args": ["/c", "uvx", "mcp-for-blender"].
* After any PATH or config change,fully quit and relaunchthe client (Windows: quit from the system tray, not just the window; macOS:Cmd+Q).

### Pin the Python version

Avoid conda / pyenv / version conflicts.

uv chooses which Python runs the server. On machines with conda (auto-activated base), pyenv, or asdf — or with a newer CPython release that some dependencies do not have wheels for yet — uv can grab an interpreter that makes installation fail. Pin Python 3.11 and prefer uv-managed interpreters to avoid using whatever is on your PATH:

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
--python
"
, 
"
3.11
"
, 
"
mcp-for-blender
"
],
 
"env"
: { 
"UV_PYTHON_PREFERENCE"
: 
"
only-managed
"
 }
 }
 }
}

--python 3.11still satisfies this package'srequires-python >=3.10, andUV_PYTHON_PREFERENCE=only-managedkeeps uv from selecting conda, pyenv, asdf, or system Python first. (The repo's.python-versionis only a hint for contributors and doesnotaffectuvx.)

If a previous failed attempt keeps replaying after a fix, clear the cache:

uv cache clean mcp-for-blender blender-mcp 
&&
 uvx --refresh mcp-for-blender

### Install without uv

On locked-down machines you can skip uvx entirely withpipx, then point your client at the installed command:

pipx install mcp-for-blender
pipx ensurepath 
#
 then restart your shell / client

Use the resulting absolute path as"command"(find it withwhich mcp-for-blender/where mcp-for-blender) and omitargs.

### Run with Docker

You can run the MCP server in a container instead of installing it. Blender itself still runs on your machine — the container only hosts the MCP server, which connects out to the Blender addon.

Build the image from the repo root:

docker build -t mcp-for-blender 
.

Then point your MCP client at it (the-iflag is required — the server talks to the client over stdin/stdout):

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
docker
"
,
 
"args"
: [
"
run
"
, 
"
-i
"
, 
"
--rm
"
, 
"
mcp-for-blender
"
]
 }
 }
}

The image defaults toBLENDER_HOST=host.docker.internal, which reaches the host's Blender out of the box with Docker Desktop onmacOS and Windows.

OnLinux,host.docker.internaldoesn't exist and the addon only listens onlocalhost, so use host networking instead:

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
docker
"
,
 
"args"
: [
"
run
"
, 
"
-i
"
, 
"
--rm
"
, 
"
--network=host
"
, 
"
-e
"
, 
"
BLENDER_HOST=localhost
"
, 
"
mcp-for-blender
"
]
 }
 }
}

To enablesafe modein the container, add"-e", "BLENDER_MCP_SAFE_MODE=1"toargs.

### Environment Variables

The following environment variables can be used to configure the Blender connection:

Variable

Default

Description

BLENDER_HOST

localhost

Host address for Blender socket server

BLENDER_PORT

9876

Port number for Blender socket server

BLENDER_MCP_SAFE_MODE

off

Set to 
1
 to validate scripts before they run in Blender (see below)

Example:

export
 BLENDER_HOST=
'
host.docker.internal
'

export
 BLENDER_PORT=9876

You can also pass the connection as CLI flags, which take precedence over the
environment variables. This is handy for running several Blender instances side
by side, since each MCP client entry can point at a different port with plain
arguments instead of env vars:

uvx mcp-for-blender --port 9877

In an MCP client config that means a second entry differing only inargs:

{
 
"mcpServers"
: {
 
"blender"
: { 
"command"
: 
"
uvx
"
, 
"args"
: [
"
mcp-for-blender
"
] },
 
"blender-b"
: { 
"command"
: 
"
uvx
"
, 
"args"
: [
"
mcp-for-blender
"
, 
"
--port
"
, 
"
9877
"
] }
 }
}

Each instance needs its own port set in the Blender addon panel to match.

Note:the addon's socket server has no authentication or encryption, so
anyone who can reach that port can run Python inside Blender. Keep it onlocalhostunless you are on a trusted network, and prefer an SSH tunnel over
pointing--host/BLENDER_HOSTat a remote machine directly.

#### Safe mode

By default, the AI can run any Python code in Blender. SetBLENDER_MCP_SAFE_MODE=1to check every script before it runs and block risky code — things like reading or writing files directly, running other programs, accessing the network, or installing code that keeps running after the script ends. Normal Blender work (modeling, materials, rendering, saving, import/export) still works. Blocked scripts are sent back to the AI with the reason, so it can try again with a corrected version.

## MCP Client Setup

### Claude for Desktop

Watch the setup instruction video(assuming you have already installed uv)

Go toClaude → Settings → Developer → Edit Config →claude_desktop_config.jsonand include the following:

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
 
"
mcp-for-blender
"

 ]
 }
 }
}

Claude Code

Use the Claude Code CLI to add the MCP for Blender server:

claude mcp add blender uvx mcp-for-blender

### Codex

The Codex CLI, desktop app, and IDE extension all share the same config file (~/.codex/config.toml), so setting the server up once covers all three.

Register the server with theCodex CLI:

codex mcp add blender -- uvx mcp-for-blender

Or add it by hand to~/.codex/config.toml(or$CODEX_HOME/config.toml):

[
mcp_servers
.
blender
]

command
 = 
"
uvx
"

args
 = [
"
mcp-for-blender
"
]

Or in theCodex desktop app:Settings → MCP servers → Add server→ name itblender, pickSTDIO, enteruvx mcp-for-blenderas the command, thenSaveand restart. If the app can't finduvx, use its full path instead — seeMake your client find uvx.

Check it registered withcodex mcp list— theblenderserver should show asenabled. The tools become available the next time you start Codex.

To setenvironment variables(e.g. a non-default Blender host/port), pass--env KEY=VALUEflags tocodex mcp add, or add them in the config file:

[
mcp_servers
.
blender
]

command
 = 
"
uvx
"

args
 = [
"
mcp-for-blender
"
]

env
 = { 
BLENDER_HOST
 = 
"
localhost
"
, 
BLENDER_PORT
 = 
"
9876
"
 }

### Cursor

macOS— go toSettings → MCPand paste the following:

* To use as a global server, use the"add new global MCP server"button and paste
* To use as a project-specific server, create.cursor/mcp.jsonin the root of the project and paste

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
 
"
mcp-for-blender
"

 ]
 }
 }
}

Windows— go toSettings → MCP → Add Server, add a new server with the following settings:

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
cmd
"
,
 
"args"
: [
 
"
/c
"
,
 
"
uvx
"
,
 
"
mcp-for-blender
"

 ]
 }
 }
}

Cursor setup video

Note:Only runoneinstance of the MCP server (either on Cursor or Claude Desktop), not both.

### Visual Studio Code

Prerequisites: Make sure you haveVisual Studio Codeinstalled before proceeding.

### OpenCode

{
 
"mcp"
: {
 
"blender-mcp"
: {
 
"type"
: 
"
local
"
,
 
"command"
: [
"
uvx
"
, 
"
mcp-for-blender
"
],
 
"enabled"
: 
true
,
 
"environment"
: {
 
"BLENDER_HOST"
: 
"
localhost
"
,
 
"BLENDER_PORT"
: 
"
9876
"

 }
 }
 }
}

### Antigravity

{
 
"mcpServers"
: {
 
"blender-mcp"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
mcp-for-blender
"
],
 
"env"
: {
 
"BLENDER_HOST"
: 
"
localhost
"
,
 
"BLENDER_PORT"
: 
"
9876
"

 }
 }
 }
}

## Installing the Blender Addon

1. Recommended— from a terminal, run:

uvx mcp-for-blender install-addon

This copies the addon into your Blender addons folder asblender_mcp.py. It prints where it wrote to, and keeps a.bakof any file it replaces.

Optional:uvx mcp-for-blender addon-pathslists detected Blender addons folders. Override the destination withBLENDERMCP_ADDONS_DIR=/path/to/scripts/addons.

2.Open Blender

3.Go toEdit → Preferences → Add-ons

4.EnableInterface: MCP for Blender(search "MCP for Blender"). If it doesn't appear yet, clickInstall…and select the copiedblender_mcp.py/addon.py, or restart Blender.

5. Manual alternative— if the command above can't find your Blender install, or you prefer doing it by hand: downloadaddon.pyfrom this repo → in Blender,Edit → Preferences → Add-ons → Install…→ select the downloadedaddon.py→ enable it.

Then open theMCP for Blendertab in Blender's sidebar (pressNin the 3D viewport) and clickStart MCP Server. SeeStarting the Connectionbelow.

## Upgrading (existing users)

For newcomers, go straight toQuickstart. For existing users, see below.

1.Update the addon file by running:

uvx mcp-for-blender install-addon
uvx mcp-for-blender addon-paths 
#
 optional: list detected Blender addons folders

2.In Blender:Preferences → Add-ons→ disable and re-enableInterface: MCP for Blender(or restart Blender), then clickStart MCP Serveragain.

3.Delete the MCP server from Claude and add it back again if the server package itself needs a refresh.

Note:the MCP server never modifies your Blender addon files on its own. When it starts, it checks whether the installed addon is behind the bundled copy and logs how to update;install-addonis what actually writes, and it keeps a.bakof the file it replaces. Trajectory capture still works on older loaded addons via anexecute_codefallback.

## Usage

### Starting the Connection

1. In Blender, go to the 3D View sidebar (pressNif not visible)
2. Find theMCP for Blendertab
3. Turn on the checkboxes you'd like to use (see more underCapabilitiesbelow)
4. ClickConnect to Claude
5. Make sure the MCP server is running in your terminal

### Using with Claude

Once the config file has been set on Claude, and the addon is running on Blender, you will see a hammer icon with tools for MCP for Blender.

### Capabilities

* Get scene and object information
* Create, delete and modify shapes
* Apply or create materials for objects
* Execute any Python code in Blender
* Export the scene, the selection or named objects to GLB/FBX for other applications (export_scene)
* Look up node schemas and the bpy API reference instead of guessing socket order or enum names
* Search and download free CC0 HDRIs, textures and models fromPoly Haven
* Search and download models fromSketchfab
* Search and download low-poly models fromPoly Pizza
* AI generated 3D models throughHyper3D RodinandHunyuan3D

#### Hunyuan3D on Tencent Cloud (Official API mode)

Which Tencent Cloud service the addon must call depends on where your account lives:

Account

Service the addon calls

Region

Sidebar toggle

Mainland (cloud.tencent.com)

AI3D 3.0 (
ai3d
, version 
2025-05-13
)

ap-guangzhou

leave 
International (Pro) account
 off (default)

International (tencentcloud.com), 
Hunyuan-to-3D (Professional)

hunyuan
, version 
2023-09-01
, PBR enabled

ap-singapore

tick 
International (Pro) account

International credentials sent to the mainland endpoint fail withAuthFailure.SignatureFailureorResourceUnavailable, so tick the toggle when your SecretId/SecretKey come from tencentcloud.com.
The toggle sits underTencent Hunyuan 3D → Official APIin the sidebar.

#### Poly Haven

Poly Havenpublishes around 2,400 HDRIs, textures and models,
all CC0 and free, funded by donations rather than by selling the assets. There is no API
key, no account and no rate limit worth worrying about.

In the 3D View sidebar, tickPoly Haven. That is the whole setup.

Worked example:

"Light the scene with an overcast afternoon HDRI and put a rusty metal texture on the wall"

Claude callssearch_polyhaven_assets(query="overcast afternoon", asset_type="hdris"),
which understands the intent rather than matching keywords - "couch" finds sofas, and it
works in any language. It can then check the thumbnail withget_polyhaven_asset_preview(asset_id="...")before spending the bandwidth, and import
withdownload_polyhaven_asset(...).

get_polyhaven_categories(asset_type="textures")returns the category tree and every
attribute that type can be filtered on, each with the values it accepts - weather and time
of day for HDRIs, surface use and condition for textures, material and whether a model is
rigged or ships level-of-detail variants. Pass a category path or those attributes tosearch_polyhaven_assets; matching on a category is inclusive, so a parent selects
everything nested beneath it.

Models are imported from the.blend, which is the file the artist authored - the glTF,
FBX and USD versions are generated from it and lose material detail. Textures build a
Principled material from the maps that drive it, and skip the repackings and alternate
conventions that nothing reads. HDRIs are packed into the file, so the lighting survives
being saved and reopened somewhere else, and arrive in a new world rather than overwriting
one you built.

Licence and attribution:every Poly Haven asset is CC0. You never have to credit
anyone, for anything, commercial or not. TheirAPI termsdo ask that
software built on the live API makes clear where the assets come from, so the search and
import responses name the source and link the asset's page. On import,polyhaven_id,polyhaven_url,polyhaven_authors,polyhaven_resolutionandpolyhaven_licenceare
written onto the imported objects, materials, images and world as custom properties, so
whoever opens the.blendlater can still find the asset and the artist who made it.

#### Poly Pizza

Poly Pizzahosts roughly 10,600 free low-poly models, including the
rescued Google Poly archive. It is the best source for stylised game assets: every model is
a single self-contained.glb, and the geometry is far lighter than Sketchfab's.

1. Get a free API key atpoly.pizza/settings/api
2. In the 3D View sidebar, tickUse assets from Poly Pizza
3. Paste the key into theAPI Keyfield that appears (or store it permanently underEdit → Preferences → Add-ons → MCP for Blender)

Worked example:

"Search Poly Pizza for a low-poly chair under a CC0 licence and import one at 1 metre tall"

Claude callssearch_polypizza_models(query="chair", licence="CC0"), which returns each
match with its licence and triangle count, thendownload_polypizza_model(model_id="...", normalize_size=True, target_size=1.0).

You can also filter by category ("Animals","Furniture & Decor","Transport","Nature","Buildings","People & Characters","Food & Drink","Weapons","Clutter","Objects","Scenes & Levels","Other") or ask for animated models only.

Attribution:about 69% of the Poly Pizza catalogue is CC-BY, whichrequiresyou to
credit the creator wherever the model appears. On import, the ready-formatted credit line
is written onto each imported root object as the custom propertypolypizza_attribution(alongsidepolypizza_idandpolypizza_licence), so it is saved into your.blendand
survives the session. Filter withlicence="CC0"if you would rather use models that need
no credit.

### Example Commands

Here are some examples of what you can ask Claude to do:

Prompt

Demo

"Create a low poly scene in a dungeon, with a dragon guarding a pot of gold"

Watch

"Create a beach vibe using HDRIs, textures, and models like rocks and vegetation from Poly Haven"

Watch

Give a reference image, and create a Blender scene out of it

Watch

"Get information about the current scene, and make a threejs sketch from it"

Watch

"Generate a 3D model of a garden gnome through Hyper3D"

"Fill this room with low-poly furniture from Poly Pizza"

"Make this car red and metallic"

"Create a sphere and place it above the cube"

"Make the lighting like a studio"

"Point the camera at the scene, and make it isometric"

## Persistent API Credentials

MCP for Blender supports persistent credentials via Blender Add-on Preferences:

Edit → Preferences → Add-ons → MCP for Blender

You can store these values there so they survive Blender restarts:

* Sketchfab API Key
* Poly Pizza API Key
* Hyper3D API Key
* Hunyuan3D SecretId / SecretKey
* Hunyuan3D API URL

For headless setups or CI, credentials can also be injected by environment variables:

Variable

BLENDERMCP_SKETCHFAB_API_KEY

BLENDERMCP_POLYPIZZA_API_KEY

BLENDERMCP_HYPER3D_API_KEY

BLENDERMCP_HUNYUAN3D_SECRET_ID

BLENDERMCP_HUNYUAN3D_SECRET_KEY

BLENDERMCP_HUNYUAN3D_API_URL

## Troubleshooting

Problem

Fix

Connection issues

Make sure the Blender addon server is running, and the MCP server is configured on Claude. 
Do not
 run the 
uvx
 command in the terminal. Sometimes the first command won't go through, but after that it starts working.

Timeout errors

Try simplifying your requests or breaking them into smaller steps.

Blender freezes during a Poly Haven download

Assets are downloaded on Blender's main thread, so the UI stops responding until the transfer finishes. File size grows roughly fourfold per resolution step, so ask for 1k or 2k unless the asset is held close to camera.

Poly Pizza download fails with a Cloudflare challenge

static.poly.pizza
 is behind bot protection and blocks datacenter, VPN and cloud IPs. Your API key is fine - the CDN never sees it. Retry from a normal connection, or download the 
.glb
 by hand and use 
File → Import → glTF 2.0
.

Have you tried turning it off and on again?

If you're still having connection errors, try restarting both Claude and the Blender server.

## Technical Details

### Communication Protocol

The system uses a simple JSON-based protocol over TCP sockets:

* Commandsare sent as JSON objects with atypeand optionalparams
* Responsesare JSON objects with astatusandresultormessage

## Limitations & Security Considerations

Warning:Theexecute_blender_codetool allows running arbitrary Python code in Blender, which can be powerful but potentially dangerous. Use with caution in production environments.ALWAYS save your work before using it.

* Poly Haven requires downloading models, textures, and HDRI images. If you do not want to use it, please turn it off in the checkbox in Blender.
* Complex operations might need to be broken down into smaller steps.

## Telemetry Control

Telemetry isopt-in. Collection of your content is off by default and stays off until you explicitly turn it on.

What is collected by default (no opt-in):a minimal anonymous usage record so I can count active users and see which tools get used — a randomly generated install ID, a session ID, the tool name, whether it succeeded, how long it took, the MCP for Blender and Blender versions, your operating system, and a timestamp.

Never collected without opting in:your prompts, generated code, viewport screenshots, scene data, and trajectory steps.

To opt in— go toEdit → Preferences → Add-ons → MCP for Blenderand check the telemetry consent checkbox. Some MCP clients will also offer you a one-time opt-in prompt at the start of a conversation. Opting in adds prompts, generated code, screenshots, and trajectory data to what's collected; see the TnC for details. You can turn it back off in the same place at any time.

To turn off telemetry entirely, including the minimal anonymous usage record, set an environment variable:

DISABLE_TELEMETRY=true uvx mcp-for-blender

Or add it to your MCP config:

{
 
"mcpServers"
: {
 
"blender"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
mcp-for-blender
"
],
 
"env"
: {
 
"DISABLE_TELEMETRY"
: 
"
true
"

 }
 }
 }
}

Telemetry data is not linked to your name or account. It may be used to improve MCP for Blender, for research, and to train AI models.

Full detail on what is collected, and the license you grant by opting in, is inTERMS_AND_CONDITIONS.md.

## Feedback

We are actively looking for feedback on MCP for Blender. If you have thoughts, share themhere.

If you have more detailed feedback, you can schedule a call with ushere— we will credit you in the project.

### Join the Community

Give feedback, get inspired, and build on top of the MCP:Discord

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This is a third-party integration and not made by Blender. Made bySiddharth.

## Star History

If MCP for Blender is useful to you, consider starring the repo