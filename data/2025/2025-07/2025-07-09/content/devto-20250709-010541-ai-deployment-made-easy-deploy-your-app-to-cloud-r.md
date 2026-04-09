---
title: 'AI deployment made easy: Deploy your app to Cloud Run from AI Studio or MCP-compatible AI agents - DEV Community'
url: https://dev.to/googleai/ai-deployment-made-easy-deploy-your-app-to-cloud-run-from-ai-studio-or-mcp-compatible-ai-agents-34lf
site_name: devto
fetched_at: '2025-07-09T01:05:41.678595'
original_url: https://dev.to/googleai/ai-deployment-made-easy-deploy-your-app-to-cloud-run-from-ai-studio-or-mcp-compatible-ai-agents-34lf
author: Steren
date: '2025-07-03'
description: Cloud Run has become a go-to app hosting solution for its remarkable simplicity, flexibility, and... Tagged with ai, google, mcp, cloud.
tags: '#ai, #google, #mcp, #cloud'
---

Cloud Runhas become a go-to app hosting solution for its remarkable simplicity, flexibility, and scalability. But the age of AI-assisted development is here, and going from idea to application is faster and more streamlined than ever. Today, we're excited to make AI deployments easier and more accessible by introducing new ways to deploy your apps to Cloud Run:

1. Deploy applications in Google AI Studio to Cloud Run with a single button click
2. Scale your Gemma projects with direct deployment of Gemma 3 models from Google AI Studio to Cloud Run
3. Empower MCP-compatible AI agents to deploy apps with the new Cloud Run MCP server

### 1. Streamlining app development and deployment with AI Studio and Cloud Run

Google AI Studiois the fastest way to start building with Gemini. Once you develop an app in AI Studio, you candeploy it toCloud Run with a single button click, allowing you to go from code to shareable URL in seconds (video at 2x speed):

Once deployed, the app is available at a stable HTTPS endpoint that automatically scales, including down to zero when not in use. You can re-deploy with updates from AI Studio, or continue your development journey in the Cloud Run source editor. Plus, your Gemini API key remains securely managed server-side on Cloud Run and is not accessible from the client device.

It’s also a very economical solution for hosting apps developed with AI Studio: Cloud Run hasrequest-based billingwith 100ms granularity and a free tier of 2 million requests per month, in addition to any free Google Cloud credits.

### 2. Bring your Gemma app to production in a click with Cloud Run

Gemma is a leading open model for single-GPU performance. To help you scale your Gemma projects,AI Studionow enables direct deployment of Gemma 3 models to Cloud Run:

This provides an endpoint running on Cloud Run's simple, pay-per-second, scale-to-zero infrastructure with GPU instances starting in less than five seconds, and it scales to zero when not in use. It’s even compatible with theGoogle Gen AI SDKout-of-the-box, simply update two parameters in your code to use the newly deployed endpoint:

from

google

import

genai

from

google.genai.types

import

HttpOptions

# Configure the client to use your Cloud Run endpoint and API key

client

=

genai
.
Client
(
api_key
=
"
KEY_RECEIVED_WHEN_DEPLOYING
"
,


http_options
=
HttpOptions
(
base_url
=
"
CLOUD_RUN_ENDPOINT_URL
"
))

# Example: Stream generate content

response

=

client
.
models
.
generate_content_stream
(


model
=
"
gemma-3-4b-it
"
,


contents
=
[
"
Write a story about a magic backpack.
You are the narrator of an interactive text adventure game.
"
]

)

for

chunk

in

response
:


print
(
chunk
.
text
,

end
=
""
)

Enter fullscreen mode

Exit fullscreen mode

### 3. Empower AI agents to deploy apps with the new Cloud Run MCP server

TheModel Context Protocol(MCP)is an open protocol standardizing how AI agents interact with their environment. At Google I/O, we shared that supporting open standards for how agents will interact with tools is a top priority for us.

Today, we are introducing theCloud Run MCP serverto enable MCP-compatible AI agents to deploy apps to Cloud Run. Let's see it in action with a variety of MCP clients: AI assistant apps, AI-powered Integrated Development Environments (IDEs), and agent SDKs.

1. AI assistant apps

Using the Claude desktop application to generate a Node.js app and deploy it to Cloud Run (video at 4x speed)

2. AI-powered IDEs

Updating a FastAPI Python app from VS Code with Copilot in agent mode using Gemini 2.5 Pro, and deploying it using the Cloud Run MCP server (video at 4x speed)

3. Agent SDKs, like theGoogle Gen AI SDKorAgent Development Kitalso have support for calling tools via MCP, and can therefore deploy to Cloud Run using the Cloud Run MCP server.

Add the Cloud Run MCP server to your favorite MCP client:

{
 "cloud-run": {
 "command": "npx",
 "args": ["-y", "https://github.com/GoogleCloudPlatform/cloud-run-mcp"]
 }
}

Enter fullscreen mode

Exit fullscreen mode

### Get Started

Build, deploy, and scale AI apps faster with AI Studio's integration with Cloud Run and the new Cloud Run MCP server. Give it a try:

* Build in AI Studioand deploy to Cloud Run
* Install Cloud Run MCP serveron your local machine
* Chat with Gemma 3 in AI Studioand deploy Gemma 3 to Cloud Run

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
