---
title: AEO and GEO for AI Overviews, ChatGPT, Claude, Gemini, an...
url: https://www.trevorlasn.com/blog/aeo-geo-vs-seo-google-ai-optimization
site_name: tldr
content_file: tldr-aeo-and-geo-for-ai-overviews-chatgpt-claude-gemini
fetched_at: '2026-05-18T19:36:11.448412'
original_url: https://www.trevorlasn.com/blog/aeo-geo-vs-seo-google-ai-optimization
date: '2026-05-18'
published_date: '2026-05-17T00:00:00.000Z'
description: What Answer Engine Optimization and Generative Engine Optimization mean, and how to get your site cited by AI Overviews, ChatGPT, Claude, Perplexity, and Gem...
tags:
- tldr
---

# AEO and GEO for AI Overviews, ChatGPT, Claude, Gemini, and Perplexity

 

## What Answer Engine Optimization and Generative Engine Optimization mean, and how to get your site cited by AI Overviews, ChatGPT, Claude, Perplexity, and Gemini.

 
 
 
 
Trevor I. Lasn
 
·
 
 
 
 May 17, 2026 
 
·
 
13 min read
 
 
 

Building 
0xinsider.com
 — see who's winning across prediction markets (Polymarket, Kalshi, and more) — and what they're trading right now.

 
 
 

Search results don’t look the way they did two years ago. Google now opens with AI Overviews, ChatGPT and Claude pull live web results into their answers, Perplexity built an entire product around it, and Gemini sits one tap away inside every Google surface. The page is no longer the destination. The page is a source the model is reading on your behalf.

Two acronyms have shown up to describe the work of being visible inside those answers.AEOstands for Answer Engine Optimization, which is the work of being the source an “answer engine” uses when it returns a direct answer instead of a list of links.GEOstands for Generative Engine Optimization, which is the same idea framed around generative AI specifically: appearing inside answers a model writes from scratch using your page as a reference.

Google’s ownAI optimization guidetreats both as variations of regular SEO. From their perspective, “optimizing for generative AI search is optimizing for the search experience, and thus still SEO.” The ranking and quality systems that decide what shows up in a list of blue links are the same systems that decide what shows up inside an AI Overview. Improving for one improves the other.

One reason this matters: each AI surface pulls from a different web index, but most of those indexes are downstream of the same crawl, rendering, and quality work.

1
 
Your page
2
 
│
3
 
▼
4
 
Search engine indexes (where the crawl lands)
5
 
┌────────────────────────────────────────────────────────┐
6
 
│ Google index ──▶ Google Search, AI Overviews, Gemini │
7
 
│ Bing index ──▶ Bing, Microsoft Copilot │
8
 
│ OpenAI index ──▶ ChatGPT Search │
9
 
│ Anthropic + Brave ▶ Claude web search │
10
 
│ Perplexity + Bing ▶ Perplexity answers │
11
 
└────────────────────────────────────────────────────────┘
12
 
│
13
 
▼
14
 
The AI surface reads from the index, cites your page

The practical question is what you do to your site. The rest of this post walks through it, with sources for every recommendation.

### Eligibility comes before everything else

Before any of the content work matters, the page has to be allowed to appear in AI features at all. Google’s guide is explicit: a page is only eligible for AI features if it’s eligible to appear as a regular search snippet (source). That means the URL needs to be indexed, the page needs to be crawlable inrobots.txt, snippets need to be allowed (nonosnippet, nomax-snippet:0), and the content has to load without requiring the crawler to execute heavy JavaScript first.

Open Google Search Console and run a URL inspection on a page you care about. The “Test live URL” view shows you what Google sees, including the rendered HTML after JavaScript has executed. If the article body is missing from that rendered HTML, fix it before doing anything else. Google’sJavaScript SEO basicscovers the patterns that work and the ones that break crawling. Server rendering and static generation are the safest bets.

A 30-second sanity check from your terminal, one per major AI crawler:

Terminal window
1
# Google Search (feeds AI Overviews and Gemini grounding)
2
curl
 
-A
 
"Googlebot/2.1 (+http://www.google.com/bot.html)"
 
-I
 
https://0xinsider.com/article
3

4
# Bing (feeds Microsoft Copilot)
5
curl
 
-A
 
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
 
-I
 
https://0xinsider.com/article
6

7
# OpenAI search indexer (ChatGPT Search)
8
curl
 
-A
 
"OAI-SearchBot/1.3; +https://openai.com/searchbot"
 
-I
 
https://0xinsider.com/article
9

10
# Anthropic search indexer (Claude web search)
11
curl
 
-A
 
"Claude-SearchBot/1.0 (+https://www.anthropic.com)"
 
-I
 
https://0xinsider.com/article
12

13
# Perplexity indexer
14
curl
 
-A
 
"PerplexityBot/1.0 (+https://perplexity.ai/perplexitybot)"
 
-I
 
https://0xinsider.com/article

A200 OKfrom a spoofed user agent isn’t proof that the real crawler can reach the page. Bot operators block UA spoofing, so the only authoritative check is to verify the request against published IP ranges or reverse-DNS records. Google documents itscrawler verification process, and OpenAI, Anthropic, and Perplexity all publish IP ranges in their bot docs. Use thecurltest to catch obvious blocks (a403,503, or login-page redirect that suggests Cloudflare’s bot-fight rule or a misconfigured WAF), then confirm against the official IP list for the bots that matter to you.

The full list of bots worth thinking about, with what they do and the canonical reference:

1
Bot user agent Purpose Reference
2
──────────────────────────────────────────────────────────────────────────
3
Googlebot Google Search index developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers
4
Google-Extended Gemini Apps + Vertex AI Grounding + developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers
5
 
AI training (separate from Search)
6
Bingbot Bing index (feeds Copilot) bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0
7
GPTBot/1.3 OpenAI training developers.openai.com/api/docs/bots
8
OAI-SearchBot/1.3 ChatGPT Search live index developers.openai.com/api/docs/bots
9
ChatGPT-User ChatGPT user-initiated fetch developers.openai.com/api/docs/bots
10
ClaudeBot Anthropic training support.claude.com/en/articles/8896518
11
Claude-SearchBot Anthropic search index (Claude search) support.claude.com/en/articles/8896518
12
Claude-User Claude user-initiated fetch support.claude.com/en/articles/8896518
13
PerplexityBot Perplexity search index docs.perplexity.ai/docs/resources/perplexity-crawlers
14
Perplexity-User Perplexity user-initiated fetch docs.perplexity.ai/docs/resources/perplexity-crawlers
15
Applebot-Extended Apple Intelligence training support.apple.com/en-us/119829
16
Meta-ExternalAgent Meta AI training developers.facebook.com/docs/sharing/webmasters/web-crawlers
17
CCBot Common Crawl (feeds many models) commoncrawl.org/ccbot

Arobots.txtyou can copy that allows AI search visibility (the surfaces that cite your page) while opting out of training (the bots that scrape for model training data):

1
# Allow indexing for search and AI search surfaces
2
User-agent: Googlebot
3
Allow: /
4

5
User-agent: Bingbot
6
Allow: /
7

8
User-agent: OAI-SearchBot
9
Allow: /
10

11
User-agent: ChatGPT-User
12
Allow: /
13

14
User-agent: PerplexityBot
15
Allow: /
16

17
User-agent: Perplexity-User
18
Allow: /
19

20
User-agent: Claude-SearchBot
21
Allow: /
22

23
User-agent: Claude-User
24
Allow: /
25

26
# Block AI training crawlers (does not affect Google Search inclusion)
27
User-agent: GPTBot
28
Disallow: /
29

30
User-agent: ClaudeBot
31
Disallow: /
32

33
User-agent: Google-Extended
34
Disallow: /
35

36
User-agent: Applebot-Extended
37
Disallow: /
38

39
User-agent: Meta-ExternalAgent
40
Disallow: /
41

42
User-agent: CCBot
43
Disallow: /
44

45
# Fallback
46
User-agent: *
47
Allow: /
48

49
Sitemap: https://0xinsider.com/sitemap.xml

The distinction matters.GPTBotandClaudeBotare training crawlers, and blocking them does not affect search inclusion.Google-Extendedis broader: it controls AI trainingandgrounding inside Gemini Apps and Vertex AI Grounding, but does not affect Google Search ranking or AI Overview eligibility (Google source). The bots that determine whether your page can show up inside an AI answer are the search indexers:Googlebot,Bingbot,OAI-SearchBot,Claude-SearchBot, andPerplexityBot(OpenAI source,Anthropic source,Perplexity source). Many sites accidentally block one of those and tank their visibility.

Meta robots tags are the other lever, page-level rather than site-level:

1
<!-- Eligible for AI Overviews and AI search citations -->
2
<
meta
 
name
=
"robots"
 
content
=
"index, follow"
>
3

4
<!-- Indexed, but excluded from snippets and AI Overviews -->
5
<
meta
 
name
=
"robots"
 
content
=
"index, follow, nosnippet"
>
6

7
<!-- Indexed, but snippet capped too short for AI answers to use -->
8
<
meta
 
name
=
"robots"
 
content
=
"index, follow, max-snippet:50"
>

To opt out ofGoogle-Extended(Gemini Apps and Vertex AI Grounding), use therobots.txtproduct token shown earlier. Google does not documentGoogle-Extendedas a robots meta tag, only as arobots.txttoken (source). The snippet directives above are documented in Google’smeta tags reference.

1
 
Page exists
2
 
│
3
 
▼ robots.txt allows crawl? ── no ──▶ invisible
4
 
▼ page renders without JS errors? ── no ──▶ invisible
5
 
▼ indexed in Search Console? ── no ──▶ invisible
6
 
▼ snippet allowed (no nosnippet)? ── no ──▶ regular search only
7
 
▼ quality + originality signals? ── weak ─▶ ranked, rarely cited
8
 
│
9
 
▼
10
 
Eligible to appear in AI Overviews and related surfaces

Every layer is a gate. The fancier optimization work only matters once all the gates are open.

### What gets cited is what a model can’t write from training data alone

Generative search rewards specificity. Models can summarize generic information without quoting anyone, so the pages that get cited are the ones that say something the model can’t synthesize on its own. Google’s guide tells creators to focus on “unique, valuable, people-first content” rather than commodity content that re-states what every other page on the topic already says (source). The deeper version of this advice lives in Google’shelpful content guidance, which goes into how to demonstrate firsthand experience, real expertise, and original perspective.

Here are two real versions of the same paragraph for an article about migrating to Next.js 16. Same topic, same word count, wildly different odds of being cited:

1
Commodity version:
2
"Next.js 16 introduces async params, making route parameters
3
asynchronous. This is a breaking change you should plan for
4
when upgrading from Next.js 15. Make sure to await your params
5
in dynamic routes."
6

7
Distinctive version:
8
"We migrated a 240-route Next.js 15 app to 16 last week. The
9
async params change broke 47 pages in CI on the first run.
10
The mechanical fix: wrap every `params.slug` access in
11
`await params`. The catch we hit: dynamic API routes that
12
destructure params in the function signature need the
13
signature itself marked async, not just the body. Took
14
3 hours, almost all of it search-replace."

A model can produce the commodity version from training data alone, so it won’t cite the source. There’s nothing in there it couldn’t write itself. The distinctive version has a number (47 broken pages), a specific catch (the function signature subtlety), and a time estimate (3 hours), none of which the model can generate without quoting the source. Even one of those details is often enough to flip a page from “training data summary” to “cited reference”.

1
 
What the model sees about your topic
2
 
│
3
 
├──▶ Commodity content
4
 
│ "Same overview 50 other pages have"
5
 
│ │
6
 
│ ▼
7
 
│ Model synthesizes from training data
8
 
│ │
9
 
│ ▼
10
 
│ Not cited
11
 
│
12
 
└──▶ Distinctive content
13
 
"Specific data, screenshot, opinion,
14
 
result you tested in production"
15
 
│
16
 
▼
17
 
Model can't synthesize, must quote
18
 
│
19
 
▼
20
 
Cited in the answer

### Clean technical structure helps the crawler and the model

Semantic HTML matters. Use real heading levels in a sensible hierarchy, put the answer to the question the page is about near the top, and avoid burying content under preamble. A real before/after on the same blog post:

1
<!-- Bad: divs and classes carry no semantic weight -->
2
<
div
 
class
=
"title"
>
How to migrate to Next.js 16
</
div
>
3
<
div
 
class
=
"subtitle"
>
A practical guide
</
div
>
4
<
div
 
class
=
"body"
>
We migrated 240 routes last week...
</
div
>
5

6
<!-- Good: explicit semantics the crawler and model understand -->
7
<
article
>
8
 
<
h1
>
How to migrate to Next.js 16
</
h1
>
9
 
<
p
 
class
=
"lede"
>
A practical guide to async params,
10
 
Turbopack defaults, and the gotchas we hit.
</
p
>
11
 
<
section
>
12
 
<
h2
>
Async params, in practice
</
h2
>
13
 
<
p
>
We migrated 240 routes last week...
</
p
>
14
 
</
section
>
15
</
article
>

The second version gives the crawler clear structure (article,h1,section,h2) and the model clean boundaries for what’s heading, lede, and body.

Google’s documentation onpage experienceexplains how Core Web Vitals feed into ranking, which feeds directly into AI feature eligibility. The thresholds Google publishes (source):

1
Metric Good Poor
2
─────────────────────────────────────────────────────
3
LCP Largest Contentful Paint ≤ 2.5s > 4.0s
4
INP Interaction to Next Paint ≤ 200ms > 500ms
5
CLS Cumulative Layout Shift ≤ 0.1 > 0.25

The numbers ranking algorithms look at are the 28-day field data from real Chrome users (CrUX), not a Lighthouse run on your laptop. Read them fromweb-vitalsin JavaScript to align local testing with what Google’s systems see:

1
import
 
{
 onLCP
,
 onINP
,
 onCLS 
}
 
from
 
'web-vitals'
;
2

3
onLCP
(
metric
 
=>
 console
.
log
(
'LCP'
,
 metric
.
value
,
 metric
.
rating))
;
4
onINP
(
metric
 
=>
 console
.
log
(
'INP'
,
 metric
.
value
,
 metric
.
rating))
;
5
onCLS
(
metric
 
=>
 console
.
log
(
'CLS'
,
 metric
.
value
,
 metric
.
rating))
;

The AI optimization guide also pushes back on several “optimization hacks” circulating online. Adding anllms.txtfile is not a ranking signal and isn’t used by Google’s AI features (source). Chunking content into tiny sections or rewriting every heading as a question is unnecessary, because models read context across the whole page. The guide also says structured data is useful where it powers a documented rich result, but it isn’t required for AI feature visibility. Spend the time on real content quality and rendering instead.

1
 
What the crawler fetches
2
 
─────────────────────────────────────────────────────────
3
 
Server-rendered HTML Client-only SPA shell
4
 
───────────────────── ─────────────────────
5
 
<h1>Title</h1> <div id="root"></div>
6
 
<p>Real content...</p> <script src="app.js">
7
 
<h2>Section</h2> (renders later)
8
 
│ │
9
 
▼ ▼
10
 
Crawler reads it now Crawler runs JS, may stall
11
 
│ │
12
 
▼ ▼
13
 
Indexed, AI-eligible May never reach the content

### Visuals, schema, and commerce data are the structured pipelines

AI Overviews pull images and video directly when they’re high quality. Real screenshots, real diagrams, and short video walkthroughs are more useful than stock photos. Apply the same image SEO basics Google has always recommended in itsimage best practices: descriptivealttext, meaningful filenames, captions where they help the reader, and the same forvideo best practices.

A real alt-text before/after for an article about Next.js performance:

1
<!-- Bad: alt tells the crawler nothing -->
2
<
img
 
src
=
"chart.png"
 
alt
=
"chart"
>
3
<
img
 
src
=
"screenshot.png"
 
alt
=
""
>
4

5
<!-- Good: alt describes what the image conveys -->
6
<
img
 
src
=
"chart.png"
7
 
alt
=
"Next.js 16 vs 15 build time: 4.2s vs 6.8s on a 240-route app"
>
8
<
img
 
src
=
"screenshot.png"
9
 
alt
=
"Search Console URL inspection showing the page is indexed"
>

The second pair is what gets pulled into an AI Overview’s image carousel because the alt text is descriptive enough for the model to understand what the image proves.

Structured data is worth adding where it powers a specific rich result. Recipe schema, product schema, FAQ schema, event schema, and Article schema all have documented effects in regular search and feed into the same understanding layer the AI features use. Google’srich results gallerylists every supported type. A workingArticleschema for a blog post:

1
<
script
 
type
=
"application/ld+json"
>
2
{
3
 
"@context": "https://schema.org",
4
 
"@type": "Article",
5
 
"headline": "How to migrate to Next.js 16",
6
 
"datePublished": "2026-05-17",
7
 
"dateModified": "2026-05-17",
8
 
"author": {
9
 
"@type": "Person",
10
 
"name": "Trevor Lasn",
11
 
"url": "https://www.trevorlasn.com"
12
 
},
13
 
"publisher": {
14
 
"@type": "Organization",
15
 
"name": "trevorlasn.com"
16
 
},
17
 
"image": "https://www.trevorlasn.com/article-cover.webp",
18
 
"description": "A practical guide to async params and Turbopack defaults."
19
}
20
</
script
>

Test it inside Google’sRich Results Testbefore deploying. The tool will tell you exactly which required fields are missing or malformed.

If you run a local business or sell products, two unrelated surfaces matter more than schema. A verifiedGoogle Business Profilefeeds local AI answers with your hours, location, services, and reviews. AMerchant Centerfeed is what AI Overviews pull product information from. The AI optimization guide names both explicitly as the primary input for business and commerce results (source).

1
 
Type of result Source feed Where it shows
2
 
────────────────────────────────────────────────────────────────────
3
 
Local business ◀── Google Business Profile ──▶ Maps, local panel,
4
 
(hours, location, reviews) local AI answers
5

6
 
Products ◀── Merchant Center feed ────▶ Shopping cards,
7
 
(price, stock, variants) product AI answers
8

9
 
Recipes, FAQs, ◀── Schema.org JSON-LD ──────▶ Rich results,
10
 
events, articles (on-page structured data) AI understanding

### Agentic experiences are the next surface

The newer wrinkle is autonomous agents browsing on the user’s behalf (Claude with computer use, ChatGPT Operator, Perplexity’s assistant). Google’s AI optimization guide recommends sites consider how agents interpret their DOM, controls, and content (source). Sites with confusing markup, hidden controls, or essential information rendered only as images are hard for agents to operate. The accessibility work you’d already do for screen readers covers most of the same ground.

A real before/after of an interactive control on a booking page:

1
<!-- Agent-hostile: div pretending to be a button, no label -->
2
<
div
 
class
=
"btn-primary"
 
onclick
=
"
submitBooking
()"
>
3
 
<
svg
 
viewBox
=
"0 0 24 24"
>
<!-- check icon -->
</
svg
>
4
</
div
>
5

6
<!-- Agent-friendly: real button, explicit label, real semantics -->
7
<
button
 
type
=
"submit"
8
 
aria-label
=
"Confirm booking for 7:00 PM on May 17"
>
9
 
<
svg
 
viewBox
=
"0 0 24 24"
 
aria-hidden
=
"true"
>
10
 
<!-- check icon -->
11
 
</
svg
>
12
 
Confirm booking
13
</
button
>

The second version tells an agent three things: it’s a submit button, the action is “Confirm booking”, and the icon is decorative. The first version tells it nothing. An agent that can’t identify the booking confirmation gives up and picks a site it can operate.

Form fields work the same way. An agent readsname,id,aria-label, and the surrounding<label>element:

1
<!-- Agent-hostile: placeholder is the only hint, no semantic link -->
2
<
input
 
type
=
"text"
 
placeholder
=
"When?"
>
3

4
<!-- Agent-friendly: explicit label, real input type, real name -->
5
<
label
 
for
=
"reservation-time"
>
Reservation time
</
label
>
6
<
input
 
type
=
"datetime-local"
7
 
id
=
"reservation-time"
8
 
name
=
"reservation_time"
9
 
required
>

Switching totype="datetime-local"is a tiny change that gives both browsers and agents a native datetime picker with structured value handling. No agent has to guess what format you want.

1
 
User intent: "Book me a table for 7pm tonight"
2
 
│
3
 
▼
4
 
Agent opens your site
5
 
│
6
 
▼
7
 
┌───────────────────────────────────────────────┐
8
 
│ Can it find the booking widget? │
9
 
│ Can it read the available time slots? │
10
 
│ Are the buttons labeled, not just icons? │
11
 
│ Does the form submit without a 3s JS stall? │
12
 
└───────────────────────────────────────────────┘
13
 
│
14
 
┌──────────────┴──────────────┐
15
 
▼ ▼
16
 
Task completes on Agent gives up,
17
 
your site picks a competitor

### Measure what you can, and don’t chase what you can’t

Search Console is still the source of truth for Google-side data. AI Overviews and AI Mode traffic is rolled into the standard Web performance report (Google source), so impressions and clicks for the pages you care about are the right place to look. Bing Webmaster Tools provides the equivalent for Bing and Copilot.

One inference you can draw, carefully: filter Performance by Query containing a conversational starter (how,what,why,is,can). These long-tail queries are the kind AI Overviews trigger on, and a noticeable shift in impressions vs clicks on those queries is consistent with the page being summarized inside an AI answer rather than visited. It is not proof. Layout changes, ranking shifts, query mix changes, and seasonality can all produce similar patterns. Use it as a hypothesis to investigate, not a verdict.

