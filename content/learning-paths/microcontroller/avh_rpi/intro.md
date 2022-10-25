---
# User change
title: "Introduction to the Raspberry Pi 4 in Arm Virtual Hardware" 

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Introduction 

[Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware) includes several virtual devices including a [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/). Raspberry Pi products have made a significant impact in many areas of computing. In 2022, the Raspberry Pi was hailed as the [most successful computer ever created in the UK](https://www.cam.ac.uk/stories/raspberrypi). More than 40 million boards have shipped during the first 10 years.

The Raspberry Pi provided by Arm Virtual Hardware uses a combination of native software execution and modeling extensions to cover the architecture and peripherals of the physical board.  

Virtual boards are very similar to physical boards, but virtual boards run in the cloud and users connect to them using a browser, command line, or an API.

Software developers use virtual machines and cloud services from providers such as AWS, Microsoft Azure, and Google Cloud to do development tasks. These compute resources help with a variety of tasks, but don't take the place of special purpose hardware such as Raspberry Pi boards. Historically, access to special purpose computing hardware in the cloud has not been available, and most developers rely on physical boards to do many software development and testing tasks. 

This learning path introduces the Raspberry Pi 4 provided by Arm Virtual Hardware, and compares it to a physical Raspberry Pi 4. Developers will be able to decide if Arm Virtual Hardware is right for them.

## Background	
				
Embedded and IoT end-node developers often use a combination of physical boards (on their desk or in a lab) and virtual hardware models. Tools such as [Arm Fast Models](https://developer.arm.com/tools-and-software/simulation-models/fast-models) and [QEMU](https://www.qemu.org) are used for early software development and testing. 

Most virtual models translate Arm instructions to x86_64 instructions. Instruction translation has trouble keeping up with the performance needs of software developers. This is especially true for recent Cortex-A and Neoverse processors. 

Creating models of complete boards using Fast Model technology is challenging.

Arm Virtual Hardware is an alternative solution that provides complete, high-performance models based on virtualization technology running in the cloud. 

There are many common questions about the differences between a virtual board and the physical board.	
 
- What is different about them? 
- What kind of software can be run? 
- Can I measure performance on the virtual board?

Let’s review the differences and similarities between a Raspberry Pi 4 and a virtual Raspberry Pi 4 running in the cloud.

## Raspberry Pi 4 hardware specs

First, let’s review the Raspberry Pi 4 specs.

- SoC: Broadcom BCM2711B0 quad-core A72 (ARMv8-A) 64-bit @ 1.5GHz
- GPU: Broadcom VideoCore VI 	
- Networking: 2.4 GHz and 5 GHz 802.11b/g/n/ac wireless LAN
- RAM: 1GB, 2GB, or 4GB LPDDR4 SDRAM 
- Bluetooth: Bluetooth 5.0, Bluetooth Low Energy (BLE) 		
- GPIO: 40-pin GPIO header, populated
- Storage: microSD
- Ports: 2 × micro-HDMI 2.0, 3.5 mm analogue audio-video jack, 2 × USB 2.0, 2 × USB 3.0, Gigabit Ethernet, Camera Serial Interface (CSI), Display Serial Interface (DSI)

In many ways the Raspberry Pi 4 looks like a regular Arm Linux computer. Recent performance increases, dual-monitor support, and the Raspberry Pi 400 kit make it a suitable desktop computer for many use cases. 

In other ways, the Raspberry Pi looks more like a board for embedded systems. It has GPIO pins for connecting to extra hardware and has inspired people around the world to create thousands of unique projects.

Let’s start comparing the physical Raspberry Pi 4 and the virtual Raspberry Pi 4. 
