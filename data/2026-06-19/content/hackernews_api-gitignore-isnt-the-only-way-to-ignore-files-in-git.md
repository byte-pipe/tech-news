---
title: .gitignore Isn’t the Only Way To Ignore Files in Git | Nelson Figueroa
url: https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/
site_name: hackernews_api
content_file: hackernews_api-gitignore-isnt-the-only-way-to-ignore-files-in-git
fetched_at: '2026-06-19T12:23:43.313981'
original_url: https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/
author: Nelson Figueroa
date: '2026-06-18'
published_date: '2026-06-18T00:00:00+00:00'
description: You can ignore files in .gitignore, .git/info/exclude, and ~/.config/git/ignore
tags:
- hackernews
- trending
---

I’ve been using Git for so long and I just realized you can ignore files at three different levels and not just with.gitignore. The three files you can use to ignore files are:

* .gitignore
* .git/info/exclude
* ~/.config/git/ignore

## .gitignore

.gitignoreis the usual file where you write files you want to ignore. It’s checked into Git along with the rest of the code. Whatever files you add to it will not get taken into account when runninggitcommands.

## .git/info/exclude

Theexcludefile lives in the.gitdirectory of every Git repository but changes to it are not checked into Git. It usually has a few comment lines on a fresh Git repository. This file is useful for ignoring things on a per-repo basis. For example, you may have a personalnotes.txtfile in a repository that you don’t want to check into git but you also don’t want to add to.gitignorebecause it’s unique to your workflow. In that case you would addnotes.txtto.git/info/exclude.

## ~/.config/git/ignore

Theignorefile lives in your machine’s home directory in~/.config/git/ignore. Whatever filenames are added to this file are ignored globally at a machine-level. This file is not checked into Git and isn’t associated with any particular repository. It’s a great place to add files that you want to ignore in every git repository on your computer. For example, if you’re on macOS, adding.DS_Storehere would be ideal.

You can customize the global ignore file to be a different file. For example, if you want your global git ignore file to be.gitignore_globalyou would run the command:

Shell
git config --global core.excludesFile ~/.gitignore_global

And if you ever want to return to the default setting, run:

Shell
git config --global --unset core.excludesFile

## Checking Which File Is Ignoring a Specific File

When adding filenames to any of these, you can use this command to check how a filename is being ignored. For example, if you want to check how.DS_Storeis being ignored, rungit check-ignore -v .DS_Storein any Git repository.

Here is the output when the repository’s.gitignoreis ignoring.DS_Store:

Console
$
 git check-ignore -v .DS_Store

.gitignore:1:.DS_Store	.DS_Store

Here is the output when the repository’s.git/info/excludeis ignoring.DS_Store:

Console
$
 git check-ignore -v .DS_Store

.git/info/exclude:7:.DS_Store	.DS_Store

Here is the output when the global~/.config/git/ignorefile is ignoring.DS_Store:

Console
$
 git check-ignore -v .DS_Store

/Users/nelson/.config/git/ignore:2:.DS_Store	.DS_Store

And here is the output when a custom global ignore file.gitignore_globalis ignoring.DS_Store:

Console
$
 git check-ignore -v .DS_Store

/Users/nelson/.gitignore_global:1:.DS_Store	.DS_Store

If there is nothing ignoring a file, thegit check-ignore -vcommand produces no output.