---
title: Open Source Toolkit for Building AI Agents in 2026 - DEV Community
url: https://dev.to/anmolbaranwal/open-source-toolkit-for-building-ai-agents-in-2026-55h1
site_name: devto
content_file: devto-open-source-toolkit-for-building-ai-agents-in-2026
fetched_at: '2026-05-21T19:36:31.734942'
original_url: https://dev.to/anmolbaranwal/open-source-toolkit-for-building-ai-agents-in-2026-55h1
author: Anmol Baranwal
date: '2026-05-21'
description: It used to take a lot of effort to get your first PR merged in open source. Now you can ship... Tagged with programming, tutorial, opensource, javascript.
tags: '#programming, #tutorial, #opensource, #javascript'
---

Focuses on maintained repos over hype

It used to take a lot of effort to get your first PR merged in open source. Now you can ship something real in a weekend thanks to coding agents like Claude Code.

But that also means the noise went way up. I saw the wave of openclaw repos a while back but the ratio of hype to actual maintenance is quite different.

I have a habit of exploring new projects almost every day, been doing that for 2+ years. Lately I have been deep in the AI agents space and these are the repos that actually stuck.

These aren't random projects, I have come across these in my journey and built with some of them. Agent harness, frontend stack, engineering skills for coding agents, voice agents, browser automation, computer use and a lot more. If you are building AI agents in 2026, this list is for you.

If you are new to open source, check outthis free guideI made a while back. For any project you're considering: look for aCONTRIBUTING.mdand a healthy community profile.

Let's jump in.

## Categories

* Frontend & UI Layer(6)
* Skills & Plugins(4)
* Computer Use(6)
* Agent Orchestration(6)
* Coding Agent Harness(4)
* Open-Source Coding Agents(7)
* Browser Automation(5)
* Web Scraping & Ingestion(5)
* Multi-Agent Frameworks(6)
* Document Processing(7)
* Voice Agents(7)
* Visual Builders(6)
* MCP & Tool Integration(5)
* Sandboxing & Code Execution(5)
* Agent Memory(5)
* Testing & Evaluation(7)
* Monitoring & Observability(5)

Just remember, there's no specific order in this post. Every open source project is good in its own way.

## 1. Frontend & UI Layer - CopilotKit

CopilotKitis the frontend stack for Agents. Most agent stacks give you the backend and leave the user-facing layer entirely to you.

CopilotKit is the layer that provides all the building blocks. Chat components, hooks, headless UI for custom agent interfaces, persistent threads, human-in-the-loop, shared state and a built-in Inspector for debugging.

They support all three generative UI patterns in one runtime. Basically, it allows the agent to show components rather than just describing them (A2UI by Google is one pattern).

The part I really like is that they have amcp server for coding agentsthat lets coding agents fetch live docs without any usage limit.

You can connect directly to any LLM in just a few lines without any agent framework on the backend and make it context-aware about your app. They also have 13+ first-party integration support with major frameworks.

import
 
{

 
CopilotRuntime
,

 
copilotRuntimeNextJSAppRouterEndpoint
,

}
 
from
 
"
@copilotkit/runtime
"
;

import
 
{
 
BuiltInAgent
 
}
 
from
 
"
@copilotkit/runtime/v2
"
;
 

import
 
{
 
NextRequest
 
}
 
from
 
"
next/server
"
;

const
 
builtInAgent
 
=
 
new
 
BuiltInAgent
({
 
 
model
:
 
"
openai:gpt-5.5
"
,

});

const
 
runtime
 
=
 
new
 
CopilotRuntime
({

 
agents
:
 
{
 
default
:
 
builtInAgent
 
},
 

});

export
 
const
 
POST
 
=
 
async 
(
req
:
 
NextRequest
)
 
=>
 
{

 
const
 
{
 
handleRequest
 
}
 
=
 
copilotRuntimeNextJSAppRouterEndpoint
({

 
runtime
,

 
endpoint
:
 
"
/api/copilotkit
"
,

 
});

 
return
 
handleRequest
(
req
);

};

Enter fullscreen mode

Exit fullscreen mode

You can enable multimodal attachments like images, PDFs, audio, video & passreasoningEffortto control how hard the model thinks.

The framework-agnostic design is what makes it practical. It's built onAG-UIprotocol, the open event protocol for agent-user interaction now adopted by Google, AWS, Microsoft, LangChain, and many more. So if you switch any framework or protocol, everything on the frontend stays exactly the same.

I have used it for a couple of my recent projects, including a job search assistant I built using LangChain Deep Agents & it helped me surface all the things it was doing under the hood.

CopilotKit has 31.5k stars on GitHub.

Star CopilotKit ⭐️

### Alternatives

* TanStack AI- Framework-agnostic, vendor-neutral AI SDK from the TanStack team. Strong TypeScript support, modular adapters per provider. Direct alternative to Vercel AI SDK without the Next.js coupling.
* Vercel AI SDK- Good for streaming and tool calling in Next.js. Stateless and tied to the Vercel ecosystem.
* Tambo- React SDK focused purely on generative UI. Still early and not the full agent-chat stack.
* Assistant UI- Headless React primitives for building chat UIs.
* agent-native- Framework from Builder.io where agent and UI share the same action model. Define actions once, expose them to both. No separate agent API - if the UI can do it, the agent can and vice versa.

## 2. Skills & Plugins - agent-skills

Anthropic shipped the Skills format and the ecosystem took off fast. A lot of people are even saying MCP is dead because of Skills (I don't really believe so).

A skill is basically a directory containing a SKILL.md file that contains organized folders of instructions, scripts, and resources that give agents additional capabilities.

Theofficial repohas 138k stars & it's worth reading theengineering blogto understand how progressive disclosure works in practice.

agent-skillsby Addy Osmani is the gold. 23 production-grade engineering skills with 7 slash commands that map to the full dev lifecycle (/spec,/plan,/build,/test,/review,/ship).

Hard exit criteria, anti-rationalization tables, progressive disclosure. Encodes Google engineering culture -- Hyrum's Law, the Beyonce Rule, trunk-based development.

It has 43.8k stars on GitHub. Here are all the skills included.

Star Agent Skills ⭐️

agent-skills/
├── skills/ # 23 skills (22 lifecycle + 1 meta)
│ ├── interview-me/ # Define
│ ├── idea-refine/ # Define
│ ├── spec-driven-development/ # Define
│ ├── planning-and-task-breakdown/ # Plan
│ ├── incremental-implementation/ # Build
│ ├── context-engineering/ # Build
│ ├── source-driven-development/ # Build
│ ├── doubt-driven-development/ # Build
│ ├── frontend-ui-engineering/ # Build
│ ├── test-driven-development/ # Build
│ ├── api-and-interface-design/ # Build
│ ├── browser-testing-with-devtools/ # Verify
│ ├── debugging-and-error-recovery/ # Verify
│ ├── code-review-and-quality/ # Review
│ ├── code-simplification/ # Review
│ ├── security-and-hardening/ # Review
│ ├── performance-optimization/ # Review
│ ├── git-workflow-and-versioning/ # Ship
│ ├── ci-cd-and-automation/ # Ship
│ ├── deprecation-and-migration/ # Ship
│ ├── documentation-and-adrs/ # Ship
│ ├── shipping-and-launch/ # Ship
│ └── using-agent-skills/ # Meta: how to use this pack
├── agents/ # 3 specialist personas
├── references/ # 4 supplementary checklists
├── hooks/ # Session lifecycle hooks
├── .claude/commands/ # 7 slash commands (Claude Code)
├── .gemini/commands/ # 7 slash commands (Gemini CLI)
└── docs/ # Setup guides per tool

Enter fullscreen mode

Exit fullscreen mode

### Alternatives

* skills.sh- The npm for agent skills (marketplace). Install any skill withnpx skills add <owner/repo>. The leaderboard surfaces what developers are actually using rather than what got hyped on launch day.
* taste-skill- Portable design taste skills (minimalist, brutalist, GPT-tuned) that fix the generic-looking AI slop. One of the few skills that visibly changes what the agent produces. I have been using it for a couple of months.
* Repomix- Packs an entire repo into one AI-friendly file. Pick when you need the agent to see the whole codebase at once.

## 3. Computer Use - UI-TARS Desktop

Most computer-use agents take a screenshot and ask a generalist VLM to guess pixel coordinates.UI-TARSwas trained end-to-end on GUI grounding - it understands UI elements as a first-class concept rather than image regions to click on.

What I find really interesting is the "System-2 reflection" -- after each action, it compares before/after screenshots and generates a corrective plan if something didn't land right, instead of just going through a broken sequence.

It scores higher on OSWorld vs Claude Computer Use. Personally, I believe practical usage matters a lot more than benchmarks. 😅

They also shipAgent TARS- a CLI and Web UI that brings the same vision + MCP tool integration to your terminal and browser.

You can say something like: Please help me book the earliest flight from San Jose to New York on September 1st and the last return flight on September 6th on Priceline. All the demos are in the readme.

It has 34k stars on GitHub.

Star UI-TARS Desktop ⭐️

One very interesting repo I found isSutando. It's a personal AI agent for macOS and runs on your Claude Code subscription with minimal extra costs.

The use cases are pretty wild. You can say "join my 2pm call" - it reads your calendar, joins Zoom via the desktop app or Google Meet via browser, takes screenshots to identify participants, does live research when someone asks a question and writes you a summary when the call ends.

Or you can call it from your phone, say "summon" - it opens Zoom with screen sharing and you control your computer by voice while walking around.

When you're not giving it tasks, Sutando runs an autonomous build loop - it monitors its own health, detects patterns in how you work, discovers new skills, and builds missing capabilities, which is crazy.

It has like 300 stars on Github but it is genuinely interesting.

### Alternatives

* Midscene- Also from ByteDance's Web Infra team. Vision-driven UI automation across web, Android, and iOS from one API. Integrates with Playwright and Puppeteer, ships a Chrome extension, CLI, and MCP server.
* Agent-S- Hierarchical planning approach that builds a knowledge base from past interactions and uses it to plan future tasks. Benchmarks well on OSWorld and WindowsAgentArena.
* Bytebot- Self-hosted AI desktop agent in a containerized Linux environment. The agent gets its own full virtual desktop -- browser, file system, password manager, any app.docker-compose upand it's running.
* cua- macOS/Linux VM sandbox so the agent runs on a virtual machine, not your real machine.
* OpenHands- Full developer environment that can browse, write code, run tests, and commit PRs. Covered again under Coding Agents.

## 4. Agent Orchestration - LangGraph

LangGraphis the stateful graph runtime built on LangChain. It is the most mature framework for building, managing, and deploying long-running, stateful agents.

The loop is a graph. Every step is a node. State is typed and checkpointed. You can pause at any node, serialize the entire state to disk, resume on a different machine days later.

They also shipDeep Agents- a coding agent harness on top of LangGraph with planning, filesystem tools, sub-agents, and context compression, if you want to skip writing the graph yourself.

Combining it with other products like LangSmith Engine, LangChain, Deep Agents gives developers a full suite of tools for building agents. And it's super useful for debugging.

If you're confused, here's a simple distinction:

* LangChain - agents via chains andcreate_agent. Simple, fast to get started, less control over the state. The foundation on which everything else is built. If the process dies, the agent starts over.
* LangGraph - stateful graph runtime built on LangChain. You can replay from any checkpoint to debug what went wrong.
* Deep Agents - harness built on top of LangGraph.

LangGraph has 32.3k stars on GitHub.

Star LangGraph ⭐️

### Alternatives

* Agno- lightweight support for agents needing persistent memory and multimodal inputs. Ships with AgentOS, a pre-built FastAPI server with sessions, streaming, RBAC, and observability. Claims 529x faster instantiation than LangGraph.
* Mastra- TypeScript-first with RAG, observability, MCP, and workflows baked in. Pick if your team lives in JS/TS rather than Python.
* Pydantic AI- Type-safe agent framework from the Pydantic team. Pick when you want validated structured outputs without writing the validators yourself.
* Google ADK- Google's official agent dev kit with native Vertex AI integration. Pick if you're building on Google Cloud.
* PocketFlow- A 100-line LLM framework. Genuinely minimal. Pick when LangGraph feels like too much infrastructure.

## 5. Coding Agent Harness - Deep Agents

A harness is everything around the model that makes it an agent - tools, state, planning, memory, feedback loops, guardrails.

You can say: "Agent = Model + Harness". LangChain proved this matters more than most teams expect: harness-layer changes alone moved the same model from 52.8% to 66.5% on Terminal Bench 2.0, jumping from Top 30 to Top 5. No model change.

Deep Agentsis LangChain's batteries-included harness built on LangGraph. Planning, filesystem tools, sub-agents, and context compression out of the box.

User goal
 ↓
Deep Agent (LangGraph StateGraph)
 ├─ Plan: write_todos → updates "todos" in state
 ├─ Delegate: task(...) → runs a subagent with its own tool loop
 ├─ Context: ls/read_file/write_file/edit_file → persists working notes/artifacts
 ↓
Final answer

Enter fullscreen mode

Exit fullscreen mode

The core problem with long-running agents is that they accumulate tool call results until the context window fills -- causing context poisoning, distraction, and confusion.

Their fix:

* Large tool outputs go to a virtual filesystem instead of the prompt
* Skills load only frontmatter at startup, full content on demand
* Conversation history gets compressed as sessions grow
* Sub-agents run in their own context window, the main agent only gets the final result

You can build lots of stuff around this likeDeep Research Assistant.

Deep Agents has 23.1k stars on GitHub.

Star Deep Agents ⭐️

### Alternatives

* Hive- Outcome-driven agent development framework. Agents evolve based on whether they actually achieved the goal, not just whether they completed steps.
* Browser Harness- From the Browser Use team. Self-healing harness that gives the LLM maximum freedom -- instead of wrapping Chrome with thousands of lines of heuristics, it lets the LLM use CDP directly and add its own tools when it needs them. Different philosophy from most browser frameworks.
* Archon- Open-source harness builder for AI coding. Describe what you want and it generates a deterministic, repeatable agent harness for you.

## 6. Open-Source Coding Agents - OpenCode

I have used Claude Code and Codex extensively. Both are great but locked to their respective ecosystems.

OpenCodeis the open-source alternative - terminal-native, 75+ provider support, LSP integration, multi-session (run multiple agents in parallel on the same project), privacy-first.

What makes it stand out: genuinely provider-agnostic from day one. You can switch between Claude, Gemini, GPT-5 and local models in the same session without reconfiguring anything. Most other coding agents have a preferred model set up in the defaults.

You can also share a link to any session for reference or to debug. It is available as a terminal interface, desktop app, and IDE extension - though I have only used the terminal.

OpenCode has 162k stars on GitHub.

Star OpenCode ⭐️

### Alternatives

* Codex (OpenAI)- OpenAI's official terminal coding agent. Pick when you want first-party support and the cleanest GPT-5 integration.
* Gemini CLI- Google's official terminal agent with 1M token context. The free tier is hard to beat for experimentation.
* Cline- VS Code extension with per-step approval. Pick if you want IDE-native control rather than a terminal.
* Aider- Git-native terminal pair programmer. 70%+ of Aider's own code is now written by Aider. Fast and model-agnostic.
* OpenHands- Full agentic developer environment that can browse, run shell, and commit PRs. Heavier than the others.
* Goose- Block's extensible coding agent with first-class MCP and a clean extension model.

## 7. Browser Automation - Browser Use

Browser Usegives your agent a browser. Point it at a URL, describe what you want done, and it clicks, types, and navigates. You write intent, not selectors -- the agent reads the DOM and figures out the interaction itself.

The LLM-first design means you describe intent, not selectors, and the agent figures out the DOM.

The reason they are so good is that they have built purpose-built LLMs specifically for browser tasks. Theirbu-ultramodel scores 97% on Mind2Web vs 62% forclaude-opus-4-6.

The open source library works with any model but their custom ones are what the benchmarks run on.

They also have adesktop appthat controls your local Chrome directly andBrowser Use Box- a 24/7 Claude Code agent you can deploy on any $5 VPS and control via Telegram.

# pip install browser-use-sdk

from
 
browser_use_sdk.v3
 
import
 
AsyncBrowserUse

client
 
=
 
AsyncBrowserUse
()

result
 
=
 
await
 
client
.
run
(

 
"
Go to amazon.com, extract 200 products with name, price and reviews, save to products.csv
"

Enter fullscreen mode

Exit fullscreen mode

It has 94k stars on GitHub.

Star Browser Use ⭐️

### Alternatives

* Stagehand- Four primitives:act,extract,observe,agent. Deterministic step-by-step control when you need it, autonomous execution when you don't. Self-healing -- "click submit" survives page redesigns because it's resolved by AI at runtime, not hardcoded selectors.
* Playwright MCP- Microsoft's MCP server wrapping Playwright. Pick if you already write Playwright tests and want your agent to drive the same browser.
* Skyvern- Uses a swarm of agents + computer vision to operate on sites it's never seen before. No XPaths, no selectors -- maps visual elements to actions in real-time. Also ships a no-code workflow builder.
* Scrapling- Adaptive scraper that survives selector drift. Bypass anti-bot systems like Cloudflare Turnstile out of the box. Allows concurrent, multi-session crawls with automatic proxy rotation.

## 8. Web Scraping & Ingestion - Firecrawl

Agents need to pull content from the web constantly - research, monitoring, competitive intel, RAG pipelines.

Most scrapers give you raw HTML full of nav menus, ads, and cookie banners that burn tokens and confuse the model.

Firecrawlconverts any website into clean LLM-ready Markdown or structured JSON. Three core endpoints that cover everything:

* /searchfor web search with content already extracted
* /scrapefor full page Markdown
* /extractfor structured JSON via natural language prompt.

They also have an/agentendpoint where basically you describe what you want in natural language and it searches, navigates, and extracts across multiple sites autonomously. No URLs needed.

import
 
Firecrawl
 
from
 
'
@mendable/firecrawl-js
'
;

import
 
{
 
z
 
}
 
from
 
'
zod
'
;

const
 
firecrawl
 
=
 
new
 
Firecrawl
({
 
 
apiKey
:
 
'
fc-YOUR-API-KEY
'
 

});

const
 
schema
 
=
 
z
.
object
({

 
companies
:
 
z
.
array
(
z
.
object
({

 
name
:
 
z
.
string
(),

 
founders
:
 
z
.
array
(
z
.
string
()),

 
funding
:
 
z
.
string
().
optional
(),

 
website
:
 
z
.
string
()

 
}))

});

const
 
result
 
=
 
await
 
firecrawl
.
agent
({

 
prompt
:
 
'
Get all YC W24 companies
'
,

 
schema
:
 
schema

});

Enter fullscreen mode

Exit fullscreen mode

TheirFIRE-1 navigation agent (beta)can autonomously navigate complex sites, clicks, scrolls, fills forms and handles multi-step flows before extracting. Pages behind login or pagination are no longer a blocker.

There's a lot more so feel free to explore. It has 122k stars on GitHub.

Star Firecrawl ⭐️

### Alternatives

* Gitingest- Replace 'hub' with 'ingest' in any GitHub URL and get a prompt-friendly extract of the codebase. Filter by file size, include/exclude specific paths, and support private repos too.
* Crawl4AI- Open-source, self-hosted, no API key needed. Built specifically for RAG pipelines - LLM-aware chunking, BM25 content filtering, full-site crawling with depth control. Pick when you want full control without per-request fees.
* Jina Reader- Prependr.jina.ai/to any URL and get clean Markdown. Zero setup, zero SDK. Pick for quick one-off page conversion or prototyping, where you don't want any configuration.
* ScrapeGraphAI- Prompt-driven scraping. Describe what you want extracted in natural language and it builds the scraping workflow. Pick when you need structured JSON extraction, not just Markdown.

## 9. Multi-Agent Frameworks - CrewAI

CrewAIis the most widely adopted multi-agent framework right now. You define a crew of agents with specific roles, goals, and tools and CrewAI handles how they collaborate to finish a task.

The role-based model (PM, researcher, engineer) is intuitive because it maps to how you would actually divide work between people.

It's the easiest entry point into multi-agent systems. Well-documented, large community, with examples for almost everything.

The tradeoff is control - agent-to-agent communication is mediated through task outputs, not direct messaging and there's no built-in checkpointing for long-running workflows.

CrewAI Flows (the newer event-driven mode) addresses some of this for predictable pipelines. For cyclical workflows with feedback loops, most teams end up moving parts to LangGraph.

CrewAI has 51.6k stars on GitHub.

Star CrewAI ⭐️

### Alternatives

* AG2- The community fork of AutoGen (Microsoft moved AutoGen to maintenance mode). Conversable agents that talk to each other in group chats, swarms, and nested chats. Better for research and custom communication patterns.
* Microsoft Agent Framework- The enterprise successor to AutoGen. Stable APIs, long-term support, A2A and MCP built in. Pick when you need long-term support guarantees.
* OWL- Multi-agent automation framework built on CAMEL. Uses a planning agent + execution agent model for long-horizon real-world tasks. Ranked #1 on the GAIA benchmark among open-source frameworks.
* MetaGPT- Simulates a software company with PM, architect, and engineer agents. Best for code-generation pipelines.
* AgentScope- Alibaba's production framework with realtime voice, MCP, A2A, and OTel built in.

## 10. Document Processing - Docling

Feeding a PDF to an agent and watching it miss things that were right there in the table is frustrating. Most parsers extract raw text and lose the structure - tables flatten, multi-column layouts collapse, equations come out unreadable.

Doclingis IBM Research's document conversion engine, now donated to the Linux Foundation. It uses Granite-Docling-258M - a parameter vision-language model purpose-built for document conversion that rivals systems several times its size.

The output usesDocTags, a universal markup format IBM Research developed that captures every page element, its type, position and reading order. Not only Markdown. This is what makes the RAG downstream more accurate.

Red Hat called it "the number one open source repository for document intelligence". Sharing this for no reason 😅

from
 
docling.document_converter
 
import
 
DocumentConverter

source
 
=
 
"
https://arxiv.org/pdf/2408.09869
"
 
# file path or URL

converter
 
=
 
DocumentConverter
()

doc
 
=
 
converter
.
convert
(
source
).
document

print
(
doc
.
export_to_markdown
())
 
# output: "### Docling Technical Report[...]"

Enter fullscreen mode

Exit fullscreen mode

Docling has 60.1k stars on GitHub.

Star Docling ⭐️

### Alternatives

* LlamaIndex- Full RAG framework with 160+ data connectors. Pick when you need orchestration across many data sources, not just document parsing.
* MinerU- PDF parser with SOTA table and formula extraction. Pick for technical or scientific documents where math and equations dominate.
* RAGFlow- DeepDoc pipeline that handles parsing, chunking, and retrieval end-to-end. Pick when you want the full RAG stack, not just the parser.
* Marker- PDF, EPUB, PPTX to Markdown with high fidelity. Faster than Docling, lower GPU requirements. Pick for clean plain-text output at scale.
* PaddleOCR- The OCR engine powering MinerU, RAGFlow, and OmniParser under the hood. 100+ languages, browser SDK. Pick when you need raw OCR power directly.
* Unstructured- 65+ file formats including emails, spreadsheets, and images. Pick for mixed-input pipelines beyond just PDFs.

## 11. Voice Agents - Pipecat

Building voice agents is still harder than it should be. The AI part is mostly solved in my opinion. The hard part is everything around it, like interruption handling, transport, latency budgets across STT/LLM/TTS boundaries.

Pipecatis a Python framework from Daily for real-time voice and multimodal AI agents. STT, LLM, and TTS are composable frame processors like Unix pipes, but for voice.

The reason I picked it: you can swap any STT, LLM, or TTS without rewriting the pipeline. Most devs don't want to be locked into one provider, especially when voice model quality is still changing fast.

Silero VAD (voice activity detection) handles interruption at the framework level - voice activity mid-response stops the audio and re-engages the LLM automatically.

Pipecat Flows then adds predefined conversation paths with dynamic transitions so agents stay on task without going off-script mid-call.

import
 
{

 
PipecatAppBase
,

 
ConnectButton
,

 
UserAudioControl
,

}
 
from
 
"
@pipecat-ai/voice-ui-kit
"
;

<
PipecatAppBase

 
transportType
=
"
smallwebrtc
"

 
connectParams
=
{{
 
webrtcUrl
:
 
"
/api/offer
"
 
}}

>

 
<
div
>

 
<
ConnectButton
 
/>

 
<
UserAudioControl
 
/>

 
<
/div
>

<
/PipecatAppBase
>

Enter fullscreen mode

Exit fullscreen mode

You can go to the website and try it out live. As you can see, I asked How can I bring it to my app & it opened the code panel as well as gave me a proper explanation.

There were multiple panels of code (install, pipeline, final implementation). The part that surprised me was that it was able to detect that I played around with the code when I stopped it, which makes it context-aware to the app.

It has 12k stars.

Star Pipecat ⭐️

The other day I was in a project where the agent would create an appropriate form based on the call and it worked. Generally, it's very hard to collect data from just voice.

### Alternatives

* LiveKit Agents- The WebRTC stack that OpenAI (ChatGPT Voice) and Meta run on. Room-first, not pipeline-first - your agent joins as a participant. Native telephony, semantic turn detection, MCP support. Pick when you need production infrastructure bundled with the framework.
* fish-speech- SOTA open TTS with multilingual zero-shot voice cloning. Pick when output quality matters more than orchestration.
* Moonshine- Very low-latency on-device STT. Pick when latency is the constraint and cloud isn't an option.
* Whisper- OpenAI's STT model. The default transcription layer for custom voice stacks.
* GPT-SoVITS- Few-shot voice cloning from 1 minute of audio, zero-shot from 5 seconds. Chinese, English, Japanese, Korean. Pick for cloned-voice TTS with minimal training data.
* CosyVoice- Alibaba's multilingual zero-shot voice generation with 150ms latency. Pick for non-English voice quality.

## 12. Visual Builders - Langflow

Langflowis a drag-and-drop agent pipeline builder, IBM-backed. Connects to any LLM, any vector DB, any tool.

The way the CTO puts it: "Langflow is essentially an API designer. The flow becomes an endpoint you can call from anywhere."

What makes it interesting: the flow becomes a callable REST endpoint. You prototype visually, then your engineers call it an API from any codebase.

Every component exposes its Python class so you can extend with custom logic without leaving the tool.

You can find a lot ofpre-built templatesto get started. Here is a Supply chain risk monitoring workflow that scores disruption risk by linking supplier and route data with live news signals.

It has 149k stars on GitHub.

Star Langflow ⭐️

### Alternatives

* Dify- LLM app platform with a visual agent builder, RAG pipeline, and plugin marketplace. Pick the more polished UI and built-in app shell.
* Sim- Drag-and-drop agent orchestration, very actively developed. The cleanest 2026-native alternative to Langflow.
* n8n- Workflow automation with 400+ integrations and strong AI nodes. Pick when the workflow is mostly cross-service automation with an agent at the center.
* Flowise- Simpler no-code LangChain builder. Pick for non-technical users who need to build agent workflows without writing code.
* Coze Studio- ByteDance's open-source visual agent platform. Agent builder with RAG and plugins, workflow engine with loops and custom Python execution.

## 13. MCP & Tool Integration - Composio

MCP servers solved how agents connect to tools. But managing OAuth, token refresh, and keeping 1000+ integrations working is still your problem.

Composiois the integration layer between your agent and real-world tools with managed auth.

The part I liked the most is the Tool Router - one MCP endpoint that dynamically discovers and loads the right tools based on what the agent is trying to do. Instead of pre-loading every tool and bloating the context, it surfaces only what's relevant.

They have 28.4k stars on GitHub.

Star Composio ⭐️

### Alternatives

* LiteLLM- One unified API across 100+ LLM providers. Azure, Bedrock, Anthropic all look like OpenAI to your code. Cost tracking, routing, fallback. Pick the model gateway layer.
* MindsDB- SQL access to 200+ data sources from a single interface, no ETL. Also ships as an MCP server. Pick when your agent needs to read data, not take actions.
* ACI- 600+ tool integrations via a unified MCP server. Self-hosted Composio alternative.
* Portkey AI Gateway- 1,600+ models with guardrails built in. Pick when gateway latency matters.

## 14. Sandboxing & Code Execution - E2B

When an agent generates and runs code, that code needs somewhere safe to execute. Regular Docker containers share the host kernel - one vulnerability and untrusted code breaks out.

E2Bprovides isolated sandboxes that let agents safely execute code, process data, and run tools. Their SDKs make it easy to start and manage these environments.

It runs agent-generated code in Firecracker microVMs - each sandbox gets its own dedicated kernel. ~150ms boot, full Linux filesystem, Python, Node, and common packages pre-installed.

import
 
{
 
Sandbox
 
}
 
from
 
'
e2b
'

const
 
sandbox
 
=
 
await
 
Sandbox
.
create
()
 
// Needs E2B_API_KEY environment variable

const
 
result
 
=
 
await
 
sandbox
.
commands
.
run
(
'
echo "Hello from E2B Sandbox!"
'
)

console
.
log
(
result
.
stdout
)

Enter fullscreen mode

Exit fullscreen mode

Nothing touches the host machine. Manus uses it to run 27 different tools. Perplexity uses it for data analysis. Hugging Face uses it to replicate DeepSeek-R1.

You can check some of the examples in their cookbook repo on how to use all of this.

It has 12k stars on GitHub.

Star E2B ⭐️

### Alternatives

* OpenSandbox- Alibaba's internal sandbox infrastructure. Covers coding agents, GUI agents, browser automation, VNC desktops, and RL training from one API. Docker and Kubernetes runtimes. Broader scope than E2B.
* Daytona- ~90ms spin-up, open-source, persistent environments with Git integration and LSP. Pick when you need a state that persists across sessions.
* microsandbox- Local, programmable sandboxes. Pick when you want sandboxes on the dev machine without cloud dependency.
* Firecracker- The microVM tech under E2B, Lambda, and Fargate. Pick when you need the raw layer with full control.

## 15. Agent Memory - mem0

Memory is where most agent demos fall apart in production. The agent knows things in one session and forgets them in the next. We seriously don't want agents to die after closing the tab haha.

mem0is the most widely deployed standalone memory layer right now. Instead of storing raw conversation chunks, it runs an extraction phase that identifies salient facts and distills them into compact natural language memories. Handles short-term, long-term, and entity memory behind one interface.

# Add a memory

messages
 
=
 
[

 
{
"
role
"
:
 
"
user
"
,
 
"
content
"
:
 
"
I
'
m a vegetarian and allergic to nuts.
"
},

 
{
"
role
"
:
 
"
assistant
"
,
 
"
content
"
:
 
"
Got it! I
'
ll remember your dietary preferences.
"
},

]

client
.
add
(
messages
,
 
user_id
=
"
user123
"
)

# Search memories

results
 
=
 
client
.
search
(

 
"
What are my dietary restrictions?
"
,

 
user_id
=
"
user123
"
,

)

# print(results)

Enter fullscreen mode

Exit fullscreen mode

Most major frameworks are building memory in such a way that LangGraph has checkpointing built in (state persists per thread, time travel, crash recovery) and CopilotKit has persistent threads viauseThreads.

The gap worth knowing: Mem0 scores 49% on LongMemEval vs Zep's 63.8% - the difference comes from temporal reasoning.

For personalization memory it's the pragmatic choice. For agents that need to reason about how facts changed over time, Graphiti is the better pick.

It has 55k stars on GitHub.

Star Mem0 ⭐️

### Alternatives

* Graphiti- Zep's temporal knowledge-graph engine. Stores facts with validity windows -- not just what happened, but when and whether it's still true.
* Letta (formerly MemGPT)- Memory built into the system prompt at runtime. The agent itself decides what to keep - not retrieved after the fact, baked into how it reasons.
* Supermemory- Cross-agent memory API with plugins for OpenCode, OpenClaw, and Claude Code. Say "remember that this project uses Bun" and it saves. Context shows up automatically next session.
* Cognee- Deterministic knowledge-graph memory pipelines. Pick for structured memory over large corpora.

## 16. Testing & Evaluation - DeepEval

Most teams skip evals entirely until something breaks in production. By then, you're debugging blind - no idea if it's the prompt, the retrieval, the model, or all three.

DeepEvalbrings eval into your test suite. Write assertions the way you write unit tests, run them in CI, and catch regressions before they ship.

50+ metrics covering RAG, agents, tool-use, multi-turn conversations, and safety. The agent-specific ones are the most useful: task completion, argument correctness, tool correctness, step efficiency. Also generates synthetic datasets for edge cases that are hard to collect manually.

It has 15.6k stars on GitHub.

Star DeepEval ⭐️

### Alternatives

* promptfoo- CLI-first eval and red-teaming in one tool. Pick when adversarial testing matters as much as accuracy metrics.
* Phoenix- OTel-native tracing + evals from Arize AI. Auto-instruments LangChain, LlamaIndex, Mastra, Vercel AI SDK. Pick when you're already on OTel and want tracing and evals in one tool.
* Opik- Comet's open eval and tracing platform. Pick when you want evals and observability together.
* MLflow- Now has full LLM and agent eval features alongside the ML lifecycle tools. Pick when your team already runs MLflow for traditional ML.
* garak- NVIDIA's LLM vulnerability scanner. Probes your agent for weaknesses before someone else does.
* AI-Infra-Guard- Tencent's red teaming platform. Scans MCP servers, agent skills, and AI infrastructure. Pick when you want to find vulnerabilities before deploying.

## 17. Monitoring & Observability - Langfuse

Most teams find out their agent is broken when a user reports it. By then, you're debugging a black box - no trace of what the agent did, in what order, or where it went wrong.

Langfuseis the de facto open-source LLM observability stack. Traces, evals, prompt versioning, and cost tracking in one self-hostable package.

The trace shows exactly what the agent did, at what latency, with what cost. Debugging multi-step agents becomes a lot easier.

It has 27.6k stars on GitHub.

Star Langfuse ⭐️

### Alternatives

* Opik- Comet's tracing, evals, and dashboards. Pick for the Langfuse-equivalent with Comet's ML lineage behind it.
* TensorZero- Gateway, observability, and optimization unified in one tool. Pick when you want one box instead of three.
* Logfire- OTel-native LLM observability from the Pydantic team. Pick the tightest fit with Python and Pydantic-AI agents.
* OpenLLMetry- OTel instrumentation library for LLM apps. Pick when you want agent traces feeding into an existing Grafana or Datadog backend.

## A brief note on agent protocols

Three protocols run the modern agent stack. Worth knowing the difference:

* MCP (Model Context Protocol)- agent to tools. Anthropic's standard, now under the Linux Foundation, adopted by OpenAI, Google, and Microsoft.GitHub
* A2A (Agent-to-Agent)- agent to agent. Google's protocol for inter-agent communication.GitHub
* AG-UI- agent to user. The open event protocol for agent-user interaction originated by CopilotKit and is now adopted by Google, AWS, Microsoft, LangChain, and Mastra.GitHub

## Extra Resources

1)12-Factor Agents- Dex Horthy's principles for shipping LLM software that actually works in production. The core insight: most successful AI products aren't autonomous agents -- they're mostly deterministic code with LLM steps placed at exactly the right points. One of my favorite repos in open source.

2)Generative Agents- The Stanford simulacra paper code. 25 agents in a Sims-like sandbox that wake up, form relationships, plan their days, and remember past interactions. The canonical reference for how memory, reflection, and planning work in multi-agent simulations.

3)AI Agents for Beginners (Microsoft)- 12-lesson structured course from Microsoft. Pick this if you want a guided path rather than piecing it together yourself.

4)HuggingFace Agents Course- Stronger on the model and tool-use fundamentals. Better for ML practitioners coming into agents from the model side.

5)Roadmap.sh AI Agents- Visual map of everything you need to know to build agents in 2026. Good starting point if you want to see the full picture before diving in.

Whew! This took a really long time to write, but I enjoyed every bit of it.

This list is based on my opinions and what I've actually seen get adopted in the open source community. If I missed something you think deserves a spot, drop it in the comments.

And on that note, here's what multi-agent collaboration actually looks like in 2026 😅

Have a great day! Until next time :)

Connect with me onGitHub,TwitterandLinkedIn.

thanks for reading!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse