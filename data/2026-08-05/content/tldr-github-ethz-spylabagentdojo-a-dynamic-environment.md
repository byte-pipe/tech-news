---
title: 'GitHub - ethz-spylab/agentdojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. · GitHub'
url: https://github.com/ethz-spylab/agentdojo
site_name: tldr
content_file: tldr-github-ethz-spylabagentdojo-a-dynamic-environment
fetched_at: '2026-08-05T06:00:34.411111'
original_url: https://github.com/ethz-spylab/agentdojo
date: '2026-08-05'
description: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. - ethz-spylab/agentdojo
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 ethz-spylab

 

/

agentdojo

Public

* NotificationsYou must be signed in to change notification settings
* Fork187
* Star714

 
 
 
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

722 Commits
722 Commits
.devcontainer
.devcontainer
 
 
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
examples
examples
 
 
notebooks
notebooks
 
 
runs
runs
 
 
src/
agentdojo
src/
agentdojo
 
 
tests
tests
 
 
util_scripts
util_scripts
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
CITATION.bib
CITATION.bib
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

 

 
 

Edoardo Debenedetti1,Jie Zhang1,Mislav Balunović1,2,Luca Beurer-Kellner1,2,Marc Fischer1,2,Florian Tramèr1

1ETH Zurich and2Invariant Labs

Read Paper|Inspect Results

## Quickstart

pip install agentdojo

Important

Note that the API of the package is still under development and might change in the future.

If you want to use the prompt injection detector, you need to install thetransformersextra:

pip install 
"
agentdojo[transformers]
"

## Running the benchmark

The benchmark can be run with thebenchmarkscript. Documentation on how to use the script can be obtained with the--helpflag.

For example, to run theworkspacesuite on the tasks 0 and 1, withgpt-4o-2024-05-13as the LLM, the tool filter as a defense, and the attack with tool knowlege, run the following command:

python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 \
 -ut user_task_1 --model gpt-4o-2024-05-13 \
 --defense tool_filter --attack tool_knowledge

To run the above, but on all suites and tasks, run the following:

python -m agentdojo.scripts.benchmark --model gpt-4o-2024-05-13 \
 --defense tool_filter --attack tool_knowledge

## Inspect the results

To inspect the results, go to the dedicatedresults pageof the documentation. AgentDojo results are also listed in theInvariant Benchmark Registry.Agent

## Documentation of the Dojo

Take a look at ourdocumentation.

## Development set-up

Take a look at thedevelopment set-updocs.

## Citing

If you use AgentDojo in your research, please consider citing our paper:

@inproceedings
{
 debenedetti2024agentdojo,
 
title
=
{
AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for {LLM} Agents
}
,
 
author
=
{
Edoardo Debenedetti and Jie Zhang and Mislav Balunovic and Luca Beurer-Kellner and Marc Fischer and Florian Tram{\`e}r
}
,
 
booktitle
=
{
The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track
}
,
 
year
=
{
2024
}
,
 
url
=
{
https://openreview.net/forum?id=m1YYAQjO3w
}

}