---
title: 'GitHub - warproxxx/poly_data: Polymarket Data Retriever that fetches, processes, and structures Polymarket data including markets, order events and trades. · GitHub'
url: https://github.com/warproxxx/poly_data
site_name: github
content_file: github-github-warproxxxpoly_data-polymarket-data-retrieve
fetched_at: '2026-04-21T20:02:28.644450'
original_url: https://github.com/warproxxx/poly_data
author: warproxxx
description: Polymarket Data Retriever that fetches, processes, and structures Polymarket data including markets, order events and trades. - warproxxx/poly_data
---

warproxxx

 

/

poly_data

Public

* NotificationsYou must be signed in to change notification settings
* Fork306
* Star1.4k

 
 
 
 
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

24 Commits
24 Commits
backtrader_plotting
backtrader_plotting
 
 
poly_utils
poly_utils
 
 
update_utils
update_utils
 
 
.DS_Store
.DS_Store
 
 
.gitignore
.gitignore
 
 
Example 1 Trader Analysis.ipynb
Example 1 Trader Analysis.ipynb
 
 
Example 2 Backtest.ipynb
Example 2 Backtest.ipynb
 
 
Isolated.ipynb
Isolated.ipynb
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
parallel_sync.py
parallel_sync.py
 
 
pyproject.toml
pyproject.toml
 
 
update_all.py
update_all.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Polymarket Data

A comprehensive data pipeline for fetching, processing, and analyzing Polymarket trading data. This system collects market information, order-filled events, and processes them into structured trade data.

## Quick Download

First-time users: Download thelatest data snapshot(Credits to@PendulumFlowfor fixing some missing points in the data and sending it over) and extract it in the main repository directory before your first run(backup if this doesn't work). This will save you over 2 days of initial data collection time.

## Overview

This pipeline performs three main operations:

1. Market Data Collection- Fetches all Polymarket markets with metadata
2. Order Event Scraping- Collects order-filled events from Goldsky subgraph
3. Trade Processing- Transforms raw order events into structured trade data

## Installation

This project usesUVfor fast, reliable package management.

### Install UV

#
 macOS/Linux

curl -LsSf https://astral.sh/uv/install.sh 
|
 sh

#
 Windows

powershell -c 
"
irm https://astral.sh/uv/install.ps1 | iex
"

#
 Or with pip

pip install uv

### Install Dependencies

#
 Install all dependencies

uv sync

#
 Install with development dependencies (Jupyter, etc.)

uv sync --extra dev

## Quick Start

#
 Run with UV (recommended)

uv run python update_all.py

#
 Or activate the virtual environment first

source
 .venv/bin/activate 
#
 On Windows: .venv\Scripts\activate

python update_all.py

This will sequentially run all three pipeline stages:

* Update markets from Polymarket API
* Update order-filled events from Goldsky
* Process new orders into trades

## Project Structure

poly_data/
├── update_all.py # Main orchestrator script
├── update_utils/ # Data collection modules
│ ├── update_markets.py # Fetch markets from Polymarket API
│ ├── update_goldsky.py # Scrape order events from Goldsky
│ └── process_live.py # Process orders into trades
├── poly_utils/ # Utility functions
│ └── utils.py # Market loading and missing token handling
├── markets.csv # Main markets dataset
├── missing_markets.csv # Markets discovered from trades (auto-generated)
├── goldsky/ # Order-filled events (auto-generated)
│ └── orderFilled.csv
└── processed/ # Processed trade data (auto-generated)
 └── trades.csv

## Data Files

### markets.csv

Market metadata including:

* Market question, outcomes, and tokens
* Creation/close times and slugs
* Trading volume and condition IDs
* Negative risk indicators

Fields:createdAt,id,question,answer1,answer2,neg_risk,market_slug,token1,token2,condition_id,volume,ticker,closedTime

### goldsky/orderFilled.csv

Raw order-filled events with:

* Maker/taker addresses and asset IDs
* Fill amounts and transaction hashes
* Unix timestamps

Fields:timestamp,maker,makerAssetId,makerAmountFilled,taker,takerAssetId,takerAmountFilled,transactionHash

### processed/trades.csv

Structured trade data including:

* Market ID mapping and trade direction
* Price, USD amount, and token amount
* Maker/taker roles and transaction details

Fields:timestamp,market_id,maker,taker,nonusdc_side,maker_direction,taker_direction,price,usd_amount,token_amount,transactionHash

## Pipeline Stages

### 1. Update Markets (update_markets.py)

Fetches all markets from Polymarket API in chronological order.

Features:

* Automatic resume from last offset (idempotent)
* Rate limiting and error handling
* Batch fetching (500 markets per request)

Usage:

uv run python -c 
"
from update_utils.update_markets import update_markets; update_markets()
"

### 2. Update Goldsky (update_goldsky.py)

Scrapes order-filled events from Goldsky subgraph API.

Features:

* Resumes from last timestamp automatically
* Handles GraphQL queries with pagination
* Deduplicates events

Usage:

uv run python -c 
"
from update_utils.update_goldsky import update_goldsky; update_goldsky()
"

### 3. Process Live Trades (process_live.py)

Processes raw order events into structured trades.

Features:

* Maps asset IDs to markets using token lookup
* Calculates prices and trade directions
* Identifies BUY/SELL sides
* Handles missing markets by discovering them from trades
* Incremental processing from last checkpoint

Usage:

uv run python -c 
"
from update_utils.process_live import process_live; process_live()
"

Processing Logic:

* Identifies non-USDC asset in each trade
* Maps to market and outcome token (token1/token2)
* Determines maker/taker directions (BUY/SELL)
* Calculates price as USDC amount per outcome token
* Converts amounts from raw units (divides by 10^6)

## Dependencies

Dependencies are managed viapyproject.tomland installed automatically withuv sync.

Key Libraries:

* polars- Fast DataFrame operations
* pandas- Data manipulation
* gql- GraphQL client for Goldsky
* requests- HTTP requests to Polymarket API
* flatten-json- JSON flattening for nested responses

Development Dependencies(optional, installed with--extra dev):

* jupyter- Interactive notebooks
* notebook- Jupyter notebook interface
* ipykernel- Python kernel for Jupyter

## Features

### Resumable Operations

All stages automatically resume from where they left off:

* Markets: Counts existing CSV rows to set offset
* Goldsky: Reads last timestamp from orderFilled.csv
* Processing: Finds last processed transaction hash

### Error Handling

* Automatic retries on network failures
* Rate limit detection and backoff
* Server error (500) handling
* Graceful fallbacks for missing data

### Missing Market Discovery

The processing stage automatically discovers markets that weren't in the initial markets.csv (e.g., markets created after last update) and fetches them via the Polymarket API, saving tomissing_markets.csv.

## Data Schema Details

### Trade Direction Logic

* Taker Direction: BUY if paying USDC, SELL if receiving USDC
* Maker Direction: Opposite of taker direction
* Price: Always expressed as USDC per outcome token

### Asset Mapping

* makerAssetId/takerAssetIdof "0" represents USDC
* Non-zero IDs are outcome token IDs (token1/token2 from markets)
* Each trade involves USDC and one outcome token

## Notes

* All amounts are normalized to standard decimal format (divided by 10^6)
* Timestamps are converted from Unix epoch to datetime
* Platform wallets (0xc5d563a36ae78145c45a50134d48a1215220f80a,0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e) are tracked inpoly_utils/utils.py
* Negative risk markets are flagged in the market data

## Troubleshooting

Issue: Markets not found during processingSolution: Runupdate_markets()first, or letprocess_live()auto-discover them

Issue: Duplicate tradesSolution: Deduplication is automatic - re-run processing from scratch if needed

Issue: Rate limitingSolution: The pipeline handles this automatically with exponential backoff

## Analysis

### Loading Data

import
 
pandas
 
as
 
pd

import
 
polars
 
as
 
pl

from
 
poly_utils
 
import
 
get_markets
, 
PLATFORM_WALLETS

# Load markets

markets_df
 
=
 
get_markets
()

# Load trades

df
 
=
 
pl
.
scan_csv
(
"processed/trades.csv"
).
collect
(
streaming
=
True
)

df
 
=
 
df
.
with_columns
(
 
pl
.
col
(
"timestamp"
).
str
.
to_datetime
().
alias
(
"timestamp"
)
)

### Filtering Trades by User

Important: When filtering for a specific user's trades, filter by themakercolumn. Even though it appears you're only getting trades where the user is the maker, this is how Polymarket generates events at the contract level. Themakercolumn shows trades from that user's perspective including price.

USERS
 
=
 {
 
'domah'
: 
'0x9d84ce0306f8551e02efef1680475fc0f1dc1344'
,
 
'50pence'
: 
'0x3cf3e8d5427aed066a7a5926980600f6c3cf87b3'
,
 
'fhantom'
: 
'0x6356fb47642a028bc09df92023c35a21a0b41885'
,
 
'car'
: 
'0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b'
,
 
'theo4'
: 
'0x56687bf447db6ffa42ffe2204a05edaa20f55839'

}

# Get all trades for a specific user

trader_df
 
=
 
df
.
filter
((
pl
.
col
(
"maker"
) 
==
 
USERS
[
'domah'
]))

## License

Go wild with it

## About

Polymarket Data Retriever that fetches, processes, and structures Polymarket data including markets, order events and trades.

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.4k

 stars
 

### Watchers

17

 watching
 

### Forks

306

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python50.4%
* Jupyter Notebook48.6%
* Jinja1.0%