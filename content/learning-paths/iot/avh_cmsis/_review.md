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
            Can I run and build CMSIS-DSP Tests for F16 data type?
        answers:
            - "Yes"
            - "No"
        correct_answer: 0                     
        explination: >
            Yes tests for F16 data type are included in the CMSIS DSP Test suite.

    - questions:
        question: >
            A post-processing script is included to transform the raw output from the tests into human readable output.
        answers:
            - "Yes"
            - "No"
        correct_answer: 0                     
        explination: >
            Yes. Use the post-processing script to understand the results.
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
