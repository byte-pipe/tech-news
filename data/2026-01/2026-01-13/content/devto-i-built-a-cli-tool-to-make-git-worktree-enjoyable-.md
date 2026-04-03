---
title: I Built a CLI Tool to Make Git Worktree Enjoyable - DEV Community
url: https://dev.to/kexi/i-built-a-cli-tool-to-make-git-worktree-enjoyable-4fh3
site_name: devto
fetched_at: '2026-01-13T19:08:19.144210'
original_url: https://dev.to/kexi/i-built-a-cli-tool-to-make-git-worktree-enjoyable-4fh3
author: Kei Nakayama
date: '2026-01-08'
description: Introduction The AI world never stops evolving, and the start of this year has been busy... Tagged with git, cli, productivity, deno.
tags: '#git, #cli, #productivity, #deno'
---

# Introduction

The AI world never stops evolving, and the start of this year has been busy with keeping up with new technologies and building things. To streamline my development workflow, I created a CLI tool called"vibe"that makes managing Git Worktrees much easier.

https://github.com/kexi/vibe

# What is Git Worktree?

Git Worktree is a built-in Git feature that allows you to have multiple branches checked out simultaneously from a single repository.

Normally, when switching branches usinggit checkoutorgit switch, the file contents change completely. This creates several challenges:

* You need to stash or temporarily commit work-in-progress changes
* Development servers and build processes restart
* Editors and IDEs reload

Git Worktree solves these problems.By creating a new worktree in a separate directory, you can work on a different branch while keeping the original branch intact.

# Traditional approach

git checkout main
git checkout
-b
 feature/new-feature
# Work on main is interrupted

# Using Worktree

git worktree add ../new-feature feature/new-feature
# Work on main continues

Enter fullscreen mode

Exit fullscreen mode

This enables workflows like:

* Creating a worktree for urgent bug fixes while implementing features on another branch
* Running a dev server on branch A while reviewing or investigating on branch B
* Running multiple AI Agents on different branches simultaneously

## Worktree vs. Cloning Multiple Repositories

You might think: "Why not just clone the repository multiple times?" Git Worktree has clear advantages over this approach:

### Disk Space and Clone Time Savings

With multiple clones, each creates its own.gitdirectory containing the entire repository history. Git Worktreeshares Git objects, significantly reducing disk usage.

Clone time is also dramatically reduced. Multiple clones require runninggit clonerepeatedly, but with Git Worktree,you only clone once, then usegit worktree addto create new working directories. Sincegit worktree adddoesn't need to download Git objects and only checks out the working directory, it completes almost instantly.

# Multiple clones

project1/.git
# e.g., 500MB (30 seconds to clone)

project2/.git
# e.g., 500MB (30 seconds to clone)

project3/.git
# e.g., 500MB (30 seconds to clone)

# Total: 1.5GB, 90 seconds

# Git Worktree

project/.git
# e.g., 500MB (initial clone: 30 seconds)

project-worktree1/
# Worktree only (adds in seconds)

project-worktree2/
# Worktree only (adds in seconds)

# Total: 500MB + minimal overhead, 30 seconds + seconds

Enter fullscreen mode

Exit fullscreen mode

For large repositories or parallel work on multiple branches, this difference is significant.

### Centralized Git Operations

All worktrees share the same.gitdirectory, providing these benefits:

* Single fetch/pull: Runninggit fetchin one worktree updates all of them
* Unified branch list: View all branches and worktree states from any worktree
* Shared configuration:.git/configsettings apply to all worktrees

# With clones: fetch needed in each directory

cd
project1
&&
 git fetch

cd
project2
&&
 git fetch

cd
project3
&&
 git fetch

# With Worktree: one fetch updates everything

cd
project
&&
 git fetch

Enter fullscreen mode

Exit fullscreen mode

### Prevents Confusion

Managing multiple clones makes it easy to lose track of "which directory am I working in?" With Git Worktree,git worktree listgives you a clear overview, making management straightforward.

$
git worktree list
/path/to/project abc1234
[
main]
/path/to/project-feature def5678
[
feature/new-ui]
/path/to/project-hotfix ghi9012
[
hotfix/critical-bug]

Enter fullscreen mode

Exit fullscreen mode

For these reasons, I strongly recommend using Git Worktree over multiple clones for parallel work.

# Why I Built vibe

Git Worktree is a powerful feature, but after runninggit worktree add, there's often a routine workflow: copying files like.env, runningnpm install, building, etc.

With AI Agents becoming more capable, parallel development is becoming the norm. These routine tasks started feeling heavy, and I wanted a lighter way to handle them. That's why I built this tool.

# What is vibe?

vibeis a CLI tool that manages the creation, setup, and deletion of Git Worktrees. It's built with Deno and works across various operating systems.

# Installation

On macOS, you can install via Homebrew:

brew
install
kexi/tap/vibe

Enter fullscreen mode

Exit fullscreen mode

Deno (JSR), Linux, and Windows are also supported. See the repository README for details:https://github.com/kexi/vibe#installation

# Usage

## Creating a Worktree

Usevibe start <branch>to create a worktree. It handles directory creation and checks for existing worktrees interactively.

vibe start feat/new-feature

Enter fullscreen mode

Exit fullscreen mode

## Automation with Configuration Files

Place a.vibe.tomlin your project root to define worktree creation behavior.

.vibe.toml:

[copy]

files

=

[
".env"
,

"config/*.json"
]

dirs

=

[
"node_modules"
,

".cache"
]

[hooks]

pre_start

=

[
"echo 'Preparing worktree...'"
]

post_start

=

[
"pnpm install"
,

"claude"
]

pre_clean

=

[
"git stash"
]

post_clean

=

[
"echo 'Cleanup complete'"
]

Enter fullscreen mode

Exit fullscreen mode

Configuration options:

* files: Files to copy (supports glob patterns like**/*.json)
* dirs: Directories to copy entirely (optimized with Copy-on-Write). On CoW-enabled filesystems (APFS, Btrfs, etc.), copyingnode_modulesis nearly instant and dramatically reducesnpm installtime.
* Hooks: Execute commands at different stagespre_start: Before worktree creationpost_start: After worktree creationpre_clean: Before worktree deletionpost_clean: After worktree deletion
* pre_start: Before worktree creation
* post_start: After worktree creation
* pre_clean: Before worktree deletion
* post_clean: After worktree deletion

This is optimized for workflows where you copy.envand config files right after creating a worktree, run setup commands likepnpm install, and then immediately launch an AI Agent likeclaudeto start coding.

### Local Configuration Override

You can create a.vibe.local.tomlfile to extend or override the shared configuration. This is useful for separating team-wide settings from personal preferences.

.vibe.local.toml:

[hooks]

post_start

=

[
"pnpm install"
,

"code ."
]

# Use VS Code instead of claude

Enter fullscreen mode

Exit fullscreen mode

Add.vibe.local.tomlto your.gitignoreto keep personal settings out of version control.

This brings the lead time from worktree creation to coding start down to nearly zero. Once you experience jumping straight into AI pair programming without breaking your train of thought, you won't want to go back.

## Deleting Worktrees

When you're done, usevibe cleanto delete the worktree.

vibe clean

Enter fullscreen mode

Exit fullscreen mode

For detailed usage and configuration options, see the repository documentation:https://github.com/kexi/vibe

# Conclusion

When doing parallel work with Git Worktree, vibe saves you the hassle of environment setup and file copying, making your workflow more efficient. It's especially useful when running multiple AI Agents on different branches simultaneously.

Give vibe a try!

For feature requests or bug reports, please open an issue on the repository:

https://github.com/kexi/vibe

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
