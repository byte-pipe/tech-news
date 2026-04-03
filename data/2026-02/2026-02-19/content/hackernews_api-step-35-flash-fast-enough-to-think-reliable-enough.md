---
title: 'Step 3.5 Flash: Fast Enough to Think. Reliable Enough to Act.'
url: https://static.stepfun.com/blog/step-3.5-flash/
site_name: hackernews_api
content_file: hackernews_api-step-35-flash-fast-enough-to-think-reliable-enough
fetched_at: '2026-02-19T19:25:04.715511'
original_url: https://static.stepfun.com/blog/step-3.5-flash/
author: kristianp
date: '2026-02-19'
description: Step 3.5 Flash – Open-source foundation model, supports deep reasoning at speed
tags:
- hackernews
- trending
---

2026-02-12 updated · StepFun

# Step 3.5 Flash

|

 GitHub


 HuggingFace


 Tech Report

New

 ModelScope


 OpenClaw Guidance

🔥Hot

Score

82
80
78
76

81.0

Step 3.5 Flash

Params (B)

196

Avg Score

81.0

78.5

GLM-4.7

Params (B)

355

Avg Score

78.5

77.3

DeepSeek V3.2

Params (B)

671

Avg Score

77.3

80.5

Kimi K2.5

Params (B)

1000

Avg Score

80.5

80.7

Gemini 3.0 Pro

Params (B)

Unknown

Avg Score

80.7

80.6

Claude Opus 4.5

Params (B)

Unknown

Avg Score

80.6

82.2

GPT-5.2 xhigh

Params (B)

Unknown

Avg Score

82.2

200
400
600
800
1000
Likely >1000

Total Model Parameters (B)

Scores represent the mean of the following eight benchmarks listed below, excluding xbench-DeepSearch. The Step 3.5 Flash score is derived under standard settings (i.e., $w/o$ Parallel Thinking).

Step 3.5 Flashis our most capable open-source foundation model, engineered to deliver frontier reasoning and agentic capabilities with exceptional efficiency. Built on a sparse Mixture of Experts (MoE) architecture, it selectively activates only11B of its 196B parametersper token. This "intelligence density" allows it to rival the reasoning depth of top-tier proprietary models, while maintaining the agility required for real-time interaction.

* Deep Reasoning at Speed:While chatbots are built for reading, agents must reason fast. Powered by 3-way Multi-Token Prediction (MTP-3), Step 3.5 Flash achieves a generation throughput of 100–300 tok/s in typical usage (peaking at 350 tok/s for single-stream coding tasks). This allows for complex, multi-step reasoning chains with immediate responsiveness.
* A Robust Engine for Coding & Agents:Step 3.5 Flash is purpose-built for agentic tasks, integrating a scalable RL framework that drives consistent self-improvement. It achieves 74.4% on SWE-bench Verified and 51.0% on Terminal-Bench 2.0, proving its ability to handle sophisticated, long-horizon tasks with unwavering stability.
* Efficient Long Context:The model supports a cost-efficient 256K context window by employing a 3:1 Sliding Window Attention (SWA) ratio—integrating three SWA layers for every one full-attention layer. This hybrid approach ensures consistent performance across massive datasets or long codebases while significantly reducing the computational overhead typical of standard long-context models.
* Accessible Local Deployment:Optimized for accessibility, Step 3.5 Flash brings elite-level intelligence to local environments. It runs securely on high-end consumer hardware (e.g., Mac Studio M4 Max, NVIDIA DGX Spark), ensuring data privacy without sacrificing performance.

#### Reasoning

AIME 2025

100

90

80

97.3

Step 3.5 Flash

Score:
97.3

Params:
196B

99.9

Step 3.5 Flash (PaCoRe)

Score:
99.9

Params:
196B

95.7

GLM-4.7

Score:
95.7

Params:
355B

93.1

DeepSeek V3.2

Score:
93.1

Params:
671B

96.1

Kimi K2.5

Score:
96.1

Params:
1T

95.0

Gemini 3.0 Pro

Score:
95.0

Params:
Unknown

92.8

Claude Opus 4.5

Score:
92.8

Params:
Unknown

100.0

GPT-5.2 xhigh

Score:
100.0

Params:
Unknown

IMOAnswerBench

90

80

70

85.4

Step 3.5 Flash

Score:
85.4

Params:
196B

88.8

Step 3.5 Flash (PaCoRe)

Score:
88.8

Params:
196B

82.0

GLM-4.7

Score:
82.0

Params:
355B

78.3

DeepSeek V3.2

Score:
78.3

Params:
671B

81.8

Kimi K2.5

Score:
81.8

Params:
1T

83.3

Gemini 3.0 Pro

Score:
83.3

Params:
Unknown

84.0

Claude Opus 4.5

Score:
84.0

Params:
Unknown

86.3

GPT-5.2 xhigh

Score:
86.3

Params:
Unknown

HMMT 2025 (Avg. Feb and Nov)

100

90

80

96.2

Step 3.5 Flash

Score:
96.2

Params:
196B

98.9

Step 3.5 Flash (PaCoRe)

Score:
98.9

Params:
196B

95.3

GLM-4.7

Score:
95.3

Params:
355B

91.4

DeepSeek V3.2

Score:
91.4

Params:
671B

93.3

Kimi K2.5

Score:
93.3

Params:
1T

96.0

Gemini 3.0 Pro

Score:
96.0

Params:
Unknown

92.3

Claude Opus 4.5

Score:
92.3

Params:
Unknown

98.3

GPT-5.2 xhigh

Score:
98.3

Params:
Unknown

#### Coding

SWE-bench Verified

81

68

55

74.4

Step 3.5 Flash

Score:
74.4

Params:
196B

73.8

GLM-4.7

Score:
73.8

Params:
355B

73.1

DeepSeek V3.2

Score:
73.1

Params:
671B

76.8

Kimi K2.5

Score:
76.8

Params:
1T

76.2

Gemini 3.0 Pro

Score:
76.2

Params:
Unknown

80.9

Claude Opus 4.5

Score:
80.9

Params:
Unknown

80.0

GPT-5.2 xhigh

Score:
80.0

Params:
Unknown

Terminal-Bench 2.0

60

40

20

51.0

Step 3.5 Flash

Score:
51.0

Params:
196B

41.0

GLM-4.7

Score:
41.0

Params:
355B

46.4

DeepSeek V3.2

Score:
46.4

Params:
671B

50.8

Kimi K2.5

Score:
50.8

Params:
1T

54.2

Gemini 3.0 Pro

Score:
54.2

Params:
Unknown

59.3

Claude Opus 4.5

Score:
59.3

Params:
Unknown

54.0

GPT-5.2 xhigh

Score:
54.0

Params:
Unknown

LiveCodeBench-V6

91

83

75

86.4

Step 3.5 Flash

Score:
86.4

Params:
196B

88.9

Step 3.5 Flash (PaCoRe)

Score:
88.9

Params:
196B

84.9

GLM-4.7

Score:
84.9

Params:
355B

83.3

DeepSeek V3.2

Score:
83.3

Params:
671B

85.0

Kimi K2.5

Score:
85.0

Params:
1T

90.7

Gemini 3.0 Pro

Score:
90.7

Params:
Unknown

84.8

Claude Opus 4.5

Score:
84.8

Params:
Unknown

87.7

GPT-5.2 xhigh

Score:
87.7

Params:
Unknown

#### Agent

τ²-Bench

95

73

50

88.2

Step 3.5 Flash

Score:
88.2

Params:
196B

87.4

GLM-4.7

Score:
87.4

Params:
355B

85.2

DeepSeek V3.2

Score:
85.2

Params:
671B

85.4

Kimi K2.5

Score:
85.4

Params:
1T

90.7

Gemini 3.0 Pro

Score:
90.7

Params:
Unknown

92.5

Claude Opus 4.5

Score:
92.5

Params:
Unknown

85.5

GPT-5.2 xhigh

Score:
85.5

Params:
Unknown

BrowseComp (w/ Context Manager)

75

40

5

69.0

Step 3.5 Flash

Score:
69.0

Params:
196B

67.5

GLM-4.7

Score:
67.5

Params:
355B

67.6

DeepSeek V3.2

Score:
67.6

Params:
671B

74.9

Kimi K2.5

Score:
74.9

Params:
1T

59.2

Gemini 3.0 Pro

Score:
59.2

Params:
Unknown

57.8

Claude Opus 4.5

Score:
57.8

Params:
Unknown

65.8

GPT-5.2 xhigh

Score:
65.8

Params:
Unknown

xbench-DeepSearch (2025.10)

75

40

5

56.3

Step 3.5 Flash

Score:
56.3

Params:
196B

35.0

StepFun Research

Score:
35.0

Params:
Unknown

40.0

Kimi K2.5 (Thinking)

Score:
40.0

Params:
1T

40.0

Manus Agent (Quality Mode)

Score:
40.0

Params:
Unknown

40.0

SuperGrok Expert

Score:
40.0

Params:
Unknown

75.0

ChatGPT-5-Pro

Score:
75.0

Params:
Unknown

Performance of Step 3.5 Flash measured acrossReasoning, Coding, and Agentic Tasks. Open-source models (left) are sorted by their total parameter count, while top-tier proprietary models are shown on the right. xbench-DeepSearch scores are sourced fromofficial publicationsfor consistency. The shadowed bars represent the enhanced performance of Step 3.5 Flash usingParallel Thinking.

## Step 3.5 Flash: Intelligence in Practice

True intelligence density is not just about peak performance on conventional benchmarks, but about robustness in dynamic, real-world scenarios. While we value strong results on standard metrics as a foundation, our primary goal is to validate that the model functions as a resilient and effective partner when facing the unpredictability of actual execution.

In the following part, we consolidate a range of performance feedback from real-world showcases, rigorous internal benchmarks, and supplemental public leaderboards. Covering everything from advanced reasoning in math and coding to everyday interaction capabilities, these results demonstrate that Step 3.5 Flash is not just fast enough to think—it isReliable Enough to Act.

### Orchestrated Tool-use

Tool-use is far more than a technical feature; it is the fundamental atomic capability that transforms a static model into an active agent. It serves as the bridge between internal reasoning and external impact, allowing the model to transcend the limitations of its training data and interact with the real world.

Step 3.5 Flash distinguishes itself through a unique "Think-and-Act" synergy in tool environments. Rather than merely executing commands, the model exhibits massive-scale orchestration and cross-domain precision. It maintains flawless intent-alignment even when navigating vast, high-density toolsets, and possesses the adaptive reasoning required to pivot seamlessly between raw code execution and specialized API protocols.

Stock Investment

Result

Trace

Loading case...

We demonstrate an open-world stock investment scenario powered by Step 3.5 Flash with seamless MCP integration. The user asks to generate professional trading recommendations for an existing portfolio while simultaneously managing cloud-based archiving and automated alerts. Step 3.5 Flash, acting as the central controller, first orchestrates over 80 MCP tools to aggregate market data and technical indicators. It then executes raw code for bespoke financial metrics and data visualization to identify key investment insights. Once the analysis is complete, the model automatically triggers cloud storage protocols and schedules the notification system to ensure end-to-end workflow automation. This demonstrates the model's ability to map complex intent to high-density tool-use in a single, integrated session.

Step 3.5 Flash's superior tool-use capability is further evidenced by the performance metrics below. By integrating Python code execution within its Chain-of-Thought reasoning, the model achieves substantial performance gains across elite logic and mathematics benchmarks, including AIME 2025 (99.8), HMMT 2025 Nov. (98.0), IMOAnswerBench (86.7), and ARC-AGI-1 (56.5).

#### Tool-Augmented Reasoning Performance

Comparison of Step 3.5 Flash with and without Python code execution capability

AIME 2025

97.3

99.8

HMMT 2025 (Nov.)

94.0

98.0

IMOAnswerBench

85.4

86.7

ARC-AGI-1

54.8

56.5

Step 3.5 Flash

Step 3.5 Flash w. Python

### Agentic Coding

The shift from traditional coding to agentic coding marks a transition from passive code completion to the autonomous resolution of end-to-end engineering objectives. Rather than merely predicting syntax, Step 3.5 Flash functions by decomposing complex requirements into a series of actionable steps within a codebase. It treats code as a tool to verify logic, map out dependencies, and navigate the structural depth of real-world repositories. Step 3.5 Flash is compatible with Claude Code, serving as an efficient backend for agent-led development. By leveraging its long-context reasoning and precision in tool invocation, the model can handle repository-level tasks and maintain the continuity of the development loop. Here we show some examples:

Tactical Weather Intelligence Dashboard — A flight-cockpit inspired 3D globe visualizer engineered for high-density data environments. Featuring a custom WebGL 2.0 engine, it manages 15,000+ active nodes with real-time WebSocket telemetry. This case demonstrates our model's ability to build low-latency data pipelines and high-performance geospatial visualizations with a focus on system stability and professional-grade UI/UX.

View Prompt

For an artistic weather dashboard that feels like a pilot's glass cockpit, create a 3D real Earth rendered via WebGL. Each country's major cities should have a glowing marker; clicking it zooms in on that region, shifting to a semi-transparent 2D overlay with detailed weather charts. Real-time data streamed via WebSockets with graceful fallback to cached snapshots.

Three.js Procedural Ocean Engine — A high-performance rendering system featuring fractal-based wave geometry and ray-traced surfaces. It leverages Fresnel reflectance and PBR materials for photorealistic lighting. This showcase highlights our model's expertise in Computer Graphics (CG), complex rendering pipeline design, and seamless integration of Three.js/GLSL/Shadertoy workflows.

View Prompt

Write a single html: Achieve a fully procedural dynamic ocean scene rendering that precisely captures the complex interaction between wave geometry generated from fractal noise and a physically-based lighting model. The core algorithm must employ ray tracing optimized for height maps to render a dynamic water surface generated by iteratively layering fractal noise functions (Fractal Brownian Motion). The material system must be physics-based, implementing a Fresnel effect to blend reflections from a procedural sky dome with depth-based water transmission colors, and include a specular reflection component to simulate sun glints. The parameter control specifications should expose at least three key dimensions: controlling the sharpness and agitation of wave patterns, controlling the time evolution rate of the sea surface animation, and controlling the path and perspective of automated camera navigation. The Three.js integration requires a dynamic multi-pass rendering architecture with built-in automated support for a Ping-Pong (double buffering) mechanism to handle simulations requiring state feedback, and the ability to inject a shared codebase into all rendering passes. Specifically, the implementation should encapsulate GLSL logic within a THREE.ShaderMaterial and apply it to a full-screen THREE.PlaneGeometry. The system must implement a complete shader interface that automatically maps Three.js scene variables (such as time, resolution, and mouse 4D vectors) to the standard uniforms used in Shadertoy. The rendering pipeline must strictly follow pass dependency order and precisely update time-related uniforms within the requestAnimationFrame loop to drive the procedural animation of the entire scene.

Agentic Workflow Take In — A case demonstrates how Step assists in executing daily data processes, achieving end-to-end data production. It aligns upstream data formats, accurately calls data generation models, verifies and transforms the results, and generates workflow reports, embodying the core concept of Agent-in-the-loop. Step can effectively take over our daily workflows, undertaking complex and repetitive processes.

View Prompt

skills.md
---
name: rollout-data-workflow
description: Generate rollout SFT data under /data/dataset/rollout by converting query JSON to tasks, running websftgen.production.cli with checkpointed sharded JSONL output, and exporting chat-style SFT via websftgen.production.refresh_exported_sft_data; use when asked to create/continue rollout cases, resume from checkpoints, or organize paths and artifacts for handoff.
---
# Rollout Data Workflow
## Fixed paths
- Root: `/data/dataset/rollout/`
- Queries: `/data/dataset/rollout/queries/`
- Tasks: `/data/dataset/rollout/tasks/`
- Rollout cases (raw generation output): `/data/dataset/rollout/rollout-cases/`
## Workflow
### Step 0 — Confirm run parameters
Ask for (if not provided):
- `model_name` (used in rollout output file names and `--models`)
- `repeat_per_model` (default `3`, must be `<= 3` unless user explicitly overrides)
- `concurrency` (default `10`, must be `<= 10` unless user explicitly overrides)
Also confirm the input query file path under `/data/dataset/rollout/queries/`.
### Option A — One-command pipeline (recommended)
Use `scripts/rollout_pipeline.py` to compute file names and run the whole workflow while always executing from the repo root.
### Step 1 — Convert query JSON to task JSON list
Goal: create a JSON list of strings.
### Step 2 — Generate rollout cases via websftgen CLI
Goal: run `websftgen.production.cli` on the task file and write sharded JSONL outputs + an append-only checkpoint.
### Step 3 — Export chat-style SFT data
Goal: turn the raw rollout JSONL (possibly sharded) into chat-style SFT JSON.
### Step 4 — Handoff summary
Always report paths and parameters for handoff.

Epic Solar System Simulation — A 3D interactive model of the solar system with cinematic lighting and atmosphere, presenting a shocking visual narrative from nothingness to a complete galaxy through an epic opening performance of dynamically generated and orbiting planets one by one. This demonstrates Step comprehensive creative ability in 3D scene orchestration, lighting and atmosphere creation, and control of interactive narrative rhythm.

View Prompt

We need to build an interactive 3D solar system model with ample light and shadow atmosphere and an epic, cinematic opening effect. The core gameplay is to allow users to witness the entire solar system from scratch, with each planet dynamically generated and entering orbit.

Autonomous Business Intelligence Engine — End-to-end data processing—from CSV ingestion to Cubic Spline interpolation and multi-scenario forecasting. Demonstrates high-order reasoning in multi-step tool use, automated error correction during code execution, and complex data visualization. Successfully modeled a 60% DNU drop scenario, identifying a 1.6x quality gap between acquisition channels. It reflects the model's agentic strength in systematic problem solving and its ability to act as a self-directed Data Scientist.

View Prompt

Stability Prediction of DAU for Real Estate Platform

Problem
A real estate transaction platform (similar to Beike or Lianjia) primarily acquires new users through multi-channel marketing. Users search for properties, view details, and contact agents on the platform. The platform's core business metrics include DAU (Daily Active Users), DNU (Daily New Users), and the number of leads.

Starting from January 2022, the company's strategy shifted toward gradually migrating traffic from the app side to the Douyin platform. As a result, the marketing budget for the app began to decrease. With this adjustment in marketing, DNU dropped from a daily average of 500 to 200, and DAU gradually declined from around 5,000 accordingly.

Management is highly concerned about this trend and has repeatedly asked in multiple meetings: "To what level will DAU drop before stabilizing? If the current marketing level is maintained, what will the future DAU be?"

The operations team has also raised questions: "We currently have multiple marketing channels. Are there differences in user quality across these channels? If we adjust the structure of channel investments, will it affect the final DAU level?"

User acquisition and retention data from January to December 2022 are now provided, including both overall data and data segmented by channels (organic traffic, information flow, app stores, internal referrals, and search). Please use retention analysis to project DAU and provide recommendations for marketing strategies. Finally, submit a Report.md.

Autonomous Large-Scale Repository Architect — A specialized agentic workflow for navigating and deciphering high-complexity codebases. Beyond simple file scanning, the model performs deep-trace logic mapping and cross-module dependency analysis to synthesize the "mental model" of an entire ecosystem. This showcase demonstrates the model's superior cognitive capacity for large-scale software architecture, enabling it to autonomously generate professional Wikis that connect high-level design patterns to low-level implementation details across thousands of lines of code.

View Prompt

# Agent Task: Comprehensive Repo Discovery & Wiki Generation
You are a Senior Documentation Engineer. Your goal is to explore this repository and generate a high-quality, professional Wiki in Markdown format.
## Phase 1: Exploration Strategy
1. **Architecture Audit**: Identify the core tech stack, entry points, and high-level directory structure.
2. **Logic Mapping**: Trace the data flow for the most critical features.
3. **Dependency Analysis**: Check `package.json`, `go.mod`, `requirements.txt`, etc., to understand the ecosystem.
4. **Pattern Recognition**: Identify design patterns (e.g., Singleton, Factory, Middleware) used in the codebase.
## Phase 2: Wiki Structure Requirements
Generate a folder named `docs/wiki/` containing the following sections:
### 1. Project Overview & Value Prop
### 2. Architecture & Design
### 3. Getting Started (Deep Dive)
### 4. Code Standards & Contribution
## Phase 3: Writing Style
- **Clarity over Complexity**: Use professional, concise language.
- **Visuals**: Use Mermaid.js for diagrams where logic is complex.
- **Contextual**: Link to actual files in the repo using relative paths.
---
**Instruction**: Start by scanning the file tree and then provide a proposed outline for the Wiki before writing the full content.

Beyond Vibe Coding - Driving Professional Data Agent in Claude Code.Within advanced agent frameworks like Claude Code, LLMs have evolved beyond "vibe coding" to becoming active problem-solvers capable of driving complex workflows to accomplish sophisticated objectives. To evaluate this in a real-world context, we task Step 3.5 Flash to act as a professional data analyst within the Claude Code environment.

We curate a benchmark of 50 end-to-end tasks that reflect the intricate nature of Internet backend data analysis. As shown in the table below, Step 3.5 Flash demonstrates exceptional proficiency in managing these multi-stage processes—independently handling data ingestion, cleaning, feature construction, and results interpretation. With a score of 39.58%, it proves to be a robust engine for sophisticated agentic systems, outperforming several frontier models in analytical accuracy.

### Professional Data Analysis Benchmark

Claude Opus 4.5

45.0

Step 3.5 Flash

39.6

GPT-5.2

39.3

Gemini 3.0 Pro

33.6

Deepseek V3.2

27.9

We notice that frontier models like Gemini 3.0 Pro didn't perform as expected in this specific test. This could be due to framework compatibility issues within Claude Code, or simply a difference in analytical capability. Either way, the takeaway here is how well Step 3.5 Flash syncs with the Claude Code, enabling it to handle professional data tasks with solid reliability.

### Deep Research

While Step 3.5 Flash is compact, its utility is no longer limited by its internal parametric knowledge. In the agentic era, the ability to leverage the internet as a dynamic knowledge base is more critical than static memory—a strength proven by Step 3.5 Flash's performance on benchmarks like xbench-DeepSearch and BrowserComp.

Deep Research extends basic information retrieval by delegating the entire research workflow to an agentic loop of planning, searching, reflecting, and writing. To evaluate Step 3.5 Flash on this complex process, we use the Scale AIResearch Rubrics, a benchmark designed to assess the factual grounding and reasoning depth of long-form research. Our implementation facilitates this through a single-agent loop based on a ReAct architecture, natively integrating specialized tools such asbatch_web_surferandshellfor iterative investigations. This approach allows Step 3.5 Flash to achieve a score of 65.27%, delivering research quality that competes with OpenAI and Gemini Deep Research while maintaining significantly higher inference efficiency.

### Performance onResearchRubrics

Step 3.5 Flash

65.3

ReAct Agent

Gemini DeepResearch

63.7

Agent System

Step-DeepResearch

61.4

ReAct Agent

OpenAI DeepResearch

60.7

Agent System

Qwen DeepResearch

49.2

Agent System

We evaluated commercial agents by collecting reports from their official web interfaces (captured Dec 2–15, 2025) under default configurations, while our internal models utilized the ReAct framework for report generation. All outputs were subsequently appraised by an LLM judge using a ternary grading for each criterion.

We demonstrate Step 3.5 Flash's exceptional Deep Research capabilities through a case study on early childhood science education. In this instance, Step 3.5 Flash synthesized a comprehensive research report of approximately 10,000 words, distilling complex neuroplasticity theories into an actionable, expert-grade guide for ages 0–3. The output bridges theoretical milestones with practical "Parental Scripts," reframing sensory play as structured inquiry while maintaining a rigorous focus on both cognitive depth and safety guidance.

Deep Research

Result

Trace

Loading result...

Loading case...

▲

▼

Multi-Agent Orchestration Framework.Step 3.5 Flash also natively supports a multi-agent architecture where a Master Agent orchestrates complex tasks through autonomous planning and dynamic routing. This hierarchical framework dispatches specialized Search and Verify agents to handle retrieval and factual grounding via parallel tool-invocation loops. To ensure precision, a Summary Agent consolidates each sub-agent's trajectory into structured feedback, enabling the Master Agent to synthesize a final, coherent response.

Multi-Agent Deep Research

Loading case...

### Edge–Cloud Collaboration

Edge-Cloud Collaboration, as a specialized form of multi-agent architecture, offers inherent advantages over cloud-only solutions in context management, privacy protection, and cost control.

Here we examine the synergy between the cloud-basedStep 3.5 Flashand the edge-deployedStep-GUI. We demonstrate how they work together to execute complex tasks ondiverse edge devices(smartphones in this case).

Note: These scenarios represent out-of-distribution tasks not present in Step 3.5 Flash's training process, thereby also serving as a test of its zero-shot generalization.

In this case, the user asks to search for the latest Arxiv papers on GUI Agents, summarize them, and immediately share the result via WeChat. Step 3.5 Flash, acting as the 'Cloud Brain,' first executes the search and summarization in the cloud for maximum speed. Once the content is ready, it triggers the 'Hand'—our on-deviceStep-GUI—to wake up the phone, open WeChat, and deliver the message to the specific contact. This is Cloud-Device Synergy in action.

In this case, the user asks to compare Mac Mini M4 prices across platforms. Step 3.5 Flash, acting as the 'Cloud Brain,' decomposes this complex request into specific sub-tasks for Taobao, JD.com, and Pinduoduo. This cloud-side planning significantly lowers the difficulty for the on-deviceStep-GUI, ensuring higher success rates as it retrieves real-time data from each app. Step 3.5 Flash then synthesizes the results to identify Pinduoduo as the cheapest option and offers a buying guide. This demonstratesCloud-Device Synergy: cloud intelligence simplifies local execution for reliable results.

Furthermore, we conduct a comparative evaluation on theAndroidDaily Hardsubset, a benchmark tailored for Chinese mobile application scenarios encompassing e-commerce, entertainment, and other daily tasks.

### Performance on AndroidDaily Hard

Step-GUI

40

Edge Only

Step 3.5 Flash + Step-GUI

57

Edge–Cloud

We compare two paradigms: (1) single-agentStep-GUIexecuting tasks independently on-device, and (2) an edge-cloud collaborative framework integrating Step 3.5 Flash withStep-GUIvia GUI-MCP. The results demonstrate that utilizing Step 3.5 Flash as the cloud-based host agent to orchestrateStep-GUIsignificantly enhances the system's performance in complex scenarios.

### Competition-level Math

Step 3.5 Flash demonstrates exceptional logical rigor in competition-level math. Through the deep analysis of IMO Shortlisted problems, the model proves its core strength in complex symbolic reasoning and abstract structural synthesis.

IMO Shortlisted Problem 1

Problem

Solution

The problem seeks to characterize all real numbers \(\alpha\) such that the sum of the floor functions \(S_n = \sum_{k=1}^n \lfloor k\alpha\rfloor\) is always divisible by \(n\). The primary difficulty lies in the fact that \(\alpha\) is a real number, requiring one to separate its integer part \(m\) and fractional part \(\theta\) to analyze how the summation interacts with the modularity of \(n\). The core insight of the proof is reducing the problem to the behavior of the fractional sum \(T_n = \sum_{k=1}^n \lfloor k\theta\rfloor\) and employing induction to show that the divisibility constraints force extreme values for the floor functions.

IMO Shortlisted Problem 2

Problem

Solution

The problem asks whether a specific inequality involving the sums of exponential terms \(3^{a_n}\) and \(2^{a_n}\) must hold for at least one \(n\) in any sequence of positive real numbers. The primary difficulty lies in the potentially divergent behavior of the numerator and denominator, which makes it non-obvious whether the ratio ever drops below a fixed constant like \(1/2024\). The core insight of the proof is to perform a change of variables \(x_i = 2^{a_i}\) and identify the power \(\alpha = \log_2 3\), transforming the expression into a ratio of power sums \(\frac{\sum x_i^\alpha}{(\sum x_i)^2}\).

### Reliability in Interaction

We also care about interaction reliability—the model's ability to not just solve problems, but to engage users with precision and professional judgment. To test this, we evaluated Step 3.5 Flash across two critical dimensions:

* Proactive Intent Clarification: In our internal benchmark of 74 ambiguous real-world requests (primarily localized queries), Step 3.5 Flash consistently identified missing information and asked targeted questions to clarify user intent rather than making assumptions.

### Proactive Intent Clarification

GPT-5.2

70.8

Claude Opus 4.5

68.3

Gemini 3.0 Pro

64.0

Step 3.5 Flash

62.5

Deepseek V3.2

52.3

* Advisory & Consultation: Across 500 prompts in a balanced bilingual setting spanning life, learning, and workplace contexts, the model demonstrated solid domain knowledge and a professional style, maintaining high instruction-following standards in both English and Chinese.

Model

Average

Usefulness

Logic

Tone

Instruction-following

GPT-5.2
77.8%
77.2%
81.9%
73.0%
79.6%

Gemini 3.0 Pro
70.6%
73.9%
61.7%
72.3%
74.4%

Step 3.5 Flash
70.5%
73.3%
62.1%
72.4%
74.2%

Deepseek V3.2
70.3%
72.5%
64.4%
71.2%
72.9%

Claude Opus 4.5
68.5%
69.7%
66.5%
65.9%
72.1%

## The Engine Behind

### Architecture Optimized for Flash-Speed Decoding and Inference

The architecture ofStep 3.5 Flashis defined by a model-system co-design that prioritizesinference cost and speedas the core architectural constraint. We employ aSparse Mixture-of-Experts (MoE)backbone to decouple global model capacity from per-token computation. While the total knowledge base spans196B parameters, the system only activates11B parameters per tokenduring inference. To further reducememory overhead, we strategically utilize dense layers for the first few layers of the network for high intelligence density.

To navigate the quadratic bottleneck of long-context processing, we leverage a hybrid attention layout that interleavesSliding-Window Attention (SWA)withFull Attentionat a 3:1 ratio. We specifically opted for SWA over linear alternatives to maintain the architectural flexibility required forspeculative decoding. SWA is inherently compatible withMulti-Token Prediction (MTP)heads. These heads predict additional future tokens in parallel with the primary output, enablingparallel verification. This allows the model to validate multiple token hypotheses in a single pass, effectively breaking the serial constraints of standard autoregressive decoding.

To ensure this lightweight hybrid structure retains peak performance, we implemented two critical enhancements. We utilized anaugmented query-head countin the SWA layers—increasing from 64 to 96—to strengthen representational power without expanding the \(KV\) cache footprint. This modification is highly efficient: since the attention window is fixed, the computational cost of these additional heads remains constant regardless of total sequence length. This allows us to scale up model expressiveness without the "long-context penalty" where attention costs usually explode as the conversation grows. Complementing this is ourHead-wise Gated Attention, which functions as an input-dependent attention sink. By dynamically modulating information flow, this mechanism preserves numerical stability while incurring negligible overhead.

These strategic architectural refinements demonstrate that frontier-level reasoning can be decoupled from prohibitive latency. By integratingsparse-active executionwithconcurrent token verification, the model achieves a decoding throughput up to350 tokens per second (TPS)on NVIDIA Hopper GPUs while running SWE-bench Verified.

Last but not least, theoptimized total parameter scaleof Step 3.5 Flash facilitates highly accessible, local inference. By consolidating its total capacity to a scale compatible with high-end personal hardware, the model supports high-fidelity private deployment on workstations such as theApple M4 Max,NVIDIA DGX Spark, orAMD AI Max+ 395, providing a 100% trusted execution environment.

The overall architecture of Step 3.5 Flash.

As the local deployment of large language models (LLMs) becomes increasingly prevalent, we have successfully adapted the Step 3.5 Flash to NVIDIA DGX Spark 128GB device based on the edge-side inference engine llama.cpp, and simultaneously released the INT4 quantized model weights in GGUF format. On NVIDIA DGX Spark, the Step 3.5 Flash achieves a generation speed of 20 tokens per second; by integrating the INT8 quantization technology for KVCache, it supports an extended context window of up to 256K tokens, thus delivering long text processing capabilities on par with cloud-based inference. The new model can be tested by developers on NVIDIA accelerated infrastructure viabuild.nvidia.com.

### Scalable RL Unleashes the Reasoning Potential

We introduce a scalable reinforcement learning framework designed to reliably train reasoning and agentic language models at scale.

Modern RL pipelines for LLMs rely on high-throughput inference engines to generate rollouts, while optimization happens asynchronously in a separate training system. At scale, this setup introduces two compounding challenges:

1. Training–inference mismatch, caused by numerical and architectural differences between systems
2. Off-policy drift, as policies evolve while rollouts lag behind

For long reasoning sequences, even minor token-level discrepancies can explode into extreme importance weights—leading to unstable updates, early convergence, or complete training collapse.

To address this, we proposeMetropolis Independence Sampling Filtered Policy Optimization (MIS-PO), which replaces fragile importance weighting withstrict sample filtering. Instead of scaling gradients with continuous importance-sampling ratios as in PPO, MIS-PO uses these ratios solely as abinary acceptance criterion. Trajectories whose likelihood deviates too far between the inference and training policies are simply excluded from optimization, while accepted samples are treated as effectively on-policy. Concretely, the policy update is driven by

 \[\mathcal{L}_{actor} = - \mathbb{E}_{\tau \sim \pi_{\theta_\text{vllm}}} \left[ \mathbb{I}(\tau) \cdot \log \pi_\theta(a_t|s_t) \cdot \hat{A}_t \right],\]


where the binary indicator \(\mathbb{I}(\tau)\) filters out off-distribution samples. This design dramatically reduces gradient variance and enables stable, long-horizon optimization without aggressive clipping.

Our framework also includestruncation-aware value bootstrapping, which prevents long reasoning trajectories from being incorrectly penalized when hitting context limits, androuting confidence monitoringfor Mixture-of-Experts models, providing a practical signal for RL stability at scale.

Together, these components turn reinforcement learning into areliable engine for continuous self-improvement, enabling consistent gains across mathematics, coding, and tool use, while remaining stable under large-scale, off-policy training.

Training dynamics of different RL algorithms. Ablations are conducted on the Qwen model.

## Benchmarks

In our benchmark table, we provide a detailed, side-by-side comparison of today's top-performing open-source models. Across a wide range of metrics, Step 3.5 Flash stands out with consistently strong results. Our evaluation focuses on three core dimensions—Reasoning, Coding and Agentic Capability—and visualizes score differences across peer models in a horizontal, at-a-glance format.

Benchmark

Step 3.5 Flash

DeepSeek V3.2

Kimi
K2 Thinking / K2.5

GLM-4.7

MiniMax M2.1

MiMo-V2 Flash

# Activated Params

11B

37B
32B
32B
10B
15B

# Total Params (MoE)

196B

671B
1T
355B
230B
309B

Est. decoding cost
@ 128K context, Hopper GPU**

1.0x
100 tok/s, MTP-3, EP8

6.0x
33 tok/s, MTP-1, EP32

18.9x
33 tok/s, no MTP, EP32

18.9x
100 tok/s, MTP-3, EP8

3.9x
100 tok/s, MTP-3, EP8

1.2x
100 tok/s, MTP-3, EP8

Agent

τ²-Bench
88.2
80.3 (85.2*)
74.3*
/
85.4*
87.4
86.6*
80.3 (84.1*)

BrowseComp
51.6
51.4
41.5* /
60.6
52.0
47.4
45.4

BrowseComp
(w/ Context Manager)
69.0
67.6
60.2
/
74.9
67.5
62.0
58.3

BrowseComp-ZH
66.9
65.0
62.3 / 62.3*
66.6
47.8*
51.2*

BrowseComp-ZH
(w/ Context Manager)
73.7
—
—
/
—
—
—
—

GAIA
(no file)
84.5
75.1*
75.6*
/
75.9*
61.9*
64.3*
78.2*

xbench-DeepSearch
(2025.05)
83.7
78.0*
76.0*
/
76.7*
72.0*
68.7*
69.3*

xbench-DeepSearch
(2025.10)
56.3
55.7*
—
/
40+
52.3*
43.0*
44.0*

ResearchRubrics
65.3
55.8*
56.2*
/
59.5*
62.0*
60.2*
54.3*

Reasoning

AIME 2025
97.3
93.1
94.5
/
96.1
95.7
83.0
94.1 (95.1*)

HMMT 2025 (Feb.)
98.4
92.5
89.4
/
95.4
97.1
71.0*
84.4 (95.4*)

HMMT 2025 (Nov.)
94.0
90.2
89.2*
/
—
93.5
74.3*
91.0*

IMOAnswerBench
85.4
78.3
78.6
/
81.8
82.0
60.4*
80.9*

Coding

LiveCodeBench-V6
86.4
83.3
83.1
/
85.0
84.9
—
80.6 (81.6*)

SWE-bench Verified
74.4
73.1
71.3
/
76.8
73.8
74.0
73.4

Terminal-Bench 2.0
51.0
46.4
35.7*
/
50.8
41.0
47.9
38.5

* "—" indicates the score is not publicly available or not tested.
* "*" indicates the original score was inaccessible or lower than our reproduced, so we report the evaluation under the same test conditions as Step 3.5 Flash to ensure fair comparability.
* BrowseComp (with Context Manager): when the effective context length exceeds a predefined threshold, the agent resets the context and restarts the agent loop. (By contrast, Kimi K2.5 and DeepSeek-V3.2 used a discard-all strategy.)
* In decoding cost section, decoding **Estimated using a similar but more accurate approach thanarxiv.org/abs/2507.19427

## Known Issues and Future Directions

1. Token Efficiency.Step 3.5 Flash achieves frontier-level agentic intelligence but currently relies on longer generation trajectories than Gemini 3.0 Pro to reach comparable quality.
2. Efficient Universal Mastery.We aim to unify generalist versatility with deep domain expertise. To achieve this efficiently, we are advancing variants of on-policy distillation, allowing the model to internalize expert behaviors with higher sample efficiency.
3. RL for More Agentic Tasks.While Step 3.5 Flash demonstrates competitive performance on academic agentic benchmarks, the next frontier of agentic AI necessitates the application of RL to intricate, expert-level tasks found in professional work, engineering, and research.
4. Operational Scope and Constraints.Step 3.5 Flash is tailored for coding and work-centric tasks, but may experience reduced stability during distribution shifts. This typically occurs in highly specialized domains or long-horizon, multi-turn dialogues, where the model may exhibit repetitive reasoning, mixed-language outputs, or inconsistencies in time and identity awareness.

## Meet StepFun

* OpenClawis a powerful agentic platform that works seamlessly with Step 3.5 Flash.Quick SetupInstall:curl -fsSL https://openclaw.ai/install.sh | bashOnboard:Runopenclaw onboard.Configure:In WebUI (Config → Models), add a new provider:Type:openai-completions→ Base URL:https://api.stepfun.ai/v1Model ID:step-3.5-flash(Context: 256000)For a full walkthrough, see ourOpenClaw Cookbook.
* Type:openai-completions→ Base URL:https://api.stepfun.ai/v1
* Model ID:step-3.5-flash(Context: 256000)
* Step 3.5 Flash is available via ourAPI platform (中文/EN), and you can chat with it on theWeb (中文/EN)or in ourApp (iOS/Android).
* Join ourDiscord communityfor updates, support, and early access.
