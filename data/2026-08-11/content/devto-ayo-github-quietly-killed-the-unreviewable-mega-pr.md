---
title: Ayo GitHub Quietly Killed the Unreviewable Mega-PR - DEV Community
url: https://dev.to/lovestaco/ayo-github-quietly-killed-the-unreviewable-mega-pr-3868
site_name: devto
content_file: devto-ayo-github-quietly-killed-the-unreviewable-mega-pr
fetched_at: '2026-08-11T11:42:52.787133'
original_url: https://dev.to/lovestaco/ayo-github-quietly-killed-the-unreviewable-mega-pr-3868
author: Athreya aka Maneshwar
date: '2026-08-10'
description: If you've ever opened a PR with 47 changed files and a diff so long GitHub just gives up and shows... Tagged with webdev, programming, productivity, github.
tags: '#webdev, #programming, #productivity, #github'
---

If you've ever opened a PR with 47 changed files and a diff so long GitHub just gives up and shows you "Load Diff" seventeen times, this one's for you.

GitHub quietly shipped what might be the biggest pull request update in years, and it's aimed squarely at that problem.

Let's talk about stacked pull requests.

## The problem, in one sentence

Big PRs are where good reviews go to die.

Nobody reads a 2000 line diff carefully.

Some folks reach for AI code review tools likeLiveReviewto take the edge off, and honestly that helps, but even the best reviewer (human or model) does a better job on a tight, focused diff than on a 2000 line wall.

Smaller inputs, better reviews. That's true no matter who's doing the reviewing.

Stacked PRs are GitHub's answer: break one massive change into a chain of small, dependent PRs, where each one only reviews the diff it actually introduces, not everything below it.

## What a stack actually is

The rule is simple. You need two or more PRs in the same repo where:

* The bottom PR targets your trunk branch (usuallymain)
* Every PR after that targets the PR below it, notmain

That's it. That's the whole trick.

Foundational stuff (schemas, shared types) goes at the bottom.

Stuff that depends on it (API routes, UI) goes higher up the chain.

And here's the part that surprised me: if you just do this manually with plain git, by opening PR #11 against the branch for PR #10 instead of againstmain, GitHub now recognizes that as a stack automatically.

No special tool required.

It just notices the base branches form a chain and lights up a banner.

Stacking isn't a git concept at all, it's purely a GitHub UI concept layered on top of branches you were already making.

## Let's actually build one

Enough theory. I built a real stack in one of my own repos (peektea, a terminal file browser I maintain), using a harmless scratch file so nothing real got touched.

Here's the actual terminal session, copy pasted, warts and all.

First I tried to be fancy and use the CLI extension:

$ gh stack --help
unknown command "stack" for "gh"

Enter fullscreen mode

Exit fullscreen mode

Yeah. Turns outgh stackneeds a CLI extension or a newerghversion than the one sitting in my$PATH, and mine's from a Ubuntu apt repo that hasn't heard about this feature yet.

Software, everyone.

So I did it the "old school" way the docs mention, plain git branches, chained base to base, no extension needed.

Which, from git's point of view, gives you exactly what git always gives you: three branches sitting on top of each other like tired commuters on a train.

Nothing special yet. This is just branches.

The magic happens once you push them and open the PRs with the right bases:

$ git push -u origin stack/01-setup-database stack/02-api-endpoints stack/03-setup-frontend

$ gh pr create --base master --head stack/01-setup-database \
 --title "demo: setup database layer"
https://github.com/lovestaco/peektea/pull/10

$ gh pr create --base stack/01-setup-database --head stack/02-api-endpoints \
 --title "demo: add api endpoints"
https://github.com/lovestaco/peektea/pull/11

$ gh pr create --base stack/02-api-endpoints --head stack/03-setup-frontend \
 --title "demo: setup frontend"
https://github.com/lovestaco/peektea/pull/12

Enter fullscreen mode

Exit fullscreen mode

