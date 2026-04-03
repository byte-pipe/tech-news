---
title: News publishers limit Internet Archive access due to AI scraping concerns | Nieman Journalism Lab
url: https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/
site_name: hackernews_api
content_file: hackernews_api-news-publishers-limit-internet-archive-access-due
fetched_at: '2026-02-15T11:08:45.269089'
original_url: https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/
author: ninjagoo
date: '2026-02-14'
description: Outlets like The Guardian and The New York Times are scrutinizing digital archives as potential backdoors for AI crawlers.
tags:
- hackernews
- trending
---

Jan. 28, 2026, 3:09 p.m.

Aggregation & Discovery
Business Models

## News publishers limit Internet Archive access due to AI scraping concerns

Outlets like The Guardian and The New York Times are scrutinizing digital archives as potential backdoors for AI crawlers.

By
Andrew Deck

and

Hanaa' Tameez

Jan. 28, 2026, 3:09 p.m.


Jan. 28, 2026, 3:09 p.m.

As part of its mission to preserve the web, the Internet Archive operates crawlers that capture webpage snapshots. Many of these snapshots are accessible through its public-facing tool, theWayback Machine. But as AI bots scavenge the web for training data to feed their models, the Internet Archive’s commitment to free information access has turned its digital library into a potential liability for some news publishers.

When The Guardian took a look at who was trying to extract its content, access logs revealed that the Internet Archive was a frequent crawler, saidRobert Hahn, head of business affairs and licensing. The publisher decided to limit the Internet Archive’s access to published articles, minimizing the chance that AI companies might scrape its content via the nonprofit’s repository of over one trillion webpage snapshots.

RELATED ARTICLEThe Wayback Machine’s snapshots of news homepages plummet after a “breakdown” in archiving projectsAndrew DeckOctober 21, 2025

Specifically, Hahn said The Guardian has taken steps to exclude itself from the Internet Archive’s APIs and filter out its article pages from the Wayback Machine’s URLs interface. The Guardian’s regional homepages, topic pages, and other landing pages will continue to appear in the Wayback Machine.

In particular, Hahn expressed concern about theInternet Archive’s APIs.

“A lot of these AI businesses are looking for readily available, structured databases of content,” he said. “The Internet Archive’s API would have been an obvious place to plug their own machines into and suck out the IP.” (He admits the Wayback Machine itself is “less risky,” since the data is not as well-structured.)

As news publishers try to safeguard their contents from AI companies, the Internet Archive is also getting caught in the crosshairs. The Financial Times, for example, blocks any bot that tries to scrape its paywalled content, including bots from OpenAI, Anthropic, Perplexity, and the Internet Archive. The majority of FT stories are paywalled, according to director of global public policy and platform strategyMatt Rogerson. As a result, usually only unpaywalled FT stories appear in the Wayback Machine because those are meant to be available to the wider public anyway.

“Common Crawl and Internet Archive are widely considered to be the ‘good guys’ and are used by ‘the bad guys’ like OpenAI,”said Michael Nelson, a computer scientist and professor at Old Dominion University. “In everyone’s aversion to not be controlled by LLMs, I think the good guys are collateral damage.”

RELATED ARTICLETo preserve their work — and drafts of history — journalists take archiving into their own handsHanaa' TameezJuly 31, 2024

The Guardian hasn’t documented specific instances of its webpages being scraped by AI companies via the Wayback Machine. Instead, it’s taking these measures proactively and is working directly with the Internet Archive to implement the changes. Hahn says the organization has been receptive to The Guardian’s concerns.

The outlet stopped short of an all-out block on the Internet Archive’s crawlers, Hahn said, because it supports the nonprofit’s mission to democratize information, though that position remains under review as part of its routine bot management.

“[The decision] was much more about compliance and a backdoor threat to our content,” he said.

When asked about The Guardian’s decision, Internet Archive founder Brewster Kahle said that “if publishers limit libraries, like the Internet Archive, then the public will have less access to the historical record.” It’s a prospect, he implied, that could undercut the organization’s work countering “information disorder.”

RELATED ARTICLEAfter 25 years, Brewster Kahle and the Internet Archive are still working to democratize knowledgeJoshua BentonMarch 24, 2022

The Guardian isn’t alone in reevaluating its relationship to the Internet Archive. The New York Times confirmed to Nieman Lab that it’s actively “hard blocking” the Internet Archive’s crawlers. At theend of 2025, the Times also added one of those crawlers — archive.org_bot — to itsrobots.txt file, disallowing access to its content.

“We believe in the value of The New York Times’s human-led journalism and always want to ensure that our IP is being accessed and used lawfully,” said a Times spokesperson. “We are blocking the Internet Archive’s bot from accessing the Times because the Wayback Machine provides unfettered access to Times content — including by AI companies — without authorization.”

Last August,Reddit announcedthat it would block the Internet Archive, whose digital libraries include countless archived Reddit forums, comments sections, and profiles. This content is not unlike what Reddit now licenses toGoogle as AI training data for tens of millions of dollars.