A direct way to test whether models cite you: open each surface and ask a question your content should answer. Concrete, copy-paste tests:

1
ChatGPT (Search mode):
2
 
"What's a practical way to migrate a Next.js 15 app to Next.js 16?"
3

4
Claude (with web search):
5
 
"Find me a recent first-hand account of migrating to Next.js 16
6
 
on a large app. I want specifics, not generic advice."
7

8
Perplexity:
9
 
"Real-world Next.js 16 migration: what broke, how it was fixed."
10

11
Gemini (or Google with AI Overview):
12
 
"How do you handle async params when migrating to Next.js 16?"

If your domain shows up in the inline source list or the answer cites it, you’re being retrieved. Repeat across the major surfaces every few weeks for the topics that matter to your business. Track the count of cite-events the same way you’d track backlinks.

1
 
What to track Where it lives Signal it gives
2
 
────────────────────────────────────────────────────────────────────
3
 
Impressions ◀── Search Console ──▶ Visibility growth
4
 
Clicks ◀── Search Console ──▶ Selection rate
5
 
Conversions ◀── Your own analytics ──▶ Business outcome
6
 
Cite events ◀── Ask ChatGPT / Claude ──▶ Whether models cite
7

8
 
What to skip:
9
 
"AI Overview rank trackers" no reliable public methodology yet

Doing the work above covers everything Google’sAI optimization guiderecommends and everything the other AI search surfaces reward. AEO and GEO aren’t separate disciplines from SEO. They’re the same work, applied with sharper attention to content originality, rendering, and the structured pipelines that feed every AI surface on the web.

 
 
 

# Trevor I. Lasn

Building0xinsider.com— see who's winning across prediction markets (Polymarket, Kalshi, and more) — and what they're trading right now. Product engineer based in Tartu, Estonia, building and shipping for over a decade.

 
 
 
 
 
 
 
 
 
 
 
 
 
 

Found this article helpful? You might enjoy my free newsletter. I
 share dev tips and insights to help you grow your coding skills
 and advance your tech career.

 
 
 
 
 
 
 
 
 
 
 

## Related Articles

 

### Check out these related articles that might be useful for you. They cover
 similar topics and provide additional insights.

 
 
 
 
 Webdev 
 
 
 
 
 
 3 min read 
 

#### CSS ::target-text for Text Highlighting

 

A look at how browsers can highlight text fragments using CSS ::target-text, making text sharing and navigation more user-friendly

 
 
 Dec 17, 2024 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 4 min read 
 

#### Explicit is better than implicit

 

Clarity is key: being explicit makes your code more readable and maintainable.

 
 
 Sep 4, 2024 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 5 min read 
 

#### Programming Trends to Watch in 2020 and Beyond

 

Here are my bets on the programming trends

 
 
 Jul 19, 2019 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 12 min read 
 

#### Frontend Security Checklist

 

Tips for Keeping All Frontend Applications Secure

 
 
 Jul 30, 2024 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 3 min read 
 

#### NPQ: Open source CLI tool that audits and protects your npm installs from malicious packages

 

A CLI tool that checks packages for security issues and social engineering attacks before they hit your project

 
 
 Jul 26, 2025 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 3 min read 
 

#### CSS content-visibility: The Web Performance Boost You Might Be Missing

 

The content-visibility CSS property delays rendering an element, including layout and painting, until it is needed

 
 
 Dec 5, 2024 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 3 min read 
 

#### CSS :has() - The Parent Selector We've Always Wanted

 

Transform your CSS with :has(), the game-changing selector that finally lets us style elements based on their children.

 
 
 Dec 4, 2024 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 6 min read 
 

#### SecretLint — A Linter for Preventing Committing Credentials

 

A guide to catching and preventing credential leaks in your code using Secretlint

 
 
 Oct 22, 2024 
 

Read article

 
 
 
 
 
 
 
 Webdev 
 
 
 
 
 
 8 min read 
 

#### Invisible columns in SQL

 

It’s a small feature, but it can make a big difference.

 
 
 Aug 26, 2024 
 

Read article

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 all articles 
 
 
 
 
 
 

This article was originally published onhttps://www.trevorlasn.com/blog/aeo-geo-vs-seo-google-ai-optimization. It was written by a human and polished using grammar tools for
 clarity.