---
title: Regression: encrypted MultiAgentV2 messages remove readable task audit trail · Issue #28058 · openai/codex · GitHub
url: https://github.com/openai/codex/issues/28058
date: 2026-07-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:49:16.560634
---

# Regression: encrypted MultiAgentV2 messages remove readable task audit trail · Issue #28058 · openai/codex · GitHub

# Regression: encrypted MultiAgentV2 messages remove readable task audit trail

## Description
- The change introduced in PR #26210 encrypts MultiAgentV2 payloads, storing data only in `encrypted_content` and leaving `content` empty.
- While encryption improves privacy, it eliminates human‑readable task/message text from rollout history, trace logs, and audit surfaces.
- This regression affects any build with MultiAgentV2 enabled (post‑0.137.0) and appears when models invoke `spawn_agent`, `send_message`, or `followup_task`.

## Reproduction Steps
1. Run a Codex CLI version that includes the “Encrypt multi‑agent v2 message payloads” change.  
2. Have a model call `spawn_agent`, `send_message`, or `followup_task`.  
3. Inspect the parent rollout/history/trace for the sub‑agent task.  
4. Observe that the task/message appears only as ciphertext; no readable text is available.

## Expected Behavior
- Preserve a human‑readable, structured copy of the sub‑agent task/message locally for audit and debugging.
- Suggested approach: keep the encrypted field for model delivery **and** add a separate non‑encrypted audit field that is persisted in rollout/history metadata.

## Technical Details
- `InterAgentCommunication::new_encrypted` sets `content` to an empty string and stores the payload in `encrypted_content`.
- `to_model_input_item` emits only the encrypted payload when `encrypted_content` is present, omitting any plaintext.
- The helper `communication_from_tool_message` constructs encrypted communication without retaining the original plaintext, preventing any readable audit record.

## Related Issues
- PR #26210 – Encryption of MultiAgentV2 message payloads.  
- Issue #26753 – Schema validation failures for encrypted tool schemas (different problem).  

## Goal
- Implement a local audit persistence path that records the original task/message text while still delivering encrypted content to the recipient model, without reverting the encryption change.