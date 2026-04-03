---
title: 'GitHub - agentscope-ai/ReMe: ReMe: Memory Management Kit for Agents - Remember Me, Refine Me. · GitHub'
url: https://github.com/agentscope-ai/ReMe
site_name: github
content_file: github-github-agentscope-aireme-reme-memory-management-ki
fetched_at: '2026-03-03T19:19:40.677363'
original_url: https://github.com/agentscope-ai/ReMe
author: agentscope-ai
description: 'ReMe: Memory Management Kit for Agents - Remember Me, Refine Me. - agentscope-ai/ReMe'
---

agentscope-ai

 

/

ReMe

Public

* NotificationsYou must be signed in to change notification settings
* Fork114
* Star1.2k

 
 
 
 
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

737 Commits
737 Commits
.github/
workflows
.github/
workflows
 
 
benchmark
benchmark
 
 
cookbook
cookbook
 
 
docs
docs
 
 
reme
reme
 
 
reme_ai
reme_ai
 
 
test
test
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_ZH.md
README_ZH.md
 
 
example.env
example.env
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

A memory management toolkit for AI agents — Remember Me, Refine Me.

For legacy versions, see0.2.x Documentation

🧠 ReMe is amemory management frameworkbuilt forAI agents, offering bothfile-basedandvector-basedmemory systems.

It addresses two core problems of agent memory:limited context windows(early information gets truncated or lost
during
long conversations) andstateless sessions(new conversations cannot inherit history and always start from scratch).

ReMe gives agentsreal memory— old conversations are automatically condensed, important information is persisted,
and the next conversation can recall it automatically.

## 📁 File-Based ReMe

Memory as files, files as memory

Treatmemory as files— readable, editable, and portable.

Traditional Memory Systems

File-Based ReMe

🗄️ Database storage

📝 Markdown files

🔒 Opaque

👀 Read anytime

❌ Hard to modify

✏️ Edit directly

🚫 Hard to migrate

📦 Copy to migrate

.reme/
├── MEMORY.md # Long-term memory: user preferences, project config, etc.
└── memory/
 └── YYYY-MM-DD.md # Daily logs: work records for the day, written upon compact

### Core Capabilities

ReMe File Basedis the core class of the file-based memory system. It acts like anintelligent
secretary, managing all memory-related operations:

Method

Function

Key Components

start

🚀 Start memory system

BaseFileStore
 (local file storage)
BaseFileWatcher
 (file watcher)
BaseEmbeddingModel
 (embedding cache)

close

📕 Close and save

Close file store, stop file watcher, save embedding cache

context_check

📏 Check context limit

ContextChecker

compact

📦 Compact history to summary

Compactor

summary

📝 Write important memory to files

Summarizer

memory_search

🔍 Semantic memory search

MemorySearch

memory_get

📖 Read specified memory file

MemoryGet

## 🗃️ Vector-Based ReMe

ReMe Vector Basedis the core class for the vector-based memory system, supporting unified management of
three memory types:

Memory Type

Purpose

Usage Context

Personal memory

User preferences, habits

user_name

Task / procedural memory

Task execution experience, success/failure patterns

task_name

Tool memory

Tool usage experience, parameter tuning

tool_name

### Core Capabilities

Method

Function

Description

summarize_memory

🧠 Summarize memory

Automatically extract and store memory from conversations

retrieve_memory

🔍 Retrieve memory

Retrieve relevant memory by query

add_memory

➕ Add memory

Manually add memory to vector store

get_memory

📖 Get memory

Fetch a single memory by ID

update_memory

✏️ Update memory

Update content or metadata of existing memory

delete_memory

🗑️ Delete memory

Delete specified memory

list_memory

📋 List memory

List memories with filtering and sorting

## 💻 ReMeCli: Terminal Assistant with File-Based Memory

马
上
有
钱

remecli_en_1080p_3x.mp4

马
到
成
功

### When Is Memory Written?

Scenario

Written to

Trigger

Auto-compact when context is too long

memory/YYYY-MM-DD.md

Automatic in background

User runs 
/compact

memory/YYYY-MM-DD.md

Manual compact + background save

User runs 
/new

memory/YYYY-MM-DD.md

New conversation + background save

User says "remember this"

MEMORY.md
 or log

Agent writes via 
write
 tool

Agent finds important decisions/preferences

MEMORY.md

Agent writes proactively

### Memory Retrieval Tools

Method

Tool

When to use

Example

Semantic search

memory_search

Unsure where it is, fuzzy lookup

"Earlier discussion about deployment"

Direct read

read

Know the date or file

Read 
memory/2025-02-13.md

Search usesvector + BM25 hybrid retrieval(vector weight 0.7, BM25 weight 0.3), so queries using both natural
language and exact
keywords can match.

### Built-in Tools

Tool

Function

Details

memory_search

Search memory

Vector + BM25 hybrid search over MEMORY.md and memory/*.md

bash

Run commands

Execute bash commands with timeout and output truncation

ls

List directory

Show directory structure

read

Read file

Text and images supported, with segmented reading

edit

Edit file

Replace after exact text match

write

Write file

Create or overwrite, auto-create directories

execute_code

Run Python

Execute code snippets

web_search

Web search

Search via Tavily

## 🚀 Quick Start

### Installation

pip install -U reme-ai

### Environment Variables

API keys are set via environment variables; you can put them in a.envfile in the project root:

Variable

Description

Example

REME_LLM_API_KEY

LLM API key

sk-xxx

REME_LLM_BASE_URL

LLM base URL

https://dashscope.aliyuncs.com/compatible-mode/v1

REME_EMBEDDING_API_KEY

Embedding API key

sk-xxx

REME_EMBEDDING_BASE_URL

Embedding base URL

https://dashscope.aliyuncs.com/compatible-mode/v1

TAVILY_API_KEY

Tavily search API key (optional)

tvly-xxx

### Using ReMeCli

#### Start ReMeCli

remecli config=cli

#### ReMeCli System Commands

Year of the Horse easter egg:/horse— fireworks, galloping animation, and random horse-year blessings.

Commands starting with/control session state:

Command

Description

Waits for response

/compact

Manually compact current conversation and save to long-term memory

Yes

/new

Start new conversation; history saved to long-term memory

No

/clear

Clear everything, 
without saving

No

/history

View uncompressed messages in current conversation

No

/help

Show command list

No

/exit

Exit

No

Difference between the three commands

Command

Compact summary

Long-term memory

Message history

/compact

New summary

Saved

Keep recent

/new

Cleared

Saved

Cleared

/clear

Cleared

Not saved

Cleared

/clearpermanently deletes; nothing is persisted anywhere.

### Using the ReMe Package

#### File-Based ReMe

import
 
asyncio

from
 
reme
 
import
 
ReMeFb

async
 
def
 
main
():
 
# Initialize and start

 
reme
 
=
 
ReMeFb
(
 
default_llm_config
=
{
 
"backend"
: 
"openai"
, 
# Backend type, OpenAI-compatible API

 
"model_name"
: 
"qwen3.5-plus"
, 
# Model name

 },
 
default_file_store_config
=
{
 
"backend"
: 
"chroma"
, 
# Store backend: sqlite/chroma/local

 
"fts_enabled"
: 
True
, 
# Enable full-text search

 
"vector_enabled"
: 
False
, 
# Enable vector search (set False if no embedding service)

 },
 
context_window_tokens
=
128000
, 
# Model context window size (tokens)

 
reserve_tokens
=
36000
, 
# Tokens reserved for output

 
keep_recent_tokens
=
20000
, 
# Tokens to keep for recent messages

 
vector_weight
=
0.7
, 
# Vector search weight (0–1) for hybrid search

 
candidate_multiplier
=
3.0
, 
# Candidate multiplier for recall

 )
 
await
 
reme
.
start
()

 
messages
 
=
 [
 {
"role"
: 
"user"
, 
"content"
: 
"I prefer Python 3.12"
},
 {
"role"
: 
"assistant"
, 
"content"
: 
"Noted, you prefer Python 3.12"
},
 ]

 
# Check if context exceeds limit

 
result
 
=
 
await
 
reme
.
context_check
(
messages
)
 
print
(
f"Compact result: 
{
result
}
"
)

 
# Compact conversation to summary

 
summary
 
=
 
await
 
reme
.
compact
(
messages_to_summarize
=
messages
)
 
print
(
f"Summary: 
{
summary
}
"
)

 
# Write important memory to files (ReAct Agent does this automatically)

 
await
 
reme
.
summary
(
messages
=
messages
, 
date
=
"2026-02-28"
)

 
# Semantic search over memory

 
results
 
=
 
await
 
reme
.
memory_search
(
query
=
"Python version preference"
, 
max_results
=
5
)
 
print
(
f"Search results: 
{
results
}
"
)

 
# Read specified memory file

 
content
 
=
 
await
 
reme
.
memory_get
(
path
=
"MEMORY.md"
)
 
print
(
f"Memory content: 
{
content
}
"
)

 
# Close (save embedding cache, stop file watcher)

 
await
 
reme
.
close
()

if
 
__name__
 
==
 
"__main__"
:
 
asyncio
.
run
(
main
())

#### Vector-Based ReMe

import
 
asyncio

from
 
reme
 
import
 
ReMe

async
 
def
 
main
():
 
# Initialize ReMe

 
reme
 
=
 
ReMe
(
 
working_dir
=
".reme"
,
 
default_llm_config
=
{
 
"backend"
: 
"openai"
,
 
"model_name"
: 
"qwen3-30b-a3b-thinking-2507"
,
 },
 
default_embedding_model_config
=
{
 
"backend"
: 
"openai"
,
 
"model_name"
: 
"text-embedding-v4"
,
 
"dimensions"
: 
1024
,
 },
 
default_vector_store_config
=
{
 
"backend"
: 
"local"
, 
# Supports local/chroma/qdrant/elasticsearch

 },
 )
 
await
 
reme
.
start
()

 
messages
 
=
 [
 {
"role"
: 
"user"
, 
"content"
: 
"Help me write a Python script"
, 
"time_created"
: 
"2026-02-28 10:00:00"
},
 {
"role"
: 
"assistant"
, 
"content"
: 
"Sure, I'll help you write it"
, 
"time_created"
: 
"2026-02-28 10:00:05"
},
 ]

 
# 1. Summarize memory from conversation (auto-extract user preferences, task experience, etc.)

 
result
 
=
 
await
 
reme
.
summarize_memory
(
 
messages
=
messages
,
 
user_name
=
"alice"
, 
# Personal memory

 
# task_name="code_writing", # Task memory

 )
 
print
(
f"Summarize result: 
{
result
}
"
)

 
# 2. Retrieve relevant memory

 
memories
 
=
 
await
 
reme
.
retrieve_memory
(
 
query
=
"Python programming"
,
 
# user_name="alice",

 )
 
print
(
f"Retrieve result: 
{
memories
}
"
)

 
# 3. Manually add memory

 
memory_node
 
=
 
await
 
reme
.
add_memory
(
 
memory_content
=
"User prefers concise code style"
,
 
user_name
=
"alice"
,
 )
 
print
(
f"Added memory: 
{
memory_node
}
"
)
 
memory_id
 
=
 
memory_node
.
memory_id

 
# 4. Get single memory by ID

 
fetched_memory
 
=
 
await
 
reme
.
get_memory
(
memory_id
=
memory_id
)
 
print
(
f"Fetched memory: 
{
fetched_memory
}
"
)

 
# 5. Update memory content

 
updated_memory
 
=
 
await
 
reme
.
update_memory
(
 
memory_id
=
memory_id
,
 
user_name
=
"alice"
,
 
memory_content
=
"User prefers concise, well-commented code style"
,
 )
 
print
(
f"Updated memory: 
{
updated_memory
}
"
)

 
# 6. List all memories for user (with filtering and sorting)

 
all_memories
 
=
 
await
 
reme
.
list_memory
(
 
user_name
=
"alice"
,
 
limit
=
10
,
 
sort_key
=
"time_created"
,
 
reverse
=
True
,
 )
 
print
(
f"User memory list: 
{
all_memories
}
"
)

 
# 7. Delete specified memory

 
await
 
reme
.
delete_memory
(
memory_id
=
memory_id
)
 
print
(
f"Deleted memory: 
{
memory_id
}
"
)

 
# 8. Delete all memories (use with caution)

 
# await reme.delete_all()

 
await
 
reme
.
close
()

if
 
__name__
 
==
 
"__main__"
:
 
asyncio
.
run
(
main
())

## 🏛️ Technical Architecture

### File-Based ReMe Core Architecture

graph TB
 User[User / Agent] --> ReMeFb[File based ReMe]
 ReMeFb --> ContextCheck[Context Check]
 ReMeFb --> Compact[Context Compact]
 ReMeFb --> Summary[Memory Summary]
 ReMeFb --> Search[Memory Retrieval]
 ContextCheck --> FbContextChecker[Check Token Limit]
 Compact --> FbCompactor[Compact History to Summary]
 Summary --> FbSummarizer[ReAct Agent + File Tools]
 Search --> MemorySearch[Vector + BM25 Hybrid Search]
 FbSummarizer --> FileTools[read / write / edit]
 FileTools --> MemoryFiles[memory/*.md]
 MemoryFiles -.->|File change| FileWatcher[Async File Watcher]
 FileWatcher -->|Update index| FileStore[Local DB]
 MemorySearch --> FileStore

 
Loading

#### Memory Summary: ReAct + File Tools

Summarizeris the core component for memory summarization. It uses theReAct + file toolspattern.

graph LR
 A[Receive conversation] --> B{Think: What's worth recording?}
 B --> C[Act: read memory/YYYY-MM-DD.md]
 C --> D{Think: How to merge with existing content?}
 D --> E[Act: edit to update file]
 E --> F{Think: Anything missing?}
 F -->|Yes| B
 F -->|No| G[Done]

 
Loading

#### File Tool Set

Summarizer is equipped with file operation tools so the AI can work directly on memory files:

Tool

Function

Use case

read

Read file content

View existing memory, avoid duplicates

write

Overwrite file

Create new memory file or major rewrite

edit

Edit part of file

Append or modify specific sections

#### Context Compaction

When a conversation gets too long,Compactorcompresses history into a concise
summary — likemeeting minutes, turning long discussion into key points.

graph LR
 A[Messages 1..N] --> B[📦 Compact summary]
C[Recent messages] --> D[Keep as-is]
B --> E[New context]
D --> E

 
Loading

The compact summary includes what’s needed to continue:

Content

Description

🎯 Goals

What the user wants to accomplish

⚙️ Constraints

Requirements and preferences mentioned

📈 Progress

Completed / in progress / blocked tasks

🔑 Decisions

Decisions made and reasons

📌 Context

Key data such as file paths, function names

#### Memory Retrieval

MemorySearchprovidesvector + BM25 hybrid retrieval. The two methods
complement each other:

Retrieval

Strength

Weakness

Vector semantic

Captures similar meaning with different wording

Weaker on exact token match

BM25 full-text

Strong exact token match

No synonym or paraphrase understanding

Fusion: Both retrieval paths are used; results are combined by weighted sum (vector 0.7 + BM25 0.3), so both
natural-language queries and exact lookups get reliable results.

graph LR
 Q[Search query] --> V[Vector search × 0.7]
Q --> B[BM25 × 0.3]
V --> M[Dedupe + weighted merge]
B --> M
M --> R[Top-N results]

 
Loading

### Vector-Based ReMe Core Architecture

graph TB
 User[User / Agent] --> ReMe[Vector Based ReMe]
 ReMe --> Summarize[Memory Summarize]
 ReMe --> Retrieve[Memory Retrieve]
 ReMe --> CRUD[CRUD]
 Summarize --> PersonalSum[PersonalSummarizer]
 Summarize --> ProceduralSum[ProceduralSummarizer]
 Summarize --> ToolSum[ToolSummarizer]
 Retrieve --> PersonalRet[PersonalRetriever]
 Retrieve --> ProceduralRet[ProceduralRetriever]
 Retrieve --> ToolRet[ToolRetriever]
 PersonalSum --> VectorStore[Vector DB]
 ProceduralSum --> VectorStore
 ToolSum --> VectorStore
 PersonalRet --> VectorStore
 ProceduralRet --> VectorStore
 ToolRet --> VectorStore

 
Loading

## ⭐ Community & Support

* Star & Watch: Star helps more agent developers discover ReMe; Watch keeps you updated on new releases and
features.
* Share your work: In Issues or Discussions, share what ReMe unlocks for your agents — we’re happy to highlight
great community examples.
* Need a new feature?Open a Feature Request; we’ll iterate with the community.
* Code contributions: All forms of code contribution are welcome. See
theContribution Guide.
* Acknowledgments: Thanks to OpenClaw, Mem0, MemU, CoPaw, and other open-source projects for inspiration and
support.

## 📄 Citation

@software
{
AgentscopeReMe2025
,
 
title
 = 
{
AgentscopeReMe: Memory Management Kit for Agents
}
,
 
author
 = 
{
ReMe Team
}
,
 
url
 = 
{
https://reme.agentscope.io
}
,
 
year
 = 
{
2025
}

}

## ⚖️ License

This project is open source under the Apache License 2.0. See theLICENSEfile for details.

## 📈 Star History

## About

ReMe: Memory Management Kit for Agents - Remember Me, Refine Me.

reme.agentscope.io

### Topics

 agent

 memory

 ai-agents

 rag

 reme

 memoryscope

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.2k

 stars
 

### Watchers

11

 watching
 

### Forks

114

 forks
 

 Report repository

 

## Releases34

v0.3.0.2: Update Halumemeval and Longmemeval ; Update Version 0.3.0.2 (#132)

 Latest

 

Mar 3, 2026

 

+ 33 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors8

## Languages

* Python100.0%