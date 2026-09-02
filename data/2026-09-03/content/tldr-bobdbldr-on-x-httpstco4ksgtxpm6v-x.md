---
title: 'bobdbldr on X: "https://t.co/4KsGTXPm6v" / X'
url: https://x.com/0xBobdbldr/status/2094449688611094835
site_name: tldr
content_file: tldr-bobdbldr-on-x-httpstco4ksgtxpm6v-x
fetched_at: '2026-09-03T07:20:47.833640'
original_url: https://x.com/0xBobdbldr/status/2094449688611094835
date: '2026-09-03'
published_date: '2026-08-31T15:38:13.000Z'
description: Stani's big vision for Aave
tags:
- tldr
---

## Post

Log in
Sign up

## Post

bobdbldr
@0xBobdbldr

# Stani's big vision for Aave

Aave spent 2026 quietly assembling the four things an ultimate bank actually is: a balance sheet, a deposit franchise, an institutional credit book, and a capital policy. Each piece shipped separately, got its own news cycle, and disappeared

In this article i will dive deeper in what i think Stani and the team have in mind in terms of company structure, based on what they did so far over the last 2 years, and how that will change and reprice $Aave for me

1. V4: Restructuring the infrastructure

V4 went live on Ethereum mainnet on March 30, 2026, the first full rework of the protocol since V1, after two years of development, third-party audits, formal verification, invariant testing and a six-week public security contest

The architecture is hub-and-spoke. Hubs hold the liquidity and pokes are tailored lending markets that draw on it, with risk isolated by collateral type and borrowing environment. The point is that Aave can now open a new desk without fragmenting its deposit base, which is precisely the thing that broke every previous attempt to serve institutional and retail credit out of the same pool

At launch, dedicated spokes went live from Lido, EtherFi, Kelp, Ethena and Lombard. Supported assets included USDT and XAUt from Tether, USDC and EURC from Circle, cbBTC from Coinbase, frxUSD from Frax, and USDG from Paxos, with Chainlink as the exclusive oracle across V4 markets. A dedicated USDG hub and spoke followed on June 25. Avalanche came on July 15, a Core Hub with Main, Forex and AVAX Correlated spokes, and the first proof the architecture travels

Two details that get missed:

1- V4 runs alongside V3 : Aave Labs originally planned to push V3 users across and backed off after the DAO pushed back. No forced migration means no liquidity air pocket, which is the usual way protocol upgrades destroy their own numbers, clean road to PMF

2- aTokens stop rebasing: V4 moves to ERC-4626 share accounting, eliminating exchange rates and scaled balances. This is boring and it is the single most important line for institutional adoption, it makes positions legible to auditors, tax software, and every downstream integrator that previously had to write custom handling for Aave

2. The acquisitions: arranging the consumer layer

The app in the next section did not come from nowhere. Aave has been quietly buying the one capability a protocol team cannot hire its way into, consumer product design, and this is the part of the story that never made it into a single article

1- Los Feliz Engineering / Family (November 2023): The team behind Family, the best-designed self-custody Ethereum wallet in the market, plus the ConnectKit developer library. Founder Benji Taylor came in as SVP of Product and Design with the entire engineering team. This one compounded: the acquisition produced Family Accounts, fully white-labelled embedded wallets that now serve as the authentication and wallet infrastructure underneath the Aave App, Aave Pro and Aave Kit. Aave didn't buy a wallet. It bought the onboarding layer for every consumer product it would ship afterward

2- Stable Finance (October 2025):A San Francisco fintech whose iOS app let people deposit from a bank account, debit card or crypto and earn on stablecoins. Founder Mario Baxter Cabrera became Director of Product; the engineering team came with him, the Stable app was phased out and its technology folded into Aave Labs products. The Aave App shipped roughly three weeks later

Then, in February 2026, the cleanup: Aave Labs retired the Avara umbrella brand, wound down Family as a standalone consumer app, and handed Lens off to Mask. Everything now sits under one brand, and Family Accounts continues as infrastructure rather than a product

Read the sequence as a capital allocator would: multiple acqui-hires, each buying a capability rather than a revenue line, each brand subsequently retired once the capability was absorbed

The pieces got stripped for parts and bolted onto the core franchise. Berkshire buys businesses and leaves them alone, Aave buys teams and readjust them into the balance sheet. Different mechanism, same discipline: acquire the thing you can find better people to build, then point it at the one asset that compounds

3. The Aave App: Aave stops renting its customers

For its entire history Aave has been a protocol that other people's frontends monetized, but the Aave App ends that

It launched in early access on iOS in November 2025 and became the consumer pillar of the 2026 plan: up to 9% on deposits, $1M of balance protection, funding from a bank account, debit card or stablecoin, plus automated savings and a compounding visualizer. The pitch is aimed squarely at people who have never used a wallet. Aave's own marketing page does the comparison for you, 3.25% at Cash App, 0.38% as the FDIC national deposit rate, as of August 2026

Stani called it a trojan horse, with an initial target was a million users

The distinction from Chime, Revolut and Monzo is that those neobanks are still a UI sitting on old banking rails, paying out a fraction of what they earn on your balance. Aave's app sits directly on the largest credit book in DeFi. There is no correspondent bank in the middle taking the spread, and the yield the app pays is the same yield the protocol generates, minus far less overhead

(debatable here between the morpho angle of being the backend and supplying front ends via curators, or re building distribution from the start, each with pros and cons, but i like the boldness of aave team that want to have a defi app as first face app, which is something we need for defi consumer)

4. Stable Vaults: Aave becomes the correspondent bank

This is the piece almost nobody priced yet

In July 2026, Aave Labs opened Stable Vaults, the fixed-rate yield engine that powers its own savings app, to any business. An operator picks the supported stablecoin, the yield strategy, and the rate it promises its users. Chainlink price feeds and CCIP handle pricing and cross-chain movement. Deposits start earning on arrival

Basically their B2B answer to morpho backend thesis

The economics are the interesting part: whatever the strategy earns above the promised rate belongs to the operator. A fintech can register its own stablecoin, run a closed-loop earn product, and offer boosted rates to premium subscribers or run promotions, with no yield infrastructure of its own

Read that as a business model rather than a feature. Aave just turned every neobank, wallet, exchange and payments company into a distribution channel that pays Aave for wholesale funding. The integration cost of shipping a one-tap earn feature collapses to a single connection. Aave doesn't need to win the consumer app war if it is the balance sheet behind everyone who does

5. Horizon and GHO: the institutional book and the liability side

Horizon is Aave's permissioned RWA market, institutions borrowing stablecoins against tokenized treasuries and credit assets. It launched in August 2025, passed $50M of deposits within days, and ended the year above $570M, with a stated 2026 target of $1B and beyond via Circle, Ripple, Franklin Templeton and VanEck

The unlock behind it was regulatory: in December 2025 the SEC formally closed its four-year investigation into Aave without charges. That is what makes a Franklin Templeton conversation possible at all

GHO is the other side of the ledger, roughly $600M in circulation, generating fee income that, post-V4, has a native home in the hub structure. Every GHO minted is a liability Aave issues against its own credit book, at a spread it sets. That is not a stablecoin side project. That is deposit issuance

6- Funding abundance : End game

Past the two-year window sits the thing Kulechov actually spends his time talking about. In a February 2026 post he argued that tokenization so far has been aimed at good but not best assets, Treasuries, equities, commodities, private credit, real estate, all of them scarce, and that the real prize is abundance assets: things that get cheaper as you produce more of them

Solar first, at an estimated $15–30T of a $50T pool by 2050, then batteries, robotics for labor, vertical farming, semiconductors, 3D printing. The argument for putting them onchain is capital velocity, infrastructure capital normally locks up for decades, while a tokenized claim trades continuously, so the same dollar finances several projects over its life. A credit book's ceiling is set by the collateral available to it, and Aave's founder has decided that the constraint worth attacking is the supply of things worth lending against, not the supply of borrowers. Funding energy transitions, in his words, is the single largest opportunity in front of the protocol

https://x.com/StaniKulechov/status/2023079479493452013?s=20

The map: what Aave now covers

Now arrange all what you saw in 1 point view, and you can see that everything narrows as it rises: one liquidity base at the bottom serving progressively more specific customers above it, with the capital policy as the floor the whole structure stands on:

Liquidity maneuvering and flexibility

Front end integrations and front end app that attracts consumer LPs

Institutional integrations and institutional products that attracts serious LPs

Legal banking licenses that allow web2 tier integrations

Full pipeline that will empower new credit markets that funds abundance

Berkshire onchain?

So, where the value actually goes?

On June 27, 2026, Aave activated Aavenomics 3.0, and this is the part that converts everything above into a token argument

The old buyback was a committee mandate, $1M a week, resizable, pausable, redirectable. Aavenomics 3.0 replaced it with an immutable, non-discretionary on-chain mechanism that runs continuously unless governance votes to stop it. It sits on top of the Aave Will Win framework, passed in April 2026, under which 100% of revenue from the protocol, from GHO, and from Aave-branded products, the App, Aave Pro, Swaps flows to the DAO treasury. Aave Labs is a service provider with no claim on product revenue, and all IP, including the brand, belongs to the token

The scoreboard so far: the old discretionary program acquired more than 205,000 AAVE, about 1.28% of the 16M max supply, between April 2025 and mid-2026. The new engine has been floated at roughly 292 AAVE a day

Annualized fees run near $400M on a trailing seven-day basis, with all-time fees past $2.2B. Annualized net revenue to the DAO is closer to $134M, against $142M in 2025 and a 2026 operating budget near $190M. That gap is why the buyback budget was trimmed from ~$50M to ~$30M in March

Buyback capacity is net revenue minus opex. At the current $30M annual run-rate, Aave retires roughly 1.5–2% of supply a year. The entire question for the next two years is whether the four products above grow net revenue faster than the DAO grows its budget, because every incremental dollar above opex converts directly into retired supply, against a float of ~15.4M tokens with an FDV/market cap ratio of about 1.05x. There is nothing left to unlock. Every buy is a net retirement

so to tldr, aave now in capex spending time, and you can probably have it at cheaper price. which is why i think aave is one of the most mispriced companies in defi

3:38 PM · Aug 31, 2026
25.4K
Views
3
10
78
70