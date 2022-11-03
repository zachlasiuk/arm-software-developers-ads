---
# ================================================================================
#       Edit
# ================================================================================

title: "Fully integrate Arm Virtual Hardware into CI/CD workflow"
# Should start with a verb (learn, build, etc.), have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: >
    Learn to integrate your Arm Virtual Hardware instances on AWS into a GitHub CI/CD development flow.
# One sentance, is a quick summary of this learning path, viewable when searching through all learning paths. 

minutes_to_complete: 20   
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

who_is_this_for: >
    Embedded and DevOps engineers new to Arm Virtual Hardware and/or AWS.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Prepare AWS account for GitHub integration
    - Integrate Arm Virtual Hardware into CI/CD flow with GitHub Actions
# 2-5 bullet points, one sentance each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Some familiarity with CI/CD concepts is assumed
    - Valid AWS and GitHub accounts are required
# List any prereqs needed before this learning path can be completed. Can include:
    # Online service accounts                                   (An Amazon Web Services account)
    # Prior knowledge                                           (Some familiarity with embedded programing)
    # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
    # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)





##### Tags
skilllevels: Introductory
subjects: NONE
armips:
    - Cortex-M
tools:
    - Arm Virtual Hardware
    - GitHub
    - AWS EC2 
softwares:
    - yml
operatingsystems:


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

- This learning path builds on concepts introduced [here](../avh_cicd/).
