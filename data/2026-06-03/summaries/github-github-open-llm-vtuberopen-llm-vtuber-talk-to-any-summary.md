---
title: GitHub - Open-LLM-VTuber/Open-LLM-VTuber: Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face running locall...
url: https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-03T01:52:57.816128
---

# GitHub - Open-LLM-VTuber/Open-LLM-VTuber: Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face running locall...

# Open-LLM-VTuber Summary

## Overview
- Open-LLM-VTuber is a voice‑interactive AI companion that runs entirely offline.
- Provides real‑time voice conversation, visual perception, and a Live2D avatar.
- Available for Windows, macOS, and Linux with both web and desktop client modes.
- Designed as a customizable “VTuber” style companion rather than a generic chatbot.

## Key Features
- Cross‑platform support for macOS, Linux, and Windows; works with NVIDIA, non‑NVIDIA GPUs, CPU, or cloud APIs.
- Offline operation using local models; no internet connection required for core functionality.
- Web client and desktop client (including transparent‑background “pet” mode) for flexible placement on screen.
- Advanced interaction:
  - Visual perception via camera, screen recording, and screenshots.
  - Voice interruption handling so the AI does not hear its own output.
  - Touch feedback through clicks or drags.
  - Live2D expression control via backend emotion mapping.
  - Display of AI’s internal thoughts and proactive speaking.
  - Persistent chat logs for resuming conversations.
  - TTS translation (e.g., user chats in Chinese, AI speaks Japanese).
- Extensive model compatibility:
  - Large Language Models: Ollama, OpenAI‑compatible APIs, Gemini, Claude, Mistral, DeepSeek, Zhipu AI, GGUF, LM Studio, vLLM, etc.
  - Automatic Speech Recognition: sherpa‑onnx, FunASR, Faster‑Whisper, Whisper.cpp, Whisper, Groq Whisper, Azure ASR, etc.
  - Text‑to‑Speech: sherpa‑onnx, pyttsx3, MeloTTS, Coqui‑TTS, GPTSoVITS, Bark, CosyVoice, Edge TTS, Fish Audio, Azure TTS, etc.
- Highly customizable:
  - Simple module switching via configuration files.
  - Import custom Live2D models and modify prompts to shape persona.
  - Optional voice cloning for personalized voice output.

## Development Status
- Early‑stage project with active development.
- v2.0 is being rewritten; new feature requests should be directed to the developer community on Zulip.
- Ongoing bug fixes for v1 and processing of existing pull requests.

## Usage Notes
- Remote access requires HTTPS (or localhost) because the front‑end microphone only works in a secure context; set up a reverse proxy with HTTPS for non‑local access.
- Long‑term memory feature is temporarily removed but will return in future updates.

## Repository Highlights
- Main directories: `src/open_llm_vtuber`, `frontend`, `live2d-models`, `avatars`, `backgrounds`, `characters`, `scripts`, `doc`.
- Documentation available in multiple languages (English, Chinese, Korean, Japanese) and a FAQ in Chinese.
- Includes configuration templates, upgrade scripts, and Dockerfile for containerized deployment.