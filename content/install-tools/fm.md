---
title: "Arm Fast Models"

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
[Arm Fast Models](https://developer.arm.com/Tools%20and%20Software/Fast%20Models) are accurate, flexible programmer's view models of Arm IP. They are used to build a virtual platform, either standalone, or as part of Hybrid Simulation environment within EDA partner environments. Use the virtual platform for software development and verification throughout the development process, even long before any real hardware is available.

This article discusses the stand alone use case. If using as part of an EDA partner's environment, please contact the relevant vendor for guidance.

## Pre-requisites

A Fast Model based virtual platform is an executable that runs on your Linux or Windows host. To **build** such an executable, you must ensure that the appropriate host toolchain is installed.

For Linux hosts, use `gcc 9.3.0`.

For Windows hosts use [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/) 16.7.3 (or later). Express or Community editions can NOT be used.

More information is given in [the documentation](https://developer.arm.com/documentation/100965/1117/Installing-Fast-Models/Requirements-for-Fast-Models).

## Download installer packages

You can download the Fast Models installer from the [Product Download Hub]((https://developer.arm.com/downloads). Linux and Windows hosts are supported.

Full installation instructions are provided [here](https://developer.arm.com/documentation/100965/latest/Installing-Fast-Models/Installation).

Windows users, once installed, open the System Canvas IDE, and select File > Preferences > Applications, and locate the folder containing `devenv.com` in your Visual Studio installation (`\\Common7\IDE`).

## Setting up product license

Arm Fast Models are license managed. License setup instructions are available [here](../license/).

## Get started

To verify everything is working OK, you can build one of the many example projects provided.

 - Launch the System Canvas IDE, and select `File` > `Load Project`, and browse to the `FastModelsPortfolio_<version>\examples' folder.
 - Select any example (such as `\LISA\FVP_MPS2\Build_Cortex-M3\FVP_MPS2_Cortex-M3.sgproj`).
 - Ensure an appropriate Project Configuration is selected from the pulldown in the upper toolbar (such as `Win64_Release-VC19`).
 - Click `Build` in the upper toolbar to build the virtual platform.
 - Once built, click `Run` and select `ISIM system` before launching the virtual platform.
   - If a suitable program image is available (such as the `startup_Cortex-M3_AC6.axf` example from [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio)), you can load this with the `-a` option.

## Fixed Virtual Platforms {#fvp}

Arm supplies a library of ready made [Fixed Virtual Platforms (FVP)](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) that can be used without Arm Fast Models installed. A number of these FVPs are also provided as components of [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

Arm Fixed Virtual Platforms are [license managed](../license/).

## Further Reading

   [Get started with Arm Fast Models](https://developer.arm.com/documentation/102441)
