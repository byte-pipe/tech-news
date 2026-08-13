---
title: "Introducing Delta — Zed's Blog"
url: https://zed.dev/blog/introducing-delta
date: 2026-08-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:44:34.218468
---

# Introducing Delta — Zed's Blog

# Introducing Delta — Zed's Blog

## Overview
- Delta is a multiplayer environment that lets developers code together with AI agents while keeping code and conversations tightly linked.  
- It is built on **DeltaDB**, a real‑time replicated database that syncs the worktree and chat thread, and works with existing Git repositories.  

## Review where the work happened
- Comments can be attached to any line of code or to any part of the conversation and stay anchored as the code evolves.  
- Agents participate directly in the thread, can explain or fix issues, and their actions remain connected to the surrounding discussion.  
- The combined history of code and rationale stays in DeltaDB for future teammates and agents to understand why the code looks the way it does.  

## Agentic development becomes multiplayer
- Threads are private until shared; invited participants can explore, comment, or continue work in real time.  
- Each participant has a local copy of the code that stays synchronized with the shared worktree.  

## Delta, everywhere
- DeltaDB extends to cloud runners, allowing work to continue when a laptop is closed while keeping the thread in sync.  
- Threads can be opened in a browser via **Delta.dev**, a Rust‑compiled‑to‑WebAssembly app rendered with WebGL, providing the same experience as the desktop client.  
- Integration with third‑party agent harnesses (starting with Claude Code) lets terminal sessions sync live into a Delta thread for collaborative review.  

## Interface built to keep up with agents
- Full diffs and complete conversation transcripts are displayed without collapsing or truncating.  
- The conversation is treated as a document; the cursor can move anywhere, and comments attach precisely to the selected text, diff line, plan step, or thinking block.  
- This design lets users respond directly to specific parts of the agent’s output, reducing serial back‑and‑forth.  

## A new application for a new reality
- DeltaDB required a dedicated client to evolve without the constraints of the existing Zed editor.  
- The first Delta client was built from the ground up with the thread as the central abstraction, while Zed will later incorporate DeltaDB.  

## Join the private beta
- Initial private‑beta invitations have been sent; more will be offered in the coming weeks.  
- Interested users can sign up for early access.  

## Related posts & calls to action
- Links to other Zed blog entries (e.g., Parallel Agents, Zed AI).  
- Invitation to try the Zed editor on macOS, Windows, or Linux.  
- Hiring notice for those passionate about the blog’s topics.