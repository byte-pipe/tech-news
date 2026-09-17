---
title: How AI Actually Calls an API? Tool Calling Explained from Scratch - DEV Community
url: https://dev.to/aws/how-ai-actually-calls-an-api-tool-calling-explained-from-scratch-4lf8
date: 2026-09-16
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-18T05:28:30.021107
---

# How AI Actually Calls an API? Tool Calling Explained from Scratch - DEV Community

# How AI Actually Calls an API? Tool Calling Explained from Scratch

## Overview
- Foundation models are static; they cannot fetch live data on their own.  
- “Tool calling” lets a model request external functions, receive the results, and incorporate them into its answer.  
- The model only decides *what* to call and *with which arguments*; your application executes the actual code.

## The Four‑Step Loop
1. **Prompt** – Send the user’s question together with a description of the allowed tools.  
2. **Decision** – The model replies either with a final answer or with a structured *toolUse* request (e.g., `call get_weather, city=Toronto`).  
3. **Execution** – Your code parses the request, runs the real function (hits the external API), and obtains the result.  
4. **Result Injection** – Return the result to the model as a *toolResult* message; the model then generates the final, grounded response.

## Describing a Tool
- A tool is defined by three components supplied to the model:
  - **name** – identifier used in the request.  
  - **description** – plain‑English purpose of the tool.  
  - **inputSchema** – JSON schema specifying required arguments and their types.  
- Example (weather tool):
  ```json
  {
    "toolSpec": {
      "name": "get_weather",
      "description": "Get the current weather for a single city.",
      "inputSchema": {
        "json": {
          "type": "object",
          "properties": {
            "city": { "type": "string", "description": "A plain city name, e.g. Toronto or Paris." }
          },
          "required": ["city"]
        }
      }
    }
  }
  ```

## Single‑Tool Demo (Weather)
1. User asks: “Do I need an umbrella in Toronto today?”  
2. Model returns a `toolUse` request with `name: get_weather` and `city: Toronto`.  
3. Application calls `get_weather("Toronto")`, fetches data from Open‑Meteo, and packages it as a `toolResult`.  
4. Model receives the result and answers: “Based on the current weather in Toronto, you probably don’t need an umbrella right now.”  

The flow is linear: **question → tool request → execution → result → final answer**.

## Adding a Second Tool (Current Date)
- When asked “What’s today’s date?” the model initially replies it lacks the information because only the weather tool is available.  
- Adding a `get_current_datetime` tool (name, description, empty schema) enables the model to request the current date, follow the same loop, and produce an up‑to‑date answer.

## Injection Trick (Hand‑off vs. Direct Call)
- The model never runs code; it only emits a structured request.  
- Your surrounding code acts as the “hands” that:
  - Detect `toolUse` messages,  
  - Invoke the corresponding real function,  
  - Return the outcome as `toolResult`.  
- This separation keeps the model sandboxed while still allowing dynamic, real‑time data retrieval.

## Key Takeaways
- **Model = decision maker**; **Application = executor**.  
- Tool descriptions are the only prompt data the model uses to decide when and how to call a tool.  
- The four‑step loop works with any number of tools; each request is independent and can be chained if needed.  
- Adding appropriate tools eliminates “I don’t know” responses and reduces hallucinations by grounding answers in live data.