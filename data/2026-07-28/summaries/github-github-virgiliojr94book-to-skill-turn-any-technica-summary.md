---
title: GitHub - virgiliojr94/book-to-skill: Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work. · GitHu...
url: https://github.com/virgiliojr94/book-to-skill
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-28T11:45:17.111514
---

# GitHub - virgiliojr94/book-to-skill: Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work. · GitHu...

**Book-to-Skill**

# Overview

The Book-to-Skill (BTS) tool turns any technical book, document folder, or collection of sources into a unified agent skill. It is designed to be easily integrated with popular development tools such as GitHub Copilot CLI, Amp, and Claude Code.

**Key Features**

* **Dumps data directly into the skills directory**: BTS generates a new skill in your agent's skills directory, containing all the information from the original book.
* **Loaded on-demand**: The agent loads the skill to answer questions and perform tasks by reading from the actual content of the books.
* **No hallucinations or digging through PDFs**: BTS ensures accurate answers are provided without requiring manual searches or note-taking.

**How It Works**

1. Choose a file, folder, or glob within the book's directory.
2. The agent builds the skill by distilling the book into frameworks, decision rules, anti-patterns, and per-chapter files.
3. Your agent loads the skill on demand, reading from the corresponding chapter files ( structured data).

**Benefits**

* **Elevates productivity**: Save time and effort searching for answers to your questions or understanding complex concepts.
* **Improves knowledge retention**: By directly engaging with the content of books, you'll be able to retain knowledge more effectively.

**Installation**

Run `book-to-skill <filename>` (where `<filename>` is the desired book file). The agent will generate a new skill in its skills directory. To use it with other tools:

* **GitHub Copilot CLI**: Run `copilot cli <tool> /books/<slug>` to execute BTS.
* **Amp**: Run `amp /books/<slug>` to activate BTS for Amp users.
* **Claude Code**: Run `claude <book_file> /skills/*` to integrate BTS with Claude Code skills.