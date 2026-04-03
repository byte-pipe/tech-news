---
title: 'GitHub - vectorize-io/hindsight: Hindsight: Agent Memory That Learns · GitHub'
url: https://github.com/vectorize-io/hindsight
site_name: github
content_file: github-github-vectorize-iohindsight-hindsight-agent-memor
fetched_at: '2026-03-12T11:15:49.850470'
original_url: https://github.com/vectorize-io/hindsight
author: vectorize-io
description: 'Hindsight: Agent Memory That Learns. Contribute to vectorize-io/hindsight development by creating an account on GitHub.'
---

vectorize-io

 

/

hindsight

Public

* NotificationsYou must be signed in to change notification settings
* Fork213
* Star2.8k

 
 
 
 
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

615 Commits
615 Commits
.githooks
.githooks
 
 
.github
.github
 
 
cookbook
cookbook
 
 
docker
docker
 
 
helm/
hindsight
helm/
hindsight
 
 
hindsight-api
hindsight-api
 
 
hindsight-cli
hindsight-cli
 
 
hindsight-clients
hindsight-clients
 
 
hindsight-control-plane
hindsight-control-plane
 
 
hindsight-dev
hindsight-dev
 
 
hindsight-docs
hindsight-docs
 
 
hindsight-embed
hindsight-embed
 
 
hindsight-integration-tests
hindsight-integration-tests
 
 
hindsight-integrations
hindsight-integrations
 
 
hindsight
hindsight
 
 
monitoring/
grafana/
dashboards
monitoring/
grafana/
dashboards
 
 
scripts
scripts
 
 
skills
skills
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
.sesskey
.sesskey
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
hindsight-favicon.png
hindsight-favicon.png
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Documentation•Paper•Cookbook•Hindsight Cloud

## What is Hindsight?

Hindsight™ is an agent memory system built to create smarter agents that learn over time. Most agent memory systems focus on recalling conversation history. Hindsight is focused on making agents that learn, not just remember.

hindsight-learning-demo.mp4

It eliminates the shortcomings of alternative techniques such as RAG and knowledge graph and delivers state-of-the-art performance on long term memory tasks.

## Memory Performance & Accuracy

Hindsight is the most accurate agent memory system ever tested according to benchmark performance. It has achieved state-of-the-art performance on the LongMemEval benchmark, widely used to assess memory system performance across a variety of conversational AI scenarios. The current reported performance of Hindsight and other agent memory solutions as of January 2026 is shown here:

The benchmark performance data for Hindsight has been independently reproduced by research collaborators at the Virginia TechSanghani Center for Artificial Intelligence and Data Analyticsand The Washington Post. Other scores are self-reported by software vendors.

Hindsight is being used in production at Fortune 500 enterprises and by a growing number of AI startups.

## Adding Hindsight to Your AI Agents

The easiest way to use Hindsight with an existing agent is with the LLM Wrapper. You can add memory to your agent with 2 lines of code. That will swap your current LLM client out with the Hindsight wrapper. After that, memories will be stored and retrieved automatically as you make LLM calls.

If you need more control over how and when your agent stores and recalls memories, there's also a simple API you can integrate with using the SDKs or directly via HTTP.

🤖Using a coding agent?Install the Hindsight documentation skill for instant access to docs while you code:

npx skills add https://github.com/vectorize-io/hindsight --skill hindsight-docs

Works with Claude Code, Cursor, and other AI coding assistants.

## Quick Start

### Docker (recommended)

export
 OPENAI_API_KEY=sk-xxx

docker run --rm -it --pull always -p 8888:8888 -p 9999:9999 \
 -e HINDSIGHT_API_LLM_API_KEY=
$OPENAI_API_KEY
 \
 -v 
$HOME
/.hindsight-docker:/home/hindsight/.pg0 \
 ghcr.io/vectorize-io/hindsight:latest

API:http://localhost:8888UI:http://localhost:9999

