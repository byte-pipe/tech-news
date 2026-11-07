---
title: GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub
url: https://github.com/astral-sh/ruff
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:08.773593
---

# GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub

# Ruff – Extremely Fast Python Linter and Formatter

## Overview
- Ruff is a Python linter and code formatter written in Rust, offering 10‑100× speed improvements over traditional tools such as Flake8 and Black.  
- Provides drop‑in compatibility with Flake8, isort, Black, and many popular Flake8 plugins (e.g., flake8‑bugbear).  
- Supports automatic fixing of issues, built‑in caching, and hierarchical configuration via `pyproject.toml`, `ruff.toml`, or `.ruff.toml`.  
- Designed for monorepos and integrates with editors (VS Code, etc.), pre‑commit hooks, GitHub Actions, and various package managers.

## Key Features
- **Performance:** 10‑100× faster than existing linters/formatters; some users report up to 1000× speed gains.  
- **Installation:** Available on PyPI (`ruff`), installable via `uv`, `pip`, `pipx`, Homebrew, Conda, or standalone installers for macOS, Linux, and Windows.  
- **Usage:**  
  - Lint: `ruff check [path]` (supports glob patterns and argument files).  
  - Format: `ruff format [path]`.  
  - Can be invoked as a pre‑commit hook or GitHub Action.  
- **Rules:** Over 900 built‑in rules, including native re‑implementations of common Flake8 plugins.  
- **Configuration defaults:**  
  - Excludes typical VCS and build directories.  
  - Line length 88, indent width 4, target Python 3.11.  
  - All rules are fixable by default when `--fix` is used.  
- **Editor Integration:** First‑party extensions for VS Code and other editors.

## Adoption
- Used in major open‑source projects such as Apache Airflow, Apache Superset, FastAPI, Hugging Face, Pandas, and SciPy.  
- Backed by Astral, the creators of `uv` and `ty`.

## Testimonials
- Sebastián Ramírez (FastAPI): “Ruff is so fast I add intentional bugs just to confirm it’s running.”  
- Nick Schrock (Elementl): “Nearly 1000× faster; our 250k‑LOC codebase checks in 0.4 s vs. 2.5 min with pylint.”  
- Bryan Van de Ven (Bokeh, Conda): “150‑200× faster than flake8; whole‑repo scan in ~0.2 s.”  
- Timothy Crosley (isort): “So fast I doubted it was working until I introduced errors.”  
- Tim Abbott (Zulip): “Ridiculously fast—ruff is amazing.”

## Getting Started
1. **Install** (example with `uv`): `uv tool install ruff@latest` or `pip install ruff`.  
2. **Run lint**: `ruff check` (or specify paths).  
3. **Run format**: `ruff format`.  
4. **Configure** via `pyproject.toml` or `ruff.toml` to customize rule selection, line length, target Python version, etc.

## Resources
- Documentation, playground, and detailed rule list are available in the repository.  
- Community contributions and support guidelines are outlined in `CONTRIBUTING.md`.  
- License: Open source under the MIT License.