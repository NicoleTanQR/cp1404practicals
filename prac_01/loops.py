"""
for odd number between 1 and 20
    print odd number
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
"""
for number from 0-100 in increment of 10
    print number
"""

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
"""
for number from 20-1 in decrement of 1
    print number 
"""

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
"""
get number_of_stars
for star in number_of_stars
    print "*"
"""

number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars):
    print("*", end='')
print()

# d.
"""
get number_of_stars
for star in number_of_stars
    star_line = "*" * (star+1)
    print star_line
"""

number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars):
    star_line = "*" * (star+1)
    print(star_line)
print()

"""
get number_of_stars
for star in number_of_stars
    print "*" multiplied by star's position 
"""

number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars):
    print("*" * (star+1))
print()
