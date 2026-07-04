---
title: 'GitHub - teamchong/pxpipe: cut Fable 5 token usage by rendering text context as images · GitHub'
url: https://github.com/teamchong/pxpipe
site_name: hackernews_api
content_file: hackernews_api-github-teamchongpxpipe-cut-fable-5-token-usage-by
fetched_at: '2026-07-04T11:32:38.971468'
original_url: https://github.com/teamchong/pxpipe
author: dimitropoulos
date: '2026-07-03'
description: cut Fable 5 token usage by rendering text context as images - teamchong/pxpipe
tags:
- hackernews
- trending
---

teamchong

 

/

pxpipe

Public

* NotificationsYou must be signed in to change notification settings
* Fork47
* Star990

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

298 Commits
298 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
bench
bench
 
 
bin
bin
 
 
demo
demo
 
 
docs
docs
 
 
eval
eval
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
FINDINGS.md
FINDINGS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
wrangler.toml
wrangler.toml
 
 
View all files

## Repository files navigation

# pxpipe

Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens.

An image's token cost is fixed by its pixel dimensions, not by how much text
is inside it. Dense content (code, JSON, tool output) packs ~3.1 chars per
image-token vs ~1 char per text-token on real Claude Code traffic. pxpipe is
a local proxy that exploits the gap: it rewrites the bulky parts of each
request into compact PNGs before it leaves your machine. At current Fable
list prices that lands as a~59–70% lower end-to-end bill— but prices
move and workloads differ, so the durable number is the token cut itself,
measured per-request against a freecount_tokenscounterfactual in~/.pxpipe/events.jsonl.

This is what the model sees instead of text:

~48k chars of system prompt + tool docs: ≈25k tokens as text, ≈2.7k image
tokens as this page. Real pipeline output; the model reads renders like this
at 100/100 (see benchmarks).

## Demo

Fable 5 (the default, 100/100 reader) — plain left, pxpipe right:

Fable-AB-Demo.mp4

pxpipe counts an exact token10/10across 39 imaged filler files
(matchesgrepline-for-line), gets the multi-step ledger arithmetic right,
and ends the session at$6.06with context to spare (73.5k/1M) vs$42.21at 96% full. One caveat visible in the clip: the pxpipe arm
needed a nudge to match the requested one-line output format.

Opus 4.8 (disabled by default) — same layout:

Opus-AB-Demo.mp4

Text needles read fine on both arms; the imaged phrase-count doesn't read on
Opus — and pxpipesays so instead of fabricating a number. That misread
rate is why Opus is opt-in.

## Try it (30 seconds)

npx pxpipe-proxy 
#
 proxy on 127.0.0.1:47821

ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude 
#
 point Claude Code at it

Dashboard athttp://127.0.0.1:47821/: tokens saved, every text→image
conversion side by side, kill switch, live model chips. Responses stream
normally — pxpipe compresses therequestonly, never the model's output.
Recent turns stay text; the system prompt, tool docs, and older bulk history
are imaged.

## The honest part

* It is lossy.Exact 12-char hex strings in dense imaged content:13/15on Fable 5,0/15on Opus — and misses aresilent
confabulations, not errors. Byte-exact values (IDs, hashes, secrets)
must stay text; recent turns do. A dedicated verbatim-risk guard is not
built yet.
* Escape hatch:subagents on non-allowlisted models pass through as
text — route byte-exact work there
(CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-4-6, ormodel: sonnetin
agent frontmatter).
* Real work:SWE-bench Lite pilot10/10 both armsat −65% request
size; SWE-bench Pro14/19 ON vs 15/19 OFFat −60%, verdicts agree
18/19, and the single split re-resolved 3/3 on replication — run-to-run
variance, not compression. Small n; receipts ineval/.
* Workload-dependent.Wins on token-dense content (~1 char/token),
loses money on sparse prose (~3.5 chars/token); a profitability gate
(calibrated on N=391 production rows) images only where the math wins.
* Model scope:defaultPXPIPE_MODELS=claude-fable-5,gpt-5.6. Opus
4.7/4.8 misread ~7% of renders and GPT 5.5 degrades on imaged context, so
both are opt-in viaPXPIPE_MODELSor the dashboard chips.PXPIPE_MODELS=offdisables imaging. Everything else passes through
byte-identical. On the GPT path, tool definitions stay native JSON and no
Anthropiccache_controlmarkers are used.

## Benchmarks (reproducible)

Measured with novel random-number problems the model cannot have memorized:

test

N

text

pxpipe (image)

tokens

novel arithmetic, 
claude-fable-5

100

100%

100%

−38%

novel arithmetic, 
claude-opus-4-8

100

100%

93%

−38%

gist recall A/B (decisions, values, paths, names, negations; with distractors; 15k-45k char sessions), Fable 5

98/arm

98/98

98/98

-

state tracking (value mutated 3x, final/first/count), Fable 5

18/arm

18/18

18/18

-

confabulation on never-stated facts (lower is better), Fable 5

16/arm

0/16

0/16

-

verbatim 12-char hex recall, dense render, Opus

15

15/15

0/15

-

verbatim 12-char hex recall, dense render, Fable 5

15

-

13/15

-

SWE-bench run totals, receipts, and caveats:eval/swe-bench/·eval/swe-bench-pro/·eval/needle-haystack/·eval/gist-recall/· analysis inFINDINGS.md. (GSM8K scored 96% imaged, but it's in training
data — memorized answers survive misreads — so we lead with the novel-number
evals.)

## How it works

tool_result string ──► wrap at 1928px-wide columns ──► pack ~92,000 chars/page ──► PNG[]

The proxy intercepts/v1/messages, rewrites eligible bulk into image
blocks, splices them back cache-friendly (static prefix preserved, prompt
caching keeps working), and forwards. A 1928×1928 image costs ≈4,761 vision
tokens and holds ≈92,000 chars, so text wins only above ~19 chars/token —
Claude Code traffic runs ~1.91 (N=391). A per-request estimator decides;
sparse prose stays text. Events log to~/.pxpipe/events.jsonl.

## Library use (no proxy)

import
 
{
 
renderTextToPngs
,
 
transformAnthropicMessages
 
}
 
from
 
"pxpipe"
;

const
 
imgs
 
=
 
await
 
renderTextToPngs
(
toolResultText
)
;
 
// RenderedImage[]

const
 
{
 body
,
 applied
,
 info 
}
 
=
 
await
 
transformAnthropicMessages
(
{

 
body
: 
requestBytes
,

 
model
: 
"claude-fable-5"
,

}
)
;

options.keepSharp(block)pins blocks as text;options.emitRecoverablereturns the originals of imaged blocks. Pure-JS runtime (Node and
edge/Workers);@napi-rs/canvasis build-time only. Full API:src/core/index.ts.

## Development

pnpm install 
&&
 pnpm 
test

pnpm run build 
#
 regenerates dist/

## FAQ

Is the headline end-to-end, or only on the requests you touched?End-to-end, the whole bill. Most compression tools report savings only on
the input slice they touched, which flatters the number. The end-to-end
denominator iseveryproduction request: the small ones pxpipe correctly
left untouched, all cache writes and reads, and all output tokens (which the
proxy never compresses). On a 13,709-request snapshot that was 59% ($100 →
~$41); a later 8,904-compressed-request trace measured ~70%. Compressed-only
runs higher (~72–74%) and is quoted separately, never as the headline. The
exact figure is workload-dependent — reproduce it on your own log.

How is the math measured?Both sides of the same request, at the same moment. For every/v1/messagesPOST the proxy fires a freecount_tokensprobe on the original uncompressed
body (the counterfactual) in parallel with the real forward, and reads
Anthropic's actually-billed usage block off the response. Both land in the
same row of~/.pxpipe/events.jsonl, so there is no turn-count or
run-to-run confound. Dollar conversion uses Fable 5 list ratios: input ×1.0,
cache write ×1.25, cache read ×0.1, output ×5. Cache pricing is applied
identically to both sides, so the caching discount cancels and cannot be
double-counted as "savings". Re-derive it yourself from the events log: the
formula and field names are documented insrc/core/baseline.ts.

What does it actually compress?Three kinds ofinputblocks, each behind a profitability gate:

1. largetool_resultbodies (file reads, command output, logs) above
~6k chars of token-dense content
2. older collapsed history: turns behind the live tail get re-rendered as
image pages, recent turns always stay text
3. the static system prompt + tool docs slab

Everything else passes through byte-identical: your messages, recent turns,
the model's output (it is the response, the proxy never touches it), sparse
prose, and anything too small to win. Models outside the allowlist pass
through entirely — the default scope is Fable 5 and GPT 5.6 only. Opus 4.8
and GPT 5.5 read imaged content measurably worse (FINDINGS.md 2026-06-16),
so they are deliberately opt-in via the dashboard orPXPIPE_MODELS, never
silently imaged.

Has it ever failed for real, outside the benchmarks?Yes, once in weeks of daily use: the model recalled a person's name from
imaged chat history and got it confidently wrong. No error, just a
plausible wrong name. That is the documented failure mode: exact strings
in imaged content are not byte-safe. Coding sessions tolerate this because
the agent re-reads files before editing; pure chat recall has no such check.
This failure mode is measured, not anecdotal:the legibility auditquantifies
exact-string recall off rendered pages (blind reads top out at 63% on dense
identifiers, with every miss predicted by a glyph-confusability matrix) and
documents the shipped mitigations — page geometry clamped to the API's
resample cap so billed pixels actually reach the vision encoder, and exact
identifiers (SHAs, numbers) riding alongside as text.

Why does the README read like an AI wrote it?Because one did. Most of this repo's commits — the code and the docs — were
authored by Opus/Fable agent sessions running behind pxpipe itself, reading
their own collapsed history as image pages while they worked.

## Limitations

* Lossy (above); verbatim recall from images is unreliable.
* PNG encoding adds latency to large requests before they leave.
* ASCII/Latin-1 well tested; CJK works but conservatively.

## Roadmap

Hypotheses, not claims — they ship as numbers with an n or they get cut:
sharper glyph rendering (eval/glyph-matrix/, paused mid-run), whether
imaged bulk stretches effective context (~2x the real content in the same
1M window), and whether a smaller active context improves long-task
accuracy.

## License

MIT.

## About

cut Fable 5 token usage by rendering text context as images

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

990

 stars
 

### Watchers

6

 watching
 

### Forks

47

 forks
 

 Report repository

 

## Releases2

v0.7.1

 Latest

 

Jul 3, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript96.1%
* JavaScript1.8%
* Shell1.1%
* Python1.0%