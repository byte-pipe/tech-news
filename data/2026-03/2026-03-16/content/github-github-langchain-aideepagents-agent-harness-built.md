---
title: 'GitHub - langchain-ai/deepagents: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. · GitHub'
url: https://github.com/langchain-ai/deepagents
site_name: github
content_file: github-github-langchain-aideepagents-agent-harness-built
fetched_at: '2026-03-16T11:23:17.110084'
original_url: https://github.com/langchain-ai/deepagents
author: langchain-ai
description: Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks. - langchain-ai/deepagents
---

langchain-ai

 

/

deepagents

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.9k
* Star12.1k

 
 
 
 
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

955 Commits
955 Commits
.github
.github
 
 
.vscode
.vscode
 
 
examples
examples
 
 
libs
libs
 
 
.gitignore
.gitignore
 
 
.markdownlint.json
.markdownlint.json
 
 
.mcp.json
.mcp.json
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
action.yml
action.yml
 
 
pr-labeler-consolidation.md
pr-labeler-consolidation.md
 
 
release-please-config.json
release-please-config.json
 
 
View all files

## Repository files navigation

### The batteries-included agent harness.

Deep Agents is an agent harness. An opinionated, ready-to-run agent out of the box. Instead of wiring up prompts, tools, and context management yourself, you get a working agent immediately and customize what you need.

What's included:

* Planning—write_todosfor task breakdown and progress tracking
* Filesystem—read_file,write_file,edit_file,ls,glob,grepfor reading and writing context
* Shell access—executefor running commands (with sandboxing)
* Sub-agents—taskfor delegating work with isolated context windows
* Smart defaults— Prompts that teach the model how to use these tools effectively
* Context management— Auto-summarization when conversations get long, large outputs saved to files

Note

Looking for the JS/TS library? Check outdeepagents.js.

## Quickstart

pip install deepagents

#
 or

uv add deepagents

from
 
deepagents
 
import
 
create_deep_agent

agent
 
=
 
create_deep_agent
()

result
 
=
 
agent
.
invoke
({
"messages"
: [{
"role"
: 
"user"
, 
"content"
: 
"Research LangGraph and write a summary"
}]})

The agent can plan, read/write files, and manage its own context. Add tools, customize prompts, or swap models as needed.

Tip

For developing, debugging, and deploying AI agents and LLM applications, seeLangSmith.

## Customization

Add your own tools, swap models, customize prompts, configure sub-agents, and more. See thedocumentationfor full details.

from
 
langchain
.
chat_models
 
import
 
init_chat_model

agent
 
=
 
create_deep_agent
(
 
model
=
init_chat_model
(
"openai:gpt-4o"
),
 
tools
=
[
my_custom_tool
],
 
system_prompt
=
"You are a research assistant."
,
)

MCP is supported vialangchain-mcp-adapters.

## Deep Agents CLI

curl -LsSf https://raw.githubusercontent.com/langchain-ai/deepagents/main/libs/cli/scripts/install.sh 
|
 bash

Web search, remote sandboxes, persistent memory, human-in-the-loop approval, and more. See theCLI READMEfor the full feature set.

## LangGraph Native

create_deep_agentreturns a compiledLangGraphgraph. Use it with streaming, Studio, checkpointers, or any LangGraph feature.

## FAQ

### Why should I use this?

* 100% open source— MIT licensed, fully extensible
* Provider agnostic— Works with any Large Language Model model that supports tool calling, including both frontier and open models
* Built on LangGraph— Production-ready runtime with streaming, persistence, and checkpointing
* Batteries included— Planning, file access, sub-agents, and context management work out of the box
* Get started in seconds—uv add deepagentsand you have a working agent
* Customize in minutes— Add tools, swap models, tune prompts when you need to

## Documentation

* docs.langchain.com– Comprehensive documentation, including conceptual overviews and guides
* reference.langchain.com/python– API reference docs for Deep Agents packages
* Chat LangChain– Chat with the LangChain documentation and get answers to your questions

Discussions: Visit theLangChain Forumto connect with the community and share all of your technical questions, ideas, and feedback.

## Additional resources

* Examples— Working agents and patterns
* Contributing Guide– Learn how to contribute to LangChain projects and find good first issues.
* Code of Conduct– Our community guidelines and standards for participation.

## Acknowledgements

This project was primarily inspired by Claude Code, and initially was largely an attempt to see what made Claude Code general purpose, and make it even more so.

## Security

Deep Agents follows a "trust the LLM" model. The agent can do anything its tools allow. Enforce boundaries at the tool/sandbox level, not by expecting the model to self-police. See thesecurity policyfor more information.

## About

Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks.

docs.langchain.com/deepagents

### Topics

 ai

 langchain

 langgraph

 deepagents

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

12.1k

 stars
 

### Watchers

80

 watching
 

### Forks

1.9k

 forks
 

 Report repository

 

## Releases70

deepagents==0.4.11

 Latest

 

Mar 13, 2026

 

+ 69 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors91

+ 77 contributors

## Languages

* Python99.4%
* Other0.6%