---
title: Returning To Rails in 2026 - markround.com
url: https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/
date: 2026-03-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:14:20.235051
---

# Returning To Rails in 2026 - markround.com

# Returning To Rails in 2026

## The Unapologetic Rubyist
- I chose Ruby on Rails for a personal side‑project despite its waning popularity.
- The 2025 Stack Overflow Developer Survey shows Rails at #20 and Ruby outside the top‑10 languages.
- My attachment to Ruby stems from its expressive syntax, method chaining, and readable blocks, which feel natural after years of Perl and shell scripting.
- The Ruby community’s quirky, welcoming vibe (e.g., Why the Lucky Stiff) reinforced my loyalty.

## The Engine Room
- My professional focus has always been back‑end, DevOps, and infrastructure—what I call the “engine room.”
- I have a long history with front‑end work (late‑90s HTML, Fireworks, table layouts) but view modern JavaScript frameworks as impressive yet not fun for me.
- Front‑end development is a necessary skill, but I treat it as a utility rather than a passion.

## Rails 8: A Familiar Stranger
- I hadn’t built a full Rails app since the Rails 3‑4 era, but Rails 8 still feels recognizable: MVC, conventions, generators.
- Under the hood Rails 8 has evolved significantly, especially in how it handles front‑end assets.

### Frontend
- Rails 8 adopts a “no‑build” philosophy, avoiding heavy tooling like Webpack.
- I could create an interactive set‑list manager with minimal JavaScript by leveraging Hotwire (Turbo + Stimulus).
- Turbo intercepts links and form submissions, swapping page fragments to give SPA‑like responsiveness while keeping server‑rendered ERB templates.
- Small Stimulus controllers added needed dynamic behavior (e.g., drag‑and‑drop reordering, modals) without drowning in JS.

#### Stimulus and “No‑Build”
- Stimulus has a smaller ecosystem than major JS frameworks, but quality component libraries (Stimulus Library, Stimulus Components) are easy to integrate.
- This approach let me build a modern‑feeling UI with the least possible custom JavaScript, aligning with my preference for server‑side rendering.