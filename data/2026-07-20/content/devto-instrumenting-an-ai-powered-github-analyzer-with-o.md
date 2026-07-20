---
title: Instrumenting an AI-Powered GitHub Analyzer with OpenTelemetry and SigNoz - DEV Community
url: https://dev.to/divyasinghdev/instrumenting-an-ai-powered-github-analyzer-with-opentelemetry-and-signoz-55l3
site_name: devto
content_file: devto-instrumenting-an-ai-powered-github-analyzer-with-o
fetched_at: '2026-07-20T11:58:08.159118'
original_url: https://dev.to/divyasinghdev/instrumenting-an-ai-powered-github-analyzer-with-opentelemetry-and-signoz-55l3
author: Divya
date: '2026-07-17'
description: 'This article is my submission for the Agents of SigNoz Hackathon: Blog Track, where participants... Tagged with opentelemetry, signoz, observability, ai.'
tags: '#opentelemetry, #signoz, #observability, #ai'
---

Tracks 52-second delays and 40k token usage

This article is my submission for theAgents of SigNoz Hackathon: Blog Track, where participants instrument real applications with OpenTelemetry and SigNoz to make AI systems observable.

## Meet GitIntel

GitIntel is an AI-powered GitHub repository analyzer that usesGemini 2.5 Flashto evaluate repositories and generate a comprehensive developer assessment. Given a GitHub username and selected repositories (atmost 5), it analyzes code across eight engineering dimensions: architecture, security, testing, documentation, complexity, and engineering practices to build both repository-level insights and an overall developer profile.

The idea was straightforward: Combine GitHub data with an LLM to understand not just what the code does, but what it says about the developer behind it.

## Why Observability Became Essential

As GitIntel evolved, every analysis became a multi-step workflow involving GitHub API requests, asynchronous file fetching, prompt construction, multiple Gemini API calls, response aggregation, and report generation.

From the user's perspective, it was just oneAnalyzebutton.

From the application's perspective, it was a distributed pipeline.

That mismatch quickly became a problem.

Some repository analyses consumed nearly 40,000 Gemini tokens, while others finished with fewer than 4,000. End-to-end latency ranged from 8 secs to 52 secs, even for repositories that appeared similar.

My application logs already gave me useful information. I could see total token usage, overall analysis duration, GitHub rate-limit status, and when requests succeeded or failed.

But they couldn't answer many other questions like:

* Which step inside the analysis was taking the longest?
* Which Gemini batch caused the latency spike?
* How did GitHub API time compare with Gemini processing time?
* Which repository was driving token usage?
* What was the application doing immediately before a failure occurred?

I had the outcomes.

I didn't have the execution story.

Terminal logs told me what happened. They couldn't show me how the entire pipeline behaved or where time was actually being spent. Every optimization still involved a degree of guesswork.

That's when I decided to instrument GitIntel withOpenTelemetryand useSigNozas the observability backend.

## Instrumenting GitIntel with OpenTelemetry & SigNoz

To make GitIntel observable, I instrumented the application with OpenTelemetry and connected it to a self-hosted SigNoz instance.

Instead of treating the application as a black box, I could now trace every request end-to-end from GitHub API calls to Gemini interactions, while correlating traces, metrics, and logs in a single place. The result was complete visibility into latency, token usage, failures, retries, and the overall execution flow.

In this article, I'll share the setup, the instrumentation process, the challenges I encountered, the insights observability uncovered, and how you can reproduce the same environment on Ubuntu.

## Project Links

Live Demo:GitIntel

Source Code:

## Divya4879/Github-Analyzer

### Turn any GitHub username into a scored developer profile. AI-powered, instant, shareable.

# GitIntel

AI-powered GitHub profile analyzer. Enter a username, select up to 5 repos, and get a deep code assessment powered by Gemini 2.5 Flash; with full observability via OpenTelemetry and SigNoz.

Live demo:gitintel-2kh2.onrender.com

Built for theAgents of SigNoz Hackathon: Blog Track.

