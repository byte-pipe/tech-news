---
title: 'GitHub - twostraws/SwiftUI-Agent-Skill: SwiftUI agent skill for Claude Code, Codex, and other AI tools. · GitHub'
url: https://github.com/twostraws/SwiftUI-Agent-Skill
site_name: github
content_file: github-github-twostrawsswiftui-agent-skill-swiftui-agent
fetched_at: '2026-10-09T17:19:15.466773'
original_url: https://github.com/twostraws/SwiftUI-Agent-Skill
author: twostraws
description: SwiftUI agent skill for Claude Code, Codex, and other AI tools. - twostraws/SwiftUI-Agent-Skill
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

18 Commits
18 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude-plugin
.claude-plugin
 
 
assets
assets
 
 
swiftui-pro
swiftui-pro
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# SwiftUI Agent Skill for AI Coding Assistants

An agent skill that helps AI coding assistants write smarter, simpler, and more modern SwiftUI, including guidance on API usage, design, performance, and accessibility. Covers navigation, layout, animations, state management, VoiceOver, deprecated API, and more, targeting the mistakes LLMs actually make.

Also available:

* SwiftData Pro
* Swift Concurrency Pro
* Swift Testing Pro

Find more agent skills for Swift and Apple platform development atSwift Agent Skills.

The skill builds upon my existingAGENTS.mdfile, meaning that you can bring years of knowledge and practical experience into your coding agent of choice in just a few minutes. It uses theAgent Skillsformat, so it works smoothly with Claude Code, Codex, Gemini, Cursor, and more.

## Installing SwiftUI Pro

You can install this skill into Claude Code, Codex, Gemini, Cursor, and more by using npx:

npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro

If you get the errornpx: command not found, it means you don’t currently have Node installed. You need to run this command to install Node through Homebrew:

brew install node

And ifthatfails it usually means you need toinstall Homebrewfirst.

When usingnpx, you can select exactly which agents you want to use during the installation. You can also select whether the skill should be installed just for one project, or whether it should be made available for all your projects.

Claude Code users can add the SwiftUI Agent Skill marketplace then install the plugin directly through Claude, like this:

/plugin marketplace add twostraws/SwiftUI-Agent-Skill
/plugin install swiftui-pro@swiftui-agent-skill

Alternatively, you can clone this whole repository and install it however you want.

If you’re using Xcode, watch the YouTube video onHow to Install and Use Agent Skills in Xcodefor a walkthrough.

## Using SwiftUI Pro

The skill is called SwiftUI Pro, and can be triggered in various ways. For example, in Claude Code you would use this:

/swiftui-pro

And in Codex you would use this:

$swiftui-pro

In both cases you can provide specific instructions if you want only a partial review. For example,/swiftui-pro Check for deprecated APIon Claude, or$swiftui-pro Focus on accessibilityin Codex.

You can also trigger the skill using natural language:

Use the SwiftUI Pro skill to look for performance problems in this project.

## Why Use an Agent Skill for SwiftUI?

This skill is built on thousands of hours of learning, experimenting, and building real-world SwiftUI projects. The rules contained here directly target common SwiftUI mistakes made by LLMs. They sometimes make buttons invisible to VoiceOver, they frequently use deprecated API, and they would often write code that causes surprise performance problems.

You can read more about why I created this skill in my article:SwiftUI Agent Skill - Write better code with Claude, Codex, and other AI tools.

## Contributing

I welcome all contributions, whether that's adding new checks, improving existing checks, or editing this README – everyone is welcome!

* Keep your Markdown concise. There is a token cost to using skills, particularly with SKILL.md, so please respect the token budgets of users.
* Do not repeat things that LLMs already know, because it burns tokens for no benefit. Focus on edge cases, surprises, soft deprecations, and similar.
* All work must be licensed under the MIT license so it can benefit the most people.

Please ensure you abide by theCode of Conduct.

## License

SwiftUI Pro was originally created byPaul Hudson, who writesfree Swift tutorials over at Hacking with Swift. It’s available under theMIT License, which permits commercial use, modification, distribution, and private use.

 

A Hacking with Swift Project