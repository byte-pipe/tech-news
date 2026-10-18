---
title: An LLM-friendly website checklist, with a test for each step
url: https://pournasserian.com/writing/llm-friendly-website-checklist
site_name: tldr
content_file: tldr-an-llm-friendly-website-checklist-with-a-test-for
fetched_at: '2026-10-18T21:14:56.521789'
original_url: https://pournasserian.com/writing/llm-friendly-website-checklist
date: '2026-10-18'
published_date: '2026-10-18'
description: Eight steps to make a website easy for AI crawlers and agents to read, in the order the bots actually fetched them, each with a command you can run to check your own site.
tags:
- tldr
---

# An LLM-friendly website checklist: eight steps and a test for each

October 18, 2026

Mylonger article on making a website AI friendlyends with a checklist: eight things I’d do, in the order the evidence says they get read. The evidence was 18 days of this site’s Cloudflare logs (30 September to 17 October 2026) and the standards and vendor documentation as they stood on 18 October 2026. A list only helps if you can tell when an item is done, so here it is again, short, with a check for each step that you can run against your own site in a minute or two. LLM-friendly, friendly to large language models (LLMs), means here what AI friendly means there: a site that AI crawlers and agents can find, read and cite.

The checks are shell commands. Set your site’s address once, and the rest can be pasted as they are:

SITE
=
https://example.com

## In brief

1. Serve the text in the HTML.Most AI crawlers don’t run JavaScript, so text built in the browser can be invisible to them.
2. Write arobots.txtthat answers each purpose.The big operators split their crawlers into training, search and fetching for a person, so you can say yes or no to each.
3. Keep a sitemap with honestlastmoddates, and ping IndexNow when you deploy.ClaudeBot fetched this site’s sitemap 122 times in 18 days.
4. Publish a Markdown copy of each page and name it in the head.Seven verified crawlers found this site’s copies the day after they went live.
5. Put the whole post in your feeds.Feeds are read mostly by feed readers, and most of their requests only ask whether anything changed.
6. Add anllms.txtfor coding agents.No verified AI or search crawler fetched this site’s in 17 days, but coding agents do read the file.
7. If you want agents to search you, run an MCP server and publish an AI Catalog.No mainstream client finds a site’s server on its own yet, so hand out the address yourself.
8. Measure at the edge, and count only verified bots.113 requests here said they came from PerplexityBot without Cloudflare verifying them.

## Serve the text in the HTML

The text of each page has to be in the HTML your server sends, because most AI crawlers don’t run JavaScript. InVercel’s measurement of December 2024, OpenAI’s, Anthropic’s and Perplexity’s crawlers didn’t, while Googlebot and Applebot did, so a page whose text is built in the browser can look fine in Google and be empty to most AI crawlers. The rest is what has always helped a machine read a page: one<main>, real headings, and JSON-LD that matches what the page shows.

Fetch a page the way a crawler without JavaScript does, and look for a few plain words from a paragraph you can see in the browser:

curl 
-s
 "$SITE/about"
 |
 grep 
-c
 "a few plain words from the page"

curl 
-s
 "$SITE/about"
 |
 grep 
-o
 "<main"
 |
 wc 
-l

curl 
-s
 "$SITE/about"
 |
 grep 
-c
 "application/ld+json"

The first should print 1 or more; 0 means the text arrives later, from a script. Pick words without apostrophes or quotes, which the HTML may write differently. The second should print 1, and the third at least 1.

To see what a text extractor keeps, askJina Reader, a service that turns a page into text for language models. The page’s title and its text should be there:

curl 
-s
 "https://r.jina.ai/$SITE/about"
 |
 head 
-20

## Write a robots.txt that answers each purpose

Arobots.txtfile lets you answer each kind of crawler separately, because the big operators split theirs by purpose: training crawlers (GPTBot, ClaudeBot, Amazonbot), search crawlers that build the index AI answers cite (OAI-SearchBot, Applebot, Googlebot), and fetchers that get one page because a person asked (ChatGPT-User, Claude-User, Perplexity-User). Its rules are not a form of access control, and the fetchers may not follow them: OpenAI says they may not apply to ChatGPT-User, and Perplexity says Perplexity-User generally ignores them, while Anthropic says all three of its bots honour them, Claude-User included. Cloudflare’sContent Signals Policyadds aContent-Signalline that says what may be done with the content once it’s fetched, with three answers,search,ai-inputandai-train, though none of the crawler documentation I read mentions it yet. Mine says yes to all three:

User-agent: *

Content-Signal: search=yes, ai-input=yes, ai-train=yes

Allow: /

Sitemap: https://pournasserian.com/sitemap.xml

Check the file crawlers actually get, not the one in your repository. On Cloudflare, for example, the managedrobots.txtwould addai-train=noto it.

curl 
-s
 "$SITE/robots.txt"

Look for aUser-agentgroup for each crawler you treat differently, and make sure the*group says what you mean for everyone else.

## Keep the sitemap’s dates honest, and ping IndexNow

A sitemap is read often, so itslastmoddates are worth getting right: ClaudeBot fetched this site’s sitemap 122 times in 18 days, Googlebot 19 times and GPTBot 10.Googleuseslastmodonly when it’s consistently accurate, so each page’s date should be the day its content last changed, never the build date.

IndexNow is the other half. It’s a protocol that lets a site ping one search engine when an address is added, changed or deleted, and that engine shares the ping with the others in itsregistry: Bing, Yandex, Seznam, Naver, Yep, the Internet Archive and Amazonbot. Bing’s guidelines say timely pings reduce outdated addresses in Copilot answers. Google isn’t part of it.

curl 
-s
 "$SITE/robots.txt"
 |
 grep 
-i
 "^sitemap"

curl 
-s
 "$SITE/sitemap.xml"
 |
 grep 
-o
 "<lastmod>[^<]*"
 |
 sort 
|
 uniq 
-c
 |
 sort 
-rn
 |
 head

The first should name your sitemap. The second counts the addresses that share each date: if one date covers nearly all of them, it’s probably the day you last built the site. If your sitemap is an index of other sitemaps, run it on each of those.

For IndexNow, the key file at your site’s root should print your key, and each ping your deploy sends should get200or202back, both of which mean the ping was received:

curl 
-s
 "$SITE/your-key.txt"

## Publish a Markdown copy of each page

A Markdown copy of each page, named in the page’s head, was the door crawlers found fastest on this site: seven verified crawlers fetched the copies, starting the day after they went live, and Amazonbot most of all. Here each copy sits at its page’s address with.mdadded, is served astext/markdown, is kept out of search results withnoindex, and is named in the page’s head:

<
link
 rel=
"alternate"
 type=
"text/markdown"
 href=
"/about.md"
>

curl 
-s
 "$SITE/about"
 |
 grep 
-o
 '<link[^>]*text/markdown[^>]*>'

curl 
-s
 -o
 /dev/null
 -D
 -
 "$SITE/about.md"
 |
 grep 
-i
 "^content-type"

The first should print the link, and the secondtext/markdown.

