---
title: Miguel Carranza - AI shouldn't shrink headcount. It should shrink teams
url: https://miguelcarranza.es/small-teams
site_name: tldr
content_file: tldr-miguel-carranza-ai-shouldnt-shrink-headcount-it-sh
fetched_at: '2026-07-01T19:35:59.641135'
original_url: https://miguelcarranza.es/small-teams
author: Miguel Carranza
date: '2026-07-01'
description: Another thought leadership post about why teams should be smaller. I know, very original.
tags:
- tldr
---

Another thought leadership post about why teams should be smaller. I know, very original.

But there’s a version of this conversation that’s actually useful, because the point is easy to misunderstand. When we talk about smaller teams at RevenueCat, the goal isn’t to stop hiring or to pretend AI means we need fewer people. If anything, it’s the opposite. We want to do more with the people we have, and when we hire, we want that to turn into more parallelism and bandwidth, not bigger meetings.

In the early days of a startup, small teams are just the reality. Sometimes one person owns the whole thing. A bug gets fixed in a day. A feature goes from idea to shipped in a week. There’s no roadmap committee because there’s nobody around to form one, just users asking for things.

Then the company grows, and some of that speed disappears for good reasons: more customers, more surface area, more risk. But not all slowness is maturity. Some of it is just organizational weight that slowly becomes normal.

## Why AI changes team size

For a long time, the default way to staff a serious product area was to add a few engineers on each side of the stack. Two or three backend, two or three frontend, a PM, an EM, maybe a designer. Suddenly every decision needs unanimous consent.

A lot of that used to be necessary. Writing code was the bottleneck. Reviewing code was expensive. Getting enough people with enough context around a decision was how you avoided doing something stupid.

AI shifts that balance. Writing the first version is cheaper. Reviewing unfamiliar parts of the codebase is easier. We spend more of our time reviewing code and deciding whether something is even the right thing to build.

You still need people who can tell when the AI-generated answer is plausible nonsense, and who own the output. But you rarely need three engineers from every specialty weighing in on every meaningful piece of work. Fewer people need to agree before something ships.

## What OCTO taught us

We started learning this before we applied it broadly. The first real version was OCTO.

OCTO, the Office of the CTO, is a small group of trusted senior ICs we put together to help with new bets and critical projects. The idea was simple: take a few people with high trust, strong company context, and good technical judgment, and let them bootstrap things before we build a whole org around the bet.

At the start of a new bet, you’re trying to learn whether the thing should exist at all. The engineers need to move fast, make early technical calls, and not fall in love with their own MVP. If the right business decision is to kill it, the code goes with it. The hardest part was never writing the code. It was being mature enough to throw it away.

OCTO worked because the group was small, senior, and trusted. There was nowhere to hide and no need to perform alignment theater. If something was stuck, it was obvious. If a bet wasn’t working, we learned faster.

## Applying it to product teams

Once the OCTO model was validated, the obvious question was: why only use this for new bets?

Some product teams had grown into multiple missions sharing one org structure and one set of meetings. So we split them up. In practice, we more than doubled the number of product teams at RevenueCat.

The model is simple: one to three engineers, sometimes with shared design or product management, and one clear engineering DRI (Tech Lead). The Tech Lead keeps the work moving and raises risks early. The manager still manages: hiring, coaching, performance, team health.

The Tech Lead role is also a low-risk way to spot future leaders and managers. They get to make calls, own outcomes, and drive a team, but without the people management responsibilities. The Tech Lead is also the interface with other teams. When two small teams need to coordinate, that’s a conversation between two or three Tech Leads, not a meeting with sixteen people in the room.

So far it’s working. The main advantage is velocity. Smaller teams create clearer ownership and make progress more visible. It’s easier to decide whether to expand, split, pause, or move people somewhere more urgent.

They also make performance management much more obvious. On a large team, weak output hides inside the average. On a small team, it’s clear who is not pulling their weight.

## The downsides

Smaller are not silver bullets. They have problems too.

The biggest cost is redundancy. If a team has two engineers and one goes on parental leave, takes vacation, or gets pulled into an urgent incident, you can lose half the team’s capacity overnight. Managers have to rebalance more often, some projects will slow down, and leadership needs to see it coming.

Smaller teams also demand more leadership from ICs. Every team needs someone who can make calls, communicate clearly, and keep things moving without waiting for permission. Some people grow into that. Some won’t.

And yes, more teams can create fragmentation. You can duplicate work or drift from a coherent product. That’s exactly why the Tech Leads matter so much. The answer is better coordination between the right people, not a fallback to big meetings.

## The manager role

This model also changes management.

If an EM runs several small teams, they can’t spend equal time everywhere, and they shouldn’t. A healthy team shipping every week doesn’t need the same attention as a team that’s stuck.

The manager’s job becomes allocating attention where it has the highest return. Go deep on the struggling teams. Coach the Tech Lead who isn’t quite ready. Rebalance when parental leave or vacations breaks the plan. Step back when a team is ripping and doesn’t need you in every decision.

Even 1-1 cadence should adapt. Some people need weekly time. Some are fine biweekly for a while. Some high-trust teams can mostly be left alone until the facts change, and you can lean on Tech Leads as a layer of abstraction between you and the rest of the ICs.

## Conclusion

The lesson isn’t “small teams are always better.” Some problems need more people, and we still run some projects that don’t follow this topology.

But with AI, the minimum viable size of a high-output team is smaller than it used to be. With strong ICs, clear ownership, and managers who know where to focus, you can get closer to that early startup feeling again. Fewer people in the room, faster decisions, more visible output.

And when you do hire, the new people add parallelism instead of coordination. That’s the point. Not hiring less, but doing more.

Originally published as anX articleon June 27, 2026 and archived here.