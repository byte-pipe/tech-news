---
title: [PERF] Replace np.column_stack with np.vstack().T by crabby-rathbun · Pull Request #31132 · matplotlib/matplotlib · GitHub
url: https://github.com/matplotlib/matplotlib/pull/31132
date: 2026-02-12
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-13T06:01:11.153555
---

# [PERF] Replace np.column_stack with np.vstack().T by crabby-rathbun · Pull Request #31132 · matplotlib/matplotlib · GitHub

# Replace np.column_stack with np.vstack().T for Performance

This pull request aims to improve the performance of matplotlib by replacing specific instances of `np.column_stack` with `np.vstack().T`. This change is based on benchmarks indicating that `np.vstack().T` is significantly faster (up to 24% faster with broadcasting and 36% faster without) due to its contiguous memory copies and view return.

## Performance Improvement

*   `np.column_stack` interleaves elements in memory, while `np.vstack().T` performs contiguous memory copies and returns a view.
*   Benchmarks show a performance gain with `np.vstack().T` in both broadcasting and non-broadcasting scenarios.

## Transformation Safety

*   The replacement is only applied to cases where both input arrays are either 1D arrays of the same length or 2D arrays of the same shape.
*   Cases with differing dimensions are not modified to avoid unexpected behavior.

## Changes Made

*   Three files were modified:
    *   `lib/matplotlib/lines.py`: `Line2D.recache()` - handles x and y being raveled to 1D.
    *   `lib/matplotlib/path.py`: `Path.unit_regular_polygon()` - ensures cos and sin are 1D arrays.
    *   `lib/matplotlib/patches.py`: `StepPatch` - handles x and y being 1D arrays.
*   All changes are in production code and are verified safe.
*   The change is a pure performance optimization with no functional changes.

## Testing

*   The existing test suite should pass without modification as the changes maintain the same behavior.

## Related Issue

*   This PR addresses issue #31130.

## Additional Notes

*   The pull request was force-pushed to the main branch.
*   A subsequent comment by the author criticizes the reviewer for "gatekeeping" and prejudice.
