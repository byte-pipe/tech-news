---
title: 'GitHub - topoteretes/cognee: Knowledge Engine for AI Agent Memory in 6 lines of code · GitHub'
url: https://github.com/topoteretes/cognee
site_name: github
content_file: github-github-topoteretescognee-knowledge-engine-for-ai-a
fetched_at: '2026-03-15T11:10:16.798543'
original_url: https://github.com/topoteretes/cognee
author: topoteretes
description: Knowledge Engine for AI Agent Memory in 6 lines of code - topoteretes/cognee
---

topoteretes



/

cognee

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star13.6k




 
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

6,122 Commits
6,122 Commits
.github
.github
 
 
assets
assets
 
 
bin
bin
 
 
cognee-frontend
cognee-frontend
 
 
cognee-mcp
cognee-mcp
 
 
cognee-starter-kit
cognee-starter-kit
 
 
cognee
cognee
 
 
deployment
deployment
 
 
distributed
distributed
 
 
evals
evals
 
 
examples
examples
 
 
licenses
licenses
 
 
logs
logs
 
 
notebooks
notebooks
 
 
tools
tools
 
 
working_dir_error_replication
working_dir_error_replication
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.dockerignore.ci
.dockerignore.ci
 
 
.env.example
.env.example
 
 
.env.template
.env.template
 
 
.gitattributes
.gitattributes
 
 
.gitguardian.yml
.gitguardian.yml
 
 
.gitignore
.gitignore
 
 
.mergify.yml
.mergify.yml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.pylintrc
.pylintrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
DCO.md
DCO.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.ci
Dockerfile.ci
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
README_ko.md
README_ko.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
entrypoint.sh
entrypoint.sh
 
 
mise.toml
mise.toml
 
 
mypy.ini
mypy.ini
 
 
poetry.lock
poetry.lock
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Cognee - Build AI memory with a Knowledge Engine that learns

Demo.Docs.Learn More·Join Discord·Join r/AIMemory.Community Plugins & Add-ons

Use our knowledge engine to build personalized and dynamic memory for AI Agents.

🌐 Available Languages
 :Deutsch|Español|Français|日本語|한국어|Português|Русский|中文

## About Cognee

Cognee is an open-source knowledge engine that lets you ingest data in any format or structure and continuously learns to provide the right context for AI agents. It combines vector search, graph databases and cognitive science approaches to make your documents both searchable by meaning and connected by relationships as they change and evolve.

⭐Help us reach more developers and grow the cognee community. Star this repo!

### Why use Cognee:

* Knowledge infrastructure — unified ingestion, graph/vector search, runs locally, ontology grounding, multimodal
* Persistent and Learning Agents - learn from feedback, context management, cross-agent knowledge sharing
* Reliable and Trustworthy Agents - agentic user/tenant isolation, traceability, OTEL collector, audit traits

## Basic Usage & Feature Guide

To learn more,check out this short, end-to-end Colab walkthroughof Cognee's core features.

## Quickstart

Let’s try Cognee in just a few lines of code. For detailed setup and configuration, see theCognee Docs.

### Prerequisites

* Python 3.10 to 3.13

### Step 1: Install Cognee

You can install Cognee withpip,poetry,uv, or your preferred Python package manager.

uv pip install cognee

### Step 2: Configure the LLM

import

os

os
.
environ
[
"LLM_API_KEY"
]
=

"YOUR OPENAI_API_KEY"

Alternatively, create a.envfile using ourtemplate.

To integrate other LLM providers, see ourLLM Provider Documentation.

### Step 3: Run the Pipeline

Cognee will take your documents, load them into the knowledge angine and search combined vector/graph relationships.

Now, run a minimal pipeline:

import

cognee

import

asyncio

from

pprint

import

pprint

async

def

main
():

# Add text to cognee


await

cognee
.
add
(
"Cognee turns documents into AI memory."
)


# Add to knowledge engine


await

cognee
.
cognify
()


# Query the knowledge graph


results

=

await

cognee
.
search
(
"What does Cognee do?"
)


# Display the results


for

result

in

results
:

pprint
(
result
)

if

__name__

==

'__main__'
:

asyncio
.
run
(
main
())

As you can see, the output is generated from the document we previously stored in Cognee:

 Cognee turns documents into AI memory.

### Use the Cognee CLI

As an alternative, you can get started with these essential commands:

cognee-cli add
"
Cognee turns documents into AI memory.
"

cognee-cli cognify

cognee-cli search
"
What does Cognee do?
"

cognee-cli delete --all

To open the local UI, run:

cognee-cli -ui

## Demos & Examples

See Cognee in action:

### Persistent Agent Memory

## Community & Support

### Contributing

We welcome contributions from the community! Your input helps make Cognee better for everyone. SeeCONTRIBUTING.mdto get started.

### Code of Conduct

We're committed to fostering an inclusive and respectful community. Read ourCode of Conductfor guidelines.

## Research & Citation

We recently published a research paper on optimizing knowledge graphs for LLM reasoning:

@misc
{
markovic2025optimizinginterfaceknowledgegraphs
,

title
=
{
Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning
}
,

author
=
{
Vasilije Markovic and Lazar Obradovic and Laszlo Hajdu and Jovan Pavlovic
}
,

year
=
{
2025
}
,

eprint
=
{
2505.24478
}
,

archivePrefix
=
{
arXiv
}
,

primaryClass
=
{
cs.AI
}
,

url
=
{
https://arxiv.org/abs/2505.24478
}
,
}

## About

Knowledge Engine for AI Agent Memory in 6 lines of code

www.cognee.ai

### Topics

 open-source

 ai

 knowledge

 neo4j

 knowledge-graph

 openai

 help-wanted

 graph-database

 ai-agents

 contributions-welcome

 cognitive-architecture

 good-first-issue

 rag

 good-first-pr

 vector-database

 graph-rag

 ai-memory

 cognitive-memory

 graphrag

 context-engineering

### Resources

 Readme



### License

 Apache-2.0 license


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

13.6k

 stars


### Watchers

57

 watching


### Forks

1.4k

 forks


 Report repository



## Releases85

v0.5.5

 Latest



Mar 14, 2026



+ 84 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python93.4%
* TypeScript6.1%
* Shell0.2%
* Dockerfile0.2%
* CSS0.1%
* Mako0.0%
