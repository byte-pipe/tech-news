---
title: Adopting Herb at GitHub - Joel Hawksley
url: https://hawksley.org/2026/05/06/adopting-herb-at-github.html
date: 2026-05-16
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-16T06:01:54.917211
---

# Adopting Herb at GitHub - Joel Hawksley

# Adopting Herb at GitHub

## Why we are adopting Herb
- Rails core team wants Herb to replace Erubi; GitHub serves as a large‑scale validation ground.  
- GitHub.com contains ~500 k lines of ERB across ~10 k files (≈50 lines/file).  
- Recent UI work added 350 files and 15 k lines of ERB in 2025, showing continued ERB usage.

## Our process
- Started in December 2025; initial runs of `npx @herb-tools/linter` with only the `parser-no-errors` rule.  
- First run: <75 % of ERB files passed; 2,768 files required fixing.  
- Most bugs caught were benign, making the effort worthwhile.

## Bugs found by Herb
### Invalid HTML
- Missing closing tags and swapped closing tags for HTML elements and ERB blocks.  
- Browsers tolerate some errors, but fixing improves code quality.

### Conditional opening/closing tags
- Patterns where opening/closing tags are wrapped in conditional ERB blocks caused AST translation issues.  
- Refactored to capture content in a variable and render conditionally; Herb later added support for the original pattern.  
- ~150 occurrences; fixed efficiently using Claude Opus models for one‑shot AI fixes.

### Invalid Ruby
- Herb detected Ruby syntax errors inside ERB that were missed by `erb_lint` and not exercised in CI, e.g., malformed `if` statements and misplaced `do` blocks.  
- Because Herb parses Ruby with Prism, these errors surfaced immediately.

## Bugs found in Herb
### Whitespace handling
- Example: `hello\n<%=-%>\nworld` produced `helloworld` in Erubi but `hello\nworld` in Herb.

### Invalid Ruby generation
- When a comment followed an `end` on the same line, Herb emitted invalid Ruby, leading to potential runtime exceptions.  
- Highlighted a broader issue: Rails trusts ActionView handlers to produce valid Ruby; added Ruby validation to Herb’s `analyze` command.

### Vendored templates
- Herb CLI ignores `vendor` directory; gems with ERB (e.g., Primer ViewComponents, good_job) could cause crashes if Herb cannot parse them.  
- Implemented a custom CI check to force‑compile all vendored `.erb` files and opened a bug report.  
- Submitted PRs to make GraphQL‑Ruby and Primer ViewComponents Herb‑compatible.

## Performance impact
- Runtime performance unchanged, but boot time increased from ~2 min to ~3 min.  
- Compilation of templates is significantly slower with Herb (7–15× slower depending on size).  
- Example metrics:  
  - Tiny (58 B): Erubi 3.9 µs → Herb 28.3 µs (+24 µs)  
  - Small (250 B): Erubi 10.4 µs → Herb 116.1 µs (+106 µs)  
  - Medium (1 KB): Erubi 24.4 µs → Herb 365.6 µs (+341 µs)  
  - Large (3 KB): Erubi 81.7 µs → Herb 1,059.7 µs (+978 µs)  
- GitHub.com uses `ActionView::Precompiler` to warm the template cache at boot, amplifying the slowdown but also saving ~500 MB memory per container.  
- Exploring build‑time caching (similar to Bootsnap) but currently blocked from production deployment until compilation speed improves.  
- Marco Roth believes Herb can be optimized to address this issue.