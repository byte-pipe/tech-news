---
title: I'm Not on the DEV Team. I Still Debugged Their Missing Badges From Public Code. (And My First Test Was Wrong.) - DEV Community
url: https://dev.to/dj29/im-not-on-the-dev-team-i-still-debugged-their-missing-badges-from-public-code-and-my-first-test-18oo
site_name: devto
content_file: devto-im-not-on-the-dev-team-i-still-debugged-their-miss
fetched_at: '2026-10-25T14:49:16.178467'
original_url: https://dev.to/dj29/im-not-on-the-dev-team-i-still-debugged-their-missing-badges-from-public-code-and-my-first-test-18oo
author: Dhruv Jani
date: '2026-10-24'
description: I’m not on the DEV team. I don’t have an admin panel, production database access, or internal Slack.... Tagged with opensource, ruby, rails, testing.
tags: '#opensource, #ruby, #rails, #testing'
---

A humbling reminder that passing tests can lie

I’m not on the DEV team. I don’t have an admin panel, production database access, or internal Slack. Everything I know about how DEV works comes from reading the publicforem/foremrepository. 🕵️‍♂️

Today, that was enough to diagnose why nobody on DEV was receiving multi-commit contributor badges, ship the service fix upstream, and get a"Thank you for this"and merge from@benhalpernSir himself. 🚀

The 4x DEV Contributor Club badge: "Awarded for 4+ merged commits to Forem — Thank you so much for your contributions!"

It also taught me a humbling lesson about tests that pass for the wrong reason. 🧪

## 1. The Itch: 4 Merged PRs, 1 Badge 🤔

Over the past few days, I went on a contribution sprint inforem/foremand merged four pull requests:

* #24003— Docs: fix broken Kamal TOC anchor and index missing guides
* #24056— A11y: remove duplicatearia-describedbyattributes in admin forms
* #24094— A11y: remove danglingaria-describedbyreferences in creator settings
* #24095— Views/Liquids: quotesrcand add missingaltinuser_subscriptiontag

My1x(dev-contributor) badge showed up right away after PR #1. ✅

When PR #4 merged, I knew fromconfig/schedule.ymlthatBadgeAchievements::BadgeAwardWorkerruns every hour at:20past the hour (cron: "20 * * * *"). I checked GitHub’s Contributors API (/repos/forem/forem/contributors) and confirmed my account was sitting on page 2 withcontributions: 4. Because Forem setsOctokit.auto_paginate = true, the worker was definitely reaching page 2.

One hourly cron passed. Then two. Then three. Still no4x-commit-clubbadge. 💀

Me at :20 past the hour, every hour, refreshing my profile like it owes me money.

Instead of refreshing my profile for another 24 hours, I cracked openapp/services/badges/award_contributor_from_github.rb. 🔍

## 2. Reading the Code Like a Detective 🕵️‍♂️

Here is howBadges::AwardContributorFromGithublooked onmain:

BADGE_SLUGS
 
=
 
{

 
"dev-contributor"
:
 
1
,

 
"4x-commit-club"
:
 
4
,

 
"8x-commit-club"
:
 
8
,

 
"16x-commit-club"
:
 
16
,

 
"32x-commit-club"
:
 
32

}.
freeze

Enter fullscreen mode

Exit fullscreen mode

When I comparedaward_single_commit_contributors(which awarded my 1x badge) againstaward_multi_commit_contributors(which handles 4x, 8x, 16x, and 32x), three bugs jumped right off the screen:

### 🐛 Problem 1: Silent Slug Drops

Each key inBADGE_SLUGSis resolved viaBadge.id_for_slug(slug). If a slug in the productionbadgestable doesn't match the hardcoded constant,id_for_slugreturnsnil. The service called.compacton the resulting hash and moved on. No error. No log line. Just a badge tier that quietly vanishes into the void. 👻

Because Forem only exposesresources :badges, only: [:index]without public/badges/:slugshow routes, you can't query individual badge slugs directly. However, inspecting the publicdev.to/badgescatalog gave me a massive clue:

Badge #423 on/badges:

* Title:4x DEV Contributor Club
* Description:4x-commit-club

Wait—why was4x-commit-clubsitting in thedescriptionfield while the title was4x DEV Contributor Club? BecauseBadge#generate_slugparameterizes the title when no explicit slug is set (4x-dev-contributor-club), the storedslugcolumn in production didn't match the hardcoded"4x-commit-club"constant at all! 💡

ConnectingBadge#generate_slugto DOM element IDs on/badgesat 9 AM with zero database access.

### 💌 Problem 2: Missing Context Messages

Single-commit badges were awarded with:

BadgeAchievement

 
.
where
(
user_id: 
i
.
user_id
,
 
badge_id: 
dev_contributor_badge_id
)

 
.
first_or_create
(
rewarding_context_message_markdown: 
msg
)

Enter fullscreen mode

