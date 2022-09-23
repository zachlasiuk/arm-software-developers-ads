---
title: "Docker for Windows on Arm"
weight: 4 # (intro is 1), 2 is first, 3 is second, etc.

multitool_install_part: true    # DO NOT MODIFY. Must be true for parts of multi-tools to ensure correct navigation
layout: "installtoolsall"  # DO NOT MODIFY
---

## Install Docker on Windows on Arm {#docker-woa}

Docker can be run on Windows on Arm machines using the Windows Subsystem for Linux 2 (WSL2).

There is no Docker Desktop for Windows on Arm, [please show your support by asking for it](https://github.com/docker/roadmap/issues/91)

### Prerequisites

- Install WSL 2 on the Windows on Arm laptop
- Install a Linux distribution such as Ubuntu 22.04 Linux distribution in WSL 2 from the Microsoft Store

### Example Windows on Arm computers

- Lenovo Thinkpad X13s
- Microsoft Surface Pro X
- Samsung Galaxy Book S

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

There are numerous Linux distribution options from the Microsoft Store including [Ubuntu on Windows](https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6?hl=en-us&gl=us).

For more information about [installing WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install)

