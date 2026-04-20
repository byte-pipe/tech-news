---
title: 'GitHub - openai/codex-plugin-cc: Use Codex from Claude Code to review code or delegate tasks. · GitHub'
url: https://github.com/openai/codex-plugin-cc
site_name: tldr
content_file: tldr-github-openaicodex-plugin-cc-use-codex-from-claude
fetched_at: '2026-04-05T01:01:24.834918'
original_url: https://github.com/openai/codex-plugin-cc
date: '2026-04-05'
description: Use Codex from Claude Code to review code or delegate tasks. - openai/codex-plugin-cc
tags:
- tldr
---

openai



/

codex-plugin-cc

Public

* NotificationsYou must be signed in to change notification settings
* Fork600
* Star11.5k




 
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

11 Commits
11 Commits
.claude-plugin
.claude-plugin
 
 
.github/
workflows
.github/
workflows
 
 
plugins/
codex
plugins/
codex
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.app-server.json
tsconfig.app-server.json
 
 
View all files

## Repository files navigation

# Codex plugin for Claude Code

Use Codex from inside Claude Code for code reviews or to delegate tasks to Codex.

This plugin is for Claude Code users who want an easy way to start using Codex from the workflow
they already have.

## What You Get

* /codex:reviewfor a normal read-only Codex review
* /codex:adversarial-reviewfor a steerable challenge review
* /codex:rescue,/codex:status,/codex:result, and/codex:cancelto delegate work and manage background jobs

## Requirements

* ChatGPT subscription (incl. Free) or OpenAI API key.Usage will contribute to your Codex usage limits.Learn more.
* Usage will contribute to your Codex usage limits.Learn more.
* Node.js 18.18 or later

## Install

Add the marketplace in Claude Code:

/plugin marketplace add openai/codex-plugin-cc

Install the plugin:

/plugin install codex@openai-codex

Reload plugins:

/reload-plugins

Then run:

/codex:setup

/codex:setupwill tell you whether Codex is ready. If Codex is missing and npm is available, it can offer to install Codex for you.

If you prefer to install Codex yourself, use:

npm install -g @openai/codex

If Codex is installed but not logged in yet, run:

!
codex login

After install, you should see:

* the slash commands listed below
* thecodex:codex-rescuesubagent in/agents

One simple first run is:

/codex:review --background
/codex:status
/codex:result

## Usage

### /codex:review

Runs a normal Codex review on your current work. It gives you the same quality of code review as running/reviewinside Codex directly.

Note

Code review especially for multi-file changes might take a while. It's generally recommended to run it in the background.

Use it when you want:

* a review of your current uncommitted changes
* a review of your branch compared to a base branch likemain

Use--base <ref>for branch review. It also supports--waitand--background. It is not steerable and does not take custom focus text. Use/codex:adversarial-reviewwhen you want to challenge a specific decision or risk area.

Examples:

/codex:review
/codex:review --base main
/codex:review --background

This command is read-only and will not perform any changes. When run in the background you can use/codex:statusto check on the progress and/codex:cancelto cancel the ongoing task.

### /codex:adversarial-review

Runs asteerablereview that questions the chosen implementation and design.

It can be used to pressure-test assumptions, tradeoffs, failure modes, and whether a different approach would have been safer or simpler.

It uses the same review target selection as/codex:review, including--base <ref>for branch review.
It also supports--waitand--background. Unlike/codex:review, it can take extra focus text after the flags.

Use it when you want:

* a review before shipping that challenges the direction, not just the code details
* review focused on design choices, tradeoffs, hidden assumptions, and alternative approaches
* pressure-testing around specific risk areas like auth, data loss, rollback, race conditions, or reliability

Examples:

/codex:adversarial-review
/codex:adversarial-review --base main challenge whether this was the right caching and retry design
/codex:adversarial-review --background look
for
 race conditions and question the chosen approach

This command is read-only. It does not fix code.

### /codex:rescue

Hands a task to Codex through thecodex:codex-rescuesubagent.

Use it when you want Codex to:

* investigate a bug
* try a fix
* continue a previous Codex task
* take a faster or cheaper pass with a smaller model

Note

Depending on the task and the model you choose these tasks might take a long time and it's generally recommended to force the task to be in the background or move the agent to the background.

It supports--background,--wait,--resume, and--fresh. If you omit--resumeand--fresh, the plugin can offer to continue the latest rescue thread for this repo.

Examples:

/codex:rescue investigate why the tests started failing
/codex:rescue fix the failing
test
 with the smallest safe patch
