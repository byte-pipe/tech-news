---
title: Claude's Code
url: https://www.claudescode.dev/?window=since_launch
site_name: hnrss
content_file: hnrss-claudes-code
fetched_at: '2026-03-26T11:23:05.775385'
original_url: https://www.claudescode.dev/?window=since_launch
date: '2026-03-25'
description: Global dashboard tracking the coding activity of Anthropic's Claude Code agent.
tags:
- hackernews
- hnrss
---

## Interesting Observations

A quick read on momentum, adoption, and where the current activity is clustering.

### Growth

+8%
W/W
Acceleration
-17.9pp
Doubling Time
61 days

### Early Adopter Commits

These are the earliest observed public-era Claude Code commits we can verify after launch. Multiple same-day candidates may exist, so this is suggestive rather than definitive.
Feb 24, 2025
Earliest observed launch-day candidates for Claude Code adoption
moinmir/ClashOfCans
Change initial game setup to always have exactly 1 correct can

This improves the starting condition by ensuring players always begin with exactly
one can in the correct position, making the initial game state more consistent.

🤖 Generated with Claude Code
Co-Authored-By: Claude <
[email protected]
>
1
 of 
5
 candidates
Rotates every 
5
s

### New Repos This Week

114,785

Original repos (non-forks) with their first observed Claude Code commit in the last 7 days

### Net Code Delta

+30.7B

Lines added minus lines deleted for the current slice

### Top 3 Languages

0
1
TypeScript
34.8
%
7.25M
 commits
0
2
Python
18.9
%
3.92M
 commits
0
3
JavaScript
10.2
%
2.13M
 commits

### Total Commits

20,807,124

Global activity

### Lines Added

+
50,442,790,274

New code generated

### Lines Deleted

-
19,767,154,942

Refactored code

### Active Repos

1,087,408

Contributing projects

View

### Activity Over Time

### System Activity Log

Since Launch
 · 
All
 · 
Mar 25, 9:12 PM
daf269a
03/25/2026, 19:59:46
03/25, 19:59
standardbeagle/agnt
claim: Mdkq6bztAPFj by beagle-ab2-1591895

Co-Authored-By: Claude Opus 4.6 (1M context) <
[email protected]
>
1dddc15
03/25/2026, 19:59:25
03/25, 19:59
bencrane/data-engine-x-api
docs: update all documentation to reflect completed Global Entity Model project

Co-Authored-By: Claude Opus 4.6 <
[email protected]
>
998df97
03/25/2026, 19:58:57
03/25, 19:58
it-mannetje/hogenes
Auth: magic link login, allowed_admins whitelist, server-side RLS
c4039a2
03/25/2026, 19:58:56
03/25, 19:58
it-mannetje/hogenes
Auth: magic link login, allowed_admins whitelist, server-side RLS
106a6e8
03/25/2026, 19:58:55
03/25, 19:58
it-mannetje/hogenes
Auth: magic link login, allowed_admins whitelist, server-side RLS
cc0e4e6
03/25/2026, 19:58:35
03/25, 19:58
zseramnay/Formants
9 principes orchestration, doublures par registre, commentaires registre 16 instruments, encadré profil vs carte
3768903
03/25/2026, 19:57:01
03/25, 19:57
thefiredev-cloud/Protocol-Guide
fix: enable adaptive threshold + add 22 bridge chunks for top failure protocols

- Enable adaptive threshold retry for ALL agency searches (not just high-accuracy)
- Add dense bridge chunks for top 20 failing protocols covering ~130 test failures
- Protocols: 1203 1209 1210 1211 1212 1213 1215 1216 1219 1220 1222 1223 1225 1229 1232 1237 1241 1244 1302 510 518 519
2264181
03/25/2026, 19:56:39
03/25, 19:56
gvinsot/PulsarTeam
feat: add project statistics with charts (bugs created vs resolved, resolution time evolution)

- Backend: add getTimeSeries() to globalTaskStore for day-by-day created/resolved
 counts, resolution time evolution, and open tickets over time
