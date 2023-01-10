---
title: "Arm Compiler for Linux"

additional_search_terms:
  - armclang
  - compiler


tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
[Arm Compiler for Linux](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux) is tailored to the development of High Performance Computing (HPC) applications. Arm Compiler for Linux is a combination of Arm C/C++ Compiler (armclang), Arm Fortran Compiler (armflang), and Arm Performance Libraries (ArmPL).

## Prerequisites

[Arm Compiler for Linux](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux) runs on 64-bit Arm computers, it is not a cross-compiler.

You need 64-bit Arm hardware running one of the following Linux distributions:
  * Ubuntu (18.04 or 20.04)
  * Red Hat Enterprise Linux (RHEL7 or RHEL8) 
  * SUSE Linux Enterprise Server (SLES-15)

If any of the following tools are not already installed by your Linux distribution, you must install them before installing Arm Compiler for Linux:

* Python (version 2.7 or later)
* C Libraries:
  - SUSE and RHEL: glibc-devel
  - Ubuntu: libc6-dev


Confirm you are using an Arm machine by running:

```bash { command_line="user@localhost | 2" }
uname -m
aarch64
```

## Download  {#download}

Visit [Download Arm Compiler for Linux](https://developer.arm.com/downloads/-/arm-compiler-for-linux) and select the package for your Linux distribution. 
The packages contain the C/C++ and Fortran Compilers and Arm Performance Libraries.

Individual packages with only the Arm Performance Libraries (ArmPL) are also available for download.

Download releases from the command line using wget.

For Ubuntu:

```bash { target="ubuntu:latest" }
wget  https://developer.arm.com/-/media/Files/downloads/hpc/arm-compiler-for-linux/22-1/arm-compiler-for-linux_22.1_Ubuntu-20.04_aarch64.tar
```

For Red Hat:
```bash { target="fedora:latest" }
wget https://developer.arm.com/-/media/Files/downloads/hpc/arm-compiler-for-linux/22-1/arm-compiler-for-linux_22.1_RHEL-8_aarch64.tar
```

## Installation

To install the Arm Compiler for Linux package on your 64-bit Linux Arm machine extract the package and run the installation script. 

Each command sequence includes accepting the license agreement to automate the installation and installing the `modules` software.

For Ubuntu:

```bash { target="ubuntu:latest" }
tar -xvf arm-compiler-for-linux_22.1_Ubuntu-20.04_aarch64.tar 
cd arm-compiler-for-linux_22.1_Ubuntu-20.04
sudo ./arm-compiler-for-linux_22.1_Ubuntu-20.04.sh --accept
sudo apt-get install environment-modules -y
```

For Red Hat:

```bash { target="fedora:latest" }
tar -xvf arm-compiler-for-linux_22.1_RHEL-8_aarch64.tar
cd arm-compiler-for-linux_22.1_RHEL-8.sh
sudo ./arm-compiler-for-linux_22.1_RHEL-8.sh --accept
sudo yum -y install environment-modules
```

Arm Compiler for Linux uses environment modules to dynamically modify your user environment on Linux. If needed, refer to the [Environment Modules documentation](https://lmod.readthedocs.io/en/latest/#id) for more information.

Add module files to the `MODULEPATH` environment variable. 

```bash
export MODULEPATH=$MODULEPATH:/opt/arm/modulefiles
```

To list available modules:

```console
module avail
```

To configure Arm Compiler for Linux:

```bash
module load acfl/22.1
```

To configure GCC:

```bash
module load gnu/11.2.0
```

Refer to the [installation instructions](https://developer.arm.com/documentation/102621/0100/Install) for more details.

## Setting up product license

You do not require a license to use Arm Compiler for Linux.

## Get started

To get started with the Arm C/C++ Compiler and compile a simple application follow the steps below. 

Check that the correct compiler version is being used:
```bash
armclang --version
```

To compile an example program, create a text file named hello.c with the contents below.

```C { file_name="hello.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

To compile the hello-world program use:

```console
armclang hello.c -o hello
```

Run the application.

```bash 
./hello
```

The hello-world program will print the string specified in the print statement.

To get started with the Arm Fortran Compiler and compile a simple application follow the steps below. 

To confirm the installation is complete run:

```bash
armflang --version
```

To compile an example program, create a text file named hello.f90 with the contents below.

```fortran { file_name="hello.f90" }
program hello
  ! This is a comment line; it is ignored by the compiler
  print *, 'Hello, Arm world!'
end program hello
```

To compile the hello-world program use:

```bash
armflang hello.f90 -o hello
```

To run the application enter:

```bash 
./hello
```

The hello-world program will print the string specified in the print statement.

To get started with the [Arm Performance Libraries](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Libraries) and learn how to select the optimal library for your system, follow the guide [here](https://developer.arm.com/documentation/102574/0100).
