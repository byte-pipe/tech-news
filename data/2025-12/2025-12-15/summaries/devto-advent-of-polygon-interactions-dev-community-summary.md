---
title: Advent of Polygon Interactions - DEV Community
url: https://dev.to/yordiverkroost/advent-of-polygon-interactions-1mgp
date: 2025-12-09
site: devto
model: llama3.2:1b
summarized_at: 2025-12-15T11:17:52.490384
screenshot: devto-advent-of-polygon-interactions-dev-community.png
---

# Advent of Polygon Interactions - DEV Community

## Main Idea: Finding the Largest Rectangle in a Grid

The problem consists of two parts. In the first part, we are given a grid of coordinates and asked to find the largest rectangle that can be formed using any combination of two points from the grid. The second part involves a more complex calculation involving closed shapes.

### Part One: Simplifying the Problem

The solution for the first part is an efficient brute-force approach that considers all possible combinations of two coordinates without duplicates, calculates their areas, and keeps track of the largest area found so far.

*   It uses a recursive function `area_size` to calculate the area of a single rectangle formed by two points.
*   The maximum rectangle size seen during this process is stored as the final result.

### Part Two: Analyzing Closed Shapes

In part two, we are dealing with closed shapes drawn from specific coordinates. To find the largest rectangle enclosed within these shapes, we need to consider all possible combinations of two input coordinates (without duplicates) that define a closed shape and identify the maximum area found.

*   The solution involves iterating over each coordinate in the grid, potentially creating closed shapes on-the-fly.
*   It uses another algorithmic approach to calculate the areas enclosed by these shapes.
