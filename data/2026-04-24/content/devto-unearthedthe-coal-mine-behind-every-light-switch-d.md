---
title: Unearthed—The Coal Mine Behind Every Light Switch - DEV Community
url: https://dev.to/anchildress1/unearthed-the-coal-mine-behind-every-light-switch-234m
site_name: devto
content_file: devto-unearthedthe-coal-mine-behind-every-light-switch-d
fetched_at: '2026-04-24T11:56:30.663198'
original_url: https://dev.to/anchildress1/unearthed-the-coal-mine-behind-every-light-switch-234m
author: Ashley Childress
date: '2026-04-20'
description: Your electricity traces back to a specific mine, a specific operator, a specific county. Unearthed names all three—and what it cost the mountain. Tagged with devchallenge, weekendchallenge.
tags: '#devchallenge, #weekendchallenge'
---

DEV Weekend Challenge: Earth Day

This is a submission forWeekend Challenge: Earth Day Edition

## What I Built

EPA's Power Profilertells you your grid is 32% coal.iLoveMountainstells you mountaintop removal is destroying Appalachia. Neither one names the specific hole in the ground feeding your house, neither tells you which workers got hurt pulling the coal out of it, and neither puts that cost back on the consumer flipping the switch.

Uneartheddoes all three. It names the coal mine feeding your electric grid—the accident record, the operator, the county, the tons—and hands you a natural-language interface to the data behind it.

### Why This 🪨

I miss being in the mountains, but the economy in that area is mostly nonexistent and work there is hard to come by. Mostly because companies come into the area, mine everything they can, and then leave when the coal is gone. This leaves behind strip jobs—where the land will quite literally never recover—black lung in the men and women who worked the mines for decades, and abandoned shafts that aren't exactly known for their structural integrity over time.

Virginia produced 8.6 million short tons of coal in 2024. Southwest Virginia carries most of that history—roughly 100,000 acres of abandoned mine land, plus 245 legacy "GOB piles" (mining waste) leaching acid mine drainage into the creeks. Those same mines have public accident records going back to the 1980s—the Mine Safety and Health Administration (MSHA) documents the injuries, fatalities, and the narratives that go with them. Virginia Energy's hazard list for those old sites reads like a ghost tour: landslides, stream sedimentation, dangerous highwalls, subsidence, loss of water supply, open mine shafts, underground explosions, and underground fires.

The men and women who work underground often work decades or until they can't anymore. They rarely recover from the harsh conditions. Anyone who has spent any significant time in that area will share my fatalist outlook. When work is a mile or more underground and you never really know if you are going to come back up again, then you just learned it's a normal part of life.

So, when you ask me to think about the planet, what I picture is the mostly empty coalfields where I grew up. Which got me to thinking, what are we really doing with all of that coal that tookover 300 million yearsto form from nothing but pressure buried under the mountains of Appalachia. This is a follow-up toCarbon Trace—first you got the story, now you have the data to back it up.

Unearthedtranslates your specific energy grid anywhere in the US into the coal tons it takes to power it. The map will show you the closest mining facility responsible for powering your home—from small appliances to keeping the lights on. It is my hope that every person really takes the time to understand the depth of love and family that went into keeping the lights on all over the country from the men and women who are still living underground to make it happen.

### The Product 🔧

Unearthedis an emotional product first and a data product second. The data, managed by Snowflake, makes the emotions real, and a public-domain photograph—one of the many stripped mountaintops like the ones I grew up surrounded by—shows you the actual cost we pay to keep the lights on in our homes.

You can use your current location or search by address.Unearthedfinds the power plant feeding your electricity and the coal mine feeding resources into that plant.

Snowflake Cortex does the work. Cortex COMPLETE describes the mine in prose; the goal is to convey what this mine is actually doing to the mountain it's in, honestly—doom included. Then you can ask it the follow-up questions—is this mine still active, who else buys from this operator, how much did it produce last year. Cortex Analyst routes those through a hand-written semantic model and returns the answer (and the SQL, if you want to see it).

Feel it first, then prove it with Snowflake.

## Demo

Enter your address. In under a minute you'll know which mine powers your lights, who runs it, what county it's in, how many tons it shipped to your plant last year, and who got hurt pulling that coal out of the ground.

What that looks like for one real address—Carrollton, GA:

James H Miller Jr power plant (AL) ← 5,064,233 tons ← Black Thunder mine (WY)Operator: Thunder Basin Coal Company LLC · Type: SurfaceMSHA accident record: 4 fatalities · 188 lost-time injuries · 8,763 days lostEPA emissions (since 2020, via Snowflake Marketplace): 125.9M tons CO₂ · 6K tons SO₂ · 39K tons NOₓ

### Live 🗺️

* Deployed:https://unearthed.anchildress1.dev—use this site to search by your current location

Try it in about a minute:

1. Land on the Hero. Enter your address, or allow location.
2. The page scrolls you into the results.
3. PlantReveal—the power plant actually feeding your grid.
4. MapSection—animated SVG path traces mine → plant → your meter, with a pulse bead along the route and an EPA subregion label on your pin.
5. H3Density—hex grid of active vs abandoned mines feeding your plant, with a Cortex-written summary.
6. CortexChat—ask the grid your own question. Chip or free-form.
7. Ticker—tons of coal pulled out of that mine since you started reading this page. Paced off the mine's own annual tonnage.

💡The Ticker is why this app exists instead of being a spreadsheet.It paces off the mine's 2024 tonnage from MSHA and counts up in real time. While you've been reading the post, the mine feeding your grid has pulled several more tons out of the ground.

## Code

### Repo ⚙️

## anchildress1/unearthed

### Show any US resident which coal mine supplies their local power plant. Federal data (MSHA + EIA) in Snowflake Cortex + Gemini. DEV Weekend Challenge 2026.

# Unearthed

Tagline:Find the coal mine under contract to your local power plant. Watch it die in real time. Ask it questions.

Unearthed turns public federal data (MSHA + EIA + EPA) into a consumer-scale reveal: enter an address, see the specific coal mine feeding your grid, read memorial prose written from that mine's safety record, then ask natural-language questions about the contract. Built for theDEV Weekend Challenge 2026 — Earth Day Edition, targeting theSnowflake Cortexsponsor category.

* Cortex Analystdrives natural-language Q&A (semantic model → SQL → real rows).
* Cortex Complete(llama3.3-70b) writes the mine-memorial prose and the 2–3 sentence summary under the national density map — both carry a degraded flag so template fallbacks never sit under a Cortex byline.
* H3 hexbin geospatial+Marketplace(EPA Clean Air Markets) are used natively inside Snowflake — no extraction, no ETL away.

For challenge judges:…

View on GitHub

Worth checking out:

* assets/semantic_model.yaml—hand-written Analyst training with 6 tables, 5 relationships, and 8 verified natural-language→SQL queries
* app/prose_client.py—the CortexCOMPLETEprompt plus per-subregion caching so repeat views don't pay the LLM tax
* assets/fallback/—19 pre-generated subregion fallbacks (one per US eGRID subregion) for when the warehouse is cold
* frontend/src/lib/reveal.js—the scroll-driven section reveal that came out of the one-day rewrite

⚖️ This project is licensed underPolyform Shield 1.0.0.

## How I Built It

### The Data Spine 🧬

* Six public-domain federal datasets—all from the Mine Safety and Health Administration (MSHA), Energy Information Administration (EIA), or Environmental Protection Agency (EPA):MSHA Mines—every US mine: lat/lon, operator, county, status, typeMSHA Quarterly Production—tonnage per mine per quarterMSHA Accident Reports—injuries, fatalities, narratives per mineEIA-923 Fuel Receipts (2024 annual, published 2025)—the contract: source mine → destination plant → tonsEIA-860 Plants (2024 annual, published 2025)—plant locations, eGRID subregion, capacityEPA emissions(via Snowflake Marketplace)—CO₂, SO₂, NOx per plant since 2020
* MSHA Mines—every US mine: lat/lon, operator, county, status, type
* MSHA Quarterly Production—tonnage per mine per quarter
* MSHA Accident Reports—injuries, fatalities, narratives per mine
* EIA-923 Fuel Receipts (2024 annual, published 2025)—the contract: source mine → destination plant → tons
* EIA-860 Plants (2024 annual, published 2025)—plant locations, eGRID subregion, capacity
* EPA emissions(via Snowflake Marketplace)—CO₂, SO₂, NOx per plant since 2020
* Mine-level data joins on MSHA Mine ID; plant-level data joins through EIA plant ID.
* Two materialized tables sit on top of the raw joins—MINE_PLANT_FOR_SUBREGIONandEMISSIONS_BY_PLANT—plus two views. Cortex queries hit the materialized layer, not the raw tables.
* H3 hex grid layered on top for active-vs-abandoned density visualization.
* EIA-923 is the one that makes this whole thing possible.Every monthly coal shipment, mine-to-plant, back to the 1990s—the actual contracts that tie your power bill to a specific hole in the ground.
* MSHA Accident Reports are the other half of the story.The human cost on the same mines showing up in the contracts.
* Both feed researchers and journalists just fine. What I didn't see was anything pointed at a regular person standing at their kitchen light switch—so I pointed you right at it.

### Stack 🏗️

* Frontend: SvelteKit 2 + Svelte 5 runes + Vite, static adapter, pnpm. Scroll-driven section reveal.
* Map: Google Maps JavaScript API (dynamicimportLibrary) + Google Places API (New)
* Backend: Python 3.12 + FastAPI
* Deployment: Google Cloud Run
* Data platform: Snowflake—federal ingest + Snowflake Marketplace (EPA emissions); hand-written semantic model YAML for Analyst
* AI: Snowflake Cortex—COMPLETE(llama3.3-70b) for mine prose + H3-density narrative; Analyst for NL Q&A
* Auth: Snowflake key-pair; private key in GCP Secret Manager
* Testing: pytest (unit/integration/perf) · vitest · Playwright · Lighthouse CI witha11y=1.0,SEO=1.0,BP≥0.98,perf≥0.90
* Stateless. No accounts. No login.

### One Day Left 🎨

The UI you see is a late-stage rewrite, courtesy of Claude Design dropping partway through this build. I fed it my first iteration, it came back with a much better idea than what I had, and with one day left on the clock I decided it was absolutely worth the cost to throw out the old one and build the new one.

## Prize Categories

### Best Use of Snowflake ❄️

Snowflake Cortex shows up in three different places in this app, and in each one the LLM call just lives inside the warehouse as a SQL function—llama3.3-70brunningCOMPLETEnext to the rest of yourSELECTstatements. I'd seen you could hook an LLM up to SQL before, but not this specific setup, where the model is another thing you canSELECTfrom.

Verdict: without Cortex, this app is three services glued together with secrets. With it, it's threeSELECTstatements from a warehouse I set up in a weekend.

It was also my first time touching Snowflake, ever—the whole thing runs on the trial credits, and AI did a lot of the translating while I did the plugging-in. I came in with six federal datasets and the vague idea that a coal mine ought to be able to talk back to you, and Snowflake is what made that second part real instead of a pitch deck.

#### Cortex Writes the Mine

SNOWFLAKE.CORTEX.COMPLETE('llama3.3-70b', …)generates the mine prose per subregion—3-5 sentences, named operator, named county, named tonnage, and the accident history folded in. Cached per subregion; no per-request LLM cost on repeat views.

Prompt (fromapp/prose_client.py):

{plant_name} ({plant_operator}) received {tons} tons of coal in {tons_year} from {mine_name}, a {mine_type} mine ({mine_operator}) in {mine_county} County, {mine_state}. Safety record: {fatalities} deaths, {injuries} lost-time injuries, {days_lost} days lost.

Write one paragraph, 3-5 sentences: plant → mine → human cost → the reader's demand. Omit any zero stat. No jargon, no hedging, no markdown.

Enter fullscreen mode

Exit fullscreen mode

#### Cortex Writes the Density Narrative 🎙️

SameCOMPLETEcall, different prompt, on the H3 hex grid of active vs abandoned mines feeding your plant. Fires fromGET /h3-density.

#### Cortex Analyst Handles the Follow-ups 📊

Hand-written semantic model YAML over the federal-data schema. Backs the "Ask your grid" input. Ask about accidents, production, who else buys from this operator—Analyst writes the SQL, runs it, and returns the answer. Chip questions surface the obvious paths; the free-text input handles the rest.

Every Cortex-generated SQL is validated as read-only and single-statement, then executed throughUNEARTHED_READONLY_ROLEwithSTATEMENT_TIMEOUT_IN_SECONDS=10and a 500-row cap. Analyst can read the warehouse. It cannot write to it.

The semantic model is hand-written—every dimension, synonym, filter, and verified query. An excerpt fromassets/semantic_model.yaml:

name
:
 
unearthed_coal_mines

description
:
 
>

 
Federal coal mine and power plant data from MSHA and EIA.

tables
:

 
-
 
name
:
 
MSHA_MINES

 
description
:
 
Registry of all US coal mines from MSHA.

 
dimensions
:

 
-
 
name
:
 
mine_operator

 
synonyms
:
 
[
operator
,
 
company
,
 
owner
,
 
mining company
]

 
description
:
 
Current operator of the mine

 
expr
:
 
TRIM(CURRENT_OPERATOR_NAME)

 
sample_values
:

 
-
 
Peabody Powder River Mining LLC

 
-
 
Arch Resources WY LLC

 
-
 
Murray American Energy Inc

 
# ... full schema in repo

 
-
 
name
:
 
MSHA_ACCIDENTS

 
measures
:

 
-
 
name
:
 
fatality_count

 
expr
:
 
SUM(CASE WHEN TRIM(DEGREE_INJURY) = 'FATALITY' THEN 1 ELSE 0 END)

verified_queries
:

 
-
 
name
:
 
fatalities_at_mine

 
question
:
 
"
How
 
many
 
fatalities
 
have
 
occurred
 
at
 
Upper
 
Big
 
Branch
 
Mine?"

 
sql
:
 
>

 
SELECT SUM(CASE WHEN TRIM(a.DEGREE_INJURY) = 'FATALITY' THEN 1 ELSE 0 END)

 
FROM UNEARTHED_DB.RAW.MSHA_ACCIDENTS a

 
JOIN UNEARTHED_DB.RAW.MSHA_MINES m ON a.MINE_ID = m.MINE_ID

 
WHERE TRIM(m.CURRENT_MINE_NAME) ILIKE 'Upper Big Branch%'

# 7 more verified_queries in the full file

Enter fullscreen mode

Exit fullscreen mode

💡 The fullsemantic_model.yamlcan be found inthe repo.

#### Snowflake Marketplace

The Marketplace is the one I'd put on a billboard. MSHA and EIA I loaded myself, which was a weekend of writing scripts and swearing at CSV encodings. EPA emissions—CO₂, SO₂, NOx per plant since 2020—I clicked a button on the Marketplace and the data was just there, ready to join on plant ID. Cortex plus Marketplace is what moves this fromdata storagetodata product—don't do what I did for the other datasets, click this instead.

#### Cost Dashboards and Cortex Code

This view is optimized for cost over performance, but I used it to troubleshoot slow queries and figure out where to spend my time to actually improve the experience for the user. I'm far from an expert on Snowflake's monitoring surface, but this dashboard and the ones next to it were the difference between the 40+ second queries I started with and something that finishes in time for the scroll to matter.

Cortex Code picked up the last of the excessive queries I had sitting around that Claude hadn't already caught. It behaves noticeably better than the MCP version I leaned on as my main driver for this build, but I was scared to hand my UI to an unfamiliar Streamlit-in-Snowflake AI on a weekend deadline. Definitely something I want to experiment with next time.

## Closing 💜

The cost of mining coal from miles underground has always been paid by the miners and the mountains—rarely by the companies that come in, take what they can, and leave with the profit.Unearthedexists to put that cost in front of the person flipping the light switch, in a form they can interrogate without needing a degree in energy policy. Enter your address and within a minute you'll have the name of the mine, the operator, the county, and the people who got hurt keeping your lights on. Ask the grid a follow-up question in plain English and Cortex writes the SQL for you. Snowflake backs up every claim with data seeded from public sources. This Earth Day, remember the thousands of miners who went underground so your lights could come on, and the mountains that gave life to make it happen.

## Ashley ChildressFollow

Distributed backend specialist. Perfectly happy playing second fiddle—it means I get to chase fun ideas, dodge meetings, and break things no one told me to touch, all without anyone questioning it. 😇

## Sources 📚

* Virginia Department of Energy—Abandoned Mine Land Program—100,000 acres of abandoned mine land + hazard list (landslides, highwalls, subsidence, shafts, fires, etc.)
* EIA—Annual Coal Report 2024 (published Nov 2025)—Virginia 2024 production: 8.6 million short tons
* Appalachian Journal of Law—Addressing Virginia's Legacy GOB Piles—245 legacy GOB piles in Southwest Virginia
* NPS—Pennsylvanian Period (323.2 to 298.9 MYA)—"over 300 million years" coal-formation window
* EPA Power Profiler—closest analogue I found: enter zip, see fuel mix. Stops at percentages.
* iLoveMountains.org—closest emotional analogue: zip-to-mountaintop-removal health correlation. Qualitative, Appalachia-specific, no mine-to-plant data.

### 🛡️ Unearthed One Draft at a Time

This post was written by me with collaborative editing from Claude—who typed most of it, got told it was wrong roughly every three paragraphs, and had every TED-talk rewrite cut before it hit the page. I gave it my voice; it tried to give me something polished; we settled on mine. No AI was harmed in the making of this post, but Claude has now been told to stop editing out my voice enough times to consider filing a formal grievance.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse