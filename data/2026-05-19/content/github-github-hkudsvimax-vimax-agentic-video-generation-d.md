---
title: 'GitHub - HKUDS/ViMax: "ViMax: Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)" · GitHub'
url: https://github.com/HKUDS/ViMax
site_name: github
content_file: github-github-hkudsvimax-vimax-agentic-video-generation-d
fetched_at: '2026-05-19T12:04:02.073835'
original_url: https://github.com/HKUDS/ViMax
author: HKUDS
description: '"ViMax: Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)" - HKUDS/ViMax'
---

HKUDS

 

/

ViMax

Public

* NotificationsYou must be signed in to change notification settings
* Fork895
* Star5.1k

 
 
 
 
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

329 Commits
329 Commits
agents
agents
 
 
assets
assets
 
 
configs
configs
 
 
interfaces
interfaces
 
 
pipelines
pipelines
 
 
tests
tests
 
 
tools
tools
 
 
utils
utils
 
 
.gitignore
.gitignore
 
 
Communication.md
Communication.md
 
 
LICENSE
LICENSE
 
 
README_ZH.md
README_ZH.md
 
 
TODO
TODO
 
 
main_idea2video.py
main_idea2video.py
 
 
main_script2video.py
main_script2video.py
 
 
pyproject.toml
pyproject.toml
 
 
readme.md
readme.md
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# ViMax: Agentic Video Generation

### 🚨 Current Video Generation Limitations:

* ❌Limited to Short Clips- Most AI tools generate only seconds of footage.
* ❌Consistency Chaos- Characters and scenes change unpredictably across frames.
* ❌Visual-Only Focus- Missing scripts, audio, narrative structure, and storytelling depth.

### 💡 ViMax Solution:

🎬Director,Screenwriter,Producer, andVideo GeneratorAll-in-One! We're exploring a future where AI becomes a complete creative powerhouse. 💡 Simply input your concept. ViMax autonomously handles the rest. It orchestrates scriptwriting, storyboarding, character creation, and final video generation—all end-to-end. 🚀

vimax_demo.mp4

## 📑 Table of Contents

* 💡 Key Features
* 🔮 Demos
* 🏗️ Architecture
* 🚀 Quick Start

## 💡Key Features

### 🌟Idea2Video

From Spark to Screen

Transformraw ideasinto complete video stories through intelligent multi-agent workflows automatingstorytelling, character design, and production.

### 🎨Novel2Video

Smart Literary Adaptation Engine

Transformcomplete novelsintoepisodic video contentwith intelligent narrative compression, character tracking, and scene-by-scene visual adaptation

### ⚙️Script2Video

Unlimited Screenplay Video Creation

Unleash your creativity by writingany screenplayfrom personal stories to epic adventures, giving you complete control over every aspect of your visual storytelling.

### 🤳AutoCameo

Generate Video from Your Photo

Create your own cameovideo, transforming yourself/pet into a guest star who appears across limitless creative scripts, cinematic sequences, and interactive storylines.

## 🔮Video Demos Generated from Scratch

f1.mp4

underwater.mp4

otter.mp4

carrier.mp4

vampire.mp4

skydiving.mp4

tree.mp4

cameo_skycastle.mp4

cameo_cat.mp4

### 🎯End-to-End Video Creation Engine

The Challenges:

* 🌅Reference Images: Time-consuming acquisition, organization, and alignment of reference frames that accurately capture characters, objects, positions, and environments.
* 🫠Consistency Check: Sometimes, the image generator may generate unusable images even if it is given the correct characters, position, environment reference image and prompts.
* 📄Scripts Generation: Professional and high-quality videos need to have rich information density and structured design.
* 📝Storyboard Design: Converting stories into visual narratives requires expertise in cinematography, scene composition, and visual storytelling that most creators lack.
* 🎬Shot Design: Creating coherent camera sequences with proper angles, transitions, and pacing while maintaining narrative flow across complex scenes.
* 🎨Development Delays: Ensuring character appearances, environments, and artistic style remain consistent across hundreds of shots in long-form content.
* ⏱️Production Efficiency: Traditional video creation involves multiple specialists and lengthy workflows, creating barriers for independent creators and rapid prototyping.
* 🎥Scaling AI Generated Video: AI-generated videos are usually only a few seconds long, high-quality long videos at the minute or even hour level require complex cross-scene continuity and multi-storyboards design and processing capabilities.

ViMAX: eliminates these production bottlenecks by automating the entire video creation pipeline from narrative input to final video output.

### 🔥Why ViMax?

🧠 
Effortless Production

🚀 
Complete Creative Freedom

🔊 
Audio and Video Binding

🎨 
Professional Quality

🤩 
Interactive Video

One-Prompt to Finished Video

From Any Narrative to Reality

Synchronized Storytelling

Movie-Grade Output

Make Your Own Cameo Video

Skip the technical complexity—just describe your vision and let ViMax handle script generation, storyboarding, shot design, reference management, and consistency validation

No creative limits—whether it's a trailer, short story, novel chapter, or original concept, ViMax intelligently structures narratives and designs cinematography to bring any idea to life

Seamlessly integrate character voice, and sound effects with visual content to create immersive experiences where audio and video work in perfect harmony

Automated quality control ensures character consistency, proper scene composition, and professional visual standards across every frame of your video

Interact in your own short stories by uploading your photo—ViMax intelligently integrates you as a character with consistent appearance and natural interactions throughout the entire video

### ☄️Coming Soon

* 👨‍💻Google AI Studio API config✅
* 📹Dev mode branch
* 🤳AutoCameo integrate
* 📺More demos
* 🎞️Shot planning
* 🤖New features

## 🏗️ Architecture

### 📊System Overview

ViMaxis a multi-agent video framework that enables automated multi-shot video generation while ensuring character and scene consistency. Our system seamlessly translates your ideas into corresponding videos, allowing you to focus on storytelling rather than technical implementation.

🎯Technical Capabilities:

🧬Intelligent Long Script Generation

RAG-based long script design engine that intelligently analyzes lengthy, novel-like stories and automatically segments them into a multi-scene script format. The process meticulously ensures that all key plot developments and character dialogues are accurately retained within the new structure.

🪄Expressive Storyboard Design

Shot-level storyboard design system that create expressive storyboards through cinematography language based on user requirements and target audiences, which establishs the narrative rhythm for subsequent video generation.

🔮Multi-camera Filming Simulation

Simulates multi-camera filming to deliver an immersive viewing experience while maintaining consistent character positioning and backgrounds within the same scene.

🧸Intelligent Reference Images Selection

Intelligently select the reference image required for the first frame of the current video, including the storyboards that occurred in the previous timeline, to ensure the accuracy of multiple characters and environmental elements as the video becomes longer.

⚙️Automated Images Generation

Based on the selected reference image and the visual logical order on the previous timeline, the prompt of the image generator is automatically generated to reasonably arrange the spatial interaction position between the character and the environment.

✅Automated Image Generation Consistency Check

Generate multiple images in parallel and select the best consistent image as the first frame through MLLM/VLM to imitate the workflow of human creators.

⚡High-efficiency Parallel Shot Generation

Parallel processing for sequential shots captured from the same camera enables highly efficient video production.

### 🤖Multi-Agent Video Generation Pipeline

 🧠 
INPUT LAYER

 📝 Idea & Scripts & Novels • 💭 Natural Language Prompts • 🖼️ Reference Images • 🎨 Style Directives • 🧩 Configs
 

 🧭 
CENTRAL ORCHESTRATION

 Agent Scheduling • Stage Transitions • Resource Management • Retry/Fallback Logic
 

 🧾 
SCRIPT UNDERSTANDING

 Character/Environment Extraction • Scene Boundaries • Style Intent
 

 🎥 
SCENE & SHOT PLANNING

 Storyboard Steps • Shot List • Key Frames & Beats
 

 🧪 
VISUAL ASSET PLANNING

 Reference Image Selection • Look/Style Guidance • Prompt Conditioning
 

 🗂️ 
ASSET INDEXING

 Frames/Refs Catalog • Embeddings • Retrieval for Reuse
 

 ♻️ 
CONSISTENCY & CONTINUITY

 Character/Environment Tracking • Ref Matching • Temporal Coherence
 

 ✂️ 
VISUAL SYNTHESIS & ASSEMBLY

 Image Generation • Best-Frame Selection • First/Last-Frame→Video • Cut & Timeline Assembly
 

 🚀 
OUTPUT LAYER

 🖼️ Frames • 🎞️ Clips & Final Videos • 📜 Logs • 📦 Working Directory Artifacts
 

## 🚀Quick Start

### 🖥️Environment

OS: Linux, Windows

### 📥Clone and Install

We use uv to manage the environment. For uv installation, please refer to thehttps://docs.astral.sh/uv/getting-started/installation/.

git clone https://github.com/HKUDS/ViMax.git

cd
 ViMax
uv sync

### 🎯Usage

main_idea2video.py is used to convert your ideas into videos.
You need to configure the model and API key information in the configs/idea2video.yaml file, including three parts—the chat model, the image generator, and the video generator, as shown below

chat_model
:
 
init_args
:
 
model
: 
google/gemini-2.5-flash-lite-preview-09-2025

 
model_provider
: 
openai

 
api_key
: 
<YOUR_API_KEY>

 
base_url
: 
https://openrouter.ai/api/v1

image_generator
:
 
class_path
: 
tools.ImageGeneratorNanobananaGoogleAPI

 
init_args
:
 
api_key
: 
<YOUR_API_KEY>

video_generator
:
 
class_path
: 
tools.VideoGeneratorVeoGoogleAPI

 
init_args
:
 
api_key
: 
<YOUR_API_KEY>

working_dir
: 
.working_dir/idea2video

Then, provide a simple yet thoughtful idea and the corresponding creative requirements in main_idea2video.py.

idea = \

"
"
"

If a cat and a dog are best friends, what would happen when they meet a new cat?

"
"
"

user_requirement = \

"
"
"

For children, do not exceed 3 scenes.

"
"
"

style = 
"
Cartoon
"

#### Using MiniMax as Chat Model Provider

MiniMaxmodels can be used as an alternative chat model provider. MiniMax offers OpenAI-compatible API access to models such asMiniMax-M2.7(1M context window) andMiniMax-M2.5(204K context).

Simply setmodel_provider: minimaxin your config — the base URL is resolved automatically:

chat_model
:
 
init_args
:
 
model
: 
MiniMax-M2.7

 
model_provider
: 
minimax

 
api_key
: 
<YOUR_MINIMAX_API_KEY>

Or export the API key as an environment variable and leaveapi_keyempty:

export
 MINIMAX_API_KEY=
<
YOUR_KEY
>

Seeconfigs/idea2video_minimax.yamlandconfigs/script2video_minimax.yamlfor complete examples.

Model

Context

Note

MiniMax-M2.7

1M tokens

Latest, recommended

MiniMax-M2.7-highspeed

1M tokens

Fast variant

MiniMax-M2.5

204K tokens

Stable

MiniMax-M2.5-highspeed

204K tokens

Fast variant

main_script2video.py generates a video based on a specific script.
You similarly need to set up the API configuration in configs/script2video.yaml file. Then, provide a scene script and the corresponding creative requirements in main_script2video.py, as shown below.

script
 
=
 \

"""

EXT. SCHOOL GYM - DAY

A group of students are practicing basketball in the gym. The gym is large and open, with a basketball hoop at one end and a large crowd of spectators at the other end. John (18, male, tall, athletic) is the star player, and he is practicing his dribble and shot. Jane (17, female, short, athletic) is the assistant coach, and she is helping John with his practice. The other students are watching the practice and cheering for John.

John: (dribbling the ball) I'm going to score a basket!

Jane: (smiling) Good job, John!

John: (shooting the ball) Yes!

...

"""

user_requirement
 
=
 \

"""

Fast-paced with no more than 20 shots.

"""

style
 
=
 
"Animate Style"

🌟 If this project helps you, please give us a Star!

❤️ Thanks for visiting ✨ ViMax!

## About

"ViMax: Agentic Video Generation (Director, Screenwriter, Producer, and Video Generator All-in-One)"

### Topics

 video-generation

 agentic-aigc

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

5.1k

 stars
 

### Watchers

51

 watching
 

### Forks

895

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%