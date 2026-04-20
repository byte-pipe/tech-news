---
title: 'GitHub - yannick-cw/korb: REWE delivery CLI · GitHub'
url: https://github.com/yannick-cw/korb
site_name: hnrss
content_file: hnrss-github-yannick-cwkorb-rewe-delivery-cli-github
fetched_at: '2026-04-01T19:28:13.976014'
original_url: https://github.com/yannick-cw/korb
date: '2026-03-30'
description: REWE delivery CLI. Contribute to yannick-cw/korb development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

yannick-cw



/

korb

Public

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star196




 
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

40 Commits
40 Commits
.github/
workflows
.github/
workflows
 
 
api
api
 
 
app
app
 
 
leanKorb
leanKorb
 
 
src
src
 
 
test
test
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
fourmolu.yaml
fourmolu.yaml
 
 
korb.cabal
korb.cabal
 
 
release.sh
release.sh
 
 
View all files

## Repository files navigation

## // korb

ThekorbCLI allows using the REWE APIs programmatically to create baskets and order them for pickup to your local REWE market.

The CLI is handwritten in Haskell, but designed to be a CLI mostly used by agents to organise your REWE shopping on your behalf. All output is JSON.

korb_demo.mp4

## // My e2e flow

My current E2E flow (I use claude to run korb) is as follows:

1. Add grocery when I think of itA Siri shortcut appends items to a shared markdown file. I say"Add oat milk to the shopping list"in the kitchen and it's on the list.
2. Weekly OrderTell the agent "use korb to buy groceries, I need X,Y,Z". It begins from a default template (my usual items and quantities, created withkorb orders history) and checks the shopping list file and my input for anything extra.
3. Adjust template suggestionI tell the agent what to skip, change, or add. It searches products viakorb search/korb favorites searchand adds them withkorb basket add.
4. Review & confirmThe agent prints the full basket and a selected timeslot. After I confirm, it runskorb checkout order.
5. Clean shopping listOrdered items get ticked off in the shopping list.

In the directory that store the shopping list file I also have a claude.md explaining this process.
Themagicis the generated template of what I always order. Just tell an agent to usekorb orders historyto identify commonly ordered items.

## // Installation

### Binary (recommended)

Download the latest release fromGitHub Releases:

#
 macOS (Apple Silicon)

curl -L https://github.com/yannick-cw/korb/releases/latest/download/korb-aarch64-macos -o korb

#
 macOS (Intel)

curl -L https://github.com/yannick-cw/korb/releases/latest/download/korb-x86_64-macos -o korb

#
 Linux (x86_64)

curl -L https://github.com/yannick-cw/korb/releases/latest/download/korb-x86_64-linux -o korb

Then:

chmod +x korb
mv korb /usr/local/bin/
#
 or sudo mv on Linux

### From source

Requires GHC 9.12+ and Cabal. You also need the REWE mTLS client certificates.

git clone https://github.com/yannick-cw/korb.git

cd
 korb

#
 Extract mTLS certificates from the REWE app

#
 See: https://github.com/ByteSizedMarius/rewerse-engineering/tree/main/docs

#
 Place them at:

#
 certs/mobile-clients-api.rewe.de/private.pem

#
 certs/mobile-clients-api.rewe.de/private.key

cabal install --install-method=copy

## // Getting started

#
 1. Authenticate with your REWE account (one-time, use Chrome to get the link, firefox does not work for this)

korb login --pretty

#
 2. Find and set your pickup store - stored locally, needs to be done just once

korb store search 80336
#
 returns market identifier for zip code

korb store
set
 420240 80336

#
 3. Search for products by name or EAN barcode

korb search
"
milch
"
 --pretty
korb search
"
milch
"
 --organic --pretty
korb search
"
4305615100005
"
 --pretty
#
 search by EAN barcode

#
 Or browse your favorites

korb favorites
korb favorites search
"
avo
"

#
 4. Add items to basket

korb basket add 8-6AJQ3RLX-bd7c2a1e-f1c1-3464-8250-900b12c90f70

