---
title: "Learn how to use Docker" 

description: >
    Learn how to use Docker for single and multi-architecture use.

minutes_to_complete: 20

who_is_this_for: >
     Learning path for single and multi-architecture Docker commands.

learning_objectives:
    -  Run Docker build to build and run a container image on any computer supporting Docker
    -  Use Docker buildx for multi-architecture image builds
    -  Install binfmt on Linux to add multi-architecture support for buildx
    -  Perform a remote docker build on an Arm server
    -  Utilize Docker manifest for multi-architecture builds


## Tags. No whitespace. An underscore will be visually replaced with whitespace.
skilllevels: Introductory
armips:
    - Neoverse	
tools:
    - Docker
softwares:
operatingsystems:
    - Linux
subjects:
    - Containers and Virtualization
developerprograms:
    - 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---
- Docker is installed on the machines being used. For information about the installation refer to [Installing Docker](/install-tools/docker)

