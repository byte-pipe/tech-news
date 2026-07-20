---
title: 'GitHub - PrefectHQ/fastmcp: 🚀 The fast, Pythonic way to build MCP servers and clients. · GitHub'
url: https://github.com/PrefectHQ/fastmcp
site_name: github
content_file: github-github-prefecthqfastmcp-the-fast-pythonic-way-to-b
fetched_at: '2026-07-20T11:57:58.036960'
original_url: https://github.com/PrefectHQ/fastmcp
author: PrefectHQ
description: 🚀 The fast, Pythonic way to build MCP servers and clients. - PrefectHQ/fastmcp
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 PrefectHQ

 

/

fastmcp

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.2k
* Star26.4k

 
 
 
 
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

3,659 Commits
3,659 Commits
.claude
.claude
 
 
.cursor/
rules
.cursor/
rules
 
 
.github
.github
 
 
docs
docs
 
 
examples
examples
 
 
fastmcp_remote
fastmcp_remote
 
 
fastmcp_slim
fastmcp_slim
 
 
scripts
scripts
 
 
skills/
fastmcp-client-cli
skills/
fastmcp-client-cli
 
 
tests
tests
 
 
v3-notes
v3-notes
 
 
.ccignore
.ccignore
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
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
 
 
justfile
justfile
 
 
logo.py
logo.py
 
 
loq.toml
loq.toml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# FastMCP 🚀

Move fast and make things.

Made with 💙 byPrefect

TheModel Context Protocol(MCP) connects LLMs to tools and data. FastMCP gives you everything you need to go from prototype to production:

from
 
fastmcp
 
import
 
FastMCP

mcp
 
=
 
FastMCP
(
"Demo 🚀"
)

@
mcp
.
tool

def
 
add
(
a
: 
int
, 
b
: 
int
) 
->
 
int
:
 
"""Add two numbers"""

 
return
 
a
 
+
 
b

if
 
__name__
 
==
 
"__main__"
:
 
mcp
.
run
()

## Why FastMCP

Building an effective MCP application is harder than it looks. FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. Connect to a server with a URL, and transport negotiation, authentication, and protocol lifecycle are managed for you. You focus on your logic, and the MCP part just works:with FastMCP, best practices are built in.

That's why FastMCP is the standard framework for working with MCP.FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages.

FastMCP has three pillars:

Servers

Expose tools, resources, and prompts to LLMs.

Apps

Give your tools interactive UIs rendered directly in the conversation.

Clients

Connect to any MCP server — local or remote, programmatic or CLI.

Serverswrap your Python functions into MCP-compliant tools, resources, and prompts.Clientsconnect to any server with full protocol support. AndAppsgive your tools interactive UIs rendered directly in the conversation.

Ready to build? Start with theinstallation guideor jump straight to thequickstart.

## Run FastMCP in production with Horizon

FastMCP is the standard way to build MCP servers.Prefect Horizonis the enterprise MCP gateway for running them safely.

Built by the FastMCP team, Horizon packages the best practices we've learned shipping the world's most popular MCP framework.

Deploy FastMCP servers from GitHub with branch previews and instant rollback. Create a private registry of every MCP your company uses. Secure access with SSO and tool-level RBAC. Get audit logs, observability, and governance across your MCP stack. Remix approved tools into purpose-built endpoints for teams and agents.

Start with FastMCP.Scale with Horizon →

## Installation

We recommend installing FastMCP withuv:

uv pip install fastmcp

For full installation instructions, including verification and upgrading, see theInstallation Guide.

Upgrading?We have guides for:

* Upgrading from FastMCP v2
* Upgrading from the MCP Python SDK
* Upgrading from the low-level SDK

Note

Ifimport fastmcpfails right after apipupgrade from FastMCP 3.2 or earlier, runpip install --force-reinstall fastmcp. SeeTroubleshootingfor why this happens (uvis unaffected).

## 📚 Documentation

FastMCP's complete documentation is available atgofastmcp.com, including detailed guides, API references, and advanced patterns.

Documentation is also available inllms.txt format, which is a simple markdown standard that LLMs can consume easily:

* llms.txtis essentially a sitemap, listing all the pages in the documentation.
* llms-full.txtcontains the entire documentation. Note this may exceed the context window of your LLM.

Community:Join ourDiscord serverto connect with other FastMCP developers and share what you're building.

## Contributing

We welcome contributions! See theContributing Guidefor setup instructions, testing requirements, and PR guidelines.

## About

🚀 The fast, Pythonic way to build MCP servers and clients.

gofastmcp.com

### Topics

 python

 mcp

 agents

 llms

 model-context-protocol

 mcp-servers

 mcp-tools

 fastmcp

 mcp-clients

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

26.4k

 stars
 

### Watchers

119

 watching
 

### Forks

2.2k

 forks
 

 Report repository

 

## Releases106

v3.4.4: Host in Translation

 Latest

 

Jul 9, 2026

 

+ 105 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%