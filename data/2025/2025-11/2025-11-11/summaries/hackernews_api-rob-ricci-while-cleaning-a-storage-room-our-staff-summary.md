---
title: "Rob Ricci: \"While cleaning a storage room, our staff found th…\" - discuss.systems"
url: https://discuss.systems/@ricci/115504720054699983
date: 2025-11-06
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-11T11:11:27.122824
screenshot: hackernews_api-rob-ricci-while-cleaning-a-storage-room-our-staff.png
---

# Rob Ricci: "While cleaning a storage room, our staff found th…" - discuss.systems

# Enabling JavaScript in the Mastodon Web Application

The following instructions provide guidance on how to access the Mastodon web application by enabling JavaScript or using a native app.

## Method 1: Enable JavaScript in Browser Browsers

To enable JavaScript in most modern browsers, follow these steps:

*   Open your preferred browser.
*   Type `about:config` (not `about:settings`) in the address bar to open the Preferences tab of Internet Explorer, Mozilla Firefox, Google Chrome, Safari, or Opera browser.
*   In the "Compatibility mode:" section, disable JavaScript.

### Using Multiple Browsers

If you want to enable JavaScript across multiple browsers at once, you can follow this:

1.  Go to https://en.wikipedia.org/ref/cookies in your favorite Firefox browser and look for the cookie named `javascript_enabled`. If it exists, it will be set to "true". However, there is no direct way to disable all JavaScripts from websites in modern browsers; each website has its own policy regarding these cookies.
2.  You can disable most other types of cookies by deeming certain ones as unwanted for your web browser's needs:
    *   `cookieName1` -> Cookie you want to delete with preference is on
    *   cookie_name2 -> Cookie you want to keep intact
    *

You'll need to add an exception in the browser.

For example, you can use the following script snippet that disables JavaScript in all browsers by default:

```javascript
(function () {
    try {
        document.querySelectorAll('*').forEach(function (element) {
            if (/^(https?:\/\/[^\/]+)\/.*?\.js$/.test(element.ownerDocument_URL)) {
                element.style.position = "absolute";
                element.style.zIndex = -100;
                element.style.left = '0';
                element.style.top = '0'
                document.body.appendChild(element);

            }
        });
    } catch (e) {
   }
})();
```

This code creates JavaScript file blocks for all HTML files and prevents browsers from loading new scripts directly after a page load. You can adjust it to target specific websites or even entire domains by adjusting the regular expression accordingly.

**Method 2: Using Native Apps**

If you prefer native apps over web browsers, here are some popular options:

### For Windows 10

1.  **Skype**: Open Messenger Skye, which supports JavaScript enabled Mastodon accounts via Microsoft's integration for third-party services.
2.  **Nanodeck**: A user-friendly app that uses JavaScript to interact with different social media platforms.

### For Mac OS X

1.  **Mastodon Chat Client**: A minimalistic native application that allows interacting directly with your personal account without requiring any configuration or setup.

Note: Using a third-party app like this might require an initial installation, and some configurations might need adjustments for compatibility with the platform you're on.

### For Android

If using native apps involves jailbreaking devices, use caution before proceeding because once a device is jailbroken, it doesn't receive official updates from its manufacturer. As well as the permission to install outside of standard app stores; apps like such as those described do not support this:

For example, you can try installing `skype` using the following command when in the terminal.

### For iOS

1.  **Mastodon App**: You'll need an account in your Mastodon installation for this method to work.
2.  **ChatClient** by **Devon Larsh**

Again, be sure to check each app's privacy policies before proceeding with any application that demands access to sensitive personal data or configuration settings.

The choice of native apps depends on familiarity and preference among users regarding specific platforms and social media websites they use for their personal accounts. Always read reviews and understand the limitations of using third-party apps for accessing your account, considering security as a priority at all times.
