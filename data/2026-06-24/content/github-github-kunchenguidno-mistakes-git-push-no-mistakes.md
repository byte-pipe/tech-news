---
title: 'GitHub - kunchenguid/no-mistakes: git push no-mistakes · GitHub'
url: https://github.com/kunchenguid/no-mistakes
site_name: github
content_file: github-github-kunchenguidno-mistakes-git-push-no-mistakes
fetched_at: '2026-06-24T19:35:44.972461'
original_url: https://github.com/kunchenguid/no-mistakes
author: kunchenguid
description: git push no-mistakes. Contribute to kunchenguid/no-mistakes development by creating an account on GitHub.
---

kunchenguid

 

/

no-mistakes

Public

* NotificationsYou must be signed in to change notification settings
* Fork131
* Star1.9k

 
 
 
 
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

360 Commits
360 Commits
.github/
workflows
.github/
workflows
 
 
.no-mistakes/
evidence
.no-mistakes/
evidence
 
 
cmd
cmd
 
 
docs
docs
 
 
internal
internal
 
 
skills/
no-mistakes
skills/
no-mistakes
 
 
.gitignore
.gitignore
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
demo.gif
demo.gif
 
 
demo.mp4
demo.mp4
 
 
demo.tape
demo.tape
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install_script_test.go
install_script_test.go
 
 
makefile_test.go
makefile_test.go
 
 
release-please-config.json
release-please-config.json
 
 
workflow_ci_test.go
workflow_ci_test.go
 
 
workflow_docs_test.go
workflow_docs_test.go
 
 
workflow_guard_generated_files_test.go
workflow_guard_generated_files_test.go
 
 
workflow_no_mistakes_required_test.go
workflow_no_mistakes_required_test.go
 
 
workflow_release_test.go
workflow_release_test.go
 
 
View all files

## Repository files navigation

# git push no-mistakes

### Kill all the slop. Raise clean PR.

English·简体中文

no-mistakesputs a local git proxy in front of your real remote.
Push tono-mistakesinstead oforigin, and it spins up a disposable worktree, runs an AI-driven validation pipeline, forwards the branch to the configured push target only after every check passes, and opens a clean PR automatically.

* Non-blocking- the pipeline runs in an isolated worktree without disrupting your work.
* Agent-agnostic-claude,codex,rovodev,opencode,pi, oracp:<target>viaacpx.
* Agent-native-/no-mistakeslets your coding agent do a task and gate it, or gate existing committed work: it runs the pipeline, has the pipeline apply safe fixes, and escalates the rest to you.
* Human stays in charge- auto-fix or review findings, your call.
* Clean PRs by default- push, open PR, watch CI, and auto-fix failures in one shot.

Full documentation:https://kunchenguid.github.io/no-mistakes/

## How it works

 your branch
 │ git push no-mistakes
 ▼
 ┌──────────────────────────────────────────────┐
 │ disposable worktree — your work stays put │
 │ review → test → docs → lint → push → PR → CI │
 └──────────────────────────────────────────────┘
 │ every check green
 ▼
 clean PR, opened for you

Each step either passes on its own or stops with afindingfor you to act on.
Safe, mechanical fixes are applied automatically; anything that touches your intent is escalated for you toapprove,fix, orskip.
Nothing reaches the configured push target until every check is green.

## Install

curl -fsSL https://raw.githubusercontent.com/kunchenguid/no-mistakes/main/docs/install.sh 
|
 sh

Windows, Go install, and build-from-source instructions are in theinstallation guide.

## Quick Start

$ no-mistakes init
 ✓ Gate initialized

 repo /Users/you/src/my-repo
 gate no-mistakes → /Users/you/.no-mistakes/repos/abc123def456.git
 remote git@github.com:you/my-repo.git
 skill /no-mistakes installed 
for
 agents at user level

 Push through the gate with:
 git push no-mistakes 
<
branch
>

$ git checkout my-branch

#
 do some work in the branch...

$ git push no-mistakes
 
*
 Pipeline started

 Run no-mistakes to review.

$ no-mistakes

#
 opens the TUI for the active run

For GitHub fork contributions, keeporiginpointed at the parent repository and initialize withno-mistakes init --fork-url <your-fork-url>.

From the TUI you act on eachfinding:auto-fixones are applied for you (or approve to let them),ask-userones are a judgement call you approve, fix, or skip.
Once every check is green, the gate forwards your branch to the configured push target and opens the PR for you, so there is no manualgit push originand no hand-written PR body.
Prefer to let your coding agent drive the same flow headlessly?
Use/no-mistakes(see below).

## Three ways to trigger the gate

Every change runs through the same pipeline. Pick the entry point that fits how you're working when the change is ready:

* git push no-mistakes- the explicit Git path. Push a committed branch to the gate remote instead oforigin.
* no-mistakes- the TUI. Run it after making changes (no commit needed) and a wizard walks you through creating a branch, committing, and pushing through the gate, then attaches to the run.no-mistakes -ydoes all of that automatically.
* /no-mistakes- the agent skill. Tell the coding agent to do a task and gate it with/no-mistakes <task>, or use bare/no-mistakesto gate existing committed work. It runs the pipeline, has the pipeline apply safe fixes, and stops to ask you about anything that needs a human call.

no-mistakes initinstalls the/no-mistakesskill for Claude Code and other agents. Under the hood the skill drivesno-mistakes axi, a non-interactive TOON interface to the same approval flow.

See thequick startfor the full first-run walkthrough.

## Development

make build 
#
 Build bin/no-mistakes with version info

make 
test
 
#
 Run go test -race ./... (excludes the e2e suite)

make e2e 
#
 Run the tagged end-to-end agent journey suite

make e2e-record 
#
 Re-record e2e fixtures when agent wire formats change

make lint 
#
 Check generated skill drift and run go vet ./...

make skill 
#
 Regenerate committed no-mistakes skill files

make fmt 
#
 Run gofmt -w .

make demo 
#
 Regenerate demo.gif and demo.mp4 (needs vhs and ffmpeg)

make docs 
#
 Build the Astro docs site in docs/dist

SeeMakefilefor the full target list.

make e2e-recordoverwritesinternal/e2e/fixtures/from the realclaude,codex, andopencodeCLIs, spends real API quota, and should be reviewed before committing.

## Star History

## About

git push no-mistakes

kunchenguid.github.io/no-mistakes/

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.9k

 stars
 

### Watchers

4

 watching
 

### Forks

131

 forks
 

 Report repository

 

## Releases71

v1.30.1

 Latest

 

Jun 21, 2026

 

+ 70 releases

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go99.8%
* Makefile0.2%