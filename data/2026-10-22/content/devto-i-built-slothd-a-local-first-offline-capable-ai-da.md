---
title: 'I Built slothd: A Local-First, Offline-Capable AI Daemon That Patiently Organizes Your Messy Workspace - DEV Community'
url: https://dev.to/dj29/i-built-slothd-a-local-first-offline-capable-ai-daemon-that-patiently-organizes-your-messy-53e7
site_name: devto
content_file: devto-i-built-slothd-a-local-first-offline-capable-ai-da
fetched_at: '2026-10-22T22:04:33.647273'
original_url: https://dev.to/dj29/i-built-slothd-a-local-first-offline-capable-ai-daemon-that-patiently-organizes-your-messy-53e7
author: Dhruv Jani
date: '2026-10-21'
description: 'This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady 💡... Tagged with devchallenge, hf26challenge, opensource, gemma.'
tags: '#devchallenge, #hf26challenge, #opensource, #gemma'
---

Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady Submission 🦥

This is a submission for theHacktoberfest Open-Source AI Challenge Week 3: Slow and Steady

💡Quick Navigation:What I Built·Live Demo·Code·Architecture & Funnel·Open Innovation·Lazy Payoff·Prize Categories (8 Tracks)·Discussion

📖 Table of Contents(Click to expand)

* What I BuiltWho gets to be a little lazier because of it?
* Who gets to be a little lazier because of it?
* Demo35-Second Walkthrough DemonstrationThe Offline Demo Fixture
* 35-Second Walkthrough Demonstration
* The Offline Demo Fixture
* Code & Key Modules
* How I Built It (Two-Stage Intelligence Funnel)The Architecture: Two-Stage Prediction FunnelStage 1: Prior Labs TabPFN Metadata TriageStage 2: Gemma 3 Local Vision & Extraction via OllamaSafe, Reversible Operations via SQLite WALObservability: Using Sentry as an Active Debugging Loop
* The Architecture: Two-Stage Prediction Funnel
* Stage 1: Prior Labs TabPFN Metadata Triage
* Stage 2: Gemma 3 Local Vision & Extraction via Ollama
* Safe, Reversible Operations via SQLite WAL
* Observability: Using Sentry as an Active Debugging Loop
* Why Does Open Innovation Matter?
* The Lazy Payoff
* Prize Categories & Partner Tracks⏱️ 10-Second Judge Navigation Matrix1. Grand Prize: Hacktoberfest Week 3 "Slow and Steady"2. Featured Track: Best Use of Gemma3. Featured Track: Best Use of TabPFN4. Partner Track: Best Use of Tiger Data5. Partner Track: Best Use of Sentry Agent Tracing6. Partner Track: Best Use of SerpApi7. Partner Track: Best Use of ElevenLabs8. Partner Track: Best Use of GitHub Copilot9. Partner Track: Best Use of Entire
* ⏱️ 10-Second Judge Navigation Matrix
* 1. Grand Prize: Hacktoberfest Week 3 "Slow and Steady"
* 2. Featured Track: Best Use of Gemma
* 3. Featured Track: Best Use of TabPFN
* 4. Partner Track: Best Use of Tiger Data
* 5. Partner Track: Best Use of Sentry Agent Tracing
* 6. Partner Track: Best Use of SerpApi
* 7. Partner Track: Best Use of ElevenLabs
* 8. Partner Track: Best Use of GitHub Copilot
* 9. Partner Track: Best Use of Entire
* 🦥 Parting Sloth Thoughts: Reclaiming Digital Calm💬 Community Discussion
* 💬 Community Discussion

## What I Built

Last week I randu -sh ~/Downloadson my laptop and realized I was hoarding hundreds of cryptic PDFs (INV-9041-final(1).pdf), forgotten.exeinstallers, and unnamed screenshots—and I refused to upload my private bank receipts or.envconfigs to a cloud AI just to sort them. So for International Sloth Day, I built a daemon that waits until I walk away from my keyboard and cleans the mess locally while I sleep.

Workspaces, Desktop dumps, and project inboxes are where good intentions go to hibernate. Cryptic filenames pile up (Screenshot 2026-10-18 at 2.34.12 PM.png,INV-9041-final(1).pdf,DockerDesktopInstaller.exe). Receipts, strategy documents, archives, and configuration files end up in a flat, unorganized heap because standard file extensions tell you almost nothing about what a document actuallycontains.

I builtslothd, a local-first, offline-capable AI file organizer designed around the philosophy of"Slow and Steady":

