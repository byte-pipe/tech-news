---
title: Cold Starts Are Dead - DEV Community
url: https://dev.to/aws/cold-starts-are-dead-5fod
site_name: devto
content_file: devto-cold-starts-are-dead-dev-community
fetched_at: '2026-05-01T03:52:27.446425'
original_url: https://dev.to/aws/cold-starts-are-dead-5fod
author: Eric D Johnson
date: '2026-04-29'
description: It never fails. Every time I talk about serverless, someone pushes back with the cold start argument.... Tagged with serverless, aws, lambda, coldstarts.
tags: '#serverless, #aws, #lambda, #coldstarts'
---

Sub-100ms performance for Go and Rust

It never fails. Every time I talk about serverless, someone pushes back with the cold start argument. I still see it in forums, in blog comments, in architecture review meetings. "Sure, but what about cold starts?"

I get it. Five or six years ago, that was a legitimate concern.

But it's 2026. The data tells a different story. And if you're still making decisions based on the cold start argument, you're arguing against a version of Lambda that hasn't existed in years.

## How Long Are Lambda Cold Starts in 2026?

Let's start with what cold starts actually look like today. These numbers come fromproduction workloads observed in the wild, not synthetic hello-world tests. Your mileage will vary by package size, initialization code, and memory configuration, but the ranges are representative of what teams are seeing in 2026.

Runtime

P50

P99

Notes

Python 3.13

200-400ms

800ms-1.2s

Fastest scripting runtime

Node.js 22

200-350ms

600ms-1s

Solid general choice

Go

50-100ms

150-250ms

Near-zero

Rust

50-80ms

100-200ms

Fastest overall

Java 21 (no SnapStart)

2-5s

6-10s

Still slow without SnapStart

Java 21 + SnapStart

90-140ms

200-400ms

Dramatically better

Running on arm64 (Graviton)? Knock another15-40% off those numbersacross the board.

Rust cold starts have beenmeasured as low as 16mson arm64. Sixteen milliseconds, which is less a cold start problem and more a rounding error.

The scripting runtimes, Python and Node, land in the 200-400ms range at P50. For context, that's less than the time it takes your browser to render a page after receiving the HTML.

## Does VPC Still Cause Lambda Cold Starts?

This one still comes up in conversations, and it frustrates me because it was solved in 2019.

The old problem: when a Lambda function needed VPC connectivity, AWS had to create an Elastic Network Interface (ENI) on the fly. That meant 10-15 seconds of additional cold start latency on top of everything else. VPC-connected Lambda was genuinely painful.

AWS fixed this when Lambdamigrated to Firecracker microVMs in 2019, dropping cold start overhead from over ten seconds to under a second. Werner Vogels recently wrote aboutthe invisible engineering behind Lambda's network. The team used eBPF to rewrite Geneve tunnel headers, taking tunnel latency from 150 milliseconds to 200microseconds. The VPC cold start penalty now approaches zero for most workloads.

That was seven years ago. If someone tells you Lambda cold starts are bad because of VPC, they're working from outdated information.

## How Much Does SnapStart Reduce Cold Starts?

Java was the poster child for the cold start argument. And honestly, it earned that reputation. A Spring Boot app on Lambda could take3-10 seconds to cold start. That's painful no matter how you frame it.

SnapStart changed the math. Here's the timeline:

* November 2022: SnapStart GA for Java at re:Invent
* November 2024: Python 3.12+ and .NET 8+ GA
* 2025: Expanded to additional regions, arm64 support

How it works: Lambda takes a snapshot of the initialized Firecracker microVM after your INIT code runs. That snapshot gets cached across three tiers: L1 on the worker, L2 in the placement group, S3 at the region level. On cold start, Lambda restores from the snapshot instead of re-running your initialization code.

The benchmarks are real:

* Python (Flask, LangChain, Pandas):several seconds → sub-second
* Java Spring Boot:5.8s → 180ms(97% reduction)
* .NET:58-94% cold start reduction

SnapStart has continued to evolve.Python and .NET supportwent GA in late 2024, with additional regions and arm64 support following in 2025.

## Did the Lambda INIT Billing Change Increase Costs?

In August 2025, AWSstandardized billing for the Lambda INIT phase. Functions packaged as ZIP files with managed runtimes now get billed for the INIT phase, which was previously free. This triggered some alarming blog posts.

The headline claim: a "22x cost increase." Let's look at the math.

That 22x number requires a perfect storm of worst-case assumptions:

* 100% cold start rate (every invocation is a cold start)
* 2-second Java INIT duration
* 512MB memory configuration

Here's the problem with that scenario:AWS's own production analysisshows cold starts occur in less than 1% of invocations.Not 100%. Less than 1%.

AWS's own assessment: "most users will see minimal impact on their overall Lambda bill from this change, as the INIT phase typically occurs for a very small fraction of function invocations." The actual impact depends on your cold start ratio and INIT duration relative to handler duration. Use the CloudWatch query below to check your own numbers.

Don't take my word for it. AWS published a CloudWatch Logs Insights query so you can calculate your exact impact:

filter
 
@
type
 
=
 
"REPORT"

|
 
stats

 
sum
((
@
memorySize
/
1000000
/
1024
)
 
*
 
(
@
billedDuration
/
1000
))
 
as
 
BilledGBs
,

 
sum
((
@
memorySize
/
1000000
/
1024
)
 
*
 
((
@
duration
 
+
 
@
initDuration
 
-
 
@
billedDuration
)
/
1000
))
 
as
 
UnbilledInitGBs
,

 
UnbilledInitGBs
 
/
 
(
UnbilledInitGBs
 
+
 
BilledGBs
)
 
as
 
UnbilledInitRatio

Enter fullscreen mode

Exit fullscreen mode

Run that against your own functions. If yourUnbilledInitRatiois anywhere near the number that would produce a 22x increase, you have a bigger problem than billing changes. You have an architecture problem.

With SnapStart enabled, INIT durations drop to sub-second, which shrinks that ratio even further.

## I Decided to See for Myself

I wasn't satisfied citing someone else's numbers for a post called "Cold Starts Are Dead." So I built a benchmarker. Thirteen Lambda functions across six runtimes, both arm64 and x86_64, 50 cold start invocations each, 512MB memory, us-west-2. Minimal hello-world handlers, no frameworks, no dependencies beyond the runtime SDK. This measures the platform floor, not application init time.

Runtime

Arch

P50 (ms)

P99 (ms)

Blog Claim

Verdict

Rust

arm64

14.1

31.9

50-80ms

⚡ Faster

Rust

x86_64

17.0

29.3

50-80ms

⚡ Faster

Go

arm64

45.0

61.2

50-100ms

⚡ Faster

Go

x86_64

59.8

94.9

50-100ms

✅ Verified

Python 3.13

arm64

88.3

147.1

200-400ms

⚡ Faster

Python 3.13

x86_64

106.2

142.3

200-400ms

⚡ Faster

Node.js 22

arm64

121.5

168.5

200-350ms

⚡ Faster

Node.js 22

x86_64

155.0

231.3

200-350ms

⚡ Faster

Java 21

arm64

365.3

539.2

2-5s

⚡ Faster

Java 21

x86_64

443.8

573.5

2-5s

⚡ Faster

Every runtime came in at or below the production ranges I cited earlier. That's expected. Those production numbers include application dependencies, framework initialization, and SDK client setup. My minimal handlers isolate just the platform overhead. Think of these as the floor: your cold starts will be at least this fast, plus whatever your initialization code adds.

The arm64 advantage verified cleanly too:

Runtime

arm64 P50

x86_64 P50

Improvement

Rust

14.1ms

17.0ms

17% faster

Go

45.0ms

59.8ms

25% faster

Python

88.3ms

106.2ms

17% faster

Node.js

121.5ms

155.0ms

22% faster

Java

365.3ms

443.8ms

18% faster

17-25% faster across every runtime. If you're still deploying on x86_64 in 2026, you're leaving performance on the table for no reason.

I also tested VPC vs non-VPC with the Python function. The VPC-connected function was 1.4msfasterat P50, within noise.

One honest caveat: SnapStart on my minimal Java handler showed a ~670ms restore duration. That's because there's almost nothing to snapshot. The restore mechanism's own overhead dominates. For a Spring Boot app where SnapStart eliminates 3-5 seconds of framework init, you'd see the dramatic improvement the benchmarks above describe. SnapStart's value scales with how much init work your app does.

Thefull benchmarker is open source on GitHub. You can run it yourself:

git clone https://github.com/singledigit/lambda-benchmark.git

cd 
lambda-benchmark
sam build 
&&
 sam deploy 
--guided

cd 
orchestrator
python benchmark.py 
--stack-name
 <stack> 
--iterations
 50
python generate_report.py

Enter fullscreen mode

Exit fullscreen mode

## When Do Lambda Cold Starts Still Matter?

Here's where cold starts still matter.

But first, is 200ms even slow? For a website, a chat app, an API powering a mobile experience, an AI agent? You won't notice it. A typical page load involves DNS resolution, TLS handshake, and content rendering that add up to far more than 200ms. If you're building AI agents, the LLM call alone takes 2-10 seconds, so 200ms of cold start is a rounding error on that. It's the first request after a quiet period, and it happens in less time than a blink.

The cases where cold starts actually matter are narrow:

Sub-10ms latency SLAs.If you're building for high-frequency trading or real-time bidding, 200ms of cold start latency is unacceptable. At that point, you're probably looking at containers on ECS or EKS where you control the warm pool directly. Provisioned Concurrency is an option too, but it has its own cost tradeoffs.

Very spiky, unpredictable traffic with strict P99 requirements.If your traffic pattern goes from zero to thousands of concurrent invocations with no ramp-up, and you have hard P99 latency SLAs, cold starts will hit that tail. You have options: containers with pre-scaled task counts, Provisioned Concurrency, or accepting slightly higher P99s during the initial burst. The right answer depends on your cost tolerance and how strict "strict" actually is.

Java without SnapStart.Just... use SnapStart. If you're running Java on Lambda without SnapStart enabled, you're choosing to have a cold start problem. The fix is a configuration change.

The honest framing: the question isn't "do cold starts exist?" They do. The question is "do they matter for your workload?" For the vast majority of workloads, the answer is no.

## Conclusion

VPC cold starts were fixed in 2019, and SnapStart took Java from 5 seconds to 180 milliseconds. Python and Node sit under 200ms on arm64, and AWS's own data says cold starts happen in less than 1% of invocations. I built a benchmarker and tested it myself. The production claims are conservative, and the numbers are better than advertised.

The cold start argument had its day. That day was 2018. If you're still leading with it, I get it, it used to be real. But the data has moved on, and it's time we did too.

## For the Agents

If you're using an AI coding assistant or agent, I've put together a companion skill file for this post. It includes the 2026 cold start benchmarks, SnapStart configurations, and the CloudWatch query for INIT billing analysis. Everything your agent needs to give you accurate cold start guidance instead of outdated advice.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse