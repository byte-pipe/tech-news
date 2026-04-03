---
title: How I Taught GitHub Copilot Code Review to Think Like a Maintainer - DEV Community
url: https://dev.to/techgirl1908/how-i-taught-github-copilot-code-review-to-think-like-a-maintainer-3l2c
site_name: devto
fetched_at: '2025-11-30T11:06:32.366543'
original_url: https://dev.to/techgirl1908/how-i-taught-github-copilot-code-review-to-think-like-a-maintainer-3l2c
author: Angie Jones
date: '2025-11-25'
description: Open source maintainers are getting more contributions than ever, thanks to AI-assisted coding. That's great for community growth but it also means a flood of PRs to review. Here's how I taught GitHub Copilot Code Review to think like a maintainer. Tagged with github, githubcopilot, ai.
tags: '#github, #githubcopilot, #ai'
---

Say what you want about vibe coding, but it's been great for open source. Contributing to unfamiliar codebases used to be daunting, which meant maintainers of open source projects received very little community help no matter how popular the project was. But now with AI coding tools, the barrier to contribute is much lower. In fact, we have quite the opposite problem withgoose, an open source AI agent framework built in Rust. We're getting so many contributions that it's hard to keep up! It's a beautiful problem to have, and we want to make sure the contributors are having a good experience. But it's just too much for us to review on our own. Fortunately, there's aCopilot Code Review agentalready in GitHub ready to review every PR as soon as it's opened.

I turned it on thinking everyone would love it, but honestly it didn’t go so well. The other maintainers said the reviews were too noisy and most of the comments were of low value. They asked if we could just turn it off.

Here's what I know from helping engineers work with AI: you don’t throw in the towel. You don’t disable. You tune. You teach the model how you want to work, not just hope for the best.

In assessing some of its reviews, I could see the problems were pretty consistent:

* The comments were long and overwhelming
* There were too many "maybe" and "consider" comments signaling low confidence
* Only about 1 in 5 comments were actually good catches that the contributor would have missed

I don't blame Copilot for any of this. How would it know what we cared about? We didn't tell it! Fortunately, there's a way to do just that.

Copilot supportscustom instructionsthrough a.github/copilot-instructions.mdfile. That’s where I specified exactly how we wanted it to behave.

### Review Philosophy

I started by teaching Copilot the same principles we expect from human reviewers.

## Review Philosophy

* Only comment when you have HIGH CONFIDENCE (>80%) that an issue exists
* Be concise: one sentence per comment when possible
* Focus on actionable feedback, not observations
* When reviewing text, only comment on clarity issues if the text is genuinely confusing or could lead to errors.

Enter fullscreen mode

Exit fullscreen mode

This immediately cut down the noise. It stopped speculating and started focusing on clear, confident feedback.

### Priority Areas

Then I told it exactly what to prioritize. These are the areas we actually care about in reviews. Again, how would Copilot know that unless I give it this context?

## Priority Areas (Review These)

### Security & Safety

* Unsafe code blocks without justification
* Command injection risks (shell commands, user input)
* Path traversal vulnerabilities
* Credential exposure or hardcoded secrets
* Missing input validation on external data
* Improper error handling that could leak sensitive info

### Correctness Issues

* Logic errors that could cause panics or incorrect behavior
* Race conditions in async code
* Resource leaks (files, connections, memory)
* Off-by-one errors or boundary conditions
* Incorrect error propagation (using `unwrap()` inappropriately)
* Optional types that don’t need to be optional
* Booleans that should default to false but are set as optional
* Error context that doesn’t add useful information
* Overly defensive code with unnecessary checks
* Unnecessary comments that restate obvious code behavior

### Architecture & Patterns

* Code that violates existing patterns in the codebase
* Missing error handling (should use `anyhow::Result`)
* Async/await misuse or blocking operations in async contexts
* Improper trait implementations

Enter fullscreen mode

Exit fullscreen mode

Once it had this list, Copilot stopped nitpicking and started catching real problems.

### Project-Specific Context

Copilot doesn't magically know your setup. You have to tell it what kind of project it's reviewing.

## Project-Specific Context

* This is a Rust project using cargo workspaces
* Core crates: `goose`, `goose-cli`, `goose-server`, `goose-mcp`
* Error handling: Use `anyhow::Result`, not `unwrap()` in production
* Async runtime: tokio
* See HOWTOAI.md for AI-assisted code standards
* MCP protocol implementations require extra scrutiny

Enter fullscreen mode

Exit fullscreen mode

This context helps it understand our architecture and the patterns that matter most.

### CI Pipeline Context

Copilot reviews PRs before CI finishes, so without context, it'll comment on things CI already checks. I added this so it knows what's covered.

## CI Pipeline Context

**Important**: You review PRs immediately, before CI completes. Do not flag issues that CI will catch.

### What Our CI Checks (`.github/workflows/ci.yml`)

**Rust checks:**

* cargo fmt --check
* cargo test --jobs 2
* ./scripts/clippy-lint.sh
* just check-openapi-schema

**Desktop app checks:**

* npm ci
* npm run lint:check
* npm run test:run

**Setup steps CI performs:**

* Installs system dependencies
* Activates hermit environment
* Caches Cargo and npm deps
* Runs npm ci before scripts

**Key insight**: Commands like `npx` check local node_modules first. Don't flag these as broken unless CI wouldn't handle it.

Enter fullscreen mode

Exit fullscreen mode

### Skip These

The next section is crucial. I told it whatnotto bother us with.

## Skip These (Low Value)

Do not comment on:

* Style/formatting (rustfmt, prettier)
* Clippy warnings
* Test failures
* Missing dependencies (npm ci covers this)
* Minor naming suggestions
* Suggestions to add comments
* Refactoring unless addressing a real bug
* Multiple issues in one comment
* Logging suggestions unless security-related
* Pedantic text accuracy unless it affects meaning

Enter fullscreen mode

Exit fullscreen mode

### Response Format

To fix verbosity, I gave it a structure.

## Response Format

1. State the problem (1 sentence)
2. Why it matters (1 sentence, if needed)
3. Suggested fix (snippet or specific action)

Example:
This could panic if the vector is empty. Consider using `.get(0)` or adding a length check.

Enter fullscreen mode

Exit fullscreen mode

### When to Stay Silent

LLMs love to overshare. Sometimes silence is the right call.

## When to Stay Silent

If you’re uncertain whether something is an issue, don’t comment.

Enter fullscreen mode

Exit fullscreen mode

### Key Takeaways

After tuning Copilot, the difference was immediate. The noise dropped dramatically, and the comments became more useful.

But this isn't its final form. As more PRs came in, I watched how Copilot responded and refined the instructions each time. Here's the current version of ourcode review instructions.

If you decide to set this up for your own repo, expect to do the same. It's not a one-time fix. You'll need to observe, adjust, and keep teaching it as your project evolves.

If AI isn't quite working for your codebase, don't write it off. You can likely make it work in your favor by following these tips:

1. Be specific. Vague instructions lead to vague results.
2. Set confidence thresholds to reduce noise.
3. Tell it what CI already covers.
4. Include real examples from your codebase.
5. Iterate to keep improving results over time.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
