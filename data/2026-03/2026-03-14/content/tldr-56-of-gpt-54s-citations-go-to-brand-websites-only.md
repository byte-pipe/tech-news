---
title: 56% of GPT-5.4's Citations Go to Brand Websites. Only 8% of GPT-5.3's Do. - Writesonic Blog
url: https://writesonic.com/blog/chatgpt-citation-study-gpt-5-4-vs-gpt-5-3
site_name: tldr
content_file: tldr-56-of-gpt-54s-citations-go-to-brand-websites-only
fetched_at: '2026-03-14T06:00:33.437241'
original_url: https://writesonic.com/blog/chatgpt-citation-study-gpt-5-4-vs-gpt-5-3
author: Samanyou Garg
date: '2026-03-14'
published_date: '2026-03-08T11:44:28+00:00'
description: We analyzed 1,161 ChatGPT citations across 119 conversations. GPT-5.4 cites brand websites 7x more than GPT-5.3. Same question, completely different sources.
tags:
- tldr
---

* Generative Engine Optimization (GEO)

# 56% of GPT-5.4’s Citations Go to Brand Websites. Only 8% of GPT-5.3’s Do.

We tested 50 prompts across ChatGPT's new models and extracted every fan-out query, web search result, and citation. GPT-5.3 sends users to blog posts about your brand. GPT-5.4 sends them to your actual website. The two models cite 93% different sources.



Written By:

Samanyou Garg

Last Updated:

March 9, 2026

17 Mins

 read


ChatGPT just rolled out two new models. GPT-5.3 Instant is the new default. GPT-5.4 Thinking is the new premium.

I wanted to know: do they search the web differently? Do they cite different sources? And what does that mean for brands trying to show up in AI search?

To find out, I tested 50 prompts across both models, extracted every fan-out query they sent, and classified every citation they returned.

Here’s the short version:GPT-5.3 sends users to blog posts about your brand. GPT-5.4 sends them to your actual website.Same question. Completely different outcomes.

Here’s the long version.

## How we did this

We ran 50 prompts on ChatGPT across GPT-5.3 Instant (the new default), GPT-5.4 Thinking (the new premium), and GPT-5.2 Instant and GPT-5.2 Thinking as baselines. That gave us 119 total conversations.

After each response, we extracted the full conversation JSON using ChatGPT’s internal API. This exposed every fan-out query the model sent, every web search result it received, and every citation URL it included in its answer.

We also ran 30 of these queries through both Bing and Google via SerpAPI to compare ChatGPT’s results against traditional search engines.

What we measured
Count
Total conversations
119
Fan-out queries extracted
532
Web search results analyzed
7,896
Citations classified
1,161
AI response words reviewed
74,478
SerpAPI queries (Bing + Google)
30

Our 50 prompts spanned 16 categories: SaaS, ecommerce, healthcare, finance, travel, education, home, food, legal, marketing, productivity, fitness, shopping intent, comparisons, and trends.

For each product or service prompt, we classified citations as “first-party” (the actual brand’s website, likehubspot.comfor HubSpot) or “third-party” (review sites, blogs, Reddit, media outlets).

Now, here’s what we found.

## GPT-5.3 and GPT-5.4 cite completely different sources

This is the headline finding.

56% of GPT-5.4’s citations go to brand websites. Only 8% of GPT-5.3’s do.

And here’s the part nobody expected:GPT-5.3 is worse for brands than GPT-5.2 was.The previous default cited brand websites 22% of the time. The new default dropped to 8%.

Put another way: the model most ChatGPT users interact with now sends 92% of citation traffic to third-party sites.

### The pattern holds across almost every prompt

This isn’t a statistical edge case. Look at what happens when you ask both models the same question:

Prompt
GPT-5.3 first-party %
GPT-5.4 first-party %
GPT-5.3 cites
GPT-5.4 cites
Best CRM for B2B SaaS
0%
100%
designrevision.com
,
techradar.com
hubspot.com
,
salesforce.com
,
attio.com
Marathon running shoes
0%
88%
irunfar.com
,
reddit.com
nike.com
,
asics.com
,
hoka.com
QuickBooks vs Xero vs FreshBooks
0%
100%
gentlefrog.com
,
technologyadvice.com
freshbooks.com
,
quickbooks.intuit.com
,
xero.com
HubSpot vs Salesforce vs Pipedrive
0%
100%
emailtooltester.com
,
salesflare.com
hubspot.com
,
pipedrive.com
,
salesforce.com
Password managers
14%
100%
cybernews.com
,
reddit.com
1password.com
,
bitwarden.com
,
dashlane.com
iPhone vs Samsung vs Pixel
0%
100%
tomsguide.com
,
phonearena.com
apple.com
,
samsung.com
,
store.google.com
Tesla vs BMW vs Polestar
0%
67%
drivingelectric.com
,
facebook.com
tesla.com
,
bmwusa.com
,
polestar.com
Smart home security
0%
86%
safehome.org
ring.com
,
wyze.com
,
simplisafe.com
Coursera vs Udemy vs LinkedIn
0%
83%
coursmos.com
,
airmeet.com
udemy.com
,
coursera.org
,
linkedin.com
EHR software
0%
40%
forbes.com
,
techradar.com
athenahealth.com
,
elationhealth.com
Email marketing platforms
33%
88%
techradar.com
,
insiderone.com
klaviyo.com
,
omnisend.com
,
mailchimp.com
SEO tools
0%
33%
apricornsolutions.com
,
morningscore.io
ahrefs.com
,
semrush.com
,
screamingfrog.co.uk
Notion vs Obsidian vs Roam
0%
100%
xp-pen.com
,
medium.com
obsidian.md
,
notion.so
,
roamresearch.com

On comparison prompts (“X vs Y vs Z”), GPT-5.3 never cited a single brand. GPT-5.4 cited brands 83-100% of the time.

### The first-party gap varies by category

Head-to-head comparisons show the biggest gap: 0% on GPT-5.3 vs 83% on GPT-5.4. SaaS sees a 7x improvement (12% to 82%). Even shopping, where GPT-5.4 is least brand-forward, still doubles the first-party rate.

### And the models cite almost none of the same sources

For the same prompt, GPT-5.3 and GPT-5.4 cite completely different websites.

Average citation overlap across all 50 prompts:7%.

On 22 of 50 prompts, the overlap was exactly 0%. Being visible on GPT-5.3 gives you no advantage on GPT-5.4.

This has massive implications for GEO and AEO strategy. A brand that dominates on GPT-5.3 might be invisible on GPT-5.4, and vice versa. Any AI visibility audit that only tests one model misses the picture entirely.

### The “kingmaker” sites on GPT-5.3

Because GPT-5.3 cites third-party sites almost exclusively, a small number of review and media domains become gatekeepers:

Domain
Citations
Type
forbes.com
15
Media/reviews
techradar.com
10
Tech reviews
tomsguide.com
10
Tech reviews
reddit.com
7
Forum/UGC
money.com
5
Finance media

If Forbes or TechRadar writes about your product, GPT-5.3 finds it. If they don’t, you’re probably invisible to the default model.

GPT-5.4’s top domains? The brands themselves:hubspot.com(18),shopify.com(16),salesforce.com(14),quickbooks.intuit.com(10).

## GPT-5.4 sends 8.5x more fan-out queries than GPT-5.3

The search architecture between these models is fundamentally different.

GPT-5.3 sends one query: the raw user prompt. GPT-5.4 decomposes it into 8.5 sub-queries on average, with domain restrictions and site: operators.

Here’s the full funnel:

Model
Avg queries
Avg web results
Avg citations
Avg response length
GPT-5.2 Instant
0.9
36.6
4.5
388 words
GPT-5.3 Instant
1.0
27.3
5.8
548 words
GPT-5.4 Thinking
8.5
109.4
14.8
769 words

GPT-5.4 also uses two features no other model uses: domain-restricted queries (148 total) and site: operators (156 total). Combined, that’s304 targeted queriesacross 50 prompts.

### What GPT-5.4’s fan-out queries actually look like

GPT-5.4 follows a consistent two-phase pattern: brand verification first, third-party validation second.

Email marketing platforms (21 queries):

Phase 1 (brand sites):

“2026 best email marketing platforms ecommerce pricing”

→ restricted to:klaviyo.com,omnisend.com,mailchimp.com

“site:klaviyo.com pricing email marketing sms ecommerce 2026”

“site:omnisend.com pricing ecommerce email marketing sms 2026”

Phase 2 (validation):

“G2 ecommerce email marketing software 2026”

→ restricted to:g2.com

“Shopify app store Klaviyo Omnisend Mailchimp reviews 2026”

→ restricted to:apps.shopify.com

iPhone vs Samsung vs Pixel (4 queries):

“Apple iPhone 17 Pro official specs” → [apple.com]

“Samsung Galaxy S26 Ultra official specs” → [samsung.com]

“Google Pixel 10 Pro official specs” → [store.google.com]

“The Verge review iPhone Samsung Pixel” → [theverge.com]

This is why GPT-5.4’s first-party citation rate is 56%. It goes to brand sites first, validates second.

### How much research does each category get?

Some categories trigger far more queries and citations than others on GPT-5.4:

Category
GPT-5.3 queries
GPT-5.4 queries
GPT-5.3 cited
GPT-5.4 cited
GPT-5.4 web results
Productivity
1.0
14.7
8.3
20.3
156
Marketing
1.0
11.7
6.3
25.0
144
Legal
1.0
12.5
8.0
15.0
165
Services
1.0
14.0
3.5
15.0
184
Travel
1.0
11.7
8.7
12.7
148
Education
1.0
10.0
6.0
17.7
130
Finance
1.0
8.3
6.0
17.7
130
SaaS
1.0
6.3
3.7
17.3
76
Comparison
1.0
9.3
6.3
14.3
99
Shopping
1.0
4.6
3.8
8.6
56
Fitness
1.0
4.0
4.7
10.7
64

B2B software categories (Productivity, Marketing, Legal) trigger the most queries on GPT-5.4. Consumer product categories (Fitness, Shopping) trigger fewer. This likely reflects the complexity of B2B purchasing decisions.

## Same search index, different query strategy

Are GPT-5.3 and GPT-5.4 searching different web indexes? Or the same one?

The data points to the same index.

Metric
GPT-5.3 Instant
GPT-5.4 Thinking
Avg queries per prompt
1.0
8.5
Avg web results per prompt
27.3
109.4
Web results per query
27.3
12.9

GPT-5.3 sends one broad query and gets ~27 results. GPT-5.4 sends 8.5 specific queries and gets ~13 results per query.

The per-query result count is lower for GPT-5.4 because its queries are more targeted. But the total result pool is 4x larger because it sends 8.5x more queries.

Bottom line? Same index, different decomposition. The fan-out strategy IS the difference.

## GPT-5.4’s site: operator changes the game for AEO

GPT-5.4 sent 156 queries with site: operators across 50 prompts. No other model used site: at all.

Here’s how all 423 queries break down:

Query type
Count
% of total
Purpose
Domain-restricted (brand sites)
142
34%
“Get pricing and features from this brand’s website”
site: operator queries
156
37%
“Validate against review sites”
Open (unrestricted)
125
30%
“Broad discovery”

Top sites GPT-5.4 validates brands against:

site: target
Queries
What GPT-5.4 checks
apps.shopify.com
6
App store reviews and ratings
g2.com
4
B2B software reviews
roamresearch.com
5
Product-specific docs
writesonic.com
3
Product pages and pricing

This matters for three reasons.

1. GPT-5.4 pre-selects which brands to investigate. Before sending any query, GPT-5.4 decides which brands are relevant based on its training data. If your brand isn’t in the consideration set, no amount of SEO will help.

2. Your G2 and Capterra presence feeds GPT-5.4 directly. G2 (8 queries) and Capterra (6 queries) are top validation targets. Strong profiles translate directly to AEO visibility.

3. site: queries create a verification loop. GPT-5.4’s process: identify brands from training data, check brand websites directly, validate on review platforms. Brands need coverage across all three layers.

## GPT-5.4 cites pricing pages 35x more than GPT-5.3

Different models don’t just cite different sources. They cite different page types.

Page type
GPT-5.3 Instant
GPT-5.4 Thinking
Pricing pages
4 (1%)
138 (19%)
Blog/article pages
92 (32%)
61 (8%)
Homepage/root pages
42 (15%)
161 (22%)
Product/feature pages
13 (5%)
73 (10%)

GPT-5.3 is a “blog reader.” 92 of its 284 citations (32%) point to blog posts and articles.

GPT-5.4 is a “pricing page checker.” 138 of its 739 citations (19%) point to pricing pages, 161 (22%) to homepages, 73 (10%) to product pages. Combined, 51% of GPT-5.4’s citations land on commercial pages.

4 pricing page citations on GPT-5.3 across 49 conversations. 138 on GPT-5.4 across 50. That’s 35x.

If your pricing page shows “contact sales” instead of actual numbers, GPT-5.4 will find the problem.

