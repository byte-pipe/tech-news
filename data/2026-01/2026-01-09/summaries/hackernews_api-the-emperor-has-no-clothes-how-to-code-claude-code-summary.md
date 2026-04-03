---
title: The Emperor Has No Clothes: How to Code Claude Code in 200 Lines of Code - Mihail Eric
url: https://www.mihaileric.com/The-Emperor-Has-No-Clothes/
date: 2026-01-08
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-01-09T11:16:30.867678
screenshot: hackernews_api-the-emperor-has-no-clothes-how-to-code-claude-code.png
---

# The Emperor Has No Clothes: How to Code Claude Code in 200 Lines of Code - Mihail Eric

## Implementing a Functional Coding Agent from Scratch (Claude Code)

### Introduction
Today, we'll explore creating a functional coding agent using straightforward Python. Our goal is not magic, but rather to design a tool that allows users to converse with powerful Large Language Models (LLMs) like Claude.

### Mental Model

A decoding process occurs as follows:

1. Receive instructions (e.g., "Create a new file with a hello world function")
2. Decode an action (or multiple actions) based on the LLM's context
3. Execute the decoded action locally
4. Send results back to the LLM for further processing

### Essential Tools

*   Read Files tool: allows the LMM to access project files
*   List Files tool: enables navigation through project directories
*   Edit Files tool: permits code modifications

For our purposes, we need three additional capabilities:

*   **Create** tool: facilitates file creation
*   **List** tool: enables navigating project directories
*   **Edit** tool: gives directives for creating and modifying code

### Setting Up the Scaffolding

We start with a basic import of necessary libraries:

```python
import os
```

Next, we need to establish an API client using OpenAI's LLM provider (anthropic):

```python
import anthropic
```

**API Key**: Set your own ant-hropic api key in `.env` file.

We then define our Claude client and load the environment variables:

```python
claude_client = anthropic(
    api_key os.environ['ANTHROPIC_API_KEY']
)
```

**Scaffolding**

Finally, we set up utility functions to resolve terminal colors and provide a path resolver for handling absolute paths on Unix-like systems:

```python
from typing import Dict, List

def resolve_abs_path(path_str: str) -> Path:
    """
    Returns the resolved file path by expanding user home directory if necessary.

    Parameters:
    path_str (str): String representing the full or relative path

    Returns:
    Path
    """
    if not Path(path_str).is_absolute():
        return (
            os.path.expanduser("~")
            .path.resolve()
            .joinpath(str(Path(path_str)))
        )
```

### Tool Implementation

#### File Read Tool

```python
def read_file_tool(filename: str) -> Dict[str, Any]:
    """
    Retrieves the full content of a provided file.

    Parameters:
    filename (str): Name of the file to be accessed

    Returns:
    dict[str, Any]
    """
    return {
        "contents": open(filename).read(),
        "file_type": os.path.isfile(filename)
    }
```

#### Tool 1: Read File

```python
def read_file(filenames: List[str]) -> Dict[List[str], Any]:
    """
    Handles a list of file names by returning content of each file.

    Parameters:
    filenames (list): Names of files to be processed

    Returns:
    dict[list[str], Any]
    """
    return [
        read_file_tool(filename)
        for filename in filenames
        if os.path.isfile(filenamesfilename)
    ]
```

#### Tool 2: Create File

```python
def create_file(filename: str, content: str) -> None:
    """
    Creates a new file at the specified path using provided content.

    Parameters:
    filename (str): Name of the file to be created

    Returns:
    None
    """
    with open(filename, "w") as f:
        f.write(content)
```

#### Tool 3: Edit File

```python
def edit_file(filenames: List[str], content: str) -> None:
    """
    Modifies a list of file names by updating their respective contents.

    Parameters:
    filenames (list): Names of files to be modified

    Returns:
    dict[list[str], Any]

    Note: This tool is currently experimental and may not work as described
          in Claude's documentation.
    """
    for filename in filenames:
        # For example, update existing code in this file using
        # Claude's Python interpreter.
        claude_content = read_file_tool(filename)
        create_file(
            filename,
            f"{claude_content['contents']}\nsend content back to LLM\n"
            + ("  (update files)\n" if claudes_content["file_type"] else "")
            + "\n"
        )
```

### Conclusion

In summary, we've demonstrated how to create a functional coding agent using Python, showcasing essential tools like `read_file`, `create_file`, and `edit_file`. These basic capabilities can be extended with additional features when working closely with powerful LLMs like Claude.
