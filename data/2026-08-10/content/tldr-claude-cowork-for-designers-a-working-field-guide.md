---
title: 'Claude Cowork for Designers: A Working Field Guide'
url: https://nervegna.substack.com/p/claude-cowork-for-designers-a-working
site_name: tldr
content_file: tldr-claude-cowork-for-designers-a-working-field-guide
fetched_at: '2026-08-10T15:30:34.704107'
original_url: https://nervegna.substack.com/p/claude-cowork-for-designers-a-working
author: Tommaso Nervegna
date: '2026-08-10'
description: Most designers already have three or four AI tabs open right now.
tags:
- tldr
---

# Claude Cowork for Designers: A Working Field Guide

Tommaso Nervegna
Jul 28, 2026
8
Share

Most designers already have three or four AI tabs open right now. One drafts copy, one makes images, one summarises a call. None of them remember your client, your brand rules, or the decision you made last Tuesday. You retype context every single time. That is not a workflow. That is a slot machine.

Claude Cowork is the first tool from Anthropic that treats knowledge work the way we designers actually experience it: as multi-step tasks with real files, real deliverables, and a chain of judgment calls in the middle. It is not a chatbot with a nicer skin. It is an agent that opens your folders, reads your source material, runs code, drives your browser, and hands back a finished deck, spreadsheet, or document while you do something more valuable.

I run an Agentic Experience Design practice inside a large studio. My through-line for a decade has been orchestration not decoration, and my read on where our craft is heading is simple: we moved from designing interfaces, to designing experiences, and we are now designing agents. Cowork is the clearest consumer-grade proof of that shift I have used. This is a hands-on guide to running it as a designer, with the actual prompts, file structures, and skills I use, plus an honest map of where it breaks.

## What Cowork actually is

Cowork is Claude Code’s agentic engine wrapped in an interface that does not require a terminal. Same brain, different hands. Anthropic launched it on January 12, 2026 as a macOS research preview for Max subscribers, then expanded it to Windows, then to web and mobile in a beta that began on July 7, 2026 starting with the Max plan. The build story tells you something about the tool: Boris Cherny, head of Claude Code, told Fortune the team built Cowork in approximately a week and a half, largely using Claude Code itself, and Cowork PM Felix Rieseberg posted on X, “@claudeai wrote Cowork.” The product is Claude Code pointed at its own audience problem.

Here is the mental model that matters. There are three surfaces, one model:

* Claude chatresponds turn by turn and produces text you then act on. It cannot touch your files directly.
* Claude Codelives in the terminal and the IDE. It plans, edits code across a repo, runs commands, and you review the diffs. It is built for shipping software.
* Coworklives in the same home as chat now, but instead of answering, it executes. You describe an outcome, it makes a plan, breaks the work into subtasks, runs those subtasks in an isolated environment, coordinates parallel workstreams, and delivers files you can preview and download.

The distinction I give my team: in chat, Claude tells you how to do the task. In Cowork, Claude does the task. That difference is the entire product.

Anthropic’s own usage data backs up why this matters for designers specifically. In its blog “How people are using Claude Cowork,” Anthropic classified 1.2 million sampled sessions from more than 600,000 organizations gathered between May 11 and 31, 2026. The largest category was business process and operations at 33.4 percent; content creation and copywriting was second at 16.4 percent, covering drafts, slide decks, posts, and proposals. Software development was only 8.7 percent, followed by DevOps at 7 percent, research at 6.4 percent, and data analysis at 5.8 percent. Anthropic calls the dominant use cases “the work around the work.” For a design team, that is exactly the tax that eats your billable hours: the decks, the audits, the synthesis, the handoff docs.

Sorted Pixels is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

## How it runs, and why you should care about the plumbing

Cowork now runs your sessions remotely by default in beta. The agent loop and code execution happen in an isolated, temporary sandbox on Anthropic’s servers. Each session gets its own sandbox, created when the session starts and destroyed when it ends. Sessions and files save to your Claude account, so you can start a task on your laptop, monitor it from your phone, and pick up the output later even with the laptop closed. Scheduled tasks run with no device online at all.

When a task needs something local, like a file on your Mac or your browser, Claude reaches it through the Claude Desktop app on that machine. So the desktop app stays the place for deep work with local files, browser use, computer use, and live artifacts. On the earlier desktop-only architecture, code execution ran inside a full local Linux virtual machine. Anthropic’s own architecture documentation states shell commands “execute inside a dedicated Linux VM, isolated from the host operating system by the platform’s hypervisor (Apple Virtualization.framework on macOS, Hyper-V on Windows).” This was independently corroborated: Simon Willison had Claude Code reverse-engineer the desktop app to expose the VM architecture, and security researcher Jimmy Vo documented a fully virtualized ARM64 Linux guest (Ubuntu 22.04 LTS) running on macOS Virtualization.framework. The point for you: your host operating system has a hard boundary between it and the agent, and Claude can only read and write in folders you explicitly grant.Coworker AI

Requirements are straightforward. You need a paid plan (Pro, Max, Team, or Enterprise). For local file access, browser use, and computer use you need the desktop app open and connected. You need an internet connection throughout the session.

## Setup and first run

1. Install or update the Claude desktop app for macOS or Windows from claude.com/download, or open claude.ai on web. Sign in on a paid plan.
2. Find the message box. Chat and Cowork share one home. Select “Cowork” instead of “Chat,” then describe your task. To go back to conversation, select “Chat.”
3. Set your permission mode. This is the single most important setting and most people ignore it.

Cowork has three modes:

* Manual(formerly “Ask before acting”): Claude pauses and asks approval for actions. You review each one.
* Auto: Claude keeps working and reviews each action for safety itself, blocking anything it judges unsafe, such as data exfiltration or prompt injection. It will not auto-approve sensitive actions like granting access to new folders, deleting files, or creating scheduled tasks. Auto mode consumes more of your usage limit because of the extra checking.
* Skip(formerly “Act without asking”): no pauses, nothing checks the actions. Only use this when you completely trust every file, connector, and app involved.

My rule for the studio: Manual for anything that sends a message as you, touches money, or writes to a client system. Auto for internal synthesis and drafting inside a scoped folder. Skip almost never.

1. Set global instructions. Go to Settings then Cowork, and add standing instructions that apply to every session. This is where you tell Claude who you are and how you write. Mine reads roughly:
I am an executive design director. Default to British English.
Write in short, direct sentences with no em dashes. When you produce
a deliverable, always tell me the exact file path and filename.
Never overwrite a file whose name contains REFERENCE or MASTER.
When you are unsure of a fact, ask rather than invent.

That last line matters. Anthropic and experienced skill authors both call it the escape valve. Without an explicit “ask if you do not know” instruction, the model will fill gaps with confident fiction.

1. Set folder instructions. When you point Cowork at a local folder on desktop, you can add project-specific context that lives with that folder.

## Exercise 1: your first real task, in ten minutes

Do not start with file organisation. Start with something that proves the difference between chat and an agent. Drop a folder of raw research on your desktop, then:

Look in the folder ~/Desktop/acme-usability. It contains 6 usability
session transcripts as .txt files and one screener spreadsheet.
Read all of them. Produce a single Markdown document called
FINDINGS.md in that folder that lists the top 8 usability issues,
ranked by how many participants hit each one, with a one-line verbatim
quote for each issue and the participant number it came from.
Do not paraphrase the quotes. If an issue only appeared once, put it
in a separate "watch list" section.

This is the tell. Chat would summarise what you paste. Cowork reads every file itself, counts across sessions, keeps the quotes verbatim, and writes the file to disk. Watch the progress indicators. When it finishes, open FINDINGS.md and check the quotes against a transcript. This verification habit is not optional, and I will return to why.

## Exercise 2: a competitive audit driven through the browser

Pair Cowork with Claude in Chrome. Chrome navigates and gathers, Cowork compiles. In practice this is one of the strongest designer workflows on the platform.

