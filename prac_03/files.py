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
total = 0
with open(FILENAME) as in_file:
    for i in range(0, 2):
        number = in_file.readline()
        total = total + int(number)
print(total)

# 4.
FILENAME = "numbers.txt"
total = 0
with open(FILENAME) as in_file:
    for line in in_file:
        total += int(line)
print(total)
