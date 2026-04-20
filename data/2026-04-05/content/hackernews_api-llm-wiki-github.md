---
title: llm-wiki · GitHub
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
site_name: hackernews_api
content_file: hackernews_api-llm-wiki-github
fetched_at: '2026-04-05T11:12:33.124970'
original_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: tamnd
date: '2026-04-04'
description: 'llm-wiki. GitHub Gist: instantly share code, notes, and snippets.'
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# karpathy/llm-wiki.md

 Created

April 4, 2026 16:25



Show Gist options



* Download ZIP





* Star3,102(3,102)You must be signed in to star a gist
* Fork603(603)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.



Embed

# Select an option



* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found





Learn more about clone URLs





 Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;





Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

Download ZIP

 llm-wiki




Raw

 llm-wiki.md


# LLM Wiki

A pattern for building personal knowledge bases using LLMs.

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

## The core idea

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLMincrementally builds and maintains a persistent wiki— a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and thenkept current, not re-derived on every query.

This is the key difference:the wiki is a persistent, compounding artifact.The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

This can apply to a lot of different contexts. A few examples:

* Personal: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.
* Research: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.
* Reading a book: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis likeTolkien Gateway— thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.
* Business/team: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.
* Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives— anything where you're accumulating knowledge over time and want it organized rather than scattered.

## Architecture

There are three layers:

Raw sources— your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

The wiki— a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

The schema— a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

## Operations

Ingest.You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

Query.You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight:good answers can be filed back into the wiki as new pages.A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

Lint.Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

## Indexing and logging

Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

index.mdis content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

log.mdis chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g.## [2026-04-02] ingest | Article Title), the log becomes parseable with simple unix tools —grep "^## \[" log.md | tail -5gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.

## Optional: CLI tools

At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search.qmdis a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.

## Tips and tricks

* Obsidian Web Clipperis a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.
* Download images locally.In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g.raw/assets/). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.
* Obsidian's graph viewis the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.
* Marpis a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.
* Dataviewis an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.
* The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.

## Why this works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

## Note

This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.

Load earlier comments...



### peascommentedApr 5, 2026

@karpathyIt's great to see you as a piece of the current Zeitgeist of how AI is actually being applied. You've been synthesizing a lot of scattered thinking and currents into clear patterns, bringing signal out of the noise of a thousand simultaneous mini-projects. This gist is another example — the pattern needed a name and a shape, and you gave it one.

I've been building a voice-first version of this since February — same core architecture (raw → wiki → schema), with some extensions that might be interesting.

Voice-first capture.Most knowledge systems fail at capture, not synthesis. I record voice memos into Telegram while walking. Whisper transcribes, an LLM classifier tags and routes, a synthesizer updates interlinked KB nodes. No laptop needed. 70+ voice memos have compiled into 100 KB nodes and several published blog posts.

Two wiki layers.I split the wiki into KB (machine-managed reference: concepts, people, projects) and Drafts (a writing workspace). An intent classifier detects when I'm developing a blog post vs. planning a project vs. noting a task, and routes entries to the right draft. Multiple voice memos about the same topic get merged over days. The system doesn't just accumulate — it produces.

No content invention.The hardest constraint and the most important. The LLM must be an editor, not a writer — every sentence must trace to something the user actually said. Gaps get[TODO: ...]markers, not hallucinated filler. Without this you get a wiki full of plausible content you never thought. Dostoevsky dictated to his wife as stenographer; the LLM is my stenographer, not my ghostwriter.

Cross-links are mechanical, not LLM-generated.Title mentions in body text, slug pattern matching, journal co-occurrence. This avoids hallucinated connections and makes the knowledge graph trustworthy. You can see the graph live atpaulo.com.br/signals— 169 nodes, 195 links between posts, concepts, and source voice memos.

Provenance.Full traceability from published blog post back to the voice memo that sparked it. Each blog post links to its /signals subpage where you can listen to the original audio and read the raw transcription. The Zettelkasten had numbered cards with cross-references; this system has numbered voice memos with machine-traced lineage.

On why this is an idea, not a product.I think you're right to frame this as an idea rather than a spec. Each solution is deeply personal. How you capture (voice memos vs. web clippings vs. screenshots), how you process (pipeline vs. chat vs. deterministic scripts), how the graph gets wired — it's all particular to each person's thinking patterns. I don't think open source solves this. Each person will fabricate something that's a woven fabric of code and prompts that feed back into each other. It's disposable software that mutates constantly — neither the prompts nor the code are static. The system co-evolves with how you think.

More details:

* Open Claw, Personal Knowledge and the Second Brain(motivation + workflow)
* Building a PKM with Telegram, Whisper, and LLMs: Technical Decisions(file-based dedup, editor-not-writer prompts, auto markers, context-aware classification)
* Signals + KB Graph(the knowledge graph and signal grid)

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### pedronauckcommentedApr 5, 2026

I also create a skill here for this 😅https://github.com/pedronauck/skills/tree/main/skills/karpathy-kb

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### tkgallycommentedApr 5, 2026

Thank you for the idea, Andrej!

For the last few months, I have been using Claude Code to build a Japanese-English dictionary for people studying Japanese (GitHub,live site). The project is moving along smoothly, but its unavoidable complexity is making me uneasy about whether I have a strong enough grasp of the dictionary’s overall design and possible future directions. So I created a new directory in the repository called planning/, put your LLM wiki markdown file in it, and told Claude to start building a knowledge base that it would be able to refer to in the weeks and months ahead as the project continues to grow. I have scheduled a prompt to have Claude Code work on the knowledge base every night. It seems to be off to a good start, and I look forward to seeing how well this might help my project in the future.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### arnoldadlvcommentedApr 5, 2026

obsidian cli has been a life saver for this

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### bluewater8008commentedApr 5, 2026

We've been running this pattern in production for a few weeks across multiple related knowledge domains. A few things we learned that might help others:

1. Classify before you extract. When ingesting sources, don't treat every document the same. Classify by type first (e.g., report vs. letter vs. transcript vs. declaration), then run type-specific extraction. A 50-page report needs different handling than a 2-page letter. This comes from Folio's sensemaking pipeline — classify → narrow → extract → deepen — and it saves significant tokens while producing better results. Without it, you get shallow, uniform summaries of everything.
2. Give the index a token budget. The progressive disclosure idea is right, but it helps to make it explicit. We use four levels with rough token targets: L0 (~200 tokens, project context, every session), L1 (~1-2K, the index, session start), L2 (~2-5K, search results), L3 (5-20K, full articles). The discipline of not reading full articles until you've checked the index first is what makes this scale. Without it, the agent either reads too little or burns context reading everything.
3. One template per entity type, not one generic template. A person page needs different sections than an event page or a document summary. Define type-specific required sections in your schema. The LLM follows them consistently, and the wiki stays structurally coherent as it grows. Seven types has been our sweet spot — enough to be useful, not so many that the schema becomes overhead.
4. Every task produces two outputs. This is the rule that makes the wiki compound. Whatever the user asked for — an analysis, a comparison, a set of questions — that's output one. Output two is updates to the relevant wiki articles. If you don't make this explicit in your schema, the LLM will do the work and let the knowledge evaporate into chat history.
5. Design for cross-domain from day one. If there's any chance your knowledge spans multiple projects, cases, clients, or research areas — add a domain tag to your frontmatter now. Shared entities (people, organizations, concepts that appear in multiple domains) become the most valuable nodes in your graph. Retrofitting this is painful.
6. The human owns verification. The wiki pattern works. But "the LLM owns this layer entirely" needs a caveat for anyone using this in high-stakes contexts. The LLM can synthesize without citing, and you won't notice unless you look. Build source citation into your schema rules, and budget time to spot-check the wiki — not just the deliverables. The LLM is the writer. You're the editor-in-chief.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### xoaicommentedApr 5, 2026

Built this.sage-wiki— a single Go binary working cross platforms that does exactly what you described end-to-end:

sage-wiki init --vaulton an existing Obsidian vault, or simply run in a new empty folder.

Edit config.yaml to add API key, pick any LLM you want.

sage-wiki compilefor the first time compilesage-wiki compile --watchto incrementally compile sources into wiki articles with concepts, backlinks, and cross-references

The compiled outputs go back into Obsidian as markdown with [[wikilinks]] and YAML frontmatter — graph view spans both your source docs and the compiled articles.

sage-wiki search "any keyword"for searching through the knowledge basesage-wiki query "ask any question"for Q&A against the wiki with cited answers

Also built the linting piece you described. It catches inconsistencies, suggests missing connections, fills in gaps. Feels like having a research assistant that never forgets what it read.

If you want your familiar LLM interface working with your personal knowledge base? No problem.

sage-wiki serveexposes the wiki as an MCP server so any LLM agent can operate on it

The part that clicked for me was the same thing you mentioned, filing query outputs back into the wiki. Once you start doing that, the knowledge base genuinely compounds. Every question you ask makes it better at answering the next one.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### KeremSalmancommentedApr 5, 2026

Andrej, this is an absolute paradigm shift. Thank you.

I am currently going through a massive operational and personal "hard reset" in my life. I’ve been struggling with the stateless, fragmented nature of traditional RAG systems for personal knowledge management. Your concept of treating the LLM not just as a search engine, but as a continuously running "compiler" over a Markdown codebase provided the exact architecture I needed.

I am implementing this today as KS_LIFE_OS. I am feeding my raw daily data (physical rehab logs for a torn Achilles, complex VC meeting transcripts, and mental state markers) into the system, letting the LLM "lint" and compile them into a deterministic, version-controlled personal wiki in Obsidian.

As the lead architect of a Zero-Trust / Fail-Closed verification protocol (Mnemosyne), this approach deeply resonates with me. True memory isn't about semantic retrieval; it's about state management, lineage, and verifiable truth.

Thank you for open-sourcing your clarity. It just became the foundation of my reconstruction.

KS - Chief ArchiTech, Mnemosyne

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### karesansui-ucommentedApr 5, 2026

@karpathy日本語失礼！是非知ってもらいたいんだけど、トークン量じゃなくて、矛盾の蓄積が性能劣化の根本原因だから、自律的に矛盾を解消するアーキテクチャにしたらすごいいい感じになったよ。

だからそのまま要約・圧縮してもそのデータをもっていても、いつかは性能劣化しちゃう。

論理崩壞は背景的にちゃんと数学的な理由があって、それを解説してるから是非見てほしい！

https://github.com/karesansui-u/delta-zerohttps://zenodo.org/records/19396452https://zenodo.org/records/19396459

詳しく書いてます。論文のPDFとgithubのURLを高性能なLLMに読み込ませて！面白い反応すると思うよ！

・条件付き定理でLean証明済み・条件のA3は近似で良いことも証明済み・LLM実験でも効果あり確認済み

みんな早く気付いてくれるといいんだけど誰にも伝わらなくて困ってたよ。ありがとう。

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### VictorVVedtioncommentedApr 5, 2026

Loved this pattern. We implemented it inVibe Sensei— an AI trading terminal with 52 historical master guardians (Soros, Livermore, Buffett, etc.) that watch your trades and warn you in character.

Here's how we adapted the LLM Wiki pattern for real-time trading:

### Three-Layer Architecture (same spirit, trading twist)

1. Raw Sources → JSONL Event Store: Every trade, guardian alert, ghost warning, regime change, and circuit breaker fires into~/.vibe-sensei/events/YYYY-MM.jsonl. Nine event types, append-only, Zod-validated on read-back.
2. The Wiki →~/.vibe-sensei/wiki/: Markdown articles organized by domain:* markets/BTC-USDT.md— Per-symbol stats, win rate, regime history
* patterns/overview.md— Behavioral pattern frequency tables
* self/profile.md— Trader strengths/weaknesses (auto-derived)
* notes/— Query file-back articles (the compounding loop!)
3. The Schema → WikiTool: 6 operations matching Karpathy's model —compile,query,ingest,lint,browse,status.

### Key Adaptations

Dual compilation mode: Gemini 2.5 Flash for rich analysis, but a pure template fallback that generates valid wiki from statistics alone — zero API dependency. The wiki always works.

Incremental compilation:.compile-state.jsontracks the last processed event. Only new events get compiled. Template mode reads all events (to avoid erasing history); LLM mode gets a delta + existing article context.

Guardian context injection: After every trade, the guardian observer callsqueryWikiBySymbol(symbol)→ injects ~400 chars of your historical performance with that symbol directly into the guardian's personalized alert. Your guardian literally remembers your trading history with each asset.

