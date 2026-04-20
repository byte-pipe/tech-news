---
title: 'GitHub - langflow-ai/openrag: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch. · GitHub'
url: https://github.com/langflow-ai/openrag
site_name: github
content_file: github-github-langflow-aiopenrag-openrag-is-a-comprehensi
fetched_at: '2026-03-13T03:12:38.763576'
original_url: https://github.com/langflow-ai/openrag
author: langflow-ai
description: 'OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch. - GitHub - langflow-ai/openrag: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.'
---

langflow-ai



/

openrag

Public

* NotificationsYou must be signed in to change notification settings
* Fork116
* Star1.3k




 
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

3,220 Commits
3,220 Commits
.github
.github
 
 
docs
docs
 
 
flows
flows
 
 
frontend
frontend
 
 
keys
keys
 
 
kubernetes/
helm/
openrag
kubernetes/
helm/
openrag
 
 
openrag-documents
openrag-documents
 
 
scripts
scripts
 
 
sdks
sdks
 
 
securityconfig
securityconfig
 
 
src
src
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
.secrets.baseline
.secrets.baseline
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.backend
Dockerfile.backend
 
 
Dockerfile.frontend
Dockerfile.frontend
 
 
Dockerfile.langflow
Dockerfile.langflow
 
 
Dockerfile.langflow.dev
Dockerfile.langflow.dev
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.gpu.yml
docker-compose.gpu.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
patch-netty.sh
patch-netty.sh
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
warm_up_docling.py
warm_up_docling.py
 
 
View all files

## Repository files navigation

# OpenRAG

### Intelligent Agent-powered document search



OpenRAG is a comprehensive Retrieval-Augmented Generation platform that enables intelligent document search and AI-powered conversations.

Users can upload, process, and query documents through a chat interface backed by large language models and semantic search capabilities. The system utilizes Langflow for document ingestion, retrieval workflows, and intelligent nudges, providing a seamless RAG experience.

Check out thedocumentationor get started with thequickstart.

Built withFastAPIandNext.js.
Powered byOpenSearch,Langflow, andDocling.

## ✨ Highlight Features

* Pre-packaged & ready to run- All core tools are hooked up and ready to go, just install and run
* Agentic RAG workflows- Advanced orchestration with re-ranking and multi-agent coordination
* Document ingestion- Handles messy, real-world data with intelligent parsing
* Drag-and-drop workflow builder- Visual interface powered by Langflow for rapid iteration
* Modular enterprise add-ons- Extend functionality when you need it
* Enterprise search at any scale- Powered by OpenSearch for production-grade performance

## 🔄 How OpenRAG Works

OpenRAG follows a streamlined workflow to transform your documents into intelligent, searchable knowledge:

## 🚀 Install OpenRAG

To get started with OpenRAG, see the installation guides in the OpenRAG documentation:

* Quickstart
* Install the OpenRAG Python package
* Deploy self-managed services with Docker or Podman

## ✨ Quick Start Workflow

1. Launch OpenRAG

↓

2. Add Knowledge

↓

3. Start Chatting

## 📦 SDKs

Integrate OpenRAG into your applications with our official SDKs:

### Python SDK

pip install openrag-sdk

Quick Example:

import

asyncio

from

openrag_sdk

import

OpenRAGClient

async

def

main
():

async

with

OpenRAGClient
()
as

client
:

response

=

await

client
.
chat
.
create
(
message
=
"What is RAG?"
)

print
(
response
.
response
)

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

📖Full Python SDK Documentation

### TypeScript/JavaScript SDK

npm install openrag-sdk

Quick Example:

import

{

OpenRAGClient

}

from

"openrag-sdk"
;

const

client

=

new

OpenRAGClient
(
)
;

const

response

=

await

client
.
chat
.
create
(
{

message
:
"What is RAG?"

}
)
;

console
.
log
(
response
.
response
)
;

📖Full TypeScript/JavaScript SDK Documentation

## 🔌 Model Context Protocol (MCP)

Connect AI assistants like Cursor and Claude Desktop to your OpenRAG knowledge base:

pip install openrag-mcp

Quick Example (Cursor/Claude Desktop config):

{

"mcpServers"
: {

"openrag"
: {

"command"
:
"
uvx
"
,

"args"
: [
"
openrag-mcp
"
],

"env"
: {

"OPENRAG_URL"
:
"
http://localhost:3000
"
,

"OPENRAG_API_KEY"
:
"
your_api_key_here
"

 }
 }
 }
}

The MCP server provides tools for RAG-enhanced chat, semantic search, and settings management.

📖Full MCP Documentation

## 🛠️ Development

For developers who want tocontribute to OpenRAGor set up a development environment, seeCONTRIBUTING.md.

## 🛟 Troubleshooting

For assistance with OpenRAG, seeTroubleshoot OpenRAGand visit theDiscussions page.

To report a bug or submit a feature request, visit theIssues page.

## About

OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.

www.openr.ag

### Resources

 Readme



### License

 Apache-2.0 license


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

1.3k

 stars


### Watchers

11

 watching


### Forks

116

 forks


 Report repository



## Releases51

Release 0.3.0

 Latest



Mar 11, 2026



+ 50 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python62.1%
* TypeScript34.7%
* Makefile1.8%
* Shell0.5%
* CSS0.4%
* Dockerfile0.3%
* Other0.2%
