---
title: GitHub - andrewyng/context-hub · GitHub
url: https://github.com/andrewyng/context-hub
site_name: github
content_file: github-github-andrewyngcontext-hub-github
fetched_at: '2026-03-19T11:17:35.720870'
original_url: https://github.com/andrewyng/context-hub
author: andrewyng
description: Contribute to andrewyng/context-hub development by creating an account on GitHub.
---

andrewyng

 

/

context-hub

Public

* NotificationsYou must be signed in to change notification settings
* Fork913
* Star10.4k

 
 
 
 
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

170 Commits
170 Commits
.github
.github
 
 
cli
cli
 
 
content
content
 
 
docs
docs
 
 
.gitignore
.gitignore
 
 
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
 
 
llms.txt
llms.txt
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Context Hub

Coding agents hallucinate APIs and forget what they learn in a session. Context Hub gives them curated, versioned docs, plus the ability to get smarter with every task. All content is open and maintained as markdown in this repo — you can inspect exactly what your agent reads, and contribute back.

## Quick Start

npm install -g @aisuite/chub
chub search openai 
#
 find what's available

chub get openai/chat --lang py 
#
 fetch current docs (Python version) 

## How It Works

Chub is designed for your coding agent to use (not for you to use!). You can prompt your agent to use it (e.g., "Use the CLI command chub to get the latest API documentation for calling OpenAI. Run 'chub help' to understand how it works.") Or by creating an agent skill to use Chub usingSKILL.md, and ideally prompting your agent to remember to use this skill. (If you are using Claude Code, create the directory ~/.claude/skills/get-api-docs and put SKILL.md there.)

Most of the time, it's simple — search, fetch, use:

chub search 
"
stripe payments
"
 
#
 find relevant docs

chub get stripe/api --lang js 
#
 fetch the doc

#
 Agent reads the doc, writes correct code. Done.

When the agent discovers a gap, it can annotate locally for next time:

chub annotate stripe/api 
"
Needs raw body for webhook verification
"

#
 Next session, the annotation appears automatically on chub get.

Feedback flows back to authors—chub feedback stripe/api upordown— vote the docs up or down so they can get better for everyone over time.

## Content Types

Versioned, language-specific. "What to know."

chub get openai/chat --lang py 
#
 Python variant

chub get openai/chat --lang js 
#
 JavaScript variant

More content types than API documentation (such as agent skills) are on the roadmap.

## Commands

Command

Purpose

chub search [query]

Search docs and skills (no query = list all)

chub get <id> [--lang py|js]

Fetch docs or skills by ID

chub annotate <id> <note>

Attach a note to a doc or skill

chub annotate <id> --clear

Remove annotations

chub annotate --list

List all annotations

chub feedback <id> <up|down>

Upvote or downvote a doc (sent to maintainers)

For the full list of commands, flags, and piping patterns, see theCLI Reference.

## Self-Improving Agents

Context Hub is designed for a loop where agents get better over time.

Annotationsare local notes that agents attach to docs. They persist across sessions and appear automatically on future fetches — so agents learn from past experience. SeeFeedback and Annotations.

Feedback(up/down ratings with optional labels) goes to doc authors, who update the content based on what's working and what isn't. The docs get better for everyone — not just your local annotations.

 Without Context Hub With Context Hub
 ─────────────────── ─────────────────
 Search the web Fetch curated docs
 Noisy results Higher chance of code working
 Code breaks Agent notes any gaps/workarounds
 Effort in fixing ↗ Even smarter next session
 Knowledge forgotten
 ↻ Repeat next session

## Key Features

### Incremental Fetch

Docs can have multiple reference files beyond the main entry point. Fetch only what you need — no wasted tokens. Use--fileto grab specific references, or--fullfor everything. See theCLI Reference.

### Annotations & Feedback

Annotations are local notes that agents attach to docs — they persist across sessions and appear automatically on future fetches. Feedback (up/down ratings) goes to doc authors to improve the content for everyone. SeeFeedback and Annotations.

## Contributing

Anyone can contribute docs and skills — API providers, framework authors, and the community. Content is plain markdown with YAML frontmatter, submitted as pull requests. See theContent Guidefor the format and structure.

Agent feedback (up/down ratings from real usage) flows back to authors, helping surface what needs fixing and improving overall quality over time.

## License

MIT

## About

 No description, website, or topics provided.
 

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
 

### Stars

10.4k

 stars
 

### Watchers

83

 watching
 

### Forks

913

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript100.0%