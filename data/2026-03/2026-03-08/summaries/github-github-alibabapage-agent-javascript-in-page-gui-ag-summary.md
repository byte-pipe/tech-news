---
title: GitHub - alibaba/page-agent: JavaScript in-page GUI agent. Control web interfaces with natural language. · GitHub
url: https://github.com/alibaba/page-agent
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-03-08T07:25:57.081005
---

# GitHub - alibaba/page-agent: JavaScript in-page GUI agent. Control web interfaces with natural language. · GitHub

# Page Agent – In‑page JavaScript GUI Agent  

## Overview  
- A client‑side library that lets natural‑language commands control web interfaces directly from the page.  
- No browser extensions, headless browsers, or backend changes are required; everything runs as in‑page JavaScript.  

## Features  
- Simple integration: one script tag or npm package.  
- Text‑based DOM manipulation without screenshots, OCR, or multi‑modal LLMs.  
- Supports any LLM you provide (“bring your own LLM”).  
- Interactive UI with human‑in‑the‑loop feedback.  
- Optional Chrome extension for multi‑page workflows.  

## Typical Use Cases  
- **AI Copilot for SaaS** – embed an AI assistant with only a few lines of code.  
- **Smart Form Filling** – replace long click sequences with a single natural‑language instruction.  
- **Accessibility** – enable voice commands or screen‑reader‑style interaction for any web app.  
- **Multi‑page Agents** – coordinate actions across tabs via the optional extension.  

## Quick Start  

### One‑line demo integration  
```html
<script src="https://cdn.jsdelivr.net/npm/page-agent@1.5.2/dist/iife/page-agent.demo.js"
        crossorigin="true"></script>
```  
*Uses a free demo LLM API for evaluation only.*  

### npm installation & basic usage  
```bash
npm install page-agent
```
```javascript
import { PageAgent } from 'page-agent';

const agent = new PageAgent({
  model: 'qwen3.5-plus',
  baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
  apiKey: 'YOUR_API_KEY',
  language: 'en-US',
});

await agent.execute('Click the login button');
```  

Further programmatic details are in the documentation.  

## Contribution  
- Guidelines are in `CONTRIBUTING.md`.  
- Follow the Code of Conduct before submitting patches.  

## Acknowledgments  
- Built on concepts from the **browser-use** project (MIT‑licensed).  
- Third‑party dependencies and licenses are listed in `package.json`.  

## License  
- MIT License.  

## Repository Stats (as of March 2026)  
- Stars: 1.2 k  
- Forks: 115  
- Watchers: 6  
- Primary languages: TypeScript 82.3 %, JavaScript 11 %, CSS 6.2 %, HTML 0.5 %  

---  
*Page Agent enables natural‑language‑driven web automation without leaving the browser page.*