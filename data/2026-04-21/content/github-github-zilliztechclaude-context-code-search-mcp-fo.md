---
title: 'GitHub - zilliztech/claude-context: Code search MCP for Claude Code. Make entire codebase the context for any coding agent. · GitHub'
url: https://github.com/zilliztech/claude-context
site_name: github
content_file: github-github-zilliztechclaude-context-code-search-mcp-fo
fetched_at: '2026-04-21T11:59:31.946242'
original_url: https://github.com/zilliztech/claude-context
author: zilliztech
description: Code search MCP for Claude Code. Make entire codebase the context for any coding agent. - zilliztech/claude-context
---

zilliztech

 

/

claude-context

Public

* NotificationsYou must be signed in to change notification settings
* Fork543
* Star6.2k

 
 
 
 
master
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

159 Commits
159 Commits
.github
.github
 
 
.vscode
.vscode
 
 
assets
assets
 
 
docs
docs
 
 
evaluation
evaluation
 
 
examples
examples
 
 
packages
packages
 
 
python
python
 
 
scripts
scripts
 
 
.env.example
.env.example
 
 
.eslintrc.js
.eslintrc.js
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build-benchmark.json
build-benchmark.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

🆕Looking for persistent memory for Claude Code?Check outmemsearch Claude Code plugin— a markdown-first memory system that gives your AI agent long-term memory across sessions.

### Your entire codebase as Claude's context

Claude Contextis an MCP plugin that adds semantic code search to Claude Code and other AI coding agents, giving them deep context from your entire codebase.

🧠Your Entire Codebase as Context: Claude Context uses semantic search to find all relevant code from millions of lines. No multi-round discovery needed. It brings results straight into the Claude's context.

💰Cost-Effective for Large Codebases: Instead of loading entire directories into Claude for every request, which can be very expensive, Claude Context efficiently stores your codebase in a vector database and only uses related code in context to keep your costs manageable.

## 🚀 Demo

Model Context Protocol (MCP) allows you to integrate Claude Context with your favorite AI coding assistants, e.g. Claude Code.

## Quick Start

### Prerequisites

Get a free vector database on Zilliz Cloud 👈

Claude Context needs a vector database. You cansign upon Zilliz Cloud to get an API key.

Copy your Personal Key to replaceyour-zilliz-cloud-api-keyin the configuration examples.

Get OpenAI API Key for embedding model

You need an OpenAI API key for the embedding model. You can get one by signing up atOpenAI.

Your API key will look like this: it always starts withsk-.Copy your key and use it in the configuration examples below asyour-openai-api-key.

### Configure MCP for Claude Code

System Requirements:

* Node.js >= 20.0.0 and < 24.0.0

Claude Context is not compatible with Node.js 24.0.0, you need downgrade it first if your node version is greater or equal to 24.

#### Configuration

Use the command line interface to add the Claude Context MCP server:

claude mcp add claude-context \
 -e OPENAI_API_KEY=sk-your-openai-api-key \
 -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
 -- npx @zilliz/claude-context-mcp@latest

See theClaude Code MCP documentationfor more details about MCP server management.

### Other MCP Client Configurations

OpenAI Codex CLI

Codex CLI uses TOML configuration files:

1. Create or edit the~/.codex/config.tomlfile.
2. Add the following configuration:

#
 IMPORTANT: the top-level key is `mcp_servers` rather than `mcpServers`.

[
mcp_servers
.
claude-context
]

command
 = 
"
npx
"

args
 = [
"
@zilliz/claude-context-mcp@latest
"
]

env
 = { 
"OPENAI_API_KEY"
 = 
"
your-openai-api-key
"
, 
"MILVUS_TOKEN"
 = 
"
your-zilliz-cloud-api-key
"
 }

#
 Optional: override the default 10s startup timeout

startup_timeout_ms
 = 
20000

1. Save the file and restart Codex CLI to apply the changes.

Gemini CLI

Gemini CLI requires manual configuration through a JSON file:

1. Create or edit the~/.gemini/settings.jsonfile.
2. Add the following configuration:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

1. Save the file and restart Gemini CLI to apply the changes.

Qwen Code

Create or edit the~/.qwen/settings.jsonfile and add the following configuration:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

Cursor

Go to:Settings->Cursor Settings->MCP->Add new global MCP server

Pasting the following configuration into your Cursor~/.cursor/mcp.jsonfile is the recommended approach. You may also install in a specific project by creating.cursor/mcp.jsonin your project folder. SeeCursor MCP docsfor more info.

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
-y
"
, 
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

