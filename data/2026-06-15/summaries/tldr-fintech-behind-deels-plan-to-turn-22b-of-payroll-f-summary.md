---
title: Fintech: Behind Deel’s Plan to Turn $22B of Payroll Flow Into Stablecoin Float
url: https://lex.substack.com/p/fintech-behind-17b-payroll-platform
date: 2026-06-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-15T06:01:46.232112
---

# Fintech: Behind Deel’s Plan to Turn $22B of Payroll Flow Into Stablecoin Float

# Fintech: Behind Deel’s Plan to Turn $22B of Payroll Flow Into Stablecoin Float

## Overview
- Crypto markets are volatile, while traditional equities climb, creating uncertainty.
- Deel, a $17 B payroll platform, is launching its own dollar‑stablecoin (DLUSD) on Stripe’s Tempo blockchain.
- The stablecoin lets contractors hold earnings in a low‑volatility asset and earn on‑chain DeFi yield.

## Deel’s Business Model
- Founded in 2019 by Alex Bouaziz and Shuo Wang to simplify cross‑border hiring.
- Acts as Employer of Record, enabling onboarding in 150+ countries with a fixed monthly fee.
- Serves 35 K+ businesses, processes $22 B in payroll annually, and reported >$1 B annual revenue run‑rate in 2023.
- Revenue mix: $300 M+ from EOR services; 25‑30 % from FX and payment commissions.

## Why a Native Stablecoin?
1. **Economic Ownership**
   - DLUSD reserves are held in short‑term Treasury bills yielding ~3.6 %.
   - Deel retains most of the issuance fee after paying Bridge, avoiding bank custody fees or the cost of obtaining banking licenses.
   - Potential idle balance: applying Revolut’s 20:1 transaction‑to‑deposit ratio to Deel’s $22 B payroll flow suggests ~ $1 B could sit as DLUSD, generating ~ $30 M annual revenue at 3 % yield.
2. **Access to DeFi Yield**
   - Workers can opt‑in to “Earn” by routing DLUSD into a curated on‑chain vault.
   - Vault manager (Sentora) allocates funds to lending pools on Morpho, which currently supports >$10 B in deposits.
   - Advertised rewards are up to ~4 %; part of this is bootstrapped by reserve income, with the remainder coming from actual borrower interest.

## DeFi Yield Mechanics
- **Bootstrapping Phase:** New stablecoin lacks organic borrowing demand; Deel subsidizes yield using reserve returns.
- **Transition Phase:** As deposits grow, borrower demand increases, allowing the subsidy to be reduced.
- **Comparison:** PayPal’s PYUSD vault on Solana uses the same curator (Sentora) and funds ~3 % of its 5 % advertised yield via subsidies.

## Infrastructure Stack
- **Bridge:** Issuance and orchestration layer.
- **Privy:** Abstracts wallet complexity for end users.
- **Tempo (Stripe):** Underlying blockchain settlement layer.
- DLUSD and Klarna’s USD stablecoin are among the first stablecoins built end‑to‑end on this stack.

## Market Focus
- Initial rollout in Argentina, where stablecoins account for 62 % of retail crypto transactions (vs. 44 % global average).
- Provides a native dollar exposure for workers in inflation‑prone economies without requiring external fintech platforms.

## Strategic Implications
- Creates a deposit base that can be monetized through additional products (e.g., interchange income on the upcoming Deel Card).
- Positions Deel as both a payroll processor and a financial services provider, leveraging DeFi to differentiate its offering.