"""Practical 4 - "Quick Pick" Lottery Ticket Generator"""

import random

NUMBER_OF_RANDOM_NUMBERS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
quick_pick = []
number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    for j in range(NUMBER_OF_RANDOM_NUMBERS):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    quick_pick = [f"{number:2}" for number in quick_pick]
    print(" ".join(sorted(quick_pick)))
    quick_pick = []
