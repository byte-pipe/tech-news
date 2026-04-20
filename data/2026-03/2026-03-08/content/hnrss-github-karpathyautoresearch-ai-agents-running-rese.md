---
title: 'GitHub - karpathy/autoresearch: AI agents running research on single-GPU nanochat training automatically · GitHub'
url: https://github.com/karpathy/autoresearch
site_name: hnrss
content_file: hnrss-github-karpathyautoresearch-ai-agents-running-rese
fetched_at: '2026-03-08T11:07:46.299846'
original_url: https://github.com/karpathy/autoresearch
date: '2026-03-07'
description: AI agents running research on single-GPU nanochat training automatically - karpathy/autoresearch
tags:
- hackernews
- hnrss
---

karpathy



/

autoresearch

Public

* NotificationsYou must be signed in to change notification settings
* Fork604
* Star4.9k




 
master
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
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
README.md
README.md
 
 
analysis.ipynb
analysis.ipynb
 
 
prepare.py
prepare.py
 
 
program.md
program.md
 
 
progress.png
progress.png
 
 
pyproject.toml
pyproject.toml
 
 
train.py
train.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# autoresearch

One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of "group meeting". That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies. The agents claim that we are now in the 10,205th generation of the code base, in any case no one could tell if that's right or wrong as the "code" is now a self-modifying binary that has grown beyond human comprehension. This repo is the story of how it all began. -@karpathy, March 2026.

The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. You wake up in the morning to a log of experiments and (hopefully) a better model. The training code here is a simplified single-GPU implementation ofnanochat. The core idea is that you're not touching any of the Python files like you normally would as a researcher. Instead, you are programming theprogram.mdMarkdown files that provide context to the AI agents and set up your autonomous research org. The defaultprogram.mdin this repo is intentionally kept as a bare bones baseline, though it's obvious how one would iterate on it over time to find the "research org code" that achieves the fastest research progress, how you'd add more agents to the mix, etc. A bit more context on this project is here in thistweet.

## How it works

The repo is deliberately kept small and only really has a three files that matter:

* prepare.py— fixed constants, one-time data prep (downloads training data, trains a BPE tokenizer), and runtime utilities (dataloader, evaluation). Not modified.
* train.py— the single file the agent edits. Contains the full GPT model, optimizer (Muon + AdamW), and training loop. Everything is fair game: architecture, hyperparameters, optimizer, batch size, etc.This file is edited and iterated on by the agent.
* program.md— baseline instructions for one agent. Point your agent here and let it go.This file is edited and iterated on by the human.

By design, training runs for afixed 5-minute time budget(wall clock, excluding startup/compilation), regardless of the details of your compute. The metric isval_bpb(validation bits per byte) — lower is better, and vocab-size-independent so architectural changes are fairly compared.

## Quick start

Requirements:A single NVIDIA GPU (tested on H100), Python 3.10+,uv.

#
 1. Install uv project manager (if you don't already have it)

curl -LsSf https://astral.sh/uv/install.sh
|
 sh

#
 2. Install dependencies

uv sync

#
 3. Download data and train tokenizer (one-time, ~2 min)

uv run prepare.py

#
 4. Manually run a single training experiment (~5 min)

uv run train.py

If the above commands all work ok, your setup is working and you can go into autonomous research mode.

Platforms support. This code currently requires that you have a single NVIDIA GPU. In principle it is quite possible to support CPU, MPS and other platforms but this would also bloat the code. I'm not 100% sure that I want to take this on personally right now. The code is just a demonstration and I don't know how much I'll support it going forward. People can reference (or have their agents reference) the full/parent nanochat repository that has wider platform support and shows the various solutions (e.g. a Flash Attention 3 kernels fallback implementation, generic device support, autodetection, etc.), feel free to create forks or discussions for other platforms and I'm happy to link to them here in the README in some new notable forks section or etc.

## Running the agent

Simply spin up your Claude/Codex or whatever you want in this repo (and disable all permissions), then you can prompt something like:

Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.

Theprogram.mdfile is essentially a super lightweight "skill".

## Project structure

prepare.py — constants, data prep + runtime utilities (do not modify)
train.py — model, optimizer, training loop (agent modifies this)
program.md — agent instructions
pyproject.toml — dependencies

## Design choices

* Single file to modify.The agent only touchestrain.py. This keeps the scope manageable and diffs reviewable.
* Fixed time budget.Training always runs for exactly 5 minutes, regardless of your specific platform. This means you can expect approx 12 experiments/hour and approx 100 experiments while you sleep. There are two upsides of this design decision. First, this makes experiments directly comparable regardless of what the agent changes (model size, batch size, architecture, etc). Second, this means that autoresearch will find the most optimal model for your platform in that time budget. The downside is that your runs (and results) become not comparable to other people running on other compute platforms.
* Self-contained.No external dependencies beyond PyTorch and a few small packages. No distributed training, no complex configs. One GPU, one file, one metric.

## Notable forks

* miolini/autoresearch-macos

## License

MIT

## About

AI agents running research on single-GPU nanochat training automatically

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

4.9k

 stars


### Watchers

48

 watching


### Forks

604

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors5

## Languages

* Python83.4%
* Jupyter Notebook16.6%
