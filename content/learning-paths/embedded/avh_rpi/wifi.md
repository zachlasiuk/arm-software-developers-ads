---
# User change
title: "Wifi"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Wifi
							
The virtual Raspberry Pi supports Wifi. Arm Virtual Hardware provides a network named "Arm" to connect to. Enter `password` as the password. 

Connect the wireless using the Raspberry Pi OS wizard that runs on first installation. 
The wireless connection can be controlled using the icon on the top right of the Linux desktop. 

To connect to wireless using the command line use `raspi-config`.

```bash
sudo raspi-config
```

Select System Options and then Wireless LAN and select your country.

Enter Arm for the SSID followed by the password above. 

Do not reboot after entering the wireless information.

Use ifconfig to see the network configuration for wlan0.

```bash
ifconfig
```

Here is the output for the wireless connection.

```console
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.11.0.2  netmask 255.255.252.0  broadcast 10.11.3.255
        inet6 fe80::7d83:5b81:56ad:4244  prefixlen 64  scopeid 0x20<link>
        ether 7c:c5:37:a0:05:a6  txqueuelen 1000  (Ethernet)
        RX packets 77  bytes 7086 (6.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 49  bytes 7303 (7.1 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Use iwconfig to see the wireless information.

```bash
iwconfig
```

Here is the output

```console
wlan0     IEEE 802.11  ESSID:"Arm"  
          Mode:Managed  Frequency:2.452 GHz  Access Point: 84:F1:29:FF:FF:FC   
          Tx-Power=3 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
```

Disable the Ethernet interface so the wireless interface is used.

```bash
sudo ifconfig eth0 down
```

Test the wireless connection.

```bash
ping google.com
```

Use ifconfig to see the number of TX and RX packets increasing on wlan0.

Enable Ethernet interface again.

```bash
sudo ifconfig eth0 up
```


## Summary
					
Wifi works on the virtual Raspberry Pi just as it does on a physical Raspberry Pi by using Arm Virtual Hardware provided wireless access point.


