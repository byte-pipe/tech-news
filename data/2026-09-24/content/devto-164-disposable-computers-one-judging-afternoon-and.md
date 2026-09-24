---
title: 164 disposable computers, one judging afternoon, and a question nobody had time to ask - DEV Community
url: https://dev.to/lolocoding/164-disposable-computers-one-judging-afternoon-and-a-question-nobody-had-time-to-ask-19da
site_name: devto
content_file: devto-164-disposable-computers-one-judging-afternoon-and
fetched_at: '2026-09-24T21:57:42.583724'
original_url: https://dev.to/lolocoding/164-disposable-computers-one-judging-afternoon-and-a-question-nobody-had-time-to-ask-19da
author: Lauren Lee👩🏼‍💻
date: '2026-09-18'
description: 'Does it build? I have run hackathon judging the careful way. By that I mean: rubrics... Tagged with hackathon, showdev, opensource, devrel.'
tags: '#showdev, #hackathon, #opensource, #devrel'
---

## Does it build?

I have run hackathon judging the careful way. By that I mean: rubrics written before submissions open, 3 judges assigned to each project, scores reconciled in a calibration call, and a technical reviewer for anything in contention for a prize. And in all of that, one question never made the list, because there was never time to ask it of 60 teams: Does it build?

As organizers, we can build a fair and honest process for judging projects. But one thing a weekend hackathon rarely has time to do is build the code. A well-run panel will clone a handful: the ones a reviewer flagged, the ones near the prize line, the one whose README made a claim someone didn't believe. 5 or 6, perhaps, out of the 60. The rest are evaluated on what they claim to do.

No panel is failing here. The clock is, and frankly, so is the math.

## Do the math on a judging afternoon

Close your eyes. Picture the standard weekend hackathon. 48 hours, somewhere between 40-80 teams, and at the end an expo: tables in rows, laptops open, a team at each one waiting to demo. Judging happens on foot. Each judge takes a slice of the room and moves table to table: 4-5 minutes each, hear the pitch, watch the demo, ask one question, score on a phone, move on.

5 minutes is enough to hear a story and form a view. It's not enough to clone a repo, install its dependencies, and find out whether the thing you were just shown builds anywhere other than the machine it was shown on. If you tried, you'd finish your slice sometime after the pizza ran out.

A demo that works simply proves that their laptop works.

So the format grew a process shaped by its constraint, and over the years the constraint faded from view. Rubrics grew categories for innovation, presentation, user experience, and sponsor alignment, and rarely a line for "Does it build," because there was no honest way to fill it in for 60 teams before the venue closed. Some ecosystems now compile the smart contract, which is real progress. Almost no one builds the entire project, and the few who do are running 60 strangers' install scripts on their own laptops, where any one of those scripts can read their files, their keys, and their browser sessions😳

The result is a competition that measures the ability to describe software. And yes, that's a real skill. But it's a different skill from building software, and the first has stood in for the second for as long as hackathons have existed. Teams understand this better than anyone, which is why the pitch gets more rehearsal on Sunday afternoon than the build actually does.

For most of my career, that was a fact about the format, like the weekend or the pizza.

Then I spent a week finding out it no longer has to be.

## What changed is the price of a computer

I had been messing about withFly.io's Sprites, which hands you a fresh Linux machine through an API call, bills you by the second, and lets you throw it away when you're done. I wanted an excuse to build something real with them, and the judging problem was sitting right there. If a clean machine costs a fraction of a cent a minute and appears in seconds, "build every submission" stops being a fantasy and becomes a for loop.

So I wrote one. Hand it a list of repositories and, for each one, it creates a machine, clones the repo, works out what kind of project it is, installs the dependencies, compiles whatever there is to compile, runs whatever tests exist, and writes downexactlyhow far it got.

npm run judge 
--
 
--input
 submissions.csv 
--executor
 sprites 
--concurrency
 4

Enter fullscreen mode

Exit fullscreen mode

That's the whole tool. The interesting part iswhat it refusesto do.

## What the tool refuses to do

It refuses to give a score.Every submission lands on one rung of a ladder, and the rungs are facts, not subjective opinions.

Rung

Meaning

Unreachable

the repository is gone, private, or was never a repository

Empty

it exists but has no meaningful code

Not evaluable

has code, but needed a toolchain my machine could not obtain; that failure is mine, not theirs

Install failed

dependencies would not install

Build failed

installed, but would not compile or build

Installed, no build

installed; there was nothing to build or check

Built, no tests

built; no tests to run

Tests failed

built; tests exist and fail

Tests passed

built; tests pass

A judge can argue with a score. They can't argue with exit code 2 at line 40 of the type checker.

It refuses to share a machine.A hackathon install script can do anything at all, from writing to your home directory to installing a global package that changes how the next project behaves. Run 60 on one runner, and project 40's result depends on what 1-39 left behind. Run each on a fresh machine, and every result stands independently on its own. That same isolation makes it safe to build a stranger's code: whatever an install script does, it does to a machine you were going to throw away anyway,not to yours.

It refuses to blame the team for my mistakes.If a clone fails because the repository is gone, that's on them. If it fails because my machine couldn't reach GitHub, or didn't have the right compiler installed, that's on me, and the tool says so in a separate category instead of marking the project as broken.

It refuses to throw away a failure.When a build breaks, the machine is checkpointed and kept, frozen at the moment it broke. Anyone with access can open it and see the exact state. A passing project's machine is deleted. There's nothing to look at. The machines are named by hash, so even the dashboard is a list of anonymous builds. Not a list of teams.

A failing project's machine is a piece of feedback a team can open.

The run itself is unremarkable. Which is exactly the point. 164 submissions, 4 at a time, done in about 55 minutes while I made lunch, a median of 58 seconds per project. Every run in this post, including the ones I got wrong and had to repeat, cost a little over a dollar in usage. Imagine how long it would have taken to read 164 READMEs.

Every run in this post, on Fly's Cost Explorer: 2 days, $1.01 of usage.

## What 164 projects look like when you build them all

The submissions came from one event, and I ran them all.

Of 164 submissions from a single hack, 113 built end to end: 69%.33 installed their dependencies and then failed to compile or build.8 would not install at all.9 installed and had nothing to build, which is its own kind of answer.1 repository was reachable on my first run and gone by my second, a day later.

I want to be careful about what "built" means here. It means the compiler accepted the code and the build script exited 0. It does not mean the project works, does what the README says, or would survive contact with a user. Building is the least a piece of software can do. It would be easy to read the 69% as projects being good. Of the 51 that did not build, 10 had either nothing to build or nothing to clone. The other 41, a quarter of the cohort, would not have built on any machine but their authors'. And at the judging table they looked identical to the ones that would, so every decision was made without the one fact that separates working software from a working demo.

The failures had shapes:

* The most common was a contract that compiled cleanly with an application around it that didn't: the hard part worked, and the ordinary part (a TypeScript error, a missing build artifact, a package that never resolved) was what broke.
* Second was the monorepo where one package failed and took the build with it.
* Third, and rarest, was a repository that was a README and a diagram. Those are types, not teams. No project in this post is identified, and none will be.

## Did they use the sponsor's tech or just the sponsor's logo?

Every sponsored hackathon has a second question underneath the first. Sponsors put up prizes to see their technology used, and the standard way to check is to read the README and look for the logo on the slide.Teams know this too.

Some of that question is machine-checkable, and some isn't. Checkable: does the repository contain a contract for the sponsor's platform at all? Is that contract the starter-kit example with the names changed? Does it use the platform's distinguishing feature or only the parts any database could do? Does it compile? In this cohort, 157 of 164 had a contract, exactly one was the example template with a fresh coat of paint, and 114 of the 157 compiled with the compiler version the contract itself declared. That last clause matters, and I'll come back to it.

Not checkable: whether the use was meaningful. A contract can declare a private input and do nothing interesting with it. The tool can tell a judge where to look. It cannot tell them what to conclude, and a tool that claimed otherwise would be doing the thing this whole post is against.

## What the tool can't tell you and what I got wrong

Built is not the same as correct. "Tests passed" needs a caveat of its own: most teams started from a starter kit that came with tests already written, so a passing suite may be the starter's tests, untouched, and the tool can't yet tell those apart, which is why this post quotes no test-pass rate.

The tool answers one question, "Does it build?", and that's the lowest bar software can clear. It has no opinion on originality, difficulty, or whether the thing is any good. It can't see ambition either, so a team that attempted something hard and fell one compile error short lands on the same rung as a team that shipped a to-do list. Judges can see the difference. The tool is there to make sure they also see which one builds, which is exactly why it belongs beside a judging panel and not in place of one.

Then there's the mistake. The first version chose a compiler by date, the newest that existed when the repo was last touched. But a contract declares which language version it was written for, and a new compiler had shipped between the event and my run. 42 working contracts came back as failures, blamed on their authors, until the tool learned to read the declaration and install the compiler each contract asked for. The tool that exists to catch confident wrong answers produced one, and I only caught it because the error messages were all the same. It did it once more, after I thought it was finished: 6 build failures were my sandbox missing a compiler version the teams had pinned in their own scripts. All 6 build, and the numbers above are the corrected ones.

The compiler fix produced one more number worth knowing: compiled with today's release instead, a third of the working contracts no longer built. Every fast-moving platform does this to its early builders, and that's why you have to ask, "Does it work?" with the tools the team had, not the tools that shipped last week.

## Tips before you run your next event

1. Run every submission before judging opens, and hand the judges the ladder. Not a score, a rung. The panel still decides what matters. They decide it knowing which projects build.
2. Give failing teams their machine. The tool saves it at the moment the build broke, so the team can open it, see the exact error, and fix it. Most hackathon teams have never received feedback that specific, and a saved machine costs nothing to keep.
3. Put "Does it build?" on the rubric. It was left off because it couldn't be filled in honestly for 60 teams in an afternoon. It can now, in about the time it takes the pizza to arrive.

Next, I'm taking my own advice: giving those 39 broken builds to an agent with a shell, a time limit, and one instruction. Make it build, and tell the team what was wrong. More on that in thenext post😉

The tool is on GitHub atgithub.com/laurenelee/hackjudge.It's small, opinionated, and yours to run on your own submissions if you'd like!

Find me@lolocoding👩🏼‍💻

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse