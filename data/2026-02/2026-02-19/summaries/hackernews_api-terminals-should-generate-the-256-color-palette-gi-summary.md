---
title: Terminals should generate the 256-color palette · GitHub
url: https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783
date: 2026-02-18
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-19T06:02:22.633688
---

# Terminals should generate the 256-color palette · GitHub

# Terminals should generate the 256-color palette

This article proposes that terminals should automatically generate a 256-color palette based on the user's existing base16 theme. The current default 256-color palette has drawbacks, including clashing with base16 themes, poor readability, and inconsistent contrast.

## Understanding the 256-Color Palette

The 256-color palette consists of three parts:

*   **Base 16 Colors:** The first 16 colors (black, white, and primary/secondary colors with normal and bright variants).
*   **216-Color Cube:** A 6x6x6 color cube, calculated using a formula based on RGB values (0-5).
*   **Grayscale Ramp:** The final 24 colors, a grayscale ramp between black and white, excluding pure black and white.

## Problems with the 256-Color Palette

The default 256-color palette has several issues:

*   **Base16 Clash:** It often doesn't align well with user-defined base16 themes.
*   **Incorrect Interpolation:** The default color cube interpolates incorrectly, leading to lighter shades and readability problems in dark backgrounds.
*   **Inconsistent Contrast:** The default palette uses fully saturated colors, resulting in inconsistent brightness against a black background.

## Generating the Palette

To address these problems, the article suggests generating the 256-color palette from the user's base16 colors. This involves:

*   Using the base16 colors as corners of the 216-color cube.
*   Employing trilinear interpolation for the color cube and a simple background-to-foreground interpolation for the grayscale ramp.
*   Utilizing the LAB color space to ensure consistent apparent brightness across hues.

The provided code implements this generation process, using functions to interpolate between colors and generate the full 256-color palette.

## Conclusion

The default 256-color palette has limitations and is often avoided by terminal program maintainers. Automatically generating the palette from the user's base16 theme offers significant advantages:

*   Provides a wide color range without requiring separate configuration files.
*   Enables light/dark switching without developer effort.
*   Increases terminal support by avoiding compatibility issues associated with trucolor.

The article highlights that this approach would make the 256-color palette a viable and expressive option for terminals.
