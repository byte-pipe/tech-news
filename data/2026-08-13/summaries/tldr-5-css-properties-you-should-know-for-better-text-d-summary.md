---
title: 5 CSS Properties You Should Know for Better Text Designs – Master.dev Blog
url: https://master.dev/blog/typographic-css-tricks/
date: 2026-08-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:44:22.125064
---

# 5 CSS Properties You Should Know for Better Text Designs – Master.dev Blog

# 5 CSS Properties You Should Know for Better Text Designs

## 1. background-clip
- Allows a background image or gradient to be clipped to the shape of the text, creating striking “knock‑out” effects.  
- Use `background-clip: text` together with `color: transparent` so the clipped background shows through the letters.  
- Example:  
  ```css
  p {
    background: url("image.jpg") center/auto 1lh;
    background-clip: text;
    color: transparent;
  }
  ```

## 2. vertical-align / align-content
- `vertical-align` aligns inline elements (e.g., `span`, `img`) relative to surrounding text; it originated for table‑cell alignment.  
- It does **not** vertically center block‑level text inside a container.  
- `align-content` (used in flexbox and grid) aligns the content of a block box along the vertical axis, centering items without needing additional layout modules.  
- Example:  
  ```css
  .emoji { vertical-align: top; }

  p {
    width: 360px;
    aspect-ratio: 1;
    text-align: center;
    align-content: center;
  }
  ```

## 3. box-decoration-mode
- Controls how borders, shadows, padding, etc., are rendered when a line box breaks across columns, pages, or fragments.  
- Setting `box-decoration-break: clone` (or the prefixed version) copies the element’s decorative styles to each fragment, preventing uneven edges.  
- Example:  
  ```css
  span {
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
    border: solid blue 0 1px 1px 0;
    box-shadow: 2px 2px 3px rgb(171,171,245);
    padding-inline: 6px;
    border-radius: 3px;
  }
  ```

## 4. letter-spacing
- Adjusts the space between characters; accepts positive (increase) and negative (decrease) values.  
- Useful for typographic aesthetics and for creating reveal animations by animating the spacing from a negative value to zero.  
- Example animation:  
  ```css
  span {
    letter-spacing: -1ch;
    color: transparent;
  }
  span::first-letter { color: #FBDA0C; }

  body:has(:checked) & {
    letter-spacing: 0ch;
    color: #0057AD;
    transition: letter-spacing 0.4s cubic-bezier(.8,-.5,.2,1.4),
                color 0.8s linear;
  }
  ```

## 5. text-combine-upright
- Designed for East Asian vertical typography; combines consecutive characters into a single upright glyph when `writing-mode` is vertical.  
- Can be applied to short horizontal snippets within vertical text, useful for mixed‑language layouts or space‑saving designs.  
- Example:  
  ```css
  p {
    writing-mode: vertical-lr;
  }
  p span { text-combine-upright: all; }
  ```

## Closing Thoughts
- These five properties—`background-clip`, `vertical-align`/`align-content`, `box-decoration-mode`, `letter-spacing`, and `text-combine-upright`—provide a solid foundation for enhancing web typography.  
- Mastering them opens up creative possibilities for more engaging and readable text designs.