---
title: 'GitHub - PrimeIntellect-ai/prime-agent: A self-improving RLM agent for coding workflows and long-running autonomous tasks. · GitHub'
url: https://github.com/PrimeIntellect-ai/prime-agent
site_name: github
content_file: github-github-primeintellect-aiprime-agent-a-self-improvi
fetched_at: '2026-08-07T11:43:56.224158'
original_url: https://github.com/PrimeIntellect-ai/prime-agent
author: PrimeIntellect-ai
description: A self-improving RLM agent for coding workflows and long-running autonomous tasks. - PrimeIntellect-ai/prime-agent
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 PrimeIntellect-ai

 

/

prime-agent

Public

* NotificationsYou must be signed in to change notification settings
* Fork402
* Star5k

 
 
 
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

4,475 Commits
4,475 Commits
.github
.github
 
 
.husky
.husky
 
 
assets/
brand
assets/
brand
 
 
packages
packages
 
 
prime-agent-runtime
prime-agent-runtime
 
 
scripts
scripts
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
install.sh
install.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
prime-agent.sh
prime-agent.sh
 
 
test.sh
test.sh
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

### Prime Agent: A Self-Improving RLM Agent

Documentation•Verifiers•PRIME-RL•pi-mono

Prime Agent is an open-source coding and research agent for general and long-running work. It is designed around two core abstractions:

* TheRecursive Language Model (RLM)treats context as variables (prompt-as-a-variable) and tools like recursive subagents as function calls (programmatic tool /sub-agent calling) inside a persistent REPL.
* TheContinual Harnessstores supplemental prompts, memories, skill descriptions, and reusable subagent specifications as durable state that Prime Agent can refine through small, evidence-backed updates, local to the session by default.

Prime Agent combines a persistent Python control environment with durable harness state, so useful working context and reusable operating patterns can outlive a single chat window.

* Everything is programmatic:persistent IPython is the built-in model tool; file operations, shell commands, tool use, subagents, and context management happen through code.
* Subagents are built in:rlm(...)spawns real child agents for parallel or background work and returns their results programmatically.
* The harness can improve:/refinereviews the current trajectory and can apply small, evidence-backed updates to supplemental harness state. It never rewrites the immutable base system prompt, and recorded snapshots support rollback.
* Skills are executable:skills are importable Python packages, and the built-in skill creator can turn recurring workflows into project or personal skills.
* Sessions run in the background:daemon-backed agents keep running when the terminal disconnects and can be reattached later.
* Agents communicate directly:running agents can exchange messages and orchestrate one another without routing everything through the user.
* Long tasks keep moving:automatic compaction, persistent goals, heartbeats, schedules, autonomous mode, and retained subagents preserve progress across turns and terminal sessions.

## Getting Started

Install the latest stable release on macOS or Linux:

curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh 
|
 sh

The installer downloads a versioned release, verifies its SHA-256 checksum, installs theprime-agentcommand, and can prepare the IPython runtime used by the agent.

Start Prime Agent from the repository or directory you want it to work in:

cd
 /path/to/project
prime-agent

On first launch, run/loginto choose a subscription or API-key provider. Prime Agent works in the current directory and can run commands and modify files there. Use a disposable clone, clean worktree, or another checkpoint you can inspect and restore.

Warning

Prime Agent executes model-generated Python and project commands with your user permissions. Its worker and kernel processes improve lifecycle isolation and recovery; they arenota security sandbox. Review changes and use trusted repositories, instructions, skills, and extensions only. Run untrusted code or instructions in an external sandbox or restricted environment.

Useful commands:

prime-agent agents 
#
 Browse running, idle, and saved sessions

prime-agent attach 
<
agent
>
 
#
 Reattach to a running session

prime-agent --resume 
<
path
|
id
>
 
#
 Resume a saved session

prime-agent status 
#
 Inspect background service state

prime-agent doctor [--fix] 
#
 Inspect or repair background services

prime-agent update [--force] 
#
 Update Prime Agent

prime-agent shutdown [--force] 
#
 Stop every agent, worker, and background service

## Built for Long-Running Work

Prime Agent is built for long-running work, especially for evaluations in research. These features are available in the TUI, and when run autonomously.

* Continual Harness:/refinecan persist focused, reviewable lessons as supplemental prompts, memories, reusable skill descriptions, or subagent specifications, with recorded refinement history. It does not replace packaging and reviewing new executable skills.
* Direct agent-to-agent communication:running agents and retained subagents can discover one another, exchange messages, and steer active work.
* Daemon-backed continuity:active sessions, IPython state, schedules, and subagents keep running when the terminal detaches and can be reattached later.
* Heartbeats and schedules:/heartbeat,rlm_heartbeat, andprime-agent schedulecan re-enter a session periodically or at a specific time.
* Persistent goals:/goalkeeps an objective and its progress active across turns until it is completed, paused, or cleared.
* Bounded autonomous mode:/autonomouscontinues within configured turn, token, and time budgets and can run user-defined quality gates. A passed gate checks only what that gate verifies; reaching a limit does not imply task success.

## Documentation

* Quickstart— install, authenticate, and run a first session
* Usage and CLI reference— commands, sessions, autonomous limits, and output modes
* Long-running and background agents— detach and reattach, goals, heartbeats, and schedules
* RLM programming model— persistent IPython, subagents, skills, and the trust model
* JSON modeandRPC mode— headless automation and integrations
* Skills— install and create reusable capabilities
* Provider setup— subscription and API-key providers
* Architecture overview— daemon, worker, kernel, and persistence boundaries
* Development— build and run from source

## Acknowledgements

Our agent and TUI is built on top ofpi. We thank the authors ofpifor their valuable work.

## License

Prime Agent is fully open source and released under theMIT License.