Using Chrome, visit these five competitor product pages: [paste URLs].
For each one, capture: the primary value proposition in their own words,
their pricing tiers, the three most prominent features above the fold,
and their primary call to action. Take a screenshot of each hero section
and save it to ~/Desktop/comp-audit/screens.
Then build a PowerPoint called comp-audit.pptx with one slide per
competitor using that captured content, plus a final summary slide
that maps all five on two axes: price versus breadth of features.

A note on trust here. Cowork respects your network egress permissions, but those permissions do not apply to web fetch, web search, or MCPs including Claude in Chrome. Web fetch runs server-side and is limited to search results and URLs you have shared. Treat anything the browser touches as a place where prompt injection can live, and keep this kind of task in Manual mode the first few times.

## Exercise 3: design research synthesis at volume

This is where the tool earns its keep. Interview synthesis is high-effort, repeatable, and exactly the work that quietly gets skipped when the timeline compresses. Anthropic’s own framing is that tedious tasks that might otherwise get skipped now get done, which leads to better decisions.

In ~/Research/onboarding-study there are 14 interview transcripts,
a discussion guide, and a spreadsheet of participant metadata (role,
tenure, plan type). Cluster the findings into themes. For each theme:
name it, give the count of participants who expressed it, split that
count by plan type using the metadata, pull two verbatim supporting
quotes with participant IDs, and note any disconfirming evidence.
Output an affinity-style Markdown report and a companion Excel file
with one row per coded quote so I can re-sort it myself.
Flag any theme where fewer than 3 participants support it as low confidence.

The Excel output is not a CSV that needs fixing. Cowork produces spreadsheets with working formulas and multiple tabs, and you can push them further with Claude for Excel. The “flag low confidence” and “note disconfirming evidence” lines are your guardrails against the model manufacturing a tidy narrative. Insist on them.

## Exercise 4: the advanced multi-step workflow, run on a schedule

Now assemble the pieces into something that runs itself. This is a Monday client-prep pipeline that touches connectors, files, and a schedule. Type/scheduleinside a Cowork task to set the cadence, or use “Scheduled” in the left sidebar.

Every Monday at 6am, prepare my client briefing for Acme.
1. Pull my Granola notes from any meeting tagged "Acme" in the last 7 days.
2. Search Gmail for unread threads from anyone @acme.com and summarise
 open questions and anything they are waiting on from us.
3. Check the ~/Clients/Acme/deliverables folder for files modified
 in the last week and list what changed.
4. Do a web search for any Acme news in the last week.
5. Build a one-page briefing doc in ~/Clients/Acme/prep dated this Monday,
 with sections: decisions needed, open questions, our commitments due,
 external news.
6. Draft, but do not send, a follow-up email to my main contact that
 chases the two most important open items. Leave it in drafts for me.

The draft-but-do-not-send instruction is deliberate. Consequential actions stay with you. The scheduled task runs remotely with no device online, so the briefing is waiting when you sit down with coffee. This is the shape of agent design: you are not writing prompts, you are designing a standing operating procedure that an agent executes and escalates from.

## Skills: turning your judgment into infrastructure

Prompts are instructions you give once. Skills are instructions that persist. A skill is a folder containing a SKILL.md file with YAML frontmatter (a name and a description) and Markdown instructions below it. Claude reads the description to decide when to load the skill automatically, or you invoke it with a slash command. Skills follow the open Agent Skills standard and work across both Cowork and Claude Code.

For designers this is the highest-leverage feature on the platform and the one almost nobody uses well. Skills are where you encode the reasoning you have never written down: how you frame a critique, what your brand voice is and is not, how you structure a handoff. The act of writing the skill is itself the value, because it forces you to make implicit judgment explicit.

There are several ways to author one. You can write the SKILL.md by hand. You can describe what you want and let Claude build it. In Cowork on Claude for Mac you can even record a skill: you perform a task on screen while narrating, and Claude proposes a skill from what it observed (available on Pro, Max, and Team plans, not on Windows, Free, or Enterprise). The video and audio are not retained; only screenshots from the session are kept inside the task.

### A complete worked example: a design handoff skill

Here is a skill I actually run. Create a folder namedhandoff-spec, and inside it a file namedSKILL.md:

---
name: Handoff Spec Generator
description: Generate an engineering handoff spec for a UI component or
 screen. Use whenever I ask for a handoff, a dev spec, or component
 documentation. Enforces complete interaction states and accessibility.
---

## Overview
Produce a developer-ready handoff spec. The spec must be complete enough
that an engineer never has to ask about a state I forgot to define.

## Required sections, in this order
1. Component name and purpose (one sentence).
2. Anatomy: list every element and its design token (colour, type, spacing).
 Use token names, never raw hex, if a tokens file is present in the folder.
3. States: define default, hover, focus, active, disabled, loading, error,
 and empty. If a state does not apply, write "not applicable" and say why.
 Never silently omit a state.
4. Behaviour: interaction on click, keyboard, and touch. Include focus order.
5. Accessibility: WCAG 2.2 AA. Specify text and non-text contrast ratios,
 focus indicator, ARIA role and label, and keyboard operation.
6. Responsive behaviour at mobile, tablet, and desktop breakpoints.
7. Open questions for engineering.

## Rules
- If contrast cannot be verified from the tokens provided, list it under
 open questions rather than asserting it passes.
- Output as Markdown. Name the file [component]-handoff.md.

## Example
Input: "handoff for the primary button"
Output: a Markdown file with all seven sections, states fully enumerated,
contrast ratios stated as ratios (for example 4.6:1), and an open-questions
section listing anything the tokens did not specify.

Zip the folder so the skill folder is the root, upload it in Customize then Skills, and enable it. Now when anyone on the team says “generate a handoff for the filter chip,” Claude produces the full spec in your house format without being re-briefed. Note the two escape valves: states that do not apply must be justified, and unverifiable contrast goes to open questions instead of a false pass. Those two lines are the difference between a spec you trust and one you fact-check line by line.

The best skills are focused, specific in their description, and include at least one example. Overengineering is the common failure: if the instruction is longer than the output, simplify. Anthropic maintains example skills on GitHub you can use as templates, and a/skill-creatorcommand can interview you and draft one.

Other design skills worth building, drawn from real practice: a brand and voice guide that states what the brand is, is not, and why (not a dump of the PDF); a critique-prep skill that reframes the same design decision for a peer, a PM, and a VP; a research-plan template skill; and an accessibility audit skill. On the accessibility point, community authors have built genuinely rigorous WCAG 2.2 skills that do programmatic contrast checking, which catches non-text contrast failures that visual inspection misses. Treat the output as a first pass that surfaces issues, not a compliance sign-off.The AI Career Lab

## Connectors and MCP: giving the agent reach

Skills tell Claude how to work. Connectors give Claude access to where the work lives. Under the hood connectors are MCP (Model Context Protocol) servers, the open standard Anthropic created. Each authenticates through OAuth or an API key and inherits your permissions: if you cannot see a file, the connector cannot reach it either.

You add connectors from the plus menu in the chat box, or from Customize then Connectors. The permission mode you set earlier governs how often each connector asks before acting. For designers, the connectors that change the job are:

* Google Drive: where the real context usually lives. Claude searches, summarises, compares, and reads docs and decks directly, no copy-paste.
* Gmail: turns your inbox into context. Client requests, attachments, deadlines, and the thing someone is waiting on all become readable.
* Granola: this is the sleeper for research and design ops. Granola captures meeting transcripts as a quiet desktop widget, no bot joining the call, and its MCP connector lets Claude reason directly over your meeting history. Ask it to find every session where you discussed a given flow and synthesise the decisions.Claude
* Notion or Confluence: your team knowledge base becomes queryable. Notion’s permission model is the cleanest, letting you scope Claude to a single page or database, which makes it a safe first connector.

