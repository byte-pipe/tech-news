---
title: What do Visa and Mastercard do? An intro to card networks @ tautology.town
url: https://tautology.town/2026/06/01/card-networks.html
date: 2026-09-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:40.597105
---

# What do Visa and Mastercard do? An intro to card networks @ tautology.town

# What Visa and Mastercard Do – Summary

## Overview
- Visa and Mastercard are widely recognized brands; most consumers use their cards daily.
- They are not the issuers of cards, banks, payment processors, merchant acquirers, card manufacturers, or POS hardware producers.
- Their core function is to operate as card **networks**, connecting cardholders, issuers, merchants, and acquirers in a two‑sided market.

## What They Do Not Do
- Issue cards (that is done by banks or other card issuers).  
- Act as banks themselves.  
- Provide point‑of‑sale software or online checkout solutions (handled by payment processors).  
- Perform merchant onboarding or underwriting (handled by acquiring banks or modern processors like Stripe, Square, Adyen).  
- Manufacture physical cards or POS terminals.

## Role as Card Networks
- Facilitate card transactions by routing messages and money between issuers and acquirers.  
- Grow participation in their networks by setting incentives, rules, and dispute mechanisms.

## Four Key Responsibilities

### 1. Run the Telecommunications Network
- Maintain secure, redundant data centers and lease fiber‑optic links to connect all participants.  
- Act as a “switch” that forwards authorization requests from merchants to issuers and returns approvals/declines.  
- Use the Primary Account Number (PAN) like an IP address; the first 6‑8 digits (Bank Identification Number) identify the issuing bank.  
- Handle authorization (temporary hold) and clearing (final transaction amount) electronically, replacing older phone‑and‑mail processes.

### 2. Coordinate the Banking Network
- Manage settlement of funds after a transaction is cleared.  
- Perform net settlement: each participant’s daily debits and credits are summed, and a single net transfer is made at day‑end.  
- Support domestic settlement via central banks and international settlement with currency conversion, acting as an adapter between different banking systems.  
- Hold substantial liquidity (e.g., $11.2 billion in 2024) to cover settlement risk; daily settlement exposure can exceed $100 billion.

### 3. Set Incentives
- Determine the fee structure for participation in the network (interchange fees, assessment fees, etc.).  
- Example (U.S. credit card): a $100 purchase results in a merchant fee of about 2.5 % ($2.50), split among issuer, acquirer, and the network.

### 4. Set and Enforce Rules
- Define network rules governing transaction processing, security standards, and dispute resolution.  
- Provide mechanisms for handling chargebacks and other disputes between parties.