---
title: Google Antigravity 1.0 to 2.0/IDE Quick Migration Guide - DEV Community
url: https://dev.to/gde/google-antigravity-10-to-20ide-quick-migration-guide-35p5
site_name: devto
content_file: devto-google-antigravity-10-to-20ide-quick-migration-gui
fetched_at: '2026-05-23T11:28:43.718146'
original_url: https://dev.to/gde/google-antigravity-10-to-20ide-quick-migration-guide-35p5
author: Regnard Raquedan
date: '2026-05-22'
description: Like many Google Antigravity users, I was very excited about the Antigravity 2.0 announcement at... Tagged with ai, webdev, programming, productivity.
tags: '#ai, #webdev, #programming, #productivity'
---

Like manyGoogle Antigravityusers, I was very excited about theAntigravity 2.0announcement at Google I/O 2026.

Who would't be enthusiastic about the new cost efficient Gemini 3.5 Flash? Plus, a standalone desktop app form factor that seems to rival Claude Code and OpenAI Codex at that!

There are a lot of great things to be eager to try it out but I want to provide some pointers in the upgrade and migration to save you some headaches and hassles later.

The upgrade path from Antigravity 1.0 to 2.0 is straightforward:

1. At the Antigravity 1.0 user interface, there should be a button that asks you to restart the app to update.
2. Follow the steps to install Antigravity 2.0, including logging into your Google account linked to the app.
3. There's a call-out to install Antigravity IDE in addition to 2.0.
4. When you're done with the upgrade, you will be asked about customizations.

Now here's the key point: Antigravity 2.0 is a huge departure from 1.0 in the sense that it is functionally no longer based on Microsoft'sVS Code. That means a huge majority of all the personalizations from 1.0 will not carry over to 2.0.

Yes, there was a quick patch that would let you import your customizations, including a migration flow that allows users to import settings, extensions, and keybindings from Antigravity 1.0. (Imagine a very eager person like me making the upgrade before this patch was applied). However any history and past work you've done in extensions like Claude, Cline, and Codex will not be carried over. Even your work history with the Gemini agents in 1.0 will not be ported.

If you want to retain as much information from your 1.0 setup, here's the playbook I wish I'd had on day one.

Back up before you click update.Specifically, copy~/.gemini/antigravitysomewhere safe. The migration has a known quirk where past conversations, scratch space, and agent brain entries get stranded in~/.gemini/antigravity-backuprather than carried into the new app. If you've already updated and your chat history looks gone, it isn't — that's where it went. You can rsync the backup directory back into~/.gemini/antigravity(skipmcp_config.json, you want the new one) and restart.

Say yes to installing the Antigravity IDE alongside 2.0.The IDE isn't being sunset — it's positioned as a sibling product, still maintained, still the VS Code fork you remember. That's where your keybindings, extensions, and editor muscle memory live. The cleanest mental model: 2.0 is for agent orchestration, the IDE is for everything VS Code-shaped you already do. Just don't run both against the same working tree simultaneously — you'll fight yourself.

If 2.0 isn't your speed yet, you can stay on the IDE.Uninstall 2.0, install Antigravity IDE 1.23.2 from the releases page, set updates to manual. There's no forced migration deadline on the IDE side — thedeprecation pressureis on Gemini CLI users (June 18, 2026), not Antigravity IDE users.

The mental note that helped me most:this isn't a version bump. It's Google shipping a second product that shares a name with the first. Your 1.0 work doesn't need to migrate — it needs to coexist. Once I stopped expecting parity and started treating 2.0 as a new tool in the kit, I felt better about this (but still licking my wounds from the re-work and missing stuff).

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse