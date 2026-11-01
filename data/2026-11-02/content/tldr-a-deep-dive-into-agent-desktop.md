---
title: A deep dive into agent-desktop
url: https://flaviocopes.com/agent-desktop
site_name: tldr
content_file: tldr-a-deep-dive-into-agent-desktop
fetched_at: '2026-11-02T08:48:34.750566'
original_url: https://flaviocopes.com/agent-desktop
date: '2026-11-02'
published_date: '2026-11-01T20:41:00.000Z'
description: agent-desktop is Vercel Labs' CLI for computer use on macOS, Windows, and Linux. Agents drive desktop apps through the accessibility tree and stable refs.
tags:
- tldr
---

~~~

agent-desktop is a command line tool fromVercel Labs. A coding agent uses it to see a desktop app and operate it.

It reads the operating system’s accessibility tree. That is the structure a screen reader already uses. Each control comes back as JSON, with a ref the agent can click, type into, or read. The loop stays in your agent. agent-desktop is the tool, not the model.

Chris Tate introduced it on 31 October 2026. He called it “agent-browser, for your whole computer.” The post says it is computer use for any coding agent, on macOS, Windows, and Linux, that it runs in the background while you keep working, and that agents can use the computer in parallel, each with its own cursor. The post includes a demo video.

This guide was written againstagent-desktop 1.0.2. That is the npmlatestrelease, and thechangelog entryis dated 30 October 2026. Commands, flags, and error codes come from that release and from the repository docs. One section shows output from a real run on Ubuntu on 1 November 2026. I have not installed it on my Mac. Where the docs do not cover something, the section says so.

The package isApache-2.0. The npm page isagent-desktop. It lists Node 18 or newer, and it ships native binaries for macOS, Windows, and Linux, on x64 and ARM64.

## What is agent-desktop?

An agent often has a shell, a browser, and a pile of files. A lot of software still lives in a window: a settings pane, a desktop app, a dialog with no API.

agent-desktop is the CLI for that window. You install one binary. The agent runs commands. Each command prints one JSON object. The agent reads it, decides, and runs the next command.

agent-browseris the older sibling, and it stays inside a browser. I checked npm on 1 November 2026: agent-browser’slatestwas 0.41.1, described as a browser automation CLI for AI agents. You install it, then runagent-browser installto fetch Chrome for Testing. A snapshot is the accessibility tree of a page. Its quick start clicks a bare ref such as@e2.

agent-desktop is the same idea pointed at the whole desktop. Refs look different on purpose. A desktop ref includes the snapshot id, like@s8f3k2p9:e8. A bare@e8is rejected.

There is a short mention of agent-browser inwhich browser to give your AI agents on macOS. That post is about browsers. This one is about native windows. There is no separate agent-browser guide on this site.

agent-desktop
agent-browser
What it drives
Desktop apps on macOS, Windows, and Linux
A browser, Chrome for Testing by default
How it sees the UI
OS accessibility tree
Page accessibility tree
Ref shape
@<snapshot_id>:eN
Bare 
@eN
 in the quick start
Install
npm install -g agent-desktop
npm install -g agent-browser
, then 
agent-browser install
Homebrew
Not in the default catalog yet
brew install agent-browser
 is documented
License
Apache-2.0
Apache-2.0, also Vercel Labs

Both are CLIs. Neither one is a model, and neither one replaces the agent that decides what to do next.

## How does agent-desktop work?

The agent observes, acts, and observes again. The README’s macOS example is Finder:

agent-desktop
 snapshot
 --app
 Finder
 -i

agent-desktop
 click
 @s8f3k2p9:e8

agent-desktop
 snapshot
 --app
 Finder
 -i

-ikeeps interactive elements. The first snapshot assigns refs. The click uses a ref from that snapshot. The second snapshot is how the agent checks the result. There is no pixel match in that loop. Screenshots exist as a separate command when you want one.

How an agent drives a desktop app
The agent calls agent-desktop, which reads the accessibility tree and returns a ref. The agent acts on that ref, then snapshots again to check.
Coding agent
agent-desktop
Accessibility tree

A few rules sit under every command.

Refs belong to one snapshot.The id is part of the ref, so@sofkkd3q8w04y:e269names both the element and the snapshot that produced it. When the UI changes, an action returnsSTALE_REForAMBIGUOUS_TARGET. Snapshot again and use the new refs.

Several windows need a window id.Ifsnapshotcannot tell which window you mean, it returnsAMBIGUOUS_TARGETand lists candidate window ids inerror.details. Pass one with--window-id.

