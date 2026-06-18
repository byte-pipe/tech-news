---
title: 'GitHub - yifanfeng97/Hyper-Extract: Transform unstructured text into structured knowledge with LLMs. Graphs, hypergraphs, and spatio-temporal extractions — with one command. · GitHub'
url: https://github.com/yifanfeng97/Hyper-Extract
site_name: github
content_file: github-github-yifanfeng97hyper-extract-transform-unstruct
fetched_at: '2026-06-18T19:49:53.249952'
original_url: https://github.com/yifanfeng97/Hyper-Extract
author: yifanfeng97
description: Transform unstructured text into structured knowledge with LLMs. Graphs, hypergraphs, and spatio-temporal extractions — with one command. - yifanfeng97/Hyper-Extract
---

yifanfeng97

 

/

Hyper-Extract

Public

* NotificationsYou must be signed in to change notification settings
* Fork195
* Star1.7k

 
 
 
 
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

278 Commits
278 Commits
.github
.github
 
 
docs
docs
 
 
examples
examples
 
 
hyperextract-skills
hyperextract-skills
 
 
hyperextract
hyperextract
 
 
tests
tests
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_ZH.md
README_ZH.md
 
 
docs_hooks.py
docs_hooks.py
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Smart Knowledge Extraction CLI

Transform documents into structured knowledge with one command.

📖 English Version·中文版

"Stop reading. Start understanding.""告别文档焦虑，让信息一目了然"

Hyper-Extract is an intelligent, LLM-powered knowledge extraction and evolution framework. It radically simplifies transforming highly unstructured texts into persistent, predictable, and strongly-typedKnowledge Abstracts. It effortlessly extracts information into a wide spectrum of formats—ranging from simpleCollections(Lists/Sets) andPydantic Models, to complexKnowledge Graphs,Hypergraphs, and evenSpatio-Temporal Graphs.

## ✨ Core Features

🔷 
8 Knowledge Structures

From simple Lists to advanced Graphs, Hypergraphs, and Spatio-Temporal Graphs

🧠 
10+ Extraction Engines

GraphRAG, LightRAG, Hyper-RAG, KG-Gen, and more — ready to use

📝 
80+ YAML Templates

Zero-code extraction across Finance, Legal, Medical, TCM, Industry, and General domains

🔄 
Incremental Evolution

Feed new documents anytime to expand and refine your knowledge base

## 🎯 What Can You Do With It?

📄 Researcher — Turn papers into knowledge graphs

Feed a 20-page academic paper, get an interactive graph of key concepts, authors, and citations.

he parse paper.pdf -t general/academic_graph -o ./paper_kb/
he show ./paper_kb/

🏦 Financial Analyst — Extract entities from earnings reports

Automatically identify companies, executives, financial metrics, and their relationships from unstructured reports.

he parse earnings.md -t finance/earnings_graph -o ./finance_kb/
he search ./finance_kb/ 
"
What are the key risk factors?
"

🔒 Local Deployment — Keep data on-premise with vLLM

Run Qwen3.5-9B + bge-m3 locally via vLLM. No data leaves your machine.

from
 
hyperextract
 
import
 
create_client

llm
, 
emb
 
=
 
create_client
(
 
llm
=
"vllm:Qwen3.5-9B@http://localhost:8000/v1"
,
 
embedder
=
"vllm:bge-m3@http://localhost:8001/v1"
,
 
api_key
=
"dummy"
,
)

## 🚀 Supported Platforms & Models

Hyper-Extract relies on the LLM's structured output capability (json_schemaor Function Calling).

Platform

Verified Models

OpenAI

gpt-4o, gpt-4o-mini, gpt-5

阿里云百炼

qwen-plus, qwen-turbo, deepseek-r1

Local vLLM

Qwen3.5-9B (GPTQ-Marlin)

Embedding models(semantic search) work with any OpenAI-compatible endpoint:text-embedding-3-small,text-embedding-v4(Bailian),bge-m3(local vLLM).

📖 Full guide:Provider System & Local Model Support

## ⚡ 30-Second Quick Start

#
 Install

uv tool install hyperextract

#
 Configure API key

he config init -k YOUR_OPENAI_API_KEY

#
 Extract knowledge from a document

he parse examples/en/tesla.md -t general/biography_graph -o ./output/ -l en

#
 Query it

he search ./output/ 
"
What are Tesla's major achievements?
"

#
 Visualize

he show ./output/

🐍 Python API
 (click to expand)

uv pip install hyperextract

from
 
hyperextract
 
import
 
Template

ka
 
=
 
Template
.
create
(
"general/biography_graph"
)

with
 
open
(
"examples/en/tesla.md"
) 
as
 
f
:
 
result
 
=
 
ka
.
parse
(
f
.
read
())

result
.
show
()

🔗 More examples:examples/en

## 📈 Why Hyper-Extract?

Feature

GraphRAG

LightRAG

KG-Gen

ATOM

Hyper-Extract

Knowledge Graph

✅

✅

✅

✅

✅

Temporal Graph

✅

❌

❌

✅

✅

Spatial Graph

❌

❌

❌

❌

✅

Hypergraph

❌

❌

❌

❌

✅

Domain Templates

❌

❌

❌

❌

✅

Interactive CLI

✅

❌

❌

❌

✅

Multi-language

✅

❌

❌

❌

✅

## 🧩 Supported Knowledge Structures

From simple to complex — pick the right structure for your data:

Example — AutoGraph visualization:

📋 What's under the hood? (Architecture & Templates)

Hyper-Extract follows athree-layer architecture:

* Auto-Types— 8 strongly-typed data structures (Model, List, Set, Graph, Hypergraph, Temporal Graph, Spatial Graph, Spatio-Temporal Graph)
* Methods— Extraction algorithms: KG-Gen, GraphRAG, LightRAG, Hyper-RAG, Cog-RAG, and more
* Templates— 80+ presets across 6 domains. Zero-code setup.

Template example (Graph type):

language
: 
en

name
: 
Knowledge Graph

type
: 
graph

tags
: 
[general]

description
: 
'
Extract entities and their relationships.
'

output
:
 
entities
:
 
fields
:
 - 
name
: 
name

 
type
: 
str

 - 
name
: 
type

 
type
: 
str

 - 
name
: 
description

 
type
: 
str

 
relations
:
 
fields
:
 - 
name
: 
source

 
type
: 
str

 - 
name
: 
target

 
type
: 
str

 - 
name
: 
type

 
type
: 
str

identifiers
:
 
entity_id
: 
name

 
relation_id
: 
'
{source}|{type}|{target}
'

* Browse all 80+ templates
* Create custom templates

## 📚 Documentation & Resources

Resource

Link

Full Documentation

yifanfeng97.github.io/Hyper-Extract

CLI Guide

Command-line interface

Provider System

Model compatibility & local deployment

Template Gallery

80+ presets

Examples

Working code

## 🤝 Contributing & License

Contributions are welcome! Please submitIssuesandPRs.Licensed underApache-2.0.

## ⭐ Star History

## About

Transform unstructured text into structured knowledge with LLMs. Graphs, hypergraphs, and spatio-temporal extractions — with one command.

yifanfeng97.github.io/Hyper-Extract/

### Topics

 python

 cli

 ai

 knowledge

 information-extraction

 knowledge-graph

 hypergraph

 ai-agents

 rag

 llm

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.7k

 stars
 

### Watchers

12

 watching
 

### Forks

195

 forks
 

 Report repository

 

## Releases3

v0.2.0 - Unified Provider System

 Latest

 

May 18, 2026

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%