---
title: "Arm Keil Studio (VS Code Extension)"

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
[Arm Keil Studio](https://keil.arm.com/) is the next generation software development environment for Arm Cortex-M based microcontroller devices. The desktop version is available as a set of [VS Code](https://code.visualstudio.com/) extensions that offer the same functionality as the cloud-native version.

It supports more than 9,500 devices and is easy to learn and use.

## Prerequisites

- Install an appropriate compiler toolchain.
    * [Install Arm Compiler for Embedded toolchain](/install-tools/armclang/)
    * [Install Arm GNU toolchain](/install-tools/gcc/#Arm-GNU)
- Install [CMake](https://cmake.org/) and [Ninja](https://ninja-build.org/).
- Install [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases).
- Initialize or update the catalog of public CMSIS-Pack versions (using [cpackget](https://github.com/Open-CMSIS-Pack/devtools/blob/main/tools/cpackget/docs/cpackget.md)).


## Install the extensions

1. In VS Code, go to the **Extensions** view.

1. Search for **Keil Studio Pack**.

1. Click the **Install** button for the extension pack.

    Visual Studio Code installs the extensions. All recommended extensions are now available in the **Extensions** view.

## Get started

In the **Extensions** view, select the **Keil Studio Pack** extension and follow the supplied **Tutorial** to verify everything is installed correctly.
