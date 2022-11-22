---
title: "Terraform"

additional_search_terms:

# Maintenance settings
test_maintenance: true          # Enables maintenance tests on article
test_images:                    # List Docker images to run instructions on
  - ubuntu:latest

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---

[Terraform](https://www.terraform.io/) automates cloud infrastructure. It is an infrastructure as code tool. 

Terraform is available for Windows, macOS, Linux and supports the Arm architecture. 

## Introduction

[General installation information](https://developer.hashicorp.com/terraform/downloads) is available which covers all supported operating systems. 

In some cases the instructions don't work well for Arm platforms. 

This article provides a quick solution to install Terraform for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The result should be `aarch64` 

## Download and Install

The easiest way to install Terraform for Ubuntu on Arm is to use the zip file and copy the executable. 

The installation options with the Ubuntu package manager don't work well, but feel free to try them as they may improve. 

Make sure unzip is available. If not, install it. 

```bash { target="ubuntu:latest" }
sudo apt install unzip
```

Download and install the latest version. There is just 1 executable to copy to the desired location.

```bash { target="ubuntu:latest" }
TER_VER=`curl -s https://api.github.com/repos/hashicorp/terraform/releases/latest | grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`
wget https://releases.hashicorp.com/terraform/${TER_VER}/terraform_${TER_VER}_linux_arm64.zip
unzip terraform_${TER_VER}_linux_arm64.zip
sudo cp terraform /usr/local/bin/
```

Confirm the executable is available.

```bash { target="ubuntu:latest" }
terraform version
```

Visit the [Terraform documentation](https://developer.hashicorp.com/terraform/docs) for more information. 