The compounding loop(my favorite part):querywithfileBack=truesynthesizes an answer from multiple wiki articles, then files the synthesis as anewarticle innotes/. Next query benefits from the synthesis. Knowledge compounds.

Morning brief: On first startup each day, the system auto-compiles (if needed) then generates a brief: current regime + your top behavioral pattern + discipline streak + alert-heeding accuracy + wiki health score. All voiced by your assigned guardian's personality.

Counterfactual tracking: We track which guardian alerts you heeded vs ignored, then measure outcome accuracy. This feeds back into the wiki's trader profile — the system learns whether its own advice was good.

### What we learned

* Template fallback is non-negotiable. LLM APIs fail; your knowledge base shouldn't.
* ~400 chars is the sweet spot for context injection — enough to be useful, not enough to distract the LLM.
* The file-back loop from queries → new articles is where the magic happens. It turns passive Q&A into active knowledge accumulation.
* JSONL event store + markdown wiki is a surprisingly robust combo. Human-readable, git-friendly, zero infrastructure.

Built with Bun + TypeScript. The wiki system is ~2000 lines across compiler, query engine, ingest pipeline, health auditor, and the guardian integration layer.

Repo:github.com/VictorVVedtion/vibe-sensei

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### pjmattinglycommentedApr 5, 2026

Hi, thanks for this. I've been working on implementing something similar, but using NotebookLM as the backing "wiki" layer. Here's the latest ...

see:https://github.com/pjmattingly/Claude-persistent-memory

It's not ready for release, but I'd welcome feedback.

Take care. <3

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ycc42commentedApr 5, 2026

Thanks for sharing! Excited to put this into practice

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### hrishikeshscommentedApr 5, 2026

This is exactly what I've been trying to do with this PR on claude code:anthropics/claude-code#25879

and a version of it is built into my emacs manager:https://github.com/hrishikeshs/magnus

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### mpazikcommentedApr 5, 2026

I've been doing this for a while now and there are two things that break first.

Queries.Once you're past a few hundred pages you want to ask your wiki things. "What did I add last week about X?" "Show me everything tagged unverified." You can't do that by reading files. The index helps early on but it doesn't scale.

Structure.It creeps in whether you plan it or not. Frontmatter, naming conventions, folder rules. The wiki grows a schema on its own. At some point you realize you're fighting your tools instead of working with them.

That's what got me to flip it. Instead of files that slowly become a database, start from structured data that renders as markdown. The index isn't a file the agent maintains by hand. It's a query. Always current.

I've been buildingBinderaround this. Data goes into a transaction log, gets indexed in SQLite, and every entity shows up as a markdown file you can edit in whatever editor you want. Edits go back in. Agent writes through an API. Both directions.

https://assets.binder.do/binder-demo.mp4

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### localwolfpackaicommentedApr 5, 2026

with the Ingest/Query operation, a good idea might be to include a Divergence Check. Every time the LLM updates a concept page, it must generate a hidden section called ## Counter-Arguments & Data Gaps.

So if you ingest 5 articles praising a specific UI framework, the LLM should be tasked to search for (or simulate) the most sophisticated critique of that framework. could make a good sanitized version of your own biases.

ive been noticing my bias more lately....maybe just me 😉

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### Astro-HancommentedApr 5, 2026

Turned this into a plug-and-play skill for Claude Code / Cursor / Codex. One install, then just tell your agent "ingest this URL" and it handles the raw → wiki compilation, cross-references, and index.

npx add-skill Astro-Han/karpathy-llm-wiki

The part that clicked for me: once you set up the three-layer flow (raw → wiki → index), each new source genuinely enriches the existing articles instead of just piling up. The wiki compounds.

https://github.com/Astro-Han/karpathy-llm-wiki

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### tlk3commentedApr 5, 2026

vibe-coded a potentially better IDE for this kind of thinking flow:https://github.com/anuragrpatil23/Thinking-Space

Curious to hear any thoughts or feedback from folks trying similar setups!   tldr: Obsidian updated for the Claude Code / agent era — local-first AI native Markdown workspace

This looks sick.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### uggrockcommentedApr 5, 2026

This is essentially what I've been converging toward, except my raw sources aren't just articles — they include PDFs, saved emails, screenshots of whiteboards, bookmarked web pages, and voice memo transcripts. Obsidian handles the wiki layer well but struggles as a file browser for non-markdown formats. I prefer usingTagSpacesto manage the raw sources folder (it previews everything inline, and tagging works across file types), then pointing the LLM at that folder for ingestion. The separation of "browsable file manager for raw inputs" vs "structured wiki for compiled knowledge" maps nicely onto the three-layer architecture described here.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### LakshX413commentedApr 5, 2026•edited

Thanks for sharing! Have been working on something like for a niche technical space. Look forward to injecting your thoughts also into the project.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ractivecommentedApr 5, 2026

I built a tool to exactly help an LLM navigate and search a knowledgebase of md files. It helps a lot to build such a wiki by providing basic content search à la grep but also structured search for frontmatter properties. It also helps to move files around without breaking links and to fix links automatically. It is a CLI tool, mainly meant to be driven by AI tools.

Check it out:https://github.com/ractive/hyalo

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### OkohedekicommentedApr 5, 2026

I've done something similar but I pulled in a lot of other sources. Mainly tiktoks/tweets/youtube/etc.https://github.com/Okohedeki/NANTA. Main issue I see with many people with this is you are collecting a knowledge base but are you actually consuming that knowledge? Part of my workflow was to create different formats for the injestable data so I can come back to it. Converted nearly all of my bookmarked tweets and tiktoks over to this to build out my own podcasts.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### nachoadcommentedApr 5, 2026

Thanks for sharing!I personally love the idea of Personal Knowledge Management/Base (PKM). So I'll be following the community's ideas on this topic closely. 😀

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### flyerswordercommentedApr 5, 2026

We've been building something along similar lines since mid-March:LENS— but focused ondistilling higher-order patterns across papersrather than summarizing individual sources.

The core idea: LLM extracts structured tradeoffs, architecture variants, and agentic patterns from research papers, then aggregates them into cross-paper knowledge structures — acontradiction matrix(which techniques resolve which tradeoffs, inspired by TRIZ), anarchitecture catalog(component variants organized by slot), and anagentic pattern catalog(emergent categories). A single insight might be backed by 10+ papers.

This scales because new papers slot into existing structures automatically via a canonical vocabulary — the LLM normalizes concepts at extraction time using guided extraction, so no manual curation or post-hoc clustering is needed.

After reading this post, we added two features directly inspired by it:

* Lint(lens lint) — the health-check operation, with 6 checks and auto-fix
* Event log(lens log) — chronological audit trail

Backend is SQLite + sqlite-vec (hybrid FTS5 + vector search), along the lines mpazik suggested above.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### jahalacommentedApr 5, 2026•edited

@karpathy- I'd be curious to hear what you think abouthttps://www.github.com/jahala/o-o/.... Polyglot bash / html that is "self-updating" .. can be used for self-updating articeles, wikis, etc.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### karan842commentedApr 5, 2026

@karpathyjust curious about your opinion on LLM As A judge? I am thinking of implementing your LLM wiki architecture with LLM as a judg.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ilyabelikincommentedApr 5, 2026•edited

@karpathyI built the same idea but for People and orgs intelligencehttps://github.com/Know-Your-People/peeps-skill

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### luotwocommentedApr 5, 2026•edited

@karpathyI also create a skill here for thishttps://github.com/luotwo/llm-wiki

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### tcbhagatcommentedApr 5, 2026

I am not clear about how to use it on my Ubuntu desktop pc ? What to use and how?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### jeremyraynercommentedApr 5, 2026

Thanks Andrej, made a forkable repo using only your core ideas, so I can have a play with the this over the holidays -https://github.com/jeremyrayner/kb-template

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### GuiminChencommentedApr 5, 2026

Thanks@karpathy— this gist nails the “persistent wiki as compounding artifact” framing.I’ve been building CRATE around the same three-layer idea: immutable raw/, LLM-maintained wiki/, and schema/agent hints. It’s a file-first Python CLI (compile / ask / lint / ingest, Obsidian-friendly paths, OpenAI-compatible providers). Open source here:https://github.com/GuiminChen/crateSharing in case others want a concrete reference implementation, not a product pitch — the gist remains the conceptual source of truth.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### Done-0commentedApr 5, 2026

I have the same idea as this.

https://github.com/Done-0/openarche

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.





Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
