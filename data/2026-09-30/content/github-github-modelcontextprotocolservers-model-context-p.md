---
title: 'GitHub - modelcontextprotocol/servers: Model Context Protocol Servers · GitHub'
url: https://github.com/modelcontextprotocol/servers
site_name: github
content_file: github-github-modelcontextprotocolservers-model-context-p
fetched_at: '2026-09-30T16:40:34.101833'
original_url: https://github.com/modelcontextprotocol/servers
author: modelcontextprotocol
description: Model Context Protocol Servers. Contribute to modelcontextprotocol/servers development by creating an account on GitHub.
---

modelcontextprotocol

 

/

servers

Public

* NotificationsYou must be signed in to change notification settings
* Fork11.7k
* Star90.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

4,189 Commits
4,189 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
scripts
scripts
 
 
src
src
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.npmrc
.npmrc
 
 
ADDITIONAL.md
ADDITIONAL.md
 
 
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
 
 
RELEASING.md
RELEASING.md
 
 
SECURITY.md
SECURITY.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Model Context Protocol servers

This repository is a collection ofreference implementationsfor theModel Context Protocol(MCP), as well as references to community-built servers and additional resources.

Important

If you are looking for a list of MCP servers, you can browse published servers onthe MCP Registry. The repository served by this README is dedicated to housing just the small number of reference servers maintained by the MCP steering group.

Warning

The servers in this repository are intended asreference implementationsto demonstrate MCP features and SDK usage. They are meant to serve as educational examples for developers building their own MCP servers, not as production-ready solutions. Developers should evaluate their own security requirements and implement appropriate safeguards based on their specific threat model and use case.

The servers in this repository showcase the versatility and extensibility of MCP, demonstrating how it can be used to give Large Language Models (LLMs) secure, controlled access to tools and data sources.
Typically, each MCP server is implemented with an MCP SDK:

* C# MCP SDK
* Go MCP SDK
* Java MCP SDK
* Kotlin MCP SDK
* PHP MCP SDK
* Python MCP SDK
* Ruby MCP SDK
* Rust MCP SDK
* Swift MCP SDK
* TypeScript MCP SDK

## 🌟 Reference Servers

These servers aim to demonstrate MCP features and the official SDKs.

* Everything- Reference / test server with prompts, resources, and tools.
* Fetch- Web content fetching and conversion for efficient LLM usage.
* Filesystem- Secure file operations with configurable access controls.
* Git- Tools to read, search, and manipulate Git repositories.
* Memory- Knowledge graph-based persistent memory system.
* Sequential Thinking- Dynamic and reflective problem-solving through thought sequences.
* Time- Time and timezone conversion capabilities.

### Archived

The following reference servers are now archived and can be found atservers-archived.

* AWS KB Retrieval- Retrieval from AWS Knowledge Base using Bedrock Agent Runtime.
* Brave Search- Web and local search using Brave's Search API. Has been replaced by theofficial server(@brave/brave-search-mcp-server).
* EverArt- AI image generation using various models.
* GitHub- Repository management, file operations, and GitHub API integration.
* GitLab- GitLab API, enabling project management.
* Google Drive- File access and search capabilities for Google Drive.
* Google Maps- Location services, directions, and place details.
* PostgreSQL- Read-only database access with schema inspection.
* Puppeteer- Browser automation and web scraping.
* Redis- Interact with Redis key-value stores.
* Sentry- Retrieving and analyzing issues from Sentry.io.
* Slack- Channel management and messaging capabilities. Now maintained byZencoder
* SQLite- Database interaction and business intelligence capabilities.

## 🚀 Getting Started

### Using MCP Servers in this Repository

TypeScript-based servers in this repository can be used directly withnpx.

For example, this will start theMemoryserver:

npx -y @modelcontextprotocol/server-memory

Python-based servers in this repository can be used directly withuvxorpip.uvxis recommended for ease of use and setup.

For example, this will start theGitserver:

#
 With uvx

uvx mcp-server-git

#
 With pip

pip install mcp-server-git
python -m mcp_server_git

Followtheseinstructions to installuv/uvxandtheseto installpip.

### Using an MCP Client

However, running a server on its own isn't very useful, and should instead be configured into an MCP client. For example, here's the Claude Desktop configuration to use the above server:

{
 
"mcpServers"
: {
 
"memory"
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
@modelcontextprotocol/server-memory
"
]
 }
 }
}

On Windows, wrapnpxwithcmd /c:

{
 
"mcpServers"
: {
 
"memory"
: {
 
"command"
: 
"
cmd
"
,
 
"args"
: [
"
/c
"
, 
"
npx
"
, 
"
-y
"
, 
"
@modelcontextprotocol/server-memory
"
]
 }
 }
}

Additional examples of using the Claude Desktop as an MCP client might look like:

{
 
"mcpServers"
: {
 
"filesystem"
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
@modelcontextprotocol/server-filesystem
"
, 
"
/path/to/allowed/files
"
]
 },
 
"git"
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
mcp-server-git
"
, 
"
--repository
"
, 
"
path/to/git/repo
"
]
 },
 
"github"
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
@modelcontextprotocol/server-github
"
],
 
"env"
: {
 
"GITHUB_PERSONAL_ACCESS_TOKEN"
: 
"
<YOUR_TOKEN>
"

 }
 },
 
"postgres"
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
@modelcontextprotocol/server-postgres
"
, 
"
postgresql://localhost/mydb
"
]
 }
 }
}

On Windows, apply the same wrapper to eachnpx-based entry above by changing"command"to"cmd"and prepending"/c", "npx"to the existingargs. Leaveuvxentries unchanged.

## 🛠️ Creating Your Own Server

Interested in creating your own MCP server? Visit the official documentation atmodelcontextprotocol.iofor comprehensive guides, best practices, and technical details on implementing MCP servers.

## 📚 Learn More

SeeADDITIONAL.mdfor a curated list of frameworks and resources that simplify building MCP servers and clients.

## 🤝 Contributing

SeeCONTRIBUTING.mdfor information about contributing to this repository.

## 📦 Releasing

SeeRELEASING.mdfor how packages are published (OIDC trusted publishing from CI — no registry tokens) and how to retry a failed publish.

## 🔒 Security

SeeSECURITY.mdfor reporting security vulnerabilities.

## 📜 License

This project is licensed under the Apache License, Version 2.0 for new contributions, with existing code under MIT - see theLICENSEfile for details.

## 💬 Community

* GitHub Discussions

## ⭐ Support

If you find MCP servers useful, please consider starring the repository and contributing new servers or improvements!

Managed by Anthropic, but built together with the community. The Model Context Protocol is open source and we encourage everyone to contribute their own servers and improvements!