Set connectors up read-only first. Learn what each one actually does before you grant write access. The most common mistake is being too permissive on day one.

### Figma MCP, treated honestly

This is the connector designers ask about first, and it needs a precise answer because the internet is full of imprecise ones.

The official Figma MCP server gives an agentic client structured access to your design data. It can read design context including components, variables and design tokens, layout data, FigJam content, and Make resources, generate code from selected frames, and use Code Connect to stay aligned with your real components. It can also write to the canvas: with the right skills it creates and updates native Figma content across Figma Design, FigJam, and Figma Slides, and its code-to-canvas capability sends live web interfaces into Figma as editable layers rather than flat screenshots. Write access is remote-server-only and, per Figma, currently restricted to Full and Dev seats on paid plans.

Figma ships two versions: a remote server hosted at Figma’s endpoint (mcp.figma.com) that needs no desktop app and carries the broadest feature set, and a desktop server that runs locally through the Figma desktop app for specific organisation and enterprise cases. During the beta the server is free, and Figma states it “will eventually be a usage-based paid feature, but is currently available for free during the beta period.” The remote server is available on all seats and plans, but write-to-canvas requires a Full or Dev seat.

Now the part the hype skips. As of late July 2026, Figma’s official supported-client list for its remote MCP server names Claude Code, Cursor, VS Code, Windsurf, and Codex, among others. It does not name Claude Cowork. The deep, official Figma-to-agent workflow, including write-to-canvas, is documented and supported through Claude Code, where the recommended setup installs Anthropic’s official Figma plugin that bundles the MCP settings plus Agent Skills. The Cowork-to-Figma connections you will see written up rely on third-party bridges such as Composio, not Figma’s own server. So my honest guidance: if you want the real design-to-code and code-to-canvas round trip, that lives in Claude Code today. If you are working in Cowork, treat Figma access as read-oriented and third-party until Figma lists Cowork as a supported client. This is the clearest current example of why a designer comfortable with both tools should keep both installed.

## Cowork versus Claude Code for designers

The tired version of this comparison is “Code is for developers, Cowork is for everyone else.” That was never quite right and it is less right now. You can build a website in Cowork and you can write a client proposal in Code. The model is identical.

The real decision rule I use:

* Reach forCoworkwhen the deliverable is a document, deck, spreadsheet, or a synthesis across files, when you want to steer from your phone, when the task should run on a schedule, or when you want the safety of the auto-mode action review. This is the overwhelming majority of a design leader’s non-visual work.
* Reach forClaude Codewhen the work is genuinely technical: a live prototype you intend to ship, a design-token pipeline, or the full Figma MCP round trip with write-to-canvas. Code gives you diffs, git, and the officially supported Figma integration.

If you are comfortable with both, the pattern is: synthesise and produce in Cowork, build and integrate in Code, and let skills travel between them because they follow the same open standard.

A related tool to keep straight: Claude Design, launched April 17, 2026 by Anthropic Labs, is a separate prompt-to-canvas product for prototypes, decks, and mockups. Per Anthropic’s announcement, it “is powered by our most capable vision model, Claude Opus 4.7, and is available in research preview for Claude Pro, Max, Team, and Enterprise subscribers.” It is not Cowork and it is not Code. It is where early visual ideation and buy-in happen before anyone commits to building. The three compose: ideate in Design, produce and synthesise in Cowork, ship in Code.Claude

## Where it breaks, honestly

I have shipped real work through this tool. I have also watched it fail. Here is the map.

