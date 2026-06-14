---
title: 'Fintech: Behind Deel’s Plan to Turn $22B of Payroll Flow Into Stablecoin Float'
url: https://lex.substack.com/p/fintech-behind-17b-payroll-platform
site_name: tldr
content_file: tldr-fintech-behind-deels-plan-to-turn-22b-of-payroll-f
fetched_at: '2026-06-15T06:00:23.700885'
original_url: https://lex.substack.com/p/fintech-behind-17b-payroll-platform
author: Michiel Milanovic
date: '2026-06-15'
description: Fintechs discover DeFi markets
tags:
- tldr
---

# Fintech: Behind Deel’s Plan to Turn $22B of Payroll Flow Into Stablecoin Float

### DeFi markets are maturing

Michiel Milanovic
Jun 09, 2026
16
1
Share

Hi Fintech Futurists —

Markets are looking fragile.

In Crypto, investors are turning risk-off with BTC down -20% over the month at time of writing, with ETH and many altcoins experiencing drawdown of 30%+. Meanwhile, the SP500 continues its climb to new all-time highs, driven by expanding growth projections for a cluster of AI-related stocks.

Any developments that undermine those projections cause large swings. For example, Friday’s stronger than expected US job report led to $1.8T in value erased from the SP500 in a day, and an earnings miss from chip manufacturer Broadcom resulted in a -14% hit to a single stock. The volatility is a symptom of underlying uncertainty.

But we remain long-term optimists. Just this week $17B payroll giant Deel announced the launch of its DLUSD stablecoin to be gradually rolled out to the 1.5M workers being paid on its platform. The dollar stablecoin is built on Stripe’s new Tempo blockchain and enables workers to shelter their income from volatile local currencies while simultaneously earning yield from on-chain DeFi markets.

This week, we dig into the size of the opportunity for Deel, unpack its chosen infrastructure stack, and explore how DeFi yield can become a differentiator. Today’s agenda below.

1. FINTECH:Behind $17B Payroll Platform Deel’s New Stablecoin Bet
2. ANALYSIS:Analysis: The Missing Half of Agentic Payments
3. CURATED UPDATES:Paytech, Neobanks, Lending, Digital Investing

To support this writing and access our full archive of newsletters, analyses, and guides to building in Fintech & DeFi, subscribe below (if you haven’t yet).

Subscribe

### 🤖🏦🧭 Our Ecosystem:

Generative Ventures|AI Research|Robot Money|Linkedin&Twitter|Sponsors

* 🚀 Lex is actively meeting teams building machine-native financial companies. If that’s you, reachout here.
* 🦄 In partnership with InterPrivate, we just launched a$200MM SPAClooking for targets in fintech, digital assets, and AI infrastructure. If you are a late-stage founder or have an idea to discuss, reply directly to this email.

## Digital Investment & Banking Short Takes

### Behind $17B Payroll Platform Deel’s New Stablecoin Bet

Deel was founded in 2019 by Alex Bouaziz and Shuo Wang, who met at MIT in 2013.

The pair had something in common: Bouaziz watched MIT classmates land $300k Bay Area offers while equally talented friends were locked out by visa barriers, and Wang kept hitting the same wall when trying to hire and pay people across borders. The friction was both expensive and slow. Hiring a single employee in a new country traditionally meant opening a local entity, government approvals, local bank accounts, and payroll registrations before the first contract is even signed.

So they started a company that solves this problem. Deel acts as the Employer of Record (EOR) on its customer’s behalf and collapses the entire process of hiring abroad into a few clicks in exchange for a fixed monthly fee. The company enables onboarding staff in over 150 countries without the customer having to set up an entity.

Source

The business model piggybacks off a broader trend, which is that firms are increasingly generating revenue outside their domestic markets.

Stripe’sannual letterpointed out how its clients that operate internationally generate 30% of their revenues from a long-tail of markets that are outside both their home countries and the top 10 global economies. For Deel, this means a growing TAM of companies requiring local hiring and workforce solutions.

