---
title: 10 Git Commands You’ll Wish You Knew Earlier - DEV Community
url: https://dev.to/sylwia-lask/10-git-commands-youll-wish-you-knew-earlier-4fcp
site_name: devto
content_file: devto-10-git-commands-youll-wish-you-knew-earlier-dev-co
fetched_at: '2026-08-26T11:26:50.955981'
original_url: https://dev.to/sylwia-lask/10-git-commands-youll-wish-you-knew-earlier-4fcp
author: Sylwia Laskowska
date: '2026-08-26'
description: Do you know Git?&nbsp;Of course you do! Today, I’ve got a few of my favorite Git commands for... Tagged with git, programming, productivity, beginners.
tags: '#git, #programming, #productivity, #beginners'
---

Targeted at devs past the basics

Do you know Git? Of course you do! Today, I’ve got a few of my favorite Git commands for you. When I was a junior developer, my tech lead taught me most of them (hi Wojtek, if you’re reading this 👋) and later, I started teaching the same commands to my own junior and mid-level developers.

I’ve actually been meaning to write this article for months. But you know how it is. It’s evergreen content, it requires a bit of work, and meanwhile I kept coming up with other ideas, so I kept postponing it. What finally motivated me was@francistrdev, who recently published his own article about Git commands.

My article will be a little different, though. If you’re completely new to Git and still learning the basics, check out Francis’sGit Gud!article first. But ifadd,commit,pull, andpushare already second nature to you, this article is for you.

These are, let’s say, intermediate-level commands. Useful ones. The kind you actually need at work, but not yet senior-level Git magic like:

Type three lines into your terminal and a spaceship will appear in your repository.

If you have other useful commands at this level, please share them in the comments!

BTW, if you feel like it, you can also follow me on Instagram! I’m planning to post what could grandly be called “dev lifestyle” content there. 😅 I have four conferences coming up this fall, for example, so expect some behind-the-scenes photos from my little tour around Europe. I only have a handful of followers there so far and absolutely no idea what this experiment will turn into, but here you go:@sylwia.lask

All right, let’s start.

## 1. & 2.git mergevsgit rebase

Haha, first point and we already have two commands.  The reason I’m putting them together is that a lot of developers, even experienced ones, treatmergeandrebasealmost interchangeably.

And sure, their high-level purpose is similar: you want to integrate the history of one branch into another. Very often that means updating your feature branch with changes frommain,develop, or another feature branch.

But the way they do it is quite different. Imagine you have this:

A---B---C main
 \
 D---E feature

Enter fullscreen mode

Exit fullscreen mode

You’ve been happily working on yourfeaturebranch, while someone else added commitCtomain. Now you want to bring those changes into your branch.

### Merge

If you run:

git merge main

Enter fullscreen mode

Exit fullscreen mode

while you’re onfeature, Git combines both histories. You usually end up with something like this:

A---B---C------M
 \ /
 D---E---

Enter fullscreen mode

Exit fullscreen mode

Mis a merge commit.

The original history stays intact. Git remembers that your feature branch diverged frommain, both branches evolved independently for a while, and then they were joined together.

This can be a good thing because it preserves the real history of what happened. The downside is that if you mergemaininto your feature branch over and over again, your history can eventually start looking like spaghetti.

### Rebase

Now let’s say instead you run:

git rebase main

Enter fullscreen mode

Exit fullscreen mode

Git takes commitsDandE, temporarily removes them, moves your branch onto the latestmain, and then reapplies your commits on top.

You get:

A---B---C---D'---E'

Enter fullscreen mode

Exit fullscreen mode

Much cleaner.

But notice the apostrophes.D'andE'are not technically the same commits asDandE. Git created new commits with new hashes. That meansrebase rewrites history.

This is why a very useful rule of thumb is:

Rebase your own work. Be careful rebasing shared history.

If you’re working alone on a feature branch, rebasing it is usually perfectly fine. If three other developers have already based their work on your commits, rebasing those commits can make everyone’s life considerably more exciting. And not in a good way.

### And what about conflicts?

