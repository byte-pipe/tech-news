---
title: 'Cleaning up merged git branches: a one-liner from the CIA''s leaked dev docs | spencer.wtf'
url: https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html
site_name: hackernews_api
content_file: hackernews_api-cleaning-up-merged-git-branches-a-one-liner-from-t
fetched_at: '2026-02-20T19:19:23.477507'
original_url: https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html
author: Spencer Dixon
date: '2026-02-20'
published_date: '2026-02-20T00:00:00+00:00'
description: How to delete all merged git branches locally with a single command. This one-liner has been in my zshrc since 2017 — I found it buried in the CIA's Vault7 l...
tags:
- hackernews
- trending
---

# Cleaning up merged git branches: a one-liner from the CIA's leaked dev docs

20 Feb 2026

In 2017, WikiLeaks published Vault7 - a large cache of CIA hacking tools and internal documents. Buried among the exploits and surveillance tools was something far more mundane:a page of internal developer documentation with git tips and tricks.

Most of it is fairly standard stuff, amending commits, stashing changes, using bisect. But one tip has lived in my~/.zshrcever since.

## The Problem

Over time, a local git repo accumulates stale branches. Every feature branch, hotfix, and experiment you’ve ever merged sits there doing nothing.git branchstarts to look like a graveyard.

You can list merged branches with:

git branch --merged

But deleting them one by one is tedious. The CIA’s dev team has a cleaner solution:

## The original command

git branch --merged | grep -v "\*\|master" | xargs -n 1 git branch -d

How it works:

* git branch --merged— lists all local branches that have already been merged into the current branch
* grep -v "\*\|master"— filters out the current branch (*) andmasterso you don’t delete either
* xargs -n 1 git branch -d— deletes each remaining branch one at a time, safely (lowercase-dwon’t touch unmerged branches)

## The updated command

Since most projects now usemaininstead ofmaster, you can update the command and exclude any other branches you frequently use:

git branch --merged origin/main | grep -vE "^\s*(\*|main|develop)" | xargs -n 1 git branch -d

Run this frommainafter a deployment and your branch list goes from 40 entries back down to a handful.

I keep this as a git alias so I don’t have to remember the syntax:

alias ciaclean='git branch --merged origin/main | grep -vE "^\s*(\*|main|develop)" | xargs -n 1 git branch -d'

Then in your repo just run:

ciaclean

Small thing, but one of those commands that quietly saves a few minutes every week and keeps me organised.
