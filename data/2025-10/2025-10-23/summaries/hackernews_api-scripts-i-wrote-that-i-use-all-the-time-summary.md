---
title: Scripts I wrote that I use all the time
url: https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/
date: 2025-10-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-23T11:29:26.113690
screenshot: hackernews_api-scripts-i-wrote-that-i-use-all-the-time.png
---

# Scripts I wrote that I use all the time

## My Favorite Scripts: A Personal Collection

By Evan Hahn, posted October 22, 2025

In my decade-plus experience maintaining my dotfiles, I've accumulated a collection of shell scripts that cater to various tasks. Below is a summary of my most frequently used scripts:

### Clipboard Management

*   ```bash
copyandpastaare simple wrappers around system clipboard managers.
```

Run some command:    `run_some_command | copy`
*   Paste the contents:  `$ pasta > file_from_my_clipboard.txt`
*   Decode base64:      `base64 --decode pasta`
*   Pastasprints the current state of your clipboard to stdout, and then whenever the clipboard changes, it prints the new version.
    ```
$pasta | base64 --decode
```

### File Management

*   `mkcd`: Makes a directory and cd into it.
  ```bash
mkcd foomakes a directory andcds inside
```
*   `tempe`: Changes to a temporary directory.
  ```bash
tempechanges to a temporary directory
```
*   Download file or extract tar archive:    ```
wget
'https://example.com/big_file.tar.xz'
tar -xf big_file.tar.xz
```

### Basic File Utility

*   `trash`: Moves a text file and its contents to the trash.
  ```bash
movesa.txtandb.pngto the trash
Supports macOS and Linux. I use this every day.
```

## Conclusion
