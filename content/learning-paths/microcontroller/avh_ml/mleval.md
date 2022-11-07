---
# User change
title: "Using the ML Evaluation Kit"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [Arm ML Evaluation Kit](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit) provides a number of ready-to-use ML applications. These allow you to investigate the embedded software stack and evaluate performance of the networks running on the Cortex-M55 and Ethos-U55 processors.

In this learning path we will build and run these examples with [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware).

Full instructions are provided in the evaluation kit [documentation](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit/+/HEAD/docs/quick_start.md)

## Pre-requisites

A valid [AWS](https://aws.amazon.com/) account is required.

Launch the Arm Virtual Hardware AMI. For full instructions see [here](/install-tools/avh#corstone).

## Clone the Evaluation kit repository:

In your Arm Virtual Hardware terminal, clone the ML Evaluation Kit repository, and navigate into its directory.
```console
git clone "https://review.mlplatform.org/ml/ethos-u/ml-embedded-evaluation-kit"
cd ml-embedded-evaluation-kit
```

## Resolve external dependencies and prepare build environment:
```console
git submodule update --init
sudo apt install python3.8-venv
```

## Build the example applications

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

Both toolchains are installed within the AMI.

This will take a few minutes to complete.

{{< tabpane code=true >}}
  {{< tab header="Arm Compiler for Embedded" >}}
./build_default.py --toolchain arm
{{< /tab >}}
  {{< tab header="GCC" >}}
./build_default.py
{{< /tab >}}
{{< /tabpane >}}

When complete, you will find the example images (`.axf` files) in the `cmake-build-*/bin` directory. Navigate to that directory.
```console
cd cmake-build-mps3-sse-300-ethos-u55-128-arm/bin
```
## Run an example
To run an example, launch the Virtual Hardware with one of the images, for example:
```console
VHT_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf
```
Note that the virtual hardware takes some time (approx 1 minute) to initialize the NPU. Be patient. If you see warnings regarding loading the image, these can likely be ignored.

When the example is running, a telnet instance will open allowing you to interact with the example.

## Setting model parameters (Optional)

Some additonal parameters can be specified to Arm Virtual Hardware to configure certain aspects of how it executes.

### List parameters

For a full list of the available parameters, launch the executable with the `--list-params` option, for example:
```console
VHT_Corstone_SSE-300_Ethos-U55 --list-params > parameters.txt
```
### Set parameters
Individual parameters can be set with the `-C` command option. For example, to put the Ethos-U component into fast execution mode:
```console
VHT_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf -C ethosu.extra_args="--fast"
```
If you wish to set many parameters, you may find it easier to list them in a text file (without `-C`) and use `-f` to specify that file.

For example, create an `options.txt` containing:
```console
mps3_board.visualisation.disable-visualisation=1
ethosu.extra_args="--fast"
```
and specify with:
```console
VHT_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf -f options.txt
```
## Next steps
The ML Evaluation Kit provides some stand alone examples. These building blocks have been integrated into complete software stacks in the [Open-IoT-SDK](https://github.com/ARM-software/open-iot-sdk).
