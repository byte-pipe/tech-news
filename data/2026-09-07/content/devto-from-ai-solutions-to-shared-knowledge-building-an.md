---
title: 'From AI Solutions to Shared Knowledge: Building an MCP for the Community - DEV Community'
url: https://dev.to/pascal_cescato_692b7a8a20/from-ai-solutions-to-shared-knowledge-building-an-mcp-for-the-community-6bk
site_name: devto
content_file: devto-from-ai-solutions-to-shared-knowledge-building-an
fetched_at: '2026-09-07T16:17:31.971178'
original_url: https://dev.to/pascal_cescato_692b7a8a20/from-ai-solutions-to-shared-knowledge-building-an-mcp-for-the-community-6bk
author: Pascal CESCATO
date: '2026-09-07'
description: 'This is a submission for the Weekend Challenge: Generosity Edition Don''t Just Ask AI. Give the... Tagged with devchallenge, weekendchallenge, ai, mcp.'
tags: '#devchallenge, #weekendchallenge, #ai, #mcp'
---

DEV Weekend Challenge: Generosity Edition Submission 💜

This is a submission for theWeekend Challenge: Generosity Edition

Don't Just Ask AI. Give the Answer Back.

AI is a real force multiplier for software development. It's also the ideal companion for solving technical problems fast.But all that knowledge — we keep it to ourselves. Or rather, we lose it.

The story always stops there.

Question → answer → problem solved — and the conversation sinks into the chat history, gone.

Then someone else hits the exact same wall. Same cycle: question → answer → problem solved — and the conversation sinks into the chat history, gone.

That's the problem. Not that AI can't solve the same issue twice — it's that a working solution already exists somewhere: someone already investigated, tested, found the fix, and had a conversation detailed enough to explain it properly.

Why should that knowledge evaporate the moment the session ends? Why keep asking the same question over and over — burning electricity, water, and time that's already been spent — instead of recycling that raw material?

That's the idea behindShared Knowledge MCP.

## What I Built

Shared Knowledge is an MCP server that turns a solution from an AI conversation into a proposed Markdown article, then into a GitHub Pull Request submitted for human review. Once merged, the contribution is published to a documentation site and gets an audio version generated with ElevenLabs.

The project turns a solved problem into a reusable piece of community knowledge — but only when the user makes the explicit decision to share it.

The conversation itself stays strictly private. The MCP server extracts only the relevant solution, structures it as a standalone English Markdown article, validates it, and opens a Pull Request on GitHub.

Nothing gets published automatically. A human reviews the contribution and decides whether it belongs in the shared knowledge base. Only once the PR is merged does the article land on the public documentation site, which in turn kicks off its audio version.

The pipeline is deliberately minimal:

AI conversation → explicit sharing → MCP → Markdown → Pull Request → human review → merge → docs + audio

The one boundary that matters is human review. The MCP can structure knowledge and prepare a contribution — it can't decide, on anyone's behalf, what deserves to become public knowledge.

## Demo

The public documentation site is live:

## AI-assisted problems already solved | Shared Knowledge

A community knowledge base built around AI-assisted problem solving - solved problems, shared on purpose.

 pcescato.github.io
 

It currently hosts four published articles, each with a generated audio version.

To prove the system actually works across different clients — no shortcuts, nothing hard-coded — I testedpublish_knowledgethrough two very different paths.

### Direct script execution

The first contribution published through Shared Knowledge went out as a real Pull Request:Optional dependency crashes the import chain when the import itself isn't optional.

That PR walks through the whole flow end to end:

* a real technical problem solved with an AI assistant (an optional dependency inpyproject.tomlthat crashed the import chain);
* an explicit turn into a structured Markdown article (sections, metadata, tags);
* automatic validation by the MCP server, which opens the PR;
* an automated review from GitHub Copilot, flagging YAML formatting and heading issues;
* fixes applied, then a merge intomain;
* and, after the merge, an ElevenLabs audio version generated and published to the docs site.

That first PR is also a concrete act of generosity: someone took the time to turn their fix into a resource every future developer hitting the same wall can reuse.

### Conversational Agent mode

Next, I used a real AI client — GitHub Copilot Chat in Agent mode, running inside a Codespace.

Here, the assistant spontaneously started by querying the existing base throughsearch_knowledgeto check for duplicates before deciding to publish:PR #2.

That behavior wasn't hard-coded anywhere in the MCP server: the server just provides the tools, and the calling assistant decides how to use them.Shared Knowledge isn't a closed AI app tied to one model — it's an open MCP interface for sharing knowledge.

## Code

The full project is open source on GitHub:

## pcescato/shared-knowledge

### community-driven knowledge base built around AI-assisted problem solving

# Shared Knowledge MCP

Turn solved problems into shared knowledge.Don't just get the answer. Give the answer back.

Shared Knowledge MCPis a community-driven knowledge base built around AI-assisted problem solving. It is anMCP (Model Context Protocol)server that lets any MCP-compatible AI assistant (Claude, ChatGPT/Codex, Cursor, …)searcha shared knowledge base before solving a problem from scratch, andpublisha freshly solved problem as a community knowledge article — submitted as a GitHub Pull Request for human review, then published as a static documentation website.

The core principle:

The conversation remains private. The knowledge extracted from it can be shared.Sharing is always explicit and voluntary — nothing is ever published without the user asking for it.

Private conversation
 ↓
AI-assisted solution
 ↓
User chooses to share
 ↓
Caller structures the article (guidelines prompt)
 ↓
GitHub Pull Request
 ↓
Human review
 ↓
Shared knowledge base
 ↓
Available
…

View on GitHub

The repo includes the MCP server, the knowledge articles, the Astro/Starlight static site, the GitHub Actions workflows, the test suite, and the documentation.

## How I Built It

### Weekend-MVP pragmatism

Building a solo PoC in a weekend forces hard limits.

I could have designed a PostgreSQL database, added vector search with embeddings, built a full authentication system, and shipped an admin dashboard.

I didn't.

For this MVP:

* GitHub is the only source of truth.The knowledge base is plain Markdown. Git already handles versioning, history, branches, diffs, and code review — no reason to rebuild any of that.
* Astro + Starlight handles the rendering.No need to run an application server around the clock just to serve static content that a human has already approved.
* Search stays intentionally simple.Field-weighted keyword search is more than enough at this scale. At four articles, adding a vector database wouldn't have made the system smarter — it would have just added weight to the prototype for no real benefit.

### Three narrowly-scoped MCP tools

The server exposes three deliberately simple tools:

* search_knowledge— searches the base with field-weighted ranking.
* get_knowledge— fetches a specific article safely (path-traversal protected).
* publish_knowledge— validates the structure and opens a GitHub Pull Request.

### Using it today

Any stdio-compatible MCP client can connect to the server — Claude Desktop, VS Code with GitHub Copilot Chat in Agent mode, and others. A minimal.vscode/mcp.jsonis enough:

{

 
"servers"
:
 
{

 
"shared-knowledge"
:
 
{

 
"type"
:
 
"stdio"
,

 
"command"
:
 
"${workspaceFolder}/.venv/bin/python3"
,

 
"args"
:
 
[
"${workspaceFolder}/server.py"
],

 
"env"
:
 
{

 
"GITHUB_TOKEN"
:
 
"${env:GITHUB_TOKEN}"
,

 
"GITHUB_REPO"
:
 
"pcescato/shared-knowledge"
,

 
"KNOWLEDGE_DIR"
:
 
"${workspaceFolder}/knowledge"

 
}

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Clone the repo,pip install -e ., set your ownGITHUB_TOKEN, point it at your own knowledge repo — and any assistant that speaks MCP can start reading from and contributing to the base, opening Pull Requests under your own GitHub identity.

### The architectural pivot: interoperability over prize categories

In my first implementation, the MCP server called Gemini directly, internally, to turn a conversation summary into a structured article. It worked — but it went against the whole point of MCP: the server was turning into a monolithic app tied to one specific AI vendor.

So I reworked the architecture mid-build.

The server now exposes an MCP prompt (knowledge_article_guidelines) that lays out the structuring rules — English output, mandatory## Problem/## Solutionsections, a controlled category and tag vocabulary. It's the calling assistant that usesits own modelto structure the content, whilepublish_knowledgeonly validates and publishes.

It doesn't matter whether the client runs on Claude, GPT, Gemini, or a local model.

That choice had a real cost for the challenge: by taking Gemini out of the critical path, I knowingly gave up eligibility for theBest Use of Google AIprize. But I'd rather submit a project whose architecture stays true to the idea of interoperability than force a dependency in just to check a prize-category box.

### Multi-agent collaboration: practicing what it preaches

There's a nice loop in this project:it was built using exactly the paradigm it argues for.

Instead of relying on a single assistant, the repo was developed by having several AI environments collaborate, each in a specific role, under human supervision:

* FreeBuff + GLM 5.3— drove development through seven sequential, sealed-off batches, each with explicit guardrails ("Do NOT implement...", "Do ONLY...") to keep scope from drifting and stop one component's changes from breaking another.
* GitHub Copilot CLI + Haiku 4.5— acted as an independent code reviewer, inspecting PRs and running critical checks.
* OpenCode + Big Pickle— handled local code iteration, refactoring, fast edge-case fixes, and bug squashing.

### Real bugs from the real world

A weekend PoC is a fast reminder that architecture diagrams aren't reality:

### The AI-generated bug that wasn't there

An automated review from Copilot CLI reported a very convincing GitHub authentication bug — code excerpt and line number included. I checked before touching anything: the line, and the code it described, simply didn't exist in the repo. A useful reminder that AI review is genuinely valuable, but it still needs a human to check its homework.

### The ElevenLabs Voice Library trap

Audio generation kept failing with a deeply misleadinginvalid_uiderror. The voice picked from the web interface belonged to the sharedVoice Library, which isn't reachable through the API on a free account. Once I added the voice to "My Voices," a second issue surfaced: an emptyELEVENLABS_MODEL_IDvariable in GitHub Actions was silently overriding the code's default value — becauseos.environ.get()only falls back to its default when the key is missing, not when it's set to an empty string.

### The manually-broken state problem

During a local test, I deleted an MP3 file without updating.audio_manifest.jsonto match. On the next CI run, the workflow read the manifest and concluded the audio was already up to date. The code wasn't broken — I had just thrown the system's state out of sync by editing files by hand.

## What's Left to Do

### Improving audio generation

Audio generation through ElevenLabs happensstrictly after human review and merge.No audio is ever produced for an unreviewed Pull Request.

That said, listening back to the generated MP3s surfaced an interesting engineering reality:a format that's perfectly suited for human reading and Git diffs isn't necessarily suited for a text-to-speech engine.Markdown is built for Git, not for speech.

When a TTS engine reads raw Markdown, section headings (## Problem,## Context) run straight into the following text with no real prosodic break. The result lacks breathing room and narrative structure.

The audio pipeline will need an intermediate scripting step:

Validated Markdown article
 ↓
Structure parser
 ↓
Narration script (pauses & transition cues)
 ↓
ElevenLabs API
 ↓
Final MP3 file

Enter fullscreen mode

Exit fullscreen mode

Instead of sending raw Markdown syntax straight to ElevenLabs, the pipeline will turn the editorial structure into an actual narration script. The Markdown article stays the single source of truth — the audio becomes a purpose-built derived format.

The obvious temptation would be to turn this into a full community platform — voting, comments, vector search, dashboards.

I don't think that's the right priority. The point, first, is to validate the simplicity of the loop itself:someone solves a problem → chooses to give the answer back → someone else gets to reuse it.

The natural next step toward a genuinely usable product is hosting the MCP server remotely overStreamable HTTP— no local install, just a URL added to whatever assistant you already use.

But the loop doesn't need voting, dashboards, or a bigger model to work. It needs someone willing to give the answer back — and someone else willing to trust it enough to read it.

## Prize Categories

### Best Use of ElevenLabs

Shared Knowledge uses ElevenLabs to make validated technical solutions accessible as audio. Audio generation is decoupled from the MCP server and runs exclusively inside GitHub Actions after a Pull Request is merged — guaranteeing that only reviewed, approved content ever gets synthesized into speech.

Not submitted for Best Use of Google AI: the architectural pivot described above deliberately took Gemini out of the critical path in favor of model-agnostic structuring. That's a trade made on purpose, not an oversight.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse