---
# User change
title: "Download and run Geekbench"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
When creating a cloud instance, users may struggle to select an appropriate configuration for their workloads. Simple benchmarking runs on different configurations is a good idea to help you decide.

[Geekbench](https://www.geekbench.com/index.html) is a cross-platform benchmark that easily measures your system's performance. Preview builds for Arm were provided in [Geekbench 5.4](https://www.geekbench.com/blog/2021/03/geekbench-54/). Newer versions may be available, check the Geekbench [downloads](https://www.geekbench.com/download/) section for latest information.

It provides an overall score (for both single and multi-core configuration), as well as individual performance scores for specific tests, which can easily be compared against other configurations (higher is better).

Additional features are available with a purchased [license](https://www.primatelabs.com/store/).

## Pre-requisites

You will need a local Arm platform or an [Arm based instance](/learning-paths/cloud/providers/) from your cloud service providers, running an appropriate operating system (at time of writing, `Ubuntu 16.04 LTS` or later).

## Fetch pre-built binaries
The binaries are available to download from the Geekbench website directly. Check the website for the latest link. The below is for the 5.4 preview build.

Once downloaded `untar` the archive, and navigate into its directory:
```console
wget https://cdn.geekbench.com/Geekbench-5.4.0-LinuxARMPreview.tar.gz
tar -xf Geekbench-5.4.0-LinuxARMPreview.tar.gz
cd Geekbench-5.4.0-LinuxARMPreview
```
## Run benchmark
Run the `geekbench5` benchmark.
```console
./geekbench5
```
It will run a number of single-core and multi-core tests. When complete, it will upload your results to the [Geekbench browser](https://browser.geekbench.com) and provide a link to the specific results for your platform.

You can browse other platform scores, or repeat your test with other cloud configurations to see how they compare. We also encourage you to compare against servers build with other architectures.

Please also see any of the [application specific examples](/learning-paths/cloud/) we have prepared.

## Other resources

| Type          | Content             |
| ---           | ---                 |
| Blog          | [Performance Analysis for Arm vs x86 CPUs in the Cloud](https://www.infoq.com/articles/arm-vs-x86-cloud-performance/) |
| Blog          | [GCP, AWS, and Azure ARM-based server performance comparison](https://apisix.apache.org/blog/2022/08/12/arm-performance-google-aws-azure-with-apisix/) |
