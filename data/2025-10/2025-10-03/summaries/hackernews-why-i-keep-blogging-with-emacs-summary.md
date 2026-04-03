---
title: Why I Keep Blogging With Emacs
url: https://entropicthoughts.com/why-stick-to-emacs-blog
date: 2025-10-03
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-03T11:21:49.020837
screenshot: hackernews-why-i-keep-blogging-with-emacs.png
---

# Why I Keep Blogging With Emacs

**Creating an Advanced Blogging Engine in 2,000 Lines of Code**
=================================================================

The author's experience highlights the benefits of using a lightweight markup format like Markdown or ReStructuredText for blog publishing, which enables embedding code blocks and conditional compilation.

**Org Mode Summarization**
---------------------------

## Introduction to Org Mode

The problem starter uses most standard Org publishing functions, but struggles with understanding how it exports articles to HTML. This is mitigated by leveraging Babel's flexibility in handling multiple languages.

## ExportingArticles using org-publish-function

**Overview of the Export Process**

1.  `org-publish-current-filecommand`: Runs the exported code block
2.  `ox-html.el` (5,000 lines): The actual exporting process generates HTML code that can be directly displayed in the published document.
3.  `org-element.el` (9,000 lines): This framework relies on `org-publish-last-command`, which requires parsing Org structure.

## Real-World Complexity

**Babel's Limitations**

While easy to use and powerful, Babel comes with a trade-off: limited JavaScript support in the exported HTML. This limits its ability to showcase external resources or dynamic content.

Conclusion
----------

*   **Choose an Effective Tools**: Consider using Markdown or ReStructuredText for blog publishing.
*   **Babel's Strengths**:

    *   **Flexible Language Support**
    *   **Embedded Code Blocks**
    *   **Reusability**

### Tips

*   If you're interested in creating a blogging engine, consider taking advantage of Babel's features and start by leveraging its functionality for your use case.
*   When developing a custom solution, weigh the benefits of simplicity against potential complexities to meet specific needs.
