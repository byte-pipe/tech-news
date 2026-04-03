---
title: 'Git: Don’t create .gitkeep files, use .gitignore instead - Adam Johnson'
url: https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/
site_name: hnrss
content_file: hnrss-git-dont-create-gitkeep-files-use-gitignore-instea
fetched_at: '2026-02-22T11:08:29.800165'
original_url: https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/
date: '2026-02-20'
description: Git only tracks files, not directories. It will only create a directory if it contains a tracked file. But sometimes you need to “track” a directory, to ensure it exists for fresh clones of a repository. For example, you might need an output directory called build.
tags:
- hackernews
- hnrss
---

# Git: Don’t create.gitkeepfiles, use.gitignoreinstead

2023-09-18

Git only tracks files, not directories. It will only create a directory if it contains a tracked file. But sometimes you need to “track” a directory, to ensure it exists for fresh clones of a repository. For example, you might need an output directory calledbuild.In this post, we’ll look at two ways to achieve this. First, the common but slightly flawed.gitkeeptechnique, then a simpler one using only a.gitignorefile.## The.gitkeeptechniqueThis technique uses an empty file called.gitkeep:build
└── .gitkeepThe empty file ensures that Git creates the directory with minimal cost. Any other filename may be used, as Git doesn’t treat.gitkeepfiles any differently.To set this up, you might create an empty file withtouch:$touchbuild/.gitkeepThen ignore all files in the directory, except.gitkeep, by adding patterns in the repository’s.gitignorefile:/build/*!/build/.gitkeepThe first pattern ignores everything in thebuilddirectory. The second one then un-ignores the.gitkeepfile, allowing it to be committed.This technique works, but it has some downsides:It requires editing two files.If the directory is renamed,.gitignoreneeds updating, which is easy to miss..gitkeepis not a name recognized by Git, so there’s no documentation on it, potentially confusing other developers.There’s a better way that doesn’t have these flaws.## The better.gitignoretechniqueThis technique uses only a short.gitignorefile inside the directory:build
└── .gitignoreThe.gitignorefile has these contents:*!.gitignoreThe first pattern ignores all files in the directory. The second one then un-ignores the.gitignorefile, so it can be committed.You can create this file withechoand file redirection:$echo'*\n!.gitignore'>build/.gitignoreWhen you add and commit the directory, Git will pick up on the.gitignorefile first, skipping other files within the directory:$gitaddbuild$gitstatusOn branch mainChanges to be committed:new file: build/.gitignore$gitcommit-m"Track build directory"[main1cc9120]Track build directory1 file changed, 2 insertions(+)create mode 100644 build/.gitignoreThe directory is now “tracked” with a single, standard file that will work even after renames.## FinDon’t ignore this technique,—Adam😸😸😸 Check out my new book on using GitHub effectively,Boost Your GitHub DX! 😸😸😸Subscribe viaRSS,Twitter,Mastodon, or email:Your email address:One summary email a week, no spam, I pinky promise.Related posts:Git: Output the top-level directory of the current repositoryGit: Output just the current branch nameGit: How to add and remove execute permissionsTags:git
