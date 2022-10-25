---
# ================================================================================
#       Edit
# ================================================================================

title: "Get Started with the Arm Virtual Hardware Raspberry Pi 4" 
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Introduction to the virtual Raspberry Pi 4 in Arm Virtual Hardware
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 90
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Learning path for software developers interested in using the Raspberry Pi 4 available on Arm Virtual Hardware.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Compare and contrast a physical Raspbery Pi 4 with the virtual Raspberry Pi in AVH
    - Build and run multiple software examples on the virtual Raspberry Pi 
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Some familiarity with embedded Linux is assumed
    - Experience with single board computers, such as Raspberry Pi 
# List any prereqs needed before this learning path can be completed. Can include:
    # Online service accounts                                   (An Amazon Web Services account)
    # Prior knowledge                                           (Some familiarity with embedded programing)
    # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
    # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)

##### Tags
# Don't enter whitespace. An underscore will be visually replaced with whitespace.

skilllevels: Introductory
# Options:
    # Getting-Started   (for a basic overview of certain tools/softwares/topics)
    # Introductory      (the next stage up from getting started)
    # Experienced       (for topics that require a fair amount of background knowledge in tools/softwares/topics to complete)

armips:
    # Groups of IP      (Cortex-M, Cortex-A, Cortex-R, Neoverse, GPU, System IP, etc.)
    # or Specific IP    (Cortex-M7, Neoverse-N1, AHB_Cache, etc.)
    - Cortex-A

tools:
    # Environments      (AWS_EC2)
    # Toolchains        (GCC, Arm_Compiler_for_Embedded)
    # IDEs              (Arm Development Studio, VS_Code)
    # Online tools      (GitHub, Jenkins)
    # General tools     (cbuild)
    - Arm_Virtual_Hardware


softwares:
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - TensorFlow
    - Docker

operatingsystems:
    # OSes              (Linux, Windows, macOS, FreeRTOS, Bare-metal)
    - Linux

subjects:
    # Unique list per main topic. Select from existing list.
    - 

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
