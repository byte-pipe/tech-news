---
title: From Supabase to Clerk to Better Auth | Val Town Blog
url: https://blog.val.town/better-auth
date: 2026-05-06
site: hnrss
model: llama3.2:1b
summarized_at: 2026-05-07T12:44:43.131316
---

# From Supabase to Clerk to Better Auth | Val Town Blog

# From Supabase to Clerk to Better Auth: A Summary

In 2023, I moved from Supabase to Clerk for authentication and data management. After a successful transition, we later switched to Better Auth due to an issue with social media integration.

The core challenge was that Clerk attempted to replace our users table and session management system with its own. However, this approach ran into issues with limited scalability and reliability.

Some key points:

*   **Supabase limitations:** Supabase's underlying framework has rate limits for user data access, which led to significant performance bottlenecks when loading user information from the API.
*   **Clerk's default UI assumptions:** Clerk's design assumes users only see their own avatar and limited profile information. Val Town requires more advanced social features, including syncing avatars among multiple accounts and storing more detailed user settings.
*   **Better Auth alternatives:** After facing difficulties with Clerk's architecture, we transitioned to a different authentication layer called Better Auth. While it has its own set of limitations and challenges, it seems to be working for Val Town's needs.

The move to Clerk can be attributed to success in other areas, such as the company's positive funding and user adoption (Clerk raised $50 million). The benefits don't outweigh the drawbacks due to issues with scalability and robustness.