---
title: "Docker"

multi_install:         # True only for tools that have multiple options to install them (like Docker Engine vs Desktop). can be deleted if this does not apply.
    - install:
        name: "xyz"
        page_link: "#docker-engine"
        explination: >
            MongoDB is fully supported on 64-bit Arm servers running Linux.

    - questions:
        question: >
            Can you test MongoDB performance by running multiple threads executing different operation types?
        answers:
            - "Yes"
            - "No"
        correct_answer: 0                     
        explination: >
            You can run multiple threads executing either all the same or different database operations.
               
tool_install: true         # DO NOT MODIFY. Always true for tool installs

additional_search_terms:
  - container

---

# Install Docker {#top}

Docker containers are widely used, primarily because they run the same everywhere. Containers are used on all operating systems, on all computing architectures to build, share, and run software.

The operating system of the computer and the architecture (x86 or Arm) will determine how to install Docker.

Select from the links below to install Docker.

[Install Docker Engine on Linux](#docker-engine)

Docker Engine for Linux runs on a variety of Linux distributions and architectures, including arm and arm64 (aarch64). Use these instructions for Linux and Chrome OS (using the Linux feature).

[Install Docker Desktop](#docker-desktop)

Docker Desktop is the easiest way to install Docker on Windows and macOS.

The macOS version supports both Intel and Apple Silicon. The Windows version does not support Windows on Arm.

There is also a new Docker Desktop for Linux available if the machine has KVM support and is running a KDE or Gnome desktop environment.

[Install Docker on Windows on Arm ](#docker-woa)

Docker can be run on Windows on Arm machines using the Windows Subsystem for Linux 2 (WSL2).

There is no Docker Desktop for Windows on Arm, [please show your support by asking for it](https://github.com/docker/roadmap/issues/91)


## Install Docker Engine on Linux {#docker-engine}

For any Linux machine, the commands below will install Docker.

These commands are the (almost) universal install instructions for Docker on Linux.

The architecture can be x86_64 or Arm, including a cloud server and a Raspberry Pi.

The commands can also be used in the Windows Subsystem for Linux (WSL) and on a Chromebook.

For information about starting the docker daemon on WSL refer to [Install Docker on Windows on Arm](#docker-woa).

```console
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

To confirm the installation is successful run:

```console
docker run hello-world
```

The output should be a welcome message such as:

```console
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

To identify the architecture of the machine use the uname command:

```console
uname -m
```
Output values can be aarch64 (Arm 64-bit), armv7l (Arm 32-bit) or x86_64. 

### Docker Engine versions

The Stable channel (get.docker.com) provides the latest releases for general availability.

The Test channel (test.docker.com) installs pre-releases that are for testing before general availability. 

Replace get.docker.com with test.docker.com to use the test version.

### Linux distributions where [get.docker.com](https://get.docker.com) isn't supported

Some Linux distributions are not supported by get.docker.com

Generally, the supported list is:
* Ubuntu
* Debian
* SUSE Linux Enterprise Server
* Red Hat Enterprise Linux
* Fedora
* CentOS

An example of a distribution which is not supported and popular on Arm is [Manjaro](https://manjaro.org).

On Manjaro, install docker using pacman.

```console
sudo pacman -Syu 
sudo pacman -S docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER ; newgrp docker
```

To confirm the installation is successful run the same hello-world as above.

```console
docker run hello-world
```

### Start and Stop the Docker daemon on Linux distributions with systemd

To start the docker daemon.

```console
sudo systemctl start docker
```

To stop the docker daemon.

```console
sudo systemctl stop docker
```

If a message is displayed:

```console
Warning: Stopping docker.service, but it can still be activated by:
  docker.socket
```

Then stop docker.socket.

```console
sudo systemctl stop docker.socket
```

### More information

Refer to the [Installation instructions](https://docs.docker.com/engine/install/) for more information about installing Docker Engine on Linux.

[Return to the top](#top)


### Install and test Docker Desktop{#docker-desktop}

All of the download files are available on the 
[Docker Desktop product page](https://www.docker.com/products/docker-desktop/).

Use the links below for more information

[Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install) 

[Install Docker Desktop on Apple Silicon](https://docs.docker.com/desktop/mac/apple-silicon/) 

[Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) 

[Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/) 

All of the Docker Desktop products use the x86_64 / amd64 architecture except macOS on Apple Silicon.

On any platform, To confirm the Docker Desktop installation is successful run:

```console
docker run hello-world
```

The output should be a welcome message such as:

```console
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

To identify the architecture for macOS use the uname command. 

```console
uname -m
```
Apple Silicon will be reported as arm64


[Return to the top](#top)

## Install Docker on Windows on Arm {#docker-woa}

Docker can be run on Windows on Arm machines using the Windows Subsystem for Linux 2 (WSL2).

There is no Docker Desktop for Windows on Arm, [please show your support by asking for it](https://github.com/docker/roadmap/issues/91)

### Prerequisites

- Install WSL 2 on the Windows on Arm laptop
- Install a Linux distribution such as Ubuntu 22.04 Linux distribution in WSL 2 from the Microsoft Store

### Example Windows on Arm computers

- [Lenovo Thinkpad X13s](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadx/thinkpad-x13s-(13-inch-snapdragon)/len101t0019)
- [Microsoft Surface Pro X](https://www.microsoft.com/en-us/d/surface-pro-x/8xtmb6c575md?activetab=pivot%3aoverviewtab)

### Install and test Docker Engine

From within WSL2 running a Linux distribution on a Windows on Arm laptop, the general Linux install instructions can be used. 

```console
curl -fsSL test.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

The Docker daemon will not automatically start in WSL 2. 

It can be started manually:
```console
sudo /etc/init.d/docker start
```

It can also be started automatically using by editing /etc/wsl2.conf

Add the info below to the file:

```console
# Set a command to run when a new WSL instance launches. This example starts the Docker container service.
[boot]
command = service docker start
```



To confirm the installation is successful run:

```console
docker run hello-world
```

The output should be a welcome message such as:

```console
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

### More information

Refer to the [Installation instructions](https://docs.docker.com/engine/install/) for more information about installing Docker Engine on Linux.

There are numerous Linux distribution options from the Microsoft Store including [Ubuntu on Windows](https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6?hl=en-us&gl=us).

For more information about [installing WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install)

[Return to the top](#top)
