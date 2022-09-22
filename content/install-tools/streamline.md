---
title: "Arm Streamline"

tool_install: true
---
[Arm Streamline Performance Analyzer](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) is an application profiler for Android, Linux and bare-metal applications. This tool helps you optimize your software written for devices with Arm processors.

Streamline is available as a component of [Arm Mobile Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio) or [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

The version of Streamline provided with Arm Mobile Studio supports [certain Android targets](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Supported-Devices) only. For other use cases, use the version of Streamline provided with Arm Development Studio.

## Download installer packages

Download the appropriate package from the [Product Download Hub](https://developer.arm.com/downloads).

 - [Arm Mobile Studio](https://developer.arm.com/downloads/view/MOBST-PRO0)
 - [Arm Development Studio](https://developer.arm.com/downloads/view/DS000B)

## Installation

Install Arm Mobile Studio using these [instructions](https://developer.arm.com/documentation/102526).

Install Arm Development Studio using the instructions in the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio). See also [this article](../armds).

If using an Android target, you must install Android Debug Bridge(adb) available with [Android SDK platform tools](https://developer.android.com/studio/releases/platform-tools). Add the path to the downloaded Android SDK platform tools directory to your `PATH` environment variable.

## Setting up product license

Arm Mobile Studio includes a free starter edition license which is automatically configured.

Arm Development Studio, as well as Arm Mobile Studio [Professional Edition](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Editions), is license managed. License setup instructions are available [here](../license).

## Get started

To configure your target and/or application for Streamline, follow the appropriate instructions below depending on your use case:

 - [Android](https://developer.arm.com/documentation/101813)
 - [Linux](https://developer.arm.com/documentation/101814)
 - [Bare-metal (and RTOS)](https://developer.arm.com/documentation/101815)

Depending on your type of application, choose the appropriate guide below to get started with profiling your application using Streamline.

- [Profile your Android Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-Android-application)
- [Profile your Linux Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-Linux-application)
- [Profile your bare-metal Application](https://developer.arm.com/documentation/101816/latest/Getting-started-with-Streamline/Profile-your-bare-metal-application)