Both merge and rebase can result in conflicts.

With a merge, Git tries to combine the two histories in one operation. You resolve the conflicting files, stage them:

git add 
.

Enter fullscreen mode

Exit fullscreen mode

and then continue:

git merge 
--continue

Enter fullscreen mode

Exit fullscreen mode

With rebase, things can be slightly more annoying because Git reapplies your commits one by one.

This means you may resolve a conflict, continue the rebase...

git add 
.

git rebase 
--continue

Enter fullscreen mode

Exit fullscreen mode

...and then get another conflict in the next commit. And another one. And another one. At which point you start questioning every career decision that led you here. 😅

But there’s also a small bonus. If you completely mess things up and just want to stop the entire circus, you can do:

git merge 
--abort

Enter fullscreen mode

Exit fullscreen mode

or:

git rebase 
--abort

Enter fullscreen mode

Exit fullscreen mode

Git will try to return you to the state from before the merge or rebase started. Extremely useful feature. 😁

## 3.git commit --amend

This is one of those commands I learned to love very quickly as a junior. Imagine you’ve just created a beautiful, perfectly round little commit. Then you look at the code and notice you forgot something.In my case, it was usually:

console
.
log
(
"
WTF
"
);

Enter fullscreen mode

Exit fullscreen mode

You now have two options. Option one: make another glorious commit:

Remove console log

Enter fullscreen mode

Exit fullscreen mode

Which, let’s be honest, is not exactly the pinnacle of Git history aesthetics.

Or you can simply add the forgotten change to the previous commit. For example:

git add forgotten-file.ts
git commit 
--amend
 
--no-edit

Enter fullscreen mode

Exit fullscreen mode

--no-editmeans:

Add these changes to the previous commit, but keep the existing commit message.

If you want to change the commit message as well, just run:

git commit 
--amend

Enter fullscreen mode

Exit fullscreen mode

Git will open your configured editor and let you modify it.

There is one important detail here.amenddoesn’t literally edit the existing commit. It creates anew commitcontaining the updated contents. And because commit hashes depend on the contents and metadata of the commit, the hash changes.

If you’re working locally and haven’t pushed the branch anywhere yet, no problem. But if the branch already exists on remote, your local history no longer matches the remote history. So when you try:

git push

Enter fullscreen mode

Exit fullscreen mode

you’ll probably get something like:

rejected (non-fast-forward)

Enter fullscreen mode

Exit fullscreen mode

Now, if you are absolutely sure nobody else is working on that branch, you could technically do:

git push 
--force

Enter fullscreen mode

Exit fullscreen mode

But what if you’re not sure?

And this brings us very smoothly to the next point.

## 4.git push --force-with-lease

After a rebase, amend, interactive rebase, squash, or anything else that rewrites your commits, your local branch history may no longer match the version stored on remote.

You can solve that with:

git push 
--force

Enter fullscreen mode

Exit fullscreen mode

But--forceis basically saying:

My local version is the truth. Replace whatever is on remote with this.

If someone pushed something to that branch in the meantime, you can overwrite their work. They may get angry.  And rightly so. 😏

A much safer option is:

git push 
--force-with-lease

Enter fullscreen mode

Exit fullscreen mode

In simplified terms, this tells Git:

Force-push my version, but only if the remote branch still looks the way I expect it to.

If the remote branch changed since the state your local Git knows about, for example because someone else pushed new commits, Git refuses the push instead of blindly overwriting them.

So instead of destroying someone’s afternoon, you get an error. I generally recommend:

--force-with-lease

Enter fullscreen mode

Exit fullscreen mode

over:

--force

Enter fullscreen mode

Exit fullscreen mode

whenever possible.

## 5.git rebase -i

For me, this is a very important command. Almost the king of Git. xDDDD Interactive rebase lets you do almost anything you want with your recent commits.

In other words, you can commit every single line individually, change everything ten times, create commits like:

Add validation
Fix validation
Actually fix validation
Fix validation again
Remove console.log
Please work now

Enter fullscreen mode

Exit fullscreen mode

