---
title: I’ve banned query strings — Chris Morgan
url: https://chrismorgan.info/no-query-strings
date: 2026-05-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-10T07:46:09.197031
---

# I’ve banned query strings — Chris Morgan

# I’ve banned query strings

## Main points
- The author dislikes any tracking parameters added to URLs, especially query strings like `utm_source` or custom ref tags.
- Preference is to rely on the `Referer` header for referral information; if absent, it’s likely intentional.
- A blanket policy is implemented on the site: **no unauthorized query strings** are allowed.
- Currently the site uses no query strings; future use will be limited to explicitly approved parameters only.
- Past use of query strings for cache‑busting (e.g., `?t=…`, `?h=…`) is being discontinued; such requests will be broken.
- The author invites readers to test the restriction, noting that they control their own website and can apply similar rules.
- Implementation is done via the Caddy web server configuration (`Caddyfile`).