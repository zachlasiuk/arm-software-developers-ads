---
title: "Install GCC on Arm Linux"

tool_install: true
---

GCC, the GNU Compiler Collection, is available on all Linux distributions and can be installed using the package manager.

## Introduction

Follow the instructions below to install and use GCC on an Arm Linux distribution. This covers gcc and g++ for compiling C and C++

Confirm you are using an Arm machine by running:

```console
uname -m
```

The output should be:

```console
aarch64
```

## Download 

The Linux package manager downloads the required files so there are no special instructions.

## Installation {#install}

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install software packages on any Debian based Linux distribution, including Ubuntu.

```console
sudo apt update
sudo apt install gcc g++ -y
```

Another meta-package on Ubuntu is ``build-essential``. This will install the most common tools libraries with a single command.

```console
sudo apt install -y build-essential
```

### Installing on Red Hat / Fedora / Amazon Linux

These Linux distributions use `yum` as the package manager. 

To install the most common development tools use the commands below. If the machine has `sudo` you can use it.

```console
sudo yum update
sudo yum groupinstall 'Development Tools'
```

If `sudo` is not available become _root_ and omit the `sudo`.

```console
yum update
yum groupinstall 'Development Tools'
```

## Setting up product license {#license}

Arm GNU Toolchain is open source and freely available for use. No licenses need to be set up for use.

## Get started {#start}

To confirm the installation is complete run:

```console
gcc --version
```

To compile an example program, create a text file named hello-world.c with the contents below.

```C
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

To compile the hello-world program use:

```console
gcc -o hello-world hello-world.c
```

To run the application enter:

```console
./hello-world
```

The program will print the string in the printf() statement.

