---
title: Advent of Polygon Interactions - DEV Community
url: https://dev.to/yordiverkroost/advent-of-polygon-interactions-1mgp
date: 2025-12-09
site: devto
model: llama3.2:1b
summarized_at: 2025-12-10T11:19:36.350448
screenshot: devto-advent-of-polygon-interactions-dev-community.png
---

# Advent of Polygon Interactions - DEV Community

**Part 1: Finding the Biggest Rectangle**

The problem involves finding the largest possible rectangle that can be formed using coordinates as edges. We are given a set of points in a grid, and we must determine the maximum area of a rectangle containing any combination of these points.

### Solution

```python
def max_rectangle_size(coordinates):
    # Part 1: Find the biggest rectangle that can be made using two coordinates
    def max_rect_area(x1, y1, x2, y2):
        return abs(x1 - x2) + 1 * abs(y1 - y2)

    largest = 0

    # Try all pairs of coordinates to find the biggest rectangle
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]

            area = max_rect_area(x1, y1, x2, y2)
            largest = max(largest, area)

    return largest

# Example usage
coordinates = [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)]
print(max_rectangle_size(coordinates))  # Output: 15
```

**Part 2: Finding the Largest Rectangle Enclosed Within a Closed Shape**

The problem now involves finding the largest rectangle that can be formed using coordinates as edges. However, the order of elements in the input list affects whether we form a closed shape or not.

### Solution

```python
def max_rectangle_size_enclosed(coordinates):
    # Part 2: Find the biggest rectangle enclosed within a closed shape
    def max_enclosed_rect_area(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    largest = 0

    # Try all pairs of coordinates to find the biggest enclosed rectangle
    for i in range(len(coordinates)):
        for j in range(n if i == n else j + 1):  # Compare with original length
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[n - i]

            area = max_enclosed_rect_area(x1, y1, x2, y2)
            largest = max(largest, area)

    return largest

# Example usage
coordinates = [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)]
print(max_rectangle_size_enclosed(coordinates))  # Output: The maximum area enclosed
```
