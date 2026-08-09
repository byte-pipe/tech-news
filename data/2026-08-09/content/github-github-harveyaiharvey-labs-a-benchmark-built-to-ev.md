---
title: 'GitHub - harveyai/harvey-labs: A benchmark built to evaluate and improve agent capabilities for supporting legal work. · GitHub'
url: https://github.com/harveyai/harvey-labs
site_name: github
content_file: github-github-harveyaiharvey-labs-a-benchmark-built-to-ev
fetched_at: '2026-08-09T11:26:22.776650'
original_url: https://github.com/harveyai/harvey-labs
author: harveyai
description: A benchmark built to evaluate and improve agent capabilities for supporting legal work. - harveyai/harvey-labs
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 harveyai

 

/

harvey-labs

Public

* NotificationsYou must be signed in to change notification settings
* Fork170
* Star683

 
 
 
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

33 Commits
33 Commits
.github
.github
 
 
docs
docs
 
 
evaluation
evaluation
 
 
harness
harness
 
 
sandbox
sandbox
 
 
scripts
scripts
 
 
tasks
tasks
 
 
tests
tests
 
 
utils
utils
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Legal Agent Benchmark (LAB): An open-source benchmark for evaluating agents on real legal work.

Harvey LAB is an open-source project aimed at benchmarking LLM agents' abilities to perform legal work in realistic environments.

LAB consists of two parts: a dataset oftaskscontaining agent instructions, documents, and rubrics as well as anexecution harnessfor running and evaluating agents against those tasks.

LAB is an ongoing project and we expect to consistently add to and refine the task set and execution harness.

Read the announcement post:Introducing Harvey's Legal Agent Benchmark

## Getting Started

Start with the full walkthrough indocs/tutorial.md— it takes one realistic M&A data-room assignment end to end: setup, task inspection, agent run, scoring, report review, and comparison dashboards.

## Additional Documentation

Guide

Description

Architecture

Task model, harness, tools, adapters, reports, and sweeps

Evaluation Methodology

All-pass rubric scoring and LLM judge behavior

Contributing

Add tasks, model adapters, evaluation improvements, and docs

## Citation

If you use Harvey LAB in your research, please cite it as:

@misc
{
harveylab2026
,
 
title
 = 
{
Harvey LAB: The Legal Agent Benchmark
}
,
 
author
 = 
{
{Harvey AI}
}
,
 
year
 = 
{
2026
}
,
 
version
 = 
{
v1.0
}
,
 
url
 = 
{
https://github.com/harveyai/harvey-labs/tree/v1.0
}
,
 
note
 = 
{
Announcement: \url{https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark}
}

}