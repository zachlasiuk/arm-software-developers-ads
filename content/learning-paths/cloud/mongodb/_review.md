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
            Does MongoDB run on Arm servers?
        answers:
            - "Yes"
            - "No"
        correct_answer: 0                     
        explination: >
            MongoDB is fully supported on 64-bit Arm servers running Linux.

    - questions:
        question: >
            Can you test MongoDB performance by running multiple threads executing different operation types?
        answers:
            - "Yes"
            - "No"
        correct_answer: 0                     
        explination: >
            You can run multiple threads executing either all the same or different database operations.
               
    - questions:
        question: >
            What software is required to run YCSB?
        answers:
            - "None"
            - "Arm Assembly"
            - "Go"
            - "Java"
        correct_answer: 3                     
        explination: >
            You will need Java 1.8 or newer installed, which can be done with one bash command.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
