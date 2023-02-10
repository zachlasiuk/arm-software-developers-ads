---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Kubectl

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- Kubernetes

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

### Link to official documentation
official_docs: https://kubernetes.io/docs/reference/kubectl

### TEST SETTINGS
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-software-developers-ads/actions/runs/3540052189
test_maintenance: true
test_status:
- passed

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

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

Confirm the executable is available and get the version of the client:

```bash { target="ubuntu:latest" }
kubectl version -o json --client
```
