---
title: Why TUIs are back by Alcides Fonseca
url: https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/
date: 2026-05-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:53:09.784754
---

# Why TUIs are back by Alcides Fonseca

# Why TUIs are back

## Introduction
- Terminal User Interfaces (TUIs) are resurging as a practical alternative to fragmented native GUI toolkits.
- The author notes a historical shift from native editors (BBEdit, TextMate, Notepad++, Sublime) to Electron‑based code editors (Atom, VSCode) and the subsequent retreat of hardcore users to Vim/Emacs for speed and consistency.

## Windows
- Native Windows GUI frameworks have been inconsistent: MFC wrapped Win32, followed by OLE/COM, ActiveX, then a succession of APIs (WinForms, WPF, Silverlight, WinUI, MAUI) without a coherent strategy.
- Each new layer introduces gaps and complexity, making it hard to maintain visual integration across the OS.
- Many applications resort to Electron because rebuilding native UI layers every few years is costly and error‑prone.

## Linux
- UI inconsistency is intentional: different teams chose different toolkits (GTK, Qt) leading to a diversity of looks.
- Despite this, applications built with GTK or Qt can coexist reasonably well, unlike the Windows situation.
- Testing across the myriad of distributions, desktop environments, and hardware combinations discourages companies from investing in native Linux apps; they often default to Electron or rely on community‑driven solutions.

## macOS
- Apple once provided a single, well‑documented Human Interface Guidelines that shaped UI education worldwide.
- Recent releases ignore established principles (e.g., Fitts’ law), make window resizing difficult, and overload menus with icons, reducing the platform’s consistency and designer friendliness.

## Electron
- Electron apps are criticized for high memory usage and lack of visual consistency, especially regarding keyboard‑driven workflows.
- Example: Cursor (and VSCode) do not expose common navigation actions via obvious shortcuts or menu items, forcing users to rely on hidden HTML‑based interfaces.
- Even Slack, which handles shortcuts better, is not perfect.

## Restarting from scratch
- Google attempted a fresh OS and UI toolkit (Flutter) with Dart but abandoned it before a product launch, highlighting the need for market dominance to succeed.
- Zed created a cross‑platform GPU renderer (GPUI) in Rust; while fast, it lacks deep OS integration, forcing developers to add bindings manually.
- The author prefers slower, well‑integrated renderers over high‑speed but isolated solutions.

## TUIs
- TUIs are fast, easy to automate, and work uniformly across operating systems, including remote sessions without X forwarding.
- They fill the void left by inconsistent native toolkits, offering a consistent, keyboard‑centric experience.
- AI assistants like Claude and Codex thrive on the command line, emphasizing interaction over OS‑specific UI concerns.

## What’s next
- Interfaces should require minimal thought; consistent shortcuts (e.g., Cmd + C) must work everywhere.
- Developers need solid UI theory knowledge (Nielsen, Norman, Johnson) and should treat UI design as a core software engineering skill.
- Educational curricula should enforce sensible UI design, rejecting projects with poor interfaces.
- Toolkit and OS authors should invest in accessible, low‑barrier frameworks to reduce reliance on Electron and TUIs, aiming for long‑lasting, homogeneous user experiences.