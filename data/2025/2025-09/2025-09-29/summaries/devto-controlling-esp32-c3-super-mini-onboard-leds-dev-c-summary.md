---
title: Controlling ESP32-C3 Super Mini Onboard LEDs - DEV Community
url: https://dev.to/gapple/controlling-esp32-c3-super-mini-onboard-leds-2mmn
date: 2025-09-25
site: devto
model: llama3.2:1b
summarized_at: 2025-09-29T11:10:52.111628
screenshot: devto-controlling-esp32-c3-super-mini-onboard-leds-dev-c.png
---

# Controlling ESP32-C3 Super Mini Onboard LEDs - DEV Community

**Controlled LEDs on ESP32 C3 Super Mini Boards**
=====================================================

*   **Standard ESP32 Dev Boards:** The onboard LEDs typically use GPIO2 or GPIO8 as the default pin source, which are pulled high. However, controlling these LEDs can be challenging with standard ESPHome components.
*   **C3 Board Specifics:**
*       *   RGB LED: A WS2812-based LED connected to GPIO8 during boot. It then flashes and goes off once started.
*       *   Basic LED: Connected to GPIO8 during boot, but remains on constantly.
    Setting GPIO8 high or low controls the basic LED, while the status LED can be configured for specific pin settings with the `status_led` component.
*   **ESP32 RMT Light Strip Component and NeoPixel/FASTLED components:** These are separate components that control the RGB LED via a binary output (GPIO17) and the WS2812 LED (GPIO8), respectively.

**Best Practices**

1.  Configure your board with an addressable RS-Lite RGB or WS2812-based LED.
2.  Use `status_led` component to set LED states, which is easier for control without affecting other components.
3.  Set up separate binary output component(s) if needed to handle other LED states.

**Optimization and Troubleshooting Tips**

*   Double-check the pin numbers and settings in your board configuration
*   Verify that GPIO8 or GPIO17 are not used as a strapping pin for your onboard LEDs
