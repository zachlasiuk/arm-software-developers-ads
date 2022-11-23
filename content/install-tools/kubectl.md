---
additional_search_terms: null
layout: installtoolsall
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- failed
title: Kubectl
tool_install: true
---

{{< test >}}

Kubectl is the [Kubernetes](https://kubernetes.io/) command-line tool. 

It is available for Linux, macOS, and Windows.

## Introduction

[General installation information](https://kubernetes.io/docs/tasks/tools/) is available which covers all supported operating systems, but it doesn't talk about Arm. 

This article provides a quick solution to install `kubectl` for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash { command_line="user@localhost | 2" }
uname -m
aarch64
```

## Download and Install

The easiest way to install `kubectl` for Ubuntu on Arm is to use curl and copy the executable to a common location. 

To install curl, for example on ubuntu:

```bash { target="ubuntu:latest" }
sudo apt install -y curl
```

Download and install the latest version of `kubctl`. There is just 1 executable to copy to the desired location.

```bash { target="ubuntu:latest" }
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
```

Install the executable in a common location for all users. 

```bash { target="ubuntu:latest" }
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

Confirm the executable is available.

```bash { target="ubuntu:latest" }
kubectl version
```

Visit the [kubectl documentation](https://kubernetes.io/docs/reference/kubectl/) for more information. 