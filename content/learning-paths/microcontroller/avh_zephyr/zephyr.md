---
# User change
title: "Build and run Zephyr applications"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Zephyr](https://zephyrproject.org/) is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with security in mind.

The Zephyr RTOS is based on a small-footprint kernel designed for use on resource-constrained systems: from simple embedded environmental sensors and LED wearables to sophisticated smart watches and IoT wireless gateways.

We will get the Zephyr source, install the Zephyr SDK, build sample applications, and run them on [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware) Corstone-300 FVP.

## Pre-requisites

A valid [AWS](https://aws.amazon.com/) account is required.

Launch the Arm Virtual Hardware AMI. For full instructions see [here](/install-tools/avh#corstone).

Start by adding the extra repositories to your sources list. This is needed to install the Zephyr dependencies.
```console
wget https://apt.kitware.com/kitware-archive.sh
sudo bash kitware-archive.sh
```

Then, install pre-requisites for Zephyr:

```console
sudo apt update
sudo apt install --no-install-recommends gperf ccache dfu-util device-tree-compiler python3-tk gcc-multilib g++-multilib
```
Some other pre-requisistes needed by Zephyr like python3 and cmake are already installed on your AVH AMI. 

Next, install Python dependencies and activate a new virtual environment

```console
sudo apt install python3-venv
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```
Get the Zephyr source code and install additional python dependencies declared in the source

```console
west init ~/zephyrproject
cd ~/zephyrproject
west update
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

## Install Zephyr SDK on AVH AMI
To build Zephyr applications we need to install the Zephyr Software Development Kit (SDK). It contains the compiler, assembler, linker and other programs needed for building Zephyr applications. Zephyr SDK is supported on Arm architecure but in this case we install the x86_64 version of the SDK as we are building the applications on the AVH AMI.

Download, verify, extract and setup the Zephyr SDK bundle

```
cd ~
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.1/zephyr-sdk-0.15.1_linux-x86_64.tar.gz
wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.1/sha256.sum | shasum --check --ignore-missing
tar xvf zephyr-sdk-0.15.1_linux-x86_64.tar.gz
cd zephyr-sdk-0.15.1
./setup.sh
```

## Build the hello world sample application

There are sample applications included with Zephyr source repo. We will build the [hello world](https://docs.zephyrproject.org/latest/samples/hello_world/README.html) application for the AVH Corstone-300 target.

```console
cd ~/zephyrproject/zephyr
west build -p auto -b mps3_an547 samples/hello_world
```

The application binaries are built in the `~/zephyrproject/zephyr/build/zephyr/` directory.

## Run Zephyr application on AVH Corstone-300 FVP

To run the Zephyr application on the AVH Corstone-300 FVP target, run the command below

```console
VHT_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf
```

You will see telnet terminal windows pop up from the running simulation on the FVP with the output as shown below

```
*** Booting Zephyr OS build zephyr-v3.2.0-881-g35ec706d82a5  ***
Hello World! mps3_an547
```
You have now successfully build a Zephyr application and run it on the AVH Corstone-300 target system. You can now try some of the other sample applications included or build your own.

To build and run the [Dining Philosophers](https://docs.zephyrproject.org/latest/samples/philosophers/README.html) example, use:

```console
west build -p auto -b mps3_an547 samples/philisophers
VHT_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf
```
