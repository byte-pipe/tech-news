---
title: 'Ran out of Cursor tokens and switched to GitHub Copilot: Side-by-Side - DEV Community'
url: https://dev.to/maximsaplin/ran-out-of-cursor-tokens-and-switched-to-github-copilot-side-by-side-2n5p
site_name: devto
content_file: devto-ran-out-of-cursor-tokens-and-switched-to-github-co
fetched_at: '2026-02-19T11:19:46.311301'
original_url: https://dev.to/maximsaplin/ran-out-of-cursor-tokens-and-switched-to-github-copilot-side-by-side-2n5p
author: Maxim Saplin
date: '2026-02-18'
description: DISCLAIMER! The best AI coding tool is the one available to you, that gives you the best model and... Tagged with ai, githubcopilot, programming, productivity.
tags: '#ai, #githubcopilot, #programming, #productivity'
---

DISCLAIMER! The best AI coding tool is the one available to you, that gives you the best model and reasonable token limits. From the text below it might look like GitHub Copilot is a horrible product - it's not. I use Copilot and I'm productive. It's just an irritating experience when I switch from Cursor.

The banner is a screenshot from my Cursor 2025 retrospective with almost 1T tokens used - I guess one might call me a heavy user. I've been usingitsince 2023 and it happens to be my favourite VSCode fork. I tried different AI assisted IDEs: Kiro, Antigravity, Windsurf, Project IDX; used VSCode extensions such as Continue, Cody.

When my monthly token limit in Cursor ran out last December, I've been spending more time with GH Copilot (the Insider Preview version with the newest features). Before that I occasionally used Copilot and mostly followed its progress from media/posts and my colleagues' discussions. It's hard to miss the major AI Coding assistant which Copilot is. Since 2023 I have formed an opinion that GH Copilot is an inferior product compared to Cursor which lagged by ~6 months. Recently the gap in new feature releases in Copilot has narrowed yet the execution is not great.

## What I don't like about Copilot

* Plan Modeis a gray piece of misery compared to Cursor's implementation. I use it a lot in Cursor but see no reason to use it in Copilot. When I tried it for the first time in GH I didn't even understand that the plan was provided - it was just a few paragraphs of text produced by a subagent and clicking the 'Proceed' button just switched the mode to 'Agent' and pasted 'Proceed' text into chat. All of that seemed like a waste of tokens on subagent that did many tool calls and provided a very generic response. In Cursor you get a detailed and structured.MDplan; there's a 'Build' button allowing you to spawn a new agent in a new dialog (with a different model of choice and a clean context); or you can proceed implementing it in the same thread.

* Dialog features are poor(and it's the core of UX). For example, you can't clone dialogs or branch out from certain messages in the middle - something I used a lot in Cursor to manage the ever growing threads and context overflows. There are a few more conveniences around overall UX that are missing in GH and keep the experience irritating (e.g., jumpy prompt input, adding a selected piece of a file to the dialog was not instantly apparent due to a faint animation, etc.)

* There's no manual dialog summarisation, only automatic. Here's how I got trapped by this "feature"... In the middle of a chat (and I had no idea how big the chat was, since there was no token counter; otherwise I'd have branched it into a new thread) I typed "Proceed". After the implementation started and I saw a few tool calls summarisation kicked in and the agent got lost and "What do you want me to proceed with?".

* Token counter missing for too long. Insider preview has added this feature at the end of January.Theissuerequesting the feature in Copilot has been sitting since April 2025 and collected many reactions. Cursor had the context window usage indicator since I can't remember when.
* Theissuerequesting the feature in Copilot has been sitting since April 2025 and collected many reactions. Cursor had the context window usage indicator since I can't remember when.
* Shorter context windows. For example, GPT-5 family has 272K input limit and Anthropic's Claude models by default allow for 200K total context size. I had this perception that in Copilot my dialogs hit the summarisation threshold sooner than in Cursor - turns out there's a reason for that. Why have these low defaults?

* Gemini 3 Pro instability. My favourite model of November randomly threw errors in longer dialogs - trying Again didn't help; I had to drop those dialogs or switch models. Never noticed this instability in Cursor.
* GitHub instructionslook inferior to Cursor's rules. For example, there are no semantic rules - where an agent pulls relevant instructions automatically. I even had to do a smallworkaround for that handy feature. Recently Insider Preview added support of Agent Skills which does exactly that, yet
* Piling-up legacy in prompts management. There are instructions, chat modes, different approaches to prompts - recently when doing a cleanup in our teams repo where GH Copilot was used there were a lot of questions around "how do I do my guardrails properly". A good example in my opinion is how Cursor dropped its Rules discipline making Agent Skills the default choice and instantly provided amigration pathfor existing Cursor rules/commands.This also gives another example of a half-baked feature in Copilot. Agent Skills in Copilot are automatic only - the model decides when the skill is pulled into the thread. And for some reason there's no way to explicitly reference the skill. We used/specand/taskslash commands for Spec-Driven development, and those are called explicitly. When introducing Agent Skill Cursor added both option to use those - automatic or via slash commands.
* This also gives another example of a half-baked feature in Copilot. Agent Skills in Copilot are automatic only - the model decides when the skill is pulled into the thread. And for some reason there's no way to explicitly reference the skill. We used/specand/taskslash commands for Spec-Driven development, and those are called explicitly. When introducing Agent Skill Cursor added both option to use those - automatic or via slash commands.
* Missing Multi-model parallel agents- Cursor allows you to pick several models to process a single prompt; each one creates a Git worktree and you can proceed working in the worktree you liked the most. Copilot has a Background agent feature allowing you to spin up a new GH Copilot CLI agent - while it also relies on a worktree it doesn't give the same convenience.

* Getting newer models can be slow. GH announcements of model availability in Copilot come the same day the model is introduced. Yet it's often opt-in when Copilot subscription admins enable new models manually. In the case of Cursor I learn aboutnew model releases from its model picker
* No choice of reasoning effort for models. For example, for GPT-5.2 there's only a single line in the picker, while in Cursor there are 8 options ( low, medium, high, xhigh, and then the same four with the -fast suffix, which is twice as expensive but faster). Technically, one can switch reasoning effort to "High" for OpenAI models, though only under experimental setting "Chat: Responses Api Reasoning Effort", which is a bit awkward and hard-to-reach feature.

* Restoring checkpoints can be unreliable. I ended up with a broken solution a few times when going back in chat history. Frankly, it is not always reliable in Cursor either; sometimes agents tend to make changes bypassing standard edit tools. It just seems GH checkpoint restoring was less reliable.
* System prompts seem awkward and less effective. For instance, in Copilot I often get the agent responding with a "Plan" section after it completes a long thread. Essentially it fills the top of its report with a scroll of what the plan was. Who cares when job is done? Very confusing after switching from Cursor. Besides, when using Copilot in CLI it often gets the intent wrong and doesn't produce the right command, requiring further interaction.

* The recent Cursor release of subagents is yet to be matched by Copilot. The UX is better; the whole orchestration seems more polished. See below how in Cursor I kicked off parallel agents in their own worktrees which in turn kicked off subagents - all in one click. Compare to the very simplistic GH variant:

* Models in Copilotcan't view image files- you can only paste an image into chat; this way they do see images, otherwise they are blind. Use case? Using ADB to take screenshots and saving them in PNG for further inspection - it took me hours running failing verification loops before I realized Copilot lacked that trivial ability. Cursor does this well.

## What I Like about Copilot

* (Long awaited) Token counter gives a breakdown. It's curious to observe howagentic coding has recently leaped forwarddue to verification - you can easily check how much tool call results occupy in the dialog.

* You can inspect prompts- under "Output > GitHub Copilot Cha"t you can view very detailed LLM traces. For example, you can see what sort of prompts are used to wrap your interactions, might be useful, especially if you like tinkering.

* Open about standard tools- there's no UI in Cursor to control standard tool selection, only MCP ones. If you are up for tinkering you can configure tool bundles, can see their exact names. For example, I often explicitly ask GH to use therunSubagenttool to delegate to subagents - works like a charm for bigger tasks.

* Kinda open-source- while the back-end part has not been open-sourced, the extension has been. Besides, many AI coding assistant features have been merged intovscodedirectly, making the creation of third-party extensions much easier. Though it's a pity that GH Copilot always requires a sign-in locking out of true local LLM use - the ticket for that is very popular and has been sitting for almost a year.
* Easier installation of MCP- I found the integration in GH easier (button click); with Cursor I had to update config files.
* Ecosystem and integration with GitHub- you have Copilot integrated in GH web app; you can easily assign issues to Cloud agents via you phone while browsing GitHub; the extension is accessible in plenty of IDEs (though people say non-VSCode IDEs struggle with feature parity). They have recently added support forClaude Code and Codexallowing you to run other major coding agents through a GH subscription. The breadth and outreach of Copilot is great.

* More tokens- it feels like GH's premium requests model allows for more usage compared to Cursor's token-based pricing. Unfortunately there's no user-facing dashboard in Copilot to draw a clear comparison.

## From the Creators of SharePoint...

Pun intended. Corporate touch adds a certain flavour making software disgusting. SharePoint or Dynamics CRM are in my view classical examples - ugly UI, slow. The ".aspx" extensions in URLs remind of decades-old ASP.NET Web Forms used to build them.

Somehow GitHub Copilot follows in the steps of other corporate products... It often feels like software that is created by people who (a) don't use it and (b) don't care. A product built by aslideware company.

Just recently this "don't care" approachhas surfacedwhen a user discovered an exploit to bypass billing. That was hilarious! A vulnerability report was submitted privately to Microsoft Security Response Center; the folks there told that billing wasn't their responsibility and advised to create a ticket on a public GitHub repo - where everyone could see the exploit and free-ride Microsoft on tokens. And even after that the GH issue got closed automatically by some AI bot. A few days later it was re-opened after the exploit received public attention and media coverage.

Copilot vs Others might be a yet another Harvard Business School case study on how a large established company turns slow and loses touch with the market, while more nimble and energetic startups build better products.

## Cursor's Apple Magic

"It just works" often comes to my mind when I use Cursor. There aren't that many options and toggles. They like building minimalist and refined UI (one of the reasons I don't like GitHub - because it's often ugly to my eye). A small example, Copilot in CLI:

Vs. Cursor:

There's a bit of closedness and secrecy at AnySphere. Take for example theirComposer releasewhere they compare their model to an unnamed best-on-the-market model and vaguely describe what they did - not even mentioning what the context window size for the new model is. Or how they implemented the "use your own API key" feature when they process all LLM requests on their back-end making use within a closed perimeter impossible.

Apple vs. Microsoft, iOS vs. Android, startup vs. enterprise - all those analogies sum up my impressions when comparing Cursor to Copilot.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