## Features

* AI code assessment: scores each repo across 8 dimensions: code quality, architecture, security, test coverage, documentation, complexity, engineering practices, and overall
* Developer profile: cross-repo analysis with maturity level (Junior → Staff), strengths, weaknesses, and growth areas
* Side-by-side comparison: compare two GitHub profiles against each other
* Downloadable assessment card: export your full results as a PNG with your GitHub profile picture and all scores
* Real-time streaming: analysis progress streamed live via SSE, no page refresh needed
* Full observability: traces, metrics, and logs via OpenTelemetry exported to SigNozGemini token usage tracked per repo (gemini.tokens.total,gemini.tokens.prompt,gemini.tokens.completion)…
* Gemini token usage tracked per repo (gemini.tokens.total,gemini.tokens.prompt,gemini.tokens.completion)
* …

View on GitHub

## Development Environment

Component

Stack

Backend

Python 3.12, FastAPI, Uvicorn

AI

Gemini 2.5 Flash (
google-genai
)

Data Fetching

GitHub REST API, 
aiohttp
 (10 concurrent workers)

Observability

OpenTelemetry SDK + Self-hosted SigNoz

Frontend

HTML, CSS, Vanilla JavaScript

Platform

Ubuntu 24.04 LTS, Docker & Docker Compose

## Prerequisites

Before getting started, make sure you have the following ready:

* System:Ubuntu 24.04, Python 3.12, Docker, and Docker Compose v2.
* GitHub Personal Access Token:Visithttps://github.com/settings/tokens, generate aClassic Personal Access Token, and enable therepoandread:userscopes. GitIntel uses this token to fetch repository contents and public profile information.
* Gemini API Key:Generate one athttps://aistudio.google.com/apikey. The free tier is sufficient since GitIntel usesgemini-2.5-flash, which is both fast and cost-effective. Just avoid analyzing several large repositories back-to-back if you're using the free quota.

Before continuing, verify that your environment is set up correctly:

python3 
--version
 
# should be 3.12.x

docker 
--version
 
# 20+ is fine

docker compose version

Enter fullscreen mode

Exit fullscreen mode

Ifdocker compose versionfails, you're most likely using the legacydocker-compose (v1). Install Docker Compose v2 with:

sudo 
apt-get 
install 
docker-compose-plugin

Enter fullscreen mode

Exit fullscreen mode

## Part 1: Fork and Run

1) Start by forking the repository on GitHub, then clone your fork locally:

 git clone https://github.com/YOUR_USERNAME/Github-Analyzer
 
cd 
Github-Analyzer

Enter fullscreen mode

Exit fullscreen mode

2) Create a virtual environment and install the project dependencies:

 python3 
-m
 venv venv
 
source 
venv/bin/activate
 pip 
install
 
-r
 requirements.txt

Enter fullscreen mode

Exit fullscreen mode

3) Next, create your environment file:

 
cp
 .env.example .env
 nano .env

Enter fullscreen mode

Exit fullscreen mode

4) Update it with your GitHub token, Gemini API key, and OpenTelemetry configuration:

 GITHUB_TOKEN=ghp_yourtokenhere
 GEMINI_API_KEY=AIzaSy_yourkeyhere
 OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
 OTEL_SERVICE_NAME=gitintel

Enter fullscreen mode

Exit fullscreen mode

OTEL_EXPORTER_OTLP_ENDPOINTpoints to the SigNoz OpenTelemetry Collector, which we'll set up in Part 2. Don't worry if it isn't running yet—the application works perfectly fine without it.

5) Now start the application:

 uvicorn main:app 
--reload

Enter fullscreen mode

Exit fullscreen mode

6) Openhttp://localhost:8000, enter any GitHub username, select a few repositories, and clickAnalyze.

You'll get a complete developer assessment: repository scores, developer profile, strengths, weaknesses, and the generated report.

At this point, the application is fully functional.

But there's one problem:-

