---
title: The Emperor Has No Clothes: How to Code Claude Code in 200 Lines of Code - Mihail Eric
url: https://www.mihaileric.com/The-Emperor-Has-No-Clothes/
date: 2026-01-08
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-01-11T11:15:46.902282
screenshot: hackernews_api-the-emperor-has-no-clothes-how-to-code-claude-code.png
---

# The Emperor Has No Clothes: How to Code Claude Code in 200 Lines of Code - Mihail Eric

## Building a Functional Coding Agent from Scratch with Claude Code

*   Introduction
    *   Understanding how coding agents work
    *   The importance of tools in supporting these agents
*   Mental Model of Conversation
    *   Yousend a message to the LLM, receive response for tool call
    *   Local execution of tool calls on your project files
    *   Result is provided by the LLM, used as context
*   Essential Tools for Building a Coding Agent

    1.  **File Management**

        *   Three main tools needed:
            *   Read Files (resolve_abs_path)
                *   Reads file contents at given path
                *   Returned in dict containing filename and content
            *   List Files (list_files)
                *   Navigates project folder and lists files
                *   Returned as list of paths to target files
            *   Edit Files (edit_file_tool)
                *   Dynamically edits file contents at given path
                *   Returned in dict containing modified content

*   Setting Up the Scaffolding

    1.  **Basic Imports**

        -   Import Python and required modules
        -   Load environment variables from .env file using load_dotenv()
        -   Initialize OpenAI API client with provided key
        -   Import various utility functions

*   Implementing Tools

    ### Tool 1: Read File

        A simple tool that reads the contents of a given file

            ```python
def read_file_tool(filename: str) -> dict[str, Any]:
    # Resolve absolute path to target file
    full_path = resolve_abs_path(filename)

    # Load initial file contents from resolved path as string
    file_contents = open(full_path).read()

    return {
        "filename": filename,
        "content": file_contents,
    }
```

### Tool 2: List Files

        A tool that navigates the project folder and identifies files of interest

            ```python
def list_files(self):
    # Navigate to target directory path using resolve_abs_path
    path = resolve_abs_path("path_to_target_folder")

    # Initialize empty lists to store paths to target files
    file_paths = []

    return {
        "file_paths": file_paths,
    }
```

### Tool 3: Edit File

        A tool that dynamically edits the contents of a given file

            ```python
def edit_file_tool(self, filename: str):
    # Dynamically replace filename in contents with edited text
    edited_contents = self.edit_file(open(full_path, "r").read(), filename)

    return {
        "modified_content": edited_contents,
    }
```

*   Production Agent Claude Code

    *   Integrates all three tools into a single production agent
    *   Utilizes OpenAI API client and Python environment variables for communication
