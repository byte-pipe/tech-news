---
title: Bun Rewrites 535K Lines of Zig into Rust in Four Months, Eliminates Numerous Memory Leaks - InfoQ
url: https://www.infoq.com/news/2026/09/bun-AI-rewrite-zig-rust-4-months
site_name: tldr
content_file: tldr-bun-rewrites-535k-lines-of-zig-into-rust-in-four-m
fetched_at: '2026-09-22T08:46:39.177012'
original_url: https://www.infoq.com/news/2026/09/bun-AI-rewrite-zig-rust-4-months
date: '2026-09-22'
description: Bun creator Jarred Sumner recently announced that Bun, the JavaScript/TypeScript runtime, bundler and package manager has been rewritten from Zig to Rust. The rewrite seeks to eliminate recurrent memo
tags:
- tldr
---

InfoQ HomepageNewsBun Rewrites 535K Lines of Zig into Rust in Four Months, Eliminates Numerous Memory Leaks

 Web Development
 

InfoQ Certified AI-Assisted Engineering Program (online, Oct 19): Build the harness that holds. 

# Bun Rewrites 535K Lines of Zig into Rust in Four Months, Eliminates Numerous Memory Leaks

Sep 20, 20264
									min read

by

* Bruno Couriol

#### Follow us on

Youtube
232K Followers

Linkedin
26K Followers

Instagram
New

RSS
19K Readers

X
57.1k Followers

Facebook
21K Likes

Bluesky
New

Bun creator Jarred Sumnerrecently announcedthat Bun, the JavaScript/TypeScript runtime, bundler and package manager has been rewritten from Zig to Rust. The rewrite seeks to eliminate recurrent memory safety vulnerabilities via Rust’s borrow checker. The AI-assisted rewrite was released after 4 months of work instead of the estimated one year.

Sumner summarizes the motivation behind what started as a spike:

A large percentage of bugs […] are use-after-free, double-free, and “forgot to free” in an error path. In safe Rust, these are compiler errors and RAII-like automatic cleanup withDrop. Compiler errors are a better feedback loop than a style guide.

Historically, rewrites are a terrible idea. […] Bun is 535,496 lines of Zig. A rewrite in another language would take a small team of engineers a full year. It would mean freezing bugfixes, security fixes or feature development for that time.

Fortunately, Bun’s own test suite is written in TypeScript which means it doesn’t depend on the runtime’s programming language.

What if, instead, I spend a week testing if Anthropic’s new model can rewrite Bun in Rust?

At first, I didn’t expect it to work. A few days in, a high % of the test suite started passing and I saw how much the new Rust code matched up with the original Zig codebase. My opinion went from “this is worth trying” to “I’m going to merge this”.

Sumner executed an automated all-at-once port leveraging for most of the rewrite a pre-release version of Claude Fable 5 orchestrated across approximately 50 dynamic workflows. The Zig would be transpiled into Rust (possibly usingunsafeRust that could be refactored later) and validated against the existing extensive test suite of more than one million assertions. A porting guide would help Claude map Zig patterns & types to Rust patterns & types. Adversarial agentic code reviews would further detect issues before they make it to the final port. The implementation loop would be improved after each error by improving the implementation process rather than manually fixing the implementation artifacts (e.g., the code).

The constant process improvement revealed useful patterns. The planning phase is critical to success and must result in key challenges being anticipated and mitigated.PORTING.md(describing the mapping from Zig to Rust) andLIFETIMES.tsvfile (describing lifetimes of every struct field in the codebase) were key success factors for the port.

An implementer would then use those files to translate Zig files into Rust code. The implementer agent would be faced with two adversarial reviewer agents running in isolated context windows with access only to the file diffs, with their only task being to discover bugs and behavioral divergences. Sumner emphatically explains:

The implementer doesn’t review. The reviewer doesn’t implement.

Suggestions and issues found by the reviewer agents were dealt with by a fixer agent.

The implementation process efficiency massively leverages the parallelization of the implementation tasks. That however requires addressing concurrent updates of the shared codebase, and the starvation of limited computing resources.

The effort was ultimately distributed across four workspace shards running 16 agents each, operating 64 Claude instances in parallel. At peak velocity, the system generated roughly 1,300 lines of code per minute and logged up to 695 commits an hour.

Getting to the full test suite passing required $165,000 worth of tokens — to be contrasted with Sumner’s estimate of human engineering effort:

Pre-merge, this took 5.9 billion uncached input tokens, 690 million output tokens, and 72 billion cached input token reads — around $165,000 at API pricing. By hand, I think this would’ve taken 3 engineers with full context on the codebase about a year.

Having what became over 1 million lines of code pass the test suite was then followed by further testing and validation, which surfaced further issues.

The mechanical nature of the port introduced 19 subtle semantic regressions rooted in syntactic similarities between Zig and Rust. 11 rounds of security review fromClaude Code Securityfixed several security issues. 24/7 coverage-guided fuzzing of every parser in Bun resulted in 15 PRs.

According to the Bun team, the resulting Rust implementation in Bun v1.4.0 resolved 128 longstanding bugs present in v1.3.14 while delivering noticeable dividends. Native memory leaks were addressed. In-process bundling tests running 2,000 consecutiveBun.build()operations plateaued stably at 609 MB in Rust rather than climbing past 6.7 GB. HTTP throughput increased by 2% to 5%.

Bun v1.4.0 was finallyreleased in August 2026.

Zig creator Andrew Kelley published a sharply critical reaction titled“My Thoughts on the Bun Rust Rewrite,”which included the following comments:

There’s a dichotomy being presented here where you have to either choose a “style guide” or a programming language feature in order to avoid bugs. The sleight of hand misdirects the reader away from the main way bugs are eliminated: by dedicating engineering resources to it. […]

The argument for shipping all the million lines of unreviewed code is that the test suite is good enough to catch everything. Then why are you saying you have so many annoying bugs in the Zig code? What happened to the test suite being sufficient to catch everything? It’s not sufficient to catch bugs in Zig code but it is sufficient to catch bugs in 1 million lines of unreviewed slop?

Concurrently, uservitaminCPPposited that merging over one million lines of machine-transpiled code establishes Bun as a crucial industry canary for whether massive, LLM-generated codebases can remain maintainable over the software engineering lifecycle.

Developers are encouraged toread the full article, which contains in-depth technical explanations and accompanying illustration and graphics.

Bun wasacquired by Anthropic in December 2025.

 

## About the Author

 

 

 

#### Bruno Couriol

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theWeb Developmenttopic

##### Related Topics:

* Development
* Web Development
* Bundlers
* AI Assisted Coding
* Rust
* System Programming

* #### Related Editorial
* #### Related Sponsors
* #### Related SponsorOctober 8, 2026, 12 PM EDT##### When AI Accelerates Development, Can Your CI Pipeline Keep Up?Presented by: Eric Metaj - Product Marketing Manager, Software Delivery at Datadog, and Rohin Chandra - Product Manager, CI/CD Optimization at Datadog
* October 8, 2026, 12 PM EDT##### When AI Accelerates Development, Can Your CI Pipeline Keep Up?Presented by: Eric Metaj - Product Marketing Manager, Software Delivery at Datadog, and Rohin Chandra - Product Manager, CI/CD Optimization at Datadog

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this 
Privacy Notice
.

We protect your privacy.