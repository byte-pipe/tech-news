---
title: What ORMs have taught me: just learn SQL
url: https://wozniak.ca/blog/2014/08/03/1/index.html
date: 2026-07-01
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-05T11:38:46.436072
---

# What ORMs have taught me: just learn SQL

# What ORMs Have Taught Me: Just Learn SQL

In my experience working with code that interacts with Postgres and SQLite for the past 30 months, I have concluded that ORMs are more detrimental than beneficial. Here's why:

## Key Takeaways from My Experience with ORMs

*   **Entity Identity Issues**: ORM-related problems like entity identity issues can lead to complex relationships between entities.
    *   For example, when you add an attribute to a class, the ORM might encourage it to access that attribute in every query.
*   **Dual-Schema Problem**: When working with multiple models and tables in an ORM-based application, data retrieval mechanisms can become cumbersome.
    *   This is especially true if both models are designed for event-based storage and rely heavily on existing data models and data models from other sources.
*   **Partial Object Problem**: Often ORM-related issues involve dealing with partially defined objects that cannot be properly populated or referenced in the database.

## Specific Examples of Difficulty with ORMs

*   **Attribute Creep**: The author of this piece has dealt with tables that just grow beyond what's expected, requiring specialized techniques to manage data effectively.
    *   This could happen when clients provide a lot of relevant data for reports based on complex business logic.
*   **Foreign Keys and Data Intensity Overloads**: Many ORM users have struggled to use foreign keys correctly, leading to significant performance issues.
    *   Excessive foreign key-based querying can result in large numbers of joins in the database.

## Best Practices for Using ORMs Effectively

While ORMs can be a powerful tool, mastering them requires understanding the risks associated with their usage. To minimize these pitfalls, it is advisable to approach ORM implementation carefully and stay informed about potential issues that can arise. Effective best practices include:

*   Understanding the benefits of each table's identity.
*   Implementing normalized data models where possible
*   Utilizing ORM-specific features, such as `@Relationship` annotations,
*   Keeping up with advanced query techniques in ORMs.

By following these insights and staying attentive to potential pitfalls, developers working with postgreSQL or SQLite databases can make more informed choices regarding the use of Object-Relational Mappings.