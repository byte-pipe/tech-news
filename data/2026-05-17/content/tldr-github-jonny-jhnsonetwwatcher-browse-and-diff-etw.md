---
title: 'GitHub - jonny-jhnson/EtwWatcher: Browse and diff ETW provider snapshots across Windows builds. Backed by ETWInspector. · GitHub'
url: https://github.com/jonny-jhnson/EtwWatcher
site_name: tldr
content_file: tldr-github-jonny-jhnsonetwwatcher-browse-and-diff-etw
fetched_at: '2026-05-17T19:29:39.679586'
original_url: https://github.com/jonny-jhnson/EtwWatcher
date: '2026-05-17'
description: Browse and diff ETW provider snapshots across Windows builds. Backed by ETWInspector. - jonny-jhnson/EtwWatcher
tags:
- tldr
---

jonny-jhnson

 

/

EtwWatcher

Public

* NotificationsYou must be signed in to change notification settings
* Fork1
* Star29

 
 
 
 
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

20 Commits
20 Commits
.github/
workflows
.github/
workflows
 
 
css
css
 
 
js
js
 
 
scripts
scripts
 
 
snapshots
snapshots
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
index.html
index.html
 
 
View all files

## Repository files navigation

# EtwWatcher

A static web app for browsing and diffing snapshots of Windows ETW (Event Tracing for Windows) provider state across builds. Snapshots are produced byETWInspectorand committed to this repo as NDJSON.

## Using it

Live site:https://jonny-jhnson.github.io/EtwWatcher/

You don't need to clone or run anything to use EtwWatcher. Open the live site and you can:

* Browseany committed snapshot - filter providers by name/GUID, scope by Manifest or MOF, drill into events, search descriptions/keywords/template fields.
* Diffany two snapshots to see providers added, changed, and removed - including per-event field-level changes.
* Bring your ownsnapshot via the upload zone at the top of the page. The file is parsed entirely in your browser; nothing is uploaded anywhere. Either plain.ndjson(straight fromExport-EtwSnapshot) or gzipped.ndjson.gzworks - the upload zone detects the format from the filename and decompresses in-browser when needed. You only need the.ndjson.gzform if you want a smaller file to share around; produce one by dropping the plain.ndjsonintosnapshots/and running./scripts/update-manifest.ps1(it compresses in place).
* Share findingsby copying the URL - it captures the active tab, picked snapshots, and all filters, so a teammate clicking your link sees the exact same view.

## Why this exists

Detection engineers, threat hunters, and Windows internals researchers frequently need to answer questions like:

* What ETW providers and events exist on a given Windows build?
* Which events were added, removed, or had their metadata changed between two builds?
* Did a Patch Tuesday update silently rename or rewrite an event that an existing detection depends on?
* Which keywords and template fields does a specific event expose, and how did those evolve?

Today, getting this information usually means provisioning a VM, installing tooling, dumping provider state, and repeating the whole process on a second VM to compare. That's a meaningful barrier - and it's why a lot of detection content is written against assumptions that go stale silently.

EtwWatcher does that work once. Real Windows snapshots are produced byETWInspector, committed to this repo, and rendered in a browser-side UI. Anyone can browse, search, and diff provider state across Windows builds without standing up infrastructure - and link a teammate directly to a specific finding.

## What's coming

Snapshots will be added on an ongoing basis. The intent is to cover:

* Patch Tuesday cumulative updatesfor currently-supported Windows builds, so you can see what shifted between e.g.26200.7171and26200.7462.
* Insider / Canary buildsas Microsoft ships them - early signal on what providers and events are being added or restructured before they hit general availability.

If you want a specific build snapshotted, open an issue with the build number, or grabETWInspectorand contribute the NDJSON directly via theAdding a snapshotflow below.

## What it does

* Browse- pick a snapshot and explore every Manifest, MOF, or TraceLogging provider on that Windows build. Filter by provider (name, GUID, resource path), event description, keyword name, or template XML field. Toggle All / Manifest / MOF / TraceLogging at the top to scope by schema source. Click a provider to see its events, levels, opcodes, keyword names, full template XML, and (for TraceLogging) the list of binaries the provider was discovered in.
* Diff- pick two snapshots and see exactly what changed: providers added, providers whose events were added/removed/changed, and per-event field-level diffs with line-by-line highlighting on Description and Template. New schema versions of an existing event Id are paired against the closest version in the older snapshot and rendered as a "new version" diff (e.g.Id 2 v1 -> v3 [NEW VERSION]) instead of as separate "added" events.

Everything runs in your browser. No backend, no telemetry. The page fetches the NDJSON files committed to/snapshots/and parses them client-side.

Manifest, MOF, and TraceLogging providers are covered (out of the four ETW provider types - WPP is not yet supported). Toggle between them in the Browse and Diff views with the schema-source segmented control.

## Querying providers

Browse and Diff both expose the same four text filters plus a schema-source toggle. All filters arecase-insensitive substring matchesand areAND-combined- a provider has to satisfy every filter you've set. Leave a box empty to ignore that dimension.

Filter

What it matches

Provider

ProviderName
, 
ProviderGuid
, or 
ResourceFilePath
 (any of the three). Use this to pin to a known GUID, search a name fragment like 
Kernel-Process
, or scope by binary path.

Description

Substring of an event's 
Description
. For Manifest events this is the human-readable description; for TraceLogging events it's the event name (e.g. 
ProcessStarted
).

Keyword

Substring of an ETW keyword name. Keywords are the 64-bit bitmask flags a provider declares (e.g. 
KERNEL_THREATINT_KEYWORD_ALLOCVM_REMOTE
 on Microsoft-Windows-Threat-Intelligence) - consumers enable a session by OR'ing these together to receive only events tagged with the matching bits. Use this filter when you know the keyword you want to subscribe to and need to find which provider declares it.

Template

Substring of an event's template XML - field names, 
inType
/
outType
 values. Use this to find every event that exposes a field like 
ProcessId
 or 
TargetUserName
.

Schema toggle

All
 / 
Manifest
 / 
MOF
 / 
TraceLogging
. Filters out providers from the other source kinds.

A few practical patterns:

* "What providers carry aCommandLinefield?"- clear all filters, set Template toCommandLine. The provider list narrows to providers with at least one event containing that field.
* "Show me everything new in TraceLogging this build."- in the Diff view, set Schema toggle toTraceLogging. Providers Added / Changed / Removed sections all scope down.
* "Find this specific provider."- paste the GUID (with or without braces) into the Provider box. Substring matching means partial GUIDs work too.
* "Reset."- clickClear filtersnext to the schema toggle.

The active filter set is also encoded into the URL (#view=browse&snap=...&p=...&d=...&k=...&t=...&s=manifest), so once a query lands on something interesting, copy the URL send to a teammate. By clicking it, they sees the same filtered view.

### Querying your own snapshot

Upload a snapshot via the drop zone at the top of the page and the Browse and Diff views work against it identically - same four filters, same schema toggle, same URL state. Plain.ndjsonstraight fromExport-EtwSnapshotworks;.ndjson.gzworks too (decompressed in the browser). Uploaded files live only in the current tab; close it and they're gone.

Note: MOFprovidersare listed, but theireventsdon't currently populate due to enumeration complexities - the MOF event metadata isn't always present in WMI even when the provider class is registered. Manifest and TraceLogging providers carry their full event metadata. Better approaches to MOF event enumeration are being actively explored.

Note on TraceLogging: events are not individually mapped to a specific provider. TraceLogging metadata is compiled into the binary itself as a_TraceLoggingMetadata_tstructure beginning with the four-byte signatureETW0. It carries an array of provider metadata and an array of event metadata, but no per-event provider ID. When a binary declares multiple TraceLogging providers, each one ends up listed against the binary's full event set. If you need a real per-event binding, do static analysis on the binary via IDA or leverage a plugin like -TLGMapperwhich walksTraceLoggingWritecalls and recovers the actual mapping. Better approaches to in-tool attribution are being actively explored.

## ETW Provider Snapshots

Stored inNDJSON(newline-delimited JSON: one JSON object per line) in/snapshots/:

* First line of each file is a header:{"SchemaVersion":"1.0","OSVersion":"10.0.x.y.z"}(the OS version isMajor.Minor.Build.UBR, read straight from the registry by ETWInspector).
* Each subsequent line is one provider record.

snapshots/manifest.jsonis the index of which snapshots show up in the dropdowns - it's regenerated automatically by the deploy workflow whenever NDJSONs change.

## Adding a snapshot (contributors)

1. On a target machine, installETWInspectorand run:Import-Module.\EtwInspector\EtwInspectorModule\EtwInspector.psd1-ForceExport-EtwSnapshotC:\Snapshots\<filename>.ndjsonNaming convention:<major>_<minor>_<build>_<UBR>.ndjson(e.g.10_0_26200_7171.ndjson).
2. Copy the file into this repo'ssnapshots/directory.
3. Run./scripts/update-manifest.ps1from the repo rootbefore committing. This is required, not optional:.\scripts\update-manifest.ps1The script gzips every plain*.ndjsoninsnapshots/in place (the originals are removed; only*.ndjson.gzships) and rewritessnapshots/manifest.jsonsorted by OS version. TraceLogging-aware snapshots routinely exceed 100 MB, which is GitHub's hard per-file push limit - if you skip this step, your push is rejected outright. CI cannot fix this for you, since the rejection happens before the workflow runs.
4. Commit the resulting*.ndjson.gzand the updatedmanifest.json, then push. The deploy workflow re-runsupdate-manifest.ps1on its end, but at that point it's a no-op safety net (the compression already happened locally; the manifest just gets validated).

Existing manifest labels are preserved across re-runs (customizations like(Insider)survive); new entries get a default label ofBuild <OSVersion>that you can edit if you want a prettier name.

## Running locally

You only need this if you're developing the site itself. The site is plain HTML + JS + Tailwind via CDN with no build step:

#
 Python

python -m http.server 8080

#
 Node

npx http-server -p 8080

Then openhttp://localhost:8080.

Note: openingindex.htmldirectly viafile://won't work - the JS usesfetch()and ES module imports, both of which require an HTTP origin. Use a local server.

## Tech

* Vanilla HTML / JS / CSS
* Tailwind CSSloaded via CDN
* ES modules, no bundler
* Hosted onGitHub Pages

## Backing tool

Snapshots are produced byETWInspector- a PowerShell module that enumerates Manifest, MOF, and TraceLogging providers and exports them as JSON or NDJSON. The diff algorithm in this site (js/diff.js) is a JavaScript port ofCompare-EtwSnapshotfrom the same module.

## License

MIT. SeeLICENSE.

## About

Browse and diff ETW provider snapshots across Windows builds. Backed by ETWInspector.

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

29

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

* JavaScript74.8%
* HTML16.2%
* PowerShell7.5%
* CSS1.5%