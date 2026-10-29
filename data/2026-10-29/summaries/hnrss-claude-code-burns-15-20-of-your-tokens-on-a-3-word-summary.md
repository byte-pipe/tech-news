---
title: Claude Code burns ~15-20% of your tokens on a 3-word status line: a Bun preload that turns agent_summary off · by Flamerix AI, flamerix.ai · MIT · Git...
url: https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
date: 2026-10-29
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:01.275054
---

# Claude Code burns ~15-20% of your tokens on a 3-word status line: a Bun preload that turns agent_summary off · by Flamerix AI, flamerix.ai · MIT · Git...

# Claude Code burns ~15–20% of your tokens on a 3‑word status line  
## TL;DR  
- Download the preload script `no-agent-summary.js` and place it in a stable location.  
- Stop any running Claude daemon: `claude daemon stop --any`.  
- Set `BUN_OPTIONS` to include `--preload /path/to/no-agent-summary.js` (e.g., in `~/.profile` or a wrapper script).  
- Restart Claude Code; the agent summary timers are disabled permanently.  

## The problem  
- Every ~30 seconds each background agent sends its full transcript to its own model (usually Opus) asking for a 3‑5‑word status description.  
- These “agent_summary” requests consume ~15–20 % of total token usage (≈ 1 in 5 API calls) and reduce rate‑limit headroom.  
- The behavior started with version 2.1.232 (August 2026) and cannot be turned off via a setting.  

## How the fix works  
- `no-agent-summary.js` is a Bun preload (~80 lines) that intercepts `setTimeout`/`setInterval`.  
- When the callback source contains the agent‑summary anchor (`[AgentSummary] Timer fired`), it returns an inert timer (delay = 2³¹‑1 ms) so the request is never made.  
- All other timers operate normally.  
- The preload is loaded via `BUN_OPTIONS=--preload …`, avoiding the need to modify the Claude binary.  

## Installation steps  
1. Save `no-agent-summary.js` to an absolute path (e.g., `~/.local/share/no-agent-summary.js`).  
2. Add the preload to `BUN_OPTIONS` globally:  
   - Bash/Zsh: `export BUN_OPTIONS="${BUN_OPTIONS:+$BUN_OPTIONS} --preload /abs/path/no-agent-summary.js"` in `~/.profile` or `~/.bashrc`.  
   - Fish: `set -gx BUN_OPTIONS "$BUN_OPTIONS --preload /abs/path/no-agent-summary.js"` in `~/.config/fish/config.fish`.  
   - Systemd user env: create `~/.config/environment.d/50-no-agent-summary.conf` with `BUN_OPTIONS=--preload /abs/path/no-agent-summary.js`.  
   - Or use a wrapper script named `claude` that injects the preload before invoking the real binary.  
3. Restart the Claude daemon and any existing sessions: `claude daemon stop --any`.  

## Environment variables (optional)  
- `CC_AGENT_SUMMARY_MODE=off` (default) – disables the summary timer.  
- `CC_AGENT_SUMMARY_MODE=pass` – loads the hook but lets timers run (useful for A/B testing).  
- `CC_AGENT_SUMMARY_LOG=/path/to/log` – logs preload activity and suppressed timers.  
- `CC_AGENT_SUMMARY_MARKER=/path/to/marker` – writes a single line indicating preload status.  

## Verification after each update  
1. Run `claude --version` with `BUN_OPTIONS` set and check the log for “preload active mode=off”.  
2. Start a background sub‑agent for a minute; the log should show the summary timer suppressed and the OpenTelemetry `query_source = agent_summary` metric should remain zero.  

## Nuances & failure modes  
- The daemon must be restarted after setting `BUN_OPTIONS`; otherwise already‑spawned processes inherit the old environment.  
- Headless executions (cron, CI, editor integrations) also need the preload.  
- The hook matches by source‑text anchor; if future Claude updates rename the log line or change timer implementation, the hook may stop working (fail‑open). Re‑run verification after each Claude update.  

## Observed effect  
- On a machine running Claude 2.1.301, the preload eliminated all `agent_summary` requests without impacting sub‑agents, background skills, or other functionality.  
- Token consumption dropped by the measured 15–20 % share, freeing rate‑limit headroom.