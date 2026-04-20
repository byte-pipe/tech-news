---
title: I vibe-coded an internal tool that slashed my content workflow by 4 hours - DEV Community
url: https://dev.to/dumebii/i-vibe-coded-an-internal-tool-that-slashed-my-content-workflow-by-4-hours-310f
date: 2026-02-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-03-03T06:02:24.286058
---

# I vibe-coded an internal tool that slashed my content workflow by 4 hours - DEV Community

# I vibe‑coded an internal tool that slashed my content workflow by 4 hours

## Problem & Motivation
- Repurposing blog posts for social media was time‑consuming; I had to ask AI for summaries or do it manually.
- Need for a Human‑in‑the‑Loop (HITL) workflow was emphasized in a recent content‑professionals meeting.
- Existing AI tools lacked context about my research, voice, and technical nuances.

## Solution Overview
- Built an **Agentic Content Engine** that reads my dev.to articles, creates a 3‑day multi‑platform campaign, lets me audit and edit, and deploys with a single click.
- Emphasized agency over pure automation: the agent reasons, structures, and waits for my approval before posting.

## Technical Stack
- **Reasoning Engine:** Gemini 3.1 Pro (Tier 1) for complex instruction following and strict JSON schema enforcement.
- **Frontend:** Next.js 15 (App Router) for server‑side rendering and SEO.
- **Styling:** Tailwind CSS with `@tailwindcss/typography` for markdown rendering.
- **Deployment:** Discord Webhooks for instant, zero‑auth execution.

## Handling AI Hallucinations in Next.js
- Gemini often returns JSON wrapped in markdown code blocks, causing `JSON.parse` failures.
- Implemented a sanitization middleware using regex to strip markdown wrappers before parsing.
- Added error handling to return a clear message if parsing fails.

## UI/UX Strategy: Kanban‑style Board
- Initial UI was cluttered; moving to a columnar dashboard improved readability.
- Created a `PostCard` component that truncates content to 250 characters with a “Read More” toggle, allowing quick audits without excessive scrolling.

## Agentic Content Flow (Photo Dump)
1. **Dashboard start:** Minimal “command centre” view.
2. **3‑Day Campaign Map:** Paste article URL → agent generates a structured 3×3 grid of posts, each truncated with a toggle.
3. **Deployment:** Click “Post to Discord” → content is sent instantly, eliminating manual copy‑pasting.

## Future Roadmap (BloggerHelper v1)
- Add X (Twitter) and LinkedIn publishing integrations.
- Expand the “context tank” beyond the article and `agents_instruction.md`.
- Implement an edit‑before‑post feature.
- Allow ingestion of additional context sources besides blog posts.

## Conclusion
- The tool reduced my workflow by roughly 4 hours, shifting my role from technical writer to content engineer/architect.
- It demonstrates how AI can be used responsibly with HITL, reinforcing my position as an AI influencer.

**Call to Action:**
- Connect with me on LinkedIn.
- Share your thoughts on agentic workflows—full automation or keeping the human in the loop?

---

*Note: The tool is live; try it, but be mindful of API credit usage.*
