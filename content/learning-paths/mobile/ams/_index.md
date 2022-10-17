---
# ================================================================================
#       Edit
# ================================================================================

title: "Get started with Arm Mobile Studio"
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Get started with the various components of Arm Mobile Studio.
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 60
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Android application and games developers new to Arm Mobile Studio.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Learn the basic features of each component of Arm Mobile Studio.
    - Get started profiling and optimizing your application.
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
# List any prereqs needed before this learning path can be completed. Can include:
    # Online service accounts                                   (An Amazon Web Services account)
    # Prior knowledge                                           (Some familiarity with embedded programing)
    # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
    # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)


##### Tags
# Don't enter whitespace. An underscore will be visually replaced with whitespace.

skilllevels: Getting-Started
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
    - Arm_Mobile_Studio

softwares:
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - C++
    - Java

operatingsystems:
    # OSes              (Linux, Windows, macOS, FreeRTOS, Bare-metal)
    - Android

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
- [These devices](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Supported-Devices) have been tested internally within Arm, and confirmed to work with Arm Mobile Studio.

- Download and install Arm Mobile Studio from [Product Download Hub](https://developer.arm.com/downloads/view/MOBST-PRO0). It is supported on Windows, Linux, and macOS host platforms.

- Download and install [Android SDK Platform tools](https://developer.android.com/studio/releases/platform-tools.html). Required for [Android Debug bridge (adb)](https://developer.android.com/studio/command-line/adb).
