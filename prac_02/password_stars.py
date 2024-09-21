"""
Practical 2 - Refactoring
Password Check with Functions
"""


def main():
    """Print a line of asterisks based on password length."""
    minimum_length = int(input("Password minimum length: "))
    password = get_password("Password: ", minimum_length)
    print_star_line(password)


def get_password(prompt, minimum_length):
    """Get a valid password of at least minimum length."""
    password = input(prompt)
    while len(password) < minimum_length:
        print(f"Password needs to be at least {minimum_length} characters long")
        password = input(prompt)
    return password


def print_star_line(sequence):
    """Print as many asterisks as sequence items."""
    print("*" * len(sequence))


main()
