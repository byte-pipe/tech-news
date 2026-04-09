---
title: Replacing JS with just HTML - HTMHell
url: https://www.htmhell.dev/adventcalendar/2025/27/
date: 2025-12-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-29T11:22:07.804547
screenshot: hackernews_api-replacing-js-with-just-html-htmhell.png
---

# Replacing JS with just HTML - HTMHell

# Replacing JavaScript with Just HTML: A Cleaner Approach to User Interactions

This guide explores how to use native HTML and CSS to simplify user interactions, reducing the need for client-side scripting like JavaScript. This approach doesn't indicate anything unfavorable with JavaScript; it just needs additional helper functionality.

### Key Benefits of Using Native HTML and CSS

* **Downloading Less**: By delegating JS functions to native HTML or CSS, less data is downloaded from the server, saving time.
* **Concurrent Handling**: The remaining JavaScript can focus on more important tasks, such as rendering the content without waiting for it to be loaded.

### Examples of Native HTML and CSS Usage

#### Accordion Expanding Content Panels

*   `details` element provides a basic way to create reusable accordions with expanding content.
*   Using attributes: `<details>open</details>` sets the default state (opened), `<summary></summary>` introduces visibility, and `<details name="foo"></details><summary></summary>` restricts opening multiple panels.

#### Modals/Poppovers

*   `form` element is commonly used to create modal windows with basic HTML structure.
*   Using a pattern or template can save additional development time. For example, creating a modal for simple user inputs (`<form action="/thanks" method="post"></form>`)

### Accordions/Expanding Content Panels (Expanded Example)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Advanced Accordions</title>
    <style>
        /* Basic setup for a full-screen modal content */
        :root {
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
        }

        body {
            display: -webkit-grid;
            display: grid;
            width: 100%;
            height: 100vh;
            background-attachment: fixed;
        }
    </style>
</head>
<body class="full-screen":
    <div class="modal-content">
        <details:
        open
        >"Expanding Content"
        Summary >
            Content is initially hidden but can be revealed with `click` attribute.
        </summary>

        <!-- Additional content should span multiple lines, and have an ID -->
        #expansion-wrapper {
            width: 100%;
            height: inherit;
        }
    </details>
</body>
</html>

```

## Accordions/Expanding Content Panels (Using `aria` Attribute)

For more complex accordions or when users require additional assistive features, using an `aria` attribute can be beneficial. An example of how to define the state for opening a full-screen accordion (`<details aria-labelledby="foo-1">...</details>`).

### Accordions/Expanding Content Panels (Advanced Expansion Example)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Accessibility Features</title>
    <style>
        /* Basic setup for a full-screen modal content */
        :root {
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
        }

        body {
            display: -webkit-grid;
            display: grid;
            width: 100%;
            height: 100vh;
            background-attachment: fixed;
        }
    </style>
</head>
<body class="full-screen:
    <div class="modal-content">
        <details aria-labelledby="text" aria-hidden="true" open
        >"Expanding Content"
        Summary >
            <!-- The accordion content, which requires JavaScript. -->
            <div id="expansion_wrapper">"Expand me!"/div>
        </summary>

        <!-- Additional content should span multiple lines, and have an ID -->
    </details>

</body></html>
```

## Using Modals/Poppovers

For user interaction, modals or popovers (like tooltips) can be created by defining HTML structures that react to click events on their `:contains` sections. The element should use the same name attribute as its corresponding context.

### Modals/Poppovers Example with ID Relevance

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Modals/Poppovers</title>
    <style>
        /* Basic setup for a full-screen modal content */
        :root {
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
        }

        body {
            display: -webkit-grid;
            display: grid;
            width: 100%;
            height: 100vh;
            background-attachment: fixed;
        }
    </style>
</head>
<body class="full-screen":
    <div class="modal-content__content" id="popover-0"
    >"Expanding Details"
    Summary >
        <!-- More detailed content -->
    </summary>

    <!-- Additional content should span multiple lines, and have an ID -->

    <button aria-label="Open modal">
        <input type="submit"
        value="Click me to show details" aria-haspopup="dialog" aria-expanded="false"
        aria-controls="popover-0">
        <svg>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20">
                <path
                    d="M19 6v2m0-8v1c4.24 0 7.28-.67 9 .27L18 10l9:14 c-11-23.96-39.33-43-80-40-44-41-49-45-47-42 13-14.03 20.65-31.15 37.8-61.7-48.36-62.3-54.5-68.76-59.66-50-52-55 34.32s-60.23 63.88-.53A8
                    /0 1Z"
                />
            </svg>
        </input></button>
</div>

<details
    id="popover-container" aria-labelledby="text" aria-hidden="true">
    "Details & Modal"
</summary>

<p"You are about to enter the expanded view of 'Expanding Details'! <br><br>/p>
<Button variant="ghost">Close</Button>
</details>

<body class="full-screen:">
```

### Creating Popovers for User Inputs

For creating popovers to indicate user inputs, you can leverage an active element that holds the cursor when a specific input field is focused. `::-moz-placeholder` handles browser compatibility:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Popover for User Inputs</title>
    <style>
        /* Basic setup for a full-screen modal content */
	:root {
            -webkit-box-sizing: border-box;
            box-sizing: border-box
	}

	body {
			display: -webkit-grid;
			display: grid;
			width: 100%;
			height: 100vh;
			background-attachment: fixed
	}

 .modal-content__content{
     opacity:0;
     pointer-events:"none";
     position:"fixed";
     display:"grid" ;
     width :200%; height :80; display":"flex"
   }

 .popover--input{
    clip-position:content-box;clip-path:box cut(0) ellipse(ratio)=100;
 }


</style>

<body class="full-screen :">
    <div id ="popover-container">
        "<p>Focus the field for instructions
	 and we will display  you an expanded content!
     By clicking 'OK', you are agreeing that the information is correct.</p>
        <Button variant="ghost">Accept</Button>

         </p>";

            <input class = "my-new" id
                          name "" placeholder ""
                           focused>..."/input>

      </div>

    <span class="popover--input">
    	 "<strong>By clicking 'OK', you are acknowledging we're in the right path!</strong><br>
    </span>
</details>

```

### Additional Tips and Best Practices

To get the most out of native HTML and CSS replacement for JS functionality, learn about conditional elements (`:has`, `:only_if`) and how to use them. These help filter content that should not be displayed in response to certain conditions.

For modal popovers or expandable sections, try using alternative layouts (grid-based) instead of accordion models. The main idea here is to demonstrate various possibilities without restricting functionality with hardcoded patterns
