---
title: Compute Scarcity Is Permanent. Build a Ladder. — Casey West
url: https://caseywest.com/compute-scarcity-is-permanent-build-a-ladder/
site_name: tldr
content_file: tldr-compute-scarcity-is-permanent-build-a-ladder-casey
fetched_at: '2026-08-16T06:01:00.236205'
original_url: https://caseywest.com/compute-scarcity-is-permanent-build-a-ladder/
author: Casey West
date: '2026-08-16'
description: Every resilience pattern you know assumes the machine shows up. Accelerator scarcity breaks that assumption, and the pattern catalogs have not caught up. Here is the Compute Fallback Ladder—an ordered set of rungs your workload can run on, a selector that picks the highest obtainable one, and a promotion path back up when capacity returns.
tags:
- tldr
---

Read the reliability documentation for any major cloud and you’ll find, sitting under everything else, one quiet assumption: the hardware you ask for will be there. AWS writes it down. Its Well-Architected reliability pillar states that“the cloud is designed to be nearly limitless, so it’s the responsibility of AWS to satisfy the requirement for sufficient networking and compute capacity.”That is not a throwaway line. It’s a contract, and for fifteen years it held.

Then everyone tried to buy the same accelerators at the same time.

If you’ve shipped anything touching a GPU or a TPU lately, you already know the assumption cracked. You ask for an eight-GPU node in the region your data lives in, and the API tells you to wait. Notno—wait. The capacity simply isn’t there this hour, and no amount of retry logic will conjure it. Every resilience pattern you know how to build assumes the machine shows up. This one doesn’t.

A word on why, for anyone who doesn’t live in the hardware weeds. A GPU—NVIDIA’s H100 and its successors are the ones you’ve heard of—is a general-purpose parallel accelerator with its own bank of high-bandwidth memory soldered right next to the compute. A TPU is Google’s application-specific chip, built for the matrix math that dominates machine learning and wired into large, tightly-networked pods. What makes both of them scarce is the same bottleneck: the high-bandwidth memory and the advanced packaging that binds it to the die are capacity-limited across the entire industry. You can’t fix that with a bigger cloud budget or a patient retry loop. The constraint is upstream of you, upstream of your cloud provider, and it isn’t clearing this fiscal year.

I want to argue something the pattern catalogs haven’t caught up to yet:compute scarcity is the permanent condition, not the emergency.Demand for these chips is climbing faster than the packaging lines that build them, and packaging capacity takes years to add. So stop waiting for the shortage to end. Build for it. I call the discipline for building inside it theCompute Fallback Ladder.

## The Slot in the Catalog Is Empty

Go look at the three big pattern catalogs and ask a narrow question:which pattern treats “the compute I want may be unobtainable” as its problem statement?Azure’s Cloud Design Patternsrun to about forty entries. Throttling, Rate Limiting, Queue-Based Load Leveling—those governdemandagainst capacity you’re assumed to have. Circuit Breaker, Bulkhead, Retry—those keep youupwhen a dependency misbehaves. Deployment Stamps, Geode—those scale youout, which presumes there are nodes to scale out onto. Google Cloud’s reliability pillar tells you to build for high availability through redundancy and to take advantage of horizontal scalability. AWS, as we saw, names its own assumption directly.

Not one of them names supply acquisition as the thing that can fail. The demand axis is covered. The uptime axis is covered. The utilization axis is covered. The question of whether you canget the hardware at allis a gap in the vocabulary. That gap is the AWS quote turned into an architecture diagram: a whole discipline organized around a premise that no longer always holds.

## What the Ladder Is

The Compute Fallback Ladder is an ordered set of substitution rungs a workload descends when its preferred compute is unobtainable, plus the machinery to climb back up when capacity returns.

The rungs.An explicit, ordered list of execution targets, best to worst: preferred accelerator, then an alternate accelerator, then a smaller or quantized model that fits a cheaper chip, then CPU, then a cached or approximate answer. Each rung trades fidelity or latency for a better chance of actually running. Notice the bottom rungsaregraceful degradation—cached answers, reduced-capability modes. The Ladder doesn’t compete with load shedding and brownout; it contains them as its lowest steps.

The selector.A policy that picks the highest obtainable rung at request or schedule time, not at deploy time. Choose your fallback when you write the config and you’re guessing at a capacity picture that’s hours stale; choose it when the request arrives and you’re responding to the hardware that exists this second.

The promotion mechanism.When the preferred rung frees up, the system climbs back. Leave this out and “ladder” mis-describes the thing—you’ve built a one-way slide into degradation, and you’ll be serving int4 answers on CPU long after the H100s came back. The climb is what makes it a ladder instead of a trapdoor.