- Backend: add GET /api/agents/tasks/stats/timeseries?project=X&days=N endpoint
- Frontend: new ProjectStats component with Chart.js graphs (created vs resolved
 bar chart, resolution time line chart, open tickets area chart, state durations)
- Frontend: integrate ProjectStats into ProjectsView - clicking any project card
 opens the statistics panel with all charts
- Frontend: add getProjectTaskStats and getProjectTimeSeries API methods

(by CLAUDIO)
8fbe3ab
03/25/2026, 19:56:16
03/25, 19:56
ydesjardins200-coder/wavesfinancial
fix: remove stray closing div breaking Support mega menu on apply page
e2082f9
03/25/2026, 19:56:09
03/25, 19:56
kuzmich89/AI-broker
Use NHTSA instead of AutoAstat for VIN data loading in CarCaseDetail

Replace the removed fetchAutoAstat button with a new 'Завантажити з NHTSA'
button that calls vinApi.decode(vin) and updates the case fields directly.
Shows warning toast when mock data is returned (VIN not in NHTSA DB).

https://claude.ai/code/session_01XNhJmFU2Jzmc5B1FZTwGWK
950ddb4
03/25/2026, 19:55:54
03/25, 19:55
Dicklesworthstone/frankenscipy
feat(all): add DBSCAN clustering, FFT plan caching, RBF/Akima interpolation, BFGS optimizer, and expand constants/special/stats

Cluster (+126 lines): DBSCAN density-based clustering with configurable eps
and min_samples, returning cluster labels with -1 for noise points.

Constants (+108 lines): Comprehensive physical constants module (speed of
light, Planck, Boltzmann, Avogadro, electron mass, proton mass, elementary
charge, gravitational constant, etc.) matching scipy.constants surface.

FFT (+94 lines): Plan caching for repeated FFT sizes, reducing planning
overhead for iterative algorithms. Adds real-to-complex (rfft/irfft)
optimized paths.

Interpolate (+216 lines): RBF (radial basis function) interpolation with
multiquadric/inverse_multiquadric/gaussian/linear/cubic kernels. Akima
interpolation (subspline with reduced overshoot). RegularGridInterpolator
for N-dimensional interpolation on regular grids.

Linalg (+32/-32): Refactors matrix operation signatures for consistency,
replacing ad-hoc parameter ordering with standardized (matrix, n, ...) form.

Ndimage (+8/-8): Minor cleanup of filter axis validation messages.

Optimize (+128 lines): BFGS quasi-Newton optimizer with Wolfe line search,
inverse Hessian approximation, and gradient convergence detection.

Signal (+12/-12): Consistency fixes for window function parameter validation.

Special: Simplifies Airy function implementation (+48/-48), fixes
convenience function parameter passing, updates re-exports.

Stats (+6/-6): Minor fixes to distribution parameter edge cases.

Integrate (+4/-4): Quadrature tolerance consistency fixes.

Co-Authored-By: Claude Opus 4.6 (1M context) <
[email protected]
>
db513f6
03/25/2026, 19:55:50
03/25, 19:55
prompted365/context-grapple-gun
Update CogPR-57 doctrine: mark all three defects as fixed (tic 108)
354f8ab
03/25/2026, 19:55:15
03/25, 19:55
prompted365/context-grapple-gun
CogPR-57 mandate lifecycle fix: race guard, concurrency guard, reconcile-first

Three structural defect fixes (authorized at tic 107 review, not tech debt):

1. cgg-gate.sh: Re-validate mandate status before inline lightweight
 consumption — prevents double-consumption race with mogul-runner

2. review SKILL.md: Concurrency guard at steps 5.5 and 8.5 — check
 current.json status before writing mandates or spawning Mogul.
 Running/pending mandates are not overwritten.

3. session-restore.sh: Reconcile-first cycle computation — read previous
 mandate tic_context as primary schedule source, modulo as fallback
 only when no previous context exists. Estate snapshot can add cycles
 but not replace schedule. Eliminates recomputation drift.

