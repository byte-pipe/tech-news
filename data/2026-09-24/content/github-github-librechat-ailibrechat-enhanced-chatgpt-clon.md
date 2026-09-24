---
title: 'GitHub - LibreChat-AI/LibreChat: Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active · GitHub'
url: https://github.com/LibreChat-AI/LibreChat
site_name: github
content_file: github-github-librechat-ailibrechat-enhanced-chatgpt-clon
fetched_at: '2026-09-24T15:44:10.473297'
original_url: https://github.com/LibreChat-AI/LibreChat
author: LibreChat-AI
description: 'Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active - LibreChat-AI/LibreChat'
---

LibreChat-AI

 

/

LibreChat

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork9.2k
* Star44.9k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

5,748 Commits
5,748 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude/
skills
.claude/
skills
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
api
api
 
 
client
client
 
 
config
config
 
 
docs
docs
 
 
e2e
e2e
 
 
helm
helm
 
 
otel/
langfuse-fanout
otel/
langfuse-fanout
 
 
packages
packages
 
 
redis-config
redis-config
 
 
scripts
scripts
 
 
search
search
 
 
skill
skill
 
 
src/
tests
src/
tests
 
 
utils
utils
 
 
.codex
.codex
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTEXT.md
CONTEXT.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.multi
Dockerfile.multi
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh.md
README.zh.md
 
 
UPGRADING.md
UPGRADING.md
 
 
bun.lock
bun.lock
 
 
deploy-compose.langfuse-fanout.yml
deploy-compose.langfuse-fanout.yml
 
 
deploy-compose.yml
deploy-compose.yml
 
 
docker-compose.langfuse-fanout.yml
docker-compose.langfuse-fanout.yml
 
 
docker-compose.override.yml.example
docker-compose.override.yml.example
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
librechat.example.yaml
librechat.example.yaml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
rag.yml
rag.yml
 
 
tool-intent-spec.md
tool-intent-spec.md
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# LibreChat

English·中文

## 🚀 What's New in v0.8.8-rc4

* Public Agents API docs:Serve an OpenAPI specification and interactive Swagger UI for inference, events, Agent management, and Skill management.
* Attached workspaces (highly experimental):Isolate workspaces by conversation, load repository instructions, and use bounded queue waits and command timeouts.
* Trace Viewer:Inspect model conversations as ordered steps with roles, Agent identity, tool rounds, previews, and cost.
* Skills:Author or import a Skill and invoke it in the same Agent run, with safer rollback for failed imports.
* Agent activity:Render system events as distinct turns and hold live activity to one stable row.
* MCP reliability:Send per-request headers without hiding tools, coordinate OAuth refresh across replicas, and preserve credentials through provider outages.
* Performance:Stream Markdown incrementally, virtualize model search, and reduce completed Agent message rendering work.

Read thefull v0.8.8-rc4 changelog.

# ✨ Features

* 🖥️UI & Experienceinspired by ChatGPT with enhanced design and features
* 🤖AI Model Selection:Anthropic (Claude), AWS Bedrock, OpenAI, Azure OpenAI, Google, Vertex AI, OpenAI Responses API (incl. Azure)Custom Endpoints: Use any OpenAI-compatible API with LibreChat, no proxy requiredCompatible withLocal & Remote AI Providers:Ollama,AMD Lemonade, groq, Cohere, Mistral AI, Apple MLX, koboldcpp, together.ai,OpenRouter, Helicone, Perplexity, ShuttleAI, Deepseek, Qwen, and more
* Anthropic (Claude), AWS Bedrock, OpenAI, Azure OpenAI, Google, Vertex AI, OpenAI Responses API (incl. Azure)
* Custom Endpoints: Use any OpenAI-compatible API with LibreChat, no proxy required
* Compatible withLocal & Remote AI Providers:Ollama,AMD Lemonade, groq, Cohere, Mistral AI, Apple MLX, koboldcpp, together.ai,OpenRouter, Helicone, Perplexity, ShuttleAI, Deepseek, Qwen, and more
* Ollama,AMD Lemonade, groq, Cohere, Mistral AI, Apple MLX, koboldcpp, together.ai,
* OpenRouter, Helicone, Perplexity, ShuttleAI, Deepseek, Qwen, and more
* 🔧Code Interpreter API:Secure, Sandboxed Execution in Python, Node.js (JS/TS), Go, C/C++, Java, PHP, Rust, and FortranSeamless File Handling: Upload, process, and download files directlyNo Privacy Concerns: Fully isolated and secure executionOpen-Source & Self-Hostable: powered byClickHouse/code-interpreter
* Secure, Sandboxed Execution in Python, Node.js (JS/TS), Go, C/C++, Java, PHP, Rust, and Fortran
* Seamless File Handling: Upload, process, and download files directly
* No Privacy Concerns: Fully isolated and secure execution
* Open-Source & Self-Hostable: powered byClickHouse/code-interpreter
* 🔦Agents & Tools Integration:LibreChat Agents:No-Code Custom Assistants: Build specialized, AI-driven helpersAgent Marketplace: Discover and deploy community-built agentsCollaborative Sharing: Share agents with specific users and groupsFlexible & Extensible: Use MCP Servers, tools, file search, code execution, and moreSkills: Create reusableSKILL.mdinstruction bundles for manual, automatic, or always-on agent workflowsAgent Plugins: Experimentally bundle deployment Skills and MCP servers into startup-loaded packagesSubagents: Delegate focused work to isolated child agent runs with their own context windowsAgent Management API: Automate Agent, file, and Skill management with deployment-bound OIDC clientsAttached Code Workspaces: Let Agents inspect, search, edit, and run commands in managed or personal workspaces (highly experimental)Compatible with Custom Endpoints, OpenAI, Azure, Anthropic, AWS Bedrock, Google, Vertex AI, Responses API, and moreModel Context Protocol (MCP) Supportfor Tools
* LibreChat Agents:No-Code Custom Assistants: Build specialized, AI-driven helpersAgent Marketplace: Discover and deploy community-built agentsCollaborative Sharing: Share agents with specific users and groupsFlexible & Extensible: Use MCP Servers, tools, file search, code execution, and moreSkills: Create reusableSKILL.mdinstruction bundles for manual, automatic, or always-on agent workflowsAgent Plugins: Experimentally bundle deployment Skills and MCP servers into startup-loaded packagesSubagents: Delegate focused work to isolated child agent runs with their own context windowsAgent Management API: Automate Agent, file, and Skill management with deployment-bound OIDC clientsAttached Code Workspaces: Let Agents inspect, search, edit, and run commands in managed or personal workspaces (highly experimental)Compatible with Custom Endpoints, OpenAI, Azure, Anthropic, AWS Bedrock, Google, Vertex AI, Responses API, and moreModel Context Protocol (MCP) Supportfor Tools
* No-Code Custom Assistants: Build specialized, AI-driven helpers
* Agent Marketplace: Discover and deploy community-built agents
* Collaborative Sharing: Share agents with specific users and groups
* Flexible & Extensible: Use MCP Servers, tools, file search, code execution, and more
* Skills: Create reusableSKILL.mdinstruction bundles for manual, automatic, or always-on agent workflows
* Agent Plugins: Experimentally bundle deployment Skills and MCP servers into startup-loaded packages
* Subagents: Delegate focused work to isolated child agent runs with their own context windows
* Agent Management API: Automate Agent, file, and Skill management with deployment-bound OIDC clients
* Attached Code Workspaces: Let Agents inspect, search, edit, and run commands in managed or personal workspaces (highly experimental)
* Compatible with Custom Endpoints, OpenAI, Azure, Anthropic, AWS Bedrock, Google, Vertex AI, Responses API, and more
* Model Context Protocol (MCP) Supportfor Tools
* 🔍Web Search:Search the internet and retrieve relevant information to enhance your AI contextCombines search providers, content scrapers, and result rerankers for optimal resultsCustomizable Jina Reranking: Configure custom Jina API URLs for reranking servicesLearn More →
* Search the internet and retrieve relevant information to enhance your AI context
* Combines search providers, content scrapers, and result rerankers for optimal results
* Customizable Jina Reranking: Configure custom Jina API URLs for reranking services
* Learn More →
* 🪄Generative UI with Code Artifacts:Code Artifactscreate React, HTML, and Mermaid content directly in chatOpen previews fullscreen and export Mermaid diagrams as SVG or PNG
* Code Artifactscreate React, HTML, and Mermaid content directly in chat
* Open previews fullscreen and export Mermaid diagrams as SVG or PNG
* 🎨Image Generation & EditingText-to-image and image-to-image withGPT-Image-1Text-to-image withDALL-E (3/2),Stable Diffusion,Flux, or anyMCP serverProduce stunning visuals from prompts or refine existing images with a single instruction
* Text-to-image and image-to-image withGPT-Image-1
* Text-to-image withDALL-E (3/2),Stable Diffusion,Flux, or anyMCP server
* Produce stunning visuals from prompts or refine existing images with a single instruction
* 💾Presets & Context Management:Create, Save, & Share Custom PresetsSwitch between AI Endpoints and Presets mid-chatEdit, Resubmit, and Continue Messages with Conversation branchingCreate and share prompts with specific users and groupsFork Messages & Conversationsfor Advanced Context controlCompact long conversations on demand while preserving recent context
* Create, Save, & Share Custom Presets
* Switch between AI Endpoints and Presets mid-chat
* Edit, Resubmit, and Continue Messages with Conversation branching
* Create and share prompts with specific users and groups
* Fork Messages & Conversationsfor Advanced Context control
* Compact long conversations on demand while preserving recent context
* 💬Multimodal & File Interactions:Upload and analyze images with Claude 3, GPT-4.5, GPT-4o, o1, Llama-Vision, and Gemini 📸Chat with Files using Custom Endpoints, OpenAI, Azure, Anthropic, AWS Bedrock, & Google 🗃️Copy messages as formatted rich text for documents, email, and collaboration apps
* Upload and analyze images with Claude 3, GPT-4.5, GPT-4o, o1, Llama-Vision, and Gemini 📸
* Chat with Files using Custom Endpoints, OpenAI, Azure, Anthropic, AWS Bedrock, & Google 🗃️
* Copy messages as formatted rich text for documents, email, and collaboration apps
* 🌎Multilingual UI:English, 中文 (简体), 中文 (繁體), العربية, Deutsch, Español, Français, ItalianoPolski, Português (PT), Português (BR), Русский, 日本語, Svenska, 한국어, Tiếng ViệtTürkçe, Nederlands, עברית, Català, Čeština, Dansk, Eesti, فارسیSuomi, Magyar, Հայերեն, Bahasa Indonesia, ქართული, Latviešu, ไทย, ئۇيغۇرچە
* English, 中文 (简体), 中文 (繁體), العربية, Deutsch, Español, Français, Italiano
* Polski, Português (PT), Português (BR), Русский, 日本語, Svenska, 한국어, Tiếng Việt
* Türkçe, Nederlands, עברית, Català, Čeština, Dansk, Eesti, فارسی
* Suomi, Magyar, Հայերեն, Bahasa Indonesia, ქართული, Latviešu, ไทย, ئۇيغۇرچە
* 🧠Reasoning UI:Dynamic Reasoning UI for Chain-of-Thought/Reasoning AI models like DeepSeek-R1
* Dynamic Reasoning UI for Chain-of-Thought/Reasoning AI models like DeepSeek-R1
* 🎨Customizable Interface:Customizable Dropdown & Interface that adapts to both power users and newcomersLight, dark, system, and high-contrast appearance modes
* Customizable Dropdown & Interface that adapts to both power users and newcomers
* Light, dark, system, and high-contrast appearance modes
* 📈Observability:Export traces and logs with OpenTelemetry and connect Langfuse for Agent and model insights
* Export traces and logs with OpenTelemetry and connect Langfuse for Agent and model insights
* 🌊Resumable Streams:Never lose a response: AI responses automatically reconnect and resume if your connection dropsMulti-Tab & Multi-Device Sync: Open the same chat in multiple tabs or pick up on another deviceProduction-Ready: Works from single-server setups to horizontally scaled deployments with Redis
* Never lose a response: AI responses automatically reconnect and resume if your connection drops
* Multi-Tab & Multi-Device Sync: Open the same chat in multiple tabs or pick up on another device
* Production-Ready: Works from single-server setups to horizontally scaled deployments with Redis
* 🗣️Speech & Audio:Chat hands-free with Speech-to-Text and Text-to-SpeechAutomatically send and play AudioSupports OpenAI, Azure OpenAI, and Elevenlabs
* Chat hands-free with Speech-to-Text and Text-to-Speech
* Automatically send and play Audio
* Supports OpenAI, Azure OpenAI, and Elevenlabs
* 📥Import & Export Conversations:Import Conversations from LibreChat, ChatGPT, Chatbot UIExport conversations as screenshots, markdown, text, json
* Import Conversations from LibreChat, ChatGPT, Chatbot UI
* Export conversations as screenshots, markdown, text, json
* 🔍Search & Discovery:Search all messages/conversations
* Search all messages/conversations
* 👥Multi-User & Secure Access:Multi-User, Secure Authentication with OAuth2, LDAP, & Email Login SupportBuilt-in Moderation, and Token spend tools
* Multi-User, Secure Authentication with OAuth2, LDAP, & Email Login Support
* Built-in Moderation, and Token spend tools
* 🎛️Admin Panel:Browser-based UI to manage users, groups, roles, and configuration overridesEdit settings and per-role/group permissions live, without redeployingBundled with the Docker Compose stacks for one-command setup
* Browser-based UI to manage users, groups, roles, and configuration overrides
* Edit settings and per-role/group permissions live, without redeploying
* Bundled with the Docker Compose stacks for one-command setup
* ⚙️Configuration & Deployment:Configure Proxy, Reverse Proxy, Docker, & many Deployment optionsUseS3 with CloudFrontfor stable media links, edge delivery, signed cookies, and secured downloadsUse completely local or deploy on the cloud
* Configure Proxy, Reverse Proxy, Docker, & many Deployment options
* UseS3 with CloudFrontfor stable media links, edge delivery, signed cookies, and secured downloads
* Use completely local or deploy on the cloud
* 📖Open-Source & Community:Completely Open-Source & Built in PublicCommunity-driven development, support, and feedback
* Completely Open-Source & Built in Public
* Community-driven development, support, and feedback

