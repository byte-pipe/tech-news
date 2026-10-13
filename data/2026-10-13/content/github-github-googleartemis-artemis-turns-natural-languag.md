---
title: 'GitHub - google/artemis: ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code. It also achieves 99%+ success rate on AndroidWorld Benchmark. · GitHub'
url: https://github.com/google/artemis
site_name: github
content_file: github-github-googleartemis-artemis-turns-natural-languag
fetched_at: '2026-10-13T23:13:24.740542'
original_url: https://github.com/google/artemis
author: google
description: ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code. It also achieves 99%+ success rate on AndroidWorld Benchmark. - google/artemis
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

121 Commits
121 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
apps
apps
 
 
artemis
artemis
 
 
config
config
 
 
docs/
assets
docs/
assets
 
 
mcp_server
mcp_server
 
 
packages
packages
 
 
playground
playground
 
 
scripts
scripts
 
 
tests
tests
 
 
third_party/
mobile_use
third_party/
mobile_use
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.quality-baseline.json
.quality-baseline.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
pyproject.toml
pyproject.toml
 
 
pyright-core.json
pyright-core.json
 
 
setup.py
setup.py
 
 
start.bat
start.bat
 
 
start.sh
start.sh
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Let AI assistants and test suites use real phones like a human.

English•中文文档•Workflow Showcase•Quick Start•MCP for IDEs•Benchmarks•Discord Community

Live Demo: Setup driving routes and calculate total durations in Google Maps, then open YouTube to play a Coldplay song.

## Key Highlights

* Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions.
* Multimodal Targeting: Uses element indices when available, with coordinate and visual locating fallbacks for custom interfaces.
* IDE Diagnostics:Model Context Protocol (MCP)integration letsAntigravity, Claude Code, and Windsurfdrive test devices and collectLogcatoutput and screenshots.
* Flash Execution: A reactive observe-and-act loop with asynchronous history summaries, typically3–5s per step.
* Pro Exploration: Checks targets before individual actions and returns blocked actions to the Operator for recovery. Supports long-running exploratory and stability tests.
* AndroidWorld Results:99%+ task completionon Google Research'sAndroidWorldbenchmark (100+ multi-step tasks).

## Antigravity × ARTEMIS: Autonomous Testing Workflow

AntigravityusesARTEMISthrough MCP to turn a test request into a plan, device execution, and a diagnostic report:

1. Prompt Input (Task Dispatch)

Describe your test scenario and target metrics in Antigravity

2. Test Plan Generation

Formulates a step-by-step test plan & architecture for review

3. Autonomous Test Execution

Drives real device, navigates UI, and profiles performance

4. Final Report

Delivers structured audit findings, metric tables, and raw datasets

## Quick Start

Ensure an Android device (withUSB Debuggingenabled) or emulator is connected. The one-click startup script will automatically:

* Install System Toolchains: Detect and auto-install ADB, scrcpy, FFmpeg, and Python (uv) dependencies.
* Mount Global MCP Server & AI Agent Rules: Prompt to automatically install global MCP configurations and theArtemis Mobile Testing Mindset (rules.md)into your AI IDEs (Antigravity,Cursor,Claude Code,Codex,Windsurf,VS Code,Cline/Roo,OpenClaw).

### macOS and Linux

#
 1. Clone repo & navigate to directory

git clone https://github.com/google/artemis.git 
&&
 
cd
 artemis

#
 2. One-click launch

./start.sh

### Windows PowerShell

#
 1. Clone repo & navigate to directory

git clone https:
//
github.com
/
google
/
artemis.git
cd artemis

#
 2. One-click launch

.\
start.bat

PowerShell does not search the current directory for executable scripts by default, so use.\start.batwithout a trailing\. In Command Prompt (CMD), usestart.batinstead.

Tip: Openshttp://localhost:8000in your default browser with a device connection wizard, live screen mirroring, prompt sandbox, and execution replays. You can also run directly from CLI:uv run artemis run "Open Settings, find Battery and tell me current level" --profile flash.

MCP Setup for Codex / Antigravity / Claude Code / Windsurf (Click to expand)

ARTEMIS includes a nativeModel Context Protocol (MCP)server. Connect your real phone directly into AI IDEs:

### 1. One-Click Auto Install (Recommended)

Running./start.sh(macOS/Linux) or.\start.bat(Windows PowerShell) will prompt you to configure global MCP and testing rules for detected IDEs (or you can install/update anytime later manually using the commands below):

#
 Auto-install MCP server & global rules for Antigravity / Jetski:

uv run artemis mcp --install antigravity

#
 Or install for all supported AI IDEs (including Codex):

uv run artemis mcp --install all

Tip: You can also configure MCP interactively during first-time setup viauv run artemis init.Pro Tip: If you want to use theartemiscommand globally withoutuv runin any directory, runuv tool install -e .once in the project root.

### 2. Manual Configuration (Optional)

If you prefer to configure manually, runuv run artemis mcp --generate-config <client>(for example,codexorantigravity) to output the appropriate TOML or JSON snippet. Replace/path/to/artemiswith your actual repo path and pointcommandto your.venvPython executable:

