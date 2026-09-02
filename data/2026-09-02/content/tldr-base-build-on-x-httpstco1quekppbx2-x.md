---
title: 'Base Build on X: "https://t.co/1QuEkPPBX2" / X'
url: https://x.com/buildonbase/status/2092990360477737128
site_name: tldr
content_file: tldr-base-build-on-x-httpstco1quekppbx2-x
fetched_at: '2026-09-02T14:59:03.784846'
original_url: https://x.com/buildonbase/status/2092990360477737128
date: '2026-09-02'
published_date: '2026-08-27T14:59:22.000Z'
description: 'B20: The Standard Behind Tokenized Stocks on Base'
tags:
- tldr
---

## Post

Log in
Sign up

## Post

Base Build
@buildonbase

# B20: The Standard Behind Tokenized Stocks on Base

Tokenized stocks are live on Base. See our launch post for more information.

Coinbase Tokenized Stocks bring real securities onchain. Each one is fully backed by real US company shares held with a regulated custodian.

Coinbase Tokenized Stocks are only available to persons in eligible jurisdictions outside of the U.S.

Coinbase Tokenized Stocks are built on B20, a Base-native token standard designed for secure, compliant, and frictionless asset issuance. Modular compliance controls enabled Tokenized Stocks to add “freeze and seize” functionality to fulfill legal requirements. A multiplier enables supporting corporate actions like stock splits and dividends while streamlining tax consequences of transacting in DeFi. Announcements and extra metadata enabled clear metadata references for stock holders to understand our assets and their management history.

Why real world assets need a purpose-built standard

Many real-world assets are dynamic: they can pay out yields, undergo reference-asset changes, and can carry eligibility rules. Base created B20 to handle all three natively. Tokenized stocks are one example - they undergo corporate actions and carry jurisdictional eligibility rules - but the same mechanics can support other RWA use cases.

Stocks illustrate the pattern; B20’s mechanics apply to any asset with similar characteristics:

Corporate actions

When the underlying stock pays a dividend or splits, B20 adjusts a single number: the multiplier.

The multiplier records how many real shares each B20 token can be redeemed for. Tokens launch with a multiplier of 1.00. Cash dividends are reinvested into additional shares, raising the multiplier by the amount received, net of dividend withholding tax and a Coinbase fee. For example, a dividend that nets 2% after those deductions raises the multiplier to ~1.02. A 2-for-1 split doubles the multiplier from 1.02 to 2.04. Today, holders receive dividends through a higher multiplier rather than additional B20 tokens.

Consider a tokenized stock trading in an AMM pool when the company runs a 10-for-1 split. A token that applied the split by rewriting balances would silently change the pool's reserves, break its pricing invariant, and force every venue to migrate liquidity on the issuer's schedule. Because B20 updates the multiplier instead, the pool's ERC-20 balances never change: liquidity stays put and the pool works as normal.

As a result, a B20 tokenized stock does not permanently equal one share, so anything converting between tokens and shares must account for the current multiplier either by reading multiplier() directly, or by utilizing the built-in helpers (toScaledBalance, toRawBalance, scaledBalanceOf). Support for ERC-8056 is coming with the future Cobalt upgrade, which will expose the same values through the standard interface.

One B20 token does not permanently equal one share. Always read the current multiplier when converting between tokens and shares.

Compliance and transfer controls

Certain assets have to honor regulatory requirements at the token level; B20 supports this natively. Where an asset requires it, such as jurisdictional eligibility or sanctions screening, a transfer policy can block a transfer. Policies live in a shared Policy Registry: a policy is defined once (eg, a sanctions blocklist), and can be referenced by ID across many tokens. A single membership update propagates to every asset that points at it, which lets one issuer run many assets off a common compliance surface.

For Coinbase Tokenized Stocks on Base, minting and redeeming against the underlying shares remains restricted to KYC-onboarded Authorized Participants (APs). B20 provides token-level pause switches; some operational controls sit above the token and are not enforced by B20, eg, AP mint and redeem availability and price-feed behavior outside US market hours.Policy and pause interfaces are detailed within the developer docs.

For builders

A tokenized stock moves like any ERC-20, so existing wallets, routers, and pools handle it as-is (identify a token by its verified contract address, not its ticker). Coinbase Tokenized Stocks on Base pair each token with a Chainlink total-return feed that already bakes in the multiplier, so it reflects splits and dividends directly. The only real additions are reading a position's value from the total-return feed and refreshing it when the multiplier changes. ERC-8056 support arrives with the future Cobalt upgrade, after which the same reads work through the standard interface.

To go deeper, see the B20 spec, the interfaces in base/base-std, Chainlink's AggregatorV3Interface, and the verified asset list at base.org/stocks.

Disclaimer: Coinbase tokenized stocks are only available to persons in eligible jurisdictions outside of the U.S.

Inclusion of any third-party protocol or venue is for developer reference only and is not an endorsement, partnership, or warranty. Confirm addresses, feeds, and the token list against official sources before integrating.

Base is open-source, permissionless blockchain infrastructure. Each B20 token is deployed and configured by its issuer, who sets and controls all token parameters and administrative permissions; Base does not configure, administer, or control tokens deployed on the protocol.

2:59 PM · Aug 27, 2026
50K
Views
38
51
204
45