For a thorough review of our features, see our docs here📚

## 🪶 All-In-One AI Conversations with LibreChat

LibreChat is a self-hosted AI chat platform that unifies all major AI providers in a single, privacy-focused interface.

Beyond chat, LibreChat provides AI Agents, Model Context Protocol (MCP) support, Artifacts, Code Interpreter, custom actions, conversation search, and enterprise-ready multi-user authentication.

Open source, actively developed, and built for anyone who values control over their AI infrastructure.

## 🌐 Resources

GitHub Repo:

* RAG API:github.com/LibreChat-AI/rag-api
* Website:github.com/LibreChat-AI/librechat.ai

Other:

* Website:librechat.ai
* Documentation:librechat.ai/docs
* Blog:librechat.ai/blog

## 📝 Changelog

Keep up with the latest updates by visiting the releases page and notes:

* Releases
* Changelog

⚠️Please consult thechangelogfor breaking changes before updating.

## ⭐ Star History

## ✨ Contributions

Contributions, suggestions, bug reports and fixes are welcome!

For new features, components, or extensions, please open an issue and discuss before sending a PR.

If you'd like to help translate LibreChat into your language, we'd love your contribution! Improving our translations not only makes LibreChat more accessible to users around the world but also enhances the overall user experience. Please check out ourTranslation Guide.

## 💖 This project exists in its current state thanks to all the people who contribute

## 🎉 Special Thanks

We thankLocizefor their translation management tools that support multiple languages in LibreChat.