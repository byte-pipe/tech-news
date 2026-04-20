# Migrating from Poetry + pipx to uv

## Why

uv replaces both Poetry and pipx with one faster tool:

- Rust-based: 10-100x faster installs and dependency resolution
- Single tool: no more Poetry + pipx split
- Same `pyproject.toml` — no changes to project files
- `uv tool install --editable .` replaces `pipx install --editable .`
- `uv run` / `uv sync` replace `poetry run` / `poetry install`

## Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Command mapping

| Poetry + pipx                       | uv                                     |
| ----------------------------------- | -------------------------------------- |
| `poetry install`                    | `uv sync`                              |
| `poetry run pytest`                 | `uv run pytest`                        |
| `poetry add package`                | `uv add package`                       |
| `poetry lock`                       | `uv lock`                              |
| `pipx install --editable . --force` | `uv tool install --editable . --force` |
| `pipx list`                         | `uv tool list`                         |

## pyproject.toml — add [project] table

uv requires a PEP 621 `[project]` table. Poetry uses `[tool.poetry]` — keep that for Poetry compatibility, but add `[project]` alongside it:

```toml
[project]
name = "your-project"
version = "0.1.0"
description = "..."
requires-python = ">=3.11,<4"

[tool.poetry]
# unchanged ...
```

Both tables can coexist. uv reads `[project]`, Poetry reads `[tool.poetry]`.

`[project.dependencies]` must also be populated — uv does not read `[tool.poetry.dependencies]`. Convert Poetry specifiers (`^1.0`) to pip-style (`>=1.0`).

For path dependencies, use `[tool.uv.sources]` instead of inline path specs:

```toml
[project.dependencies]
...
"rootlog",

[tool.uv.sources]
rootlog = { path = "../rootlog", editable = true }
```

## Dev dependencies

uv does not read `[tool.poetry.group.dev.dependencies]`. Add a `[dependency-groups]` section (PEP 735, natively supported by uv):

```toml
[dependency-groups]
dev = [
  "pytest>=8.0.0",
  "pytest-cov>=6.0.0",
  "pytest-mock>=3.14.0",
  "black>=25.0.0",
  "isort>=6.0.0",
  "flake8>=7.0.0",
  "mypy>=1.8.0",
]
```

`uv sync` installs all dependency groups by default. Both `[tool.poetry.group.dev.dependencies]` and `[dependency-groups]` can coexist — keep both for Poetry compatibility.

Without this, `uv run pytest` fails if `pytest.ini` has `addopts = --cov=src` (requires `pytest-cov`) since dev deps are never installed.

## Library packages (no CLI scripts)

For packages installed into the system/active environment rather than as isolated tools, use:

```bash
uv pip install -e . --system
```

This replaces `pip install -e . --break-system-packages`.

## update install.sh

Replace:

```bash
poetry install
pipx install --editable . --force
```

With:

```bash
uv sync
uv tool install --editable . --force
```

## Keep Poetry if needed

`pyproject.toml` is unchanged — Poetry still works alongside uv. Switch gradually: use uv for installs and day-to-day dev, keep Poetry only if a specific workflow requires it.

## .gitignore

Add `.venv` — uv creates it in the project directory:

```
.venv
```

## Notes

- uv respects `poetry.lock` — no need to regenerate
- `uv tool` installs into `~/.local/share/uv/tools/` (isolated, same as pipx)
- Editable installs mean path deps like `../chatbot` work without a build step