Notice the--baseon PR #11 isstack/01-setup-database, notmaster.

That one flag is the entire secret sauce.

## And GitHub actually notices

This is the bit that got me. I expected to have to manually flip some setting somewhere.

Instead, the second I opened the top PR of the chain, GitHub just showed a banner: "This pull request can be stacked with other pull requests," with a "Preview stack" button sitting right there.

Clicking it pops up a little preview that walks the whole chain, top PR down tomain, correctly ordered, correctly linked, with zero config from me beyond opening PRs against the right base branches.

Hit "Create stack" and every PR in the list picks up a tiny progress badge,1/3,2/3,3/3, right there in the pull request list, so you can see at a glance how deep any given PR sits in its stack without opening a single one.

According toGitHub's own docs on stacked pull requests, once you're happy with the whole chain there's a "merge stack" action that walks down and merges every PR in order in one go, no manual rebasing between each merge.

I didn't actually pull that trigger on my demo repo (closing four browser tabs is enough chaos for one blog post), but the docs and the UI both point at it being one button for what used to be N sequential merges plus N rebases.

Here's roughly what that flow looks like end to end, CLI or manual, doesn't matter which:

## Wait, didn't I already have this?

Kind of, and this is worth being honest about. You could always open a PR against another PR's branch.

That's not new, that's just git plus GitHub's base branch dropdown, and people have been daisy chaining branches like this for a decade.

What's new is that GitHub now understands the relationship, tracks it as a first class object (mine got assigned its own stack ID the moment I hit "Create stack"), shows progress across the whole list view, and gives you one merge action instead of a manual merge-then-rebase-then-merge dance for every layer.

So no, git itself didn't get a new stacked PR primitive.

GitHub's UI did.

If you clone the repo and look at the branches, there is genuinely nothing different about them from any other feature branch.

The "stack" only exists as metadata GitHub keeps on its side.

## Why I actually care about this (hint: it's the bots)

Here's the part that got me more excited than a database migration screen usually gets me.

Think about what claude does when you point it at a big task and let it run for a few hours unattended.

Historically you get one of two bad outcomes: either it hands you back one enormous PR that's basically unreviewable, or it opens a dozen totally disconnected PRs that don't tell you which one depends on which.

Stacked PRs give agents a third option: build the feature the way a careful human would, in reviewable layers, and let the dependency chain itself communicate the order.

Schema first, then the API that needs the schema, then the UI that needs the API. You review it the same way the agent built it.

No more choosing between "one unreviewable 3000 line PR" and "twelve PRs with no visible relationship to each other."

The stack is the changelog of how the agent actually thought through the problem.

## Should you actually use this

If your team already splits work into small PRs by hand and just eats the rebase pain, yes, obviously, this removes the pain and keeps the habit.

If your team is currently a "one PR per feature, no matter how big" shop, stacked PRs are a nice on ramp, because you get to keep working the way you already do (branch off the previous branch) while GitHub handles the bookkeeping you used to do in your head.

It's still labeled as a newer feature in GitHub's docs, so expect some rough edges (myghCLI didn't even know the command existed yet), but the web UI side of it worked exactly as advertised the first time I tried it, no config, no opt in flag, just open PRs with the right base branches and watch GitHub connect the dots.

Go forth and stack responsibly. And maybe update yourghCLI before you try the extension route, unlike me.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Git Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|🇮🇳 हिन्दी|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

GenAI today is arace car without brakes. It accelerates fast -- you describe something, and large blocks of code appear instantly. But AI agentssilently break things: they remove logic, relax constraints, introduce expensive cloud calls, leak credentials, and change behavior -- without telling you. You often find out in production.

git-lrcis your braking system.It hooks intogit commitand runs an AI review on every diffbeforeit lands. 60-second setup. Completely free.

In short, git-lrc helpsPrevent Outages, Breaches, and Technical Debt Before They Happen

At a glance:10 risk categories·100+ failure patterns tracked· every commit…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse