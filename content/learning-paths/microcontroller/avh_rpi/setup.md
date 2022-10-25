---
# User change
title: "Setup a Raspberry Pi 4 with Arm Virtual Hardware" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Pre-requisites

The following pre-requisites are needed to try the steps yourself:

- Physical Rasbperry Pi 3 or 4 (optional)
- A user account for [Arm Virtual Hardware 3rd Party Hardware](https://avh.arm.com/). 

Refer to [Arm Virtual Hardware](/install-tools/avh/#thirdparty) for more information.

## Login to the Arm Virtual Hardware console

Open your browser, and navigate to [Arm Virtual Hardware dashboard](https://app.avh.arm.com):

The URL is:

```console
https://app.avh.arm.com/
```

## Create a Raspberry Pi 4 virtual device

Click on `Create Device`.

Select `Raspberry Pi 4` from the list of available devices.

Select `Raspberry Pi OS Desktop` as the software image and finally `Create Device`.

## Login to virtual Raspberry Pi instances

When your instance is created, select the `Console` tab, and log into the Raspberry Pi 4.

- Username: `pi`
- Password: `raspberry`

It is also possible to log in via the CLCD window view. 

## (Optional) Connect via SSH

The `Console` view within the browser will suffice to complete this learning path.

If you wish to connect via `SSH` (rather than `Console`), it is easiest to download and install the appropriate [OpenVPN Community](https://openvpn.net/community-downloads) version for your host.

In the Arm Virtual Hardware `Connect` tab, Click on `DOWNLOAD OVPN FILE` within the `Connect via VPN` section.

In the `OpenVPN` GUI, select `Import` > `Import file...` and browse to the downloaded `OVPN file`. Click `Connect`.

On your host, open terminal(s), and connect to the virtual hardware instance(s) with the command shown in the `Connect` tab, or use your preferred terminal application.

## Install Raspberry Pi OS on the physical Raspberry Pi 

Install Raspberry Pi OS on a physical board using the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html). This will enable side-by-side comparison. Make sure to install the 64-bit version of Raspberry Pi OS. 

We are now ready to compare the physical and the virtual Raspberry Pi to learn more.