You can modify the LLM provider by settingHINDSIGHT_API_LLM_PROVIDER. Valid options areopenai,anthropic,gemini,groq,ollama, andlmstudio. The documentation provides more details onsupported models.

### Docker (external PostgreSQL)

export
 OPENAI_API_KEY=sk-xxx

export
 HINDSIGHT_DB_PASSWORD=choose-a-password

cd
 docker/docker-compose
docker compose up 

API:http://localhost:8888UI:http://localhost:9999

### Client

pip install hindsight-client -U

#
 or

npm install @vectorize-io/hindsight-client

#### Python

from
 
hindsight_client
 
import
 
Hindsight

client
 
=
 
Hindsight
(
base_url
=
"http://localhost:8888"
)

# Retain: Store information

client
.
retain
(
bank_id
=
"my-bank"
, 
content
=
"Alice works at Google as a software engineer"
)

# Recall: Search memories

client
.
recall
(
bank_id
=
"my-bank"
, 
query
=
"What does Alice do?"
)

# Reflect: Generate disposition-aware response

client
.
reflect
(
bank_id
=
"my-bank"
, 
query
=
"Tell me about Alice"
)

#### Node.js / TypeScript

npm install @vectorize-io/hindsight-client

const
 
{
 HindsightClient 
}
 
=
 
require
(
'@vectorize-io/hindsight-client'
)
;

const
 
main
 
=
 
async
 
(
)
 
=>
 
{

 
const
 
client
 
=
 
new
 
HindsightClient
(
{
 
baseUrl
: 
'http://localhost:8888'
 
}
)
;

 
await
 
client
.
retain
(
'my-bank'
,
 
'Alice loves hiking in Yosemite'
)
;

 
const
 
results
 
=
 
await
 
client
.
recall
(
'my-bank'
,
 
'What does Alice like?'
)
;

 
console
.
log
(
results
)
;

}

main
(
)
;

### Python Embedded (no server required)

pip install hindsight-all -U

import
 
os

from
 
hindsight
 
import
 
HindsightServer
, 
HindsightClient

with
 
HindsightServer
(
 
llm_provider
=
"openai"
,
 
llm_model
=
"gpt-5-mini"
, 
 
llm_api_key
=
os
.
environ
[
"OPENAI_API_KEY"
]
) 
as
 
server
:
 
client
 
=
 
HindsightClient
(
base_url
=
server
.
url
)
 
client
.
retain
(
bank_id
=
"my-bank"
, 
content
=
"Alice works at Google"
)
 
results
 
=
 
client
.
recall
(
bank_id
=
"my-bank"
, 
query
=
"Where does Alice work?"
)

## Use Cases

Hindsight is built to support conversational AI agents as well as agents that are intended to perform tasks autonomously. The ideal use case for Hindsight are agents that require a blend of these features such as AI employees that need to handle open-ended tasks, change behavior based on user feedback, and learn to perform complex tasks to automate work at a level that approximates a human work. Hindsight can be used with simple AI workflows like those built with n8n and other similar tools, but may be overkill for such applications.

### Per-User Memories and Chat History

One of the simpler use cases you can use Hindsight for is to personalize AI chatbots and other conversational agents by storing and recalling memories associated with individual users.

The requirements for this use case usually look something like this:

per-user-memory.mp4

Satisfying these requirements in Hindsight is straightforward. When new user inputs and tool calls are ingested into Hindsight using the retain operation, custom metadata can be used to enrich the new memories. Metadata provides a convenient way to isolate memories that need to be restricted to a given user. Once these are fed into the retain operation, any raw memories and mental models that get created can be filtered when retrieving relevant memories.

## Architecture & Operations

Most agent memory implementations rely on basic vector search or sometimes use a knowledge graph. Hindsight uses biomimetic data structures to organize agent memories in a way that is more like how human memory works:

* World:Facts about the world ("The stove gets hot")
* Experiences:Agent's own experiences ("I touched the stove and it really hurt")
* Mental Models:Learned understanding of the agent's world formed by reflecting on raw memories and experiences.

Memories in Hindsight are stored in banks (i.e. memory banks). When memories are added to Hindsight, they are pushed into either the world facts or experiences memory pathway. They are then represented as a combination of entities, relationships, and time series with sparse/dense vector representations to aid in later recall.

Hindsight provides three simple methods to interact with the system:

* Retain:Provide information to Hindsight that you want it to remember
* Recall:Retrieve memories from Hindsight
* Reflect:Reflect on memories and experiences to generate new observations and insights from existing memories.

### Retain

Theretainoperation is used to push new memories into Hindsight. It tells Hindsight toretainthe information you pass in as an input.

from
 
hindsight_client
 
import
 
Hindsight

client
 
=
 
Hindsight
(
base_url
=
"http://localhost:8888"
)

# Simple

client
.
retain
(
 
bank_id
=
"my-bank"
,
 
content
=
"Alice works at Google as a software engineer"

)

# With context and timestamp

client
.
retain
(
 
bank_id
=
"my-bank"
,
 
content
=
"Alice got promoted to senior engineer"
,
 
context
=
"career update"
,
 
timestamp
=
"2025-06-15T10:00:00Z"

)

Behind the scenes, the retain operation uses an LLM to extract key facts, temporal data, entities, and relationships. It passes these through a normalization process to transform extracted data into canonical entities, time series, and search indexes along with metadata. These representations create the pathways for accurate memory retrieval in the recall and reflect operations.

### Recall

The recall operation is used to retrieve memories. These memories can come from any of the memory types (world, experiences, etc.)

from
 
hindsight_client
 
import
 
Hindsight

client
 
=
 
Hindsight
(
base_url
=
"http://localhost:8888"
)

# Simple

client
.
recall
(
bank_id
=
"my-bank"
, 
query
=
"What does Alice do?"
)

# Temporal

client
.
recall
(
bank_id
=
"my-bank"
, 
query
=
"What happened in June?"
)

Recall performs 4 retrieval strategies in parallel:

* Semantic: Vector similarity
* Keyword: BM25 exact matching
* Graph: Entity/temporal/causal links
* Temporal: Time range filtering

The individual results from the retrievals are merged, then ordered by relevance using reciprocal rank fusion and a cross-encoder reranking model.

The final output is trimmed as needed to fit within the token limit.

### Reflect

The reflect operation is used to perform a more thorough analysis of existing memories. This allows the agent to form new connections between memories and build a more thorough understanding of its world.

For example, thereflectoperation can be used to support use cases such as:

* AnAI Project Managerreflecting on what risks need to be mitigated on a project.
* ASales Agentreflecting on why certain outreach messages have gotten responses while others haven't.
* ASupport Agentreflecting on opportunities where customers have questions not answered by current product documentation.

Thereflectoperation can also be used to handle on-demand question answering or analysis which require more deep thinking.

from
 
hindsight_client
 
import
 
Hindsight

client
 
=
 
Hindsight
(
base_url
=
"http://localhost:8888"
)

client
.
reflect
(
bank_id
=
"my-bank"
, 
query
=
"What should I know about Alice?"
)

## Resources

Documentation:

* https://hindsight.vectorize.io

Clients:

* Python
* Node.js
* REST API
* CLI

Community:

* Slack
* GitHub Issues

## Star History

## Contributing

SeeCONTRIBUTING.md.

## License

MIT — seeLICENSE

Built byVectorize.io

## About

Hindsight: Agent Memory That Learns

hindsight.vectorize.io/

### Topics

 memory

 agents

 agentic-ai

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.8k

 stars
 

### Watchers

23

 watching
 

### Forks

213

 forks
 

 Report repository

 

## Releases40

v0.4.17

 Latest

 

Mar 10, 2026

 

+ 39 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors28

+ 14 contributors

## Languages

* Python73.4%
* TypeScript15.7%
* Rust3.9%
* MDX3.3%
* Shell1.8%
* CSS0.9%
* Other1.0%