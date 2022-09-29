---
title: "Anaconda"

additional_search_terms:
  - Python
  - TensorFlow
  - Pytorch

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---

[Anaconda Distribution](https://www.anaconda.com/products/distribution) is a popular open-source Python distribution. 

It includes access to a repository with over 8,000 open-source data science and machine learning packages.

The conda command can be used to quickly install and use Python packages. 

## Introduction

Follow the instructions below to install and use Anaconda Distribution on an Arm server.

Confirm you are using an Arm machine by running:

```console
uname -m
```

The output should be:

```console
aarch64
```

The installer requires some desktop related libraries. The dependencies can be met by installing a desktop environment. 

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/Debian" >}}
sudo apt install xfce4 -y
  {{< /tab >}}
  {{< tab header="Amazon Linux" >}}
sudo amazon-linux-extras install mate-desktop1.x
  {{< /tab >}}
{{< /tabpane >}}

## Download 

Download the latest Anaconda Distribution.

```console
wget -O - https://www.anaconda.com/distribution/ 2>/dev/null | sed -ne 's@.*\(https:\/\/repo\.anaconda\.com\/archive\/Anaconda3-.*-Linux-aarch64\.sh\)\">64-Bit (AWS Graviton2 / ARM64) Installer.*@\1@p' | xargs wget
```

Depending on the latest version, the download will be of the form **Anaconda3-202X.0X-Linux-x86_64.sh** where the X values represent the year and month of the latest release.

## Installation {#install}

Run the downloaded install script. It will review the license agreement and ask to accept the terms. 

The default installation directory is $HOME/anconda3. Change the installation directory as needed.

```console
sh ./Anaconda3-2022.05-Linux-aarch64.sh
```

The install will take a couple of minutes to complete.

Near the end of the installer, answer yes to the question below to add the Anaconda setup to .bashrc

```console
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>> yes
```

To complete the installation source the .bashrc which was updated by the installer.

```console
. ~/.bashrc
```

## Setting up product license {#license}

Anaconda Distribution is open source and freely available for use. No licenses need to be set up for use.

## Get started {#start}

Test Anaconda Distribution by running simple TensorFlow and Pytorch examples.

### TensorFlow

Create a new conda environment named tf, install TensorFlow, and activate the new environment.

```console
conda create -n tf tensorflow -y
```

Activate the environment.

```console
conda activate tf
```

The shell prompt will now show the tf environment.

```console
(tf) ubuntu@ip-10-0-0-251:~$
```

Run a simple check to make sure TensorFlow is working.

```console
python
```

Enter the four commmands below shown at the right of the Python prompt, **\>\>\>**

```console
Python 3.7.13 (default, Mar 28 2022, 12:46:38)
[GCC 10.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> print(tf.__version__)
2.9.1
>>> print(tf.reduce_sum(tf.random.normal([1000,1000])))
tf.Tensor(-545.09094, shape=(), dtype=float32)
>>> exit()
```

### Pytorch

Create a new conda environment named torch, install PyTorch, and activate the new environment.

```console
conda create -n torch pytorch -y
```

```console
conda activate torch
```

Run a simple check to make sure TensorFlow is working.
```console
python
```

Enter the four commmands below shown at the right of the Python prompt, **\>\>\>**

```console
Python 3.10.4 (main, Mar 31 2022, 08:35:17) [GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> x = torch.rand(5,3)
>>> print(x)
tensor([[0.1940, 0.9709, 0.6611],
        [0.8440, 0.1421, 0.3442],
        [0.7958, 0.6730, 0.1843],
        [0.9762, 0.6765, 0.6456],
        [0.6913, 0.4201, 0.4174]])
>>> exit()
```

There are many machine learning articles and examples using TensorFlow and Pytorch on Arm servers.

