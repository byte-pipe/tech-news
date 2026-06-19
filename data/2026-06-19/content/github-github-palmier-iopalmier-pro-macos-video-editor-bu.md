---
title: 'GitHub - palmier-io/palmier-pro: macOS video editor built for AI · GitHub'
url: https://github.com/palmier-io/palmier-pro
site_name: github
content_file: github-github-palmier-iopalmier-pro-macos-video-editor-bu
fetched_at: '2026-06-19T12:23:41.281000'
original_url: https://github.com/palmier-io/palmier-pro
author: palmier-io
description: macOS video editor built for AI. Contribute to palmier-io/palmier-pro development by creating an account on GitHub.
---

palmier-io

 

/

palmier-pro

Public

* NotificationsYou must be signed in to change notification settings
* Fork161
* Star1.4k

 
 
 
 
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

612 Commits
612 Commits
Sources/
PalmierPro
Sources/
PalmierPro
 
 
Tests/
PalmierProTests
Tests/
PalmierProTests
 
 
assets
assets
 
 
mcpb
mcpb
 
 
models
models
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
FAQ.md
FAQ.md
 
 
LICENSE
LICENSE
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
appcast.xml
appcast.xml
 
 
View all files

## Repository files navigation

# Palmier Pro

The video editor built for AI.

Requires macOS 26 (Tahoe) on Apple Silicon

Palmier Pro is an open source video editor for Mac. You and your agent can generate and edit videos together inside the timeline.

### Swift-native video editor

We built Palmier Pro from scratch with Swift. The north star is Premiere Pro, with our take on integrating AI into the workflow.

### Built-in Generative AI

Generate videos and images with SOTA models like Seedance, Kling, Nano Banana Pro inside the timeline editor.

### Integrates with your agents

Connects your Claude/Codex/Cursor via MCP, or use the in-app agent to work on the same project together.

## MCP server

When the app is open, it exposes an MCP server athttp://127.0.0.1:19789/mcpvia HTTP. To connect:

Claude Code

claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp

Codex

codex mcp add palmier-pro --url http://127.0.0.1:19789/mcp

Cursor

The easiest way is go inside the appHelp->MCP Instructions->Install in Cursor, or install manually by adding this to~/.cursor/mcp.json:

{
 "mcpServers": {
 "palmier-pro": {
 "type": "http",
 "url": "http://127.0.0.1:19789/mcp"
 }
 }
}

Claude Desktop

We bundle amcpbwith the app that allows a one click install Desktop Extension on Claude Desktop. Go toHelp->MCP Instructions->Install in Claude Desktop

## FAQ

Is Palmier Pro fully open source?

The video editor (without the generative AI features) is fully open source. The MCP server and the agent chat are also open source. The only thing that is closed source is the generative AI processing.

Is it free?

The editor is free. You can download it with no login required, and use it as a video editor like CapCut or Adobe Premiere. You can also use the MCP server for free, and start experimenting using Claude Code/Desktop or Cursor to interact with your timeline editor.

Generative AI features require login and subscription.

What platforms does it support?

macOS 26 (Tahoe) on Apple Silicon only.

SeeFAQ.mdfor more.

## Development

SeeCONTRIBUTING.md

## Community & Support

* Discord:Join the community onDiscord.
* Twitter / X:Follow@Palmier_iofor updates and announcements.
* Instagram:Follow@palmier.io
* Feedback & Support:Create aGithub Issueor email us atfounders@palmier.io

## Star History

## License

Copyright (C) 2026 Palmier, Inc.

Palmier Pro is open source underGPLv3.

## About

macOS video editor built for AI

palmier.io

### Topics

 macos

 swift

 mcp

 video-editor

 claude

 ai-video

 seedance2

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.4k

 stars
 

### Watchers

7

 watching
 

### Forks

161

 forks
 

 Report repository

 

## Releases52

v0.3.4

 Latest

 

Jun 19, 2026

 

+ 51 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Swift98.8%
* Other1.2%