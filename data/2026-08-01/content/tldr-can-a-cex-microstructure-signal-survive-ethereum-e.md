---
title: Can a CEX microstructure signal survive Ethereum execution latency and MEV? - Economics - Ethereum Research
url: https://ethresear.ch/t/can-a-cex-microstructure-signal-survive-ethereum-execution-latency-and-mev/25562
site_name: tldr
content_file: tldr-can-a-cex-microstructure-signal-survive-ethereum-e
fetched_at: '2026-08-01T19:28:21.585918'
original_url: https://ethresear.ch/t/can-a-cex-microstructure-signal-survive-ethereum-execution-latency-and-mev/25562
date: '2026-08-01'
published_date: '2026-07-28T21:53:23+00:00'
description: 'Motivation We are investigating a narrow cross-venue market-microstructure question: Can a predictive signal generated from BTC and ETH perpetual trades on a centralized exchange reduce adverse selection when liquidity &hellip;'
tags:
- tldr
---

# Can a CEX microstructure signal survive Ethereum execution latency and MEV?

Economics

market-microstructure
, 
 
execution
, 
 
data-availability
, 
 
mev

amlsl

 July 28, 2026, 9:53pm
 

1

## Motivation

We are investigating a narrow cross-venue market-microstructure question:

Can a predictive signal generated from BTC and ETH perpetual trades on a centralized exchange reduce adverse selection when liquidity is provided on an Ethereum-based decentralized venue?

We are not assuming that a profitable CEX construct can simply be copied to a DEX. Our starting prior is deliberately sceptical. Even if the source signal is informative, the edge may disappear because of:

* source-feed and network latency;
* order construction and signing;
* gateway, sequencer or block timing;
* different matching and price-formation rules;
* MEV and transaction ordering;
* fees and liquidity fragmentation;
* queue position, missed fills and cancellation races;
* different participant behaviour across venues.

We have source-venue evidence that several fixed model outputs contain short-horizon information after controlling for the previous price-change direction. We do not yet know whether that information survives long enough to improve execution on another venue.

We would value criticism of the proposed experiment, especially from researchers working on MEV, order flow, DEX execution, sequencers and market making.

## Source stream and production path

The source stream consists of BTCUSDT and ETHUSDT perpetual trades from a centralized exchange.

Equal-price trades are excluded from decision events. Each remaining event is a price-changing trade. At each event, the production engine:

1. updates causal features using only information available at that event;
2. evaluates directional, reversal and swing model families;
3. updates a fixed directional-protection construct calleddir_mr;
4. records the source-market timestamp, generation timestamp, model outputs and construct state;
5. observes later price changes only for evaluation.

The production path is implemented in Rust/C++. Local inference takes approximately4–50 microseconds, depending on the model family.

This is local inference time, not end-to-end execution latency. It excludes:

* exchange publication latency;
* market-data transport;
* cross-venue propagation;
* order construction and signing;
* destination-gateway acknowledgement;
* sequencer or block inclusion;
* final settlement.

This distinction is central to the experiment. A microsecond inference path is economically irrelevant if the information decays before an order becomes executable on the destination venue.

## Exact semantics of thedir_mrconstruct

dir_mris an event-driven state machine with three possible states:

[q_t \in {-1,0,+1},]

where:

* (q_t=0): no active directional-protection state;
* (q_t=+1): active long/upward state;
* (q_t=-1): active short/downward state.

The construct combines:

* directional long/short signals, which initiate a directional state;
* reversal signals, which identify possible exhaustion or reversal of the active direction;
* swing signals, which identify an opposing mean-reversion or swing state.

The transition rules are fixed:

### Opening a state

* When flat, a validlongdirectional signal opens (q_t=+1).
* When flat, a validshortdirectional signal opens (q_t=-1).
* reversalandswingdonotindependently open adir_mrstate.

### Closing a long state

An active long state closes when any of the following occurs:

* a valid short directional signal;
* a reversal signal against the long state;
* a swing signal against the long state;
* the hard timeout.

### Closing a short state

An active short state closes when any of the following occurs:

* a valid long directional signal;
* a reversal signal against the short state;
* a swing signal against the short state;
* the hard timeout.

In pseudocode:

if state == FLAT:
 if long_signal:
 state = LONG
 elif short_signal:
 state = SHORT

elif state == LONG:
 if short_signal or reversal_down or swing_down or timeout:
 state = FLAT

elif state == SHORT:
 if long_signal or reversal_up or swing_up or timeout:
 state = FLAT

The state is event-driven rather than held for a fixed wall-clock interval. Depending on when an opposing condition arrives, observed states can last from milliseconds to several minutes.

## Why this may be useful for adverse-selection control

dir_mris not intended to prove that every triggered state is a directly executable directional strategy. Its proposed execution use is narrower: determine which side of passive liquidity is more exposed to an imminent adverse move.

For example:

* During an active upward state, a passive ask may be toxic because it can fill shortly before the market moves higher.
* During an active downward state, a passive bid may be toxic because it can fill shortly before the market moves lower.
* The opposite quoting side may have a more favourable subsequent markout, subject to inventory and fill constraints.

This mapping is a hypothesis to be tested on destination-venue fills. A correct prediction of source-market direction does not by itself prove that a DEX order would be filled, avoid toxicity or produce positive net P&L.

## Source-venue results

In the current CEX-only proof of concept:

Instrument

Construct

Gross P&L/trade

Trade WR

Raw return IC

Momentum-controlled partial IC

Coverage

BTCUSDT perpetual

dir_mr

+0.82 bps

76.4%

+0.525

+0.394

2.4%

ETHUSDT perpetual

dir_mr

+0.95 bps

69.5%

+0.606

+0.160

3.6%

Trade WRis the fraction of profitable evaluateddir_mrstates, not directional accuracy over every source event.Coverageis the fraction of eligible source events at which the construct is active or triggered under the evaluation definition.

These aregross source-venue results before fees, spread, queue position, rejected orders, missed fills and cross-venue latency. They are not demonstrated DEX P&L.

The source metrics are included to establish that there is a fixed relationship worth attempting to falsify cross-venue. The destination experiment should not tune model orientation, thresholds or exit semantics after observing DEX outcomes.

## Controlling for the tick-momentum baseline

Price-changing trade streams contain a strong continuation component. A model can appear predictive merely by reproducing the sign of the previous price change.

We therefore use the naive source baseline:

[m_t=\operatorname{sign}(\Delta P_t)]

and calculate partial Spearman correlation controlling for the previous price-change sign from both sides:

# [

\rho_{\text{model},\text{forward}\mid\text{previous}}

\frac{\rho_{ms}-\rho_{mp}\rho_{sp}}{\sqrt{(1-\rho_{mp}^{2})(1-\rho_{sp}^{2})}}.]

Here:

* (\rho_{ms}) is the Spearman correlation between the model score and the forward signed return;
* (\rho_{mp}) is the correlation between the model score and the previous price-change sign;
* (\rho_{sp}) is the correlation between the forward signed return and the previous price-change sign.

A partial IC near zero suggests that the model is largely a momentum proxy. A positive partial IC indicates incremental rank information after removing this rank-linear relationship.

Representative source-stream results are:

Model family

h=1

h=3

h=5

h=10

hh_step1_updwn

0.136

0.104

0.084

0.059

lh_v4_step1_updwn

0.210

0.167

0.130

0.081

roc2_step1_updwn

0.462

0.364

0.283

0.183

roc3_updwn

0.349

0.280

0.218

0.142

ha_roc1_step1_updwn

0.424

0.335

0.262

0.170

The horizons (h) are measured in subsequent price-changing events. These values are partial Spearman ICs, not accuracy or executable P&L.

We do not interpret an arbitrary magnitude such as (|IC|>0.05) as a significance test. Formal inference must account for serial dependence, overlapping horizons, model multiplicity and regime instability.

## Why CEX-to-DEX transfer may fail

### 1. Signal decay during transport

Let:

[t_s=\text{local signal-generation time}]

and:

[t_e=\text{time at which the action becomes executable on the destination venue}.]

The economically relevant delay is:

[L=t_e-t_s.]

The full path may include:

[L =L_{\text{feed}}+L_{\text{network}}+L_{\text{inference}}+L_{\text{signing}}+L_{\text{gateway}}+L_{\text{sequencer/block}}.]

If the conditional return decays faster than this path, a statistically strong source signal becomes economically useless.

The primary analysis should therefore include a delay curve rather than one latency assumption:

[\operatorname{Edge}(L), \qquadL\in{0,1,5,10,25,50,100,250,500\text{ ms},1\text{ s},1\text{ block}}.]

### 2. Different destination mechanisms

A CEX central limit order book, an AMM, an RFQ system and an off-chain order book with on-chain settlement expose different economic states.

For a central-limit-order-book destination, relevant outcomes may include:

* fill probability;
* queue-adjusted post-fill markout;
* spread captured net of fees;
* cancellation success;
* inventory-adjusted P&L.

For an AMM destination, more appropriate outcomes may include:

* LP markout;
* loss versus rebalancing;
* arbitrage loss;
* inventory displacement;
* CEX–DEX convergence following a swap.

The same source signal should not be judged with an identical execution metric across incompatible venue designs.

### 3. Mechanical price leadership

A positive transfer result may not represent universal cross-venue prediction. The destination may use:

* a CEX-influenced oracle;
* an index containing the source exchange;
* arbitrageurs monitoring the same source;
* market makers hedging on the source venue.

The experiment should distinguish independent prediction from mechanical source-venue leadership. The latter can still be economically useful, but it is a different claim.

### 4. Fill selection and cancellation races

Source performance is conditional on source events. Destination performance is conditional on whether an order is submitted, acknowledged and filled.

A mid-price simulation can look favourable while failing after:

* queue position;
* post-only rejection;
* partial fills;
* cancellation latency;
* gas and protocol fees;
* missed fills during the most informative events;
* inventory accumulation.

The principal outcome should therefore be markout conditional on a real or realistically simulated destination fill, not only subsequent mid-price direction.

### 5. MEV and ordering

On a public Ethereum venue, a submitted action may reveal intent. It can be:

* reordered;
* sandwiched;
* deprived of priority;
* included only after the predicted move;
* excluded when its execution would have been favourable.

Private order flow and private sequencers may reduce some risks while introducing different trust, censorship and data-availability assumptions.

### 6. Clock alignment and hidden look-ahead

CEX exchange time, local receive time, model time, destination gateway time, sequencer time and Ethereum block time are different clocks.

A defensible record should contain:

* source exchange timestamp;
* local source-receive timestamp;
* local model-generation timestamp;
* order-construction and submission timestamp;
* destination acknowledgement timestamp;
* fill or inclusion timestamp;
* destination market-state timestamp.

Without these fields, a cross-venue result can contain hidden look-ahead even when the model itself is causal.

## Proposed falsification experiment

The source construct should be frozen before destination outcomes are inspected:

* fixed source models;
* fixed model orientation;
* fixeddir_mrtransitions;
* fixed source thresholds;
* fixed destination action mapping;
* predeclared latency and markout horizons.

For every source event:

1. record source exchange, local receive and generation timestamps;
2. record the latest destination state observable before submission;
3. submit or simulate the predefined destination action;
4. record submission, acknowledgement, cancellation and fill events;
5. measure destination outcomes at fixed event-time and wall-clock horizons;
6. recompute the outcomes under explicit artificial delays;
7. compare against causal destination-aware baselines.

Suggested controls include:

* previous source price-change sign;
* source and destination momentum;
* source and destination order-flow imbalance;
* realized volatility;
* destination spread and available depth;
* CEX–DEX basis;
* oracle update timing;
* gas price;
* block or sequencer position;
* time of day;
* funding and liquidation events.

The primary incremental test is:

[\operatorname{Outcome}_{DEX}\sim\text{destination controls}+\text{CEX controls}+\text{fixed source signal}.]

The relevant question is not whether the source signal correlates with a later DEX price. It is whether thefixedsource signal improves an execution-relevant destination outcome beyond information already observable at the destination.

## Public point-in-time records

Source records are mirrored asynchronously to a public, read-only, versioned Amazon S3 archive.

The browser listing is:

https://finaipub.s3.ap-southeast-1.amazonaws.com/?list-type=2&prefix=signals/

The object structure is:

signals/{symbol}/{engine_session}/{generation_timestamp}.json

For example:

signals/BTCUSDT/20260629_104323/1782730034703.json

Here:

* symbolis the source instrument;
* engine_sessionidentifies a continuous production-engine session and separates restarts or deployments;
* generation_timestampidentifies one point-in-time event record.

Each event object contains the available timestamps, individual model outputs, derived signals and the construct state needed to reconstruct the source-side sequence. Thedir_mrstate must be interpreted using the transition rules above: directional long/short signals open a state, while an opposing directional signal, opposing reversal, opposing swing or timeout closes it.

The complete public archive can be downloaded without an AWS account:

aws s3 sync s3://finaipub/signals/ \
 ./finai-signals/ \
 --no-sign-request

The archive generally becomes publicly available150–200 millisecondsafter local signal generation because upload is asynchronous. It is not part of the execution path and should not be used as a low-latency feed.

The archive exists for point-in-time inspection and independent reconstruction. S3 version history and separate market and generation timestamps make later modifications observable. We would welcome feedback on whether this is adequate research provenance or whether records should additionally be hash-chained and periodically anchored to Ethereum.

Researchers interested in a controlled replication can also request a read-only historical extract or research stream without charge for independent, non-commercial evaluation.

## Open questions

We would particularly value feedback on:

1. Which destination architecture provides the cleanest first falsification test: AMM, RFQ or Ethereum-secured order book/Validium?
2. What is the most defensible adverse-selection outcome for comparing incompatible venue designs?
3. How should event-time source signals be aligned with sequencer-time or block-time destination outcomes?
4. Which latency sweep is realistic rather than artificially favourable?
5. How should missed fills, partial fills and cancellation races enter the evaluation?
6. Which oracle, basis and destination-flow controls are essential?
7. Should source records be hash-chained or periodically anchored on Ethereum?
8. Are any researchers or venue teams interested in independently reproducing or extending this experiment?

We developed the source system and therefore have an obvious conflict of interest. We are not offering a token, investment product or trading service in this post. The purpose is to determine whether a measurable source-market relationship survives contact with a materially different execution mechanism.

1 Like