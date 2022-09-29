---
title: "Windows on Arm native build tools"

additional_search_terms:
  - clang
  - compiler


tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
This is a summary of native tooling available for [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview) (WoA) applications.

# Visual Studio

[Visual Studio 2022 17.3 Preview 2](https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices) (and higher) natively supports Windows on Arm.

For more information, see [this announcement blog](https://devblogs.microsoft.com/visualstudio/arm64-visual-studio/) from Microsoft.

Previous releases required WoA applications to be cross-compiled on other hosts. When run on an Arm platform with x86 emulation, some features were not supported and performance was poor.

Check the [Microsoft Learn](https://learn.microsoft.com/en-us/windows/arm/overview) site For the latest updates on Arm-native development.

## Install C and C++ support

During installation process, you will be asked what workloads you wish to install. At a minimum, select `Desktop development with C++`.

See the [documentation](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation) for more information.

## Runtime libraries

If needed, download the Arm64 redistributable [runtime libraries](https://aka.ms/vs/17/release/vc_redist.arm64.exe) as described [here](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist).

# LLVM toolchain

[LLVM](https://llvm.org/) (LLVM 14 or higher) natively supports Windows on Arm.

Previous releases required cross-compiling on another host, or using x86 emulation. Typically compilation is twice as fast using the native toolchain vs emulation.

You can download the latest LLVM builds from [here](https://releases.llvm.org/download.html).
  - The pre-built binary for Windows on Arm is typically named `LLVM-<version>-woa64.exe`.

## Compatibility with existing Visual Studio / MSVC projects

LLVM supports `clang-cl`, a compatibility layer for Microsoft Visual C++ (MSVC). This means that most developers can use `clang-cl` to compile their C/C++ applications on Visual Studio/MSBuild on the Windows on Arm device, without needing to change the command line. This allows you to easily modify legacy projects that use MSVC to use native compilation.
