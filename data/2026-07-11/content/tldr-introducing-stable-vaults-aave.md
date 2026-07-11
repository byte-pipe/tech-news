---
title: Introducing Stable Vaults | Aave
url: https://aave.com/blog/introducing-stable-vaults
site_name: tldr
content_file: tldr-introducing-stable-vaults-aave
fetched_at: '2026-07-11T11:24:46.606994'
original_url: https://aave.com/blog/introducing-stable-vaults
date: '2026-07-11'
description: An all-in-one way for any business to embed fixed-rate stablecoin yield into its product without building yield infrastructure from scratch.
tags:
- tldr
---

## Back to BlogIntroducing Stable Vaults

Aave Labs

Product

Today Aave Labs is introducing Stable Vaults, an all-in-one way to embed fixed-rate stablecoin yield into any product. Stable Vaults are the smart contract vaults that already power the Aave mobile savings app, and they are now available for any business to build on.

Integrating DeFi yield into a consumer product has always meant managing volatile rates, multi-chain liquidity, and a heavy layer of infrastructure between an onchain yield strategy and the end user. After years of working on this problem at Aave Labs, we built Stable Vaults to solve it.

Stable Vaults convert variable onchain lending rates into a fixed rate a business can offer its users, and they make it easy to manage the rebalancing, the cross-chain operations, and the rate paid to users.

Any business can now integrate Aave-powered yield, or any ERC-4626 vault strategy it chooses, into its product without building yield infrastructure from scratch.

## What Businesses Can Build

Stable Vaults give any business a ready-made backend for onchain stablecoin yield. The business chooses which stablecoins to accept, which yield strategies to use, and what fixed rate to offer each user. Examples of what can be built include:

* A neobank embedding fixed-rate savings, powered by Aave markets, directly into its app.
* A payments company letting merchants earn on idle settlement balances using a Veda vault between payouts.
* A wallet provider or exchange adding a one-tap earn feature backed by Savings GHO, without building or managing yield infrastructure.
* A fintech issuing its own stablecoin registering it as a supported deposit asset, creating a closed-loop earn product for its existing users with a custom ERC-4626 yield strategy vault.

Businesses can also reward target user groups, such as premium subscribers, with higher rates, or run temporary promotions that boost a user's rate. Anything the underlying strategies earn above those commitments belongs to the operator as revenue. Because the operator controls which assets and strategies the vault uses, each deployment can be tailored to a specific product, jurisdiction, or risk profile.

## Why Stable Vaults?

Stable Vaults solve a variety of engineering challenges at once including volatile rates, fragmented cross-chain liquidity, and operations between an onchain strategy and an end user.

The Stable Vault stack also makes life easier for users when integrated. User deposits start earning yield the moment they’re received, and they can deposit or withdraw from any chain the operator supports, in whichever stablecoins the operator integrates. ChainlinkPrice FeedsandCCIPcan power any Stable Vaults deployment, providing reliable pricing data and secure cross-chain bridging. The Aave App will use both in its production deployment.

Stable Vaults are a production system, already running in the Aave App, now open for any business to build on.

## Get Started

Read the documentation, explore the codebase, or reach out to the Aave Labs team:

* Stable Vault landing page
* Documentation
* Codebase
* Audits
Need
 
help
 
or
 
want
 
to
 
learn
 
more?

Share your questions or feedback and we'll get back to you.

Name
 
*
Email
 
*
Your message
 
*
Send Message