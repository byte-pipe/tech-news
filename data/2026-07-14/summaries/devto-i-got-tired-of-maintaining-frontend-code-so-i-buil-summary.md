---
title: I Got Tired of Maintaining Frontend Code. So I Built a Declarative UI Runtime. - DEV Community
url: https://dev.to/thuangf45/i-got-tired-of-maintaining-frontend-code-so-i-built-a-declarative-ui-runtime-5dbl
date: 2026-07-10
site: devto
model: llama3.2:1b
summarized_at: 2026-07-14T11:35:58.525072
---

# I Got Tired of Maintaining Frontend Code. So I Built a Declarative UI Runtime. - DEV Community

# Systems-Level Shift: From Code to Data in Frontend Development

## Turning Shippy

When shipping a UI, how many files are needed before nobody can confidently say what happens when you click a button?

For the author, who shipped **200+ small code files**, it took too long. Although logic wasn't complicated, nothing agreed with anything else about building a button.

## The Journey to Stability

The story of this journey highlights costs and challenges:

*   **Taxes**: Two main taxes affected the development process:
    *   **Tax 1: File Count**: Author split the project into hundreds of small files to organize and bundle it for better performance. This change solved readability issues but introduced additional problems with load times.
        *   Before (hundreds of small files): Slow, scattered, and hard to manage.
*   **Tax 2: Code Structure**: Using a modular approach to split the project into hundreds of smaller files helped in some ways but created new issues related to page loading and rendering.
    *   After (bundled code): Reduced load times and improved overall performance.

## Building Solutions

The author's experience has taught that frontend development is not about writing small, individual elements; it requires a shift from thinking in terms of code to considering how those components interact and function together. The key skills for successful project management include:

*   Organizing data into an intuitive structure
*   Understanding the role of different files and modules within the system