You still have no idea what happened behind the scenes. The terminal logs show you total token counts and overall duration, but not which batch cost what, not per-step timing, not which API call took 30 of those 40 secs, and not why one repo took 5x longer than another.

The results are there. The why isn't.

The application gives you the results, but none of the answers.

That's exactly whatPart 2solves.

## Part 2: Self-Hosting SigNoz

One of the reasons I chose SigNoz is that it's Open Source, OpenTelemetry-native, and can be self-hosted in just a few mins. That meant I could keep my entire observability stack running locally while developing GitIntel, without relying on any third-party SaaS.

The repo already includes a complete Docker Compose configuration underpours/deployment/compose.yaml. Spinning it up launches everything GitIntel needs to collect, process, store, and visualize telemetry:

1. SigNoz UI & API:- Runs on port 8080, providing the web interface for exploring traces, metrics, logs, and dashboards.
2. OpenTelemetry Collector:- Listens on4317 (gRPC)and4318 (HTTP), receiving telemetry exported from GitIntel.
3. ClickHouse:- The high-performance database that stores traces, metrics, and logs.
4. ClickHouse Keeper:- Handles coordination for the ClickHouse cluster.
5. Postgres:- Stores SigNoz metadata and configuration.

Start the entire stack with:

cd 
pours/deployment
docker compose up 
-d

# Verify everything is healthy

docker compose ps

Enter fullscreen mode

Exit fullscreen mode

The first startup usually takes around 60 secs, as ClickHouse needs a little time to initialize.

Once everything is ready, openhttp://localhost:8080.

At this point, the SigNoz dashboard will load, but it will be empty. That's expected because GitIntel hasn't exported any telemetry yet.

Now restart GitIntel so it can connect to the OpenTelemetry Collector:

cd
 ../..

source 
venv/bin/activate
uvicorn main:app 
--reload

Enter fullscreen mode

Exit fullscreen mode

With both GitIntel and SigNoz running, analyze any GitHub repository.

As soon as the analysis begins, GitIntel starts exporting telemetry through the OpenTelemetry Collector. Within a few seconds, a new service namedgitintelautomatically appears underServicesin SigNoz.

No manual registration, configuration, or dashboard creation is required, the service is discovered automatically from the OpenTelemetryservice.nameresource attribute configured in the application.

OpenServices → gitintel, and you'll immediately see live application health, including:

## Part 3:- How the Instrumentation Works

With SigNoz up & running, the next step is teaching GitIntel what telemetry to collect and where to send it.

Instead of scattering observability code throughout the project, I centralized everything in a single file:telemetry.py. One setup function initializes traces & metrics then exports them to the OpenTelemetry Collector using OTLP/gRPC on port 4317.

# telemetry.py

OTLP_ENDPOINT
 
=
 
os
.
getenv
(
"
OTEL_EXPORTER_OTLP_ENDPOINT
"
,
 
"
http://localhost:4317
"
)

SERVICE_NAME
 
=
 
os
.
getenv
(
"
OTEL_SERVICE_NAME
"
,
 
"
gitintel
"
)

resource
 
=
 
Resource
.
create
({
"
service.name
"
:
 
SERVICE_NAME
})

def
 
setup_telemetry
(
app
):

 
otlp_available
 
=
 
OTLP_ENDPOINT
 
!=
 
"
http://localhost:4317
"
 
or
 
os
.
getenv
(
"
OTEL_ENABLED
"
)

 
tracer_provider
 
=
 
TracerProvider
(
resource
=
resource
)

 
if
 
otlp_available
:

 
tracer_provider
.
add_span_processor
(

 
BatchSpanProcessor
(

 
OTLPSpanExporter
(
endpoint
=
OTLP_ENDPOINT
,
 
insecure
=
True
)

 
)

 
)

 
trace
.
set_tracer_provider
(
tracer_provider
)

Enter fullscreen mode

Exit fullscreen mode

A few lines here do most of the heavy lifting.

TheResourcedefines the identity of the application by assigning it the service namegitintel. Every trace, metric, & log generated by the application carries this metadata, allowing SigNoz to group everything under a single service automatically.

