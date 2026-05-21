---
title: 'GitHub - Helvesec/rmux: Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows. · GitHub'
url: https://github.com/helvesec/rmux
site_name: hnrss
content_file: hnrss-github-helvesecrmux-universal-rust-multiplexer-wit
fetched_at: '2026-05-22T06:00:47.787306'
original_url: https://github.com/helvesec/rmux
date: '2026-05-21'
description: Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows. - Helvesec/rmux
tags:
- hackernews
- hnrss
---

Helvesec

 

/

rmux

Public

* NotificationsYou must be signed in to change notification settings
* Fork11
* Star460

 
 
 
 
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

661 Commits
661 Commits
.github/
workflows
.github/
workflows
 
 
benches
benches
 
 
crates
crates
 
 
docs
docs
 
 
resources/
windows
resources/
windows
 
 
scripts
scripts
 
 
spec
spec
 
 
src
src
 
 
tests
tests
 
 
xtask
xtask
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.fr.md
README.fr.md
 
 
README.ja.md
README.ja.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
build.rs
build.rs
 
 
deny.toml
deny.toml
 
 
rmux.1
rmux.1
 
 
View all files

## Repository files navigation

Universal Rust multiplexer for the agentic era: detachable, scriptable, and inspectable, with a tmux-compatible CLI, daemon-backed SDK, and nativeRatatuiintegration.

English ·Français·简体中文·日本語

Important

Current release:v0.2.0, published on18 May 2026. All 90 tmux-compatible commands are implemented, but bugs are expected — this is a fresh public preview. Pleasefile issuesif you hit one.

## Why RMUX

RMUX exists because I believe the tmux use case has only been partially explored. My own starting point was simple: I wanted to run long-lived agents over SSH without losing their terminals, while still being able to inspect, script, and orchestrate everything around them.

So I rebuilt that idea from scratch in Rust: a blazing-fast, tmux-compatible multiplexer with a typed SDK, persistent sessions, structured snapshots, and native local transports on Linux, macOS, and Windows, including Windows Named Pipes. No WSL required.

RMUX is usable by agents, headless CLI workflows, and humans alike: you can give terminal apps detachable execution, reconnect later, inspect their state, drive them from code, or simply use it for normal tmux-style terminal work.

## Demos

Short, real examples of what RMUX can be used for.

Multi Agents Orchestration
≃ 514 lines

Agent Broadcast Arena
≃ 2,171 lines

Mini-Zellij
≃ 944 lines

Terminal <> Browser Mirroring
≃ 649 lines

Playwright Testing
≃ 1,495 lines

## Install

Prebuilt binary for macOS and Linux:

curl -fsSL https://rmux.io/install.sh 
|
 sh

Prebuilt binary for Windows PowerShell:

irm https:
//
rmux.io
/
install.ps1 
|
 iex

Direct downloads and SHA256 checksums are available from thev0.2.0 GitHub Release.

From crates.io with Cargo:

cargo install rmux --locked

From a local checkout:

cargo install --path 
.
 --locked

For Rust applications:

cargo add rmux-sdk
cargo add ratatui-rmux

## Documentation

The full RMUX documentation is available atrmux.io/docs.

It includesinstallation guides,CLI references,SDK examples,terminal automation examples, andAPI documentation.

## CLI Quickstart

rmux new-session -d -s work
rmux split-window -h -t work
rmux send-keys -t work 
'
echo "hello from rmux"
'
 Enter
rmux attach-session -t work

Use command help locally:

rmux list-commands
rmux new-session --help
rmux split-window --help

## SDK Quickstart

[
dependencies
]

rmux-sdk
 = 
"
0.2
"

tokio
 = { 
version
 = 
"
1
"
, 
features
 = [
"
rt-multi-thread
"
, 
"
macros
"
] }

use
 std
::
time
::
Duration
;

use
 rmux_sdk
::
{

 
EnsureSession
,
 
EnsureSessionPolicy
,
 
Rmux
,
 
SessionName
,
 
TerminalSizeSpec
,

}
;

#
[
tokio
::
main
]

async
 
fn
 
main
(
)
 -> rmux_sdk
::
Result
<
(
)
>
 
{

 
let
 rmux = 
Rmux
::
builder
(
)

 
.
default_timeout
(
Duration
::
from_secs
(
5
)
)

 
.
connect_or_start
(
)

 
.
await
?
;

 
let
 session_name = 
SessionName
::
new
(
"work"
)
.
expect
(
"valid session name"
)
;

 
let
 session = rmux
 
.
ensure_session
(

 
EnsureSession
::
named
(
session_name
)

 
.
policy
(
EnsureSessionPolicy
::
CreateOrReuse
)

 
.
detached
(
true
)

 
.
size
(
TerminalSizeSpec
::
new
(
120
,
 
32
)
)
,

 
)

 
.
await
?
;

 
let
 pane = session
.
pane
(
0
,
 
0
)
;

 pane
.
send_text
(
"printf 'ready
\\
n' && sleep 1
\n
"
)
.
await
?
;

 pane
.
wait_for_text
(
"ready"
)
.
await
?
;

 
let
 snapshot = pane
.
snapshot
(
)
.
await
?
;

 
println
!
(
"{}x{}"
,
 snapshot
.
cols
,
 snapshot
.
rows
)
;

 
Ok
(
(
)
)

}

## Ratatui Widget

use
 ratatui
::
{
buffer
::
Buffer
,
 layout
::
Rect
,
 widgets
::
Widget
}
;

use
 ratatui_rmux
::
{
PaneState
,
 
PaneWidget
}
;

use
 rmux_sdk
::
PaneSnapshot
;

fn
 
render
(
snapshot
:
 
PaneSnapshot
,
 
area
:
 
Rect
,
 
buffer
:
 
&
mut
 
Buffer
)
 
{

 
let
 state = 
PaneState
::
from_snapshot
(
snapshot
)
;

 
PaneWidget
::
new
(
&
state
)
.
render
(
area
,
 buffer
)
;

}

## Architecture

Three public surfaces — armuxCLI, armux-sdkRust crate, and aratatui-rmuxwidget — share a single local protocol to talk to the daemon. Anything one surface can do, the others can do too.

## Workspace

Crate

Role

Publication

rmux-types

Shared platform-neutral value types

public

rmux-proto

Detached IPC DTOs, framing, wire-safe errors

public

rmux-os

Small OS boundary helpers

public

rmux-ipc

Local IPC endpoints and transports

public

rmux-sdk

Daemon-backed Rust SDK

public

ratatui-rmux

Ratatui integration widget

public

rmux-pty

PTY allocation, resize, child process control

support crate

rmux-core

Sessions, panes, layouts, formats, hooks, buffers

support crate

rmux-server

Tokio daemon and request dispatch

support crate

rmux-client

Local IPC client and attach plumbing

support crate

rmux

CLI and hidden daemon entrypoint

public binary

rmux-render-core

Shared snapshot rendering core

workspace-internal

## Platform Support

Platform

PTY backend

IPC backend

Default endpoint

Linux

Unix PTY

Unix socket

/tmp/rmux-{uid}/default

macOS

Unix PTY

Unix socket

/tmp/rmux-{uid}/default

Windows

ConPTY

Named pipe

per-user named pipe

## Configuration

On Linux and macOS, RMUX reads.rmux.conffrom the standard system and user locations:

1. /etc/rmux.conf
2. ~/.rmux.conf
3. $XDG_CONFIG_HOME/rmux/rmux.conf
4. ~/.config/rmux/rmux.conf

On Windows, RMUX reads.rmux.confas well, from the following locations:

1. %XDG_CONFIG_HOME%\rmux\rmux.conf
2. %USERPROFILE%\.rmux.conf
3. %APPDATA%\rmux\rmux.conf
4. %RMUX_CONFIG_FILE%

## Verification

The workspace is designed to be checked from source with locked dependencies:

cargo fmt --all -- --check
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo 
test
 --workspace --locked --no-fail-fast

Additional local checks:

scripts/cfg-check.sh
scripts/unsafe-check.sh
scripts/no-network-in-runtime.sh
scripts/check-platform-neutrality.sh
scripts/ratatui-rmux-budget.sh
scripts/verify-package.sh

Release artifact checks are driven by:

scripts/release-local.sh
scripts/package-unix.sh

#![forbid(unsafe_code)]is used in the upper-level crates. OS and terminal boundary code is isolated in the lower-level runtime crates.

## License

RMUX is dual-licensed under either:

* MIT License
* Apache License 2.0

at your option.

## About

Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows.

rmux.io

### Topics

 windows

 macos

 linux

 agent

 rust

 cli

 terminal

 ai

 powershell

 tokio

 multiplexer

 multiplexers

 ratatui

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

460

 stars
 

### Watchers

2

 watching
 

### Forks

11

 forks
 

 Report repository

 

## Releases3

v0.2.0

 Latest

 

May 18, 2026

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust98.9%
* Other1.1%