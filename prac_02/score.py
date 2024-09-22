"""
Practical 2 - Refactoring
Scores
"""

import random

MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Display evaluations for input score and random score."""
    score = float(input("Enter score: "))
    print(determine_evaluation(score))
    print(determine_evaluation(random.randint(MINIMUM_THRESHOLD, MAXIMUM_THRESHOLD)))


def determine_evaluation(score):
    """Determine evaluation for score."""
    if score < MINIMUM_THRESHOLD or score > MAXIMUM_THRESHOLD:
        return "Invalid score"
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    if score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


main()