TheBatchSpanProcessorbatches spans before exporting them to the OpenTelemetry Collector. Instead of sending every span individually, telemetry is exported efficiently in batches, reducing overhead during repository analysis.

Perhaps my favorite part is how little manual instrumentation was actually required.

FastAPIInstrumentor
.
instrument_app
(
app
)

RequestsInstrumentor
().
instrument
()

Enter fullscreen mode

Exit fullscreen mode

These two lines unlock a surprising amount of observability.

One small detail ended up being far more important than I expected:

otlp_available
 
=
 
OTLP_ENDPOINT
 
!=
 
"
http://localhost:4317
"
 
or
 
os
.
getenv
(
"
OTEL_ENABLED
"
)

Enter fullscreen mode

Exit fullscreen mode

During local development, GitIntel exports telemetry to the self-hosted SigNoz instance as expected.

When deployed to Render, however, there's no OpenTelemetry Collector running. Without this guard, the application would repeatedly try to export telemetry and flood the logs with connection refused errors every few seconds.

I only discovered that after deploying the project, so this check became a simple but an important one.

Once GitIntel starts with SigNoz running, openhttp://localhost:8080→ Services.

Because the service name is already defined in the OpenTelemetryResource, SigNoz automatically discoversgitinteland begins collecting telemetry immediately. Without writing a single dashboard query, you can already monitor:

* Request rate
* Error rate
* p50, p95, and p99 latency
* Endpoint-level performance

At this point, every request through GitIntel is visible, timed, and traceable.

## Custom Metrics:- Measuring What Actually Matters

Auto-instrumentation gives you excellent visibility into HTTP requests, but GitIntel isn't just another web application, it's a LLM-powered analysis pipeline.

Knowing that an endpoint took 12 secs is useful, but it doesn't answer the questions I actually cared about.

* How many Gemini tokens did this repository consume?
* Which repository was the most expensive to analyze?
* How many files and lines of code were processed?
* How close am I to GitHub's rate limit?
* How long does a complete assessment actually take?

To answer those questions, I created eight custom OpenTelemetry instruments intelemetry.py:

# telemetry.py

github_ratelimit_gauge
 
=
 
meter
.
create_gauge
(
"
github.ratelimit.remaining
"
)

gemini_tokens_counter
 
=
 
meter
.
create_counter
(
"
gemini.tokens.total
"
,
 
unit
=
"
tokens
"
)

gemini_prompt_tokens_counter
 
=
 
meter
.
create_counter
(
"
gemini.tokens.prompt
"
,
 
unit
=
"
tokens
"
)

gemini_completion_tokens_counter
 
=
 
meter
.
create_counter
(
"
gemini.tokens.completion
"
,
 
unit
=
"
tokens
"
)

files_processed_counter
 
=
 
meter
.
create_counter
(
"
github.files.processed
"
)

loc_processed_counter
 
=
 
meter
.
create_counter
(
"
github.loc.processed
"
,
 
unit
=
"
lines
"
)

assessment_duration_histogram
 
=
 
meter
.
create_histogram
(
"
assessment.duration
"
,
 
unit
=
"
s
"
)

api_error_counter
 
=
 
meter
.
create_counter
(
"
api.errors
"
)

Enter fullscreen mode

Exit fullscreen mode

Each instrument captures a different aspect of GitIntel's execution, from LLM token usage and GitHub rate limits to assessment latency and processing volume. Together, they provide a much more complete picture than HTTP metrics alone.

One implementation detail turned out to be particularly valuable.

Every token counter includes the repository name as an attribute.

# gemini_client.py — _track_usage()

def
 
_track_usage
(
usage
,
 
repo
:
 
str
):

 
pt
 
=
 
getattr
(
usage
,
 
"
prompt_token_count
"
,
 
0
)
 
or
 
0

 
ct
 
=
 
getattr
(
usage
,
 
"
candidates_token_count
"
,
 
0
)
 
or
 
0

 
gemini_prompt_tokens_counter
.
add
(
pt
,
 
{
"
repo
"
:
 
repo
})

 
gemini_completion_tokens_counter
.
add
(
ct
,
 
{
"
repo
"
:
 
repo
})

 
gemini_tokens_counter
.
add
(
pt
 
+
 
ct
,
 
{
"
repo
"
:
 
repo
})

Enter fullscreen mode

Exit fullscreen mode

That small{"repo": repo}attribute completely changes how useful the data becomes.

Without it, I'd only know GitIntel consumed 50,000 tokens.

With it, I can immediately identify which repository consumed 38,000 of those tokens, compare repositories side by side, and focus optimization efforts where they'll have the biggest impact.

In observability, context is just as important as the metric itself.

GitHub's remaining API quota is tracked in a similar way.

# github_client.py 

remaining
 
=
 
resp
.
headers
.
get
(
"
X-RateLimit-Remaining
"
)

if
 
remaining
 
is
 
not
 
None
:

 
github_ratelimit_gauge
.
set
(
int
(
remaining
))

Enter fullscreen mode

Exit fullscreen mode

GitHub conveniently includes the remaining rate limit in every API response header. Updating the gauge here means it's always current without making any additional API requests.

## Visualizing the Data in SigNoz

Once telemetry starts flowing, openMetrics → Query Builderin SigNoz.

Here are the visualizations I found most useful:

* gemini.tokens.totalgrouped by therepoattribute as a bar chart to compare token consumption across repositories.
* assessment.durationas a time-series to monitor latency and identify slow analyses.
* github.ratelimit.remainingas a time-series to watch the remaining API quota decrease during consecutive analyses.

These dashboards quickly answered questions that were impossible to answer before instrumentation:

* Which repositories are the most expensive?
* Which analyses take the longest?
* Am I approaching GitHub's API limit?
* Where should I optimize first?

## Bringing Everything Together

Finally, I combined these visualizations into a custom dashboard namedGitIntel LLM Observability.

Instead of jumping between multiple pages, I now have a single view showing token usage, GitHub rate-limit headroom, request latency, and overall application health every time I open SigNoz.

## Manual Spans:- Tracing the Entire Analysis Pipeline

Auto-instrumentation is fantastic for HTTP requests, but it doesn't know anything about your application's business logic.

It can't tell you:

* Which repository is being analyzed.
* How many source files were processed.
* How large the LLM prompt was.
* Which Gemini call was slow.
* Where the request actually spent its time.

To answer those questions, I addedmanual spansaround the critical parts of GitIntel's analysis pipeline.

For every Gemini request,gemini_client.pycreates a span that records both the repository being analyzed and the size of the prompt sent to the model.

# gemini_client.py 

def
 
_call_gemini
(
prompt
:
 
str
,
 
repo
:
 
str
)
 
->
 
str
:

 
with
 
tracer
.
start_as_current_span
(

 
"
gemini.generate
"
,

 
attributes
=
{

 
"
gemini.repo
"
:
 
repo
,

 
"
gemini.prompt_chars
"
:
 
len
(
prompt
),

 
},

 
):

 
for
 
attempt
 
in
 
range
(
5
):

 
try
:

 
response
 
=
 
client
.
models
.
generate_content
(

 
model
=
MODEL
,

 
contents
=
prompt
,

 
)

 
_track_usage
(
response
.
usage_metadata
,
 
repo
)

 
return
 
response
.
text

 
except
 
Exception
 
as
 
e
:

 
api_error_counter
.
add
(
1
,
 
{
"
service
"
:
 
"
gemini
"
,
 
"
repo
"
:
 
repo
})

 
if
 
attempt
 
==
 
4
:

 
raise

 
time
.
sleep
(
10
 
*
 
(
attempt
 
+
 
1
))

Enter fullscreen mode

Exit fullscreen mode

Theprompt_charsattribute became surprisingly useful. While it isn't the exact token count (that's tracked separately as a metric), it's an excellent indicator of prompt size and makes it much easier to correlate larger prompts with longer response times.

I applied the same idea to GitHub.

Rather than simply tracing the HTTP requests, GitIntel recordsrepository-level metadataduring file collection.

# github_client.py

with
 
tracer
.
start_as_current_span
(

 
"
github.get_all_files
"
,

 
attributes
=
{

 
"
github.repo
"
:
 
f
"
{
owner
}
/
{
repo
}
"
,

 
"
github.branch
"
:
 
branch
,

 
},

):

 
span
 
=
 
trace
.
get_current_span
()

 
span
.
set_attribute
(
"
github.file_count.total
"
,
 
len
(
tree
))

 
span
.
set_attribute
(
"
github.file_count.source
"
,
 
len
(
source_files
))

Enter fullscreen mode

Exit fullscreen mode

By attaching these attributes directly to the span, every trace now includes useful context such as:

* Which repository was analyzed
* Which branch was scanned
* Total files discovered
* Source-code files actually processed

That context makes the trace far more useful than a simple timeline of function calls.

When everything runs together, one repository analysis produces a distributed trace that looks like this:

api.analyze
├── github.get_user (github.username)
├── github.get_repos
├── github.get_all_files (file_count.total, file_count.source)
├── gemini.assess_repo (github.repo, file_count)
│ ├── gemini.generate (prompt_chars - batch 1)
│ └── gemini.generate (prompt_chars - batch 2, large repos only)
└── gemini.developer_profile
 └── gemini.generate

Enter fullscreen mode

Exit fullscreen mode

Instead of seeing a single request that took 42 seconds, I can now see exactly where those 42 seconds were spent.

Open Traces -> Filter byapi.analyzeand select any request.

The trace expands into the full execution tree, showing every nested span, its duration, and its metadata.

Click on anygemini.generatespan, and the details panel immediately shows attributes such as:

* gemini.repo
* gemini.prompt_chars
* Start time
* End time
* Duration

This was the moment observability finally clicked for me.

The problem was never that GitIntel was slow. The problem was that I had no visibility intowhyit was slow.

With distributed tracing, that mystery disappeared.

## Part 4:- What the Telemetry Revealed

At this point, GitIntel was fully instrumented. The real question wasn't whether telemetry was flowing, it was whether it could answer the questions I actually cared about.

To make the differences obvious, I ran analyses on two repositories with very different characteristics:

* Repository A:a small project with fewer than 30 source files.
* Repository B:a much larger project with well over 100 source files.

Seeing these runs side by side is where observability becomes valuable. The contrast makes latency spikes, token usage, and processing costs immediately visible instead of hidden behind a single loading spinner.

### 1. Token Usage Wasn't Even Close

The first thing that stood out was token consumption.

Some repositories finished after a single Gemini request, while larger ones required multiple batches, causing token usage to increase dramatically.

Instead of guessing why one analysis was expensive, I could see exactly which repository consumed the most tokens and correlate that with the trace.

### 2. Latency Was Driven by the LLM

Before instrumentation, all I knew was that some analyses took 10 secs while others took nearly a minute.

Distributed traces showed exactly where that time was spent.

GitHub requests completed relatively quickly, while one or moregemini.generatespans dominated the overall request duration.

Rather than treating the request as a single slow operation, I could pinpoint the specific step responsible for the delay.

### 3. GitHub Wasn't the Bottleneck

One assumption I had before adding telemetry was that downloading hundreds of files from GitHub would dominate the execution time.

The traces showed otherwise.

Repository fetching remained relatively fast, even for larger projects. Most of the end-to-end latency came from prompt generation and LLM inference.

That insight completely changed where I would spend time optimizing GitIntel.

### 4. Rate Limits Became Predictable

Every GitHub API response updates thegithub.ratelimit.remaininggauge.

Instead of wondering how close I was to GitHub's limit, I could watch it decrease in real time during consecutive analyses.

This makes it much easier to decide when to slow requests, introduce caching, or back off before hitting the hourly quota.

### 5. One Dashboard Told the Whole Story

After creating a custom dashboard, I no longer needed to jump between traces, metrics, and logs.

One screen showed:

* overall request latency,
* Gemini token consumption,
* GitHub rate-limit headroom,
* assessment duration,
* and application health.

Instead of debugging reactively, I could monitor GitIntel proactively.

## What Surprised Me

Three things surprised me after instrumenting GitIntel:

* GitHub wasn't the bottleneck. Gemini inference dominated overall latency.
* Repository size wasn't a reliable predictor of token cost.Prompt structure and batching mattered just as much.
* One trace explained more than hundreds of log lines.Before SigNoz I could tell an analysis was slow. After SigNoz I knew exactly why it was slow.

Those are the kinds of insights I simply couldn't have gained without end-to-end observability.

## Why All of This Matters

Before adding observability, every failed analysis looked identical.

Something was slow.

Something failed.

Something used too many tokens.

I had no way of knowing where, why, or how expensive it was.

After instrumenting GitIntel with OpenTelemetry and SigNoz, every request became explainable.

Theprompt_charsspan attribute immediately shows which Gemini batch caused a latency spike. Therepoattribute on my custom metrics identifies exactly which repository consumed the most tokens. And because every log is correlated with its trace, I can see the complete execution path that led to a failure instead of staring at an isolated error message.

Observability didn't just make GitIntel easier to debug.

It made the application understandable.

That's the difference between using AI APIs and owning AI infrastructure.

## Two Big Problems I Faced

This wouldn't be a completely honest engineering blog if everything worked perfectly the first time.

It didn't.

These were the two issues that cost me the most time, and the fixes that finally made the setup reliable.

### Problem 1:- OpenTelemetry Connection Spam on Render

After deploying GitIntel to Render, my application logs were immediately flooded with this message every few seconds:

WARNING opentelemetry.exporter.otlp.proto.grpc.exporter Transient error
StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317,
retrying in 0.82s. Failed to connect to remote host: Connection refused

Enter fullscreen mode

Exit fullscreen mode

The reason was simple.

Render wasn't running SigNoz, so nothing was listening onlocalhost:4317.

OpenTelemetry kept retrying indefinitely, filling the logs with connection errors and making it difficult to spot genuine application issues.

The fix was a small guard insidetelemetry.py:

otlp_available
 
=
 
OTLP_ENDPOINT
 
!=
 
"
http://localhost:4317
"
 
or
 
os
.
getenv
(
"
OTEL_ENABLED
"
)

Enter fullscreen mode

Exit fullscreen mode

If the exporter endpoint is still the default localhost address andOTEL_ENABLEDhasn't been explicitly enabled, GitIntel simply skips creating the OTLP exporters altogether.

That means:

* Local development with SigNoz:telemetry exports normally.
* Production deployment on Render:no exporter, no retry loop, no noisy logs.

One condition removed hundreds of unnecessary log messages.

### Problem 2:- SigNoz Wasn't Receiving Data After Startup

The second issue was much more confusing.

I started the entire SigNoz stack successfully.

The application launched.

Requests completed normally.

But theServicespage remained completely empty.

The problem wasn't OpenTelemetry at all.

It was startup timing.

Although the containers report as running almost immediately afterdocker compose up -d, ClickHouse still needs roughly a minute to finish initializing before it can persist telemetry. During that window, the OpenTelemetry Collector accepts incoming spans, but the backend isn't fully ready to store them.

The solution was simply to wait until every container reported a healthy state before launching GitIntel.

cd 
pours/deployment
docker compose up 
-d

# Wait until all services are healthy - takes ~60 seconds

docker compose ps

# Look for (healthy) on:

# signoz-signoz-0

# signoz-telemetrystore-clickhouse-0-0

# signoz-telemetrykeeper-clickhousekeeper-0

# signoz-metastore-postgres-0

cd
 ../..
uvicorn main:app 
--reload

Enter fullscreen mode

Exit fullscreen mode

After starting the application, I ran a single repository analysis and waited another 15-20 secs.

That's expected. SigNoz batches telemetry before writing it to storage.

If the Services page is still empty after about half a minute, the fastest way to diagnose the issue is to inspect the Collector logs:

cd 
pours/deployment
docker compose logs ingester 
--tail
=
20

Enter fullscreen mode

Exit fullscreen mode

Once the first spans appear, everything behaves normally from that point onward.

The delay only affects the initial startup while the telemetry backend finishes initializing.

### What I Learned

Neither of these bugs had anything to do with GitIntel itself.

They were observability infrastructure problems.

Ironically, building observability meant I first had to debug the observability stack.

Once those issues were solved, though, every repository analysis became traceable, measurable, and far easier to reason about. And that's exactly the point of instrumenting an AI application, we spend less time guessing and more time understanding what our system is actually doing.

### 1. Auto-Instrumentation Gets You Started. Custom Instrumentation Gives You Answers.

OpenTelemetry's auto-instrumentation gave me immediate visibility into GitIntel. With just a few lines of code,FastAPIInstrumentorandRequestsInstrumentorautomatically traced every FastAPI request and every outbound GitHub API call. Latency, status codes, request rate; they were all available without touching my application logic.

That was a great starting point, but it wasn't enough.

Auto-instrumentation could tell me that a request took 52 secs. It couldn't tell me why.

The real value came from the telemetry I added myself. Attributes likeprompt_chars,repo, and file counts transformed traces and metrics into something I could actually reason about. Instead of seeing a slow request, I could identify which Gemini batch was responsible. Instead of seeing total token usage, I could pinpoint exactly which repository consumed the most tokens. And because every log was correlated with its trace, a single click showed the complete execution path leading to a failure.

The biggest lesson I took away is this:

Auto-instrumentation gives you visibility. Custom instrumentation gives you understanding.

### 2. Instrument Before You Need It

When I started GitIntel, I almost skipped observability altogether. I wanted to finish the project first and "add monitoring later."

I'm glad I didn't.

The unexpected 40,000-token analyses, the OpenTelemetry exporter spam on Render, the ClickHouse cold-start delay, and the huge latency differences between repositories would all have looked like random bugs without traces and metrics. Instead of guessing, I always had evidence pointing me in the right direction.

Observability also changed how I think about metrics. A global token count wasn't nearly as useful as attaching arepoattribute to every measurement. A retry log became far more valuable once it was linked to the exact distributed trace that produced it. Every small piece of context made debugging dramatically easier.

The biggest shift wasn't technical, it was mental.

I stopped asking, "Why is my app behaving like this?" and started asking, "What does the telemetry tell me?"

That's a much better question.

## Conclusion

Building GitIntel taught me that integrating an LLM is only half the problem. Understanding what the application is doing in production is the other half.

With OpenTelemetry and SigNoz, every repository analysis became observable from end to end. I could follow GitHub API requests, inspect Gemini calls, measure token usage, monitor latency, correlate logs with traces, and identify failures, all from a single platform.

That's what observability should do: replace assumptions with evidence.

If you're building applications powered by LLMs, agents, or external APIs, don't wait until production to add telemetry. Instrument them from day one. The first time something behaves unexpectedly, you'll be glad you did.

Because in the end,you can't optimize what you don't measure, you can't debug what you can't see, and you don't truly own an AI system until you can observe it.

## Thank You

At last but not the least, I want to send out a huge thank you to everyone who made this possible. A massive shoutout goes to the organizers of the Agents of SigNoz Hackathon and the engineering team behind SigNoz for building an incredible open-source, OpenTelemetry-native platform that makes deep observability genuinely fun to work with. I also want to thank the community at WeMakeDevs for fostering such an energetic environment for builders, as well as Dev.to for providing a clean, developer-first space to share these engineering stories. And finally, thank you to you, my readers; for taking the time to read through my experience. Let's keep building, learning along the way, and growing everyday!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse