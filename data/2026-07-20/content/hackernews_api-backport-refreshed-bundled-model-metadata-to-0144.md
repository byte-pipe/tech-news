---
title: 'Backport refreshed bundled model metadata to 0.144 by sayan-oai · Pull Request #33972 · openai/codex · GitHub'
url: https://github.com/openai/codex/pull/33972/files
site_name: hackernews_api
content_file: hackernews_api-backport-refreshed-bundled-model-metadata-to-0144
fetched_at: '2026-07-20T11:58:02.883543'
original_url: https://github.com/openai/codex/pull/33972/files
author: AmazingTurtle
date: '2026-07-19'
description: Summary Backport d26a9bf671b1c03aabfc32e1092d137c1feb3962 to the 0.144 release line. Refresh bundled GPT-5.6 model instructions and context-window metadata. Refresh reasoning-summary, skills, permissions, and auto-review catalog metadata. Why The catalog refresh has propagated to public main, but stable 0.144 clients still bundle the older model metadata. This backport makes the refresh available in the next non-alpha 0.144.x hotfix. The release branch's existing supports_reasoning_summaries values were preserved while adding supports_reasoning_summary_parameter from the source commit. Validation just test -p codex-models-manager (40 passed) jq empty codex-rs/models-manager/models.json Verified GPT-5.6 Sol does not include the ultrafast service tier
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 openai

 

/

codex

Public

* NotificationsYou must be signed in to change notification settings
* Fork15k
* Star99.9k

Add this suggestion to a batch that can be applied as a single commit.

This suggestion is invalid because no changes were made to the code.

Suggestions cannot be applied while the pull request is closed.

Suggestions cannot be applied while viewing a subset of changes.

Only one suggestion per line can be applied in a batch.

Add this suggestion to a batch that can be applied as a single commit.

Applying suggestions on deleted lines is not supported.

You must change the existing code in this line in order to create a valid suggestion.

Outdated suggestions cannot be applied.

This suggestion has been applied or marked resolved.

Suggestions cannot be applied from pending reviews.

Suggestions cannot be applied on multi-line comments.

Suggestions cannot be applied while the pull request is queued to merge.

Suggestion cannot be applied right now. Please check back later.