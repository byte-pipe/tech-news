---
title: Changelog | OpenAI API
url: https://developers.openai.com/api/docs/changelog
site_name: hackernews_api
content_file: hackernews_api-changelog-openai-api
fetched_at: '2026-04-25T08:21:37.778346'
original_url: https://developers.openai.com/api/docs/changelog
author: arabicalories
date: '2026-04-25'
description: See all of the latest features and updates to the OpenAI API.
tags:
- hackernews
- trending
---

# Changelog

Upcoming deprecations can be found on the
 
deprecations page
.

### April, 2026

Apr 24
Feature
gpt-5.5
gpt-5.5-pro
v1/responses
v1/chat/completions
v1/batch

ReleasedGPT-5.5, a new frontier model for complex professional work, to the Chat Completions and Responses API, and releasedGPT-5.5 profor Responses API requests for tougher problems that benefit from more compute.

GPT-5.5 supports a 1M token context window, image input, structured outputs, function calling, prompt caching, Batch, tool search, built-in computer use, hosted shell, apply patch, Skills, MCP, and web search. Key updates include:

* Reasoning effort now defaults tomedium.
* Whenimage_detailis unset or set toauto, the model now usesoriginal behavior.
* Caching for GPT-5.5 only works with extended prompt caching. In-memory prompt caching is not supported.
Learn morehere.
Apr 21
Feature
gpt-image-2
v1/images/generations
v1/images/edits
v1/batch

ReleasedGPT Image 2, a state-of-the-art image generation model for image generation and editing. GPT Image 2 supports flexible image sizes, high-fidelity image inputs, token-based image pricing, and Batch API support with a 50% discount.

Apr 15
Update

Updated theAgents SDKwith new capabilities, including:

* running agents in controlled sandboxes;
* inspecting and customizing the open-source harness; and
* controlling when memories are created and where they're stored.

### March, 2026

Mar 17
Feature
gpt-5.4-mini
gpt-5.4-nano
v1/responses
v1/chat/completions

ReleasedGPT-5.4 miniandGPT-5.4 nanoto the Chat Completions and Responses API. GPT-5.4 mini brings GPT-5.4-class capabilities to a faster, more efficient model for high-volume workloads, while GPT-5.4 nano is optimized for simple high-volume tasks where speed and cost matter most.

GPT-5.4 mini supportstool search, built-incomputer use, andcompaction. GPT-5.4 nano supports compaction, but does not support tool search or computer use.

Mar 16
Update
gpt-5.3-chat-latest

Updated thegpt-5.3-chat-latestslug to point to the latest model currently used in ChatGPT.

Mar 13
Fix
gpt-5.4
v1/responses
v1/chat/completions

Updated our image encoder to fix a small bug withinput_imageinputs in GPT-5.4. Some image understanding use cases may now see improved quality. No action is required.

Mar 12
Feature
sora-2
sora-2-pro
v1/videos
v1/videos/characters
v1/videos/extensions
v1/batch

Expanded the Sora API with reusable character references, longer generations up to20seconds,1080poutput forsora-2-pro, video extensions, and Batch API support forPOST /v1/videos.1080pgenerations onsora-2-proare billed at$0.70per second. Learn morehere.

Mar 12
Update
sora-2
sora-2-pro
v1/videos/edits
v1/videos/{video_id}/remix

AddedPOST /v1/videos/editsfor editing existing videos. This will replacePOST /v1/videos/{video_id}/remix, which will be deprecated in6months. Learn morehere.

Mar 5
Feature
gpt-5.4
gpt-5.4-pro
v1/responses
v1/chat/completions

ReleasedGPT-5.4, our newest frontier model for professional work, to the Chat Completions and Responses API, and releasedGPT-5.4 proto the Responses API for tougher problems that benefit from more compute.

Also released:

* Tool searchin the Responses API, which lets models defer large tool surfaces until runtime to reduce token usage, preserve cache performance, and improve latency.
* Built-inComputer usesupport in GPT-5.4 through the Responses APIcomputertool for screenshot-based UI interaction.
* A 1M token context window and nativeCompactionsupport for longer-running agent workflows.
Mar 3
Feature
gpt-5.3-chat-latest
v1/chat/completions
v1/responses

