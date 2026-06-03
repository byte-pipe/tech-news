---
title: 'GitHub - HKUDS/Vibe-Trading: "Vibe-Trading: Your Personal Trading Agent" · GitHub'
url: https://github.com/HKUDS/Vibe-Trading
site_name: github
content_file: github-github-hkudsvibe-trading-vibe-trading-your-persona
fetched_at: '2026-06-03T20:09:04.381819'
original_url: https://github.com/HKUDS/Vibe-Trading
author: HKUDS
description: '"Vibe-Trading: Your Personal Trading Agent". Contribute to HKUDS/Vibe-Trading development by creating an account on GitHub.'
---

HKUDS

 

/

Vibe-Trading

Public

* NotificationsYou must be signed in to change notification settings
* Fork2k
* Star9.8k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

244 Commits
244 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
agent
agent
 
 
assets
assets
 
 
frontend
frontend
 
 
scripts
scripts
 
 
tools
tools
 
 
wiki
wiki
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
README_ar.md
README_ar.md
 
 
README_ja.md
README_ja.md
 
 
README_ko.md
README_ko.md
 
 
README_zh.md
README_zh.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

English|中文|日本語|한국어|العربية

# Vibe-Trading: Your Personal Trading Agent

One Command to Empower Your Agent with Comprehensive Trading Capabilities

Website·Docs·News·Features·Shadow Account·Demo·Quick Start·Examples·API / MCP·Roadmap·Contributing

## 📰 News

* 2026-06-03🧹Community triage + trace correlation: Tool-call trace entries now carry the originatingcall_id, so atool_resultcan be matched back to itstool_callwhen replaying a run trace — arg previews stay truncated to keep trace files small (#168, thanks @zwrong). Source comments no longer point at an internal-only docs path that external contributors couldn't find (#166, thanks @jaleelpersonal). Also clarified that thelangchain-communityresolver warning on install is a harmless leftover-package notice, not a failure (#167), and scoped Gemini 2.5/3.0thoughtSignatureround-tripping for function calls as ahelp wantedtask with a full fix plan (#170, thanks @jliu6789).
* 2026-06-02🔌Six new broker connectors (Tiger / Longbridge / Alpaca / OKX / Binance / Futu): The connector-first trading layer gains a direct-SDK transport alongside IBKR (local) and Robinhood (MCP). Each connector exposes read-only account / positions / orders / quote / historyplus paper-account order placement— test your strategies across these broker paper accounts. Five of them (Tiger, Alpaca, OKX, Binance, Futu) also supportbounded, mandate-gated order placementbehind the same safety model as Robinhood: a user-committed mandate (symbol universe / order size / exposure / leverage / daily cap), a filesystem kill switch, a fail-closed pre-trade gate, and a full audit ledger.Longbridge is paper + read-only only(its API exposes no runtime paper/live discriminator). Every paper/live distinction is a structural per-broker guard — account-id format, host separation, demo flag, or trade environment. Newtrading_place_order/trading_cancel_ordertools; HK and A-share asset classes added to the mandate universe. Experimental / use at your own risk.
* 2026-06-01🚀v0.1.9 released(pip install -U vibe-trading-ai): Rolls up everything since 0.1.8. Connector-first broker profiles (IBKR local read-only TWS / IB Gateway + Robinhood Agentic Trading behind OAuth, a committed mandate, order guard, audit ledger, and instant halt). Research Goal runtime across CLI / REST / MCP / Web. A swarm pass — live reconcile + MCP keepalive, operator-configured worker MCP tools, a strict alpha-bench random control, and a newretry_runto relaunch failed/stale runs (36 MCP toolsnow). Theagent/cli/package refactor with a refreshed terminal UI, themootdxno-token A-share loader, and a robustness pass across backtest / agent loop / sessions.--versionnow always matches the installed package, fixing the 0.1.8 drift (#156).

Earlier news

* 2026-05-31🔌Connector-first broker architecture (IBKR + Robinhood): Trading access now starts from a selectable connector profile instead of separate broker/live entry points.vibe-trading connector list/use/check/account/positions/orders/quote/historyand the MCPtrading_*tools share the same selected profile, where paper/live is an attribute of the connector. IBKR can be used immediately through a local read-only TWS / IB Gateway profile, while the official IBKR remote MCP path is seeded as an OAuthmcp.readprobe until stable read tool names are available. Robinhood Agentic Trading remains the bounded live MCP connector behind OAuth, a committed mandate, order guard, audit ledger, and instant halt.
* 2026-05-30🧰Robustness pass — backtest, agent loop, sessions: LLM-generated signal engines now pass pre-flight interface validation before instantiation, catching circular self-imports, a missinggenerate(), non-defaulted__init__args, and wrong return types with actionable JSON errors instead of raw tracebacks (#149); a follow-up routes source-level AST validation errors through the same clean JSON envelope. The agent loop no longer burns all 50 iterations into afailedstatus with no output — it mirrors the swarm worker's wrap-up nudge at 80% of the iteration budget and drops tool definitions on the last iteration to force a final text answer (#148), guarded to fire only mid-run so it never displaces research-goal context. Session message writes nowflush + fsynceach append so expensive AI responses survive a mid-write crash, and the read path skips corrupted JSONL lines (logging the first 200 chars for recovery) instead of 500-ing the whole/messagesendpoint (#147). The Web composer also fixes IME Enter handling so a composition-confirming Enter no longer submits mid-word (#146).
* 2026-05-29🔐Robinhood Agentic Trading support (opt-in, bounded autonomy): Adds support for Robinhood Agentic Trading (remote MCP, OAuth). Off and read-only by default; the agent acts only inside a user-committed mandate (symbols / order size / exposure / leverage / daily cap), with a filesystem-level instant kill switch, preemptive flatten, mandate auto-expiry, a full audit ledger, and a persistent autonomous runner. No custody, no venue — the broker holds funds and executes; we only relay intent. Experimental / use at your own risk.
* 2026-05-28🧪Swarm safety + strict alpha gate + worker MCP: Swarm DAG blocks downstream tasks when upstream fails (#145). Newrun_bench_strict()adds a same-universe random control + OOS split to catch factors that just track market beta (#143, thanks @Soli22de). Swarm workers can call operator-configured external MCP servers, with trust boundary pinned (#142, thanks @shadowinlife).
* 2026-05-27📊mootdx A-share data source + output polish: Newmootdxloader speaks the native 通达信 TCP protocol for A-share OHLCV (no auth, no IP rate-limit, daily + intraday with 25-page walk-back pagination), slotting between tushare and akshare in the fallback chain (#107). CCXT loader now readsHTTP_PROXY/HTTPS_PROXY/ALL_PROXYso Binance/OKX public data works from restricted networks (#126, thanks @ruok808). Final-answer rendering also dropped the ugly full-width---horizontal separators on CLI and Web: the system prompt now nudges the agent toward markdown tables and##headings, the CLI renderer strips standalone HRs as defense-in-depth, and the chat bubble hides any<hr>that slips through (#139, thanks @sdwxm188).
* 2026-05-26✅Research Goal lifecycle closure: Goal mode now behaves like a real task runner: Web UI goal creation creates or binds the session and immediately sends the kickoff turn; active goals can be continued, edited, cancelled, and completed across Web/API/CLI/MCP; and the agent advances from the current goal snapshot (criteria, evidence, claims, open items) instead of only the original prompt. Covered-but-still-active goals now enter an audit/status update instead of stopping silently, with regression coverage across backend, CLI, MCP, and frontend events.
* 2026-05-25🧼Cleaner chat UI + composer workflow: The Web UI keeps chat focused on the next action: upload, swarm, and research-goal modes now live behind the composer+menu instead of floating panels. Active context appears above the input as compact chips, and goal details expand inline only when needed. The UI also drops the old custom i18n layer in favor of direct English copy, gates Full Report cards to report-worthy runs, and hardens local dev startup/status reporting for reliable browser smoke tests.
* 2026-05-24🎯Research Goal runtime: Added a session-scoped Research Goal layer across backend, CLI, API/MCP, SSE, and Web UI. Goals persist claims, acceptance criteria, evidence rows, budgets, and completion policy; agent tools can create goals and attach evidence;/goalgives the CLI a direct entry point; REST/MCP expose goal snapshots and evidence writes; SSE keeps chat clients fresh. Follow-up audit fixes locked down verified evidence, blocked live-trading risk tiers through agent tools, wired CLI-created goals into later turns, cleaned goal ledgers on session deletion, enabled replay-all, and fixed cross-session frontend races.
* 2026-05-23🖥️Interactive CLI refresh: The terminal front door now opens with a larger Vibe-Trading banner, a cleaner prompt divider, prior-turn recap, post-run timing, and a Claude Code-style activity rail for live agent work. Tool calls, web/data fetches, shell-style actions, Markdown answers, and pipe tables render in a more readable transcript, while piped or non-TTY runs keep plain-text output for automation. Generated CLI screenshots are now treated as local artifacts instead of committed docs files, keeping the repository lighter.
* 2026-05-22🧭Swarm recovery + MCP keepalive: Swarm status now reconciles from live task files on every read, so API/MCP/SSE/list views recover crashed or stale runs instead of showing permanentrunningsnapshots.run_swarmsends MCP progress heartbeats while it polls, with a fixed first frame ofswarm_started run_id=<id>for clients that reconnect after transport drops; workers now heartbeat through LLM streaming, grounding fetches, and tool execution. The stale-run reaper uses per-run thresholds and derives terminal status from task states,SwarmToolno longer cancels a still-running team just because its wait budget elapsed, and MCP clients can callreap_stale_runs()for explicit cleanup. Today's DX pass also refreshed provider default models and aligned CI syntax checks with the newagent/cli/package. 22 new regressions cover hydration, terminal recovery, stale reaping, keepalive cadence, env parsing, and heartbeat wiring; the full swarm/MCP suite is at 169 passed, 4 skipped.
* 2026-05-21🧱CLI package refactor:agent/cli.py(3216 LOC) split into theagent/cli/package — interactive front door, slash router, Rich components, plus a_legacy.pyshim that preserves every subcommand and re-exports every public symbol socli.cmd_*/cli._INIT_ENV_PATH/cli.Confirmkeep working. New FastAPI middleware serves the SPA shell when a browser opens/runs/{id}or/correlationdirectly; same narrowing landed in the Vite dev proxy. Version unified viacli/_version.py(no more drift between--versionand the banner),python -m clirestored via__main__.py, and the chat-gate narrowed sochat --help/chat extrareach legacy argparse instead of being swallowed by the REPL.
* 2026-05-20🔬Hypothesis Registry CLI: Closes the CLI side of the Hypothesis Registry shipped backend-only on 2026-05-16.vibe-trading hypothesis listprints a Rich table or JSON (--statusfilter,--limit);show <id>renders a detail panel including linked run cards;invalidate <id> --note "..."flips status torejectedwhile preserving prior invalidation notes when--noteis omitted. Honors the existingVIBE_TRADING_HYPOTHESES_PATHenv override and adds a per-invocation--path. 22 new tests cover wiring, JSON output, status filter, limit, missing-id errors, and note persistence.
* 2026-05-19✨Live tool feedback + graceful cancel: Long-running tools (backtests, large PDFs, swarm workers) no longer look frozen. Each tool call now emits a 3-second heartbeat plus structured per-stage progress —run_backtestshows phase markers (validate/simulate/finalize),read_documentticks per page on PDF or per sheet on Excel,read_urlmarksfetch/parse. The CLI Rich Live dashboard renders a Unicode spinner, ASCII progress bar, ETA, and stacks up to 3 parallel tools keyed by name; the frontend chat ships a newToolProgressIndicatorwith rAF-coalesced renders, ARIArole="status"+ hidden native<progress>for screen readers, and a determinateProgressRingSVG when total is known. FirstCtrl+Cduring a CLI run now callsagent.cancel()for graceful exit (current step finishes, trace closes cleanly); a second within 2s force-quits. Reusable primitives extracted along the way:ProgressBar.tsxandlib/tools.ts(shared tool-name i18n).
* 2026-05-18🧹Cleanup pass + three latent bug fixes:CompositeEngineno longer misroutes bare Chinese-futures codes likeRB2410toGlobalFuturesEngine—_is_china_futuresmoved into a shared_market_hooksmodule with a case-normalized product table and a non-CN exchange guard, plus 9 new regression cases. Session FTS5 indexes now persist timestamps so cross-session search can sort by date; the same path also fixed a re-upsert that was wall-clocking every session'sstarted_at. The Vite dev-mode proxy gained the missing/alphaentry so the AlphaZoo page resolves onnpm run dev.tests/test_e2e_harness_v2.py(real-LLM e2e suite) is now gated behindVIBE_TRADING_RUN_LIVE_E2E=1so CI no longer changes shape based on env-key presence. Ruffper-file-ignoresadded for the factor zoo (3783 → 0 F401 noise), frontend tsconfig enablesnoUnusedLocals/noUnusedParametersas regression guards, and 76 unusedvw = vwap(...)boilerplate lines were dropped fromgtja191alphas. Net-918 LOC.
* 2026-05-17🧬Alpha Zoo v1 (0.1.8): 452 pre-built quant alphas across 4 zoos —qlib158(Microsoft Qlib, Apache-2 attribution),alpha101(Kakushadze 101 Formulaic Alphas, paper rewrite from arXiv:1601.00991),gtja191(Guotai Junan 2014 short-horizon factor report), andacademic(Fama-French 5 + Carhart price-based proxies). One-line CLI to bench any zoo on your universe:vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025. Ships with AST purity gate, lookahead-guard test,pytest-socketnetwork kill-switch, per-zoo LICENSE.md, and a Developer Certificate of Origin (DCO) workflow for community PRs. Auto-rendered Alpha Library atvibetrading.wiki/alpha-library/+ research-lab postWhich of the 191 GTJA alphas still work in 2026?.
* 2026-05-16🧪Research spine update: Added a backend Hypothesis Registry withcreate_hypothesis,update_hypothesis,link_backtest, andsearch_hypotheses; external-content readers now attach warning-onlysecurity_warnings; and Shadow Account scanning now uses deterministic OHLCV feature evaluation instead of the old calendar-phase stub.
* 2026-05-15🪪 The run detail page now surfaces the Trust Layer run card alongside metrics and artifacts, completing the UI side of therun_card.jsonwork landed on 2026-05-12.PersistentMemory.add()was also hardened on length, empty/whitespace-only names, and C0/C1 control bytes from the #108/#109/#110 triage (#112, thanks @Teerapat-Vatpitak).
* 2026-05-14🌐 the public wiki is now live atvibetrading.wikiwith docs, tutorials, Research Lab, and Alpha Library sections deployed through Cloudflare Pages. Persistent memory is also inspectable from the CLI viavibe-trading memory list/show/search/forget(#102, thanks @Teerapat-Vatpitak), and memory tokenization/slugs now support Thai, Arabic, Hebrew, and Cyrillic text (#104).
* 2026-05-13🧭 Swarm runs now ground workers with fetched market data and cleaner persisted reports (#93,#84).
* 2026-05-12🧾 Backtests now emitrun_card.jsonandrun_card.mdalongside artifacts for reproducible research runs.
* 2026-05-11🧭Memory slugs, swarm accounting, and CLI preflight: Persistent memory now preserves CJK characters when generating file slugs, preventing silent filename collisions for Chinese/Japanese/Korean notes (#95, thanks @voidborne-d). Swarm run totals now prefer provider-reported token usage with the existing estimate fallback (#94, thanks @Teerapat-Vatpitak), and the CLI run UI gained a startup preflight check for common environment issues (#96, thanks @ykykj).
* 2026-05-10🧱Regression guardrails + run metadata: Memory recall now treats underscores as token boundaries, so snake_case saved memories such asmcp_wiring_testmatch natural-language queries like "mcp wiring" (#87, thanks @hp083625). The MCP server has a subprocess smoke test covering initialize →tools/list→tools/callto guard the first-call deadlock path (#86), while low-risk hardening landed for Windows path-sensitive tests, API best-effort exception handling, backtestrun_dirallowed-root validation, and SwarmRun provider/model metadata (#88,#90,#91,#92, thanks @Teerapat-Vatpitak).
* 2026-05-09🛡️API path hardening + MCP server stability: API run/session routes now validate path IDs before lookup, rejecting malformed newline-containing parameters and pinning the behavior in the auth/security regression suite (#80, thanks @SJoon99). The MCP server now pre-warms the tool registry on the main thread before servingtools/call, avoiding a first-call deadlock in lazy tool discovery (#85, thanks @Teerapat-Vatpitak). The Vite dev proxy also honorsVITE_API_URLfor non-default backend targets (#82, thanks @voidborne-d).
* 2026-05-08🧾Tushare statement fields in filters: A-share daily backtests can now request PIT-safe financial statement fields throughfundamental_fields, so signal engines can screen onincome_total_revenue,income_n_income,balancesheet_total_hldr_eqy_exc_min_int,fina_indicator_roe, and similar table-prefixed columns after their announcement/disclosure dates (#76, thanks @mrbob-git). Follow-up hardening makes explicit statement-field requests fail fast if Tushare enrichment cannot run, instead of silently falling back to raw price bars (#77).
* 2026-05-07📈Tushare fundamentals + community triage: Added a point-in-timeTushareFundamentalProvidercontract for fundamental research workflows, with regression coverage for the projectTUSHARE_TOKENenvironment path (#74). Community triage also clarified that Vibe-Trading keeps rapid iteration focused on one UI language for now, avoids adding redundant search dependencies while DuckDuckGo-backedweb_searchis already bundled, and treats unofficial hosted deployments as untrusted places for API keys or data-source tokens.
* 2026-05-06🚀v0.1.7 released(Release notes,pip install -U vibe-trading-ai): Security-boundary hardening is now published on PyPI and ClawHub, covering safer API/read/upload/file/URL/generated-code/shell-tool/Docker defaults while keeping localhost CLI/Web UI workflows low-friction. This cycle also includes Web UI Settings, correlation heatmap, OpenAI Codex OAuth, A-share pre-ST filtering, interactive CLI UX, swarm preset inspection, dividend analysis, dev workflow polish, and audited frontend build-dependency floors. Thanks to the 0.1.7 contributors and to lemi9090 (S2W) for coordinated security validation.
* 2026-05-05🛡️Security boundary follow-up: Completes the remaining security-boundary hardening around explicit CORS origins, Settings credential indicators, web URL reading, and Shadow Account code generation, with regression tests added for each path. Normal localhost CLI/Web UI workflows stay the same; remote deployments should continue usingAPI_AUTH_KEYand explicit trusted origins.
* 2026-05-04🖥️Interactive CLI UX + CI cleanup: Interactive mode now has a live bottom status bar showing provider/model, session duration, last-run latency, and cumulative tool-call stats, plus prompt history navigation and cursor editing with arrow keys viaprompt_toolkit(#69). The CLI still falls back to Rich prompts whenprompt_toolkitor a TTY is unavailable. CI path expectations were also aligned with the hardened file-import sandbox and cross-platform/tmpresolution, returning main to green (bb67dc7).
* 2026-05-03🛡️Security hardening patch: Tightens default API authentication for non-local deployments, protects sensitive run/session/swarm reads, restricts upload and local file-reading boundaries, gates shell-capable tools by entry point, validates generated strategy loading before import, and runs the Docker image as a non-root user with a localhost-only published port by default. Local CLI and localhost Web UI workflows remain low-friction; remote API/Web deployments should setAPI_AUTH_KEY.
* 2026-05-02🧭Dividend analysis + sharper roadmap: Added thedividend-analysisskill for income stocks, payout sustainability, dividend growth, shareholder yield, ex-dividend mechanics, and yield-trap checks, pinned by bundled-skill regression tests. The public roadmap now focuses on upcoming work: Research Autopilot, Data Bridge, Options Lab, Portfolio Studio, Alpha Zoo, Research Delivery, Trust Layer, and Community sharing.
* 2026-05-01🔥Correlation heatmap + OpenAI Codex OAuth + A-share pre-ST filter: New correlation dashboard/API computes rolling return correlations and renders an ECharts heatmap for portfolio and symbol analysis (#64). OpenAI Codex provider support now uses ChatGPT OAuth viavibe-trading provider login openai-codex, with Settings metadata and adapter regression tests (#65). Added and hardened theashare-pre-st-filterskill for A-share ST/*ST risk screening, including Sina penalty relevance filtering so securities-account mentions do not inflate E2 counts (#63).
* 2026-04-30⚙️Web UI Settings + validation CLI hardening: New Settings page for LLM provider/model, base URL, reasoning effort, and data source credentials, backed by local/auth-protected settings APIs and data-driven provider metadata (#57). Also hardenspython -m backtest.validation <run_dir>so missing, blank, malformed, non-existent, and non-directory inputs fail with clear operator-facing messages before validation starts (#60).
* 2026-04-28🚀v0.1.6 released(pip install -U vibe-trading-ai): Fixesvibe-trading --swarm-presetsreturning empty afterpip install/uv tool install(#55) — preset YAMLs now bundled inside thesrc.swarmpackage and pinned by a 6-test regression suite. Plus AKShare loader correctly routes ETFs (510300.SH) and forex (USDCNH) to the right endpoints with hardened registry fallback. Rolls up everything since v0.1.5: benchmark comparison panel,/uploadstreaming + size limits, Futu loader (HK + A-share), vnpy export skill, security hardening, frontend lazy loading (688KB → 262KB).
* 2026-04-27📊Benchmark panel + upload safety: Backtest output now ships a benchmark comparison panel (ticker / benchmark return / excess return / information ratio) with yfinance-backed resolution for SPY, CSI 300, etc. (#48). Plus/uploadstreams the request body in 1 MB chunks and aborts pastMAX_UPLOAD_SIZE, bounding memory under oversized/malformed clients (#53) — pinned by a 4-case regression suite.
* 2026-04-22🛡️Hardening + new integrations: Path containment enforced insafe_path+ journal/shadow tool sandbox,MANIFEST.inships.env.example/ tests / Docker files in sdist, route-level lazy loading shrinks frontend initial bundle 688KB → 262KB. Plus Futu data loader for HK & A-share equities (#47) and vnpy CtaTemplate export skill (#46).
* 2026-04-21🛡️Workspace + docs: Relativerun_dirnormalized to active run dir (#43). README usage examples (#45).
* 2026-04-20🔌Reasoning + Swarm:reasoning_contentpreserved across allChatOpenAIpaths — Kimi / DeepSeek / Qwen thinking work end-to-end (#39). Swarm streaming + clean Ctrl+C (#42).
* 2026-04-19📦v0.1.5: Published to PyPI & ClawHub.python-multipartCVE floor bump, 5 new MCP tools wired (analyze_trade_journal+ 4 shadow-account tools),pattern_recognition→patternregistry fix, Docker dep parity, SKILL manifest synced (22 MCP tools / 71 skills).
* 2026-04-18👥Shadow Account: Extract your strategy rules from a broker journal → backtest the shadow across markets → 8-section HTML/PDF report showing exactly how much you leave on the table (rule violations, early exits, missed signals, counterfactual trades). 4 new tools, 1 skill, 32 tools total. Trade Journal + Shadow Account samples now live in the web UI welcome screen.
* 2026-04-17📊Trade Journal Analyzer + Universal File Reader: Upload broker exports (同花顺/东财/富途/generic CSV) → auto trading profile (holding days, win rate, PnL ratio, drawdown) + 4 bias diagnostics (disposition effect, overtrading, chasing momentum, anchoring).read_documentnow dispatches PDF, Word, Excel, PowerPoint, images (OCR), and 40+ text formats behind one unified call.
* 2026-04-16🧠Agent Harness: Persistent cross-session memory, FTS5 session search, self-evolving skills (full CRUD), 5-layer context compression, read/write tool batching. 27 tools, 107 new tests.
* 2026-04-15🤖Z.ai + MiniMax: Z.ai provider (#35), MiniMax temperature fix + model update (#33). 13 providers.
* 2026-04-14🔧MCP Stability: Fixed backtest toolConnection closederror on stdio transport (#32).
* 2026-04-13🌐Cross-Market Composite Backtest: NewCompositeEnginebacktests mixed-market portfolios (e.g. A-shares + crypto) with shared capital pool and per-market rules. Also fixed swarm template variable fallback and frontend timeout.
* 2026-04-12🌍Multi-Platform Export:/pineexports strategies to TradingView (Pine Script v6), TDX (通达信/同花顺/东方财富), and MetaTrader 5 (MQL5) in one command.
* 2026-04-11🛡️Reliability & DX:vibe-trading init.env bootstrap (#19), preflight checks, runtime data-source fallback, hardened backtest engine. Multi-language README (#21).
* 2026-04-10📦v0.1.4: Docker fix (#8),web_searchMCP tool, 12 LLM providers,akshare/ccxtdeps. Published to PyPI and ClawHub.
* 2026-04-09📊Backtest Wave 2: ChinaFutures, GlobalFutures, Forex, Options v2 engines. Monte Carlo, Bootstrap CI, Walk-Forward validation.
* 2026-04-08🔧Multi-market backtestwith per-market rules, Pine Script v6 export, 5 data sources with auto-fallback.

## ✨ Key Features

### 🔍 Self-Improving Trading Agent

 • Natural-language market research

 • Strategy drafts and file/web analysis

 • Memory-backed workflows
 

### 🐝 Multi-Agent Trading Teams

 • Investment, quant, crypto, and risk teams

 • Streaming progress and persisted reports

 • Workers grounded with fetched market data
 

### 📊 Cross-Market Data & Backtesting

 • A/HK/US equities, crypto, futures, and forex

 • Data fallback and composite backtests

 • PIT data, validation, and run cards
 

### 👥 Shadow Account

 • Broker-journal behavior diagnostics

 • Rule-based Shadow Account comparisons

 • Exportable audit reports and strategy code
 

## 💡 What Is Vibe-Trading?

Vibe-Trading is an open-source research workspace for turning finance questions into runnable analysis. It connects natural-language prompts to market-data loaders, strategy generation, backtest engines, reports, exports, and persistent research memory.

It is designed for research, simulation, and backtesting — and, when you choose, autonomous trading through a broker you authorize yourself (e.g. Robinhood Agentic Trading). It holds no funds and never trades outside the limits you set, and you can halt it instantly.

## ✨ What You Can Do

Task

Output

Ask a trading question

Market research with tools, data, documents, and reusable session context.

Backtest a strategy idea

Strategy code, metrics, benchmark context, validation artifacts, and run cards.

Review your own trades

Broker-journal parsing, behavior diagnostics, rule extraction, and Shadow Account comparisons.

Improve repeated research

Persistent memory and editable skills turn useful routines into reusable workflows.

Run analyst teams

Multi-agent research reviews for investment, quant, crypto, macro, and risk workflows.

Ship usable artifacts

Reports, TradingView Pine Script, TDX, MetaTrader 5, MCP tools, and later research sessions.

Bench a pre-built alpha zoo

One-line IC + alive/reversed/dead categorisation across 452 alphas (Qlib 158 + Kakushadze 101 + GTJA 191 + FF5 + Carhart) on your universe.

## ⚡ Quick Example

pip install vibe-trading-ai

#
 Natural-language research

vibe-trading run -p 
"
Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report
"

#
 Bench a pre-built alpha zoo (one line)

vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20

vibe-trading --upload trades_export.csv
vibe-trading run -p 
"
Analyze my trading behavior, extract my shadow strategy, and compare it with my actual trades
"

## 👥 Shadow Account

Shadow Account starts from your own trading records instead of a generic strategy template.

Upload a broker export, let the agent summarize your behavior, then compare the actual trading path with a rule-based shadow strategy.

Step

Agent output

1. Read your journal

Parses broker exports from 同花顺, 东方财富, 富途, and generic CSV formats.

2. Profile your behavior

Holding days, win rate, PnL ratio, drawdown, disposition effect, overtrading, momentum chasing, and anchoring checks.

3. Extract your rules

Turns recurring entries/exits into an explicit strategy profile instead of a hand-wavy summary.

4. Run the shadow

Backtests the extracted rules and highlights rule breaks, early exits, missed signals, and alternative trade paths.

5. Deliver the report

Produces an HTML/PDF report that can be inspected, archived, or refined in a later session.

vibe-trading --upload trades_export.csv
vibe-trading run -p 
"
Analyze my trading behavior, extract my shadow strategy, and compare it with my actual trades
"

## 🧪 Research Workflow

Most runs follow the same evidence path: route the request, load the right market context, execute tools, validate outputs, and keep the artifacts inspectable.

Layer

What happens

Plan

Selects the relevant finance skills, tools, data sources, and swarm preset when useful.

Ground

Pulls A-shares, HK/US equities, crypto, futures, forex, documents, or web context through the available loaders.

Execute

Generates testable strategy code, runs tools, and uses the matching backtest engine or analysis workflow.

Validate

Adds metrics, benchmark comparison, Monte Carlo, Bootstrap, Walk-Forward, run cards, and warnings where applicable.

Deliver

Returns reports, artifacts, tool traces, and exports for TradingView, TDX, MetaTrader 5, MCP clients, or later sessions.

## 🔩 Detailed Capabilities

Detailed inventories are folded below to keep the main README scannable. Open them when you want to inspect the available building blocks.

Finance Skill Library
 
77 skills across 8 categories

* 📊 77 specialized finance skills organized into 8 categories
* 🌐 Complete coverage from traditional markets to crypto & DeFi
* 🔬 Comprehensive capabilities spanning data sourcing to quantitative research

Category

Skills

Examples

Data Source

7

data-routing
, 
tushare
, 
yfinance
, 
okx-market
, 
akshare
, 
mootdx
, 
ccxt

Strategy

17

strategy-generate
, 
cross-market-strategy
, 
technical-basic
, 
candlestick
, 
ichimoku
, 
elliott-wave
, 
smc
, 
multi-factor
, 
ml-strategy

Analysis

17

factor-research
, 
macro-analysis
, 
global-macro
, 
valuation-model
, 
earnings-forecast
, 
credit-analysis
, 
dividend-analysis

Asset Class

9

options-strategy
, 
options-advanced
, 
convertible-bond
, 
etf-analysis
, 
asset-allocation
, 
sector-rotation

Crypto

7

perp-funding-basis
, 
liquidation-heatmap
, 
stablecoin-flow
, 
defi-yield
, 
onchain-analysis

Flow

7

hk-connect-flow
, 
us-etf-flow
, 
edgar-sec-filings
, 
financial-statement
, 
adr-hshare

Tool

11

backtest-diagnose
, 
report-generate
, 
pine-script
, 
doc-reader
, 
web-reader
, 
vnpy-export
, 
alpha-zoo

Risk Analysis

1

ashare-pre-st-filter

Preset Trading Teams
 
29 swarm presets

* 🏢 29 ready-to-use agent teams
* ⚡ Pre-configured finance workflows
* 🎯 Investment, trading & risk management presets

Preset

Workflow

investment_committee

Bull/bear debate → risk review → PM final call

global_equities_desk

A-share + HK/US + crypto researcher → global strategist

crypto_trading_desk

Funding/basis + liquidation + flow → risk manager

earnings_research_desk

Fundamental + revision + options → earnings strategist

macro_rates_fx_desk

Rates + FX + commodity → macro PM

quant_strategy_desk

Screening + factor research → backtest → risk audit

technical_analysis_panel

Classic TA + Ichimoku + harmonic + Elliott + SMC → consensus

risk_committee

Drawdown + tail risk + regime review → sign-off

global_allocation_committee

A-shares + crypto + HK/US → cross-market allocation

Plus 20+ additional specialist presets — run vibe-trading --swarm-presets to explore all.

Alpha Zoo
 
452 pre-built quant alphas across 4 zoos

* 🧬 452 cross-sectional alphas, lookahead-banned at the operator layer
* 📈 IC + IR + alive/reversed/dead categorisation in one CLI command
* 🔬 AST purity gate + 300-row lookahead sentinel test +pytest-socketnetwork kill-switch
* 📦 Apache-2 attribution for Qlib; per-zooLICENSE.mddeclaring formulas as mathematical content
* 🤝 Developer Certificate of Origin (DCO) sign-off workflow for community PRs

Zoo

Count

Source

License

qlib158

154

Microsoft Qlib 
Alpha158
 (Apache-2.0, commit-pinned)

Apache-2.0

alpha101

101

Kakushadze (2015), "101 Formulaic Alphas", arXiv:1601.00991

Formulas are mathematical content

gtja191

191

Guotai Junan (2014), "191 Short-period Trading Alpha Factors"

Formulas are mathematical content

academic

6

Fama-French 5 + Carhart momentum (price-based proxies)

Public academic literature

Runvibe-trading alpha listto browse,vibe-trading alpha show <id>for formulas + source,vibe-trading alpha bench --zoo X --universe Y --period Zto score a whole zoo.

## 🎬 Demo

cli_sm.mp4

frontend_sm.mp4

☝️ Natural-language backtest & multi-agent swarm debate — Web UI + CLI

## 🚀 Quick Start

### One-line install (PyPI)

pip install vibe-trading-ai

Then run a first research task:

vibe-trading init
vibe-trading run -p 
"
Backtest a BTC-USDT 20/50 moving-average strategy for 2024 and summarize return and drawdown
"

Package name vs commands:The PyPI package isvibe-trading-ai. Once installed, you get three commands:

Command

Purpose

vibe-trading

Interactive CLI / TUI

vibe-trading serve

Launch FastAPI web server

vibe-trading-mcp

Start MCP server (for Claude Desktop, OpenClaw, Cursor, etc.)

vibe-trading init 
#
 interactive .env setup

vibe-trading 
#
 launch CLI

vibe-trading serve --port 8899 
#
 launch web UI

vibe-trading-mcp 
#
 start MCP server (stdio)

### Or choose a path

Path

Best for

Time

A. Docker

Try it now, zero local setup

2 min

B. Local install

Development, full CLI access

5 min

C. MCP plugin

Plug into your existing agent

3 min

D. ClawHub

One command, no cloning

1 min

### Prerequisites

* AnLLM API keyfrom any supported provider — or run locally withOllama(no key needed)
* Python 3.11+for Path B
* Dockerfor Path A
* OpenAI Codex can also be used with ChatGPT OAuth: setLANGCHAIN_PROVIDER=openai-codex, then runvibe-trading provider login openai-codex. This does not useOPENAI_API_KEY.

Supported LLM providers:OpenRouter, OpenAI, DeepSeek, Gemini, Groq, DashScope/Qwen, Zhipu, Moonshot/Kimi, MiniMax, Xiaomi MIMO, Z.ai, Ollama (local). See.env.examplefor config.

Tip:All markets work without any API keys thanks to automatic fallback. yfinance (HK/US), OKX (crypto), mootdx (A-shares, TCP-direct, no IP throttle), and AKShare (A-shares, US, HK, futures, forex) are all free. Tushare token is optional — mootdx is the preferred no-token A-share fallback, with AKShare as a broader backup.

### Path A: Docker (zero setup)

git clone https://github.com/HKUDS/Vibe-Trading.git

cd
 Vibe-Trading
cp agent/.env.example agent/.env

#
 Edit agent/.env — uncomment your LLM provider and set API key

docker compose up --build

Openhttp://localhost:8899. Backend + frontend in one container.

Docker publishes the backend on127.0.0.1:8899by default and runs the app as a non-root container user. If you intentionally expose the API beyond your own machine, set a strongAPI_AUTH_KEYand sendAuthorization: Bearer <key>from clients.

### Path B: Local install

git clone https://github.com/HKUDS/Vibe-Trading.git

cd
 Vibe-Trading
python -m venv .venv

#
 Activate

source
 .venv/bin/activate 
#
 Linux / macOS

#
 .venv\Scripts\Activate.ps1 # Windows PowerShell

pip install -e 
.

cp agent/.env.example agent/.env 
#
 Edit — set your LLM provider API key

vibe-trading 
#
 Launch interactive TUI

Start web UI (optional)

#
 Terminal 1: API server

vibe-trading serve --port 8899

#
 Terminal 2: Frontend dev server

cd
 frontend 
&&
 npm install 
&&
 npm run dev

Openhttp://localhost:5899. The frontend proxies API calls tolocalhost:8899.

Production mode (single server):

cd
 frontend 
&&
 npm run build 
&&
 
cd
 ..
vibe-trading serve --port 8899 
#
 FastAPI serves dist/ as static files

### Path C: MCP plugin

SeeMCP Pluginsection below.

### Path D: ClawHub (one command)

npx clawhub@latest install vibe-trading --force

The skill + MCP config is downloaded into your agent's skills directory. SeeClawHub installfor details.

## 🧠 Environment Variables

Copyagent/.env.exampletoagent/.envand uncomment the provider block you want. Each provider needs 3-4 variables:

Variable

Required

Description

LANGCHAIN_PROVIDER

Yes

Provider name (
openrouter
, 
deepseek
, 
groq
, 
ollama
, etc.)

<PROVIDER>_API_KEY

Yes*

API key (
OPENROUTER_API_KEY
, 
DEEPSEEK_API_KEY
, etc.)

<PROVIDER>_BASE_URL

Yes

API endpoint URL

LANGCHAIN_MODEL_NAME

Yes

Model name (e.g. 
deepseek-v4-pro
)

TUSHARE_TOKEN

No

Tushare Pro token for A-share data (falls back to AKShare)

TIMEOUT_SECONDS

No

LLM call timeout, default 120s

API_AUTH_KEY

Recommended for network deployments

Bearer token required when the API is reachable from non-local clients

VIBE_TRADING_ENABLE_SHELL_TOOLS

No

Explicit opt-in for shell-capable tools in remote API/MCP-SSE style deployments

VIBE_TRADING_ALLOWED_FILE_ROOTS

No

Extra comma-separated roots for document and broker-journal imports

VIBE_TRADING_ALLOWED_RUN_ROOTS

No

Extra comma-separated roots for generated-code run directories

* Ollama does not require an API key. OpenAI Codex uses ChatGPT OAuth and stores tokens viaoauth-cli-kit, not inagent/.env.

Free data (no key needed):A-shares via AKShare, HK/US equities via yfinance, crypto via OKX, 100+ crypto exchanges via CCXT. The system automatically selects the best available source for each market.

### 🎯 Recommended Models

Vibe-Trading is a tool-heavy agent — skills, backtests, memory, and swarms all flow through tool calls. Model choice directly decides whether the agentusesits tools or fabricates answers from training data.

Tier

Examples

When to use

Best

anthropic/claude-opus-4.7
, 
anthropic/claude-sonnet-4.6
, 
openai/gpt-5.5-pro
, 
google/gemini-3.5-flash

Complex swarms (3+ agents), long research sessions, paper-grade analysis

Sweet spot
 (default)

deepseek-v4-pro
, 
deepseek/deepseek-v4-pro
, 
x-ai/grok-4.20
, 
z-ai/glm-5.1
, 
moonshotai/kimi-k2.6
, 
qwen/qwen3-max-thinking

Daily driver — reliable tool-calling at ~1/10 the cost

Avoid for agent use

*-nano
, 
*-flash-lite
, 
*-coder-next
, small / distilled variants

Tool-calling is unreliable — the agent will appear to "answer from memory" instead of loading skills or running backtests

The defaultagent/.env.exampleships with DeepSeek official API +deepseek-v4-pro; OpenRouter users can usedeepseek/deepseek-v4-pro.

## 🖥 CLI Reference

The interactive TUI (vibe-trading) now uses a terminal-native transcript: a startup banner, prompt rule, previous-turn recap, live activity rail, Markdown/table rendering, and run timing all stay in the CLI. Non-interactive invocations such asvibe-trading run, pipes, and--jsonremain script-friendly.

vibe-trading 
#
 interactive TUI

vibe-trading run -p 
"
...
"
 
#
 single run

vibe-trading serve 
#
 API server

vibe-trading alpha list 
#
 browse 452 pre-built alphas; show / bench / compare / export-manifest sub-commands available

Slash commands inside TUI

Command

Description

/help

Show all commands

/skills

List all 77 finance skills

/swarm

List 29 swarm team presets

/swarm run <preset> [vars_json]

Run a swarm team with live streaming

/swarm list

Swarm run history

/swarm show <run_id>

Swarm run details

/swarm cancel <run_id>

Cancel a running swarm

/list

Recent runs

/show <run_id>

Run details + metrics

/code <run_id>

Generated strategy code

/pine <run_id>

Export indicators (TradingView + TDX + MT5)

/trace <run_id>

Full execution replay

/continue <run_id> <prompt>

Continue a run with new instructions

/sessions

List chat sessions

/settings

Show runtime config

/clear

Clear screen

/quit

Exit

Single run & flags

vibe-trading run -p 
"
Backtest BTC-USDT MACD strategy, last 30 days
"

vibe-trading run -p 
"
Analyze AAPL momentum
"
 --json
vibe-trading run -f strategy.txt

echo
 
"
Backtest 000001.SZ RSI
"
 
|
 vibe-trading run

vibe-trading -p 
"
your prompt
"

vibe-trading --skills
vibe-trading --swarm-presets
vibe-trading --swarm-run investment_committee 
'
{"topic":"BTC outlook"}
'

vibe-trading --list
vibe-trading --show 
<
run_id
>

vibe-trading --code 
<
run_id
>

vibe-trading --pine 
<
run_id
>
 
#
 Export indicators (TradingView + TDX + MT5)

vibe-trading --trace 
<
run_id
>

vibe-trading --continue 
<
run_id
>
 
"
refine the strategy
"

vibe-trading --upload report.pdf

vibe-trading alpha list --zoo gtja191 --limit 10
vibe-trading alpha show gtja191_171
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20

## 💡 Examples

### Strategy & Backtesting

#
 Moving average crossover on US equities

vibe-trading run -p 
"
Backtest a 20/50-day moving average crossover on AAPL for the past year, show Sharpe ratio and max drawdown
"

#
 RSI mean-reversion on crypto

vibe-trading run -p 
"
Test RSI(14) mean-reversion on BTC-USDT: buy below 30, sell above 70, last 6 months
"

#
 Multi-factor strategy on A-shares

vibe-trading run -p 
"
Backtest a momentum + value + quality multi-factor strategy on CSI 300 constituents over 2 years
"

#
 After backtesting, export to TradingView / TDX / MetaTrader 5

vibe-trading --pine 
<
run_id
>

Bench a pre-built alpha zoo(one line):

vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20

Browse the catalogueand inspect a single alpha:

vibe-trading alpha list --zoo gtja191 --theme reversal --limit 10
vibe-trading alpha show gtja191_171

Compose a multi-factor signalfrom the zoo (Python):

from
 
src
.
skills
.
multi_factor
.
zoo_signal_engine
 
import
 
ZooSignalEngine

engine
 
=
 
ZooSignalEngine
.
from_zoo
([
"gtja191_171"
, 
"gtja191_111"
, 
"gtja191_163"
])

panel
 
=
 ... 
# your wide OHLCV panel

signal
 
=
 
engine
.
compute_signal
(
panel
)

### Market Research

#
 Equity deep-dive

vibe-trading run -p 
"
Research NVDA: earnings trend, analyst consensus, option flow, and key risks for next quarter
"

#
 Macro analysis

vibe-trading run -p 
"
Analyze the current Fed rate path, USD strength, and impact on EM equities and gold
"

#
 Crypto on-chain

vibe-trading run -p 
"
Deep dive BTC on-chain: whale flows, exchange balances, miner activity, and funding rates
"

### Swarm Workflows

#
 Bull/bear debate on a stock

vibe-trading --swarm-run investment_committee 
'
{"topic": "Is TSLA a buy at current levels?"}
'

#
 Quant strategy from screening to backtest

vibe-trading --swarm-run quant_strategy_desk 
'
{"universe": "S&P 500", "horizon": "3 months"}
'

#
 Crypto desk: funding + liquidation + flow → risk manager

vibe-trading --swarm-run crypto_trading_desk 
'
{"asset": "ETH-USDT", "timeframe": "1w"}
'

#
 Global macro portfolio allocation

vibe-trading --swarm-run macro_rates_fx_desk 
'
{"focus": "Fed pivot impact on EM bonds"}
'

### Cross-Session Memory

#
 Save your preferences once

vibe-trading run -p 
"
Remember: I prefer RSI-based strategies, max 10% drawdown, hold period 5–20 days
"

#
 The agent recalls them in future sessions automatically

vibe-trading run -p 
"
Build a crypto strategy that fits my risk profile
"

### Upload & Analyze Documents

#
 Analyze a broker export or earnings report

vibe-trading --upload trades_export.csv
vibe-trading run -p 
"
Profile my trading behavior and identify any biases
"

vibe-trading --upload NVDA_Q1_earnings.pdf
vibe-trading run -p 
"
Summarize the key risks and beats/misses from this earnings report
"

## 🌐 API Server

vibe-trading serve --port 8899

Method

Endpoint

Description

GET

/runs

List runs

GET

/runs/{run_id}

Run details

GET

/runs/{run_id}/pine

Multi-platform indicator export

POST

/sessions

Create session

POST

/sessions/{id}/messages

Send message

GET

/sessions/{id}/events

SSE event stream

POST

/upload

Upload PDF/file

GET

/swarm/presets

List swarm presets

POST

/swarm/runs

Start swarm run

GET

/swarm/runs/{id}/events

Swarm SSE stream

GET

/alpha/list

List alphas (filter by zoo/theme/universe)

GET

/alpha/{alpha_id}

Alpha metadata + source code

POST

/alpha/bench

Start a bench job (returns 
job_id
)

GET

/alpha/bench/{job_id}/stream

SSE progress stream

GET

/settings/llm

Read Web UI LLM settings

PUT

/settings/llm

Update local LLM settings

GET

/settings/data-sources

Read local data source settings

PUT

/settings/data-sources

Update local data source settings

Interactive docs:http://localhost:8899/docs

### Security defaults

For localhost development,vibe-trading servekeeps the browser workflow simple. For any non-local client, sensitive API endpoints requireAPI_AUTH_KEY; useAuthorization: Bearer <key>for JSON/upload requests. Browser EventSource streams are handled by the Web UI after you enter the same key once in Settings.

Shell-capable tools are available to local CLI and trusted localhost workflows, but are not exposed to remote API sessions unless you explicitly setVIBE_TRADING_ENABLE_SHELL_TOOLS=1. Document and journal readers are limited to upload/import roots by default; place files underagent/uploads,agent/runs,./uploads,./data,~/.vibe-trading/uploads, or~/.vibe-trading/imports, or add a dedicated directory throughVIBE_TRADING_ALLOWED_FILE_ROOTS.

### Web UI Settings

The Web UI Settings page lets local users update the LLM provider/model, base URL, generation parameters, reasoning effort, and optional market data credentials such as the Tushare token. Settings are persisted toagent/.env; provider defaults are loaded fromagent/src/providers/llm_providers.json.

Settings reads are side-effect free:GET /settings/llmandGET /settings/data-sourcesnever createagent/.env, and they only return project-relative paths. Settings reads and writes can expose credential state or update credentials/runtime environment, so they requireAPI_AUTH_KEYwhen configured. IfAPI_AUTH_KEYis unset for dev mode, settings access is accepted only from loopback clients.

## 🔌 MCP Plugin

Vibe-Trading exposes 36 MCP tools for any MCP-compatible client. Runs as a stdio subprocess — no server setup needed. Core research tools work with zero API keys for HK/US/crypto; trading connector tools use the selected connector profile, andrun_swarmneeds an LLM key.

Claude Desktop

Add toclaude_desktop_config.json:

{
 
"mcpServers"
: {
 
"vibe-trading"
: {
 
"command"
: 
"
vibe-trading-mcp
"

 }
 }
}

OpenClaw

Add to~/.openclaw/config.yaml:

skills
:
 - 
name
: 
vibe-trading

 
command
: 
vibe-trading-mcp

For a first research-only smoke test, confirm tool discovery and run a market
data or backtest request before selecting a trading connector profile. Core
research tools can run without broker credentials; connector-backedtrading_*tools should be used only after you intentionally select and check a connector
profile.run_swarmrequires an LLM key.

Cursor / Windsurf / other MCP clients

vibe-trading-mcp 
#
 stdio (default)

vibe-trading-mcp --transport sse 
#
 SSE for web clients

MCP tools exposed (36):list_skills,load_skill,start_research_goal,get_research_goal,add_goal_evidence,update_research_goal_status,backtest,factor_analysis,analyze_options,pattern_recognition,read_url,read_document,web_search,write_file,read_file,list_swarm_presets,run_swarm,get_market_data,get_swarm_status,get_run_result,list_runs,reap_stale_runs,retry_run,analyze_trade_journal,extract_shadow_strategy,run_shadow_backtest,render_shadow_report,scan_shadow_signals,trading_connections,trading_select_connection,trading_check,trading_account,trading_positions,trading_orders,trading_quote,trading_history.

### SWARM external MCP tools

run_swarmworkers can call operator-approved tools from external MCP servers. Configure the server-side allowlist inVIBE_TRADING_SWARM_AGENT_CONFIG,~/.vibe-trading/swarm-agent.json, or the fallback~/.vibe-trading/agent.json; then list remote tools in a swarm preset using the local MCP wrapper name, such asmcp_internal_kb_search. Caller-providedvariablesstay template data only and cannot inject MCP URLs, commands, environment variables, or allowlist overrides.

Install from ClawHub (one command)

npx clawhub@latest install vibe-trading --force

--forceis required because the skill references external APIs, which triggers VirusTotal's automated scan. The code is fully open-source and safe to inspect.

This downloads the skill + MCP config into your agent's skills directory. No cloning needed.

Browse on ClawHub:clawhub.ai/skills/vibe-trading

OpenSpace — self-evolving skills

All 77 finance skills are published onopen-space.cloudand evolve autonomously through OpenSpace's self-evolution engine.

To use with OpenSpace, add both MCP servers to your agent config:

{
 
"mcpServers"
: {
 
"openspace"
: {
 
"command"
: 
"
openspace-mcp
"
,
 
"toolTimeout"
: 
600
,
 
"env"
: {
 
"OPENSPACE_HOST_SKILL_DIRS"
: 
"
/path/to/vibe-trading/agent/src/skills
"
,
 
"OPENSPACE_WORKSPACE"
: 
"
/path/to/OpenSpace
"

 }
 },
 
"vibe-trading"
: {
 
"command"
: 
"
vibe-trading-mcp
"

 }
 }
}

OpenSpace will auto-discover all 77 skills, enabling auto-fix, auto-improve, and community sharing. Search for Vibe-Trading skills viasearch_skills("finance backtest")in any OpenSpace-connected agent.

## 🔌 Loading Tools from External MCP Servers (MCP Client Mode)

This is the opposite direction from the MCP Plugin above.The MCP Plugin letsotheragents call Vibe-Trading tools.
This section lets thebuilt-inVibe-Trading agent call tools fromyourexternal MCP servers.

### Quick start

Create~/.vibe-trading/agent.json:

{
 
"mcpServers"
: {
 
"my-server"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
my-mcp-server
"
]
 }
 }
}

Run any CLI command — tools from ordinary external servers are automatically injected into the agent's registry after local tools:

vibe-trading run 
"
use my-server to do X
"

### Official IBKR MCP read-only probe

Vibe-Trading can connect directly to Interactive Brokers' official remote MCP
endpoint in read-only mode. Add this to~/.vibe-trading/agent.json:

{
 
"mcpServers"
: {
 
"ibkr"
: {
 
"type"
: 
"
streamableHttp
"
,
 
"url"
: 
"
https://api.ibkr.com/v1/api/mcp
"
,
 
"auth"
: {
 
"type"
: 
"
oauth
"
,
 
"scopes"
: [
"
mcp.read
"
],
 
"clientName"
: 
"
Vibe-Trading
"
,
 
"cacheDir"
: 
"
~/.vibe-trading/live/ibkr/oauth
"

 },
 
"enabledTools"
: [
"
*
"
]
 }
 }
}

Then start the browser OAuth flow:

vibe-trading connector authorize ibkr-live-official-mcp-readonly

The wildcard is accepted only for IBKR'smcp.readprobe. Authorizing this
profile confirms access to IBKR's official read scope; generictrading_accountandtrading_positionscalls stay disabled until IBKR publishes stable read
tool names that Vibe-Trading can map safely. A config that addsmcp.writemust
pin an explicit tool allowlist and still passes through the live order guard.

If IBKR issues a pre-registered OAuth client, addclientIdandclientSecretinsideauth.

### Trading connectors: fastest path

For users who cannot wait for IBKR OAuth client approval, connect to a local
TWS or IB Gateway session. Credentials stay inside IBKR's desktop app; Vibe-
Trading only connects to127.0.0.1and exposes it as a connector profile.

Install the optional SDK:

pip install 
"
vibe-trading-ai[ibkr]
"

Open TWS paper trading or IB Gateway paper, enable API socket clients, then run:

vibe-trading connector list
vibe-trading connector use ibkr-paper-local
vibe-trading connector configure ibkr-paper-local --yes
vibe-trading connector check
vibe-trading connector account
vibe-trading connector positions
vibe-trading connector orders
vibe-trading connector quote AAPL
vibe-trading connector 
history
 AAPL --duration 
"
30 D
"
 --bar-size 
"
1 day
"

Default local ports:

App

Paper

Live read-only

TWS

7497

7496

IB Gateway

4002

4001

The agent exposes connector-scoped tools namedtrading_connections,trading_select_connection,trading_check,trading_account,trading_positions,trading_orders,trading_quote, andtrading_history.
Live-broker raw MCP tools are not registered directly asmcp_<broker>_*.
No IBKR order-placement tool is registered.

### Config reference

Field

Type

Default

Description

type

string

inferred for stdio; required for HTTP

Omit for stdio, or set to 
sse
 / 
streamableHttp
 for URL-based servers.

command

string

required for stdio

Executable to spawn for stdio servers. Invalid for 
sse
 / 
streamableHttp
 servers.

args

array

[]

Command-line arguments for stdio servers only.

env

object

{}

Extra environment variables merged into the subprocess env for stdio servers only.

url

string

required for 
sse
 / 
streamableHttp

Remote SSE / streamable HTTP endpoint URL. Not used for stdio servers.

headers

object

{}

Extra HTTP headers for 
sse
 / 
streamableHttp
 servers only.

toolTimeout

number

30

Per-tool call timeout in seconds

enabledTools

array

["*"]

Tool allowlist. Use 
["*"]
 to expose all tools from the server

Config file location:~/.vibe-trading/agent.json(JSON or YAML).

For URL-based transports,typeis required. The agent no longer guesses between SSE and streamable HTTP from the URL suffix.

### Per-session overrides (API)

When creating a session via the API you can passmcpServersinsidesession.configto extend or override the global config for that session only:

{
 
"config"
: {
 
"mcpServers"
: {
 
"research-server"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
"
research-mcp
"
],
 
"enabledTools"
: [
"
search
"
, 
"
fetch
"
]
 }
 }
 }
}

### Tool naming

Ordinary remote tools are exposed with stable names:mcp_<server>_<tool>.
Live-broker MCP servers stay behind thetrading_*connector surface.

If two server names produce the same ASCII-safe local prefix (e.g.foo-barandfoo_barboth becomefoo_bar), a deterministic hash suffix is appended at the server-segment level so names remain unique. The operator receives a warning:

WARNING: Configured MCP server 'foo-bar' collides with another server after local name
normalization. Using local tool prefix 'mcp_foo_bar_<hash>_<tool>' to keep generated
tool names unique. Rename the server in agent config if you want a different prefix.

### v1 limits

Limit

Detail

Transport

stdio, SSE, and streamable HTTP

Execution

serial only — MCP tools never enter the parallel readonly path

Surfaces

tools only (resources and prompts excluded in v1)

Hot reload

not supported — restart the process to pick up config changes

Swarm path

MCP tools are not available inside Swarm worker registries in v1

## 📁 Project Structure

Click to expand

Vibe-Trading/
├── agent/ # Backend (Python)
│ ├── cli/ # CLI package — interactive TUI + subcommands
│ ├── api_server.py # FastAPI server — runs, sessions, upload, swarm, SSE
│ ├── mcp_server.py # MCP server — 36 tools for OpenClaw / Claude Desktop
│ │
│ ├── src/
│ │ ├── agent/ # ReAct agent core
│ │ │ ├── loop.py # 5-layer compression + read/write tool batching
│ │ │ ├── context.py # system prompt + auto-recall from persistent memory
│ │ │ ├── skills.py # skill loader (77 bundled + user-created via CRUD)
│ │ │ ├── tools.py # tool base class + registry
│ │ │ ├── memory.py # lightweight workspace state per run
│ │ │ ├── frontmatter.py # shared YAML frontmatter parser
│ │ │ └── trace.py # execution trace writer
│ │ │
│ │ ├── memory/ # Cross-session persistent memory
│ │ │ └── persistent.py # file-based memory (~/.vibe-trading/memory/)
│ │ │
│ │ ├── tools/ # 31 auto-discovered agent tools
│ │ │ ├── backtest_tool.py # run backtests
│ │ │ ├── remember_tool.py # cross-session memory (save/recall/forget)
│ │ │ ├── skill_writer_tool.py # skill CRUD (save/patch/delete/file)
│ │ │ ├── session_search_tool.py # FTS5 cross-session search
│ │ │ ├── swarm_tool.py # launch swarm teams
│ │ │ ├── web_search_tool.py # DuckDuckGo web search
│ │ │ └── ... # bash, file I/O, factor analysis, options, alpha browser + bench, etc.
│ │ │
│ │ ├── factors/ # Alpha Zoo — 452 alphas across 4 zoos
│ │ │ ├── base.py # 19 operators (rank/scale/ts_*/delta/decay_linear/safe_div/vwap)
│ │ │ ├── registry.py # AST-only metadata load + lazy compute + sanity gates
│ │ │ ├── bench_runner.py # IC + alive/reversed/dead categorisation
│ │ │ └── zoo/ # qlib158 (154) + alpha101 (101) + gtja191 (191) + academic (6)
│ │ │
│ │ ├── api/ # FastAPI route modules
│ │ │ └── alpha_routes.py # /alpha/list, /alpha/{id}, /alpha/bench, SSE stream
│ │ │
│ │ ├── skills/ # 77 finance skills in 8 categories (SKILL.md each)
│ │ ├── swarm/ # Swarm DAG execution engine
│ │ │ └── presets/ # 29 swarm preset YAML definitions
│ │ ├── session/ # Multi-turn chat + FTS5 session search
│ │ └── providers/ # LLM provider abstraction
│ │
│ └── backtest/ # Backtest engines
│ ├── engines/ # 7 engines + composite cross-market engine + options_portfolio
│ ├── loaders/ # 7 sources: tushare, okx, yfinance, akshare, mootdx, ccxt, futu
│ │ ├── base.py # DataLoader Protocol
│ │ └── registry.py # Registry + auto-fallback chains
│ └── optimizers/ # MVO, equal vol, max div, risk parity
│
├── frontend/ # Web UI (React 19 + Vite + TypeScript)
│ └── src/
│ ├── pages/ # Home, Agent, AlphaZoo, RunDetail, Compare, Correlation, Settings
│ ├── components/ # chat, charts, layout
│ └── stores/ # Zustand state management
│
├── Dockerfile # Multi-stage build
├── docker-compose.yml # One-command deploy
├── pyproject.toml # Package config + CLI entrypoint
├── tools/ # Repo-level CI helpers
│ └── ci_grep_gates.sh # rejects yaml.load / trademark / per-stock-data leaks
└── LICENSE # MIT

## 🏛 Ecosystem

Vibe-Trading is part of theHKUDSagent ecosystem:

NanoBot

Ultra-Lightweight Personal AI Assistant

AI-Trader

Agent-Native Signal & Copy Trading Platform

CLI-Anything

Making All Software Agent-Native

OpenSpace

Self-Evolving AI Agent Skills

ClawTeam

Agent Swarm Intelligence

## 🗺 Roadmap

We ship in phases. Items move toIssueswhen work begins.

Phase

Feature

Status

Trust Layer

Reproducible run cards are emitted and shown in Run Detail; v1 adds tool traces and citations

v0 Shipped

Hypothesis Registry

Durable research hypotheses with lifecycle status, data sources, skills, run-card links, and invalidation notes

Backend MVP Shipped

Research Autopilot

Manual-first research loop: hypothesis → deterministic backtest → evidence report

Next

Data Bridge

Bring-your-own data: local CSV/Parquet/SQL connectors with schema mapping

Planned

Options Lab

Vol surface, Greeks dashboard, payoff/scenario explorer

Planned

Portfolio Studio

Risk x-ray, constraints, turnover-aware optimizer, rebalance notes

Planned

Alpha Zoo

452 pre-built alphas (Qlib 158 + Kakushadze 101 + GTJA 191 + FF5 + Carhart) with one-line bench, agent integration, and Web UI

Shipped 0.1.8

Research Delivery

Scheduled briefs to Slack / Telegram / email-style channels

Planned

Community

Shareable skills, presets, and strategy cards

Exploring

## Contributing

We welcome contributions! SeeCONTRIBUTING.mdfor guidelines.

Good first issuesare tagged withgood first issue— pick one and get started.

Want to contribute something bigger? Check theRoadmapabove and open an issue to discuss before starting.

## Contributors

Thanks to everyone who has contributed to Vibe-Trading!

Recent v0.1.9 cycle contributors and credits:

* @toanalien — session JSONL crash-hardening (#147), graceful agent-loop exit at the iteration budget (#148), pre-flight validation for LLM-generated signal engines (#149), and cross-browser Full Report links (#150)
* @ai7eam-dev — cross-market correlation timestamp alignment (#158) and the session running-status indicator + swarm retry (#159 → #160)
* @shadowinlife — remote MCP servers over SSE/HTTP (#125) and operator-configured external MCP tools in swarm workers (#142)
* @DoubleSky123 — configurable SSE idle timeout (#157)
* @ArthurXi — IME Enter submission handling in the Web composer (#146)
* @omcdecor-cyber — swarm DAG gating when an upstream task fails (#145)
* @Soli22de — strict alpha-bench mode with a mandatory random control (#143)
* @ruok808 — proxy-env support in the CCXT loader (#126)
* @faizack — remote Ollama base-URL normalization (#129)
* @fightZy — agent session history loading fix (#136)
* @lcwSeven — short universe names in the alpha list endpoint (#137)
* @Teerapat-Vatpitak — resolved .env-source logging (#124)
* @warren618 / Haozhe Wu — connector-first broker profiles, the Robinhood Agentic Trading channel, Research Goal runtime, swarm reconcile + retry_run, the agent/cli refactor, the mootdx loader, and release integration

## Disclaimer

Vibe-Trading is research and trading software. It is not investment advice, holds no funds, and runs no execution venue. Trading through a broker channel you explicitly authorize (e.g. Robinhood Agentic Trading) happens only within the limits you set and which you can halt at any time. This broker-trading capability is experimental and not verified by us against a real broker account — use it at your own risk. Past performance does not guarantee future results.

## License

MIT License — seeLICENSE

## Star History

⭐ IfVibe-Tradinghelps your research, a star helps more people find it.

Thanks for visitingVibe-Trading✨

## About

"Vibe-Trading: Your Personal Trading Agent"

vibetrading.wiki/

### Topics

 python

 trading

 mcp

 multi-agent

 fintech

 quantitative-finance

 algorithmic-trading

 backtesting

 ai-agent

 llm

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

9.8k

 stars
 

### Watchers

80

 watching
 

### Forks

2k

 forks
 

 Report repository

 

## Releases6

v0.1.9 — Connectors + Research Goal + swarm retry/reconcile + robustness

 Latest

 

Jun 1, 2026

 

+ 5 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python89.9%
* TypeScript7.1%
* HTML1.6%
* JavaScript0.6%
* CSS0.5%
* Shell0.2%
* Other0.1%