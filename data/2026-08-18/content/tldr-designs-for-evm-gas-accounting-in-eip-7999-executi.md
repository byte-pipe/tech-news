---
title: Designs for EVM gas accounting in EIP-7999 - Execution Layer Research - Ethereum Research
url: https://ethresear.ch/t/designs-for-evm-gas-accounting-in-eip-7999/25696
site_name: tldr
content_file: tldr-designs-for-evm-gas-accounting-in-eip-7999-executi
fetched_at: '2026-08-18T12:12:02.835205'
original_url: https://ethresear.ch/t/designs-for-evm-gas-accounting-in-eip-7999/25696
date: '2026-08-18'
published_date: '2026-08-12T23:22:25+00:00'
description: Introduction A multidimensional fee market enables precise control over resource consumption. It allows the market to fairly price resources according to targets and limits deemed safe by developers, and it allows resour&hellip;
tags:
- tldr
---

# Designs for EVM gas accounting in EIP-7999

Execution Layer Research

fee-market

aelowsson

 August 12, 2026, 11:22pm
 

1

## Introduction

A multidimensional fee market enables precise control over resource consumption. It allows the market to fairly price resources according to targets and limits deemed safe by developers, and it allows resources to be consumed at maximum capacity within these limits.EIP-8037introduces state creation as a separately metered resource. Its resource-pricing design is kept simple so as not to delay Glamsterdam, but the lack of a separate base fee may lead to variousfailure modes. To alleviate this, it is desirable to make state a fully separate resource with its own base fee in the future, allowing more precise control over both state and execution gas rather than the coupled pricing of the existing design.

EIP-7999provides a broad framework for a unified multidimensional fee market with a single aggregatemax_fee. An openPR with proposed changesexplores adding state and data as separately priced resources. The data resource covers both transaction-content bytes and block-access-list (BAL) bytes. This post compares four design paradigms for reconciling separate resource prices with transaction limits,GAS, and the scalar gas parameter of legacy calls.

The central difficulty is that multidimensional pricing naturally gives each resource its own meter and base fee, while the EVM currently exposes one scalar gas budget. We can preserve that scalar interface in several different ways, or decide that new contracts should interact with the resource dimensions directly. Each choice moves the complexity to a different part of the protocol.

## Overview of design paradigms

Four paradigms will be described in greater detail in subsequent sections. They are:

* Aggregate EVM gas:The EVM continues to use one shared gas meter for execution, state, and data. The protocol separately records which resource consumed the gas and lets each resource have its own base fee, target, and block accounting. This is the closest to today’s scalar EVM, but the transaction must be funded as though the shared gas were spent on the most expensive resource.
* Multidimensional subfee market:The transaction supplies separate limits for regular gas, state bytes, and data bytes, but the EVM still runs on one scalar gas meter. At the beginning of the block, the relative base fees are converted into a fixed scalar gas cost for state and data operations. This avoids the conservative funding check required by Aggregate EVM gas and lets contracts continue to useGASandCALL(g)similarly to today. However, contracts that reserve gas for state or data would need to be updated to first read the current conversion rate.
* Universal overflow:The transaction has a dedicated limit for each resource and an additional scalar overflow that any EVM resource may consume after its own limit is exhausted. A legacyCALL(g)controls how much of this overflow is forwarded, while the dedicated limits are forwarded separately. This preserves a scalar post-call reserve without making the entire EVM allowance fungible.
* Multidimensional fee market with an updated EVM:The separate resource budgets remain visible inside the EVM. New calls can forward or reserve execution, state, and data capacity directly, and new introspection can report the remaining resource vector. Legacy contracts would receive a best-effort compatibility rule, potentially supplemented by Universal overflow.

These options preserve the current scalar EVM in different ways. Aggregate EVM gas keeps today’s gas schedule and shared meter, but pays for that simplicity in the funding check. The subfee market keeps scalar calls by allowing the gas cost of state and data operations to float, shifting complexity to opcode pricing and contracts that reserve capacity for specific work. Universal overflow preserves a scalar buffer that the caller may retain, but weakensGASas a measure of total remaining capacity and the ability to cap callees without subjecting more capacity to the highest-price funding check. An updated EVM gives new contracts direct control over every resource, but requires a larger compatibility and tooling transition.

### A note on the EIP-8037 reservoir

In several paradigms, the gas reservoir of EIP-8037 is relevant. We introduce it here to unfamiliar readers.EIP-7825caps a transaction’s declared gas limit at2^{24}. EIP-8037 instead applies the cap only to execution gas, allowing additional state gas, and divides the post-intrinsic transaction gas into two pools:

gas_left = gas available to ordinary execution
state_gas_reservoir = additional gas available only to state creation

Execution operations consume onlygas_left. State-gas charges consume the reservoir first and then fall back togas_left. TheGASopcode reports onlygas_left, so a transaction can still have state capacity that is not visible throughGAS.

The reservoir therefore preserves the per-transaction execution-gas cap while permitting additional state capacity. It is a state-specific solution to a more general problem: if transactions also receive additional BAL-data capacity, that capacity must not become spendable as execution. Aggregate EVM gas and the subfee market can address this through protected resource-specific pools or by independently enforcing the execution-gas cap with an explicit counter. Universal overflow and an updated EVM track execution separately and can apply EIP-7825 directly to execution usage.

## Aggregate EVM gas

### Design

Aggregate EVM gasretains one scalar gas meter for non-deterministic EVM execution. Execution, state-creation, and BAL-data charges incurred during execution consume a shared gas budget under a fixed gas schedule. At the same time, the protocol separately records how much execution gas, state gas, and data gas was consumed, allowing each resource to have its own base fee, target, and block accounting.

The shared scalar meter controls execution, while the realized resource vector determines the fee. If a transaction consumesg_eexecution gas,g_sstate gas, andg_ddata gas, its base-fee payment is

b_e\,g_e+b_s\,g_s+b_d\,g_d.

The difficulty is that the protocol does not yet know which resource will consume the aggregated EVM gas. IfG_adenotes the fungible aggregate gas that can become execution, state, or data gas, a strict funding check must cover

\max(b_e,b_s,b_d) \, G_a.

Deterministic resource components can instead be funded separately at their applicable base fees. The same uncertainty affects pre-execution block-capacity checks: a shared limit must be conservatively counted against every hard-limited block dimension it may consume. A more permissive variant could let the sender waive the full funding guarantee. An ETH-denominatedfee_leftmeter would then fall as resources are consumed, and execution would halt if the funded amount were exhausted. This can lower the upfront requirement, but it introduces a new failure condition for users and requires careful rules for propagation and settlement.

Other variants discussed in EIP-7999 instead move the post-execution funding risk to the block producer, leaving fee sufficiency unresolved (e.g., in the mempool) until execution. It would be desirable to explore options that make Aggregate EVM gas compatible with an acceptable funding check.

### Benefits

Aggregate EVM gas retains the current transaction format and makes the smallest change to the current EVM interface. A scalar gas limit is retained for EVM work, and legacyGASandCALL(g)continue to operate on a familiar shared meter. Existing contracts do not need to read a changing state-gas or data-gas conversion rate before making a call.

Opcode gas costs also remain stable. Separate base fees change what the transaction pays for each resource, but they do not change how much scalar gas an operation consumes. The EIP-8037 reservoir provides a direct way to preserve the EIP-7825 execution cap while allowing larger state-creating transactions. This makes Aggregate EVM gas a plausible transitional design when minimizing EVM changes is the main objective and large base-fee divergence is not expected.

### Drawbacks

The conservative funding check is the central drawback. A transaction may need to escrow enough ETH to cover its entire fungible shared limit at the highest EVM base fee even when it uses little of that resource. As the base fees diverge, transactions that would be affordable under their realized resource mix may fail the upfront balance check or require a much larger temporary balance. The blob base fee has at times diverged significantly from the execution base fee, and EVM base fees may diverge to some extent as well. Reserve prices of the kind deployed in EIP-7918 could preserve viable funding checks, but would couple the resource prices.

The reservoir also weakens the meaning ofGAS. A child call can consume state from the transaction-wide reservoir even though that capacity is not included ingas_leftand therefore is not reflected inGASor fully controlled by the scalar call parameter. EIP-8037 already notes that systems which attribute subcall gas use fromgasleft()differences cannot see state gas funded by the reservoir. With separate base fees, a scalar difference also does not reveal the subcall’s fee-relevant resource mix, affecting any contract that uses gas differences for internal fee attribution. If future resources receive similar protected capacity, a larger share of the transaction’s possible work would sit outside the scalar value observed by legacy contracts.

The design does not scale gracefully to many independently priced runtime resources. Every additional resource increases the chance that one base fee is much higher than the others, worsening the funding check. It can also require additional special fallback rules to preserve resource-specific transaction caps. The builder must therefore consider a wider range of block-packing combinations, and conservative pre-execution checks can still exclude transaction sets whose realized use would have fit.

## Multidimensional subfee market

### Design

Amultidimensional subfee marketsuggested in EIP-8075 could instead preserve a scalar EVM by assigning floating gas prices to state and data. Execution, state, and data retain separate base fees, while the scalar gas costs used inside the EVM are derived from their ratios.

The transaction supplies separate limits for regular gas, state bytes, and data bytes. At the beginning of each block, the protocol computes one effective scalar gas cost per state and data byte and keeps it fixed for every transaction and subcall in that block. Taking the execution base fee as the scalar EVM base fee, and lettingc_sbe the baseline state gas per byte, the effective state cost per byte can, abstracting from integer representation, be written as

C_s= c_s\frac{b_s}{b_e},

whereb_eis the execution base fee andb_sis the state base fee. The state component of an operation that createsxbytes then consumesxC_sscalar gas. Charging this scalar gas atb_eproduces the same base-fee payment as charging the baseline state gas atb_s.

The same conversion is applied to the data resource. Transaction-content bytes and BAL bytes both settle at the data base fee, although transaction-content usage is already known before execution. If the supplied limits areL_eregular gas,L_sstate bytes, andL_ddata bytes, the protocol computes

G=L_e+C_sL_s+C_dL_d.

Execution can proceed againstGalone, so the resource limits are not enforced separately. In that case, an explicit execution-gas counter must enforce EIP-7825 so that converted state or data capacity cannot become additional execution capacity. Alternatively, the limits can also be enforced separately for more precise control, using the separate per-resource tracking also needed by Universal overflow and the full multidimensional fee market. The second option also permits dedicated censorship-resistance strategies for BAL data, as will be described in a separate research post.

Contracts that use a gas parameter to reserve capacity for later state or data work must read the exact effective cost for the current block. They can then calculate the necessary scalar amount and useGASandCALL(g)as today. Existing contracts that hard-code gas assumptions may nevertheless break. The conversion rate is fixed for the full block, so there is no further adjustment during the transaction or between call frames.

### Benefits

The subfee market removes the highest-price funding problem while retaining one scalar EVM meter. Once state and data allowances have been converted into execution-equivalent gas, every unit of the shared meter has the same base-fee value. The separate limits can therefore be priced at their own base fees when the scalar limit is constructed.

TheGASandCALL(g)interfaces remain scalar. A contract that reads the current effective state or data cost can calculate how much gas to reserve or forward for a specified amount of work without changing the call signature or introducing a resource vector into each frame.

The transaction format also protects against conversion-rate drift between submission and inclusion: the scalar allowance is recomputed from the supplied limits using the inclusion block’s rates, although the unifiedmax_feemust still cover those rates. After conversion, execution uses one fixed gas schedule and one scalar limit.

The design retains separate resource targets and base fees. It therefore preserves separate control of block-level resource use without requiring multidimensional calls.

### Drawbacks

The main drawback is opcode-price volatility. The scalar gas charged for state and data operations changes whenever their base fees move relative to the execution base fee. Contracts that rely on hard-coded stipends, exactgasleft()thresholds, or fixed assumptions about the cost of state or data work will often need to be adjusted to read the current rates before they can reserve a correct amount of gas. The protocol must thus expose the exact effective rates used by consensus and define precise fixed-point and rounding rules.

If the scalar capacity is fungible after conversion, builders must still project it conservatively into any raw resource dimension with a hard block limit. Any protected resource-specific capacity outsidegas_leftsimilarly weakens the meaning ofGAS.