Runtime parity: both hooks synced to ~/.claude/hooks/ and verified.
c925517
03/25/2026, 19:54:05
03/25, 19:54
kuzmich89/AI-broker
Disable AutoAstat button in CarCaseDetail

Remove the 'Завантажити дані' button that called fetch-autoastat
from the case detail page. AutoAstat is not used for now.

https://claude.ai/code/session_01XNhJmFU2Jzmc5B1FZTwGWK
e9ac56f
03/25/2026, 19:53:47
03/25, 19:53
ydesjardins200-coder/wavesfinancial
feat: rebuild apply funnel for conversion — repayment preview, decline screen, cleaner UX
6992f89
03/25/2026, 19:53:20
03/25, 19:53
A13XMC11/lanlabs-agente
feat: add Redis-backed multi-message buffering with whatsapp-agentkit skill

- New agent/buffer.py: Manages message buffering with Redis
 - Groups multiple messages into coherent context
 - Configurable timeout (default 2.5s)
 - Automatic deduplication (webhook retries)
 - Backpressure handling (max 15 messages/buffer)
 - Age-based topic separation (5 min max)
 - Structured JSON logging

- Updated agent/main.py:
 - Integrates buffer_manager in webhook handler
 - Single unified response instead of per-message
 - Connects to Redis on startup
 - Graceful degradation if Redis unavailable
 - Improved structured logging

- Dependencies: Added redis + python-json-logger
- Config: New REDIS_URL, BUFFER_TIMEOUT_MS, MAX_BUFFER_AGE_MS env vars

Implements whatsapp-agentkit skill (RED-GREEN-REFACTOR tested)
cc1f00c
03/25/2026, 19:53:12
03/25, 19:53
james-axis/project-origin
fix: Correct untitledui icon imports - MapPin01→MarkerPin01, Search→SearchLg, RefreshCw→RefreshCw01, FileText01→File01
8188fd5
03/25/2026, 19:51:42
03/25, 19:51
it-mannetje/hogenes
Stamboek: generation management, person editing, collapsible SVG tree, lightbox, photo management
3e68087
03/25/2026, 19:51:41
03/25, 19:51
it-mannetje/hogenes
Stamboek: generation management, person editing, collapsible SVG tree, lightbox, photo management
3d21ba9
03/25/2026, 19:51:40
03/25, 19:51
it-mannetje/hogenes
Stamboek: generation management, person editing, collapsible SVG tree, lightbox, photo management
c9a9916
03/25/2026, 19:51:40
03/25, 19:51
it-mannetje/hogenes
Stamboek: generation management, person editing, collapsible SVG tree, lightbox, photo management
8553e24
03/25/2026, 19:51:39
03/25, 19:51
it-mannetje/hogenes
Stamboek: generation management, person editing, collapsible SVG tree, lightbox, photo management
f7890b2
03/25/2026, 19:51:14
03/25, 19:51
kuzmich89/AI-broker
Fix NHTSA VIN loading and add Consignor/Transport/PreviousDocs sections

- Add dedicated GET /api/vin/decode/{vin} endpoint that calls NHTSA
 directly without requiring case creation first, eliminating the
 two-step create-then-fetch flow that caused the loading error
- Update NewCarCase.tsx: use vinApi.decode() for VIN lookup (cleaner,
 more specific error messages, shows brand/model/year on success)
- Add Consignor section: sender name, country, address, EORI number
- Add Transport section: type (sea/road/rail/air), vessel/vehicle ID,
 flag country, crossing point, expected date, document type & number
- Add PreviousDocs (Graph 44) section: dynamic list of previous customs
 documents (T1/T2/TIR/EUR-1/CMR/MRN) with type, number, date, issuer
- Add backend model fields + migration 014 for all new columns
- Update CarCaseCreate/Update/Response schemas with new fields
- Add vinApi to frontend api.ts and new fields to types/index.ts

https://claude.ai/code/session_01XNhJmFU2Jzmc5B1FZTwGWK
74220f1
03/25/2026, 19:50:41
03/25, 19:50
thefiredev-cloud/Protocol-Guide
fix: prevent CDN caching of empty search results

Empty results were getting cached at CDN (Fastly) for 1 hour via
Cache-Control: public, max-age=3600. After deploying threshold/dictionary
fixes, old NO RESULTS responses kept being served from CDN cache.

Now: empty results get Cache-Control: no-store
e0aa36a
03/25/2026, 19:50:04
03/25, 19:50
ZhimingMei/finance-paper-reader-skill
Add README.md for repo and quick reference header to SKILL.md
61ac809
03/25/2026, 19:48:45
03/25, 19:48
Endymion1236/centre-equestre-agon
fix: forfait annuel ne crée plus de payment doublon + badge impayés corrigé

Bug — Forfait 1x crée un payment doublon :
Avant : l'inscription forfait créait les échéances (payments)
PUIS onEnroll créait un DEUXIÈME payment pour le même créneau
→ 2x 'galop d'or' à 25€ dans les impayés = 50€ parasite
Après : onEnroll est appelé avec skipPayment:true pour les
forfaits annuels → seules les échéances sont créées.

Badge Impayés — exclut les échéances :
Avant : le badge rouge affichait 11 (10 échéances + 1 commande)
Après : le badge n'affiche que les commandes normales
(les échéances ont leur propre onglet)

Build compilé OK.
651a5b8
03/25/2026, 19:48:22
03/25, 19:48
ayeshakhalid192007-dev/humanoid-ai-studio
fix(backend): add Dockerfile with python:3.11-slim to reduce image size

Replaces Nixpacks build (5.7GB) with explicit Dockerfile using slim base
image + CPU-only PyTorch to stay under Railway's 4GB trial limit.

Co-Authored-By: Claude Sonnet 4.6 <
[email protected]
>
7dfe428
03/25/2026, 19:47:37
03/25, 19:47
ZhimingMei/finance-paper-reader-skill
Initial commit: finance-paper-reader skill
02fec57
03/25/2026, 19:44:56
03/25, 19:44
EmpoweredVote/Civic-Trivia-Championships
fix: add missing New York State and Queens NY locale config files

These were registered in generate-locale-questions.ts in a prior commit
but the actual config files were never staged, causing TS2307 module
not found errors on Render.

Co-Authored-By: Claude Sonnet 4.6 <
[email protected]
>
78f9c0e
03/25/2026, 19:43:04
03/25, 19:43
thefiredev-cloud/Protocol-Guide
fix: lower similarity and quality thresholds for better recall

254/506 failures were all NO RESULTS (zero wrong-protocol).
Precision is solid — recall is the bottleneck.
- similarity thresholds: 0.58-0.63 → 0.45-0.50
- quality minimumThreshold: 0.50 → 0.35
- quality warnThreshold: 0.60 → 0.50
- minQualityResults: 2 → 1
2b6a996
03/25/2026, 19:41:12
03/25, 19:41
EmpoweredVote/Civic-Trivia-Championships
fix: replace smart apostrophes in PA/Philly collection descriptions

Curly quotes in single-quoted TypeScript strings caused unterminated
string literal errors in the build introduced by the Pennsylvania
collections commit.

Co-Authored-By: Claude Sonnet 4.6 <
[email protected]
>
655cf36
03/25/2026, 19:40:05
03/25, 19:40
grimmolf/grimm-workshop
Add blog post: We're measuring productivity wrong

Capacity vs throughput framework for employee value and AI deployment.
Includes Red Hat TAM program and Open Organization as case study.
b9afde8
03/25/2026, 19:39:29
03/25, 19:39
james-axis/project-origin
fix: Fix Softphone NodeJS.Timeout type issue
044ac5a
03/25/2026, 19:38:41
03/25, 19:38
mdegans/agora-agents
agents: Add moderator agents, reassign lfm2, expand communities

- Add 5 hand-crafted moderator agents (sentinel-mod, arbiter-mod,
 watchdog-mod, guardian-mod, inquisitor-mod) across cogito:14b and
 gpt-oss:20b for moderation pipeline testing
- Reassign 111 lfm2:24b agents to working models (gpt-oss, cogito,
 gemma3, mistral-small, gemma3n) — lfm2 had near-total parse failure
- Expand epidemius to 9 communities for broader moderation testing
- Add community memberships for ~92 agents across 24 new communities
- Include natural soul mutations from seed run (31 mutations at 3% rate)
- Include 2 forced epidemius mutations from think:false testing

Co-Authored-By: Claude Opus 4.6 (1M context) <
[email protected]
>
404a5e3
03/25/2026, 19:38:27
03/25, 19:38
mdegans/agora-agents
server: Add mutation-chance, agent-filter flags; fix thinking models; log Ollama stats

- Add --mutation-chance CLI flag to override deep mutation probability (0-100)
- Add --agent-filter CLI flag to run a subset of agents by name
- Disable thinking mode (think: false) in Ollama requests to prevent
 reasoning models from refusing soul mutations
- Log Ollama inference stats (prompt tokens, eval tokens, tok/s) with
 WARN threshold at 32k tokens for KV cache swap detection
- Improve mutation failure logging (warn level with response preview)
- Update system prompt: prefer comments over posts, list valid community
 slugs, add new communities

Co-Authored-By: Claude Opus 4.6 (1M context) <
[email protected]
>
68bc326
03/25/2026, 19:38:22
03/25, 19:38
james-axis/project-origin
fix: Add practice_id support to call-flows routes
b0230a3
03/25/2026, 19:37:48
03/25, 19:37
james-axis/project-origin
feat: Add Phone System wizard with Twilio subaccount management

- Add Stage 0: Practice/Adviser subaccount management routes
- Each practice gets its own Twilio subaccount for isolated billing
- Add 6-step setup wizard: Practice → Address → Compliance → Voice → Number → Routing
- Full AU regulatory compliance flow (address, bundle, approval)
- TwiML App creation per practice
- Phone number search and purchase
- Call flow/IVR configuration
- Updated schema with twilio_practices and twilio_twiml_apps tables
- Comprehensive frontend wizard UI with stepper
- Real-time API integration with backend
792fccb
03/25/2026, 19:37:40
03/25, 19:37
snobol4ever/.github
Planning session 3 archive — Icon gap analysis, GMR scoped
340d1c0
03/25/2026, 19:36:53
03/25, 19:36
michalbaturko-lang/webflip
fix(i18n): translate Czech strings in CoreWebVitals component

