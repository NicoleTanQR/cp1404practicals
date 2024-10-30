"""
Game, Set, Match
Estimate: 70 minutes
Actual:  148 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Display champions and their win count and countries from file."""
    records = load_records(FILENAME)
    champion_to_number_of_wins, countries = process_records(records)
    display_champion_details(champion_to_number_of_wins, countries)


def load_records(filename):
    """Load records from file."""
    with open(filename, encoding="utf-8-sig") as in_file:
        records = in_file.readlines()[1:]
    return records


def process_records(records):
    """Return dictionary of champions and set of countries from records."""
    champion_to_number_of_wins = {}
    countries = set()
    for record in records:
        record = record.split(",")
        champion, country = record[INDEX_CHAMPION], record[INDEX_COUNTRY]
        champion_to_number_of_wins[champion] = champion_to_number_of_wins.get(
            champion, 0) + 1
        countries.add(country)
    return champion_to_number_of_wins, countries


def display_champion_details(champion_to_number_of_wins, countries):
    """Display champion details stored."""
    print("Wimbledon Champions: ")
    for champion, number_of_wins in champion_to_number_of_wins.items():
        print(champion, number_of_wins)
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
