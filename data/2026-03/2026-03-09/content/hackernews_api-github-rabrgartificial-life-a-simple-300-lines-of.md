---
title: 'GitHub - Rabrg/artificial-life: A simple (300 lines of code) reproduction of Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction · GitHub'
url: https://github.com/Rabrg/artificial-life
site_name: hackernews_api
content_file: hackernews_api-github-rabrgartificial-life-a-simple-300-lines-of
fetched_at: '2026-03-09T19:20:10.013611'
original_url: https://github.com/Rabrg/artificial-life
author: tosh
date: '2026-03-08'
description: 'A simple (300 lines of code) reproduction of Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction - Rabrg/artificial-life'
tags:
- hackernews
- trending
---

Rabrg



/

artificial-life

Public

* NotificationsYou must be signed in to change notification settings
* Fork15
* Star210




 
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

8 Commits
8 Commits
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
README.md
README.md
 
 
main.py
main.py
 
 
pyproject.toml
pyproject.toml
 
 
universe.gif
universe.gif
 
 
universe.mp4
universe.mp4
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# artificial-life

A simple (300 lines of code) reproduction ofComputational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction.

## Program description

A 240x135 grid of 64 instruction-lengthBrainfuck-like programs are randomly initialized. Every iteration, neighboring programs are randomly paired, have their instruction tapes concattenated together, and are run for a maximum of$2^{13}$steps. Once execution completes, the tapes are split back apart. The instructions are such that they can loop and mutate the instruction tapes (programs) themselves. As found in the paper, self-replicating programs that copy themselves over their neighbor's tape often spontaneously emerge, which soon spread to take over the entire grid.

## Example simulation

Every pixel is an instruction; each instruction has a unique color, while black represents a value on the tape that is raw data storage / not an instruction. Every 8x8 section of pixels represents a single program.

uv run main.py --seed 1

In this run, a self-replicator emerges relatively early on into the run and soon takes over most of the grid, until a more efficient self-replicator evolves and takes over everything.

## About

A simple (300 lines of code) reproduction of Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

210

 stars


### Watchers

0

 watching


### Forks

15

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

* Python100.0%
