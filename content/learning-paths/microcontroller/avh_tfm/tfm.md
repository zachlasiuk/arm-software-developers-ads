---
# User change
title: "Build and run TF-M test cases"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Trusted Firmware-M](https://www.trustedfirmware.org/projects/tf-m/) (TF-M) implements the Secure Processing Environment (SPE) for Armv8-M, Armv8.1-M architectures. It is the platform security architecture reference implementation aligning with [PSA Certified](https://www.psacertified.org/) guidelines.

We will build reference examples, and run them on [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware).

## Pre-requisites

A valid [AWS](https://aws.amazon.com/) account is required.

Launch the Arm Virtual Hardware AMI. For full instructions see [here](/install-tools/avh#corstone).

Install `python 3` pre-requisites for TF-M:
```console
sudo apt update
sudo apt install python3.8-venv
sudo ln -s /usr/local/bin/pip3 /usr/bin/pip3.8
python3.8 -m pip install imgtool cbor2
python3.9 -m pip install imgtool cffi intelhex cbor2 cbor pytest click
```

## Clone the TF-M repository
```console
git clone https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git
cd trusted-firmware-m
```
TF-M uses `cmake` as the build system. Create a build directory, and then set the relevant `cmake` variables to build the TF-M suite of tests. For example:
```console
mkdir cmake_build
cd cmake_build
cmake .. -DTFM_PLATFORM=arm/mps3/an552 -DTEST_NS=ON -DTEST_S=ON
```
In the command above we have prepared a build of both the secure and non-secure suite of TF-M tests. To build individual tests from these suites you can set the appropriate cmake variable instead. All the variables and options are defined in [section 2.12](https://tf-m-user-guide.trustedfirmware.org/docs/getting_started/tfm_build_instruction.html) of the documentation.

## Build using make
```console
make install
```
On a successful build, the TF-M test binaries are created in the `bin` directory. This includes binaries files for the `MCUBoot bootloader`, `TF-M secure firmware` and `TF-M non-secure` app. Signed variants of both the TF-M secure and non-secure images are created along with a combined signed image of both the secure and non-secure image.

## Run the TF-M tests on the Corstone-300 FVP
```console
VHT_Corstone_SSE-300_Ethos-U55 -a cpu0*="bin/bl2.axf" --data "bin/tfm_s_ns_signed.bin"@0x01000000
```
- `bl2.axf` is the MCUBoot bootloader image.

- `tfm_s_ns_signed.bin` is the combined signed image for the TF-M secure and non-secure image
  - `@<addr>` indicates where in the Corstone-300 FVP memory the image is loaded. 

The memory map for the FVP is documented [here](https://developer.arm.com/documentation/100966/1118/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300).

The test results will be output in a `telnet` window.