/codex:rescue --resume apply the top fix from the last run
/codex:rescue --model gpt-5.4-mini --effort medium investigate the flaky integration
test

/codex:rescue --model spark fix the issue quickly
/codex:rescue --background investigate the regression

You can also just ask for a task to be delegated to Codex:

Ask Codex to redesign the database connection to be more resilient.

Notes:

* if you do not pass--modelor--effort, Codex chooses its own defaults.
* if you sayspark, the plugin maps that togpt-5.3-codex-spark
* follow-up rescue requests can continue the latest Codex task in the repo

### /codex:status

Shows running and recent Codex jobs for the current repository.

Examples:

/codex:status
/codex:status task-abc123

Use it to:

* check progress on background work
* see the latest completed job
* confirm whether a task is still running

### /codex:result

Shows the final stored Codex output for a finished job.
When available, it also includes the Codex session ID so you can reopen that run directly in Codex withcodex resume <session-id>.

Examples:

/codex:result
/codex:result task-abc123

### /codex:cancel

Cancels an active background Codex job.

Examples:

/codex:cancel
/codex:cancel task-abc123

### /codex:setup

Checks whether Codex is installed and authenticated.
If Codex is missing and npm is available, it can offer to install Codex for you.

You can also use/codex:setupto manage the optional review gate.

#### Enabling review gate

/codex:setup --enable-review-gate
/codex:setup --disable-review-gate

When the review gate is enabled, the plugin uses aStophook to run a targeted Codex review based on Claude's response. If that review finds issues, the stop is blocked so Claude can address them first.

Warning

The review gate can create a long-running Claude/Codex loop and may drain usage limits quickly. Only enable it when you plan to actively monitor the session.

## Typical Flows

### Review Before Shipping

/codex:review

### Hand A Problem To Codex

/codex:rescue investigate why the build is failing
in
 CI

### Start Something Long-Running

/codex:adversarial-review --background
/codex:rescue --background investigate the flaky
test

Then check in with:

/codex:status
/codex:result

## Codex Integration

The Codex plugin wraps theCodex app server. It uses the globalcodexbinary installed in your environment andapplies the same configuration.

### Common Configurations

If you want to change the default reasoning effort or the default model that gets used by the plugin, you can define that inside your user-level or project-levelconfig.toml. For example to always usegpt-5.4-minionhighfor a specific project you can add the following to a.codex/config.tomlfile at the root of the directory you started Claude in:

model
 =
"
gpt-5.4-mini
"

model_reasoning_effort
 =
"
xhigh
"

Your configuration will be picked up based on:

* user-level config in~/.codex/config.toml
* project-level overrides in.codex/config.toml
* project-level overrides only load when theproject is trusted

Check out the Codex docs for moreconfiguration options.

### Moving The Work Over To Codex

Delegated tasks and anystop gaterun can also be directly resumed inside Codex by runningcodex resumeeither with the specific session ID you received from running/codex:resultor/codex:statusor by selecting it from the list.

This way you can review the Codex work or continue the work there.

## FAQ

### Do I need a separate Codex account for this plugin?

If you are already signed into Codex on this machine, that account should work immediately here too. This plugin uses your local Codex CLI authentication.

If you only use Claude Code today and have not used Codex yet, you will also need to sign in to Codex with either a ChatGPT account or an API key.Codex is available with your ChatGPT subscription, andcodex loginsupports both ChatGPT and API key sign-in. Run/codex:setupto check whether Codex is ready, and use!codex loginif it is not.

### Does the plugin use a separate Codex runtime?

No. This plugin delegates through your localCodex CLIandCodex app serveron the same machine.

That means:

* it uses the same Codex install you would use directly
* it uses the same local authentication state
* it uses the same repository checkout and machine-local environment

### Will it use the same Codex config I already have?

Yes. If you already use Codex, the plugin picks up the sameconfiguration.

### Can I keep using my current API key or base URL setup?

Yes. Because the plugin uses your local Codex CLI, your existing sign-in method and config still apply.

If you need to point the built-in OpenAI provider at a different endpoint, setopenai_base_urlin yourCodex config.

## About

Use Codex from Claude Code to review code or delegate tasks.

### Resources

 Readme



### License

 Apache-2.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

11.5k

 stars


### Watchers

37

 watching


### Forks

600

 forks


 Report repository



## Releases3

v1.0.2

 Latest



Mar 31, 2026



+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* JavaScript100.0%
