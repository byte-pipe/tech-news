---
title: 'GitHub - hauntsaninja/git_bayesect: Bayesian git bisect · GitHub'
url: https://github.com/hauntsaninja/git_bayesect
site_name: hackernews_api
content_file: hackernews_api-github-hauntsaninjagit_bayesect-bayesian-git-bisec
fetched_at: '2026-04-02T11:20:46.093712'
original_url: https://github.com/hauntsaninja/git_bayesect
author: hauntsaninja
date: '2026-03-28'
description: Bayesian git bisect. Contribute to hauntsaninja/git_bayesect development by creating an account on GitHub.
tags:
- hackernews
- trending
---

hauntsaninja

 

/

git_bayesect

Public

* NotificationsYou must be signed in to change notification settings
* Fork1
* Star306

 
 
 
 
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

61 Commits
61 Commits
.github/
workflows
.github/
workflows
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
git_bayesect.py
git_bayesect.py
 
 
pyproject.toml
pyproject.toml
 
 
test_git_bayesect.py
test_git_bayesect.py
 
 
View all files

## Repository files navigation

# git bayesect

Bayesian git bisection!

Use this to detect changes in likelihoods of events, for instance, to isolate a commit where
a slightly flaky test became very flaky.

You don't need to know the likelihoods (although you can provide priors), just that something
has changed at some point in some direction

## Installation

pip install git_bayesect

Or:

uv tool install git_bayesect

## How it works

git_bayesectuses Bayesian inference to identify the commit introducing a change, with
commit selection performed via greedy minimisation of expected entropy, and using a Beta-Bernoulli
conjugacy trick while calculating posterior probabilities to make handling unknown failure rates
tractable.

Seehttps://hauntsaninja.github.io/git_bayesect.htmlfor a write up.

## Usage

Start a Bayesian bisection:

git bayesect start --old $COMMIT

Record an observation on the current commit:

git bayesect fail

Or on a specific commit:

git bayesect pass --commit $COMMIT

Check the overall status of the bisection:

git bayesect status

Reset:

git bayesect reset

## More usage

Set the prior for a given commit:

git bayesect prior --commit $COMMIT --weight 10

Set prior for all commits based on filenames:

git bayesect priors_from_filenames --filenames-callback "return 10 if any('suspicious' in f for f in filenames) else 1"

Set prior for all commits based on the text in the commit message + diff:

git bayesect priors_from_text --text-callback "return 10 if 'timeout' in text.lower() else 1"

Get a log of commands to let you reconstruct the state:

git bayesect log

Undo the last observation:

git bayesect undo

Run the bisection automatically using a command to make observations:

git bayesect run $CMD

Checkout the best commmit to test:

git bayesect checkout

## Demo

This repository contains a little demo, in case you'd like to play around:

# Create a fake repository with a history to bayesect over
python scripts/generate_fake_repo.py
cd fake_repo

# The fake repo contains a script called flaky.py
# This is a simple script that fails some fraction of the time
# At some point in the history of the repo, that fraction was changed
python flaky.py
git log --oneline

# Start the bayesection
OLD_COMMIT=$(git rev-list HEAD --reverse | head -n 2 | tail -n 1)
git bayesect start --new main --old $OLD_COMMIT

# Run a bayesection to find the commit that introduced the change
git bayesect run python flaky.py

## About

Bayesian git bisect

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

306

 stars
 

### Watchers

0

 watching
 

### Forks

1

 fork
 

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