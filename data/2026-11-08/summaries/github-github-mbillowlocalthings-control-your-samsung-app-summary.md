---
title: GitHub - mbillow/localthings: Control your Samsung appliances from Home Assistant over your home network, with no cloud account. · GitHub
url: https://github.com/mbillow/localthings
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:34.602795
---

# GitHub - mbillow/localthings: Control your Samsung appliances from Home Assistant over your home network, with no cloud account. · GitHub

# LocalThings – Samsung Appliance Integration for Home Assistant

## Overview
- Enables control of Samsung appliances (washers, dryers, refrigerators, ACs, ovens, etc.) directly from Home Assistant over the local network.  
- No cloud account required; after initial setup, no communication with Samsung servers.  
- Fast updates: push‑enabled devices send real‑time changes, others are polled every 30 seconds.  

## Supported Appliances
- Air conditioners (including multi‑unit systems)  
- Microwaves, ovens, range hoods, cooktops (gas, electric, induction)  
- Refrigerators, kimchi fridges, wine cellars  
- Washers, dryers, washer‑dryers  
- Dishwashers, dehumidifiers, air purifiers, air dressers, soundbars  
- Robot vacuums, vacuum clean stations, water purifiers, EHS heat pumps  
- Sensors and controls vary per model (power, mode, temperature, timers, door lock, energy use, alarms, etc.)  

## Technical Foundations
- **OCF**: discovers devices via `/oic/res` and reads types such as `oic.d.washer`.  
- **CoAP over DTLS**: encrypted communication using X.509 client certificates; supports Observe (push) and block‑wise transfers.  
- **Home Assistant integration**: UI config flow, data‑update coordinator, DHCP discovery, repair notices, multilingual entity names.  
- **Declarative appliance maps**: tables map OCF resources to Home Assistant entities; validated against >90 real‑device captures.  

## Installation
1. In HACS → Integrations, search for **LocalThings** and install (default repository).  
2. Or manually copy `custom_components/localthings/` into Home Assistant’s `custom_components` folder.  
3. Restart Home Assistant.  

## Adding an Appliance
1. Settings → Devices & Services → Add Integration → **LocalThings**.  
2. Enter the appliance’s IP address (most devices require only this).  
3. LocalThings reads the type/model and creates a Home Assistant device.  

- First appliance triggers a one‑time request to Samsung for a public identifier; subsequent devices need only the IP address.  
- Some devices may require a pre‑shared key or a device token (older TCP 8888 appliances).  

## Per‑Device Settings
- **Allow writes when remote control is off** – permits commands even if the appliance reports remote control disabled.  
- **Estimated finish – minimum change (minutes)** – throttles finish‑time updates to reduce jitter (default 3 min).  
- **Remember undocumented modes** – keeps track of modes the device uses but does not advertise.  
- Subdevice management for multi‑unit appliances (e.g., each indoor AC unit).  

## Known Device Behavior
- Brief Wi‑Fi disconnects are normal; LocalThings reconnects and retains last known values.  
- Excessive reconnects may indicate weak Wi‑Fi or another device holding the single allowed connection.  
- Keep appliances registered in the SmartThings app; removal resets network settings and may disconnect Wi‑Fi until re‑added.  

## Contributing & Support
- Diagnostics can be downloaded from Home Assistant notices to help maintainers add missing capabilities.  
- Reports of capability gaps, older‑device issues, and certificate handling are welcomed via the repository’s issue tracker.