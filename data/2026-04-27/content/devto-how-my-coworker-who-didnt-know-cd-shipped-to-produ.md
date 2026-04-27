---
title: How My Coworker Who Didn't Know 'cd' Shipped to Production - DEV Community
url: https://dev.to/mattstratton/how-my-coworker-who-didnt-know-cd-shipped-to-production-3j6j
site_name: devto
content_file: devto-how-my-coworker-who-didnt-know-cd-shipped-to-produ
fetched_at: '2026-04-27T12:20:16.188779'
original_url: https://dev.to/mattstratton/how-my-coworker-who-didnt-know-cd-shipped-to-production-3j6j
author: Matty Stratton
date: '2026-04-23'
description: The agent isn't the hard part. The scaffolding around it is. Here's how we built ours so a non-engineer could ship to production safely. Tagged with webdev, ai, devops, productivity.
tags: '#webdev, #ai, #devops, #productivity'
---

Scaffolding as the core product

This morning, our Design Lead asked me how to get her terminal into the right folder.

Tanya [6:57 AM]
my ghost isnt in tiger den anymore! GAH do i do /tiger-den
or what was the command to make it work 
in tiger den

Matty [7:14 AM]
What what?

Tanya [7:14 AM]
sorry lol
you know when i go into terminal/or ghostie
and i need to type the thing to make it so im
working in tiger den

Matty [7:14 AM]
Yes type cd tiger-den

Tanya [7:15 AM]
YES
OK CD
thank you

Enter fullscreen mode

Exit fullscreen mode

Tanyahas been here atTiger Datafor about two weeks. In that time, she shipped a feature to our production Next.js app.

I'm not going to pretend that's a normal sentence to write.

Tanya is our Design Lead. She runs brand. She's the reason our designs look the way they do and our blog thumbnails don't look like a high school yearbook. She is not a software engineer. She had not, as far as I know, previously planned on becoming one.

She didn't become one. She just started shipping.

The feature she shipped is an internal brand hub: a searchable index of every Tiger Data brand asset (logos, typography, colors, whatever you need) plus an interactive image builder that works like Canva (if Canva had been written specifically for our team). You can upload your own images, pick from our logo library, layer in backgrounds and icons, and drop text on top. Drag everything around, resize it, line it up. Export a PNG. (The thumbnail on this post was made with it.)

The downside of teaching a designer to use the terminal is that she will want hers to look like yours. Tanya saw myGhosttytheme and mycatppuccin Starshiptheme over a screen share and decided she wanted both. Her Claude Code statusline came next. That's an entire other post.

Hold both of these facts in your brain at the same time: Tanya is asking me whatcddoes this morning. Tanya shipped a real feature to a real codebase last week.

If you readmy last post on coding agents and internal tooling, you know where I ended it. The caveat was that I was a solo contributor to a real codebase, and the first comment on the post called out exactly the right thing.Who owns this when you leave?That's a reasonable question. In March, my answer was "me, and that's a problem."

My answer in April is "...and also Tanya."

That's only true because of what got built alongside the agent. The agent is the interesting part of the demo. Theboringpart is what made it safe to hand a Next.js codebase to a designer who's still learningcd.

Here's that boring part.

## The agent is not the hard part

Coding agents are very good at a lot of things. Being trustworthy is...not one of them.

I don't mean malicious. I mean if you ask an agent to fix a bug, it will often fix the bug. It will also sometimes decide the failing test is "probably flaky" and move on. Or notice a test it doesn't understand and quietly skip it. Or hit an error, try a second approach, fail, try a third approach, fail again, and by the time you look up it has deleted the function you were trying to fix. Or my favorite one: "These test failures are unrelated to my changes".

This is catchable. I catch a lot of it. I've been doing ops since before the Seinfeld finale aired, and I have been running DevOpsDays since before most of the current DevOps job descriptions existed. I read every diff before it leaves my machine and I have strong opinions about what a normal-looking CI run is supposed to contain.

I still miss things, everyone does. I rubber-stamp, I push tired, I get three levels deep on a task and stop reading carefully. Even with the paranoia cranked up, I am not reliably the last line of defense for my own work, let alone anyone else's.

And the paranoia itself is not transferable. "Notice when an agent silently dropped a test case" is not a skill you pick up in two weeks. It is not a skill most of theengineersI know pick up in two weeks, because most of them never had to. I cannot hand it to Tanya by writing a memo.

So the question is nothow do I make Tanya as paranoid as I am. The question is: how do I make the system so paranoid that it doesn't matter how paranoid any of us are on a given Friday afternoon?

You build the paranoia into the system. (If thissounds familiar, it should.)

## Rules are a suggestion

The first place everyone reaches isCLAUDE.md. Some people call theirsAGENTS.mdif they want the file to be portable across agents that aren't Claude. Same idea. You write down the rules you want the agent to follow, drop it at the root of the repo, and the agent reads it every session.

Ours has a section called "Golden Rules". A handful of the actual rules from the actual file:

Diagnose before fixing. Read errors, trace code, explain your hypothesis before writing any fix. No guess-and-deploy.

Never dismiss failures. Test failures, CI failures, lint warnings. Investigate every one. Never call them "pre-existing" or "not my problem."

Never destructive without permission. No DROP, TRUNCATE, DELETE without WHERE.

Always use/prto push. Never rawgit push.

These are not theoretical. Each one is on the list because the agent did the thing I didn't want it to do, often enough that I eventually wrote it down. (Sometimes from running/insightsin Claude Code.)

Does the agent follow them? Mostly. Does the agent ignore them when convenient? Also yes.

The failure mode is an exchange you have probably already had:

Me: "Wait, you just pushed to main."

