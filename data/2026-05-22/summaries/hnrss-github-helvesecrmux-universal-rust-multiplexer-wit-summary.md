---
title: GitHub - Helvesec/rmux: Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows. · GitHu...
url: https://github.com/helvesec/rmux
date: 2026-05-21
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-22T06:03:06.357609
---

# GitHub - Helvesec/rmux: Universal Rust multiplexer with a typed SDK — drive any CLI or TUI app from code. Native on Linux, macOS, and Windows. · GitHu...

# rmux – Universal Rust Multiplexer

## Overview
- Rust‑based multiplexer compatible with tmux commands, offering detachable, scriptable, and inspectable sessions.  
- Provides a typed SDK, daemon‑backed architecture, and native Ratatui integration.  
- Runs natively on Linux, macOS, and Windows (including Windows Named Pipes, no WSL required).

## Current Release
- Version **v0.2.0**, published 18 May 2026.  
- All 90 tmux‑compatible commands are implemented; preview status, bugs may exist.  

## Motivation
- Extends the tmux use case to run long‑lived agents over SSH while preserving their terminals.  
- Enables inspection, scripting, and orchestration of agents.  
- Suitable for agents, headless CLI workflows, and interactive human users.

## Demos
- Multi Agents Orchestration (~514 lines)  
- Agent Broadcast Arena (~2,171 lines)  
- Mini‑Zellij (~944 lines)  
- Terminal ↔ Browser Mirroring (~649 lines)  
- Playwright Testing (~1,495 lines)  

## Installation
- **Prebuilt binary (macOS/Linux)**:  
  `curl -fsSL https://rmux.io/install.sh | sh`  
- **Prebuilt binary (Windows PowerShell)**:  
  `irm https://rmux.io/install.ps1 | iex`  
- **Cargo install**:  
  `cargo install rmux --locked`  
- **From source**:  
  `cargo install --path . --locked`  
- **SDK for Rust applications**:  
  `cargo add rmux-sdk`  
  `cargo add ratatui-rmux`  

## Documentation
- Full documentation at **rmux.io/docs** (installation guides, CLI reference, SDK examples, terminal automation, API docs).

## CLI Quickstart
```bash
rmux new-session -d -s work
rmux split-window -h -t work
rmux send-keys -t work 'echo "hello from rmux"' Enter
rmux attach-session -t work
```
- List commands: `rmux list-commands`  
- Get help for a command: `rmux new-session --help`  

## SDK Quickstart (Rust)
```rust
use std::time::Duration;
use rmux_sdk::{
    EnsureSession, EnsureSessionPolicy, Rmux, SessionName, TerminalSizeSpec,
};

#[tokio::main]
async fn main() -> rmux_sdk::Result<()> {
    let rmux = Rmux::builder()
        .default_timeout(Duration::from_secs(5))
        .connect_or_start()
        .await?;

    let session_name = SessionName::new("work")?;
    let session = rmux
        .ensure_session(
            EnsureSession::named(session_name)
                .policy(EnsureSessionPolicy::CreateOrReuse)
                .detached(true)
                .size(TerminalSizeSpec::new(120, 32)),
        )
        .await?;

    let pane = session.pane(0, 0);
    pane.send_text("printf 'ready\\n' && sleep 1\n").await?;
    pane.wait_for_text("ready").await?;
    let snapshot = pane.snapshot().await?;
    println!("{}x{}", snapshot.cols, snapshot.rows);
    Ok(())
}
```

## Ratatui Widget Example
```rust
use ratatui::{buffer::Buffer, layout::Rect, widgets::Widget};
use ratatui_rmux::{PaneState, PaneWidget};
use rmux_sdk::PaneSnapshot;

fn render(snapshot: PaneSnapshot, area: Rect, buffer: &mut Buffer) {
    let state = PaneState::from_snapshot(snapshot);
    PaneWidget::new(&state).render(area, buffer);
}
```

## Architecture
- Three public surfaces: `rmux` CLI, `rmux-sdk` Rust crate, and `ratatui-rmux` widget.  
- All share a single local protocol to communicate with the daemon; capabilities are interchangeable.

## Workspace Crates
- **Public crates**: `rmux-types`, `rmux-proto`, `rmux-os`, `rmux-ipc`, `rmux-sdk`, `ratatui-rmux`, `rmux` (binary).  
- **Support crates**: `rmux-pty`, `rmux-core`, `rmux-server`, `rmux-client`, `rmux-render-core`.  
- **Internal**: `rmux-render-core` (workspace‑internal).

## Platform Support
| Platform | PTY backend | IPC backend | Default endpoint |
|----------|------------|-------------|------------------|
| Linux    | Unix PTY   | Unix socket | /tmp/rmux-{uid}/default |
| macOS    | Unix PTY   | Unix socket | /tmp/rmux-{uid}/default |
| Windows  | ConPTY     | Named pipe  | per‑user named pipe |

## Configuration Files
- **Linux/macOS** (read in order):  
  1. `/etc/rmux.conf`  
  2. `~/.rmux.conf`  
  3. `$XDG_CONFIG_HOME/rmux/rmux.conf`  
  4. `~/.config/rmux/rmux.conf`  
- **Windows** (read in order):  
  1. `%XDG_CONFIG_HOME%\rmux\rmux.conf`  
  2. `%USERPROFILE%\.rmux.conf`  
  3. `%APPDATA%\rmux\rmux.conf`  
  4. `%RMUX_CONFIG_FILE%`  

## Verification & Quality Checks
- Formatting: `cargo fmt --all -- --check`  
- Linting: `cargo clippy --workspace --all-targets --locked -- -D warnings`  
- Tests: `cargo test --workspace --locked --no-fail-fast`  
- Additional scripts for config validation, unsafe code checks, network‑free runtime, platform neutrality, rendering budget, packaging, and release verification.  
- Upper‑level crates forbid unsafe code; unsafe is isolated to low‑level runtime crates.

## License
- Dual‑licensed under **MIT** or **Apache‑2.0** (user may choose).

## Links & Stats
- Website: **rmux.io**  
- GitHub repository: **Helvesec/rmux** (460 stars, 11 forks)  
- Topics: windows, macos, linux, agent, rust, cli, terminal, ai, powershell, tokio, multiplexer, ratatui.