---
title: Can I opt out of my input or output data being used for training? | Mistral Help Center
url: https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training
date: 2026-09-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-03T07:21:18.398900
---

# Can I opt out of my input or output data being used for training? | Mistral Help Center

# Can I opt out of my input or output data being used for training? | Mistral Help Center

## Overview
- Mistral may include user‑provided content (conversations, documents, etc.) in model training.
- Users have full control and can opt out at any time; the process varies by service.

## Opt‑out for Vibe (Admin panel)
- Default: Vibe users are **not** opted out; Vibe Enterprise customers are opted out by default.
- To opt out:
  1. Go to **Vibe** under the **Manage** section.
  2. In the **Privacy** section, disable the toggle **Allow your interactions to be used to train our models**.
- Uploaded documents are treated as input data; opting out prevents their use in training.
- After confirmation, Mistral stops using your input and output data for training.

## Opt‑out for Vibe (Mobile app – iOS & Android)
- Steps:
  1. Open the app’s **Settings** page.
  2. Select **Data & Account Controls** under **Account**.
  3. Deselect the **Enable data sharing** checkbox.

## Opt‑out for Mistral Studio and API (Admin panel)
- Customers can opt out at any time.
- To opt out:
  1. In the Admin panel, open the **Privacy** menu on the left navigation.
  2. Under **Anonymous improvement data**, disable the toggle to block API calls and related data from training.
- Note: Vibe and API toggles are independent; each must be set separately.

## Additional Resources
- Articles on Zero Data Retention, data usage for AI training, conversation visibility, GDPR rights, and handling data with the Memories feature.