* It overwrites files.Cowork has no version control. It will happily overwrite a file you cared about if you did not tell it not to. This is the single most reported gotcha. Protect reference material by naming convention and a global instruction, and keep masters out of the working folder entirely. Back up before granting folder access.
* It still hallucinates.It is the same model underneath. If you do not say what you mean, it invents. The verbatim-quote and low-confidence flags in my prompts above exist precisely because the default behaviour is to produce a clean story whether or not the data supports it.
* Memory is thin.What Claude remembers about you in chat does not carry into Cowork yet. Inside Cowork, memory works only within projects. Do not assume continuity across sessions unless you built it with a project.
* Auto mode costs more, and everything costs more than chat.Multi-step agentic work is compute-intensive. You will hit usage limits faster. Batch related work into single sessions and use plain chat for simple things. Anthropic ran a promotion doubling the Cowork 5-hour usage limit (weekly limits unchanged), first from June 5 to July 5, 2026, then extended through August 5, 2026 at 11:59 PM PT for Pro, Max, Team, and legacy seat-based Enterprise, which softens this temporarily.
* Governance is immature for teams.Cowork activity is not captured in the Compliance API at this time, and it is not yet in audit logs, though Team and Enterprise admins can monitor activity with OpenTelemetry. If you lead a regulated studio, know this before you roll it out.
* The browser is an attack surface.Egress permissions do not cover web fetch, search, or MCPs. A malicious page can attempt prompt injection. Anthropic documented a real disclosure from security firm PromptArmor, building on a Files API flaw reported by researcher Johann Rehberger, in which an allowlisted domain (api.anthropic.com) was abused to exfiltrate workspace files; in Anthropic’s words, “the sandbox worked perfectly, and yet the data was exfiltrated.” It was fixed with a defensive proxy inside the VM, but the lesson stands: stay in Manual mode for anything sensitive and review planned actions.
* Some things are desktop-only.Live artifacts and plugins that include local MCP servers work only through the desktop app. Web and mobile are still catching up.

None of this is disqualifying. All of it is the price of an agent that takes real actions. Design leaders who treat Cowork like a product they are responsible for, with guardrails and review gates, get enormous leverage. Those who treat it like magic get burned.

## What this does to the design function

For most of my career the implicit logic behind our decisions lived in our heads and died there. We could not search our own judgment, hand it to a junior, or retrieve it six months later. Skills change that equation. When you write down how you run a critique or structure a handoff, you are not just automating a task, you are externalising the expertise that made you effective. That is the most important thing Cowork does, and it has nothing to do with pixels.

The career arc of our field has run from interfaces to experiences to agents. Cowork sits squarely at the third stage. The unit of design work is shifting from the artifact to the orchestration: the standing procedures, the skills, the connected sources, and the review gates that let an agent carry a task from intent to deliverable while you hold the judgment. That is orchestration not decoration, made literal.

The teams that win the next two years will not be the ones that generate the prettiest mockups fastest. They will be the ones whose leaders wrote their judgment down clearly enough that an agent could act on it, and who kept themselves in the loop exactly where consequences live. Start this week. Pick the one recurring task you resent most, build a skill for it, point Cowork at one real folder, and run it. The tool is ready. The question is whether your thinking is explicit enough to hand over.

## Recommendations

Week 1, prove it works.Install the desktop app, set global instructions with the escape-valve line, and run Exercise 1 on one real folder in Manual mode. Verify the output against a source file before you trust anything. Benchmark: if it saved you time and the quotes checked out, continue.

Week 2, add reach.Connect Google Drive and Granola read-only. Run Exercise 3 (research synthesis) on a real study. If a connector ever writes somewhere unexpected, drop back to Manual mode and tighten scope.

Week 3, encode judgment.Build one skill for the recurring task you resent most, using the handoff-spec pattern above with at least one worked example and an explicit escape valve. Benchmark: the skill is working when a colleague can trigger it and get your house-standard output without briefing you.

Week 4, automate.Stand up one scheduled pipeline like Exercise 4 with a draft-but-do-not-send gate on any external action.

When to change course:if you are doing production prototyping, design-token pipelines, or want the write-to-canvas Figma round trip, move that work to Claude Code, not Cowork. If you lead a regulated or audited studio, hold enterprise rollout until Cowork activity lands in the Compliance API and audit logs; monitor with OpenTelemetry in the meantime. Reserve Skip mode for tasks with zero external consequences, and never use it against client systems.

8
Share