## Universal overflow

### Design

Universal overflowgives the transaction a separate limit for each EVM resource and one additional scalar overflow limit. An operation first consumes its dedicated resource budget. If that budget is exhausted, it can consume Universal overflow instead.

A legacyCALL(g)forwards the remaining dedicated budgets in full, while the amount of Universal overflow forwarded follows the existing scalar call rule. The legacyGASopcode correspondingly reports the remaining Universal overflow. The caller can therefore hold back a fungible buffer for cleanup, accounting, or other work after the subcall, while most of the transaction remains funded through separate resource limits.

LetL_ibe the dedicated limit for resourcei,b_iits base fee,Othe Universal overflow, andb_{\max}the highest relevant EVM base fee. The base-fee funding check is

\text{required base-fee coverage}=\sum_i b_i\,L_i+b_{\max}\,O.

Only the overflow must be funded at the highest base fee. The dedicated limits are funded at their own prices.

A substantial class of transactions can set the overflow to zero, including simple transfers and transactions whose execution neither relies onGASnor requires a guaranteed scalar reserve after a legacy call. Universal overflow is mainly a compatibility mechanism for legacyCALL(g)and a fallback for transactions with uncertain resource use. How many existing transactions need it, or rely onGASfor other purposes, should be measured empirically.

By default,CALL(g)forwards all remaining dedicated resource capacity, while Universal overflow is forwarded only according tog. An alternative strict-cap call opcode could instead retain all dedicated budgets and forward only the overflow selected byg. This would let a caller cap a small subcall while retaining most of its capacity in separately priced dedicated budgets, avoiding a large highest-price funding requirement.

The interaction with EIP-7825 is straightforward because execution gas would be tracked explicitly throughout the EVM. Clients would therefore count all execution gas consumed, including execution drawn from Universal overflow, and prevent the transaction from exceeding the cap.

At block level, clients continue to track actual consumption in every resource. Because Universal overflow can be spent entirely on any eligible resource, a conservative pre-execution check must reserve corresponding headroom in each eligible hard-limited dimension.

### Benefits

Universal overflow preserves the main retained-gas use case of the legacy scalar call parameter. A caller can reserve a fungible amount for post-call work without requiring the whole transaction to use Aggregate EVM gas.

Most of the transaction can be funded against the actual base fee of each resource. Only the explicitly chosen overflow is priced at the highest base fee. When the compatibility buffer is small compared with the dedicated limits, the upfront funding requirement is much lower than under Aggregate EVM gas.

The gas schedule remains stable. State creation and data operations keep fixed costs in their own dimensions, while demand changes affect their base fees rather than the amount of gas consumed inside the EVM.

The mechanism also extends naturally to additional resources. Each new resource receives a dedicated limit and base fee, while the same overflow can provide a scalar fallback when fungibility is genuinely needed.

### Drawbacks

A legacyCALL(g)no longer necessarily places a complete cap on the callee. The scalar parameter limits the forwarded Universal overflow, but the dedicated resource budgets are forwarded separately. A callee may therefore consume substantial dedicated execution, state, or data capacity even when the caller supplies a smallg. This is a real compatibility concern for contracts that deliberately use a gas stipend to sandbox or limit an untrusted callee.

It is not absolute, however. The transaction sender can place most of the relevant capacity in Universal overflow, makingCALL(g)once again cap most of the callee’s work. This recreates much of the highest-price funding requirement of Aggregate EVM gas. Universal overflow therefore offers a continuum: more dedicated capacity improves funding efficiency, while more overflow more closely preserves the historical scalar cap. The same trade-off applies to conservative block-capacity reservation. As noted previously, a separate strict-cap opcode could instead forward only Universal overflow for this use case.

TheGASopcode reports only the Universal overflow, not the complete remaining resource vector. This is sufficient for contracts that use it only to manage the scalar reserve controlled by legacy calls. Contracts that genuinely need to know the remaining execution, state, or data capacity would need new multidimensional introspection.

## Multidimensional fee market with an updated EVM

### Design

Amultidimensional fee market with an updated EVMkeeps resource budgets separate inside each EVM call frame. A frame would carry, for example, distinct remaining budgets for execution, state, and data. An operation fails when the required resource budget is exhausted.

New calls would operate directly on this vector. A caller could specify the resource vector to forward or, equivalently, the vector that must remain with the caller after the call. The exact opcode interface is open, but new contracts would no longer need to compress several resource budgets into one scalar gas argument. Another option, following the direction of EOF’s new call instructions, is to remove gas observability for new contracts and have calls automatically forward a protocol-defined share of each remaining resource.

Legacy contracts would still need a best-effort rule. One option outlined in EIP-7999 is to calculate an aggregate scalar value from the remaining resource vector. A legacyGASreturns that aggregate, and a legacyCALL(g)forwards the same fraction of every remaining resource budget. This preserves a rough proportional interpretation of the old scalar parameter, but it cannot preserve every exact gas threshold or gas-capped subcall.

The updated EVM can also be combined with Universal overflow or an overflow vector. New contracts can use exact multidimensional calls, while legacy calls control a narrower compatibility budget.

Funding is direct. If the transaction specifies limitL_ifor each resource with base feeb_i, the base-fee requirement is

\text{required base-fee coverage}=\sum_i b_i\,L_i.

No shared budget must be funded at the highest base fee, and no market-price ratio is embedded in opcode gas costs.

### Benefits

This is the cleanest long-run resource model. Transaction limits, block limits, fee controllers, call-frame budgets, and introspection can all use the same resource dimensions. A new caller can independently cap an untrusted callee’s execution, state creation, and data production while retaining an exact resource vector for later work.

Resource costs remain stable in their respective units. Base-fee changes affect payment, but do not change how much state or data a given allowance buys. Funding is precise, and adding another scarce resource extends the existing vectors rather than adding another scalar conversion or protected pool.

The design also makes the trade-off explicit. New contracts receive precise multidimensional semantics, while compatibility machinery for legacy contracts can be isolated rather than shaping the entire EVM forever.

### Drawbacks

The migration cost is substantial. The EVM and execution clients need new call and introspection semantics. Contract languages and compilers need a way to express the new resource budgets, while gas estimation, transaction simulation, and tracers need to expose more than one runtime meter. Infrastructure that attributes work fromgasleft()differences, including some bundling and account-abstraction systems, may also need revised accounting.

No scalar compatibility rule can preserve every use of legacyGASandCALL(g). Proportional forwarding may preserve approximate behavior, and Universal overflow may preserve a scalar post-call buffer, but contracts relying on exact stipends, precise thresholds, or strict scalar caps can still change behavior. Calls between legacy and updated code therefore require careful boundary rules.

## Comparison of design paradigms

### Qualitative scorecard

The following table gives a rough qualitative assessment.++indicates a strong advantage,+a moderate advantage,0a mixed or design-dependent outcome,-a drawback, and--a substantial drawback. The grades are intended to expose the trade-offs rather than select a winner. Any--grade may for example make a design infeasible.

Property

Aggregate EVM gas

Multidimensional subfee market

Universal overflow

Updated EVM

Funding efficiency

--

++

+

++

Callee-cap compatibility

+

+

0

0

Legacy scalar post-call reserve

++

++

++

-

Legacy 
GAS
 accuracy

+

+

--

0

Opcode-cost stability

++

--

++

++

Deployment ease

++

+

+

--

Extensibility

--

+

+

++

The callee-cap row reflects the overall compatibility available within each paradigm, including the possible new strict-cap call under Universal overflow, rather than only the default behavior of legacyCALL(g).

### Transaction format

Under Aggregate EVM gas, the single limit minimizes transaction-format changes, but it leaves the protocol unable to distinguish the transaction’s worst-case resource mix before execution. This is what produces the conservative funding and block-capacity checks.

The subfee market uses separate regular-gas, state-byte, and data-byte limits to calculate one scalar gas limit at inclusion. The separate fields protect the user against conversion-rate drift. If the resource limits are additionally enforced, they also constrain the corresponding runtime use.

Universal overflow and the updated EVM also use per-resource limits. Universal overflow adds a scalar compatibility buffer that can be consumed by any EVM resource. The updated EVM keeps the limits separate throughout execution and lets new calls forward or reserve them directly.

State and data limits may be easier to reason about in bytes. A byte-denominated limit remains stable if the protocol later changes a fixed gas-per-byte coefficient. The protocol can apply the relevant coefficient before execution. This denomination choice is useful across several paradigms and is distinct from the choice of EVM call semantics.

Legacy transaction types expose only one EVM gas limit. Deterministic transaction-content usage can be accounted for before execution, but the difficulty is assigning the remaining allowance across multiple runtime resources such as execution, state creation, and BAL data.

Under Aggregate EVM gas, the scalar limit retains its current meaning as one shared runtime limit. Under the subfee market, it can likewise remain a scalar runtime limit under the inclusion block’s converted gas schedule. The sender would not, however, specify separate state- and data-byte allowances, so changes in the conversion rates would alter how much state or BAL work fits within the signed limit. This speaks in favor of having slower-moving gas prices for these resources under the subfee market.

Universal overflow and an updated EVM instead work with separate runtime budgets. A legacy transaction could then be processed through an Aggregate EVM gas fallback. Under Universal overflow, this is equivalent to placing its entire EVM allowance in fungible overflow. This preserves scalar behavior but reintroduces the highest-price funding and conservative block-capacity checks. The updated EVM could either use such a Universal overflow fallback or a scalar-to-vector mapping, as discussed previously.

A unified scalarmax_feeremains compatible with all four paradigms. What changes is the set of resource limits and counterfactual uses against which that ETH budget is checked.

### Gas observability and call functionality

There are three related but distinct compatibility goals:

1. preserving the ability of a caller to reserve capacity for work after a subcall;
2. preserving the ability to impose a hard cap on the work performed by the callee; and
3. preservingGASas a scalar measure of all remaining EVM capacity.

Today, one scalar meter largely serves all three purposes. The four designs preserve different subsets.

Aggregate EVM gas and the subfee market both preserve the familiar scalar relationship for capacity held ingas_left: charges drawing from it consume one scalar meter, and legacyCALL(g)controls how much of that meter is forwarded.

If protected capacity remains outsidegas_left, both designs have the same exception: that capacity is not included inGASand is not fully capped by the scalar call parameter. If the subfee market additionally enforces its resource limits during execution, those limits also impose constraints not represented byGAS. A contract using the subfee market that wants to reserve gas for a specified amount of state or data must also read the current effective cost.

Universal overflow is designed primarily around the first property. A legacy caller can reserve a scalar overflow buffer. The same scalar parameter does not however cap the callee budgets, andGASdoes not report the full resource vector. A transaction can recover a cap by placing more capacity in overflow, at the cost of giving up that part of the funding advantage.

This does not restore the guarantee for a legacy contract that treatsCALL(g)as a security boundary, because the contract cannot require the sender to allocate capacity in this way. New or updated contracts would need the possible strict-cap call opcode discussed above. With zero overflow,GASreports zero despite remaining dedicated capacity, so contracts that merely usegasleft()as a runtime guard may also break.

An updated EVM is the least compatible with legacy contracts and instead provides optimized multidimensional equivalents for new contracts. Under these new interfaces, calls can reserve or cap a resource vector, and introspection can report that vector exactly. This direction could potentially be combined with functionality for legacy contracts drawn from another paradigm, such as Universal overflow.

### Funding checks and block packing

The funding distinction can be summarized as follows:

* Aggregate EVM gas funds the fungible shared allowance at the highest EVM base fee, unless the protocol accepts some form of post-execution funding risk.
* The subfee market converts the supplied resource limits into scalar gas so that the scalar funding check is economically equivalent to pricing those limits separately.
* Universal overflow funds dedicated limits at their own base fees and only the overflow at the highest EVM base fee.
* The updated EVM directly funds each resource limit at its own base fee.

Concerning block packing, the updated EVM gives the builder a clear worst-case resource vector. Universal overflow does so for the dedicated budgets, but its overflow must still be conservatively projected. Under Aggregate EVM gas, the fungible shared limit must be conservatively projected into every constrained resource it may become. A subfee market without separately enforced resource limits has the same issue.

## Open questions

1. Which legacy gas properties are the most important to preserve?We could try to distinguish post-call reservation, callee capping, and scalar introspection, and measure how frequently deployed contracts rely on each behavior. A useful empirical question is thus not only whether contracts invokeGAS, but what they use it for.
2. How much Universal overflow is needed in practice?Many transactions can use zero, but which usage patterns can be observed among legacy contracts that readGAS, and what do developers indicate they would use Universal overflow for?
3. Can Aggregate EVM gas adequately relax the funding check?An opt-infee_leftmeter, post-execution block validity rule, or block-producer guarantee could reduce the upfront requirement, but each shifts risk and changes failure or inclusion semantics.
4. How should EIP-7825 apply after resources are separated?If this path is pursued, it would be desirable to implement EIP-7825 under separately tracked resources and verify that the intended functionality is straightforward to achieve.
5. What is the best migration path for updated calls?Possibilities include proportional legacy forwarding, Universal overflow, an overflow vector, versioned code with exact multidimensional calls, and combinations of these.

1 Like

vbuterin

 August 12, 2026, 11:37pm
 

2

I think the multidimensional subfee market and universal overflow are solving different problems.

For instance, notice that if we JUST did the multidimensional subfee market and not overflow, then we would not have been able to solve the “allow deploying big contracts while keeping the 16m limit” problem. Multidimensional subfee market alone would have forced us to have a consistent ratio of “max in a block” / “max in a transaction” across all resource types, which does not actually make sense. The fundamental thing it can’t handle is different resources that accept different levels of burstiness. And in addition to this, you don’t get the benefit of being able to accommodate more burst consumption within a block if that burst consumption is split among different resources.

Meanwhile, if you do universal overflow without floating prices, then you get inefficiency if you did not set ratios correctly - you risk a situation where the gas of some type that gets consumed ends up being far less than the amount that is safe to consume.

So I think there’s value in exploring combinations of the two, doing universal overflow with floating prices (!!)

(This also gives you most of what you want out of opcode cost stability, because you only get gas cost volatility once gas consumption bleeds over into universal overflow - while it’s within buckets, you’re consuming separate resources and costs are stable while gasprices (which float) are at the transaction layer, not the VM layer)

1 Like

aelowsson

 August 13, 2026, 12:37am
 

3

Note that the Multidimensional subfee market has separate native resource limits (e.g., bytes), and derives from these limits an aggregate gas limit at inclusion time. EIP-7825 is enforced on execution alone via the EIP-8037 reservoir or an explicit counter. In my view, this should alleviate concerns around, e.g., burstiness, since the gas cost cannot drift to exceed the user-specified (byte) limits. But any users relying on old transaction formats would indeed not be able to count on that.

Since the Universal overflow has general floating base fees, I take it your suggestion is that the overflow should have floating gas costs derived from those base fees, fixed at the start of each block. This would further alleviate any potential issues with the funding check. The downside is that since the gas cost would drift, we are back to transactions potentially setting a too low overflow limit. To alleviate that, we would need to apply the full subfee market, including separate, e.g., byte limits, for the overflow resource, which then are converted to a scalar at inclusion time. We are in that case essentially comparing applying Aggregate EVM gas or the Multidimensional subfee market to the overflow resource. That’s interesting to discuss further concerning benefits and drawbacks!

vbuterin

 August 13, 2026, 2:17pm
 

4

Yeah basically:

* Do vectorized gas limits and prices like in 7706
* Overflow gas is one of those dimensions
* Option 1: overflow gas is treated as equivalent to EVM gas, and so if the EVM gas in execution is fully consumed, it starts burning overflow at a 1:1 ratio, and if other gas (eg. state gas) in execution is fully consumes, it starts burning overflow at a (state gasprice):(EVM gasprice) ratio
* Option 2: overflow gasprice is hardcoded to 1, if any gas in execution is fully consumed, it starts burning overflow at a (gasprice of that gas):1 ratio

(An open question is how to set the block-level target and limit of overflow in this case. One simple option is “set the target to be whatever lets you buy min(2**24 EVM gas, 25% of the sum of the other limits), and the limit to that * 2”)