Exit fullscreen mode

Multi-commit badges, however, were awarded with a bare.create:

BadgeAchievement
.
create
(
user_id: 
user_id
,
 
badge_id: 
slug_id
)

Enter fullscreen mode

Exit fullscreen mode

Even when a multi-commit badgewascreated, it omittedrewarding_context_message_markdown: msg("Thank you so much for your contributions!"). Four times the commits, zero times the thank-you note. 😭

### 🔁 Problem 3: Missing Idempotency Guard

create_badges_for_usercalledBadgeAchievement.create(...)on every hourly run instead of.where(...).first_or_create(...). Every hour, it re-attempted already-earned badges for every contributor on the list, relying on ActiveRecord'suniquenessvalidationto fail silently. Worse, if a badge ever hadallow_multiple_awards: true, bare.createwould insert a duplicate achievement every hour—firingafter_create_commit :notify_recipientandsend_email_notification(flooding your inbox fromyo@dev.to) each time. 📬💥

## 3. Filing the Issue & Shipping PR #24113 🛠️

I openedIssue #24114laying out the slug mismatch on badge IDs423–426, and paired it withPR #24113to fix the service itself:

1. ✅ Attachedrewarding_context_message_markdown: msgto multi-commit badge awards.
2. 🔒 Replaced bareBadgeAchievement.createwith.where(...).first_or_create(...).
3. 📊 Deferred slug lookup behind the GitHub auth provider check and added logging whenever configured slugs are missing from the database.

## 4. The Plot Twist in Code Review 🎬

The initial deep-dive review on@benhalpernSir’s account was posted by Forem's automated review agent (OpenHands), and it did something awesome—it ran a read-only lookup against thebadgestable and confirmed my exact diagnosis from Issue #24114:

"I ran a read-only lookup on thebadgestable for the fiveBADGE_SLUGSkeys. Only one of the five slugs resolves. The fourNx-commit-clubslugs have no matching row, socreate_badges_for_userskips them and nobody can earn them today. The issue reporter's guess is correct."

Bingo. 🎯

Even better, the review caughttwo subtle flawsin my PR that taught me more than the bug itself:

### 📢 Lesson A: MyRails.logger.warnWas Log Spam

I originally logged aRails.logger.warninside the loop for each missing slug. Why was that bad?

1. Until the production slugs were aligned, DEV would log 4warnlines every hour.
2. Forem powers many independent communities. Most self-hosted Forems enable GitHub authwithoutseeding DEV-specific contributor badges. Fivewarnlines an hour for expected configuration turnswarninto permanent background noise.

The Fix (5e36999):Collect all missing slugs and emit a singleRails.logger.infoline per run. 🧹

### 🤡 Lesson B: My Regression Test Passed onmain(For the Wrong Reason!)

To test idempotency, I wrote a spec that randescribed_class.calltwice and asserted that the user still had only1badge achievement for4x-commit-club.

It passed! Green dots everywhere. 🟢

Except the review pointed out something brutal:that test also passed onorigin/mainwithout my fix.

When your shiny new regression test passes onmainwithout your bugfix.

Why? Thebadgefactory defaults toallow_multiple_awards: false. Onmain, the secondBadgeAchievement.createhitvalidates :badge_id, uniqueness: { scope: :user_id, if: :single_award_badge? }, failed validation silently, and left the count at1. My test wasn't testingfirst_or_createat all—it was testing ActiveRecord's uniqueness validator! 🤦‍♂️

The Fix (5e36999):I updated the spec to create the badge withallow_multiple_awards: true(where bare.creategenuinely inserts duplicates onmain) and assertedexpect { described_class.call }.not_to change(BadgeAchievement, :count)on the second run.

After I pushed5e36999and all 34 checks went green,@benhalpernSir stepped in personally, dropped a comment:

That"Thank you for this"from@benhalpernSir genuinely made my entire day! 🙌 And right after that, he merged#24113intoforem:mainasd1b962e(my 5th merged PR!). 🎉

Shortly after, the badge email fromyo@dev.tohit my inbox and the4x DEV Contributor Clubbadge landed on my profile—complete with the"Thank you so much for your contributions!"context message my PR wired up. The code is cleaner, the PR is merged, and the green4xcircuit board is finally home. 💚

## 💡 3 Takeaways I’d Tell Past Me

1. 🔴A regression test isn't real until you watch it fail onmain.Before you celebrate a green spec,git stashyour change and run the spec againstmain. If it still passes, you haven't written a regression test—you've written a test that agrees with you.
2. 🪵Log levels are an operator contract.warnmeans someone should act. If a platform supports optional data seeds, missing optional rows areinfo, notwarn.
3. 🔓You don't need production access to debug production.You just need the public source code, a falsifiable hypothesis, and the curiosity to follow the trail.

Your turn:What’s the sneakiest time one of your tests passed for the completely wrong reason? Drop it in the comments 👇

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse