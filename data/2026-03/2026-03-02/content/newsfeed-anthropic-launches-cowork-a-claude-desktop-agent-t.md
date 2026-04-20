---
title: Anthropic launches Cowork, a Claude Desktop agent that works in your files — no coding required | VentureBeat
url: https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no
site_name: newsfeed
content_file: newsfeed-anthropic-launches-cowork-a-claude-desktop-agent-t
fetched_at: '2026-03-02T08:25:37.757764'
original_url: https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no
date: '2026-01-12'
published_date: 2026-01-12T03:30-08:00
description: Anthropic’s Cowork brings Claude Code–style AI agents to the desktop, letting Claude access and manage local files and browse the web—boosting productivity while raising new security and trust risks.
tags:
- venturebeat-ai
- technology
- ai
- automation
---

All Posts
Featured
Michael Nuñez

 January 12, 2026


Credit: VentureBeat made with Midjourney

AnthropicreleasedCoworkon Monday, a new AI agent capability that extends the power of its wildly successfulClaude Codetool to non-technical users — and according to company insiders, the team built the entire feature in approximately a week and a half, largely using Claude Code itself.

The launch marks a major inflection point in the race to deliver practical AI agents to mainstream users, positioning Anthropic to compete not just withOpenAIandGooglein conversational AI, but withMicrosoft's Copilotin the burgeoning market for AI-powered productivity tools.

"Cowork lets you complete non-technical tasks much like how developers use Claude Code," thecompany announcedvia its official Claude account on X. The feature arrives as a research preview available exclusively toClaude Max subscribers— Anthropic's power-user tier priced between $100 and $200 per month — through the macOS desktop application.

For the past year, the industry narrative has focused on large language models that can write poetry or debug code. WithCowork, Anthropic is betting that the real enterprise value lies in an AI that can open a folder, read a messy pile of receipts, and generate a structured expense report without human hand-holding.

## How developers using a coding tool for vacation research inspired Anthropic's latest product

The genesis ofCoworklies in Anthropic's recent success with the developer community. In late 2024, the company releasedClaude Code, a terminal-based tool that allowed software engineers to automate rote programming tasks. The tool was a hit, but Anthropic noticed a peculiar trend: users were forcing the coding tool to perform non-coding labor.

According toBoris Cherny, an engineer at Anthropic, the company observed users deploying the developer tool for an unexpectedly diverse array of tasks.

"Since we launched Claude Code, we saw people using it for all sorts of non-coding work: doing vacation research, building slide decks, cleaning up your email, cancelling subscriptions, recovering wedding photos from a hard drive, monitoring plant growth, controlling your oven," Cherny wrote on X. "These use cases are diverse and surprising — the reason is that the underlying Claude Agent is the best agent, and Opus 4.5 is the best model."

Recognizing this shadow usage, Anthropic effectively stripped the command-line complexity from their developer tool to create a consumer-friendly interface. In its blog post announcing the feature,Anthropic explainedthat developers "quickly began using it for almost everything else," which "prompted us to build Cowork: a simpler way for anyone — not just developers — to work with Claude in the very same way."

## Inside the folder-based architecture that lets Claude read, edit, and create files on your computer

Unlike a standard chat interface where a user pastes text for analysis,Coworkrequires a different level of trust and access. Users designate a specific folder on their local machine that Claude can access. Within that sandbox, the AI agent can read existing files, modify them, or create entirely new ones.

Anthropic offers several illustrative examples: reorganizing a cluttered downloads folder by sorting and intelligently renaming each file, generating a spreadsheet of expenses from a collection of receipt screenshots, or drafting a report from scattered notes across multiple documents.

"In Cowork, you give Claude access to a folder on your computer. Claude can then read, edit, or create files in that folder,"the company explainedon X. "Try it to create a spreadsheet from a pile of screenshots, or produce a first draft from scattered notes."

The architecture relies on what is known as an "agentic loop." When a user assigns a task, the AI does not merely generate a text response. Instead, it formulates a plan, executes steps in parallel, checks its own work, and asks for clarification if it hits a roadblock. Users can queue multiple tasks and let Claude process them simultaneously — a workflow Anthropic describes as feeling "much less like a back-and-forth and much more like leaving messages for a coworker."

The system is built on Anthropic'sClaude Agent SDK, meaning it shares the same underlying architecture as Claude Code. Anthropic notes that Cowork "can take on many of the same tasks that Claude Code can handle, but in a more approachable form for non-coding tasks."

## The recursive loop where AI builds AI: Claude Code reportedly wrote much of Claude Cowork

Perhaps the most remarkable detail surrounding Cowork's launch is the speed at which the tool was reportedly built — highlighting a recursive feedback loop where AI tools are being used to build better AI tools.

During a livestream hosted by Dan Shipper, Felix Rieseberg, an Anthropic employee, confirmed thatthe teambuilt Cowork in approximately a week and a half.

Alex Volkov, who covers AI developments, expressed surprise at the timeline: "Holy shit Anthropic built 'Cowork' in the last... week and a half?!"

