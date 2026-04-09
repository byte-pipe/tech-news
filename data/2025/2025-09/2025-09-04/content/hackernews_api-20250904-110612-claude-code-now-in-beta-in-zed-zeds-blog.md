---
title: 'Claude Code: Now in Beta in Zed — Zed''s Blog'
url: https://zed.dev/blog/claude-code-via-acp
site_name: hackernews_api
fetched_at: '2025-09-04T11:06:12.751545'
original_url: https://zed.dev/blog/claude-code-via-acp
author: meetpateltech
date: '2025-09-03'
published_date: 09/03/2025
description: 'From the Zed Blog: You asked, and here it is. Use Claude Code in public beta directly in Zed, built on the new Agent Client Protocol.'
tags:
- hackernews
- trending
---

← Back to Blog

# Claude Code: Now in Beta in Zed

You asked for it. A lot.

@EricBuess

Would LOVE a Claude Code integration. On the roadmap?

@lucasbastianik

Waiting for Claude Code integration 🤘

@ugbahisioma

Claude code too please…

@nicojrme

when Claude Code?

@kdcokenny

It would be absolutely killer if you guys were able to move claude code into the assistant panel.

@EricBuess

Would LOVE a Claude Code integration. On the roadmap?

@lucasbastianik

Waiting for Claude Code integration 🤘

@ugbahisioma

Claude code too please…

@nicojrme

when Claude Code?

@kdcokenny

It would be absolutely killer if you guys were able to move claude code into the assistant panel.

@EricBuess

Would LOVE a Claude Code integration. On the roadmap?

@lucasbastianik

Waiting for Claude Code integration 🤘

@ugbahisioma

Claude code too please…

@nicojrme

when Claude Code?

@kdcokenny

It would be absolutely killer if you guys were able to move claude code into the assistant panel.

@EricBuess

Would LOVE a Claude Code integration. On the roadmap?

@lucasbastianik

Waiting for Claude Code integration 🤘

@ugbahisioma

Claude code too please…

@nicojrme

when Claude Code?

@kdcokenny

It would be absolutely killer if you guys were able to move claude code into the assistant panel.

@osdiab

If I could just plug in Claude Code or whatever else comes out into any editor that supported some common protocol for agents, that would be sweeeet

@ZainMerchant9

It’s game over when claude code gets added, I’m converting instantly

@wiedymi

Cool, now we need claude code to support the protocol

@iamkgn

Does this work with Claude Code?

@mitryco

nice, waiting for Claude Code and I can switch to Zed finally 🙂

@osdiab

If I could just plug in Claude Code or whatever else comes out into any editor that supported some common protocol for agents, that would be sweeeet

@ZainMerchant9

It’s game over when claude code gets added, I’m converting instantly

@wiedymi

Cool, now we need claude code to support the protocol

@iamkgn

Does this work with Claude Code?

@mitryco

nice, waiting for Claude Code and I can switch to Zed finally 🙂

@osdiab

If I could just plug in Claude Code or whatever else comes out into any editor that supported some common protocol for agents, that would be sweeeet

@ZainMerchant9

It’s game over when claude code gets added, I’m converting instantly

@wiedymi

Cool, now we need claude code to support the protocol

@iamkgn

Does this work with Claude Code?

@mitryco

nice, waiting for Claude Code and I can switch to Zed finally 🙂

@osdiab

If I could just plug in Claude Code or whatever else comes out into any editor that supported some common protocol for agents, that would be sweeeet

@ZainMerchant9

It’s game over when claude code gets added, I’m converting instantly

@wiedymi

Cool, now we need claude code to support the protocol

@iamkgn

Does this work with Claude Code?

@mitryco

nice, waiting for Claude Code and I can switch to Zed finally 🙂

So we built it: our Claude Code integration is now available in public beta, running natively in Zed through our newAgent Client Protocol (ACP).

For months, developers have been asking us to bring Claude Code into Zed. We didn’t just want to bolt on a one-off integration; we wanted to build something better. ACP is our new open standard that lets any agent connect to Zed (and other editors, too). Claude Code is a perfect example of what’s possible.

Now you can:

* Run Claude Code as a first-class citizenin Zed's high-performance editor, not just a terminal interface
* Follow alongin real-timeas it edits across multiple files, with full syntax highlighting and language server support
* Review and approve granular changesin amultibuffer- accept or reject individual code hunks
* Keep Claude Code's task list anchoredin your sidebar, so you always see what the agent is working on
* Define custom workflowswithClaude Code's custom slash commandsfor your most common development tasks

## Escape the Terminal

A walkthrough of Claude Code in Zed.

Claude Code has gained broad popularity among developers thanks to its powerful code generation and finely tuned tools. While the command-line interface is powerful, when Claude Code is making changes across multiple files or refactoring complex logic, you may want to see the bigger picture and have more control on what code you accept or reject. With Zed, you get the best of both worlds: Claude Code's intelligence, freed from the terminal and deeply integrated into a highly performant editor.

You can now run Claude Code directly in Zed and use it side-by-side with Zed's first-party agent, Gemini CLI, and any other ACP-compatible agent. Make sure you’re onthe latest version of Zedand find your available agents in the Plus menu in the Agent Panel.

## Built with ACP

Rather than creating a tightly-coupled integration specific to Claude Code, we built this integration using theAgent Client Protocol. Welaunched ACPas our open standard for connecting any AI agent with any compatible editor.

We built an adapter that wraps Claude Code's SDK and translates its interactions into ACP's JSON RPC format. This adapter bridges between Claude Code and ACP's standardized interface, allowing Claude Code to run as an independent process while Zed provides the user interface.

We are open sourcing the Claude Code adapter under the Apache license, making it freely available for any editor that’s adopted ACP to use; you can findthe source code here. Since the popularCodeCompanion pluginfor Neovim has already adopted ACP, Claude Code willalsobe available in Neovim.

We want to thankGitHub user Xuanwofor all his work since the ACP launch in building an ACP implementation for Claude Code - your speed to solution inspired us to work hard to keep up! We appreciate you for your contribution to the protocol's adoption. Give him a follow onGitHubandTwitter/X.

## Bring Any Agent to Zed

We want every agent usable in Zed. Gemini CLI and Claude Code are a great start, and we have more on the way, but there are new agents released every week and many great existing ones not yet speaking the protocol. ACP makes it simple to bring any agent into Zed's, Neovim's, or any other ACP-adapted editor's interface!

This beta delivers as much core Claude Code functionality as possible via the SDK. We're adding features like Plan mode in the coming days, and more advanced capabilities as Anthropic expands SDK support; for example, many built-in slash commands are not yet supported by the SDK. From here:

* Building an agent?We want to help you integrate with Zed -reach outwith questions.
* Want more Claude Code features?Join us in asking Anthropic to bring the SDK to parity with Claude Code oradopt ACP directly.
* Ready to contribute?Contributeto or discuss ACPandthe Claude Code adapterrepos.

We're always looking forfeedback on ACP, and welcome contributions from other agent (and client) builders. The more agents that work in Zed, the more choice you have as a developer.

### Looking for a better editor?

You can try Zed today on macOS or Linux.Download now!

### We are hiring!

If you're passionate about the topics we cover on our blog, please considerjoining our teamto help us ship the future of software development.
