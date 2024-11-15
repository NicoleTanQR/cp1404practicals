"""More Guitars! - Program to use the class"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
INDEX_NAME = 0
INDEX_YEAR = 1
INDEX_COST = 2


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = load_guitars(FILENAME)
    display_guitar_details(guitars)
    get_new_guitars(guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from filename."""
    guitars = []
    in_file = open(filename)
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[INDEX_NAME]
        year = int(parts[INDEX_YEAR])
        cost = float(parts[INDEX_COST])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


def display_guitar_details(guitars):
    """Display guitar details stored."""
    guitars.sort()
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    """Get new guitars from user input."""
    name = input("Any new guitars?\nName: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Overwrite file contents with updated guitars."""
    out_file = open(filename, 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