Dense apps get a skeleton first.snapshot --skeleton --app Slack -i --compactis the shallow map. Thensnapshot --root @s8f3k2p9:e3 -i --compactdrills into one region. Slack is the README’s example. I did not run Slack.

Headless is the default.A ref action goes through the accessibility API. It does not move the pointer, take focus, synthesize keys, or use the clipboard. The global--headedflag allows physical input. The docs say not to flip--headedjust to recover from a headless failure. A raw--xycoordinate never implies focus.

PowerShell treats@as splat.Quote the ref:'@s8f3k2p9:e8'. cmd.exe and bash do not need that quoting.

On macOS, CLI calls reuse a private command host per snapshot namespace and binary build. The host keeps native accessibility objects so a removed row cannot silently resolve to a surviving row with the same identifier. The host exits after 15 idle minutes.TMPDIRmust be owned by the current user with mode0700. The usual per-user temporary directory already is.

Every command prints one envelope. Success looks like this, from the JSON contract:

{

 "version"
: 
"2.5"
,

 "ok"
: 
true
,

 "command"
: 
"click"
,

 "data"
: {

 "action"
: 
"click"
,

 "disposition"
: { 
"delivery"
: 
"delivered_unverified"
, 
"retry"
: 
"unsafe"
 }

 }

}

versionhere is the envelope schema,"2.5", not the CLI release. The CLI release shows up insideversioncommand data, as"1.0.2".

## How do you install agent-desktop?

The documented install is global npm, on macOS, Windows, or Linux:

npm
 install
 -g
 agent-desktop

agent-desktop
 version

Bun, Yarn, and pnpm can install the same package. A non-global install lands in./node_modules/.bin. Run it withnpx agent-desktop, or install globally.

Thepostinstallscript replaces a Node launcher with a link to the native binary. The install doc says that native link is about 21 ms per call. If the package manager blocks install scripts, and npm 12 does by default, the Node launcher stays and each call costs about 146 ms. A one-time notice on stderr tells you, which is a 1.0.2 change. Approve the script withnpm install-scripts approve agent-desktop, or install with--allow-scripts.

You can also download the native archive fromGitHub Releases. Keep the helper beside the executable. Upgrade by replacing both from the same release. Checksums catch corruption. They do not prove the archive came from the project. The docs give this check:

gh
 attestation
 verify
 <
downloaded-archiv
e
>
 --repo
 vercel-labs/agent-desktop

I did not run that attestation.

Official Homebrew and Scoop packages are being submitted. They are not in the default catalogs. The repo no longer maintains a custom tap or bucket. An older custom install can shadow the new binary. Check withcommand -v agent-desktopon macOS and Linux, orGet-Command agent-desktopon Windows.

Building from source needs Rust 1.89 or later, plus Xcode command line tools on macOS 13 or newer, MSVC on Windows, or a C linker on Linux:

git
 clone
 https://github.com/vercel-labs/agent-desktop
 && 
cd
 agent-desktop

cargo
 build
 --release
 -p
 agent-desktop

On Linux, also buildagent-desktop-linuxand keepagent-desktop-linux-clipboard-ownerbeside the CLI. npm and the release archives already include that helper.

The Linux check on this page used a user prefix, so it did not need root:

npm
 install
 -g
 agent-desktop
 --prefix
 "
$HOME
/.local"

npm added the package.agent-desktop versionthen printed:

{

 "version"
: 
"2.5"
,

 "ok"
: 
true
,

 "command"
: 
"version"
,

 "data"
: {

 "os"
: 
"linux"
,

 "target"
: 
"x86_64"
,

 "version"
: 
"1.0.2"

 }

}

That machine is Ubuntu 24.04.5 LTS, x86_64, glibc 2.39. The docs name Ubuntu 24.04 or newer with GNOME 46 as the measured desktop, and a glibc 2.35 floor. This session was XFCE on X11, not GNOME, and not Wayland.at-spi2-corewas already installed. The shell was not the graphical session, so the run copiedDISPLAYandDBUS_SESSION_BUS_ADDRESSfrom that session before any command could see apps. A TTY or SSH shell without the session bus, the display, and the runtime directory cannot see those apps. That matches the install doc.

## Which permissions does each OS need?

Runagent-desktop permissionsbefore you automate anything. It reports state and does not prompt.

### macOS

macOS 13 or newer, Intel or Apple Silicon. Accessibility has to be granted to the app that launches agent-desktop: Terminal, iTerm2, Warp, VS Code, Codex, or whichever host you actually use. macOS 27 and later name that list Device Control and Data Access. If System Settings also lists theagent-desktopbinary, grant that too.