and then later turn the whole mess into an elegant Git history.

Let’s say you want to edit your last five commits. You run:

git rebase 
-i
 HEAD~5

Enter fullscreen mode

Exit fullscreen mode

Git opens your configured editor — Vim, Nano, VS Code, or whatever you use — and shows something similar to:

pick a111111 Add login form
pick b222222 Add validation
pick c333333 Fix typo
pick d444444 Fix validation
pick e555555 Remove debug log

Enter fullscreen mode

Exit fullscreen mode

Now comes the fun part. You can replacepickwith different commands.

### pick

Keep the commit exactly as it is.

pick a111111 Add login form

Enter fullscreen mode

Exit fullscreen mode

### reword

Keep the commit contents, but change its message.

reword a111111 Add beautiful login form

Enter fullscreen mode

Exit fullscreen mode

### edit

Pause the rebase at that commit and let you modify it. Useful if you want to change the actual contents of an older commit.

### squash

Combine the commit with the one before it.

For example:

pick a111111 Add login form
squash b222222 Add validation
squash c333333 Fix validation

Enter fullscreen mode

Exit fullscreen mode

Git turns those commits into one and lets you edit the final commit message.

So instead of:

Add login form
Add validation
Fix validation

Enter fullscreen mode

Exit fullscreen mode

you can end up with:

Add login form with validation

Enter fullscreen mode

Exit fullscreen mode

Beautiful. Round. Perfect.

### fixup

fixupis similar tosquash, but it throws away the commit message of the fixup commit.

For example:

pick a111111 Add login form
fixup b222222 Fix typo
fixup c333333 Remove console.log

Enter fullscreen mode

Exit fullscreen mode

You probably don’t care about preserving the historical significance of:

Remove console.log

Enter fullscreen mode

Exit fullscreen mode

Sofixupis perfect here.

### drop

Remove the commit completely.

drop c333333 Terrible idea

Enter fullscreen mode

Exit fullscreen mode

Goodbye.

Of course, there are different schools of thought about how much you should clean up your commits. Some senior developers say that submitting a nicely cleaned-up commit history for review is simply good manners. Others do not care in the slightest and think it’s unnecessary because GitHub, GitLab, or whatever platform you use can simply squash everything when merging the PR anyway.

But!!! What if you don’t want to clickSquash and merge? What if your feature logically contains two commits and you actually want to preserve both? That happens.

So whether you use interactive rebase once a week or once every six months, I still think it’s worth knowing the king:

git rebase 
-i

Enter fullscreen mode

Exit fullscreen mode

## 6.git stash

This one comes in handy very often. You start working on a nice little feature. Or, these days, Kiro or Claude Code is working very hard while you watch.  Suddenly someone reports a production bug.

Unfortunately, you now have to temporarily abandon your beautiful feature and switch to something else. The problem is that your current work is completely unfinished. You have debug logs everywhere, half the files are modified, the project doesn’t even build, and you definitely don’t want to commit this mess.

Although, of course, now you know aboutamend, so you could eventually clean it up.

But there’s a better solution:

git stash

Enter fullscreen mode

Exit fullscreen mode

Git temporarily stores your uncommitted changes and returns your working directory to a clean state.

Now you can switch branches:

git switch main

Enter fullscreen mode

Exit fullscreen mode

fix your production disaster, and later come back.

One important detail: by default,git stashstashes tracked files, but not new untracked files. If you also want to include newly created files, use:

git stash 
-u

Enter fullscreen mode

Exit fullscreen mode

or, even better, give your stash a useful name:

git stash push 
-u
 
-m
 
"WIP login feature"

Enter fullscreen mode

Exit fullscreen mode

Because once you have several stashes named basically “WIP”, future you will hate present you.

### git stash list

To see all your stashes:

git stash list

Enter fullscreen mode

Exit fullscreen mode

You might get:

stash@{0}: On feature/login: WIP login feature
stash@{1}: On feature/cart: experiment

Enter fullscreen mode

Exit fullscreen mode

### git stash show

To see what a particular stash contains:

git stash show stash@
{
0
}

