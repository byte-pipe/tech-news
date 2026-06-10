---
title: Apache Burr (Incubating) - Build Reliable AI Agents and Applications
url: https://burr.apache.org/
date: 2026-06-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-11T06:02:00.129299
---

# Apache Burr (Incubating) - Build Reliable AI Agents and Applications

# Apache Burr (Incubating) – Build Reliable AI Agents and Applications

## Overview
- Apache Burr is an incubating Apache project that simplifies the development of AI‑driven applications, from simple chatbots to complex multi‑agent systems.  
- It is pure Python with no hidden magic, targeting developers who want a straightforward, composable interface.  

## Core API Example
- Uses decorators (`@action`) to declare actions that read and write state.  
- `ApplicationBuilder` assembles actions, transitions, initial state, and a tracker to create a runnable application.  
- Example snippet shows a chatbot action that appends LLM responses to a message list and runs the app with a single halt condition.  

## Key Features
- **Simple Python API** – Define actions and transitions directly in Python; no DSL or YAML required.  
- **Built‑in Observability** – Real‑time UI visualizes state changes, debugging, and tracing.  
- **Persistence & State Management** – Automatic state storage to disk, databases, or custom backends; supports resuming from checkpoints.  
- **Human‑in‑the‑Loop** – Pause execution for manual input, enabling approval workflows and interactive agents.  
- **Branching & Parallelism** – Execute actions in parallel, fan‑out/fan‑in, and compose sub‑applications into DAGs.  
- **Testing & Replay** – Replay past runs, unit‑test actions, and validate state transitions for production confidence.  

## Integrations
- **LLM Providers:** OpenAI, Anthropic, Instructor.  
- **Frameworks:** LangChain, Hamilton, Haystack.  
- **UI & Serving:** Streamlit, FastAPI.  
- **Utilities:** Pydantic (validation), PostgreSQL (storage).  

## Community & Adoption
- Hosted on GitHub with open‑source licensing; project page lists stars, PyPI downloads, and Discord members (numbers omitted).  
- Encourages contributions and integration with existing Python stacks without vendor lock‑in.  

## Testimonials
- *Ashish Ghosh, CTO, Peanut Robotics*: “Elegant yet comprehensive state management solved our AI‑driven robot rollout.”  
- *Ishita, Founder, Watto.ai*: “Modular AI building is a no‑brainer; the UI makes debugging a piece of cake.”  
- *Matthew Rideout, Staff Engineer, Paxton AI*: “No weird esoteric concepts—just what we needed for AI.”  
- *Rinat Gareev, Senior Solutions Architect, Provectus*: “State snapshots enable debugging, replay, and evaluation cases.”  
- *Hadi Nayebi, Co‑founder, CognitiveGraphs*: “More robust than LangChain, CrewAi, AutoGen, etc., for complex behaviors.”  
- *Aditya K., DS Architect, TaskHuman*: “Switched from LangChain to Burr in hours; dramatically faster time‑to‑production.”  
- *Reddit User, r/LocalLlama*: “Production‑ready and cuts code‑to‑prod time; Burr is the answer.”