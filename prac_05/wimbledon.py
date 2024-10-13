"""
Game, Set, Match
Estimate: 70 minutes
Actual:    minutes
"""

FILENAME = "wimbledon.csv"
champion_to_number_of_wins = {}
countries = set()
print("Wimbledon Champions: ")
with open(FILENAME, encoding="utf-8-sig") as in_file:
    records = in_file.readlines()[1:]
for record in records:
    record = record.split(",")
    champion, country = record[2], record[1]
    champion_to_number_of_wins[champion] = champion_to_number_of_wins.get(
        champion, 0) + 1
    countries.add(country)
for champion, number_of_wins in champion_to_number_of_wins.items():
    print(f"{champion} {number_of_wins}")
print()
print("These 12 countries have won Wimbledon: ")
print(", ".join(sorted(countries)))