You can also answer a request for Markdown at the page’s own address, which is how coding agents ask: Claude Code sendsAccept: text/markdown, text/html, */*. The server answers with Markdown andVary: Accept, and sends a browser, which asks fortext/html, the HTML it always had, with the sameVary: Accept, so a cache keeps the two apart.

A browser → Your site: GET /about, Accept: text/html; Your site → A browser: The HTML it always had, Vary: Accept; A coding agent → Your site: GET /about, Accept: text/markdown; Your site → A coding agent: Markdown, Vary: Accept
A coding agent
Your site
A browser
GET /about, Accept: text/html
The HTML it always had, Vary: Accept
GET /about, Accept: text/markdown
Markdown, Vary: Accept

curl 
-s
 -o
 /dev/null
 -D
 -
 -H
 "Accept: text/markdown"
 "$SITE/about"
 |
 grep 
-iE
 "^(content-type|vary)"

curl 
-s
 -o
 /dev/null
 -D
 -
 "$SITE/about"
 |
 grep 
-iE
 "^(content-type|vary)"

The first should printtext/markdownandVary: Accept, the secondtext/htmland the sameVary: Accept. If your site is on a Cloudflare Pro plan or above,Markdown for Agentsdoes the negotiation for you by converting your HTML at the edge.

## Put the whole post in your feeds

A feed that carries each post in full is still read, mostly by feed readers, and most of their requests only ask whether anything changed: in a 30-day count, 401 of 551 answers on this site’s/rss.xmlwere304 Not Modified. Google and Bing both accept a feed as a sitemap, which is one more reason to keep it.

curl 
-s
 "$SITE/rss.xml"
 |
 grep 
-o
 "<item>"
 |
 wc 
-l

curl 
-s
 "$SITE/rss.xml"
 |
 grep 
-o
 "<content:encoded>"
 |
 wc 
-l

curl 
-s
 -o
 /dev/null
 -D
 -
 "$SITE/rss.xml"
 |
 grep 
-iE
 "^(etag|last-modified)"

In an RSS feed the first two numbers should match: one full text for each post. The third should print anETagor aLast-Modifiedheader, which is what lets a reader ask whether anything changed. Send theETagback, and the answer should be304:

curl 
-s
 -o
 /dev/null
 -w
 "%{http_code}\n"
 -H
 'If-None-Match: "the-etag-you-got"'
 "$SITE/rss.xml"

## Add an llms.txt for coding agents

Anllms.txtis cheap to add and coding agents read it, but don’t expect search or AI crawlers to: in 17 days, no verified AI or search crawler fetched this site’s. It’s a Markdown file at a site’s root that gives language models a short map of the site, a title, a one-line summary and lists of links, asthe proposaldescribes.Gauge found Codexopening one in about a third of its sessions, while Google Search says it doesn’t use the file.

curl 
-s
 "$SITE/llms.txt"
 |
 head 
-5

It should open with a#title and a>summary line, with the lists of links under##headings after them. Lighthouse’s Agentic Browsing category, also inPageSpeed Insights, checks the file’s form when there is one and doesn’t penalise a site without one.

## Run an MCP server and publish an AI Catalog

An MCP server lets an agent search your site rather than read it page by page, but you’ll have to hand out its address yourself, because no mainstream client finds a site’s server on its own yet. MCP, the Model Context Protocol, is an open standard that connects AI applications to outside systems. An AI Catalog is a JSON file at/.well-known/ai-catalog.jsonthat lists a site’s AI artifacts, such as its MCP server’s card, the route theMCP Server Cards proposalsets out. This site runsmcp-my-site, the open-source server I built, and the44 tools in my earlier roundupare the ways to get one without writing it.

curl 
-s
 "$SITE/.well-known/ai-catalog.json"
 |
 head 
-12

It should print JSON with an entry of typeapplication/mcp-server-card+jsonfor your server. Then connect a client to the server’s address and list its tools; the officialMCP Inspectordoes it, and I compared it with the other testing tools inan earlier article. Last, check that a person can find the address on your site, as theagents pagegives it here.

## Measure at the edge, and count only verified bots

Count crawlers in your CDN’s or your server’s logs, and only the ones verified, because a crawler’s name in a request proves nothing: 113 requests here said they came from PerplexityBot without Cloudflare verifying them. Analytics that run as JavaScript in the page can’t see them, since most AI crawlers don’t run scripts. Cloudflare verifies a crawler by a published IP list, reverse DNS or a signature on the request; count what passes, and count a request that only names a crawler apart.

A request names a crawler → A published IP list; A request names a crawler → Reverse DNS; A request names a crawler → A signature on the request; A published IP list → Verified, count it; Reverse DNS → Verified, count it; A signature on the request → Verified, count it; A request names a crawler → Only named, count it apart: none of them
A request names a crawler
A published IP list
Reverse DNS
A signature on the request
Verified, count it
Only named, count it apart
none of them

On Cloudflare,AI Crawl Controlis on every plan, and theGraphQL Analytics APIbehind it keeps 31 days on the Free plan. This query lists who fetched one path in a week.requestSource: "eyeball"leaves out Cloudflare’s own requests, the host filter leaves out your zone’s other hostnames, and an emptyverifiedBotCategorymeans Cloudflare didn’t verify the request, whatever its user agent says:

query
 {

 viewer {

 zones(filter: { 
zoneTag
: 
"YOUR_ZONE_ID"
 }) {

 httpRequestsAdaptiveGroups(

 filter: {

 datetime_geq
: 
"2026-10-11T00:00:00Z"

 datetime_lt
: 
"2026-10-18T00:00:00Z"

 requestSource
: 
"eyeball"

 clientRequestHTTPHost
: 
"example.com"

 clientRequestPath
: 
"/llms.txt"

 }

 limit: 20

 orderBy: [count_DESC]

 ) {

 count

 dimensions { verifiedBotCategory userAgent }

 }

 }

 }

}

Off Cloudflare, you can check a crawler by reverse DNS yourself. Look up the address a request came from:Google’s crawlersresolve to a name undergooglebot.com,google.comorgoogleusercontent.com, and that name resolves back to the same address.

nslookup 
66.249.66.1

nslookup 
crawl-66-249-66-1.googlebot.com

## Method and caveats

* The steps, their order and every figure come fromthe longer article, which read this site’s Cloudflare logs from 30 September to 17 October 2026 and the standards and documentation as they stood on 18 October 2026. Its own method and caveats apply here.
* The checks are new in this article. I ran each one against this site on 18 October 2026: the shell commands with curl in bash (they’re written for a Unix shell such as bash or zsh), the GraphQL query against this site’s Cloudflare zone, and the two lookups against the Googlebot address shown. I didn’t send an IndexNow ping for this article;200and202are the answers IndexNow’s documentation lists for a ping it received.
* A check that passes says a door is open, not that anyone uses it, and a count of requests says nothing about what a crawler did with a page.
* This is one small personal site. A larger or busier site will see more crawlers and different proportions, and several of the standards here were still changing when I wrote this.