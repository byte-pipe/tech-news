---
title: Friends Don't Let Friends Use Ollama | Sleeping Robots
url: https://sleepingrobots.com/dreams/stop-using-ollama/
site_name: hackernews_api
content_file: hackernews_api-friends-dont-let-friends-use-ollama-sleeping-robot
fetched_at: '2026-04-16T11:58:50.247499'
original_url: https://sleepingrobots.com/dreams/stop-using-ollama/
author: Zetaphor
date: '2026-04-16'
published_date: '2026-04-15T00:00:00.000Z'
description: Ollama gained traction by being the first easy llama.cpp wrapper, then spent years dodging attribution, misleading users, and pivoting to cloud, all while riding VC money earned on someone else's engine. Here's the full history, and why the alternatives are better.
tags:
- hackernews
- trending
---

Ollama is the most popular way to run local LLMs. It shouldn’t be. It gained that position by being first, the first tool that madellama.cppaccessible to people who didn’t want to compile C++ or write their own server configs. That was a real contribution, briefly. But the project has since spent years systematically obscuring where its actual technology comes from, misleading users about what they’re running, and drifting from the local-first mission that earned it trust in the first place. All while taking venture capital money.

This isn’t a “both sides” piece. I’ve used Ollama. I’ve moved on. Here’s why you should too.

## A llama.cpp Wrapper With Amnesia

Ollama’s entire inference capability comes fromllama.cpp, the C++ inference engine created by Georgi Gerganov in March 2023. Gerganov’s project is what made it possible to run LLaMA models on consumer laptops at all, he hacked together the first versionin an evening, and it kicked off the entire local LLM movement. Today llama.cpp has over 100,000 stars on GitHub, 450+ contributors, and is the foundation that nearly every GGUF-based tool depends on.

Ollama was founded in 2021 by Jeffrey Morgan and Michael Chiang, both previously behindKitematic, a Docker GUI that was acquired by Docker Inc. They went through Y Combinator’s Winter 2021 batch, raised pre-seed funding, and launched publicly in 2023. From day one, the pitch was “Docker for LLMs”, a convenient wrapper that downloads and runs models with a single command. Under the hood, it was llama.cpp doing all the work.

For over a year, Ollama’s README containedno mention of llama.cpp. Not in the README, not on the website, not in their marketing materials. The project’s binary distributionsdidn’t include the required MIT license noticefor the llama.cpp code they were shipping. This isn’t a matter of open-source etiquette, the MIT license has exactly one major requirement: include the copyright notice. Ollama didn’t.

The community noticed.GitHub issue #3185was opened in early 2024 requesting license compliance. It wentover 400 days without a response from maintainers. Whenissue #3697was opened in April 2024 specifically requesting llama.cpp acknowledgment, community PR#3700followed within hours. Ollama’s co-founder Michael Chiang eventuallyadded a single lineto the bottom of the README: “llama.cpp project founded by Georgi Gerganov.”

The response to the PR was revealing. Ollama’s team wrote: “We spend a large chunk of time fixing and patching it up to ensure a smooth experience for Ollama users… Overtime, we will be transitioning to more systematically built engines.” Translation: we’re not going to give llama.cpp prominent credit, and we plan to distance ourselves from it anyway.

As oneHacker News commenterput it: “I’m continually puzzled by their approach, it’s such self-inflicted negative PR. Building on llama is perfectly valid and they’re adding value on ease of use here. Just give the llama team proper credit.” Another: “The fact that Ollama has been downplaying their reliance on llama.cpp has been known in the local LLM community for a long time.”

## The Fork That Made Things Worse

In mid-2025, Ollama followed through on that distancing. They moved away from using llama.cpp as their inference backend and built a custom implementation directly on top ofggml, the lower-level tensor library that llama.cpp itself uses. Their stated reason was stability, llama.cpp moves fast and breaks things, and Ollama’s enterprise partners need reliability.

The result was the opposite. Ollama’s custom backendreintroduced bugs that llama.cpp had solved years ago. Community members flagged broken structured output support, vision model failures, and GGML assertion crashes across multiple versions. Models that worked fine in upstream llama.cppfailed in Ollama, including new releases like GPT-OSS 20B, where Ollama’s implementation lacked support for tensor types that the model required. Georgi Gerganov himselfidentifiedthat Ollama had forked and made bad changes to GGML.

The irony is thick. They downplayed their dependence on llama.cpp for years, then when they finally tried to go it alone, they produced an inferior version of the thing they refused to credit.

Benchmarks tell the story. Multiple community tests show llama.cpp running1.8x faster than Ollamaon the same hardware with the same model, 161 tokens per second versus 89. On CPU, the gap is30-50%. Arecent comparison on Qwen-3 Coder 32Bshowed ~70% higher throughput with llama.cpp. The performance overhead comes from Ollama’s daemon layer, poor GPU offloading heuristics, and a vendored backend that trails upstream.

## Misleading Model Naming

When DeepSeek released its R1 model family in January 2025, Ollama listed the smaller distilled versions, models like DeepSeek-R1-Distill-Qwen-32B, which are fine-tuned Qwen and Llama models, not the actual 671-billion-parameter R1,simply as “DeepSeek-R1”in their library and CLI. Runningollama run deepseek-r1pulls an 8B Qwen-derived distillate that behaves nothing like the real model.

This wasn’t an oversight. DeepSeek themselves named these models with the “R1-Distill” prefix. Hugging Face listed them correctly. Ollama stripped the distinction. The result was a flood of social media posts from people claiming they were running “DeepSeek-R1” on consumer hardware, followed by confusion about why it performed poorly,doing reputational damage to DeepSeekin the process.

GitHub issues#8557and#8698requested separation of the models. Both were closed as duplicates with no fix. As of today,ollama run deepseek-r1still launches a tiny distilled model. Ollama knew the difference and chose to obscure it, presumably because “DeepSeek-R1” drives more downloads than “DeepSeek-R1-Distill-Qwen-32B” does.

## The Closed-Source App

In July 2025, Ollamareleased a GUI desktop appfor macOS and Windows. The app was developed in a private repository (github.com/ollama/app), shipped without a license, and the source code wasn’t publicly available. For a project that had built its reputation on being open-source, this was a jarring move.

Community membersimmediately raised concerns. The license issue received 40 upvotes. Developers foundpotential AGPL-3.0 dependenciesin the binary. The website placed the download button next to a GitHub link, giving the impression users were downloading the MIT-licensed open-source tool when they were actually getting an unlicensed closed-source application. Maintainers were silent for months. The code was eventuallymerged into the main repoin November 2025, but the initial rollout revealed where the project’s instincts lie.

AsXDA put it: “If your project trades on being open source, you do not get to be vague about what is and is not open at launch.”

## The Modelfile: Reinventing a Solved Problem

GGUF, the model format created by Georgi Gerganov, was designed withone core principle: single-file deployment. Bullet point #1 in the GGUF spec reads: “Full information: all information needed to load a model is contained in the model file, and no additional information needs to be provided by the user.” Chat templates, stop tokens, model metadata, it’s all embedded in the file. You point llama.cpp at a GGUF and it works.

Ollama added the Modelfile on top of this. It’s a separate configuration file, inspired by Dockerfiles, naturally, that specifies the base model, chat template, system prompt, sampling parameters, and stop tokens. Most of this information already exists inside the GGUF file. Asone Hacker News commenterput it: “We literally just got rid of that multi-file chaos only for Ollama to add it back.”

The problems with this approach compound quickly. Ollama onlyauto-detects chat templates it already knows aboutfrom a hardcoded list. If a GGUF file has a valid Jinja chat template embedded in its metadata but it doesn’t match one of Ollama’s known templates, Ollama falls back to a bare{{ .Prompt }}template, silently breaking the model’s instruction format. The user has to manually extract the chat template from the GGUF, translate it into Go template syntax (which is different from Jinja), and write it into a Modelfile. Meanwhile, llama.cpp reads the embedded template and just uses it.

Modifying parameters is worse. If you want to change the temperature or system prompt on a model you pulled from Ollama’s registry, the workflow is: export the Modelfile withollama show --modelfile, edit it, then runollama createto build a new model entry. Usershave reportedthat this process copies the entire model, 30 to 60 GB, to change one parameter. As one user described it: “The ‘modelfile’ workflow is a pain in the booty. It’s a dogwater pattern and I hate it. Some of these models are 30 to 60GB and copying the entire thing to change one parameter is just dumb.”

Compare this to llama.cpp, where parameters are command-line flags. Want a different temperature? Pass--temp 0.7. Different system prompt? Pass it in the API request. No files to create, no gigabytes to copy, no proprietary format to learn.

The Modelfile also locks users into Ollama’s Go template syntax, which isa different language from the Jinja templatesthat model creators actually publish. LM Studio accepts Jinja templates directly. llama.cpp reads them from the GGUF. Only Ollama requires you to translate between template languages, and gets it wrong often enough thatentire GitHub issuesare dedicated to mismatched templates between Ollama’s library and the upstream GGUF metadata.

## The Registry Bottleneck

When a new model drops, say a new Qwen, Gemma, or DeepSeek variant, GGUFs typically appear on Hugging Face within hours, quantized by community members like Unsloth or Bartowski. With llama.cpp, you can run them immediately:llama-server -hf unsloth/Qwen3.5-35B-A3B-GGUF:Q4_K_M. One command, straight from Hugging Face, no intermediary.

With Ollama, you wait. Someone at Ollama has to package the model for their registry, choose which quantizations to offer (typicallyjust Q4_K_M and Q8_0, no Q5, Q6, or IQ quants), convert the chat template to Go format, and push it. Until then, the model doesn’t exist in Ollama’s world unless you do the Modelfile dance yourself.

This creates arecurring pattern on r/LocalLLaMA: new model launches, people try it through Ollama, it’s broken or slow or has botched chat templates, and the model gets blamed instead of the runtime. A recent PSA post titled “If you want to test new models, use llama.cpp/transformers/vLLM/SGLang” documented how Qwen models showed problems with tool calls and garbage responses that “only happen with Ollama” due to their vendored backend and broken template handling. As one commenter put it: “Friends don’t let friends use ollama.”

The quantization limitation is particularly frustrating. Ollamaonly supports creating Q4_K_S, Q4_K_M, Q8_0, F16, and F32 quantizations. If you need Q5_K_M, Q6_K, or any IQ quant, formats that llama.cpp has supported for years, you’re out of luck unless you do the quantization yourself outside of Ollama. When a userasked about Q2_K support, the response was effectively “use a different tool.” For a project that markets itself as the easy way to run models, telling users to go elsewhere for basic quantization options is telling.

Ollama eventually addedollama run hf.co/{repo}:{quant}to pull directly from Hugging Face, which partially addresses the availability problem. But even then, the file gets copied into Ollama’s hashed blob storage, you still can’t share the GGUF with other tools, and the template detection issues still apply. The fundamental architecture remains: Ollama inserts itself as a middleman between you and your models, and that middleman is slower, less capable, and less compatible than the tools it sits on top of.

## The Cloud Pivot

In late 2025, Ollama introduced cloud-hosted models alongside its local library. The tool that was synonymous with local, private inferencestarted routing prompts to third-party cloud providers. Proprietary models like MiniMax appeared in the model list without clear disclosure that selecting them would send your data off-machine.

Usersraised concerns about data routing, when you run a closed-source model like MiniMax-m2.7 through “Ollama Cloud,” your prompts may be forwarded to the external provider who actually hosts the model. Ollama’s own documentation says “we process your prompts and responses to provide the service but do not store or log that content,” but says nothing about what the third-party provider does with it. For models hosted by Alibaba Cloud,users noted there is no zero-data-retention guarantee.

This was compounded byCVE-2025-51471, a token exfiltration vulnerability that affects all Ollama versions. A malicious registry server can trick Ollama into sending its authentication token to an attacker-controlled endpoint during a normal model pull. The fix exists as a PR but took months to land. In a tool that built its brand on local privacy, a vulnerability that leaks credentials to arbitrary servers is not a minor issue, it’s an architectural philosophy problem.

## The VC Pattern

All of this makes more sense when you look at the incentive structure. Ollama is a Y Combinator-backed (W21) startup, founded by engineers who previously built a Docker GUI that was acquired by Docker Inc. The playbook is familiar: wrap an existing open-source project in a user-friendly interface, build a user base, raise money, then figure out monetization.

The progression follows the pattern cleanly:

1. Launch on open source, build on llama.cpp, gain community trust
2. Minimize attribution, make the product look self-sufficient to investors
3. Create lock-in, proprietary model registry format, hashed filenames that don’t work with other tools
4. Launch closed-source components, the GUI app
5. Add cloud services, the monetization vector

The model registry is worth examining. Ollama stores downloaded models using hashed filenames in its own format. If you’ve been pulling models through Ollama for months, you can’t just point llama.cpp or LM Studio at those files without extra work. You can bring your own GGUFs to Ollama via a Modelfile, but it’s deliberately friction-filled to take them out. This is a form of vendor lock-in that most users don’t notice until they try to leave.

## What To Use Instead

The tools Ollama wraps are directly accessible, and they’re not much harder to set up.

llama.cppis the engine. It has an OpenAI-compatible API server (llama-server), a built-in web UI, full control over context windows and sampling parameters, and consistently better throughput than Ollama. In February 2026, Gerganov’s ggml.aijoined Hugging Faceto ensure the long-term sustainability of the project. It’s truly community-driven, MIT-licensed, and under active development with 450+ contributors.

llama-swaphandles multi-model orchestration, loading, unloading, and hot-swapping models on demand behind a single API endpoint. Pair it withLiteLLMand you get a unified OpenAI-compatible proxy that routes across multiple backends with proper model aliasing.

LM Studiogives you a GUI if that’s what you want. It uses llama.cpp under the hood, exposes all the knobs, and supports any GGUF model without lock-in.Janis another open-source desktop app with a clean chat interface and local-first design.Mstyoffers a polished GUI with multi-model support and built-in RAG.koboldcppis another option with a web UI and extensive configuration options.

Red Hat’sramalamais worth a look too, a container-native model runner thatexplicitly credits its upstream dependenciesfront and center. Exactly what Ollama should have done from the start.

None of these tools require more than a few minutes to set up. The idea that Ollama is the only accessible option hasn’t been true for a long time.

## The Bigger Picture

Georgi Gerganov hacked together llama.cpp in an evening in March 2023 and kicked off a revolution in local AI. He and a community of hundreds of contributors have spent years making it possible to run increasingly powerful models on consumer hardware. That work is genuinely important, it’s the foundation that keeps local inference open and accessible.

Ollama wrapped that work in a nice CLI, raised VC money on the back of it, spent over a year refusing to credit it, forked it badly, shipped a closed-source app alongside it, and then pivoted the whole thing toward cloud services. At every decision point where they could have been good open-source citizens, they chose the path that made them look more self-sufficient to investors.

The local LLM ecosystem doesn’t need Ollama. It needs llama.cpp. The rest is packaging, and better packaging already exists.