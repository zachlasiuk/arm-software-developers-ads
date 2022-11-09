---
# ================================================================================
#       Edit
# ================================================================================

title: "Build an RTOS in N easy steps"
# Should start with a verb (learn, build, etc.), have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Learn how to use CMSIS-RTOS and other CMSIS features to build an RTOS application using Keil-RTX
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 30
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Embedded software developers new to CMSIS or RTOS development
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Learn how to implement a basic RTOS-based application
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Keil MDK or Arm Development Studio is required (MDK recommended)

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
    - Cortex-M
   

tools:
    # Environments      (AWS_EC2)
    # Toolchains        (GCC, Arm_Compiler_for_Embedded)
    # IDEs              (Arm Development Studio, VS_Code)
    # Online tools      (GitHub, Jenkins)
    # General tools     (cbuild)
    - Keil_MDK
    - Arm_Development_Studio

softwares:
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - C

operatingsystems:
    # OSes              (Linux, Windows, macOS, FreeRTOS, Bare-metal)
    - RTX

subjects:
    # Unique list per main topic. Select from existing list.
    # - RTOS

developerprograms:
    # - Add your tag here

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================


# Prerequisites
#   - Place in a list in the content section, directly below the front-matter. 
#   - Add key links to prereqs such as a link to [AWS EC2](https://aws.amazon.com/ec2/) or a [learning path](/learning-paths/cloud/providers).
#   - List any prereqs needed before this learning path can be completed. Can include:
        # Online service accounts                                   (An Amazon Web Services account)
        # Prior knowledge                                           (Some familiarity with embedded programing)
        # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
        # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)
---
[CMSIS](https://www.keil.com/pack/doc/CMSIS/General/html/index.html), is an open standard that enables platform vendors to provide all the necessary set up required for their platform. These are also integrated with other vendor tools, such as [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) or [MCUXpresso](https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-integrated-development-environment-ide:MCUXpresso-IDE).

In this learning path, we will use one of the supplied Fixed Virtual Platforms with Keil MDK (or Arm Development Studio).

The instructions are written for [Keil MDK](/install-tools/mdk), however the same steps can also be done with [Arm Development Studio](/install-tools/armds).

