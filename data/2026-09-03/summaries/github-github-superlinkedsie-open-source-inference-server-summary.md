---
title: GitHub - superlinked/sie: Open-source inference server and production cluster for all the models your agent needs. · GitHub
url: https://github.com/superlinked/sie
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-03T07:21:41.212142
---

# GitHub - superlinked/sie: Open-source inference server and production cluster for all the models your agent needs. · GitHub

# SIE (Superlinked Inference Engine) – Overview

## About the project
- Open‑source inference server that consolidates all models an agent needs into a single API.
- Provides OpenAI‑compatible endpoints: `/v1/embeddings`, `/v1/chat/completions`, `/v1/completions`, `/v1/responses`.
- Pre‑configured catalog includes over 100 models (e.g., Stella, SPLADE, Qwen3, GLiNER, SigLIP) with MTEB‑benchmarked embeddings and retrieval models.
- Supports simultaneous model serving with on‑demand loading and LRU eviction.
- Deployable via Kubernetes/Helm with load‑balancing gateway, KEDA autoscaling, and Grafana dashboards.
- Integrates with LangChain, LlamaIndex, Haystack, DSPy, CrewAI, Chroma, Qdrant, Weaviate, LanceDB.

## Development workflow
- Toolchain bootstrap: `./tools/init.sh` (installs Python 3.12, Rust, Node.js, Helm via `mise`).
- Common tasks executed with `mise run <task>`:
  - `test`, `lint`, `typecheck`, `serve`, `rust-check`, `rust-test`, `gateway-test`, `server-sidecar-test`.
- Python workspace uses locked dependencies (`uv sync --frozen`); native audio builds are optional (requires CMake).

## Core tasks and associated models
| Task | Description | Example models |
|------|-------------|----------------|
| Search | Embed, match, and rerank for context retrieval | bge‑m3, splade‑v3, colbertv2, qwen3‑reranker |
| Document to markdown | Convert PDFs, Office files, scans to clean markdown | lightonocr, glm‑ocr, mineru, paddleocr‑vl, docling |
| Structured output | Produce schema‑valid JSON, extracted or generated | gliner2, nuner‑zero, qwen3.6‑27b |
| Guard content | Safety verdict with probability threshold | granite‑guardian‑2b |
| Run agent loop | Plan steps, call tools with an LLM (streaming supported) | qwen3.6‑27b |

## Quickstart guide
1. **Start the server**  
   - macOS/Linux (native, Python 3.12):  
     ```bash
     pip install "sie-server[local]" && sie-server serve
     ```  
   - Linux + NVIDIA GPU (Docker, default image):  
     ```bash
     docker run --gpus all -p 8080:8080 -v sie-hf-cache:/app/.cache/huggingface ghcr.io/superlinked/sie-server:latest-cuda12-default
     ```  
   - GPU image with OCR models: `latest-cuda12-transformers5`.  
   - CPU‑only image: `latest-cpu-default`.  

   Verify readiness: `curl http://localhost:8080/readyz` → `ok`.

2. **Make a test request** (embeddings endpoint):
   ```bash
   curl http://localhost:8080/v1/embeddings \
        -H 'Content-Type: application/json' \
        -d '{"model":"sentence-transformers/all-MiniLM-L6-v2","input":"Hello world"}'
   ```

3. **Install SDKs**  
   - Python: `pip install sie-sdk`  
   - TypeScript: `npm install @superlinked/sie-sdk` (pnpm/yarn also supported)

4. **Example Python usage**
   ```python
   from sie_sdk import SIEClient, Item

   client = SIEClient("http://localhost:8080")

   # Embeddings
   emb = client.encode("sentence-transformers/all-MiniLM-L6-v2", Item(text="Hello world"))
   print(emb["dense"].shape)   # (384,)

   # Rerank
   scores = client.score(
       "cross-encoder/ms-marco-MiniLM-L-6-v2",
       Item(text="What is machine learning?"),
       [Item(text="ML learns from data."), Item(text="The weather is sunny.")],
   )
   print(scores["scores"][0])

   # Entity extraction
   ents = client.extract(
       "urchade/gliner_multi-v2.1",
       Item(text="Tim Cook is the CEO of Apple."),
       labels=["person", "organization"],
   )
   print(ents["entities"][0])
   ```

5. **Text generation (GPU image)**
   - Stop the first server, start the generation image (`latest-cuda12-sglang`), then:
   ```python
   result = client.generate(
       "Qwen/Qwen3-0.6B",
       "Reply with a single word: the capital of France.",
       max_new_tokens=16,
       temperature=0.0,
   )
   print(result["text"])   # Paris
   ```

   Apple Silicon generation via MLX is documented separately.

## Production deployment
- Helm chart provides load‑balancing gateway, KEDA autoscaling (scale‑to‑zero), and Grafana dashboards.
- Public Terraform modules for Alibaba Cloud ACK, AWS EKS, Azure AKS, Google GKE.
- Example Helm install (GKE overlay):
  ```bash
  helm upgrade --install sie-cluster oci://ghcr.io/superlinked/charts/sie-cluster \
       --namespace sie --create-namespace \
       --set hfToken.create=true \
       --set hfToken.value=YOUR_HF_TOKEN \
       -f https://raw.githubusercontent.com/superlinked/sie/main/deploy/helm/sie-cluster/values-gke.yaml
  ```
- All components are Apache 2.0 licensed.

## Telemetry
- SIE collects anonymous usage data (version, OS, architecture, GPU type) to improve the product.