#
 5. Check your basket

korb basket --pretty

#
 6. Pick a timeslot and checkout

korb timeslots
#
 lists available timeslots for pickup

korb checkout create
<
TIMESLOT_ID
>

#
 create checkout - not ordered yet

korb checkout order
#
 order it with selected timeslot and payment in market

#
 7. Cancel an order if needed

korb orders
korb orders delete
<
ORDER_ID
>

## // Usage

Usage: korb COMMAND [-p|--pretty] [-v|--version]
 REWE Pickup CLI

Available options:
 -p,--pretty Pretty JSON output
 -h,--help Show this help text
 -v,--version Show version

Commands:

 korb store Show currently selected store
 korb store search <ZIP> Find pickup stores near ZIP code
 korb store set <ID> <ZIP> Set active store by market ID and ZIP

 korb search <QUERY|EAN> Search products by name or EAN barcode (use * to browse all)
 korb search <Q> --organic Filter by attribute (--organic, --regional, --vegan, --vegetarian)

 korb favorites Show all favorite products across all lists
 korb favorites search <QUERY> Filter favorites by name (case-insensitive, substring match)
 korb favorites add <LID> <PID> Add product to default favorites list (listing ID + product ID)
 korb favorites delete <ITEM_ID> Remove item from default favorites list (item ID from favorites)

 korb basket Show current basket with items, totals, and free pickup status
 korb basket add <LISTING_ID> Set item quantity by listing ID. Overwrites existing quantity.
 --qty N sets absolute quantity. Default 1. Use --qty 0 to remove.

 korb timeslots List available pickup timeslots

 korb checkout Show the checkout for current basket. Payment is always in market.
 korb checkout create <TIMESLOT_ID> Create a checkout for a given timeslot id
 korb checkout order Place the order. Timeslot must be attached first.

 korb orders Show open orders.
 korb orders history Show all orders.
 korb orders get <ORDER_ID> Get an order (with details) by id.
 korb orders delete <ORDER_ID> Cancel an order by order ID - will give 200 on successive calls.

 korb suggestion threshold <N> Suggest N items to add to reach free pickup threshold.
 Ranks by purchase frequency, excludes items already in basket.

 korb ebons List digital receipts (eBons).
 korb ebons download <EBON_ID> Download eBon PDF. --output FILE (default: ebon.pdf)

 korb login Authenticate via REWE PKCE browser flow.

All commands support --pretty for formatted JSON output.
Output is JSON for agent consumption.

## // API documentation

Reverse-engineered OpenAPI specs for the REWE mobile API:

* REWE Product & Checkout API
* REWE Account / Keycloak API

## // Platform support

Currently macOS and linux.

## // Formal verification with Lean 4

The suggestion engine (korb suggestion threshold) is re-implemented inLean 4with five mathematically proven properties: suggestions have positive frequency, are sorted descending, come from ordered and available products, exclude basket items, and respect the count limit.
A Differential Random Testing bridge in the Haskell test suite generates random inputs, runs both implementations, and asserts identical output.
If the Lean proofs compile and the DRT passes, the Haskell production code behaves like the proven spec.
Inspired by howAWS Cedarverifies their authorization engine.

I also summarised the approach in aBlog post.

Oh and yes, this is complete overkill here and just for fun.

## // Prior work & attribution

* https://github.com/ByteSizedMarius/rewerse-engineering
* https://github.com/foo-git/rewe-discounts
* https://github.com/torbenpfohl/rewe-discounts

## // Disclaimer

This project is unofficial and not affiliated with REWE. It uses reverse-engineered APIs that may change without notice. Use at your own risk.

## About

REWE delivery CLI

### Resources

 Readme



### License

 BSD-3-Clause license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

196

 stars


### Watchers

0

 watching


### Forks

2

 forks


 Report repository



## Releases8

v0.4.6

 Latest



Apr 1, 2026



+ 7 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Haskell91.0%
* Lean7.6%
* Shell1.4%