“[The] Internet Archive provides a service to the open web, but we’ve been made aware of instances where AI companies violate platform policies, including ours, and scrape data from the Wayback Machine,” a Reddit spokespersontold The Vergeat the time. “Until they’re able to defend their site and comply with platform policies…we’re limiting some of their access to Reddit data to protect redditors.”

Kahle has also alluded to steps the Internet Archive is taking to restrict bulk access to its libraries. In aMastodon postlast fall, he wrote that “there are many collections that are available to users but not for bulk downloading. We use internal rate-limiting systems, filtering mechanisms, and network security services such as Cloudflare.”

Currently, however, the Internet Archive does not disallow any specific crawlers through its robots.txt file, including those of major AI companies. As of January 12, the robots.txt file forarchive.orgread: “​​Welcome to the Archive! Please crawl our files. We appreciate it if you can crawl responsibly. Stay open!” Shortly after we inquired about this language, it was changed. The file now reads, simply, “Welcome to the Internet Archive!”

There is evidence that the Wayback Machine, generally speaking, has been used to train LLMs in the past. Ananalysis of Google’s C4 datasetby the Washington Post in 2023 showed that the Internet Archive was among millions of websites in the training data used to build Google’s T5 model and Meta’s Llama models. Out of the 15 million domains in the C4 dataset, the domain for the Wayback Machine (web.archive.org) was ranked as the 187th most present.

RELATED ARTICLEHundreds of thousands of videos from news publishers like The New York Times and Vox were used to train AI modelsAndrew DeckOctober 30, 2025In May 2023, the Internet Archive wentofflinetemporarily after an AI company caused a server overload, Wayback Machine directorMark Grahamtold Nieman Lab this past fall. The company sent tens of thousands of requests per second from virtual hosts on Amazon Web Services to extract text data from the nonprofit’s public domain archives. The Internet Archive blocked the hosts twice before putting out a public call to “respectfully” scrape its site.

“We got in contact with them. They ended up giving us a donation,” Graham said. “They ended up saying that they were sorry and they stopped doing it.”

“Those wanting to use our materials in bulk should start slowly, and ramp up,”wrote Kahle in a blog postshortly after the incident. “Also, if you are starting a large project please contact us …we are here to help.”

The Guardian’s moves to limit the Internet Archive’s access made us wonder whether other news publishers were taking similar actions. We looked at publishers’ robots.txt pages as a way to measure potential concern over the Internet Archive’s crawling.

A website’s robots.txt page tells bots which parts of the site they can crawl, acting like a “doorman,” telling visitors who is and isn’t allowed in the house and which parts are off limits. Robots.txt pages aren’t legally binding, so the companies running crawling bots aren’t obligated to comply with them, but they indicate where the Internet Archive is unwelcome.

For example, in addition to “hard blocking,” The New York Times and The Athletic include the archive.org_bot in their robots.txt file, though they do not currently disallow other bots operated by the Internet Archive.

To explore this issue, Nieman Lab used journalistBen Welsh‘sdatabase of 1,167 news websitesas a starting point. As part of a larger side project to archive news sites’ homepages, Welsh runs crawlers that regularly scrape the robots.txt files of the outlets in his database. In late December, we downloaded a spreadsheet from Welsh’s site that displayed all the bots disallowed in the robots.txt files of those sites. We identified four bots that the AI user agent watchdog serviceDark Visitorshas associated with the Internet Archive. (The Internet Archive did not respond to requests to confirm its ownership of these bots.)

This data is not comprehensive, but exploratory. It does not represent global, industry-wide trends — 76% of sites in the Welsh’s publisher list are based in the U.S., for example — but instead begins to shed light on which publishers are less eager to have their content crawled by the Internet Archive.

In total, 241 news sites from nine countries explicitly disallow at least one out of the four Internet Archive crawling bots.

Most of those sites (87%) are owned by USA Today Co., the largest newspaper conglomerate in the United States formerly known as Gannett. (Gannett sites only make up 18% of Welsh’s original publishers list.) Each Gannett-owned outlet in our dataset disallows the same two bots: “archive.org_bot” and “ia_archiver-web.archive.org”. These bots were added to the robots.txt files of Gannett-owned publications in 2025.

Some Gannett sites have also taken stronger measures to guard their contents from Internet Archive crawlers.URL searches for the Des Moines Register in the Wayback Machinereturn a message that says, “Sorry. This URL has been excluded from the Wayback Machine.”

“USA Today Co. has consistently emphasized the importance of safeguarding our content and intellectual property,” a company spokesperson said via email. “Last year, we introduced new protocols to deter unauthorized data collection and scraping, redirecting such activity to a designatedpageoutlining our licensing requirements.”

Gannett declined to comment further on its relationship with the Internet Archive. In an October 2025earnings call, CEO Mike Reed spoke to the company’s anti-scraping measures.

