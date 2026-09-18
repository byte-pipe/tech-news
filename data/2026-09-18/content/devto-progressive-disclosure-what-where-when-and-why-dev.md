---
title: 'Progressive Disclosure: What, Where, When, and Why - DEV Community'
url: https://dev.to/reporails/progressive-disclosure-what-where-when-and-why-36m3
site_name: devto
content_file: devto-progressive-disclosure-what-where-when-and-why-dev
fetched_at: '2026-09-18T14:48:07.225345'
original_url: https://dev.to/reporails/progressive-disclosure-what-where-when-and-why-36m3
author: Gábor Mészáros
date: '2026-09-16'
description: Do you remember when we first started using AGENTS.md files? You would have a project root file... Tagged with ai, claude, performance, productivity.
tags: '#ai, #claude, #performance, #productivity'
---

Traces AGENTS.md history to modern harness paths

Do you remember when we first started using AGENTS.md files?

You would have a project root file describing the project, and some nested ones describing the content in the folder where they reside. This opened up exciting possibilities for everyday users: For the first time you could put a rule where the work was and trust it to show up only there. I ran an entire project this way once, one small instruction file sitting in each layer of the codebase.

You only had to keep the mental model locked, and you could manage your instructions so they loaded only when the agent was working in the folders they belonged to.

This was one of the earliest forms of progressive disclosure, and coding agents still support it to this day. It comes with a price, though. Relevant instructions only load if the agent is working in your folder. So you hit the classic context rot problem right away, because you might be working on the backend while some frontend pieces need adjusting along with it. Having the coding agent work front and backend at once always causes mayhem: the instructions compete for attention, and the system has to split its attention between the two big areas.

Cursor and Claude were quick to offer a finer-grained solution here. Instead of scattering some number of AGENTS/CLAUDE.md files through the subfolders, you use a harness artifact that carries the path configuration for where to load. Not just folder level, but file level. Dandy. Problem solved? Not even close.

## The problem

So what is the problem itself? To see why even file-level scoping is not the finish line, go back to the crudest option for a second. Wouldn't it be easier to just load everything into the context at one go and leave the LLM to figure out the rest?

That is what most of us tried first, and it is the reason your CLAUDE.md is three hundred lines long, the kind of file people now argue you should just delete (Opus 5: Delete your CLAUDE.md?). Every rule you ever wrote, in the window every turn, always in reach. It feels like the careful choice, but it is the expensive one, and tokens are the smallest part of the bill.

A model does not work through your instructions the way you work through a checklist, line by line, giving each one its moment. It spreads a fixed amount of attention across everything in front of it, and every line you add is one more thing pulling on that same budget. Ten rules and each gets a real share. A hundred, and the one rule that matters for this turn is a single voice in a crowded room, shouting over ninety-nine others that have nothing to do with the task at hand. It is the front-and-backend problem again, the one from a moment ago, except now you have signed the agent up for it permanently: every turn, every rule, all at once.

This is not just a hunch about attention. When we went through 28,721 real repositories, the median instruction file carried about fifty items and only a dozen of them were actual directives. The rest was scaffolding the model still reads past on every turn: most of your always-on file is not even telling the agent to do anything, and all of it competes for the same budget. We wrote that up asThe State of AI Instruction Quality.

So "load everything" does not dodge the problem. It is the problem, turned all the way up.

That is what the path configuration was for. Loading the payments rule only when the agent is actually in the payments code is the honest fix: keep each rule out of the crowd until the turn it belongs to. Real progress, and still only part of the answer, because where a rule lives is one lever and there are others.

A rule can be the wrong thing to load, not only loaded in the wrong place. It can be something you want at a moment rather than in a folder. What you actually want is a way to decide, for every rule you have, what loads, where, and when. That already has a name.

## The solution: Progressive Disclosure

What is progressive disclosure? It is the procedure for how you gradually introduce the relevant instructions and context to the coding agent. Instead of one always-on file, you hand the agent each rule at the moment it is about to matter, and keep it out of the way the rest of the time. That is the whole idea. What makes it something you can build with is that it comes apart into three handles, and once you can see them separately you stop reaching for the root file by reflex.

This is also the fix Anthropic now writes down in as many words. In its guidance for the Claude 5 generation, Anthropic's Thariq Shihipar names the habit that grew your file, the "myth ... that you want to make these a central repository for every known practice," and the cure, to "use progressive disclosure heavily" and let the rest load from skills the file points at (the new rules of context engineering).

### What loads

A rule does not have to be a line in a file the agent reads top to bottom. Package it as a skill: a self-contained instruction the agent pulls in when the task calls for it and never sees otherwise. Your commit conventions have no business in the window while the agent is chasing a layout bug, and a skill keeps them out of it until you reach forgit.

### Where it loads

You have already met this one. A rule that only governs the payments code lives next to the payments code: folder level with a nested file, or file level with the path configuration Cursor and Claude added. It shows up on the turns the agent works there and is not in the room the rest of the time. The rule did not get weaker; it got aimed.

### When it loads

Some rules only matter at a moment, not in a place. Tie them to the moment: pull a rule in when a session starts, or when a certain kind of work begins, and keep it dark until then. Same rule, later entrance. You are not rewriting it; you are deciding when it walks on.

### Why

None of the three changes what a rule says. They change when the agent has to carry it. And what you are short on is not disk space or even tokens; it is the agent's attention on the turn that counts. What, where, and when are three ways to spend that attention on the rule that matters instead of the ninety-nine that do not. Get them right and the three-hundred-line always-on file comes apart into a lean root plus a set of rules that show up on cue: the crowded room empties, and the rule for this turn is one of three in the window instead of one of a hundred. That is the loading problem solved, or as solved as loading gets, the right rule in front of the agent, uncrowded, exactly on the turn it applies.

## The file was never the unit

Something changed while you were splitting that file, and it is bigger than the file. You did not tidy a document. You built a system: a lean root, and a set of rules that each load on cue, some pinned to a path, some to a moment. And a system has a shape you can no longer take in by scrolling one file. Is this rule still loading where you think it is? Did you scope that one so tightly it now reaches nobody? Are two of them set to load on the same turn, back to competing for attention, the crowded room rebuilt in miniature? Or worse, are two of them quietly telling the agent opposite things, the kind of contradiction we put a price on inOpus 5: Cost of Instruction Conflicts?

"Is it in the file" was the right question when there was one file. There is no one file now. The question is what actually loads, where, and when, and whether that still matches what you meant. None of it lives in your root file anymore, because you moved it out yourself.

That is the ground the rest of this series stands on. Each piece takes one handle and goes deep, with the code to run it: what loads, and how you would know it did; where to scope a rule so it stops diluting every unrelated turn; when to move a rule off the page and onto an event. (And a rule can load perfectly and the agent can still ignore it. That is a different problem with a different fix, and it earns its own piece.)

When you want to see the shape of what you have built, which rules still load and where two of them now collide, that is the readReporailsgives you: free, on your own machine, on the files you wrote. It reads what you author; it never touches your agent while it runs.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse