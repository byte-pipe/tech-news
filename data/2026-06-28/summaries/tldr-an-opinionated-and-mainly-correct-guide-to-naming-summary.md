---
title: An opinionated (and mainly correct) guide to naming
url: https://adamtornhill.substack.com/p/an-opinionated-and-mainly-correct
date: 2026-06-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-28T18:03:09.993159
---

# An opinionated (and mainly correct) guide to naming

# An opinionated (and mainly correct) guide to naming

## Why naming matters
- Names act as cognitive compression, letting us hold more information mentally.  
- Strong class and function names ease the construction of mental models when reading unfamiliar code.  
- Clear identifiers can cut debugging time (about 19 % reduction).  
- Better names improve AI‑assisted development; studies show they give the biggest gains for LLM code understanding.

## Optimize function names for calling context
- Most advice targets declaration sites, but developers read call sites more often.  
- Choose names that form readable sentences at the call site, e.g. `notify_all(registered_clients, about=the_new_version)`.  
- Sentence‑like calls act as cognitive chunks, expanding the amount of information that fits in working memory.

## Derive names via wishful thinking
- Write code as if the ideal abstraction already exists (inspired by SICP).  
- First craft the natural‑language sentence you want the code to read, then implement the functions to match it.  
- This yields code that feels natural without being overly verbose.

## Let domain types liberate your parameter names
- Avoid “primitive obsession” where domain concepts are represented by raw types (e.g., `int languageId`).  
- Introduce proper domain types (`Language`, `NewsItem`) to convey meaning.  
- With expressive types, parameter names can focus on *why* the argument is needed (e.g., `preferredRssFeedLanguage`, `clickedArticle`).

## Scope determines length
- Variable names should reflect their scope: shorter names for tight scopes, longer, explicit names for broader scopes.  
- Example: `for i, article in enumerate(front_page_articles): publish(article)` – `article` is fine inside the loop.  
- One‑letter names are harmful for instance variables or public APIs where context is insufficient.

## Naming conventions that detract
### Drop the I
- Do not prefix interface names with `I` (e.g., use `ChatConnection` instead of `IChatConnection`).  
- The fact that something is an interface is rarely the most important information and can distract.

### Get rid of the getters … and the setters
- Prefixes like `get` and `set` add procedural noise and encourage “Ask” rather than “Tell” patterns.  
- Prefer intent‑driven names, e.g., `suspend(a_customer)` instead of `set_customer_status(customer, SUSPENDED)`.  
- Even when a query is needed, rename for clarity: `buyer = customer_for(customer_id)`.

### Avoid the dumpster
- Steer clear of generic placeholders such as `Utils`, `Misc`, or `Helper`.  
- Vague names attract vague code; instead, seek a concrete domain concept and give it a precise name.

## Good names reduce reconstruction work
- Over three decades, the author has found that explicit, context‑rich naming minimizes the effort required to understand and modify code.  
- Clear names benefit both human readers and increasingly common AI coding agents, guiding future development with explicit intent.