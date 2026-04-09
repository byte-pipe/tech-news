---
title: Introducing Emacs agent-shell (powered by ACP)
url: https://xenodium.com/introducing-agent-shell
site_name: hackernews
fetched_at: '2025-10-13T11:07:24.900793'
original_url: https://xenodium.com/introducing-agent-shell
author: Karrot_Kream
date: '2025-10-13'
---

xenodium.com

 ██ ██ ███████ ███ ██ ██████ ██████ ██ ██ ██ ███ ███
 ██ ██ ██ ████ ██ ██ ██ ██ ██ ██ ██ ██ ████ ████
 ███ █████ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ████ ██
 ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██
 ██ ██ ███████ ██ ████ ██████ ██████ ██ ██████ ██ ██

September 25, 2025

# Introducing Emacs agent-shell (powered by ACP)

Not long ago, Iintroduced acp.el, an Emacs lisp implementation of ACP (Agent Client Protocol), the agent protocoldeveloped between Zed and Google folks.

While I've been happily accessing LLMs from my beloved text editor viachatgpt-shell(amulti-modelpackage I built), I've been fairly slow on the AI agents uptake. Probably a severe case ofold-man-shouts-at-cloudsorta thing, but hey I want well-integrated tools in my text editor. When I heard of ACP, I knew this was the thing I was waiting for to play around with agents.

With an earlyacp.elclient library in place, I set out to build an Emacs-native agent integration… Today, I have an initial version ofagent-shellI can share.

agent-shellis a native Emacs shell, powered bycomint-mode(check out Mickey'scomint articlebtw). As such, we don't have to dance between char and line modes to interact with things.agent-shellis just a regular Emacs buffer like any other you're used to.

## Agent-agnostic

Thanks to ACP, we can now build agent-agnostic experiences by simply configuring our clients to communicate with their respective agents using a common protocol. As users, we benefit from a single, consistent experience, powered by any agent of our choice.

Configuring different agents fromagent-shellboils down which agent we want running in the comms process. Here's an example of Gemini CLI vs Claude Code configuration:

(defun agent-shell-start-gemini-agent ()
 "Start an interactive Gemini CLI agent shell."
 (interactive)
 (agent-shell--start
 :new-session t
 :mode-line-name "Gemini"
 :buffer-name "Gemini"
 :shell-prompt "Gemini> "
 :shell-prompt-regexp "Gemini> "
 :needs-authentication t
 :authenticate-request-maker (lambda ()
 (acp-make-authenticate-request :method-id "gemini-api-key"))
 :client-maker (lambda ()
 (acp-make-client :command "gemini"
 :command-params '("--experimental-acp")
 :environment-variables (list (format "GEMINI_API_KEY=%s" (agent-shell-google-key)))))))

(defun agent-shell-start-claude-code-agent ()
 "Start an interactive Claude Code agent shell."
 (interactive)
 (agent-shell--start
 :new-session t
 :mode-line-name "Claude Code"
 :buffer-name "Claude Code"
 :shell-prompt "Claude Code> "
 :shell-prompt-regexp "Claude Code> "
 :client-maker (lambda ()
 (acp-make-client :command "claude-code-acp"
 :environment-variables (list (format "ANTHROPIC_API_KEY=%s" (agent-shell-anthropic-key)))))))

I've yet to try other agents. If you get another agent running, I'd love to hear about it. Maybe submit apull request?

## Traffic

While I've been relying on myacp.elclient library, I'm still fairly new to the protocol. I often inspect traffic to see what's going on. After staring at json for far too long, I figured I may as well build some tooling aroundacp.elto make my life easier. I added a traffic buffer for that. Fromagent-shell, you can invoke it viaM-x agent-shell-view-traffic.

## Fake agents

Developingagent-shellagainst paid agents got expensive quickly. Not only expensive, but my edit-compile-run cycle also became boringly slow waiting for agents. While I knew I wanted some sort of fake agent to work against, I didn't want to craft the fake traffic myself. Remember that traffic buffer I showed ya? Well, I can now save that traffic to disk and replay it later. This enabled me to run problematic sessions once and quickly replay multiple times to fix things. While re-playing has its quirks and limitations, it's done the job for now.

You can see a Claude Code session below, followed by its replayed counterpart via fake infrastructure.

## What's next

Getting here took quite a bit of work. Having said that, it's only a start. I myself need to get more familiar with agent usage and evolve the package UX however it feels most natural within its new habitat. Lately, I've been experimenting with a quick diff buffer, driven by n/p keys, shown along the permission dialog.

#+ATTR_HTML: :width 99%

While I've implemented enough parts of theAgent Client Protocol Schemato make the package useful, it's hardly complete. I've yet to fully familiarize myself with most protocol features.

## Take them for a spin

Both of my new Emacs packages,agent-shellandacp.el, are now available on GitHub. As an agent user, go straight toagent-shell. If you're a package author and would like to build an ACP experience, then giveacp.ela try. Both packages are brand new and may have rough edges. Be sure to file bugs or feature requests as needed.

## Paying for LLM tokens? How about sponsoring your Emacs tools?

I've been heads down, working on these packages for some time. If you're using cloud LLM services, you're likely already paying for tokens. If you find my work useful, please considerrouting some of those coinsto help fund it. Maybe my tools make you more productive at work? Ask youremployer to support the work. These packages not only take time and effort, but also cost me money.Help fund the work.

powered byLMNO.lol

privacy policy·terms of service
