---
title: Hashcards: A Plain-Text Spaced Repetition System
url: https://borretti.me/article/hashcards-plain-text-spaced-repetition
date: 2025-12-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-15T11:14:24.192294
screenshot: hackernews_api-hashcards-a-plain-text-spaced-repetition-system.png
---

# Hashcards: A Plain-Text Spaced Repetition System

**HashCards: A Local-First Spaced Repetition System**

**Key Points:**

* Hashcards uses File System Review Schedule (FSRS) for scheduled reviews
* Centralized flashcard collection stored in directory of Markdown files
* Unique feature: doesn't use a database, instead using a Git repository and file system

**HashCards Design Decisions:**

* **No Database**: Maintains ownership of flashcard collection with Markdown files in Git repository
* **Simple Flashcard Creation**: "Lightweight markup" for writing flashcards similar to ordinary notes
* **Centralized Learning Interface**: Hashcards' web interface available on localhost:8000, allows review sessions to be managed directly from the app

**Benefits and Challenges:**

* **Ownership**: User has control over their flashcard collection and can use scripts to generate content using structured data
* **Convenience**: Can review and edit flashcards with preferred editor, track changes through Git repository, share on GitHub
* **Efficiency**: No need to dig into internal database, using standard Unix tools for querying and manipulation
