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
            Arm Compiler for Embedded can be used to build the ML Evaluation Kit
        answers:
            - "True"
            - "False"
        correct_answer: 0
        explination: >
            True. Use "--toolchain arm" when building the application(s).

    - questions:
        question: >
            Which option is used put the Virtual Hardware into a "fast" mode?
        answers:
            - "-C mps3_board.visualisation.disable-visualisation=1"
            - "--fastmode"
            - "-C ethosu.extra_args=\"--fast\""
        correct_answer: 2
        explination: >
            When used in this mode, the execution performance is improved, but any timing information output should be ignored.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