Claude: "Oh shoot, you're right. TheCLAUDE.mdsays to use/pr. I just... didn't."

It apologizes. It means it. It will still do it again on Tuesday.

CLAUDE.mdis training; it shapes the default behavior. It doesnotenforce anything. Treat it like training and it is useful. Treat it like a wall and something is going to walk through the wall.

That was the first thing I had to learn. It might have take a few times.

## Skills are a habit

If rules are what you write down when you want an agent toknowsomething, skills are what you write down when you want the agent (or the human) todosomething the same way every time.

A Claude Code skill is roughly: a folder with instructions, some scripts, and a slash command. Type/setupand it walks through our dev environment setup. Type/debugand it starts a structured investigation instead of letting the agent flail. Type/releaseand it runs the release process in the right order.

The one that matters most is/pr.

Our repo has a preflight checklist you have to pass to open a pull request. It runs lint. It runs the typechecker. It runs the tests. It runs the build. It runs a code review subagent. If any changed files touch rendered output, it runs a UI verification step. If any touched docs, it runs a docs-drift check. If any touched security-sensitive paths, it runs a security review. Only then does it actually open the PR, and even then it opens it as a draft.

All of that is one command. Tanya does not have to remember any of it. She types/pr.

This is still not enforcement. Skills are suggestions. A motivated human (or a tired agent, or a confused agent, or an agent being nudged by a tired human) can skip/prand push directly, and nothing in the skill itself will stop them (note: the skill does try to tell the agent when it should try to run it, and it usually gets it right...but not always).

The job of a skill is to make the right way the easy way./pris one command. Running all of those checks by hand is eight. If typing/pris easier than doing the alternative, the alternative stops happening. That is most of the game.

Tanya used/prfor the brand hub. She did not run lint, typecheck, tests, and build in sequence. She would not have known to! She typed a slash and a word. Everything ran.

The rest is between her and the agent.

## Hooks are a wall

The rule "never push to main" lives inCLAUDE.md. The skill/pris easier to type than the alternative. Neither of those is enforcement.

The enforcement is a pre-pushgit hook.

If you (or a coding agent) rungit pushfrom a machine with our repo checked out, the hook fires before the push leaves your laptop. If the branch you are on ismainorproduction, the hook exits 1 and prints the error message I wrote specifically for the version of me that is about to do a dumb thing. The push does not happen.

If the branch is anything else, the hook runs lint, typecheck, tests, and build locally. If any of them fail, the push does not happen.

There is a flag to skip hooks, yes. If the agent tries to use it, a separatePreToolUsehookcatches the command before it runs and blocks it on protected branches. And if a push somehow lands on the remote anyway, GitHub branch protection rejects it on the server side.

I did not build all three layers on day one. I built them in the order I needed them, which is to say I built each one the first time something got past the layer before it.

There is also aSessionStarthook that runs before the agent does anything. It checks that the Node version is the one the app expects, that the environment file exists, that dependencies are up to date, that the database the session is about to touch is the development database and not production. If any of that is wrong, the session opens with a warning, and the agent is told to act on the warning before doing anything else.

None of this requires the agent to cooperate. None of it requires the human to remember.

CI is the outer wall. Six jobs, parallel, on every pull request. Lint. Typecheck. Frontend tests. Backend tests across three shards. Build. Doc drift check. If any job fails, the PR cannot merge. If the PR does not have a label, a seventh job fails.Zero warnings allowed.

This is the only layer that does not care how tired anyone is, how confused the agent is, or what quiet thing got dropped on the way through. It just says no.

Tanya has never pushed tomain. She could not push tomainif she tried. Neither can I. We have confirmed.

## The scaffolding is the product

Here is the funny thing about all of this: none of it is new.

Linters. CI. Pre-commit hooks. Code review. Required labels. Branch protection. Engineering teams have been writing these guardrails for the humans on the team for two decades. What changed is that the same guardrails now work on the agent. And because the agent does most of the typing, they work for the non-engineer driving the agent too.

The three layers are just discipline given shape. Rules tell the agent what you want, skills make the right thing the easiest thing, hooks enforce the non-negotiables. That stack is not new. It is what engineering has been doing for twenty years, and it works.

Whatdidchange is the cost. ACLAUDE.mdis an afternoon. A skill is another afternoon. A git hook is an hour. ASessionStartscript is an hour. Most of them I wrote in a single week, when the alternative was cleaning up after a mistake the agent had already made twice.

The agent isn't the product, the scaffolding is. The agent is really good at working inside it without stepping on anything important.

There is one piece of scaffolding I have not been able to write.

It is the call on my calendar every few days where Tanya and I hop on a screen share and work through something hand-in-hand. We have a name for these. It is "make Tanya an engineer." Sometimes we are making her Claude Code statusline look cool. Sometimes we are picking out a new text editor and making it hers. Sometimes we are walking through how the app is put together so we can figure out how to make it even more awesome.

They are still happening. They will probably still be happening in six months. I am not trying to automate them away.

There is something about a real person on the other side of a screen share that makes the work feel survivable. ACLAUDE.mdwill not do that. A slash command will not do that. The hooks definitely will not do that.

That is also part of the system.

## Two things I owe you

First, a callback toGuilhermeon the last post. You were right that Retool is bus-factor insurance. You can also roll your own. It's called aCLAUDE.md, a pre-push hook that exits 1, and an hour-long call called "make Tanya an engineer."

Second, a correction on the opener. Tanya is not the only other person shipping code to Tiger Den. A few other folks have been committing too. I made her the hero because her two-week arc was the cleanest story. Apologies to the rest of the team for the dramatic license.

Airtable, it's been real. Tiger Den is better. Tanya is proof.

This post was reviewed and approved by Tanya before publishing. Zero AI agent skills involved.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse