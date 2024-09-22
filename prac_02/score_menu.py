"""
Practical 2 - Menu
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Display evaluation or a number of asterisks based on a valid input score."""
    pass
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


main()
