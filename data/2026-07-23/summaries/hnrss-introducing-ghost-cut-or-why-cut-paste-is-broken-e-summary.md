---
title: Introducing Ghost Cut - or why Cut & Paste is broken everywhere — Ishmael
url: https://ishmael.textualize.io/blog/ghost-cut/
date: 2026-07-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T18:59:43.366771
---

# Introducing Ghost Cut - or why Cut & Paste is broken everywhere — Ishmael

# Introducing Ghost Cut – Summary

## Problems with Traditional Cut & Paste
- **Undo limitation** – Undo restores the removed text in the document but does not revert the clipboard change; the original clipboard content is lost.
- **Reflow issue** – Cutting text causes the surrounding content to reflow, forcing the user to locate the new insertion point again.
- **Non‑atomic operation** – Cutting and pasting are separate steps; undoing requires multiple actions, especially if intermediate edits occur.

## Ghost Cut Mechanism
- Pressing **Ctrl+X** (or Cmd+X) fades the selected text, making it inert while keeping it in the document; nothing is placed on the clipboard and there is no undo entry.
- Pressing **Esc** restores the faded text to an editable state if the user decides not to paste.
- Pasting with **Ctrl+V** (or Cmd+V) removes the ghosted span from its original location and inserts it at the cursor, performing a single atomic move that can be undone in one step without affecting the clipboard.

## Side Effects
- To achieve the classic “cut” semantics (remove and copy to clipboard), the user must perform two actions: copy (**Ctrl+C** / **Cmd+C**) followed by **Backspace** to delete the original text.
- The author rarely needs a cut without an immediate paste, so this trade‑off is acceptable.

## Conclusion
- The author would welcome adoption of Ghost Cut in text editors, noting that while the benefit is clearer for prose editors, it could also improve the workflow in code editors such as VSCode.