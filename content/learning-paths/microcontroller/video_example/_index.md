---
title:  CI/CD and MLOps Workflow for IoT Endpoint Development

description: Today, the validation process for IoT endpoint applications relies heavily on target hardware with manual user interaction. For automated CI/CD workflows a robust test environment with controlled, repeatable input stimuli is required. Fast Models combined with Python scripting provide this for unit and integration testing. Using a flexible tool flow, applications can be validated in simulation on CI/CD or MLOps environments, verified for correctness on hardware, and deployed to the final system.

minutes_to_complete: 26

who_is_this_for: MLOps developers who want to scale up CI/CD unit and integration tests using virtual hardware.

learning_objectives: 
    - Install the Raspberry Pi Pico SDK
    - Run a hello world example
    - Measure application performance
    - Debug applications

prerequisites:
    - Familiar with simulation technology such as Arm Fast Models
    - Python language knowledge is helpful 

author_primary: Reinhard Keil

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M
tools:
    - Keil MDK
    - uVision
softwares:
    - Python
operatingsystems:
    - RTOS

### video only
video_url: 3fBwVi-F8vI
video_date: Jan 5, 2022
author_info: Senior Director of Embedded Tools - Arm
further_reading:
    - resource:
        title: GitHub Actions
        link: https://docs.github.com/en/actions
        type: documentation
    - resource:
        title: Arm Virtual Hardware
        link: https://arm-software.github.io/AVH/main/examples/html/GetStarted.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "video-page"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
