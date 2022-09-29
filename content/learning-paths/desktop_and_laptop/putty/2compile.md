---
# User change
title: "Compile PuTTY natively on Windows-on-Arm"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Pre-requisites

You will need a Windows on Arm device with appropriate build software installed. For full instructions see [here](/install-tools/woa).

Additionally, you will need:
- [Perl](https://www.linaro.org/windows-on-arm/perl/) environment
- A file archive utility, such as [7-Zip](https://www.7-zip.org/download.html)
- A make utility, for example [GnuWin32](http://gnuwin32.sourceforge.net/) or similar

The example application used in this tutorial is [PuTTY](https://www.putty.org/), an open-source SSH and telnet client. License details [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/licence.html).

## Create build folder

Start a Windows command prompt with `Start` > `cmd`.
Create a folder to use for the build, for example `C:\putty`, and move into that folder:
```command
mkdir C:\putty
cd C:\putty
```
## Download source

Download the PuTTY [source archive](https://the.earth.li/~sgtatham/putty/latest/putty-src.zip) and extract into the build folder, using 7-Zip or similar.

## Generate makefiles

**RONAN WHERE IS THIS FILE??**\
**Looks like build system changed (to cmake) since doc was written?**\
See [here](https://developer.arm.com/documentation/102563/0100/Compiling-PuTTY-natively-on-WoA-with-Clang)


The supplied Perl script `mkfiles.pl` automatically generates the makefiles and folders used by the build process:
```code
perl mkfiles.pl
```
The script generates makefiles for several different compilers.

## Configure environment

**RONAN is this necesary?**

 Run the Visual Studio batch file to configure `Command Prompt for Developers`, to automatically configure your environment to compile for Arm-based targets:
```code
cmd /k ""C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat"" x64_arm64
```

## Build application with Microsoft C++ compiler (MSVC) {#msvc}
perl 
TO DO

## Build application with clang {#clang}

Move to the windows subdirectory in the build folder:
```code
cd windows
```
Use the GnuWin32 make utility, or similar, to build the PuTTY application:
```console
C:\GnuWin32\bin\make.exe Platform=arm64 -f Makefile.clangcl all
```
The following options control the build process:
- `Platform=arm64` specifies that the build target is a 64-bit Arm-based system.
- `-f Makefile.clangcl` specifies that the build process uses the Clang compiler.
- `all` directs the build process to compile all components of the PuTTY application.

## Run application

When the build process completes, there will be a new executable `putty.exe` in the windows subdirectory in the build folder. This is the natively compiled PuTTY application.

Double-click it to run and check that it works on your Windows on Arm device.

## Other resources

| Type          | Content             |
| ---           | ---                 |
| Blog          | [Porting PuTTY to Windows on Arm](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/porting-putty-to-windows-on-arm) |
| Documentation | [Compiling with Clang for Windows on Arm](https://developer.arm.com/documentation/102563) |
| Documentation | [Building libraries for Windows on Arm](https://developer.arm.com/documentation/102528) |
