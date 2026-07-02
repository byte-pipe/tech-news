---
title: 'GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub'
url: https://github.com/agentskills/agentskills
site_name: github
content_file: github-github-agentskillsagentskills-specification-and-do
fetched_at: '2026-07-02T11:50:30.767246'
original_url: https://github.com/agentskills/agentskills
author: agentskills
description: Specification and documentation for Agent Skills. Contribute to agentskills/agentskills development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 agentskills

 

/

agentskills

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star21.4k

 
 
 
 
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

127 Commits
127 Commits
.claude
.claude
 
 
docs
docs
 
 
skills-ref
skills-ref
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Agent Skills

A standardized way to give AI agents new capabilities and expertise.

## What are Agent Skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing aSKILL.mdfile. This file includes metadata (nameanddescription, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.

my-skill/
├── SKILL.md # Required: metadata + instructions
├── scripts/ # Optional: executable code
├── references/ # Optional: documentation
├── assets/ # Optional: templates, resources
└── ... # Any additional files or directories

## Why Agent Skills?

Agents are increasingly capable, but often don't have the context they need to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand. This gives agents:

* Domain expertise: Capture specialized knowledge — from legal review processes to data analysis pipelines to presentation formatting — as reusable instructions and resources.
* Repeatable workflows: Turn multi-step tasks into consistent, auditable procedures.
* Cross-product reuse: Build a skill once and use it across any skills-compatible agent.

## How do Agent Skills work?

Agents load skills throughprogressive disclosure, in three stages:

1. Discovery: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
2. Activation: When a task matches a skill's description, the agent reads the fullSKILL.mdinstructions into context.
3. Execution: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.

Full instructions load only when a task calls for them, so agents can keep many skills on hand with only a small context footprint.

## Where can I use Agent Skills?

Agent Skills are supported by a large number of AI tools and agentic clients — see theClient Showcaseto explore some of them!

## Getting started

* Documentation— Guides and tutorials
* Specification— Format details
* Example Skills— See what's possible
* Discord— Share what you're building!

## Open development

The Agent Skills format was originally developed byAnthropic, released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem — seeCONTRIBUTING.mdfor how to get involved.

## License

Code in this repository is licensed underApache 2.0. Documentation is licensed underCC-BY-4.0. See individual directories for details.

## About

Specification and documentation for Agent Skills

agentskills.io

### Topics

 agent-skills

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

21.4k

 stars
 

### Watchers

181

 watching
 

### Forks

1.4k

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

* Python99.1%
* Shell0.9%