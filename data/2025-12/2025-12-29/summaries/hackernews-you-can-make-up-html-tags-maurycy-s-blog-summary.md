---
title: "You can make up HTML tags: (Maurycy's blog)"
url: https://maurycyz.com/misc/make-up-tags/
date: 2025-12-29
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-29T11:25:15.186083
screenshot: hackernews-you-can-make-up-html-tags-maurycy-s-blog.png
---

# You can make up HTML tags: (Maurycy's blog)

## Introduction to HTML Tags and CSS

HTML (Hypertext Markup Language) is used for structuring and presenting content on the web. It allows developers to create dynamic and interactive web pages by adding relevant tags around their desired structure.

### Using Built-in HTML Tags vs Making Up Your Own

When using built-in HTML tags, the browser will automatically render them as specified in the CSS (Cascading Style Sheets). However, if you choose to use descriptive named tags instead of relying on class names for organization, it can lead to improved readability and compatibility issues.

### Understanding Browser Behavior

Browsers may recognize and display unknown HTML tags without any effect. Nevertheless, their default behavior can include rendering generic elements with no additional styling beyond the CSS definition.

## Code Example: Descriptive vs Unnamed Tags

Here is a code example demonstrating the difference between using descriptive named tags for organization (HTML) and making up your own tags for readability purposes:

```html
#article-main

<main>
  <article>
    <div class="article-header">
      <h1>Heading</h1>
    </div>
    <p>This section holds our content.</p>
    <div class="article-quote">
      Quote: <em>Useful quote here</em>.
    </div>
  </article>

  #quote-bodies

  <main>
    <section id="author-about" class="article-header">
      <h1>About author</h1>
    </section>

    <p>This section holds our contribution details.</p>

    <section id="content-about">
      <!-- content goes here -->
    </section>

    #quote-body

  </main>

</main>
```

The use of descriptive named tags (`#article-main`, `#author-about`, etc.) ensures that these elements are correctly identified by the browser and their CSS styling. This leads to a better experience for users on various devices.

Additionally, using named tags helps simplify code and makes maintenance more manageable if you ever need to update your structure in the future.

In conclusion, understanding how to effectively use HTML tags while also making up custom tags can facilitate efficient and accessible content creation on the web.
