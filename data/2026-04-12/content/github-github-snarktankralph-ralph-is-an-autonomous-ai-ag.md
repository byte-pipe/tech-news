---
title: 'GitHub - snarktank/ralph: Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. · GitHub'
url: https://github.com/snarktank/ralph
site_name: github
content_file: github-github-snarktankralph-ralph-is-an-autonomous-ai-ag
fetched_at: '2026-04-12T11:34:11.344844'
original_url: https://github.com/snarktank/ralph
author: snarktank
description: 'Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. - GitHub - snarktank/ralph: Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.'
---

snarktank



/

ralph

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star15.6k




 
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

20 Commits
20 Commits
.claude-plugin
.claude-plugin
 
 
.github/
workflows
.github/
workflows
 
 
flowchart
flowchart
 
 
skills
skills
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
prd.json.example
prd.json.example
 
 
prompt.md
prompt.md
 
 
ralph-flowchart.png
ralph-flowchart.png
 
 
ralph.sh
ralph.sh
 
 
ralph.webp
ralph.webp
 
 
View all files

## Repository files navigation

# Ralph

Ralph is an autonomous AI agent loop that runs AI coding tools (AmporClaude Code) repeatedly until all PRD items are complete. Each iteration is a fresh instance with clean context. Memory persists via git history,progress.txt, andprd.json.

Based onGeoffrey Huntley's Ralph pattern.

Read my in-depth article on how I use Ralph

## Prerequisites

* One of the following AI coding tools installed and authenticated:Amp CLI(default)Claude Code(npm install -g @anthropic-ai/claude-code)
* Amp CLI(default)
* Claude Code(npm install -g @anthropic-ai/claude-code)
* jqinstalled (brew install jqon macOS)
* A git repository for your project

## Setup

### Option 1: Copy to your project

Copy the ralph files into your project:

#
 From your project root

mkdir -p scripts/ralph
cp /path/to/ralph/ralph.sh scripts/ralph/

#
 Copy the prompt template for your AI tool of choice:

cp /path/to/ralph/prompt.md scripts/ralph/prompt.md
#
 For Amp

#
 OR

cp /path/to/ralph/CLAUDE.md scripts/ralph/CLAUDE.md
#
 For Claude Code

chmod +x scripts/ralph/ralph.sh

### Option 2: Install skills globally (Amp)

Copy the skills to your Amp or Claude config for use across all projects:

For AMP

cp -r skills/prd
~
/.config/amp/skills/
cp -r skills/ralph
~
/.config/amp/skills/

For Claude Code (manual)

cp -r skills/prd
~
/.claude/skills/
cp -r skills/ralph
~
/.claude/skills/

### Option 3: Use as Claude Code Marketplace

Add the Ralph marketplace to Claude Code:

/plugin marketplace add snarktank/ralph

Then install the skills:

/plugin install ralph-skills@ralph-marketplace

Available skills after installation:

* /prd- Generate Product Requirements Documents
* /ralph- Convert PRDs to prd.json format

Skills are automatically invoked when you ask Claude to:

* "create a prd", "write prd for", "plan this feature"
* "convert this prd", "turn into ralph format", "create prd.json"

### Configure Amp auto-handoff (recommended)

Add to~/.config/amp/settings.json:

{

"amp.experimental.autoHandoff"
: {
"context"
:
90
 }
}

This enables automatic handoff when context fills up, allowing Ralph to handle large stories that exceed a single context window.

## Workflow

### 1. Create a PRD

Use the PRD skill to generate a detailed requirements document:

Load the prd skill and create a PRD for [your feature description]

Answer the clarifying questions. The skill saves output totasks/prd-[feature-name].md.

### 2. Convert PRD to Ralph format

Use the Ralph skill to convert the markdown PRD to JSON:

Load the ralph skill and convert tasks/prd-[feature-name].md to prd.json

This createsprd.jsonwith user stories structured for autonomous execution.

### 3. Run Ralph

#
 Using Amp (default)

./scripts/ralph/ralph.sh [max_iterations]

#
 Using Claude Code

./scripts/ralph/ralph.sh --tool claude [max_iterations]

Default is 10 iterations. Use--tool ampor--tool claudeto select your AI coding tool.

Ralph will:

1. Create a feature branch (from PRDbranchName)
2. Pick the highest priority story wherepasses: false
3. Implement that single story
4. Run quality checks (typecheck, tests)
5. Commit if checks pass
6. Updateprd.jsonto mark story aspasses: true
7. Append learnings toprogress.txt
8. Repeat until all stories pass or max iterations reached

## Key Files

File

Purpose

ralph.sh

The bash loop that spawns fresh AI instances (supports
--tool amp
 or
--tool claude
)

prompt.md

Prompt template for Amp

CLAUDE.md

Prompt template for Claude Code

prd.json

User stories with
passes
 status (the task list)

prd.json.example

Example PRD format for reference

progress.txt

Append-only learnings for future iterations

skills/prd/

Skill for generating PRDs (works with Amp and Claude Code)

skills/ralph/

Skill for converting PRDs to JSON (works with Amp and Claude Code)

.claude-plugin/

Plugin manifest for Claude Code marketplace discovery

flowchart/

Interactive visualization of how Ralph works

## Flowchart

View Interactive Flowchart- Click through to see each step with animations.

Theflowchart/directory contains the source code. To run locally:

cd
 flowchart
npm install
npm run dev

## Critical Concepts

### Each Iteration = Fresh Context

Each iteration spawns anew AI instance(Amp or Claude Code) with clean context. The only memory between iterations is:

* Git history (commits from previous iterations)
* progress.txt(learnings and context)
* prd.json(which stories are done)

### Small Tasks

Each PRD item should be small enough to complete in one context window. If a task is too big, the LLM runs out of context before finishing and produces poor code.

Right-sized stories:

* Add a database column and migration
* Add a UI component to an existing page
* Update a server action with new logic
* Add a filter dropdown to a list

Too big (split these):

* "Build the entire dashboard"
* "Add authentication"
* "Refactor the API"

### AGENTS.md Updates Are Critical

After each iteration, Ralph updates the relevantAGENTS.mdfiles with learnings. This is key because AI coding tools automatically read these files, so future iterations (and future human developers) benefit from discovered patterns, gotchas, and conventions.

Examples of what to add to AGENTS.md:

* Patterns discovered ("this codebase uses X for Y")
* Gotchas ("do not forget to update Z when changing W")
* Useful context ("the settings panel is in component X")

### Feedback Loops

Ralph only works if there are feedback loops:

* Typecheck catches type errors
* Tests verify behavior
* CI must stay green (broken code compounds across iterations)

### Browser Verification for UI Stories

Frontend stories must include "Verify in browser using dev-browser skill" in acceptance criteria. Ralph will use the dev-browser skill to navigate to the page, interact with the UI, and confirm changes work.

### Stop Condition

When all stories havepasses: true, Ralph outputs<promise>COMPLETE</promise>and the loop exits.

## Debugging

Check current state:

#
 See which stories are done

cat prd.json
|
 jq
'
.userStories[] | {id, title, passes}
'

#
 See learnings from previous iterations

cat progress.txt

#
 Check git history

git log --oneline -10

## Customizing the Prompt

After copyingprompt.md(for Amp) orCLAUDE.md(for Claude Code) to your project, customize it for your project:

* Add project-specific quality check commands
* Include codebase conventions
* Add common gotchas for your stack

## Archiving

Ralph automatically archives previous runs when you start a new feature (differentbranchName). Archives are saved toarchive/YYYY-MM-DD-feature-name/.

## References

* Geoffrey Huntley's Ralph article
* Amp documentation
* Claude Code documentation

## About

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.

x.com/ryancarson/status/2008548371712135632

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

15.6k

 stars


### Watchers

96

 watching


### Forks

1.6k

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

* TypeScript62.9%
* Shell17.6%
* CSS14.6%
* JavaScript3.1%
* HTML1.8%
