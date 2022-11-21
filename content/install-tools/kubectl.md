---
title: "Kubectl"

additional_search_terms:

# Maintenance settings
test_maintenance: true          # Enables maintenance tests on article
test_images:                    # List Docker images to run instructions on
  - ubuntu:latest

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---

Kubectl is the [Kubernetes](https://kubernetes.io/) command-line tool. 

It is available for Linux, macOS, and Windows.

## Introduction

[General installation information](https://kubernetes.io/docs/tasks/tools/) is available which covers all supported operating systems, but it doesn't talk about Arm. 

This article provides a quick solution to install `kubectl` for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The result should be `aarch64` 

## Download and Install

The easiest way to install `kubectl` for Ubuntu on Arm is to use curl and copy the executable to a common location. 

Download and install the latest version. There is just 1 executable to copy to the desired location.

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
