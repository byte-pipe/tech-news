---
title: 'Cowork feature creates 10GB VM bundle that severely degrades performance · Issue #22543 · anthropics/claude-code · GitHub'
url: https://github.com/anthropics/claude-code/issues/22543
site_name: hackernews_api
content_file: hackernews_api-cowork-feature-creates-10gb-vm-bundle-that-severel
fetched_at: '2026-03-02T19:19:43.145835'
original_url: https://github.com/anthropics/claude-code/issues/22543
author: mystcb
date: '2026-03-02'
description: Description After using the cowork feature, Claude Desktop becomes extremely slow - slow startup, UI lag, and slow responses. Performance degrades over time even during a single session. Investigation VM Bundle (10GB) The cowork feature ...
tags:
- hackernews
- trending
---

anthropics

 

/

claude-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork5.8k
* Star72.7k

# Cowork feature creates 10GB VM bundle that severely degrades performance#22543

Open
Open
Cowork feature creates 10GB VM bundle that severely degrades performance
#22543
Assignees
 
Labels
bug
Something isn't working
Something isn't working
high-priority
oncall
performance

## Description

mjbyt
opened 
on 
Feb 2, 2026
Issue body actions

## Description

After using the cowork feature, Claude Desktop becomes extremely slow - slow startup, UI lag, and slow responses. Performance degrades over time even during a single session.

## Investigation

### VM Bundle (10GB)

The cowork feature creates a VM bundle at:

~/Library/Application Support/Claude/vm_bundles/claudevm.bundle/rootfs.img

This file grows to10GBand is never cleaned up. It regenerates quickly after deletion (deleted one day, back to 10GB the next).

### Cleanup Test Results

Deleted vm_bundles, Cache, and Code Cache directories (reduced from 11GB to 639MB).

Result: ~75% faster immediately after cleanup on tasks that previously failed/hung.

### Performance Degradation Over Time

Even after cleanup (VM bundle at 0 bytes), performance degrades within minutes:

* Immediately after restart: ~24% CPU at idle
* After several minutes of use: ~55% CPU (renderer at 24%, main at 21%, GPU at 7%)
* Swap activity increases (swapins climbing from 20K to 24K+)

This suggests a memory leak or accumulating work that causes degradation regardless of VM bundle state.

## Environment

* macOS (Darwin 25.2.0)
* Claude Desktop (latest)
* 8GB system RAM

## Observed Behavior

* High CPU at idle (~24-55% combined across processes)
* Heavy swap activity that increases over time
* Performance degrades within minutes of use
* 10GB VM bundle regenerates after every cowork session
* Tasks that failed before cleanup now complete (75% faster initially)

## Workaround

Quit Claude Desktop and delete the VM bundle:

rm -rf 
~
/Library/Application
\ 
Support/Claude/vm_bundles
rm -rf 
~
/Library/Application
\ 
Support/Claude/Cache
rm -rf 
~
/Library/Application
\ 
Support/Claude/Code
\ 
Cache

Provides ~75% improvement but degrades again over time.Must restart periodically.

## Expected Behavior

* Stable CPU usage that doesn't degrade over time
* VM bundles cleaned up after cowork sessions
* Usable performance on 8GB RAM systems

Filed via Claude Code

Reactions are currently unavailable

## Metadata

## Metadata