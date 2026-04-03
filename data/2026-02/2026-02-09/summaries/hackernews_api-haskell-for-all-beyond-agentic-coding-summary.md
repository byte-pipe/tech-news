---
title: Haskell for all: Beyond agentic coding
url: https://haskellforall.com/2026/02/beyond-agentic-coding
date: 2026-02-08
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-09T06:08:57.252775
---

# Haskell for all: Beyond agentic coding

# Haskell for all
## Beyond agentiic coding

The author expresses skepticism about the benefits of agentic coding in software development, arguing it often hinders productivity and user comfort. This view is based on personal experience, observations from interviews with candidates, and research studies (Becker and Shen) indicating that agentic coding doesn't necessarily improve outcomes and can sometimes worsen them.

The author believes that while agentic coding isn't a lost cause, its current implementation detracts from software development. Instead of focusing on agentic coding, the author proposes exploring alternative AI-assisted development solutions.

A key design principle for AI-assisted tools, and generally for good tools, is to maintain the user in a flow state. Agentic coding often disrupts this flow, leading to increased idle time and interruptions.

The author introduces "calm technology," a design discipline focused on promoting flow states. Key principles include minimizing attention demands, building tools to be "pass-through" (enhancing the user's focus on the task), and creating calm to facilitate flow.

Examples of calm technology in use today include inlay hints in IDEs (like VSCode) and file tree previews. These elements are unobtrusive, enhance the user's existing workflow, and fade into the background as the user becomes familiar with them.

Chat-based coding agents are contrasted with calm technology, as they place high demands on attention, are not "pass-through" interfaces (being indirect, slow, and imprecise), and undermine calm by requiring constant user interaction.

GitHub Copilot's inline suggestions are presented as an early example of an AI coding assistant that attempts to model calm design principles by being a "pass-through" interface. However, the default frequency of suggestions can disrupt flow and undermine calm due to attention demands and visual intrusiveness.
