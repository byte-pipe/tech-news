---
title: linux/Documentation/process/coding-assistants.rst at master · torvalds/linux · GitHub
url: https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst
site_name: hackernews_api
content_file: hackernews_api-linuxdocumentationprocesscoding-assistantsrst-at-m
fetched_at: '2026-04-11T11:12:40.149729'
original_url: https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst
author: hmokiguess
date: '2026-04-10'
description: Linux kernel source tree. Contribute to torvalds/linux development by creating an account on GitHub.
tags:
- hackernews
- trending
---

torvalds



/

linux

Public

* NotificationsYou must be signed in to change notification settings
* Fork61.5k
* Star228k







## FilesExpand file tree

 
master
/

# coding-assistants.rst

Copy path
Blame
More file actions
Blame
More file actions


## Latest commit

 

## History

History
History
59 lines (40 loc) · 1.82 KB
 
master
/

# coding-assistants.rst

Top

## File metadata and controls

* Preview
* Code
* Blame
59 lines (40 loc) · 1.82 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions

# AI Coding Assistants

This document provides guidance for AI tools and developers using AI
assistance when contributing to the Linux kernel.

AI tools helping with Linux kernel development should follow the standard
kernel development process:

* Documentation/process/development-process.rst
* Documentation/process/coding-style.rst
* Documentation/process/submitting-patches.rst

## Licensing and Legal Requirements

All contributions must comply with the kernel's licensing requirements:

* All code must be compatible with GPL-2.0-only
* Use appropriate SPDX license identifiers
* See Documentation/process/license-rules.rst for details

## Signed-off-by and Developer Certificate of Origin

AI agents MUST NOT add Signed-off-by tags. Only humans can legally
certify the Developer Certificate of Origin (DCO). The human submitter
is responsible for:

* Reviewing all AI-generated code
* Ensuring compliance with licensing requirements
* Adding their own Signed-off-by tag to certify the DCO
* Taking full responsibility for the contribution

## Attribution

When AI tools contribute to kernel development, proper attribution
helps track the evolving role of AI in the development process.
Contributions should include an Assisted-by tag in the following format:

Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]

Where:

* AGENT_NAMEis the name of the AI tool or framework
* MODEL_VERSIONis the specific model version used
* [TOOL1] [TOOL2]are optional specialized analysis tools used
(e.g., coccinelle, sparse, smatch, clang-tidy)

Basic development tools (git, gcc, make, editors) should not be listed.

Example:

Assisted-by: Claude:claude-3-opus coccinelle sparse
