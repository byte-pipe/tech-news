---
title: Everything I Know About GitHub Copilot Instructions — From Zero to Onboarded (For Real) ⚡ - DEV Community
url: https://dev.to/anchildress1/everything-i-know-about-github-copilot-instructions-from-zero-to-onboarded-for-real-4nb0
site_name: devto
fetched_at: '2025-08-19T22:01:59.480797'
original_url: https://dev.to/anchildress1/everything-i-know-about-github-copilot-instructions-from-zero-to-onboarded-for-real-4nb0
author: Ashley Childress
date: '2025-08-13'
description: Everything you need to know about Copilot custom instructions — why they work, how to write them, and how to go from zero to useful fast. Tagged with githubcopilot, ai, productivity, learn.
tags: '#githubcopilot, #ai, #productivity, #learn'
---

Updated: Yes — I had to change the banner. It was killing me 🤣 I'm going to get Leonardo trained with this charactereventually. In the meantime ChatGPT is doing just fine (after you ignore the personality change and retraining brought on by the v5 upgrade).

🦄 I honestly hadn’t planned to write this one until next week, but the post Ididwrite this week... disappeared. And redoing work you’ve already done?Zero fun.It’s like reheating French fries —technicallyedible, but you know it’s not going to be as good. So here we are, skipping the fries, and moving on!

Also, you might want a snack for this one! It's a little more in-depth than usual. And yes — I did rate my own approach higher than Microsoft and GitHub. Obviously. 😛

## TL;DR 🪼

Stop tossing Copilot into the deep end without floaties! Write repo instructions, test them, tweak them, build them, repeat. Whether you use Microsoft’s, Coding Agent’s, or my Instructionalist, the goal’s the same: keep Copilot coloring insideyourlines.

## Background

This post is one part personal call-out (Ireallyneed testers 🙋‍♀️) and one part sequel to my most-read postAll I’ve Learned About GitHub Copilot Instructions (so far).

If you've never read it or if you missed some of the more recent updates (yes — I always try to go back and call out changes whenever GitHub or VS Code changes something), then go check out the basics first before getting too deep here. If you're already up to speed? Great — hop on in and I'll give you the grand tour! 🏎️

The original post still represents ~95% of how I handle custom instructions. I still use almost everything in it. But a few things have changed — new ways to get started, lessons learned from letting Copilot roam — on a leash — in enterprise codebases, and a sharper focus on making it write what you want instead of what it thinks you might have meant.

🦄 Also, yes,shameless plug:I started anawesome-github-copilotrepo. It’s still a WIP, but there are already a few gems in there. If you’re willing to be a guinea pig 🐹, reach out!

## Why Repo Instructions Matter ⚠️👇

Let’s set the scene. You’ve got a legacy monster app sitting in the corner.No onewants to touch it. And now a brand-new senior dev walks in the door. Would you say:

“Hey, go refactor something. Good luck!”

Of course not!But that'sexactlywhat's happening every single time you drop Copilot in cold with zero guidance or direction about what you expect. It will producesomething— and it will produce itconfidently— and based entirely on your repo’sworstpatterns. You’ll get more code, faster, sure... but not at all better!

### Plan an Up-Front 15 Min ⌚️

So instead of sending your golden senior developer off to the trenches on their first day, what if you just took15 minuteswith them?Explainwhy half the code is wired together like an escape room puzzle, which systems will blow up if they touch the wrong file, and why thatjava.ioserialization is still hanging around after three Java upgrades.

That’sexactlyhow you should treat Copilot.

And you'll see the exact same returns from Copilot as you would any well-trained developer who's capable of reading documentation and making the right call when it matters.

🦄Be aware:This isnevergoing to be a "set-and-forget" system. It doesn't need constant care like a newborn (after a solid round of testing), but it's still gonna grow and change with your app. App changes = instructions change. Always!

### Repo Instructions to the Rescue 🚢🛟

Repo instructions are your chance to give Copilot a tour before it starts swinging a hammer. They work everywhere Copilot runs — IDE, GitHub.com, even mobile (according to the docs anyway). Put them inmain, and suddenly everyone prompting Copilot is working from the same rules, style, and “don’t touch” list.

If you're thinking about simply listing best coding practices just to show Copilot where commas go? You're not using them correctly. Start thinking of these files as the de facto onboarding for any senior dev and approach them with that level of info and let the auto-formatter handle the commas and new lines.

💡ProTip:Copilot will naturally catch on, but a quick one-liner that says "Follow rules in [eslint.config.js](./eslint.config.js)" is generally all you need to have it start checking the lint commands automatically.

Start small and don't get the file get too bloated. If you have a set of similar instructions, you can always break them out into a custom instruction file apart from the primary version. Then useapplyToin the front-matter to define which files they should be applied to.

For example, you have specific database instructions that outline constraints or upcoming planned features and you want to start "forward thinking"? Put them in.github/instructions/database.instructions.mdinstead of the default file and add theapplyTo. Any time Copilot references one of these DAO classes, these instructions would be attached automatically.

---

applyTo
:

src/main/java/dao/**/*

---

# My Custom Database Instructions

Enter fullscreen mode

Exit fullscreen mode

## The Three Best Ways to Get Started

### 1. Microsoft’s “Generate Instructions” in VS Code (⭐️⭐️⭐️)

When this first came out, I’ll be honest — I hated it. I mean, it wasbad. “Go read the first line of every file in the repo, copy/paste them into a doc, and call it instructions” bad. It was like your coworker emailing you a Google search link instead of an actual answer.

But I have to be fair — it’s better now. It actually reads your repo, finds the important stuff, maps out project structure, and even calls out workflows and automation. Still not perfect, but you could hand it to a new dev and they wouldn’t immediately run screaming.

💡ProTip:Let your formatter + linter handle style rules so you don’t waste instruction space showing Copilot where commas go. Absolutelyno oneneeds 14 examples of what JavaScript looks like in their instructions file.

#### How to run it:

💻 Expand for screenshots in VS Code for generating Microsoft repo instructionsIn VS Code:Click the gear icon ⚙️ at the top of the chat window.ClickGenerate InstructionsLet it run.Then, like any responsible repo owner,trim the fluffbefore committing.Alternate:PressCtrl+Shift+P/Cmd+Shift+P.SearchChat: Generate Workspace Instructions File.

### 2. Coding Agent (⭐️⭐️⭐️½ – creeping toward 4)

This one’s a little different — it runs onClaude Sonnet 4, and no, you don’t get to change that. The upside? Claude’s got a good sense of architecture and implementation strategy, so it’s a bit like asking the “big picture” person on your team for a first draft. The downside? If you aren’tspecific, it’ll start guessing... and you might get a fully stocked contributor guide when you really just wanted repo setup notes.

Coding Agent is also PR-safe — italwayscreates a separate branch. You could tell it “go wild,” walk away, and it wouldn’t touch your main branch without a pull request. Bonus — you can prompt it with a mini-series and as long as it fits in the single prompt, it will tackle your whole list for a single premium request.

💡ProTip:Thespecificshere are key. Think of it like you're leading KT. What are all the important highlights that you'll need to get the basics across? If you're not sure, it's better toomitsomething than be wrong or mention amaybethat will force Copilot to guess on your behalf.

#### How to run it:

💻 Click for screenshots on GitHub.com for generating repo instructions with Coding AgentAt GitHub.com/Copilot:Go toGitHub.com/Copilot.ClickAgentsin the lefthand sidebar.Pick your repo + base branch (Copilot will still make its own branch from there).Prompt it: “Generate custom repository instructions for this repo” + any importantspecifics.

### 3. My “Instructionalist” Chat Mode (⭐️⭐️⭐️⭐️, with bias admitted)

Okay, yes, I’m biased. But this thing exists because I got tired of explaining — for the fourth or fifth time — why every repo should have good Copilot instructions.

It’s a Q&A where you (aka the person who actually knows the repo) fill in the stuff Copilot can’t guess: your SLAs, the weird dependencies that no one touches, the “if X happens at 3:15 AM, restart Y or the whole system falls over” kind of lore.

It writes from “where we want to be,” not “where we are,” and builds in things the other methods skip — anti-patterns, testing goals, deployment notes, even gentle nudges like “acknowledge uncertainty” when multiple solutions exist.

📢Model note:This one’s running on GPT-4.1 too!

#### How to run it:

💻 Click for a quick video on loading custom chat modes in VS CodeCopy the chat mode:My repo is atgithub.com/anchildress1/awesome-github-copilotFindThe Instructionalistchat mode and copy raw content⚠️Careful!Don't grab docs by mistake. You're looking for the file that ends in.chatmode.mdCreate a newchat modein VS Code and replace default with pasted InstructionalistSelect custom mode from the dropdownPrompt Copilot to begin🦄 Try something likeHelp me create repo instructionsand give it time to scan your setup. Then answer as much as you can — Copilot will filter out what it doesn't need.🎤 This is a perfect time to try theSpeechplugin, but check the delay setting first so it doesn't send before you're ready.🎥 Check outLoading GitHub Copilot Chat Modes in VS Codeon YouTube.

## The Results 🐙

### Microsoft in VS Code 🪼

Microsoft’s instructions were very structure-first. You get a “Welcome to this repository” blurb at the top (which I left out in mine, becausewhy?) and sections likeProject StructureandKey Concepts. I was surprised that it even calls out the status badge system. It’s tidy and functional. It works.

🦄 It also adds a short “how to turn on custom instructions” note — which you shouldn’t need, unless you’ve gone in and toggled them off on purpose before.

### Coding Agent via GitHub 🧩

Coding Agent’s version swaps the order around a bit and renames a few headers (although, I don’t consider “structure” and “principles” to be interchangeable — so if you use this method, consider renaming that!) It skips the status badge part in the intro but circles back later with its ownStatus Systemsection. You also get content guidelines, writing style notes, and real markdown link refs for internal docs (which is best practice).

But it also tries to sneak in a whole Contribution Guidelines section... which, let’s be honest, belongs in aCONTRIBUTING.md, not in instructions for Copilot.

🦄 This is not the first time Coding Agent has tried to add every possible document GitHub makes available during a PR. Itseemsto be wired into the fact that if you have a public repo, then you need all of these things to exist. I'm going to dig into this more and report back.

### The Instructionalist Custom Chat Mode 📢

My version ignores all of the “Welcome” and “Structure” boilerplate and instead jumps straight into "Purpose" and "Value". It defines chat modes, prompts, and instructions in a way that makes Copilot’s role more engaging and interactive. Copilot makes it clear these aren’t just generic AI prompts — they’re curated for all stages of the dev process.

These don’t explicitly call out the status badge system, but it's referenced in context. And you get extras you won’t see in the other two: "Maturity Level" (so Copilot knows if the project is actively maintained or just camping in test mode), "Dependencies on Other Systems", and, yes, the occasional bit of lore. 😇 Plus explicit anti-patterns and testing/deployment plans.

🦄 I have to call out this is theonlyversion that requires the user to participate up front. So naturally it takes longer to spin up. If you're asking me? Completely worth the trade off.

## Final Answer? ⁉️

When you stack them side-by-side, you can see the philosophy differences right away:

* Microsoft: Orient Copilot by describing the map (structure, files, concepts).
* Coding Agent: Orient Copilot by describing the rules of the game (guidelines, principles, styles).
* My Instructionalist: Orient Copilot by describing the player’s role (purpose, value, patterns, anti-patterns).

The truth? If you completely ignore the fact that Iclearlythink mine is the best (because of course I do),the ideal file is actually a hybrid. A little structure from Microsoft, a little guideline clarity from Coding Agent, and a little persona and context from The Instructionalist.

Every generated file is long, so don’t be afraid to cut anything that's not adding obvious value. Save extras in a/future-reviewfolder. Keep essentials in the main file, and for the love of your PR sanity —update them every time something changes!

⚠️ Seriously, y'all! Old instructions arejust as dangerousas no instructions at all!

## What Else Have You Tried?

Have you tried writing instructions by hand or generating your own with Copilot yet? Whether you go Microsoft, Coding Agent, my Instructionalist, some weird hybrid of all three, or something different entirely — I want to know what worked (and what exploded).

Drop your results, screenshots, or horror stories in the comments. Bonus points if you rate yours higher than mine. 😛

## 🛡️ Built with AI

...but only after I gave it a proper tour, told it where the coffee machine was, and warned it about the zombie curse actively infecting LLC..

No Copilots were left unsupervised during the making of this post.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