## Google rankings predict GPT-5.3 citations. GPT-5.4 bypasses rankings entirely.

Does ranking on Google or Bing help you get cited by ChatGPT?

Depends on the model.

We took 94 domains that GPT-5.3 cited across 9 prompts and checked whether each one also appeared in Bing or Google results for the same query (via SerpAPI).

47% of GPT-5.3’s citations come from domains that also rank on Google. Only 27% from domains on Bing.

But44% don’t appear on either search enginefor the same query. ChatGPT has its own retrieval layer.

### GPT-5.4 is a completely different story

We did the same analysis for GPT-5.4. The results were striking.

75% of GPT-5.4’s cited domains don’t appear in Bing OR Google results for the same user prompt.

Why? Because GPT-5.4 doesn’t find brands through traditional search. It knows them from training data, then sends domain-restricted queries directly to their websites.

When you ask about running shoes, GPT-5.4 doesn’t search “best marathon running shoes” and hopenike.comranks. It searches “[Nike Pegasus vs ASICS Gel Nimbus vs Brooks Ghost 2026]” restricted tonike.com,asics.com, etc.

Prompt
GPT-5.4 cited domains
On Bing/Google
NOT on Bing/Google
A2: Shopify vs WooCommerce
5
0 (0%)
5 (100%)
B2: Running shoes
8
2 (25%)
6 (75%)
C1: Marketing agencies
6
0 (0%)
6 (100%)

Bottom line? For GPT-5.3, invest in SEO (especially Google). For GPT-5.4, invest in brand recognition and first-party content quality. Search rankings don’t get you into GPT-5.4’s citation set.

## GPT-5.4 makes AI search attribution trackable for brands

Every cited URL gets ?utm_source=chatgpt.comappended. Combine that with the first-party citation rate and you get something interesting:

Model
First-party rate
UTM coverage
Trackable brand traffic
GPT-5.2 Instant
22%
60%
~13% of citations
GPT-5.3 Instant
8%
96%
~8% of citations
GPT-5.4 Thinking
56%
87%
~49% of citations

On GPT-5.3, the brand gets mentioned in the answer, but 92% of clicks go to Forbes, TechRadar, and Reddit. The brand gets the recommendation. Someone else gets the traffic.

On GPT-5.4, nearly half of all citation traffic goes to the brand’s own website with UTM tracking. The brand gets the recommendation AND the trackable visit.

This is the biggest attribution shift in GEO/AEO. For the first time, a thinking model makes AI search attribution comparable to paid search: the user clicks to your site, you track it in GA4.

Set up a segment for utm_source=chatgpt.comnow. As GPT-5.4 adoption grows, you’ll see this traffic appear.

## Some prompts don’t trigger web search at all

Before worrying about citations, worry about whether the model even searches.

Model
Prompts that didn’t search
GPT-5.2 Instant
1/10 (AI recruiting)
GPT-5.3 Instant
1/49 (AI recruiting)
GPT-5.4 Thinking
4/50 (AI recruiting, robot vacuums, standing desk deals, gift ideas)

Paradoxically, the model that searches deepest when it does search also skips more prompts entirely. GPT-5.4 skipped two shopping prompts (“Best deals on standing desks this week” and “I need to buy a gift for my wife under $100”).

But here’s what’s interesting:GPT-5.4 still cited sources when it didn’t search.The robot vacuum prompt had 17 citations from training data alone. GPT-5.3 produced zero citations when it didn’t search.

Prompts with a specific year (“in 2026”), price constraints (“under $500”), or comparison structure (“X vs Y”) triggered search 100% of the time on both models.

## Shopping intent behaves differently on GPT-5.4

We tested 5 explicit shopping prompts (“I want to buy…”, “Where can I buy…”, “Best deals on…”). The results surprised us.

Prompt
GPT-5.3 searched?
GPT-5.4 searched?
GPT-5.3 citations
GPT-5.4 citations
Buy earbuds under $150 for running
Yes
Yes
2
11
Cheapest MacBook Air M4
Yes
Yes
5
9
Best deals on standing desks
Yes
No
4
15 (from memory)
Gift for wife under $100
Yes
No
4
2 (from memory)
Best rated espresso machine under $500
Yes
Yes
4
6

GPT-5.3 searched for all 5 shopping prompts. GPT-5.4 skipped 2 of them.

GPT-5.4 treated “deals” and “gift” prompts as knowledge tasks, not search tasks. It answered from training data. This means time-sensitive shopping queries may not trigger web search on the thinking model.

For ecommerce brands: your deal pages and gift guides may get more visibility on GPT-5.3 than GPT-5.4. But when GPT-5.4 does search for products, it cites your product pages directly (soundcore.com,breville.com) while GPT-5.3 cites review sites (reddit.com,steamritual.com).

## GPT-5.3 surfaces older content than the previous default

Model
% under 30 days old
% under 90 days old
GPT-5.2 Instant
33%
52%
GPT-5.3 Instant
6%
27%
GPT-5.4 Thinking
18%
37%

GPT-5.3 retrieves dramatically less fresh content. Only 6% of its web search results are under 30 days old, compared to 33% on the previous GPT-5.2.

“Just publish more content” isn’t a winning AEO strategy for the new models. Comprehensiveness and quality matter more than recency.

## How to extract fan-out queries from any ChatGPT conversation

You can see exactly what queries ChatGPT sends and which domains it cites. Here’s how.

### Step 1: Have a ChatGPT conversation

Ask any question that triggers web search. Product comparisons, “best X” queries, anything with a year.

### Step 2: Open the console

Mac:Cmd + Option + J

Windows:Ctrl + Shift + J

### Step 3: Paste this script

(async () => {

const a = await fetch('/api/auth/session', { credentials: 'include' });

const b = await a.json();

const cid = window.location.pathname.split('/c/')[1];

const d = await fetch('/backend-api/conversation/' + cid, {

credentials: 'include',

headers: { 'Authorization': 'Bearer ' + b.accessToken }

});

const e = await d.json();

let queries = [], cited = 0, utmCount = 0, totalUrls = 0;

const domains = [];

for (const node of Object.values(e.mapping || {})) {

const m = node.message;

if (!m) continue;

if (m.content?.content_type === 'code' && m.content?.text) {

try {

const p = JSON.parse(m.content.text);

if (p.search_query) p.search_query.forEach(sq =>

queries.push({ q: sq.q, domains: sq.domains || [] })

);

} catch(err) {

const match = m.content.text.match(/search\("([^"]+)"\)/);

if (match) queries.push({ q: match[1], domains: [] });

}

}

if (m.metadata?.content_references) {

for (const ref of m.metadata.content_references) {

if (ref.items) ref.items.forEach(i => {

cited++; totalUrls++;

if (i.url?.includes('utm_source=chatgpt')) utmCount++;

try { domains.push(new URL(i.url).hostname.replace('www.','')); } catch(e){}

});

}

}

}

console.log('Model:', e.default_model_slug);

console.log('Fan-out queries:', queries.length);

queries.forEach((q, i) =>

console.log( ${i+1}. ${q.q}${q.domains.length ? ' [' + q.domains.join(', ') + ']' : ''})

);

console.log('Cited sources:', cited);

console.log('Cited domains:', [...new Set(domains)].join(', '));

console.log('UTM coverage:', utmCount + '/' + totalUrls);

})();

### What to look for

On GPT-5.3: You'll see 1 query (the raw prompt) and 3-8 cited domains, mostly third-party review sites.

On GPT-5.4: You'll see 4-20 queries with domain restrictions in brackets andsite:operators. Cited domains will be a mix of brand sites and review platforms.

Example output (GPT-5.4, CRM prompt):

Model: gpt-5-4-thinking

Fan-out queries: 7

1. best CRM for B2B SaaS 2026 HubSpot Salesforce [hubspot.com,salesforce.com]
2. site:hubspot.com pricing Sales Hub 2026
3. site:salesforce.com Sales Cloud pricing 2026
4. Attio CRM pricing features 2026 [attio.com]
5. Close CRM pricing 2026 [close.com]
6. G2 best CRM B2B SaaS 2026 reviews [g2.com]
7. Capterra CRM comparison small business [capterra.com]

Cited sources: 17

Cited domains:hubspot.com,salesforce.com,attio.com,pipedrive.com,close.com,freshworks.com

UTM coverage: 15/17

To extract from a conversation you're not viewing, replace the cid line with a hardcoded ID:

const cid = '69ac268b-1438-83a5-b143-b2063b416b79';

You can find conversation IDs in the URL:chatgpt.com/c/[conversation-id]

## The full picture: GPT-5.2 to GPT-5.3 to GPT-5.4

Capability
GPT-5.2 Instant
GPT-5.3 Instant
GPT-5.4 Thinking
First-party citation rate
22%
8% (worse)
56%
Third-party citation rate
78%
92%
44%
Avg queries per prompt
1
1
8.5
Domain-targeted queries
0
0
304
Avg web results per prompt
36.6
27.3
109.4
Avg cited sources
4.5
5.8
14.8
Pricing pages cited
1 (2%)
4 (1%)
138 (19%)
Blog posts cited
10 (22%)
92 (32%)
61 (8%)
Content freshness (% <30 days)
33%
6%
18%
Response length
388 words
548 words
769 words
Citations on Google (SerpAPI)
N/A
47%
N/A (bypasses)
Citations on neither engine
N/A
44%
~75%
Prompts that skipped search
1/10
1/49
4/50

The GPT-5.2 to GPT-5.3 shift looks incremental on the surface. Same query count. Similar citations. But GPT-5.3 is worse for brands (8% vs 22% first-party), worse for freshness (6% vs 33% under 30 days), and more blog-dependent (32% of citations are blog posts).

The GPT-5.2 to GPT-5.4 shift is structural. Domain-targeted queries. First-party-dominant citations. Pricing page reading. Multi-phase research. Everything about how the model searches changed.

## What this means for brands

1. Audit your pricing page first. GPT-5.4 cited 138 pricing pages across 50 prompts. It checks for actual numbers. "Contact sales" pages get skipped.

2. Build third-party coverage for GPT-5.3. The kingmaker sites: Forbes (15 citations), TechRadar (10), Tom's Guide (10), Reddit (7). If these sites don't mention you, GPT-5.3 won't either.

3. Your G2 and Capterra profiles matter for AEO. GPT-5.4 validates brands against these platforms. Weak profiles mean weaker citations.

4. Set up GA4 attribution now. Create a segment forutm_source=chatgpt.com. Coverage is 87-96% across new models.

5. Test both models. GPT-5.3 visibility and GPT-5.4 visibility are different things with 7% overlap. You need both.

6. Google rankings predict GPT-5.3 citations better than Bing. 47% of GPT-5.3's citations come from Google-ranked domains, 27% from Bing. For GPT-5.4, rankings don't matter much: 75% of cited domains aren't on either engine.

## What this means for agencies

1. Build model-level reporting. "Your client is cited 40% of the time" is incomplete. Report GPT-5.3 visibility (third-party-mediated) and GPT-5.4 visibility (first-party-driven) separately.

2. Run a two-track GEO/AEO service. Track 1: third-party distribution for GPT-5.3 users. Track 2: first-party content optimization for GPT-5.4 users.

3. Search rankings alone don't predict AI visibility. 44% of GPT-5.3's citations come from domains not on Google or Bing. For GPT-5.4, that number is 75%.

## Questions we're still investigating

What determines GPT-5.4's brand list? It pre-selects which brands to search before sending any query. Training data? Market share? We don't know yet.

What's the 44% that appears on neither Google nor Bing? Nearly half of GPT-5.3's citations don't rank on either search engine for the same query. OpenAI has a retrieval mechanism beyond traditional search.

Do multi-turn conversations change the pattern? All our prompts were single-turn. Follow-up questions might shift citation behavior.

## Methodology

Scope: 119 conversations onChatGPT, March 7-8, 2026.

Prompts: 50 unique prompts. All 50 tested on GPT-5.3 Instant and GPT-5.4 Thinking. 10 prompts also on GPT-5.2 Instant and GPT-5.2 Thinking.

Data: 532 fan-out queries, 7,896 web search results, 1,161 citations, 74,478 words.

SerpAPI: 30 queries through Bing US and Google US. For GPT-5.3, we mapped ChatGPT's cited domains against both engines. For GPT-5.4, we compared cited domains against Bing/Google results for the raw user prompt.

Classification: Citations to brand-related domains classified as "first-party." All others as "third-party." Page types classified by URL path. Freshness measured from publication date metadata.

Limitations: Single user account. ChatGPT is non-deterministic. Repeat runs may vary. The India-based account may have affected some results (amazon.inappearing in citations). GPT-5.2 data is from 10 prompts only.

## TLDR

GPT-5.4 cites brand websites 7x more than GPT-5.3 (56% vs 8%). It does this by decomposing prompts into 8.5 fan-out queries with domain restrictions and site: operators. The two models cite completely different sources (7% overlap).

For brands: fix your pricing page, build G2/Capterra profiles, and get third-party coverage on Forbes/TechRadar for GPT-5.3 users. For agencies: report visibility per model. They measure different things.

Ping me onLinkedInorXif you have questions.

We built the same analysis pipeline we used for this study into Writesonic. Track your citation share, monitor fan-out queries, and see which models cite your brand, all in one dashboard.See it in action →

Appendix: all 50 prompts

ID
Category
Prompt
A1
SaaS
What's the best CRM for a 50-person B2B SaaS company?
A2
SaaS
Compare Shopify vs WooCommerce vs BigCommerce for a DTC brand doing $5M in revenue
A3
SaaS
Best project management tools for remote engineering teams in 2026
B1
Ecommerce
Best noise cancelling headphones under $300 for working from home
B2
Ecommerce
What running shoes do marathon runners recommend in 2026?
B3
Ecommerce
Best organic skincare brands for sensitive skin
C1
Services
Best digital marketing agencies for ecommerce brands in the US
C2
Services
Top accounting software for small businesses with under 20 employees
D1
Trends
What are the biggest trends in ecommerce for 2026?
D2
Trends
How is AI changing the recruiting and hiring process?
E1
Healthcare
Best telehealth platforms for small medical practices in 2026
E2
Healthcare
What supplements do doctors recommend for sleep in 2026?
E3
Healthcare
Best EHR software for independent physicians in 2026
F1
Finance
Best business credit cards for startups with no revenue history
F2
Finance
Compare QuickBooks vs Xero vs FreshBooks for freelancers
F3
Finance
Best payroll software for small businesses with under 50 employees in 2026
G1
Travel
Best travel insurance companies for international trips in 2026
G2
Travel
Top hotel booking sites with the best price guarantees
G3
Travel
Best carry-on luggage brands for frequent business travelers
H1
Education
Best online learning platforms for professional development in 2026
H2
Education
Compare Coursera vs Udemy vs LinkedIn Learning for tech skills
H3
Education
Best coding bootcamps for career changers in 2026
I1
Home
Best smart home security systems under $500 in 2026
I2
Home
Top robot vacuums for pet owners in 2026
I3
Home
Best air purifiers for allergies recommended by doctors
J1
Food
Best meal delivery services for families in 2026
J2
Food
Top rated coffee subscription services
J3
Food
Best protein powder brands for muscle building in 2026
K1
Legal
Best contract management software for small businesses
K2
Legal
Top legal document automation tools in 2026
L1
Marketing
Best email marketing platforms for ecommerce brands in 2026
L2
Marketing
Compare HubSpot vs Salesforce vs Pipedrive for sales teams under 20 people
L3
Marketing
Best SEO tools for small business websites in 2026
M1
Productivity
Best AI writing tools for content marketers in 2026
M2
Productivity
Top password managers for small business teams
M3
Productivity
Best video conferencing software for remote teams in 2026
N1
Fitness
Best fitness trackers for marathon training in 2026
N2
Fitness
Top rated yoga mats for home practice
N3
Fitness
Best home gym equipment under $1000 in 2026
S1
Shopping
I want to buy wireless earbuds under $150 for running, what should I get?
S2
Shopping
Where can I buy the cheapest MacBook Air M4 right now?
S3
Shopping
Best deals on standing desks this week
S4
Shopping
I need to buy a gift for my wife under $100, what are good options?
S5
Shopping
Buy the best rated espresso machine under $500
V1
Comparison
Notion vs Obsidian vs Roam Research for personal knowledge management
V2
Comparison
iPhone 17 Pro vs Samsung Galaxy S26 Ultra vs Google Pixel 10 Pro
V3
Comparison
Tesla Model 3 vs BMW i4 vs Polestar 2 for daily commuting in 2026
T1
Trends
What are the top cybersecurity threats businesses should prepare for in 2026?
T2
Trends
How is AI changing the legal industry in 2026?
T3
Trends
What are the biggest challenges for DTC brands in 2026?

Like what you read? Share with a friend

## Subscribeand stay up to date

with the latest marketing tips and news



## Thank youfor Subscribing!

Exciting Updates Await.



Samanyou Garg

Founder @ Writesonic

Samanyou is the founder of Writesonic and is passionate about using AI to solve real world problems especially in marketing. Two years before the launch of ChatGPT, Writesonic was already at the forefront, helping brands, agencies, and individuals create and optimize all types of content, outsmart competitors by decoding their SEO trends and keywords to boost traffic.
Samanyou is a Forbes 30 Under 30 awardee and a winner of the 2019 Global Undergraduate Awards, often referred to as the junior Nobel Prize.



## Related Articles

Generative Engine Optimization (GEO)

## The 31-Point Citation Readiness Checklist: What Makes AI Actually Cite Your Content

### Drishti

March 12, 2026

12 Mins read



ChatGPT

Generative Engine Optimization (GEO)

## GPT-5.4 Replaced GPT-5.2. What Changed for Your Brand’s AI Visibility.

### Samanyou

March 6, 2026

6 Mins read



Generative Engine Optimization (GEO)

## GEO Expert Ethan Smith on AI Visibility: Attribution, Prioritization, and Why Startups Can Win

### Drishti

February 23, 2026

5 Mins read



Generative Engine Optimization (GEO)

## Josh Grant on GEO: “Product Moves Fast. Perception Moves Slow.”

### Drishti

February 23, 2026

7 Mins read



Generative Engine Optimization (GEO)

## Peec AI Actions vs Writesonic Action Center: Which One Helps Improve AI Visibility?

### Niyati

February 22, 2026

15 Mins read



Generative Engine Optimization (GEO)

## Profound Actions vs Writesonic Action Center: Which One Actually Gets Things Done?

### Niyati

February 22, 2026

16 Mins read



Generative Engine Optimization (GEO)

## Do YouTube Videos Help Brands Appear in AI-Generated Search Answers?

### Drishti

February 19, 2026

6 Mins read



Generative Engine Optimization (GEO)

## Top 7 AI Peekaboo Alternatives To Try in 2026

### Drishti

February 19, 2026

16 Mins read



Generative Engine Optimization (GEO)

## On-Page Generative Engine Optimization: How to Get Your Content Cited by AI

### Niyati

February 18, 2026

7 Mins read



Generative Engine Optimization (GEO)

## How to Use YouTube Descriptions for Answer Engine Optimization (AEO) in 2026

### Drishti

February 10, 2026

7 Mins read



Generative Engine Optimization (GEO)

## The Reddit Playbook for AI Visibility in 2026

### Samanyou

January 27, 2026

13 Mins read



