---
title: "What Karpathy's LLM Wiki Is Missing (And How to Fix It) - DEV Community"
url: https://dev.to/penfieldlabs/what-karpathys-llm-wiki-is-missing-and-how-to-fix-it-1988
date: 2026-04-13
site: devto
model: llama3.2:1b
summarized_at: 2026-04-16T06:13:43.219531
---

# What Karpathy's LLM Wiki Is Missing (And How to Fix It) - DEV Community

## Gap 1: Typedef relationships as wikilinks

To create typed relationships between wiki articles, we can use the `@syntax` option in our `wikilink-types` plugin to add semantic relationship types. This will allow us to create wikilinks that indicate whether one article supports, contradicts, or supersedes another.

`[[Previous Analysis|The new research supersede's previous analysis]]
[[Redis Paper|This paper follows the principles supported by the previous Redis paper]]

## Gap 2: Indicate specific relationships in frontmatter

In addition to adding relationship types to standard wikilinks, we can also use `@syntax` on other types of frontmatter, such as citations and references. This will allow us to specify the specific relationship between two articles.

```
[
  "references":
  {
    "@type": "https://github.com/daviskl/datasheet",
    "href": "/refs"
  }
]

```


## Gap 3: Save changes and trigger autocomplete

We can save our changes and trigger autocomplete whenever we open a wikilink. For example, to enable autocomplete when opening a wikilink using a space before the relationship type (`@link=<type>`) alias, we can add:

```
"link=<type>",
```

This will allow users to use auto-completion for wiki links without explicitly selecting the relationship type.

The final answer is

### Typed Relationship Pattern for Karpathy's LLM Wiki

To implement a keyword-based wiki using Obsidian, implement the following steps:
  * Add typed relationships as wikilinks.
    * The `@syntax` option defines specific relationship types (e.g. supersedes, contradicts).
  * Indicate specific relationship between articles in frontmatter.
  * Save changes to trigger autocomplete.

Example:

```yaml
[
  "references":
  {
    "@type": "https://github.com/daviskl/datasheet",
    "href": "/refs"
  }
]

/**
 * The new research supersede's previous analysis */
 [[Previous Analysis]]
```
