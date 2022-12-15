---
# ================================================================================
#       Edit
# ================================================================================

title: "AXI-Lite and GPIOs" 
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Design and implement AXI-Lite peripheral to control General Purpose Input and Output Ports (GPIOs). 

# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 60
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Learning path for software developers interested in System on Chip Design.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing System.
	- Modify a C code to program the Cortex-A9 processor so that it reads the state of switches and control the LEDs.
	- Demonstrate a functional simple system that lights up the LEDs based on the status of the switches.  
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Some familiarity with Verilog
    - Basic understanding of System on Chip
    - Have a 'Zybo Z7-10' development board 
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

subjects: NONE

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
    - Xilinx Vivado
    - Xilinx Vitis


softwares:
    # Languages         (Python, Go, MongoDB, Assembly, Java)
    - Verilog

operatingsystems:
    # OSes              (Linux, Windows, macOS, FreeRTOS, Bare-metal)
    - Windows


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---