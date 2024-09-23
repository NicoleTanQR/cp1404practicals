"""
Practical 2 - Refactoring
Password Check with Functions
"""

MINIMUM_LENGTH = 7


def main():
    """Print a line of asterisks based on password length."""
    password = get_password("Password: ")
    print_star_line(password)


def get_password(prompt):
    """Get a valid password of at least minimum length."""
    password = input(prompt)
    while len(password) < MINIMUM_LENGTH:
        print(f"Password needs to be at least {MINIMUM_LENGTH} characters long")
        password = input(prompt)
    return password


def print_star_line(sequence):
    """Print as many asterisks as sequence items."""
    print("*" * len(sequence))


main()
