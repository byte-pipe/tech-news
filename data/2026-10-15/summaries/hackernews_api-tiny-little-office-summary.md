---
title: Tiny Little Office
url: https://tinylittleoffice.com/
date: 2026-10-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-15T15:34:13.641279
---

# Tiny Little Office

# Tiny Little Office
======================
## Key Points
---------------

* The Tiny Little Office (TLO) needs JavaScript to display a document.
* The document is stored locally on the device (no online accounts or saving).
* Documents are stored as files inside a "fence" (named by the app).
* The link to the document is provided using a text file URL.

## How It Works
---------------

The TLO uses a link to a text file that contains instructions on how to create and display a document. When a document is created, it is stored as a file on the device's local storage.
 Inside the file, there is a name assigned to the document by the app itself. The app creates the document when it needs it.

## Example Use Case
---------------------

To use Tiny Little Office, you can create a document and then link to it from another document. For example:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Tiny Little Office</title>
</head>
<body>
    <p>Visit the link to download the TLO text file: https://tinylittleoffice.com/llms.txt</p>
    <!-- Download the script to display the document -->
    <script src="document.js"></script>
</body>
</html>
```

## Notes
-------

* Only files stored locally on the device can be displayed using Tiny Little Office.
* The TLO script can be downloaded and stored on the device for offline use.