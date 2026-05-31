---
title: '🎙️ How I AI: How the engineer behind Claude Cowork actually uses Claude Cowork & What launched at Google I/O 2026'
url: https://www.lennysnewsletter.com/p/how-i-ai-how-the-engineer-behind
site_name: tldr
content_file: tldr-how-i-ai-how-the-engineer-behind-claude-cowork-act
fetched_at: '2026-06-01T04:17:45.706767'
original_url: https://www.lennysnewsletter.com/p/how-i-ai-how-the-engineer-behind
author: Lenny Rachitsky
date: '2026-06-01'
description: Your weekly listens from How I AI, part of the Lenny’s Podcast Network
tags:
- tldr
---

How I AI

# 🎙️ How I AI: How the engineer behind Claude Cowork actually uses Claude Cowork & What launched at Google I/O 2026

### Your weekly listens from How I AI, part of the Lenny’s Podcast Network

Lenny Rachitsky
May 25, 2026
252
1
6
Share

### How the engineer behind Claude Cowork actually uses Claude | Felix Rieseberg (Anthropic)

Listen now onYouTube•Spotify•Apple Podcasts

Brought to you by:

* Magic Patterns—Prototypes that look like your product
* Guru—The AI layer of truth

Felix Rieseberg, the engineering lead for Claude Cowork and Claude Code Desktop at Anthropic, joins Claire to show how he actually uses Claude in his own life and work. In this episode, Felix walks through building a 3D floor planner from a 2D house plan, using email as a personal inventory database, creating live dashboards from connected apps, and hacking together a $20 hardware “Claude buddy.” He also shares his philosophy for getting more out of AI: go one abstraction layer up, let Claude work in the background, and stop assuming computers can’t solve some of the annoying little problems in your life.

#### Biggest takeaways:

1. The biggest barrier to AI adoption is people not realizing they can ask AI to solve almost any problem.Felix sees this constantly—the tools are incredibly powerful, but users haven’t built the muscle memory to reach for them. His advice: whenever you’re doing something annoying that doesn’t feel creative, pause and ask yourself if Claude could do it instead. The gap isn’t technical; it’s psychological.
2. Your email is an untapped gold mine of personal data.Felix used his email to inventory all his furniture when moving houses: every purchase receipt, every confirmation, every dimension. Claude parsed it all and built him a 3D floor planner with his actual furniture. This same principle applies to clothing, medical records, travel history, or any domain where you’ve been emailing receipts and confirmations for years. You already have a structured database—you just need to point Claude at it.
3. Go one abstraction layer up, then do it again.Felix started manually entering furniture dimensions into his floor planner, then stopped and asked Claude to figure out what furniture he had. Then he went another layer up and told Claude to find the furniture in his emails. This is the key pattern: every time you catch yourself doing tedious work, ask how Claude could do it instead. Then ask how Claude could figure out what to do without your telling it.
4. Live artifacts are Claude’s answer to keeping your personal dashboards always up-to-date.Unlike static artifacts, live artifacts refresh with real-time data from your connected services—Spotify, Gmail, Calendar, Notion, whatever you’ve authorized. Felix built a personal dashboard that looks like early-2000s software that updates throughout the day. The killer feature: you never have to manually update your pitch deck, your daily briefing, or your personal reports again.
5. Choose Opus when you don’t know what you’re really asking for.Felix’s heuristic for model selection: use Sonnet when the problem is well-scoped and specific. Reach for Opus when you need Claude to interpret what you actually want, not just what you said. It’s the difference between “make me a floor plan with units” (Sonnet territory) and “help me figure out how to organize my life” (Opus territory). For most tasks, Sonnet is perfectly capable, but when you need that extra layer of problem decomposition, Opus is worth it.
6. Kids are the best AI users because they aren’t afraid to ask for things.Felix gets videos from parents showing what their kids build with Claude—custom video games with hand-drawn characters, interactive stories, tools that would have required a software engineer just a few years ago. Adults have spent 20 years in a “mind prison” learning what computers can’t do. Unlearning that is the unlock.
7. When Claude makes mistakes, debug your workflow, not the model.Felix doesn’t curse at Claude (though he notes it’s useful for the team to know when people do). Instead, he asks it: “Here’s what I expected. Can you walk me through where things went differently? How can we prevent this in the future?” Usually the fix isn’t “Claude can’t do this”; it’s “I need to change the prompt, clean up the data source, or set up a dry run.” Treat Claude like a collaborator who needs better instructions, not a tool that’s broken.

#### Blog & detailed workflow walkthroughs from this episode:

How I AI: Felix Rieseberg’s Claude Workflows for 3D House Design and a $20 Hardware Buddy:https://www.chatprd.ai/how-i-ai/felix-rieseberg-claude-code-cowork-workflows-for-3d-house-design-and-hardware-buddy

