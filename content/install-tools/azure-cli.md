---
title: "Azure CLI"

additional_search_terms:

# Maintenance settings
test_maintenance: true          # Enables maintenance tests on article
test_images:                    # List Docker images to run instructions on
  - ubuntu:latest

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---

[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) is a cross-platform command-line tool that can be installed locally on development computers. Azure CLI is used to connect to Azure and execute administrative commands on Azure resources. 

It is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

## Introduction

[General installation information](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) is available which covers all supported Linux distributions. The instructions state that Azure CLI doesn't support Linux on Arm. 

It's likely Arm support will come soon, monitor the [GitHub issue](https://github.com/Azure/azure-cli/issues/7368) for new details. 

This article provides a quick solution to install Azure CLI for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The result should be `aarch64` 

## Download and Install

The easiest way to install Azure CLI for Ubuntu on Arm is to use Python pip. 

Install Python pip. 

```bash { target="ubuntu:latest" }
sudo apt install python3-pip python-is-python3 -y
```

Download and install Azure CLI.

```bash { target="ubuntu:latest" }
pip install azure-cli
```

The pip install updates $HOME/.profile with the path the `az` executable.

```bash { target="ubuntu:latest" }
source $HOME/.profile
```

Confirm the executable is available.

```bash { target="ubuntu:latest" }
az version
```

Visit the [Azure CLI documentation](https://learn.microsoft.com/en-us/cli/azure/) for more information. 
