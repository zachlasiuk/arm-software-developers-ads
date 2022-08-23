---
# ================================================================================
#       Edit
# ================================================================================

title: "Learn about MongoDB on Arm servers"
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Learn how to install and run MongoDB Community Edition on differet flavors of AWS EC2 instances powered by Arm64 achitecture.
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 20   
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Learning path for software developers using MongoDB as their database for mobile, IoT applications, content management or real-time analytics running on Arm servers.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Install and run MongoDB on your 64-bit Arm AWS EC2 instance
    - Test MongoDB performance on your 64-bit Arm AWS EC2 instance using open-source tooling
    - Measure and compare the performance of MongoDB on Arm versus other architectures with Yahoo Cloud Serving Benchmark (YCSB)
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - An Amazon Web Services(AWS) account.
    - Some familiarity with launching and running EC2 instances in AWS is helpful but not necessary.
# List any prereqs needed before this learning path can be completed. Can include:
    # Online service accounts                                   (An Amazon Web Services account)
    # Prior knowledge                                           (Some familiarity with embedded programing)
    # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
    # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)





##### Tags
# Don't enter whitespace. An underscore will be visually replaced with whitespace.

skilllevel: Introductory
# Options:
    # Getting-Started   (for a basic overview of certain tools/softwares/topics)
    # Introductory      (the next stage up from getting started)
    # Advanced          (for topics that require a fair amount of background knowledge in tools/softwares/topics to complete)

armips:
    # Groups of IP      (Cortex-M, Cortex-A, Neoverse, System IP)
    # or Specific IP    (Cortex-M7, Neoverse-N1, AHB_Cache)
    - Neoverse

tools:
    # Environments      (AWS_EC2)
    # Toolchains        (GCC, Arm_Compiler_for_Embedded)
    # IDEs              (Arm Development Studio, VS_Code)
    # Online tools      (GitHub, Jenkins)
    # General tools     (cbuild)
    - AWS_EC2
    - cbuild
    - GCC
    - Snort

softwares:
    # OSes              (Linux, Windows, Mac, FreeRTOS, Bare-metal)
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - Linux
    - MongoDB



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---