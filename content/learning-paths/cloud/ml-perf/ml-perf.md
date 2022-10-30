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

We use the MLPerf Inference benchmark suite from MLCommons to benchmark models for a widely used ML use-case such as Image classification and Object detection. 
Start by cloning the repository below.

```console
git clone --recurse-submodules https://github.com/mlcommons/inference.git mlperf_inference
```

## Build and Install the MLPerf Inference Benchmark

Next, build and install the MLPerf Inference Benchmark for the image classification and object detection use case using the steps below.

```console
cd mlperf_inference/loadgen/
CFLAGS="-std=c++14" sudo python3 setup.py develop --user
cd ../vision/classification_and_detection/
sudo python3 setup.py develop
```

## Install Tensorflow

MLPerf Inference Benchmark suite can use different backends such as onnx or tensorflow. We will install Tensorflow as the backend. Install tensorflow using the commands below.

```console
pip install tensorflow
pip install tensorflow-io
```
We set 2 environment variables:
* Enable oneDNN, an open-source cross-platform performance library for deep learning applications
* Use 16-bit floating-point storage format (BF16) to accelerate performance

```console
export TF_ENABLE_ONEDNN_OPTS=1
export ONEDNN_DEFAULT_FPMATH_MODE=BF16
```
AWS Graviton3 instances are the first instances with BF16 support.

## Download the ML Model 

Next, download the ML model you want to run the benchmark with. In this example, we download the resnet50-v1.5 model.

```console
wget -q https://zenodo.org/record/2535873/files/resnet50_v1.pb
```

## Download the dataset 

You will also need to download a dataset for the ML model you want to benchmark. The imagenet2012 validation dataset is best used with this ML model. You can download the dataset after you register on the site [here](http://image-net.org/challenges/LSVRC/2012/)

For this example, we will generate a fake image dataset using the tooling included in the repo. Use the command below

```console
tools/make_fake_imagenet.sh
```

## Setup Environment Variables

Finally, before you run the benchmark you will need to setup the environment variables below to point to the location of the ML model and dataset.

```console
export MODEL_DIR=`pwd`
export DATA_DIR=`pwd`/fake_imagenet
```

## Now run the benchmark on your Arm machine

You can now launch the benchmark on your Arm machine, using the command below. 

```console
./run_local.sh tf resnet50 cpu
```

This command runs the benchmark with the "tf" tensorflow backend on the "resnet50" ML model with the device set to "cpu".

The minimal arguments that you need to pass to the benchmark are shown below

```
./run_local.sh backend model device

backend is one of [tf|onnxruntime|pytorch|tflite]
model is one of [resnet50|mobilenet|ssd-mobilenet|ssd-resnet34]
device is one of [cpu|gpu]
```

For all other options, run help as shown below

```console
./run_local.sh --help
```

## View Results

At the end of the benchmark run, the aggregated ML performance results are printed on the console. For example, using the command above, the output will be similar to:
```
INFO:main:starting TestScenario.SingleStream
TestScenario.SingleStream qps=13.88, mean=0.0719, time=600.153, queries=8333, tiles=50.0:0.0718,80.0:0.0731,90.0:0.0738,95.0:0.0743,99.0:0.0755,99.9:0.0771

```
Detailed results with breakdowns are available in the `output/tf-cpu/resnet50` folder. The folder name is dependent on the arguments passed to the benchmark script.

