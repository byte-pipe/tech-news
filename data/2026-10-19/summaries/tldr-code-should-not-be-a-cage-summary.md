---
title: Code Should Not Be a Cage
url: https://www.seuros.com/blog/code-should-not-be-a-cage
date: 2026-10-19
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-19T09:17:08.131955
---

# Code Should Not Be a Cage

# Code Should Not Be a Cage

## Introduction
- Recent releases (Photoshop rebuilt with Opus 5.5, Word, AutoCAD, Pro Tools) show that any software can now be rebuilt locally using AI‑generated code.
- This marks the end of an era where proprietary binaries could be trusted to stay opaque; the next era aligns with warnings long issued by the free‑software movement.

## Lean Into It
- Scott Werner (Sublayer) suggests embracing REA (Reverse Engineer Anything) by providing coding‑agent interfaces for users to modify releases.
- The author doubts this temporary fix, noting that future software will be server‑side and undocumented.
- Werner cites the pre‑AI reconstruction of Asheron’s Call servers as a precedent.

## Asheron’s Call
- Turbine shut down the game in 2017; players captured network traffic, enabling the ACE project to rebuild a functional server.
- ACE relied on an encrypted cache from the private PhatAC emulator and a 2005 world snapshot; missing data were hand‑crafted.
- Similar reconstructions (City of Heroes, Star Wars Galaxies Legends) depended on leaked server code; pure packet‑only attempts took years and remained incomplete.
- Modern services expose only login pages and JSON, making full reconstruction far harder.

## REA Is a Wrapper
- REA’s first commit (April 2026) added a binary MCP server for Hopper Disassembler.
- Community plugins (GhidraMCP, IDA server) existed a year earlier, showing REA is essentially a wrapper around existing decompilation servers.
- Tools like OpenGoldHEN illustrate how AI can drive such servers without deep reverse‑engineering knowledge.

## OpenGoldHEN
- GoldHEN is the dominant PS4 homebrew enabler; its source was made private after abuse.
- In October 2026, “zer0days‑op” released OpenGoldHEN, rebuilt with AI, without a license, and with a manifesto proclaiming “Code should not be a cage.”
- The author opened a critical issue, receiving a hostile response warning that future releases would cease.
- The project highlights a tension: AI‑generated clones can bypass original source restrictions, but the lack of understandable code makes them effectively closed.

## Sony Won
- PS5 scene leader Andy Nguyen (“TheFloW”) quit after discovering a hypervisor bug and agreeing to hold it until after GTA VI.
- The bug was later found by others using AI tools; it was reported to Sony’s bounty program.
- The community’s habit of withholding bugs may keep flaws alive across console generations, but AI makes discovery cheap and tempting.

## Stallman Saw the Server Coming
- Richard Stallman’s 2010 essay “Who Does That Server Really Serve?” warned that services replace running one’s own copy of software, limiting user freedom.
- The AGPLv3 (2007) attempted to force sharing of network‑served modifications but only protects server operators, not end users.
- As AI can recreate shipped software, vendors are likely to shift to cloud‑only delivery, turning applications into inaccessible services.

## Freedom, From $19 a Month
- The article notes recent price hikes (e.g., Beehiiv) that push users toward subscription models, reinforcing the move to server‑side software.
- The underlying message: when code cannot be examined or modified locally, freedom erodes, regardless of price.

## Conclusion
- AI‑driven REA enables anyone to rebuild proprietary software, undermining the traditional barrier between closed and open code.
- While “leaning in” by providing modification interfaces may help, the broader trend is a shift to opaque, server‑only services.
- The free‑software community’s historic warnings are becoming reality: without the ability to run and understand code locally, users lose true freedom.