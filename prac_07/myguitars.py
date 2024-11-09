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


main()
