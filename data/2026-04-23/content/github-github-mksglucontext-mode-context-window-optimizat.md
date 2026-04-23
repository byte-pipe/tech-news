---
title: 'GitHub - mksglu/context-mode: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms · GitHub'
url: https://github.com/mksglu/context-mode
site_name: github
content_file: github-github-mksglucontext-mode-context-window-optimizat
fetched_at: '2026-04-23T20:05:51.190837'
original_url: https://github.com/mksglu/context-mode
author: mksglu
description: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms - mksglu/context-mode
---

mksglu

 

/

context-mode

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork653
* Star9.3k

 
 
 
 
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

903 Commits
903 Commits
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.github
.github
 
 
.openclaw-plugin
.openclaw-plugin
 
 
.pi/
extensions/
context-mode
.pi/
extensions/
context-mode
 
 
configs
configs
 
 
docs
docs
 
 
hooks
hooks
 
 
insight
insight
 
 
scripts
scripts
 
 
skills
skills
 
 
src
src
 
 
tests
tests
 
 
web
web
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.npmignore
.npmignore
 
 
BENCHMARK.md
BENCHMARK.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
cli.bundle.mjs
cli.bundle.mjs
 
 
llms-full.txt
llms-full.txt
 
 
llms.txt
llms.txt
 
 
openclaw.plugin.json
openclaw.plugin.json
 
 
package.json
package.json
 
 
server.bundle.mjs
server.bundle.mjs
 
 
start.mjs
start.mjs
 
 
stats.json
stats.json
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Context Mode

The other half of the context problem.

 
 
 
 
 
 

Used across teams at

## The Problem

Every MCP tool call dumps raw data into your context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone. And when the agent compacts the conversation to free space, it forgets which files it was editing, what tasks are in progress, and what you last asked for.

Context Mode is an MCP server that solves all three sides of this problem:

1. Context Saving— Sandbox tools keep raw data out of the context window. 315 KB becomes 5.4 KB. 98% reduction.
2. Session Continuity— Every file edit, git operation, task, error, and user decision is tracked in SQLite. When the conversation compacts, context-mode doesn't dump this data back into context — it indexes events into FTS5 and retrieves only what's relevant via BM25 search. The model picks up exactly where you left off. If you don't--continue, previous session data is deleted immediately — a fresh session means a clean slate.
3. Think in Code— The LLM should program the analysis, not compute it. Instead of reading 50 files into context to count functions, the agent writes a script that does the counting andconsole.log()s only the result. One script replaces ten tool calls and saves 100x context. This is a mandatory paradigm across all 12 platforms: stop treating the LLM as a data processor, treat it as a code generator.

## Install

Platforms are grouped by install complexity. Hook-capable platforms get automatic routing enforcement. Non-hook platforms need a one-time routing file copy.

Claude Code
 — plugin marketplace, fully automatic

Prerequisites:Claude Code v1.0.33+ (claude --version). If/pluginis not recognized, update first:brew upgrade claude-codeornpm update -g @anthropic-ai/claude-code.

Install:

/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode

Restart Claude Code (or run/reload-plugins).

Verify:

/context-mode:ctx-doctor

All checks should show[x]. The doctor validates runtimes, hooks, FTS5, and plugin registration.

Routing:Automatic. The SessionStart hook injects routing instructions at runtime — no file is written to your project. The plugin registers all hooks (PreToolUse, PostToolUse, PreCompact, SessionStart) and 6 sandbox tools (ctx_batch_execute,ctx_execute,ctx_execute_file,ctx_index,ctx_search,ctx_fetch_and_index) plus meta-tools (ctx_stats,ctx_doctor,ctx_upgrade,ctx_purge,ctx_insight).

Slash Command

What it does

/context-mode:ctx-stats

Context savings — per-tool breakdown, tokens consumed, savings ratio.

/context-mode:ctx-doctor

Diagnostics — runtimes, hooks, FTS5, plugin registration, versions.

/context-mode:ctx-upgrade

Pull latest, rebuild, migrate cache, fix hooks.

/context-mode:ctx-purge

Permanently delete all indexed content from the knowledge base.

/context-mode:ctx-insight

Personal analytics dashboard — 15+ metrics on tool usage, session activity, error rate, parallel work patterns, and mastery curve. Opens a local web UI.

Note:Slash commands are a Claude Code plugin feature. On other platforms, typectx stats,ctx doctor,ctx upgrade, orctx insightin the chat — the model calls the MCP tool automatically. SeeUtility Commands.

Alternative — MCP-only install (no hooks or slash commands)

claude mcp add context-mode -- npx -y context-mode

This gives you the 6 sandbox tools without automatic routing. The model can still use them — it just won't be nudged to prefer them over raw Bash/Read/WebFetch. Good for trying it out before committing to the full plugin.

Gemini CLI
 — one config file, hooks included

Prerequisites:Node.js 18+, Gemini CLI installed.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add the following to~/.gemini/settings.json. This single file registers the MCP server and all four hooks:{"mcpServers": {"context-mode": {"command":"context-mode"}
 },"hooks": {"BeforeTool": [
 {"matcher":"run_shell_command|read_file|read_many_files|grep_search|search_file_content|web_fetch|activate_skill|mcp__plugin_context-mode","hooks": [{"type":"command","command":"context-mode hook gemini-cli beforetool"}]
 }
 ],"AfterTool": [
 {"matcher":"","hooks": [{"type":"command","command":"context-mode hook gemini-cli aftertool"}]
 }
 ],"PreCompress": [
 {"matcher":"","hooks": [{"type":"command","command":"context-mode hook gemini-cli precompress"}]
 }
 ],"SessionStart": [
 {"matcher":"","hooks": [{"type":"command","command":"context-mode hook gemini-cli sessionstart"}]
 }
 ]
 }
}
3. Restart Gemini CLI.

Verify:

/mcp list

You should seecontext-mode: ... - Connected.

Routing:Automatic. The SessionStart hook injects routing instructions at runtime — noGEMINI.mdfile is written to your project. All four hooks (BeforeTool, AfterTool, PreCompress, SessionStart) handle enforcement programmatically.

Why the BeforeTool matcher?It targets only tools that produce large output (run_shell_command,read_file,read_many_files,grep_search,search_file_content,web_fetch,activate_skill) plus context-mode's own tools (mcp__plugin_context-mode). This avoids unnecessary hook overhead on lightweight tools while intercepting every tool that could flood your context window.

Full config reference:configs/gemini-cli/settings.json

VS Code Copilot
 — hooks with SessionStart

Prerequisites:Node.js 18+, VS Code with Copilot Chat v0.32+.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Create.vscode/mcp.jsonin your project root:{"servers": {"context-mode": {"command":"context-mode"}
 }
}
3. Create.github/hooks/context-mode.json:{"hooks": {"PreToolUse": [
 {"type":"command","command":"context-mode hook vscode-copilot pretooluse"}
 ],"PostToolUse": [
 {"type":"command","command":"context-mode hook vscode-copilot posttooluse"}
 ],"SessionStart": [
 {"type":"command","command":"context-mode hook vscode-copilot sessionstart"}
 ]
 }
}
4. Restart VS Code.

Verify:Open Copilot Chat and typectx stats. Context-mode tools should appear and respond.

Routing:Automatic. The SessionStart hook injects routing instructions at runtime — nocopilot-instructions.mdfile is written to your project.

Full hook config including PreCompact:configs/vscode-copilot/hooks.json

Cursor
 — hooks with stop support

Prerequisites:Node.js 18+, Cursor with agent mode.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Create.cursor/mcp.jsonin your project root (or~/.cursor/mcp.jsonfor global):{"mcpServers": {"context-mode": {"command":"context-mode"}
 }
}
3. Create.cursor/hooks.json(or~/.cursor/hooks.jsonfor global):{"version":1,"hooks": {"preToolUse": [
 {"command":"context-mode hook cursor pretooluse","matcher":"Shell|Read|Grep|WebFetch|Task|MCP:ctx_execute|MCP:ctx_execute_file|MCP:ctx_batch_execute"}
 ],"postToolUse": [
 {"command":"context-mode hook cursor posttooluse"}
 ],"stop": [
 {"command":"context-mode hook cursor stop"}
 ]
 }
}ThepreToolUsematcher is optional — without it, the hook fires on all tools. Thestophook fires when the agent turn ends and can send a followup message to continue the loop.afterAgentResponseis also available (fire-and-forget, receives full response text).
4. Copy the routing rules file. Cursor lacks a SessionStart hook, so the model needs a rules file for routing awareness:mkdir -p .cursor/rules
cp node_modules/context-mode/configs/cursor/context-mode.mdc .cursor/rules/context-mode.mdc
5. Restart Cursor or open a new agent session.

Verify:Open Cursor Settings > MCP and confirm "context-mode" shows as connected. In agent chat, typectx stats.

Routing:Hooks enforce routing programmatically viapreToolUse/postToolUse/stop. The.cursor/rules/context-mode.mdcfile provides routing instructions at session start since Cursor'ssessionStarthook is currently rejected by their validator (forum report). Project.cursor/hooks.jsonoverrides~/.cursor/hooks.json.

Known limitation:Cursor acceptsadditional_contextin hook responses but does not surface it to the model (forum #155689). Routing relies on the.mdcrules file instead of hook context injection.

Full configs:configs/cursor/hooks.json|configs/cursor/mcp.json|configs/cursor/context-mode.mdc

OpenCode
 — TypeScript plugin with hooks

Prerequisites:Node.js 18+, OpenCode installed.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add toopencode.jsonin your project root (or~/.config/opencode/opencode.jsonfor global):{"$schema":"https://opencode.ai/config.json","mcp": {"context-mode": {"type":"local","command": ["context-mode"]
 }
 },"plugin": ["context-mode"]
}Themcpentry registers the 6 sandbox tools. Thepluginentry enables hooks — OpenCode calls the plugin's TypeScript functions directly before and after each tool execution, blocking dangerous commands and enforcing sandbox routing.
3. (Optional)Copy the routing rules file. OpenCode lacks a SessionStart hook, so the model needs anAGENTS.mdfile for routing awareness:cp node_modules/context-mode/configs/opencode/AGENTS.md AGENTS.mdThis tells the model which tools to use and which commands are blocked. Without it, hooks still enforce routing — but the model won't knowwhya command was denied.
4. Restart OpenCode.

Verify:In the OpenCode session, typectx stats. Context-mode tools should appear and respond.

Routing:Hooks enforce routing programmatically viatool.execute.beforeandtool.execute.after. The optionalAGENTS.mdfile provides routing instructions for model awareness. Theexperimental.session.compactinghook builds resume snapshots when the conversation compacts.

Note:OpenCode's SessionStart hook is not yet available (#14808), so startup/resume session restore is not supported. Compaction recovery works fully via the plugin.

Full configs:configs/opencode/opencode.json|configs/opencode/AGENTS.md

KiloCode
 — TypeScript plugin with hooks

Prerequisites:Node.js 18+, KiloCode installed.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add tokilo.jsonin your project root (or~/.config/kilo/kilo.jsonfor global):{"$schema":"https://app.kilo.ai/config.json","mcp": {"context-mode": {"type":"local","command": ["context-mode"]
 }
 },"plugin": ["context-mode"]
}Themcpentry registers the 6 sandbox tools. Thepluginentry enables hooks — KiloCode calls the plugin's TypeScript functions directly before and after each tool execution, blocking dangerous commands and enforcing sandbox routing.
3. (Optional)Copy the routing rules file. KiloCode shares the OpenCode plugin architecture and lacks SessionStart, so the model needs anAGENTS.mdfile for routing awareness:cp node_modules/context-mode/configs/opencode/AGENTS.md AGENTS.md
4. Restart KiloCode.

Verify:In the KiloCode session, typectx stats. Context-mode tools should appear and respond.

Routing:Hooks enforce routing programmatically viatool.execute.beforeandtool.execute.after. The optionalAGENTS.mdfile provides routing instructions for model awareness. Theexperimental.session.compactinghook builds resume snapshots when the conversation compacts.

Note:KiloCode shares the same plugin architecture as OpenCode, using the OpenCodeAdapter with platform-specific configuration paths (kilo.jsoninstead ofopencode.json,~/.config/kilo/instead of~/.config/opencode/). SessionStart hook availability depends on KiloCode's implementation.

OpenClaw / Pi Agent
 — native gateway plugin

Prerequisites:OpenClaw gateway running (>2026.1.29), Node.js 22+.

context-mode runs as a nativeOpenClawgateway plugin, targetingPi Agentsessions (Read/Write/Edit/Bash tools). Unlike other platforms, there's no separate MCP server — the plugin registers directly into the gateway runtime via OpenClaw'splugin API.

Install:

1. Clone and install:git clone https://github.com/mksglu/context-mode.gitcdcontext-mode
npm run install:openclawThe installer uses$OPENCLAW_STATE_DIRfrom your environment (default:/openclaw). To specify a custom path:npm run install:openclaw -- /path/to/openclaw-stateCommon locations:Docker—/openclaw(the default).Local—~/.openclawor wherever you setOPENCLAW_STATE_DIR.The installer handles everything:npm install,npm run build,better-sqlite3native rebuild, extension registration inruntime.json, and gateway restart via SIGUSR1.
2. Open a Pi Agent session.

Verify:The plugin registers 8 hooks viaapi.on()(lifecycle) andapi.registerHook()(commands). Typectx statsto confirm tools are loaded.

Routing:Automatic. All tool interception, session tracking, and compaction recovery hooks activate automatically — no manual hook configuration or routing file needed.

Minimum version:OpenClaw >2026.1.29 — this includes theapi.on()lifecycle fix fromPR #9761. On older versions, lifecycle hooks silently fail. The adapter falls back to DB snapshot reconstruction (less precise but preserves critical state).

Full documentation:docs/adapters/openclaw.md

Codex CLI
 — MCP + hooks (waiting for upstream dispatch)

Prerequisites:Node.js 18+, Codex CLI installed.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add to~/.codex/config.toml:[mcp_servers.context-mode]command="context-mode"
3. (Waiting for upstream)Enable the hooks feature flag. Add to~/.codex/config.toml:[features]codex_hooks=trueStatus:Codex CLI's hook system is implemented in source (codex-rs/hooks/) but hook dispatch is not yet wired into the tool execution pipeline (Stage::UnderDevelopment). The feature flag is accepted but hooks don't fire during sessions as of v0.118.0. Our hook scripts are ready — they'll work immediately once Codex enables dispatch. Track progress:openai/codex#16685.
4. (Prepare for when dispatch is enabled)Add hooks for routing enforcement and session tracking. Create~/.codex/hooks.json:{"hooks": {"PreToolUse": [{"hooks": [{"type":"command","command":"context-mode hook codex pretooluse"}] }],"PostToolUse": [{"hooks": [{"type":"command","command":"context-mode hook codex posttooluse"}] }],"SessionStart": [{"hooks": [{"type":"command","command":"context-mode hook codex sessionstart"}] }]
 }
}PreToolUseenforces sandbox routing (blocks dangerous commands, redirects to MCP tools).PostToolUsecaptures session events.SessionStartrestores state after compaction.Note:PreToolUse routing supports deny rules only (blocks dangerous commands). Context injection (additionalContext) is not supported in Codex PreToolUse — it works via PostToolUse and SessionStart instead. This is handled automatically.
5. Copy routing instructions (recommended even with hooks for full routing awareness):cp node_modules/context-mode/configs/codex/AGENTS.md ./AGENTS.mdFor global use:cp node_modules/context-mode/configs/codex/AGENTS.md ~/.codex/AGENTS.md. Global applies to all projects. If both exist, Codex CLI merges them.
6. Restart Codex CLI.

Verify:Start a session and typectx stats. Context-mode tools should appear and respond.

Routing:MCP tools work. Hook-based routing is ready but waiting for Codex to enable hook dispatch. TheAGENTS.mdfile provides routing instructions for model awareness in the meantime.

Exec mode regression (v0.118.0):codex execcancels all MCP tool calls with "user cancelled MCP tool call". Thetool_call_mcp_elicitationflag went stable in 0.118.0, adding an approval prompt that exec-mode can't handle.Pin to Codex ≤0.116.0 for exec-mode MCP.Confirmed by upstream:openai/codex#16685. Interactive mode (codex/codex --full-auto) is not affected.

Antigravity
 — MCP-only, no hooks

Prerequisites:Node.js 18+, Antigravity installed.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add to~/.gemini/antigravity/mcp_config.json:{"mcpServers": {"context-mode": {"command":"context-mode"}
 }
}
3. Copy routing instructions (Antigravity has no hook support):cp node_modules/context-mode/configs/antigravity/GEMINI.md ./GEMINI.md
4. Restart Antigravity.

Verify:In an Antigravity session, typectx stats. Context-mode tools should appear and respond.

Routing:Manual. TheGEMINI.mdfile is the only enforcement method (~60% compliance). There is no programmatic interception. Auto-detected via MCP protocol handshake (clientInfo.name) — no manual platform configuration needed.

Full configs:configs/antigravity/mcp_config.json|configs/antigravity/GEMINI.md

Kiro
 — hooks with steering file

Prerequisites:Node.js 18+, Kiro with MCP enabled (Settings > search "MCP").

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add to.kiro/settings/mcp.jsonin your project (or~/.kiro/settings/mcp.jsonfor global):{"mcpServers": {"context-mode": {"command":"context-mode"}
 }
}
3. Create.kiro/hooks/context-mode.json:{"name":"context-mode","description":"Context-mode hooks for context window protection","hooks": {"preToolUse": [
 {"matcher":"*","command":"context-mode hook kiro pretooluse"}
 ],"postToolUse": [
 {"matcher":"*","command":"context-mode hook kiro posttooluse"}
 ]
 }
}
4. Copy routing instructions. Kiro'sagentSpawn(SessionStart) is not yet implemented, so the model needs a routing file at session start:cp node_modules/context-mode/configs/kiro/KIRO.md ./KIRO.md
5. Restart Kiro.

Verify:Open the Kiro panel > MCP Servers tab and confirm "context-mode" shows a green status indicator. In chat, typectx stats.

Routing:Hooks enforce routing programmatically viapreToolUse/postToolUse. TheKIRO.mdfile provides routing instructions sinceagentSpawn(SessionStart equivalent) is not yet wired. Tool names appear as@context-mode/ctx_batch_execute,@context-mode/ctx_search, etc. Auto-detected via MCP protocol handshake.

Full configs:configs/kiro/mcp.json|configs/kiro/agent.json|configs/kiro/KIRO.md

Zed
 — MCP-only, no hooks

Prerequisites:Node.js 18+, Zed installed.

Install:

1. Install context-mode globally:npm install -g context-mode
2. Add to~/.config/zed/settings.json(Windows:%APPDATA%\Zed\settings.json):{"context_servers": {"context-mode": {"command": {"path":"context-mode"}
 }
 }
}Note: Zed uses"context_servers"and"command": { "path": "..." }syntax, not"mcpServers"or"command": "..."like other platforms.
3. Copy routing instructions (Zed has no hook support):cp node_modules/context-mode/configs/zed/AGENTS.md ./AGENTS.md
4. Restart Zed (or savesettings.json— Zed auto-restarts context servers on config change).

Verify:Open the Agent Panel (Cmd+Shift+A), go to settings, and check the indicator dot next to "context-mode" — green means active. Typectx statsin the agent chat.

Routing:Manual. TheAGENTS.mdfile is the only enforcement method (~60% compliance). There is no programmatic interception. Tool names appear asmcp:context-mode:ctx_batch_execute,mcp:context-mode:ctx_search, etc. Auto-detected via MCP protocol handshake.

Pi Coding Agent
 — extension with full hook support

Prerequisites:Node.js 18+, Pi Coding Agent installed.

Install:

1. Clone the extension:git clone https://github.com/mksglu/context-mode.git~/.pi/extensions/context-modecd~/.pi/extensions/context-mode
npm install
npm run build
2. Add to~/.pi/agent/mcp.json(or.pi/mcp.jsonfor project-level):{"mcpServers": {"context-mode": {"command":"node","args": ["/home/youruser/.pi/extensions/context-mode/node_modules/context-mode/start.mjs"]
 }
 }
}Note:JSON does not expand~. Replace/home/youruserwith your actual home directory (runecho $HOMEto find it).
3. Restart Pi.

Verify:In a Pi session, typectx stats. Context-mode tools should appear and respond.

Routing:Automatic. The extension registers all key lifecycle events (tool_call,tool_result,session_start,session_before_compact), providing full session continuity and routing enforcement.

Build Prerequisites
 
(CentOS, RHEL, Alpine)

Context Mode usesbetter-sqlite3on Node.js, which ships prebuilt native binaries for most platforms. On glibc >= 2.31 systems (Ubuntu 20.04+, Debian 11+, Fedora 34+, macOS, Windows),npm installworks without any build tools.

Linux + Node.js >= 22.13:Context Mode automatically uses the built-innode:sqlitemodule instead ofbetter-sqlite3. This eliminates the native addon entirely, avoidingsporadic SIGSEGV crashescaused by V8'smadvise(MADV_DONTNEED)corrupting the addon's.got.pltsection on Linux. No configuration needed — detection is automatic. Falls back tobetter-sqlite3on older Node.js versions.

Bun users:No native compilation needed. Context Mode automatically detects Bun and uses the built-inbun:sqlitemodule via a compatibility adapter.better-sqlite3and all its build dependencies are skipped entirely.

On older glibc systems (CentOS 7/8, RHEL 8, Debian 10), prebuilt binaries don't load and better-sqlite3automatically falls back to compiling from sourceviaprebuild-install || node-gyp rebuild --release. This requires a C++20 compiler (GCC 10+), Make, and Python with setuptools.

CentOS 8 / RHEL 8(glibc 2.28):

dnf install -y gcc-toolset-10-gcc gcc-toolset-10-gcc-c++ make python3 python3-setuptools
scl 
enable
 gcc-toolset-10 
'
npm install -g context-mode
'

CentOS 7 / RHEL 7(glibc 2.17):

yum install -y centos-release-scl
yum install -y devtoolset-10-gcc devtoolset-10-gcc-c++ make python3
pip3 install setuptools
scl 
enable
 devtoolset-10 
'
npm install -g context-mode
'

Alpine Linux:

Alpine prebuilt binaries (musl) are available in better-sqlite3 v12.8.0+. With the^12.6.2dependency range,npm installresolves to the latest 12.x and works without build tools on Alpine. If you pin an older version:

apk add build-base python3 py3-setuptools
npm install -g context-mode

## Tools

Tool

What it does

Context saved

ctx_batch_execute

Run multiple commands + search multiple queries in ONE call.

986 KB → 62 KB

ctx_execute

Run code in 11 languages. Only stdout enters context.

56 KB → 299 B

ctx_execute_file

Process files in sandbox. Raw content never leaves.

45 KB → 155 B

ctx_index

Chunk markdown into FTS5 with BM25 ranking.

60 KB → 40 B

ctx_search

Query indexed content with multiple queries in one call.

On-demand retrieval

ctx_fetch_and_index

Fetch URL, chunk and index. 24h TTL cache — repeat calls skip network. 
force: true
 to bypass.

60 KB → 40 B

ctx_stats

Show context savings, call counts, and session statistics.

—

ctx_doctor

Diagnose installation: runtimes, hooks, FTS5, versions.

—

ctx_upgrade

Upgrade to latest version from GitHub, rebuild, reconfigure hooks.

—

ctx_purge

Permanently deletes all indexed content from the knowledge base.

—

## How the Sandbox Works

Eachctx_executecall spawns an isolated subprocess with its own process boundary. Scripts can't access each other's memory or state. The subprocess runs your code, captures stdout, and only that stdout enters the conversation context. The raw data — log files, API responses, snapshots — never leaves the sandbox.

Eleven language runtimes are available: JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, and Elixir. Bun is auto-detected for 3-5x faster JS/TS execution.

Authenticated CLIs work through credential passthrough —gh,aws,gcloud,kubectl,dockerinherit environment variables and config paths without exposing them to the conversation.

When output exceeds 5 KB and anintentis provided, Context Mode switches to intent-driven filtering: it indexes the full output into the knowledge base, searches for sections matching your intent, and returns only the relevant matches with a vocabulary of searchable terms for follow-up queries.

## How the Knowledge Base Works

Thectx_indextool chunks markdown content by headings while keeping code blocks intact, then stores them in aSQLite FTS5(Full-Text Search 5) virtual table. The SQLite backend is selected automatically at runtime:bun:sqliteon Bun,node:sqliteon Linux + Node.js >= 22.13, andbetter-sqlite3everywhere else. Search usesBM25 ranking— a probabilistic relevance algorithm that scores documents based on term frequency, inverse document frequency, and document length normalization.Porter stemmingis applied at index time so "running", "runs", and "ran" match the same stem. Titles and headings are weighted5xin BM25 scoring for precise navigational queries.

When you callctx_search, it returns relevant content snippets focused around matching query terms — not full documents, not approximations, the actual indexed content with smart extraction around what you're looking for.ctx_fetch_and_indexextends this to URLs: fetch, convert HTML to markdown, chunk, index. The raw page never enters context. Use thecontentTypeparameter to filter results by type (e.g.codeorprose).

### Ranking: Reciprocal Rank Fusion

Search runs two parallel strategies and merges them withReciprocal Rank Fusion (RRF):

* Porter stemming— FTS5 MATCH with porter tokenizer. "caching" matches "cached", "caches", "cach".
* Trigram substring— FTS5 trigram tokenizer matches partial strings. "useEff" finds "useEffect", "authenticat" finds "authentication".

RRF merges both ranked lists into a single result set, so a document that ranks well in both strategies surfaces higher than one that ranks well in only one. This replaces the old cascading fallback approach where trigram results were only used if porter returned nothing.

### Proximity Reranking

Multi-term queries get an additional reranking pass. Results where query terms appear close together are boosted —"session continuity"ranks passages with adjacent terms higher than pages where "session" and "continuity" appear paragraphs apart.

### Fuzzy Correction

Levenshtein distance corrects typos before re-searching. "kuberntes" becomes "kubernetes", "autentication" becomes "authentication".

### Smart Snippets

Search results use intelligent extraction instead of truncation. Instead of returning the first N characters (which might miss the important part), Context Mode finds where your query terms appear in the content and returns windows around those matches.

### TTL Cache

Indexed content persists in a per-project SQLite database at~/.context-mode/content/. Whenctx_fetch_and_indexis called for a URL that was already indexed within the last 24 hours, the fetch is skipped entirely. The model searches the existing index directly.

* Fresh (<24h):Returns a cache hint (0.3KB) instead of re-fetching (48KB+). Model proceeds toctx_search.
* Stale (>24h):Re-fetches silently. No user action needed.
* force: true:Bypasses cache and re-fetches regardless of TTL.
* 14-day cleanup:Content databases and sources older than 14 days are removed on startup.

This means--continuesessions preserve indexed docs across restarts. No re-fetching, no wasted context tokens.

ctx_statsreports cache performance separately: hits, data avoided, network requests saved, and total context savings including cache.

### Progressive Throttling

* Calls 1-3:Normal results (2 per query)
* Calls 4-8:Reduced results (1 per query) + warning
* Calls 9+:Blocked — redirects toctx_batch_execute

## Session Continuity

When the context window fills up, the agent compacts the conversation — dropping older messages to make room. Without session tracking, the model forgets which files it was editing, what tasks are in progress, what errors were resolved, and what you last asked for.

Context Mode captures every meaningful event during your session and persists them in a per-project SQLite database. When the conversation compacts (or you resume with--continue), your working state is rebuilt automatically — the model continues from your last prompt without asking you to repeat anything.

Session continuity requires 4 hooks working together:

Hook

Role

Claude Code

Gemini CLI

VS Code Copilot

Cursor

OpenCode

KiloCode

OpenClaw

Codex CLI

Antigravity

Kiro

Zed

Pi

PreToolUse

Enforces sandbox routing before tool execution

Yes

--

--

Yes

--

--

--

Yes

--

Yes

--

✓ (via tool_call event)

PostToolUse

Captures events after each tool call

Yes

Yes

Yes

Yes

Plugin

Plugin

Plugin

Yes

--

Yes

--

✓ (via tool_result event)

UserPromptSubmit

Captures user decisions and corrections

Yes

--

--

--

--

--

--

--

--

--

--

--

PreCompact

Builds snapshot before compaction

Yes

Yes

Yes

--

Plugin

Plugin

Plugin

--

--

--

--

✓ (via session_before_compact)

SessionStart

Restores state after compaction or resume

Yes

Yes

Yes

--

--

--

Plugin

Yes

--

--

--

✓ (via session_start event)

Session completeness

Full

High

High

Partial

High

High

High

Partial

--

Partial

--

High

Note:Full session continuity (capture + snapshot + restore) works onClaude Code,Gemini CLI, andVS Code Copilot.OpenCodeprovideshighsession continuity: it captures tool events and injects compaction snapshots via the plugin, but SessionStart is not yet available (#14808), so startup/resume restore is not supported.KiloCodeshares the same plugin architecture as OpenCode via the OpenCodeAdapter, so its continuity level depends on KiloCode's SessionStart support.Cursorcaptures tool events viapreToolUse/postToolUse, butsessionStartis currently rejected by Cursor's validator (forum report), so session restore after compaction is not available yet.OpenClawuses native gateway plugin hooks (api.on()) for full session continuity.Pi Coding Agentprovides high session continuity via extension hooks (tool_call,tool_result,session_start,session_before_compact).Codex CLIhook-based session tracking is ready but waiting for upstream hook dispatch (codex_hooks Stage::UnderDevelopment,openai/codex#16685). MCP tools work. Once dispatch is enabled, session tracking will activate automatically.Antigravity,Kiro, andZedhave no hook support in the current release, so session tracking is not available.

What gets captured

Every tool call passes through hooks that extract structured events:

Category

Events

Priority

Captured By

Files

read, edit, write, glob, grep

Critical (P1)

PostToolUse

Tasks

create, update, complete

Critical (P1)

PostToolUse

Rules

CLAUDE.md / GEMINI.md / AGENTS.md paths + content

Critical (P1)

SessionStart

Decisions

User corrections, preferences ("use X instead", "don't do Y")

High (P2)

UserPromptSubmit

Git

checkout, commit, merge, rebase, stash, push, pull, diff, status

High (P2)

PostToolUse

Errors

Tool failures, non-zero exit codes

High (P2)

PostToolUse

Environment

cwd changes, venv, nvm, conda, package installs

High (P2)

PostToolUse

MCP Tools

All 
mcp__*
 tool calls with usage counts

Normal (P3)

PostToolUse

Subagents

Agent tool invocations

Normal (P3)

PostToolUse

Skills

Slash command invocations

Normal (P3)

PostToolUse

Role

Persona / behavioral directives ("act as senior engineer")

Normal (P3)

UserPromptSubmit

Intent

Session mode classification (investigate, implement, debug)

Low (P4)

UserPromptSubmit

Data

Large user-pasted data references (>1 KB)

Low (P4)

UserPromptSubmit

User Prompts

Every user message (for last-prompt restore)

Critical (P1)

UserPromptSubmit

How sessions survive compaction

PreCompact fires
 → Read all session events from SQLite
 → Build priority-tiered XML snapshot (≤2 KB)
 → Store snapshot in session_resume table

SessionStart fires (source: "compact")
 → Retrieve stored snapshot
 → Write structured events file → auto-indexed into FTS5
 → Build Session Guide with 15 categories
 → Inject <session_knowledge> directive into context
 → Model continues from last user prompt with full working state

The snapshot is built in priority tiers — if the 2 KB budget is tight, lower-priority events (intent, MCP tool counts) are dropped first while critical state (active files, tasks, rules, decisions) is always preserved.

After compaction, the model receives aSession Guide— a structured narrative with actionable sections:

* Last Request— user's last prompt, so the model continues without asking "what were we doing?"
* Tasks— checkbox format with completion status ([x]completed,[ ]pending)
* Key Decisions— user corrections and preferences ("use X instead", "don't do Y")
* Files Modified— all files touched during the session
* Unresolved Errors— errors that haven't been fixed
* Git— operations performed (checkout, commit, push, status)
* Project Rules— CLAUDE.md / GEMINI.md / AGENTS.md paths
* MCP Tools Used— tool names with call counts
* Subagent Tasks— delegated work summaries
* Skills Used— slash commands invoked
* Environment— working directory, env variables
* Data References— large data pasted during the session
* Session Intent— mode classification (implement, investigate, review, discuss)
* User Role— behavioral directives set during the session

Detailed event data is also indexed into FTS5 for on-demand retrieval viasearch().

Per-platform details

Claude Code— Full session support. All 5 hook types fire, capturing tool events, user decisions, building compaction snapshots, and restoring state after compaction or--continue.

Gemini CLI— High coverage. PostToolUse (AfterTool), PreCompact (PreCompress), and SessionStart all fire. Missing UserPromptSubmit, so user decisions and corrections aren't captured — but file edits, git ops, errors, and tasks are fully tracked.

VS Code Copilot— High coverage. Same as Gemini CLI — PostToolUse, PreCompact, and SessionStart all fire. User decisions aren't captured but all tool-level events are.

Cursor— Partial coverage. NativepreToolUseandpostToolUsehooks capture tool events.sessionStartis documented by Cursor but currently rejected by their validator, so session restore is not available. Routing instructions are delivered via MCP server startup instead.

OpenCode— Partial. The TypeScript plugin captures PostToolUse events viatool.execute.after, but SessionStart is not yet available (#14808). Events are stored but not automatically restored after compaction.

KiloCode— Partial. Shares the same plugin architecture as OpenCode via the OpenCodeAdapter. The TypeScript plugin captures PostToolUse events viatool.execute.after, but SessionStart availability depends on KiloCode's implementation. Events are stored but may not be automatically restored after compaction.

OpenClaw / Pi Agent— High coverage. All tool lifecycle hooks (after_tool_call,before_compaction,session_start) fire via the native gateway plugin. User decisions aren't captured but file edits, git ops, errors, and tasks are fully tracked. Falls back to DB snapshot reconstruction if compaction hooks fail on older gateway versions. Seedocs/adapters/openclaw.md.

Codex CLI— MCP active, hooks ready. Hook scripts (PreToolUse, PostToolUse, SessionStart) are implemented and tested but Codex CLI doesn't dispatch them yet (Stage::UnderDevelopment). MCP tools work. Track:openai/codex#16685.

Antigravity— No session support. No hooks, no event capture. Requires manually copyingGEMINI.mdto your project root. Auto-detected via MCP protocol handshake (clientInfo.name).

Zed— No session support. No hooks, no event capture. Requires manually copyingAGENTS.mdto your project root. Auto-detected via MCP protocol handshake (clientInfo.name).

Kiro— Partial coverage. NativepreToolUseandpostToolUsehooks capture tool events and enforce sandbox routing.agentSpawn(the Kiro equivalent of SessionStart) is not yet implemented, so session restore after compaction is not available. Requires manually copyingKIRO.mdto your project root. Auto-detected via MCP protocol handshake (clientInfo.name).

Pi Coding Agent— High coverage. The extension registers all key lifecycle events:tool_call(PreToolUse),tool_result(PostToolUse),session_start(SessionStart), andsession_before_compact(PreCompact). File edits, git ops, errors, and tasks are fully tracked. Session restore after compaction works via the extension's event hooks.

## Platform Compatibility

Feature

Claude Code

Gemini CLI

VS Code Copilot

Cursor

OpenCode

KiloCode

OpenClaw

Codex CLI

Antigravity

Kiro

Zed

Pi

MCP Server

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

PreToolUse Hook

Yes

Yes

Yes

Yes

Plugin

Plugin

Plugin

Yes

--

Yes

--

Yes (extension)

PostToolUse Hook

Yes

Yes

Yes

Yes

Plugin

Plugin

Plugin

Yes

--

Yes

--

Yes (extension)

SessionStart Hook

Yes

Yes

Yes

--

--

--

Plugin

Yes

--

--

--

Yes (extension)

PreCompact Hook

Yes

Yes

Yes

--

Plugin

Plugin

Plugin

--

--

--

--

Yes (extension)

Can Modify Args

Yes

Yes

Yes

Yes

Plugin

Plugin

Plugin

Yes

--

--

--

Yes (extension)

Can Block Tools

Yes

Yes

Yes

Yes

Plugin

Plugin

Plugin

Yes

--

Yes

--

Yes (extension)

Utility Commands (ctx)

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes (/ctx-stats, /ctx-doctor)

Slash Commands

Yes

--

--

--

--

--

--

--

--

--

--

--

Plugin Marketplace

Yes

--

--

--

--

--

--

--

--

--

--

--

OpenCodeuses a TypeScript plugin paradigm — hooks run as in-process functions viatool.execute.before,tool.execute.after, andexperimental.session.compacting, providing the same routing enforcement and session continuity as shell-based hooks. SessionStart is not yet available (#14808), but compaction recovery works via the plugin's compacting hook.

KiloCodeshares the same TypeScript plugin architecture as OpenCode via the OpenCodeAdapter, with platform-specific configuration paths (kilo.jsoninstead ofopencode.json,~/.config/kilo/instead of~/.config/opencode/). Hook capabilities depend on KiloCode's implementation of the plugin interface.

OpenClawruns context-mode as a native gateway plugin targeting Pi Agent sessions. Hooks register viaapi.on()(tool/lifecycle) andapi.registerHook()(commands). All tool interception and compaction hooks are supported. Seedocs/adapters/openclaw.md.

Codex CLIhooks are implemented but dispatch is not yet active (codex_hooksisStage::UnderDevelopment). MCP tools work. Hook scripts are ready and will activate once Codex enables dispatch (openai/codex#16685). PreToolUse supportspermissionDecision: "deny"only —additionalContextis not supported in PreToolUse (context injection works via PostToolUse and SessionStart instead; the codex formatter handles this automatically). See the Codex install section for setup.AntigravityandZeddo not support hooks. They rely solely on manually-copied routing instruction files (AGENTS.md/GEMINI.md) for enforcement (~60% compliance). See each platform's install section for copy instructions. Antigravity and Zed are auto-detected via MCP protocol handshake — no manual platform configuration needed.

Kirosupports nativepreToolUseandpostToolUsehooks for routing enforcement and tool event capture.agentSpawn(SessionStart equivalent) andstopare not yet wired. Requires manually copyingKIRO.mdto your project root. Kiro is auto-detected via MCP protocol handshake (clientInfo.name).

Pi Coding Agentruns context-mode as an extension with full hook support. The extension registerstool_call,tool_result,session_start, andsession_before_compactevents, providing high session continuity coverage. The MCP server provides the 6 sandbox tools.

### Routing Enforcement

Hooks intercept tool calls programmatically — they can block dangerous commands and redirect them to the sandbox before execution. Instruction files guide the model via prompt instructions but cannot block anything.Always enable hooks where supported.

Note:Routing instruction files were previously auto-written to project directories on first session start. This was disabled to prevent git tree pollution (#158,#164). Hook-capable platforms (Claude Code, Gemini CLI, VS Code Copilot, Cursor, OpenCode, OpenClaw, Codex CLI) inject routing via hooks and need no file. Non-hook platforms (Zed, Kiro, Antigravity) require a one-time manual copy — see each platform's install section.

Platform

Hooks

Instruction File

With Hooks

Without Hooks

Claude Code

Yes (auto)

CLAUDE.md

~98% saved

~60% saved

Gemini CLI

Yes

GEMINI.md

~98% saved

~60% saved

VS Code Copilot

Yes

copilot-instructions.md

~98% saved

~60% saved

Cursor

Yes

context-mode.mdc

~98% saved

~60% saved

OpenCode

Plugin

AGENTS.md

~98% saved

~60% saved

OpenClaw

Plugin

AGENTS.md

~98% saved

~60% saved

Codex CLI

Yes

AGENTS.md

~98% saved

~60% saved

Antigravity

--

GEMINI.md

--

~60% saved

Kiro

Yes

KIRO.md

~98% saved

~60% saved

Zed

--

AGENTS.md

--

~60% saved

Pi

✓

AGENTS.md

~98% saved

~60% saved

Without hooks, one unroutedcurlor Playwright snapshot can dump 56 KB into context — wiping out an entire session's worth of savings.

Seedocs/platform-support.mdfor the full capability comparison.

## Utility Commands

Inside any AI session— just type the command. The LLM calls the MCP tool automatically:

ctx stats → context savings, call counts, session report
ctx doctor → diagnose runtimes, hooks, FTS5, versions
ctx upgrade → update from GitHub, rebuild, reconfigure hooks
ctx purge → permanently delete all indexed content from the knowledge base
ctx insight → personal analytics dashboard (opens local web UI)

From your terminal— run directly without an AI session:

context-mode doctor
context-mode upgrade
context-mode insight 
#
 opens analytics dashboard in browser

bash scripts/ctx-debug.sh 
#
 full diagnostic report for bug reports

The debug script collects OS info, runtime versions, better-sqlite3 status, adapter detection, config files (redacted), hook validation, FTS5/SQLite test, executor test, process check, session databases, and environment variables into a single pasteable markdown report.

Works onall platforms. On Claude Code, slash commands (/ctx-stats,/ctx-doctor,/ctx-upgrade,/ctx-purge,/ctx-insight) are also available.

## Benchmarks

Scenario

Raw

Context

Saved

Playwright snapshot

56.2 KB

299 B

99%

GitHub Issues (20)

58.9 KB

1.1 KB

98%

Access log (500 requests)

45.1 KB

155 B

100%

Context7 React docs

5.9 KB

261 B

96%

Analytics CSV (500 rows)

85.5 KB

222 B

100%

Git log (153 commits)

11.6 KB

107 B

99%

Test output (30 suites)

6.0 KB

337 B

95%

Repo research (subagent)

986 KB

62 KB

94%

Over a full session: 315 KB of raw output becomes 5.4 KB. Session time extends from ~30 minutes to ~3 hours.

Full benchmark data with 21 scenarios →

## Try It

These prompts work out of the box. Run/context-mode:ctx-statsafter each to see the savings.

Deep repo research— 5 calls, 62 KB context (raw: 986 KB, 94% saved)

Research https://github.com/modelcontextprotocol/servers — architecture, tech stack,
top contributors, open issues, and recent activity. Then run /context-mode:ctx-stats.

Git history analysis— 1 call, 5.6 KB context

Clone https://github.com/facebook/react and analyze the last 500 commits:
top contributors, commit frequency by month, and most changed files.
Then run /context-mode:ctx-stats.

Web scraping— 1 call, 3.2 KB context

Fetch the Hacker News front page, extract all posts with titles, scores,
and domains. Group by domain. Then run /context-mode:ctx-stats.

Large JSON API— 7.5 MB raw → 0.9 KB context (99% saved)

Create a local server that returns a 7.5 MB JSON with 20,000 records and a secret
hidden at index 13000. Fetch the endpoint, find the hidden record, and show me
exactly what's in it. Then run /context-mode:ctx-stats.

Documentation search— 2 calls, 1.8 KB context

Fetch the React useEffect docs, index them, and find the cleanup pattern
with code examples. Then run /context-mode:ctx-stats.

Session continuity— compaction recovery with full state

Start a multi-step task: "Create a REST API with Express — add routes, tests,
and error handling." After 20+ tool calls, type: ctx stats to see the session
event count. When context compacts, the model continues from your last prompt
with tasks, files, and decisions intact — no re-prompting needed.

## Privacy & Architecture

Context Mode is not a CLI output filter or a cloud analytics dashboard. It operates at the MCP protocol layer — raw data stays in a sandboxed subprocess and never enters your context window. Web pages, API responses, file analysis, Playwright snapshots, log files — everything is processed in complete isolation.

Nothing leaves your machine.No telemetry, no cloud sync, no usage tracking, no account required. Your code, your prompts, your session data — all local. The SQLite databases live in your home directory and die when you're done.

This is a deliberate architectural choice, not a missing feature. Context optimization should happen at the source, not in a dashboard behind a per-seat subscription. Privacy-first is our philosophy — and every design decision follows from it.License →

## Security

Context Mode enforces the same permission rules you already use — but extends them to the MCP sandbox. If you blocksudo, it's also blocked insidectx_execute,ctx_execute_file, andctx_batch_execute.

Zero setup required.If you haven't configured any permissions, nothing changes. This only activates when you add rules.

{
 
"permissions"
: {
 
"deny"
: [
 
"
Bash(sudo *)
"
,
 
"
Bash(rm -rf /*)
"
,
 
"
Read(.env)
"
,
 
"
Read(**/.env*)
"

 ],
 
"allow"
: [
 
"
Bash(git:*)
"
,
 
"
Bash(npm:*)
"

 ]
 }
}

Add this to your project's.claude/settings.json(or~/.claude/settings.jsonfor global rules). All platforms read security policies from Claude Code's settings format — even on Gemini CLI, VS Code Copilot, and OpenCode. Codex CLI security enforcement requires thecodex_hooksfeature flag to be enabled.

The pattern isTool(what to match)where*means "anything".

Commands chained with&&,;, or|are split — each part is checked separately.echo hello && sudo rm -rf /tmpis blocked because thesudopart matches the deny rule.

denyalways wins overallow. More specific (project-level) rules override global ones.

## Contributing

SeeCONTRIBUTING.mdfor the development workflow and TDD guidelines.

git clone https://github.com/mksglu/context-mode.git

cd
 context-mode 
&&
 npm install 
&&
 npm 
test

## License

Licensed underElastic License 2.0(source-available). You can use it, fork it, modify it, and distribute it. Two things you can't do: offer it as a hosted/managed service, or remove the licensing notices. We chose ELv2 over MIT because MIT permits repackaging the code as a competing closed-source SaaS — ELv2 prevents that while keeping the source available to everyone.

## About

Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms

context-mode.com

### Topics

 skills

 mcp

 opencode

 copilot

 codex

 claude

 zed-extension

 antigravity

 mcp-server

 mcp-tools

 cursor-plugin

 claude-code

 codex-cli

 kiro

 claude-code-hooks

 claude-code-plugins

 claude-code-skill

 pi-agent

 openclaw

 context-mode

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

9.3k

 stars
 

### Watchers

66

 watching
 

### Forks

653

 forks
 

 Report repository

 

## Releases116

v1.0.89

 Latest

 

Apr 14, 2026

 

+ 115 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript52.8%
* JavaScript44.0%
* Shell2.0%
* HTML1.1%
* CSS0.1%