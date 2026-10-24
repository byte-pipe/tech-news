---
title: Bringing uv and ty together
url: https://astral.sh/blog/uv-ty-integration
date: 2026-10-20
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-24T14:33:56.993919
---

# Bringing uv and ty together

# Bringing uv and ty together

## Expertise

On [October 13, 2026](# bringing-uv-and-ty-together), Astral announced an experimental integration between uv and ty, two key components of the Python ecosystem.

### tl;dr

Experimental uv-ty integration enables 1st-class support for Python scripts on both CLI and editor, and a unified uv checkcommand. This integration builds towards an integrated Astral toolchain that unifies traditionally separate capabilities.

#### First-class support for Python scripts

With uv, scripts can declare dependencies and Python version requirements inline. uv ensures an environment is set up for each script, enabling additional features like checkin, completions, hover, and Go to Definition.

### Enhanced Integration

- **Inline Metadata**: Declare dependencies inline with PEP 723 and save to sync with uv. This allows uv to prepare the script's environment.
- **Unified checkcommand**: Starting with uv check, ty provides a unified diagnostic interface to uv, introducing support for typing and linting.

### Future Developments

- **Auto-environment Setup**: Enable script support by default over time.
- **Script Integration**: Enabling automatic environment setup for standard Python projects.