This prompted immediate speculation about how much of Cowork was itself built by Claude Code.Simon Smith, EVP of Generative AI at Klick Health, put it bluntly on X: "Claude Code wrote all of Claude Cowork. Can we all agree that we're in at least somewhat of a recursive improvement loop here?"

The implication is profound: Anthropic's AI coding agent may have substantially contributed to building its own non-technical sibling product. If true, this is one of the most visible examples yet of AI systems being used to accelerate their own development and expansion — a strategy that could widen the gap between AI labs that successfully deploy their own agents internally and those that do not.

## Connectors, browser automation, and skills extend Cowork's reach beyond the local file system

Cowork doesn't operate in isolation. The feature integrates with Anthropic's existing ecosystem of connectors — tools that linkClaudeto external information sources and services such asAsana,Notion,PayPal, and other supported partners. Users who have configured these connections in the standard Claude interface can leverage them within Cowork sessions.

Additionally, Cowork can pair withClaude in Chrome, Anthropic's browser extension, to execute tasks requiring web access. This combination allows the agent to navigate websites, click buttons, fill forms, and extract information from the internet — all while operating from the desktop application.

"Cowork includes a number of novel UX and safety features that we think make the product really special,"Cherny explained, highlighting "a built-in VM [virtual machine] for isolation, out of the box support for browser automation, support for all your claude.ai data connectors, asking you for clarification when it's unsure."

Anthropichas also introduced an initial set of "skills" specifically designed for Cowork that enhance Claude's ability to create documents, presentations, and other files. These build on theSkills for Claudeframework the company announced in October, which provides specialized instruction sets Claude can load for particular types of tasks.

## Why Anthropic is warning users that its own AI agent could delete their files

The transition from a chatbot that suggests edits to an agent that makes edits introduces significant risk. An AI that can organize files can, theoretically, delete them.

In a notable display of transparency, Anthropic devoted considerable space in its announcement towarning users about Cowork's potential dangers— an unusual approach for a product launch.

The company explicitly acknowledges that Claude "can take potentially destructive actions (such as deleting local files) if it's instructed to." Because Claude might occasionally misinterpret instructions, Anthropic urges users to provide "very clear guidance" about sensitive operations.

More concerning is the risk of prompt injection attacks — a technique where malicious actors embed hidden instructions in content Claude might encounter online, potentially causing the agent to bypass safeguards or take harmful actions.

"We've built sophisticated defenses against prompt injections," Anthropic wrote, "but agent safety — that is, the task of securing Claude's real-world actions — is still an active area of development in the industry."

The company characterized these risks as inherent to the current state of AI agent technology rather than unique to Cowork. "These risks aren't new with Cowork, but it might be the first time you're using a more advanced tool that moves beyond a simple conversation," the announcement notes.

## Anthropic's desktop agent strategy sets up a direct challenge to Microsoft Copilot

The launch ofCoworkplaces Anthropic in direct competition withMicrosoft, which has spent years attempting to integrate itsCopilot AIinto the fabric of the Windows operating system with mixed adoption results.

However, Anthropic's approach differs in its isolation. By confining the agent to specific folders and requiring explicit connectors, they are attempting to strike a balance between the utility of an OS-level agent and the security of a sandboxed application.

What distinguishes Anthropic's approach is its bottom-up evolution. Rather than designing an AI assistant and retrofitting agent capabilities, Anthropic built a powerful coding agent first —Claude Code— and is now abstracting its capabilities for broader audiences. This technical lineage may give Cowork more robust agentic behavior from the start.

Claude Code has generated significant enthusiasm among developers since its initial launch asa command-line tool in late 2024. The company expanded access with aweb interfacein October 2025, followed by aSlack integrationin December. Cowork is the next logical step: bringing the same agentic architecture to users who may never touch a terminal.

## Who can access Cowork now, and what's coming next for Windows and other platforms

For now, Cowork remains exclusive toClaude Max subscribersusing the macOS desktop application. Users on other subscription tiers — Free, Pro, Team, or Enterprise — can join a waitlist for future access.

Anthropic has signaled clear intentions to expand the feature's reach. The blog post explicitly mentions plans to add cross-device sync and bring Cowork to Windows as the company learns from the research preview.

Cherny set expectations appropriately, describing the product as "early and raw, similar to what Claude Code felt like when it first launched."

To accessCowork, Max subscribers can download or update the Claude macOS app and click on "Cowork" in the sidebar.

## The real question facing enterprise AI adoption

For technical decision-makers, the implications of Cowork extend beyond any single product launch. The bottleneck for AI adoption is shifting — no longer is model intelligence the limiting factor, but rather workflow integration and user trust.

Anthropic's goal, as the company puts it, is to make working with Claude feel less like operating a tool and more like delegating to a colleague. Whether mainstream users are ready to hand over folder access to an AI that might misinterpret their instructions remains an open question.

But the speed of Cowork's development — a major feature built in ten days, possibly by the company's own AI — previews a future where the capabilities of these systems compound faster than organizations can evaluate them.

The chatbot has learned to use a file manager. What it learns to use next is anyone's guess.

## More