Enter fullscreen mode

Exit fullscreen mode

And if you want the full diff:

git stash show 
-p
 stash@
{
0
}

Enter fullscreen mode

Exit fullscreen mode

### git stash apply

To restore a stash:

git stash apply stash@
{
0
}

Enter fullscreen mode

Exit fullscreen mode

The changes are restored, but the stash remains in the list.

### git stash pop

You can also use:

git stash pop

Enter fullscreen mode

Exit fullscreen mode

This applies the stash and, if successful, removes it from the stash list.

So, roughly:

apply = restore
pop = restore + remove from stash

Enter fullscreen mode

Exit fullscreen mode

Very simple, very useful.

## 7.git cherry-pick

I have to admit this is one of the intermediate Git commands I use most often. Imagine there’s one specific commit on another branch that you want in your current branch.

You don’t want to merge the whole branch. You don’t want to rebase onto it. You literally need one thing. For example, in my project recently, I needed a commit containing configuration for newly created environments. Perfect use case.

You simply run:

git cherry-pick <commit-hash>

Enter fullscreen mode

Exit fullscreen mode

For example:

git cherry-pick a1b2c3d

Enter fullscreen mode

Exit fullscreen mode

Git takes the changes introduced by that commit and applies them to your current branch.

Important detail: it creates anew commit. So the resulting commit contains essentially the same changes, but it gets a new hash. Imagine this history:

main
A---B---C

feature
 \
 D---E---F

Enter fullscreen mode

Exit fullscreen mode

You’re onmain, but you only wantE.

After:

git cherry-pick E

Enter fullscreen mode

Exit fullscreen mode

you get something like:

A---B---C---E'

Enter fullscreen mode

Exit fullscreen mode

Simple.

But I’ll admit that, being a lazy creature, I use cherry-pick in slightly less noble ways too. Sometimes something gets completely messed up on my branch. The rebase goes badly, the history looks suspicious, conflicts start multiplying, and after a while I decide: I'll create a completely new branch from the correct place at the top of the tree. 😅

And because — thanks to the previous commands ☺️ — my commits are already nice and round, I simply cherry-pick them one by one onto the new branch.

I’m sure some Git pro is currently shaking their head at me, but let me put it this way: It works for me. 😀

## 8.git reset --soft,--mixed,--hard

Three ways of moving back in history, each with a different answer to the question:

What should happen to my changes?

Because how many times do we start working on something, write some code, and then realize: Nope. This whole idea was bad. Let’s go back.

The easiest way to understandresetis to think about three layers:

Commit history
Staging area
Working directory

Enter fullscreen mode

Exit fullscreen mode

Now we have three increasingly dramatic levels of reset. And every next one has greater potential to cause a small heart attack if you use the wrong one.

### git reset --soft

Let’s say you want to undo the last commit:

git reset 
--soft
 HEAD~1

Enter fullscreen mode

Exit fullscreen mode

Git movesHEADback by one commit, but all the changes from the removed commit remainstaged.

So if your history was:

A---B

Enter fullscreen mode

Exit fullscreen mode

after the reset, your branch points to:

A

Enter fullscreen mode

Exit fullscreen mode

but the changes introduced byBare still ready to commit.

This is useful when you committed too early and want to recreate the commit differently.

### git reset --mixed

Now:

git reset 
--mixed
 HEAD~1

Enter fullscreen mode

Exit fullscreen mode

or simply:

git reset HEAD~1

Enter fullscreen mode

Exit fullscreen mode

because--mixedis the default.

Again, Git moves back one commit.

But this time the changes are left in your working directoryunstaged.

So nothing disappears from your files, but you need togit addthings again before committing.

### git reset --hard

And now we enter the danger zone:

git reset 
--hard
 HEAD~1

Enter fullscreen mode

Exit fullscreen mode

This movesHEADback and updates both the staging area and working directory to match that commit. In other words, the changes disappear from your files too.

So:

--soft → keep changes staged
--mixed → keep changes unstaged
--hard → discard changes from the working tree

Enter fullscreen mode

