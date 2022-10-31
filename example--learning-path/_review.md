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
            Enter your first question here?
        answers:
            - "Answer choice 0"
            - "Answer choice 1"
        correct_answer: 0                     
        explination: >
            Enter a brief explanation for the right answer.

    - questions:
        question: >
            Enter your second question here?
        answers:
            - "Answer choice 0"
            - "Answer choice 1"
        correct_answer: 1                     
        explination: >
            Enter a brief explanation for the right answer.
               
    - questions:
        question: >
            Enter your third question here?
        answers:
            - "Answer choice 0"
            - "Answer choice 1"
            - "Answer choice 2"
            - "Answer choice 3"
        correct_answer: 3                     
        explination: >
            Enter a brief explanation for the right answer.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
