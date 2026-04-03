---
title: April 2026 TLDR setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon) — auto-start, preload, and keep-alive · GitHub
url: https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5
date: 2026-04-03
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:05:16.091584
---

# April 2026 TLDR setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon) — auto-start, preload, and keep-alive · GitHub

# April 2026 TLDR Setup for Ollama + Gemma 4 26B on a Mac mini (Apple Silicon)

## Prerequisites
- Mac mini with Apple Silicon (M1‑M5)  
- At least 24 GB unified memory for Gemma 4 26B  
- macOS with Homebrew installed  

## Installation & Startup
- Install Ollama via Homebrew cask:  
  `brew install --cask ollama-app`  
- Launch the app: `open -a Ollama` (icon appears in menu bar)  
- Verify server: `ollama list`  
- Pull the model: `ollama pull gemma4:26b` (~17 GB)  
- Test the model: `ollama run gemma4:26b`  
- Check GPU acceleration: `ollama ps` (e.g., 14 %/86 % CPU/GPU)  

## Auto‑Start & Keep‑Alive
### Enable Launch at Login
- Ollama menu → “Launch at Login” **or** add Ollama to System Settings → General → Login Items.  

### Auto‑Preload Model on Startup
- Create launch agent `~/Library/LaunchAgents/com.ollama.preload-gemma4.plist` with the following content:  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.ollama.preload-gemma4</string>
  <key>ProgramArguments</key>
  <array>
    <string>/opt/homebrew/bin/ollama</string>
    <string>run</string>
    <string>gemma4:26b</string>
    <string></string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>StartInterval</key><integer>300</integer>
  <key>StandardOutPath</key><string>/tmp/ollama-preload.log</string>
  <key>StandardErrorPath</key><string>/tmp/ollama-preload.log</string>
</dict>
</plist>
```  

- Load the agent:  
  `launchctl load ~/Library/LaunchAgents/com.ollama.preload-gemma4.plist`  

This sends an empty prompt every 5 minutes, keeping the model warm.  

### Keep Models Loaded Indefinitely
- Set environment variable: `launchctl setenv OLLAMA_KEEP_ALIVE "-1"`  
- Restart Ollama.  
- To persist across reboots, add `export OLLAMA_KEEP_ALIVE="-1"` to `~/.zshrc` or create a dedicated launch agent.  

## Verification
- Server running: `ollama list`  
- Model in memory: `ollama ps` (should show “Forever” status)  
- Launch agent active: `launchctl list | grep ollama`  

## API Access
- Local API endpoint: `http://localhost:11434`  
- Example OpenAI‑compatible request:  

```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "gemma4:26b",
        "messages": [{"role": "user", "content": "Hello"}]
      }'
```  

## Useful Commands
- `ollama list` – list downloaded models  
- `ollama ps` – show running models & memory usage  
- `ollama run gemma4:26b` – interactive chat  
- `ollama stop gemma4:26b` – unload model from memory  
- `ollama pull gemma4:26b` – update model to latest version  
- `ollama rm gemma4:26b` – delete model  

## Uninstall / Remove Auto‑Start
- Unload and delete preload agent:  
  `launchctl unload ~/Library/LaunchAgents/com.ollama.preload-gemma4.plist`  
  `rm ~/Library/LaunchAgents/com.ollama.preload-gemma4.plist`  
- Uninstall Ollama: `brew uninstall --cask ollama-app`  

## Recent Ollama Changes (v0.19+, March 31 2026)
- **MLX backend** automatically used on Apple Silicon; extra acceleration on M5 series chips.  
- **NVFP4 support** for NVIDIA‑optimized models, reducing memory bandwidth and storage while preserving accuracy.  
- **Improved caching**: lower memory utilization, intelligent checkpoints, smarter eviction of shared prefixes.  

## Notes
- Loaded Gemma 4 26B consumes ~20 GB; on a 24 GB Mac mini only ~4 GB remain for the OS and other apps. Close memory‑heavy applications before running.  

## References
- Ollama MLX Blog Post (Mar 31 2026)  
- Ollama v0.20.0 Release notes  
- Google DeepMind Gemma 4 Announcement