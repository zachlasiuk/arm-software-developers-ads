---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentance question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explination:      A short (1-3 sentance) explination of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            Do I need to create AWS EC2 instance with Graviton processors to build a Docker image for Arm?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                     
        explination: >
            That's right! AWS CodeBuild will create all of the needed infrastructure automatically.

    - questions:
        question: >
            Do Docker images created on AWS CodeBuild need to be run in AWS?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                     
        explination: >
            That's right! You can run Docker images created in AWS CodeBuild on any Arm machine with Docker installed.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
