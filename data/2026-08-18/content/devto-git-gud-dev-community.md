---
title: Git Gud! - DEV Community
url: https://dev.to/francistrdev/git-gud-4e6g
site_name: devto
content_file: devto-git-gud-dev-community
fetched_at: '2026-08-18T12:11:53.651980'
original_url: https://dev.to/francistrdev/git-gud-4e6g
author: FrancisTRᴅᴇᴠ (っ◔◡◔)っ
date: '2026-08-17'
description: You heard me. Alright, that was mean lol. Though based on the title, you probably already knew the... Tagged with discuss, community, git, productivity.
tags: '#discuss, #community, #git, #productivity'
---

Transitioning from GitHub Desktop to CLI commands

You heard me.

Alright, that was mean lol. Though based on the title, you probably already knew the idea of this article.

Git was something we have all heard. Don't get confused with GitHub though.They are both different.

I have used Git, but not in a way most people have used it,which is via GitHub Desktop.I have used GitHub Desktop since the beginning because of its friendly UI and how it is easy to use.

So what's the issue?The issue is that I am using GitHub Desktop. I have "Git" on my resume and it just feels wrong since I have been using a UI.

I thought it would be a great idea of learning Git via CLI. That way, I can understand from both worlds of UI and in the command line! I know it's difficult sometimes to learn something new, so I thought it would be best to get community feedback on other commands I should learn and in hope this article will help other new and existing developers to fresh up some Git.

With that said,if you are a type of person who relies on UI for Git and want to learn some Git commands to get conformable with, this is the place to git gud! Here are some Git commands to get started that reflects to GitHub Desktop and will help you get started getting into the habit of using in the terminal!This list will go in order based on starting to somewhat finishing the task/project. I will also reference Hollow Knight: Silksong if you are a visual learner as well.

Note:This is based on my experience when learning Git Commands after moving away from the GitHub Desktop. If there is something I forgot to mention or any information that needs to be updated, let me know!

 

 

## 1. git init

If you are starting a new project, this is the first command you should do! Even if you have an existing project, but git isn't initialize, then it would be best to run this command!

Think of this as starting up a new game in Hollow Knight: Silksong. Starting up the game gives you more features to work with,which we will get into a bit.

Note:If you are cloning an existing project from GitHub that is already have git initialized, no need to do this command. You can if you want, but it would make no sense.

 

 

## 2. git cloneurl

Speaking of existing projects, if you want to grab an existing project and have it on your computer, this is the command!

For example, if you want to clone the Forem (dev.to) repository, you would clone via website url here:

More Specifically, copy the HTTPS link:

Then, in your VScode terminal, you would do:

git clone https://github.com/forem/forem.git

Enter fullscreen mode

Exit fullscreen mode

Think of this as you are opening up an existing file in the game. Simple as that.

If you are grabbing someone else's file and importing to your own machine, I would think of it as assuming they have everything installed. If the file is outdated, you will have to update it. For programming terms, if they don't have git, dogit init.

Note:Make sure you are in an empty folder when cloning the repository.

 

 

## 3. git addfilepath

Now you have a project and you make some changes in the project, like any other developer.

Before sending your changes to the branch on GitHub, you want to add the files you changed before doing the commit.

If you have change a lot of files and you want to include all of them in a commit, you would do:

git add 
.

Enter fullscreen mode

Exit fullscreen mode

However, if you want to include a specific file in a commit, you will have to find the file path. For example, if I change a file namedtests.jsand it lives in theappfolder, it would be:

git add /app/tests.js

Enter fullscreen mode

Exit fullscreen mode

 

### Extra Command to Know!

If you accidentally add all files to be tracked, you can revert by following the command to revert all files.

git restore 
.

Enter fullscreen mode

Exit fullscreen mode

For specific files, you would need the file path as usual.

git restore /app/tests.js

Enter fullscreen mode

Exit fullscreen mode

I would think of this as you play the game. Sometimes you equip charms, which I treat it as "Tracked files" where you have an inventory of items (untracked files). The equip items is what you want to use, while the inventory is the list of things you have collected/modified so far.

 

 

## 4. git commit -m "Hollow Purple"

Once you added the files based on the previous command, you are ready to commit! I treat this as a "checkpoint". It's like saving a game before you continue.

In the event where something went completely wrong, you can go back to the previous commit. For example, you have 3 commits:

 

A --> B --> C (You are here)

 

If you want to go back to "B", you will need to find the hash for Commit "B" and revert the commit by doing the following:

# Find the commit hash

git log

# Revert a specific commit

git revert <commit-hash>

Enter fullscreen mode

Exit fullscreen mode

Just like in the game, you can go back to your previous save point.

Pro Tip:Always make sure to fill out the commit message of what you did. It's best practice to say something likegit commit -m "Fix a rerouting bug"than sayinggit commit -m "Update file".

 

 

## 5. git push origin main

At this point, you have a lot of commits and changes. It's time to push it to the GitHub repository! This would be the command to do so!

However, it is best practice to fetch the changes that are on GitHub by doing the following:

git fetch origin main

Enter fullscreen mode

Exit fullscreen mode

Sometimes, if there were changes in the repository, but is not up-to-date in your local dev environment, then you would do the following after fetching:

git pull origin main

Enter fullscreen mode

Exit fullscreen mode

I would treat this as the version of the game. If the game is outdated, you would "fetch" the latest version and update the version from there. That way, the game will save properly.If you have a save data that is not align with the current version of the game, it will may likely lead to conflicts, which we would not cover since we are covering the basics.

 

 

## 6. Creating/Switching Branches

If you want to create a branch:

git branch nameBranch

Enter fullscreen mode

Exit fullscreen mode

To switch to that branch and work on the developments there:

git checkout existingBranch

Enter fullscreen mode

Exit fullscreen mode

Pro Tip:If you want a single command where it creates the branch and switching it at the same time, use the following command below. Discovery based on@inayicomment!

git checkout 
-b
 branchName

 

 

## 7. git status

The main thing it will show you are the files that are tracked and not tracked.The ones that are tracked is the ones is going to be commit. The untracked files are the ones that are changed, but is not part of the upcoming commit.This command provides information to help you keep track on which files are changed and which files are going to be part of the commit.

 

 

That is it. It's not perfect and there is a GOOD chance I am missing something, butit is at least a good start on moving away from using GitHub Desktop and getting into the habit of learning these commands.Of course, there is many more I did not cover such as thegit mergeand all, but I want to keep it simple. Besides, this is based on my experience and the commands I use frequently that is mentioned in this article.

If you would like to learn more about git, check out the official documentation here:https://git-scm.com/docs

That is only if you want to...

or be doomed.

Speaking of Doom, new trailer for Doomsday is here andit's just Doom Aura Farming lol.

# Special Request to the Reader before Commenting!

If there are other commands that are good to know, feel free to leave a comment while having this image as part of your comment!(see below).If you are stopping by, I would love to see just the image of Hornet saying "Git Gud!" :D

Add this as part of your comment!

 

 

Questions or Comments? Love to hear from you!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (16 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse