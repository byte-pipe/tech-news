---
title: GitHub - sterlingcrispin/nothing-ever-happens · GitHub
url: https://github.com/sterlingcrispin/nothing-ever-happens
site_name: hnrss
content_file: hnrss-github-sterlingcrispinnothing-ever-happens-github
fetched_at: '2026-04-13T20:05:38.448492'
original_url: https://github.com/sterlingcrispin/nothing-ever-happens
date: '2026-04-13'
description: Contribute to sterlingcrispin/nothing-ever-happens development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

sterlingcrispin



/

nothing-ever-happens

Public

* NotificationsYou must be signed in to change notification settings
* Fork38
* Star385




 
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

1 Commit
1 Commit
bot
bot
 
 
docs
docs
 
 
scripts
scripts
 
 
tests
tests
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
LICENSE
LICENSE
 
 
Procfile
Procfile
 
 
README.md
README.md
 
 
alive.sh
alive.sh
 
 
config.example.json
config.example.json
 
 
kill.sh
kill.sh
 
 
live_disabled.sh
live_disabled.sh
 
 
live_enabled.sh
live_enabled.sh
 
 
logs.sh
logs.sh
 
 
logshtml.sh
logshtml.sh
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# Nothing Ever Happens Polymarket Bot

Focused async Python bot for Polymarket that buys No on standalone non-sports yes/no markets.

FOR ENTERTAINMENT ONLY. PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USE AT YOUR OWN RISK. THE AUTHORS ARE NOT LIABLE FOR ANY CLAIMS, LOSSES, OR DAMAGES.

* bot/: runtime, exchange clients, dashboard, recovery, and thenothing_happensstrategy
* scripts/: operational helpers for deployed instances and local inspection
* tests/: focused unit and regression coverage

## Runtime

The bot scans standalone markets, looks for NO entries below a configured price cap, tracks open positions, exposes a dashboard, and persists live recovery state when order transmission is enabled.

The runtime isnothing_happens.

## Safety Model

Real order transmission requires all three environment variables:

* BOT_MODE=live
* LIVE_TRADING_ENABLED=true
* DRY_RUN=false

If any of those are missing, the bot usesPaperExchangeClient.

Additional live-mode requirements:

* PRIVATE_KEY
* FUNDER_ADDRESSfor signature types1and2
* DATABASE_URL
* POLYGON_RPC_URLfor proxy-wallet approvals and redemption

## Setup

pip install -r requirements.txt
cp config.example.json config.json
cp .env.example .env

config.jsonis intentionally local and ignored by git.

## Configuration

The runtime reads:

* config.jsonfor non-secret runtime settings
* .envfor secrets and runtime flags

The runtime config lives understrategies.nothing_happens. Seeconfig.example.jsonand.env.example.

You can point the runtime at a different config file withCONFIG_PATH=/path/to/config.json.

## Running Locally

python -m bot.main

The dashboard binds$PORTorDASHBOARD_PORTwhen one is set.

## Heroku Workflow

The shell helpers use either an explicit app name argument orHEROKU_APP_NAME.

export
 HEROKU_APP_NAME=
<
your-app
>

./alive.sh
./logs.sh
./live_enabled.sh
./live_disabled.sh
./kill.sh

Generic deployment flow:

heroku config:set BOT_MODE=live DRY_RUN=false LIVE_TRADING_ENABLED=true -a
"
$HEROKU_APP_NAME
"

heroku config:set PRIVATE_KEY=
<
key
>
 FUNDER_ADDRESS=
<
addr
>
 POLYGON_RPC_URL=
<
url
>
 DATABASE_URL=
<
url
>
 -a
"
$HEROKU_APP_NAME
"

git push heroku
<
branch
>
:main
heroku ps:scale web=1 worker=0 -a
"
$HEROKU_APP_NAME
"

Only run thewebdyno. Theworkerentry exists only to fail fast if it is started accidentally.

## Tests

python -m pytest -q

## Included Scripts

Script

Purpose

scripts/db_stats.py

Inspect live database table counts and recent activity

scripts/export_db.py

Export live tables from
DATABASE_URL
 or a Heroku app

scripts/wallet_history.py

Pull positions, trades, and balances for the configured wallet

scripts/parse_logs.py

Convert Heroku JSON logs into readable terminal or HTML output

## Repository Hygiene

Local config, ledgers, exports, reports, and deployment artifacts are ignored by default.

## About

 No description, website, or topics provided.


### Resources

 Readme



### License

 CC0-1.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

385

 stars


### Watchers

0

 watching


### Forks

38

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors1

* sterlingcrispinSterling Crispin

## Languages

* Python94.7%
* HTML4.7%
* Other0.6%
