"""
Guitars! - Playing the Guitars
Estimated work duration: 30 min
Current time: 4 p.m.
Actual work duration: ~2 hours
"""

from prac_06.guitar import Guitar


def main():
    """Store and display guitar details."""
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.sort()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        name_width = max((len(guitar.name) for guitar in guitars))
        cost_width = max(
            (len(str(format(guitar.cost, ",.2f"))) for guitar in guitars))
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}:  {guitar.name:>{name_width}} ({guitar.year}), "
              f"worth $ {guitar.cost:{cost_width},.2f}{vintage_string}")


main()
