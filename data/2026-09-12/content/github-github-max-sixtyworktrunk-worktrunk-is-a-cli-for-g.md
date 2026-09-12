---
title: 'GitHub - max-sixty/worktrunk: Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows · GitHub'
url: https://github.com/max-sixty/worktrunk
site_name: github
content_file: github-github-max-sixtyworktrunk-worktrunk-is-a-cli-for-g
fetched_at: '2026-09-12T13:52:44.734203'
original_url: https://github.com/max-sixty/worktrunk
author: max-sixty
description: Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows - max-sixty/worktrunk
---

max-sixty

 

/

worktrunk

Public

* NotificationsYou must be signed in to change notification settings
* Fork250
* Star7k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

5,046 Commits
5,046 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.cargo
.cargo
 
 
.claude-plugin
.claude-plugin
 
 
.claude/
skills
.claude/
skills
 
 
.codex
.codex
 
 
.config
.config
 
 
.github
.github
 
 
benches
benches
 
 
dev
dev
 
 
docs
docs
 
 
hooks
hooks
 
 
nix
nix
 
 
plugins/
worktrunk
plugins/
worktrunk
 
 
skills
skills
 
 
src
src
 
 
templates
templates
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.typos.toml
.typos.toml
 
 
.worktreeinclude
.worktreeinclude
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
Taskfile.yaml
Taskfile.yaml
 
 
build.rs
build.rs
 
 
dist-workspace.toml
dist-workspace.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
gemini-extension.json
gemini-extension.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

# Worktrunk

September 2026: Worktrunk wasreleasedat the start of the year, and has quickly become the most popular git worktree manager. It's built with love (there's no slop!). Please let me know any frictions at all; I'm intensely focused on continuing to make Worktrunk excellent, and the biggest help is folks posting problems they perceive.

Worktrunk is a CLI for git worktree management, designed for running AI agents in parallel.

Worktrunk's three core commands make worktrees as easy as branches. Plus, Worktrunk has a bunch of quality-of-life features to simplify working with many parallel changes, including hooks to automate local workflows.

A quick demo:

### 📚 Full documentation atworktrunk.dev📚

## Context: git worktrees

AI agents like Claude Code and Codex can handle longer tasks without
supervision, such that it's possible to manage 5-10+ in parallel. Git's native
worktree feature give each agent its own working directory, so they don't step
on each other's changes.

But the git worktree UX is clunky. Even a task as small as starting a new
worktree requires typing the branch name three times:git worktree add -b feat ../repo.feat, thencd ../repo.feat.

## Worktrunk makes git worktrees as easy as branches

Worktrees are addressed by branch name; paths are computed from a configurable template. Commands that take a branch also accept the path of the worktree it is checked out in.

Start with the core commands

Core commands:

Task

Worktrunk

Plain git

Switch worktrees

wt switch feat

cd ../repo.feat

Create + start Claude

wt switch -c -x claude feat

git worktree add -b feat ../repo.feat && \
cd ../repo.feat && \
claude

Clean up

wt remove

cd ../repo && \
git worktree remove ../repo.feat && \
git branch -d feat

List with status

wt list

git worktree list
 (paths only)

Expand into the more advanced commands as needed

Workflow automation:

* Hooks— run commands on create, pre-merge, post-merge, etc
* LLM commit messages— generate commit messages from diffs
* Merge workflow— squash, rebase, merge, clean up in one command
* Interactive picker— browse worktrees with live diff and log previews
* Share build caches— ten worktrees gettarget/,node_modules/, etc without building or copying them (on APFS, btrfs, and XFS)
* wt list --full—CI statusandAI-generated summariesper branch
* PR checkout—wt switch pr:123to jump straight to a PR's branch
* Dev server per worktree—hash_porttemplate filter gives each worktree a unique port
* Aliases&per-branch variables— customwt <name>commands and branch-scoped state for hook templates
* ...andlots more

Multiple parallel agents, same simple commands:

## Install

Homebrew (macOS & Linux):

brew install worktrunk 
&&
 wt config shell install

