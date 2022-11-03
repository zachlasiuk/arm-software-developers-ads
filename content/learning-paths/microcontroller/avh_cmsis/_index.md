---
# ================================================================================
#       Edit
# ================================================================================

title: "Learn how to build and run CMSIS-DSP tests on AVH Corstone-300"
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Build CMSIS-DSP tests and run on Arm Virtual Hardware.
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 15
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Learning path for embedded software developers new to CMSIS-DSP.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Build CMSIS-DSP tests for the Corstone-300 AVH FVP
    - Run CMSIS-DSP tests on the Corstone-300 AVH FVP
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.


##### Tags
# Don't enter whitespace. An underscore will be visually replaced with whitespace.

skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-M
tools:
    - Arm Virtual Hardware
    - AWS EC2
softwares:
    - C
operatingsystems:
    - Bare-metal

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---
- Some familiarity with embedded programing is assumed
