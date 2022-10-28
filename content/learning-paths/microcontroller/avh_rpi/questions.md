---
# User change
title: "Questions"

weight: 11 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Other questions

Here are some frequently asked questions related to the virtual Raspberry Pi. 

### Can I create a program that works on the virtual Raspberry Pi but not on a physical Raspberry Pi?
					
Yes, some of the software that is compiled for Arm Neoverse-N1 will work on the virtual Raspberry Pi 4, but not on the actual Raspberry Pi.

One example in Anaconda. Refer to the [installation for Anaconda](/install-tools/anaconda/). Anaconda is clearly targeted for server hardware and uses architecture features not available on the Raspberry Pi. 

The Anaconda installation of PyTorch works on the virtual Raspberry Pi 4 and the simple PyTorch example also works. The physical Raspberry Pi 4 doesn't complete the installation.
					
As happens with software which uses architecture features newer than the Cortex-A72 the software stops with “Illegal instruction” and this happens on the physical Raspberry Pi 4.		

The same thing will likely happen on any software compiled with instructions not included in the Cortex-A72 but present in the Neoverse-N1 processor. This may include dot product instructions or low-cost atomic instructions (also known as [Large System Extensions, LSE](/learning-paths/cloud/lse/)).	
				
### Can I create a program that works on the physical Raspberry Pi but not on the virtual Raspberry Pi?
					
Vulkan support on the Raspberry Pi 4 is one way to demonstrate this. Follow the [instructions for building some demo Vulkan apps](https://qengineering.eu/install-vulkan-on-raspberry-pi.html). Both systems build the Vulkan software and demo applications correctly. The demos work fine on the physical Raspberry Pi 4. The traditional “gears” application and others on the referenced instructions work just like the article. On the virtual Raspberry Pi 4 the gears application fails with a Vulkan error.	
			
### Can KVM (kernel-based virtual machine) be used?
					
Because the virtual Raspberry Pi 4 is running under the control of a hypervisor it cannot use KVM.
					
The physical Raspberry Pi does have KVM support and it can be seen in the kernel boot log and the device node.

```console
pi@raspberrypi:~ $ dmesg | grep kvm
[    0.297625] kvm [1]: IPA Size Limit: 44 bits
[    0.298810] kvm [1]: vgic interrupt IRQ9
[    0.299076] kvm [1]: Hyp mode initialized successfully
```			
					
The virtual Raspberry Pi 4 does not have KVM. Probably doesn’t matter much for application development and this is the point of the virtual Raspberry Pi, it is an alternative to using qemu + kvm as a type 1 hypervisor.

```console
pi@pimodel:~ $ dmesg | grep kvm
[    0.779186] kvm [1]: HYP mode not available
```
					

### Can Raspberry Pi OS be updated to the latest version?

Update and install software as normal on the virtual Raspberry Pi. 

```bash
sudo apt update ; sudo apt upgrade -y
```

It's important to be aware that if the Linux kernel is updated the kernel needs to be updated in the device configuration. Refer to [Fixing the Updated Kernel File](https://intercom.help/arm-avh/en/articles/6278501-updating-the-raspberry-pi-4-kernel#h_7d121890f9)

### Can other operating systems such as Ubuntu Desktop be installed?

Yes, refer to [Package Ubuntu Desktop Firmware for AVH](https://intercom.help/arm-avh/en/articles/6523083-package-ubuntu-desktop-firmware-for-avh) for more information.

## Summary
					
There are some differences between the physical and virtual Raspberry Pi devices, but they are minor and don't impact most developers. 


