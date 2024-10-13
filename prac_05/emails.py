"""
Emails
Estimate: 80 minutes
Actual:   65 minutes
"""


def main():
    """Display names and emails based on user input with dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirmation not in "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Get name based on email."""
    name = " ".join((name_part.title() for name_part in
                     email[:email.find("@")].split(".")))
    return name


main()
