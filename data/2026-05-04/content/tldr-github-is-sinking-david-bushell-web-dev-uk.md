---
title: GitHub is sinking – David Bushell – Web Dev (UK)
url: https://dbushell.com/2026/04/29/github-is-sinking/
site_name: tldr
content_file: tldr-github-is-sinking-david-bushell-web-dev-uk
fetched_at: '2026-05-04T06:00:34.650163'
original_url: https://dbushell.com/2026/04/29/github-is-sinking/
author: David Bushell
date: '2026-05-04'
description: The one where I suggest finding the nearest lifeboat
tags:
- tldr
---

# GitHub is sinking

Wednesday

29Apr2026Play Synthesised Audio

TL;DR:GitHub used to be cool and now it’s a lame slop graveyard.

GitHub is racing towards the mythicalzero ninesof uptime. Users are starting to notice that GitHub is now a Microsoft product.Eww!

Official uptime paints a concerning chart. Themissing status pagetell a far worse story. Whatever the truth, it’s impossible to miss thedelightfulexperience that is Microsoft GitHub if you use it semi-regularly.

Alt

Line chart showing GitHub average uptime by month following the Microsoft acquisition. A green line turns into an orange and red roller coaster.

GitHub’s Historic Uptime

Microsoft acquired GitHuband applied their unique brand of enshittification. Amongst their achievements was the spawning of theCopilot circle of hell. Now they’re effectivelyDDoSing themselves with slop. I won’t dwell on what else went wrong. I don’t know and I don’t care. GitHub is impressively bad now.It’s embarrassing.Shameful.

As I write this the obituaries are flooding in:

* Ditching GitHub - Lonami
* Ghostty Is Leaving GitHub - Mitchell Hashimoto
* Before GitHub - Armin Ronacher
* From GitHub to Codeberg/Forgejo - Jonas Hietala

It’s long past time to get off this sinking ship!

## Git is not GitHub

GitHub has become synonymous with “source control” and I worry too many users don’t know that Git is not GitHub. The core technology of Git is open source. It’s distributed, meaning that all repositories are equal. Git works without a centralised service. Such a practice is a construct of social convenience. GitHub was a useful add-on. Microsoft has turned GitHub into an expensive liability.

### But network effect…

Network effects are hard to topple but if anyone can do it, Microsoft can. GitHub’sfake star economyis worthless. GitHub is inundated with bots anddrowning in slopand doing everything to encourage it. Microsoft is turning GitHub into theMoltbookof code, it ain’t for you and me anymore.

### But continuous integration…

Your CI pipeline is over-engineered and GitHub Actions are an abomination (see:[1][2]). Finding another solution is an absolute chore but do you trust GitHub to be reliable?

### But more excuses…

Look, the ship is sinking! Sure, the water looks freezing. Don’t hang around and allow Microsoft to pull you under. You don’t need to move everything in one go. Start the process.

## Alternatives

The nearest lifeboat to escape GitHub is another centralised Git forge. Just sign up and push your repo to the new upstream. Some services can automate the migration and maybe even import issues. Personally I’d leave issues behind in a tragic boating accident.

Edit:none of the options below are 100% rainbows and butterflies. They arenot GitHub, that’s all I can vouch for. Do your own research etc.

Codeberg— a non-profit and community-led project with an established track record. This is the safe alternative that’ll stick around. It’s the flagship instance ofForgejo.

Tangled— an alpha stage start-up with interestingAT protocolintegration. Worth considering for smaller solo projects.

Gitea— they offer cloud managed Git hosting. It’s the original open source project that Codeberg/Forgejo forked away from.

GitLab— enterprise grade, meaning it’s bloated and confusing but it’ll impress your boss. This could be the choice if you need multiple meetings to make the choice.

Bitbucket— trade one soul destroying corpo fun vacuum for another. Strongly discouraged, but Bitbucket does technically fit theanything but GitHubcategory.

Edit:Game of Trees,Radicle, andSourcehutwere suggested to me. I’ve no idea how they work, investigate yourself!

## Self-hosted

If you’recool like me, you or your organisation can self-host a Git forge withactionsandreleases. My recommendation isForgejo. There istalk of federationbetween Forgejo instances (edit:and Tangled) but it’s not happening anytime soon. If you want open collaboration push a copy to Codeberg. Gitea and GitLab also have self-hosted options. Be aware, GitLab is a comparative chonker.

When I said “Git is not GitHub” the same applies to other forges. Do you need those add-ons? Nothing is stopping you from raw-doggin’ Git over SSH:

git
 
clone
 
user@192.168.1.67:/path/to/repo
Copy Code

How you manage collaboration is another question. If Linux can be maintained by sending patches to an email mailing list,“doesn’t work at scale”arguments are skill issues. But seriously, a centralised Git forge is a decent compromise in my opinion. Maybe they collapse like GitHub in future. Always have an exit plan.

Just use anything but GitHub.