Void

Go to:Settings->MCP->Add MCP Server

Add the following configuration to your Void MCP settings:

{
 
"mcpServers"
: {
 
"code-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
-y
"
, 
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

Claude Desktop

Add to your Claude Desktop configuration:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

Windsurf

Windsurf supports MCP configuration through a JSON file. Add the following configuration to your Windsurf MCP settings:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
-y
"
, 
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

VS Code

The Claude Context MCP server can be used with VS Code through MCP-compatible extensions. Add the following configuration to your VS Code MCP settings:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
-y
"
, 
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

Cherry Studio

Cherry Studio allows for visual MCP server configuration through its settings interface. While it doesn't directly support manual JSON configuration, you can add a new server via the GUI:

1. Navigate toSettings → MCP Servers → Add Server.
2. Fill in the server details:* Name:claude-context
* Type:STDIO
* Command:npx
* Arguments:["@zilliz/claude-context-mcp@latest"]
* Environment Variables:OPENAI_API_KEY:your-openai-api-keyMILVUS_ADDRESS:your-zilliz-cloud-public-endpointMILVUS_TOKEN:your-zilliz-cloud-api-key
* OPENAI_API_KEY:your-openai-api-key
* MILVUS_ADDRESS:your-zilliz-cloud-public-endpoint
* MILVUS_TOKEN:your-zilliz-cloud-api-key
3. Save the configuration to activate the server.

Cline

Cline uses a JSON configuration file to manage MCP servers. To integrate the provided MCP server configuration:

1. Open Cline and click on theMCP Serversicon in the top navigation bar.
2. Select theInstalledtab, then clickAdvanced MCP Settings.
3. In thecline_mcp_settings.jsonfile, add the following configuration:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

1. Save the file.

Augment

To configure Claude Context MCP in Augment Code, you can use either the graphical interface or manual configuration.

#### A. Using the Augment Code UI

1. Click the hamburger menu.
2. SelectSettings.
3. Navigate to theToolssection.
4. Click the+ Add MCPbutton.
5. Enter the following command:npx @zilliz/claude-context-mcp@latest
6. Name the MCP:Claude Context.
7. Click theAddbutton.

#### B. Manual Configuration

1. Press Cmd/Ctrl Shift P or go to the hamburger menu in the Augment panel
2. Select Edit Settings
3. Under Advanced, click Edit in settings.json
4. Add the server configuration to themcpServersarray in theaugment.advancedobject

"augment.advanced"
: { 
 
"mcpServers"
: [ 
 { 
 
"name"
: 
"
claude-context
"
, 
 
"command"
: 
"
npx
"
, 
 
"args"
: [
"
-y
"
, 
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 ]
}

Roo Code

Roo Code utilizes a JSON configuration file for MCP servers:

1. Open Roo Code and navigate toSettings → MCP Servers → Edit Global Config.
2. In themcp_settings.jsonfile, add the following configuration:

{
 
"mcpServers"
: {
 
"claude-context"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
 }
 }
}

1. Save the file to activate the server.

Zencoder

Zencoder offers support for MCP tools and servers in both its JetBrains and VS Code plugin versions.

1. Go to the Zencoder menu (...)
2. From the dropdown menu, selectTools
3. Click on theAdd Custom MCP
4. Add the name (i.e.Claude Contextand server configuration from below, and make sure to hit theInstallbutton

{
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@zilliz/claude-context-mcp@latest
"
],
 
"env"
: {
 
"OPENAI_API_KEY"
: 
"
your-openai-api-key
"
,
 
"MILVUS_ADDRESS"
: 
"
your-zilliz-cloud-public-endpoint
"
,
 
"MILVUS_TOKEN"
: 
"
your-zilliz-cloud-api-key
"

 }
}

1. Save the server by hitting theInstallbutton.

LangChain/LangGraph

For LangChain/LangGraph integration examples, seethis example.

Other MCP Clients

The server uses stdio transport and follows the standard MCP protocol. It can be integrated with any MCP-compatible client by running:

npx @zilliz/claude-context-mcp@latest

### Usage in Your Codebase

1. Open Claude Codecd your-project-directory
claude
2. Index your codebase:Index this codebase
3. Check indexing status:Check the indexing status
4. Start searching:Find functions that handle user authentication

🎉That's it!You now have semantic code search in Claude Code.

### Environment Variables Configuration

For more detailed MCP environment variable configuration, see ourEnvironment Variables Guide.

### Using Different Embedding Models

To configure custom embedding models (e.g.,text-embedding-3-largefor OpenAI,voyage-code-3for VoyageAI), see theMCP Configuration Examplesfor detailed setup instructions for each provider.

### File Inclusion & Exclusion Rules

For detailed explanation of file inclusion and exclusion rules, and how to customize them, see ourFile Inclusion & Exclusion Rules.

### Available Tools

#### 1.index_codebase

Index a codebase directory for hybrid search (BM25 + dense vector).

#### 2.search_code

Search the indexed codebase using natural language queries with hybrid search (BM25 + dense vector).

#### 3.clear_index

Clear the search index for a specific codebase.

#### 4.get_indexing_status

Get the current indexing status of a codebase. Shows progress percentage for actively indexing codebases and completion status for indexed codebases.

## 📊 Evaluation

Our controlled evaluation demonstrates that Claude Context MCP achieves ~40% token reduction under the condition of equivalent retrieval quality. This translates to significant cost and time savings in production environments. This also means that, under the constraint of limited token context length, using Claude Context yields better retrieval and answer results.

For detailed evaluation methodology and results, see theevaluation directory.

## 🏗️ Architecture

### 🔧 Implementation Details

* 🔍Hybrid Code Search: Ask questions like"find functions that handle user authentication"and get relevant, context-rich code instantly using advanced hybrid search (BM25 + dense vector).
* 🧠Context-Aware: Discover large codebase, understand how different parts of your codebase relate, even across millions of lines of code.
* ⚡Incremental Indexing: Efficiently re-index only changed files using Merkle trees.
* 🧩Intelligent Code Chunking: Analyze code in Abstract Syntax Trees (AST) for chunking.
* 🗄️Scalable: Integrates with Zilliz Cloud for scalable vector search, no matter how large your codebase is.
* 🛠️Customizable: Configure file extensions, ignore patterns, and embedding models.

### Core Components

Claude Context is a monorepo containing three main packages:

* @zilliz/claude-context-core: Core indexing engine with embedding and vector database integration
* VSCode Extension: Semantic Code Search extension for Visual Studio Code
* @zilliz/claude-context-mcp: Model Context Protocol server for AI agent integration

### Supported Technologies

* Embedding Providers:OpenAI,VoyageAI,Ollama,Gemini
* Vector Databases:MilvusorZilliz Cloud(fully managed vector database as a service)
* Code Splitters: AST-based splitter (with automatic fallback), LangChain character-based splitter
* Languages: TypeScript, JavaScript, Python, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Markdown
* Development Tools: VSCode, Model Context Protocol

## 📦 Other Ways to Use Claude Context

While MCP is the recommended way to use Claude Context with AI assistants, you can also use it directly or through the VSCode extension.

### Build Applications with Core Package

The@zilliz/claude-context-corepackage provides the fundamental functionality for code indexing and semantic search.

import
 
{
 
Context
,
 
MilvusVectorDatabase
,
 
OpenAIEmbedding
 
}
 
from
 
'@zilliz/claude-context-core'
;

// Initialize embedding provider

const
 
embedding
 
=
 
new
 
OpenAIEmbedding
(
{

 
apiKey
: 
process
.
env
.
OPENAI_API_KEY
 
||
 
'your-openai-api-key'
,

 
model
: 
'text-embedding-3-small'

}
)
;

// Initialize vector database

const
 
vectorDatabase
 
=
 
new
 
MilvusVectorDatabase
(
{

 
address
: 
process
.
env
.
MILVUS_ADDRESS
 
||
 
'your-zilliz-cloud-public-endpoint'
,

 
token
: 
process
.
env
.
MILVUS_TOKEN
 
||
 
'your-zilliz-cloud-api-key'

}
)
;

// Create context instance

const
 
context
 
=
 
new
 
Context
(
{

 embedding
,

 vectorDatabase

}
)
;

// Index your codebase with progress tracking

const
 
stats
 
=
 
await
 
context
.
indexCodebase
(
'./your-project'
,
 
(
progress
)
 
=>
 
{

 
console
.
log
(
`
${
progress
.
phase
}
 - 
${
progress
.
percentage
}
%`
)
;

}
)
;

console
.
log
(
`Indexed 
${
stats
.
indexedFiles
}
 files, 
${
stats
.
totalChunks
}
 chunks`
)
;

// Perform semantic search

const
 
results
 
=
 
await
 
context
.
semanticSearch
(
'./your-project'
,
 
'vector database operations'
,
 
5
)
;

results
.
forEach
(
result
 
=>
 
{

 
console
.
log
(
`File: 
${
result
.
relativePath
}
:
${
result
.
startLine
}
-
${
result
.
endLine
}
`
)
;

 
console
.
log
(
`Score: 
${
(
result
.
score
 
*
 
100
)
.
toFixed
(
2
)
}
%`
)
;

 
console
.
log
(
`Content: 
${
result
.
content
.
substring
(
0
,
 
100
)
}
...`
)
;

}
)
;

### VSCode Extension

Integrates Claude Context directly into your IDE. Provides an intuitive interface for semantic code search and navigation.

1. Direct Link:Install from VS Code Marketplace
2. Manual Search:* Open Extensions view in VSCode (Ctrl+Shift+X or Cmd+Shift+X on Mac)
* Search for "Semantic Code Search"
* Click Install

## 🛠️ Development

### Setup Development Environment

#### Prerequisites

* Node.js 20.x or 22.x
* pnpm (recommended package manager)

#### Cross-Platform Setup

#
 Clone repository

git clone https://github.com/zilliztech/claude-context.git

cd
 claude-context

#
 Install dependencies

pnpm install

#
 Build all packages

pnpm build

#
 Start development mode

pnpm dev

#### Windows-Specific Setup

On Windows, ensure you have:

* Git for Windowswith proper line ending configuration
* Node.jsinstalled via the official installer or package manager
* pnpminstalled globally:npm install -g pnpm

#
 Windows PowerShell/Command Prompt

git clone https:
//
github.com
/
zilliztech
/
claude
-
context.git
cd claude
-
context

#
 Configure git line endings (recommended)

git config core.autocrlf false

#
 Install dependencies

pnpm install

#
 Build all packages (uses cross-platform scripts)

pnpm build

#
 Start development mode

pnpm dev

### Building

#
 Build all packages (cross-platform)

pnpm build

#
 Build specific package

pnpm build:core
pnpm build:vscode
pnpm build:mcp

#
 Performance benchmarking

pnpm benchmark

#### Windows Build Notes

* All build scripts are cross-platform compatible using rimraf
* Build caching is enabled for faster subsequent builds
* Use PowerShell or Command Prompt - both work equally well

### Running Examples

#
 Development with file watching

cd
 examples/basic-usage
pnpm dev

## 📖 Examples

Check the/examplesdirectory for complete usage examples:

* Basic Usage: Simple indexing and search example

## ❓ FAQ

Common Questions:

* What files does Claude Context decide to embed?
* Can I use a fully local deployment setup?
* Does it support multiple projects / codebases?
* How does Claude Context compare to other coding tools?

❓ For detailed answers and more troubleshooting tips, see ourFAQ Guide.

🔧Encountering issues?Visit ourTroubleshooting Guidefor step-by-step solutions.

📚Need more help?Check out ourcomplete documentationfor detailed guides and troubleshooting tips.

## 🤝 Contributing

We welcome contributions! Please see ourContributing Guidefor details on how to get started.

Package-specific contributing guides:

* Core Package Contributing
* MCP Server Contributing
* VSCode Extension Contributing

## 🗺️ Roadmap

* AST-based code analysis for improved understanding
* Support for additional embedding providers
* Agent-based interactive search mode
* Enhanced code chunking strategies
* Search result ranking optimization
* Robust Chrome Extension

## 📄 License

This project is licensed under the MIT License - see theLICENSEfile for details.

## 🔗 Links

* GitHub Repository
* VSCode Marketplace
* Milvus Documentation
* Zilliz Cloud

## About

Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

github.com/zilliztech/claude-context/tree/master/docs

### Topics

 nodejs

 agent

 typescript

 mcp

 code-search

 openai

 vscode-extension

 code-generation

 cursor

 merkle-tree

 semantic-search

 embedding

 rag

 vector-database

 gemini-cli

 agentic-rag

 voyage-ai

 ai-coding

 vibe-coding

 claude-code

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

6.2k

 stars
 

### Watchers

32

 watching
 

### Forks

543

 forks
 

 Report repository

 

## Releases

23

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript69.2%
* Python15.4%
* JavaScript10.4%
* CSS3.0%
* HTML2.0%