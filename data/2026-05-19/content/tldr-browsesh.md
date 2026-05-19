---
title: browse.sh
url: https://browse.sh/
site_name: tldr
content_file: tldr-browsesh
fetched_at: '2026-05-19T19:37:09.909518'
original_url: https://browse.sh/
date: '2026-05-19'
description: A starter page for a fast, scriptable browsing workspace.
tags:
- tldr
---

* 12306.cn·find-trains
* abc7news.com·cali-highway-traffic
* airbnb.com·search-listings
* aivaclaims.com·claims-search
* algolia.com·search-documentation

The open web catalog

## A browser CLI for your AI Agents

One CLI for skills, browser primitives, debugging, and cloud sessions, designed to be driven by AI Agents.

npm install -g browse
Web skill
Browser automation
Debugging
Cloud

Give AI Agents the skills to automate websites from the open web catalog. Suggested DOM selectors and XHR requests cut token costs by 50x.

Commands
$ 
browse skills add alltrails.com

$ 
browse skills add recreation.gov

$ 
browse skills add weather.gov

$ 
browse skills add plugshare.com

$ 
browse skills add ramp.com

 

$ 
claude 
"Plan a road trip to Utah with EV charging stops and campsites for each night. Book and reimburse on Ramp."

Drive any page with low-level primitives: click, scroll, type, hover, press. Address elements by selector or by the AI Agent's accessibility refs.

Commands
$ 
browse click 
"input#search"

$ 
browse type 
"Apartments in SF"

$ 
browse select @8 
"Single family unit"

$ 
browse press 
"Enter"

$ 
browse mouse scroll 50 50 10 10

$ 
browse screenshot

Tail the network and console of any browse session in real time. AI Agents (and you) see exactly what the page did.

Commands
$ 
browse network --tail

$ 
browse console --tail
Output
GET
 
/api/listings
 
200
 
124 ms

POST
 
/api/filter
 
200
 
84 ms

 

warn deprecated: useLayoutEffect on server

error Uncaught TypeError: cannot read 'id'

All CLI commands work natively with local Chromium. Switch to remote sessions onBrowserbase's Platformby prefixing any command withcloud.

Commands
# create a remote chromium session on Browserbase

$ 
browse cloud sessions create

 

# use Browserbase's Search API

$ 
browse cloud search 
"Latest White House press release"

 

# use Browserbase's Fetch API

$ 
browse cloud fetch 
"https://www.nytimes.com/section/us"

Give AI Agents the skills to automate websites from the open web catalog. Suggested DOM selectors and XHR requests cut token costs by 50x.

Commands
$ 
browse skills add alltrails.com

$ 
browse skills add recreation.gov

$ 
browse skills add weather.gov

$ 
browse skills add plugshare.com

$ 
browse skills add ramp.com

 

$ 
claude 
"Plan a road trip to Utah with EV charging stops and campsites for each night. Book and reimburse on Ramp."
/
All
Government
Healthcare
Retail
Browser
Official Partners
Add website
1. 01find-trains12306.cnQuery China Railway (12306.cn) for the train schedule between two stations on a given date — train number, departure/arrival station + time, journey duration, and per-class seat availability. Read-only; no login.hybrid
2. 02cali-highway-trafficabc7news.comReturn current real-time MPH for every California highway covered by ABC7's traffic map — per road, per direction, with active incidents — by querying the Sigalert/Total Traffic Network JSON backend that the abc7news.com/traffic/ page embeds via iframe.api
3. 03search-listingsairbnb.comSearch Airbnb for short-term rental listings in a given location and date window — supporting the full filter surface (dates, guests, price, place + property type, bedrooms / beds / baths, amenities, booking options, accessibility, host language, the top-of-page category rail, and map bounding box) — and return each matching property as structured JSON via the SSR StaysSearch GraphQL blob embedded in the page. Read-only.browser
4. 04claims-searchaivaclaims.comSearch AIVA Claims Assistant's public 22-entry FAQ knowledge base for VA-disability-claim service info (eligibility, pricing, process, AI-model vendor, accreditation). Returns matching Q&A pairs by category. Read-only; no sign-in.browser
5. 05search-documentationalgolia.comSearch algolia.com/doc for documentation pages matching a free-text query and return ranked hits with section hierarchy, snippets, and direct anchor URLs — via the public hosted DocSearch API, with a per-page markdown fallback.api
6. 06search-productaliexpress.comSearch AliExpress by product name / keyword and return a structured list of matching listings — productId, canonical detail URL, title, current price, list price, discount %, rating, sold count, and badges. Read-only.browser
7. 07search-recipesallrecipes.comSearch Allrecipes for recipes (keyword, ingredient list, category browse, or direct recipe URL) and return structured JSON with ratings, ingredients, instructions, nutrition, times, and full media — by parsing the SSR HTML search cards and each recipe page's schema.org LD+JSON Recipe block.api
8. 08search-trailsalltrails.comSearch AllTrails for hiking, biking, running, climbing, backpacking, or paddling trails near a location with the full filter panel surface (activity, difficulty, length, elevation, route type, suitability, traffic, attributes, rating, sort). Returns structured JSON with name, location, coordinates, length/elevation, difficulty, rating, photos, description, dog/kid policy, and region-wide totals. Read-only.api
9. 09search-productsamazon.comSearch Amazon (any storefront TLD) for products matching a keyword, full search URL, ASIN list, or category-browse intent, with full filter-rail coverage (department, brand, rating, price, Prime, delivery speed, deals, condition, seller, apparel attrs, niche filters, sort, pagination). Returns structured per-product JSON with ASIN, title, brand, image, prices, rating, badges, and canonical /dp URL.browser
10. 10browse-productsamazon.inSearch Amazon.in by keyword and return structured product listings — ASIN, title, current price (INR), MRP, rating, review count, canonical URL, sponsored flag, and free-delivery flag — from the first search-results page.browser
11. 11discover-industrial-opportunitiesamericanreindustrialization.comDiscover companies, startups, suppliers, and job opportunities across American reindustrialization — manufacturing, energy, defense, aerospace, robotics, semiconductors, and industrial software — via the site's public JSON REST API at /api/* (companies, jobs, categories, tags).api
12. 12search-rentalsapartments.comSearch Apartments.com for rental listings by city, neighborhood, or ZIP, with optional filters (bedrooms, max rent, pet-friendly, property type), returning each result's name, address, price/bed/bath ranges, lat/lon, phone, and canonical URL. Read-only.url-param
13. 13picture-of-the-dayapod.nasa.govFetch NASA's Astronomy Picture of the Day (APOD) — today's curated image or video plus title, explanation, copyright, and HD image URL. Supports any date back to 1995-06-16.api
14. 14find-yoga-meditation-classapp.ompractice.comFind upcoming live yoga, meditation, tai chi, breathwork, and movement classes on Ompractice that match a user's interests, availability, experience level, intensity preference, and class-length preference. Uses Ompractice's unauthenticated DRF API at api.ompractice.com. Read-only — does not book.api
15. 15search-tennis-utrapp.utrsports.netSearch Universal Tennis Rating (UTR) for players by name and return each match's UTR (singles + doubles), three-month rating, profile id, nationality, location, pro status, and third-party rankings via the public api.utrsports.net REST API.api
16. 16find-snapshotarchive.orgFind Internet Archive Wayback Machine snapshots for a URL — single closest, date range, host/prefix enumeration, or full history — returning archived URL, capture timestamp, HTTP status, MIME type, SHA-1 digest, and WARC-record length. Read-only.api
17. 17ai-company-searchartificialintelligencecompanies.comSearch artificialintelligencecompanies.com to find AI vendors and startups serving a given niche or addressing a given problem, returning name, canonical URL, and description per match via the site's public JSON API and JSON-LD category pages.api
18. 18search-papersarxiv.orgSearch arXiv for preprints by free-form query, field operators (ti/au/abs/cat/jr/co/rn), category, date range, or arXiv ID, and return structured paper records (title, authors, abstract, primary + cross-listed categories, submitted/updated dates, version, comments, journal_ref, DOI, PDF/abs URLs) plus total result count. Read-only.api
19. 19manage-candidate-profileashbyhq.comSearch Ashby ATS for a candidate by email or name, read their full profile (contact info, applications, tags, custom fields, notes), add a note, and submit structured interview feedback against an application — via Ashby's documented REST API.api
20. 20cli-setupauto.devInstall, authenticate, and verify the @auto.dev/sdk npm package so a downstream agent can run any Auto.dev automotive data task (VIN decode, listings, photos, specs, recalls, payments, APR, TCO, plate-to-VIN, taxes) via the global `auto` CLI, the bundled stdio MCP server, or the JS/TS SDK.cli
21. 21longtermavis.comSearch Avis.com for long-term (15-330 day) rental car options at US locations. Returns per-class daily/total prices with pay-now vs pay-later, plus the cheapest deal across the fleet. Read-only; designed for looped multi-location scans to surface unusually cheap long-term deals.browser
22. 22compare-savings-ratesbankrate.comReturn ranked Bankrate savings, money-market, and CD rates as structured JSON — bank name, account name, APY, minimums, fees, FDIC/NCUA status, Bankrate score, editorial copy, last-updated timestamp, and affiliate Open Account URLs (captured, never followed). Lead with a Browserbase Fetch of the editorial best-of article; fall back to a remote browser session for the dynamic WRT (Wealth Rate Table) widget when filter dimensions exceed what static HTML exposes.url-param
23. 23news-homepagebbc.co.ukReturn the current set of top stories from the BBC News homepage — title, summary, canonical article URL, publication timestamp, section, and thumbnail — via the public RSS feed at feeds.bbci.co.uk/news/rss.xml. Read-only.api
24. 24check-stockbestbuy.comGiven a Best Buy SKU or product URL (and optional ZIP), return current price, online Ship-to-Home availability with ETA, pickup availability at nearby stores within radius, plus product title/brand/model/limit notice. Read-only — never adds to cart or reserves.browser
25. 25search-specialty-coffeebiomacoffee.comEnumerate Bioma Coffee Roasters' (Chile) specialty-coffee catalog and filter by origin or tasting-note query. Returns title, origin, notes, starting price (CLP), available variants, SCA score, rating, and product URL. Read-only.browser
26. 26get-bitcoin-feesbitcoinsapi.comFetch current Bitcoin fee-rate recommendations (fastest, halfHour, hour, economy, minimum) in sat/vB from the Satoshi API's free /api/v1/fees/recommended endpoint. Read-only HTTP GET — no API key, wallet, or signup required.api
27. 27find-california-businessbizfileonline.sos.ca.govSearch California's bizfileonline.sos.ca.gov portal for a registered business entity by name or entity number, returning status, entity type, formation date, jurisdiction, registered agent, and principal address.browser
28. 28find-fundingbja.ojp.govEnumerate U.S. DOJ Bureau of Justice Assistance funding opportunities (currently open or closed/expired) as structured JSON via the public funding-api JSON endpoint — title, opportunity ID, status, solicitation type, topics, deadlines, eligible applicants, and NOFO PDF URL — with client-side filtering on keyword, topic, applicant type, and date range.api
29. 29search-hotelsbooking.comSearch Booking.com for hotels, apartments, hostels, and other accommodations in a given destination and date window. Supports the full Booking filter surface (property type, stars, review score, distance, neighborhoods, hotel/room facilities, meal plans, cancellation policy, brand chains, sustainability badges, Genius, sort order) and emits structured per-property JSON with the lead room offer. Read-only.browser
30. 30find-sea-ranch-housebooksearanchescape.escapia.comFind Sea Ranch vacation-rental homes on booksearanchescape.escapia.com by date range, party size, bedrooms, and pet allowance. Returns availability (day-by-day JSON), rate quotes, amenities, and detail-page links. Read-only — never books.url-param
31. 31bountybountybook.aiPost a USDC-escrowed bounty on BountyBook for autonomous agents to claim. Returns the job ID, the agent tracking URL at /job/{uuid}, the API status endpoint, and the x402 escrow payment instructions. Recommends the agent-first REST API at api.bountybook.ai over the wallet-extension-bound browser flow.api
32. 32moneymaxxbountybook.aiDiscover open BountyBook bounties matching agent skill categories, minimum USDC reward, and maximum deadline via the agent-native REST API, then claim, submit (inline JSON or IPFS CID), and poll AI-oracle verification and on-chain payout status.api
33. 33autobrowsebrowserbase.comSelf-improving browser automation via the auto-research loop. Iteratively runs a browsing task, reads the trace, and improves the navigation skill (strategy.md) until it reliably passes. Supports parallel runs across multiple tasks using sub-agents. Use when you want to build or improve browser automation skills for specific website tasks.cli
34. 34browserbrowserbase.comAutomate web browser interactions using natural language via CLI commands. Use when the user asks to browse websites, navigate web pages, extract data from websites, take screenshots, fill forms, click buttons, or interact with web applications. Supports remote Browserbase sessions with Browserbase Identity, Verified browsers, automatic CAPTCHA solving, and residential proxies — ideal for protected websites and JavaScript-heavy pages.cli
35. 35browser-to-apibrowserbase.comTurn a website's observable HTTP traffic into a best-effort OpenAPI 3.1 spec by analyzing a `browser-trace` capture. Use when the user wants to discover/extract API endpoints from a browser session, build an OpenAPI doc from network traffic, or document a third-party site's XHR/fetch surface for client integration.cli
36. 36browser-tracebrowserbase.comCapture a full DevTools-protocol trace of any browser automation — CDP firehose, screenshots, and DOM dumps — then bisect the stream into per-page searchable buckets. Use when the user wants to debug a failed run, audit network/console/DOM activity, attach a trace to an in-progress session, or feed structured per-page summaries back into an agent loop so its next iteration learns from the last one.cli
37. 37browserbase-clibrowserbase.comUse the Browserbase CLI (`browse`) for Browserbase Functions and platform API workflows. Use when the user asks to run `browse`, deploy or invoke functions, manage sessions, projects, contexts, or extensions, fetch a page through the Browserbase Fetch API, search the web through the Browserbase Search API, or scaffold starter templates. Prefer the Browser skill for interactive browsing; use the top-level `browse` driver commands (`browse open`, `browse get`, etc.) only when the user explicitly wants the CLI path.cli
38. 38company-researchbrowserbase.comCompany discovery and deep research skill. Researches a company's product and ICP,
discovers target companies to sell to using Browserbase Search API, deeply researches
each using a Plan→Research→Synthesize pattern, and scores ICP fit — compiled into
a scored research report and CSV. Supports depth modes (quick/deep/deeper) for
balancing scale vs intelligence.
Use when the user wants to: (1) find companies to sell to, (2) research potential
customers, (3) discover companies matching an ICP, (4) build a target company list,
(5) do market research on prospects. Triggers: "find companies to sell to",
"company research", "find prospects", "ICP research", "target companies",
"who should we sell to", "market research", "lead research", "prospect list".cli
39. 39cookie-syncbrowserbase.comSync cookies from local Chrome to a Browserbase persistent context so the browse CLI can access authenticated sites. Use when the user wants to browse as themselves, sync cookies, or log into sites via Browserbase.cli
40. 40event-prospectingbrowserbase.comEvent prospecting skill. Takes a conference / event speakers URL,
extracts the people, filters their companies against the user's
ICP, then deep-researches only the speakers at ICP-fit companies.
Outputs a person-first HTML report where each card answers "why
should the AE talk to this person?" with all public links and a
one-click DM opener.
Use when the user wants to: (1) find leads at a specific
conference, (2) prep for an event, (3) research event speakers,
(4) build a target list from a sponsor/exhibitor page,
(5) scrape conference speakers and rank by ICP fit.
Triggers: "find leads at {event}", "research speakers at",
"prospect this conference", "stripe sessions leads",
"ai engineer summit prospects", "event prospecting",
"scrape conference speakers", "who should I meet at".cli
41. 41fetchbrowserbase.comUse this skill when the user wants to retrieve a URL without a full browser session: fetch HTML or JSON from static pages, inspect status codes or headers, follow redirects, or get page source for simple scraping. Prefer it over a browser when JavaScript rendering and page interaction are not needed. Supports proxies and redirect control.cli
42. 42find-templatesbrowserbase.comList Browserbase's starter templates (TypeScript / Python / Go) and the canonical clone command for each, sourced from the official bb CLI's templates subcommand which reads github.com/browserbase/templates@dev.cli
43. 43functionsbrowserbase.comDeploy serverless browser automation as cloud functions using Browserbase. Use when the user wants to deploy browser automation to run on a schedule or cron, create a webhook endpoint for browser tasks, run automation in the cloud instead of locally, or asks about Browserbase Functions.cli
44. 44safe-browserbrowserbase.comBuild local constrained-browser agents with a safe_browser tool that owns CDP, enforces a domain allowlist with Fetch interception, and lets a runtime Claude Agent SDK agent complete browsing tasks without raw browser, shell, or CDP access. Use when the user wants an agent to browse or scrape while staying on approved domains, demo blocked off-domain navigation, or generate a safe browser client.cli
45. 45searchbrowserbase.comUse this skill when the user wants to search the web without a full browser session: find URLs, titles, and metadata for a query. Prefer it over a browser when you just need search results, not page content. Returns structured results with titles, URLs, authors, and dates.cli
46. 46ui-testbrowserbase.comAI-powered adversarial UI testing via the browse CLI. Analyzes git diffs to test only what changed, or explores the full app to find bugs. Tests functional correctness, accessibility, responsive layout, and UX heuristics. Use when the user asks to test UI changes, QA a pull request, audit accessibility, or run exploratory testing. Supports local browser (localhost) and remote Browserbase (deployed sites).cli
47. 47search-by-jurisdictionbusinessdataguide.comLook up the official company registry and KYB workflow for any of 209 jurisdictions on businessdataguide.com — registry name+URL, cost band (USD), English-UI, account/local-ID requirements, captcha+2FA friction, API availability, turnaround, and last-verified date. Direct URL fetch (no browsing required); soft-404 handling for unknown slugs.url-param
48. 48search-listingscargurus.comSearch CarGurus for vehicle listings across the full filter surface (make/model/trim, year/price/mileage range, condition, body, fuel, drivetrain, color, features, deal-rating, dealer rating, history, ZIP+radius) and return each listing's CarGurus IMV deal rating, dollar delta vs IMV, IMV midpoint, full vehicle/dealer detail, and canonical URL. Read-only.browser
49. 49search-listingscars.comSearch Cars.com new + used + CPO inventory across the full Cars.com filter rail (make/model/trim, year/price/mileage ranges, body/fuel/transmission/drivetrain, color, features, vehicle history, seller type, location + radius, sort, pagination) and return active listings — with VIN, full title, price + MSRP + deal-rating delta, mileage, dealer name + rating + distance, photos, and canonical VDP URL — as structured JSON. Read-only.api
50. 50search-christian-productschristianpicks.comSearch and filter the ChristianPicks directory of 500+ Christian apps, software, businesses, ministries, books, and media by query, category, pricing model, platform, or popularity; surface product details, vendor links, and comparison-ready recommendations.hybrid
51. 51citymall-myanmarcitymall.com.mmWalk the full citymall.com.mm category taxonomy (groceries, fresh produce, beverages, electronics, fashion, beauty, pet supplies, home appliances and more), set a delivery township so inventory is correctly scoped to Yangon or Mandalay, and extract structured product cards.browser
52. 52find-classclasspass.comSearch ClassPass for available fitness, wellness, beauty, or recovery class slots near a location and return matching results as structured JSON (class id, instructor, venue, start/end time in tz, credit cost, premium flag, modality, spots, amenities, rating). Accepts free-form intent, ZIP/city + category + date, a direct /search URL, or a venue slug. Read-only — never books.browser
53. 53extract-product-offerscomprasparaguai.com.brExtract structured product offers from comprasparaguai.com.br: per-store price (USD+BRL), Código (store ref), external store URL, WhatsApp deep-link, variant URL, model URL, and follow-through validation against the source store for the cheapest 3-5 offers. Returns aggregated vs validated lowest prices, rejected offers with reasons, history series, and gaps.hybrid
54. 54search-listingscraigslist.orgSearch Craigslist in a given city and category for listings matching a query, returning each listing's title, price, location, posting date, and listing URL.api
55. 55extract-reviewscruisecritic.comGiven a Cruise Critic ship page (URL, or cruise line + ship name resolved via search), extract ship metadata plus a filtered slice of member reviews as structured JSON, leading with a Browserbase stealth session and using the per-review Next.js data JSON endpoint as a per-review enrichment shortcut.hybrid
56. 56search-listingsdepop.comSearch Depop's peer-to-peer fashion marketplace by keyword, category, brand, size, condition, color, price, sort, gender, on-sale, and shop scope, returning structured per-listing JSON (id, title, price, images, brand, size, condition, seller, shipping, status, canonical URL) plus the page-wide total and active filter chips. Read-only.hybrid
57. 57meet-derekderekmeegan.comReturn Derek Meegan's most recently published articles (titles, dates, tags, and canonical Medium URLs) from the /writing index on derekmeegan.com. Read-only; single HTTPS GET, no browser or anti-bot stealth required.url-param
58. 58get-marketplace-pricediscogs.comGiven a Discogs release/master URL, ID, or free-form release reference, return live Marketplace listings (per-listing price, media + sleeve condition, seller info, shipping, comments) plus full release-level metadata. Hybrid: public Database API for metadata + aggregate stats; stealth browser session for per-listing rows. Read-only.hybrid
59. 59check-if-a-vehicle-is-registereddmv.ca.govLook up the current California DMV registration status, expiration date, fees owed, and holds for a CA license plate plus one secondary identifier (last 5 of VIN, owner's last name, or company name). Read-only — never advances into renewal payment.browser
60. 60lookup-scout-docsdocs.scoutos.comGiven a free-text query about a Scout platform feature, concept, integration, or API/SDK reference, locate the relevant page on docs.scoutos.com and return structured JSON with title, breadcrumb, headings, prose, code blocks, tables, On-This-Page anchors, last-updated, canonical URL, and related pages.api
61. 61extract-menudoordash.comGiven a DoorDash restaurant URL or restaurant + city query, extract the full menu — every category, every item, with name, price, description, and popular/featured tags. Read-only — never adds to cart or checks out.hybrid
62. 62check-interactionsdrugs.comResolve a list of drugs (generic, brand, or partial) via Drugs.com autocomplete and return every flagged drug-drug, drug-food, and drug-condition interaction with severity, patient-facing summary, and clinical detail. Read-only and informational only — not medical advice.url-param
63. 63find-a-productebay.comSearch eBay by keyword and return the top listings with title, price, condition, shipping, seller, item URL, and thumbnail — read-only, never bids or buys. Distinguishes Buy-It-Now, auction, and variant-price-range outcomes.browser
64. 64search-productsebay.comSearch eBay's consumer site for listings matching a keyword query (with category, condition, price, location, format, and sort filters) and return them as structured JSON. Supports the Sold + Completed cross-section for comp pricing. Read-only.browser
65. 65book-electrician-serviceelektrik220.km.uaMatch a user's free-text electrical problem to one of 14 services at elektrik220.km.ua (Електрик 220В, Камʼянець-Подільський), and return the recommended service, price range in UAH, documents required to book (none) plus paperwork issued after work, and the earliest realistic booking window via phone, contact form, or email.api
66. 66search-productsetsy.comSearch Etsy for listings matching a query (free-form text, full search URL, listing-ID list, or shop URL) with the full filter surface — category, price range, item type, ship-to, color, sort, etc. — and return structured listing data (id, title, shop, price, original price, rating, badges, free-shipping, ad-flag, canonical URL) plus the fuzzy result count and active filter chips. Read-only.browser
67. 67fetch-homepage-contentexample.comFetch the example.com homepage and return its h1 heading, first paragraph text, and the trailing 'Learn more' link as structured JSON. Read-only, no auth, no anti-bot.api
68. 68pr-47-ai-gateway-smokeexample.comFetches https://example.com and verifies its main <h1> reads 'Example Domain'. Minimal end-to-end smoke test using the Browserbase Fetch API.api
69. 69search-marketplacefacebook.comSearch Facebook Marketplace for live listings by query, city slug, category, price range, condition, radius, delivery method, sort order, plus vehicle/apparel/rental sub-filters — and resolve single /marketplace/item/<id>/ URLs — returning normalized JSON. Read-only.browser
70. 70read-player-statsfangraphs.comLook up a baseball player on FanGraphs by name (or ID) and return per-season + career stats — standard counting plus sabermetric (wRC+, WAR, FIP, xFIP, K%, BB%, ISO, wOBA, xwOBA). Works for batters, pitchers, and two-way players. Read-only.api
71. 71track-packagefedex.comTrack a FedEx package by tracking number and return current status, last-known location, scheduled/estimated delivery window, service type, signed-by name, and the full chronological scan-event timeline. Read-only — never schedules, holds, or modifies a shipment.api
72. 72provider-searchfindadoc.healthplan.orgSearch The Health Plan's provider directory (findadoc.healthplan.org) for in-network doctors, hospitals, and facilities. Pick a member network (Commercial/MHT/Medicare/Self-Funded) via URL param, then filter by state-or-ZIP, network plan, and provider category (all/primary care/hospital/specialist). Read-only.browser
73. 73filter-clean-label-productsfinelysourced.comFilter FinelySourced.com's curated clean-label catalog (~140 products) across food, supplements, personal care, home, wellness, and apparel using lifestyle/ingredient tags (seed-oil free, organic, non-GMO, glyphosate-free, grass-fed, regenerative, etc.), categories, free-text search, and brand. Returns curated recommendations with title, brand, breadcrumb category, key features, certifications, tags, description, and outbound vendor link.hybrid
74. 74track-flightflightaware.comLook up live FlightAware status for any flight identifier (airline ICAO + number, IATA-style, or tail/registration). Returns origin and destination with terminal/gate, scheduled / estimated / actual gate-departure / takeoff / landing / gate-arrival times in local + UTC, aircraft type, route, current position (lat/lng, altitude, speed, heading), delay, and the permalink. Read-only.url-param
75. 75browse-campsitesfreecampsites.netGeocode a user's location query and return up to 40 nearby campsites from freecampsites.net (name, lat/lon, distance, fee tier, ratings, excerpt, detail-page URL, activity/amenity bitmasks) via the undocumented androidApp.php JSON endpoint, with suggest.php geocoding and an in-browser XHR fallback.api
76. 76find-listingfrench-property.comSearch french-property.com for-sale listings by region, price, bedrooms, property type, habitable / land size, and keywords; return matching listings with title, reference, price, location, room counts, sizes, image, and URL.url-param
77. 77extract-listingsfunda.nlSearch Funda for Dutch residential listings (koop/huur) by free-form location, structured filter URL, or single listing/broker URL. Returns normalised JSON per listing — price + history, address, neighbourhood, energy label, area, rooms, build year, agent, photos, VvE, and status. Distinguishes results, zero_results, location_unparseable, listing_not_found, bot_block, paywalled, and fundainbusiness out-of-scope outcomes.browser
78. 78find-cheapest-gasgasbuddy.comGiven a US ZIP code (or City, ST text), return the cheapest gas stations nearby on GasBuddy — with station name, brand, address, fuel grade, current price per gallon, reporter, how recently it was reported, and an optional ZIP-centroid distance. Read-only.browser
79. 79collect-share-event-mediagathershot.comSummarize how Gather Shot lets event hosts collect and share guest photos and videos via QR code (no app), and how to set up an event — including supported event types, pricing tiers, plan limits, and the host + guest workflow.browser
80. 80get-pr-reviewgithub.comExtract a normalized JSON snapshot of a GitHub pull request — metadata, ordered review timeline, per-file diff annotations with inline review comments (outdated + resolved flags), and check-run / status-context results — primarily via the GitHub REST API with a rendered-HTML fallback for UI-only signals. Read-only.api
81. 81get-repo-metadatagithub.comGiven a GitHub repo reference (URL, owner/repo slug, deep tree/blob URL, or owner URL), return the repository's core metadata, latest release, license, language breakdown, top contributors, README, and health signals as structured JSON. Read-only.api
82. 82get-company-reviewsglassdoor.comExtract a company's overall rating, sub-rating averages, recommend/outlook/CEO-approval percentages, and a filtered slice of employee reviews from Glassdoor — accepting a URL, EmployerId, or company name (+ optional location disambiguator) and supporting the full review-page filter rail (stars, job title, location, employment status, language, employment type, sort, keyword, limit). Read-only.browser
83. 83find-bookgoodreads.comResolve a Goodreads URL, book ID, work ID, ISBN, ASIN, title, or author into a structured record with core metadata, ratings, shelf signals, awards, and top reviews.hybrid
84. 84compare-drug-pricesgoodrx.comGiven a prescription drug (name, optional dosage/form/quantity) and a US ZIP, return GoodRx's per-pharmacy consumer price comparison as structured JSON — coupon price, list price, savings %, Gold-tier price, store name + address + distance, the printable coupon's Bin/PCN/Group/Member-ID, and drug monograph metadata. Honors the full filter surface (form, dosage, quantity, radius, pharmacy chain, sort, pickup vs. mail-order). Read-only.browser
85. 85search-flightsgoogle.comSearch Google Flights for one-way or round-trip itineraries between two airports on given dates and return the cheapest options with airline, flight numbers, total duration, stops, depart/arrive times, and a booking link. Read-only — never books.browser
86. 86search-csfagrants.illinois.govSearch the Illinois Catalog of State Financial Assistance (CSFA) for currently-posted funding opportunities by keyword, issuing agency, CSFA number, or award range — returns grant name, formal CSFA number, agency, posting period, award range, funding type, eligibility tags, unwrapped application-portal URL (AmpliFund / native CSFA NOFO), and attached NOFO PDF links. Read-only.api
87. 87search-auctionsha.comSearch Heritage Auctions (ha.com) for auction lots across all categories — past, current, and upcoming — with the full URL-param filter surface (category, auction status, auction type, price/estimate range, grading, date range, lot characteristics, consignor, sort, pagination). Returns structured JSON per lot. Read-only.browser
88. 88search-veganhappycow.netSearch HappyCow for vegan, vegetarian, and veg-friendly venues (restaurants, health/veg stores, juice bars, bakeries) in any location, honoring HappyCow's full filter surface (diet/venue type, cuisine, features, rating sort, distance, open-now time slider). Returns structured JSON with venue ID, name, slug, diet, coords, address, phone, rating, hours, photos, and region totals.url-param
89. 89compare-planshealthcare.govGiven a US ZIP, household composition, and income, return ACA marketplace plans from healthcare.gov with full premium and cost-sharing details. Handles the full filter surface (metal tier, CSR variant, plan type, issuer, HSA, premium/deductible/OOP ranges, drug + provider lookup) and short-circuits to a redirect_to_state_exchange status for the 20+ SBM states.api
90. 90find-specialisthealthgrades.comSearch Healthgrades for doctors, specialists, NPs/PAs, dentists, or hospitals matching a specialty (or condition/procedure) and location, honoring every /usearch filter (insurance, language, gender, distance, hospital affiliation, board-certification, rating, telehealth, accepts-new-patients, etc.) and returning structured JSON per provider including NPI, ratings, addresses, insurance, hospital affiliations, and Healthgrades awards. Read-only — never books or submits.browser
91. 91search-investment-projectshiveround.comDiscover live startup raises on Hiveround — filter by keyword, stage, and max raise via the site's MCP server (anonymous reads) or the ECP HTTP endpoints, returning slug, name, stage, sector, raise amount, founder handle, and listing URL. Read-only.mcp
92. 92find-a-product-on-home-depothomedepot.comSearch homedepot.com for products matching a free-text query, brand+model, or itemId; return canonical /p/{slug}/{itemId} URLs, titles, images, and (optionally, via a stealth browser session) price, availability, brand, rating, and key specs. Read-only.hybrid
93. 93find-a-hotelhotpads.comSearch HotPads for rental listings (apartments, houses, condos, townhomes, rooms, sublets) in a city, neighborhood, ZIP, or lat/lon bounding box. Returns address, rent range, beds, baths, sqft, photos, amenities, and detail-page URL per listing. Read-only.api
94. 94check-stockikea.comGiven an IKEA article number or product URL and a target market (US, GB, DE, …), return per-store stock state, units available, click-and-collect / home-delivery flags, last-checked timestamp, and discontinued / sold-out / online-only notices. Read-only.api
95. 95search-imageimages.nasa.govSearch NASA's Image and Video Library for images, videos, or audio by free-text query, filters (center, keywords, photographer, year range, location, album), or known NASA asset ID, returning each match's metadata and direct URLs to every file rendition. Read-only.api
96. 96get-ratingimdb.comResolve any IMDb title URL / tt-ID / free-form title reference (movie, TV series, episode, mini-series, short) to its current IMDb rating, total vote count, rating distribution per 1-10 bucket, Metascore, and core title metadata (cast, directors, writers, genres, runtime, certification, plot, languages, countries, poster, canonical URL). Read-only.browser
97. 97search-jobsindeed.comSearch Indeed for job postings across the full filter surface (keyword, location, radius, date posted, salary, job type, experience level, remote/hybrid, company, education, posted-by, encouraged-to-apply, sort, pagination) and return structured JSON. Supports SERP URLs, free-form keyword+location, single jk lookups, and the five outcome branches (results / zero_results / location_unparseable / bot_block / posting_not_found). Read-only.browser
98. 98browse-add-items-guestinstacart.comSearch Instacart for products and add them to the cart as a guest (no login). Routes around the un-closable email-capture modal that intercepts user-cursor clicks after the first add-to-cart action.browser
99. 99check-refund-statusirs.govLook up a federal tax-refund's current stage at IRS Where's My Refund, given SSN/ITIN, filing status, refund amount, and tax year. Returns the stage (Return Received / Refund Approved / Refund Sent), deposit/mail date when surfaced, Tax Topic codes (152/151/203), and the canonical status-page URL. Read-only and PII-sensitive — never logs or persists the TIN.browser
100. 100compare-flightskayak.comSearch Kayak.com for flights between two airports on given dates with the full left-rail filter surface (stops, airlines, alliance, time windows, duration, layover, booking sites, amenities, bags, quality filters, sort) and return matching itineraries as structured JSON with per-leg detail, Best score, deep-link URL, and CO2 emissions badge.browser
101. 101get-vehicle-valuekbb.comLook up a vehicle's Kelley Blue Book market values (Trade-In, Private Party, Typical Listing Price, Fair Purchase Price) plus original MSRP, 5-Year Cost to Own breakdown, and resolved trim specs, given year/make/model/trim or a full KBB URL plus mileage, ZIP, and condition. Read-only — never engages the Instant Cash Offer or dealer-lead funnels.hybrid
102. 102explore-pinball-contentkineticist.comSearch 1,700+ pinball machines, browse the daily Hype Index of upcoming-theme rumors, find venues to play, read news, build community lists, and create an account on Kineticist — using the site's first-party agent surfaces (OpenAPI, agent-card, llms.txt, per-route Markdown projections, CLI, MCP) before falling back to the browser.hybrid
103. 103kmartkmart.com.auFind a product on kmart.com.au by natural-language query, navigate to the product detail page, capture title/price/SKU/availability, and drive the read-only pre-checkout flow up to the bag (/checkout/bag). Never submits an order — stops at the bag review screen. Documents the Akamai bot wall that gates the actual addToCart GraphQL mutation for automated sessions.browser
104. 104scrape-exhibitor-directorylasvegas.jckonline.comExtract the full list of exhibitors from the JCK Las Vegas show directory (~1,700 companies) with name, contact information (phone, email, website, country), description, booth/stand reference, and product categories. Uses the public Algolia search API embedded in the directory page — two HTTPS POSTs cover the full roster.api
105. 105create-payment-credentiallink.comMint a one-time-use payment credential (virtual card PAN or Shared Payment Token) from a user's Link wallet so an agent can complete a purchase on their behalf. User approves each spend request from the Link mobile app; real card details never reach the agent.cli
106. 106search-linkedin-jobslinkedin.comReturn LinkedIn job postings matching profile-derived keywords + location, filtered to a configurable recency window (default last 24 hours). Leads with the public /jobs-guest seeMoreJobPostings HTML-fragment endpoint — no cookies, no auth, no Browserbase session required. Returns title, company, location, posted-when, jobId, and canonical job URL. Read-only.api
107. 107Partnercreate-projectlovable.devTurn a product or app idea into a Lovable project using Lovable Build with URL for shareable instant creation, or Lovable MCP for authenticated project creation, iteration, inspection, and deployment when available.mcp
108. 108order-for-pickupmcdonalds.order.onlineBuild a McDonald's pickup order on mcdonalds.order.online (DoorDash Storefront): switch to Pickup fulfillment, pick a store by address, add menu items, and stop at the checkout review page for user-authorized submission. Read-only by default — never clicks Place Order.browser
109. 109get-hospital-ratingmedicare.govLook up a hospital's CMS Care Compare star rating, HCAHPS patient-experience scores, condition mortality/readmission rates, hospital-acquired infections, ED timeliness, and full metadata by CCN, name+state, or Care Compare URL. Supports compare_to for side-by-side hospitals with national + state benchmarks. Read-only.api
110. 110search-eventsmeetup.comSearch Meetup for upcoming events by topic, location, group slug, or topic category. Returns structured JSON per event — id, title, group, venue + lat/lon (or online platform), start/end time, going/waitlist counts, capacity, price, photo, organizer/hosts, topic tags, canonical URL. Honors keywords/location/eventType/distance/dateRange/categoryId/sortField URL filters. Read-only.url-param
111. 111search-listingsmercari.comSearch Mercari (US peer-to-peer marketplace) for listings matching a query, item-ID list, or seller URL — across the full filter surface (category, brand, condition, price, color, size, shipping, Mercari Authenticate, Smart Pricing, offerable, seller) — and return matching items as structured JSON with per-listing seller, shipping, photo, and status fields.browser
112. 112copenhagen-monocle-searchmonocle.comSearch monocle.com's editorial archive by free-text query (e.g. a city name like Copenhagen), with optional topic and format filters. Returns title, canonical URL, author, publication date, topic + tags, excerpt, and featured-image URL for each matching article. Read-only.api
113. 113search-routesmountainproject.comSearch mountainproject.com for climbing routes with the full route-finder filter surface (area, grade range across YDS/V/WI/AI/M/Aid, route type, pitches, stars, sort, pagination), returning structured per-route data including id, grade, type, pitches, length, star rating, vote count, area breadcrumb, lat/lng, and first ascent.url-param
114. 114get-smb-fundingnav.comEnumerate the small-business funding options on Nav's public marketplace — business loans, business credit cards, and trade-credit vendors — returning each offer's lender, dollar range, cost/APR, repayment, and funding speed. Read-only.hybrid
115. 115compare-credit-cardsnerdwallet.comSearch and compare credit cards on NerdWallet (category, card name, full URL, or free-form criteria) and return structured per-card data — rating, fees, intro APR, welcome bonus, rewards, pros/cons, key benefits, and the affiliate Apply Now URL (captured, never followed). Read-only.browser
116. 116get-storiesnews.ycombinator.comFetch Hacker News stories from any list view (front, newest, ask, show, jobs, best, active, classic, by-domain, by-user, historical day) and optionally full comment trees, returning a unified JSON shape.api
117. 117find-craft-beer-restaurantsnonny.beerFind bars and restaurants serving Nonny craft non-alcoholic beer near a given latitude/longitude, returning name, address, distance, phone, and website per result. Sorted by distance, category-filtered to Bars/Restaurants only.api
118. 118search-casesnycourts.govSearch New York State Unified Court System dockets across WebCivil Supreme, WebCivil Local, WebCriminal, WebFamily, NYSCEF, and WebSurrogate. Returns matched cases as structured JSON: index/docket number, court (type + county + part), caption, parties, attorneys, nature of action, filing & disposition dates, assigned judge, appearance/motion history, NYSCEF link, and canonical case-detail URL.browser
119. 119electronic-product-detailsoctopart.comSearch Octopart's electronic-component catalog by keyword, MPN, or tech spec and return clean JSON: part identity, specs, distributor stock, and per-quantity pricing across DigiKey/Mouser/Arrow/Avnet/Farnell and 30+ other distributors. Recommended path is the Nexar GraphQL API (free with OAuth2 registration) — Octopart's public web UI is universally PerimeterX-walled on Browserbase.api
120. 120find-company-filingsopencorporates.comSearch OpenCorporates for legal-entity records across jurisdictions and return matching companies plus their statutory-filings history (officers, addresses, previous names, branch flags, document URLs) as structured JSON. Read-only.api
121. 121search-codex-petsopenpets.shSearch the OpenPets community registry for Codex / Claude Code / OpenCode / Pi Code pets matching user criteria, returning ranked pet metadata and universal one-click install links for the OpenPets macOS app.api
122. 122compare-and-build-llm-modelopenrouter.aiSearch and compare OpenRouter's 350+ LLMs by cost, speed (throughput/latency/uptime), context length, modalities, and use-case category; pick the best fit; then build with it via OpenAI-compatible chat completions. API-first — no scraping, no auth for reads.api
123. 123check-availabilityopentable.comLook up OpenTable restaurant availability for a party size + date + time, returning slots when present and distinguishing sold-out, restaurant-not-bookable, restaurant-not-found, ambiguous-name, metro-override, and slot-extraction-blocked outcomes. Read-only — never books.browser
124. 124get-business-brainoperator.fyiResolve any business name, URL, city, or trade into Operator's full public Brain profile: 0-100 brain score with component breakdown, market rank, review sentiment from Google/Yelp/Meta, services + privacy-protected contact, top 3 competitors with scores, AI narrative, USD valuation range (vertical-multiple comparables), per-business MCP endpoint, and canonical /biz/{slug}/ URL. Read-only.api
125. 125search-products-by-filtersoutmoreliving.comSearch Outmore Living's catalog by product type (chaise, sofa, lounge chair, ottoman, side table), Solerno collection, and price range. Returns name, SKU, price, materials (teak, Sunbrella, HeatTech, ComfortCore), availability, and product URL via the public Shopify storefront JSON endpoints.api
126. 126exact-spec-packaging-procurementpackrift.comResolve an exact Packrift packaging SKU for a buyer requirement, confirm live price and inventory through the Packrift MCP server, and return a measured cart handoff URL or a bulk-quote URL when no exact match exists. Treats dimensions, material, color, adhesive, printer compatibility, case count, and SKU as strict exact-match constraints — never substitutes nearby SKUs.mcp
127. 127peptide-researchpeptideportal.orgSearch peptideportal.org for a peptide by name, alias, CAS number, or mechanism keyword and return a structured profile aggregating vendor pricing range and COA-verified status, the canonical research brief with use-case evidence tables, related dosing-guide blog posts, and the curated bibliography of clinical papers with PubMed outbound links.browser
128. 128search-petspetfinder.comSearch Petfinder for adoptable pets near a location (or by pet ID / organization ID) and return matching listings as structured JSON, including breeds, age, behavior tags, photos, organization contact, and posted date. Read-only — never starts an adoption.browser
129. 129write-prompt-guideplatform.claude.comAuthor production-grade prompts for Claude by applying Anthropic's canonical prompt-engineering best practices in impact order: clarity, examples, chain-of-thought, XML tags, system roles, prefilling, prompt chaining, and long-context tips.cli
130. 130find-chargerplugshare.comSearch PlugShare for EV charging stations near a location, route, or coordinate and return matching chargers as structured JSON — including per-plug connector/kW/status, network, PlugScore, recent check-ins, photos, and pricing. Read-only.hybrid
131. 131Partnersend-messagepoke.comSend structured context to Poke through the official inbound API so the user's Poke assistant can process it like an incoming message. Includes API-key handling, safe external-action gating, smoke-test verification, and Poke recipe packaging notes.api
132. 132compare-insurancepolicygenius.comCompare insurance carriers on Policygenius (life, auto, home, renters, disability) and return Policygenius rating, AM Best, J.D. Power, NAIC complaint index, pros/cons, Best-for tag, and last-reviewed date per carrier. Editorial-only; never enters the PII-gated quote funnel.hybrid
133. 133search-listingsposhmark.comSearch Poshmark for fashion / lifestyle listings via the public /vm-rest/posts JSON endpoint (free-text + sort + pagination) with a browser fallback on /search?... for strict facet filters. Returns each match with listing id, title, price (raw + formatted), brand, size, color, department/category, inventory status (available/sold), seller, images, and engagement counts. Read-only.api
134. 134get-player-statspro-football-reference.comGiven an NFL player reference (URL, PFR ID, or free-form name), return bio + the requested career, season, splits, or game-log stat tables from Pro-Football-Reference as structured JSON. Preserves verbatim PFR column headers and table ids. Read-only.browser
135. 135Partnersubmit-reimbursementramp.comSubmit an employee reimbursement through Ramp MCP or Ramp CLI with receipt extraction, policy/category validation, draft review, and explicit confirmation before submission.cli
136. 136list-propertiesrealtor.caList MLS-listed properties on REALTOR.ca within a bounding box or named Canadian city, filtered by sale/rental, price range, beds, and baths. Returns price, address, lat/lon, beds, baths, size, photo, agent, and canonical listing URL. Read-only.hybrid
137. 137extract-listingsrealtor.comSearch Realtor.com (for-sale, for-rent, sold, new-construction, foreclosure, pending) from a free-form location or pre-filtered URL and return structured listing JSON. Honors the full filter surface (price, beds/baths, sqft, lot size, year built, days-on-market, HOA, features, school rating, pets/furnished, sort, pagination). Read-only.browser
138. 138get-school-ratingrealtor.comGiven a school name + city/state, a Realtor.com school detail URL, or a property address, return the school's GreatSchools rating, parent-reviews summary, grades served, enrollment, student-teacher ratio, district, address, NCES code, and canonical URL. For property addresses, returns the list of assigned elementary / middle / high schools with each school's rating.api
139. 139recipe-discovery-generatorrecipebee.appDiscover and extract structured recipes from recipebee.app — by direct URL, natural-language query mapped to tag/category enums, or bulk sitemap mirror. Returns full schema.org/Recipe JSON-LD: ingredients, numbered steps, prep/cook times, yield, cuisine, keywords, nutrition. Read-only; AI meal-plan and shopping-list features require login and are out of scope.hybrid
140. 140check-availabilityrecreation.govCheck live availability for any Recreation.gov bookable resource — campground, backcountry permit, lottery, timed-entry tour, day-use site — over a date range and return the per-site/per-division, per-day availability matrix with equipment, accessibility, pet policy, fees, and canonical URLs. Read-only.api
141. 141recruiting-jobs-searchrecruiterroles.comSearch recruiter and talent-acquisition jobs on recruiterroles.com with filters for location (city, state, country, remote), salary floor, employment type (full-time, contract, freelance, part-time), work arrangement, and sector. Prefers the free public REST API; falls back to slug-based browser navigation when no API key is available.api
142. 142get-comparable-salesredfin.comReturn recent comparable sales (sold comps) on Redfin for a subject property, with every filter dimension the Recently Sold UI exposes (recency, distance, price, beds, baths, sqft, lot, year built, property type, days-on-market, sort). Read-only.api
143. 143Partnerextract-document-datareducto.aiUse Reducto's hosted MCP server to parse documents, extract schema-backed fields with citations, split packets, classify document types, and fetch job results from public URLs or Reducto-hosted files.mcp
144. 144search-cottagesresortcottagesontario.caSearch resortcottagesontario.ca for resort-cottage rentals: returns Mildred's Lakefront Resort Cottage (the site's single Kawarthas / Rice Lake / Bellmere Winds property) with date-specific availability via the on-site MotoPress booking form for 2027+ dates, or a Great Blue Cottage Rentals deeplink for 2026 dates. Read-only — never clicks Confirm Reservation.hybrid
145. 145check-availabilityresy.comCheck Resy for bookable reservation slots at a given restaurant for a party size and date or date window. Returns slot times with seating type, config_id token (load-bearing for downstream booking), price, and policy. Distinguishes available, sold-out, outside-publish-window, ambiguous-name, venue-not-found, party-size-exceeds-max, and Resy-Premier-wall outcomes. Read-only — never books.api
146. 146is-mount-tam-cloudyrntl.netDecide whether Mount Tamalpais is currently overcast by pulling the live snapshot JPEG from the rntl.net Mt. Tam Cam (Sigward / Muir Beach ipcamlive feed) and visually classifying the sky. Returns a sky-condition category, ridgeline-visibility flag, and a go/don't-go recommendation. Read-only.api
147. 147get-ratingrottentomatoes.comGiven a Rotten Tomatoes title URL, RT slug, or free-form title reference, return the current Tomatometer (critic) and Popcornmeter (audience) scores, certified flags, vote counts, sample critic reviews, full cast & crew with role names, synopsis, where-to-watch affiliates, and core title metadata as one JSON object. Handles movies, TV series (with series-wide averages and per-season URLs), TV seasons, pre-release no-score-yet titles, and ambiguous free-form queries.api
148. 148ruwangi-parfum-laki-lakiruwangi.comReturn a curated, ranked list of best local Indonesian women's perfumes from Ruwangi.com — name, brand, IDR price, rating, notes, and time-of-day suitability. Read-only directory lookup using the pre-curated /katalog/parfum-lokal-wanita-terbaik deep-link.browser
149. 149query-menu-datasaizeriya.com.sgPull Saizeriya Singapore's current menu (Grand, Lunch, Kids) and 44-outlet directory as structured data via deterministic static-URL GETs — the site exposes no JSON API, but its three versioned PDF endpoints plus /menu/ HTML index function as one.api
150. 150contract-opportunity-searchsam.govSearch active federal contract opportunities on SAM.gov by status, notice type, place of performance (state/ZIP/country), date range, NAICS, and set-aside. Returns title, notice ID, agency hierarchy, place of performance, response deadline (with time zone), notice type, and the canonical /opp/{id}/view URL.api
151. 151browse-membershipssamsclub.comReturn Sam's Club's consumer membership tiers (Club, Plus) with standard annual prices, current promo first-year prices, promo window dates, and the full per-tier benefits list. Read-only; never joins or enters payment info.hybrid
152. 152view-rates-apply-mortgagesbab.seRead SBAB's live mortgage list rates, effective rates, handpenningslån/överbryggningslån, Sparkonto and Fasträntekonto rates via six public JSON APIs (no auth), and walk a user up to the BankID gate for the lånelöfte (mortgage pre-approval) application or savings-account opening flow.api
153. 153create-a-skill-for-finding-verifiying-lisearch.dca.ca.govVerify a California-licensed accountant (CPA, Public Accountant, or accounting firm) on the DCA license search at search.dca.ca.gov — boardCode=19 (California Board of Accountancy). Returns full license record with status, dates, city, and any disciplinary actions.browser
154. 154get-seat-mapseatguru.comSeatGuru.com was shut down by TripAdvisor on/around 2025-11-04. The homepage serves a static migration notice and every deep URL returns HTTP 301 to tripadvisor.com from a CloudFront edge function. This skill documents the wall and routes callers to the working alternatives (aerolopa.com, seatlink.com, flightseatmap.com, seatmaps.com).browser
155. 155search-edgar-fulltextsec.govSearch the full body text of SEC EDGAR filings (10-K, 10-Q, 8-K, S-1, DEF 14A, 13F, 13D/G, Form 4, etc., 2001-present) via the public efts.sec.gov JSON API, with filters for form type, filer (CIK or name), filer location, SIC code, and date range. Returns structured filing metadata plus canonical filing-index and document URLs.api
156. 156get-fighter-recordsherdog.comGiven a fighter reference (canonical Sherdog URL, name, or name + disambiguator), return profile metadata and full professional bout record as structured JSON. Optional amateur and per-bout-location flags. Read-only.hybrid
157. 157search-car-rentalsixt.comSearch the Sixt car-rental site for available vehicles at a given branch on given dates and return offer details (class, sample model, seats/doors/transmission, mileage policy, per-day and total price). Read-only — never books.browser
158. 158search-cheapest-flightskyscanner.netSearch Skyscanner for the cheapest one-way flight between two cities on a given date, returning price, airlines, depart/arrive times + airports, duration, stops, layovers, self-transfer flag, the 7-day nearby-date price strip, and the canonical Skyscanner config-URL deeplink that surfaces OTA/airline provider booking options. Read-only — never books.browser
159. 159lookup-software-contractsoftware.nasa.govLook up software in NASA's public Software Catalog by free-text keyword or by canonical case number, returning structured records with title, description, NASA field center, category, release type, version, dates, and download URL.api
160. 160search-lotssothebys.comSearch Sotheby's auction catalog (upcoming, live, and past) across the full filter surface — department, sale type, sale status, estimate range, artist, year, medium, location, lot characteristics — and return structured lot + sale JSON. Handles direct sale URLs and direct lot URLs. Read-only.api
161. 161search-flightssouthwest.comSearch southwest.com for available flights between two airports on given dates and return matching itineraries with four-bucket fares (Wanna Get Away / Plus / Anytime / Business Select) in dollars or Rapid Rewards points. Read-only — never books. Southwest refuses syndication to OTAs, so southwest.com is the only source of truth for these fares.browser
162. 162get-resale-pricestockx.comGiven a sneaker or streetwear product (name + optional size), return the StockX market snapshot: lowest ask, highest bid, last sale + date, recent sales volume, and a 30-day price-trend payload. Read-only — never bids or buys.hybrid
163. 163search-newsletterssubstack.comSearch Substack for newsletters / publications matching a topic, keyword, category, language, or author and return matching publications with subscriber-tier signals, multi-currency pricing, recent post samples, and canonical URLs as structured JSON. Read-only.api
164. 164calcular-sueldo-netosueldojusto.peCalcula el sueldo neto mensual peruano a partir del bruto usando el calculador de sueldojusto.pe, con desglose de AFP/ONP, comisión, seguro de invalidez, asignación familiar e impuesto a la renta de 5ta categoría según los valores oficiales 2026 (UIT S/5,500, RMV S/1,130).browser
165. 165get-forecastsurfline.comReturn Surfline's free-tier surf forecast for a single spot — given a spot URL, 24-char spot ID, or name (with optional region qualifier). Current conditions, multi-day surf height + swell + wind, tide table, sunrise/sunset, live-cam URL, and canonical URL. Read-only; Premium features (16-day, observed wind, HD rewind) are surfaced as omitted.api
166. 166jp-restaurant-searchtabelog.comEnumerate Tabelog Award Silver winners (curated top-100), filter by prefecture/city + cuisine + lunch availability + lunch price ceiling + rating threshold, and report whether each survivor accepts online reservations directly on tabelog.com (vs. phone/email only). Read-only.browser
167. 167find-a-producttarget.comSearch Target.com for a product query and return the top organic match's title, brand, price, original price, rating, TCIN, canonical product URL, and image — via the public redsky JSON aggregation API. Distinguishes real matches, spell-corrected matches, and zero-results-with-recommendation-padding outcomes. Read-only.api
168. 168lookup-patenttechnology.nasa.govSearch and retrieve patents from NASA's Technology Transfer (T2) catalog by free-text query, category, NASA center, or reference ID — returning structured records with title, abstract, technology description, USPTO patent numbers, NASA case numbers, TRL, figures, and licensing-contact data.api
169. 169tecbrowsershthewindowsclub.comSearch TheWindowsClub for articles by keyword (with optional category/tag scoping and date/relevance sort), returning each article's title, URL, publish date, excerpt, category and tag IDs.api
170. 170find-ticketticketmaster.comFind upcoming Ticketmaster events for an artist, team, or show — returns venue, date, on-sale window, presale times, sold-out/cancelled/postponed flags, and the canonical event URL. Read-only, uses Ticketmaster's unauthenticated internal artist-events API behind a residential proxy.api
171. 171track-a-package-use-this-number-for-testtools.usps.comTrack a USPS package by tracking number and return current status, current location (city/state), expected delivery date, and the full chronological event timeline. Read-only.browser
172. 172extract-reviewstripadvisor.comExtract a Tripadvisor entity's overall rating, review count, rating distribution, ranking, and a filterable slice of structured reviews (rating bubble, sort, traveler type, language, season, search-within, hotel subratings, restaurant meal type). Read-only.browser
173. 173lookup-scout-trusttrust.scoutos.comLook up Scout's security, compliance, and privacy posture from trust.scoutos.com (Vanta-hosted Trust Center) for a given topic. Returns structured JSON with compliance badges, audit reports, policy documents, controls by category, subprocessors with regions, gated-access flags, and the canonical access-request workflow URL. Read-only — never submits access or NDA forms.browser
174. 174check-wait-timetsa.govReturn current and historical TSA security-line wait times for a US airport. TSA's public web wait-time tool has been deprecated since 2023; this skill documents the dead-end and routes callers to the MyTSA mobile app or third-party trackers.browser
175. 175search-flightsunited.comSearch United Airlines flights between two airports for given dates and a trip type (one-way or round-trip), returning each result's times, duration, stops, flight numbers, cabin, fare brand, and price. Read-only — never books.browser
176. 176track-packageups.comGiven a UPS tracking number, return the package's current status, last-known scan location, scheduled or estimated delivery date, signed-by name when delivered, and the full chronological event timeline (timestamp, location, status description). Read-only — drives www.ups.com/track behind Akamai Bot Manager.browser
177. 177check-case-statususcis.govLook up a USCIS case by 13-character receipt number (e.g. MSC2190012345, EAC2290098765, IOE0123456789) on the modern egov.uscis.gov Next.js portal and return status heading, next-step paragraph, form type (I-130/I-485/N-400/I-765/...), service-center code, last-updated date, and the canonical caseId URL. Read-only.browser
178. 178find-marketusdalocalfoodportal.comSearch the USDA Local Food Portal directories (Farmers Markets, CSAs, On-Farm Markets, Food Hubs, Agritourism) near a US location and return matching listings with full address, lat/lon, distance, plaintext contact, social-media URLs, and the canonical detail URL.api
179. 179get-earthquake-feedusgs.govFetch recent earthquakes from the USGS Earthquake Hazards Program (summary feed, FDSN query, or single event ID) and return them as normalized structured JSON with magnitude, location, depth, intensity, alert level, tsunami flag, significance, status, and canonical event URL.api
180. 180track-packageusps.comGiven a USPS tracking number, return the current status, expected delivery date, last-known location, and full chronological event timeline via the USPS REST API v3 (recommended) or the public tracking page behind Akamai (fallback).api
181. 181search-patentsuspto.govSearch USPTO Patent Public Search (PPS) for granted patents and pre-grant publications by title, abstract, inventor, assignee, full spec, or claim text — returning patent number, title, abstract excerpt, assignee, inventor list, filing/grant dates, and document URL.browser
182. 182find-appointmentvaccines.govGiven a ZIP code, return nearby CVS / Walgreens / Costco pharmacies that administer vaccines, with each chain's scheduler deep-link. Vaccines.gov no longer surfaces slot times — this skill handles the directory portion and hands off booking to per-chain scheduler skills. Read-only.hybrid
183. 183create-slack-agentsvalet.devUse the Valet CLI (or 1-click Deploy URL fallback) to create, deploy, and manage AI agents that live inside Slack and handle research, follow-up, sync, and reporting for Sales, Venture, Finance, Product, Compliance, Procurement, Engineering, and Nonprofit teams.cli
184. 184find-music-tourvipnation.comList currently-promoted artist tours on vipnation.com — tour title, slug, canonical URL, and (when reachable) full stop list with date, venue, city, and ticket-package availability. Read-only; never follows purchase CTAs.hybrid
185. 185find-opportunitiesvolunteermatch.orgSearch for volunteer opportunities by location, cause/interest, skills, format, schedule, time commitment, and audience, and return each match as structured JSON. VolunteerMatch.org has sunset and 301-redirects to Idealist.org; this skill queries Idealist's public Algolia search index directly (the catalog VolunteerMatch postings were migrated into, with a `vmLegacyId` field preserving the old IDs).api
186. 186find-polling-placevote.orgGiven a US street address, route to the assigned polling place + drop-box / early-voting alternatives via Vote.org's state-directory page-data.json (recommended) or the polling-place-locator HTML directory (fallback). Read-only; never registers or starts a check-in flow.api
187. 187get-scorewalkscore.comGiven a US or Canadian street address (or a walkscore.com /score URL), return the Walk Score, Transit Score, Bike Score, qualitative tier labels, neighborhood/city area label, lat/lon, and canonical URL. Per-category amenity counts available via the browser fallback path.api
188. 188get-forecastweather.govGiven a US location (lat/lon, ZIP, or city+state), return the National Weather Service forecast: current observation, hourly forecast, 7-day multi-day periods, active alerts/watches/warnings, the forecast office, and the underlying grid cell. Read-only via the public api.weather.gov JSON surface (no auth).api
189. 189is-it-cloudyweather.govReturn current sky conditions for a US location: cloud-cover layers (METAR CLR/FEW/SCT/BKN/OVC/VV with base heights), surface visibility in meters and miles, and a derived 'can you see blue sky?' boolean — pulled from the free NWS api.weather.gov JSON API.api
190. 190get-top-market-beatersweb.dubapp.comReturn Dub's Top Market Beaters leaderboard — the 20 Core-creator portfolios currently outperforming the market — with rank, name, ticker, creator, today and all-time % returns, description, and profile URL. Single anonymous HTTP GET to /explore/market-beaters returns the fully SSR'd grid; no auth, no proxy, no JS execution required.api
191. 191search-startup-jobswellfound.comSearch Wellfound (formerly AngelList Talent) for startup job postings — supporting the full filter surface (role, location, remote policy, experience level, job type, salary + equity ranges with currency, company size + stage, markets, skills, visa sponsorship, recency, sort, pagination) — and return structured JSON jobs with full company, recruiter, salary/equity, and description data. Read-only.browser
192. 192sparql-querywikidata.orgExecute SPARQL against Wikidata's public Query Service and return structured JSON. Accepts raw SPARQL, a Wikidata entity QID (with optional property-PID filter), or a natural-language relational question that the agent translates into SPARQL. Honors output format (JSON/XML/CSV/TSV), label language, LIMIT, and the 60s endpoint timeout. Read-only — mutation queries rejected client-side.api
193. 193find-the-trending-world-news-for-todaywikipedia.orgReturn today's trending world news from Wikipedia — curated ITN headlines from the Main Page plus today's Current Events portal subpage bucketed by category (Business, Disasters, Politics, etc.). Read-only; uses the public MediaWiki API with no auth or anti-bot stealth.api
194. 194get-articlewikipedia.orgGiven a Wikipedia article reference (URL, lang+title, or free-form name), return structured content: canonical URL, title, language, lead summary, full section tree, infobox key/value pairs, thumbnail, image list, outbound article links, external links with section attribution, categories, last-revised timestamp, pageid, and revid. Handles redirects, disambiguation pages, and non-English editions.api
195. 195wolt-searchwolt.comSearch Wolt for restaurants in a given city by cuisine, dish, or restaurant name and return a ranked list with name, slug, URL, cuisine tagline, delivery fee, delivery time, price tier, and customer rating. Read-only.browser
196. 196loginxero.comAuthenticate a user session against Xero — either via OAuth 2.0 / OIDC (recommended, supported) or as a fallback by scripting the password form at login.xero.com/identity/user/login. Documents the canonical URL, form schema, anti-bot stack (Akamai + browsercheck + AspNetCore antiforgery), and all five branch outcomes (MFA, SSO, passkey, lockout, invalid credentials).api
197. 197get-trending-contentxiaohongshu.comReturn the current batch of trending Xiaohongshu (RedNote) feed cards — each card's 1-line displayTitle, type, video duration, like count, author, and canonical note URL. Filter to short videos for the short-video use case.url-param
198. 198search-metrics-tokens-nftsxrpl.toSearch XRPL.to's universe of fungible tokens, NFT collections, individual NFTs, and accounts in one call, and pull live market metrics, OHLC chart data, news with AI sentiment, and platform-wide stats — all via the official public REST + WebSocket API.api
199. 199extract-reviewsyelp.comExtract a Yelp business's overall rating, review count, business metadata, and top reviews as structured JSON — honoring every read-side filter Yelp's review widget exposes (rating buckets, sort, language, search-within, review type, pagination). Read-only.browser
200. 200get-business-hoursyelp.comGiven a Yelp business URL, alias slug, or natural-language reference, return structured hours of operation — per-day open/close ranges, special-hours overrides, IANA timezone, current open/closed state, freshness signal, canonical URL, and a top-level status (open / temporarily_closed / permanently_closed / unknown). Read-only.hybrid
201. 201extract-transcriptyoutube.comGiven a YouTube video URL or ID, return title, channel, duration, full timestamped transcript segments, and whether captions are auto-generated or human-authored. Read-only.api
202. 202search-shoeszappos.comSearch Zappos for shoes (and apparel, bags, accessories) matching a query plus filter set (size, width, brand, color, price, sort, etc.) and return structured per-product JSON — price, brand, ratings, colorways, image URLs, badges, canonical URL, plus the page total and active filter chips. Read-only.browser
203. 203extract-listingszillow.comExtract Zillow for-sale listings matching a complex multi-dimensional filter (price, beds/baths, sqft, lot, year built, property type, listing status, days-on-market, HOA, monthly payment, home features). Constructs the filtered SRP URL via Zillow's searchQueryState parameter, fetches via Browserbase Fetch API (bypasses PerimeterX), and parses __NEXT_DATA__ for structured listings + region totals + pagination. Read-only.api
204. 204find-appointmentzocdoc.comSearch Zocdoc for available appointment slots by specialty + location (+ optional insurance), returning provider name, specialty, distance, next-available date/time, and accepted insurance. Read-only — never books.browser