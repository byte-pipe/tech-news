---
title: 'Inside BYD: CT Scans of the EV You Can''t Buy in America'
url: https://www.lumafield.com/scan-of-the-month/byd
site_name: hackernews_api
content_file: hackernews_api-inside-byd-ct-scans-of-the-ev-you-cant-buy-in-amer
fetched_at: '2026-06-03T12:34:44.632961'
original_url: https://www.lumafield.com/scan-of-the-month/byd
author: viasfo
date: '2026-06-02'
description: We CT scanned four BYD components—a battery cell, window switch, EV charger, and key fob—to see what's inside the world's best-selling EV that's banned in the U.S.
tags:
- hackernews
- trending
---

#### Battery

##### Lithium Iron Phosphate (LiFP) Prismatic Cell

The cell that made BYD famous is the Blade: a long, thin Lithium Iron Phosphate (LFP) prismatic designed to lay flat across a vehicle floor, with the cells themselves forming part of the car's structure rather than sitting inside a separate enclosure. This prismatic cell is NOT a Blade, but it does share the same chemistry. LFP trades some energy density against the lithium-ion chemistries that dominate Western EV packs, but it runs cooler, tolerates more charge cycles, and replaces the nickel, manganese, and cobalt used in other chemistries with iron. That substitution is what gives LFP its stability, as well as cost and supply chain advantages. While Tesla sources cells from Panasonic and LG and most Western automakers buy from dedicated battery suppliers, BYD designs and manufactures its own, from chemistry to finished pack.

The two threaded terminals are the densest structures in the cell (negative on the left, positive on the right). Between them sits the explosion-proof valve: a pressure relief feature that vents the cell if internal gas pressure exceeds safe limits. It’s a last-resort safety mechanism. The LFP chemistry in this cell is stable enough that the valve rarely needs to function, which is precisely why BYD uses it.

Lowering the opacity of the aluminum housing, the cell resolves into two distinct electrode stacks. Each stack connects to the terminals above. Splitting the cell's capacity across two parallel jellyrolls rather than one improves current distribution and makes better use of the prismatic casing geometry. The Blade cell takes a different approach: its extreme length and thinness suits flat-stacked electrodes, sheets of anode, separator, and cathode layered directly rather than wound.

The cross-section reveals the cell's interior in full: tightly packed electrode layers of anodes and cathodes, separated by thin lines of separator material. We see four groupings, separated by slightly wider gaps where the jellyroll folds or stack boundaries fall. The current collector tabs fan out at the top before joining the terminal above. The electrode edges are mostly well-aligned, with consistent overhang between anode and cathode layers, an indicator of good process control. Hundreds of thin layers each store a fraction of the total 50 amp-hours charge.

Viewed from below, the two jellyrolls show their winding pattern in full. The electrode layers should curve in smooth, uniform concentric arcs around the base of each roll. Here they ripple, a sign of uneven tension during winding. Where tension varies, the gap between anode and cathode layers varies with it, creating inconsistencies in ion transfer and localized stress points that can accelerate degradation over the cell's lifetime.

#### Window Switch Panel

##### BYD Tang

The Tang is BYD's large seven-seat SUV, roughly competing with the Ford Explorer and Toyota Highlander in size and price. Its driver door panel consolidates mirror adjustment, mirror fold, door locks, all four window controls, and child locks into a single networked module. That consolidation exemplifies BYD's vertical integration favoring fewer subassemblies, each designed in-house and dropped into place, with firmware determining how any of it behaves.

The cross-section shows the panel's basic logic: button caps above, PCB below, a continuous band of electronics running the full width between them. The window rockers are the tallest elements in the stack, their travel depth visible in this slice. Everything mechanical in this panel exists to close a circuit on that board.

Viewed from the back, the PCB resolves into a grid of circular tact switch mechanisms, one per button function. We see six mounting screws (in red) with their heads visible on the panel's exterior underside. The layout maps directly to the button grid above: each switch position corresponds to a node on the LIN network connecting this module to the vehicle's body controller.

Here’s where tactile inputs become digital commands. A prominent IC in the upper part is likely the LIN transceiver or body domain microcontroller managing input polling and bus communication. There’s not much else to see here. Mirrors, windows, locks, and child safety all run on a board this sparse because the processing happens upstream in software.

Fourteen pins in two parallel rows carry every signal this panel produces to the rest of the vehicle. Automotive connectors are among the most common failure points in modern cars: corrosion, fretting, and thermal cycling work on these joints over years of use. One connector failure on a module this integrated takes out mirrors, windows, locks, and child safety all at once.

#### Charger

##### BYD Type 2 IC-CPD Portable AC Charger

Every BYD sold in Europe and the UK ships with one of these. The IC-CPD, or In-Cable Control and Protection Device, is a portable Mode 2 charger: It plugs into the car on one end, into a standard household socket on the other, with a control box sitting inline on the cable between them. It is the slowest way to charge an EV, a trickle from a wall outlet, but it requires no infrastructure and fits in a bag.

The seven-pin Type 2 housing holds more than this charger uses. The single active power conductor, L1, and its neutral and ground companions are the three large cylindrical contacts visible here. L2 and L3 occupy their designated positions in the housing but have no electrical connection. The two smaller pins at the top, CP and PP, manage the handshake that confirms a valid connection before current flows.

With CT we can see through the housing to the full conductor assembly. Each pin connects to its wire, and the full bundle then passes through a strain relief plate that absorbs the cable's mechanical stress before it reaches the electrical connections. Several mounting screws secure the internal structure within the housing. The CP and PP signal wires are visibly thinner than the power conductors, mapping directly to their function.

The control box contains the charger's intelligence. Two large inductors dominate the board, handling EMI filtering on the incoming AC line. Around them, a dense population of components manages the pilot signal generation, relay control, and protection functions: ground fault detection, over-temperature cutoff, and over-current protection.

At this angle the three power-carrying conductors of the wall-plug end appear in cross-section, their internal stranded copper construction clearly resolved. Ferrite cores sit along the wires, suppressing high-frequency noise on the line. The IC-CPD exists because a standard household circuit was never designed for the sustained 10-amp draw of overnight EV charging. The components on this board monitor every second of that draw and will cut power before a ground fault, an overcurrent, or an overtemperature condition can reach the cable, the outlet, or the car.

#### Key fob

##### BYD Han, Dolphin, Seal, Atto 3, and others

A single key architecture spans sedans, hatchbacks, and SUVs across BYD's lineup. Inside the two-piece housing, three functional zones stack end to end: button cluster at the top, circuit board through the middle, mechanical key folded into the base. The metal key blade and the cap enclosing it at the base are the densest structures in the assembly, reading warmest (red) in the scan.

Four switches from left to right: engine start/stop, trunk release, door unlock, door lock. Each button sits above a dedicated tact switch (yellow square) on the PCB, actuated by posts passing through the housing. The four switch positions are visible as small dense clusters distributed across the center of the board, set against the surrounding passive fields.

Folded into the base is a mechanical backup key, a flat metal blade in a hinged housing. It reads warmer than everything else in the scan. It exists for the moment the battery dies or the RF link fails. Every BYD keyless entry system includes this fallback.

The board runs the full length of the interior. A large square IC package near the top is likely the RF transceiver and immobilizer chip handling the rolling code exchange with the vehicle. Barely-visible antenna traces run the board's perimeter. We can see the individual solder joints (and their porosity) across the passive field below.

Power comes from a single CR2032 coin cell, the same 3V lithium button battery in roughly a billion other devices. Its spring contact is visible at the cell's edge. Behind it, molded into the outer housing face, we see the BYD logo.

None of these components is particularly extraordinary in isolation. The battery cell is a compact prismatic that any number of manufacturers produce. The window switch panel uses commodity tact switches and a standard automotive bus protocol. The charger is a safety device wrapped around conventional power electronics. The key fob runs on a coin cell. What’s worth paying attention to is the system that produced them: every part designed in-house, manufactured within BYD's own supply network, shipped on BYD's own vessels. Reducing suppliers and margin layers to a minimum yields faster iteration, tighter control, and lower costs at every layer of the stack.

The result is a car that starts around $15K in China and outsells every other electric vehicle on the planet. BYD already operates in the United States: its electric buses run commuter routes in California, assembled at a factory outside Los Angeles. The passenger car is a different story. A 100% tariff and a federal national security investigation into Chinese connected vehicles have effectively closed that door, at least for now. But BYD has set a target for overseas markets to make up 50% of its total sales, up from 23% in 2025, and it owns the ships to get them there. The wall around the American market is real, but so is the momentum outside of it.