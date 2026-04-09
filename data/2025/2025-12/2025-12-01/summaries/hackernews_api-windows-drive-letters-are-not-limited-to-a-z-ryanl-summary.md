---
title: Windows drive letters are not limited to A-Z - ryanliptak.com
url: https://www.ryanliptak.com/blog/windows-drive-letters-are-not-limited-to-a-z/
date: 2025-11-30
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-01T11:17:52.272977
screenshot: hackernews_api-windows-drive-letters-are-not-limited-to-a-z-ryanl.png
---

# Windows drive letters are not limited to A-Z - ryanliptak.com

## Understanding Windows Drive Letters in Detail
=============================================

Windows drive letters are not limited to a-z letters. They can also include numbers.

### Creating a Drive Letter as an Alias

In this example, the text explains how to create a drive letter alias using the `subst` command in the Command Prompt or Windows Subsystem for Linux (WSL).

For instance, creating the alias `C:\foo` creates a drive-letter mapping from `C:` to `\?C:\foo`. This effectively allows you to treat `C:` as a drive letter.

### Understanding Drive Letters in NT Namespace Paths

The text also delves into why Windows is often referred to as being driven by an abstract "NT namespace". When working in high-level APIs, such as `CreateFileW`, the system converts absolute paths like `C:\foo` to its own unique namespace path. This enables easier interaction between different layers of system calls.

The Object Manager plays a crucial role here, as it contains a copy of all named objects. To understand this directory structure, it's essential to grasp concepts related to directory organization and how they relate to object management within Windows.

## Conclusion
-----------


Understanding how drive letters function in higher-level applications provides valuable insights into how the underlying system manages namespace paths. This nuanced knowledge is especially important when working with system calls from high-abstraction layers that rely on NT-like behavior, such as `CreateFileW`.
