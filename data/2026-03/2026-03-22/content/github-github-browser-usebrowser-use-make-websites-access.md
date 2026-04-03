---
title: 'GitHub - browser-use/browser-use: 🌐 Make websites accessible for AI agents. Automate tasks online with ease. · GitHub'
url: https://github.com/browser-use/browser-use
site_name: github
content_file: github-github-browser-usebrowser-use-make-websites-access
fetched_at: '2026-03-22T11:09:42.522684'
original_url: https://github.com/browser-use/browser-use
author: browser-use
description: 🌐 Make websites accessible for AI agents. Automate tasks online with ease. - browser-use/browser-use
---

browser-use

 

/

browser-use

Public

* NotificationsYou must be signed in to change notification settings
* Fork9.6k
* Star82k

 
 
 
 
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

8,899 Commits
8,899 Commits
.github
.github
 
 
bin
bin
 
 
browser_use
browser_use
 
 
docker
docker
 
 
examples
examples
 
 
skills
skills
 
 
static
static
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
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
 
 
CLOUD.md
CLOUD.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.fast
Dockerfile.fast
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

🌤️ Want to skip the setup? Use ourcloudfor faster, scalable, stealth-enabled browser automation!

# 🤖 LLM Quickstart

1. Direct your favorite coding agent (Cursor, Claude Code, etc) toAgents.md
2. Prompt away!

# 👋 Human Quickstart

1. Create environment and install Browser-Use withuv(Python>=3.11):

uv init 
&&
 uv add browser-use 
&&
 uv sync

#
 uvx browser-use install # Run if you don't have Chromium installed

2. [Optional] Get your API key fromBrowser Use Cloud:

# .env
BROWSER_USE_API_KEY=your-key
# GOOGLE_API_KEY=your-key
# ANTHROPIC_API_KEY=your-key

3. Run your first agent:

from
 
browser_use
 
import
 
Agent
, 
Browser
, 
ChatBrowserUse

# from browser_use import ChatGoogle # ChatGoogle(model='gemini-3-flash-preview')

# from browser_use import ChatAnthropic # ChatAnthropic(model='claude-sonnet-4-6')

import
 
asyncio

async
 
def
 
main
():
 
browser
 
=
 
Browser
(
 
# use_cloud=True, # Use a stealth browser on Browser Use Cloud

 )

 
agent
 
=
 
Agent
(
 
task
=
"Find the number of stars of the browser-use repo"
,
 
llm
=
ChatBrowserUse
(),
 
# llm=ChatGoogle(model='gemini-3-flash-preview'),

 
# llm=ChatAnthropic(model='claude-sonnet-4-6'),

 
browser
=
browser
,
 )
 
await
 
agent
.
run
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

Check out thelibrary docsand thecloud docsfor more!

# Demos

### 📋 Form-Filling

#### Task = "Fill in this job application with my resume and information."

Example code ↗

### 🍎 Grocery-Shopping

#### Task = "Put this list of items into my instacart."

grocery-use-large.mp4

Example code ↗

### 💻 Personal-Assistant.

#### Task = "Help me find parts for a custom PC."

pc-use-large.mp4

Example code ↗

### 💡Seemore examples here ↗and give us a star!

# 🚀 Template Quickstart

Want to get started even faster?Generate a ready-to-run template:

uvx browser-use init --template default

This creates abrowser_use_default.pyfile with a working example. Available templates:

* default- Minimal setup to get started quickly
* advanced- All configuration options with detailed comments
* tools- Examples of custom tools and extending the agent

You can also specify a custom output path:

uvx browser-use init --template default --output my_agent.py

# 💻 CLI

Fast, persistent browser automation from the command line:

browser-use open https://example.com 
#
 Navigate to URL

browser-use state 
#
 See clickable elements

browser-use click 5 
#
 Click element by index

browser-use 
type
 
"
Hello
"
 
#
 Type text

browser-use screenshot page.png 
#
 Take screenshot

browser-use close 
#
 Close browser

The CLI keeps the browser running between commands for fast iteration. SeeCLI docsfor all commands.

### Claude Code Skill

ForClaude Code, install the skill to enable AI-assisted browser automation:

mkdir -p 
~
/.claude/skills/browser-use
curl -o 
~
/.claude/skills/browser-use/SKILL.md \
 https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md

## Integrations, hosting, custom tools, MCP, and more on ourDocs ↗

# FAQ

What's the best model to use?

We optimizedChatBrowserUse()specifically for browser automation tasks. On avg it completes tasks 3-5x faster than other models with SOTA accuracy.

Pricing (per 1M tokens):

* Input tokens: $0.20
* Cached input tokens: $0.02
* Output tokens: $2.00

For other LLM providers, see oursupported models documentation.

Should I use the Browser Use system prompt with the open-source preview model?

Yes. If you useChatBrowserUse(model='browser-use/bu-30b-a3b-preview')with a normalAgent(...), Browser Use still sends its default agent system prompt for you.

You donotneed to add a separate custom "Browser Use system message" just because you switched to the open-source preview model. Only useextend_system_messageoroverride_system_messagewhen you intentionally want to customize the default behavior for your task.

If you want the best default speed/accuracy, we still recommend the newer hostedbu-*models. If you want the open-source preview model, the setup stays the same apart from themodel=value.

Can I use custom tools with the agent?

Yes! You can add custom tools to extend the agent's capabilities:

from
 
browser_use
 
import
 
Tools

tools
 
=
 
Tools
()

@
tools
.
action
(
description
=
'Description of what this tool does.'
)

def
 
custom_tool
(
param
: 
str
) 
->
 
str
:
 
return
 
f"Result: 
{
param
}
"

agent
 
=
 
Agent
(
 
task
=
"Your task"
,
 
llm
=
llm
,
 
browser
=
browser
,
 
tools
=
tools
,
)

Can I use this for free?

Yes! Browser-Use is open source and free to use. You only need to choose an LLM provider (like OpenAI, Google, ChatBrowserUse, or run local models with Ollama).

Terms of Service

This open-source library is licensed under the MIT License. For Browser Use services & data policy, see ourTerms of ServiceandPrivacy Policy.

How do I handle authentication?

Check out our authentication examples:

* Using real browser profiles- Reuse your existing Chrome profile with saved logins
* If you want to use temporary accounts with inbox, choose AgentMail
* To sync your auth profile with the remote browser, runcurl -fsSL https://browser-use.com/profile.sh | BROWSER_USE_API_KEY=XXXX sh(replace XXXX with your API key)

These examples show how to maintain sessions and handle authentication seamlessly.

How do I solve CAPTCHAs?

For CAPTCHA handling, you need better browser fingerprinting and proxies. UseBrowser Use Cloudwhich provides stealth browsers designed to avoid detection and CAPTCHA challenges.

How do I go into production?

Chrome can consume a lot of memory, and running many agents in parallel can be tricky to manage.

For production use cases, use ourBrowser Use Cloud APIwhich handles:

* Scalable browser infrastructure
* Memory management
* Proxy rotation
* Stealth browser fingerprinting
* High-performance parallel execution

Tell your computer what to do, and it gets it done.

   

 Made with ❤️ in Zurich and San Francisco 

## About

🌐 Make websites accessible for AI agents. Automate tasks online with ease.

browser-use.com

### Topics

 python

 browser-automation

 ai-agents

 playwright

 ai-tools

 llm

 browser-use

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

82k

 stars
 

### Watchers

412

 watching
 

### Forks

9.6k

 forks
 

 Report repository

 

## Releases120

0.12.3

 Latest

 

Mar 20, 2026

 

+ 119 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by2.4k

 + 2,376
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python98.4%
* Other1.6%