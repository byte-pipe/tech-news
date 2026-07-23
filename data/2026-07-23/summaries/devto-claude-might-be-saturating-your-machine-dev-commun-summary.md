---
title: Claude might be saturating your machine - DEV Community
url: https://dev.to/sidhantpanda/claude-might-be-saturating-your-machine-3h07
date: 2026-07-16
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T19:00:58.369318
---

# Claude might be saturating your machine - DEV Community

# Identifying orphaned AI tasks via PID 1 checks

## Problem
- Laptop fan ran at full speed while the system appeared idle.  
- The cause was ten orphaned busy‑loop processes left by a Claude Code session from two days earlier.

## Quick fix (one‑liner for Claude Code)
- Prompt Claude Code to:
  - Compare load average with core count.  
  - List top CPU consumers with PPID, elapsed time, and full argument list.  
  - Show results for confirmation before any kill action.

## Finding the culprits
- `uptime` revealed a load average of ~123 on a 10‑core machine → clearly non‑idle.  
- `ps -Ao pcpu,pid,ppid,user,comm -r | head` showed many `/bin/zsh` processes at ~60 % CPU, all with **PPID 1** (reparented to `launchd`).  
- Detailed `ps -o pid,lstart,etime,pcpu,args -p 94279,94280,94281` exposed the command:
  ```sh
  /bin/zsh -c "source ~/.claude/shell-snapshots/... && eval '... while :; do :; done ...'"
  ```
  – a loop (`while :; do :; done`) running on every core for ~2 days.

- No remaining test processes (`node`, `vitest`, `pnpm`) were found, confirming only the spinners remained.  
- CPU accounting: 12 processes >20 % CPU contributed ~850 % total CPU usage.

## Why the cleanup failed
1. **Job control disabled** in the non‑interactive shell, so `jobs -p` returned empty and `kill $LOADPIDS` had no targets.  
   - Fix: capture each background PID with `$!` and build `LOADPIDS` manually.  
2. **Parent shell exited** before reaching the kill line.  
   - Fix: install a trap to ensure cleanup runs on `EXIT`, `INT`, or `TERM`.

## Fixing it
- Simple `kill` of the offending PIDs terminated all orphaned loops.  
- Verification with `ps` showed zero matching processes.  
- System returned to normal: Chrome consumed ~130 % CPU, overall load dropped, fan noise subsided after a minute or two.

## Checking your own machine
1. Run `uptime` and compare load average to core count (`sysctl -n hw.ncpu`).  
2. List top CPU consumers:  
   ```sh
   ps -Ao pcpu,pid,ppid,user,comm -r | head -15
   ```  
3. Spot processes with **PPID 1** and long elapsed time.  
4. Inspect their full arguments:  
   ```sh
   ps -o pid,ppid,lstart,etime,pcpu,args -p <pid>
   ```  
5. On macOS, Activity Monitor sorted by CPU shows the same pattern, but argument details are only visible via `ps`.

## Takeaway
- AI agents can launch resource‑heavy background work that persists after the session crashes or is cancelled.  
- Orphaned processes appear as children of PID 1 with high CPU usage and long runtimes.  
- A quick `ps -Ao pcpu,pid,ppid,user,comm -r | head` check would have revealed the issue within minutes.