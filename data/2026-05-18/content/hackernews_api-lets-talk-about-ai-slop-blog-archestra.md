---
title: Let's talk about AI slop | Blog | Archestra
url: https://archestra.ai/blog/only-responsible-ai
site_name: hackernews_api
content_file: hackernews_api-lets-talk-about-ai-slop-blog-archestra
fetched_at: '2026-05-18T19:36:07.083582'
original_url: https://archestra.ai/blog/only-responsible-ai
author: Joey Orlando
date: '2026-05-18'
published_date: '2026-04-17'
description: Is it the end of open source we know and love?
tags:
- hackernews
- trending
---

Written by

Ildar Iskhakov, CTO

 Discussion on 
Hacker News
:
 

 news.ycombinator.com
 

## The End of Open Source as We Know It

When a few months ago GitHub shared statistics about 
celebrating an enormous contribution of AI in their product metrics
, completely missing the point of degraded contribution quality, we already felt that things were going south.

The first worrying moment was the 
issue we posted with a $900 bounty
. We were hoping to motivate someone to contribute and bring shiny new "MCP Apps" support to our platform. We quickly got the attention of legitimate contributors proposing plans, asking questions, submitting attempts — but soon...

AI bots arrived and blew up the issue, taking it to 
253 comments total
, poisoning the conversation with pointless "implementation plans" and even pure aggression toward the maintainers!

AI accounts started flooding not just this issue — but the entire repo. Every sloppy comment triggered a notification for every team member watching the repo. Our GitHub notifications became a wall of noise. Real conversations from contributors like @ethanwater, @developerfred, and @Geetk172 — people actively working on bounties — were getting buried.

Later, the problem took the form of an epidemic. For example, just for the issue to add x.ai provider support to Archestra, we received 
27 pull requests
, most of which 
contributors didn't even try testing
.

One of our team members had to spend 
half a day every week cleaning AI garbage out of the repo
, removing untested PRs and closing hallucinated issues. When we forgot to do so, our repo quickly became a place completely unfriendly to legitimate contributors.

## Fighting Back

At first, we tried to calculate the "reputation" of contributors and built 
"London-Cat"
, a tiny bot calculating a contributor's reputation based on merged PRs and a few other signals (
example
). It obviously didn't stop the spam, but it helped us figure out "who is who".

As a next step, we built an "AI sheriff" (
example
), which obviously closed a few legitimate PRs 🤦.

The constant flow of useless AI comments and proposals was only getting worse, turning legitimate contributors away and making us reconsider: should we stop 
motivating contributions with bounties
? Should we stop 
giving fun test tasks to our job candidates
?

We've decided that we need to fight back and insist on making our repo a comfortable and safe space for legitimate contributors, responsible AI users, newbies, and seasoned engineers.

Today we're 
blocking the ability to create issues, open PRs, and leave comments for those who didn't go through the onboarding
.

Contributor onboarding, five steps to get whitelisted

It's a nuclear option, yes. It's especially sensitive for a VC-backed startup that is measured thoroughly by GitHub activity, but we have to pull the trigger: 
we value quality over quantity. We don't value metrics pumped by AI slop.

We want Archestra to be a great piece of software that everyone can contribute to, without it being swallowed by AI bots.

## Doing It in GitHub

There is no straightforward way to whitelist those who can comment or create PRs on an open source repo, so we had to hack around.

There is a setting called "Limit to prior contributors." Simple rule: if you haven't previously committed to 
main
, you can't comment on issues or PRs.

Prior contributors setting

The setting can't tell the difference between an AI bot and a real developer who signed up to work on a bounty. Both are "not prior contributors." Both get locked out.

GitHub defines "prior contributor" as someone whose GitHub account is the 
author
 of a commit on 
main
. Git commits have two identity fields — 
author
 and 
committer
 — and they can be different people.

You can create a commit attributed to someone else using Git's 
--author
 flag. If the email matches their GitHub account, GitHub links the commit to their profile and grants them contributor status.

Every GitHub account has a noreply email: 
<id>+<username>@users.noreply.github.com
. Look up the ID via the API and commit:

gh api 
users
/their-username --jq 
'.id'

git commit \
 --author=
"their-username <ID+their-username@users.noreply.github.com>"
 \
 -m 
"chore: add their-username to external contributors"

Push to 
main
, and they can comment immediately.

Commit attributed to external user

The external user shows up as the 
author
, our account as the 
committer
. That's all GitHub needs to consider them a prior contributor.

The full flow:

1. Onboarding on our website with ethical AI rules and a CAPTCHA:https://archestra.ai/contributor-onboard
2. A GitHub Action that fires on submission, looks up the user's GitHub ID, adds their handle to anEXTERNAL_CONTRIBUTORS.mdfile, and pushes a commit tomainauthored under their account.
3. The user becomes whitelisted and gets access to the repo.

## Final Words

While GitHub reports massive metric growth — a substantial part of which is AI-generated — we as an open source project team have to do the heavy lifting of cleaning up AI slop from our repository and come up with esoteric workarounds to keep the level of legitimacy of our open source audience.

Slop is not only demotivating contributors who want to spend their time doing good and have to break through the wall of noise instead, it's also bringing a substantial security risk, as it happened 
in the LiteLLM repo
 when attackers tried to steer the conversation using AI bots.

Dear community, it's time to have a serious talk about the effect AI has on open source.