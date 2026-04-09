---
title: Building a "Text-to-GIS" Engine with SvelteKit, PostGIS and Open-Source LLMs - DEV Community
url: https://dev.to/zeekrey/building-a-text-to-gis-engine-with-sveltekit-postgis-and-open-source-llms-57bo
site_name: devto
fetched_at: '2025-12-21T19:06:42.283022'
original_url: https://dev.to/zeekrey/building-a-text-to-gis-engine-with-sveltekit-postgis-and-open-source-llms-57bo
author: Christian
date: '2025-12-18'
description: A few days ago, I was grabbing coffee with a data scientist friend who works at a local energy... Tagged with webdev, ai, gis, svelte.
tags: '#webdev, #ai, #gis, #svelte'
---

A few days ago, I was grabbing coffee with a data scientist friend who works at a local energy provider here in Germany. He looked exhausted.

When I asked what was going on, he said:

“I’m basically a human SQL converter. Marketing, Sales, Strategy… they all send vague questions like ‘Where are our high-consumption customers?’ and I spend all day writing complex PostGIS queries to get them CSVs.”

I asked the obvious follow-up:

“Why don’t you just build a chatbot so they can ask the database directly?”

He laughed.

“Legal would shut it down immediately. We can’t send our internal schema or customer data to some hyperscaler. And IT won’t give us budget for a massive on-prem GPU cluster just to run a prototype.”

That stuck with me.

## The key idea

You don’t need a huge commercial LLM to write SQL.

And you definitely don’t need to ship your schema (or your data) to the US to get value from “AI in the business”.

So I built a smallText-to-SQL + PostGISdemo usingopen datafrom my hometown (Leipzig) to prove the concept end-to-end.

The goal: a user types something like:

“Show me all parks in Leipzig larger than 5 hectares.”

…and the system returns aGeoJSON layerthat can be rendered on a map.

What the system needs to do:

* Identify the right dataset (“parks”) →table/layer relevance
* Understand location context (“Leipzig”) →spatial context
* Translate constraints (“> 5 hectares”) →math + filtering
* Output something we can draw →GeoJSON

## Tech stack

Here’s what I used:

* SvelteKitfor the web apphttps://svelte.dev/docs/kit/introduction
* PostgreSQL + PostGISfor spatial querieshttps://postgis.net/
* A hostedopen-weights code model:qwen3-coder:30bhttps://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
* Vercel AI SDKto wire LLM calls in SvelteKithttps://ai-sdk.dev/docs/getting-started/svelte
* MapLibre GLto render the result on a maphttps://maplibre.org/maplibre-gl-js/docs/

Whyqwen3-coder:30b? For Text-to-SQL you want a model that’s extremely good at syntax and structured output. This one performs very well in coding tasksandit’s open weights—so you can run/host it in Germany without relying on a US API.

## The real “secret”: schema context (and rules)

The hardest part wasn’t the code. It was the prompt.

If you just ask an LLM “write SQL”, it will confidently hallucinate tables and columns that don’t exist. The fix is to injectreal schema contextand enforce strict rules.

Here’s the system prompt I ended up with:

You are a PostGIS expert. Your goal is to convert natural language queries into SQL queries for a PostGIS database.

The database has a single table named "city_objects" with the following schema:
- id: serial primary key
- layer_name: text (The name of the dataset)
- properties: jsonb (Attributes of the object. Keys vary by layer.)
- geometry: geometry(Geometry, 4326)

${SCHEMA_CONTEXT}

Rules:
1. Always return a valid SQL query.
2. The query should select the GeoJSON representation of the geometry using ST_AsGeoJSON(geometry) as "geojson," and the properties column.
3. Example: SELECT properties, ST_AsGeoJSON(geometry) as geojson FROM city_objects WHERE layer_name = 'SK_Vegetationsmerkmal_f' LIMIT 10;
4. Use the "Dataset Definitions" above to identify the correct 'layer_name' and property keys (e.g., 'd_FKT', 'd_BWS') for the user's request.
5. CRITICAL: Do not guess column names. If the definition says 'd_BWF', use 'd_BWF'. Do not use 'd_FKT' unless listed for that layer.
6. CRITICAL: Use ILIKE with wildcards for text filtering to match partial strings. Example: properties->>'d_FKT' ILIKE '%Schwimmbad%'. Do not use = for text descriptions.
7. If the user asks for a specific location or spatial relationship, use PostGIS functions like ST_Contains, ST_DWithin, etc.
8. Do not include markdown formatting (sql) in the output, just the raw SQL.

Enter fullscreen mode

Exit fullscreen mode

### Why${SCHEMA_CONTEXT}matters

Instead of hardcoding dataset definitions in the prompt, I generate them automatically.

At build time, a script crawls the database, discovers available layers + JSON property keys, and injects them into${SCHEMA_CONTEXT}. That single change massively improved correctness because:

* The model stops inventing columns
* It reliably picks the correctlayer_name
* Filtering uses real JSON keys that exist for that layer

Also: explicit rules help. I keep updating them as I see failure modes in real prompts.

## Model choice: small vs. “big enough”

I started with smaller models likeqwen3:4b.

Sometimes it worked—but often the SQL was wrong, incomplete, or the model just didn’t return anything usable. In the end,qwen3-coder:30bwas the sweet spot for:

* consistent SQL syntax
* fewer hallucinations (with schema context)
* better handling of multi-step spatial logic

I’m currently buildingSUPA, so I used a hosted setup for inference. (There are plenty of affordable hosted options out there if you don’t want to operate GPUs yourself.)

## Implementation notes (SvelteKit + AI SDK)

To bootstrap the app:

npx sv create my-ai-app

Enter fullscreen mode

Exit fullscreen mode

Then follow the SvelteKit guide in the AI SDK docs to wire up an API route that calls your model provider:https://ai-sdk.dev/docs/getting-started/svelte

### Provider options

If you want to run locally with a small model, you can use Ollama via the community provider:

* https://ai-sdk.dev/providers/community-providers/ollama

If you want to call a hosted endpoint (SUPA in my case) using the OpenAI-compatible provider, you can set a custom base URL:

const

openai

=

createOpenAI
({


apiKey
:

env
.
SUPA_API_TOKEN
,


baseURL
:

env
.
BASE_HREF

});

Enter fullscreen mode

Exit fullscreen mode

Flow-wise it’s simple:

* User prompt → LLM returns SQL (raw SQL only)
* Backend executes SQL against PostGIS
* Response returnsproperties+geojson
* Frontend renders it with MapLibre

I won’t go deep into MapLibre rendering here, but the GeoJSON output makes it straightforward.

## What I learned

For a lot of business problems, you don’t need a frontier “foundation model” to ship something useful.

Foundation models are amazing, and they keep getting better every week—but for workflows like “turn vague questions into database queries”, you can get very far with:

* a capable coding model
* strict output rules
* real schema injection
* and a setup that keeps data where it must stay (e.g., Germany/EU)

## Links

* Live demo:https://gis.examples.supa.works
* Repo:https://github.com/supaworks/field-guide/tree/main/examples/natural-language-gis

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
