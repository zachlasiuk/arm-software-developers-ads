---
# User change
title: "Linux Kernel Compile"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Applications and Performance	
			
Let’s try some benchmarks to investigate the performance differences between the actual Raspberry Pi and the virtual Raspberry Pi. 

The first trial is to compile the Linux kernel.	
				
## Linux Kernel Compile
					
One of the benefits of the Raspberry Pi compared to other Linux boards used in embedded projects is the ease of building the Linux kernel. The good news is the Linux kernel is very easy to build natively on the Raspberry Pi. The bad news is that it takes a very long time. The instructions even have a warning (with long in bold).	
				
“this step can take a **long** time depending on the Raspberry Pi model in use”		
			
Follow the [Linux kernel information](https://www.raspberrypi.com/documentation/computers/linux_kernel.html) to build a kernel on the real Raspberry Pi and the virtual Raspberry Pi to see how long it takes. As a reference, I did the exact same thing on an x86_64 virtual machine in AWS using a cross compiler.				
				
								
| System | Kernel compile time             |
|--------|--------------------------------:|
|Physical Raspberry Pi 4 (8 Gb RAM)   | 81 min 17 sec |
|Virtual Raspberry Pi 4 (4 Gb RAM)    | 20 min 6 sec |
|AWS EC2 c5.xlarge (4 vCPU, 8 Gb RAM) | 28 min 27 sec |	


## Summary

Kernel building is significantly faster on the virtual Raspberry Pi and no cross compiling and file copying is required. Even cross compiling on an x86_64 machine is not faster than the virtual Raspberry Pi.
	

