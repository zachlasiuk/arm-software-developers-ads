---
# User change
title: "Bluetooth"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Bluetooth
							
The physical Raspberry Pi 4 supports Bluetooth connections. Use bluetoothctl and scan for devices. I can connect my Android phone to the Raspberry Pi and create various applications to send and receive data between the Pi and the phone using Bluetooth.				
The virtual Raspberry Pi 4 can do similar things.

Use the Linux desktop Bluetooth icon on the top right or the command line.

Run `bluetoothctl` on the command, the use the bluetooth prompt to enter help or other commands.

```bash
bluetoothctl 
```

This goes to the bluetooth prompt. Run `help` to see the commands

```console
Agent registered
[bluetooth]# help
Menu main:
Available commands:
-------------------
advertise                                         Advertise Options Submenu
scan                                              Scan Options Submenu
gatt                                              Generic Attribute Submenu
list                                              List available controllers
show [ctrl]                                       Controller information
select <ctrl>                                     Select default controller
devices                                           List available devices
paired-devices                                    List paired devices
system-alias <name>                               Set controller alias
reset-alias                                       Reset controller alias
power <on/off>                                    Set controller power
pairable <on/off>                                 Set controller pairable mode
discoverable <on/off>                             Set controller discoverable mode
discoverable-timeout [value]                      Set discoverable timeout
agent <on/off/capability>                         Enable/disable agent with given capability
default-agent                                     Set agent as the default one
advertise <on/off/type>                           Enable/disable advertising with given type
set-alias <alias>                                 Set device alias
scan <on/off>                                     Scan for devices
info [dev]                                        Device information
pair [dev]                                        Pair with device
cancel-pairing [dev]                              Cancel pairing with device
trust [dev]                                       Trust device
untrust [dev]                                     Untrust device
block [dev]                                       Block device
unblock [dev]                                     Unblock device
remove <dev>                                      Remove device
connect <dev>                                     Connect device
disconnect [dev]                                  Disconnect device
menu <name>                                       Select submenu
version                                           Display version
quit                                              Quit program
exit                                              Quit program
help                                              Display help about this program
export                                            Print environment variables
```

Then run the scan command

```console
[bluetooth]# scan on 
Discovery started
[CHG] Controller 3E:A3:EC:15:18:E8 Discovering: yes
```

					
## Summary
					
Bluetooth works fine on the virtual Raspberry Pi and it can be used for testing software which relies on a working bluetooth hardware and software. 

Arm Virtual Hardware also incldues a generic Android device which can be used to connect to the bluetooth of the Raspberry Pi. 