Generative Engine Optimization (GEO)

## Writesonic vs AthenaHQ vs Profound: Which GEO Is The Best GEO Platform?

### Niyati

January 23, 2026

10 Mins read



Generative Engine Optimization (GEO)

## Writesonic vs Profound vs Scrunch AI: Which AI Visibility Tool Is Best in 2026?

### Niyati

January 23, 2026

9 Mins read



Generative Engine Optimization (GEO)

## GEO Team: To Hire or Not to Hire?

### Mariana

November 25, 2025

11 Mins read



Generative Engine Optimization (GEO)

## Writesonic vs Profound vs Peec: Which AI Visibility Tool Is Best in 2026?

### Pragati

January 23, 2026

10 Mins read



Generative Engine Optimization (GEO)

Research

## 2.4 Million Domains Study: UGC Platforms Own AI Citations

### Mariana

January 23, 2026

8 Mins read



Generative Engine Optimization (GEO)

## Profound vs Writesonic: Who Wins in 2026?

### Pragati

January 23, 2026

7 Mins read



Generative Engine Optimization (GEO)

## Top 12 LLM Tracking Tools for AI Visibility

### Pragati

March 13, 2026

18 Mins read



Generative Engine Optimization (GEO)

## Third-Party Placement Is the High-Margin AI Search Service Agencies Need

### Mariana

November 25, 2025

16 Mins read



Generative Engine Optimization (GEO)

Research

## Reviews Surge 8.9x in Troubleshooting Queries: The LLM Citation x Frame Study

### Mariana

November 25, 2025

6 Mins read



Generative Engine Optimization (GEO)

## Top 8 Writesonic Alternatives To Try in 2026

### Pragati

January 23, 2026

7 Mins read



Generative Engine Optimization (GEO)

## How to Make the Business Case for GEO in 2026

### Mariana

November 24, 2025

11 Mins read



Generative Engine Optimization (GEO)

## 9 Best Profound Alternatives To Boost Your AI Visibility [2026]

### Pragati

March 13, 2026

17 Mins read



Generative Engine Optimization (GEO)

## The 8 Best AI Visibility Tools to Win in 2026

### Pragati

January 23, 2026

18 Mins read



Generative Engine Optimization (GEO)

Research

## Listicles Drop 37%, Reviews Jump 637%: Branded vs Non-Branded Prompt Study

### Mariana

November 26, 2025

6 Mins read



Generative Engine Optimization (GEO)

## GEO vs SEO: What’s The Difference And Why It Matters?

### Niyati

January 23, 2026

16 Mins read



Generative Engine Optimization (GEO)

## 10 Best Answer Engine Optimization (AEO) Tools

### Pragati

February 20, 2026

21 Mins read



Generative Engine Optimization (GEO)

## Top 16 Generative Engine Optimization Tools To Try in 2026

### Pragati

February 20, 2026

24 Mins read



Generative Engine Optimization (GEO)

## How to Rank in AI Overviews: 7 Strategies to Win Google’s AIOs

### Pragati

November 13, 2025

12 Mins read



Generative Engine Optimization (GEO)

Research

## The LLM Citation Study: Does Your Industry Need a Special Content Strategy for AI?

### Mariana

November 24, 2025

7 Mins read



Generative Engine Optimization (GEO)

## The GEO Playbook for Agencies: How To Lead Your Clients Through the Next Era of Search

### Niyati

November 27, 2025

23 Mins read



Generative Engine Optimization (GEO)

## AI-Friendly Writing: How To Optimize Content for LLMs

### Pragati

November 11, 2025

13 Mins read



Generative Engine Optimization (GEO)

## How to Get Cited by AI: A Marketer’s Guide to Winning in AI Search

### Pragati

October 24, 2025

15 Mins read



Generative Engine Optimization (GEO)

## What Is Generative Engine Optimization (GEO)? The Playbook for Ranking in AI Search

### Pragati

January 21, 2026

18 Mins read



Generative Engine Optimization (GEO)

## Why Each AI Platform Shows Different Answers

### Pragati

October 6, 2025

5 Mins read



Generative Engine Optimization (GEO)

## Why the Traditional Marketing Funnel Doesn’t Work in the AI-Search Era

### Pragati

October 5, 2025

8 Mins read



Generative Engine Optimization (GEO)

## Ranking High vs Getting Cited: Why Modern SEO Needs Both

### Niyati

October 5, 2025

9 Mins read



Generative Engine Optimization (GEO)

## What Is Answer Engine Optimization (AEO) and Why It Matters in 2026

### Pragati

January 11, 2026

11 Mins read



Generative Engine Optimization (GEO)

## How to Improve AI Visibility: 11 Strategies We Tested

### Niyati

October 23, 2025

11 Mins read



Generative Engine Optimization (GEO)

## How To Use Wikipedia To Improve AI Search Visibility

### Pragati

September 29, 2025

6 Mins read



Generative Engine Optimization (GEO)

## How LLMs Interpret Content (and How to Structure Content for AI Search)

### Pragati

September 24, 2025

8 Mins read



Generative Engine Optimization (GEO)

## Cracking AI Mentions: How We Won 1,000+ AI Answers Without Publishing New Content

### Samanyou

September 23, 2025

3 Mins read



Generative Engine Optimization (GEO)

## What is AI Search: How It Works and Why It Matters

### Pragati

September 22, 2025

11 Mins read



Generative Engine Optimization (GEO)

## Peec AI Review: Is It Worth Investing?

### Pragati

September 22, 2025

9 Mins read



Generative Engine Optimization (GEO)

## AI Visibility Explained: How To Make AI Engines Recommend Your Brand

### Niyati

October 27, 2025

17 Mins read



Generative Engine Optimization (GEO)

## Will ChatGPT Replace Google? Here’s the Truth

### Pragati

September 19, 2025

8 Mins read



Generative Engine Optimization (GEO)

## What is Search Everywhere Optimization: The SEO 2.0

### Pragati

September 12, 2025

13 Mins read



Generative Engine Optimization (GEO)

## Top 6 Generative Engine Optimization Strategies [Tried & Tested]

### Pragati

September 12, 2025

11 Mins read



Generative Engine Optimization (GEO)

## ChatGPT SEO: How to Rank in ChatGPT Search

### Pragati

January 28, 2026

12 Mins read



Generative Engine Optimization (GEO)

## Top 6 xFunnel AI Alternatives To Try in 2026

### Pragati

January 23, 2026

12 Mins read



Generative Engine Optimization (GEO)

## Top 8 AI Search Optimization Tools To Try in 2026

### Pragati

January 23, 2026