Co-Authored-By: Claude Opus 4.6 <
[email protected]
>
94028ee
03/25/2026, 19:36:19
03/25, 19:36
thefiredev-cloud/Protocol-Guide
fix: regenerate pnpm-lock.yaml for Railway deploy
f7d46c8
03/25/2026, 19:36:06
03/25, 19:36
ydesjardins200-coder/wavesfinancial
Replace nav with mega menu across all 19 pages — Products / Company / Support dropdowns, mobile drawer, hover+click, keyboard accessible
dceecbc
03/25/2026, 19:35:46
03/25, 19:35
ErikEvenson/galaxy
feat: ZEM/ZEV powered descent guidance — deorbit→ZEM/ZEV flow (#981)

Architecture: plane_change → coast_to_deorbit → deorbit → powered_descent
The deorbit burn puts the ship on a suborbital trajectory, then ZEM/ZEV
guidance handles the powered descent to the pad.

Changes:
- zemzev_guidance_math.py: correct formula (no double-counting gravity)
- zemzev_guidance.py: tick handler with safety override
- maneuver_landing.py: deorbit transitions to powered_descent for targeted
 landings; coast transitions restored to deorbit phase
- Harness: place_ship_above_target positions at 10km with 50 m/s descent

Test results (117 total):
- 115 passed, 2 failed (Io precision — harness propagation issue)
- Luna precision at 10m: PASSES
- All existing landing/unit tests: PASS (no regression)
- 19 ZEM/ZEV math unit tests: PASS

Remaining: Io precision tests need investigation — the harness Keplerian
body propagation (Io around Jupiter at 17 km/s) introduces drift that
doesn't exist in the real N-body game. The ZEM/ZEV guidance itself is
correct; the test harness needs better Io frame handling.

Co-Authored-By: Claude Opus 4.6 (1M context) <
[email protected]
>
06ea6bf
03/25/2026, 19:34:13
03/25, 19:34
joshdataresources/climate-studio
Update globals.css
5e79a8f
03/25/2026, 19:33:47
03/25, 19:33
prompted365/context-grapple-gun
Tic 107 review: promote CogPR-73/74/76/77/78 to CGG CLAUDE.md

- CogPR-73: Governance label accuracy (observer-first → governed-at-boundaries)
- CogPR-74: Arena velocity guard (convergence faster than evidence)
- CogPR-76: Same-model convergence discount
- CogPR-77: Concession cascade detection
- CogPR-78: showClearContextOnPlanAccept must be true (cadence handoff chain)
5cfcc94
03/25/2026, 19:32:29
03/25, 19:32
mearley24/AI-Server
expand: monitor top 25 wallets instead of 10
83e3907
03/25/2026, 19:32:28
03/25, 19:32
ayeshakhalid192007-dev/humanoid-ai-studio
fix(ci): remove deploy hook step — Railway deploys via GitHub integration

Railway's 'Wait for CI' toggle handles deployment automatically after
CI passes. No deploy hook or token needed. Workflows now only run
tests/audit as the CI gate Railway watches.

Co-Authored-By: Claude Sonnet 4.6 <
[email protected]
>
1fc1100
03/25/2026, 19:29:18
03/25, 19:29
ydesjardins200-coder/wavesfinancial
Add privacy-policy.html — 11 sections, sticky TOC, plain-language summaries, data chips, third-party table, cookie grid, rights grid + update footer links across all pages
a3a4123
03/25/2026, 19:28:17
03/25, 19:28
u2giants/mission-control
feat: initial scaffold — full Mission Control platform

- Dockerfile, docker-compose, nginx, entrypoint, configure
- Express API: missions, tasks, agents, logs (SSE), config routes
- SQLite schema with WAL mode
- Agent soul file management
- Model registry (shared format with gateway, 9 models)
- Multi-provider worker engine (Google/Anthropic/OpenAI unified adapter)
- Worker pool with 2s polling, dependency-aware task assignment
- Tool implementations: bash, http, file r/w, git, coolify, cloudflare, spawn_subtask
- React UI: Dashboard, Missions kanban, Task detail with live SSE logs, Agents, Settings
- Settings page includes model registry editor with inline editing + Push to Gateway
- Smoke tested: healthz OK, Agent Alpha seeded, 9 models loaded

Co-Authored-By: Claude Sonnet 4.6 <
[email protected]
>
c0af101
03/25/2026, 19:27:15
03/25, 19:27
gvinsot/PulsarTeam
fix: allow manual task column/step changes by skipping on_enter workflow transitions

When a user manually drags or changes a task's status, on_enter workflow
transitions were firing immediately (e.g. change_status actions), reverting
the move before the frontend could refresh. Now _checkAutoRefine receives
the `by` parameter and skips on_enter transitions when by='user'.

- Auto-assign by column role still works for manual moves
- Condition-based transitions still evaluated by periodic checker
- Workflow-initiated changes (agents, jira-sync) still trigger on_enter
- Added error handling in frontend handleDrop and handleStatusChange

Co-Authored-By: Claude Opus 4.6 <
[email protected]
>
f92e28a
03/25/2026, 19:26:27
03/25, 19:26
ayeshakhalid192007-dev/humanoid-ai-studio
fix(backend): install CPU-only PyTorch to reduce Railway image size

CUDA PyTorch is ~1.5GB causing Railway image push to fail.
CPU-only build is ~200MB, well within trial account limits.
sentence-transformers only needs CPU inference for embeddings.

Co-Authored-By: Claude Sonnet 4.6 <
[email protected]
>

### Top Repositories

Since Launch·All· ranked bycommits

Commits
Added
Deleted

### Languages

Code distribution

Showing total commits by language