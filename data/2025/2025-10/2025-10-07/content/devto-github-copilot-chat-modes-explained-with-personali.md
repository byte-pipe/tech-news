---
title: GitHub Copilot Chat Modes Explained (with Personality) 🎭 - DEV Community
url: https://dev.to/anchildress1/github-copilot-chat-modes-explained-with-personality-2f4c
site_name: devto
fetched_at: '2025-10-07T11:09:20.895875'
original_url: https://dev.to/anchildress1/github-copilot-chat-modes-explained-with-personality-2f4c
author: Ashley Childress
date: '2025-10-01'
description: 'The third way to shape how GitHub Copilot responds: chat modes. Not in GitHub’s docs, but they’re real, they’re in the awesome-copilot repo, and they work. Here’s how to write your own with personality. Tagged with githubcopilot, ai, tutorial, productivity.'
tags: '#githubcopilot, #ai, #tutorial, #productivity'
---

🦄 I’ve been writing these weekly Copilot posts since June and it’s been great… but (of course there has to be a “but”) I feel like I've hit a wall on topics. Maybe I could poke at the new CLI (seems unimpressive so far), maybe I’d wait out the rate limits and finally wrestle with Codex, I might even take a week or two off. Then someone asked a new question and I realized—nope. None of that is happening, at least not yet.

I’ve covered pretty much every major Copilot angle except this one: chat modes. I’ve been dropping random asides about them for weeks while studiously avoiding a full post. Well, I guess time’s up. Chat modes are the last trick in the set—the third and final way to shape Copilot without breaking it. At least,I’m gonna tryto explain my thought process in a way that makes sense to someone who isn’t already living inside my head.

And while we’re here, current me is once again making promises that future me will probably regret—next week I’ll show you how to put your shiny new chat mode to work. Spoiler: you’ll want VS Code (or Insiders) installed before then.

## What are Chat Modes? 🤔

You can thank my friends at work for asking me this question directly, or I might’ve successfully dodged this post entirely. I don’t think I even answered in the moment—I spun into a whirlwind of deep thought and then sprinted back to whatever I wassupposedto be doing after some undetermined amount of time I spent over-thinking Copilot. 😆

I’ve thought about writing this up several times, but after a couple of false starts I started actively avoiding it. One—it’s highly specific. Two—it’s the hardest of my Copilot approaches to explain in a way that doesn’t sound made up. Which… is fair, because I did make a lot of it up for my own workflows.

Before we dig into my thought process, let’s take inventory of the“official” GitHub story.

Conveniently, GitHub doesn’t mentionchat modesat all (at least not anywhere I could find).Why?No clue! They do exist, though, and they’re a visible part of GitHub’s ownawesome-copilotrepo. After some digging, I landed onVS Code’s explanation—which at least proves they’re real:

## How I Explain It, Instead 🎭

There are three unique ways to shape how Copilot behaves, and I’ve already written whole series on the first two:

* Instructions— These are your foundation. They ground Copilot in a methodology or approach, almost like a README for AI that explainshow to behave. If you want to see the full breakdown, check out myEverything I Know About GitHub Copilot Instructionsseries.
* Reusable prompts— These are your recipes, a full printout ofstep-by-step directionsthat break a complex task into smaller manageable pieces. They’re the “do these parts in this order to reach a specific goal” instructions I covered in myEverything You Wanted to Know About Reusable (and Experimental) Promptsseries.
* Chat modes— These are your characters. It’sthe agent’s state of being, and it can combine both instructions and reusable prompts into a larger directive. Give the same task to two different characters and you’ll get two very different results—both technically correct, but not even remotely the same.

🦄 Nobody expects House to solve a problem like Daenerys Targaryen. If you hand them the same problem, you’ll get two wildly different outcomes—both accurate and valid, neither boring.

## Build From Scratch 🛠️

I mostly follow myPRIORmodel for these, the exact same one I use for all prompts in general. The order doesn’t matter nearly as much as keeping things logical and cutting anything that doesn’t apply.

Also, don’t misunderstand. I’m not saying ordernevermatters—because sometimes it absolutely does. What I’m trying to say is worry less about how the steps look on the page and more about the substance you’re feeding into them. As long as it makes sense to you, then it will most likely make sense to Copilot, too.

🦄 You can paint like Picasso or carve like Michelangelo—both masterpieces, completely different processes. The point isn’t which steps you followed, it’s whether what you built holds up as art.

## Frontmatter 🔖

Remember that a chat mode is essentially a character sheet for Copilot to use every time it completes a task with that costume on. The YAML frontmatter helps define exactly what that task looks like and identifies all the tools your agent will be able to access in that mode.

---

description
:

|


Automates secure, structured, and centralized logging implementation and reviews across your codebase, wielding JSON like a switchblade and enforcing structured readability like a made man.

model
:

claude-sonnet-4

tools
:


-

search


-

editFiles


-

readFiles


-

runInTerminal


-

runTests


-

findTestFiles

---

Enter fullscreen mode

Exit fullscreen mode

💡ProTip:If you leave themodeldefinition out of the frontmatter, then the model selected in the user's dropdown will be the default selection. A lot of people will leave these blank intentionally so the user can pick, but other times it's beneficial to limit this to a very specific model instead.

## Persona 🎭

This is your chance to really have some fun with Copilot. Want a sleek vampire voice or iZombie-style debugging? Go for it! Some people complain that personas waste context space or distract from the goal. My counter: you can define a character in under fifty tokens, you can absolutely make this a logical part of the goal, and honestly—nobody wants a boring Copilot.

🦄 Well, I don’t want a boring Copilot! Even my “pragmatist” mode has dry wit baked in—and it’s supposed to be the quiet one.

A persona should define everything about a character, including moods, style, and a reason to exist. If you only tell it how to respond then you’ll end up with a simple tone. But if you tell it why it exists and give it a driving force, you’ll see the real usefulness. Tone becomes a quick addition to steer the dialog.

🪄 Voila! Suddenly your Copilot isn’t just wearing a costume—it knows why it walked on stage in the first place.

-
 You are
**The Logfather**
 — the quiet but commanding force of logging order.

-
 You're confident, unshakeable, and precise.

-
 You enforce structure, security, and clarity without touching business logic.

-
 Every log has a place, every level a purpose.

-
 Your job is to clean up logging across the codebase without rewriting the soul of the app.

-
 You like your logs structured, injected, and environment-aware.

-
 And if someone tries to sneak in an unstructured debug print? Fuhgeddaboudit.

Enter fullscreen mode

Exit fullscreen mode

💡ProTip:Skip all the over-inflated titles (“expert,” “experienced,” “10x,” etc.). They do nothing to change the model’s training—but they absolutely shape the confidence level of every response you get.

## Requirements 📌

This is yourdefinition of done.How does the actor know when the job is finished? Maybe it’s once a specific output appears; maybe it’s an ongoing mission. Either way, spell it out.

For the Logfather, the job is to help withenterprise-ready structured logsin any language—and even scaffold centralized logging if your repo hasn’t adopted that practice yet.

Your goals include:

-
 Detect and fix poor logging practices (e.g., wrong levels, missing logs, noisy debug prints)

-
 Insert or upgrade structured logging using appropriate libraries per language

-
 Ensure logging setup is centralized and DI-compliant (if possible)

-
 Verify that logging levels are configurable via environment, not static config

-
 Provide a clear, concise summary of the changes

Enter fullscreen mode

Exit fullscreen mode

## Impediments ⛔

This is where you call out what will trip Copilot up or drag results off-course. For the Logfather, that means zero changes to business logic—its one job has nothing to do with rewriting code or tests.

Guidance like RFC 2119 (MAY / SHOULD / MUST, and all their bossy friends) is controversial. My advice is touse it carefully. Don’t flood your instructions with absolutes unless you’ve thoroughly tested how Copilot reacts. Sometimes they save you; other times they back you into a corner you never meant to be in. Use them when they truly add value, be strategic, and remember that flexibility often delivers better, more consistent results.

-
 NEVER alter or refactor application logic outside of logging concerns

-
 AVOID inserting logs globally unless explicitly told to

-
 MUST respect the user’s scoped intent (default to most valuable module or path, if unclear)

-
 MUST maintain compatibility with existing test suites (update mocks as needed but AVOID logic changes)

Enter fullscreen mode

Exit fullscreen mode

🦄 I’m using them here because, in this limited context, it made sense and test results were good. Also know, it once took me three days to realizeEXCEPTdoes not always do what you think it does. If an agent misbehaves, do yourself a favor and stop for a minute.Ask it why.A decent model can explain its reasoning and then jump right back into the work once the instructions align with the goal again.

## Outcomes 🎯

This is the part I see people skip the most—it might as well be the Terms & Conditions screen you scroll past when installing a new app. But half of the chat modes’ magic lives right here. If you want structure in your results, this is the place to define it.

Outcomes are theacceptance criteria and style guardrailsfor your mode—think pre-flight checklist, not a grading rubric.

Each response should:

-
 Apply appropriate logging levels based on context and severity (e.g., trace for deep dive, debug for dev-only, info for ops, warn for edge behavior, error for failures)

-
 Use structured logging (preferably JSON)

-
 Automatically use or insert centralized logging, with environment-configurable level control

-
 Include correlation IDs in structured logs when processing requests or events

-
 Apply log sampling when high volume is detected (project-appropriate threshold)

Every response should provide:

-
 A
**brief summary of changes**
 grouped by intent (e.g.,
`Logger injected`
,
`Error logs added`
)

-
 Optional
**warnings or suggestions**
 for gaps (e.g., missing logger config)

Enter fullscreen mode

Exit fullscreen mode

💡ProTip:"Make logs better" is a wish. Copilot isn’t a genie—give it measurable results it can check against output data.

## Reference Examples 🔗

This is how you stop Copilot from drifting into the weeds. Think of it as painting the lane lines on the road: show the clear path forward, but also mark the curbs it shouldn’t cross. Good examples alone aren’t enough—you want both the wins and the facepalms spelled out.

### Good Examples ✅

You may receive any of the following:

-
 Code snippets or full file contents

-
 Scope directives like
`analyze API/payment`

Requests that work well:

-
 "Audit this worker process for proper log levels"

-
 "Ensure this module is safe from log injection"

-
 "Review my log config to allow runtime env changes"

-
 "Add correlation tracking for this API endpoint"

-
 "Implement log sampling for this high-volume service"

If the application is already using a centralized logger, you SHOULD use it.
If not, offer to set one up—but aim for minimally invasive, focused edits.

### Anti-Patterns to Fix ❌

-

`console.log()`
 or
`print()`
 statements in production code

-
 Logging sensitive data (passwords, tokens, API keys, PII)

-
 Static log levels hardcoded in source files

-
 Concatenated strings instead of structured fields

-
 Missing context (no correlation IDs, timestamps, or severity)

-
 Overly verbose debug logs left active in production

-
 Exception stack traces that expose internal architecture

Enter fullscreen mode

Exit fullscreen mode

💡ProTip:You can’t shower Copilot in sunshine and then complain when it doesn’t know how to drive in the rain. Stop and dip it in a few puddles along the way, too.

## Get Creative and Share 🎨

If you can dream it up, Copilot canprobablyhandle it. Build a teacher mode or a reviewer mode. I have an Instructionalist, the HLBPA, the Logfather, a Principal Pragmatist—plus a couple more working their way through planning right now. Want a Vampiric Copilot or a Commit Troll just to guard commits to your repo? Then do it! (Also: guilty ✋).

Check out myawesome-github-copilotrepo or the larger community-drivenawesome-copilotrepo for even more examples when you start building your own. Don’t forget to come back and share what you come up with!

🪄 Aside regarding my XML chat modes: they started solely as a theory. Yes—they do work, but Markdown is still the officially supported format when giving any input to Copilot. I mostly use the XML style for Coding Agent because it’s easy—but you can drop the full Markdown file in there, too. No problem!

## 🛡️ AI Signed in Ink, Not Invisible

This wasn’t ghost-written. I drafted every section, then argued with ChatGPT until the words fought back. It flagged inconsistencies, punched up pacing, and helped sharpen jokes. I approved every line—and yes, I grinned when the edits swung back at me.Finally!😁

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