permissions --requestcan prompt.permissions --guideopens System Settings at the missing permission and returns immediately. The result includesguide:started,already_running, ornot_needed. The guide covers Accessibility and Screen Recording only. It does not prompt.

Screenshots, andsession start --screenshots, need Screen Recording. Opening Notification Center needs Automation permission for System Events. Automation reportsunknownwhen macOS would have to prompt. 1.0.2 makes--guideoffer the app that launched the CLI, not only the binary. After a missing permission, the command host restarts, so the next call sees a new grant without restarting the launching app.

I did not run any of this on a Mac. The paragraph is the macOS skill and the install doc.

### Windows

Windows 10 1809 or newer, or Server 2019 or newer, x64 or ARM64. Apps at your terminal’s integrity level need no extra grant.permissionsreports automation asnot_required. An admin app can be read. Only an elevated agent can send it input. Elevated input from a medium caller maps toPERM_DENIED. That boundary is UIPI.

The binary is unsigned. SmartScreen may warn on a browser download. Antivirus may quarantine it. Smart App Control on a clean Windows 11 install can block it. The npm install path does not trigger SmartScreen.--guidereturnsPLATFORM_NOT_SUPPORTEDoff macOS.

Session 0, Server Core, the secure desktop (UAC, sign-in), a locked desktop, and another user’s session are not supported.launchtakes an absolute path, or a bare name under System32 or the Windows directory, with or without.exe.notepadworks. A display name such as “Google Chrome” does not.

typeandright-clickneed--headed. Headless text goes throughset-value. Minimized windows report offscreen and ref actions fail.restore, then snapshot again. These blocked shortcuts refuse without--force:alt+f4,win+l,win+d,alt+tab,win+r,win+x,win+e,ctrl+shift+esc, and modifier supersets. In combos,cmdandmetaare the Windows key.

I did not run the CLI on Windows. Those limits are the Windows skill.

### Linux

The primary measured target is Ubuntu 24.04 or newer with GNOME 46. Ubuntu 22.04’s ATK bridge aborts onAction.GetActions. Other distributions need the at-spi2-core bridge fix the Linux skill names asdc0dc33. Run inside the signed-in user’s graphical session.

agent-desktop statusactivates and checks the accessibility bus. An emptysupported_surfaceslist means the bus did not answer. It does not mean the desktop is empty.

X11 and Wayland both work, and they differ. X11 keys need XTEST. Wayland keys need GNOME Mutter RemoteDesktop. The Wayland clipboard needswl-clipboard. On Wayland, app pointer input refuses, and native window control is unsupported.focus-windowrequires X11.

On the XFCE X11 run,statusreturned granted accessibility, automationnot_required, screen recordingnot_required, and surfaceswindow,sheet,alert, andmenu.permissions --guideexited 1:

{

 "version"
: 
"2.5"
,

 "ok"
: 
false
,

 "command"
: 
"permissions"
,

 "error"
: {

 "code"
: 
"PLATFORM_NOT_SUPPORTED"
,

 "message"
: 
"start_permission_guide is not supported on this platform"
,

 "suggestion"
: 
"Use a platform/build that advertises this capability or choose a supported command"
,

 "disposition"
: { 
"delivery"
: 
"not_delivered"
, 
"retry"
: 
"safe"
 }

 }

}

That is the documented non-macOS result, not a broken install.

The state root is~/.agent-desktop. It must be private, mode700, orsnapshotfails withINTERNAL.AGENT_DESKTOP_HOMErelocates it. The path has to be absolute. Nothing is appended to it.

--apptakes the namelist-appsprints, or a desktop-entry name or id. It does not take a window title. Chromium and Qt apps need a launch flag or variable before they show up on the bus. The Linux skill documents those flags. I did not retest Chrome here, even though the machine has it.

## How do you connect it to Claude Code, Codex, or Cursor?

agent-desktop does not document a separate plugin for Claude Code, Codex, Cursor, or OpenCode. It does not document an MCP server. GitHub topics on the repo are not a server config. If you were looking for a JSON block to paste into one product’s MCP settings, that wiring is not documented yet.

What is documented is a skill, plus a paragraph inAGENTS.md.

The binary carries docs that match its version:

agent-desktop
 skills
 get
 desktop

agent-desktop
 skills
 get
 platform

agent-desktop
 snapshot
 --help

skills get desktopreturns markdown in the JSON envelope, underdata.content. References load the same way:agent-desktop skills get desktop commands-observation, and the same forcommands-interaction,commands-system, andworkflows.

Install the skill fromskills.sh:

npx
 skills
 add
 https://github.com/vercel-labs/agent-desktop
 --skill
 agent-desktop

Or add this toAGENTS.md, which is the README’s text:

Use 
`agent-desktop`
 to see and operate desktop apps. Before the first use, run

`agent-desktop skills get desktop`
 and 
`agent-desktop skills get platform`
, and follow them.

Any agent that can run a shell can call the binary after that. The agent’s own approval rules still apply. Those arepermission modes. They are separate from the OS accessibility grant.

Products also ship their own computer-use features. Those are different tools.

Codex has a Computer Use plugin in the desktop app. I wrote that up inhow to use the Codex desktop app. Cursor hasCursor Computer Use. The built-in options include a Claude Codecomputer-useserver on macOS, the Codex plugin, and Cursor computer use on Cloud Agents and self-hosted machines. These are separate from agent-desktop.

Use the product’s own computer-use feature when you are already inside that product and the task fits it. Use agent-desktop when you want one CLI, the accessibility tree, and the same commands from whichever agent has a shell.

## Which commands does it have?

The README counts 60 command names, 56 of them operational.key-down,key-up,mouse-down, andmouse-uprefuse to run until a daemon can release a held key or button.

Group
Commands
Observe
snapshot
, 
find
, 
get
, 
is
, 
screenshot
, 
list-surfaces
Act on a ref
click
, 
double-click
, 
triple-click
, 
right-click
, 
type
, 
set-value
, 
clear
, 
focus
, 
select
, 
toggle
, 
check
, 
uncheck
, 
expand
, 
collapse
, 
scroll
, 
scroll-to
Keyboard and mouse
press
, 
hover
, 
drag
, 
mouse-move
, 
mouse-click
, 
mouse-wheel
, plus the four held-input commands that refuse for now
Apps and windows
launch
, 
close-app
, 
list-apps
, 
list-windows
, 
list-displays
, 
focus-window
, 
resize-window
, 
move-window
, 
minimize
, 
maximize
, 
restore
, 
open-system-surface
Notifications
list-notifications
, 
dismiss-notification
, 
dismiss-all-notifications
, 
notification-action
Clipboard
clipboard-get
, 
clipboard-set
, 
clipboard-clear
Wait
wait
Sessions
session
, 
trace
, 
cursor-overlay
System
status
, 
permissions
, 
version
, 
batch
, 
skills

batchruns entries in order in one process. It is not a transaction. Unknown fields are rejected. Nestedbatchis rejected.--stop-on-errorstops at the first failure.

Auto-wait is on by default. A ref action polls until the target is actionable, then fails withTIMEOUT.CONCEPTS.mdsets the bound at 5000 ms, andtypeadds 30 ms per character.--timeout-ms 0is a single shot.launch --timeoutdefaults to 30000 ms.set-value --timeout-msdefaults to 5000.

Platform support, from the README:

macOS
Windows
Linux
Accessibility tree
Yes
Yes
Yes, AT-SPI
Click, type, keyboard
Yes
Yes
AT-SPI, plus X11 or GNOME keys
Mouse input
Yes
Yes
X11 with 
--headed
Screenshot
Yes
Yes
X11 windows, Wayland portal
Clipboard
Yes
Yes
Yes, Wayland needs 
wl-clipboard
App and window management
Yes
Yes
Launch and list, X11 window control
Notifications
Yes
Yes
GNOME Shell
Shell surfaces
Planned
Yes
GNOME tray and Action Center

agent-desktop skills get platformprints the table for the OS you are on. Shell surfaces go throughopen-system-surface.

Each release also shipslibagent_desktop_ffi, a C library so a program can call the tool in process.agent-desktop skills get fficovers entry points, memory, and threads. Build it withcargo build --profile release-ffi -p agent-desktop-ffi. I did not call the library.

### What a Linux run of 1.0.2 returned

The app was Mousepad, the XFCE text editor. A file/tmp/ad-test/note.txtalready containedhello from agent-desktopand a newline. The launch asked Mousepad to open that file and wait for a window:

agent-desktop
 launch
 mousepad
 --activate
 --arg
 /tmp/ad-test/note.txt

The envelope saidok, pid 3317, window title/tmp/ad-test/note.txt - Mousepad, bounds 642 by 509, accessible, visible, not minimized.list-apps --app mousepadthen showed it in the foreground.

snapshot --app mousepad -i --compactreturned snapshot idsofkkd3q8w04y,ref_count271,completetrue. Most of those 271 refs were menu items, including a long filetype menu. The text field was one node:

