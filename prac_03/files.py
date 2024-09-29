"""Practical 3 - Files"""

# 1.
FILENAME = "name.txt"
name = input("Name: ")
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

# 2.
FILENAME = "name.txt"
in_file = open(FILENAME)
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
FILENAME = "numbers.txt"
with open(FILENAME) as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

# 4.
FILENAME = "numbers.txt"
total = 0
with open(FILENAME) as in_file:
    for line in in_file:
        total += int(line)
print(total)
