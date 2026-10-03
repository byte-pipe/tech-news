---
title: Humans Out of the Loop — Matthew Boston
url: https://matthewboston.com/blog/humans-out-of-the-loop.html
site_name: tldr
content_file: tldr-humans-out-of-the-loop-matthew-boston
fetched_at: '2026-10-03T15:04:19.214786'
original_url: https://matthewboston.com/blog/humans-out-of-the-loop.html
author: Matthew Boston
date: '2026-10-03'
published_date: '2026-10-03T00:00:00Z'
description: Agents open trivial PRs faster than anyone can read them, so the approvals turn into rubber stamps. Build the guardrails that earn trust, write down what counts as trivial, and let those changes ship without a person in the way.
tags:
- tldr
---

The industry has settled on “a human in the loop” as the safe way to run AI agents. For trivial changes, I think it’s the wrong default. Your agents open pull requests faster than your team can read them. When fifty more are waiting, someone approves the dependency bump without reading it. That approval adds a delay and a name to the audit log, and nothing else. Take the human out of the loop on purpose, and earn the right to do it with guardrails.

## The rubber stamp

This site gets them too. RuboCop 1.90.0 to 1.91.0. Liquid 5.13.0 to 5.14.0. Dependabot opens the PR, CI goes green, and I approve it. I read the title. I did not read the lockfile diff, and I wouldn’t have learned anything if I had.

Scale that up to a team running agents all day. Dependency bumps, lint autocorrects, a renamed config key, a formatter run across a directory. Each one wants an approval, and the reviewer has real work waiting. So they skim the title, check for a green build, and click. That person is ameat proxy: a human whose only job is to relay what the machine already decided. Here, the relay ends at the merge button.

A meat proxy is worse than no review at all. No review is honest about what happened. A rubber stamp tells everyone downstream that a person looked, and the incident retro will go looking for that person.

## Trust comes from guardrails

Letting a change ship with nobody reading it takes trust, and trust has to be built out of things you can check. Five of them carry most of the weight:

* Good tests.The suite has to catch a behavior change before production does. That depends on theharness of linters, types, and testsaround the agent, and on tests that don’tflake on the network. A red build nobody trusts is one more thing the meat proxy learns to ignore.
* Small diffs.A one-line version bump has one thing that can go wrong. A 400-line “cleanup” has hundreds, and nobody can call it trivial with a straight face.
* Canary deploys.Send the change to a slice of traffic first and watch error rates and latency against the baseline. The canary is a reviewer that looks at the system’s behavior instead of the diff.
* Fast rollback.If undoing a deploy takes one command and two minutes, a bad trivial change costs two minutes. If it takes a war room, nothing is trivial.
* Clear rules for what counts as trivial.This one decides whether the other four are enough, so it gets its own section.

## Write down what trivial means

“Trivial” can’t be a vibe, and it can’t be the agent’s call. It has to be a rule a machine can evaluate before the merge.

A starting list might look like this. Patch and minor bumps of development dependencies with no open security advisory. Diffs produced entirely by the formatter or a linter’s autocorrect. Config changes to keys on an allowlist. Each comes with a size limit: some number of changed lines, past which the PR goes back to a human regardless of category.

The list of what never qualifies matters just as much. Anything touching authentication, payments, database migrations, or a public API. Major version bumps. Changes to the CI pipeline or the deploy scripts themselves, because a change that edits the guardrails doesn’t get to skip them.

Put the rules in the repo. A path filter in the auto-merge workflow, a CODEOWNERS entry, a policy file the bot reads. Rules that live in someone’s head drift the first time a deadline leans on them. If a PR needs a paragraph explaining why it’s trivial, it isn’t.

## Let production do the reviewing

For this class of change, the canary is a better reviewer than a person. A human readingGemfile.lockcan’t tell you that a transitive dependency changed its default timeout. A canary running real traffic will show you the latency curve bending within minutes.

The quality bar stays where it was. I argued inShip as Fast as Possible, but Not Fasterthat the dangerous shortcut is dropping checks to hit a date. Here the checks stay. They move from a tired reviewer’s eyes to automated gates that run every time and don’t get bored.

Start with one category. Auto-merge dev dependency patch bumps for a month and count the rollbacks. If the number is zero, or close enough that the rollback took less time than the reviews would have, widen the rules. If a category keeps bouncing, pull it back to human review and figure out which guardrail was missing.

## Spend judgment where it counts

Every rubber-stamped PR spends a little of the reviewer’s attention and returns nothing. Fifty a week adds up to a person who has stopped reading reviews at all, including the ones that matter.

Taking trivial changes off their plate is how you get that attention back for the work that needs it: the feature that changes how billing works, the schema migration, the PR where you need toreview the outcome instead of the output. People are good at that kind of review. They are bad at being the fifty-first click of the afternoon.

Build the guardrails first, then let the trivial changes go to production on their own, and give your team their afternoons back.

Don’t be a meat proxy.