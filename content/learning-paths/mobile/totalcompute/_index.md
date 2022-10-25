---
# ================================================================================
#       Edit
# ================================================================================

title: "Get started with Arm Total Compute"
# Should start with a verb (learn, build, etc.), have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Get started with the reference software stack for Arm Total Compute.
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 60  
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Firmware developers for mobile devices new to Arm Total Compute.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Build the reference software stack
    - Run the stack on the FVP
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
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
    - GPU
   

tools:
    # Environments      (AWS_EC2)
    # Toolchains        (GCC, Arm_Compiler_for_Embedded)
    # IDEs              (Arm Development Studio, VS_Code)
    # Online tools      (GitHub, Jenkins)
    # General tools     (cbuild)
    - GCC

softwares:
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - Add your tag

operatingsystems:
    # OSes              (Linux, Windows, macOS, FreeRTOS, Bare-metal)
    - Linux
    - Android

subjects:
    # Unique list per main topic. Select from existing list.
    - Databases
    - Web Back-end

developerprograms:
    - Add your tag here

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
- There are a number of pre-requisites for the build machine used. See the documentation for the software version being built:
  - [TC0](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc0/user-guide.rst)
  - [TC1](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc1/user-guide.rst)
  - [TC2](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/totalcompute/tc2/user-guide.rst)