* Patient Idle Activation: Uses native OS APIs to measure keyboard and mouse inactivity. It sleeps while you work and only activates when you step away.
* Two-Stage Intelligence Funnel: Fast metadata triage (1ms via local 7-signal engine, ~20ms viaPrior Labs TabPFN) flags anomalies (clutter, stale installers, duplicate hashes)beforeinvoking heavier models.
* Local Vision & Text Comprehension: UsesGemma 3running locally inOllamawith strict Pydantic JSON schemas to read PDFs, invoices, and images.
* Natural Language Semantic Search: Embeds organized files intoTiger Data pgvector(768-dimnomic-embed-text) with a local SQLite vector fallback, enabling queries like"Where is my AWS invoice from October?".
* Non-Destructive & Reversible: Every run is a dry-run by default. Every approved move is written to an SQLite WAL log with a unique batch ID. If you dislike what it did,slothd undorestores every file to its exact original path.
* Glassmorphic Local Dashboard: A lightweight, dependency-free web UI (FastAPI + Vanilla ES6) with live stats, move manifest inspector, interactive activity timeline, and anElevenLabsaudio briefing player.

🔒Local-First & Air-Gapped by Default:The entire core workflow—idle detection, filesystem scanning, tabular metadata triage, Gemma 3 document understanding via local Ollama, SQLite WAL manifests, and 1-click rollback—executes100% locally on your machine with zero internet calls. A genuinely air-gapped deployment simply leaves external integrations disabled. Cloud partner services (Tiger Data pgvector, SerpApi vendor lookup, ElevenLabs voice) are strictly opt-in extensions via explicit CLI flags (--enrich-online), and each is engineered with a complete offline fallback (local SQLite vector search, local heuristics, terminal audio chimes). No personal file or metadata ever leaves your device by default.

### Who gets to be a little lazier because of it?

Every developer, creator, and researcher who wastes 20 minutes every week digging through unorganized files, manually dragging PDFs into dated folders, or putting off digital cleanup. You let the sloth run patiently while you make coffee, return to an inspected plan, and keep complete control.

## Demo

The complete interactive loop demonstrates the full lifecycle:

Messy Workspace 
 ➜ Fast Metadata Triage (TabPFN / Local Heuristic) 
 ➜ Local AI Plan (Gemma 3) 
 ➜ Dry-Run Preview 
 ➜ Explicit Approval 
 ➜ Semantic Search (Tiger Data) 
 ➜ SQLite Manifest Inspection 
 ➜ 1-Click Rollback

Enter fullscreen mode

Exit fullscreen mode

### 35-Second Walkthrough Demonstration

* Universal MP4 Video (1.29 MB):slothd-demo.mp4(Encoded with H.264yuv420p+faststartfor instant playback across all browsers)
* High-Definition WebM (4.65 MB):slothd-demo.webm
* High-Res Static Screenshot:08-dashboard.png

### The Offline Demo Fixture: Reproduce in 10 Seconds

You don't need to risk your own files to evaluateslothd. The repository includes a deterministic test fixture intest_workspace/messy_inboxcontaining an invoice, duplicate invoice, Uber receipt, project notes, Python benchmark, configuration file, leftover Windows installer, stale zip archive, and unsorted screenshots.

Anyone can clone and run the scan immediately:

git clone https://github.com/JaniDhruv/slothd.git

cd 
slothd
uv run slothd scan test_workspace/messy_inbox

Enter fullscreen mode

Exit fullscreen mode

In under a second, you will observe the verified metrics:

* 10 filesscanned
* 2 clutter anomaliesflagged in 1 ms (via deterministic 7-feature triage engine / TabPFN schema)
* 1 exact duplicate setdetected via SHA-256 (973 B reclaimable)
* 0 cloud API callsrequired (100% air-gapped isolation)

## Code

The project is 100% open-source under the MIT License:

👉GitHub Repository:github.com/JaniDhruv/slothd

### Key Source Modules

* CLI & Interactive TUI:slothd/cli.py&slothd/ui.py
* TabPFN Anomaly Engine:slothd/engine/tabular_predictor.py
* Gemma 3 Vision Classifier:slothd/engine/classifier.py
* Reversible Move Orchestrator:slothd/engine/organizer.py
* Tiger Data pgvector Search:slothd/engine/search.py&slothd/integrations/tiger_data.py
* Sentry Tracing & Circuit Breaker:slothd/integrations/sentry_tracing.py
* Local Web Dashboard:slothd/web/
* Verified Evidence Suite:docs/demo/

## How I Built It

A file organizer that feeds every single file into a heavy vision model is noisy, slow, and expensive. Instead,slothduses a structured two-stage funnel:

┌────────────────────────────────────────────────────────┐
│ Messy Target Directory │
└───────────────────────────┬────────────────────────────┘
 │
 1. Deduplicate & Extract Features
 │
 ▼
┌────────────────────────────────────────────────────────┐
│ STAGE 1: Prior Labs TabPFN Metadata Triage │
│ (7 tabular signals: log size, depth, ext, time, etc.) │
└─────────────┬────────────────────────────┬─────────────┘
 │ │
 Leftover installers, archives, │ Needs deeper
 screenshots, duplicate clutter │ semantic classification
 ▼ ▼
 Flagged for cleanup ┌────────────────────────┐
 │ STAGE 2: Gemma 3 Local │
 │ (Ollama Vision/Text) │
 └──────────┬─────────────┘
 │
 ▼
 ┌────────────────────────┐
 │ SQLite Reversible Log │
 │ + Tiger Data pgvector │
 └────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

### Stage 1: Lightweight Tabular Triage (Prior Labs TabPFN)

Before running AI models,slothdextracts 7 tabular signals from the filesystem:

1. Log-scaled file size
2. Extension category group
3. Path depth
4. Hour of modification
5. Day of week
6. Filename length
7. Numeric/UUID entropy signal

When TabPFN credentials or a local model checkpoint are configured, TabPFN evaluates these tabular feature distributions directly (taking ~15–25 ms). To guarantee strict zero-credential, air-gapped operation by default,slothdalso bundles a calibrated deterministic heuristic engine (TabPFN-Heuristic-Local) that evaluates the exact same 7-signal feature vector inunder 1 millisecond.