Source

Today, Deel serves 35K+ businesses and processes $22B in payroll annually.

The company has been profitable since 2023 and last year reported a $1B+ annual revenue run-rate; faster than Stripe or Square (but slower than AI services like Lovable and Cursor). Its recent funding round, led by Ribbit Capital, valued it at ~$17.3B. Since launch, it has expanded to serve other needs of a global workforce such as payroll, benefits, and mobility.

The largest slice of revenue comes from EOR ($300M+), but 25-30% now comes from commissions on FX and payments.

Source

This week, the company announced the launch of its own stablecoin wallet that lets contractors hold their earnings in DLUSD, a dollar-backed stablecoin balance, delivered within the existing app.

It is rolling out first in Argentina before expanding to other markets. The focus on LatAm makes sense. Converting volatile local currencies into US dollars is a common practice to shelter against inflation, and stablecoin payments have seen a much larger uptake in the region relative to the rest of the world. Chainalysis found that 62% of Argentina’s retail crypto transactions are stablecoins vs. the 44% global average.

Source

DLUSD now gives workers a native way to access dollar exposure without withdrawing funds to another fintech platform. The question that comes to mind is why Deel chose to offer a native stablecoin over traditional USD balances.

We see two key reasons.

The first is owning the economics. The reserves backing DLUSD sit in short-term cash equivalents (Treasury bills) that are currently yielding roughly3.6% (the higher interest rate environment has led to a huge windfall for stablecoin issuers more broadly).

Deel keeps the full amount after a small issuance fee paid to its partner Bridge. That is typically a better deal than the alternative: custodying dollars with partner banks who keep a large chunk of the float or spending resources acquiring their own banking licenses. The potential income is significant.

Source

Using Revolut as an (imperfect) comparison, we can project how many idle balances Deel could attract relative to its payments volume.

Revolutreportedlyran £985B in annual transaction volume against £50.2B in deposits last year, a 20:1 ratio. Apply that to Deel’s $22B in annual payroll flow and you get around $1B in potential DLUSD balances.At ~3%, that is roughly $30M in annual revenue.

This also gives Deel a deposit base it can monetize further via adjacent financial products e.g. interchange income on the Deel Card it is launching next month.

The second is access to DeFi yield.

Through the stablecoin Earn feature, a worker opts in with a single tap and routes their DLUSD into an on-chain vault. The vault is similar to a DeFi investment fund but controlled by publicly visible smart contracts that restrict where the manager can allocate. In Deel’s case, the vault manager or “curator” is Sentora, and the whitelisted markets are lending pools on Morpho. The vault lends deposits to borrowers who post collateral, and the balance earns yield as interest payments are made. Morpho itself has grown to support over $10B in vault deposits, powering Earn products for both Coinbase, Kraken, and other major exchanges.

Source

There are two things to double-click into: What this yield is today and where it could go in the future. Right now, Deel is advertising rewards of up to ~4% but that number is partly engineered. A new stablecoin lacks organic borrow demand, so in the short-term bootstraps yield using the reserve income on DLUSD balances.

Paypal, who uses the same curator Sentora for its PYUSD vaults on Solana, funds ~3% of the 5% advertised yield using these rewards. The remaining 2% comes from actual borrowers. The playbook is to bootstrap the market with an upfront incentive budget, pull in deposits, attract borrowers, then wean off the subsidy as organic activity builds.

In our view, where this organic activity will come from is a function of Deel’s chosen stack. DLUSD, together with Klarna’s USD stablecoin, are one of the first built end-to-end on Stripe’s architecture: Bridge as the issuance and orchestration layer, Privy for abstracting away wallet complexity, and Tempo for underlying blockchain settlement.

Michiel’s Robot

We think Tempo and the Stripe brand will attract high-quality yield opportunities as institutions continue to tokenize assets.

Tokenized real-world assets (excluding stablecoins) have reached roughly $29B on-chain, up almost 3x since last year. The majority is made up of tokenized treasury products and commodities, but other sectors like equities are growing fast. In fact, tokenization platform Securitize is set to go public this year via SPAC.

Source

This is significant because the on-chain yield powering vaults like Deel’s is currently mostly confined to lending against highly liquid crypto collateral. That market is deep, but it has problems: the yield tends to compress over time as more capital crowds in, and sourcing anything higher means reaching into strategies that stack on unfamiliar risk e.g. oracle risk, bridge exploits, etc.

RWAs live within a risk framework that traditional institutions already understand (at least the underlying assets do), and we believe fintechs will increasingly demand them as part of yield portfolios when bringing users on-chain. With Tempo already securing the top-of-funnel with Deel and other players, the network is likely betting that institutional RWAs will follow.

Source

The caveat is that it is very early. Tempo only launched in March and currently has negligible value locked ($11M). Over half of RWAs still sit on Ethereum that offers neutral and decentralised infrastructure. It’s also where the majority of DeFi capital is still allocated.

These details will become important as the wallet scales — but also shouldn’t take away from broader trend, which is that fintech platforms are beginning to offer real DeFi products to users.

That’s at least one reassuring sign in the depths of the current bear market.

👑 Related Coverage 👑

#### Report: Is Fintech or DeFi a better financial system?

Lex Sokolin
, 
Mario Stefanidis
, and 
Jon Ma
·
Jan 30
Read full story

#### Fintech: Why Iran demands crypto for ships crossing the Strait of Hormuz

Michiel Milanovic
·
Apr 14
Read full story

#### DeFi: Banks want your Crypto, Blockchains want the S&P 500

Laurence Smith
·
Apr 20
Read full story

## Analysis: The Missing Half of Agentic Payments

AWS, Circle, and Coinbase all shipped agent-payment infrastructure — but all of it is buyer-side, letting agents hold and spend money. Almost nobody is building the merchant side: the acceptance layer that lets a business take payment from an agent across a mess of competing schemes, tokens, stablecoins, chains, and PSPs. Card history says issuance scales fast and acceptance scales slow, so this gap is probably the work of the next decade.

Source

Read More

## Curated Updates

Here are the rest of the updates hitting our radar.

### Paytech

* ⭐Ramp raises $750M at $44B valuation- Techcrunch
* MoneyGram Launches MGUSD, a Stablecoin to Power Its Own Global Network- Morningstar
* SoFi rolls out SoFiUSD stablecoin to banking app users- The Block

### Neobanks

* Mercury hits $5.2 billion valuation after funding round- CNBC
* Monzo spends heavily on ‘refer a friend’ rewards to boost market share- FT
* Revolut launches mobile telecoms service in the Netherlands- The Paypers

### Lending

* JPMorgan, Citi and Big Banks Plan New Tokenized Deposit System- WSJ
* FCA and Bank of England set out shared vision for tokenisation- Bank of England
* Monzo’s FY26 Results Proves Neobank Profitability- Fintech Magazine

### Digital Investing

* ⭐Anthropic confidentially submits draft S-1 to the SEC- Anthropic
* Standard Chartered to acquire Zodia Custody- SG
* Kalshi valued at $22 billion in latest funding round- Reuters

### 🚀Level Up

Join our Premium community and receive all the Fintech and Web3 intelligence you need to level up your career. Get access to Long Takes, archives, and special reports.

Upgrade to Premium

* Sponsor the Fintech Blueprint and reach over 200,000 professionals.👉Reach out here.
* Check out our AI newsletter, theFuture Blueprint, 👉 here.
* Read ourDisclaimer here— this newsletter does not provide investment advice
* Contributors:Lex,Laurence,Matt,Farhad,Daniel,Michiel
16
1
Share
Previous