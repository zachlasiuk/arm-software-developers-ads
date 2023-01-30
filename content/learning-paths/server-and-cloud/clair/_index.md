---
title: Generate the vulnerability report using Clair on Arm

description: Learn how to run Clair in the combined and the distributed mode, submit the containers to Clair and generate the Vulnerability report that can affect the content.

minutes_to_complete: 60

who_is_this_for: Developers looking to check the vulnerabilities that can affect their containers.

learning_objectives:
    - Install and run Clair in both "combined" and "distributed" mode.
    - Submit the containers to Clair using clairctl and generate the vulnerability report.

prerequisites:
    - Cloud node or a physical machine.
    - docker and docker-compose (latest version preferred).
    - go (latest version preferred).

author_primary: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Web
armips:
    - Neoverse
tools:
    - docker and docker-compose
    - go
softwares:
operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
