---
title: DO_NOT_TRACK
url: https://donottrack.sh/
site_name: hackernews_api
content_file: hackernews_api-do_not_track
fetched_at: '2026-05-03T11:40:51.024377'
original_url: https://donottrack.sh/
author: donottrack.sh
date: '2026-05-02'
description: DO_NOT_TRACK — A proposed standard environment variable for opting out of telemetry, analytics, and tracking in CLI and TUI applications.
tags:
- hackernews
- trending
---

## The Problem

Many CLI tools, SDKs, and frameworks collect telemetry data by default.
 Each one has its own way to opt out:

Tool

Opt-out method

.NET

DOTNET_CLI_TELEMETRY_OPTOUT=1

Copy

AWS SAM CLI

SAM_CLI_TELEMETRY=0

Copy

Azure CLI

AZURE_CORE_COLLECT_TELEMETRY=0

Copy

Gatsby

GATSBY_TELEMETRY_DISABLED=1

Copy

Go

go telemetry off

Copy

Google Cloud SDK

gcloud config set disable_usage_reporting true

Copy

Homebrew

HOMEBREW_NO_ANALYTICS=1

Copy

Netlify CLI

netlify --telemetry-disable

Copy

Syncthing

STNOUPGRADE=1

Copy

You get the idea. There are too many, and they are all different.

## The Proposal

A single, standard environment variable that clearly and unambiguously
 expresses a user's wish to opt out ofanyof the following:

* Ad tracking
* Usage reporting, anonymous or not
* Telemetry
* Crash reporting
* Non-essential-to-functionalityrequests to the creator of the software or third-party

We just want local software.

export DO_NOT_TRACK=1

Copy to clipboard

Add the line above to your shell configuration file so it applies
 to all your terminal sessions:

Shell

File

Syntax

Bash

~/.bashrc

Copy

export DO_NOT_TRACK=1

Copy

Zsh

~/.zshrc

Copy

export DO_NOT_TRACK=1

Copy

Fish

~/.config/fish/config.fish

Copy

set -x DO_NOT_TRACK 1

Copy

PowerShell

$PROFILE

Copy

$env:DO_NOT_TRACK = "1"

Copy

Windows (CMD)

System Environment Variables

setx DO_NOT_TRACK 1

Copy

## For Software Authors

If you develop tools that collect telemetry, analytics, or make
 non-essential network requests, please check for this variable:

* IfDO_NOT_TRACKis set to1, disable all tracking
* Respect the variable alongside your existing opt-out mechanisms
* Consider making telemetry opt-in rather than opt-out

## See Also

* no-color.org—NO_COLOR, a standard for disabling color output
* force-color.org—FORCE_COLOR, a standard for forcing color output