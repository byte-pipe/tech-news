---
title: GitHub - pollen-robotics/microduck: A Tiny biped duck robot 🦆 · GitHub
url: https://github.com/pollen-robotics/microduck
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-10-24T14:30:37.214481
---

# GitHub - pollen-robotics/microduck: A Tiny biped duck robot 🦆 · GitHub

# Microduck Project Overview
=====================================

The Microduck project is a tiny biped robot that uses reinforcement learning policies to navigate its environment.

## Project Structure
-------------------

*   The repository is organized into several folders and files, including:
    *   `docs` for documentation and cheat sheets
    *   `repo` containing the project structure and files
    *   `tests` for unit tests
    *   `scripts` and `utils` for additional utilities
    *   `README.md` for project information

## Key Features
----------------

*   The robot is controlled by a handful of daemons on a Rockchip RK3566 processor at a 50 Hz control loop.
*   The robot uses neural policies to learn and improve its movement and actions.
*   The policies are trained on the `microduck_rl` simulator using MuJoCo and PPO algorithms.

## How it Works
----------------

1.  The robot receives instructions from the `microduck_rl` simulator to perform actions such as walking, rolling, grasping, and more.
2.  The `microduck_rl` simulator sends the instructions to the robot via a Bluetooth connection, which uses a custom application called `duckctl`.
3.  The robot receives the instructions and uses them to perform the corresponding actions.
4.  The robot collects rewards or penalties for its actions, which it uses to update its policy to encourage better behavior.

## Getting Started
------------------

*   Clone the repository to a personal computer.
*   Install the necessary dependencies, including `rock CHIP`, `torch`, and `numpy`.
*   Run the `microduck_rl` simulator to train the policies and configure the robot.
*   Once trained, use `duckctl` to deploy the robot and control it using the `microduck_rl` simulator.

## Example Use Cases
----------------------

*   **Walking**: Use the `duckctl` command to make the robot walk while it's stationary.
*   **Grasping**: Connect a tablet to the robot and use `duckctl` to control its grasping actions when the robot is in roller mode.
*   **Object detection**: Use `duckctl` to control the robot's movements and detect objects around it.