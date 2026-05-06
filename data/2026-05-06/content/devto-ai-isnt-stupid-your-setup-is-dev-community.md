---
title: AI Isn't Stupid. Your Setup Is. 🛠️ - DEV Community
url: https://dev.to/anchildress1/ai-isnt-stupid-your-setup-is-16cn
site_name: devto
content_file: devto-ai-isnt-stupid-your-setup-is-dev-community
fetched_at: '2026-05-06T20:20:51.620406'
original_url: https://dev.to/anchildress1/ai-isnt-stupid-your-setup-is-16cn
author: Ashley Childress
date: '2026-05-02'
description: The bare-minimum AI coding workflow—pick the right model, plan first, write AGENTS.md for agents not humans, and cross-check across LLMs before you blame the tool. Tagged with ai, agents, productivity, tutorial.
tags: '#ai, #agents, #productivity, #tutorial'
---

Tiered model selection and chat-first planning

The latest discourse I hear usually sounds something like, "I tried [insert agent flavor of the week] and it gave me garbage. AI is overrated."

My response: "No. You asked your mechanic to build a house and forgot to provide blueprints." 🦄

The agent isn't the problem—the setup is. Here's the workflow that actually works. None of it is clever and all of it took me longer to learn than I'd care to admit.

## 1. Pick the model that fits the task. Specs beat vibes. 🪛

Haiku is a sprinter. It'll absolutely take a swing at your distributed system architecture—the answer just won't be one you can ship. Your job is to match the model to the work.

If the problem is well-defined—clear specs, acceptance criteria, edge cases enumerated—Sonnet handles it fine. You'll spend more time in review, but you'll save real money. You'll also catch your own bad specs faster, which is its own gift.

If the feature is a tangled mess and you can't (or won't) break it down, that's also fine. Hand the whole thing to Opus instead. You don't have to scope every subproblem, but you DO have to define the whole solution. "Make it work" is not a valid requirement—it's a desperate wish the agent will not understand.

A cheap model with great specs beats an expensive model with vibes and feelings, every single time.

## 2. Plan in chat. Touch the codebase last. 🪞

I spend hours—many hours—talking through a problem before a single character lands in the codebase. AI is my rubber duck/research assistant with attitude—yes, I code that in because annoying accolades are distracting me from the goal: a solid game plan.

The language? Does not matter. I can read them all (I probably won't). Package manager? I care even less—drop a Makefile in the root and the commands stay the same regardless. Timeline? Sometimes, but the answer is usually "yesterday." What does matter:

* Meaningful tech stack
* Desired outcome
* Acceptance criteria
* Test scenarios—positive, negative, error, edge, weird, seen
* Explicit non-goals (the things you are NOT building, so they don't get sneakily built anyway)

Skip these and start prompting with "build me a thing"? You will indeed geta thing. It just won't beyour thing.

## 3. One source of truth. Stop copying instructions. 🪧

AGENTS.md,copilot-instructions,CLAUDE.md,GEMINI.md—pick one. I useAGENTS.mdas the source of truth, then drop one-line markdown links to it from the others. That gives you one file to manage instead of four.

If a rule is true everywhere—for you as the operator or across an entire project—it doesn't belong in a skill. Skills get called when triggered. Instructions get loaded always. Know which one you actually need and use accordingly. I wroteanother postdedicated solely to this concept, if you want a deeper dive.

The model should maintainAGENTS.mdas it works—you do not need a separateMEMORY.mdto muddy the waters. When it keeps violating the same rule, don't add another to the pile. Edit instead. Your agent knows exactly where it tripped if you ask, and it already knows how to fix it.

## 4. Write for the agent. Not the audience. 🪶

Left to its defaults, the model will write your instructions like a detailed onboarding doc. Section headers. Friendly intros. "This document outlines..." Polished prose for a human reader who is never supposed to show up.

Instructions load into context every turn. Every word costs tokens and burns clarity. So optimize for the actual audience: your agent.

Tell it explicitly:

* Edit for AI consumption only—no human-friendly framing, no narrative flow.
* Preserve every meaningful detail. Compress the prose, never drop the intent.
* Strip duplicates. If two rules say the same thing differently, merge them.
* Strip ambiguity. "Try to" and "consider" are noise—say what's required.
* Strip anything inferable from a reasonable code edit. If grep would answer it, cut it.

A polished onboarding doc is a tax on every prompt you ever send. Pay it once at write time, not every turn.

💡ProTip:These instructionsshould bea skill, because the agent only ever uses them when updatingAGENTS.md.

## 5. Skills aren't magical. Explicitly call them. 🪄

Skills are designed to be auto-invoked—yes. In theory... or if the description matches the prompt close enough and the planets align on a Tuesday. If youNEEDa skill used, then name it explicitly in the prompt. Otherwise you're gambling.

And please stop installing every skill from the marketplace just because the name sounded interesting. If you don't know the exact name of it already, delete it (with a backup). Use a skill builder to document the workflows you actually run. Leave the rest alone. You load trash in, you get trash out.

## 6. Install MCPs locally. Globals tax every prompt. 🪺

Having 20 MCPs globally enabled is convenient for you and a context-pollution nightmare for your agent. Every connected MCP eats tokens just by existing.

The question is simple: do I use this everywhere,all the time? If yes, then global is accurate. If not—and the honest answer is usually not—then install it only in the five projects where it actually matters. Symlinks and absolute paths can handle the duplication. Just make sure the agent has access to the directory.

## 7. Don't review. Test. Then test again. 🩻

I stopped reviewing AI-written code line by line. I was doing it badly, doing it slowly, and my eyes glazed over by the third file. The answer is to test it—extensively, often, and the moment it stops spinning. Not three days later when you open a PR.

Unit. Integration. E2E. Performance. A11y (accessibility). Sonar. Semgrep. Et cetera. Then automate and run with GitHub Actions. Make the model cover positive paths, negative paths, error paths, edge cases, and the acceptance criteria you defined back in the planning phase. (You did define them, right?) Add in anything you uncover during testing explicitly, so it doesn't happen again.

Then cross-check across models. Have Codex review Claude. Have Copilot review Codex. Each model has different blind spots and different obsessions—running them against each other in controlled doses IS the review. One LLM is a single point of failure. Three are a quorum.

## 8. Ban the shortcuts. Temporary is never temporary. 🪤

In myAGENTS.mdfiles for personal projects: backwards compatibility is strictly forbidden. Quick fixes are forbidden. Temporary solutions are not a viable path at any point. If the model wants to slap on a band-aid, it has to defend that choice. It can't, because my rule says it can't.

Now keep in mind, this is a personal-project rule and is harsh for live production code. If you're running production daily with real users, then you should probably nix the "no backwards compatibility" rule. But for your own stuff? Stop letting the model leave you with technical debt it threw around your codebase like confetti.

## 9. Clear the context. Don't iterate on broken. 🪦

If you've told the model the same thing three times and it's still wrong, then assume your conversation is poisoned. Too much wrong-direction is already baked in. Open a new chat. Start fresh with what you've learned.

A clean context with a sharper prompt beats six more rounds of "NO! I already said..."

## 10. The lesson. It was never the agent. 🧭

The agent is fine. The tooling is fine. What'snot fineis treating a multi-thousand-dollar reasoning system like a Magic 8-Ball—shaking it harder every time the answer comes back wrong, hoping round fifteen is the one. It won't be.

Pick the right model. Plan first. One source of truth. Test ruthlessly. Cross-check across models. Forbid the shortcuts. Clean up your skill folder and your MCPs. Clear the context when things go sideways and start over.

This setup? It works. Try it for yourself.

## 🛡️ Behind the Curtain 🎭

I wrote this post. Claude helped with the structure pass and the snark calibration so I'm not an accidental asshole. The opinions, the rules, and theAGENTS.mdphilosophy are mine—hardened over a year of letting AI drive and ruthlessly analyzing all the crashes.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (46 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse