---
title: Controlling ESP32-C3 Super Mini Onboard LEDs - DEV Community
url: https://dev.to/gapple/controlling-esp32-c3-super-mini-onboard-leds-2mmn
site_name: devto
fetched_at: '2025-09-29T11:08:32.965091'
original_url: https://dev.to/gapple/controlling-esp32-c3-super-mini-onboard-leds-2mmn
author: Geoff
date: '2025-09-25'
description: I bought some ESP32 C3 Super Mini boards that have an RGB LED, and information for the onboard LEDs... Tagged with esp32, esphome.
tags: '#esp32, #esphome'
---

I bought some ESP32 C3 Super Mini boards that have an RGB LED, and information for the onboard LEDs wasn't as easy to find as for the standard ESP32 dev board, so I wanted to consolidate my notes here.

Standard ESP32 dev boards often have a single LED driven by GPIO2. As a strapping pin it's pulled high by default, so the led will turn on when the board gets power and will stay on if the pin is not set low. With ESPHome, it's easy to setup theStatus LED componentwhich will turn off the LED after boot, and blink it if there is a warning or error.

status_led:
 pin:
 number: 2
 ignore_strapping_warning: True

Enter fullscreen mode

Exit fullscreen mode

For the C3 boards I purchased there is a basic LED and an addressable RGB LED, both connected to pin 8. During boot the RGB LED will flash then turn off, while the basic LED will remain on. Setting GPIO8 high or low will control the basic LED, so the status LED component can be used by configuring it to the correct pin, but the RGB LED will remain off.

The RGB light is a WS2812, and can be controlled with theESP32 RMT LED Strip componentwhich works with both the ESP-IDF and Arduino frameworks. The Arduino framework also hasNeoPixelBus LightandFastLEDcomponents as options.

light:
 - platform: esp32_rmt_led_strip
 id: board_rgb_led
 pin:
 number: 8
 ignore_strapping_warning: True
 num_leds: 1
 chipset: WS2812
 rgb_order: GRB

Enter fullscreen mode

Exit fullscreen mode

It is not possible to control both LEDs by just enabling both light components and settingallow_other_usesfor the pin.

The Status LED component can only be configured to a pin, so can't use the RGB LED. TheStatus LED Light componentwhich enables controlling the LED when it's not being used to show a warning or error status can be configured to control a binary output component instead of a pin - aTemplate Binary Output componentcould use itswrite_actiontrigger to control the RGB light during a warning/error state[1].

Another option instead of using the status component is usingon_loopwith a customlambda to check for an error state and adjust the RGB LED.

This is the definition I put together to slow blink yellow on warning, and fast blink red on error:

substitutions:
 status_pin: GPIO8

esphome:
 on_loop:
 then:
 lambda: |-
 static uint32_t last_state = 0;
 auto state = App.get_app_state();
 if (state != last_state) {
 if (state & STATUS_LED_ERROR) {
 auto call = id(board_led).turn_on();
 call.set_brightness(.2);
 call.set_rgb(1, 0.01, 0.01);
 call.set_effect("fast-pulse");
 call.perform();
 } else if (state & STATUS_LED_WARNING) {
 auto call = id(board_led).turn_on();
 call.set_brightness(.2);
 call.set_rgb(1, 1, 0.01);
 call.set_effect("slow-pulse");
 call.perform();
 } else {
 auto call = id(board_led).turn_off();
 call.perform();
 }
 last_state = state;
 }

light:
 - platform: esp32_rmt_led_strip
 id: board_led
 pin:
 number: ${status_pin}
 ignore_strapping_warning: True
 num_leds: 1
 chipset: WS2812
 rgb_order: GRB
 effects:
 - pulse:
 name: "fast-pulse"
 update_interval: 0.3s
 transition_length: 0.3s
 min_brightness: 15% # Light turns off below 11%
 max_brightness: 50%
 - pulse:
 name: "slow-pulse"
 update_interval: 1s
 transition_length: 1s
 min_brightness: 15%
 max_brightness: 50%

Enter fullscreen mode

Exit fullscreen mode

I then include it for my projects running on C3 boards:

packages:
 - !include common/c3-rgb-status.yaml

Enter fullscreen mode

Exit fullscreen mode

There'san open PR to implement triggers for status changes, which would replace the need foron_loop

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
