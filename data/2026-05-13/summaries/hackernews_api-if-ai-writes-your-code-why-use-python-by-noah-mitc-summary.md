---
title: If AI Writes Your Code, Why Use Python? | by Noah Mitchem | Apr, 2026 | Medium
url: https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055
date: 2026-05-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-13T06:03:27.671717
---

# If AI Writes Your Code, Why Use Python? | by Noah Mitchem | Apr, 2026 | Medium

# If AI Writes Your Code, Why Use Python?

## Background
- For a decade developers chose Python or TypeScript for rapid demos, deep talent pools, and massive ecosystems, accepting slower runtime performance.
- The trade‑off “ship fast, optimise later” persisted because the effort to rewrite in faster languages was high.

## AI Makes Hard Languages Easy
- Recent AI models (Claude Opus 4.7, GPT‑5.5, Gemini 3.1, DeepSeek V4) achieve >80 % on SWE‑bench Verified, handling concurrency bugs and architectural issues.
- Strong type systems and fast compile‑check loops give agents tight iteration cycles; Rust, Go, and Swift become the easiest languages for AI‑assisted development.
- A tweet summarized the shift: AI now writes better Rust than C, using compiler feedback as continuous training data.

## Real‑World Shipping
- **Microsoft** rewrote the TypeScript compiler in Go, delivering a 10× speed boost for the new TypeScript 7.0 beta.
- **Anthropic** coordinated 16 Claude agents to produce a 100 k‑line C compiler in Rust, capable of booting Linux and compiling major projects for under $20 k.
- **Steve Klabnik** built a new systems language (Ruein) in two weeks with Claude, writing ~70 k lines of Rust.
- **Andreas Kling** ported Ladybird’s JavaScript engine from C++ to Rust in two weeks, achieving byte‑for‑byte parity and zero regressions.
- These feats were impossible in 2024, marginal in 2025, and commonplace by early 2026.

## Ecosystem Shift
- Python and JavaScript’s historic advantage was their rich ecosystems (FastAPI, Django, React, npm, etc.).
- Many popular Python packages now wrap Rust code (pydantic, Polars, Hugging Face tokenizers, orjson); Rust usage in Python extensions rose from 27 % to 33 % in a year.
- New tooling (ruff, uv, ty) written in Rust has amassed hundreds of millions of downloads; major acquisitions (OpenAI buying Astral, Anthropic buying Bun) cite AI‑driven productivity gains.
- The “wrapper” overhead is shrinking, making direct use of Rust/Go more attractive.

## Patch vs. Port
- Traditional open‑source flow: pick Python, fix bugs, upstream patches, ecosystem improves.
- AI changes the unit of contribution: porting entire libraries becomes cheap (e.g., Armin Ronacher ported MiniJinja to Go in 45 minutes of human time, $60 API cost).
- When a full port costs minutes, the incentive to upstream small patches diminishes; focus shifts to tests and documentation.

## Limitations
- Some cases still favor the “old” stack: Prisma’s move to a TypeScript/WASM core reduced bundle size and increased query speed; native Rust binaries can be problematic for serverless runtimes; PyTorch remains dominant in deep‑learning research.
- AI performance varies across languages; smaller or less‑represented languages (Zig, Haskell, Gleam) receive lower quality assistance due to limited training data.

## Why the Shift Is Permanent
- The original defense of Python/TypeScript was developer experience—minimising friction from idea to shipped product.
- AI now handles the friction‑heavy coding work; human effort moves to system architecture and output review.
- As runtime advantages of compiled languages compound over time in production, the ergonomic edge of Python erodes each quarter, making the shift toward systems languages enduring.