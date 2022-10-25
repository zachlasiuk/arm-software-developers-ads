---
# User change
title: "Linux Perf"

weight: 10 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Linux Perf					

A common scenario is for a software developer to use perf to analyze performance. Install and enable it using the commands below. Make sure to become root for the last two commands.
			
```bash		
sudo apt-get install linux-perf	-y
sudo su -
```

Now as root:

```bash
echo -1 > /proc/sys/kernel/perf_event_paranoid
echo 0 > /proc/sys/kernel/kptr_restrict
```

Exit root:

```bash
exit
```
					
Linux perf works fine on both the physical and virtual Raspberry Pi 4, but there are additional perf events on the virtual Raspberry Pi 4 because of the different underlying hardware.		
				
To list the available perf events:

```console			
perf list
```
					
An example event which is included in the virtual Raspberry Pi 4 is stalled-cycles-backend. This is not available in the physical Raspberry Pi 4.

Run a tar command to zip the kernel source tree and count the `stalled-cycles-backend` event. 

```console
pi@pimodel:~ $ perf stat -e stalled-cycles-backend tar cfz test.tgz ./linux/

 Performance counter stats for 'tar cfz test.tgz ./linux/':

    27,701,570,350      stalled-cycles-backend    #    0.00% backend cycles idle

      44.461783841 seconds time elapsed

      43.283230000 seconds user
       2.121127000 seconds sys

```
					
The physical Raspberry Pi doesn’t have this event.

```console
pi@raspberrypi:~ $ perf stat -e stalled-cycles-backend tar cfz test.tgz ./linux/

 Performance counter stats for 'tar cfz test.tgz ./linux/':

   <not supported>      stalled-cycles-backend

     143.177396310 seconds time elapsed

     129.623757000 seconds user
       8.292624000 seconds sys

```			
					
## Summary

Perf works well on both devices, but there are extra events on the virtual Raspberry Pi 4 due to the Neoverse-N1 processor and its associated architecture.