Releasedgpt-5.3-chat-latestto the Chat Completions and Responses API. This model points to the GPT-5.3 Instant snapshot currently used in ChatGPT. Read morehere.

### February, 2026

Feb 24
Feature
v1/responses
v1/chat/completions

Expandedinput_filesupport to accept more document, presentation, spreadsheet, code, and text file types. Learn morehere.

Feb 24
Feature
v1/responses

Releasedphaseto the Responses API. It labels an assistant message as intermediate commentary (commentary) or the final answer (final_answer). Read morehere.

Feb 24
Feature
gpt-5.3-codex
v1/responses

Releasedgpt-5.3-codexto the Responses API. Read morehere.

Feb 23
Feature
v1/responses

Launched WebSocket mode for the Responses API. Learn morehere.

Feb 23
Feature
gpt-realtime-1.5
gpt-audio-1.5
v1/realtime
v1/chat/completions

Releasedgpt-realtime-1.5to the Realtime API. Read morehere.

Releasedgpt-audio-1.5to the Chat Completions API. Read morehere.

Feb 10
Feature
gpt-image-1.5
gpt-image-1
gpt-image-1-mini
chatgpt-image-latest
v1/batch

Batch APIis now supported for GPT Image models:gpt-image-1.5,chatgpt-image-latest,gpt-image-1, andgpt-image-1-mini.

Feb 10
Update
gpt-5.2-chat-latest

Updated thegpt-5.2-chat-latestslug to point to the latest model currently used in ChatGPT.

Feb 10
Feature
v1/responses

Launchedserver-side compactionin the Responses API.

Feb 10
Feature
v1/responses

Launched support forSkillsin the Responses API. We support Skills across both local execution and hosted container-based execution.

Feb 10
Feature
v1/responses

Launched a newHosted Shelltool, as well as support for networking in containers.

Feb 9
Feature
gpt-image-1.5
gpt-image-1
gpt-image-1-mini
chatgpt-image-latest
v1/images/edits

Added support forapplication/jsonrequests on/v1/images/editsfor GPT image models. JSON requests useimages(and optionalmask) withimage_urlorfile_idreferences instead of multipart uploads.

Feb 3
Update
gpt-5.2
gpt-5.2-codex

We have optimized our inference stack for API customers andGPT-5.2andGPT-5.2-Codexnow run ~40% faster. Model and model weights are unchanged.

### January, 2026

Jan 15
Announcement

AnnouncedOpen Responses: an open-source spec for building multi-provider, interoperable LLM interfaces built on top of the original OpenAI Responses API.

Jan 14
Feature
gpt-5.2-codex
v1/responses

Releasedgpt-5.2-codexto the Responses API. GPT-5.2-Codex is a version of GPT-5.2 optimized for agentic coding tasks in Codex or similar environments. Read morehere.

Jan 13
Feature
v1/realtime

Added dedicated SIP IP ranges for Realtime API.sip.api.openai.comdoes GeoIP routing, and will direct SIP traffic to the closest region.Learn more.

Jan 13
Update
gpt-realtime-mini
gpt-audio-mini

Updated thegpt-realtime-miniandgpt-audio-minislugs to point to the 2025-12-15 snapshots. If you need the previous model snapshots, usegpt-realtime-mini-2025-10-06andgpt-audio-mini-2025-10-06.

Jan 13
Update
sora-2

Updated thesora-2slug to point tosora-2-2025-12-08. If you need the previous model snapshot, usesora-2-2025-10-06.

Jan 13
Update
gpt-4o-mini-tts
gpt-4o-mini-transcribe

Updated thegpt-4o-mini-ttsandgpt-4o-mini-transcribeslugs to point to the2025-12-15snapshots. If you need the previous model snapshots, usegpt-4o-mini-tts-2025-03-20andgpt-4o-mini-transcribe-2025-03-20. We currently recomend usinggpt-4o-mini-transcribeovergpt-4o-transcribefor the best results.

Jan 9
Fix
gpt-image-1.5
chatgpt-image-latest

Fixed an issue wheregpt-image-1.5andchatgpt-image-latestwere incorrectly using high fidelity for image edits through/v1/images/edits, even whenfidelitywas explicitly set tolow(the default).

### December, 2025

Dec 19
Update
gpt-image-1.5
chatgpt-image-latest

Addedgpt-image-1.5andchatgpt-image-latestto the Responses API image generation tool.

Dec 16
Feature
gpt-image-1.5
chatgpt-image-latest

Releasedgpt-image-1.5andchatgpt-image-latest, our latest and most advanced models for image generation. Read morehere.

Dec 15
Feature
gpt-realtime-mini
gpt-audio-mini
gpt-4o-mini-transcribe
gpt-4o-mini-tts

Released four new dated audio snapshots. These updates deliver reliability, quality, and voice fidelity improvements for real-time, voice-driven applications. Read morehere.

* gpt-realtime-mini-2025-12-15
* gpt-audio-mini-2025-12-15
* gpt-4o-mini-transcribe-2025-12-15
* gpt-4o-mini-tts-2025-12-15

This launch also includes support forCustom voicesfor eligible customers.

Dec 11
Feature
gpt-5.2
gpt-5.2-chat-latest
v1/responses
v1/chat/completions

ReleasedGPT-5.2, the newest flagship model in the GPT-5 model family. GPT-5.2 shows improvements over the previous GPT-5.1 in:

* General intelligence
* Instruction following
* Accuracy and token efficiency
* Multimodality—especially vision
* Code generation—especially front-end UI creation
* Tool calling and context management in the API
* Spreadsheet understanding and creation.

What's new in 5.2 is a new xhigh reasoning effort level, concise reasoning summaries, and new context management using compaction.

Dec 11
Feature
v1/responses/compact

Releasedclient-side compaction. For long-running conversations with the Responses API, you can use the/responses/compactendpoint to shrink the context you send with each turn.

Dec 4
Feature
gpt-5.1-codex-max
v1/responses

Releasedgpt-5.1-codex-maxto the Responses API. GPT-5.1-Codex is our most intelligent coding model optimized for long-horizon, agentic coding tasks. Read morehere.

### November, 2025

Nov 20
Feature
v1/realtime

Added support for DTMF key presses in the Realtime API. You can now receive DTMF events while using a Realtime sideband connection. Seedocs herefor more information.

Nov 13
Feature
gpt-5.1
gpt-5.1-codex
gpt-5.1-chat-latest
gpt-5.1-codex-mini
v1/responses
v1/chat/completions

ReleasedGPT-5.1, the newest flagship model in the GPT-5 model family. GPT-5.1 is trained to be especially proficient in:

* Steerability and faster responses when less thinking's required
* Code generation and coding use cases
* Agentic workflows

Note that GPT-5.1 defaults to a newnonereasoning setting for faster responses when less thinking's required—different from the previousmediumdefault setting in GPT-5.

Nov 13
Feature

Releasedenhanced role-based access controls (RBAC). Role-based access control (RBAC) lets you decide who can do what across your organization and projects—both through the API and in the Dashboard.

Nov 13
Feature
gpt-5.1-codex
gpt-5.1-codex-mini
v1/responses

Releasedgpt-5.1-codexandgpt-5.1-codex-minito the Responses API. GPT-5.1-Codex is a version of GPT-5.1 optimized for agentic coding tasks in Codex or similar environments. Read morehere.

Nov 13
Feature

Releasedextended prompt cache retention. Extended prompt cache retention keeps cached prefixes active for longer, up to a maximum of 24 hours. Extended Prompt Caching works by offloading the key/value tensors to GPU-local storage when memory is full, significantly increasing the storage capacity available for caching.

### October, 2025

Oct 29
Feature
gpt-oss-safeguard-120b
gpt-oss-safeguard-20b

