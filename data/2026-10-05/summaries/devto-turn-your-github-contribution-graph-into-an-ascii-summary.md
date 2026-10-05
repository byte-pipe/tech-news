---
title: Turn Your GitHub Contribution Graph Into an ASCII City - DEV Community
url: https://dev.to/sizzlebop/turn-your-github-contribution-graph-into-an-ascii-city-ic5
date: 2026-10-03
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:21:16.220881
---

# Turn Your GitHub Contribution Graph Into an ASCII City - DEV Community

# Turn Your GitHub Contribution Graph Into an ASCII City

## Overview
- **Skyline** is a Go CLI that converts a GitHub contribution history into an ASCII city.
- Each week becomes a building; each day becomes a window that lights up based on activity.
- The tool can render in the terminal or generate an animated SVG for GitHub profile READMEs.

## How It Works
- Building height reflects total contributions for the week.
- Window brightness follows GitHub’s contribution levels; brighter windows indicate busier days.
- Decorative elements include stars, flickering windows, and twinkling brightest stars.
- Animations are deterministic, so the same data produces the same city layout.

## Themes
- 12 built‑in themes: neon, synthwave, matrix, amber, ice, sunset, toxic, vapor, crimson, mono, prism, rainbow.
- Themes can be previewed in the terminal and selected with the `-theme` flag.

## Installation & Local Use
- Requires Go 1.25+.
- Install: `go install github.com/pinkpixel-dev/skyline@latest`
- Basic command: `skyline your-username`
- Authentication: reads `GITHUB_TOKEN`, `GH_TOKEN`, or `gh auth token`; works with GitHub CLI auth.
- Adjust width and height:
  - `-weeks 30` limits number of weeks displayed.
  - `-height 10` sets maximum building height.

## Generating an Animated SVG
- Command: `skyline -svg skyline.svg your-username`
- Themes can be combined, e.g., `skyline -theme prism -svg skyline.svg your-username`.
- SVG respects reduced‑motion preferences.

## Adding the Skyline to a GitHub Profile
1. Create a repository named after your username (`github.com/your-username/your-username`).
2. Add a workflow file `.github/workflows/skyline.yml` that:
   - Runs nightly via a cron schedule.
   - Installs Go, runs Skyline with desired theme and SVG output.
   - Commits the generated `skyline.svg` to an `output` branch.
3. Include the SVG in your README:
   ```markdown
   ![My skyline](https://raw.githubusercontent.com/YOUR-USERNAME/YOUR-USERNAME/output/skyline.svg)
   ```
4. Replace `YOUR-USERNAME` with your actual username.

## Private Contributions
- The default GitHub Actions token may omit private contributions, resulting in a sparser city.
- Provide a personal access token with `read:user` scope as a secret named `SKYLINE_TOKEN` to include private data.

## Closing Thoughts
- Skyline turns a familiar contribution graph into a personalized, animated cityscape.
- Once the GitHub Action is set up, the skyline updates automatically with no further maintenance.
- The project is open source at `github.com/pinkpixel-dev/skyline`.