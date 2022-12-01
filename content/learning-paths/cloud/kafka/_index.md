---
title: Installing Kafka, Zookeeper, and setting up a 3 node Kafka Cluster

description: Learn how to setup a 3 node Kafka cluster, configure Zookeeper, and test write/read events into the cluster

minutes_to_complete: 10

who_is_this_for: A guide for software developers interested in learning how to use Kafka and Zookeeper to setup a 3 node Kafka cluster.

learning_objectives:
    - Install Zookeeper and Kafka
    - Configure Zookeeper to work with Kafka
    - Test write/read events into the Kafka cluster

prerequisites:
    - 7 Physical machines or 7 cloud instances with Ubuntu/Debian installed. We need 3 Kafka nodes, 3 Zookeeper nodes, and 1 client node.

author_primary: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Libraries
armips:
    - Neoverse
tools:
softwares:
    - Kafka
    - Zookeeper
operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