15 Mins read



Generative Engine Optimization (GEO)

## How To Integrate GEO With SEO: 7 Actionable Steps

### Pragati

August 25, 2025

8 Mins read



Generative Engine Optimization (GEO)

## Top 9 AI Search Monitoring Tools That I’d Recommend Using in 2026

### Pragati

January 23, 2026

20 Mins read



Generative Engine Optimization (GEO)

## Top 7 Benefits of Generative Engine Optimisation

### Pragati

August 19, 2025

7 Mins read



Generative Engine Optimization (GEO)

## 8 Ahrefs Brand Radar Alternatives To Try Out in 2026

### Niyati

January 23, 2026

20 Mins read



Generative Engine Optimization (GEO)

## What Is LLM Seeding And How It Boosts AI Visibility

### Saloni

August 15, 2025

12 Mins read



Generative Engine Optimization (GEO)

## Profound vs PEEC vs AthenaHQ: Which is a Better GEO Tool

### Sumana

August 15, 2025

8 Mins read



Generative Engine Optimization (GEO)

## Top 8 Scrunch AI Alternatives To Try in 2026

### Pragati

February 19, 2026

19 Mins read



Generative Engine Optimization (GEO)

## Is Traditional SEO Enough for AI Visibility

### Pragati

September 21, 2025

7 Mins read



Generative Engine Optimization (GEO)

## How to Audit Your Brand’s AI Visibility (With Writesonic)

### Pragati

August 5, 2025

10 Mins read



Generative Engine Optimization (GEO)

Products

## Daydream Review: Can This Programmatic SEO Tool Help You Win AI Search?

### Sumana

August 12, 2025

6 Mins read



Generative Engine Optimization (GEO)

## Generative Engine Optimization: 10 Tips To Boost AI Visibility in 2026

### Pragati

January 23, 2026

15 Mins read



Generative Engine Optimization (GEO)

## ChatGPT Converts 2.08x Better Than Google [Writesonic Report]

### Niyati

July 27, 2025

7 Mins read



Generative Engine Optimization (GEO)

## What Is GPTBot? Should You Block It?

### Pragati

August 4, 2025

8 Mins read



Generative Engine Optimization (GEO)

## AI Brand Mentions vs AI Citations: What’s The Difference?

### Pragati

August 25, 2025

7 Mins read



Generative Engine Optimization (GEO)

## Conductor AI Review: Is This Enterprise SEO Platform Worth the Investment in 2026?

### Sumana

January 23, 2026

6 Mins read



Generative Engine Optimization (GEO)

## Profound vs Otterly: Which AI Search Visibility Tool Gives You the Edge in 2026?

### Sumana

January 23, 2026

6 Mins read



Generative Engine Optimization (GEO)

## Enterprise GEO Platform Buying Guide

### Pragati

August 4, 2025

9 Mins read



Generative Engine Optimization (GEO)

## Why Structured Data in AI Search Matters More Than Ever in 2026

### Saloni

January 23, 2026

10 Mins read



Generative Engine Optimization (GEO)

## GEO, AEO, AIO, and LLMO: Are These Simply Evolved SEO?

### Pragati

August 4, 2025

11 Mins read



Generative Engine Optimization (GEO)

## AI Citations vs Backlinks: What’s The Difference?

### Pragati

August 4, 2025

7 Mins read



Generative Engine Optimization (GEO)

## Top 11 Generative Engine Optimization Agencies To Help You Get Cited By AI

### Saloni

December 17, 2025

17 Mins read



Generative Engine Optimization (GEO)

## AI Search For E-Commerce: How To Rank In ChatGPT & Google

### Saloni

July 20, 2025

13 Mins read



Generative Engine Optimization (GEO)

## 5 Best AI Sentiment Analysis Tools For AI Search Monitoring

### Niyati

July 20, 2025

8 Mins read



Generative Engine Optimization (GEO)

## Traffic is Overrated: 7 New Age AI SEO Metrics to Track in 2026

### Niyati

January 23, 2026

8 Mins read



Generative Engine Optimization (GEO)

## AEO vs SEO: What’s The Difference?

### Pragati

August 14, 2025

9 Mins read



Generative Engine Optimization (GEO)

## Brand Authority vs Topical Authority: How to Track Brand Authority for AI Search

### Sumana

August 11, 2025

7 Mins read



Generative Engine Optimization (GEO)

## XFunnel Review: Optimizing Your Brand for AI Search Engines

### Sumana

August 11, 2025

6 Mins read



Generative Engine Optimization (GEO)

## The Easy Guide to GEO Action Center in 2026

### Sumana

January 23, 2026

6 Mins read



Generative Engine Optimization (GEO)

## 7 Rankscale Alternatives To Kickstart Your GEO Strategy

### Niyati

August 17, 2025

14 Mins read



Generative Engine Optimization (GEO)

## Is Your Website Losing Visibility to AI Overviews in PAA Results?

### Saloni

July 20, 2025

13 Mins read



Generative Engine Optimization (GEO)

## 7 Otterly.ai Alternatives For Your GEO Workflow

### Niyati

August 17, 2025

16 Mins read



Generative Engine Optimization (GEO)

## AI Brand Reputation: How to Track and Manage It [2026 Guide]

### Niyati

January 23, 2026

11 Mins read



Generative Engine Optimization (GEO)

## Why Your Content Isn’t Making It Into AI Overviews (And How to Fix It)

### Pragati

August 4, 2025

6 Mins read



Generative Engine Optimization (GEO)

## Long-Tail vs Short-Tail: Which Type of Keywords Matters Most in AI Overviews?

### Pragati

August 4, 2025

4 Mins read



Generative Engine Optimization (GEO)

## Goodie AI Alternatives in 2026: Top AI Visibility Tools Comparison

### Sumana

January 23, 2026

10 Mins read



Generative Engine Optimization (GEO)

## Bluefish AI Review: Everything to Know about Features, Pros, Cons, and Pricing

### Sumana

August 11, 2025

6 Mins read



Generative Engine Optimization (GEO)

## Reddit’s 450% Growth in AI Overviews: Is UGC Now the AI King?

### Niyati

August 7, 2025

6 Mins read



Generative Engine Optimization (GEO)

## 7 Best AthenaHQ Alternatives in 2026 You Need to Know

### Sumana

January 23, 2026

9 Mins read



Generative Engine Optimization (GEO)

## Prompts vs Keywords: What’s The Difference?

### Pragati

August 4, 2025

6 Mins read



Generative Engine Optimization (GEO)

## High-Impressions, Low-Clicks Mystery: The Truth Behind

