---
title: The Cascade
url: https://thecascade.dev/article/least-amount-of-css/
date: 2025-10-06
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-07T11:19:31.871162
screenshot: hackernews_api-the-cascade.png
---

# The Cascade

# Responsive Websites
=====================================

### 1. Ensuring Responsive Images

Images can cause overflow issues on large screens. Basic solutions include increasing image width to 100%.

#### img elements

*   Set `max-width` and `display: block`.
*   Provide a fallback for older browsers that don't support these properties.

```html
<img src="image.jpg" />
```

### 2. Improving Typographics

Typographics can benefit from an alternative font family, such as System UI Kit (UI Kit). It has good performance and looks great on most systems.

Set the `font-family` to `System UI Kit`.

#### body tag

*   Set `font-family: System UI Kit;`.
*   Adjust the `font-size`, `line-height` to 1.5-1.7 and adjust to your personal preference.
```css
body {
  font-family: System UI Kit;
  font-size: 1.25rem;
  line-height: 1.5;
}
```

### 3. Adding Dark Mode Support

Dark mode can be easily enabled or disabled based on the user's system preferences.

Use `color-scheme` to set your color scheme between light and dark modes.

#### HTML Element

*   Set `color-scheme:` to `light-dark`.
```html
<html>
    <body>
        <!-- content -->
    </body>
    </html>
</body>
```

### 4. Restraining Content Width

Content width should be set between 45-90 characters per line.

Use CSS to limit the content width of main elements:

#### Main Element

*   Apply `max-width: min(70ch, 100%)` in addition to `min(70ch, 100%)`.
```css
main {
    max-width:
        min(70ch, 100%);
    margin-inline auto;
}
```

### 5. Using Responsive Elements

Switch the main selector from `main` to `.container` or `.wrapper` for more control over where you apply rules.

The final CSS files will look like this:

```css
html {
  color-scheme: light-dark;
}

body {
  font-family: System UI Kit;
  font-size: 1.25rem;
  line-height: 1.5;
}

main {
  max-width:
    min(70ch, 100%);
  margin-inline auto;
}
```

And the complete HTML code remains unchanged:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content]=""
    color-scheme: light-dark;
</head>
<body>
    <!-- content -->
</body>

</html>
```
