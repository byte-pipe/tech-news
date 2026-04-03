---
title: 'AI Dev: Testing Kiro - DEV Community'
url: https://dev.to/maximsaplin/ai-dev-testing-kiro-3b5j
site_name: devto
fetched_at: '2025-08-28T10:02:05.299779'
original_url: https://dev.to/maximsaplin/ai-dev-testing-kiro-3b5j
author: Maxim Saplin
date: '2025-08-25'
description: Kiro is a yet another VSCode fork (just like Cursor or Windsurf) that integrates AI coding features.... Tagged with ai, coding, genai, llm.
tags: '#ai, #coding, #genai, #llm'
---

Kirois a yet another VSCode fork (just like Cursor or Windsurf) that integrates AI coding features. What caught my attention was the "spec-driven development" > it makes total sense proposing a structured approach to dev (as opposed to "vibe coding"). I got my invitation and over the weekend tested Kiro. I decided to re-create a command linecross-platform disk performance benchmarkthat was built in 2018 using .NET. This time I picked Rust and used AI. My expectations were low, yet I was impressed in a good way, I (or was it Kiro) did build a working app with solid test coverage! At times Kiro was left alone working for extended periods of time following the plan... And it maintained coherence - that impressed me the most. The result is not perfect, there're some things that don't work (i.e. CI/CD is broken and God knows how much time is needed to recover it), nevertheless part of blame is on me, I could have asked for less and be more attentive to the specs. Over the course of my experiment I have extensivelydocumented the process. These notes were used to create the below blog post using Grok 4.

Update, Aug 27:After spending few more days with the app Kiro produced I am less enthusiastic. Kiro still falls for the shortcomings of other AI tools that eagerly produce code and complete the prompt "no matter what" > I poked cpdt2 codebase, using Cursor and Kiro and trying to recover CI/CD making it work, trying to get the app compile and run in Linux (under Dev Containers) - and non of the attempts succeeded under reasonable time. A classic AI SDLC dilemma, getting the result fast, wasting loads of time fixing and making it working. I think Kiro is a powerful tool (staying coherent while working on multiple tasks) yet when left unattended it can easily bloat your solution with loads of scope you, as a human, wouldn't be able to process. Is it the problem of the tool or of a human using it? Part of issue is on me, could have been more thorough and critical when sketching the specs. Anyways, below is a sample of me trying to make the integration tests running fast, launching a "spec > design > task" loop eventually discovering that I messed up "memory-mapped" files with "in-memory" files (when requesting for the feature) and went the wrong route discovering that after 1-2h of time was wasted. Btw, in a separate chat Kiro happily acknowledged the issue (and btw whatever it proposed in this chat was also not feasible):

Hey folks, it's Maxim here—back with another dive into the wild world of AI-assisted coding. If you've read mypiece on Continue.dev, you know I'm all about testing these tools in the trenches, warts and all. This time, I spent a lazy Sunday (well, "lazy" if you ignore the occasional CoD: Modern Warfare 3 breaks) experimenting with Kiro, a new AI-native IDE that promises "Spec-Driven Development." Spoiler: It turned a vague prompt into a fully functional cross-platform Rust app, but not without some hilarious detours and existential questions about my role as a developer.

Back in 2018, I builtCrossPlatformDiskTest (CPDT), a .NET-based storage speed tester that racked up 500k downloads on Android. It measured sequential/random reads/writes, memory copies, and more—nothing fancy, but it scratched an itch for benchmarking drives across platforms. This GUI app is in turn based on aCommand Line Tool. Fast-forward to 2025: I decided to recreate the CLI version in Rust (a language I barely remember from a 2021 LinkedIn course) using Kiro. No hands-on coding from me—just prompts, reviews, and AI orchestration. The result? A repo calledcpdt2with 72 files, 13k lines of code, 246 tests, and even GitHub Actions for CI/CD. But let's break down the journey, because this wasn't just coding—it was coding while AI did the heavy lifting.

## The Setup: From Prompt to Plan

Kiro's big hook is its structured workflow: Spec > Design > Tasks, all in Markdown. It's like forcing yourself to think before you code, which is honestly a breath of fresh air compared to the "prompt-and-pray" chaos of other tools.

I kicked things off with this prompt:

I want to create a cross-platform disk speed test utility. It must be compilable as a command line tool for macOS, Windows, and Linux. It must have an isolated library/component that runs the speed tests and that I can later integrate with other non-CLI apps (e.g., GUI). The tests must include sequential and random read and write measurements with block sizes of 4MB for sequential and 4KB for random (default can be overridden), it must create a test file in a given device (CLI must provide a list of devices available in the system, for system drives utilize OS facilities to get writable app folder). The app must mitigate the effects of buffered reads and cached writes (by default disabling those). The stats collected must include min, max, and avg speeds. Additionally, the app must implement a 5th test - memory copy.

Enter fullscreen mode

Exit fullscreen mode

Kiro (powered by Claude 3.7 or 4—I stuck with 4) fleshed it out into requirements, added niceties like MB/s units and progress indicators, and even suggested Android/iOS support when I nudged it. It generated a design doc, broke everything into 23 traceable tasks (e.g., core library setup, platform-specific implementations, CLI args, tests), and queued them up.

Kiro UI? Clean and intuitive—rounded corners, tabbed chats, and a content pane that feels like a souped-up VS Code. One quirk: Use#instead of@for context in chats. I stumbled there once, but overall, it was smooth sailing.

## The Build: AI Takes the Wheel, I Play CoD

With tasks queued, Kiro started chugging away. It handled everything from project setup (Cargo.toml, build.rs) to platform-specific code for Windows, macOS, Linux, Android, and iOS. I "supervised" by reviewing diffs in Cursor (using GPT-5 at high reasoning mode) and occasionally fixing linter warnings or slow tests.

Highlights (and lowlights):

* Early Wins: Tasks 1-5 flew by—core config, progress tracking, stats. Kiro even added unit tests when I prompted. A quick Cursor review confirmed it was solid, though I had to install Rust manually after a terminal hiccup.
* Platform Shenanigans (Tasks 6-8): Implementing non-buffered I/O across OSes? Kiro nailed it, but linter warnings piled up in unrelated files. I copy-pasted errors into the chat; Kiro fixed most, but it sometimes "hallucinated" checks. Still, better than older LLMs that'd just generate BS.
* Testing Drama (Tasks 9-17): The first real run was Task 9. Tests took forever (47 seconds initially) because of oversized files like 2GB dummies. I manually timed them in VS Code's Test Explorer and prompted fixes—down to 13 seconds. One test suite hung for 10-20 minutes; Kiro eventually debugged it. I even created Cursor rules for "runtime checks" (build, test, run the app) to double check after Kiro.
* The Big Queue (Tasks 18-23): I dumped the rest in one go. Kiro took ~1 hour, pausing twice for CLI approvals. It added 120+ tests, code coverage tracking, docs (like TESTING.md), and even GitHub Actions for CI/CD—plus a release script for crates.io. Mind-reading? I was thinking about CI/CD, and poof, there it was.

Meanwhile, I switched tabs to save Urzikstan in CoD MW3. Vibe-coding at its finest: AI builds while I snipe baddies. But cracks appeared—integration tests felt inconsistent, and I had to revert/restart once due to messy file placements (Rust's idiomatic unit tests in-source files tripped me up, given my rusty Rust knowledge).

I used Cursor and GPT-5 High between the Kiro tasks to review Git diffs - not much value, most of the reveiws where "OK" and the rest of the doc I didn't care to read.

End result? The app runs! Pick a path, run benchmarks, get stats. It even lists devices and handles caching as specified. But oops—one original req (interactive device selection for system drives) got lost in the shuffle. And 35 linter issues lingered, plus failing GitHub Actions. Fixable, but a reminder that AI isn't perfect.

## Code Stats: Bloat or Brilliance?

Compare cpdt2 to my 2018 .NET version:

* cpdt2 (Rust + AI): 72 files, 13k LOC, 1.9k comments, 3.5k blanks. Includes benches, docs, scripts, and heavy testing/CI.
* 2018 CPDT (.NET): 23 files, 1.8k LOC. Leaner, but no automation.

AI inflated the codebase (thanks to tests and infra), but it works cross-platform without me writing a line. In 2018, that took a week of my life; this was one Sunday.

## Reflections: Is This the Future of Coding?

Kiro enforces discipline—think before coding—which aligns with prompt engineering best practices. It's not just "prompt > code"; it's a harness for coherent, long-horizon work. The agent stayed on-task for hours, breaking down complexity without losing context.

But here's the rub: I coded blindly, barely glancing at the code. Am I even a developer anymore? It felt like pushing buttons while AI steered—fun, but I lost touch with the codebase. Maintainability? No clue. And without my prior CPDT knowledge, I'd be lost prompting effectively. Non-tech folks? Forget it; this still needs domain expertise.

Side thoughts: Are high-level languages becoming assembly? I don't grok Rust tooling, but do I need to? AI rejection of dumb asks (e.g., fixing non-existent code) is a win over older models. Yet, running in a container from the start would've avoided potential disk litter from test files.

Overall, Kiro's a promising tool—like a Swiss Army knife that mostly cuts, but occasionally needs sharpening. It turned my experiment into a working app, honed my "AI orchestration" skills, and left me pondering: If AI builds while I game, what's left for humans? Dive in, try it, and let me know your thoughts in the comments!

If you're curious, check outcpdt2 on GitHub. And yes, I'll fix those linter warnings... eventually.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.
 Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse
