---
title: "I Rebuilt My Karaoke App So Everyone's Phone Could Be a Remote - DEV Community"
url: https://dev.to/lehuygiang28/i-rebuilt-my-karaoke-app-so-everyones-phone-could-be-a-remote-4k8b
date: 2026-06-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-02T06:01:33.467575
---

# I Rebuilt My Karaoke App So Everyone's Phone Could Be a Remote - DEV Community

# I Rebuilt My Karaoke App So Everyone's Phone Could Be a Remote

## What I Built
- VKara is a browser‑based karaoke room where a TV or laptop plays YouTube videos and phones act as remotes.  
- Users join a room with a 4‑digit code or QR, then can search, queue, pause, resume, or skip songs together.  
- The app focuses on shared playback control rather than video hosting.

## Demo
- Live demo: https://vkara.vercel.app/en  
- Source code: https://github.com/lehuygiang28/vkara  
- Previous branch (pre‑refactor): https://github.com/lehuygiang28/vkara/tree/before  
- Old backend repo: https://github.com/lehuygiang28/vkara-api  
- Usage flow: open on TV/laptop → join from phone → search → add to queue → control playback.

## What Changed
- **Before**: separate frontend and backend repos, compressed desktop UI on mobile, scattered WebSocket contracts, TV screen overloaded with controls.  
- **After**: merged into a Bun workspace monorepo, shared types in `packages/shared-types`, clear role separation (TV = screen, phone = remote), streamlined mobile flow (join → search → queue → control), improved room state handling, reconnection, playback sync, and deployment.

## The Comeback Story
- Started in early 2025 to solve awkward YouTube karaoke setups (searching, accidental plays, unclear queue, Wi‑Fi casting).  
- Initial prototype proved the idea but suffered from UI clutter, fragile real‑time state, and split repositories, making changes risky.  
- Paused development, then returned to focus on making the codebase safe to modify.  
- Key steps:
  - Consolidated frontend and backend into a single monorepo with clear folder structure (`apps/web`, `apps/api`, `packages/shared-types`, `packages/shared-utils`).  
  - Adopted a two‑role model: TV/laptop as playback screen, phone as remote, simplifying responsibilities.  
  - Refined UX to prioritize joining, searching, queuing, and singing.  
  - Fixed low‑level issues: WebSocket room state, reconnect logic, playback synchronization, queue updates, Docker builds, GitHub Actions, Vercel deployment.

## My Experience with GitHub Copilot
- Shifted from naive code generation to using Copilot as an investigative and planning partner.  
- Utilized **Ask Mode** to recall project decisions (e.g., why Zustand is used instead of SWR/React Query).  
- Employed **Plan Mode** to outline complex refactors such as the monorepo migration, preserving history and identifying shared contracts.  
- Adopted a workflow: think → ask → plan → execute → verify → repeat.  
- Leveraged Copilot for debugging (pasting TypeScript errors, Docker logs), UI tweaks (screenshots), and architectural comparisons.  
- Recognized that the real value lies in solving human‑centric problems (queue fairness, quick rejoin, persistent rooms) rather than adding flashy features.