---
title: "Bug Smash: restoring dropped Gemini chat config in Sentry's JavaScript SDK - DEV Community"
url: https://dev.to/zkasuran/bug-smash-restoring-dropped-gemini-chat-config-in-sentrys-javascript-sdk-2n9a
date: 2026-08-12
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:43:13.717062
---

# Bug Smash: restoring dropped Gemini chat config in Sentry's JavaScript SDK - DEV Community

# Bug Smash: restoring dropped Gemini chat config in Sentry's JavaScript SDK

## Project Overview
- Sentry’s JavaScript SDK auto‑instrumented Google GenAI so each Gemini call appears as a span with model, generation config, and system instruction.
- A regression caused chat spans to lose the configuration, making traces incomplete.
- The fix is a targeted change in `@sentry/server-utils`, includes unit tests, and was verified against the live Gemini API.

## Bug Description & Root Cause
- The Google GenAI SDK creates a chat object with `chats.create({ model, config })`; the config includes temperature, top_p, top_k, max tokens, penalties, tool list, and system instruction.
- A previous refactor removed the `chats.create()` span, unintentionally discarding the captured config.
- The deep proxy that instruments the client re‑proxied the chat object but dropped the original arguments, so subsequent `chat.sendMessage()` and `chat.sendMessageStream()` spans lacked the config attributes.

## Code Changes
- Added `mergeChatCreateParams` helper to combine create‑time config with per‑message config, respecting the SDK’s precedence (`params.config ?? chat.config`).
- Modified the proxy to pass the original `chats.create()` arguments through to `instrumentMethod`.
- Updated `instrumentMethod` to build span attributes from the merged parameters.
- No changes to the actual request sent to Google; non‑chat calls remain untouched.

## Tests & Validation
- New test file with four cases:
  1. Config attached to `sendMessage` spans.
  2. Config attached to `sendMessageStream` spans.
  3. Per‑message config overriding create‑time config.
  4. No config leakage to `models.generateContent` spans.
- Before the fix, three cases failed (attributes undefined); after the fix, all pass.
- Test suite grew from 38 files / 335 tests to 39 files / 339 tests, all passing.
- Linting and type checks run cleanly; only pre‑existing unrelated type errors remain.

## Impact on Sentry Usage
- Restores full AI tracing reliability: `gen_ai.*` span attributes now include temperature, token limits, and system instructions.
- Enables developers to answer “what config was this call running with?” when debugging poor responses or cost spikes.
- Aligns chat spans with non‑chat `generateContent` spans, providing a consistent view of model configuration.

## Impact on Google AI Integration
- Demonstrated with a real Gemini‑2.5‑flash call (no mocks):
  - **Before fix:** only `gen_ai.request.model` present; all other config attributes missing.
  - **After fix:** all config attributes (temperature, top_p, top_k, max_tokens, system_instructions) correctly recorded.
- The model response itself remains unchanged; the difference is purely in trace completeness.

## AI Disclosure
- AI assistance (Claude, Anthropic) was used for developing the change.
- Design, review, and verification were performed by the author.
- Final verification steps included running the full Sentry test suite, linting, type checking, and a live Gemini `chats.create` + `sendMessage` run to confirm attribute presence.