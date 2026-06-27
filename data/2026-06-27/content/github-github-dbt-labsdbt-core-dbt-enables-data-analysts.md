---
title: 'GitHub - dbt-labs/dbt-core: dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications. · GitHub'
url: https://github.com/dbt-labs/dbt-core
site_name: github
content_file: github-github-dbt-labsdbt-core-dbt-enables-data-analysts
fetched_at: '2026-06-27T11:33:43.608233'
original_url: https://github.com/dbt-labs/dbt-core
author: dbt-labs
description: dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications. - dbt-labs/dbt-core
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 dbt-labs

 

/

dbt-core

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.4k
* Star13.1k

 
 
 
 
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

10,421 Commits
10,421 Commits
.cargo
.cargo
 
 
.changes
.changes
 
 
.github
.github
 
 
assets
assets
 
 
certificates
certificates
 
 
crates
crates
 
 
docs/
roadmap
docs/
roadmap
 
 
lib
lib
 
 
.changie.yaml
.changie.yaml
 
 
.gitignore
.gitignore
 
 
CHANGELOG-fusion.md
CHANGELOG-fusion.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

Warning

dbt Core v1 development has moved to the1.latestbranch.Themainbranch now hosts dbt Core v2.0 (alpha) — a ground-up rewrite in Rust that is the foundation of the Fusion engine. If you're looking for the Python implementation of dbt Core, switch to1.latest.

dbtenables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

## About dbt Core v2.0

🚧 dbt Core v2.0 is in alpha. Behavior, APIs, and on-disk formats may change before the stable release.

dbt Core v2.0 is engineered for performance at scale — parsing, compiling, and running projects in a fraction of the time compared to v1. It's released under the Apache 2.0 license and is the foundation of theFusion engine.

The big shifts from v1:

* Faster— parse and compile times are dramatically improved, especially on the largest dbt projects.
* Stricter— a tightly-defined language specification enforces correctness at parse time.
* More scalable artifacts— v2.0 produces Parquet artifacts that can be easily queried, joined, and analyzed to understand your dbt project. The artifacts encompass everything in the JSON artifacts (e.g.manifest.json), which continue to be produced for backwards compatibility.
* Easier to install— distributed as a single self-contained binary, with no Python runtime or dependency management required.
* A completely revamped local documentation experience— dbt docs is now powered by those new artifacts and capable of scaling to large projects.

### Supported operating systems and architectures

dbt Core v2.0 and its drivers are compiled per operating system and architecture.

Legend:

* 🟢 — Supported today
* 🟡 — Not yet supported

Operating system

x86-64

ARM

macOS

🟢

🟢

Linux

🟢

🟢

Windows

🟢

🟡

## Understanding dbt

Analysts using dbt can transform their data by simply writing select statements, while dbt handles turning these statements into tables and views in a data warehouse.

These select statements, or "models", form a dbt project. Models frequently build on top of one another – dbt makes it easy tomanage relationshipsbetween models, andvisualize these relationships, as well as assure the quality of your transformations throughtesting.

## Getting started

Start by choosing a distribution. dbt Core is the baseline distribution of dbt. Fusion extends dbt Core with additional SQL comprehension abilities. Both distributions are free to install and can run locally.

* If you need an Apache 2.0 licensed tooland the ability to review every line of code inside of it,install dbt Core.
* If you need a free CLI you can use locally,install Fusion. It can do more than dbt Core out of the box and you can seamlessly enable other advanced features over time if you choose to.

Regardless of the distribution you choose, each is part of a single framework with a single language specification, meaning your business logic is portable in both directions.

Explore thedbt platformfor an enhanced collaboration experience.
Read theintroductionandviewpoint

## Join the dbt Community

* Be part of the conversation in thedbt Community Slack
* Read more on thedbt Community Discourse

## Reporting bugs and contributing code

* Want to report a bug or request a feature? Let us know and openan issue
* Want to help us build dbt? Check out theContributing Guide

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow thedbt Code of Conduct.

## License

dbt Core is licensed under theApache License 2.0.

## About

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

getdbt.com

### Topics

 slack

 analytics

 dbt-viewpoint

 pypa

 business-intelligence

 elt

 data-modeling

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

13.1k

 stars
 

### Watchers

159

 watching
 

### Forks

2.4k

 forks
 

 Report repository

 

## Releases327

dbt-core v1.11.11

 Latest

 

May 20, 2026

 

+ 326 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by9.5k

 + 9,487
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.1%
* Python0.3%
* Shell0.2%
* PowerShell0.2%
* PLpgSQL0.1%
* C0.1%