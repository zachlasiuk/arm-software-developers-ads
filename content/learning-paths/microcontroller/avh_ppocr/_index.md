---
# ================================================================================
#       Edit
# ================================================================================

title: "Deploy PaddlePaddle on Arm Cortex-M with Arm Virtual Hardware"
# Should start with a verb (learn, build, etc.), have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Learn how to deploy a PP-OCRv3 English text recognition model on Arm Cortex-M55 processor with Arm Virtual Hardware.
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 30
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Learning path for developers in embedded industries using PaddlePaddle for Arm Cortex-M processor use-case.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Train an English text recognition model with PaddleOCR
    - Export Paddle inference model
    - Compile Paddle inference model with TVMC
    - Deploy on the AVH Corstone-300 platform with Arm Cortex-M55
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Some familiarity with embedded programing is assumed
    - Some familiarity with AI/ML software development is assumed
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
    - An EC2 instance with AVH installed
    - GCC
    - TVM
    - PaddleOCR

softwares:
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - C
    - Python

operatingsystems:
    # OSes              (Linux, Windows, macOS, FreeRTOS, Bare-metal)
    - Bare-metal

subjects:
    # Unique list per main topic. Select from existing list.
    

developerprograms:
    - None

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
- An AWS account to subscribe [Arm Virtual Hardware](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g) Amazon Machine Image(AMI). Refer to [this guide](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) to create an AWS account.