A shipping reference implementation already exists. TheGKE customComputeClasslets you declare a fallback-priority hierarchy of node configurations and will actively migrate a workload back to a preferred configuration once it frees. That’s rungs plus a selector plus promotion, running in production today. It influences autoscaling but isnotconsulted by the Kubernetes scheduler, so it’s the mechanism, not the whole story—but the pattern is no thought experiment. Someone already built the object.

Patterns that stick tend to share this trait. Circuit Breaker and Bulkhead were named in Michael Nygard’s 2007 bookRelease It!, but they didn’t become everyone’s vocabulary until the libraries showed up—Netflix’s Hystrix in 2012, then Polly, then Resilience4j—each shipping a class you could import with that name printed on it. Names spread through code, not citations. So I built the rest: acompanion repothat wires the full ladder end to end—theComputeClasshierarchy above, plus the selector and the climb-back—and runs it against a live GKE cluster, so you can read the object instead of taking my word for the pattern. “Capacity Airlock” and “Scarcity Governor” have no such object behind them.

### What the Object Actually Says

Three things fell out of building it that I wouldn’t have gotten from writing
about it.

The ladder is an ordered list, and the floor is a field you must declare.The GKE object states the rungs as a priority list, tried top to bottom:

1
apiVersion
: 
cloud.google.com/v1
2
kind
: 
ComputeClass
3
metadata
:
4
 
name
: 
fallback-ladder-example
5
spec
:
6
 
priorities
:
7
 
- 
machineType
: 
a3-highgpu-8g
 
# rung 0: 8x H100, the preferred rung
8
 
- 
machineType
: 
a2-highgpu-8g
 
# rung 1: 8x A100
9
 
- 
machineType
: 
g2-standard-48
 
# rung 2: L4
10
 
- 
machineFamily
: 
n4
 
# floor: CPU-only, broadly available
11
 
whenUnsatisfiable
: 
ScaleUpAnyway
12
 
nodePoolAutoCreation
:
13
 
enabled
: 
true
14
 
activeMigration
:
15
 
optimizeRulePriority
: 
true

whenUnsatisfiableis where this bites. Omit it and the API server sets it for
you:DoNotScaleUp. The manifest I first wrote was silent about it, and silence
means GKE placesnothingwhen the top rung is unobtainable—the Pod sitsPendingwithNotTriggerScaleUp, and the class reportsCrdMisconfigured. A
ladder whose floor is “serve nothing” is not a ladder.ScaleUpAnywayis what
makes it descend. The default is the opposite of the pattern, so declare the
field on purpose.

activeMigrationis the other half, and it’s the half that earns the wordladder. WithoptimizeRulePriority, GKE climbs back: when a preferred rung’s
capacity returns, it provisions a node there, cordons and drains the lower one,
moves the workload up, and deletes what it drained. Without that field you have
a slide, not a ladder—every fall is permanent.nodePoolAutoCreationis what
lets the autoscaler build a node pool for whichever rung it descends or promotes
to; leave it at its default offalseand GKE can only use pools you already
made, reportingCrdMisconfiguredwhen none of them match.

Descent and promotion aren’t symmetric, and they shouldn’t be.GKE spells
this out inspec.autoscalingPolicy, whereconsolidationDelayMinutesgates how
long it waits before consolidating onto a better rung. That gate, not slow
machinery, dominates how long a climb-back takes.

The reference library makes the same asymmetry explicit—one knob for the climb,
none for the fall:

1
@dataclass
(
frozen
=
True
, 
slots
=
True
)
2
class
 
Policy
:
3
 
promotion_hysteresis: 
int
 
=
 
1
4
 
max_degraded_seconds: 
float
 
|
 
None
 
=
 
None

A higher rung must be observed obtainablepromotion_hysteresistimes in a row
before the selector climbs to it. Descent has no such gate and never will:
hysteresis on the way down would mean waiting on capacity you don’t have. You
damp the climb because a flapping capacity signal will thrash you between rungs;
you never damp the fall, because the fall is not a choice.max_degraded_secondsboundssilentdegradation—it fires an alert when you’ve been below the
preferred rung too long. It deliberately moves nothing. Automatic escape from a
degraded rung is exactly the thrash the hysteresis exists to prevent.

The climb-back takes minutes, and you should design for that.Against a live
GKE cluster, with an unobtainable top rung forcing descent and capacity then
restored, the full promotion cycle—provision the higher-rung node, cordon and
drain the lower one, move the Pod, delete the drained node—took5m41s. Not
instant. If your fallback logic assumes the climb-back is free, five minutes of
degraded serving per capacity event is the bill you didn’t budget for.

Each of those is a claim the repo can be held to. Theverification logrecords the session against a real cluster—every command and its output, including
the run where the floor behavior was wrong.

## The Mechanisms Already Ship

Every rung and the selector already exist as product. On Google Cloud, that stack isAI Hypercomputer, and the selector rung runs onGoogle Kubernetes Engine.CustomComputeClassis the selector and the promotion mechanism together—a declared fallback priority with active migration back to a preferred config—with the honest caveat that it “influences autoscaling, isn’t considered by the Kubernetes scheduler.” The acquisition rungs sit in theAI Hypercomputer consumption models.Spot VMsrun on excess capacity at up to 91% off, “best-effort,” preemptible “at any time.”DWS flex-startprovisions accelerators as needed for up to seven days: “Compute Engine makes a best-effort attempt to schedule the provisioning,” no capacity guarantee, you wait until it appears. Calendar mode andfuture reservationssecure the top rung—but conditionally: “very high assuranceif approved,” never unconditional. That “if approved” is contingent, which is exactly why you build the lower rungs rather than assume the top one.

The pattern is vendor-neutral, and Google Cloud is where it’s furthest along, but the pieces exist elsewhere too. AWS offersCapacity Blocks for MLandon-demand capacity reservationsfor the top rung andEC2 Spotfor the bottom; Azure hascapacity reservationsandSpot VMs. What none of them ship is the word for the discipline that arranges these into an ordered fallback with a climb-back.

## What This Stands On

The Ladder isn’t new physics. It generalizes ideas that supply-aware engineers have used for decades.

Cycle scavenging is nearly forty years old. Litzkow, Livny, and Mutka describedCondor, “a hunter of idle workstations,” at ICDCS in 1988—a scheduler that harvested compute wherever it happened to be idle. Backfill scheduling formalized fitting jobs into the gaps. Brownout, froman ICSE 2014 paper by Klein and colleagues, taught cloud applications to shed optional work and stay up under strain. These are genuinely supply-aware. What they share is scope: each is bound to one owned pool or one procurement channel—the idle workstations you already have, the queue you already own.

The Ladder’s contribution is to promotesupply itselfto a first-class design variable across every channel at once: spot, on-demand, reserved, another region, another cloud, a smaller model, the CPU already sitting there.

## The Free Resilience Isn’t Free

Build for preemption and you’ll hear you got crash resilience for free: the checkpointing that survives a spot eviction should survive a node dying. Don’t count on it. Checkpoint/restart wasformalized for failures first, and a 2021 position paper found the libraries “evidently not fault tolerant” until you harden them deliberately. Apeer-reviewed spot-provisioning designgoes further, running on interruptible capacity while avoiding fault-tolerance mechanisms on purpose. The dividend is real, but you engineer it in.

## When Not to Build This

Every rung is code you write, test, and maintain. Every degraded mode is a product decision and a user-facing contract. Promotion logic is a control loop that can oscillate. Those costs are only worth paying under specific conditions.

Build it when the workload is business-critical,andthe preferred hardware is genuinely scarce—frontier accelerators today, not general-purpose CPU in a healthy region—andan outage costs more than the engineering to avoid it.

Don’t build it when capacity is reliably there, which is still most CPU workloads most of the time. Don’t build it for latency-insensitive batch that can simply wait in a queue; Dynamic Workload Scheduler flex-start already lands that work whenever capacity appears, no ladder required. A single rung is not a ladder, and building five when you need one is its own failure. Rigor you don’t need is a cost, not a virtue.

The Ladder is the acquisition side of scarcity—getting a chip at all. Its neighbor is the utilization side: once you hold the hardware, how much you get out of it. I wrote about that separately inYour Agents Aren’t Too Insecure. They’re Too Awake., on why the economics of packing agents onto GKE live in the lifecycle rather than the box. Adjacent problems, not a series—but if you’re rationing accelerators, you are probably fighting both at once.

## Decide Before the Capacity Vanishes

The catalogs will catch up. The supply-acquisition slot is too obviously empty to stay empty, and the limitless-capacity assumption is too obviously strained to survive another hardware cycle unquestioned. The only real choice is whether you meet the next stockout with a named, deliberate structure or discover your fallback behavior live, in an incident, at the worst possible time.

So name it. Draw the rungs. Decide, before the capacity vanishes, what your system does when the preferred chip isn’t there—which substitute it reaches for, how it selects, and how it climbs back. The mechanisms to wire it to are already shipping and already best-effort—a deliberate order of fallbacks beats a single hopeful request. Accept the constraint, then engineer the dividend—starting this week, from thecompanion repoand the config you can already write.

 
 
 
* architecture
* gpu
* tpu
* kubernetes
* gke
* capacity-planning
* design-patterns
 
 
Share: