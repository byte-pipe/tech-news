---
title: 'GitHub - Dimillian/Skills: My Codex Skills · GitHub'
url: https://github.com/Dimillian/Skills
site_name: github
content_file: github-github-dimillianskills-my-codex-skills-github
fetched_at: '2026-03-31T11:22:18.063600'
original_url: https://github.com/Dimillian/Skills
author: Dimillian
description: My Codex Skills. Contribute to Dimillian/Skills development by creating an account on GitHub.
---

Dimillian



/

Skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork141
* Star2.7k




 
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

55 Commits
55 Commits
app-store-changelog
app-store-changelog
 
 
bug-hunt-swarm
bug-hunt-swarm
 
 
docs
docs
 
 
github
github
 
 
ios-debugger-agent
ios-debugger-agent
 
 
macos-menubar-tuist-app
macos-menubar-tuist-app
 
 
macos-spm-app-packaging
macos-spm-app-packaging
 
 
orchestrate-batch-refactor
orchestrate-batch-refactor
 
 
project-skill-audit
project-skill-audit
 
 
react-component-performance
react-component-performance
 
 
review-and-simplify-changes
review-and-simplify-changes
 
 
review-swarm
review-swarm
 
 
scripts
scripts
 
 
swift-concurrency-expert
swift-concurrency-expert
 
 
swiftui-liquid-glass
swiftui-liquid-glass
 
 
swiftui-performance-audit
swiftui-performance-audit
 
 
swiftui-ui-patterns
swiftui-ui-patterns
 
 
swiftui-view-refactor
swiftui-view-refactor
 
 
.DS_Store
.DS_Store
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Skills Public

A collection of reusable development skills for Apple platforms, GitHub workflows, refactoring, diff review swarms, bug investigation swarms, code review, React performance work, and skill curation.

## Overview

This repository contains focused, self-contained skills that help with recurring engineering tasks such as generating App Store release notes, debugging iOS apps, improving SwiftUI and React code, packaging macOS apps, running multi-agent diff reviews and bug hunts, reviewing and simplifying code changes, orchestrating larger refactors, and auditing what new skills a project actually needs.

Install: place these skill folders under$CODEX_HOME/skills

## Skills

This repo currently includes 16 skills:

Skill

Folder

Description

App Store Changelog

app-store-changelog

Creates user-facing App Store release notes from git history by collecting changes since the last tag, filtering for user-visible work, and rewriting it into concise "What's New" bullets.

GitHub

github

Uses the
gh
 CLI to inspect and operate on GitHub issues, pull requests, workflow runs, and API data, including CI checks, run logs, and advanced queries.

iOS Debugger Agent

ios-debugger-agent

Uses XcodeBuildMCP to build, launch, and debug the current iOS app on a booted simulator, including UI inspection, interaction, screenshots, and log capture.

macOS Menubar Tuist App

macos-menubar-tuist-app

Builds, refactors, or reviews macOS menubar apps that use Tuist and SwiftUI, with emphasis on manifest ownership, store-layer architecture, and reliable local launch scripts.

macOS SwiftPM App Packaging (No Xcode)

macos-spm-app-packaging

Scaffolds, builds, packages, signs, and optionally notarizes SwiftPM-based macOS apps without requiring an Xcode project.

Orchestrate Batch Refactor

orchestrate-batch-refactor

Plans and executes larger refactor or rewrite efforts with dependency-aware parallel analysis and implementation using clearly scoped work packets.

Project Skill Audit

project-skill-audit

Analyzes a project's past Codex sessions, memory, existing local skills, and conventions to recommend the highest-value new skills or updates to existing ones.

React Component Performance

react-component-performance

Diagnoses slow React components by finding re-render churn, expensive render work, unstable props, and list bottlenecks, then suggests targeted optimizations and validation steps.

Bug Hunt Swarm

bug-hunt-swarm

Runs a read-only four-agent bug investigation focused on reproduction, code-path tracing, regressors, and the fastest proof step, then returns a ranked root-cause path.

Review and Simplify Changes

review-and-simplify-changes

Reviews a git diff or explicit file scope for reuse, code quality, efficiency, clarity, and standards issues, then optionally applies safe, behavior-preserving fixes.

Review Swarm

review-swarm

Runs a read-only four-agent diff review focused on behavioral regressions, security risks, performance or reliability issues, and contract or test coverage gaps, then returns a prioritized fix path.

Swift Concurrency Expert

swift-concurrency-expert

Reviews and fixes Swift 6.2+ concurrency issues such as actor isolation problems,
Sendable
 violations, main-actor annotations, and data-race diagnostics.

SwiftUI Liquid Glass

swiftui-liquid-glass

Implements, reviews, or refactors SwiftUI features to use the iOS 26+ Liquid Glass APIs correctly, with proper modifier ordering, grouping, interactivity, and fallbacks.

SwiftUI Performance Audit

swiftui-performance-audit

Audits SwiftUI runtime performance from code and architecture, focusing on invalidation storms, identity churn, layout thrash, heavy render work, and profiling guidance.

SwiftUI UI Patterns

swiftui-ui-patterns

Provides best practices and example-driven guidance for building SwiftUI screens and components, including navigation, sheets, app wiring, async state, and reusable UI patterns.

SwiftUI View Refactor

swiftui-view-refactor

Refactors SwiftUI view files toward smaller subviews, MV-style data flow, stable view trees, explicit dependency injection, and correct Observation usage.

## Usage

Each skill is self-contained. Refer to theSKILL.mdfile in each skill directory for triggers, workflow guidance, examples, and supporting references.

## Contributing

Skills are designed to be focused and reusable. When adding new skills, ensure they:

* Have a clear, single purpose
* Include comprehensive documentation
* Follow consistent patterns with existing skills
* Include reference materials when applicable

## About

My Codex Skills

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

2.7k

 stars


### Watchers

31

 watching


### Forks

141

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

* Shell84.6%
* Python12.8%
* Swift2.6%
