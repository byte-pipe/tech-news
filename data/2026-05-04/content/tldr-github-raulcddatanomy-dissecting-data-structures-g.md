---
title: 'GitHub - raulcd/datanomy: Dissecting data structures · GitHub'
url: https://github.com/raulcd/datanomy
site_name: tldr
content_file: tldr-github-raulcddatanomy-dissecting-data-structures-g
fetched_at: '2026-05-04T12:21:22.683902'
original_url: https://github.com/raulcd/datanomy
date: '2026-05-04'
description: Dissecting data structures. Contribute to raulcd/datanomy development by creating an account on GitHub.
tags:
- tldr
---

raulcd

 

/

datanomy

Public

* NotificationsYou must be signed in to change notification settings
* Fork8
* Star380

 
 
 
 
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

57 Commits
57 Commits
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
src/
datanomy
src/
datanomy
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
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

# Datanomy

Explore the anatomy of your columnar data files

Datanomyis a terminal-based tool for inspecting and understanding data files.
It provides an interactive view of your data's structure, metadata, and internal organization.

Currently only Parquet available:

## Features for Parquet view

### General Structure

### Schema

### Data

### Metadata

### Stats

## Installation

#
 From PyPI

uv tool install datanomy

#
# with pip

pip install datanomy

#
 From source

uv tool install 
"
datanomy @ git+https://github.com/raulcd/datanomy.git
"

#
# cloning the repo 

git clone https://github.com/raulcd/datanomy.git

cd
 datanomy
uv sync

## Usage

#
 Run without installing using uvx

uvx datanomy data.parquet

#
 Inspect a Parquet file

datanomy data.parquet

You can also use from source using uvx. This uses the development version:

uvx 
"
git+https://github.com/raulcd/datanomy.git
"
 data.parquet

## Keyboard Shortcuts

* q- Quit the application

## Development

#
 Install dependencies

uv sync

#
 Run from source

uv run datanomy path/to/file.parquet

#
 Install dev dependencies

uv sync --extra dev

#
 Run tests

uv run pytest

#
 Format code

uv run ruff format 
.

#
 Lint

uv run ruff check 
.

#
 Lint

uv run mypy 
.

## License

Apache License 2.0

## Contributing

Contributions welcome! Please open an issue or PR.

Built withTextualandPyArrow

## About

Dissecting data structures

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

380

 stars
 

### Watchers

4

 watching
 

### Forks

8

 forks
 

 Report repository

 

## Releases3

v0.3.0

 Latest

 

Apr 24, 2026

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%