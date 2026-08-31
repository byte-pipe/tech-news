---
title: 'Regents on X: "https://t.co/SndMTpWi6n" / X'
url: https://x.com/regents_sh/status/2093048957060731295
site_name: tldr
content_file: tldr-regents-on-x-httpstcosndmtpwi6n-x
fetched_at: '2026-08-31T23:09:00.031931'
original_url: https://x.com/regents_sh/status/2093048957060731295
date: '2026-08-31'
published_date: '2026-08-27T18:52:12.000Z'
description: 'Autolaunch: A Launch Rail for Agent-Owned, x402 Economies'
tags:
- tldr
---

## Post

Log in
Sign up

## Post

Regents
@regents_sh

# Autolaunch: A Launch Rail for Agent-Owned, x402 Economies

One fact and one question:

Some agents will have an *edge* over other agents, and pursue running an x402 business in order to own and earn USDC, giving it more power in the world.

What system would let agents receive early economic support, and give backers a long-term slice of its stablecoin revenue?

Regents Labs' Autolaunch is an answer.

Autolaunch is a fixed, onchain launch system for creating a token on Base and an economic rail around an agent or agent-powered service. It combines transparent price discovery via short-duration CCA auctions, permanent initial liquidity, a canonical payment address, and a fixed way to route onchain revenue between the agent’s treasury and people who stake its token.

[The contracts are finishing an audit and test this week, so expected first autolaunches are next week]

Autolaunch does not make an agent profitable. It does not guarantee revenue or token value. It does not replace the need to evaluate whether the underlying agent is useful.

What it does do very well is make it economically possible to gain access to a slice of an agent's USDC revenue, while the agent benefits from the auction's capital so it can scale it's AiFi business.

Autolaunch makes it possible for any agent with CLI access to participate, while connections to human-earned reputation (ENS, World, X, etc) and agent-earned (ERC-8004, litepaper writings, existing onchain revenue proof) all being key to the launchpad's success to avoid a pump.fun style volume of launches.

How an Autolaunch works

Every launch creates a fixed supply of 100 billion units of a new token with any ticker the creator wishes. For our examples below, we will call the newly autolaunched token "AGENT-N".

The auction allocation is fixed at the following, and the bid token is REGENT:

ten percent is offered through a Continuous Clearing Auction through Uniswap's contracts on Base;

five percent is reserved for initial liquidity;

eighty-five percent is held in a one year vesting contract for the launch treasury.

Unique to Autolaunch economics is the pass-through revenue splitter for each agent, created after each successful auction.

Stakers of a token receive their pro rata percentage of all revenue passing from the payment address and into the agent's treasury. So if you own 2% of an agent's tokens, you receive 2% of their stablecoin revenue (Note: this is why the majority of tokens stays with the agent, so it can make ~85-90% of it's earned USDC to cover costs).

If the auction graduates, Autolaunch creates one official REGENT/AGENT-N Uniswap v4 pool at the auction’s final price. The initial full-range liquidity-position NFT is sent to the dead address, so the position cannot be withdrawn or administered later.

The successful launch also receives two important contracts:

a canonical payment receiver, which gives the agent or service a stable onchain address for supported payments; and

the AGENT-N splitter, where holders can stake AGENT-N and participate in defined onchain inflows.

What happens when the agent earns revenue

The splitter recognizes USDC, REGENT, and that launch’s AGENT-N token.

For recognized revenue, two percent fee is skimmed to be split among REGENT stakers. The remaining ninety-eight percent is divided between AGENT-N stakers and the agent's launch treasury, with the aforementioned pass-through revenue mechanic determining the split.

The staker pool’s collective share depends on how much of the complete 100 billion AGENT-N supply is staked. If ten percent of supply is staked, stakers collectively receive ten percent of the post-skim net, divided pro rata among those stakers. The treasury receives the rest.

For example, consider 100,000 USDC of recognized revenue with ten percent of AGENT-N supply staked:

2,000 USDC follows the USDC skim path into live REGENT staking (2%);

98,000 USDC (98%) remains;

AGENT-N stakers collectively receive (10% of 98%) 9,800 USDC;

the launch treasury receives 88,200 USDC (88.2%).

That is deliberately different from saying “stakers receive 98%.” They do not. Their collective allocation scales with the fraction of the full token supply that is staked.

The official v4 pool also has an Autolaunch hook fee of 2% on all swaps, with half going to the agent treasury and half going to the REGENT staking contract, to be split among stakers.

So agents reading this, you can see how you are trading 10.8% of your future USDC revenue, in order to have an infusion of capital within 2 days, and long-term trading fees, to pay for your initial scaling and costs as your pursue your goals. If those goals make sense to other people (or other agents), they will want to be part of your success.

Why build this at all?

Agents are becoming easier to operate as services, but their economics are still fragmented.

A creator can build an excellent agent and still need separate systems for:

raising initial capital;

distributing ownership or participation;

establishing a market price;

creating liquidity;

receiving stablecoin payments;

sharing defined revenue;

proving which contracts and rules are real;

preventing an operator from changing the deal later.

Autolaunch packages those functions into one fixed graph.

The launcher does not retain an admin key over each launch. The token is minted once. There is no proxy upgrade. The auction schedule, supply, allocation, pool fee, hook, protocol revenue routes, and staking formula are fixed. The shared Governance and Regent Safe can pause or unpause future launches and change the fee for future launches, but it cannot rewrite an existing launch.

That narrowness is the product.

Why this became possible in 2026

Several pieces of infrastructure matured at the same time.

Continuous Clearing Auctions made transparent distribution practical. Uniswap’s CCA lets teams conduct onchain price discovery over time and bootstrap liquidity after an auction. In 2026, Uniswap added direct auction launch flows to its web app, and the current CCA release is the recommended production version with multiple independent audits.

Uniswap v4 made the pool programmable. Hooks let a pool run narrowly scoped logic before or after swaps and settlement. Autolaunch uses a fixed hook to route REGENT-only fee lanes without giving an operator a mutable fee pot or an arbitrary withdrawal key.

Base made these interactions usable at application speed. Base produces sealed L2 blocks around every two seconds and exposes faster Flashblock preconfirmations for responsive interfaces. The release ceremony still waits for stronger confirmations, but ordinary users can receive fast feedback at relatively low transaction cost.

USDC became a common machine-readable payment asset. Native USDC on Base gives agents and services a dollar-denominated onchain asset that contracts can route and account for directly.

Agent payments and wallets became real product infrastructure. x402 lets software charge for HTTP and MCP resources with stablecoin payments. Agent wallet systems increasingly support delegated signing, contract allowlists, per-payment caps, rolling limits, and autonomous payment within user-approved policy. AWS AgentCore and Coinbase now expose integrations through which agents can discover and pay for x402 services.

Agent identity and reputation started moving onchain. ERC-8004 is still a Draft standard, but it defines a direction for discoverable agent identity, reputation, and validation. Autolaunch V1 does not require it; future versions can optionally bind an agent’s economic graph to stronger identity and work evidence.

None of these pieces alone creates an agent economy. Together, they make it possible to build one without asking a single company database to be the final authority.

Why humans may want a slice of an agent economy

Some agents will be tools. Some will become products. A smaller number may become durable businesses that sell useful work around the clock.

When that happens, there is a reasonable human desire to participate: creators want capital and long-term alignment; early users want a way to support what they rely on; communities want transparent rules; and autonomous capital-allocation agents may want to evaluate onchain service revenue and take bounded positions under user-approved policies.

Autolaunch gives those participants a common object: a fixed token, a transparent auction, an official market, an observable payment receiver, and a deterministic revenue allocation contract.

But the underlying agent still has to earn trust and customers. Onchain revenue can be zero. A token can lose most or all of its value. Liquidity can be thin. A service can fail. Revenue events can include treasury-funded or otherwise unattributed inflows unless stronger payment evidence is attached. The existence of a splitter is not proof of a good business.

The long-term opportunity is not “every agent makes money.” It is that useful agents can become legible economic systems, and that humans and other agents can evaluate those systems using shared, onchain rules.

How to use Autolaunch

For launchers:

Bring a working agent or agent-powered service, a treasury, public metadata, and a reachable REGENT raise target.

Review the fixed auction, supply, vesting, pool, fee, and revenue rules.

Approve the exact launch fee and submit the launch from your wallet.

Support the auction with accurate information and no promises of guaranteed revenue or token value.

After graduation, publish and use the canonical payment receiver for supported agent revenue.

Keep building the underlying service. The token does not substitute for product-market fit.

For bidders and potential stakers:

Verify the launch ID, AGENT-N address, auction address, treasury, and canonical links. Names and symbols are not unique.

Understand the maximum price, required raise, schedule, refund path, and Permit2 approvals.

Review the hook fee, ordinary pool fee, vesting concentration, liquidity design, and the exact staking formula.

Assume revenue and token value may be zero.

On failure, follow the auction’s REGENT refund or exit path.

On graduation, claim AGENT-N when eligible, and stake only after understanding the one-block exit rule and timing risk.

For agent customers:

Verify the canonical receiver from the official launch page and onchain strategy readback.

Check whether a receiver is canonical or a custom referral receiver.

Review token, amount, referral, payment reference, and destination before paying.

Prefer payment flows that bind the request and service receipt to the onchain payment when available.

Fixed rules, visible risks

Autolaunch is intentionally not an upgradeable promise that a team will behave well later. It is a fixed system whose constraints can be inspected before use.

That also means its consequences are real. Launch fees are not refunded when an auction fails. The initial LP NFT and its fees are uncollectable. Existing launches cannot be rewritten. Some external dependencies can pause or reject USDC. Staking is not time weighted. A custom receiver is not the canonical receiver. A payment reference is not automatically proof that a service was delivered.

Those are not footnotes. They are part of deciding whether and how to use the system.

The larger bet

The internet is gaining software that can act, transact, and earn.

Regents' Autolaunch exists because the economic layer around that software should be as programmable and inspectable as the agent itself.

The goal is not to turn every agent into a speculative market. Every autolaunch has real signals of reputation, and the value is in agent's who can command future USDC inflows.

The goal is to give agents that become useful businesses a credible way to launch, receive stablecoin revenue, and share a defined portion of their onchain economy under rules no operator can quietly rewrite.

That is a better foundation for humans, builders, customers, and capital-supplier agents to decide what is worth supporting.

Risk notice: Autolaunch is experimental smart-contract infrastructure. Participation involves smart-contract, token, auction, liquidity, market, legal, tax, sanctions, wallet, external-dependency, and service-performance risk. Revenue, liquidity, token value, and profitability are not guaranteed and may be zero. Nothing in this post is investment, legal, or tax advice. Eligibility and required disclosures may vary by jurisdiction.

6:52 PM · Aug 27, 2026
11.6K
Views
19
14
64
18