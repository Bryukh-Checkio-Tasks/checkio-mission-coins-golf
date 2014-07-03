"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [9, 2, 2, 1],
            "answer": 6,
        },
        {
            "input": [1, 1, 1, 1],
            "answer": 5,
        },
        {
            "input": [1, 2, 3, 4, 5],
            "answer": 16,
        },
    ],
    "Edge": [
        {
            "input": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "answer": 11,
        },

        {
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "answer": 46,
        },

        {
            "input": [9, 8, 7, 6, 5, 4, 3, 2, 1],
            "answer": 46,
        },
        {
            "input": [6, 8, 9, 5, 9, 5, 7, 1, 2, 3],
            "answer": 56,
        },
        {
            "input": [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            "answer": 1,
        },
        {
            "input": [1],
            "answer": 2,
        },
    ],
    "Extra": [
        {
            "input": [2, 1, 3, 8],
            "answer": 7,
        },
        {
            "input": [1, 2, 7],
            "answer": 4,
        },
        {
            "input": [8, 6, 2, 1, 8, 9],
            "answer": 4,
        },
        {
            "input": [1, 6, 4, 7, 1, 2, 1],
            "answer": 23,
        },

        {
            "input": [8, 1, 1, 4, 4, 2, 1, 5, 4, 6],
            "answer": 37,
        },
        {
            "input": [4, 7, 1, 2, 6, 3],
            "answer": 24,
        },

        {
            "input": [9, 6, 4, 8, 1, 3, 1],
            "answer": 33,
        },

        {
            "input": [4, 9, 5, 1, 8, 2, 7, 2, 6, 4],
            "answer": 49,
        },
    ]
}
