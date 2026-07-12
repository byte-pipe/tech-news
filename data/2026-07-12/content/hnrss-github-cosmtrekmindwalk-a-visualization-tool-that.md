---
title: 'GitHub - cosmtrek/mindwalk: A visualization tool that replays coding-agent sessions on a 3D map of your codebase. · GitHub'
url: https://github.com/cosmtrek/mindwalk
site_name: hnrss
content_file: hnrss-github-cosmtrekmindwalk-a-visualization-tool-that
fetched_at: '2026-07-12T19:27:36.111568'
original_url: https://github.com/cosmtrek/mindwalk
date: '2026-07-12'
description: A visualization tool that replays coding-agent sessions on a 3D map of your codebase. - cosmtrek/mindwalk
tags:
- hackernews
- hnrss
---

cosmtrek

 

/

mindwalk

Public

* NotificationsYou must be signed in to change notification settings
* Fork10
* Star282

 
 
 
 
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

34 Commits
34 Commits
.claude
.claude
 
 
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
cmd/
mindwalk
cmd/
mindwalk
 
 
internal
internal
 
 
schema
schema
 
 
scripts
scripts
 
 
testdata
testdata
 
 
web
web
 
 
.gitignore
.gitignore
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
.impeccable.md
.impeccable.md
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
View all files

## Repository files navigation

# mindwalk

A visualization tool that replays coding-agent sessions on a 3D map of your codebase.

mindwalk-demo.mp4

The 30-second demo — sound on.

## The problem

A session log records what an agent did, but not how it understood the task:
which parts of the repo it treated as relevant, where it explored before it
acted, whether its footprint matched the scope you had in mind. Reading the
raw JSONL line by line doesn't answer any of that.

## The idea

Draw the repository as a night map, and play the session back as light moving
through it: where the agent searched, read, and edited, the map glows —
everything else stays dark. The agent's understanding of the task becomes a
shape you can see at a glance. One Go binary reads Claude Code and Codex
session logs, fully local; no session data leaves your machine.

## Quick start

curl -fsSL https://raw.githubusercontent.com/cosmtrek/mindwalk/master/scripts/install.sh 
|
 sh

export
 PATH=
"
$HOME
/.local/bin:
$PATH
"

mindwalk

The installer verifies the binary againstchecksums.txtand installs to~/.local/bin(override withINSTALL_DIR; pin a release withVERSION).
Windows archives are onGitHub Releases.
To build from source:make setup && make build→bin/mindwalk.

With no arguments, mindwalk scans~/.claude/projectsand~/.codex/sessions,
serves the UI on a random local port, and opens a browser:

mindwalk serve [--port N] [--no-open] [--claude-dir DIR] [--codex-dir DIR]
mindwalk open [--no-open] <session.jsonl> open one specific session
mindwalk build <repo> [-o out] write the repository citymap JSON
mindwalk trace <session> [-o out] write the normalized trace JSON

## Reading the picture

* Tree / Terrain views— the repo as a radial tree or a treemap plain;
glow ∝ how deeply and how often a file was touched.
* Touch states— each file keeps its deepest touch: seen (moss green),
read (moon white), edited (warm amber), unvisited (dark). The HUD folds
friction signals — error rate, churned files, edits after the last verify —
into a review strip.
* Playback deck— scrub or play the session over a bucketed histogram of
the run. Bars sit on a cool/warm spectrum: observation stays cool (search,
read, exec), mutation glows warm (edit, verify), so editing phases jump out
at a glance.
* Timeline marks—◇context compactions,○subagent launches,›user turns; every mark is a click-to-jump target.
* Inspector— click a file to pin its visit history; click a visit row to
jump the playhead to that moment.

Keyboard:Spaceplay/pause ·←/→step (⇧×10) ·Home/Endends ·Sspeed ·Enext edit ·Xnext error ·Mnext mark ·⌘Bsession rail.

## Under the hood

Two artifacts, kept deliberately separate:

1. atrace— the session log normalized into an ordered stream of
file-touch events (internal/adapter, one adapter per agent format);
2. acitymap— a deterministic layout of the repository
(internal/citymap); the same tree always produces the same map, so
replays are comparable across sessions.

A local Go server (internal/server) joins the two and serves the
React/Three.js frontend (web).schema/mirrors the exported JSON contracts.

## Contributing

Issues and pull requests are welcome. To get a working dev setup:

make setup 
#
 install frontend dependencies

make serve 
#
 dev server on :8765, serving web/dist from the working tree

make 
test
 
#
 go test + frontend build — run before sending a PR

make build 
#
 regenerate embedded assets and bin/mindwalk

Ground rules (seeAGENTS.mdfor the full architecture notes):

* Keep the boundaries: adapters don't know about rendering, citymap generation
doesn't depend on playback, the server just connects the two.
* Keep Go codegofmt-ed; never hand-editinternal/server/static—
regenerate it withmake build.
* When trace or citymap JSON shapes change, updateschema/and the relevant
tests in the same change.

## License

MIT© 2026 Ricko Yu

## About

A visualization tool that replays coding-agent sessions on a 3D map of your codebase.

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

282

 stars
 

### Watchers

0

 watching
 

### Forks

10

 forks
 

 Report repository

 

## Releases1

v0.1.0

 Latest

 

Jul 11, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go47.6%
* TypeScript42.3%
* CSS8.2%
* HTML1.2%
* Other0.7%