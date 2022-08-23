---
############################################
# Editable
############################################

##### High-level info
title: "Learn about MongoDB on Arm servers"
description: >
    Learn how to install and run MongoDB Community Edition on differet flavors of AWS EC2 instances powered by Arm64 achitecture.

##### Introduction to learning path
minutes_to_complete: 20   # Always measured in minutes. Should be an integer, to complete the learning path (not just read it)

who_is_this_for: >
    Learning path for software developers using MongoDB as their database for mobile, IoT applications, content management or real-time analytics running on Arm servers.

learning_objectives: # Should start with a verb, describe value
    - Install and run MongoDB on your 64-bit Arm AWS EC2 instance
    - Test MongoDB performance on your 64-bit Arm AWS EC2 instance using open-source tooling
    - Measure and compare the performance of MongoDB on Arm versus other architectures with Yahoo Cloud Serving Benchmark (YCSB)
    
prerequisites:
    - An Amazon Web Services(AWS) account.
    - Some familiarity with launching and running EC2 instances in AWS is helpful but not necessary.






##### Tags
# No whitespace. An underscore will be visually replaced with whitespace.
skilllevel: Introductory
armips:
    - Neoverse
tools:
    - AWS_EC2
    - cbuild
    - GCC
    - Snort
softwares:
    - Linux
    - MongoDB



############################################
# FIXED, do not modify
############################################
weight: 1                   # _index.md always has weight of 1
learning_path_main_page: "yes"             # indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
layout: "learningpathall"   # All files under learning paths have this same wrapper
---