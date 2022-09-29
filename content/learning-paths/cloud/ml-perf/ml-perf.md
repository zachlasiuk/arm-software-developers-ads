---
# User change
title: "Measure ML Inference Performance on Arm servers"

weight: 2

layout: "learningpathall"
 

---


## Pre-requisites

* An [Arm based instance](/learning-paths//cloud/providers) from an appropriate cloud service provider running `Ubuntu Linux 20.04`.

This learning path has been tested on AWS and Oracle platforms.


## Install necessary software and packages required by MLPerf Inference Suite

Launch an Arm-based instance running `Ubuntu 20.04`.

Install build-essential and Python3 package dependencies

```console
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install python3-pip
sudo pip install opencv-python-headless
sudo pip install Cython
sudo pip install pycotools
sudo pip install pybind11
```
## Clone the MLPerf Inference Benchmarks Repo for Image Classification and Object Detection

```console
git clone --recurse-submodules https://github.com/mlcommons/inference.git mlperf_inference
```

## Build and Install the MLPerf Inference Benchmark

```console
cd mlperf_inference/loadgen/
CFLAGS="-std=c++14" sudo python3 setup.py develop --user
cd ../vision/classification_and_detection/
sudo python3 setup.py develop
```

## Install Tensorflow

MLPerf Inference Benchmark suite can use different backends. We will install Tensorflow as the backend

```console
pip install tensorflow
pip install tensorflow-io
```

## Download the ML Model to run the benchmark with

```console
wget -q https://zenodo.org/record/2535873/files/resnet50_v1.pb
```

## Download the dataset for the model you want to benchmark

```console
tools/make_fake_imagenet.sh
```

## Setup Environment Variables to point to the ML Model and the Dataset

```console
export MODEL_DIR=`pwd`
export DATA_DIR=`pwd`/fake_imagenet
```

## Now run the benchmark on your Arm machine

```console
./run_local.sh tf resnet50 cpu
```

## View Results

At the end of the benchmark run, the aggrerated ML performance results are printed on the console. For example, using the command above, the output will be similar to:
```
INFO:main:starting TestScenario.SingleStream
TestScenario.SingleStream qps=13.88, mean=0.0719, time=600.153, queries=8333, tiles=50.0:0.0718,80.0:0.0731,90.0:0.0738,95.0:0.0743,99.0:0.0755,99.9:0.0771

```
Detailed results with breakdowns are available in the `output/tf-cpu/resnet50` folder. The folder name is dependent on the arguments passed to the benchmark script.