Shell integration allows commands to change directories.

Cargo:

cargo install worktrunk 
&&
 wt config shell install

Windows & other

Windows.wtdefaults to Windows Terminal's command, so Winget additionally installs Worktrunk asgit-wtto avoid the conflict:

winget install max-sixty.worktrunk
git-wt config shell install

Alternatively, disable Windows Terminal's alias (Settings → Apps → Advanced app settings → App execution aliases → "Terminal"/"Terminal Preview") to usewtdirectly.

Free code signing provided bySignPath.io, certificate bySignPath Foundation—policy.

Arch Linux:

sudo pacman -S worktrunk 
&&
 wt config shell install

Conda / Pixi(community-maintainedfeedstock):

conda install -c conda-forge worktrunk 
&&
 wt config shell install

Or withPixi:pixi global install worktrunk && wt config shell install.

## Quick start

Create a worktree for a new feature:

$ 
wt switch --create feature-auth

✓ Created branch feature-auth from main and worktree @ ~/repo.feature-auth

This creates a new branch and worktree, then switches to it. Do your work, then check all worktrees withwt list:

$ 
wt list

 Branch Status HEAD± main↕ main…± Remote⇅ Commit Age Message

@ feature-auth + ↑ +27 -8 ↑1 +31 4bc72dc 2h Add authenticati…

^ main ^⇡ ⇡1 0e631ad 1d Initial commit

○ Showing 2 worktrees, 1 with changes, 1 ahead, hidden: Path

The@marks the current worktree.+means staged changes,↑1means 1 commit ahead of main,⇡means unpushed commits.

When done, either:

PR workflow— commit, push, open a PR, merge via GitHub/GitLab, then clean up:

wt step commit 
#
 commit staged changes

gh pr create 
#
 or glab mr create

wt remove 
#
 after PR is merged

Local merge— squash, rebase onto main, fast-forward merge, clean up:

$ 
wt merge main

◎ Generating commit message and committing changes... (2 files, +53, no squashing needed)

 Add authentication module

✓ Committed changes @ a1b2c3d

◎ Merging 1 commit to main @ a1b2c3d (no rebase needed)

 * a1b2c3d Add authentication module

 auth.rs | 51 +++++++++++++++++++++++++++++++++++++++++++++++++++

 lib.rs | 2 ++

 2 files changed, 53 insertions(+)

✓ Merged to main (1 commit, 2 files, +53)

◎ Removing feature-auth worktree & branch in background (same commit as main, _)

○ Switched to worktree for main @ ~/repo

For parallel agents, create multiple worktrees and launch an agent in each:

wt switch -x claude -c feature-a -- 
'
Add user authentication
'

wt switch -x claude -c feature-b -- 
'
Fix the pagination bug
'

wt switch -x claude -c feature-c -- 
'
Write tests for the API
'

The-xflag runs a command after switching; arguments after--are passed to it. Configurepost-start hooksto automate setup (install deps, start dev servers).

## Next steps

* Learn the core commands:wt switch,wt list,wt merge,wt remove
* Set uphooksfor automated setup
* ExploreLLM commit messages,interactive
picker,Claude Code integration,CI
status & PR links
* Browsetips & patternsfor recipes: aliases, dev servers, databases, agent handoffs, and more
* Extending Worktrunk— customize workflows with hooks & aliases
* Runwt --helporwt <command> --helpfor quick CLI reference

## Further reading

* Claude Code: Best practices for agentic coding— Anthropic's official guide, including the worktree pattern
* Shipping faster with Claude Code and Git Worktrees— incident.io's workflow for parallel agents
* Git worktree pattern discussion— Community discussion in the Claude Code repo
* @DevOpsToolbox's video on Worktrunk
* git-worktree documentation— Official git reference

## Contributing

* ⭐ Star the repo
* Tell a friend about Worktrunk
* Open an issue— feedback, feature requests, even a small friction or imperfect user message, ora worktree pain not yet solved
* Share:X·Reddit·LinkedIn

### 📚 Full documentation atworktrunk.dev📚

### Star history