{

 "role"
: 
"textfield"
,

 "name"
: 
null
,

 "ref_id"
: 
"@sofkkd3q8w04y:e269"
,

 "available_actions"
: [
"SetValue"
, 
"TypeText"
, 
"SetFocus"
],

 "states"
: [
"focused"
]

}

Reading it:

agent-desktop
 get
 @sofkkd3q8w04y:e269
 --property
 value

data.valuewas"hello from agent-desktop\n".

A bare ref failed, exit code 1:

{

 "version"
: 
"2.5"
,

 "ok"
: 
false
,

 "command"
: 
"get"
,

 "error"
: {

 "code"
: 
"INVALID_ARGS"
,

 "message"
: 
"Invalid ref_id '@e269': expected @<snapshot_id>:e<N>"
,

 "disposition"
: { 
"delivery"
: 
"not_delivered"
, 
"retry"
: 
"safe"
 }

 }

}

The suggestion in the live envelope pointed at an example like@s8f3k2p9:e1.

Setting the same words back, without the trailing newline in the argument:

agent-desktop
 set-value
 @sofkkd3q8w04y:e269
 'hello from agent-desktop'

The result wasok.disposition.deliverywasdelivered_verified,retrywasunsafe, andverification_scopewaselement_value. The step name wasEditableText.SetTextContents, mechanismsemantic_api. A followinggetshowed the accessibility value without the newline.

That did not save the file.set-valuechanged the unsaved buffer. The file on disk stayed the original echo, newline included, which is what a later force-close left behind.

find --app mousepad --role button --name New --exactfound one button, ref@srhu9kybmxlyy:e1, stateoffscreen, on a new snapshot id. I did not click it. A skeleton snapshot of the same app returned 79 refs andcomplete: true.

screenshot --app mousepad /tmp/ad-test/mousepad.pngwrote a PNG, 642 by 509, scale factor 1. On this X11 session, screenshot worked whilescreen_recordingwasnot_required. That matches the Linux skill for X11 windows. It says nothing about a Wayland portal prompt, which this run never hit.

Closing without--forcefailed. Mousepad had a Save Changes dialog because the buffer was dirty:

{

 "ok"
: 
false
,

 "command"
: 
"close-app"
,

 "error"
: {

 "code"
: 
"ACTION_FAILED"
,

 "message"
: 
"Process 3317 has 1 open dialog(s), so no close request was sent to them"
,

 "disposition"
: { 
"delivery"
: 
"delivered_unverified"
, 
"retry"
: 
"unsafe"
 },

 "details"
: { 
"cause"
: 
"dialog_pending"
, 
"dialog"
: 
"Save Changes"
 }

 }

}

The message says no close request was sent. The disposition saysdelivered_unverified. Both are in the envelope, so the guide keeps both. The suggestion mentioned a save prompt, or--force, which discards unsaved work.

close-app mousepad --forcethen succeeded, methodforce,delivered_verified, evidenceprocess_instance_exited.list-apps --app mousepadreturned an empty app list. The file on disk was still the original line.

Before Mousepad,snapshot --app thunarfailed withWINDOW_NOT_FOUNDand the messageApplication 'thunar' is running but has no matching window. Thunar was inlist-appsas a background app.list-windowswith no app, andlist-windows --app thunar, both returned"data": []. Launch with--activatewas what produced a window the snapshot could see.

## Can several agents use the desktop at once?

A session is a folder under~/.agent-desktop/sessions/<id>/.session startprints asession_id. It does not attach later processes by itself. Pass--session, or setAGENT_DESKTOP_SESSION. The flag wins. Tracing is on unless you pass--no-trace.--screenshotsstores unredacted PNGs. Keep those private.

The cursor overlay is presentation. It does not move the OS pointer, and it does not change which actions are allowed.session start --cursororcursor-overlay enableturns it on.data.rendered: falsemeans the setting was saved and nothing was drawn.

Parallel cursors aresession start --cursor --multi-agent. The harness assigns a stable--agent-id, orAGENT_DESKTOP_AGENT_ID. An id is 1 to 64 letters, digits,-, or_. Desktop UI actions then require an agent id. Observations, clipboard commands, and session admin do not.

On the Linux run:

agent-desktop
 session
 start
 --name
 mousepad-test
 --cursor
 --multi-agent
 --no-trace

The envelope returned session idrun-1793563261320-3497-0, trace off,cursor_overlay.enabledtrue,multi_agenttrue, andrenderedfalse. The Linux skill says that start returnsrendered: falseuntil an agent acts. On X11, each agent id then gets its own cursor. On Wayland, none is drawn. I did not send a later action with--agent-id, so this run did not confirm that a cursor was actually drawn.

Parallel cursors share one input lease
Each agent id gets its own overlay cursor. Headless actions still take turns on one interaction lease, so physical input stays serial.
One session
Agent one cursor
Agent two cursor
Interaction lease
The OS pointer

Headless actions move their overlay cursor before they take the lease. Several cursors can travel at once. The actions still take turns. Snapshots stay shared by the session.cursor-overlay disableandsession endstop every cursor.

On macOS, the overlay is click-through. Reduce Motion skips travel and dwell.--travel-ms MIN,MAXneeds both numbers at least 30, with MIN at or below MAX. Travel max plus--dwell-msmust be at most 700 ms, or the command returnsINVALID_ARGS. On Windows, overlay travel is for headless semantic actions.--headedmoves the real cursor.

session endon that id returned the same session id and anended_attimestamp. I did not open a second agent against it.

If you are splitting work across helpers, thesubagentspage is about context windows inside Claude Code, Codex, and Cursor. agent-desktop’s agent id is narrower. It only names a cursor and a lease inside one desktop session.

## Can you keep working while it runs?

The background behavior Tate described is the headless default. Semantic ref actions do not steal focus and do not move the OS pointer. You can keep using the machine while those actions run.

--headedis the other mode. Physical input takes the pointer, and the interaction lease serializes that input. On Windows, headedtypeuses SendInput into the foreground queue. There is no separate “background mode” command beyond this policy. The macOS command host is the idle process that exits after 15 minutes. It is not a second product mode.

Do not mix this up with Codex Computer Use on Windows, which uses foreground input of its own. That is Codex’s plugin, documented in the Codex guide. agent-desktop’s headless path is the one that stays off your pointer.

Two GTK clicks on one button less than about 250 ms apart act once on Linux, and both can still answerokwithdelivered_unverified. Wait for the effect between clicks. A terminal text node does not accept headlesstype(POLICY_DENIED). A GTK4 secret field can show text. Only a password role is withheld.

## How I would use agent-desktop

I build Mac apps, and I let agents test them in a VM so the clicks stay off the machine I am typing on. That setup ishow to let coding agents test Mac apps in a VM.

I would install agent-desktop inside that VM, grant Accessibility to the terminal that launches it, and put the skill paragraph in the project’sAGENTS.md. The task would be an app that has no CLI for the flow I care about: open a window, snapshot, act on a ref, snapshot again, and stop. I would rather have the agent read a button’s name from the tree than guess a coordinate from a screenshot.

I would keep it off my everyday desktop. The CLI can click, type, read window text, and close apps. A VM with test data is the place for that. I would not point it at a logged-in mail client or a password manager on the machine I use all day.

Concrete jobs that match the commands, without pretending I have done them with this tool:

* Launch an app, wait until it has a window, snapshot, and read a field. The Mousepad run above is that shape.
* Set a text field withset-valuewhen you do not want keystrokes or focus. Remember that this edits the control, not necessarily the file on disk.
* Find a control by role and name when the full tree is hundreds of refs.
* Give two subagents two agent ids and two overlay cursors, and still expect their physical input to take turns.
* Screenshot one window when you want an image for yourself. The agent does not need that image to click.

A browser flow still belongs in a browser tool.Playwrightis the one I would reach for in a test suite. Gemini Computer Use with Playwright is the screenshot-and-coordinate loop, in a browser. agent-desktop is the native app next to those, not a replacement for them.

## What will it refuse to do?

A few limits are worth knowing before you write a prompt around them.

Held keys and buttons do not work yet.key-down,key-up,mouse-down, andmouse-uprefuse until something can release them.

Protected processes cannot be closed. The match is exact, not a substring, so a lookalike name stays closable. The code isINVALID_ARGSwithnot_delivered, notPERM_DENIED. CONCEPTS.md defines a protected process as a session-critical OS process. Closing it would take down the desktop session.

On macOS, quit shortcuts returnPOLICY_DENIEDunless you pass--force:cmd+q,cmd+shift+q,cmd+alt+esc,ctrl+cmd+q, andcmd+shift+delete. Useclose-appto quit.

Retry only whenerror.disposition.retryissafe. The contract says onlynot_deliveredis safe to retry.delivered_unverifiedmeans something may have landed. Sending it again can double the action.recoveryis present only when retry issafe.

A verified element value is not an application save. The Mousepad field read back the new text. The file on disk did not change. Readverification_scopeand, when you care about the file, check the file.

open-system-surfaceis planned on macOS, present on Windows, and limited to GNOME shell surfaces on Linux. I did not exercise notifications or shell surfaces. On XFCE there was no GNOME Shell to ask.

Wayland window control, Wayland cursors, macOS permission prompts, Windows UIPI, SmartScreen, the FFI library, the optional JEV helper, and a drawn multi-agent cursor were not part of the Linux run.

## How do you read an error?

Exit codes, from the JSON doc:0is success,1is a structured error on stdout,2is a parse error that still prints an envelope withINVALID_ARGS.

error.code,error.message, anderror.dispositionare always there.suggestion,recovery,platform_detail, anddetailsare omitted when empty.

Code
Meaning
PERM_DENIED
Accessibility permission not granted
ELEMENT_NOT_FOUND
No element matched the ref or query
APP_NOT_FOUND
App not running, or no windows. Nothing was sent
STALE_REF
The ref could not be found in the live UI
AMBIGUOUS_TARGET
More than one plausible target
SNAPSHOT_NOT_FOUND
Snapshot id missing or expired
POLICY_DENIED
Physical or headed path blocked by policy
ACTION_FAILED
Rejected, or the observed result contradicted the request
ACTION_NOT_SUPPORTED
The target does not expose that action
APP_UNRESPONSIVE
The matching app stopped responding
PLATFORM_NOT_SUPPORTED
This OS does not implement the method
TIMEOUT
The wait expired
INVALID_ARGS
Bad arguments, including a bare ref
WINDOW_NOT_FOUND
No such window
NOTIFICATION_NOT_FOUND
Notification id not found
INTERNAL
Unexpected error, including a state root that is not private

deliveryis one ofunknown,not_delivered,delivery_uncertain,delivered_unverified, ordelivered_verified. Treatunknownas unsafe to retry automatically.

When a snapshot runs out of budget, envelope 2.2 returnsok: truewithcomplete: falseand the tree it did observe, instead of aTIMEOUTand no tree. Readdata.complete. A--rootdrill-down is different: an incomplete observation there still returnsTIMEOUT.

## Is this safe to point at your real desktop?

The native CLI does not call a remote model. What it reads can still be private. Snapshots, clipboard reads, screenshots, command output, debug HTML, and session traces can contain whatever is on the screen. TheFAQsays to keep those out of public logs. Redaction in trace lines does not make a screenshot safe to publish.--screenshotsstores unredacted PNGs.

The optional JEV helper, inskills/jev-desktop/SKILL.md, sends goals and screen descriptions to a configured provider. Value suppression does not remove private text from labels, titles, ancestor paths, or the goal. It is separate from the native CLI. I did not run it.

agent-desktop’s own docs do not name prompt injection from on-screen content. A window title or a button label is still text your agent will read.Prompt injectionis the general problem: untrusted text that tries to steer the agent. Anthropic’scomputer use security notessay web pages and images can carry that text, and they recommend a dedicated VM, minimal privileges, no sensitive logins, a domain allowlist, and a person confirming actions that have real consequences. That advice is about their tool. It is still the right shape for any agent that can click.

agent-desktop does not document a sandbox of its own. A coding agent’ssandboxlimits files and hosts for shell commands. A desktop click can sit outside that boundary, because it talks to other apps through the accessibility API. If the task can spend money, send a message, or delete data, run it where the blast radius is a VM and a test account.

SECURITY.mdis the vulnerability report path: GitHub advisories, for the CLI, the npm package, the FFI library, releases, Actions, and adapters. It is not a threat model of desktop automation.

Quit shortcuts and protected processes are the guardrails the tool itself enforces. They are not a substitute for choosing what the agent is allowed to see.

## How does it compare with other computer-use tools?

These are different products. The column that matters is who performs the click.

Tool
What it drives
How it points
Who performs the action
agent-desktop 1.0.2
Native apps
Accessibility refs
The CLI, called by your agent
agent-browser 0.41.1
A browser
Page refs
The CLI
Anthropic computer use
A screen you attach
Screenshot, then coordinates. Toolset 
computer_toolset_20260801
Your application runs every call
OpenAI computer use
A browser or desktop interface
Screenshots and mouse or keyboard via 
ComputerToolset
Your app supplies the driver
Playwright
A browser
Selectors in a test
Your test code
Gemini Computer Use
Browser, Android, or a desktop environment
Screenshot in, click or type coordinates out
Your code. The guide on this site uses Playwright for the browser case
Cursor Computer Use
Desktop apps and the iOS Simulator, inside Cursor
Cursor’s own flow
Cursor’s agent
Codex Computer Use
macOS and Windows apps, in the Codex app
The Computer Use plugin
Codex

Anthropic’s current toolset has member tools such asscreenshot,left_click,type, andzoom. The docs say it is not available in Claude Managed Agents, and they point webpage-only tasks at a browser tool instead. Their reference environment includes Xvfb. Use their page for the sample code.

OpenAI’s guide says computer use lets a model operate a browser or desktop interface. Page text and controls go throughBrowserToolset. A browser hosted by OpenAI is a separate Agents API guide. The page lists hosted partners, including Browserbase, Browser Use, Daytona, and E2B. I checked that guide on 1 November 2026. A product named Operator was not on it, so this page leaves Operator out.

Playwright remains the tool for a repeatable browser test. Gemini’s computer-use model is a coordinate loop on top of a screen. agent-desktop is the path that skips coordinates when the OS can name the control.

## What do you do when a command fails?

Start withagent-desktop statusandagent-desktop permissions. On Linux, empty surfaces usually mean the bus, not an empty desktop. Put the CLI in the graphical session’s environment.

WINDOW_NOT_FOUNDwhilelist-appsshows the process means the app has no window yet.launch --activatewaits for one. The Thunar miss at the start of the Linux run was this case.

INVALID_ARGSon a ref usually means the ref is bare, or it came from a different snapshot or session. Use the qualified ref from the latest snapshot in the same session.

STALE_REFmeans snapshot again. Do not reuse the old id.

AMBIGUOUS_TARGETmeans pass--window-id.

PLATFORM_NOT_SUPPORTEDonpermissions --guideis expected off macOS. Grant permissions with the OS settings on macOS, and do not look for that guide on Linux or Windows.

ACTION_FAILEDwith a dialog pending means something is asking to save. Decide whether to save, or pass--forceand accept the discarded buffer.

POLICY_DENIEDontypeoften means the action wants--headed, or the control has no headless text path. On Windows,set-valueis the headless write. On Linux, a terminal text node refuses headless type.

PERM_DENIEDon macOS is the Accessibility grant, for the app that launched the CLI. On Windows it can be an integrity mismatch: you can read an elevated app, and you cannot send it input unless the agent is elevated too.

INTERNALright after install, on Linux, can be a state root that other users can write.chmod 700 ~/.agent-desktop.

If npm feels slow, check whether install scripts were blocked. The Node launcher is the about-146 ms path. The native link is the about-21 ms path.command -v agent-desktoptells you which binary you are actually running.

## FAQ

### Does agent-desktop need screenshots?

No. The core loop is the accessibility tree and refs.screenshotis optional. The FAQ says agents do not need screenshots or pixel matching to click, type, inspect menus, or move through windows.

### Which version is this guide about?

1.0.2, checked on 1 November 2026, envelope schema 2.5. A later release can add commands.agent-desktop versionandagent-desktop skills get desktopmatch the binary you installed, which is a better check than this page once you have upgraded.

### Can I use it from Claude Code, Codex, Cursor, and OpenCode?

You can run the CLI from any of them if that agent can run a shell. The documented setup is the skill from skills.sh, or theAGENTS.mdparagraph above. A dedicated integration for each product is not documented yet.

### Does it work on Windows and macOS the way the Linux section shows?

The project documents all three. The transcript on this page is Linux, XFCE, X11, agent-desktop 1.0.2. macOS and Windows behavior is in the platform skill:agent-desktop skills get platform.

### Is the cursor overlay the real mouse?

No. It is a drawing on top of the session. The OS pointer stays put during headless actions. Headed actions are the ones that move the real pointer.

### Willset-valuesave my document?

It writes the control. In the Mousepad run it updated the accessibility value and left the file on disk unchanged. Saving is a separate app command, often a button or a shortcut, and some shortcuts are blocked unless you pass--force.

### Where are the docs?

The repo README,docs/install.md,docs/json-output.md,docs/faq.md,CONCEPTS.md, and the skills printed by the binary. The npm package isagent-desktop. agent-browser isvercel-labs/agent-browser.

Tagged: 
AI
 · 
All topics
Follow @flaviocopes

Want me to talk about your product? You cansponsor this site.

~~~

Related posts about ai:

* How to use Hex for voice dictation
* How Claude Code mods change the agent loop
* What to do when an AI tool exposes your provider keys
* How to package and publish an OpenCode plugin
* How to run an LLM locally on macOS, Linux, and Windows
* Proton's AI manifesto and what it means to lead coding agents
* Try Muse Spark Open in OpenCode through Ollama Cloud
* Research keywords through OpenSEO MCP