---
title: 'Beyond Page One: Building a Highly Robust SEO Lead Generation Agent with Python and SerpApi🤖 - DEV Community'
url: https://dev.to/rafajrg21/beyond-page-one-building-a-highly-robust-seo-lead-generation-agent-with-python-and-serpapi-331h
site_name: devto
fetched_at: '2025-11-17T11:07:54.308314'
original_url: https://dev.to/rafajrg21/beyond-page-one-building-a-highly-robust-seo-lead-generation-agent-with-python-and-serpapi-331h
author: Rafael Romero
date: '2025-11-14'
description: Introduction As a SEO consultant or agency owner, finding actionable leads is a constant... Tagged with ai, python, gemini, tooling.
tags: '#ai, #python, #gemini, #tooling'
---

## Introduction

As a SEO consultant or agency owner, finding actionable leads is a constant hustle. The obvious Page 1 opportunities are highly competitive so the real opportunity is on Google Page 2 and beyond, where basic SEO mistakes by local businesses are common.

This post describes how I created a production-ready Python agent (depending on your definition) that:

* Scrapes targeted SERP pages (Page 2+)
* Performs instant on-page audits (H1, local NAP, etc.)
* Generates a personalized sales pitch for every failure

The project focuses on three pillars of production code: Efficiency, Precision, and Robustness.

## Phase 1 — Core Logic: Efficiency & Data Gathering

Scaling Google searches is the primary challenge. I used SerpApi to avoid scraping blocks and programmatically target long-tail local queries defined inserp_config.py(a combination ofCITIESandKEYWORDS). I tried making a free version with open source tools but it was a huge failure, so SerpApi really did the heavy lifting here.

Key takeaway: target Page 2+ instead of Page 1. Use CLI arguments to control which pages to scan and iterate thestartparameter.

# The SerpApi parameters in serpapi_extractor

params

=

{


# ... other parameters ...


"
start
"
:

current_rank
,

# page offset (0=Page 1, 10=Page 2, etc.)


"
num
"
:

10

}

# Iterate from start_page to end_page (increase by 10 per page)

for

current_rank

in

range
(
start_index
,

(
end_page

*

10
),

10
):


# ... API call ...

Enter fullscreen mode

Exit fullscreen mode

## Phase 2 — From Raw Data to Actionable Targets: Precision

After the data extraction we are presented with two main problems:

1. Duplicate URLs (same company ranking for multiple queries)
2. Irrelevant directories (e.g., Yelp, YellowPages)

So how did we handle these cases:

Deduplication

* Convert raw results to a DataFrame
* Normalize URLs (striphttp://,https://,www.)
* Keep the entry with the best (lowest) rank

Filtering directories

* Exclude known directory domains to avoid wasted audits and false positives.

# Directory filter example (from __main__ section)

directory_domains

=

[


'
yelp.com
'
,

'
google.com/maps
'
,

'
yellowpages.com
'
,


'
facebook.com
'
,

'
linkedin.com
'

]

def

is_directory
(
url
):


return

any
(
domain

in

url
.
lower
()

for

domain

in

directory_domains
)

cleaned_df
[
'
Is_Directory
'
]

=

cleaned_df
[
'
URL
'
].
apply
(
is_directory
)

cleaned_df_filtered

=

cleaned_df
[
cleaned_df
[
'
Is_Directory
'
]

==

False
].
drop
(
columns
=
[
'
Is_Directory
'
])

Enter fullscreen mode

Exit fullscreen mode

## Phase 3 — The Critical Audit: Robustness & Personalization

Direct audits are fragile: sites block bots or return transient errors. Initial runs produced many leads caused byConnectionErrororHTTP 403(technical failures, not SEO misses). Two enhancements fixed this:

1. CLI automation* Replaceinput()withargparseso the script can run non-interactively (e.g.,python agent.py 2 5).
2. Retry mechanism* Retry transient request errors up tomax_retriesand record real audit failures only after retries fail.

# Retry snippet from run_on_page_audit

for

attempt

in

range
(
max_retries
):


try
:


response

=

requests
.
get
(
url
,

headers
=
headers
,

timeout
=
10
)


response
.
raise_for_status
()

# raises HTTPError for 4xx/5xx


break

# success


except

requests
.
exceptions
.
RequestException

as

e
:


# Retry logic...


if

attempt

==

max_retries

-

1
:


audit_data
[
'
H1_Status
'
]

=

f
"
Error: Request Failed (
{
e
.
__class__
.
__name__
}
)
"


return

audit_data

Enter fullscreen mode

Exit fullscreen mode

## Sales Pitch Generation

Thegenerate_sales_pitchfunction turns audit failures into tailored outreach messages. It targets common failures like:

* Missing H1
* Missing NAP (Name, Address, Phone)
* Server errors / blocked pages

Each CSV row (audited URL) becomes a qualified sales opportunity with a targeted pitch.

## Conclusion and Next Steps

This agent provides a powerful foundation for automated SEO lead generation. It is highly efficient in its use of paid API credits, precise in its targeting, and robust enough to handle the realities of web scraping. The output is a highly qualified list of prospects ready for immediate outreach.

As a Frontend Developer primarily focused on JavaScript, I’m thrilled with how this project turned out! Python is a huge, yet rewarding, undiscovered land of possibilities for me. Collaborative tools like Gemini were essential, providing a step-by-step path to bring this script to an acceptable, production-ready state.

I believe open sourcing this kind of tool benefits the whole developer community. You can find the full, production-ready code, including the agent.py and instructions on how to set up serp_config.py, on GitHub:Seo Agent on Github

I'd love to hear your experiences and ideas!

Have you used automation for lead generation? What other on-page checks do you find most effective for a quick audit? Or is there a tool that you use that I can take inspiration from?

Let me know what improvements should I make! Drop a comment below or open an Issue on the repo to share your thoughts and suggestions.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