gpt-oss-safeguard-120b and gpt-oss-safeguard-20b are safety reasoning models built-upon gpt-oss. Read morehere.

Oct 24
Feature

ReleasedEnterprise Key Management (EKM). Enterprise Key Management (EKM) allows you to encrypt your customer content at OpenAI using keys managed by your own external Key Management System (KMS).

Oct 24
Feature

ReleasedUK data residency.

Oct 6
Feature
gpt-5-pro
gpt-realtime-mini
gpt-audio-mini
gpt-image-1-mini
sora-2
sora-2-pro
v1/responses
v1/batch
v1/chat/completions
v1/videos
v1/realtime
v1/images/generations

Released several new features atOpenAI DevDay:

Releasedgpt-5-pro, a version ofGPT-5that uses more compute to think harder and provide consistently better answers.

Releasedgpt-realtime-miniandgpt-audio-minifor more cost-efficient speech to speech performance.

Releasedgpt-image-1-minifor more cost-efficient image generation and editing.

Launchedv1/videosfor rich, detailed, and dynamic video generation and remixing with our latestSora 2andSora 2 Promodels.

LaunchedAgent Builderfor visually creating custom multi-agent workflows.

LaunchedChatKit, an embeddable chat interface for deploying agents.

ReleasedTrace Evals, Datasets, and Prompt Optimization tools.

Evals: Released Third-Party Model Support.

LaunchedService health dashboard.

Oct 1
Feature

ReleasedIP allowlist. IP allowlisting restricts API access to only the IP addresses or ranges you specify.

### September, 2025

Sep 26
Feature
v1/responses

Added support for image and file as atool call outputin Responses API.

Sep 23
Feature
gpt-5-codex
v1/responses

Launched special-purpose modelgpt-5-codex, built and optimized for use with theCodex CLI.

### August, 2025

Aug 28
Feature
v1/realtime

The OpenAI Realtime API is now generally available. Learn morein our Realtime API guide.

Aug 21
Feature
v1/responses

Added support forconnectorsto the Responses API. Connectors are OpenAI-maintained MCP wrappers for popular services like Google apps, Dropbox, and more that can be used to give model read access to data stored in those services.

Aug 20
Feature
v1/conversations
v1/responses
v1/assistants

Released the Conversations API, which allows you to create and manage long-running conversations with the Responses API. See themigration guideto see a side-by-side comparison and learn how to migrate from an Assistants API integration to Responses and Conversations.

Aug 7
Feature
v1/chat/completions
v1/responses

Released GPT-5 family of models in the API, includinggpt-5,gpt-5-mini, andgpt-5-nano.

Introduced theminimalreasoning effortvalue to optimize for fast responses in GPT-5 models (which support reasoning).

Introducedcustomtool calltype, which allows for freeform inputs to and outputs from the model when tool calling.

### June, 2025

Jun 27
Feature

Launched support forPriority processing. Priority processing delivers significantly lower and more consistent latency compared to Standard processing while keeping pay-as-you-go flexibility.

Jun 24
Feature
o3-deep-research
o3-deep-research-2025-06-26
o4-mini-deep-research
o4-mini-deep-research-2025-06-26
v1/responses

Releasedo3-deep-researchando4-mini-deep-research, deep research variants of our o-series reasoning models optimized for deep analysis and research tasks. Learn more in thedeep research guide.

Added support for async event handling withwebhooks.Reduced and simplified pricingfor the web search tool. Added support for theweb search tool.

Jun 13
Feature
v1/responses

New reusable promptsare now available in the dashboard andResponses API. Via API, you can now reference templates created in the dashboard via thepromptparameter (with a promptid, optionalversion) and supply dynamicvariablesthat can include strings, images, or file inputs. Reusable prompts are not available in Chat Completions.Learn more.

Jun 10
Feature
o3-pro
v1/responses
v1/batch

Releasedo3-pro, a version of theo3reasoning model that uses more compute to answer hard problems with better reasoning and consistency.Prices for the o3 model have also been reducedfor all API requests, including batch and flex processing.

Jun 4
Feature
v1/fine_tuning

Added fine-tuning support withdirect preference optimizationfor the modelsgpt-4.1-2025-04-14,gpt-4.1-mini-2025-04-14, andgpt-4.1-nano-2025-04-14.

Jun 3
Feature
v1/chat/completions
v1/realtime

New model snapshots available forgpt-4o-audio-previewandgpt-4o-realtime-preview. ReleasedAgents SDK for TypeScript.

### May, 2025

May 20
Feature
v1/responses

Added support for new built-in tools in the Responses API, includingremote MCP serversandcode interpreter.Learn more about tools.

May 20
Feature
v1/responses
v1/chat/completions

Added support for usingstrictmode for tool schemas when using parallel tool calling with non-fine-tuned models.
Added newschema features, including string validation foremailand other patterns and specifying ranges for numbers and arrays.

May 15
Feature
codex-mini-latest
v1/responses
v1/chat/completions

Launchedcodex-mini-latestin the API, optimized for use with theCodex CLI.

May 7
Feature
v1/fine-tuning
v1/responses
v1/chat/completions

Launched support forreinforcement fine-tuning. Learn about availablefine-tuning methods.gpt-4.1-nanois now available for fine-tuning.

### April, 2025

Apr 30
Feature

Launched support forEnhanced API Budget Alerts & Auto-recharge Limits.

Apr 23
Feature
v1/images/generations
v1/images/edits

Added a new image generation model,gpt-image-1. This model sets a new standard for image generation, with improved quality and instruction following.

Updated the Image Generation and Edit endpoints to support new parameters specific to thegpt-image-1model.

Apr 16
Feature
v1/chat/completions
v1/responses

Added two new o-series reasoning models,o3ando4-mini. They set a new standard for math, science, and coding, visual reasoning tasks, and technical writing.

Launched Codex, our code generation CLI tool.

Apr 14
Feature
gpt-4.1
gpt-4.1-mini
gpt-4.1-nano
v1/responses
v1/chat/completions
v1/fine_tuning

Addedgpt-4.1,gpt-4.1-mini, andgpt-4.1-nanomodels to the API. These new models feature improved instruction following, coding, and a larger context window (up to 1M tokens).gpt-4.1andgpt-4.1-miniare available for supervised fine-tuning. Announced deprecation ofgpt-4.5-preview.

### March, 2025

Mar 20
Update
v1/audio

Addedgpt-4o-mini-tts,gpt-4o-transcribe,gpt-4o-mini-transcribe, andwhisper-1models to the Audio API.

Mar 19
Feature
o1-pro
v1/responses
v1/batch

Releasedo1-pro, a version of theo1reasoning model that uses more compute to answer hard problems with better reasoning and consistency.

Mar 11
Feature
gpt-4o-search-preview
gpt-4o-mini-search-preview
computer-use-preview
v1/chat/completions
v1/assistants
v1/responses

Released several new models and tools and a new API for agentic workflows:

* Released theResponses API, a new API for creating and using agents and tools.
* Released a set of built-in tools for the Responses API:web search,file search, andcomputer use.
* Released theAgents SDK, an orchestration framework for designing, building, and deploying agents.
* Announced new models:gpt-4o-search-preview,gpt-4o-mini-search-preview,computer-use-preview.
* Announced plans to bring allAssistants APIfeatures to the easier to useResponses API, with an anticipated sunset date for Assistants in 2026 (after achieving full feature parity).
Mar 3
Feature
v1/fine_tuning/jobs

Addedmetadatafield support to fine-tuning jobs.

### February, 2025

Feb 27
Feature
GPT-4.5
v1/chat/completions
v1/assistants
v1/batch

Released a research preview ofGPT-4.5—our largest and most capable chat model yet. GPT-4.5's high "EQ" and understanding of user intent make it better at creative tasks and agentic planning.

Feb 25
Feature

Launched theAPI Usage Dashboard Update. This update addresses requests for additional data filters, such as project selection, date picker, and fine-grained intervals. There’s also better support for viewing usage across different products and service tiers.

Feb 5
Feature

Introducing data residency in Europe. Read morehere.

### January, 2025

Jan 31
Feature
o3-mini
o3-mini-2025-01-31
v1/chat/completions

Launchedo3-mini, a new small reasoning model that is optimized for science, math, and coding tasks.

Jan 21
Feature
o1

Expanded access too1 model. The o1 series of models are trained with reinforcement learning to perform complex reasoning.

### December, 2024

Dec 18
Feature

LaunchedAdmin API Key Rotations, enabling customers to programmatically rotate their admin api keys.

UpdatedAdmin API Invites, enabling customers to programmatically invite users to projects at the same time they are invited to organizations.

Dec 17
Feature
o1
gpt-4o
gpt-4o-mini
v1/fine_tuning
v1/chat/completions
v1/realtime

Added new models foro1,gpt-4o-realtime,gpt-4o-audioandmore.

Added WebRTC connection method for theRealtime API.

Addedreasoning_effortparameterfor o1 models.

Addeddevelopermessage rolefor o1 model. Note that o1-preview and o1-mini do not support system or developer messages.

Launched Preference Fine-tuning usingDirect Preference Optimization (DPO).

Launched beta SDKs for Go and Java.Learn more.

AddedRealtime APIsupport in thePython SDK.

Dec 4
Feature

LaunchedUsage API, enabling customers to programmatically query activities and spending across OpenAI APIs.

### November, 2024

Nov 20
Update
v1/chat/completions

Releasedgpt-4o-2024-11-20, our newest model in the gpt-4o series.

Nov 4
Feature
v1/chat/completions

ReleasedPredicted Outputs, which greatly reduces latency for model responses where much of the response is known ahead of time. This is most common when regenerating the content of documents and code files with only minor changes.

### October, 2024

Oct 30
Feature
gpt-4o-realtime-preview
gpt-4o-audio-preview
v1/chat/completions

Added five new voice types in theRealtime APIandChat Completions API.

Oct 17
Feature
gpt-4o-audio-preview
v1/chat/completions

Releasednewgpt-4o-audio-previewmodelfor chat completions, which supports both audio inputs and outputs. Uses the same underlying model as theRealtime API.

Oct 1
Feature
v1/realtime
v1/chat/completions
v1/fine_tuning

Released several new features atOpenAI DevDay in San Francisco:

Realtime API: Build fast speech-to-speech experiences into your applications using a WebSockets interface.

Model distillation: Platform for fine-tuning cost-efficient models with your outputs from a large frontier model.

Image fine-tuning: Fine-tune GPT-4o with images and text to improve vision capabilities.

Evals: Create and run custom evaluations to measure model performance on specific tasks.

Prompt caching: Discounts and faster processing times on recently seen input tokens.

Generate in playground: Easily generate prompts, function definitions, and structured output schemas in the playground using the Generate button.

### September, 2024

Sep 26
Feature
omni-moderation-latest
v1/moderations

Releasednewomni-moderation-latestmoderation model, which supports both images and text (for some categories), supports two new text-only harm categories, and has more accurate scores.

Sep 12
Feature
o1-preview
o1-mini
v1/chat/completions

Releasedo1-preview and o1-mini, new large language models trained with reinforcement learning to perform complex reasoning tasks.

### August, 2024

Aug 29
Feature
v1/assistants

Assistants API now supportsincluding file search results used by the file search tool, and customizing ranking behavior.

Aug 20
Feature
gpt-4o
v1/fine_tuning

GA release forgpt-4o-2024-08-06fine-tuning—all API users can now fine-tune the latest GPT-4o model.

Aug 15
Update
gpt-4o
v1/chat/completions

Releaseddynamic model forchatgpt-4o-latest—this model will point to the latest GPT-4o model used by ChatGPT.

Aug 6
Update

LaunchedStructured Outputs—model outputs now reliably adhere to developer supplied JSON Schemas.

Releasedgpt-4o-2024-08-06, our newest model in the gpt-4o series.

Aug 1
Update

LaunchedAdmin and Audit Log APIs, allowing customers to programmatically administer their organization and monitor changes using the audit logs. Audit logging must be enabled withinsettings.

### July, 2024

Jul 24
Update

Launchedself-serve SSO configuration, allowing Enterprise customers on custom and unlimited billing to set up authentication against their desired IDP.

Jul 23
Update

Launchedfine-tuning for GPT-4o mini, enabling even higher performance for specific use cases.

Jul 18
Update

ReleasedGPT-4o mini, our affordable an intelligent small model for fast, lightweight tasks.

Jul 17
Update

ReleasedUploadsto upload large files in multiple parts.

### June, 2024

Jun 6
Update

Parallel function callingcan be disabled in Chat Completions and the Assistants API by passingparallel_tool_calls=false.

.NET SDKlaunched in Beta.

Jun 3
Update

Added support forfile search customizations.

### May, 2024

May 15
Update

Added support forarchiving projects. Only organization owners can access this functionality.

Added support forsetting cost limitson a per-project basis for pay as you go customers.

May 13
Update

ReleasedGPT-4oin the API. GPT-4o is our fastest and most affordable flagship model.

May 9
Update

Added support forimage inputs to the Assistants API.

May 7
Update

Added support forfine-tuned models to the Batch API.

May 6
Update

Addedstream_options: {"include_usage": true}parameter to the Chat Completions and Completions APIs. Setting this gives developers access to usage stats when using streaming.

May 2
Update

Addeda new endpointto delete a message from a thread in the Assistants API.

### April, 2024

Apr 29
Update

Added a newfunction calling optiontool_choice: "required"to the Chat Completions and Assistants APIs.

Added aguide for the Batch APIand Batch API support forembeddings models

Apr 17
Update

Introduced aseries of updates to the Assistants API, including a new file search tool allowing up to 10,000 files per assistant, new token controls, and support for tool choice.

Apr 16
Update

Introducedproject based hierarchyfor organizing work by projects, including the ability to createAPI keysand manage rate and cost limits on a per-project basis (cost limits available only for Enterprise customers).

Apr 15
Update

ReleasedBatch API

Apr 9
Update

ReleasedGPT-4 Turbo with Visionin general availability in the API

Apr 4
Update

Added support forseedin the fine-tuning API

Added support forcheckpointsin the fine-tuning API

Added support foradding Messages when creating a Runin the Assistants API

Apr 1
Update

Added support forfiltering Messages by run_idin the Assistants API

### March, 2024

Mar 29
Update

Added support fortemperatureandassistant message creationin the Assistants API

Mar 14
Update

Added support forstreamingin the Assistants API

### February, 2024

Feb 9
Update

Addedtimestamp_granularitiesparameterto the Audio API

Feb 1
Update

Releasedgpt-3.5-turbo-0125, an updated GPT-3.5 Turbo model

### January, 2024

Jan 25
Update

Released embedding V3 models and an updated GPT-4 Turbo preview

Addeddimensionsparameterto the Embeddings API

### December, 2023

Dec 20
Update

Addedadditional_instructionsparameterto run creation in the Assistants API

Dec 15
Update

Addedlogprobsandtop_logprobsparametersto the Chat Completions API

Dec 14
Update

Changedfunction parametersargument on a tool call to be optional

### November, 2023

Nov 30
Update

ReleasedOpenAI Deno SDK

Nov 6
Update

ReleasedGPT-4 Turbo Preview,updated GPT-3.5 Turbo,GPT-4 Turbo with Vision,Assistants API,DALL·E 3 in the API, andtext-to-speech API

Deprecated the Chat Completionsfunctionsparameterin favor oftools

ReleasedOpenAI Python SDK V1.0

### October, 2023

Oct 16
Update

Addedencoding_formatparameterto the Embeddings API

Addedmax_tokensto theModeration models

Oct 6
Update

Addedfunction calling supportto the Fine-tuning API