↳How to Build a $20 Physical AI ‘Buddy’ with Claude Code:https://www.chatprd.ai/how-i-ai/workflows/how-to-build-a-20-physical-ai-buddy-with-claude-code

↳How to Create an Interactive 3D House Model from a Floor Plan Using AI:https://www.chatprd.ai/how-i-ai/workflows/how-to-create-an-interactive-3d-house-model-from-a-floor-plan-using-ai

↳How to Build a Live, Auto-Updating Personal Dashboard with Claude:https://www.chatprd.ai/how-i-ai/workflows/how-to-build-a-live-auto-updating-personal-dashboard-with-claude

### What launched at Google I/O 2026 (30-minute day 1 recap)

Listen now onYouTube•Spotify•Apple Podcasts

Brought to you by:

* Magic Patterns—Prototypes that look like your product
* ThoughtSpot—Build AI-powered analytics into your product

Claire breaks down the biggest launches from Google I/O 2026—from Gemini 3.5 Flash and Antigravity 2.0 to Google AI Studio, Omni, Flow, Stitch, and Pomelli. In this episode, she tests the tools live, shares what actually works, and explains where Google is catching up, where it may be pulling ahead, and why its launch-to-availability gap is still such a problem for builders.

#### Biggest takeaways:

1. Gemini 3.5 Flash rivals leading frontier coding models in Google’s benchmarks while running four times faster.Google positions this as their agentic coding model, optimized for tasks requiring both high reasoning and rapid execution. If the benchmarks hold in practice, this speed advantage could shift the coding agent landscape toward Google’s tools.
2. Antigravity 2.0 brings Google’s IDE to feature parity with Claude Code and Codex—but it’s playing catch-up.The update includes projects (folder-constrained workspaces), scheduled tasks on Cron, and subagents for specific tasks. The UI looks nearly identical to Codex, and the features match what Anthropic and OpenAI shipped months ago. The advantage is speed: if Gemini 3.5 Flash delivers, developers might choose Antigravity for well-scoped tasks that need to ship fast.
3. The /grill-me slash command is Antigravity’s aggressive take on Claude Code’s polite clarification tool.Instead of gently asking questions, /grill-me promises to interrogate your requirements and get to the heart of what you’re building. Whether this is actually more hardcore or just clever branding remains to be seen, but it signals Google’s attempt to differentiate on personality.
4. Google AI Studio now integrates directly with Workspace apps—or it’s supposed to.The promise: build no-code apps that read Sheets, draft Gmails, organize Drive, and see Calendar without setup. Claire couldn’t get it to work during testing. If it delivers, it would capture internal enterprise productivity use cases and personal assistant workflows where Google already owns the data layer.
5. Omni is Google’s answer to Sora, focused on longer, production-quality video.The model creates 10-second videos (versus Sora’s 6 or 7 seconds), maintains character consistency across edits, and allows conversational editing. Claire tested it by animating her kid’s drawing, and the output was impressive. The real power will be in production workflows where you iterate on the same characters and scenes multiple times.
6. Flow is Google’s production-grade video editor built on Omni.It lets you define characters, create avatars, and edit videos conversationally while maintaining cinematic quality. The tool targets creators and marketers who need consistent, high-quality video at scale. Claire tried creating an avatar of herself, but the feature failed—a recurring theme throughout I/O announcements.
7. Stitch and Pomelli are Google’s design and marketing tools.Stitch is like in-browser Figma with streaming design generation, inline AI edits, and code sync. Pomelli creates brand books, campaign assets, and websites from a URL. Both show promise but suffer from “Google slop,” the generic aesthetic of AI-generated design.
8. Gemini’s multimodal capabilities remain its strongest differentiator.For work involving files, videos, or transformative work across modalities (document to video, image to text), Gemini models excel. Claire uses them for generating blog posts from podcast videos and animating drawings. The 3.5 family continues this strength; for these use cases, Gemini’s multimodal performance is best-in-class.
9. The biggest problem: half the features don’t actually work yet.Claire encountered broken features, missing integrations, and “coming soon” disclaimers throughout testing. Workspace integration in AI Studio? Couldn’t access it. Avatar creation in Flow? Didn’t work. When you announce features that aren’t ready, people lose patience and stop trusting your roadmap.

#### Blog:

How I AI: My Live Test of Google I/O’s New AI Tools—From Gemini 3.5 Flash to Omni Video:https://www.chatprd.ai/how-i-ai/google-io-new-ai-tools-gemini-35-flash-to-omni-video

If you’re enjoying these episodes, reply and let me know what you’d love to learn more about: AI workflows, hiring, growth, product strategy—anything.

Catch you next week,Lenny

P.S. Want every new episode delivered the moment it drops? Hit “Follow” on your favorite podcast app.

252
1
6
Share
Previous
Next