---
title: .gitignore everything by default - by Alex Pliutau
url: https://packagemain.tech/p/gitignore-everything-by-default
site_name: hnrss
content_file: hnrss-gitignore-everything-by-default-by-alex-pliutau
fetched_at: '2026-09-05T20:58:17.887761'
original_url: https://packagemain.tech/p/gitignore-everything-by-default
author: Alex Pliutau
date: '2026-09-05'
description: An opposite view on .gitignore files.
tags:
- hackernews
- hnrss
---

# .gitignore everything by default

### An opposite view on .gitignore files.

Alex Pliutau
Sep 05, 2026
5
2
Share

I think we’ve all been there. You’re working on a project, making commits, and then suddenly realize you’ve been committing .DS_Store files, node_modules, IDE configuration files, or other junk (CLAUDE.md for example) that shouldn’t be in your repository. Or even worse - environment variables. Then comes the embarrassing cleanup: adding these files to .gitignore, removing them from the repository history, and hoping that no one has noticed.

What if we flipped this approach entirely? Instead of allowing everything by default and selectively ignoring files, what if we ignored everything by default and only allowed specific files?

Here’s what this could look like in practice for a simple Go project:

*
!.gitignore
!*.go
!README.md
!go.mod
!go.sum

This.gitignorefile does exactly that:

* *- Ignore everything

But not these files...

* !.gitignore- the gitignore file itself
* !*.go- Go source files
* !go.mod- Go module file
* !go.sum- Go dependencies file
* anything else you wish to include

With this setup, only the files you explicitly allow will be tracked by Git. No more accidental commits of unintended local files.

The technique isn’t necessarily the right choice for every repository or developer, but is an alternative to explore.

Nowadays, I see that projects have so much crap locally, like various agentic docs or subfolders, so it may seem easier to just ignore everything at first.

Just look atthis 207-lines .gitignorefrom typescript-go.

p.s. if you want to check if the path is ignored by git, you can run this command:

git check-ignore -v internal/server/server.go

This can save a lot of head-scratching when a file you expected to track doesn’t appear in Git.

p.s. have you heard oflazygit? The best Git TUI out there, check it out.

Discuss this post on Hacker News.

5
2
Share
Previous