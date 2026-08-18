---
title: Designs for EVM gas accounting in EIP-7999 - Execution Layer Research - Ethereum Research
url: https://ethresear.ch/t/designs-for-evm-gas-accounting-in-eip-7999/25696
date: 2026-08-18
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-18T12:12:24.558362
---

# Designs for EVM gas accounting in EIP-7999 - Execution Layer Research - Ethereum Research

# Designs for EVM gas accounting in EIP‑7999

## Introduction
- Multidimensional fee markets aim to price resources (execution, state, data) precisely according to developer‑set targets and limits.  
- EIP‑8037 adds a separate meter for state creation but lacks a distinct base fee, which can cause failure modes.  
- EIP‑7999 proposes a unified framework with a single `max_fee` and explores adding separate pricing for state and data (transaction‑content bytes and block‑access‑list bytes).  
- The core challenge: multidimensional pricing gives each resource its own meter and base fee, while the EVM currently exposes only a scalar gas budget. Different designs shift this complexity to various protocol layers.

## Overview of design paradigms
1. **Aggregate EVM gas** – One shared gas meter for execution, state, and data; protocol records per‑resource consumption for fee calculation. Transactions must fund as if the shared gas were spent on the most expensive resource.  
2. **Multidimensional sub‑fee market** – Transactions provide separate limits for gas, state bytes, and data bytes, but the EVM still uses a scalar gas meter. At block start, relative base fees are converted to a fixed scalar cost for state and data ops, allowing legacy `GAS`/`CALL(g)` usage. Contracts need to read the conversion rate when reserving state or data capacity.  
3. **Universal overflow** – Each resource has its own limit plus an additional scalar overflow that any resource may consume after its dedicated limit is exhausted. Legacy `CALL(g)` forwards a portion of this overflow; dedicated limits are forwarded separately. Preserves a scalar post‑call reserve without making the whole allowance fungible.  
4. **Updated EVM with multidimensional market** – Resource budgets are visible inside the EVM. New opcodes can forward or reserve execution, state, and data capacity directly; introspection reports the remaining vector. Legacy contracts receive best‑effort compatibility, possibly via Universal overflow.

### Relation to the EIP‑8037 reservoir
- EIP‑7825 caps transaction‑declared gas at \(2^{24}\) for execution only; state gas is placed in a separate “reservoir”.  
- `gas_left` is for ordinary execution; `state_gas_reservoir` supplies extra gas for state creation.  
- `GAS` reports only `gas_left`, so state capacity is invisible to contracts.  
- The reservoir concept helps keep execution‑gas caps while allowing extra state (or future data) capacity, influencing how each paradigm enforces caps and funding checks.

## Detailed paradigms

### Aggregate EVM gas
- **Design**: Single scalar meter consumes execution, state, and data gas under a fixed schedule; protocol separately logs consumption per resource for fee calculation.  
- **Funding check**: Must conservatively cover \(\max(b_e, b_s, b_d) \times G_a\) because the protocol cannot know beforehand which resource will dominate.  
- **Variants**:  
  - Waiving full funding guarantee and using an ETH‑denominated `fee_left` meter that depletes as resources are consumed (introduces new failure mode).  
  - Shifting post‑execution funding risk to block producers (leaves mempool sufficiency unresolved).  
- **Benefits**: Minimal changes to transaction format and EVM interface; legacy `GAS` and `CALL(g)` work unchanged; opcode gas costs stay stable; EIP‑8037 reservoir already supports execution‑gas caps.

*(The article continues with further sections on the other paradigms, their benefits, drawbacks, and implementation considerations.)*