(Note on benchmark accuracy: The 1 ms timing reported in the deterministic test fixture reflects this local offline heuristic engine. When running against TabPFN's hosted model with credentials, inference takes ~20 ms across the batch. Both modes share the exact same Pydantic triage interface and 100% test pass rate).

### Stage 2: Local Vision & Content Understanding (Gemma 3)

Only files requiring semantic classification (unlabeled PDFs, scanned receipts, documents) are forwarded to localGemma 3viaOllama.

* PDFs are converted to in-memory images via PyMuPDF.
* Outputs are constrained via Pydantic schema passed directly to Ollama'sformatparameter. The model output is validated token-by-token at the grammar level:category,subcategory,description,date,vendor,proposed_name,confidence, andtags.
* If Ollama is offline, a 0.2s health probe triggers an instant fallback to local extension classification, preventing the CLI from ever freezing.

### Safe, Non-Destructive File Operations

The organization pipeline enforces strict safety invariants:

1. Non-Destructive Dry Run:slothd organizeprints the plan without moving files. You must explicitly pass--goor click "Approve" in the dashboard.
2. Collision Avoidance: IfInvoices/AWS_Invoice_2026.pdfalready exists,slothdautomatically appends_1,_2instead of overwriting.
3. Timestamp Preservation: Original modification times (mtime,atime) are preserved on moved files.
4. SQLite WAL Manifest: Every operation logsbatch_id,old_path,new_path, andtimestamp.
5. Instant Rollback: Runningslothd undorestores the entire batch in reverse order.

### Observability: Using Sentry as an Active Debugging Loop

Sentry was not added as a decorative vanity badge; it was an active part of the developer feedback loop during development.

The integration initializes Sentry with releaseslothd@0.1.0and traces critical pipeline boundaries:scanner.scan_directory,ai.classify_batch,organizer.preview,organizer.execute,organizer.undo, andsearch.query.

#### Sentry Distributed Trace Waterfall

[Transaction] slothd.organize_cycle (total: 1,248 ms)
├─ [Span] scanner.scan_directory .................... 12 ms [10 files discovered]
├─ [Span] ai.tabular_triage (TabPFN) ................ 1 ms [2 anomalies flagged]
├─ [Span] ai.gemma_classify_batch (Ollama) .......... 1,180 ms [Prompt: 412 tok, Resp: 86 tok]
├─ [Span] organizer.preview_manifest ................ 3 ms [Manifest prepared]
├─ [Span] db.wal_log_commit ......................... 4 ms [SQLite WAL sync]
└─ [Span] search.index_pgvector (Tiger Data) ........ 48 ms [768-dim embeddings stored]

Enter fullscreen mode

Exit fullscreen mode

#### Authentic Sentry Captured Trace & Issue Evidence

Issue ID
:
 
7805015409

Release
:
 
slothd@0.1.0 (production)

Title: ConnectionError
:
 
Connection refused to 127.0.0.1:11434

Culprit
:
 
slothd.engine.classifier in classify_batch

Trace ID
:
 
71ac0b2ff1dc4c4788ff6a5b7098e354

Span ID: a1ea6839c23ccbb5 (op
:
 
ai.classify_batch, desc
:
 
"
Gemma
 
3
 
batch
 
classify
 
(4
 
files)")

Breadcrumb
:
 
[
warning
]
 
slothd.engine.classifier
:
 
Ollama server is offline or unreachable. Fast-falling back to local classification.

Handled
:
 
Yes (Circuit-breaker tripped gracefully without crashing the daemon)

Enter fullscreen mode

Exit fullscreen mode

Observed Failure in Sentry

Root Cause Revealed

Resolution & Test

ConnectionError
 on 
127.0.0.1:11434
 (Issue #7805015409)

Ollama daemon was offline during CLI execution

Added 200ms pre-flight probe, local heuristic fallback, and circuit-breaker regression test (
3a327ea
).

ValidationError: confidence > 1.0

Gemma 3 occasionally returned confidence as a percentage (
90
 or 
100
) instead of float 
0.0–1.0

Added automatic percentage normalization validator in Pydantic schema with bounds coverage (
a914b53
).

RuntimeError: generator didn't stop after throw()

Tracing context manager was incorrectly re-entering on caught exceptions

Cleaned up tracing wrapper to propagate exceptions correctly and verified with regression tests (
df19f29
).

## Why Does Open Innovation Matter?

Personal files contain our most vulnerable data:

* Tax returns and bank statements
* Medical lab reports and health records
* Invoices and payment receipts
* Confidential code and configuration secrets

Uploading this stream of daily life to closed, centralized cloud APIs creates an unacceptable privacy tradeoff.

Open-weight AI (Gemma 3) and open-source tabular models (TabPFN) fundamentally change this dynamic.They make it possible to run state-of-the-art vision and tabular triage entirely inside the boundary of your own computer:

* No document crosses your local network without explicit opt-in.
* Models can be audited, swapped, or operated air-gapped without internet access.
* Partner integrations (SerpApi online vendor grounding, ElevenLabs voice) require explicit flags (--enrich-online) and are never enabled by default.

Privacy is not a checkbox added after the architecture is done; with open-source AI, privacyisthe architecture.

## The Lazy Payoff

The lazy payoff is not about moving files a few milliseconds faster. It is aboutremoving the cognitive dread of manual digital housekeeping.

Instead of spending Sunday afternoon opening dozens of PDFs one by one, deciphering cryptic filenames, and deciding where each document belongs:

1. You letslothd daemonrun in the background.
2. It detects when you step away from your keyboard.
3. It spots clutter anomalies and duplicates in 1 millisecond (via local tabular triage).
4. It reads invoices and dates with Gemma 3.
5. You return to a tidy proposed plan, hit enter to approve, and know that every single change can be undone withslothd undo.

### Measured Efficiency from the Test Fixture

10 files scanned
2 clutter anomalies identified
1 duplicate set found
973 B reclaimable disk space
1 ms metadata triage (local deterministic 7-signal engine / TabPFN schema)
0 cloud API calls required
100% offline isolation

Enter fullscreen mode

Exit fullscreen mode

## Prize Categories

### Architectural Depth & Ecosystem Evidence

Whileslothdoperates completely offline out of the box, it was engineered with a modular architecture that cleanly interfaces with specialized ecosystem tools. Rather than a superficial checklist of sponsor imports, each partner integration represents an optional, verified subsystem that enhances capability without compromising our local-first core:

### ⏱️ 10-Second Judge Navigation Matrix

Track

How 
slothd
 Uses It

Source Module

Google Gemma

Local 
gemma3:4b
 vision + text via Ollama with strict Pydantic JSON outputs

classifier.py

Prior Labs TabPFN

1ms 7-feature tabular triage flagging stale archives & size outliers before LLM wakeup

tabular_predictor.py

Tiger Data

768-dim 
pgvector
 semantic search (
<=>
) + hybrid keyword re-ranking

tiger_data.py

Sentry Tracing

Distributed spans (
slothd.scan
, 
predict
, 
classify
, 
search
) tracking latency & tokens

sentry_tracing.py

SerpApi

Opt-in 
--enrich-online
 live web grounding for cryptic filenames & unknown vendors

serpapi_client.py

ElevenLabs

slothd briefing
 Sloan-the-Sloth voice summary via 
eleven_multilingual_v2

elevenlabs.py

GitHub Copilot

Cross-OS CI matrix (Ubuntu/Windows, Py 3.11/3.12) + 
.github/copilot-instructions.md

ci.yml

Entire

Full agent session provenance & Git checkpoints via 
.entire/settings.json

.entire/

### 1. 🦥 Grand Prize: Hacktoberfest Week 3 "Slow and Steady"

* Concept:Embodying International Sloth Day with native OS idle measurement (Win32GetLastInputInfo, macOSIOHIDSystem, Linuxxprintidle) that sleeps during work and activates only after 5+ minutes of continuous inactivity. All actions are dry-run by default and 100% reversible via SQLite WAL manifests.

### 2. 💎 Featured Track: Best Use of Gemma

* Module:slothd/engine/classifier.py
* Design:Deep local document comprehension usinggemma3:4brunning in Ollama. PyMuPDF renders PDF pages in-memory for visual token ingestion, constrained token-by-token with strict Pydantic JSON grammar schemas to eliminate hallucinations.

### 3. 📊 Featured Track: Best Use of TabPFN

* Module:slothd/engine/tabular_predictor.py
* Design:Operates as Stage 1 in the prediction agent funnel. Evaluates 7 filesystem numerical distributions in under 1 ms (local heuristic fallback) or ~20 ms (TabPFN model) to flag anomalies and installer clutter before LLM activation. Covered intests/test_tabular_predictor.py.

### 4. 🐯 Partner Track: Best Use of Tiger Data

* Module:slothd/engine/search.py&slothd/integrations/tiger_data.py
* Design:Stores 768-dimensionalnomic-embed-textembeddings in Tiger Data PostgreSQL withpgvectorIVFFlat cosine distance indexing (<=>), backed by an automatic local SQLite vector fallback.

### 5. 🔭 Partner Track: Best Use of Sentry Agent Tracing

* Module:slothd/integrations/sentry_tracing.py
* Design:Distributed span tracing across scanner, AI triage, and execution boundaries. Verified with authentic production traces (Issue #7805015409,trace_id: 71ac0b2ff1dc4c4788ff6a5b7098e354) that resolved three real development regressions (3a327ea,a914b53,df19f29).

### 6. 🔍 Partner Track: Best Use of SerpApi

* Module:slothd/integrations/serpapi_client.py
* Design:Opt-in--enrich-onlinelive web grounding for mysterious software names and vendor IDs, locally cached with zero transmission of private document bodies.

### 7. 🎙️ Partner Track: Best Use of ElevenLabs

* Module:slothd/integrations/elevenlabs.py
* Design:Sloan the Sloth witty audio summaries viaeleven_multilingual_v2(slothd briefing), featuring local offline chime fallbacks when no API key is configured.

### 8. 🤖 Partner Track: Best Use of GitHub Copilot

* Module:.github/copilot-instructions.md,.github/prompts/, andslothd/cli.py
* Design:Authoritative 85-line repository guide, 3 custom prompt templates (/new-sorter,/audit-privacy,/verify-demo), CLI prompt inspector (slothd copilot), and cross-OS CI matrix (.github/workflows/ci.yml).

### 9. 📦 Partner Track: Best Use of Entire

* Module:.entire/settings.json&.agents/hooks.json
* Design:Integrates Entire CLI 0.11.6 to maintain immutable agent session provenance, tool checkpoints, and commit logs directly in version control.

### Verification & Testing

Every test runs in total offline isolation (no live external services required):

uv run pytest 
-v

# 118 passed in 40.87s

uv run ruff check 
.

# All checks passed!

Enter fullscreen mode

Exit fullscreen mode

## 🦥 Parting Sloth Thoughts: Reclaiming Digital Calm

We spend so much time micromanaging our digital clutter—manually dragging files into folders, hunting for lost receipts, or feeling guilty about a desktop covered infinal_v2_really_final.pdf.

slothdwas built on a very simple premise:your machine should quietly work for you when you're resting, not steal your attention when you're busy.

By embracing open-weights, deterministic rule fallbacks, and respectful idle scheduling, you don't have to surrender your personal documents to cloud silos or burn your laptop's battery just to keep a clean workspace. Take a breath, close your laptop lid, and let the sloth do the heavy lifting while you take a break.

### 💬 Community Discussion

I'd love to hear your thoughts and feedback:

1. What is the single oldest or most chaotic file currently buried in your messy folders?
2. What custom classification heuristics or local AI pipelines would you like to see supported next?
3. If you runslothdon your workspace, how many megabytes of duplicate clutter did you reclaim?

Ifslothdbrought a little bit of calm to your daily workflow, consider dropping a ⭐ on theGitHub repository, leaving a comment below, and sharing your experience! Happy Hacktoberfest! 🍂🦥

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse