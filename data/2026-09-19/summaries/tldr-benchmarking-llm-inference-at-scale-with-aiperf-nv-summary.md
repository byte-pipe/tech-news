---
title: Benchmarking LLM Inference at Scale with AIPerf | NVIDIA Technical Blog
url: https://developer.nvidia.com/blog/benchmarking-llm-inference-at-scale-with-aiperf
date: 2026-09-19
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-19T06:01:25.780539
---

# Benchmarking LLM Inference at Scale with AIPerf | NVIDIA Technical Blog

# Benchmarking LLM Inference at Scale with AIPerf

## Overview
- Traditional load generators (single‑process scripts, curl, asyncio) become bottlenecks due to Python’s GIL and limited concurrency, leading to unreliable benchmark results.  
- NVIDIA AIPerf is introduced as a fast‑to‑configure, multiprocess load client that avoids client‑side bottlenecks and provides actionable output.

## What AIPerf Does Differently
- **Clean architectural break** from GenAI‑Perf; no longer built on top of Perf Analyzer.  
- **Multiprocess design**: separate worker processes generate load, record‑processor services handle results, coordination via ZMQ prevents the client from limiting throughput.  
- **Broad workload support**: 15+ endpoint types (chat, ranking, image generation, etc.) and public datasets such as ShareGPT, Mooncake, Baseten, WEKA AgentX.  
- **Configurable load shapes**: constant, Poisson, gamma arrival patterns with tunable burstiness, gradual ramp‑up, and synthetic distributions (vLLM/SGLang range‑ratio) for realistic traffic modeling.

## Example Benchmark: Synthetic ISL/OSL on vLLM
1. **Start the server**  
   ```bash
   docker pull vllm/vllm-openai:latest
   docker run --gpus all -p 8000:8000 -e HF_TOKEN vllm/vllm-openai:latest \
     --model Qwen/Qwen3-0.6B \
     --reasoning-parser qwen3 \
     --host 0.0.0.0 --port 8000
   ```
2. **Install AIPerf** (using `uv`)  
   ```bash
   uv tool install aiperf
   # or in a virtual environment
   uv venv venv
   source venv/bin/activate
   uv pip install aiperf
   ```
   *Note: on aarch64 the `crick` dependency requires a C toolchain.*  
3. **Run the benchmark**  
   ```bash
   aiperf profile \
     --model Qwen/Qwen3-0.6B \
     --endpoint-type chat \
     --streaming \
     --url localhost:8000 \
     --synthetic-input-tokens-mean 128 \
     --synthetic-input-tokens-stddev 0 \
     --output-tokens-mean 128 \
     --output-tokens-stddev 0 \
     --extra-inputs min_tokens:128 \
     --extra-inputs ignore_eos:true
   ```
   - `stddev 0` pins both input and output token counts to 128, reproducing a static benchmark.  
   - `min_tokens:128` and `ignore_eos:true` force the model to emit the full token count, ensuring consistent throughput numbers.  
   - `--streaming` is required to capture Time‑to‑First‑Token (TTFT) and Inter‑Token‑Latency (ITL).

## Metrics Reported by AIPerf
- **TTFT (Time to First Token)** – latency from request send to first token receipt; key for interactive use.  
- **ITL (Inter‑Token Latency)** – time between successive generated tokens; indicates decode‑phase health.  
- **Request Latency** – end‑to‑end time for the complete response (prefill + decode).  
- **Output Token Throughput** – total tokens generated per second across all concurrent requests.  

Each metric is presented with:
- Percentile breakdowns (p25, p50, p75, p90, p95, p99)  
- Minimum, maximum, average, and standard deviation values  
- Optional GPU telemetry when DCGM or `pynvml` is available  

Results are printed to the console and saved as CSV and JSON for further analysis.

## Next Steps and Resources
- Follow the AIPerf tutorials for advanced benchmarking scenarios.  
- Consult the Metrics Reference for detailed definitions of all reported measurements.  
- Review the NVIDIA Dynamo 1.0 documentation for multi‑node inference benchmarking.