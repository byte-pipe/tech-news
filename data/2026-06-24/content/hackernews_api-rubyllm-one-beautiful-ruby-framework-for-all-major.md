---
title: RubyLLM | One beautiful Ruby framework for all major AI providers. Chat, images, embeddings, tools.
url: https://rubyllm.com/
site_name: hackernews_api
content_file: hackernews_api-rubyllm-one-beautiful-ruby-framework-for-all-major
fetched_at: '2026-06-24T19:35:47.748177'
original_url: https://rubyllm.com/
author: RubyLLM
date: '2026-06-24'
description: A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.
tags:
- hackernews
- trending
---

Copy page
 
 
 

# Star

 

A single, beautiful Ruby framework for all major AI providers. Easily build chatbots, AI agents, RAG applications, content generators, and every AI workflow you can think of.

 
 
Get started
 
GitHub
 
 
 
 
 
 
 
 
 
 
 

Battle tested at- Fully private work AI

 

## Build a working Ruby AI chat in two minutes

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

Using RubyLLM?Share your story! Takes 5 minutes.

 

## Why RubyLLM?

 

Every AI provider ships their own bloated client. Different APIs. Different response formats. Different conventions. It’s exhausting.

 

RubyLLM gives you one beautiful framework for all of them. Same interface whether you’re using GPT, Claude, or your local Ollama. Just three dependencies: Faraday, Zeitwerk, and Marcel. That’s it.

 

## Show me the code

 
# Just ask questions

chat
 
=
 
RubyLLM
.
chat

chat
.
ask
 
"What's the best way to learn Ruby?"

 
# Analyze any file type

chat
.
ask
 
"What's in this image?"
,
 
with: 
"ruby_conf.jpg"

chat
.
ask
 
"What's happening in this video?"
,
 
with: 
"video.mp4"

chat
.
ask
 
"Describe this meeting"
,
 
with: 
"meeting.wav"

chat
.
ask
 
"Summarize this document"
,
 
with: 
"contract.pdf"

chat
.
ask
 
"Explain this code"
,
 
with: 
"app.rb"

 
# Multiple files at once

chat
.
ask
 
"Analyze these files"
,
 
with: 
[
"diagram.png"
,
 
"report.pdf"
,
 
"notes.txt"
]

 
# Stream responses

chat
.
ask
 
"Tell me a story about Ruby"
 
do
 
|
chunk
|

 
print
 
chunk
.
content

end

 
# Generate images

RubyLLM
.
paint
 
"a sunset over mountains in watercolor style"

 
# Create embeddings

RubyLLM
.
embed
 
"Ruby is elegant and expressive"

 
# Transcribe audio to text

RubyLLM
.
transcribe
 
"meeting.wav"

 
# Moderate content for safety

RubyLLM
.
moderate
 
"Check if this text is safe"

 
# Let AI use your code

class
 
Weather
 
<
 
RubyLLM
::
Tool

 
desc
 
"Get current weather"

 
def
 
execute
(
latitude
:,
 
longitude
:)

 
url
 
=
 
"https://api.open-meteo.com/v1/forecast?latitude=
#{
latitude
}
&longitude=
#{
longitude
}
&current=temperature_2m,wind_speed_10m"

 
JSON
.
parse
(
Faraday
.
get
(
url
).
body
)

 
end

end

chat
.
with_tool
(
Weather
).
ask
 
"What's the weather in Berlin?"

 
# Define an agent with instructions + tools

class
 
WeatherAssistant
 
<
 
RubyLLM
::
Agent

 
model
 
"gpt-5-nano"

 
instructions
 
"Be concise and always use tools for weather."

 
tools
 
Weather

end

WeatherAssistant
.
new
.
ask
 
"What's the weather in Berlin?"

 
# Get structured output

class
 
ProductSchema
 
<
 
RubyLLM
::
Schema

 
string
 
:name

 
number
 
:price

 
array
 
:features
 
do

 
string

 
end

end

response
 
=
 
chat
.
with_schema
(
ProductSchema
).
ask
 
"Analyze this product"
,
 
with: 
"product.txt"

 

## Features

 
* Chat:Conversational AI withRubyLLM.chat
* Vision:Analyze images and videos
* Audio:Transcribe and understand speech withRubyLLM.transcribe
* Documents:Extract from PDFs, CSVs, JSON, any file type
* Image generation:Create images withRubyLLM.paint
* Embeddings:Generate embeddings withRubyLLM.embed
* Moderation:Content safety withRubyLLM.moderate
* Tools:Let AI call your Ruby methods
* Agents:Reusable assistants withRubyLLM::Agent
* Structured output:JSON schemas that just work
* Streaming:Real-time responses with blocks
* Rails:ActiveRecord integration withacts_as_chat
* Async:Fiber-based concurrency
* Model registry:800+ models with capability detection and pricing
* Extended thinking:Control, view, and persist model deliberation
* Providers:OpenAI, xAI, Anthropic, Gemini, VertexAI, Bedrock, DeepSeek, Mistral, Ollama, OpenRouter, Perplexity, GPUStack, and any OpenAI-compatible API
 

## Installation

 

Add to your Gemfile:

 
gem
 
'ruby_llm'

 

Thenbundle install.

 

Configure your API keys:

 
# config/initializers/ruby_llm.rb

RubyLLM
.
configure
 
do
 
|
config
|

 
config
.
openai_api_key
 
=
 
ENV
[
'OPENAI_API_KEY'
]

end

 

## Rails

 
# Install Rails Integration

bin/rails generate ruby_llm:install
bin/rails db:migrate
bin/rails ruby_llm:load_models 
# v1.13+

# Add Chat UI (optional)

bin/rails generate ruby_llm:chat_ui

 
class
 
Chat
 
<
 
ApplicationRecord

 
acts_as_chat

end

chat
 
=
 
Chat
.
create!
 
model: 
"claude-sonnet-4"

chat
.
ask
 
"What's in this file?"
,
 
with: 
"report.pdf"

 

Visithttp://localhost:3000/chatsfor a ready-to-use chat interface!