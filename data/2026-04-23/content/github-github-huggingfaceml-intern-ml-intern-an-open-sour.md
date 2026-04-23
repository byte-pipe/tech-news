---
title: 'GitHub - huggingface/ml-intern: 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models · GitHub'
url: https://github.com/huggingface/ml-intern
site_name: github
content_file: github-github-huggingfaceml-intern-ml-intern-an-open-sour
fetched_at: '2026-04-23T20:05:53.057951'
original_url: https://github.com/huggingface/ml-intern
author: huggingface
description: '🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models - huggingface/ml-intern'
---

huggingface

 

/

ml-intern

Public

* NotificationsYou must be signed in to change notification settings
* Fork259
* Star2.9k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

370 Commits
370 Commits
agent
agent
 
 
backend
backend
 
 
configs
configs
 
 
frontend
frontend
 
 
tests/
unit
tests/
unit
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
Dockerfile
Dockerfile
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# ML Intern

An ML intern that autonomously researches, writes, and ships good quality ML releated code using the Hugging Face ecosystem — with deep access to docs, papers, datasets, and cloud compute.

## Quick Start

### Installation

git clone git@github.com:huggingface/ml-intern.git

cd
 ml-intern
uv sync
uv tool install -e 
.

#### That's it. Nowml-internworks from any directory:

ml-intern

Create a.envfile in the project root (or export these in your shell):

ANTHROPIC_API_KEY=
<
your-anthropic-api-key
>
 
#
 if using anthropic models

HF_TOKEN=
<
your-hugging-face-token
>

GITHUB_TOKEN=
<
github-personal-access-token
>
 

If noHF_TOKENis set, the CLI will prompt you to paste one on first launch. To get a GITHUB_TOKEN follow the tutorialhere.

### Usage

Interactive mode(start a chat session):

ml-intern

Headless mode(single prompt, auto-approve):

ml-intern 
"
fine-tune llama on my dataset
"

Options:

ml-intern --model anthropic/claude-opus-4-6 
"
your prompt
"

ml-intern --max-iterations 100 
"
your prompt
"

ml-intern --no-stream 
"
your prompt
"

## Architecture

### Component Overview

┌─────────────────────────────────────────────────────────────┐
│ User/CLI │
└────────────┬─────────────────────────────────────┬──────────┘
 │ Operations │ Events
 ↓ (user_input, exec_approval, ↑
 submission_queue interrupt, compact, ...) event_queue
 │ │
 ↓ │
┌────────────────────────────────────────────────────┐ │
│ submission_loop (agent_loop.py) │ │
│ ┌──────────────────────────────────────────────┐ │ │
│ │ 1. Receive Operation from queue │ │ │
│ │ 2. Route to handler (run_agent/compact/...) │ │ │
│ └──────────────────────────────────────────────┘ │ │
│ ↓ │ │
│ ┌──────────────────────────────────────────────┐ │ │
│ │ Handlers.run_agent() │ ├──┤
│ │ │ │ │
│ │ ┌────────────────────────────────────────┐ │ │ │
│ │ │ Agentic Loop (max 300 iterations) │ │ │ │
│ │ │ │ │ │ │
│ │ │ ┌──────────────────────────────────┐ │ │ │ │
│ │ │ │ Session │ │ │ │ │
│ │ │ │ ┌────────────────────────────┐ │ │ │ │ │
│ │ │ │ │ ContextManager │ │ │ │ │ │
│ │ │ │ │ • Message history │ │ │ │ │ │
│ │ │ │ │ (litellm.Message[]) │ │ │ │ │ │
│ │ │ │ │ • Auto-compaction (170k) │ │ │ │ │ │
│ │ │ │ │ • Session upload to HF │ │ │ │ │ │
│ │ │ │ └────────────────────────────┘ │ │ │ │ │
│ │ │ │ │ │ │ │ │
│ │ │ │ ┌────────────────────────────┐ │ │ │ │ │
│ │ │ │ │ ToolRouter │ │ │ │ │ │
│ │ │ │ │ ├─ HF docs & research │ │ │ │ │ │
│ │ │ │ │ ├─ HF repos, datasets, │ │ │ │ │ │
│ │ │ │ │ │ jobs, papers │ │ │ │ │ │
│ │ │ │ │ ├─ GitHub code search │ │ │ │ │ │
│ │ │ │ │ ├─ Sandbox & local tools │ │ │ │ │ │
│ │ │ │ │ ├─ Planning │ │ │ │ │ │
│ │ │ │ │ └─ MCP server tools │ │ │ │ │ │
│ │ │ │ └────────────────────────────┘ │ │ │ │ │
│ │ │ └──────────────────────────────────┘ │ │ │ │
│ │ │ │ │ │ │
│ │ │ ┌──────────────────────────────────┐ │ │ │ │
│ │ │ │ Doom Loop Detector │ │ │ │ │
│ │ │ │ • Detects repeated tool patterns │ │ │ │ │
│ │ │ │ • Injects corrective prompts │ │ │ │ │
│ │ │ └──────────────────────────────────┘ │ │ │ │
│ │ │ │ │ │ │
│ │ │ Loop: │ │ │ │
│ │ │ 1. LLM call (litellm.acompletion) │ │ │ │
│ │ │ ↓ │ │ │ │
│ │ │ 2. Parse tool_calls[] │ │ │ │
│ │ │ ↓ │ │ │ │
│ │ │ 3. Approval check │ │ │ │
│ │ │ (jobs, sandbox, destructive ops) │ │ │ │
│ │ │ ↓ │ │ │ │
│ │ │ 4. Execute via ToolRouter │ │ │ │
│ │ │ ↓ │ │ │ │
│ │ │ 5. Add results to ContextManager │ │ │ │
│ │ │ ↓ │ │ │ │
│ │ │ 6. Repeat if tool_calls exist │ │ │ │
│ │ └────────────────────────────────────────┘ │ │ │
│ └──────────────────────────────────────────────┘ │ │
└────────────────────────────────────────────────────┴──┘

### Agentic Loop Flow

User Message
 ↓
[Add to ContextManager]
 ↓
 ╔═══════════════════════════════════════════╗
 ║ Iteration Loop (max 300) ║
 ║ ║
 ║ Get messages + tool specs ║
 ║ ↓ ║
 ║ litellm.acompletion() ║
 ║ ↓ ║
 ║ Has tool_calls? ──No──> Done ║
 ║ │ ║
 ║ Yes ║
 ║ ↓ ║
 ║ Add assistant msg (with tool_calls) ║
 ║ ↓ ║
 ║ Doom loop check ║
 ║ ↓ ║
 ║ For each tool_call: ║
 ║ • Needs approval? ──Yes──> Wait for ║
 ║ │ user confirm ║
 ║ No ║
 ║ ↓ ║
 ║ • ToolRouter.execute_tool() ║
 ║ • Add result to ContextManager ║
 ║ ↓ ║
 ║ Continue loop ─────────────────┐ ║
 ║ ↑ │ ║
 ║ └───────────────────────┘ ║
 ╚═══════════════════════════════════════════╝

## Events

The agent emits the following events viaevent_queue:

* processing- Starting to process user input
* ready- Agent is ready for input
* assistant_chunk- Streaming token chunk
* assistant_message- Complete LLM response text
* assistant_stream_end- Token stream finished
* tool_call- Tool being called with arguments
* tool_output- Tool execution result
* tool_log- Informational tool log message
* tool_state_change- Tool execution state transition
* approval_required- Requesting user approval for sensitive operations
* turn_complete- Agent finished processing
* error- Error occurred during processing
* interrupted- Agent was interrupted
* compacted- Context was compacted
* undo_complete- Undo operation completed
* shutdown- Agent shutting down

## Development

### Adding Built-in Tools

Editagent/core/tools.py:

def
 
create_builtin_tools
() 
->
 
list
[
ToolSpec
]:
 
return
 [
 
ToolSpec
(
 
name
=
"your_tool"
,
 
description
=
"What your tool does"
,
 
parameters
=
{
 
"type"
: 
"object"
,
 
"properties"
: {
 
"param"
: {
"type"
: 
"string"
, 
"description"
: 
"Parameter description"
}
 },
 
"required"
: [
"param"
]
 },
 
handler
=
your_async_handler

 ),
 
# ... existing tools

 ]

### Adding MCP Servers

Editconfigs/main_agent_config.json:

{
 
"model_name"
: 
"
anthropic/claude-sonnet-4-5-20250929
"
,
 
"mcpServers"
: {
 
"your-server-name"
: {
 
"transport"
: 
"
http
"
,
 
"url"
: 
"
https://example.com/mcp
"
,
 
"headers"
: {
 
"Authorization"
: 
"
Bearer ${YOUR_TOKEN}
"

 }
 }
 }
}

Note: Environment variables like${YOUR_TOKEN}are auto-substituted from.env.

## About

🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.9k

 stars
 

### Watchers

20

 watching
 

### Forks

259

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python70.1%
* TypeScript29.5%
* Other0.4%