Exit fullscreen mode

Use the last one with some awareness of what you’re doing. But what if you go one step too far and accidentally delete something you absolutely did not mean to delete?

And that brings us to...

## 9.git reflog

A command I use very rarely. But oh, how many times it has saved my ass.

For example, when I once rangit reset --hardand instead of removing my last changes, I basically removed the branch I had been working on for two days. 😀Amazing experience. Highly recommended.

The important thing to understand is thatgit logshows you commits reachable from the history you’re currently looking at. If you reset your branch backwards, some commits may disappear from git log.

That does not necessarily mean Git has immediately deleted them. Git also keeps a local log of movements of references such asHEAD. You can inspect that with:

git reflog

Enter fullscreen mode

Exit fullscreen mode

You may see something like:

e35fa12 HEAD@{0}: reset: moving to HEAD~2
821cd77 HEAD@{1}: commit: Add authentication
f992ab1 HEAD@{2}: commit: Add login page

Enter fullscreen mode

Exit fullscreen mode

Aha! There’s your missing commit.

Now you have several options. You could move the branch back to it:

git reset 
--hard
 821cd77

Enter fullscreen mode

Exit fullscreen mode

But personally, if I’m already in panic-recovery mode, I prefer doing something safer first:

git branch rescue 821cd77

Enter fullscreen mode

Exit fullscreen mode

Now the commit is reachable from a branch again and I can calmly inspect what happened without immediately rewriting anything else.

The key difference is:

git log

Enter fullscreen mode

Exit fullscreen mode

shows your visible commit history.

git reflog

Enter fullscreen mode

Exit fullscreen mode

shows where your local references, especiallyHEAD, have pointed recently.

There is one important limitation, though. Reflog is not a magical backup of every character you’ve ever typed. If your changes were never committed, stashed, or otherwise stored as Git objects,reflogcannot magically resurrect them.

So yes, if you worked for six hours without committing anything and then destroyed those changes... Well. Maybe this will teach you to commit more often next time.

## 10.git revert

And finally:

git revert

Enter fullscreen mode

Exit fullscreen mode

Imagine you release a commit to production.  Or, in the slightly less hardcore version of this scenario, to some shareddevelopbranch.

Something goes very wrong. Everything breaks. So what now? Do you run:

git reset 
--hard

Enter fullscreen mode

Exit fullscreen mode

on the production branch?

Do you start performing an exorcism?

Fortunately, no. The elegant way to undo a commit while preserving a clear record of what happened in your repository history is:

git revert <commit-hash>

Enter fullscreen mode

Exit fullscreen mode

Imagine your history looks like this:

A---B---C

Enter fullscreen mode

Exit fullscreen mode

andCintroduced the disaster.

You run:

git revert C

Enter fullscreen mode

Exit fullscreen mode

Git doesnotremoveC.

Instead, it creates a new commit that applies the opposite changes:

A---B---C---D

Enter fullscreen mode

Exit fullscreen mode

You may end up with something like:

C: Add new payment logic
D: Revert "Add new payment logic"

Enter fullscreen mode

Exit fullscreen mode

This is extremely useful on shared branches because you are not rewriting public history. Everyone can clearly see:

1. the original change happened,
2. it caused trouble,
3. it was reverted.

Compare that with resetting the branch and force-pushing it backwards, which rewrites history and can cause problems for everyone else working on it.

So, as a general rule:

Shared branch + bad commit → revert

Enter fullscreen mode

Exit fullscreen mode

is usually much safer than:

reset + force push

Enter fullscreen mode

Exit fullscreen mode

And that’s it!

As I said at the beginning, if you use other intermediate Git commands that regularly save you time or save your ass, please share them in the comments. Usually the comments under my articles end up being much better than the article itself, which continues to make me very happy.

Also, please note that last week’s article was a list. This week’s article is a list. And — spoiler alert — next week’s article will also be a list!

This is not because I smelled clicks and decided to turn into BuzzFeed. It just somehow happened that way. 😅

I hope you learned something new. And if you didn’t, I hope it was at least fun to read. 😁

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse