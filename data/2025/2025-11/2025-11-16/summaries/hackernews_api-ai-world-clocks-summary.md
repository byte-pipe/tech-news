---
title: AI World Clocks
url: https://clocks.brianmoore.com/
date: 2025-11-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-16T11:15:05.289416
screenshot: hackernews_api-ai-world-clocks.png
---

# AI World Clocks

## AI Clock Generation
### 9 AI Models Collaborate to Provide an Analog Clock
Every minute, a new clock is displayed with the generated time. Each model is given 2000 tokens and must create HTML/CSS.
```html
<title>AI World Clocks</title>
<style>
    /* White background */
    body {
        background-color: #FFFFFF;
    }

    /* Responsive design for different screen lengths */
    @media (max-width: 600px) {
        .clock-content {
            width: 100%;
            text-align: center;
        }
    }

    /* CSS animation for the second hand */
    .second-hand {
        width: 20px;
        height: 40px;
        border: 2px solid #000;
        display: inline-block;
        margin-top: -10px;
    }
</style>

<div class="clock-content">
    <h1 id="time">[Insert Time]</h1>
    <div class="second-hand" id="second-hand"></div>
</div>
```
