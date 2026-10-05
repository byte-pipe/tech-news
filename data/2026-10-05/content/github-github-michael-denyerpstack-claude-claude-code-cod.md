---
title: 'GitHub - michael-denyer/pstack-claude: Claude Code, Codex, Pi, OpenCode, Gemini, and Prime Agent versions of Poteto''s pstack. Rigorous agent workflows with Cursor primitives translated for other harnesses. · GitHub'
url: https://github.com/michael-denyer/pstack-claude
site_name: github
content_file: github-github-michael-denyerpstack-claude-claude-code-cod
fetched_at: '2026-10-05T12:19:29.774646'
original_url: https://github.com/michael-denyer/pstack-claude
author: michael-denyer
description: Claude Code, Codex, Pi, OpenCode, Gemini, and Prime Agent versions of Poteto's pstack. Rigorous agent workflows with Cursor primitives translated for other harnesses. - michael-denyer/pstack-claude
---

michael-denyer

 

/

pstack-claude

Public

* NotificationsYou must be signed in to change notification settings
* Fork129
* Star1.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

169 Commits
169 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
assets
assets
 
 
docs
docs
 
 
plugins/
pstack
plugins/
pstack
 
 
tests
tests
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.markdownlint-cli2.jsonc
.markdownlint-cli2.jsonc
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CHANGES.md
CHANGES.md
 
 
CONTEXT.md
CONTEXT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
LICENSE-cursor-team-kit
LICENSE-cursor-team-kit
 
 
NOTICE-skills.md
NOTICE-skills.md
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
VERSION
VERSION
 
 
bun.lock
bun.lock
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# pstack

Lauren Tan'spstackis an opinionated Cursor skill stack that improves agent outcomes. This is a port for Claude Code, Codex, Pi and other agent harnesses. It tracks upstream and also carries named policy forks, each declared intools/forks.json.

Tellpoteto-modeyour goal and it will invoke the correct workflow for the task. It keeps your code concise, simple and verified.

For concurrency bugs and invariants that tests cannot reach, see the separateagent-formal-verifyplugin, which adds TLA+ model checking and Lean proofs.

## Install

### Claude Code

Run in Claude Code:

/plugin marketplace add michael-denyer/pstack-claude
/plugin install pstack@pstack-claude

### Codex

Run in your terminal:

codex plugin marketplace add michael-denyer/pstack-claude
codex plugin add pstack@pstack-claude

### Pi

Run in your terminal:

pi install git:github.com/michael-denyer/pstack-claude

The package loads the skills and the pstack Pi extension, which adds the subagent, question, and wake-up tools the skills use, plus/loopand the routing instruction. Invoke a skill with/skill:<name>.

Runsetup-pstackto change model defaults, set a reasoning effort per role (for examplearena runners: opus @xhigh, fable @max, which Claude Code dispatches through the plugin'spstack:effort-<level>orpstack:poteto-agent-<level>agents; roles without a level keep the session's effort unless the sheet'sdefault effortline names one), or turn automatic routing off. The plugin installs the routing hook on Claude Code and Codex; Codex asks you to trust it through/hooksbefore it runs. On Pi the extension injects the same routing instruction. In Claude Code, use/pstack:setup-pstack.

For Prime Agent, OpenCode, Gemini CLI, or skills-only installs for any harness, seeshared installation.

## Getting started

Use poteto-mode to fix the search filter resetting when I change pages.

For a bug, it reproduces the failure, useshowandwhyto investigate, delegates the fix, then reruns the failing case. If the fix crosses a function boundary, it brings inarchitectbefore implementation. You receive the fix and the failing and passing evidence.

Other playbookscover planning, features, refactoring, performance issues, investigations, prototypes, PR maintenance, shipping, and longer projects.

## Details

* Skills and slash commands
* Runtime setup
* Models and dependencies
* Maintenance and port scope

## Data handling

pstack has no server or telemetry. Anything its skills ask your agent to read, including session transcripts, goes to your model provider. Scripts run locally, and PR tools use your GitHub CLI login.

## Contributing

Thanks for helping make this port better. Bug reports, documentation fixes, and runtime improvements are welcome. SeeCONTRIBUTING.mdfor the checks and where your change belongs. Report vulnerabilities privately as described inSECURITY.md.

## License

This port, including its modifications and additions, is alsoMIT-licensed, © 2026 Michael Denyer. Original pstack © 2026 Lauren Tan; imported cursor-team-kit skills © 2026 Cursor. SeeLICENSE-cursor-team-kitandNOTICE.md.