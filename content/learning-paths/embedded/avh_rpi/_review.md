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
            Arm Virtual Hardware provides a virtual Raspberry Pi which is similar, but slower than a real Raspberry Pi.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explination: >
            The AVH Raspberry Pi is similar, but faster than the physical Raspberry Pi. 


    - questions:
        question: >
            The Arm Virtual Hardware Raspberry Pi supports Bluetooth connections with other devices in AVH
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explination: >
            It is possible to use Bluetooth to connect to other devices in AVH

    - questions:
        question: >
            Raspberry Pi OS is the only Linux distribution which can be run on the virtual Raspberry Pi in AVH
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explination: >
            Other operating systems, such as Ubuntu, can be installed. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