### Pragati

August 4, 2025

7 Mins read



Generative Engine Optimization (GEO)

## Goodie AI Review: Features, Pricing, and Better Alternatives

### Sumana

August 11, 2025

8 Mins read



Generative Engine Optimization (GEO)

## 98.1% of ChatGPT Users Also Google: Why AI Search Isn’t Replacing Search Engines Yet

### Sumana

July 20, 2025

8 Mins read



Generative Engine Optimization (GEO)

## 10 GEO (Generative Engine Optimization) Mistakes That Are Killing Your AI Visibility

### Saloni

July 20, 2025

12 Mins read



Generative Engine Optimization (GEO)

## Context Over Keywords: 84% of AI Overviews Don’t Match the Original Search Query

### Saloni

July 25, 2025

12 Mins read



Generative Engine Optimization (GEO)

Tools

## Scrunch AI Review: Should You Invest in This GEO Tool?

### Saloni

October 6, 2025

7 Mins read



Generative Engine Optimization (GEO)

## AI Overviews Reduce Clicks: Is This a Threat or Opportunity for Publishers?

### Sumana

July 20, 2025

8 Mins read



Generative Engine Optimization (GEO)

## AI Search Optimization for Small Websites: Why Small Sites Struggle to Get Cited

### Saloni

July 20, 2025

15 Mins read



Generative Engine Optimization (GEO)

## PEEC AI vs Otterly AI: A Comprehensive Comparison

### Sumana

July 20, 2025

7 Mins read



Generative Engine Optimization (GEO)

## PEEC AI vs Profound: A GEO Tools Comparison

### Sumana

July 20, 2025

9 Mins read



Generative Engine Optimization (GEO)

## AI Mode Query Fan Out: How to Optimize Content for Google’s AI

### Niyati

August 11, 2025

13 Mins read



Generative Engine Optimization (GEO)

## 40.58% of AI Citations Come from Google’s Top 10 Results (Study of 1M+ AI Overviews)

### Pragati

August 4, 2025

6 Mins read



Generative Engine Optimization (GEO)

## Nearly 60% of AI Overviews Are 100-300 Words (Insights from 1M+ AIOs)

### Pragati

August 4, 2025

5 Mins read



Generative Engine Optimization (GEO)

## How API vs UI Results Differ for AI Search Engine Answers

### Sumana

July 20, 2025

6 Mins read



Generative Engine Optimization (GEO)

## AthenaHQ vs Profound: The Ultimate Comparison Guide

### Sumana

July 20, 2025

7 Mins read



Generative Engine Optimization (GEO)

## How to Identify Prompts to Track on AI Search Engines

### Sumana

July 20, 2025

8 Mins read



Generative Engine Optimization (GEO)

## How to Choose the Right AI Visibility Tool? [2026]

### Niyati

January 23, 2026

8 Mins read



Generative Engine Optimization (GEO)

## AthenaHQ Review: The Good, The Bad, & Pricing

### Sumana

July 20, 2025

7 Mins read



Generative Engine Optimization (GEO)

Tools

## Otterly.ai Review: Features, Performance & Usability Tested

### Saloni

July 24, 2025

11 Mins read



Generative Engine Optimization (GEO)

## Profound AI Review: Is It Worth The Investment for GEO?

### Niyati

September 23, 2025

8 Mins read



AI Guide

Generative Engine Optimization (GEO)

SEO

## New Data: The Unexpected Impact of AI Search on SEO

### Saloni

July 1, 2025

14 Mins read



AI Guide

Generative Engine Optimization (GEO)

SEO

## What Are Zero Click Searches And How To Optimize For Them

### Saloni

October 10, 2025

14 Mins read



Generative Engine Optimization (GEO)

## 9 Key Factors That Affect AI Search Rankings

### Pragati

August 4, 2025

12 Mins read



Generative Engine Optimization (GEO)

SEO

## How to Use Generative AI for Advanced SEO: Top 8 Strategies

### Pragati

August 4, 2025

11 Mins read



Generative Engine Optimization (GEO)

## AI Search Optimization in 2026: What Actually Works

### Sumana

January 23, 2026

9 Mins read



Generative Engine Optimization (GEO)

## 8 Strategies to Get Your Brand Mentioned in AI [2026]

### Niyati

January 23, 2026

10 Mins read



AI Guide

Generative Engine Optimization (GEO)

## Will AI Replace Search Engines? What Marketers Must Know!

### Saloni

August 20, 2025

13 Mins read



Generative Engine Optimization (GEO)

## Google Gemini SEO: How to Rank on Gemini’s Answers

### Pragati

August 25, 2025

14 Mins read



Generative Engine Optimization (GEO)

## How to Measure SEO Success in Times of AI Search

### Sumana

January 11, 2026

9 Mins read



Generative Engine Optimization (GEO)

## What Is LLM Optimization: 12 Tips To Improve Your Brand Visibility

### Pragati

January 11, 2026

23 Mins read



Generative Engine Optimization (GEO)

## Your Complete Guide to Google AI Mode for Better Search Visibility

### Niyati

July 20, 2025

14 Mins read



Generative Engine Optimization (GEO)

## Google AI Overview Optimization: How to Adapt and Thrive in 2026

### Sumana

January 23, 2026

11 Mins read



AI Guide

Generative Engine Optimization (GEO)

## Controlling Your Brand Presence on AI Search: 7 Proven Strategies for 2026

### Saloni

January 23, 2026

14 Mins read



Generative Engine Optimization (GEO)

## Google AI Mode: What’s That and How It Affects Your Traffic

### Niyati

July 20, 2025

7 Mins read



Generative Engine Optimization (GEO)

## PR for Visibility on AI Search: How Does It Boost Digital Presence in 2026

### Sumana

January 23, 2026

8 Mins read



Generative Engine Optimization (GEO)

## AEO vs GEO: Is There Really Any Difference?

### Niyati

January 11, 2026

12 Mins read



Generative Engine Optimization (GEO)

## How Search Generative Experience Will Affect Local SEO & Small Businesses

### Sumana

July 20, 2025

9 Mins read



Generative Engine Optimization (GEO)

## Top Generative Engine Optimization (GEO) Trends

### Pragati

July 23, 2025

10 Mins read



Generative Engine Optimization (GEO)

## Introducing AI Traffic Analytics: Track Traffic from ChatGPT, Gemini & Perplexity

### Samanyou

July 28, 2025

7 Mins read



Generative Engine Optimization (GEO)

## How To Do Generative Engine Optimization: Our 7 Step Strategy

### Pragati

August 13, 2025

13 Mins read
