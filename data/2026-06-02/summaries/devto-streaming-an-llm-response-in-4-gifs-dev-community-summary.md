---
title: Streaming an LLM response, in 4 GIFs - DEV Community
url: https://dev.to/jasmin/streaming-an-llm-response-in-4-gifs-16dh
date: 2026-05-31
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-02T06:01:54.185971
---

# Streaming an LLM response, in 4 GIFs - DEV Community

# Streaming an LLM response, in 4 GIFs

## 1. Why streaming exists
- Adding `"stream": true` to the request changes the response from a single JSON blob to a live token stream.  
- Non‑streaming: cursor blinks for ~4 s, then the whole answer appears at once.  
- Streaming: first word appears in ~300 ms and subsequent words arrive as they are generated.  
- Streaming does not speed up the model; it reduces perceived wait time for the user.

## 2. What’s on the wire
- With streaming enabled the API uses Server‑Sent Events (SSE) over a persistent HTTP connection.  
- Each SSE message contains a JSON payload; the text appears in `delta.text` inside `content_block_delta` events.  
- `stop_reason` is sent at the very end inside a `message_delta` event, not in the initial response.  
- Chunk boundaries are determined by the network, not by tokens or words.

## 3. Reading the stream
- The response body is a `ReadableStream` that can be iterated with `for await`.  
- Steps to process each chunk:
  1. Decode bytes to a string.  
  2. Append to a buffer.  
  3. Split the buffer on `\n\n` (SSE message separator).  
  4. Keep the last split piece in the buffer for the next iteration.  
  5. For each complete message, locate the `data:` line, strip the prefix, and `JSON.parse` it.  
  6. If `type` is `content_block_delta` and `delta.type` is `text_delta`, output `delta.text`.  
  7. If `type` is `message_delta`, read `delta.stop_reason`.  
- Sample Node.js code demonstrates this flow.

## 4. Three common bugs
- **Ghost stream**: the fetch continues after the user navigates away. Fix with an `AbortController` and call `abort()` when the stream should stop.  
- **Silent truncation**: an `error` event can appear mid‑stream, causing the response to end silently. Handle `type === "error"` and throw an exception.  
- **Split packet**: a single SSE message may be split across TCP packets; without buffering, `JSON.parse` fails. Keeping the incomplete fragment in the buffer (`buffer = messages.pop() ?? ""`) resolves this.

## 5. `stop_reason` in a stream
- The same four values (`end_turn`, `max_tokens`, `tool_use`, `stop_sequence`) appear inside a `message_delta` event near the stream’s end.  
- Ignoring `stop_reason` can hide cases where the model was cut off (e.g., due to `max_tokens`).

## 6. Things to try before the next post
1. Run the code with `"stream": true` and then with `"stream": false` to feel the difference in latency.  
2. Log `chunk.length` inside the loop to see the variability of network‑determined chunk sizes.  
3. Disconnect Wi‑Fi mid‑stream to observe error handling behavior.

## 7. What’s next
- The author’s TinyAgent now streams token‑by‑token responses and captures `stop_reason`, though it still lacks persistent memory.  
- Future posts will explore additional important details of streaming LLM responses.  

Happy coding!