* Codex(~/.codex/config.toml):

[
mcp_servers
.
artemis
]

command
 = 
"
/path/to/artemis/.venv/bin/python
"

args
 = [
"
-m
"
, 
"
mcp_server
"
]

cwd
 = 
"
/path/to/artemis
"

[
mcp_servers
.
artemis
.
env
]

PYTHONUNBUFFERED
 = 
"
1
"

PYTHONPATH
 = 
"
/path/to/artemis
"

* Antigravity(~/.gemini/jetski/mcp_config.json):

{
 
"mcpServers"
: {
 
"artemis"
: {
 
"command"
: 
"
/path/to/artemis/.venv/bin/python
"
,
 
"args"
: [
"
-m
"
, 
"
mcp_server
"
],
 
"cwd"
: 
"
/path/to/artemis
"
,
 
"env"
: {
 
"PYTHONUNBUFFERED"
: 
"
1
"

 },
 
"tools"
: {
 
"mobile_run_task"
: { 
"eager"
: 
true
 },
 
"mobile_manage_task"
: { 
"eager"
: 
true
 },
 
"mobile_get_device_state"
: { 
"eager"
: 
true
 },
 
"mobile_inspect_trace"
: { 
"eager"
: 
true
 },
 
"mobile_diagnose"
: { 
"eager"
: 
true
 }
 }
 }
 }
}

* Claude Desktop(claude_desktop_config.json):

{
 
"mcpServers"
: {
 
"artemis"
: {
 
"command"
: 
"
/path/to/artemis/.venv/bin/python
"
,
 
"args"
: [
"
-m
"
, 
"
mcp_server
"
],
 
"cwd"
: 
"
/path/to/artemis
"

 }
 }
}

### 3. Mount Behavioral Rules for AI Agents (Highly Recommended)

To ensure your AI coding assistant acts with the rigor of a senior mobile test engineer and never hallucinates UI interactions, we provide a dedicated testing mindset rules file atmcp_server/rules.md(coveringActive Exploration before coding,Flash vs. Pro routing strategy,Latency & Timing compensation, and the"Dynamic-First, Coordinate-Fallback" locator pattern).

You can mount or copymcp_server/rules.mdinto your AI IDE's rule configuration:

* Antigravity: Add the contents ofrules.mdto your Workspace Rules, Global Rules settings, or agent instructions.
* Claude Code: Runartemis mcp --install claudeto install the rules to~/.claude/rules/artemis.md(install to exactly one location — Claude Code loads both~/.claude/CLAUDE.mdand~/.claude/rules/*.md, so duplicating the rules wastes context).
* Cursor: Copy the contents into.cursorrulesor create a rule file at.cursor/rules/artemis.mdc.
* Codex: Add the contents to~/.codex/AGENTS.md(or the activeAGENTS.override.md).
* Windsurf / OpenClaw: Add the rules to your workspace rules or global system prompts.

For more details on the testing mindset and MCP architecture, see theMCP Server README.

### 4. Prompt Your Phone in the IDE Chat

In Codex, Antigravity, or Claude Code, simply prompt:

"Build the latest changes into an APK, install it on the connected device, open the login screen with a test account, verify if there are any unexpected popups after login, and return screenshots of the final page."

Python SDK Integration (Click to expand)

Install the zero-runtime-dependency client on the development machine. ADB,
agents, models, and image processing remain on the device host:

uv add 
"
artemis-client @ git+https://github.com/google/artemis.git#subdirectory=packages/artemis-client
"

import
 
asyncio

from
 
artemis_client
 
import
 
ArtemisClient

async
 
def
 
main
():
 
client
 
=
 
ArtemisClient
(
 
"http://artemis-host:8000"
,
 
device_serial
=
"emulator-5554"
, 
# optional: target specific device serial

 
default_profile
=
"flash"
, 
# "flash" (fast reactive) or "pro" (deep reasoning)

 )

 
result
 
=
 
await
 
client
.
run
(
 
"Open System Settings, go to 'Battery', verify battery percentage is displayed, and check for any crash dialogs."
,
 )

 
assert
 
result
.
succeeded
, 
f"Test failed: 
{
result
.
error
 
or
 
result
.
status
}
"

 
print
(
f"✅ Test Passed! Device: 
{
result
.
device_serial
}
 | Trace ID: 
{
result
.
trace_id
}
"
)

if
 
__name__
 
==
 
"__main__"
:
 
asyncio
.
run
(
main
())

## Usage Modes

Console Overview:① View Switcher(Home / Workspace) ·② Model & Replay(Flash/Pro status & video replay) ·③ Live Agent Stream(Action perception, target coordinates & structured results) ·④ Prompt Dock(Natural language dispatch) ·⑤ Task Queue & Dashboard(Lifecycle & history)

* Web Visual Test Console (uv run artemis ui): Real-time screen projection and interactive panel, supporting natural language test dispatch, live reasoning telemetry, action trajectories, and execution replay; manage server lifecycle anytime from any terminal usinguv run artemis restart,uv run artemis stop, anduv run artemis status;
* MCP Server: ConnectsAntigravity, Claude Code, Windsurf, and other MCP clients to real devices for bug reproduction and test execution;
* Developer CLI (uv run artemis run): Direct terminal execution for automated test cases, exploratory stability inspection, or AndroidWorld benchmarks with high-fidelity structured terminal output;
* Python SDK: Integrates as a standard Python library into existing automated testing frameworks (e.g., pytest) or CI/CD pipelines with strongly typed Pydantic structured outputs and assertion support.

## What ARTEMIS Installs on Your Phone

The first task on a device installs theArtemis Accessibility Helper, a small
accessibility service that reads the screen layout without taking the
UiAutomation connection. Tools using UiAutomation can suppress the helper unless
they enableFLAG_DONT_SUPPRESS_ACCESSIBILITY_SERVICES. You will see
a collapsed "Artemis test helper is running" notification and a new entry under
Settings > Accessibility; both are that helper. It listens only on the phone
itself and sends nothing elsewhere.

* Pre-install it (avoids the ~3 s delay on the first task):uv run artemis helper install
* Inspect it:uv run artemis helper status/uv run artemis doctor
* Remove it any time:uv run artemis helper uninstall
* Use UIAutomator2 instead:ARTEMIS_HIERARCHY_BACKEND=uiautomatorin.env
* Prevent automatic installation:ARTEMIS_HELPER_AUTO_INSTALL=falsein.env

If the helper ever fails mid-task, ARTEMIS falls back to UIAutomator2 and says
so in the task timeline, inmobile_manage_taskstatus, and in the final report.

## Benchmarks: AndroidWorld (SOTA 99%+)

Artemis achieved a99%+ completion rateonAndroidWorld, Google Research's benchmark spanning 20+ apps and 100+ multi-step tasks.

## How ARTEMIS is Architected

* Pre-Execution Checks and Action Bursts: Pro checks the target against the live UI tree and pixels before dispatching an individual action. Action bursts handle transient controls without waiting for another model turn.
* Element Locating: Combines accessibility hierarchies and OCR with visual models for custom Canvas, Compose, and Flutter interfaces.
* Shared History Compression: Flash and Pro replace older screenshots with visual summaries and compress completed steps into searchable history chunks. Context thresholds control when raw turns are replaced.

## Execution Profiles: Flash vs. Pro

ARTEMIS supports two execution profiles tailored for different automation requirements:

* Flash Profile (--profile flash): Fast and token-efficient reactive loop (~3–5s per step): one model observes the live screen, thinks, and acts, with no graph orchestration. Ideal for routine, deterministic UI tasks. The loop is unbounded by default (agent.flash.max_turns, 0 = unlimited) because history is compressed rather than capped: Flash shares the Pro session transcript ledger (session-relativeT+mm:ssclock, screenshots folded into visual summaries, older steps chunked into eras and recallable on demand viasearch_history/replay_steps) and can query the session recording throughvideo_analyzer. Transient UI (auto-fading control bars, toasts) is handled by chaining taps into oneclick_sequence.Limitations: No task plan or notes, no pre-execution safety net, no checkpoint verification or final report, and no ADB shell.
* Pro Profile (--profile pro): A planning and verification workflow (~15–40s per step), built as a multi-agent graph. APlannermaintains a living Markdown task plan with milestones andverify/assertcheck items; theOperatorexecutes it with the full toolset (Explorer grounding whoseflash/pro/ultratier is a user setting per profile —pro.explorer.mode/flash.explorer_modeinconfig/artemis.jsoncor--explorer-pro-mode— never chosen by the agent; notes, history recall, video analysis, ADB diagnostics). Every single action passes a pre-executionSafety Net(XML-first, pixel fallback), while multi-actionfast-action burstsfire back to back to beat turn latency on transient UI. A blocked or failed action opens anexecution incidentthat stays in the Operator's context until a later action succeeds, so recovery is handled by the Operator itself with no separate repair agent. A read-onlyCheckerverifies plan checkpoints and runs an exit final review against the original goal (--verification-level:off/final(default) /checkpoints/strict), and plan milestone edits get an advisory review. Handles 100+ step long-horizon workflows,[Loop:continuous]monitoring, and an optional written report.

## Roadmap

* Android Studio Integration: Native IDE plugin and workflow integration to enable in-editor debugging, test recording, and automated device control directly within Android Studio.
* iOS Platform Expansion: Extending multimodal perception and mobile automation to iOS devices and simulators.
* On-Device Lightweight VLMs: Local execution with lightweight edge vision models for low-latency, privacy-first automation.
* Real-time Duplex Voice Interaction: Voice-driven task dispatch with real-time conversational control and interruption handling.

## Community & Contributing

Contributions are warmly welcomed!

* Star the repoto follow updates and releases
* Join theDiscord Communityfor technical discussions
* Open anIssueor submit aPull Request

## License

This project is licensed under theApache License 2.0.

### Third-party code

Code not owned by Google lives underthird_party/, one directory per upstream project, each with its ownLICENSEandMETADATA.

* third_party/mobile_use– portions ofmobile-useby Minitap, Inc., Apache License 2.0.