“In September alone, we blocked 75 million AI bots across our local and USA Today platforms, the vast majority of which were seeking to scrape our local content,” Reed said on that call. “About 70 million of those came from OpenAI.” (Gannett signed a content licensing agreement with Perplexity in July 2025.)

About 93% (226 sites) of publishers in our dataset disallow two out of the four Internet Archive bots we identified. Three news sites in the sample disallow three Internet Archive crawlers: Le Huffington Post, Le Monde, and Le Monde in English, all of which are owned by Group Le Monde.

RELATED ARTICLESome French publishers are giving AI revenue directly to journalists. Could that ever happen in the U.S.?Andrew DeckSeptember 4, 2025

The news sites in our sample aren’t only targeting the Internet Archive. Out of the 241 sites that disallow at least one of the four Internet Archive bots in our sample, 240 sites disallow Common Crawl — another nonprofit internet preservation project that has beenmore closely linked to commercial LLM development. Of our sample, 231 sites all disallow bots operated by OpenAI, Google AI, and Common Crawl.

As we’vepreviously reported, the Internet Archive has taken on the Herculean task of preserving the internet, and many news organizations aren’t equipped to save their own work. In December, Poynterannounceda joint initiative with the Internet Archive to train local news outlets on how to preserve their content. Archiving initiatives like this, while urgently needed, are few and far between. Since there is no federal mandate that requires internet content to be preserved, the Internet Archive is the most robust archiving initiative in the United States.

“The Internet Archive tends to be good citizens,” Hahn said. “It’s the law of unintended consequences: You do something for really good purposes, and it gets abused.”

Photo of Internet Archive homepage bySDF_QWEused under an Adobe Stock license.

Andrew Deck
 is a staff writer covering AI at Nieman Lab. Have tips about how AI is being used in your newsroom? You can reach Andrew via
email
,
Bluesky
, or Signal (+1 203-841-6241).
Hanaa' Tameez
 is a staff writer at Nieman Lab. You can reach her via
email
 (
[email protected]
),
Bluesky DM
 (@hanaatameez.bsky.social), or on
Signal
 (@hanaatameez.01).

POSTED
     
Jan. 28, 2026
, 3:09 p.m.

SEE MORE ON

Aggregation & Discovery

AI
AI bots
archives
digital archiving
Gannett
generative AI
Internet Archive
Le Monde
LLMs
NYT
scraping
The Guardian
The New York Times
training data
USA Today Co.
Wayback Machine

Show tags
Hide tags

  TWITTER

  FACEBOOK

  EMAIL

  SHARE ON FACEBOOK

  TWEET

 

Join the 60,000 who get the freshest future-of-journalism news in our daily email.

		Washington Post layoffs disproportionately affected union members of color, preliminary Guild data shows
“We cannot ignore what this means for equity, representation, and the future of this organization.”

		The Atlantic’s Elizabeth Bruenig on her “hypothetical,” heavily reported measles essay
“We were attracted to the idea of providing a play-by-play of the progression of measles in granular detail.”

		In the video game News Tower, as in real life, running a newspaper isn’t easy
The game, which puts you in the shoes of a newspaper publisher in the 1930s, is a test of your management skills — and your ethics.

Hanaa' Tameez
Washington Post layoffs disproportionately affected union members of color, preliminary Guild data shows
“We cannot ignore what this means for equity, representation, and the future of this organization.”
Laura Hazard Owen
The Atlantic’s Elizabeth Bruenig on her “hypothetical,” heavily reported measles essay
“We were attracted to the idea of providing a play-by-play of the progression of measles in granular detail.”
Neel Dhanesha
In the video game News Tower, as in real life, running a newspaper isn’t easy
The game, which puts you in the shoes of a newspaper publisher in the 1930s, is a test of your management skills — and your ethics.

* Subscribe
* Twitter
* Facebook
* RSS
* About
* Contact
* Archives

Help advance the Nieman Foundation’s mission “to promote and elevate the standards of journalism”
by making a donation
.

To promote and elevate the standards of journalism



Covering thought leadership in journalism



Pushing to the future of journalism



Exploring the art and craft of story



© 2026 by the President and Fellows of Harvard College
  /  
Some rights reserved

Harvard

Trademark

Privacy

Digital Accessibility

Walter Lippmann House
    
One Francis Ave.
    
Cambridge, MA 02138
    
617 495 2237

The Nieman Journalism Lab is a collaborative attempt to figure out how quality journalism can survive and thrive in the Internet age.

It’s a project of theNieman Foundation for Journalism at Harvard University.

Follow us

* Subscribe to our email
* Follow us on Twitter
* Like us on Facebook
* Download our iPhone app
* Subscribe via RSS

Subscribe to our work →

The basics

* About us
* Contact
* Archives

Projects

* Encyclo
* Fuego
* Tweet archive

About us →

Director

Joshua Benton

Staff writers

Justin Ellis

Caroline O’Donovan

© President and Fellows of Harvard College, unless otherwise noted.
Some rights reserved.
