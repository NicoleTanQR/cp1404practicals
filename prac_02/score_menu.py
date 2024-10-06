"""Practical 2 - Menu"""

MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Display evaluation or a number of asterisks based on a valid input score."""
    score = get_valid_score("Enter score: ")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter score: ")
        elif choice == "P":
            print(determine_evaluation(score))
        elif choice == "S":
            print_star_line(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score(prompt):
    """Get a valid score."""
    score = float(input(prompt))
    while score < MINIMUM_THRESHOLD or score > MAXIMUM_THRESHOLD:
        print("Invalid score")
        score = float(input(prompt))
    return score


def determine_evaluation(score):
    """Determine evaluation for score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    if score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


def print_star_line(score):
    """Print as many asterisks as score."""
    print("*" * int(score))


main()
