---
title: 'Reviving Open Source Giants: How I Brought Weave Scope Back with Multi-Platform Docker Support in One Afternoon Using Antigravity - DEV Community'
url: https://dev.to/gde/reviving-open-source-giants-how-i-brought-weave-scope-back-with-multi-platform-docker-support-in-cmo
site_name: devto
content_file: devto-reviving-open-source-giants-how-i-brought-weave-sc
fetched_at: '2026-08-15T11:17:41.606507'
original_url: https://dev.to/gde/reviving-open-source-giants-how-i-brought-weave-scope-back-with-multi-platform-docker-support-in-cmo
author: Mario Ezquerro
date: '2026-08-14'
description: How to rescue abandoned open-source projects, modernize build systems, and generate multi-architecture Docker images (x86_64, ARM64) in a single afternoon with Antigravity. Tagged with opensource, devops, docker, ai.
tags: '#opensource, #devops, #docker, #ai'
---

The open-source ecosystem is full of architectural masterpieces that—due to corporate pivots, lack of maintainers, or shifting market focus—eventually get frozen in time. One of the most prominent examples isWeave Scope: a legendary tool for visual monitoring, real-time mapping, and debugging container clusters.

When the original repository was archived and left unmaintained, its dependency tree froze and it remained strictly tied tox86_64architectures. In today’s world, with the widespread adoption of ARM servers (AWS Graviton, Apple Silicon, Raspberry Pi clusters, etc.), running the original build has become nearly impossible.

I set out to rescue it, modernize its build pipelines, and create multi-platform Docker images.The result?The project is back to life atgithub.com/mario-ezquerro/scopewith multi-arch Docker images live onDocker Hub.

The best part:the entire journey took a single afternoon and a few tokens thanks to Antigravity.

## The Challenge: Brilliant Code Locked in the Past

Weave Scope is far from a trivial codebase. Its architecture integrates:

* Low-level kernel probes and agents written inGoandeBPF.
* A reactive, interactive web UI.
* Complex legacy Makefiles and container toolchains originally engineered exclusively foramd64/x86_64.

Manually upgrading this stack to moderndocker buildxworkflows with native support for bothARM64andAMD64would traditionally mean days of painful software archaeology: resolving broken Go packages, outdated C libraries, incompatible packaging scripts, and compilation errors.

## The Catalyst: Antigravity as a Software Rescue Agent

This is whereAntigravitymakes an extraordinary difference.

Instead of spending days fighting legacyMakefilesand deprecated toolchains, I leveraged Antigravity to parse the repository structure, diagnose build blockers, and modernize the compilation and packaging pipeline for multi-architecture targets.

What used to be a tedious migration became an agile, iterative session:

1. Dependency Audit & Fixes:Identifying system calls and C bindings that prevented cross-compilation.
2. Dockerfile & Buildx Refactoring:Modernizing the multi-stage build pipeline to compile native binaries for bothlinux/amd64andlinux/arm64.
3. Automated Publishing:Generating multi-arch manifest lists and pushing them directly to Docker Hub.

## The Modernized Multi-Arch Scope

The revived project is ready for the community:

* New GitHub Repository:https://github.com/mario-ezquerro/scope
* Original Repository (Legacy):https://github.com/weaveworks/scope
* Docker Hub Multi-Arch Images:Ready to deploy on both x86 and ARM infrastructure.

### Quick Start

Run the probe and visualization UI on any local machine or server (including Apple Silicon and Raspberry Pi clusters):

# Pull and run Scope with multi-arch support

docker run 
-d
 
--name
 weave-scope 
\

 
--net
=
host 
\

 
--pid
=
host 
\

 
--privileged
 
\

 
-v
 /var/run/docker.sock:/var/run/docker.sock 
\

 marioezquerro/scope:latest
Open your browser at http://localhost:4040 to see your real-time container topology 
in 
action.

Enter fullscreen mode

Exit fullscreen mode

Takeaway: A Golden Era for Open Source MaintenanceThe true power of modern AI platforms like Antigravity isn't just generating boilerplate code from scratch—it is their astonishing capability for software restoration and modernization.

GitHub contains thousands of brilliant, abandoned projects that simply need an afternoon of care, dependency updates, and container modernization. With a single afternoon and a handful of tokens, any developer now has the superpower to revive forgotten open-source gems and give them back to the global community.

What abandoned open-source project is on your wishlist to revive next? Let me know in the comments!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse