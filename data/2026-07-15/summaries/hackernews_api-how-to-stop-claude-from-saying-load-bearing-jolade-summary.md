---
title: How to stop Claude from saying load-bearing | jola.dev
url: https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing
date: 2026-07-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:49:53.836398
---

# How to stop Claude from saying load-bearing | jola.dev

# How to stop Claude from saying load‑bearing | jola.dev

## Overview
- The post addresses frustration with Claude’s repetitive phrases like “honest takes” and “load‑bearing seams”.
- It proposes a simple hook‑based solution to replace unwanted vocabulary with custom text.

## Setup script
- Create a Python script (`wordswap.sh`) that:
  - Reads JSON from stdin.
  - Defines a dictionary of phrase‑to‑replacement mappings (e.g., “seam” → “whatchamacallit”, “load‑bearing” → “cooked”).
  - Uses regular expressions with word boundaries and case‑insensitive matching to substitute each phrase.
  - Outputs the modified JSON with the new `displayContent`.

## Installation steps
- Save the script to `~/.claude/hooks/wordswap.sh`.
- Make it executable: `chmod +x ~/.claude/hooks/wordswap.sh`.
- Edit `~/.claude/settings.json` to add the hook under the `MessageDisplay` block:

```json
{
  "hooks": {
    "MessageDisplay": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$HOME/.claude/hooks/wordswap.sh"
          }
        ]
      }
    ]
  }
}
```

- Restart Claude (start a new session) for the hook to take effect.

## Customization
- Users are encouraged to modify the `replacements` dictionary with phrases that better suit their preferences.

## Author
- Written by Johanna Larsson.  
- Contact: Bluesky @jola.dev.

## Related posts
- **Let libraries be libraries** (July 07, 2026) – rant about Elixir libraries running as applications.  
- **CI workflows on Tangled for Elixir** (July 04, 2026) – guide to setting up CI with specific Elixir/Erlang versions and PostgreSQL.  
- **Automatically syncing your blog to atproto and standard.site** (June 29, 2026) – side project for discovering and syncing blog content.