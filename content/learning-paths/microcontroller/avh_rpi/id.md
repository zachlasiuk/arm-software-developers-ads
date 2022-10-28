---
# User change
title: "Identifying the Raspberry Pi 4"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Hardware Identification	
				
The first place to start is identifying the hardware. 

Both systems are running the 64-bit Raspberry Pi OS. I have set the hostname of the virtual board to be “pimodel” and the default hostname of “raspberry” for the physical board just to make it clear which one is being shown.

To change the hostname edit the `/etc/hosts` file:

```bash
sudo nano /etc/hosts
```

Change the hostname to `pimodel`

```console
127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters

127.0.1.1       pimodel
```
					
The first command to try is uname. The output is identical on both machines. One of them is shown here. Your output may be slightly different depending on the version of the Linux kernel.

```console
pi@raspberrypi:~ $ uname -a
Linux raspberrypi 5.15.30-v8+ #1536 SMP PREEMPT Mon Mar 28 13:53:14 BST 2022 aarch64 GNU/Linux
```
					
Next, try out lscpu. The physical board shows the following:
				
```console
pi@raspberrypi:~ $ lscpu
Architecture:                    aarch64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
CPU(s):                          4
On-line CPU(s) list:             0-3
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
Vendor ID:                       ARM
Model:                           3
Model name:                      Cortex-A72
Stepping:                        r0p3
CPU max MHz:                     1800.0000
CPU min MHz:                     600.0000
BogoMIPS:                        108.00
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Vulnerable
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm crc32 cpuid
```						 				
					
The virtual board output is below. The CPU model name is Neoverse-N1 with a max frequency of 2 GHz. There are also numerous extra flags printed which are not shown by the real Raspberry Pi. 

```console
pi@pimodel:~ $ lscpu
Architecture:                    aarch64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
CPU(s):                          4
On-line CPU(s) list:             0-3
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
Vendor ID:                       ARM
Model:                           1
Model name:                      Neoverse-N1
Stepping:                        r3p1
CPU max MHz:                     2000.0000
CPU min MHz:                     100.0000
BogoMIPS:                        243.75
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdh
                                 p cpuid asimdrdm lrcpc dcpop asimddp ssbs
```			

The next check is lshw to see more info about other hardware. 

To install it:

```console
sudo apt-get install lshw
```				

The output is long and not all shown. The key differences I spotted are the different serial number (expected) and board revision on the model.
					
The real Raspberry Pi has:

```console
pi@raspberrypi:~ $ lshw
WARNING: you should run this program as super-user.
raspberrypi
    description: Computer
    product: Raspberry Pi 4 Model B Rev 1.4
    serial: 100000004d20671f
    width: 64 bits
    capabilities: smp cp15_barrier setend swp tagged_addr_disabled
```				
					
The virtual Raspberry Pi is nearly identical, just missing the Rev 1.4 on the product.

```console
pi@pimodel:~ $ lshw
WARNING: you should run this program as super-user.
raspberrypi
    description: Computer
    product: Raspberry Pi 4 Model B
    serial: 6baad94fb19b396d
    width: 64 bits
    capabilities: smp cp15_barrier setend swp tagged_addr_disabled
```
					
The Wireless interface is same in both cases. Here is the section for the Wireless interface on the real Raspberry Pi followed by the virtual Pi.
				
```console
  *-network:1
       description: Wireless interface
       physical id: 2
       logical name: wlan0
       serial: dc:a6:32:b1:b6:18
       capabilities: ethernet physical wireless
       configuration: broadcast=yes driver=brcmfmac driverversion=7.45.241 firmware=01-703fd60 ip=192.168.68.96 multicast=yes wireless=IEEE 802.11
```

The virtual Raspberry Pi is identical, just the MAC address and the IP address are different.

```console
*-network:1
       description: Wireless interface
       physical id: 2
       logical name: wlan0
       serial: 7c:c5:37:e8:9d:c6
       capabilities: ethernet physical wireless
       configuration: broadcast=yes driver=brcmfmac driverversion=7.45.241 firmware=01-abcd0123 ip=10.11.0.2 multicast=yes wireless=IEEE 802.11
```

The Ethernet networking interface is also the same, no differences are detected.
					
The initial survey shows the virtual board looks very close to a real Raspberry Pi. The virtual model of the Pi shows a 4 Gb RAM configuration. A physical Pi may have a differernt RAM size as there are also 2 Gb or 8 Gb RAM sizes available.
			
The CPU model name is really the only clear sign that this is not a real Raspberry Pi 4.

Let's look at some example software and check the performance of the virtual Raspberry Pi. 
