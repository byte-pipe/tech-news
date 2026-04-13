---
title: GitHub - sterlingcrispin/nothing-ever-happens · GitHub
url: https://github.com/sterlingcrispin/nothing-ever-happens
date: 2026-04-13
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-14T06:03:50.456235
---

# GitHub - sterlingcrispin/nothing-ever-happens · GitHub

# Nothing Ever Happens Polymarket Bot – Repository Summary

## Overview
- Async Python bot designed for Polymarket “yes/no” markets that are not sports‑related.  
- Targets “No” outcomes priced below a configurable cap.  
- Intended for entertainment; provided “as is” with no warranty or liability.

## Core Components
- **bot/** – runtime code, exchange clients, dashboard, recovery logic, and the `nothing_happens` strategy.  
- **scripts/** – helper utilities for deployment, inspection, and data export.  
- **tests/** – unit and regression tests covering key functionality.  

## Runtime Behavior
- Scans standalone markets, selects qualifying “No” entries, tracks open positions, and exposes a web dashboard.  
- Persists state for live recovery when order transmission is enabled.  
- Main entry point: `python -m bot.main`.  
- Dashboard binds to `$PORT` or `DASHBOARD_PORT`.

## Safety Model
- Real order transmission activates only when **all** of the following environment variables are set:
  - `BOT_MODE=live`
  - `LIVE_TRADING_ENABLED=true`
  - `DRY_RUN=false`
- Missing any of these switches the bot to a paper (simulated) exchange client.  
- Additional required variables for live mode:
  - `PRIVATE_KEY`
  - `FUNDER_ADDRESS` (for signature types 1 and 2)
  - `DATABASE_URL`
  - `POLYGON_RPC_URL` (for proxy‑wallet approvals and redemption)

## Setup & Configuration
1. Install dependencies: `pip install -r requirements.txt`.  
2. Copy example files:  
   - `cp config.example.json config.json` (local, git‑ignored).  
   - `cp .env.example .env` (holds secrets and flags).  
3. Runtime reads non‑secret settings from `config.json` under `strategies.nothing_happens` and secrets/flags from `.env`.  
4. Alternate config path via `CONFIG_PATH=/path/to/config.json`.

## Deployment (Heroku)
- Helper scripts (`alive.sh`, `logs.sh`, `live_enabled.sh`, `live_disabled.sh`, `kill.sh`) use `HEROKU_APP_NAME` or explicit app argument.  
- Typical workflow:
  1. Set environment variables with `heroku config:set`.  
  2. Push code: `git push heroku <branch>:main`.  
  3. Scale dynos: `heroku ps:scale web=1 worker=0`.  
- Only the web dyno runs; the worker dyno exists to fail fast if started inadvertently.

## Testing
- Run all tests with `python -m pytest -q`.

## Included Helper Scripts
| Script | Purpose |
|--------|---------|
| `scripts/db_stats.py` | Show live database table counts and recent activity |
| `scripts/export_db.py` | Export live tables from `DATABASE_URL` or a Heroku app |
| `scripts/wallet_history.py` | Retrieve positions, trades, and balances for the configured wallet |
| `scripts/parse_logs.py` | Convert Heroku JSON logs to readable terminal or HTML output |

## Repository Hygiene
- Local configuration files, ledgers, exports, reports, and deployment artifacts are excluded via `.gitignore`.

## License
- CC0‑1.0 (public domain dedication).